#!/usr/bin/env python3
"""Push updated ACs from local markdown files to Jira as comments.

Usage:
    python3 push-jira-acs.py OTEP-336 OTEP-570 OTEP-390

Each issue gets a comment containing its full Acceptance Criteria section,
labelled with the date and source file so there's a clear audit trail.
"""

import os
import sys
import json
import re
import urllib.request
import urllib.error
from base64 import b64encode
from datetime import date

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(SCRIPT_DIR, "..")

SEARCH_DIRS = [
    os.path.join(BASE_DIR, "jira-sync"),
]


def load_env():
    env_path = os.path.join(BASE_DIR, ".env")
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
        sys.exit("Missing JIRA_EMAIL or JIRA_API_TOKEN in .env")
    return "Basic " + b64encode(f"{email}:{token}".encode()).decode()


def find_md_file(issue_key):
    """Walk jira-sync/ subdirectories to find the markdown file for this issue."""
    for root, dirs, files in os.walk(os.path.join(BASE_DIR, "jira-sync")):
        for fname in files:
            if fname == f"{issue_key}.md":
                return os.path.join(root, fname)
    return None


def extract_section(content, heading):
    """Extract content from a ## heading to the next ## heading."""
    pattern = rf"(## {re.escape(heading)}.*?)(?=\n## |\Z)"
    m = re.search(pattern, content, re.DOTALL)
    return m.group(1).strip() if m else None


def markdown_to_adf(text):
    """Convert plain markdown text to a minimal ADF doc (paragraphs + code block)."""
    # Post as a code block so formatting is preserved exactly
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": f"ACs updated {date.today().isoformat()} (from local PM OS workspace):",
                        "marks": [{"type": "strong"}],
                    }
                ],
            },
            {
                "type": "codeBlock",
                "attrs": {"language": "markdown"},
                "content": [{"type": "text", "text": text}],
            },
        ],
    }


def post_comment(base, auth, issue_key, adf_body):
    url = f"{base}/rest/api/3/issue/{issue_key}/comment"
    payload = json.dumps({"body": adf_body}).encode()
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": auth,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            return data.get("id"), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}: {e.read().decode()[:300]}"


def main():
    load_env()
    site = os.environ.get("JIRA_SITE")
    if not site:
        sys.exit("Missing JIRA_SITE in .env")

    base = f"https://{site}"
    auth = make_auth_header()

    keys = sys.argv[1:] if len(sys.argv) > 1 else []
    if not keys:
        sys.exit("Usage: push-jira-acs.py OTEP-336 OTEP-570 OTEP-390")

    for key in keys:
        print(f"\n--- {key} ---")
        path = find_md_file(key)
        if not path:
            print(f"  ERROR: No markdown file found for {key}")
            continue
        print(f"  Source: {os.path.relpath(path, BASE_DIR)}")

        with open(path) as f:
            content = f.read()

        section = extract_section(content, "Acceptance Criteria")
        if not section:
            print(f"  ERROR: No '## Acceptance Criteria' section found")
            continue

        print(f"  Extracted {len(section)} chars of ACs")
        adf = markdown_to_adf(section)
        comment_id, err = post_comment(base, auth, key, adf)

        if err:
            print(f"  FAILED: {err}")
        else:
            print(f"  Posted comment {comment_id} to {key}")

    print("\nDone.")


if __name__ == "__main__":
    main()
