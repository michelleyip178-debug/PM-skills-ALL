# Post-Meeting Capture Workflow

Route meeting outputs to the right files in under 2 minutes.

## When to Trigger

Say "meeting capture", "triage meeting notes", or "process meeting notes" after any meeting. Or paste raw meeting notes and say "route these."

## What This Produces

- Decisions logged in `context/decisions-log.md`
- Action items routed to `tasks/active.md` (mine) or `context/open-items.md` (theirs)
- Open questions added to `context/open-items.md` with owner and deadline
- Optionally: raw notes archived to `archive/meetings/`

## Key Constraints

- Do this immediately after the meeting, not at end of day
- Only route decisions (D), action items (A), and open questions (Q) — let info-only items go
- Every action item needs an owner. Every open question needs a deadline.
- Scope decisions also need to be checked against MVP guardrails

## Files in This Workflow

1. `workflow-spec.md` — Full process with triage buckets and routing table

## Input

Raw meeting notes — pasted, typed, or dumped from any source. Format doesn't matter.

## Typical Runtime

Under 2 minutes per meeting.
