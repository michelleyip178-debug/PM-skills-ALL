# Step 1: Close the Sprint

## When
Friday of sprint week 2, after sprint finalisation.

## Checklist

### Archive outputs
```
outputs/*.md  -->  archive/outputs/
```
Move all generated briefs, dailies, and reviews from this sprint to the archive. Keep filenames as-is (they're already dated).

### Archive meeting notes
```
Any meeting notes still in inbox.md or loose  -->  archive/meetings/{subfolder}/
```
Subfolders: `int-sprint/`, `sprint-planning/`, `standups/`, `1on1s/`, `one-offs/`

### Snapshot current sprint context
Copy (don't move) `context/current-sprint.md` to `archive/` with a dated filename:
```
context/current-sprint.md  -->  archive/sprint-N-context-YYYY-MM-DD.md
```
This preserves a record of what was committed vs what was delivered.

### Log undocumented decisions
Scan your memory from the past 2 weeks:
- Any scope calls made in Slack/standup that aren't in `context/decisions-log.md`?
- Any "we agreed to..." from grooming that wasn't logged?
- Any R1 deferrals decided informally?

Add each to `context/decisions-log.md` with: date, decision, rationale, owner.

## Done when
- `outputs/` folder is empty
- Meeting notes are archived
- Sprint snapshot exists in `archive/`
- No undocumented decisions from the sprint
