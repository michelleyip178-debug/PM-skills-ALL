# Current Sprint Context

> Update this file at the start of each sprint.
> All commands read this file — keeping it current makes every
> output accurate and specific to where you actually are.

> ⚠️ **STALE (flagged by /sprint-pulse, 2026-07-01):** everything below is frozen at the 2026-06-02 sync and still says "Sprint 3 active." Per `04-ceremonies/sprint-calendar.md`, **Sprint 5 (Mon 29 Jun – Fri 10 Jul) is actually active — today is Day 3.** Sprint 4 (15–26 Jun) ran and closed with no record here. Run `/jira-sync` to refresh before trusting anything below.

---

## Sprint details
- **Sprint number:** **Sprint 3 active** (started 2 Jun). **Sprint 2 closed** — unfinished work carried into Sprint 3.
- **Sprint 2:** closed (Sprint 34616) — 6 stories Done at close.
- **Sprint 3 dates:** 2–12 Jun 2026 (Pathfinder Sprint 3 / Sprint 34617). 39 issues (carry-overs + new scope).
- **Note:** Design lock = Wed 3 Jun. Mid-sprint review = Mon 8 Jun.

## Sprint goal
**Sprint 2:** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

**Sprint 3:** By end of Sprint 3, an officer can find relevant opportunities using filters and successfully initiate an application to any active OTG opportunity (except SJRs), powered by live imported data.

---

## Sprint 2 — CLOSED ✅ (synced 2026-06-02)

> Sprint 2 (Sprint 34616) is **closed**. 6 stories Done at close. Unfinished work (QA + In Progress + carry-overs) was pulled into Sprint 3 when it started.

**Done at close (6):** OTEP-267 (pagination), OTEP-252 (design system), OTEP-194 (FormSG spike), OTEP-193 (data model), OTEP-288 (backend stub), OTEP-296 (report format).

**Carried into Sprint 3** (not finished in S2): 11 QA items, OTEP-85/313/322 (In Progress), OTEP-128/268, OTEP-129 (open/closed story). See Sprint 3 below.

---

## Sprint 3 — ACTIVE (started 2 Jun 2026, with carry-overs)

> Source: OTEP-Pathfinder Sprint 3 (Sprint 34617), **state = active**. Live pull 2026-06-02. **39 issues** total (carry-overs from S2 + new S3 scope). 4 Done, 3 In Progress, 11 QA, 21 Backlog.

### Carried over from Sprint 2 (finish these first)

**In QA (11)** — closest to done:
OTEP-170 (base layout), OTEP-128 (detail page), OTEP-268 (empty/error states), OTEP-314 (detail consuming response), OTEP-320 (real DB endpoint), OTEP-325/326 (empty/error UI), OTEP-327 (detail w/ design system), OTEP-332 (shared ref data), OTEP-334 (backend detail endpoint), OTEP-303 (POCDEX field check).

**In Progress (3):** OTEP-85 (cards w/ real OTG data), OTEP-313 (OTG raw ingest, Léo), OTEP-322 (Playwright E2E, Rathika).

**Backlog carry:** OTEP-129 (open/closed before applying, Thomas) — now **split into OTEP-362 + OTEP-363** (see new tickets).

**Done (4):** OTEP-191 (credential vault), plus OTEP-193/288/296 (carried from S2 as done).

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
| OTEP-192 | Recurring OTG data ingestion job | — | Critical path — no live data without it |
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
- [ ] OTEP-87 vs OTEP-319 scope split — align PM afternoon, confirm Wed grooming
- [ ] OTEP-358 (Michelle, nil-date spike) — scope + timebox
- [ ] OTEP-361 (Pow Hwee, ADR forum) — confirm timing + PM involvement
- [x] ~~Confirm OTEP-305 Sprint 3 vs 4+~~ — resolved: in Sprint 3, build via Keycloak (D 2026-06-02)
- [x] ~~OTEP-129 placement~~ — resolved: on Sprint 3 board, split into OTEP-362/363

---

*Updated: 2026-06-02 (PM) — live Jira sync. **Sprint 2 CLOSED; Sprint 3 ACTIVE** (39 issues = carry-overs + new scope).*
*Key changes this sync: S2 closed with 6 Done; 11 QA + 3 In Progress + OTEP-129 carried into S3. OTEP-129 split → OTEP-362 (backend) + OTEP-363 (UI). OTEP-305 confirmed in S3 (build via Keycloak now).*
