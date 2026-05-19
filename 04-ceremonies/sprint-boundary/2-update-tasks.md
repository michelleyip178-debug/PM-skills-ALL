# Step 2: Update Tasks

## When
Friday of sprint week 2, after closing the sprint.

## In tasks/active.md

### Move completed items to Done
For each completed item, write a one-line impact note:
- Bad: ~~Confirm C@G ingestion method~~
- Good: ~~Confirm C@G ingestion method~~ — Pow Hwee confirmed API; unblocks OTEP-89/12 for Sprint 3

### Identify carry-forward
Items that aren't done but are still relevant for next sprint. For each:
- Why didn't it finish? (blocked, deprioritised, scope grew?)
- Is it still the right priority? Or should it go back to backlog?

Move carry-forward items to the top of "Up Next" — they get first priority.

### Pull from backlog
Open `tasks/backlog.md`. Look at the next sprint's prep section (e.g., "Sprint 3 Prep"). Pull relevant items into active.md.

### Clear stale items
Remove items that are no longer relevant. Don't leave crossed-out items piling up — they create visual noise. Keep the Done section for this sprint only.

## In context/open-items.md

### Mark resolved items
Move newly resolved items from the Open table to the Resolved table with date.

### Update due dates
Any "Needed by: next grooming" items from last sprint — are they still open? Update the deadline.

### Add new items
Did this sprint surface new open items? Add them with owner and deadline.

## In projects/pm-conversion/evidence-tracker.md

This is the PM conversion evidence — update it every sprint boundary.

### Add new evidence
Ask yourself: "What did I do this sprint that a BA wouldn't have done?"

For each entry, add one row to the right competency table:
- **Outcomes thinking** — did you frame anything around user outcomes before specs?
- **Stakeholder influence** — did you make a recommendation, defend a scope call, bring someone along?
- **Roadmapping and prioritisation** — did you say no, sequence work, or make a trade-off call?

Even one entry per sprint compounds. If you can't find anything for a competency area, that's where to focus next sprint.

### Update the date
Change the "Updated" line at the top and set "Next update" to the next sprint boundary.

---

## Done when
- active.md has a clean In Progress / Up Next / Waiting On / Done structure
- No stale crossed-out items cluttering the file
- open-items.md resolved table is current
- Updated date at bottom of active.md matches today
- evidence-tracker.md has at least one new entry from this sprint
