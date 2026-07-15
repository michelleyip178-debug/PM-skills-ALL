# Current Sprint Context

> Update this file at the start of each sprint.
> All commands read this file — keeping it current makes every
> output accurate and specific to where you actually are.

> ⚠️ **STALE (flagged by /sprint-pulse, 2026-07-01):** everything below is frozen at the 2026-06-02 sync and still says "Sprint 3 active." Per `04-ceremonies/sprint-calendar.md`, **Sprint 5 (Mon 29 Jun – Fri 10 Jul) is actually active — today is Day 3.** Sprint 4 (15–26 Jun) ran and closed with no record here. Run `/jira-sync` to refresh before trusting anything below.

---

## Sprint details
- **Sprint number:** **Sprint 6 — Jira state is `future`, not started (13–26 Jul 2026).** ⚠️ See flag below — dates have passed but nobody has hit "Start Sprint" in Jira. Sprint 5 shows `closed` with a completeDate of 2026-07-14, but 41 issues carried over unresolved (not a clean close).
- **Sprint 2:** closed (Sprint 34616) — 6 stories Done at close.
- **Sprint 3 dates:** 2–14 Jun 2026 (Pathfinder Sprint 3 / Sprint 34617). Final state: 23 Done, 9 in QA at close (carry-in to S4), 4 Backlog carry-in.
- **Sprint 4 dates:** 15–26 Jun 2026. CLOSED 29 Jun 2026. Final state: 28 Done, 11 in QA (carry-in to S5), 11 In Progress (carry-in), 1 To Do, 12 Backlog carry-in.
- **Sprint 5 dates:** 29 Jun – 12 Jul 2026. Goal: officers browsing the opportunity listing can see which roles they're eligible for and filter by job category — so they spend less time on opportunities that aren't relevant to them.

**Confirmed sprint schedule (updated 2026-06-23):**

| Sprint | Dates | Notes |
|--------|-------|-------|
| S5 | 29 Jun – 12 Jul | |
| S6 | 13 Jul – 26 Jul | |
| S7 | 27 Jul – 9 Aug | |
| S8 | 11–21 Aug | UAT starts 11 Aug (Profile + Opportunities modules) |
| S9 | 24 Aug – 4 Sep | UAT continues (remaining modules from 17 Aug); dev ends 4 Sep |

**Post-dev timeline:** Code freeze → VAPT 7 Sep–16 Oct → Deploy 19–23 Oct → Soft launch 26–30 Oct → **First release: week of 2 Nov**

## Sprint goal
**Sprint 2:** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

**Sprint 3:** By end of Sprint 3, an officer can find relevant opportunities using filters and successfully initiate an application to any active OTG opportunity (except SJRs), powered by live imported data.

**Sprint 4 (agreed at planning 2026-06-11):** Deliver a complete, usable opportunity listing experience — officers can search, filter, and sort opportunities, understand what each type means, and trust that the data they're seeing is current and accurate.

**Sprint 5 (confirmed at start 2026-06-29):** By end of sprint, officers browsing the opportunity listing can see which roles they're eligible for and filter by job category — so they spend less time on opportunities that aren't relevant to them.

---

## Sprint 6 — ✅ ACTIVE (13–26 Jul 2026) — formally started between 2026-07-14 morning and midday syncs

