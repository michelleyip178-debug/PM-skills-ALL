# Sprint Allocation — The Plan

**This is the source of truth for which stories are in which sprint.** Other docs (`04-ceremonies/archive-tasks/story-readiness.md`, `04-ceremonies/sprint-checklists.md`, `04-ceremonies/sprint-calendar.md`, the story-group files in `projects/otep-mvp/stories/`) reference this — they don't restate it. Story IDs are reconciled in [story-id-map.md](../03-stories/story-id-map.md).

> **Plan of record (2026-06-04):** the team adopted **Pow Hwee's "Planning draft for sprint 3 and after"** (Confluence, PSD-OTEP) as the S2–S6 shape. This file stays the working ticket-level allocation; where they diverge, his page wins on shape and this file wins on live ticket placement. One amendment: native apply = R1 (not an S4 spike). See [adoption reconciliation](../../PM-OS/outputs/archive/2026-W23-Jun01-Jun07/analyses/2026-06-04-W23-adopt-powhwee-plan-reconciliation.md).

**Last updated:** 2026-07-07 (jira-sync — Pathfinder Sprint 6 live pull refreshed, 8→10 issues; OTEP-611 dropped, replaced by OTEP-613/614/615; created local cache files for all 10 tickets in new `Sprint-34620-OTEP-Pathfinder-Sprint-6` folder (5 moved from `Backlog/`, 5 newly created); discrepancy against the provisional plan and against the 2026-07-07 sprint-plan-brief both flagged for reconciliation at planning). Prior: 2026-07-06 (jira-sync — Pathfinder Sprint 5 live pull refreshed, 76→81 issues; OTEP-304/305 status re-confirmed unchanged; full field-level diff in `00-hub/sprint-status.md`, not restated here since this file's Sprint 5 section is a provisional-plan diff, not a status mirror). Prior: 2026-07-02 (jira-sync — added live Jira Sprint 6 placement (8 issues, all Backlog/ungroomed) alongside the existing provisional plan; flagged discrepancy between the two for grooming). Prior: 2026-07-02 (jira-sync — Pathfinder Sprint 5 cache cleanup: removed stale duplicate folder `OTEP-Pathfinder-12541-Sprint-5-34619` (11 partial, outdated files); canonical folder `Sprint-34619-OTEP-Pathfinder-Sprint-5` verified 75/75 against live Jira with zero field drift, all files stamped. Live pull confirms 75 issues, up from 74 on 2026-07-01). Prior: 2026-07-01 (jira-sync full sweep — Sprint 5 owner/status columns refreshed against live Jira (Sprint 34619, 74 issues); OTEP-71/110/127/89 flagged as stale placement, WOG-06/US-10 flagged as invalid Jira keys). Prior: 2026-06-04 (adopted Pow Hwee's Confluence plan as S2–S6 plan-of-record; S4 dates corrected 16–27 → 14–28; native-apply spike dropped → R1). Prior: 2026-06-03 (Sprints 2–3 reconciled to live Jira post-rollover — both S2 closed, both S3 active; Pathfinder S3 = 49 issues, Core S3 = 92).

**Prior:** 2026-05-21 (Sprint 3 reallocation — auth deferred; Sprint 4 restructured with contingency-first stream; **working assumption = auth lands Sprint 5** — WOG AD is a formal process, min 2 wks + back and forth; Sprint 5 carries auth realistic + C@G; Sprint 6 carries CSC SSO realistic + admin).

**Cadence:** 2-week sprints, Mon start / Fri end, from Mon 4 May 2026. Sprint 1 ran a combined Backlog-Grooming + Sprint-Planning Thursday; from Sprint 2 those split (Backlog Grooming Thu W1, Sprint Planning Thu W2). Dates + ceremonies: [04-ceremonies/sprint-calendar.md](../04-ceremonies/sprint-calendar.md).

**Feature Freeze:** end of Sprint 8 (Fri 21 Aug) — end of Phase 1, Feature Build · **Go-Live:** end of Sprint 12 (Fri 16 Oct) — end of Phase 2, Compliance & Go-Live (Sprints 9–12).

> Sprints 1–3 are reconciled and current. Sprints 4–12 are a planning sketch — scope is provisional and story IDs aren't fully reconciled against `story-id-map.md` yet; refine at each sprint's grooming.
>
> **Layout:** active + upcoming sprints lead. **Closed sprints (1 & 2) are at the bottom** under "Closed Sprints — historical record."

