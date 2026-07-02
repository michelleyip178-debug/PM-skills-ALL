# Current Sprint Context

> Update this file at the start of each sprint.
> All commands read this file — keeping it current makes every
> output accurate and specific to where you actually are.

---

## Sprint details
- **Sprint number:** **Sprint 5 ACTIVE (29 Jun – 12 Jul 2026)**
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

## Sprint 5 — ACTIVE (29 Jun – 12 Jul 2026)

> Source: OTEP-Pathfinder Sprint 5 (Sprint 34619). **Live pull: 2026-07-02.** 75 issues total (up from 74 on 2026-07-01 — OTEP-604 added, already Done).
> Goal: Officers browsing the opportunity listing can see which roles they're eligible for and filter by job category.

**In Progress (14):** OTEP-87 (C@G opp detail, Thomas), OTEP-88 (C@G listing, Léo), OTEP-276 (design-system spike, Pow Hwee), OTEP-304 (stay-authenticated, Hao Eng), OTEP-322 (Playwright, Rathika), OTEP-349 (competency spike, Pow Hwee), OTEP-350 (WOG AD onboarding, Fabian), OTEP-361 (ADR forum, Pow Hwee), OTEP-386 (opportunity type tooltip, Thomas), OTEP-405 (keyword search, Thomas), OTEP-439 (ineligible states design, Amber), OTEP-505 (CFT upload/webhook, Hao Eng), OTEP-539 (C@G background import, Léo), OTEP-541 (agencies fetch/map FE, Thomas)

**In QA (13):** OTEP-85 (listing cards), OTEP-86 (filters), OTEP-128 (detail page), OTEP-129 (open/closed, Thomas), OTEP-131 (broken FormSG link, Thomas), OTEP-268 (empty/error states), OTEP-284 (closing soon, Thomas), OTEP-305 (login/logout), OTEP-392 (federated logout, Thomas), OTEP-406 (sort, Thomas), OTEP-438 (admin view, Hao Eng), OTEP-571 (STIP/Gig card layout, Hao Eng), OTEP-595 (Keycloak realm displayName, Pow Hwee)

**To Do (1):** OTEP-445 (POCDEX code table import spike)

**Done (30):** OTEP-170, OTEP-193, OTEP-288, OTEP-296 (Michelle), OTEP-313, OTEP-314, OTEP-320, OTEP-325, OTEP-326, OTEP-327, OTEP-328, OTEP-334, OTEP-362, OTEP-363, OTEP-367, OTEP-368, OTEP-369, OTEP-374, OTEP-375, OTEP-380, OTEP-381, OTEP-440, OTEP-441, OTEP-482, OTEP-495, OTEP-496, OTEP-499, OTEP-536, OTEP-540 ✅ (Michelle), OTEP-604 (Keycloak CI build job + lowercase realm emails, Pow Hwee)

**Backlog (17):** OTEP-283, OTEP-289, OTEP-329, OTEP-336, OTEP-348, OTEP-390, OTEP-393, OTEP-403, OTEP-404, OTEP-408, OTEP-409, OTEP-437, OTEP-444, OTEP-483, OTEP-484, OTEP-485, OTEP-570

**PM-owned:** OTEP-296 ✅ Done, OTEP-540 ✅ Done. No other Michelle stories active in S5.

**Note:** OTEP-324 (OAuth refresh token rotation) no longer appears in this sprint's live pull — dropped from Backlog list, not confirmed why (check board history / decision log).

---

## Sprint 4 — CLOSED (15–26 Jun 2026, completed 29 Jun)

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

*Updated: 2026-07-02 (jira-sync — Pathfinder Sprint 5 cache folder cleanup: deleted stale duplicate `OTEP-Pathfinder-12541-Sprint-5-34619` (11 partial files); canonical `Sprint-34619-OTEP-Pathfinder-Sprint-5` verified 75/75 against live Jira, zero field drift, all 75 files stamped. Counts: 75 issues total (was 74), 14 In Progress, 13 QA, 1 To Do, 30 Done (was 29 — OTEP-604 added, already Done), 17 Backlog. Source: direct Jira REST API pull, sprint 34619.) Prior: 2026-07-01 (jira-sync full sweep — Sprint 5 recomputed from live Jira: 74 issues total (was 55), 14 In Progress (was 12), 13 QA (was 11), 1 To Do, 29 Done, 17 Backlog (was 21)). Prior: 2026-06-26 (stale-check — IP 10→12 +386/439, Backlog 15→13, total 67→66 — OTEP-127 + OTEP-397 Done; OTEP-358 In Progress not Backlog; counts 14 IP→12, 8 QA→10, 20 Done→29). Prior: 2026-06-24 (timeline update — S4 close Fri 26 Jun; S5–S9 dates; VAPT 7 Sep–16 Oct; first release 2 Nov). Sprint 3 CLOSED 12 Jun. Sprint 4 ACTIVE 15–26 Jun. S4: 12 In Progress, 10 QA, 29 Done, 1 To Do (live 2026-06-25).*