> Source: OTEP-Pathfinder Sprint 6 (Sprint 34620). **Live pull: 2026-07-14 midday (2nd pull today, direct Jira REST API via `/jira-sync`).** 89 issues total (unchanged count from this morning, but composition shifted — see deltas below). Sprint 5 (34619) shows `closed` in Jira with completeDate 2026-07-14, but 76 of its 79 tickets carried straight into Sprint 6 rather than being cleanly resolved — this is a rollover, not a clean sprint close.
> Goal: carried from Sprint 5 (officers browsing the opportunity listing can see which roles they're eligible for and filter by job category) — Sprint 6's own goal not yet separately confirmed, though the sprint is now formally active.

**In Progress (11):** OTEP-88 (C@G listing, Léo), OTEP-405 (keyword search, Thomas), OTEP-386 (opportunity type tooltip, Thomas), OTEP-390 (ringfenced detail states, Thomas), OTEP-439 (ineligible states design, Amber), OTEP-276 (design-system spike, Pow Hwee), OTEP-349 (competency matching spike, Pow Hwee), OTEP-350 (WOG AD onboarding, Fabian), OTEP-361 (ADR forum, Pow Hwee), OTEP-444 (Azure/Entra AD mock, Léo), **OTEP-683** (opportunity detail update, Thomas — new, corrected from Backlog)

**In QA (16):** OTEP-268 (empty/error states), OTEP-305 (login/logout), OTEP-128 (detail page), OTEP-284 (closing soon, Thomas), OTEP-129 (open/closed, Thomas), OTEP-87 (C@G opp detail, Thomas), OTEP-438 (admin view, Hao Eng), OTEP-131 (broken FormSG link, Thomas), OTEP-406 (sort, Thomas), OTEP-392 (federated logout, Thomas), OTEP-571 (STIP/Gig card layout, Hao Eng), OTEP-595 (Keycloak realm displayName, Pow Hwee), OTEP-304 (stay-authenticated, Hao Eng), OTEP-283 (Ministry icons, unassigned), OTEP-505 (CFT upload/webhook, Hao Eng — **re-confirmed unchanged since this morning, see open item #52**), **OTEP-613** (default agency logo, Thomas Huchedé — new, corrected from Backlog)

**To Do (6):** OTEP-445 (POCDEX code table import spike), OTEP-663 (BUG — competencies listing, Thomas), OTEP-677 (BUG — OTG/C@G data import NOT done, Thomas), OTEP-667 (BUG — opportunities details page, unassigned), OTEP-668 (BUG — search opportunities, Thomas), **OTEP-437** (filter by job family, Hao Eng — new, corrected from Backlog)

**Done (33):** OTEP-170, OTEP-193, OTEP-288, OTEP-296 (Michelle), OTEP-313, OTEP-314, OTEP-320, OTEP-325, OTEP-326, OTEP-327, OTEP-334, OTEP-362, OTEP-363, OTEP-367, OTEP-368, OTEP-369, OTEP-374, OTEP-375, OTEP-380, OTEP-381, OTEP-440, OTEP-441, OTEP-482, OTEP-484 (Léo), OTEP-495, OTEP-496, OTEP-499, OTEP-536, OTEP-540 ✅ (Michelle), OTEP-85 (listing cards), OTEP-539 (C@G background import, Léo), OTEP-86 (filters), OTEP-541 (agencies fetch/map FE, Thomas) — **note: OTEP-604 (Keycloak CI build, Pow Hwee) moved OUT of this Sprint-6 Done list; live Jira places it in the closed Sprint 5, relocated in cache accordingly**

**Backlog (23):** OTEP-289, OTEP-329, OTEP-336, OTEP-348, OTEP-393, OTEP-403, OTEP-404, OTEP-408, OTEP-409, OTEP-483, OTEP-485 (Léo), OTEP-502 (Thomas), OTEP-569, OTEP-570, OTEP-659 (smoke test, Thomas), OTEP-662 (login error after redeploy, Thomas), OTEP-666 (scheduled import trigger), OTEP-679 (CSC connectivity, Fanxu), OTEP-680 (observability check, Léo), OTEP-681 (integration testing), OTEP-682 (autogenerate doc), OTEP-684 (refactor ingestion model), OTEP-130 (STIP/Gig PostHog tracking) — **OTEP-613, OTEP-683 moved out this morning/midday; OTEP-437 moved out this pull, see To Do above**

**⚠️ Still out of sprint per live Jira, left in cache but flagged (no Sprint 7/8 Pathfinder folders exist to relocate into):** OTEP-110, OTEP-111 (→ Sprint 7), OTEP-331, OTEP-614, OTEP-615 (→ Sprint 8), OTEP-71 (→ Sprint 7), OTEP-425 (→ no sprint, removed from all sprints in Jira). These are leftover from the original 07-07 provisional pull and predate this morning's 76-file rollover — not counted in the 89-issue total above since Jira itself no longer places them in Sprint 6.

**PM-owned:** OTEP-296 ✅ Done, OTEP-540 ✅ Done. No other Michelle stories active in S6.

**2026-07-14 jira-sync — Pathfinder scope:** Relocated 76 files from the `Sprint-34619-OTEP-Pathfinder-Sprint-5` folder to `Sprint-34620-OTEP-Pathfinder-Sprint-6` (live Jira confirms these tickets now sit in Sprint 6). 2 files stayed in the Sprint 5 folder correctly (OTEP-322, OTEP-328 — both Done, historically placed in earlier closed sprints per Jira's own sprint history). 1 stale duplicate (OTEP-613) removed from the Sprint 5 folder — canonical copy already existed in Sprint 6. 4 status corrections applied: OTEP-283 (In Progress→QA), OTEP-505 (In Progress→QA), OTEP-541 (In Progress→Done), OTEP-86 (QA→Done). All 98 files in the Sprint 6 folder now carry a `Sprint:` field and today's sync stamp.

**✅ Resolved 2026-07-14 midday:** Sprint 6 (34620) is now Jira state `active` — someone hit "Start Sprint" between this morning's pull (still `future`) and this midday pull. No longer a flag.

**2026-07-14 afternoon jira-sync (3rd pass today) — 1 delta since midday:** OTEP-437 (filter by job family) moved Backlog→To Do, assigned to Hao Eng. OTEP-505 re-confirmed unchanged again (QA, Hao Eng) — three independent pulls today (morning, midday, afternoon) all agree, consistent with today's separate confirmation that OTEP-505 is resolved/ready for QA. Core board's 4 cached tickets (OTEP-78/82/83/84) unchanged since midday. The 8 out-of-sprint leftover tickets (OTEP-110/111/331/425/594/614/615/71) are unchanged — still flagged, still no Sprint 7/8 folders to relocate into.

**2026-07-14 midday jira-sync (2nd pass today) — 3 further deltas found since the morning sync:**
- OTEP-613: Backlog→QA, assignee N/A→Thomas Huchedé
- OTEP-683: Backlog→In Progress
- OTEP-604: relocated from Sprint-6 cache folder to Sprint-5 folder — live Jira places it in the closed Sprint 5 (34619), not Sprint 6, despite being Done. Cache had it misfiled.
- **8 tickets confirmed moved out of Sprint 6 to future sprints, left in place (flagged, not relocated — no Sprint 7/8 Pathfinder folders exist yet):** OTEP-110, OTEP-111 → Sprint 7; OTEP-331, OTEP-614, OTEP-615 → Sprint 8; OTEP-71 → Sprint 7; OTEP-425 → no sprint (removed from all sprints in Jira). These are the original 07-07 provisional-pull files that predate this morning's 76-file rollover — worth a follow-up run once Sprint 7/8 folders exist or get created.
- **OTEP-505 re-confirmed unchanged: still QA, still Hao Eng.** No movement between the morning and midday pulls — this is a real stall, not a sync artifact.

**Core board cache cleanup (2026-07-06):** 19 orphaned ticket files (OTEP-180, 187, 189, 213, 214, 219, 227, 234, 263, 266, 269, 275, 277, 279, 297, 298, 308, 321, 365) removed from `OTEP-Core-13640-Sprint-5-34609/` — confirmed they no longer belong to Core Sprint 5's live issue list, archived to `03-stories/jira-sync/Archive/OTEP-Core-13640-Sprint-5-34609-orphaned-2026-07-06/` rather than deleted. **2026-07-14 update:** OTEP-Core board (13640) has a genuine active "OTEP-Core Sprint 6" (34610, goal: JumpStart recommendations + course search/discovery from LEARN) with **183 live issues** — this is a much larger, mostly separate workstream (Profile, Course Discovery, Infra/DevSecOps, Analytics) from what this workspace's local cache tracks (only 4 files exist: OTEP-78/82/83/84). Confirmed those 4 files have correct status (all Backlog, unchanged) and bumped their sync stamps, but did not import the other 179 live issues — that's a scope decision (does this PM's tracking need the full Core board, or just the Pathfinder-adjacent slice?), not something to auto-decide. Also: OTEP-78 has moved to Sprint 7 (future) live — flagging for relocation once a Core Sprint 7 folder exists, not creating one unprompted.

> Source: OTEP-Pathfinder Sprint 4. Final live pull: 2026-06-29. CLOSED.
> Goal: Complete, usable listing experience — search, filter, sort, data currency.

## Sprint 2 — CLOSED ✅ (synced 2026-06-02)

> Sprint 2 (Sprint 34616) is **closed**. 6 stories Done at close. Unfinished work (QA + In Progress + carry-overs) was pulled into Sprint 3 when it started.

**Done at close (6):** OTEP-267 (pagination), OTEP-252 (design system), OTEP-194 (FormSG spike), OTEP-193 (data model), OTEP-288 (backend stub), OTEP-296 (report format).

**Carried into Sprint 3** (not finished in S2): 11 QA items, OTEP-85/313/322 (In Progress), OTEP-128/268, OTEP-129 (open/closed story). See Sprint 3 below.

---

## Sprint 4 — CLOSING TODAY (15–26 Jun 2026)

> Source: OTEP-Pathfinder Sprint 4 (Sprint 34618). **Live pull: 2026-06-26.** 66 issues total.
> Goal: Deliver a complete, usable opportunity listing experience — officers can search, filter, and sort opportunities, understand what each type means, and trust that the data they're seeing is current and accurate.

**In Progress (12):** OTEP-88 (C@G listing, Léo), OTEP-405 (keyword search, Thomas), OTEP-495 (search backend, Thomas), OTEP-322 (Playwright, Rathika), OTEP-276 (design-system spike, Pow Hwee), OTEP-350 (WOG AD onboarding, Fabian), OTEP-349 (competency spike, Pow Hwee), OTEP-361 (ADR forum, Pow Hwee), OTEP-505 (CFT upload/webhook, Hao Eng), OTEP-539 (C@G background import, Léo), OTEP-386 (ringfencing tooltip, Amber), OTEP-439 (filter ineligible states, Amber)

**In QA (10):** OTEP-86 (filters), OTEP-268 (empty/error states), OTEP-85 (listing cards), OTEP-305 (login/logout), OTEP-128 (detail page), OTEP-129 (open/closed, Thomas), OTEP-284 (closing soon label, Thomas), OTEP-392 (federated logout, Thomas), OTEP-406 (sort opportunities, Thomas), OTEP-438 (admin view placeholder, Hao Eng)

**Done (31):** OTEP-127 ✅, OTEP-170, OTEP-193, OTEP-288, OTEP-296, OTEP-313, OTEP-314, OTEP-320, OTEP-324, OTEP-325, OTEP-326, OTEP-327, OTEP-334, OTEP-358 ✅, OTEP-362, OTEP-363, OTEP-367, OTEP-368, OTEP-369, OTEP-374, OTEP-375, OTEP-380, OTEP-381, OTEP-397 ✅, OTEP-427 ✅, OTEP-440, OTEP-441, OTEP-482, OTEP-496, OTEP-499, OTEP-536

**Backlog (13):** OTEP-87, OTEP-131, OTEP-289, OTEP-328, OTEP-329, OTEP-348, OTEP-393, OTEP-403, OTEP-404, OTEP-444, OTEP-483, OTEP-484, OTEP-485

**PM-owned:** OTEP-127 ✅ Done, OTEP-358 ✅ Done, OTEP-397 ✅ Done, OTEP-427 ✅ Done. All Michelle PM stories closed at sprint end.

---

## Sprint 3 — CLOSED (ended 12 Jun 2026)

> Source: OTEP-Pathfinder Sprint 3 (Sprint 34617), **state = closed 12 Jun**. Final live pull 2026-06-16. **53 issues** in folder (4 stale dupes removed 2026-06-16). 25 Done, remainder carried to S4.
> **OTEP-Core Sprint 3** (Sprint 34607): closed. (Live 2026-06-08.)

### Sprint 3 final state

**Done (25):** OTEP-170, OTEP-193, OTEP-288, OTEP-296, OTEP-303, OTEP-313, OTEP-314, OTEP-317, OTEP-320, OTEP-325, OTEP-326, OTEP-327, OTEP-332, OTEP-334, OTEP-351, OTEP-362, OTEP-363, OTEP-367, OTEP-368, OTEP-369, OTEP-374, OTEP-375, OTEP-380, OTEP-381, OTEP-391

**Carried to S4 (QA/In Progress/Backlog):** All remaining — see Sprint 4 above.

### New Sprint 3 scope (Backlog)

| Ticket | Title | Assignee | Notes |
|--------|-------|----------|-------|
| OTEP-86 | Filter opportunities by type | — | |
| OTEP-317 | Clear filters and reset view | — | Pairs with OTEP-86 |
| OTEP-87 | View C@G Opportunity Detail | — | ⚠️ Scope overlap w/ OTEP-319 — 87 keeps CTA visibility + back-state + empty-field; 319 owns click behaviour. Align PM afternoon 2026-06-02, confirm Wed grooming. |
| OTEP-88 | Identify C@G listings | — | |
| OTEP-89 | View C@G Job (Deep-Link) | — | |
| OTEP-319 | Apply via FormSG — basic redirect | — | `formsg_url` confirmed ✅ |
| OTEP-305 | Login and Logout (replace keycloak w/ actual) | — | **Build actual pages now against Keycloak; WOG AD swaps in later (D 2026-06-02).** Needs owner. |
| OTEP-192 | Recurring OTG data ingestion job | Léo Milbor | **In Progress** — critical path |
| OTEP-324 | OAuth 2.0 Refresh Token Rotation | Thomas | |
| OTEP-348 | OTG ingestion — scheduler & observability | — | |
| OTEP-349 | [Spike] Competency matching w/ OTEP-Core | — | Cross-squad |
| OTEP-350 | Onboard WOG AD | Fabian Peh | #26 |
| OTEP-351 | [Spike] Azure AD mock for testing | — | Unblocks auth testing w/o prod WOG AD |
| OTEP-352 | Load POCDEX production code table | Pow Hwee | |
| OTEP-358 | [Spike] Robust nil-date OTG import | **Michelle** | PM-owned. Scope + timebox. |
| OTEP-361 | Conduct ADR review forum | Pow Hwee | Cross-squad |
| OTEP-362 | 🆕 Backend: don't return closed opportunities | — | **NEW — OTEP-129 split (backend half)** |
| OTEP-363 | 🆕 UI: display closed opportunity | — | **NEW — OTEP-129 split (frontend half)** |
| OTEP-86/88/89… | (C@G + filter set above) | — | |
| OTEP-276 | [Spike] Custom design system reimpl | — | Likely drop — OTEP-252 Done resolves |
| OTEP-289 | [Spike] Filter by Functions (C@G) | — | Gates OTEP-318 go/no-go |

### Still NOT on the Sprint 3 board (⚠️ reconcile)

| Ticket | Title | Notes |
|--------|-------|-------|
| OTEP-271 | Local POCDEX database | Not on board — decide: add or accept out |
| OTEP-203 | Standalone POCDEX API service | Same |
| OTEP-318 | Filter by category | Correctly excluded — OTEP-289 spike still Backlog |

**Note:** OTEP-129 is now **on the Sprint 3 board (Backlog)** and split into OTEP-362/363 — earlier "not pulled into Sprint 3" note is resolved.

---

## Design lock + key Sprint 3 constraints

- **Design lock:** Wednesday 3 June — engineers must not start UI until Amber signs off final Figma
- **Vesak Day:** already passed (~1 June) — 2 June is a normal working day; standup runs
- **Mid-sprint review:** Monday 8 June (pulse check, not formal ceremony) — ✅ invite sent
- **Thomas:** sole FE engineer; design lock is the single biggest risk for his first week
- **OTEP-289 spike still Backlog:** OTEP-318 (filter by category) can't be confirmed until spike completes. Get outcome at today's Sprint Review.

---

## Scope decisions

- (2026-06-04) **Plan of record = Pow Hwee's "Planning draft for sprint 3 and after"** (Confluence, PSD-OTEP) — adopted as the team's S2–S6 shape. **Amendment:** native apply = R1, not an S4 spike (MVP apply = FormSG redirect, OTEP-319). S4 dates **15–28 Jun** (Sprint 34618, planning ceremony 14 Jun, engineers start 15 Jun). See decisions-log + [adoption reconciliation](../../PM-OS/outputs/archive/2026-W23-Jun01-Jun07/analyses/2026-06-04-W23-adopt-powhwee-plan-reconciliation.md).
- (2026-05-29) **OTG sync cadence: one-time port only** — no ongoing automated sync. Pilot agencies driven to adopt Compass directly. See D-016. Resolves open question from Sprint 3 Planning.
- (2026-05-28) **Design lock: Wednesday 3 June** (D-013)
- (2026-05-28) **OTG competency migration: file ingestion, not live API** (D-010) — Fanxu owns Sprint 3 one-time bulk import
- (2026-06-02) **OTEP-305 login/logout: build actual pages now against Keycloak; WOG AD swaps in later.** Confirmed in Sprint 3. Auth FE proceeds in parallel while WOG AD domain submission pending (#26). See decisions-log.
- (2026-05-21) **Auth epic deferred to Sprint 4+** — OTEP-71, OTEP-110, OTEP-304 deferred; no WOG AD UAT env (#26). (OTEP-305 login/logout pages excepted — buildable now via Keycloak, see above.)
- (2026-05-21) **OTEP-271/203 confirmed in Sprint 3** — but still not on Jira Sprint 3 board; reconcile.

---

## Jira board actions still needed

- [ ] Confirm OTEP-271 + OTEP-203 — add to Sprint 3 board if still committed (still NOT on board)
- [ ] **Assign OTEP-305 an owner** — login/logout pages buildable now via Keycloak; unassigned. Raise at standup.
- [ ] OTEP-289 spike output — go/no-go for OTEP-318 (still Backlog)
- [ ] OTEP-87 competency section — scope is firm (it's included); open dependency is **data, not scope**: ingestion lands first, so whether each C@G opportunity actually carries competencies isn't confirmed yet. Track via ingestion.
- [ ] OTEP-358 (Michelle, nil-date spike) — scope + timebox
- [ ] OTEP-361 (Pow Hwee, ADR forum) — confirm timing + PM involvement
- [x] ~~Confirm OTEP-305 Sprint 3 vs 4+~~ — resolved: in Sprint 3, build via Keycloak (D 2026-06-02)
- [x] ~~OTEP-129 placement~~ — resolved: on Sprint 3 board, split into OTEP-362/363

---

*Updated: 2026-07-14 afternoon (jira-sync, 3rd pass today — 1 delta: OTEP-437 Backlog→To Do, assigned Hao Eng. OTEP-505 re-confirmed unchanged (QA, Hao Eng) for the 3rd consecutive pull today.) Prior: 2026-07-14 midday (jira-sync, 2nd pass today — Sprint 6 now Jira state `active` (was `future` this morning). 3 deltas since morning sync: OTEP-613 Backlog→QA (+assignee), OTEP-683 Backlog→In Progress, OTEP-604 relocated Sprint-6→Sprint-5 cache folder (live Jira places it there despite being Done). OTEP-505 re-confirmed unchanged (QA, Hao Eng) — genuine stall, not a sync gap. 8 tickets confirmed dropped from Sprint 6 to future sprints (7/8) or removed from all sprints — flagged, not relocated, no target folders exist yet.) Prior: 2026-07-14 morning (jira-sync — Pathfinder Sprint 5→6 rollover synced: 76 files relocated, 4 status corrections (OTEP-283/505/541/86), 1 stale duplicate removed (OTEP-613). Total moved to Sprint 6 folder: 89 issues (26 Backlog, 5 To Do, 15 QA, 33 Done, 10 In Progress). Flagged: Sprint 6 still Jira state `future`, not formally started; Core board has 183 live issues vs 4 tracked locally — scope decision needed, not auto-imported.) Prior: 2026-07-06 (jira-sync — direct Jira REST API pull, MCP unavailable this session. Total 76→81: 6 new tickets (659, 662, 663, 666, 667, 668). Field corrections: OTEP-85 QA→Done, OTEP-322 In Progress→Done, OTEP-539 In Progress→Done, OTEP-87 In Progress→QA, OTEP-444 Backlog→In Progress, plus assignee updates for OTEP-390/484/485. Counts: 12 In Progress (was 13), 13 QA (was 14), 2 To Do (was 1), 33 Done (was 30), 21 Backlog (was 18).) Prior: 2026-07-03 (stale-check — corrected In Progress/QA counts and lists against live Jira: prior version had 14 In Progress / 13 QA transposed against live 13 In Progress / 14 QA, and OTEP-87 mis-tagged as In Progress when Jira shows it in QA. Backlog corrected 17→18 — OTEP-659 added live, not yet reflected. Total 75→76.) Prior: 2026-07-02 (jira-sync — Pathfinder Sprint 5 cache folder cleanup: deleted stale duplicate `OTEP-Pathfinder-12541-Sprint-5-34619` (11 partial files); canonical `Sprint-34619-OTEP-Pathfinder-Sprint-5` verified 75/75 against live Jira, zero field drift, all 75 files stamped. Counts: 75 issues total (was 74), 14 In Progress, 13 QA, 1 To Do, 30 Done (was 29 — OTEP-604 added, already Done), 17 Backlog. Source: direct Jira REST API pull, sprint 34619.) Prior: 2026-07-01 (jira-sync full sweep — Sprint 5 recomputed from live Jira: 74 issues total (was 55), 14 In Progress (was 12), 13 QA (was 11), 1 To Do, 29 Done, 17 Backlog (was 21)). Prior: 2026-06-26 (stale-check — IP 10→12 +386/439, Backlog 15→13, total 67→66 — OTEP-127 + OTEP-397 Done; OTEP-358 In Progress not Backlog; counts 14 IP→12, 8 QA→10, 20 Done→29). Prior: 2026-06-24 (timeline update — S4 close Fri 26 Jun; S5–S9 dates; VAPT 7 Sep–16 Oct; first release 2 Nov). Sprint 3 CLOSED 12 Jun. Sprint 4 ACTIVE 15–26 Jun. S4: 12 In Progress, 10 QA, 29 Done, 1 To Do (live 2026-06-25).*
