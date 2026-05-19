# Sprint Allocation — The Plan

**This is the source of truth for which stories are in which sprint.** Other docs (`04-ceremonies/archive-tasks/story-readiness.md`, `04-ceremonies/sprint-checklists.md`, `04-ceremonies/sprint-calendar.md`, the story-group files in `projects/otep-mvp/stories/`) reference this — they don't restate it. Story IDs are reconciled in [story-id-map.md](../03-stories/story-id-map.md).

**Last updated:** 2026-05-18 (Sprint 2 start — Sprint 1 closed, Sprint 2 stories reconciled against live Jira board).
**Cadence:** 2-week sprints, Mon start / Fri end, from Mon 4 May 2026. Sprint 1 ran a combined Backlog-Grooming + Sprint-Planning Thursday; from Sprint 2 those split (Backlog Grooming Thu W1, Sprint Planning Thu W2). Dates + ceremonies: [04-ceremonies/sprint-calendar.md](../04-ceremonies/sprint-calendar.md).
**Feature Freeze:** end of Sprint 8 (Fri 21 Aug) — end of Phase 1, Feature Build · **Go-Live:** end of Sprint 12 (Fri 16 Oct) — end of Phase 2, Compliance & Go-Live (Sprints 9–12).

> Sprints 1–3 below are reconciled and current. Sprints 4–12 are a planning sketch — scope is provisional and story IDs aren't fully reconciled against `story-id-map.md` yet; refine at each sprint's grooming.

---

## Sprint 1 (4–15 May) — CLOSED — Login + Foundation + Discovery/Design

**Sprint goal:** Login and navigate to Jobs and Opportunities. Auth flows end-to-end; OTG → OTEP data pipeline delivering records; C@G ingestion method confirmed; Amber's Hub UI + card designs finalised.

**Final sign-off (2026-05-15): Partial.** Headline auth story done. OTEP-170 MR not merged by close. OTEP-202/203 and data model/pipeline stories carried to Sprint 2. Auth edge-cases (OTEP-110, WOG-04/05/06) not on Sprint 2 board — confirm Sprint 3 placement.

| Jira | Story | Area | Final Status |
|------|-------|------|--------|
| OTEP-209 | Baseline database conventions with team | Foundation | Done |
| OTEP-171 | Frontend repo setup | Foundation | Done |
| OTEP-201 | Create ref table schema migration for local dev | Foundation | Done |
| OTEP-207 | Seed ref tables with POCDEX data for local dev | Foundation | Done |
| OTEP-204 | Seed core entity tables for local dev | Foundation | Done |
| OTEP-224 | Create core entity table schema migration for local dev | Foundation | Done |
| OTEP-223 | Prepare data for OTG ingestion of Oppr types | Epic 4 | Done |
| OTEP-190 | Implement simple authentication through Keycloak | WOG AD | Done |
| OTEP-173 | Exploration: auth flow and tech | WOG AD | Done |
| OTEP-183 | [Spike] POCDEX profile lookup integration pattern | WOG AD | Done |
| OTEP-170 | Base layout for Opportunity Listing Page | Epic 4 | **Carried → Sprint 2** (MR not merged) |
| OTEP-202 | Create POCDEX seed database for local dev | Foundation | **Carried → Sprint 2/3** (not on Sprint 2 board) |
| OTEP-203 | Implement standalone POCDEX API service | Foundation | **Carried → Sprint 2/3** (not on Sprint 2 board) |
| OTEP-193 | Design data model for Opportunities | Epic 4 | **Carried → Sprint 2** |
| OTEP-192 | Design recurring job to fetch opportunities data | Epic 4 | **Carried → Sprint 2** |
| OTEP-194 | [Discovery/Design] FormSG integration & callback flow | Epic 4 | **Carried → Sprint 2** |
| OTEP-110 | Login fail / clear error | WOG AD | **Carried → Sprint 3** (not on Sprint 2 board) |
| WOG-04 | Stay logged in during session | WOG AD | **Carried → Sprint 3** (not on Sprint 2 board) |
| WOG-05 | Log out of OTEP | WOG AD | **Carried → Sprint 3** (not on Sprint 2 board) |
| WOG-06 | First-time login experience | WOG AD | **Carried → Sprint 3** (not on Sprint 2 board) |
| OTEP-251 | Create ER diagram for OTEP data model | — | Status unknown — confirm |

---

