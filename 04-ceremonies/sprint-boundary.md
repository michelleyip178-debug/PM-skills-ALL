# Sprint Boundary

Cleanly close one sprint and open the next. ~20 minutes across Friday and Monday.

Say "sprint boundary", "close the sprint", "open the sprint", or "sprint transition" to trigger this workflow.

---

## Friday — Close the Sprint (10 min)

### 1. Archive outputs
Move all dated briefs and dailies from `00-hub/outputs/` → `00-hub/outputs/archive/sprint-N/`. Move loose meeting notes from `inbox.md` → `04-ceremonies/archive-meetings/{subfolder}/` (subfolders: `int-sprint/`, `sprint-planning/`, `standups/`, `1on1s/`, `one-offs/`).

### 2. Snapshot sprint-status
Copy (don't move) `00-hub/sprint-status.md` → `00-hub/outputs/archive/sprint-N/snapshot-sprint-N-YYYY-MM-DD.md`. This preserves committed vs delivered.

### 3. Log undocumented decisions
Scan memory from the past 2 weeks: any scope calls in Slack/standup not in `06-skills-and-decisions/decisions-log.md`? Any informal R1 deferrals? Add each with date, decision, rationale, owner.

### 4. Update tasks-active.md
- Move completed items to Done with a one-line impact note (not just a strikethrough — say what it unblocked)
- Identify carry-forward items: why didn't they finish? still right priority?
- Move carry-forward to top of Up Next
- Pull next sprint's prep items from `00-hub/tasks-backlog.md`
- Clear stale crossed-out items

### 5. Update open-items.md
Move newly resolved items to Resolved with date. Update any stale "Needed by" deadlines. Add new items surfaced this sprint.

### 6. Update evidence-tracker.md
Add at least one row to `06-skills-and-decisions/pm-conversion/evidence-tracker.md`. Ask: "What did I do this sprint that a BA wouldn't have?" One entry per competency area (Outcomes thinking / Stakeholder influence / Roadmapping). If you can't find one for an area, that's where to focus next sprint.

**Friday done when:** `00-hub/outputs/` is empty · decisions logged · tasks-active clean · open-items current · evidence-tracker updated

---

## Monday — Open the New Sprint (10 min)

### 7. Update 00-hub/sprint-status.md

The single most important file. Every command reads it. If it's wrong, everything is wrong.

Required fields:
- Sprint number, start date, end date, week (Week 1)
- Sprint goal — write as outcome: "Officers can ___", not "We will deliver OTEP-85"
- Committed stories (from planning or Jira): Story ID, title, status, owner
- Carry-over from last sprint with reason
- Known constraints (holidays, reduced availability, external deps)

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

### 8. Update 00-hub/risks.md
Remove resolved dependencies. Add new cross-sprint dependencies. Check schedule — still on track for Oct go-live?

### 9. Update tasks-active.md header
Set "This Week's Focus" theme. Update the "Current sprint" header line.

### 10. Shift sprint-checklists.md
Open `04-ceremonies/sprint-checklists.md`:
- [ ] Add new section for the active sprint with stories, grooming-ready status, DoR blockers
- [ ] Last sprint's section: mark shipped vs carried (keep for audit trail)
- [ ] Confirm story IDs reconcile against `04-ceremonies/sprint-allocation.md` and Jira

### 11. Check deferred-acs.md
Open `03-stories/deferred-acs.md`: scan rows tagged for the active sprint — pull any that earned their way back in (mark 🟢 Pulled). If any AC was cut mid-sprint, append as 🟡 Open.

### 12. Update README.md (4 spots)
- Line ~7: `**Current:** Sprint N (DD MMM – DD MMM)` — bump
- `## Current State (Sprint N)` heading — bump
- `Sprint goal:` line — match `00-hub/sprint-status.md`
- Project table sprint number and theme

### 13. Run /daily
If the output matches reality, the sprint is open. If something looks wrong, a context file still has a placeholder.

**Monday done when:** `00-hub/sprint-status.md` has zero placeholders · sprint-checklists shows active sprint · README updated · `/daily` produces accurate output

---

## Common failure modes

| Failure | Prevention |
|---------|-----------|
| Forgetting sprint-status.md | Do it first on Monday — it's the single point of failure |
| Carry-forward items getting lost | Explicitly list them in tasks-active before clearing Done |
| Vague sprint goal | Write it as "Officers can ___" not "We will deliver ___" |
| Stale open-items.md | Review resolved items every sprint boundary, not ad hoc |
