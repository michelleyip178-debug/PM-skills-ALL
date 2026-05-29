# Current Sprint Context

> Update this file at the start of each sprint.
> All commands read this file — keeping it current makes every
> output accurate and specific to where you actually are.

---

## Sprint details
- **Sprint number:** Sprint 2 (closing) → Sprint 3 starts 2 Jun
- **Sprint 2 end date:** 31 May 2026 (Pathfinder) / 1 Jun 2026 (Core) — per Jira
- **Sprint 3 dates:** 2–12 Jun 2026 (Pathfinder Sprint 3 / Sprint 34617)
- **Note:** Sprint 2 is last day today (29 May). Sprint Review + Retro today. Tue 3 Jun = Vesak Day (public holiday). Sprint 3 engineering effectively starts Mon 2 Jun.

## Sprint goal
**Sprint 2:** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

**Sprint 3:** By end of Sprint 3, an officer can find relevant opportunities using filters and successfully initiate an application to any active OTG opportunity (except SJRs), powered by live imported data.

---

## Sprint 2 — Live Jira Status (synced 2026-05-29)

> Source: Jira OTEP-Pathfinder Sprint 2 (Board 12541, Sprint 34616). Live API pull.

### Parent stories

| Story | Title | Jira Status | Notes |
|-------|-------|-------------|-------|
| OTEP-85 | Display opportunity cards with real OTG data | **In Progress** | Sub-tasks progressing — see below |
| OTEP-128 | View opportunity detail page | **In Progress** | Sub-tasks in QA — see below |
| OTEP-268 | Empty, error, and partial-load states for listing | **In Progress** | Sub-tasks (OTEP-325/326) in QA |
| OTEP-267 | Pagination for the listing page | **In Progress** | Thomas |
| OTEP-129 | See whether opportunity is open/closed before applying | **Backlog** | Thomas — likely Sprint 3 carry |

### Sub-tasks — Completed ✅

| Ticket | Title | Assignee |
|--------|-------|----------|
| OTEP-193 | Design Data Model for Opportunities | Léo Milbor |
| OTEP-288 | Setup simple backend endpoint with in-memory list | Léo Milbor |
| OTEP-296 | Prepare defined report format that matches data model | Michelle Yip |
| OTEP-252 | Setup design system in otep-web | Thomas Huchedé |
| OTEP-194 | [Spike] FormSG Integration & Callback Flow | Thomas Huchedé |

### Sub-tasks — In QA

| Ticket | Title | Assignee | Notes |
|--------|-------|----------|-------|
| OTEP-170 | Base Layout for Opportunity Listing Page | Thomas Huchedé | Rathika flagged: not QA-ready until deployment flow is live |
| OTEP-314 | Opportunity detail page consuming OTEP-295 response shape | Thomas Huchedé | |
| OTEP-320 | Replace mock /opportunities endpoint with real DB access | Léo Milbor | |
| OTEP-325 | Create empty state for opportunity listing | Thomas Huchedé | |
| OTEP-326 | Create error state for opportunity listing | Thomas Huchedé | |
| OTEP-303 | POCDEX field check | Pow Hwee | |
| OTEP-332 | Shared reference data repository for cross-domain table lookups | Pow Hwee | |
| OTEP-334 | Backend endpoint for opportunity detail | Léo Milbor | |

### Sub-tasks — In Progress

| Ticket | Title | Assignee |
|--------|-------|----------|
| OTEP-313 | OTG raw ingest table and source model | Léo Milbor |
| OTEP-327 | Opportunity detail page using design system | Thomas Huchedé |
| OTEP-322 | Setup Playwright E2E Testing Framework | Rathika Ramalingam |
| OTEP-267 | Pagination for listing page | Thomas Huchedé |

### Still Backlog (likely carry to Sprint 3 or dropped)

| Ticket | Title | Notes |
|--------|-------|-------|
| OTEP-289 | [Spike] Filter Opportunities by Functions | Not started — gates OTEP-318 go/no-go decision |
| OTEP-316 | Replace mock detail endpoint with real DB query | Superseded by OTEP-320? Clarify with Pow Hwee |
| OTEP-276 | [Spike] Investigate custom design system reimplementation | Likely dropped — OTEP-252 Done resolves |

---

## Sprint 3 — Planned (starts 2 Jun 2026)

> Source: OTEP-Pathfinder Sprint 3 (Sprint 34617). All issues currently in Backlog — sprint not yet started.

### Confirmed in Jira Sprint 3

