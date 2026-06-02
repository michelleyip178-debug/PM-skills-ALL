# Cache & Tracker Sync Workflow

> Last updated: 2026-06-02
> How `/jira-sync` and `/stale-check` keep this hub honest. Both are PM-OS skills
> (run from the PM-OS workspace) that read and write files here in PM-skills-ALL-1.

---

## The two commands

| Command | Fixes | Direction |
|---|---|---|
| `/jira-sync` | The **ticket cache** (`03-stories/jira-sync/`), `sprint-allocation.md`, `sprint-status.md` counts | Pulls *from* live Jira *into* local files |
| `/stale-check` | The **planning files** (daily/weekly plans, `tasks-active`, `open-items`, `risks`, `sprint-status`) | Treats Jira + decisions log as truth, sweeps everything that reads them |

**The relationship that matters:** `/jira-sync` fixes the source, `/stale-check` fixes everything that reads from it. When both apply, **run jira-sync first.**

---

## Daily rhythm

| When | Command | Note |
|---|---|---|
| Morning | `/daily-plan` | unchanged |
| After meetings | `/meeting-notes` | unchanged |
| **End of day** | **`/stale-check`** → `/slack-message` | new EOD habit — catch drift the same day it happens |

`/stale-check` is the one new daily step. It stops a stale fact (a closed sprint, a moved ticket, a passed deadline) from walking into the next morning's standup.

---

## Weekly rhythm (Friday)

Run in this order — it's deliberate:

```
/weekly-review  →  /stale-check  →  /weekly-plan  →  /status-update
(what changed)     (clean trackers)  (plan on clean state)  (report out)
```

Why this order: `/weekly-review` just surfaced what changed this week, so the trackers are most stale *right then*. Clean them before planning, so next week's plan isn't built on drift. `/weekly-review` prompts you to run `/stale-check` next.

---

## When to run `/jira-sync` (not daily)

Reach for it when the cache could be behind:
- **Before grooming or sprint planning** — the cache must be honest
- **After a sprint transition** (e.g. Sprint 2 → 3)
- **When tickets feel mis-placed** or statuses look wrong

```
/jira-sync              → active sprint, both boards, open tickets only (fast default)
/jira-sync pathfinder   → active Pathfinder sprint only (board 12541)
/jira-sync core         → active Core sprint only (board 13640)
/jira-sync Sprint 4     → a named sprint folder
/jira-sync all          → every folder + Backlog (~198 files, slow — quarterly)
/jira-sync --dry-run    → report drift, change nothing
```

The default is fast: it diffs a manifest against live Jira in memory and only opens the files that actually changed.

---

## Notes

- **Needs the Atlassian MCP live** for the ticket refresh. If it's not loaded, `/jira-sync` stops (no file-only fallback). `/stale-check` can still run file-vs-file + decisions-log without it.
- The cache is **198 files, one per ticket, zero duplicates** (deduped 2026-06-02). Keep it that way — `/jira-sync` flags new duplicates for a batched delete.
- Board IDs and the Jira host live in PM-OS memory `reference_jira.md`.
- Fix-vs-flag discipline (both skills): unambiguous factual swaps get fixed inline; judgement calls (freeform ACs, sprint-date shifts, file deletions) get flagged for you.
