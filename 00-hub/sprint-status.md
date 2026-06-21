# Current Sprint Context

> Update this file at the start of each sprint.
> All commands read this file — keeping it current makes every
> output accurate and specific to where you actually are.

---

## Sprint details
- **Sprint number:** **Sprint 3 closed (12 Jun). Sprint 4 active from Mon 15 Jun.**
- **Sprint 2:** closed (Sprint 34616) — 6 stories Done at close.
- **Sprint 3 dates:** 2–14 Jun 2026 (Pathfinder Sprint 3 / Sprint 34617). Final state: 23 Done, 9 in QA at close (carry-in to S4), 4 Backlog carry-in.
- **Sprint 4 dates:** 15–28 Jun 2026. Goal: complete, usable listing experience — search, filter, sort, data currency.

## Sprint goal
**Sprint 2:** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

**Sprint 3:** By end of Sprint 3, an officer can find relevant opportunities using filters and successfully initiate an application to any active OTG opportunity (except SJRs), powered by live imported data.

**Sprint 4 (agreed at planning 2026-06-11):** Deliver a complete, usable opportunity listing experience — officers can search, filter, and sort opportunities, understand what each type means, and trust that the data they're seeing is current and accurate.

**Sprint 5 (draft — gates must clear first):** By end of Sprint 5, an officer can log in with their real WOG AD credentials and view full Careers@Gov opportunity details before applying — with the CSC SSO integration scoped and started.
> *Auth "realistic landing" per the adopted plan. Conditional on 4 gates: WOG AD onboarding (#26), POCDEX (#31), competency SSOT (#18), CSC SSO ownership (#30). If WOG AD slips, S5 auth slips — goal de-scopes to "C@G detail complete + CSC SSO scoped," auth carries to S6.*

---

## Sprint 2 — CLOSED ✅ (synced 2026-06-02)

> Sprint 2 (Sprint 34616) is **closed**. 6 stories Done at close. Unfinished work (QA + In Progress + carry-overs) was pulled into Sprint 3 when it started.

**Done at close (6):** OTEP-267 (pagination), OTEP-252 (design system), OTEP-194 (FormSG spike), OTEP-193 (data model), OTEP-288 (backend stub), OTEP-296 (report format).

**Carried into Sprint 3** (not finished in S2): 11 QA items, OTEP-85/313/322 (In Progress), OTEP-128/268, OTEP-129 (open/closed story). See Sprint 3 below.

---

## Sprint 4 — ACTIVE (15–28 Jun 2026)

> Source: OTEP-Pathfinder Sprint 4 (Sprint 34618) · OTEP-Core Sprint 4 (Sprint 34608). **Live pull: 2026-06-18.** Pathfinder: 50 issues (agile endpoint). Core: sprint active 16–25 Jun.
> Goal: Deliver a complete, usable opportunity listing experience — officers can search, filter, and sort opportunities, understand what each type means, and trust that the data they're seeing is current and accurate.

**In Progress (14):** OTEP-88 (C@G listing), OTEP-482 (import C@G, Léo), OTEP-405 (keyword search), OTEP-495 (search backend, Thomas), OTEP-322 (Playwright, Rathika), OTEP-276 (design-system spike, Pow Hwee), OTEP-350 (WOG AD onboarding, Fabian), OTEP-349 (competency spike, Pow Hwee), OTEP-361 (ADR forum, Pow Hwee), OTEP-397 (OTG upload spike, Michelle), OTEP-499 (upload refactor, Hao Eng), OTEP-505 (CFT integration upload/webhook, Hao Eng), OTEP-127 (ringfencing, Michelle), OTEP-427 (ingestion logic, Michelle)

**In QA (8):** OTEP-86 (filters), OTEP-268 (empty/error states), OTEP-85 (listing cards), OTEP-305 (login/logout), OTEP-128 (detail page), OTEP-129 (open/closed before applying, Thomas), OTEP-324 (OAuth token rotation, Thomas), OTEP-438 (admin view placeholder, Hao Eng)

**Done (20):** OTEP-380, OTEP-381, OTEP-375, OTEP-374, OTEP-326, OTEP-325, OTEP-193, OTEP-288, OTEP-296, OTEP-313, OTEP-320, OTEP-170, OTEP-369, OTEP-368, OTEP-334, OTEP-327, OTEP-314, OTEP-362, OTEP-363, OTEP-367

**Backlog (23):** OTEP-87, OTEP-496, OTEP-406, OTEP-386, OTEP-439, OTEP-284, OTEP-440, OTEP-441, OTEP-283, OTEP-131, OTEP-289, OTEP-404, OTEP-328, OTEP-329, OTEP-348, OTEP-358 (Michelle), OTEP-392, OTEP-393, OTEP-403, OTEP-444, OTEP-483, OTEP-484, OTEP-485 · **To Do (1):** OTEP-445

**PM-owned In Progress:** OTEP-397 (upload spike), OTEP-127 (ringfencing display — creation/criteria stays in OTG), OTEP-427 (ingestion logic tighten) — all Michelle. ⚠️ 3 In Progress at once = WIP overload; land or park one.

**PM-owned Backlog:** OTEP-358 (nil-date spike)

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

- (2026-06-04) **Plan of record = Pow Hwee's "Planning draft for sprint 3 and after"** (Confluence, PSD-OTEP) — adopted as the team's S2–S6 shape. **Amendment:** native apply = R1, not an S4 spike (MVP apply = FormSG redirect, OTEP-319). S4 dates **15–28 Jun** (Sprint 34618, planning ceremony 14 Jun, engineers start 15 Jun). See decisions-log + [adoption reconciliation](../../PM-OS/outputs/analyses/2026-06-04-adopt-powhwee-plan-reconciliation.md).
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

*Updated: 2026-06-19 (stale-check — OTEP-127/427 Backlog→In Progress per live Jira; OTEP-505 added to In Progress; counts 11→14 IP, 25→23 Backlog. PM WIP overload flagged). Sprint 3 CLOSED 12 Jun. Sprint 4 ACTIVE 15–28 Jun. S4: 14 In Progress, 8 QA, 20 Done, 23 Backlog + 1 To Do. Prior: 2026-06-18 (S4 date residue; OTEP-499/500/502 added).*
