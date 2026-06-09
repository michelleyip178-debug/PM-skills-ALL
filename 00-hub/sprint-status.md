# Current Sprint Context

> Update this file at the start of each sprint.
> All commands read this file — keeping it current makes every
> output accurate and specific to where you actually are.

---

## Sprint details
- **Sprint number:** **Sprint 3 active** (started 2 Jun). **Sprint 2 closed** — unfinished work carried into Sprint 3.
- **Sprint 2:** closed (Sprint 34616) — 6 stories Done at close.
- **Sprint 3 dates:** 2–14 Jun 2026 (Pathfinder Sprint 3 / Sprint 34617). 49 issues (carry-overs + new scope).
- **Note:** Design lock = Wed 3 Jun (passed). Mid-sprint review = Mon 8 Jun.

## Sprint goal
**Sprint 2:** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

**Sprint 3:** By end of Sprint 3, an officer can find relevant opportunities using filters and successfully initiate an application to any active OTG opportunity (except SJRs), powered by live imported data.

**Sprint 4 (proposed — confirm at grooming):** By end of Sprint 4, an officer sees both OTG and Careers@Gov opportunities in one listing, can tell which is which, and reaches the right way to apply for each — FormSG for OTG, a deep-link out to Careers@Gov.
> *Breadth-led: C@G is the new capability and is hittable. OTG apply loop = the floor it sits on. Auth ("if WOG AD clean") and FormSG Phase 2 (OTEP-130) stay out of the goal — stretch, not the promise. Fallback goal if OTG apply (319) carries as real work: "OTG discovery-to-apply verified Done + C@G appears in listing with a working apply path."*

**Sprint 5 (draft — gates must clear first):** By end of Sprint 5, an officer can log in with their real WOG AD credentials and view full Careers@Gov opportunity details before applying — with the CSC SSO integration scoped and started.
> *Auth "realistic landing" per the adopted plan. Conditional on 4 gates: WOG AD onboarding (#26), POCDEX (#31), competency SSOT (#18), CSC SSO ownership (#30). If WOG AD slips, S5 auth slips — goal de-scopes to "C@G detail complete + CSC SSO scoped," auth carries to S6.*

---

## Sprint 2 — CLOSED ✅ (synced 2026-06-02)

> Sprint 2 (Sprint 34616) is **closed**. 6 stories Done at close. Unfinished work (QA + In Progress + carry-overs) was pulled into Sprint 3 when it started.

**Done at close (6):** OTEP-267 (pagination), OTEP-252 (design system), OTEP-194 (FormSG spike), OTEP-193 (data model), OTEP-288 (backend stub), OTEP-296 (report format).

**Carried into Sprint 3** (not finished in S2): 11 QA items, OTEP-85/313/322 (In Progress), OTEP-128/268, OTEP-129 (open/closed story). See Sprint 3 below.

---

## Sprint 3 — ACTIVE (started 2 Jun 2026, with carry-overs)

> Source: OTEP-Pathfinder Sprint 3 (Sprint 34617), **state = active**. Live pull 2026-06-09 (jira-sync). **50 issues** total. 6 Done, 8 In Progress, 13 QA, 23 Backlog.
> **OTEP-Core Sprint 3** (Sprint 34607) also active: **96 issues** — 32 Done, 9 In Progress, 28 QA, 26 Backlog, 1 To Do. (Live 2026-06-08.)

### Carried over from Sprint 2 (finish these first)

**In QA (13)** — closest to done:
OTEP-128 (detail page), OTEP-170 (base layout), OTEP-268 (empty/error states), OTEP-314 (detail consuming response), OTEP-320 (real DB endpoint), OTEP-324 (token rotation, Thomas), OTEP-325/326 (empty/error UI), OTEP-327 (detail w/ design system), OTEP-332 (shared ref data), OTEP-334 (backend detail endpoint), OTEP-369 (custom login page, Thomas), OTEP-380 (BE filtering params, Léo).

**In Progress (8):** OTEP-85 (cards w/ real OTG data, unassigned), OTEP-192 (recurring OTG ingestion job, Léo), OTEP-276 (design-system spike, Pow Hwee), OTEP-322 (Playwright E2E, Rathika), OTEP-362 (BE no closed opps, Thomas), OTEP-368 (session expiry redirect, Thomas), OTEP-381 (FE filtering params, Thomas — moved In Progress 2026-06-09), OTEP-391 (virus scanning spike, Hao Eng — moved In Progress 2026-06-09). Note: Thomas has 3 active items (362, 368, 381) — capacity risk for filters closing this sprint.

**Backlog carry:** OTEP-129 (open/closed before applying, Thomas) — now **split into OTEP-362 (In Progress) + OTEP-363**.

**Done (6):** OTEP-193 (data model, Léo), OTEP-288 (backend stub, Léo), OTEP-296 (report format, Michelle), OTEP-303 (POCDEX field check, Pow Hwee — Done 2026-06-09), OTEP-313 (OTG raw ingest, Léo), OTEP-397 (UI for OTG excel file upload — new story added 2026-06-09).

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
- (2026-06-04) **Plan of record = Pow Hwee's "Planning draft for sprint 3 and after"** (Confluence, PSD-OTEP) — adopted as the team's S2–S6 shape. **Amendment:** native apply = R1, not an S4 spike (MVP apply = FormSG redirect, OTEP-319). S4 dates corrected to **14–28 Jun** (Sprint 34618). See decisions-log + [adoption reconciliation](../../PM-OS/outputs/analyses/2026-06-04-adopt-powhwee-plan-reconciliation.md).
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

*Updated: 2026-06-08 (jira-sync). **Sprint 2 CLOSED; Sprint 3 ACTIVE.***

*Key changes this sync (2026-06-08): Pathfinder +1 issue (OTEP-391 added, Hao Eng, Backlog); total 48→49. Core: OTEP-211/308/366 Done (was QA/In Progress); 28 S2 tickets relocated to S3 folder; 5 stub files created (OTEP-339/365/384/385/389). OTEP-370 flagged — not in Jira (no access/deleted).*