---

## Sprint 3 (2–14 Jun) — ACTIVE (Day 2) — Filters + Apply Flow + OTG Ingestion (live data)

**Sprint goal:** By end of Sprint 3, an officer can find relevant opportunities using filters and successfully initiate an application to any active OTG opportunity (except SJRs), powered by live imported data.

**Live pull 2026-06-05** (Sprint 34617, state=active). **49 issues:** 4 Done, 7 In Progress, 12 QA, 26 Backlog. Both Sprint 2 boards closed 2026-06-02; unfinished QA + In-Progress work bulk-carried here. **Design lock:** Wed 3 Jun (passed). **Mid-sprint review:** Mon 8 Jun.

**New scope since 05-21 plan:** OTEP-129 split into **OTEP-362 (BE, In Progress) + OTEP-363 (UI)**; C@G stories OTEP-87/88/89 + 374–379 landed; login/logout OTEP-305/368/369/370; spikes OTEP-349/351/358; filtering split OTEP-380 (BE) / OTEP-381 (FE).

### New S3 scope — the sprint-goal spine

| Jira | Story | Owner | Status (live 06-03) | Notes |
|------|-------|-------|---------------------|-------|
| OTEP-85 | Display opportunity cards with real OTG data | — | **In Progress** | Critical path. ⚠️ Still no assignee. |
| OTEP-192 | Recurring OTG data ingestion job (Excel) | — | Backlog | Critical path — listing has no live data without it. ⚠️ Unassigned. |
| OTEP-86 | Filter opportunities by type | — | Backlog | Builds on S2 listing. ⚠️ Unassigned. |
| OTEP-317 | Clear filters and reset view *(was US-05)* | — | Backlog | Pairs with OTEP-86. ⚠️ Unassigned. |
| OTEP-380 | [BE] Handle filtering params | Léo | **In Progress** | Backend half of category/type filtering. |
| OTEP-381 | [FE] Handle filtering params | Thomas | Backlog | Frontend half. |
| OTEP-319 | Apply via FormSG — basic redirect *(was US-18)* | — | Backlog | ✅ `formsg_url` confirmed. ⚠️ Unassigned. |
| OTEP-87 | View Careers@Gov opportunity detail | — | Backlog | Includes competency section (scope firm). Open dependency is **data**: whether each C@G opp carries competencies depends on ingestion landing first. Unassigned. |
| OTEP-362 | Update backend to not return closed opportunities | Thomas | **In Progress** | Split from OTEP-129. |
| OTEP-363 | UI component to display closed opportunity | — | Backlog | Split from OTEP-129. ⚠️ Unassigned. |

### Carried over from Sprint 2 (finish first)

| Jira | Story | Owner | Status (live 06-03) |
|------|-------|-------|---------------------|
| OTEP-128 | View opportunity detail page | — | QA |
| OTEP-170 | Base layout for listing page | Thomas | QA |
| OTEP-268 | Empty/error/partial-load states | — | QA |
| OTEP-314 | Detail page consuming response | Thomas | QA |
| OTEP-320 | Replace mock endpoint with real DB | Léo | QA |
| OTEP-324 | OAuth refresh token rotation | Thomas | QA |
| OTEP-325 / 326 | Empty / error state UI | Thomas | QA |
| OTEP-327 | Detail page using design system | Thomas | QA |
| OTEP-332 | Shared reference data repository | Pow Hwee | QA |
| OTEP-334 | Backend detail endpoint | Léo | QA |
| OTEP-303 | POCDEX field check | Pow Hwee | QA |
| OTEP-322 | Playwright E2E framework | Rathika | In Progress |
| OTEP-276 | [Spike] design system reimplementation | Pow Hwee | In Progress |
| OTEP-129 | See open/closed before applying | Thomas | Backlog (parent of 362/363) |

> **Moved off the live S3 board (were assumed here in the 05-21 plan):** OTEP-271, OTEP-203 (POCDEX plumbing — now under the POCDEX Integration epic), OTEP-318 (category filter — not ticketed on board), OTEP-191 (credential mgr — closed). Verify placement before relying on this.