## Sprint 2 (18–29 May) — CURRENT — Listing → Detail End-to-End

**Sprint goal:** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

### Live Jira status (2026-05-18)

| Jira | Story | Owner | Jira Status | Notes |
|------|-------|-------|-------------|-------|
| OTEP-170 | Base Layout for Opportunity Listing Page | Thomas | **In Progress** | MR not merged from Sprint 1. Sub-tasks: OTEP-252 (Done), OTEP-288 (In Progress). |
| OTEP-252 | Setup design system in otep-web | Thomas | **Done** | Sub-task of OTEP-170. |
| OTEP-288 | Setup simple backend endpoint with in-memory list | Léo | **In Progress** | Sub-task of OTEP-170. |
| OTEP-85 | Display opportunity cards with real/mock OTG data | — | Backlog | Critical path — must ship first. 3×5 grid, 15/page. Absorbs OTEP-129 sort + "Closing soon". ⚠️ No assignee. |
| OTEP-128 | View opportunity detail page | — | Backlog | Repurposed 2026-05-14. Full detail fields, closed/not-found states. ⚠️ No assignee. |
| OTEP-267 | Pagination for listing page | — | Backlog | 15/page, page indicator. Depends on OTEP-85. ⚠️ No assignee. |
| OTEP-193 | Design Data Model for Opportunities | **Léo** | Backlog | Owner updated from Pow Hwee — confirm. Sprint 2 blocker for OTEP-85 API. |
| OTEP-192 | Design recurring job to fetch OTG data (Excel) | — | Backlog | Blocked by open item #24 (which Excel reports). ⚠️ No assignee. |
| OTEP-194 | [Discovery/Design] FormSG Integration & Callback Flow | Thomas | Backlog | Sprint 3 concern — carried for discovery. |
| OTEP-191 | Handle credential manager and vault | — | Backlog | Unexpected on board — confirm Sprint 2 scope with Pow Hwee. ⚠️ No assignee. |
| OTEP-289 | [Spike] Filter Opportunities by Functions | — | Backlog | C@G + OTG function tagging. ⚠️ No assignee. |
| **OTEP-285** | **Click-through to detail + return-to-page state** | Thomas | **⚠️ NOT IN JIRA** | Committed. Highest-risk story — state persistence architecture. Create ticket or drop from sprint. |
| **OTEP-276** | **[Spike] Custom design system reimplementation** | Thomas | **⚠️ NOT IN JIRA** | OTEP-252 (sub-task) Done. Confirm if spike is resolved or still running. |

**On Jira board but shouldn't be (cleanup needed):**
- **OTEP-268** — empty/error/partial-load states. Deferred (2026-05-15). Remove from Sprint 2 board.
- **OTEP-129** — absorbed into OTEP-85 (2026-05-14). Close or link to OTEP-85.

### Carry-overs NOT yet on Sprint 2 board (placement TBC)

