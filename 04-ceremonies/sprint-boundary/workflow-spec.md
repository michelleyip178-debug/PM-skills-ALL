# Sprint Boundary Transition — Workflow Spec

## Purpose

Cleanly close one sprint and open the next. Prevents the #1 failure mode in this OS: stale context files making every command output wrong.

## When

Friday of sprint week 2 (sprint end) + Monday of new sprint (sprint start). Total: ~20 minutes across both days.

## Process Overview

```
FRIDAY (Sprint End) — 10 min
  Step 1: Close the sprint (archive + snapshot)
      |
  Step 2: Update tasks (done + carry-forward)

MONDAY (Sprint Start) — 10 min
  Step 3: Open the new sprint (context files)
      |
  Step 4: Set the week (focus + ceremonies)
```

---

## Step 1: Close the Sprint (Friday, 5 min)

See `1-close-sprint.md`

Run `/archive` or do manually:
- [ ] Move outputs from `outputs/` to `archive/outputs/`
- [ ] Move meeting notes to `archive/meetings/` (appropriate subfolder)
- [ ] Snapshot `context/current-sprint.md` to archive (copy, don't move)
- [ ] Log any undocumented decisions from the sprint into `context/decisions-log.md`

## Step 2: Update Tasks (Friday, 5 min)

See `2-update-tasks.md`

- [ ] In `tasks/active.md`: move completed items to Done section with one-line impact note
- [ ] Identify carry-forward items — anything not done that's still relevant
- [ ] Move carry-forward items to the top of Up Next (they get priority)
- [ ] Review `tasks/backlog.md` — pull candidate items for next sprint into active
- [ ] Check `context/open-items.md` — mark resolved items, update due dates

## Step 3: Open the New Sprint (Monday, 5 min)

See `3-open-sprint.md` — **this is the most important step**

Update `context/current-sprint.md`:
- [ ] Sprint number, start date, end date
- [ ] Sprint goal (outcome-oriented — what can a user do by end of sprint?)
- [ ] Committed stories (from sprint planning) with status and owner
- [ ] Carry-over from last sprint with reason
- [ ] Known constraints (holidays, reduced availability, external dependencies)

Update `context/risks.md`:
- [ ] Remove resolved dependencies
- [ ] Add any new cross-team dependencies for this sprint
- [ ] Update schedule risks based on current state

## Step 4: Set the Week (Monday, 5 min)

- [ ] Run `/daily` — confirms the system reads correctly
- [ ] Set This Week's Focus theme in `tasks/active.md`
- [ ] Check ceremony calendar — what's this week?
- [ ] Identify the #1 thing for the week

---

## Quality Check

`/archive` (Step 1) runs the OS health check — it verifies the load-bearing files are current, the inbox is cleared, the evidence-tracker has a new entry from this sprint, and `outputs/` is emptied. Read its findings before moving on.

After Monday's open-sprint steps, also confirm:
- `context/current-sprint.md` has real data for the new sprint (no placeholders, no `[TODO]`)
- Running `/daily` produces accurate, current output for where you actually are

## Failure Modes

| Failure | Prevention |
|---------|-----------|
| Forgetting to update current-sprint.md | This file is the single point of failure — do it first on Monday |
| Carry-forward items getting lost | Explicitly list them in active.md before clearing Done |
| Stale open-items.md | Review resolved items every sprint boundary |
| Sprint goal is vague | Write it as "Officers can ___" not "We will deliver ___" |
