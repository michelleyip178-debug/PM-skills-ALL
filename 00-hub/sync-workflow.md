# Cache & Tracker Sync Workflow

> Last updated: 2026-06-03
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
| Morning | `/daily-plan` | now pulls live Jira (via `jira-sprint.sh` / `jira-sync.py`) + adds a standup lens on sprint days. Absorbed the old `/daily` command (2026-06-03). |
| After meetings | `/meeting-notes` | unchanged |
| **End of day** | **`/stale-check`** → `/slack-message` | new EOD habit — catch drift the same day it happens |

`/stale-check` is the one new daily step. It stops a stale fact (a closed sprint, a moved ticket, a passed deadline) from walking into the next morning's standup.

> **Sprint-day prep** runs through the OTEP commands (`/groom-prep`, `/mid-sprint-review`, `/sprint-plan-prep`, `/retro-prep`) on their ceremony days — see [04-ceremonies/sprint-prep-rhythm.md](../04-ceremonies/sprint-prep-rhythm.md). For a deeper three-lens read, spawn the **sprint-trio** agent.

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

- **Live Jira works two ways** (confirmed 2026-06-03): the Atlassian MCP *or* the REST API directly via basic auth (`michelle_yip@psd.gov.sg` : `JIRA_API_TOKEN` from PM-OS `.mcp.json`). If the MCP isn't loaded into the session, the REST path still pulls live data — no need to stop. `/stale-check` can also run file-vs-file + decisions-log without either.
- The cache is **~198 files, one per ticket** (last big dedupe 2026-06-02; both Sprint 2s rolled into Sprint 3 on 2026-06-03). `/jira-sync` flags new duplicates for a batched delete.
- Board IDs, Jira host, and the REST-auth method live in PM-OS memory `reference_jira.md`. Active sprints (2026-06-03): Pathfinder S3 = Sprint 34617, Core S3 = Sprint 34607.
- Fix-vs-flag discipline (both skills): unambiguous factual swaps get fixed inline; judgement calls (freeform ACs, sprint-date shifts, file deletions) get flagged for you.

---

## Formatting backstop (both workspaces)

A `PostToolUse` hook (`.claude/hooks/format-md-check.py`) runs after every Write/Edit on a `.md` file in **both** PM-OS and PM-skills-ALL-1. It auto-inserts blank lines between consecutive `**Bold:**` lines (the recurring line-break issue) and flags headers missing a blank line. Silent when files are clean. Keeps the trackers here readable without manual fixes.
