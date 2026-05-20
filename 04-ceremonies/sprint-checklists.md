# Sprint Checklists

Per-story grooming readiness and DoR blockers, per sprint. **Which stories are in which sprint comes from [sprint-allocation.md](../sprint-allocation.md)** — this file tracks readiness, not assignment. Updated each sprint.

**Cut ACs (should-have, good-to-have, R1) live in [deferred-acs.md](deferred-acs.md).** Pull from there at grooming when capacity allows.

---

## Sprint 2 — Opportunities Listing Hub

**Sprint dates:** 18 May – 29 May 2026
**Sprint goal:** An officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

### Stories (reconciled against Jira Sprint 2 board 2026-05-20)

| ID | Title | Story file | Status | Grooming-ready? |
|---|---|---|---|---|
| OTEP-85 | Display opportunity cards with real OTG data | [filters.md](stories/filters.md) | Backlog | AC updated: visibility = `closing_date > today` (open item #28 resolved). "Closing soon" badge moved to OTEP-129. |
| OTEP-128 | View opportunity detail page | [otg-lifecycle.md](stories/otg-lifecycle.md) | Backlog | Absorbs OTEP-285 ACs (click-through + return-to-page). Remove "opportunity is closed" AC — belongs to OTEP-129. |
| OTEP-129 | See whether opportunity is open/closed before applying | [otg-lifecycle.md](stories/otg-lifecycle.md) | Backlog | Re-added as separate story (Pow Hwee, 2026-05-18). Owns: "Closing soon" badge (≤7 days) + deep-link error state. |
| OTEP-267 | Pagination for listing page | [filters.md](stories/filters.md) | Backlog | API dep: `total_count` needed in GET /opportunities response. |
| OTEP-268 | Empty, error, and partial-load states for listing | — | Backlog | Re-added (Pow Hwee, 2026-05-18). Drop partial-load AC (not possible with single API fetch). |
| OTEP-289 | [Spike] Filter Opportunities by Functions | [OTEP-289-spike-definition.md](stories/OTEP-289-spike-definition.md) | Backlog | Spike defined: 2-day timebox (19–20 May), output = written recommendation + go/no-go. |
| OTEP-170 | Base Layout for Opportunity Listing Page | — | In Progress | Thomas. MR in progress. Sub-task of OTEP-85. |
| OTEP-193 | Design Data Model for Opportunities | — | In Progress | Léo. .sql migration + Go structs. Must support OTG now, C@G later (open item #23). |
| OTEP-288 | Setup simple backend endpoint with in-memory list | — | In Progress | Léo. Sub-task of OTEP-85. Léo has WIP risk (2 In Progress). |
| OTEP-296 | Prepare defined report format matching data model | — | In Progress | Michelle. Standardises OTG Excel format before ingestion. Must align with OTEP-193. |
| OTEP-194 | [Spike] FormSG Integration & Callback Flow | — | Backlog | Thomas. Sprint 2 carry-over. |
| OTEP-295 | Mock detail endpoint for opportunity | — | Backlog | Léo. GET /v1/opportunities/:id — sub-task of OTEP-128. |
| OTEP-252 | Setup design system in otep-web | — | Done | Thomas. Flagship/LifeSG confirmed. |
| ~~OTEP-276~~ | ~~[Spike] Custom design system reimplementation~~ | — | Resolved | Spike complete — OTEP-252 Done confirms Flagship/LifeSG. Remove from board. |

**Scope notes (2026-05-20):**
- ~~OTEP-285~~ absorbed into OTEP-128 (Pow Hwee, 2026-05-18) — no Sprint 3 ticket needed
- ~~OTEP-191~~ removed from Sprint 2 board — deprioritised to Sprint 3+ (Pow Hwee, 2026-05-14)
- OTEP-192 (recurring OTG import job) moved to Sprint 3 (2026-05-19 decision)
- Cut-line: do not cut OTEP-85 or OTEP-128 — they are the end-to-end goal

### DoR Blockers (Sprint 2)

- [x] ~~Amber's designs finalised (card, pagination, detail page)~~ — resolved 2026-05-13
- [x] ~~`closing_date` confirmed~~ — resolved 2026-05-13: application closing date
- [x] ~~`is_published` confirmed~~ — resolved 2026-05-13: field doesn't exist; use `closing_date > today`
- [x] ~~Secondment classification~~ — resolved 2026-05-13: subsumed under SJR
- [x] ~~Sort key confirmed~~ — `posting_date`, newest first (Michelle)
- [x] ~~OTEP-85 visibility rule~~ — resolved 2026-05-19: `closing_date > today` (open item #28)
- [x] ~~OTEP-289 spike defined~~ — resolved 2026-05-19: 2-day timebox, written output (open item #29)
- [ ] Listing API contract documented (Pow Hwee) — OTEP-85 internal API (frontend ↔ backend)
- [ ] Detail page API contract documented (Pow Hwee) — GET /opportunities/:id
- [ ] Harmonised data model supports OTG + C@G (open item #23) — Léo building OTEP-193 now; alignment needed
- [ ] Design lock date agreed with Amber (open item #22) — overdue, Sprint 2 W1

---

## Sprint 3 — Auth + OTG Ingestion

**Sprint dates:** 2 Jun – 13 Jun 2026
**Sprint goal:** *(Proposed: Officer can log in via WOG AD, stay authenticated, and log out securely — auth end-to-end. OTG recurring job delivers data in background. Confirm at grooming 2026-05-21.)*
**Scope (updated 2026-05-20 Jira sync):** 5–6 stories. Original scope locked at 3 (OTEP-192, OTEP-71, OTEP-110); OTEP-304 and OTEP-305 confirmed on Jira Sprint 3 board (pulled forward from Sprint 4+, confirmed as WOG-04/05). OTEP-191 also on board — verify if still needed.

### Stories (confirmed on Jira Sprint 3 board — 2026-05-20)

| ID | Title | Story file | Status | Grooming-ready? |
|---|---|---|---|---|
| OTEP-71 | Log in with WOG AD credentials | [auth.md](stories/auth.md) | Backlog | ⚠️ Jira ACs weak — auth.md is complete. Agency determination (decision #2) unresolved. |
| OTEP-110 | Login fail / clear error | [auth.md](stories/auth.md) | Backlog | ❌ Jira AC is 1 mechanism sentence. Paste auth.md ACs to Jira before grooming. Needs compliance sign-off (WOG-15 NFR). |
| OTEP-192 | Design recurring job to fetch OTG data | — | Backlog | ❌ No user story format; mechanism AC only. Rewrite before grooming. Trigger/frequency TBD. |
| OTEP-304 | Remain authenticated during active session | — | Backlog | ⚠️ ACs present; timeout value TBD (compliance). Was WOG-04. |
| OTEP-305 | Log out of OTEP | — | Backlog | ⚠️ ACs present; concurrent-session default unresolved. Was WOG-05. |
| OTEP-191 | Handle credential manager and vault | — | Backlog | ❌ No description or ACs. Pow Hwee flagged: may be resolved by AWS infra — verify at grooming. |

**Deferred to Sprint 4+:** OTEP-86, US-05, US-03, OTEP-87, US-18, OTEP-127, WOG-06, OTEP-202, OTEP-203, OTEP-271.

### DoR Blockers (Sprint 3)

- [ ] Auth test outcome without AzureAD defined (open item #26) — Pow Hwee / Leo. Overdue.
- [ ] Agency determination source for OTEP-71 (decision #2) — Pow Hwee. Raise at grooming.
- [ ] OTEP-110 ACs pasted from auth.md into Jira **before grooming (21 May)**
- [ ] OTEP-110 error copy compliance sign-off (WOG-15 non-enumeration NFR) — Michelle to route
- [ ] OTEP-192 rewritten as user story with job trigger/frequency confirmed — Pow Hwee
- [ ] Concurrent session default decided (OTEP-305 / decision #4) — policy call, not a build item
- [ ] Idle timeout value confirmed (OTEP-304 / decision #1) — compliance / Pow Hwee
- [ ] OTEP-191 verified or closed — Pow Hwee (AWS infra may have resolved)
- [ ] Amber: design login error states (OTEP-110), logout (OTEP-305), session expiry (OTEP-304)
- [ ] Sprint 3 goal confirmed in Jira

---

## Sprint 4 — Application Routes End-to-End

**Sprint dates:** 16 Jun – 27 Jun 2026
**Sprint goal:** *(TBD)*

### Stories (provisional from story-id-map)

| ID | Title | Story file | Grooming-ready? |
|---|---|---|---|
| OTEP-130 | Apply to OTG opportunity via FormSG (full) | [otg-lifecycle.md](stories/otg-lifecycle.md) | Draft |
| US-10 | Receive application confirmation | [otg-lifecycle.md](stories/otg-lifecycle.md) | Draft |

### DoR Blockers

*(To be populated during Sprint 3)*

---

## Sprint 5 — C@G Handoff, Integration Testing, Polish

**Sprint dates:** 30 Jun – 11 Jul 2026
**Sprint goal:** *(TBD)*

### Stories (provisional from story-id-map)

| ID | Title | Story file | Grooming-ready? |
|---|---|---|---|
| OTEP-89 | View C@G opportunity summary | [cag-handoff.md](stories/cag-handoff.md) | Draft |
| OTEP-133 | Redirect to Careers@Gov to apply | [cag-handoff.md](stories/cag-handoff.md) | Draft |
| OTEP-88 | Understand OTG vs C@G flow difference | [cag-handoff.md](stories/cag-handoff.md) | Draft |

### DoR Blockers

*(To be populated during Sprint 4)*

---

*Updated: 2026-05-13*
