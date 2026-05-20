#!/usr/bin/env python3
"""Export issues from a named future sprint to per-issue markdown files in jira-sync/Backlog/.
Usage: python3 jira-sprint-future.py "Sprint 3"
"""

import os
import sys
import json
import re
import datetime
import urllib.request
from base64 import b64encode

BOARD_ID = os.environ.get("JIRA_BOARD_ID", "12541")


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
        sys.exit("Missing JIRA_EMAIL or JIRA_API_TOKEN.")
    return "Basic " + b64encode(f"{email}:{token}".encode()).decode()


def get(url, auth):
    req = urllib.request.Request(url, headers={"Authorization": auth, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 401:
            sys.exit("Authentication failed.")
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


def sanitise(name):
    name = name.replace(" ", "-")
    return re.sub(r"[^\w\-]", "", name)


def find_sprint(base, auth, name_fragment):
    for state in ("future", "active"):
        data = get(f"{base}/rest/agile/1.0/board/{BOARD_ID}/sprint?state={state}&maxResults=50", auth)
        for s in (data or {}).get("values", []):
            if name_fragment.lower() in s["name"].lower():
                return s
    return None


def get_sprint_issues(base, auth, sprint_id):
    all_issues = []
    start = 0
    while True:
        url = (
            f"{base}/rest/agile/1.0/sprint/{sprint_id}/issue"
            f"?maxResults=100&startAt={start}"
            "&fields=summary,status,assignee,customfield_10016,subtasks,description,issuetype"
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


def get_issue_detail(base, auth, key):
    data = get(f"{base}/rest/api/3/issue/{key}", auth)
    if data is None:
        print(f"  ⚠ {key} not found — skipped.")
    return data


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
    points = fields.get("customfield_10016")
    story_points = str(int(points)) if isinstance(points, float) and points == int(points) else str(points) if points is not None else "N/A"
    itype = (fields.get("issuetype") or {}).get("name", "N/A")

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

    return f"""# {key}: {summary}

**Type:** {itype}
**Status:** {status}
**Assignee:** {assignee}
**Story Points:** {story_points}

---

## Description

{description}

---

## Subtasks

{subtasks_section}

---

## Latest Comments

{comments_section}
"""


def main():
    load_env()
    site = os.environ.get("JIRA_SITE")
    if not site:
        sys.exit("Missing JIRA_SITE.")

    sprint_name = sys.argv[1] if len(sys.argv) > 1 else "Sprint 3"
    base = f"https://{site}"
    auth = make_auth_header()

    print(f"Looking for sprint matching '{sprint_name}'...")
    sprint = find_sprint(base, auth, sprint_name)
    if not sprint:
        sys.exit(f"No sprint found matching '{sprint_name}'.")

    sprint_id = sprint["id"]
    print(f"Found: {sprint['name']} (id={sprint_id})")

    folder_name = sanitise(sprint["name"])
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jira-sync", folder_name)
    os.makedirs(out_dir, exist_ok=True)

    print("Fetching sprint issues...")
    issues = get_sprint_issues(base, auth, sprint_id)
    print(f"Found {len(issues)} issues. Fetching full details...\n")

    written = 0
    change_rows = []
    for issue in issues:
        key = issue["key"]
        detail = get_issue_detail(base, auth, key)
        if detail is None:
            continue
        comments = get_comments(base, auth, key)
        path = os.path.join(out_dir, f"{key}.md")

        old_status, old_assignee, old_comment = parse_existing(path)
        fields = detail.get("fields", {})
        md = build_markdown(key, fields, comments)

        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"  ✓ {key}")
        written += 1

        new_status = (fields.get("status") or {}).get("name", "N/A")
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
            change_rows.append(f"| {key} | New | — |")
        else:
            if old_status != new_status:
                change_rows.append(f"| {key} | Status | {old_status} → {new_status} |")
            if old_assignee != new_assignee:
                change_rows.append(f"| {key} | Assignee | {old_assignee} → {new_assignee} |")
            if new_comment and old_comment != new_comment:
                change_rows.append(f"| {key} | New comment | {new_comment} |")

    today = datetime.date.today().isoformat()
    if change_rows:
        table = "| Story | Change | Detail |\n|---|---|---|\n" + "\n".join(change_rows)
    else:
        table = "_No changes since last sync._"
    changes_path = os.path.join(out_dir, ".changes.md")
    with open(changes_path, "w", encoding="utf-8") as f:
        f.write(f"# {sprint['name']} Story Changes — {today}\n\n{table}\n")

    print(f"\nDone. {written} files written to jira-sync/{folder_name}/")
    if change_rows:
        print(f"Changes detected: {len(change_rows)} (see .changes.md)")


if __name__ == "__main__":
    main()
