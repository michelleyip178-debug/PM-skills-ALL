#!/usr/bin/env python3
"""Export a Jira epic and all its child tasks to per-issue markdown files.

Usage:
    python3 jira-sync-epic.py OTEP-1047

Output goes to jira-sync/<EPIC_KEY>-<sanitised-summary>/, with an _epic-summary.md
rollup (all children + status table) plus one markdown file per child task.
Re-runnable: flags status/assignee/comment changes in .changes.md on each run.
"""

import os
import sys
import json
import re
import datetime
import urllib.request
from base64 import b64encode


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


def post(url, auth, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        url, data=data, method="POST",
        headers={"Authorization": auth, "Accept": "application/json", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.reason} — {url}\n{e.read().decode()}")


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


def get_epic_detail(base, auth, key):
    data = get(f"{base}/rest/api/3/issue/{key}?fields=summary,status,assignee,description,issuetype,labels", auth)
    if data is None:
        sys.exit(f"Epic {key} not found.")
    return data


def get_epic_children(base, auth, key):
    payload = {
        "jql": f'"Epic Link" = {key} OR parentEpic = {key} ORDER BY key ASC',
        "maxResults": 100,
        "fields": ["summary", "status", "assignee", "issuetype", "labels", "subtasks", "description"],
    }
    data = post(f"{base}/rest/api/3/search/jql", auth, payload)
    issues = data.get("issues", []) if data else []
    return [i for i in issues if i["key"] != key]


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
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 jira-sync-epic.py <EPIC_KEY>")
    epic_key = sys.argv[1].upper()

    load_env()
    site = os.environ.get("JIRA_SITE")
    if not site:
        sys.exit("Missing environment variable: JIRA_SITE")

    base = f"https://{site}"
    auth = make_auth_header()

    print(f"Fetching epic {epic_key}...")
    epic = get_epic_detail(base, auth, epic_key)
    epic_summary = epic["fields"]["summary"]
    print(f"Epic: {epic_summary}")

    folder_name = f"{epic_key}-{sanitise(epic_summary)}"
    out_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "jira-sync", folder_name
    )
    os.makedirs(out_dir, exist_ok=True)

    print("Fetching child tasks...")
    children = get_epic_children(base, auth, epic_key)
    print(f"Found {len(children)} child tasks.\n")

    written = 0
    change_rows = []
    status_counts = {}
    summary_rows = []

    for issue in children:
        key = issue["key"]
        fields = issue.get("fields", {})
        status_name = (fields.get("status") or {}).get("name", "N/A")
        assignee_obj = fields.get("assignee")
        assignee = assignee_obj.get("displayName", "N/A") if assignee_obj else "N/A"
        summary_txt = fields.get("summary", "N/A")
        status_counts[status_name] = status_counts.get(status_name, 0) + 1
        summary_rows.append(f"| {key} | {summary_txt} | {status_name} | {assignee} |")

        path = os.path.join(out_dir, f"{key}.md")
        old_status, old_assignee, old_comment = parse_existing(path)

        comments = get_comments(base, auth, key)
        md = build_markdown(key, fields, comments)

        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        written += 1

        new_comment = None
        if comments:
            c = comments[0]
            author = (c.get("author") or {}).get("displayName", "Unknown")
            date = (c.get("created") or "")[:10]
            if c.get("body") and extract_text(c.get("body")).strip():
                new_comment = f"{author} ({date})"

        if old_status is None:
            change_rows.append(f"| {key} | New task | — → {status_name} |")
        else:
            if old_status != status_name:
                change_rows.append(f"| {key} | Status | {old_status} → {status_name} |")
            if old_assignee != assignee:
                change_rows.append(f"| {key} | Assignee | {old_assignee} → {assignee} |")
            if new_comment and old_comment != new_comment:
                change_rows.append(f"| {key} | New comment | {new_comment} |")

    today = datetime.date.today().isoformat()

    status_summary = "\n".join(f"- **{s}:** {c}" for s, c in sorted(status_counts.items()))
    table_rows = "\n".join(summary_rows)
    epic_summary_md = f"""# Epic {epic_key}: {epic_summary}

**Synced:** {today}
**Child tasks:** {len(children)}

## Status Breakdown

{status_summary}

## All Child Tasks

| Key | Summary | Status | Assignee |
|---|---|---|---|
{table_rows}

---
*Individual task detail in this folder's per-key .md files.*
"""
    with open(os.path.join(out_dir, "_epic-summary.md"), "w", encoding="utf-8") as f:
        f.write(epic_summary_md)

    if change_rows:
        table = "| Task | Change | Detail |\n|---|---|---|\n" + "\n".join(change_rows)
    else:
        table = "_No changes since last sync._"
    with open(os.path.join(out_dir, ".changes.md"), "w", encoding="utf-8") as f:
        f.write(f"# {epic_key} Sync — {today}\n\n{table}\n")

    print(f"Done. {written} child tasks + _epic-summary.md written to jira-sync/{folder_name}/")
    print("\nStatus breakdown:")
    for s, c in sorted(status_counts.items()):
        print(f"  {s}: {c}")
    if change_rows:
        print(f"\nChanges detected: {len(change_rows)} (see .changes.md)")


if __name__ == "__main__":
    main()
