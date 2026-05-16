# Current Sprint Context

> Update this file at the start of each sprint.
> All commands read this file — keeping it current makes every
> output accurate and specific to where you actually are.

---

## Sprint details
- **Sprint number:** Sprint 1 (ending tomorrow)
- **Start date:** 04 May 2026
- **End date:** 15 May 2026
- **Week:** Week 2 — finalisation day tomorrow (Fri 15 May)

## Sprint goal
All auth flows working end-to-end. OTG file import delivering opportunity records to OTEP. C@G ingestion method confirmed. Amber's Hub UI and card designs finalised.

## Sprint goal status
- Auth via Keycloak: **done** (OTEP-190 completed 2026-05-15)
- OTG file import: **not started** (OTEP-192 still backlog — Sprint 2 critical blocker)
- C@G ingestion method: **resolved** (API, decided 2026-05-14)
- Amber's designs: **done** (finalised 2026-05-13 for Sprint 2 and 3)

## Committed stories
| Story ID | Title | Status | Owner |
|---|---|---|---|
| OTEP-209 | Baseline database conventions | Done | Pow Hwee |
| OTEP-171 | Frontend repo setup | Done | Thomas |
| OTEP-201 | Ref table schema migration | Done | Leo |
| OTEP-207 | Seed ref tables with POCDEX data | Done | Leo |
| OTEP-204 | Seed core entity tables | Done | Leo |
| OTEP-224 | Core entity table schema migration | Done | Leo |
| OTEP-190 | Simple auth through Keycloak | Done (15 May) | Pow Hwee / Leo |
| OTEP-173 | Exploration: auth flow and tech | Done | Pow Hwee |
| OTEP-170 | Base layout for Opportunity Listing Page | Completing today | Thomas |
| OTEP-202 | POCDEX seed database (seed data — split, see OTEP-271) | In progress | Pow Hwee |
| OTEP-271 | Local POCDEX database (container + schema — new, Leo) | Backlog | Leo |
| OTEP-183 | POCDEX profile lookup spike | Done | Pow Hwee |
| OTEP-193 | Design data model for Opportunities | Backlog | Pow Hwee |
| OTEP-192 | Design file import job for OTG data (Excel) | Backlog | Pow Hwee |
| OTEP-194 | FormSG integration discovery | Backlog | — |
| OTEP-203 | Implement standalone POCDEX API service | In progress | Pow Hwee |
| OTEP-223 | Prepare data for OTG ingestion of Oppr types | Done | Michelle |

**Summary:** 10 done, 3 in progress, 4 in backlog (17 total — reconciled against Jira board 2026-05-15). Finalisation today.

## Carry-over to Sprint 2
| Story ID | Title | Reason carried over |
|---|---|---|
| OTEP-193 | Design data model for Opportunities | **Sprint 2 blocker** — didn't start; field confirmations landed late (May 13) |
| OTEP-192 | Design file import job for OTG data | **Sprint 2 critical blocker** — didn't start; OTG file import architecture clarified May 14 |
| OTEP-202 | POCDEX seed database (seed data) | Needs splitting — Leo created OTEP-271 |
| OTEP-271 | Local POCDEX database (container) | New ticket from OTEP-202 split |
| OTEP-194 | FormSG integration discovery | Sprint 3 concern, carried forward |

## Decisions to confirm at Sprint 1 finalisation (Fri 15 May)
- [ ] Auth edge-cases: OTEP-110, WOG-04, WOG-05, WOG-06 — done as Sprint 1 carry-over, or moved to Sprint 3?
- [ ] Open item #26: Define expected auth test outcome without AzureAD (Pow Hwee / Leo)
- [x] OTEP-170 (base listing page) — Completing today

