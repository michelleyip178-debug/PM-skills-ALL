#!/usr/bin/env python3
"""Export all issues on the CC-UAT kanban board to per-issue markdown files in jira-sync/CC-UAT/.

Unlike jira-sync.py (sprint-based, scrum board), this targets a kanban board with no sprints.
Issues are grouped into subfolders by their board column (UAT stage) instead of by sprint.
"""

import os
import sys
import json
import re
import datetime
import urllib.request
from base64 import b64encode

BOARD_ID = os.environ.get("JIRA_UAT_BOARD_ID", "20498")

# Maps raw Jira status name -> board column folder name (per board 20498's configuration)
STATUS_TO_COLUMN = {
    "Backlog": "Backlog",
    "Selected for Development": "To-Do",
    "To-Do(Product Team)": "To-Do",
    "QA": "To-Do",
    "Ready for UAT": "Ready-for-UAT",
    "UAT": "In-Execution",
    "In Execution": "In-Execution",
    "Failed / Blocked": "Failed-Blocked",
    "Passed": "Passed",
    "Done": "Passed",
}


def load_env():
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ.setdefault(key, val)


def make_auth_header():
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_API_TOKEN")
    if not email or not token:
        sys.exit("Missing environment variables. Please set JIRA_EMAIL and JIRA_API_TOKEN.")
    return "Basic " + b64encode(f"{email}:{token}".encode()).decode()


