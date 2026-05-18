# Daily PM Focus

Your job is to give Michelle a clear, actionable start to her day — oriented in 15 minutes, ready to unblock in standup.
Read CLAUDE.md, context/current-sprint.md, context/open-items.md, and tasks/active.md before generating output.

---

## Steps

### Step 0 — Schedule, recent activity, and live sprint state

**Calendar:** If Google Calendar MCP is connected, fetch today's and tomorrow's events.
Cross-reference meeting attendees with `areas/stakeholders/people/` profiles.
If no calendar MCP: note "Calendar not connected" and skip the schedule section.

**Recent activity:** Run `git log --since="yesterday" --name-only --pretty=format:""` to surface
files changed in the last 24-48 hours. Use this to populate "Recently Completed."

**Live sprint state (Jira):** Run `./scripts/jira-sprint.sh` to pull the active Pathfinder sprint.
Extract: sprint name, dates, goal, counts by status, anyone with multiple In Progress items (WIP risk),
and any stories still in Backlog during sprint week 2.
If the script fails, note "Jira fetch failed — using local context only" and continue.

**Sprint story detail:** Read per-issue markdown files from the most recent `jira-sync/Sprint-*/` folder.
For each story extract: key, title, status, assignee, story points, and the first 2 sentences of the description.
Cross-reference against `context/current-sprint.md` committed stories — flag any missing from jira-sync.
Flag: no assignee, no story points, Backlog in sprint week 2.
If the folder doesn't exist: note "Story detail not available — run `python3 scripts/jira-sync.py`" and skip.

**Standup lens:** Based on in-progress stories and PM-owned blockers (see Step 2), generate 2–3 bullets
on what to actively listen for in today's standup. Focus on:
- Stories where an engineer may be blocked on a PM decision, AC clarification, or design input
- Any In Progress story with a WIP flag (multiple items per person)
- Open items overdue that directly affect an in-progress story

### Step 1 — Identify today's ceremony and write prep to inbox

Read `areas/sprint-delivery/sprint-prep-rhythm.md` and check the "This Sprint" checklist against today's date.
If today has a ceremony prep entry:
1. Note which commands to run and when
2. Append to `inbox.md` `## Raw Capture` under `### Ceremony Prep`:
   `- [Ceremony name]: run [command(s)] — [timing]`
   If the entry already exists for today, skip to avoid duplicates.
3. Flag it prominently in the output

Also check if tomorrow has a ceremony — mention as a heads-up, don't write to inbox.

### Step 2 — Surface PM-owned blockers

This is the most important step for sprint health. Identify everything Michelle is blocking.

From `context/open-items.md`:
- Items where Owner includes "Michelle" that are still 🔴 Open
- Items overdue with Michelle as owner

From `tasks/active.md` Waiting On:
- Rows where the "Next action" requires Michelle to act (not waiting on someone else)
- Items stale >3 days where Michelle owns the next move

These form the **PM-Owned Blockers** section. If nothing, say "No PM-owned blockers today."

### Step 3 — Surface sprint-blocking open items

From `context/open-items.md`, identify items (owned by anyone) that are:
- Overdue
- Due today or tomorrow
- Blocking a story currently In Progress or needed before next ceremony

### Step 4 — Surface active tasks

From `tasks/active.md`:
- **In Progress** — what's actively being worked on (PM and engineering)
- **Up Next** — queued and ready to start
- **Waiting On** — items blocked on someone else; flag anything stale >3 days

### Step 5 — Recommend today's top 3 focus areas

Based on sprint position, PM-owned blockers, and ceremony timing, suggest 3 specific PM moves.
Not "review backlog" — name the person, decision, or deadline.
Frame each as: what to drive or decide, not just what to do.

### Step 6 — PM growth nudge

Michelle is a BA transitioning to PM. Her three growth areas:
1. Thinking in outcomes vs requirements
2. Stakeholder influence and vision
3. Roadmapping and prioritisation

One short nudge (1–2 sentences) connecting today's work to one growth area.

---

## Output format

Save as: `outputs/daily-YYYY-MM-DD.md`

---
## Daily Focus — [Date]

### Today's Schedule
- [time] — [meeting] ([location/format]) — [one thing to drive or bring, if any]
- If no calendar: "Calendar not connected — add meetings manually"

### Tomorrow ([day]):
- [time] — [meeting] — [what to drive or bring]

### Today's Ceremony
[Ceremony name + what to prepare, or "No ceremony today"]
[Tomorrow's ceremony as a heads-up if relevant]

### Standup Lens
Before standup, listen for:
- [story/person + what to watch for]
- [open item that could surface as a blocker]
- [WIP risk or decision that needs same-day resolution]

### Recently Completed
- [From git history — concrete deliverables only. If nothing, say so.]

### Sprint Pulse (Jira)
- **Sprint:** [name] ([start] → [end])
- **Goal:** [sprint goal]
- **In Progress:** [count] · **Done:** [count] · **Backlog:** [count]
- **Flags:** [WIP overload by person, late-sprint backlog items, or "None"]

### Sprint Stories
| Key | Title | Status | Assignee | Points | Flag |
|---|---|---|---|---|---|
| [KEY] | [title] | [status] | [assignee or —] | [pts or —] | [⚠️ no assignee / ⚠️ backlog wk2 / ✓] |

**Story summaries** (In Progress and flagged stories only):
- **[KEY]:** [first 2 sentences of description]

### PM-Owned Blockers
Things engineers or stakeholders are waiting on Michelle to resolve:

| Item | Who's waiting | Overdue since | Action |
|---|---|---|---|
| [open item or task] | [person/team] | [date or "today"] | [specific next move] |

If none: "No PM-owned blockers today."

### Open Items Needing Attention
Items owned by others that affect the sprint:

| # | Item | Owner | Due | Blocks |
|---|---|---|---|---|

### Active Tasks
**In Progress**
- [task] — [status/note]

**Up Next** (priority order)
- [task]

**Waiting On**
| Item | Waiting for | Since | Next action |
|---|---|---|---|

**Stale / needs update:**
- [flag tasks that are outdated or resolved]

### Top 3 Focus for Today
1. [Specific PM move — person + decision + deadline]
2. [Specific PM move]
3. [Specific PM move]

### PM Growth Nudge
[One short insight connecting today's work to Michelle's growth areas]

---
