#!/usr/bin/env bash
# List all issues in the active sprint of a given board.
# Default: OTEP-Pathfinder (board 12541). Override with JIRA_BOARD_ID env var.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
set -a; source "$ROOT/.env"; set +a

BOARD_ID="${JIRA_BOARD_ID:-12541}"
AUTH="$JIRA_EMAIL:$JIRA_API_TOKEN"
BASE="https://$JIRA_SITE"

SPRINT_JSON=$(curl -sS -u "$AUTH" -H "Accept: application/json" \
  "$BASE/rest/agile/1.0/board/$BOARD_ID/sprint?state=active")

# The board/{id}/sprint endpoint can return sprints whose originBoardId is a
# DIFFERENT board (observed on this shared Jira instance — board 12541's
# "active" query returned an OTEP-Intel sprint, originBoardId 14855). Filter
# to sprints actually owned by the requested board before trusting the result.
SPRINT_ID=$(echo "$SPRINT_JSON" | BOARD_ID="$BOARD_ID" python3 -c "
import json, os, sys
board_id = int(os.environ['BOARD_ID'])
v = json.load(sys.stdin).get('values', [])
owned = [s for s in v if s.get('originBoardId') == board_id]
print(owned[0]['id'] if owned else '')
")

if [ -z "$SPRINT_ID" ]; then
  echo "No active sprint on board $BOARD_ID (owned by this board — cross-board results, if any, were filtered out)."
  exit 0
fi

echo "$SPRINT_JSON" | BOARD_ID="$BOARD_ID" python3 -c "
import json, os, sys
board_id = int(os.environ['BOARD_ID'])
v = json.load(sys.stdin)['values']
s = [x for x in v if x.get('originBoardId') == board_id][0]
print(f\"Sprint: {s['name']}  ({s.get('startDate','?')[:10]} → {s.get('endDate','?')[:10]})\")
print(f\"Goal:   {s.get('goal') or '(none set)'}\")
print()
"

curl -sS -u "$AUTH" -H "Accept: application/json" \
  "$BASE/rest/agile/1.0/sprint/$SPRINT_ID/issue?fields=summary,status,assignee,issuetype,priority&maxResults=100" \
| python3 -c "
import json,sys
from collections import defaultdict
d=json.load(sys.stdin)
by_status=defaultdict(list)
for i in d.get('issues',[]):
    f=i['fields']
    a=(f.get('assignee') or {}).get('displayName') or '—'
    t=f['issuetype']['name']
    by_status[f['status']['name']].append((i['key'], t, a, f['summary']))

# Order statuses logically
order=['To Do','Open','In Progress','In Review','Code Review','QA','Done','Closed']
seen=set()
ordered=[s for s in order if s in by_status]+[s for s in by_status if s not in order]

for s in ordered:
    print(f'─── {s} ({len(by_status[s])}) ─────────────────')
    for k,t,a,sm in by_status[s]:
        print(f'  {k:14} [{t:7}] {a:22}  {sm}')
    print()
"
