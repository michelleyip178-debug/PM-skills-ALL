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

## Committed stories

### New stories (6 — per Jira Sprint 2 board, 2026-05-15)

| Story ID | Title | Status | Owner |
|---|---|---|---|
| OTEP-85 | Display opportunity cards with real/mock OTG data (absorbs "Closing soon" label — formerly OTEP-85a) | Not started | Thomas (FE) / Pow Hwee (BE) |
| OTEP-128 | View opportunity detail page | Not started | Thomas (FE) / Pow Hwee (BE) |
| OTEP-267 | Pagination for the listing page | Not started | Thomas |
| OTEP-285 | Click-through to detail + return-to-page state | Not started | Thomas |
| OTEP-276 | [Spike] Investigate custom design system reimplementation | Not started | Thomas |
| OTEP-289 | [Spike] Filter Opportunities by Functions | Not started | — |

### Carry-over from Sprint 1

| Story ID | Title | Status | Owner | Reason |
|---|---|---|---|---|
| OTEP-193 | Design data model for Opportunities | Not started | Pow Hwee | **Sprint 2 blocker** — field confirmations landed late |
| OTEP-192 | Design recurring job to fetch OTG data | Not started | Pow Hwee | **Sprint 2 critical blocker** — OTG file import architecture clarified May 14 |
| OTEP-202 | POCDEX seed database (seed data) | In progress at S1 close | Pow Hwee | Carry-over to complete |
| OTEP-203 | Standalone POCDEX API service | In progress at S1 close | Pow Hwee | Carry-over to complete |
| OTEP-271 | Local POCDEX database (container + schema) | Not started | Leo | New ticket from OTEP-202 split |
| OTEP-194 | FormSG integration discovery | Not started | — | Sprint 3 concern, carried forward |
| OTEP-110 | Login fail / clear error | Carry-over (partial S1 sign-off) | Pow Hwee / Leo | Auth edge-case unresolved at S1 finalisation |
| WOG-04 | Stay logged in during session | Carry-over (partial S1 sign-off) | Pow Hwee / Leo | Auth edge-case unresolved at S1 finalisation |
| WOG-05 | Log out of OTEP | Carry-over (partial S1 sign-off) | Pow Hwee / Leo | Auth edge-case unresolved at S1 finalisation |
| WOG-06 | First-time login experience | Carry-over (partial S1 sign-off) | Pow Hwee / Leo | Auth edge-case unresolved at S1 finalisation |

> **Sprint 1 sign-off status (2026-05-15):** Partial. Headline stories done — auth (OTEP-190), explorations, foundation. Auth edge-cases (OTEP-110, WOG-04/05/06) and open item #26 (auth test outcome without AzureAD) carry forward to Sprint 2 / Sprint 3. Confirm placement of WOG-04/05/06 at Sprint 2 mid-sprint review.

## Scope decisions
- (2026-05-15) Sprint 2 reconciled against Jira board: **6 new stories** (OTEP-289 spike added late).
- (2026-05-15) **OTEP-85a re-absorbed into OTEP-85** — "Closing soon" label rolled back into the card story.
- (2026-05-15) **OTEP-268 (empty/error/partial states) deferred** — unticketed / unplanned for Sprint 2. ACs preserved in [deferred-acs.md](../projects/otep-mvp/deferred-acs.md).
- (2026-05-15) **OTEP-276 added** — design system reimplementation spike (Thomas). Confirms or replaces LifeSG as base.
- (2026-05-14) OTEP-129 absorbed into OTEP-85 (sort, interleave by date).
- (2026-05-14) Old OTEP-128 (type badge) absorbed into OTEP-85; OTEP-128 repurposed as Detail Page.
- (2026-05-14) OTEP-86 (type filter) + US-05 (clear filters) deferred to Sprint 3.
- Contract-first approach: Pow Hwee, Thomas, Leo aligning on API contracts.
- ACs written officer-perspective; implementation details in contract sync.
- Cut-line: OTEP-285 first (highest risk — state architecture). Do not cut OTEP-85 / OTEP-128 / OTEP-267. OTEP-276 spike runs in parallel.

## Known constraints this sprint
- [ ] Mon 18 May PM — public holiday + Pow Hwee + Michelle out. Sprint effectively starts Tue 19.
- [ ] Thu 22 May PM — Leo out.
- [ ] Thomas is sole FE — binding constraint. All frontend stories funnel through him. OTEP-276 spike adds to his load alongside 4 build stories.
- [ ] OTEP-193 (data model) and OTEP-192 (file import) must land W1 — OTEP-85 has no data without them.
- [ ] Open item #24: which OTG Excel reports to ingest — critical path for OTEP-192. Michelle to share reports.
- [ ] Open item #23: harmonised data model must support OTG (file) now + C@G (API) later.
- [ ] Open item #26: auth test outcome without AzureAD — carries from Sprint 1, Pow Hwee / Leo to resolve early Sprint 2.
- [ ] Design lock date (#22) not yet set — agree with Amber in Sprint 2 W1.
- [ ] `formsg_url` (#2) still unconfirmed — Sprint 3 blocker, not Sprint 2.

## Sprint 2 DoR status
- [x] Amber's designs finalised (card, pagination, detail page)
- [x] OTG field questions resolved (5 of 6 — only `formsg_url` open)
- [x] Sort key confirmed (`posting_date`, newest first)
- [x] Secondment classification resolved (SJR)
- [x] Opportunity lifecycle resolved (date-driven, `closing_date > today`)
- [ ] OTG file import testable with real Excel data (#24)
- [ ] Listing API contract documented (Pow Hwee)
- [ ] Detail page API contract documented (Pow Hwee — `GET /opportunities/:id`)
- [ ] OTEP-276 spike AC drafted (Thomas)

---

*Updated: 2026-05-15 (Sprint 1 archived end-sprint; Sprint 2 swapped in with reconciled 5-story scope + partial S1 sign-off carry-overs).*
