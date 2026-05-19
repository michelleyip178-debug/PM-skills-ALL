# Story Pipeline Workflow

Get user stories from draft to sprint-ready with quality gates at each stage.

## When to Trigger

Say "story pipeline", "write a story", "prep for grooming", or "check story readiness" when working on user stories for upcoming sprints.

## What This Produces

- Draft stories with AC, edge cases, and priority in the appropriate group file
- Updated story index (`user-stories.md`)
- Grooming briefs (via `/groom-prep`)
- Stories that meet DoR by sprint planning day

## Key Constraints

- Stories must be 2 sprints ahead of build
- Every story needs: outcome-oriented format, testable AC, at least one edge case
- No BA language ("the system shall") — use "As an officer..."
- Check AC against MVP guardrails before grooming
- DoR requires: designs linked, API contract documented, feature flag identified, subtasks created

## Files in This Workflow

1. `workflow-spec.md` — Full pipeline overview with lead times
2. `1-draft.md` — Write the story + self-check
3. `2-internal-groom.md` — Squad review (Tuesday week 1)
4. `3-refine.md` — Design + API + PM tracks in parallel
5. `4-backlog-groom.md` — Full team review (Thursday week 2)

## Related Commands

- `/groom-prep` — Readiness scores before grooming sessions
- `/groom` — Deep brief via NotebookLM before grooming
- `pm-reviewer` agent — Validates story format, AC quality, MVP compliance

## Typical Timeline

```
Week 1 Mon:  Draft stories for sprint N+2
Week 1 Tue:  Internal groom (squad)
Week 1-2:    Refine (design, API, AC updates)
Week 2 Thu:  Backlog groom (full team)
Week 2 Thu:  Sprint planning — DoR-ready stories committed
```
