# Projects Changelog

Track what changed, where, and when. Most recent first within each date.

---

## 2026-05-18 (Jira comment sync — scope changes from Pow Hwee)

### context/current-sprint.md
- Story table rebuilt: OTEP-285 marked absorbed into OTEP-128 (not Sprint 3); OTEP-129 re-added as separate Sprint 2 story (overrides May 14 absorption); OTEP-268 re-added to Sprint 2 (overrides May 15 deferral); OTEP-191 deprioritised to Sprint 3+; OTEP-276 marked resolved
- Scope decisions updated: 4 new entries (OTEP-285 absorption, OTEP-129 re-add, OTEP-268 re-add, OTEP-191 deprioritisation); two prior decisions struck through
- Jira board cleanup: removed stale "Remove OTEP-268" and "Close OTEP-129" items; added "Remove OTEP-191"; marked OTEP-285/276 as resolved

### tasks/active.md
- Header note updated to reflect Jira comment sync scope changes
- Up Next: removed stale "heads-up to Thomas re OTEP-285/276"; added 3 new PM action items (#28 OTEP-85 visibility, #29 OTEP-289 ACs/timebox, OTEP-128 AC cleanup); added "heads-up to Thomas: OTEP-285 absorbed, no Sprint 3 ticket"
- Waiting On: OTEP-276 row marked resolved

### context/open-items.md
- Added open item #28: OTEP-85 visibility rule conflict (Michelle to confirm before grooming)
- Added open item #29: OTEP-289 spike definition — ACs, timebox, expected output (Michelle to define before grooming Tue 19 May)

---

## 2026-05-18 (sprint-allocation.md update)

### projects/sprint-allocation.md
- Sprint 1: marked CLOSED; updated final statuses (OTEP-170 carried, OTEP-202/203 carried, auth edge-cases OTEP-110/WOG-04–06 carried to Sprint 3); added partial sign-off note
- Sprint 2: marked CURRENT; updated sprint goal to match live Jira + context/current-sprint.md version; rebuilt stories table with live Jira statuses (In Progress, Done, Backlog); flagged OTEP-285 and OTEP-276 as missing from Jira board; updated OTEP-193 owner to Léo; added OTEP-191/288 as unexpected board entries; added carry-overs not yet on board (OTEP-202/203/271); added Jira cleanup callout (OTEP-268/129)
- Key Dependencies: updated WOG AD/Keycloak to Done (Sprint 1 closed)
- Updated "Last updated" to 2026-05-18

---

## 2026-05-18 (stale file sync)

### tasks/active.md
- Removed stale Waiting On rows: "Sprint 1 overflow list" (resolved) and "Tue/Fri squad sync rename" (pending, no blocker)
- Updated auth carry-overs row: OTEP-110/WOG-04–06 confirmed NOT on Sprint 2 board; review at mid-sprint Mon 26 May
- Updated design system row: OTEP-276 not on Sprint 2 board; OTEP-252 sub-task Done — confirm with Thomas if spike is still live
- Removed OTEP-133 + OTEP-130 from In Progress (deprioritised — Sprint 3/4); moved to Up Next with low-priority label
- Reordered Up Next by priority for Sprint 2 W1 (groom-prep, #23/#24 chase, OTEP-285 confirm at top)
- Removed stale date references in Up Next ("before Sprint 2 kickoff Mon 18 May", "Fri 15 May")

### context/risks.md
- Added "Sprint 2 Jira Board — Cleanup Actions Needed" section: OTEP-268/129 still on board (needs removal), OTEP-192/193/202/203/271/110/WOG stories not on board (needs placement confirm)
- Updated timestamp to 2026-05-18

### context/current-sprint.md
- Added "Jira board cleanup needed" checklist with 6 action items: remove OTEP-268/129, add OTEP-192/193, paste sprint goal, confirm OTEP-285, confirm OTEP-202/203/271 placement

---

## 2026-05-18 (Jira live sync — Sprint 2 board)

### context/current-sprint.md
- Rebuilt committed stories tables to reflect live Jira state (statuses, actual owners, unexpected tickets)
- Flagged: OTEP-285 and OTEP-276 not found on board; OTEP-193 owner is Léo not Pow Hwee; OTEP-268/129 still in sprint despite being deferred/absorbed; OTEP-191/288 added as new unlisted tickets; OTEP-202/203/271/110/WOG-04–06 not showing on Sprint 2 board
- Added sprint goal reminder to paste into Jira

### tasks/active.md
- Added OTEP-170 (Thomas, In Progress) and OTEP-288 (Léo, In Progress) to In Progress section
- Added OTEP-252 (Thomas, Done) to Done This Sprint
- Reverted OTEP-170 from Done (was incorrectly marked done May 15)
- Updated header note to reflect live Jira count

---

## 2026-05-18 (Sprint 2 kick-off + Sprint 1 wrap-up)

### Sprint 1 wrap
- Moved 3 remaining Sprint 1 output files to `outputs/archive/sprint-1/end-sprint/`: `endday-2026-05-15.md`, `retro-brief-2026-05-15.md`, `sprint-2-meetings-2026-05-15.md`

### Sprint 2 context updates
- `areas/sprint-delivery/sprint-prep-rhythm.md` — replaced Sprint 1 "This Sprint" block with Sprint 2 dates (May 18–29)
- `tasks/active.md` — updated "This Week's Focus" to Sprint 2 W1 theme (unblock #24, Squad Grooming, design lock date #22)
- `inbox.md` — cleared "[A] Close off Sprint 1 on 18 May 2026"; updated Ceremony Prep for today/tomorrow
- New outputs: `outputs/daily-2026-05-18.md`, `outputs/retro-2026-05-18.md`

---

## 2026-05-15 (Sprint 2 Jira reconciliation)

### Story ID changes (Sprint 2)
- **OTEP-85b → OTEP-285** — click-through + return-to-page state. Renamed everywhere when Jira ticket created.
- **OTEP-85a re-absorbed into OTEP-85** — "Closing soon" label rolled back into the card story. OTEP-85a removed from active scope; AC retained in `filters.md` for grooming reference.
- **OTEP-268 deferred — unticketed / unplanned** — empty/error/partial-load states removed from Sprint 2.
- **OTEP-276 added** — `[Spike] Investigate custom design system reimplementation`. Thomas owns. Confirms or replaces LifeSG as base.
- Sprint 2 story count: **6 → 5** (OTEP-85, OTEP-128, OTEP-267, OTEP-285, OTEP-276).

### Files touched
- `context/current-sprint.md`, `tasks/active.md`, `projects/sprint-allocation.md`, `projects/otep-mvp/story-id-map.md`, `projects/otep-mvp/sprint-checklists.md`, `projects/otep-mvp/stories/index.md`, `projects/otep-mvp/stories/filters.md`, `projects/otep-mvp/stories/otg-lifecycle.md`.

---

## 2026-05-13 (evening — post internal groom)

### sprint-allocation.md
- Sprint 2 confirmed: 3 new stories (OTEP-85, 267, 268) + 5 carry-over (OTEP-202, 193, 192, 194, 183)
- OTEP-86, OTEP-128, US-05, OTEP-71, OTEP-110 deferred to Sprint 3
- Carry-over section added with owners (Leo: OTEP-202, Pow Hwee: OTEP-183)
- Capacity: 18 May PM (PH + Pow Hwee + Michelle out), 22 May PM (Leo out), Thomas leave TBC

### story-id-map.md
- OTEP-86, OTEP-128, US-05 moved from Sprint 2 → Sprint 3
- OTEP-71 + subtasks moved from Sprint 2 → Sprint 3
- Jira IDs reconciled: OTEP-85a→OTEP-85, OTEP-285→OTEP-267, OTEP-85c→OTEP-268

### stories/filters.md
- OTEP-85: 3x5 grid, 15 cards/page, type labels updated (Internal Job / SJR / STIPs & Gigs, no "OTG"), functionality-first
- OTEP-267: 15 cards/page, no deep-linking, spinner not skeleton, LifeSG patterns
- OTEP-268: missing fields = blank (not collapsed), advanced behavior deferred

### risks.md
- Added: FE/design capacity shared across squads — mid-sprint resource conflict risk
- Thomas sole-FE risk updated with correct story IDs

### Internal grooming framework (new)
- Created `areas/sprint-delivery/internal-grooming-framework.md` — 7-phase reusable template

### Archive
- Meeting notes: `archive/meetings/int-sprint/2026-05-13-internal-squad-groom.md`

---

## 2026-05-13 (earlier — pre groom)

### prd-opportunities.md
- **Regenerated** — full rewrite to reflect May 8-13 decisions
- Section 3: SJR = discovery-only, Internal Jobs = FormSG, US-19 dropped
- Section 4 Group 2: OTEP-85 split into 85/267/268 with sprint column and dependency chain
- Section 4: critical path updated to show 85a as branching point
- Section 4: story count updated (21-22 MVP, up from 19-20)
- Section 4: OTEP-129 overlap with 85a flagged
- New Section 12: OTG field status table (5 of 6 confirmed)
- Section 6: 3 new design decisions (Secondment = SJR, visibility by closing date, reporting_line removed)
- Section 10: added stakeholder volatility and SJR deferral risks
- Section 11: synced with decisions-log through May 13
- Section 14: 3 questions resolved, 3 new added
- Appendix: links to workflow coverage audit, discovery plan, DoR/DoD guidelines
- Target release updated to Oct 16 throughout

### prd-auth.md
- **Regenerated** — full rewrite
- Story ID mapping note added (internal IDs vs story-id-map Jira IDs)
- Keycloak as identity broker (from Sprint 1)
- Auth flow accepted for MVP (Adrian, May 12) noted in status and design decisions
- Sprint 1 stories table with actual Jira tickets and status
- Sprint 3 carry-over table (OTEP-110, WOG-04/05/06)
- Timeline milestones updated with Sprint 1 actuals
- Target release updated to Oct 16

### stories/filters.md
- OTEP-85 replaced with OTEP-85/b/c (3 vertical slices)
- Each sub-story has full ACs, subtasks with track labels, and test cases
- OTEP-128 edge case: Secondment marked resolved
- OTEP-86 AC: Secondment marked resolved
- Open questions: #7, #8, #9 marked resolved; #10 (pagination pattern) and #11 (OTEP-129 overlap) added
- DoR blockers: #3, #4, #12 checked off; sort key checked off
- Updated 2026-05-13

### story-id-map.md
- OTEP-85 retired, replaced with OTEP-85/b/c rows (Jira TBD)

### sprint-allocation.md
- Sprint 2 table: OTEP-85 row replaced with 85/267/268 (3 rows with dependency notes)

### scoping-gaps-tracker.md
- Gap #8 (Secondment classification) marked Resolved
- Gap #1 (OTG pipeline fields) updated — 5 of 6 fields confirmed
- Summary: 9 open -> 1 resolved (+ previous count)

### workflow-coverage-audit.md
- **New file** — full workflow coverage audit across all officer-facing flows
- 7 workflow stages mapped (entry, discovery, detail, application, post-application, ringfencing, backend)
- 11 gaps identified (4 high, 4 medium, 3 low)
- PRD staleness table (3 sections needing update — now addressed)

---

## 2026-05-12

### sprint-allocation.md
- Reconciled to OTEP-Pathfinder Sprint Ceremonies v2 (12 sprints, Feature Freeze Sprint 8, Go-Live Oct 16)
- Sprint 2 scope = 5 stories, OTG data only (decision 2026-05-11)
- US-19 marked as dropped (Sprint 3 table)

---

## 2026-05-11

### sprint-allocation.md
- Sprint 2 scope locked: 5 stories (OTEP-85, 86, 128, 129, US-05)
- C@G deferred from Sprint 2 — ingestion unconfirmed
- Apply-redirects (US-18/19), auth edge-cases, ringfencing, search, category filter all moved to Sprint 3

### stories/filters.md
- Sprint 2 stories written with full ACs, edge cases, design/data dependencies
- Sprint 2 DoR blockers listed
- Open questions catalogued

### scoping-gaps-tracker.md
- 13 items catalogued (10 open, 3 deferred to R1)

---

## 2026-05-08

### story-id-map.md
- Initial reconciliation of Jira IDs to PRD story IDs

---

## 2026-05-06

### prd-opportunities.md
- **Created** — initial draft from Confluence PRD source

### prd-auth.md
- **Created** — initial draft

### stories/ (all files)
- Initial story files created: filters.md, otg-lifecycle.md, cag-handoff.md, tracking.md, profile-dependency.md, auth.md

---

*Append new entries at the top of the most recent date section, or add a new date header. Keep entries concise — one line per change, grouped by file.*
