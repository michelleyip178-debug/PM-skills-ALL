# Sprint Boundary Transition Workflow

Cleanly close one sprint and open the next. Prevents stale context files from corrupting command output.

## When to Trigger

Say "sprint boundary", "close the sprint", "open the sprint", or "sprint transition" at the end/start of a sprint.

## What This Produces

- Archived outputs and meeting notes from the completed sprint
- Clean `tasks/active.md` with carry-forward items prioritised
- Updated `context/current-sprint.md` with new sprint data
- Updated `context/risks.md` and `context/open-items.md`
- Updated `projects/otep-mvp/sprint-checklists.md` (new sprint's stories) and `projects/otep-mvp/deferred-acs.md` (cuts + pulls)
- Updated `README.md` sprint header references (4 spots — see 3-open-sprint.md)

## Key Constraints

- `context/current-sprint.md` must have zero placeholders when done
- Sprint goal must be outcome-oriented ("Officers can ___"), not output-oriented ("Deliver OTEP-85")
- Carry-forward items need a reason, not just a checkmark
- Run `/daily` as a verification step — if the output doesn't match reality, something's wrong

## Files in This Workflow

1. `workflow-spec.md` — Full process overview
2. `1-close-sprint.md` — Archive, snapshot, log decisions
3. `2-update-tasks.md` — Done, carry-forward, pull from backlog
4. `3-open-sprint.md` — Update context files for new sprint

## Typical Runtime

~20 minutes total across Friday (close) and Monday (open).
