#!/usr/bin/env bash
# Fetch a Confluence page's content as plain text.
# Usage: confluence-page.sh <page-id-or-url>
# Uses the same Atlassian credentials as jira-sprint.sh (JIRA_EMAIL / JIRA_API_TOKEN / JIRA_SITE).

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
set -a; source "$ROOT/.env"; set +a

AUTH="$JIRA_EMAIL:$JIRA_API_TOKEN"
BASE="https://$JIRA_SITE/wiki"

INPUT="${1:?Usage: confluence-page.sh <page-id-or-url>}"

# Extract numeric page ID from a full URL if one was passed, else assume it's already an ID.
PAGE_ID=$(echo "$INPUT" | grep -oE '/pages/[0-9]+' | grep -oE '[0-9]+' || true)
if [ -z "$PAGE_ID" ]; then
  PAGE_ID="$INPUT"
fi

curl -sS -u "$AUTH" -H "Accept: application/json" \
  "$BASE/rest/api/content/$PAGE_ID?expand=body.storage,version,space" \
| python3 -c "
import json, sys, re

d = json.load(sys.stdin)

if 'statusCode' in d and d['statusCode'] >= 400:
    print(f\"Error {d['statusCode']}: {d.get('message', 'unknown error')}\", file=sys.stderr)
    sys.exit(1)

title = d.get('title', '(untitled)')
space = (d.get('space') or {}).get('name', '?')
version = (d.get('version') or {}).get('number', '?')
print(f'# {title}')
print(f'(space: {space}, version: {version})')
print()

html = d.get('body', {}).get('storage', {}).get('value', '')

# Strip Confluence storage-format XML/HTML down to readable text.
# Tables get kept as pipe-delimited rows since that's the most common structure for estimate pages.
text = html

# Table rows: convert <tr>...</tr> to a line, <td>/<th> cells to pipe-separated.
def strip_tags_keep_text(s):
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    return s.strip()

rows = re.findall(r'<tr[^>]*>(.*?)</tr>', text, re.DOTALL)
if rows:
    for row in rows:
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.DOTALL)
        cleaned = [strip_tags_keep_text(c) for c in cells]
        print(' | '.join(cleaned))
else:
    # No tables found — fall back to stripping all tags for prose content.
    print(strip_tags_keep_text(text))
"