## Known constraints this sprint
- [x] ~~Rama OTG field mapping~~ — Resolved 2026-05-13. Only `formsg_url` still unconfirmed (#2).
- [x] ~~C@G ingestion method~~ — Resolved 2026-05-14: C@G = API, OTG = file import (Excel).
- [ ] ESG onboarded onto COMET for Azure AD access — unconfirmed

---

*Updated: 2026-05-15 (Jira reconciliation — OTEP-190 done, OTEP-183 done, OTEP-203 + OTEP-223 added).*

---
---

# Sprint 2 — Ready to swap in on Mon 18 May

> Copy this section to replace everything above at sprint start.

## Sprint details
- **Sprint number:** Sprint 2
- **Start date:** 18 May 2026
- **End date:** 29 May 2026
- **Week:** Week 1

## Sprint goal
By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

## Committed stories

### New stories (5 — per Jira Sprint 2 board, 2026-05-15)

| Story ID | Title | Status | Owner |
|---|---|---|---|
| OTEP-85 | Display opportunity cards with real/mock OTG data (absorbs "Closing soon" label — formerly OTEP-85a) | Not started | Thomas (FE) / Pow Hwee (BE) |
| OTEP-285 | Click-through to detail + return-to-page state | Not started | Thomas |
| OTEP-128 | View opportunity detail page | Not started | Thomas (FE) / Pow Hwee (BE) |
| OTEP-267 | Pagination for the listing page | Not started | Thomas |
| OTEP-276 | [Spike] Investigate custom design system reimplementation | Not started | Thomas |

### Carry-over from Sprint 1

| Story ID | Title | Status | Owner |
|---|---|---|---|
| OTEP-193 | Design data model for Opportunities | Not started | Pow Hwee |
| OTEP-192 | Design recurring job to fetch OTG data | Not started | Pow Hwee |
| OTEP-202 | POCDEX seed database (in progress at S1 close) | Carry-over | Pow Hwee |
| OTEP-203 | Standalone POCDEX API service (in progress at S1 close) | Carry-over | Pow Hwee |
| OTEP-271 | Local POCDEX database (container + schema) | Not started | Leo |
| OTEP-194 | FormSG integration discovery | Not started | — |

## Scope decisions
- (2026-05-14) OTEP-85 further split into OTEP-85 (base) + OTEP-85a ("Closing soon") + OTEP-285 (click-through + state)
- (2026-05-15) **OTEP-85a re-absorbed into OTEP-85** — "Closing soon" label rolled back into the card story; OTEP-85a removed.
- (2026-05-15) **OTEP-268 (empty/error/partial states) deferred** — unticketed / unplanned for Sprint 2.
- (2026-05-15) **OTEP-276 added** — design system reimplementation spike (Thomas). Confirms or replaces LifeSG as base.
- (2026-05-14) OTEP-129 absorbed into OTEP-85 (sort, interleave by date)
- (2026-05-14) Old OTEP-128 (type badge) absorbed into OTEP-85; OTEP-128 repurposed as Detail Page
- (2026-05-14) OTEP-86 (type filter) + US-05 (clear filters) deferred to Sprint 3
- Contract-first approach: Pow Hwee, Thomas, Leo aligning on API contracts Fri 15 May
- ACs written officer-perspective; implementation details in contract sync
- Cut-line: OTEP-285 first (highest risk — state architecture). Do not cut OTEP-85/128/267.

## Known constraints this sprint
- [ ] Mon 18 May PM — public holiday + Pow Hwee + Michelle out. Sprint effectively starts Tue 19.
- [ ] Thu 22 May PM — Leo out.
- [ ] Thomas is sole FE — binding constraint. All frontend stories funnel through him.
- [ ] OTEP-193 (data model) and OTEP-192 (file import) must land W1 — OTEP-85 has no data without them.
- [ ] Open item #24: which OTG Excel reports to ingest — critical path for OTEP-192. Michelle to share reports.
- [ ] Open item #23: harmonised data model must support OTG (file) now + C@G (API) later.
- [ ] Design lock date (#22) not yet set — agree with Amber in Sprint 2 W1.
- [ ] `formsg_url` (#2) still unconfirmed — Sprint 3 blocker, not Sprint 2.

## Sprint 2 DoR status
- [x] Amber's designs finalised (card, pagination, empty/error, detail page)
- [x] OTG field questions resolved (5 of 6 — only `formsg_url` open)
- [x] Sort key confirmed (`posting_date`, newest first)
- [x] Secondment classification resolved (SJR)
- [x] Opportunity lifecycle resolved (date-driven, `closing_date > today`)
- [ ] OTG file import testable with real Excel data (#24)
- [ ] Listing API contract documented (Pow Hwee — contract sync Fri 15 May)
- [ ] Detail page API contract documented (Pow Hwee — `GET /opportunities/:id`)

---

*Prepared: 2026-05-14. Swap in at Sprint 2 start (Mon 18 May).*
