#!/usr/bin/env python3
"""Export all active sprint issues to per-issue markdown files in jira-sync/."""

import os
import sys
import json
import re
import urllib.request
import urllib.parse
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
        sys.exit("Missing environment variables. Please set JIRA_EMAIL and JIRA_API_TOKEN.")
    return "Basic " + b64encode(f"{email}:{token}".encode()).decode()


def get(url, auth):
    req = urllib.request.Request(url, headers={"Authorization": auth, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 401:
            sys.exit("Authentication failed. Check your JIRA_EMAIL and JIRA_API_TOKEN.")
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


def get_active_sprint(base, auth):
    data = get(f"{base}/rest/agile/1.0/board/{BOARD_ID}/sprint?state=active", auth)
    values = data.get("values", []) if data else []
    if not values:
        sys.exit("No active sprint found. Please provide a sprint ID to target.")
    return values[0]


def get_sprint_issues(base, auth, sprint_id):
    url = (
        f"{base}/rest/agile/1.0/sprint/{sprint_id}/issue"
        "?maxResults=100&fields=summary,status,assignee,customfield_10016,subtasks,description"
    )
    data = get(url, auth)
    return data.get("issues", []) if data else []


def get_issue_detail(base, auth, key):
    data = get(f"{base}/rest/api/3/issue/{key}", auth)
    if data is None:
        print(f"Issue {key} not found — skipped.")
    return data


def build_markdown(key, fields):
    summary = fields.get("summary", "N/A")
    status = (fields.get("status") or {}).get("name", "N/A")
    assignee_obj = fields.get("assignee")
    assignee = assignee_obj.get("displayName", "N/A") if assignee_obj else "N/A"
    points = fields.get("customfield_10016")
    story_points = str(int(points)) if isinstance(points, float) and points == int(points) else str(points) if points is not None else "N/A"

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

    return f"""# {key}: {summary}

**Status:** {status}
**Assignee:** {assignee}
**Story Points:** {story_points}

---

## Description

{description}

---

## Subtasks

{subtasks_section}
"""


def main():
    load_env()
    site = os.environ.get("JIRA_SITE")
    if not site:
        sys.exit("Missing environment variable: JIRA_SITE")

    base = f"https://{site}"
    auth = make_auth_header()

    print("Fetching active sprint...")
    sprint = get_active_sprint(base, auth)
    sprint_id = sprint["id"]
    sprint_name = sprint["name"]
    print(f"Active sprint: {sprint_name} (id={sprint_id})")

    folder_name = f"Sprint-{sprint_id}-{sanitise(sprint_name)}"
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jira-sync", folder_name)
    os.makedirs(out_dir, exist_ok=True)

    print("Fetching sprint issues...")
    issues = get_sprint_issues(base, auth, sprint_id)
    print(f"Found {len(issues)} issues. Fetching full details...\n")

    written = 0
    for issue in issues:
        key = issue["key"]
        detail = get_issue_detail(base, auth, key)
        if detail is None:
            continue
        md = build_markdown(key, detail.get("fields", {}))
        path = os.path.join(out_dir, f"{key}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"  ✓ {key}")
        written += 1

    print(f"\nDone. {written} files written to jira-sync/{folder_name}/")


if __name__ == "__main__":
    main()
