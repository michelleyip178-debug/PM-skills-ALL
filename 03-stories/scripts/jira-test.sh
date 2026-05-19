#!/usr/bin/env bash
# Quick connectivity test for Jira API.
# Fetches the current user and a sample of issues assigned to you.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
set -a; source "$ROOT/.env"; set +a

AUTH="$JIRA_EMAIL:$JIRA_API_TOKEN"
BASE="https://$JIRA_SITE"

echo "→ Whoami"
curl -sS -u "$AUTH" -H "Accept: application/json" \
  "$BASE/rest/api/3/myself" | python3 -c "import json,sys;d=json.load(sys.stdin);print(f\"  {d.get('displayName')} <{d.get('emailAddress')}> — accountId {d.get('accountId')}\")"

echo
echo "→ Issues assigned to me (max 5)"
curl -sS -u "$AUTH" -G \
  --data-urlencode "jql=assignee = currentUser() ORDER BY updated DESC" \
  --data-urlencode "fields=summary,status,project" \
  --data-urlencode "maxResults=5" \
  -H "Accept: application/json" \
  "$BASE/rest/api/3/search" | python3 -c "
import json,sys
d=json.load(sys.stdin)
issues=d.get('issues',[])
if not issues:
    print('  (none)')
for i in issues:
    f=i['fields']
    print(f\"  {i['key']:12} [{f['status']['name']:14}] {f['summary']}\")
"