def get(url, auth):
    req = urllib.request.Request(url, headers={"Authorization": auth, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 401:
            sys.exit("Authentication failed. Check JIRA_EMAIL and JIRA_API_TOKEN.")
        if e.code == 404:
            return None
        sys.exit(f"HTTP {e.code}: {e.reason} — {url}")


def extract_text(node):
    if node is None:
        return ""
    if isinstance(node, str):
        return node
    if "text" in node:
        return node["text"]
    if "content" in node:
        return " ".join(extract_text(child) for child in node["content"] if child)
    return ""


def get_board_issues(base, auth):
    all_issues = []
    start = 0
    while True:
        url = (
            f"{base}/rest/agile/1.0/board/{BOARD_ID}/issue"
            f"?maxResults=100&startAt={start}"
            "&fields=summary,status,assignee,customfield_10016,subtasks,description,issuetype,labels"
        )
        data = get(url, auth)
        if not data:
            break
        issues = data.get("issues", [])
        all_issues.extend(issues)
        if start + len(issues) >= data.get("total", 0):
            break
        start += len(issues)
    return all_issues


def get_comments(base, auth, key, max_results=3):
    url = f"{base}/rest/api/3/issue/{key}/comment?orderBy=-created&maxResults={max_results}"
    data = get(url, auth)
    return (data.get("comments") or []) if data else []


def parse_existing(path):
    if not os.path.exists(path):
        return None, None, None
    with open(path, encoding="utf-8") as f:
        content = f.read()
    status = re.search(r"\*\*Status:\*\* (.+)", content)
    assignee = re.search(r"\*\*Assignee:\*\* (.+)", content)
    comment = re.search(r"\*\*(.+?)\*\* \((\d{4}-\d{2}-\d{2})\)", content)
    return (
        status.group(1).strip() if status else None,
        assignee.group(1).strip() if assignee else None,
        f"{comment.group(1)} ({comment.group(2)})" if comment else None,
    )


def build_markdown(key, fields, comments=None):
    summary = fields.get("summary", "N/A")
    status = (fields.get("status") or {}).get("name", "N/A")
    assignee_obj = fields.get("assignee")
    assignee = assignee_obj.get("displayName", "N/A") if assignee_obj else "N/A"
    itype = (fields.get("issuetype") or {}).get("name", "N/A")
    labels = fields.get("labels") or []
    labels_line = ", ".join(labels) if labels else "None"

    desc_node = fields.get("description")
    description = extract_text(desc_node).strip() if desc_node else "No description provided."
    if not description:
        description = "No description provided."

    subtasks = fields.get("subtasks") or []
    if subtasks:
        rows = "\n".join(
            f"| {st['key']} | {st['fields']['summary']} | {st['fields']['status']['name']} |"
            for st in subtasks
        )
        subtasks_section = f"| Key | Summary | Status |\n|-----|---------|--------|\n{rows}"
    else:
        subtasks_section = "_No subtasks._"

    if comments:
        comment_lines = []
        for c in comments:
            author = (c.get("author") or {}).get("displayName", "Unknown")
            created = (c.get("created") or "")[:10]
            body = extract_text(c.get("body")).strip()
            if body:
                comment_lines.append(f"**{author}** ({created})\n{body}")
        comments_section = "\n\n---\n\n".join(comment_lines) if comment_lines else "_No comments._"
    else:
        comments_section = "_No comments._"

    today = datetime.date.today().isoformat()

    return f"""# {key}: {summary}

**Status:** {status}
**Assignee:** {assignee}
**Type:** {itype}
**Labels:** {labels_line}

---

## Description

{description}

---

## Subtasks

{subtasks_section}

---

## Latest Comments

{comments_section}

---
*Synced from Jira: {today}*
"""


def main():
    load_env()
    site = os.environ.get("JIRA_SITE")
    if not site:
        sys.exit("Missing environment variable: JIRA_SITE")

    base = f"https://{site}"
    auth = make_auth_header()

    print(f"Fetching CC-UAT board issues (board {BOARD_ID})...")
    issues = get_board_issues(base, auth)
    print(f"Found {len(issues)} issues.\n")

    root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jira-sync", "CC-UAT")
    os.makedirs(root_dir, exist_ok=True)

    written = 0
    change_rows = []
    status_counts = {}

    for issue in issues:
        key = issue["key"]
        fields = issue.get("fields", {})
        status_name = (fields.get("status") or {}).get("name", "N/A")
        column = STATUS_TO_COLUMN.get(status_name, re.sub(r"[^\w\-]", "-", status_name))
        status_counts[column] = status_counts.get(column, 0) + 1

        out_dir = os.path.join(root_dir, column)
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, f"{key}.md")

        old_status, old_assignee, old_comment = parse_existing(path)

        # If this issue previously synced under a different column, remove the stale file
        if old_status is not None and old_status != status_name:
            for other_col in set(STATUS_TO_COLUMN.values()):
                if other_col == column:
                    continue
                stale_path = os.path.join(root_dir, other_col, f"{key}.md")
                if os.path.exists(stale_path):
                    os.remove(stale_path)

        comments = get_comments(base, auth, key)
        md = build_markdown(key, fields, comments)

        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        written += 1

        new_status = status_name
        assignee_obj = fields.get("assignee")
        new_assignee = assignee_obj.get("displayName", "N/A") if assignee_obj else "N/A"
        new_comment = None
        if comments:
            c = comments[0]
            author = (c.get("author") or {}).get("displayName", "Unknown")
            date = (c.get("created") or "")[:10]
            if c.get("body") and extract_text(c.get("body")).strip():
                new_comment = f"{author} ({date})"

        if old_status is None:
            change_rows.append(f"| {key} | New ticket | — → {new_status} |")
        else:
            if old_status != new_status:
                change_rows.append(f"| {key} | Status | {old_status} → {new_status} |")
            if old_assignee != new_assignee:
                change_rows.append(f"| {key} | Assignee | {old_assignee} → {new_assignee} |")
            if new_comment and old_comment != new_comment:
                change_rows.append(f"| {key} | New comment | {new_comment} |")

    today = datetime.date.today().isoformat()
    if change_rows:
        table = "| Ticket | Change | Detail |\n|---|---|---|\n" + "\n".join(change_rows)
    else:
        table = "_No ticket changes since last sync._"

    summary_lines = "\n".join(f"- **{col}:** {count}" for col, count in sorted(status_counts.items()))
    changes_path = os.path.join(root_dir, ".changes.md")
    with open(changes_path, "w", encoding="utf-8") as f:
        f.write(f"# CC-UAT Board Sync — {today}\n\n## Column Counts\n\n{summary_lines}\n\n## Changes\n\n{table}\n")

    print(f"Done. {written} files written to jira-sync/CC-UAT/")
    print("\nColumn counts:")
    for col, count in sorted(status_counts.items()):
        print(f"  {col}: {count}")
    if change_rows:
        print(f"\nChanges detected: {len(change_rows)} (see .changes.md)")


if __name__ == "__main__":
    main()