| Jira | Story | Owner | Action needed |
|------|-------|-------|---------------|
| OTEP-202 | Create POCDEX seed database for local dev | Leo | Confirm Sprint 2 vs Sprint 3 (open item #27) |
| OTEP-203 | Implement standalone POCDEX API service | Pow Hwee | Confirm Sprint 2 vs Sprint 3 (open item #27) |
| OTEP-271 | Local POCDEX database (container + schema) | Leo | Confirm Sprint 2 vs Sprint 3 (open item #27) |

### Capacity

- 18 May PM — public holiday + Pow Hwee + Michelle out. Sprint effectively starts Tue 19.
- 22 May PM — Leo out
- **27 May — Hari Raya Haji public holiday.** 1 dev day lost. Sprint Planning Thu 29 May still on — confirm quorum.
- Thomas is sole FE — binding constraint across 4 build stories + OTEP-276 spike

### Deferred from Sprint 2

- ~~OTEP-85a~~ — "Closing soon" label re-absorbed into OTEP-85
- ~~OTEP-268~~ — empty/error/partial-load states deferred; ACs preserved in `deferred-acs.md`
- ~~OTEP-86~~ / ~~US-05~~ → Sprint 3 (deferred 2026-05-14)
- ~~OTEP-129~~ → absorbed into OTEP-85
- **OTEP-110, WOG-04/05/06** → Sprint 3 (auth edge-cases, not on Sprint 2 board)
- **OTEP-202, OTEP-203, OTEP-271** → Sprint 2/3 TBC (POCDEX, open item #27)

---

## Sprint 3 (1–12 Jun) — Ringfencing, Detail Page, Apply Redirects (+ auth polish if not carried)

**Sprint goal:** *(set at Sprint 2 mid-point)* — provisionally: officers see only eligible opportunities, can open a full detail page, and can route to apply.

| Jira | Story | Notes |
|------|-------|-------|
| OTEP-86 | Filter opportunities by type | **Deferred from Sprint 2 (2026-05-14)** to make room for detail page. Design finalised. ACs written + tiered. |
| US-05 | Clear filters and reset view | **Deferred from Sprint 2 (2026-05-14).** Pairs with OTEP-86. |
| OTEP-87 | Enhance detail page: apply CTA + competencies | **Builds on OTEP-128 (Sprint 2 base).** Adds: apply CTA for Internal Jobs/STIPs/Gigs, SJR no-apply treatment, competency display. Only Sprint 3 additions — base page ships in Sprint 2. |
| OTEP-127 | Apply ringfencing criteria | Show only eligible opps per POCDEX data. Depends on OTEP-183 spike. |
| US-03 | Filter opportunities by category | Pending categorisation hybrid-model validation (Amber / Adrian / Jacky / XZ). |
| US-18 | Apply via FormSG (basic redirect) | Internal Jobs / STIPs / Gigs → open `formsg_url` in new tab. Blocked on `formsg_url` confirmation (open item #2). |
| ~~US-19~~ | ~~Apply via OTG (basic redirect)~~ | **Dropped** — SJR apply deferred to future release (decision 2026-05-13). |
| OTEP-110 | Login fail / clear error | Sprint 3 or Sprint 1 carry-over (confirm at finalisation Fri 15 May). |
| — | "Closing soon" label (<=7 days to `closing_date`) | **From OTEP-129** (absorbed into OTEP-85 for default sort; "Closing soon" is the remaining independent value). Needs Amber design. |
| WOG-04, WOG-05, WOG-06 | Auth edge-cases (session, logout, first-time login) | Only if not finished as Sprint 1 carry-over. |
| [TBD] | Search (keyword) | **Missing Story** — Needs to be explicitly written before Sprint 3 grooming. Confirmed MVP requirement but currently has no ACs. |

**This is a heavy sprint as drawn** (ringfencing + detail page + 1 apply flow + auth polish + maybe search + "Closing soon"). Lighter than originally planned now that US-19 is dropped. Expect to push some to Sprint 4 at planning.

---

## Sprint 4 (15–26 Jun) — Full Apply Flow (FormSG webhook + confirmation) — *provisional*

| Jira | Story | Notes |
|------|-------|-------|
| OTEP-130 | Apply to OTG opportunity via FormSG (full) | Webhook confirmation, email notifications. Depends on FormSG webhook integration. |
| US-10 | Receive application confirmation | Depends on FormSG webhook + email delivery service. |
| — | Handle missing/broken FormSG link | Disabled CTA + "contact Agency POC" fallback (US-12 fallback state — see MVP guardrails). |

---

## Sprint 5 (29 Jun – 10 Jul) — Careers@Gov Integration + EDM — *provisional*

| Jira | Story | Notes |
|------|-------|-------|
| US-10 *(C@G label — distinct from the confirmation story above; ID to reconcile)* | Identify Careers@Gov listings | "Careers@Gov" label on card. Depends on C@G ingestion being live. |
| OTEP-89 | View Careers@Gov opportunity summary on OTEP | C@G detail in OTEP, "Apply via Careers@Gov" CTA, deep-link to C@G. |
| OTEP-133 | Redirect to Careers@Gov to apply / access hub via EDM deep link | Email → opportunity detail; ineligible shows a message. |
| OTEP-88 | Understand the difference between OTG and C@G flows | Button labels, visual cues. |

---

## Sprint 6 (13–24 Jul) — Admin Login + Instrumentation + Polish — *provisional*

| Jira | Story | Notes |
|------|-------|-------|
| WOG-02 | Log in as agency admin | Deferred from earlier. |
| WOG-07 | Role-based access control | 2 roles: officer, admin. |
| — | Instrumentation: all success metrics tracked | oppr_list_view, oppr_detail_view, search_performed, filter_applied, click_to_formsg, click_to_OTG, click_to_C@G. |
| — | Bug fixes + polish from Sprints 2–5 | Address mid-sprint review issues. |

---

## Sprint 7 (27 Jul – 7 Aug) — E2E Testing / Stabilisation

No new stories. Full-flow testing (login → listing → search/filter → detail → apply, all 3 channels), cross-browser, performance (< 5 s on gov network), edge-case fixes. Feature Freeze is the *end of Sprint 8* (Fri 21 Aug).

## Sprint 8 (10–21 Aug) — UAT + ⭐ Feature Freeze

UAT with 1–2 agencies (higher posting volume, willing HR partner), satisfaction target ≥ 3.5/5, bug triage (fix vs defer to R1). **Feature Freeze: Fri 21 Aug** — end of Phase 1. *(National Day observed Mon 10 Aug — sprint start + Sprint 7 retro/demo shift to Tue 11 Aug.)*

## Sprints 9–12 (24 Aug – 16 Oct) — Phase 2: Compliance & Go-Live

No new development. Security review, pen testing, compliance sign-off, go-live readiness, then launch. (Security review runs on a monthly cycle — submit early Sep.) Bi-weekly Steering check-ins with Mark & GK; final sign-off Fri 9 Oct.

- **Sprint 9** (24 Aug – 4 Sep) — security review kicks off; Steering check-in 4 Sep
- **Sprint 10** (7–18 Sep) — pen testing, compliance progressing
- **Sprint 11** (21 Sep – 2 Oct) — sign-offs; Steering check-in 2 Oct
- **Sprint 12** (5–16 Oct) — final pre-launch review; **🚀 GO-LIVE Fri 16 Oct**

---

## Deferred to R1

| Item | Reason |
|------|--------|
| Agency, grade, commitment filters | Brief explicit: type filter only for MVP |
| Persist filter selections across sessions (US-07) | Within-session via URL params is enough for MVP |
| Function/Job-function taxonomy mapping | Hybrid model adopted; contextual mapping is R1 (decision 2026-05-06) |
| Autocomplete / suggested search | Brief: not MVP |
| Competency match ratio / scoring | High cost, low proven value (decision 2026-05-08) |
| Auto-populate OTG form fields from POCDEX | Keep FormSG as-is for MVP |
| Competency proficiency levels | Binary only for MVP |
| "Save for later" | Low priority vs core apply flow |
| Supervisor endorsement workflow | UI copy only for MVP, no backend |
| Custom questions on FormSG | MVP keeps current forms unchanged |
| Rich onboarding tutorial | Minimal sufficient |
| Granular roles beyond officer/admin | 2-role model sufficient |
| Recommendation / AI matching | Out of MVP entirely |

---

## Success Metrics (from the Epic 4 one-pager)

**Outcome (North Star):** Application Completion Rate (forms submitted ÷ Apply clicks × 100); channel migration ≥ 50% of STIP/Gig applications via OTEP by Month 3.
**Input:** click-through rate (listing → detail), apply-click rate (detail → form), form field drop-off rate.
**Guardrails:** submission error rate (pause & investigate if it spikes); confirmation-email delivery rate (escalate to Infra).

---

## Key Dependencies

| Dependency | Owner | Status | Blocks |
|-----------|-------|--------|--------|
| WOG AD / Keycloak integration | Pow Hwee + Leo | **Done** — OTEP-190 closed Sprint 1. Auth edge-cases (OTEP-110, WOG-04–06) not on Sprint 2 board; Sprint 3. | Sprint 3 polish |
| OTG data import (Excel file-based, not API) — schema/fields confirmed | Rama / Pow Hwee | 5 of 6 fields resolved (2026-05-13). Only `formsg_url` still unconfirmed (open item #2). OTG = file import; C@G = API (decided 2026-05-14). | Listing (Sprint 2), Apply (Sprint 3) |
| POCDEX profile lookup | Eng (spike Sprint 1, OTEP-183) | Discovery | Ringfencing (Sprint 3) |
| Careers@Gov API integration | Pow Hwee | **Confirmed: API** (open item #11 resolved 2026-05-14) | C@G work (Sprint 5) |
| FormSG webhook integration | Eng (discovery Sprint 1, OTEP-194) | Design | Full apply flow (Sprint 4) |
| Email delivery service | Infra (Fabian?) | Unknown (open item #15) | Confirmation emails, EDM deep-links |

---

*Living doc — update after each grooming / planning session. When a story moves sprints, change it here first, then sync `story-id-map.md`'s Sprint column.*