| Ticket | Title | Assignee | Notes |
|--------|-------|----------|-------|
| OTEP-86 | Filter opportunities by type (Internal Jobs, STIPs, Gigs) | Unassigned | |
| OTEP-317 | Clear filters and reset view | Unassigned | Pairs with OTEP-86 |
| OTEP-87 | View Careers@Gov Opportunity Detail | Unassigned | ⚠️ Jira title differs from our docs (was "Enhanced detail — apply CTA only") — reconcile before grooming |
| OTEP-88 | Identify Careers@Gov listings | Unassigned | |
| OTEP-89 | View Careers@Gov Job (Deep-Link) | Unassigned | |
| OTEP-319 | Apply via FormSG — basic redirect (Internal Jobs, STIPs, Gigs) | Unassigned | `formsg_url` confirmed ✅ |
| OTEP-305 | Login and Logout (replace keycloak page with actual) | Unassigned | ⚠️ Was deferred to Sprint 4+ in our docs — back in Sprint 3 per Jira |
| OTEP-192 | Recurring OTG data ingestion job | Unassigned | Critical path — listing has no live data without it |
| OTEP-324 | Implement OAuth 2.0 Refresh Token Rotation (NextAuth + Keycloak) | Thomas Huchedé | New — not in our prior planning docs |
| OTEP-348 | OTG data ingestion — scheduler & observability | Unassigned | New |
| OTEP-349 | [Spike] Competency matching integration with OTEP-Core squad | Unassigned | New — cross-squad dependency |
| OTEP-350 | Onboard WOG AD | Fabian Peh | New — WOG AD onboarding story; aligns with open item #26 |
| OTEP-351 | [Spike] Azure AD mock solution for testing (no WOG AD test env) | Unassigned | New — unblocks auth testing without prod WOG AD |
| OTEP-352 | Load POCDEX production code table | Pow Hwee | New |
| OTEP-191 | Handle credential manager and vault | — | **Done** ✅ — resolved by AWS infra |

### In our docs but NOT in Jira Sprint 3 (⚠️ discrepancy)

| Ticket | Title | Notes |
|--------|-------|-------|
| OTEP-271 | Local POCDEX database (container + schema) | In OTEP-Pathfinder-Sprint-3 folder but not in Jira Sprint 3 board — confirm placement |
| OTEP-203 | Standalone POCDEX API service | Same — folder exists but not on board |
| OTEP-318 | Filter by category (conditional on OTEP-289 spike) | Not in Jira Sprint 3 — OTEP-289 spike still Backlog, so correctly excluded |

---

## Design lock + key Sprint 3 constraints

- **Design lock:** Wednesday 3 June — engineers must not start UI until Amber signs off final Figma
- **Vesak Day:** Tuesday 2 June — public holiday; no standup
- **Mid-sprint review:** Monday 8 June (pulse check, not formal ceremony) — ✅ invite sent
- **Thomas:** sole FE engineer; design lock is the single biggest risk for his first week
- **OTEP-289 spike still Backlog:** OTEP-318 (filter by category) can't be confirmed until spike completes. Get outcome at today's Sprint Review.

---

## Scope decisions
- (2026-05-29) **OTG sync cadence: one-time port only** — no ongoing automated sync. Pilot agencies driven to adopt Compass directly. See D-016. Resolves open question from Sprint 3 Planning.
- (2026-05-28) **Design lock: Wednesday 3 June** (D-013)
- (2026-05-28) **OTG competency migration: file ingestion, not live API** (D-010) — Fanxu owns Sprint 3 one-time bulk import
- (2026-05-21) **Auth epic deferred to Sprint 4+** — OTEP-71, OTEP-110, OTEP-304 deferred; no WOG AD UAT env (open item #26). ⚠️ OTEP-305 has reappeared in Jira Sprint 3 — confirm with Pow Hwee.
- (2026-05-21) **OTEP-271/203 confirmed in Sprint 3** — but not yet on Jira Sprint 3 board; reconcile.

---

## Jira board actions still needed

- [ ] Confirm OTEP-316 disposition — is it superseded by OTEP-320 or still open?
- [ ] Confirm OTEP-271 + OTEP-203 — add to Jira Sprint 3 board if still committed
- [ ] Confirm OTEP-305 — intended for Sprint 3 or Sprint 4+? Appeared in Sprint 3 board
- [ ] OTEP-289 spike output — go/no-go for OTEP-318 (get at Sprint Review today)
- [ ] OTEP-87 title/scope — Jira title says "View Careers@Gov Opportunity Detail", our docs say "Enhanced detail — apply CTA only". Reconcile before Sprint 3 grooming.

---

*Updated: 2026-05-29 — live Jira sync (Pathfinder Sprint 2 Board 12541 / Sprint 34616, Pathfinder Sprint 3 Sprint 34617). Jira auth: michelle_yip@psd.gov.sg.*
