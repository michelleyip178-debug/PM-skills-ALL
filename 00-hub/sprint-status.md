# Current Sprint Context

> Update this file at the start of each sprint.
> All commands read this file — keeping it current makes every
> output accurate and specific to where you actually are.

---

## Sprint details
- **Sprint number:** Sprint 2
- **Start date:** 18 May 2026
- **End date:** 29 May 2026
- **Week:** Week 1
- **Note:** 18 May PM public holiday + Pow Hwee + Michelle out. Sprint effectively starts Tue 19.

## Sprint goal
By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

> ✓ **Sprint goal set in Jira** (as of 2026-05-20).

## Committed stories

### New stories — Jira status as of 2026-05-18 (comment sync)

| Story ID | Title | Jira Status | Owner | Notes |
|---|---|---|---|---|
| OTEP-85 | Display opportunity cards with real/mock OTG data | Backlog | — | ⚠️ Visibility rule conflict — PM to confirm (see open item #28) |
| OTEP-128 | View opportunity detail page | Backlog | — | OTEP-285 ACs absorbed here (Pow Hwee, 2026-05-18). Remove overlapping "closed" AC — owned by OTEP-129. |
| OTEP-267 | Pagination for the listing page | Backlog | — | API contract dep: GET /opportunities needs total_count in response |
| OTEP-289 | [Spike] Filter Opportunities by Functions | Backlog | — | ⚠️ No ACs, no timebox — PM action needed (see open item #29) |

**Resolved / dropped:**
- ~~OTEP-285~~ — **absorbed into OTEP-128** (Pow Hwee, 2026-05-18). Click-through + return-to-page ACs folded in. No Sprint 3 ticket needed.
- ~~OTEP-276~~ — **resolved** by OTEP-252 Done. Flagship/LifeSG adopted per 2026-05-13 decision.

### In Sprint 2 on Jira

| Story ID | Title | Jira Status | Owner | Notes |
|---|---|---|---|---|
| OTEP-129 | See whether opportunity is open/closed before applying | Backlog | — | **Re-added as separate Sprint 2 story** (Pow Hwee, 2026-05-18). Overrides May 14 absorption into OTEP-85. Owns: "Closing soon" badge + deep-link behaviour only. |
| OTEP-268 | Empty, error, and partial-load states for listing | Backlog | — | **Re-added to Sprint 2** (Pow Hwee, 2026-05-18). Overrides May 15 deferral. AC feedback: drop partial-load AC; good-to-haves as separate tickets. |
| OTEP-170 | Base Layout for Opportunity Listing Page | **In Progress** | Thomas | MR in progress |
| OTEP-191 | Handle credential manager and vault | Backlog | — | ⚠️ **Deprioritised to Sprint 3+** (Pow Hwee, 2026-05-14). Removed from sprint board as of 2026-05-20. |
| OTEP-288 | Setup a simple backend endpoint with in-memory list | **In Progress** | Léo | Sub-task of OTEP-170 |
| OTEP-252 | Setup design system in otep-web | **Done** | Thomas | Sub-task of OTEP-170. Flagship/LifeSG confirmed. |
| OTEP-296 | Prepare defined report format that matches data model | **In Progress** | Michelle | Sub-task. Standardises OTG Excel report format before ingestion. Added to sprint 2026-05-20. |
| OTEP-295 | Mock detail endpoint for opportunity | Backlog | Léo | Sub-task of OTEP-128. GET /v1/opportunities/:id returns single opportunity with full detail fields + 404 for invalid IDs. Added to sprint 2026-05-20. |

### Carry-over from Sprint 1 — staying in Sprint 2

| Story ID | Title | Jira Status | Owner | Notes |
|---|---|---|---|---|
| OTEP-193 | Design data model for Opportunities | Backlog | **Léo** ⚠️ | Local context said Pow Hwee — confirm owner |
| OTEP-194 | FormSG integration discovery | Backlog | **Thomas** | Owner updated from "—" |

### Sprint 3 — reallocated (updated 2026-05-21)

> Sprint 3 dates: **1 Jun – 15 Jun**. Auth epic (OTEP-71, OTEP-110, OTEP-304, OTEP-305) moved to Sprint 4+ — no WOG AD UAT environment available (open item #26, raised at grooming 2026-05-21). Sprint 3 reallocated to filter + enhanced detail work building on Sprint 2 delivery.

| Story ID | Title | Owner | Notes |
|---|---|---|---|
| OTEP-192 | Design recurring job to fetch OTG data | — | Moved from Sprint 2. Critical path — listing has no live data without it. |
| OTEP-271 | Local POCDEX database (container + schema) | Leo | Backend plumbing — committed 2026-05-20. Unblocks Sprint 4 ringfencing (OTEP-127). |
| OTEP-203 | Standalone POCDEX API service | Pow Hwee | Backend plumbing — committed 2026-05-20. |
| OTEP-86 | Filter by opportunity type | — | Builds on Sprint 2 listing page. Moved from Sprint 4+. |
| US-05 | Clear filters and reset view | — | Pairs with OTEP-86. Moved from Sprint 4+. |
| US-03 | Filter by category | — | ⚠️ Conditional: proceed only if OTEP-289 spike output is green. Defer if taxonomy mapping is messy. |
| OTEP-87 | Enhanced detail page — apply CTA only | — | Builds on Sprint 2 OTEP-128. Scoped to apply CTA only — competency section deferred pending open item #18. |
| US-18 | Apply via FormSG (basic redirect) | — | ⚠️ Conditional on `formsg_url` confirmation (open item #2). Pull in if #2 resolves before Sprint 3 start. |

### Unscheduled — Sprint 4+ (updated 2026-05-21)

| Story ID | Title | Notes |
|---|---|---|
| OTEP-71 | Login Authentication using WOG AD | ⚠️ Moved from Sprint 3 (2026-05-21) — no WOG AD UAT environment. Escalate via Adrian before scheduling. |
| OTEP-110 | Login fail using WOG AD | ⚠️ Moved from Sprint 3 (2026-05-21) — same blocker as OTEP-71. ACs being rewritten. |
| OTEP-304 | Logged-in officer remains authenticated | ⚠️ Moved from Sprint 3 (2026-05-21) — was WOG-04. |
| OTEP-305 | Log out of OTEP | ⚠️ Moved from Sprint 3 (2026-05-21) — was WOG-05. |
| WOG-06 | First-time login experience | Mandatory fields TBD + POCDEX dep |
| OTEP-202 | POCDEX seed database | Sprint placement TBD |
| OTEP-191 | Credential manager and vault | Sprint placement TBD — possibly resolved by AWS infra setup; verify before scheduling |
| OTEP-87 | Enhanced detail page — competency section | Deferred from OTEP-87 Sprint 3 scope (apply CTA only in Sprint 3). Pending open item #18. |

> **Sprint 1 sign-off status (2026-05-15):** Partial. Headline stories done — auth (OTEP-190), explorations, foundation. Auth edge-cases (OTEP-110, WOG-04/05/06) moved to Sprint 3 (2026-05-19).

## Scope decisions
- (2026-05-21) **Auth epic deferred to Sprint 4+:** OTEP-71, OTEP-110, OTEP-304, OTEP-305 moved out of Sprint 3 — no WOG AD UAT environment, can't validate against real auth before go-live (open item #26). Sprint 3 reallocated to filter work (OTEP-86, US-05, US-03 conditional) and enhanced detail page (OTEP-87, apply CTA only). Escalation to Adrian required before auth is rescheduled. Owner: Michelle. **Overrides 2026-05-19 decision.**
- ~~(2026-05-19) Sprint 3 locked to 3 stories: OTEP-192, OTEP-71, OTEP-110~~ — *reversed 2026-05-21: auth deferred, Sprint 3 reallocated.*
- (2026-05-18) **OTEP-285 ACs absorbed into OTEP-128** (Pow Hwee) — click-through + return-to-page state folded into the detail page story. No Sprint 3 ticket needed. Overrides earlier deferral decision.
- (2026-05-18) **OTEP-129 re-added to Sprint 2 as separate story** (Pow Hwee) — owns "Closing soon" badge + deep-link error state. Overrides May 14 absorption into OTEP-85. Business rule split: OTEP-85 = visibility filter (closing_date > now); OTEP-129 = label + deep-link behaviour.
- (2026-05-18) **OTEP-268 re-added to Sprint 2** (Pow Hwee) — overrides May 15 deferral. AC feedback: drop partial-load AC (not possible with single API fetch); move good-to-haves to separate backlog tickets.
- (2026-05-18) **OTEP-191 deprioritised to Sprint 3+** (Pow Hwee) — possibly resolved by AWS infra setup; verify at grooming.
- (2026-05-18) **OTEP-276 resolved** — OTEP-252 Done confirms Flagship/LifeSG adopted. Spike complete.
- ~~(2026-05-18) OTEP-285 deferred to Sprint 3~~ — *reversed 2026-05-18: absorbed into OTEP-128 instead.*
- (2026-05-15) Sprint 2 reconciled against Jira board: **6 new stories** (OTEP-289 spike added late).
- (2026-05-15) **OTEP-85a re-absorbed into OTEP-85** — "Closing soon" label rolled back into the card story.
- ~~(2026-05-15) OTEP-268 deferred~~ — *reversed 2026-05-18: re-added by Pow Hwee.*
- ~~(2026-05-14) OTEP-129 absorbed into OTEP-85~~ — *reversed 2026-05-18: re-added by Pow Hwee as separate story.*
- (2026-05-14) Old OTEP-128 (type badge) absorbed into OTEP-85; OTEP-128 repurposed as Detail Page.
- (2026-05-14) OTEP-86 (type filter) + US-05 (clear filters) deferred to Sprint 3.
- Contract-first approach: Pow Hwee, Thomas, Leo aligning on API contracts.
- ACs written officer-perspective; implementation details in contract sync.
- Cut-line: do not cut OTEP-85 or OTEP-128 — they are the end-to-end goal.

## Known constraints this sprint
- [ ] Mon 18 May PM — public holiday + Pow Hwee + Michelle out. Sprint effectively starts Tue 19.
- [ ] Thu 22 May PM — Leo out.
- [ ] Thomas is sole FE — binding constraint. All frontend stories funnel through him. OTEP-276 spike removed 2026-05-18, freeing some headroom.
- [ ] OTEP-193 (data model) and OTEP-192 (file import) must land W1 — OTEP-85 has no data without them.
- [ ] Open item #24: which OTG Excel reports to ingest — critical path for OTEP-192. Michelle to share reports.
- [ ] Open item #23: harmonised data model must support OTG (file) now + C@G (API) later.
- [ ] Open item #26: auth test outcome without AzureAD — carries from Sprint 1, Pow Hwee / Leo to resolve early Sprint 2.
- [ ] Design lock date (#22) not yet set — agree with Amber in Sprint 2 W1.
- [ ] `formsg_url` (#2) still unconfirmed — Sprint 3 blocker, not Sprint 2.

## Jira board cleanup needed (updated 2026-05-21)

**Sprint 2 board:**
- [x] ~~Remove OTEP-191~~ — confirmed off board as of 2026-05-20
- [ ] **Remove OTEP-276** from Sprint 2 board — resolved spike; still showing in Backlog
- [x] **Paste sprint goal into Jira** — set in Jira (2026-05-20)
- [x] ~~Remove OTEP-268~~ — **overridden: Pow Hwee re-added to Sprint 2 (2026-05-18)**
- [x] ~~Close or link OTEP-129~~ — **overridden: Pow Hwee re-added as separate Sprint 2 story (2026-05-18)**
- [x] ~~Confirm OTEP-285~~ — **resolved: absorbed into OTEP-128 (Pow Hwee, 2026-05-18)**
- [x] ~~Confirm OTEP-276~~ — **resolved: OTEP-252 Done confirms Flagship adopted**

**Sprint 3 board (add):**
- [ ] **Add OTEP-192** — recurring OTG job (moved from Sprint 2)
- [x] ~~Confirm OTEP-202, OTEP-203, OTEP-271 placement~~ — **resolved 2026-05-20: OTEP-271 + OTEP-203 → Sprint 3 (Leo + Pow Hwee)**
- [ ] **Add OTEP-271** — local POCDEX database → assign Leo
- [ ] **Add OTEP-203** — standalone POCDEX API service → assign Pow Hwee
- [ ] **Add OTEP-86** — filter by opportunity type (moved from Sprint 4+, 2026-05-21)
- [ ] **Add US-05** — clear filters (moved from Sprint 4+, 2026-05-21)
- [ ] **Add US-03** — filter by category (conditional on OTEP-289 spike output)
- [ ] **Add OTEP-87** — enhanced detail page, apply CTA only (moved from Sprint 4+, 2026-05-21)

**Sprint 4+ board (move from Sprint 3):**
- [ ] **Move OTEP-71** — Login Authentication using WOG AD → Sprint 4+
- [ ] **Move OTEP-110** — Login fail using WOG AD → Sprint 4+
- [ ] **Move OTEP-304** — Stay logged in during session → Sprint 4+
- [ ] **Move OTEP-305** — Log out of OTEP → Sprint 4+

## Sprint 2 DoR status
- [x] Amber's designs finalised (card, pagination, detail page)
- [x] OTG field questions resolved (5 of 6 — only `formsg_url` open)
- [x] Sort key confirmed (`posting_date`, newest first)
- [x] Secondment classification resolved (SJR)
- [x] Opportunity lifecycle resolved (date-driven, `closing_date > today`)
- [ ] OTG file import testable with real Excel data (#24)
- [ ] Listing API contract documented (Pow Hwee)
- [ ] Detail page API contract documented (Pow Hwee — `GET /opportunities/:id`)
- [x] ~~OTEP-276 spike AC drafted (Thomas)~~ — *N/A, spike dropped 2026-05-18.*

---

*Updated: 2026-05-21 (Sprint 3 reallocation — auth epic OTEP-71/110/304/305 moved to Sprint 4+ due to no WOG AD UAT environment (open item #26). Sprint 3 replaced with filter work OTEP-86/US-05/US-03 and enhanced detail page OTEP-87. OTEP-271/203/US-18 confirmed in Sprint 3 per 2026-05-20 decision.)*
