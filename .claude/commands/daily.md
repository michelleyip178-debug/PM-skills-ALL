# Daily PM Focus

Your job is to give Michelle a clear, scannable start to her day.
Read CLAUDE.md, context/current-sprint.md, context/open-items.md,
and tasks/active.md before generating output.

---

## Steps

### Step 0 — Check schedule and recent activity
**Calendar:** If Google Calendar MCP is connected, fetch today's and tomorrow's events.
Cross-reference meeting attendees with `areas/stakeholders/people/` profiles.
If no calendar MCP: note "Calendar not connected" and skip the schedule section.

**Recent activity:** Run `git log --since="yesterday" --name-only --pretty=format:""` to surface
files changed in the last 24-48 hours. Use this to populate "Recently Completed" — what
was actually worked on, not what was planned.

**Live sprint state (Jira):** Run `./scripts/jira-sprint.sh` to pull the active Pathfinder sprint.
Parse the output to extract:
- Sprint name, dates, and goal
- Count of issues by status (In Progress, Done, Backlog/To Do)
- Names of anyone with multiple In Progress items (possible WIP overload)
- Stories still in Backlog late in the sprint (risk flag if today is in the second week)

If the script fails (auth error, network), note "Jira fetch failed — using local context only" and continue without breaking the rest of the flow.

### Step 1 — Identify today's ceremony and write prep to inbox
Read `areas/sprint-delivery/sprint-prep-rhythm.md` and check the "This Sprint" checklist against today's date.
If today has a ceremony prep entry:
1. Note which commands to run and when (morning, afternoon, after sign-off)
2. Append a line to the `## Raw Capture` section of `inbox.md` under a `### Ceremony Prep` subheading:
   `- [Ceremony name]: run [command(s)] — [timing]`
   If the `### Ceremony Prep` subheading already exists with today's entry, skip writing to avoid duplicates.
3. Flag it prominently in the output below

Also check if tomorrow has a ceremony — mention it as a heads-up but don't write to inbox.

### Step 2 — Surface the most important open items
From context/open-items.md, identify:
- Items overdue (past their needed-by date)
- Items due today or tomorrow
- Items blocking a story from being sprint-ready

### Step 3 — Surface active tasks
From tasks/active.md, show:
- **In Progress** — what Michelle is actively working on
- **Up Next** — what's queued and ready to start
- **Waiting On** — items blocked on someone else, with how long they've been waiting

Flag any tasks that are stale (no progress in >3 days), newly unblocked
(a dependency resolved since last update), or no longer relevant.
Recommend removing or updating stale items.

### Step 4 — Recommend today's top 3 focus areas
Based on sprint position, open items, and active tasks, suggest the 3
highest-leverage things Michelle should do today. Be specific — not
"review backlog" but "confirm eligibility field with Rama before Thursday grooming".

Frame each as a PM move: what to drive or decide, not just what to do.

### Step 5 — PM growth nudge
Michelle is a BA transitioning to PM. Her three growth areas are:
1. Thinking in outcomes vs requirements
2. Stakeholder influence and vision
3. Roadmapping and prioritisation

Based on what's happening in the sprint today, give one short nudge
(1-2 sentences) connecting today's work to one of her growth areas.

---

## Output format

Save as: `outputs/daily-YYYY-MM-DD.md`

---
## Daily Focus — [Date]

### Today's Schedule
- [time] — [meeting] ([location/format])
- If no calendar: "Calendar not connected — add meetings manually"

### Tomorrow ([day]):
- [time] — [meeting] — [what to drive or bring]

### Today's Ceremony
[Ceremony name + what to prepare, or "No ceremony today"]

### Recently Completed
- [What was actually finished since yesterday — from git history. Concrete deliverables, not vague summaries. If nothing, say so.]

### Sprint Pulse (Jira)
- **Sprint:** [name] ([start] → [end])
- **Goal:** [sprint goal]
- **In Progress:** [count] · **Done:** [count] · **Backlog:** [count]
- **Flags:** [WIP overload by person, late-sprint backlog items, or "None"]

### Open Items Needing Attention
| Item | Owner | Due | Status |
|---|---|---|---|

### Active Tasks
**In Progress**
- [task] — [status/note]

**Up Next**
- [task]

**Waiting On**
| Item | Waiting for | Since | Next action |
|---|---|---|---|

**Stale / needs update:**
- [flag any tasks that are outdated or resolved]

### Top 3 Focus for Today
1. [Specific action]
2. [Specific action]
3. [Specific action]

### PM Growth Nudge
[One short insight connecting today's work to Michelle's growth areas]

---
