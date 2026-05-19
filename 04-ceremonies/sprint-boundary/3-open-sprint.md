# Step 3: Open the New Sprint

## When
Monday morning of the new sprint. Do this before running `/daily`.

## Update context/current-sprint.md

This is the single most important file in the OS. Every command reads it. If it's wrong, everything is wrong.

### Required fields

**Sprint details:**
- Sprint number (increment from last sprint)
- Start date (this Monday)
- End date (Friday of week 2)
- Week: Week 1

**Sprint goal:**
Write as an outcome: "Officers can ___" or "The system can ___"
Not: "We will deliver OTEP-85, OTEP-86, US-03"

Pull from sprint planning if it happened already. If planning is later this week, write a draft goal and update after planning.

**Committed stories:**
Copy from sprint planning output or Jira. For each:
- Story ID
- Title
- Status (Not started / In progress)
- Owner

**Carry-over:**
List anything carried from the previous sprint with the reason.

**Known constraints:**
- Public holidays this sprint
- Team members with reduced availability
- External dependencies with deadlines

### Template
```markdown
## Sprint details
- **Sprint number:** Sprint N
- **Start date:** DD MMM YYYY
- **End date:** DD MMM YYYY
- **Week:** Week 1

## Sprint goal
[Outcome-oriented — what can a user do by end of sprint?]

## Committed stories
| Story ID | Title | Status | Owner |
|---|---|---|---|

## Carry-over from last sprint
| Story ID | Title | Reason carried over |
|---|---|---|

## Known constraints this sprint
- [ ] ...
```

## Update context/risks.md

- Remove dependencies that were resolved last sprint
- Add new dependencies for this sprint's stories
- Check schedule risks — are we still on track for the Sep target?

## Update tasks/active.md

- Set "This Week's Focus" theme for the new sprint
- Update the "Current sprint" header line

## Shift the Sprint Checklists

Open `projects/otep-mvp/sprint-checklists.md`:
- [ ] Add a new section for the active sprint — list its stories with grooming-ready status and DoR blockers
- [ ] Last sprint's section: mark stories shipped vs carried; keep the entry for the audit trail
- [ ] Confirm story IDs reconcile against `projects/sprint-allocation.md` and the Jira board

## Check the Deferred ACs backlog

Open `projects/otep-mvp/deferred-acs.md`:
- [ ] Scan rows tagged for the now-active sprint — pull any that earned their way back in
- [ ] Mark anything pulled as 🟢 Pulled with the sprint number + Jira ticket
- [ ] If any AC was cut mid-sprint, append it as a new 🟡 Open row under the parent story

## Update README.md headers

Stale sprint references in `README.md` mislead anyone (you included) reading the OS cold. Fix four spots:
- [ ] Line ~7: "**Current:** Sprint N (DD MMM – DD MMM)" — update to the new sprint
- [ ] "## Current State (Sprint N)" heading — bump the number
- [ ] "Sprint goal:" line under that heading — match `context/current-sprint.md`
- [ ] Project table row "OTEP MVP — Sprint N — [theme]" — update sprint number and theme

## Done when
- `context/current-sprint.md` has zero placeholders
- `projects/otep-mvp/sprint-checklists.md` shows the active sprint's stories with current status
- `projects/otep-mvp/deferred-acs.md` reflects any new cuts or pulls from the last sprint
- `README.md` sprint references match the new sprint (4 spots above)
- Running `/daily` produces output that matches reality
- `tasks/active.md` references the new sprint