**DoR blockers / open at Day 2:**
- [ ] OTEP-289 spike output reviewed — go/no-go for category filtering
- [x] `formsg_url` confirmed (open item #2 resolved 2026-05-21) — OTEP-319 unblocked
- [ ] Open item #18 (competency data source) checked — **BO Working Level 2 Jun surfaced no SSOT for competencies; consumer-vs-system-of-record fork still open.** OTEP-87's competency section is *in scope*; what's unconfirmed is whether each C@G opp will have competency data (depends on ingestion landing first).
- [x] Core S3 stories on board — confirmed live (49 Pathfinder issues now on the active board)
- [ ] **Owner assignment gap** — OTEP-85, 86, 192, 317, 319, 87, 363 all still **Unassigned** on the live board. Assign at grooming.
- [ ] Open item #26 escalated to Adrian before auth is rescheduled (WOG AD onboarding)
- [ ] OTEP-92 ("Tracking" subtask of OTEP-86) — no story file; confirm purpose and whether it needs ACs

---

## Sprint 4 (14–28 Jun) — Finish the S3 spine + C@G + Auth if WOG AD clean — *provisional, re-based 2026-06-03*

> **📌 Plan of record (2026-06-04): Pow Hwee's "Planning draft for sprint 3 and after"** (Confluence, PSD-OTEP) is now the team's S2–S6 source of truth. This file's streams already align with it; reconcile against the page when they diverge. **One amendment (Michelle, 2026-06-04):** native apply = R1, not an S4 spike — MVP apply stays the FormSG redirect (OTEP-319). See [adoption reconciliation](../../PM-OS/outputs/archive/2026-W23-Jun01-Jun07/analyses/2026-06-04-W23-adopt-powhwee-plan-reconciliation.md). *Pow Hwee's page is pre-26-May in spots (dates, CareerCompass name, C@G deep-link, R1 creation) — flagged for his refresh.*
>
> **Dates corrected 2026-06-04:** S4 = **14–28 Jun** per live Jira (Sprint 34618), was 16–27.
>
> **Re-based 2026-06-03 against live S3.** Sprint 4 is no longer a clean "new C@G + auth" sprint. Sprint 3 carries 45 open issues on Day 2 with **one FE dev (Thomas) and ~20 FE stories** — the apply/filter spine and the entire C@G UI stream will mostly carry into S4. Plan S4 as *finish-the-spine first*, new work second. Full reasoning: [Sprint 3 FE capacity + S4 impact analysis](../../PM-OS/outputs/archive/2026-W23-Jun01-Jun07/analyses/2026-06-03-W23-sprint3-fe-capacity-and-sprint4-impact.md).
>
> **🟢 Capacity boost in S4: a second full-stack dev joins** (productive day 1, even FE/BE split) → ~1.5 FE-equivalent + extra BE. This makes S4 the *catch-up* sprint that can absorb the S3 carry-over AND start some new work. Sprint 3 itself gets no relief — the catch-up only starts 16 Jun.
>
> **Auth note:** WOG AD onboarding (OTEP-350, Fabian) + login/logout UI (OTEP-305/368/369/370) already landed in **Sprint 3**, so the auth clock started earlier than the 05-21 plan assumed. **Correction (trio 2026-06-03):** OTEP-350 *has* an owner (Fabian) but zero movement — it's not an ownership gap, it's that the onboarding steps aren't mapped yet (open-item #26). The real unblock is a Michelle→Fabian session to map the process, not an eng assignment. Hold auth at Sprint 5 as the working assumption regardless.

**Stream 0 — Carry-over from S3 (plan for these FIRST — they're the realistic intake):**

| Jira | Story | Owner | Notes |
|------|-------|-------|-------|
| OTEP-319 | Apply via FormSG — basic redirect | — | The other half of the S3 goal. Likely slips if S3 FE does filters first. **Recommend apply-first in S3 to avoid this.** |
| OTEP-88/89 | C@G listing / deep-link | — | C@G UI stream — was "new" in the 05-21 plan, but already groomed into S3. Will mostly carry. |
| OTEP-87 (core) | C@G opportunity detail — non-competency fields | — | **SPLIT (trio 2026-06-03):** build the detail page from the fields C@G already provides. In scope for S4. |
| OTEP-87 (competency block) | Competency section on C@G detail | — | **CUT from S4 (trio 2026-06-03):** no data SSOT yet (open-item #18), no schema = unbuildable, designing against placeholder = guaranteed re-design. Defer until Imelda's squad confirms schema + mapping. |
| OTEP-374–379 | C@G API + payload + UI mapping + tests | — | Backend + FE for C@G. Carries from S3. |
| OTEP-305, 368, 369, 370 | Login/logout UI, session redirect | — | Auth UI carried from S3. FE-bound (Thomas). |
| OTEP-348 | OTG ingestion — scheduler & observability | — | Ingestion polish; carries if OTEP-192 lands late. |

**Stream A — New, WOG AD-independent (only if S3 spine actually lands):**

| Jira | Story | Owner | Notes |
|------|-------|-------|-------|
| ~~OTEP-130~~ | ~~Apply to OTG opportunity via FormSG (full)~~ | — | **REMOVED from S4 (2026-06-10). Moved back to Backlog — pending BO alignment. Decision 2026-06-10.** |
| OTEP-202 | Create POCDEX seed database for local dev | Leo | Seeds test profiles for ringfencing validation. |
| — | Instrumentation: success metrics tracked | — | oppr_list_view, detail_view, filter_applied, click_to_formsg. |
| ~~Native apply spike~~ | ~~[Spike] Native apply in OTEP~~ | — | **DROPPED from S4 (Michelle, 2026-06-04).** Pow Hwee's draft proposed it; native apply moves to R1 (ATS pivot, D 2026-06-02). MVP apply = FormSG redirect (319). |

**Stream B — WOG AD-dependent — DEMOTED out of S4 grooming (trio 2026-06-03). Carry as a watch-item; S5 is the working assumption.**

> **Why demoted:** OTEP-350 (WOG AD onboarding) has an owner (Fabian) but zero movement — and it *can't* move until the onboarding steps are mapped (open-item #26), so it's structurally stuck, not just unstarted. POCDEX plumbing (OTEP-271/203) is off the S3 board, OTEP-127 has no contract, and OTEP-110's error spec is contradicted (open-item #32). Don't groom these into S4. Re-evaluate at S4 mid-sprint once #26 + #31 have moved.

| Jira | Story | Owner | Gate before it can be groomed |
|------|-------|-------|-------|
| OTEP-71 | Log in with WOG AD credentials | Pow Hwee | OTEP-350 onboarding steps mapped (#26) |
| OTEP-110 | Login fail / clear error | Thomas | #32 (AC vs design spec mismatch) resolved first |
| OTEP-127 | Apply ringfencing criteria | Thomas / Leo | WOG AD + POCDEX 271/203 confirmed done (#31) + a written ringfencing contract |
| WOG-06 | First-time login experience | Thomas | POCDEX + WOG AD both cleared |

> **FE constraint eases in S4 (second full-stack dev), but doesn't vanish.** ~1.5 FE-equivalent against a backlog this deep is still tight, and at an even split FE only gets ~0.5 of the new dev. Consider weighting the new dev toward FE for their first sprint or two to clear the carry-over faster. The R1 ask to Adrian/Michelle Chen now targets *sustained* FE capacity for the net-new R1 builds (native apply + creation + the seam), not plugging this S3/S4 hole.

---

## Sprint 5 (29 Jun – 12 Jul) — Auth (realistic) + C@G detail + CSC SSO process — *provisional*

> **Realistic scenario: WOG AD completes ~19 Jun (3 weeks from late-May approval, with some back and forth). Auth stories start Sprint 5.**
> **Live pull 2026-07-06** (Sprint 34619, state=active, 81 issues — up from 76 on 2026-07-03; direct Jira REST API, MCP unavailable this session). OTEP-304 still In Progress, OTEP-305 still QA — both re-confirmed, no change. Full field-level diff for this sprint is in `00-hub/sprint-status.md`. Several rows in this provisional plan do not match live placement — see notes per row. ⚠️ **Flagged, not rewritten:** whether to keep/reallocate these rows is a scope call, not a field sync.

**Stream A — Auth (realistic landing):**

| Jira | Story | Owner | Notes |
|------|-------|-------|-------|
| OTEP-71 | Log in with WOG AD credentials | — (unassigned) | ⚠️ **Still in Backlog per live Jira, NOT in Sprint 5.** Plan assumed it would move here; it hasn't. |
| OTEP-110 | Login fail / clear error | — (unassigned) | ⚠️ **Still in Backlog per live Jira, NOT in Sprint 5.** Same as above. |
| OTEP-304 | Stay logged in during session | Hao Eng | Confirmed in Sprint 5, **In Progress** (live pull 2026-07-01). |
| OTEP-305 | Log out of OTEP | — (unassigned) | Confirmed in Sprint 5, **QA** (live pull 2026-07-01). |
| OTEP-127 | Apply ringfencing criteria | Michelle Yip | ⚠️ **Already Done — closed in Sprint 4 (34618), not landing in Sprint 5.** Plan is stale on this row. |
| WOG-06 | First-time login experience | Thomas | ⚠️ **Not a valid Jira key** — no such issue found in OTEP project. Flag for cleanup or correction to real key. |

**Stream B — C@G (depends on S04 ingestion):**

| Jira | Story | Owner | Notes |
|------|-------|-------|-------|
| OTEP-89 | View Careers@Gov opportunity summary on OTEP | Thomas Huchedé | ⚠️ **Already Done — closed in Sprint 3 (34617), not landing in Sprint 5.** Plan is stale on this row. |
| US-10 | Receive application confirmation | Thomas | ⚠️ **Not a valid Jira key** — no such issue found in OTEP project. Flag for cleanup or correction to real key. |

**CSC SSO track (external, running in parallel):**
- Documents sent to CSC ~end Sprint 4 (best case) / ~end Sprint 5 (realistic)
- CSC 4-week clock: SSO ready ~end Sprint 5 (best) / ~end Sprint 6 (realistic)
- CSC SSO integration story (Story B from dependency map) — **placeholder story needed in Jira**

---

## Sprint 6 (13–24 Jul) — CSC SSO + C@G deep-links + Admin — *provisional*

> **Realistic: CSC SSO external process completes ~17 Jul. Integration work lands here.**

| Jira | Story | Owner | Notes |
|------|-------|-------|-------|
| Story B | CSC SSO integration | Michelle (owner) | ⚠️ No story in Jira yet. Scope TBC with Imelda. Realistic landing sprint. |
| OTEP-133 | Redirect to Careers@Gov / EDM deep-link | Leo | Email → opportunity detail. Needs OTEP-127 (ringfencing) done. Moved from S05. |
| WOG-02 | Log in as agency admin | — | |
| WOG-07 | Role-based access control | — | 2 roles: officer, admin. |
| — | Bug fixes + polish from Sprints 2–5 | — | Address mid-sprint review issues. |

**Live Jira placement (pulled 2026-07-07, sprint 34620):** Jira board 12541 has 10 issues sitting in Sprint 6 (future, not started 12–26 Jul), all Backlog status / unassigned / unpointed:

| Jira | Story | Notes |
|------|-------|-------|
| OTEP-71 | Login Authentication Successful | |
| OTEP-110 | Login fail using WOG AD | |
| OTEP-111 | Officers with no access (unauthorised page - display only) | |
| OTEP-594 | Officer is routed to the correct page after WOG AD authentication | Description flags open decisions #7/#8/#9 and an unconfirmed 2-day POCDEX sync assumption — not fully resolved. |
| OTEP-331 | WOG AD - SSO integration with CSC | Matches "Story B" above conceptually — may be the actual Jira-side placeholder for CSC SSO. |
| OTEP-130 | Apply for a STIP or Gig via FormSG link | |
| OTEP-613 | [FE] Opportunities with no agency logo — default logo fallback | New since 2026-07-02 pull. Not in the provisional plan above. |
| OTEP-614 | [SPIKE] Discovery — advanced filters/search (competency, job function) | New since 2026-07-02 pull. Not in the provisional plan above. |
| OTEP-615 | [SPIKE] Suggested search after 3 characters in opportunity listing | New since 2026-07-02 pull. Not in the provisional plan above. |
| OTEP-425 | [SPIKE] Discovery — bookmark opportunities | Was already in Sprint 6 on 2026-07-02 pull. |

**Changed since 2026-07-02 pull:** OTEP-611 ([SPIKE] Bookmark of opportunities, sub-task) no longer appears in the sprint — replaced by OTEP-613/614/615 as the new discovery-spike set. Total moved 8 → 10.

⚠️ **Discrepancy, not yet reconciled:** the live Jira set (WOG AD login-flow tickets + 3 discovery spikes + a small FE fix) still doesn't match this section's provisional plan (OTEP-133, WOG-02, WOG-07 — none of which appear in the live pull). Only OTEP-331 lines up with "Story B." All 10 are still ungroomed (Backlog, unpointed) — confirm at Sprint 6 planning (9 Jul) whether this is early auto-placement to reconcile against, or whether the provisional plan above needs rewriting to match where WOG AD/login work and the discovery spikes actually landed in Jira. The Sprint 6 sprint-plan-brief drafted 2026-07-07 (`PM-OS/outputs/analyses/2026-07-07-W28-sprint-plan-brief.md`) was built from Sprint 5's leftover Backlog candidates and does **not** yet reflect this live-Jira set — reconcile the two before presenting at planning.

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
| ~~Function/Job-function taxonomy mapping~~ | ~~Hybrid model adopted; contextual mapping is R1 (decision 2026-05-06)~~ **SUPERSEDED 2026-06-16 — job family filter pulled into MVP. See decisions-log.md 2026-06-16.** |
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
| WOG AD / Keycloak integration | Pow Hwee + Leo | **Partial** — OTEP-190 (Keycloak stub) done Sprint 1. Auth stories moved to Sprint 4+ (2026-05-21). **Working assumption (2026-05-21): auth lands Sprint 5.** WOG AD is a formal onboarding process — min 2 weeks from Adrian's approval, longer with back and forth. Best case (clean run + Adrian this week) = auth Sprint 4. Realistic = auth Sprint 5. Escalation: Michelle → Adrian (#26). | Sprint 4 (best case) / Sprint 5 (working assumption) |
| OTG data import (Excel file-based, not API) — schema/fields confirmed | Rama / Pow Hwee | All 6 fields resolved: 5 on 2026-05-13, `formsg_url` confirmed 2026-05-21 (SJRs excluded — no apply flow in MVP). OTG = file import; C@G = API (decided 2026-05-14). | Listing (Sprint 2), Apply (Sprint 3) |
| POCDEX profile lookup | Eng (spike Sprint 1, OTEP-183) | Discovery | Ringfencing (Sprint 3) |
| Careers@Gov API integration | Pow Hwee | **Confirmed: API** (open item #11 resolved 2026-05-14) | C@G work (Sprint 5) |
| FormSG webhook integration | Eng (discovery Sprint 1, OTEP-194) | Design | Full apply flow (Sprint 4) |
| Email delivery service | Infra (Fabian?) | Unknown (open item #15) | Confirmation emails, EDM deep-links |

---

# Closed Sprints — historical record

> Kept for the record. These reflect each sprint as it stood at close; carry-overs are tracked in the active sprint above.

## Sprint 2 (18–29 May) — CLOSED ✅ (2026-06-02) — Listing → Detail End-to-End

**Sprint goal:** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

> **Closed 2026-06-02.** 6 stories Done at close (OTEP-267, 252, 194, 193, 288, 296). Unfinished work (11 QA + OTEP-85/313/322 In Progress + OTEP-128/268/129) carried into Sprint 3 — see the active Sprint 3 section above. Table retained as historical record of the sprint as it stood mid-flight.

### Live Jira status (snapshot 2026-05-20 — historical)

| Jira | Story | Owner | Jira Status | Notes |
|------|-------|-------|-------------|-------|
| OTEP-170 | Base Layout for Opportunity Listing Page | Thomas | **In Progress** | MR in progress. Sub-task of OTEP-85. |
| OTEP-193 | Design Data Model for Opportunities | Léo | **In Progress** | .sql migration + Go structs. Must support OTG now, C@G later (#23). |
| OTEP-288 | Setup simple backend endpoint with in-memory list | Léo | **In Progress** | ⚠️ Léo has 2 In Progress — WIP risk. New comment 2026-05-19. Sub-task of OTEP-85. |
| OTEP-296 | Prepare defined report format matching data model | Michelle | **In Progress** | Standardises OTG Excel format before ingestion. Must align with OTEP-193. |
| OTEP-252 | Setup design system in otep-web | Thomas | **Done** | Flagship/LifeSG confirmed. Sub-task of OTEP-170. |
| OTEP-85 | Display opportunity cards with real OTG data | — | Backlog | Critical path — must ship first. Visibility = `closing_date > today`. ⚠️ No assignee. |
| OTEP-128 | View opportunity detail page | — | Backlog | Absorbs OTEP-285 ACs (click-through + return-to-page). ⚠️ No assignee. |
| OTEP-129 | See whether opportunity is open/closed before applying | — | Backlog | Re-added (Pow Hwee, 2026-05-18). Owns "Closing soon" badge (≤7 days) + deep-link error state. ⚠️ No assignee. |
| OTEP-267 | Pagination for listing page | — | Backlog | Depends on OTEP-85. API dep: `total_count` in response. ⚠️ No assignee. |
| OTEP-268 | Empty, error, and partial-load states for listing | — | Backlog | Re-added (Pow Hwee, 2026-05-18). Drop partial-load AC. ⚠️ No assignee. |
| OTEP-289 | [Spike] Filter Opportunities by Functions | — | Backlog | 2-day timebox (19–20 May). Output = written recommendation + go/no-go (open item #29 resolved). ⚠️ No assignee. |
| OTEP-194 | [Spike] FormSG Integration & Callback Flow | Thomas | Backlog | Carry-over Sprint 1. Discovery/design. |
| OTEP-295 | Mock detail endpoint for opportunity | Léo | Backlog | Sub-task of OTEP-128. GET /v1/opportunities/:id + 404. |
| ~~OTEP-276~~ | ~~[Spike] Custom design system reimplementation~~ | — | Backlog | **Resolved** — OTEP-252 Done confirms Flagship/LifeSG. Remove from board. |

**Scope changes since Sprint 2 start:**
- ~~OTEP-285~~ — **absorbed into OTEP-128** (Pow Hwee, 2026-05-18). No Sprint 3 ticket needed.
- ~~OTEP-191~~ — removed from Sprint 2 board (deprioritised to Sprint 3+, Pow Hwee, 2026-05-14).
- ~~OTEP-192~~ — **moved to Sprint 3** (2026-05-19 decision). Not a Sprint 2 story.
- OTEP-129 and OTEP-268 — **re-added** to Sprint 2 by Pow Hwee (2026-05-18), overriding earlier absorptions/deferrals.
- OTEP-296, OTEP-295 — **new sub-tasks** added to Sprint 2 board (2026-05-20).

### Carry-overs — resolved (open item #27 closed 2026-05-20)

| Jira | Story | Owner | Placement |
|------|-------|-------|-----------|
| OTEP-202 | Create POCDEX seed database for local dev | Leo | **Sprint 4** |
| OTEP-203 | Implement standalone POCDEX API service | Pow Hwee | **Sprint 3** ✓ |
| OTEP-271 | Local POCDEX database (container + schema) | Leo | **Sprint 3** ✓ |

### Capacity (historical)

- 18 May PM — public holiday + Pow Hwee + Michelle out. Sprint effectively started Tue 19.
- 22 May PM — Leo out.
- **27 May — Hari Raya Haji public holiday.** 1 dev day lost.
- Thomas was sole FE — binding constraint across all frontend stories.

---

## Sprint 1 (4–15 May) — CLOSED — Login + Foundation + Discovery/Design

**Sprint goal:** Login and navigate to Jobs and Opportunities. Auth flows end-to-end; OTG → OTEP data pipeline delivering records; C@G ingestion method confirmed; Amber's Hub UI + card designs finalised.

**Final sign-off (2026-05-15): Partial.** Headline auth story done. OTEP-170 MR not merged by close. OTEP-202/203 and data model/pipeline stories carried to Sprint 2. Auth edge-cases (OTEP-110, WOG-04/05/06) carried forward.

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
| WOG-04 | Stay logged in during session | WOG AD | **→ OTEP-304, moved to Sprint 4+** (Sprint 3 → Sprint 4, 2026-05-21 reallocation) |
| WOG-05 | Log out of OTEP | WOG AD | **→ OTEP-305, moved to Sprint 4+** (Sprint 3 → Sprint 4, 2026-05-21 reallocation) |
| WOG-06 | First-time login experience | WOG AD | **Carried → Sprint 3** (not on Sprint 2 board) |
| OTEP-251 | Create ER diagram for OTEP data model | — | Status unknown — confirm |

---

*Living doc — update after each grooming / planning session. When a story moves sprints, change it here first, then sync `story-id-map.md`'s Sprint column.*
