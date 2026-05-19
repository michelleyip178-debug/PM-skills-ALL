# PRD: Opportunity Discovery Hub (Epic 4 MVP)

**Author:** Michelle Yip
**Created:** 2026-05-06
**Last updated:** 2026-05-13
**Status:** Draft
**Target Release:** Go-Live Fri 16 Oct 2026 (per programme plan, decision 2026-05-12)
**Source:** [Epic 4 Confluence PRD (Apr 6 2026)](OTEP-Epic%204_%20Opportunity%20Discovery%20(MVP).pdf)

---

## 1. Problem Statement

### What problem are we solving?

Officers **struggle to discover and apply for development opportunities** because they are **fragmented across multiple portals**, resulting in confusion on validity of job postings and friction for officers to have a single view of all short-term and long-term opportunities.

Host agencies face the same problem in reverse: no operational visibility into applicants, manual sign-up tracking, and no feedback loop on whether opportunities actually filled.

### Who has this problem?

| # | User | Primary need |
|---|------|-------------|
| 1 — Primary | Government officer seeking development opportunities (STIPs, Gigs, SJRs, job rotations) | Discover what's available without relying on informal networks; apply without friction |
| 2 — Secondary | Host agency coordinator posting opportunities and tracking applicants | Reach eligible officers at scale; track sign-ups without manual overhead |

### How do we know this is a problem?

**Demand data (STIPs + Gigs):**

| Quarter | Vacancies (OTG) | Sign-ups (FormSG) | Demand gap | Note |
|---------|----------------|-------------------|------------|------|
| Q1 | 635 | 877 | +242 | |
| Q2 | 876 | 1,334 | +458 | Gig spike (478 vacancies) |
| Q3 | 1,064 | 1,825 | +761 | |
| Q4 | 2,177 | 3,061 | +884 | Peak season |
| **Total** | **4,752** | **7,097** | **+49%** | **Demand exceeds supply** |

- STIPs: 4,056 vacancies vs 6,411 sign-ups — highest impact by volume
- Gigs: 696 vacancies vs 686 sign-ups — roughly balanced, concentrated in Q2

**Data caveat:** This captures sign-ups/interest, not attendance or fill rates. Attendance data is incomplete and not tracked centrally.

**Why now:**

| What changed | Why it creates urgency |
|-------------|----------------------|
| Leadership emphasis on competency-driven growth | Mobility participation is increasingly expected. The programme needs infrastructure that matches this expectation. |
| Opportunities visible but fragmented across channels | Officers are actively seeking opportunities but encountering inconsistent information and unequal access. |
| Decision to replace FormSG confirmed (12 March session) | OTEP-hosted application flow is the approved direction. |

### What happens if we don't solve it?

- Officers continue navigating multiple platforms — OTG, Careers@Gov, standalone FormSG links
- No channel migration from FormSG to OTEP (Phase 1 MVP fails its core KPI)
- No data on application completion or drop-off — blocking future optimisation
- Host agencies stay on manual tracking with no feedback loop

---

## 2. Hypothesis (Value Proposition)

> If we provide a unified Opportunities Hub within OTEP *[capability]*, then government officers *[user]* will be able to discover and apply for development opportunities in one place, without relying on informal networks or navigating multiple systems *[new behaviour]*, leading to increased application completion rate and channel migration from FormSG to OTEP *[measurable outcome]*.

---

## 3. Solution Overview

### High-Level Approach

A unified Opportunities Hub aggregating all five opportunity types:

| Type | Application channel (MVP) | Notes |
|------|--------------------------|-------|
| STIPs | FormSG (redirect, new tab) | Webhook back to OTEP for submission confirmation |
| Gigs | FormSG (redirect, new tab) | Same as STIPs |
| Internal Jobs | FormSG (redirect, new tab) | Confirmed at BO Senior Level meeting (2026-05-12) |
| SJRs | **No apply in MVP — discovery only** | Full detail page on OTEP; apply deferred to future release. SJR cards visible but no apply action. UX treatment TBD (Amber, open item #20). Long-term: OTEP owns all apply flows. |
| C@G Public Jobs | Careers@Gov (deep-link, new tab) | Discovery on OTEP only; no application tracking |

> **Decision 2026-05-13:** MVP apply flow = FormSG for Internal Jobs, STIPs, and Gigs only. SJR apply deferred to future release — all apply flows will go through OTEP, not OTG redirect. Supersedes the 2026-05-08 decision (SJR via OTG redirect). See `context/decisions-log.md`.

### Key Capabilities

1. **Unified listing** — all opportunity types on one page, sorted by most recently posted, with ringfenced internal jobs prioritised on top
2. **Search & filter** — keyword search + type filter (STIP, Gig, SJR, Internal Job, C@G); filter state stored in URL params
3. **Structured opportunity cards** — fixed-size cards showing type, title (max 2 lines), agency with ministry icon, commitment, relative posting date
4. **Detail pages** — full opportunity details including competencies, developmental outcomes, duration
5. **Application routing** — FormSG redirect for STIPs, Gigs, and Internal Jobs; C@G deep-link for public jobs; SJR discovery-only with clear UX treatment
6. **FormSG webhook** — submission confirmation received by OTEP, recorded against officer + opportunity ID
7. **Ringfencing** — listing filtered by officer's POCDEX data on login; refreshes on agency transfer

### What we're NOT building (MVP scope boundaries)

- SJR apply flow (deferred to future release — decision 2026-05-13)
- OTG redirect for any opportunity type (all apply flows route through FormSG or C@G deep-link)
- Agency/grade/commitment filters (R1)
- Autocomplete or suggested searches
- Persist filter selections across sessions (R1)
- Competency-based matching for STIPs/Gigs (display only, no personalisation)
- Application status tracking beyond submission confirmation
- Application status tracking for C@G opportunities (off-platform — OTEP has no visibility)
- Email/push notifications beyond FormSG submission email
- Changes to FormSG form fields (keep as current for MVP)

---

## 4. User Stories

Stories are organised into five groups along the officer journey. Full acceptance criteria, edge cases, and DoR checklists live in each group's dedicated file.

### Group 1: Profile Dependency (cross-pillar — critical path foundation)

Officer profile (HR-sourced) + competencies + pre-fill. No profile -> no low-friction apply -> no status tracking.

| ID | Story | Priority | Notes |
|----|-------|----------|-------|
| US-P1 | View my HR-sourced profile | MVP | Source: HR pipeline (VITALS TBC) |
| US-P2 | View my competencies | MVP | Binary model for MVP; proficiency tiers R1. `developmental_outcome` confirmed available in OTG export (2026-05-13). |
| US-P3 | Pre-fill application from profile | MVP if FormSG supports / R1 if not | Bridge between Profile and Apply. Open item #14 (Pow Hwee). |

Details: [profile-dependency.md](stories/profile-dependency.md)

### Group 2: Discovery & Filters (9 stories — OTEP-85 split into 3)

Officers finding and filtering opportunities across both pipelines. Filter taxonomy shaped by [categorisation research](research/categorisation-research.md) — hybrid model (Option C) recommended.

| ID | Story | Priority | Sprint | Notes |
|----|-------|----------|--------|-------|
| **OTEP-85** | Display opportunity cards with real OTG data | MVP | 2 | Full-stack: listing API + card component + feature flag. Visibility: `closing_date` > today. **Must ship first** — all other Sprint 2 stories depend on it. |
| **OTEP-267** | Pagination for the listing page | MVP | 2 | FE-only. Depends on OTEP-85. Parallel with OTEP-268. |
| **OTEP-268** | Empty state, error state, data resilience | MVP | 2 | FE-only. Empty state, error + retry, missing-field degradation. Depends on OTEP-85. Parallel with OTEP-267. |
| OTEP-86 | Filter opportunities by type | MVP | 2 | STIP, Gig, SJR, Internal Job. Secondment subsumed under SJR (resolved 2026-05-13). |
| US-03 | Filter opportunities by category | MVP | 3 | Job function — pipeline-specific in MVP (hybrid model) |
| OTEP-128 | **View opportunity detail page** *(repurposed 2026-05-14)* | MVP | 2 | Detail page at `/opportunities/:id`. Type badge absorbed into OTEP-85. See [otg-lifecycle.md](stories/otg-lifecycle.md). |
| US-05 | Clear filters and reset view | MVP | 2 | Basic UX hygiene. Pairs with OTEP-86. |
| OTEP-129 | Sort by posting date | MVP | 2 | **Overlap with OTEP-85** — OTEP-85 includes default sort. OTEP-129's independent value = "Closing soon" label (<=7 days to `closing_date`, now unblocked). May be absorbed into OTEP-85 at grooming. |
| US-07 | Persist filter selections | R1 | — | Not required for MVP target |

> **OTEP-85 split (2026-05-13):** Original story was too large. Split into 3 vertical slices, each independently demo-able with subtasks and test cases per Rama's DoR. Full details in [filters.md](stories/filters.md).

**Workflow gap:** Keyword search has no dedicated user story. Confirmed MVP (decision 2026-05-08), has open items (#9 UX, #16 infra), but needs a story with ACs before Sprint 3 grooming. See [workflow-coverage-audit.md](workflow-coverage-audit.md).

Details: [filters.md](stories/filters.md)

### Group 3: OTG Application Lifecycle (3 stories)

Discovery -> FormSG application -> confirmation. End-to-end on OTEP.

| ID | Story | Priority | Notes |
|----|-------|----------|-------|
| OTEP-87 | View OTG opportunity details | MVP | Full detail view before apply |
| US-18 | Apply via FormSG (basic redirect) | MVP | STIP + Gig + Internal Job. Scope updated per decision 2026-05-13. **ACs not yet written** — workflow gap. |
| OTEP-130 | Apply to an OTG opportunity via FormSG (full) | MVP | Webhook confirmation, email, deduplication |
| US-10 | Receive application confirmation | MVP | FormSG webhook -> OTEP confirmation |
| ~~US-19~~ | ~~Apply via OTG redirect (SJR)~~ | **Dropped** | SJR apply deferred to future release (decision 2026-05-13) |

Details: [otg-lifecycle.md](stories/otg-lifecycle.md)

### Group 4: C@G Deep-link Handoff (3 stories)

Discovery on OTEP -> handoff to Careers@Gov for application. No application tracking for C@G in MVP.

| ID | Story | Priority | Notes |
|----|-------|----------|-------|
| OTEP-89 | View C@G opportunity summary on OTEP | MVP | Context before redirect |
| OTEP-133 | Redirect to Careers@Gov to apply | MVP | Core action of C@G pipeline. Also handles EDM deep-link — consider splitting (workflow gap #1). |
| OTEP-88 | Understand the difference between OTG and C@G flows | MVP | Button labels and visual cues |

Details: [cag-handoff.md](stories/cag-handoff.md)

### Group 5: Application Status Tracking (4 stories)

Officers tracking their OTG application status. Proposed status model: Submitted -> Under Review -> Shortlisted -> Accepted / Rejected (+ Withdrawn from any non-final state).

| ID | Story | Priority | Notes |
|----|-------|----------|-------|
| US-14 | View my submitted applications | MVP | "My Applications" list |
| US-15 | See the status of an individual application | MVP | Status detail + history |
| US-16 | Receive notification when status changes | MVP | In-app only; email/push R1 |
| US-17 | Withdraw an OTG application | MVP | Confirm before action; irreversible |

**Workflow gap:** Application status source of truth undefined — where do status updates come from? Recommend: FormSG webhook = "Submitted" (automated); subsequent statuses = agency manual update via admin panel (MVP). Resolve before tracking stories are groomed.

Details: [tracking.md](stories/tracking.md)

### Critical Path

```
OTEP-71a (Auth) -> OTEP-72 (Account) -> US-P1 (Profile) -> OTEP-85 (Cards, sort, type badge) -> OTEP-267 (Pagination)
                                      |                  |                                     -> OTEP-268 (States)
                                      |                  |                                     -> OTEP-128 (Detail page)
                                      |                  |                                          |
                                      |                  |                                          -> OTEP-87 (Apply CTA + competencies, Sprint 3)
                                      |                  |                                               -> US-18 (Basic Apply) -> OTEP-130 (Full Apply) -> US-10 (Confirmation) -> US-14 (Track)
                                      |                  |
                                      |                  +-> OTEP-86 (Filter, Sprint 3) + US-05 (Clear filters)
                                      |
                                      -> US-P2 (Competencies)
                                      -> US-P3 (Pre-fill) -> OTEP-130
```

### Story Count

| Group | MVP | R1 / Dropped | Total |
|-------|-----|--------------|-------|
| Profile Dependency | 2-3 | 0-1 | 3 |
| Discovery & Filters | 8 (incl. OTEP-85/267/268) | 1 | 9 |
| OTG Lifecycle | 4 | ~~1 (US-19 dropped)~~ | 4 |
| C@G Handoff | 3 | 0 | 3 |
| Tracking | 4 | 0 | 4 |
| **Total** | **21-22** | **1-2** | **23** |

> Note: OTEP-129 may be absorbed into OTEP-85 at grooming (overlap — see Group 2 notes). If absorbed, MVP count drops by 1.

---

## 5. Success Metrics

### 5.1 Outcome Metrics (North Star)

| Metric | Definition | Target |
|--------|-----------|--------|
| Application Completion Rate | Forms submitted / Apply button clicks x 100 | TBD (baseline from FormSG) |
| Channel Migration | % of total STIP/Gig applications submitted via OTEP | >= 50% by Month 3 |

### 5.2 Input Metrics

| Metric | Event Key | What it tells us |
|--------|-----------|-----------------|
| Click-through rate | `oppr_detail_view` | % of listing views -> detail page |
| Apply click rate | `click_to_formsg`, `click_to_cg` | % of detail page -> apply action |
| Search usage | `search_performed` | % of sessions with at least one keyword search |
| Search-to-detail | `search_to_detail` | % of search result views -> detail page |
| Filter usage | `filter_applied` | % of sessions applying at least one type filter |
| Card-to-detail rate | card views -> detail page view | Measures card information scent |

### 5.3 Guardrail Metrics (triggers for pause/rollback)

| Metric | Threshold | Escalation |
|--------|-----------|-----------|
| Submission error rate | Any spike | Pause and investigate (Engineering) |
| Confirmation email delivery rate | Drop below baseline | Escalate to Infra (Fabian) |
| Zero-result search rate | `search_zero_results` > X% | Inform design for R1 filter work |
| Missing FormSG link rate | % of listings with null/invalid URL | Data quality monitoring |

---

## 6. Design & UX

### Key Screens

1. **Opportunity listing page** — cards, search bar (sticky on scroll), filter panel, "Back to Top" button
2. **Opportunity detail page** — developmental outcomes, duration, competencies ("What you'll develop"), apply CTA (visible without scrolling)
3. **Pre-redirect notices** — "You will be taken to FormSG / Careers@Gov" before leaving OTEP
4. **SJR card treatment** — SJR cards visible but no apply action; UX treatment TBD (Amber, open item #20)
5. **Empty/error states** — zero results, closed opportunity deep-link, missing FormSG link, no-access (ringfenced)

### Key Design Decisions

1. **Fixed-size cards** — firm brief requirement; overflow goes to detail page, not in-card expansion
2. **Title truncation** — max 2 lines, ellipsis at overflow, consistent across all cards
3. **Ministry icon** — each card displays posting ministry's icon alongside agency name
4. **Competency display** — "What you'll develop" tags (no matching, no scoring — decision 2026-05-08). `developmental_outcome` confirmed available in OTG export (2026-05-13).
5. **Relative posting dates** — "Posted today" / "Posted 1 week ago" / "Posted 1 month ago" / "Posted more than 3 months ago"
6. **"Closing soon" label** — shown on card and detail page when <= 7 days to `closing_date` (field confirmed 2026-05-13)
7. **Type filter only for MVP** — no agency, grade, or commitment filters (R1)
8. **Source labels** — C@G listings labelled "Careers@Gov" on card without needing to hover/click
9. **Type distinguishable without colour alone** — accessibility requirement
10. **Secondment is SJR** — no separate type badge or filter value (resolved 2026-05-13)
11. **Visibility by closing date** — no `is_published` field exists; opportunity is visible if `closing_date` > today (resolved 2026-05-13)
12. **`reporting_line` not available** — remove from detail page design (resolved 2026-05-13)

### Accessibility Considerations

- Visual treatment must distinguish opportunity type without relying on colour alone
- Search placeholder text sets expectations (e.g. "Search by role, agency, or keyword")
- Pagination recommended for performance

---

## 7. Technical Approach

### Data Sources

| Source | Integration method | Refresh | Field status |
|--------|-------------------|---------|-------------|
| OTG (STIPs, Gigs, SJRs, Internal Jobs) | OTG -> OTEP via export (daily delta — confirm with Rama) | Daily | 5 of 6 fields confirmed (2026-05-13). `formsg_url` still unconfirmed (open item #2). `eligibility` not needed. `reporting_line` not available. `developmental_outcome` confirmed. `closing_date` = application closing date. `is_published` does not exist. |
| Careers@Gov | Separate ingestion — method unconfirmed (open item #11, Pow Hwee) | Daily | API vs file export vs scrape — binary answer needed by Sprint 2 end |
| POCDEX | Officer profile data for ringfencing on login | On login | Spike in Sprint 1 (OTEP-183) |

### Dependencies

- **Internal:** WOG AD Login (officers must be authenticated); POCDEX integration (ringfencing)
- **External:** OTG/WG-managed opportunity lists (Excel input); Careers@Gov (deep-links only, no data return at MVP); FormSG (webhook for submission confirmation); Email delivery service (open item #15)

### Key Technical Decisions

1. **FormSG integration** — redirect to new tab (not embedded). Webhook set up between FormSG and OTEP for submission confirmation.
2. **Application routing** — FormSG for STIPs, Gigs, and Internal Jobs. C@G deep-link for public jobs. No OTG redirect for any type (decision 2026-05-13).
3. **Filter state** — stored in URL params so officers can share/bookmark filtered views
4. **Search** — works across opportunity titles, description, agency name at minimum. Elastic search with partial matches and minor typo tolerance. Indexing infra needs provisioning (open item #16).
5. **Listing refresh** — on search/enter, not on every keystroke
6. **Ringfencing** — all opportunities filtered per officer's POCDEX data. On agency transfer, next login refreshes listing.
7. **Visibility rule** — opportunity is visible if `closing_date` > today. No `is_published` field exists (resolved 2026-05-13).
8. **Closed postings** — hidden from listing and search. Deep-links show "This opportunity is no longer available" with link back to listing.

### Technical Risks

| Risk | Mitigation | Owner |
|------|------------|-------|
| OTG data schema — `formsg_url` field still unconfirmed | Chase Rama + PSD Ops (open item #2). Last unconfirmed OTG field. | Rama |
| C@G API availability unknown | Confirm ingestion method (open item #11). If no viable path, defer C@G to R1. | Pow Hwee |
| FormSG webhook reliability | Error handling for missed webhooks; reconciliation job | Pow Hwee |
| Search indexing infra (Elasticsearch/OpenSearch) provisioning in GCC | Confirm availability and provisioning timeline (open item #16) | Pow Hwee |
| POCDEX session/auth handling | Confirm with POCDEX integration owner | Pow Hwee |

---

## 8. Launch Plan

### Go-To-Market

- **Target launch group:** 1-2 agencies that actively post Gigs (prefer higher posting volume + willing HR partner)
- **Comms plan:** TBD
- **Training/enablement:** TBD
- **Support model:** TBD

### Rollout Phases

| Phase | When | Scope |
|-------|------|-------|
| Phase 1 Feature Build | Sprints 1-8 (4 May - 21 Aug) | All MVP stories |
| Phase 2 Compliance & Go-Live | Sprints 9-12 (24 Aug - 16 Oct) | Security review, pen testing, UAT, launch |
| Feature Freeze | End of Sprint 8 (Fri 21 Aug) | No new development after this |
| Go-Live | Fri 16 Oct 2026 | Full MVP launch |

### Feature Flags

- Each user story designed with feature flag + entry point identified (per DoR — see [dor-dod-guidelines.md](../../resources/dor-dod-guidelines.md))

---

## 9. Timeline & Milestones

### Delivery Model

12 sprints, 4 May - 16 Oct 2026 (per OTEP-Pathfinder Sprint Ceremonies v2, decision 2026-05-12).

- Phase 1 Feature Build: Sprints 1-8 (4 May - 21 Aug)
- Feature Freeze: end of Sprint 8 (Fri 21 Aug)
- Phase 2 Compliance & Go-Live: Sprints 9-12 (24 Aug - 16 Oct)
- Go-Live: Fri 16 Oct 2026

For the sprint-by-sprint story breakdown, see [sprint-allocation.md](../sprint-allocation.md) (source of truth) and [sprint-calendar.md](../../context/sprint-calendar.md) (dates + ceremonies).

### Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Steering approval | 2 April 2026 | Done |
| PRD approved | TBD | Draft |
| Design complete (Hub + Detail + Filters) | End of Sprint 1 (May 16) | In progress (Amber) |
| Application routing UX designed | Sprint 3 (Jun 13) | Not started (Amber) |
| Feature Freeze | Fri 21 Aug 2026 | Not started |
| Security review submission | Early Sep 2026 | Not started |
| UAT/Pilot | Sprints 8-10 (Aug-Sep) | Not started |
| Final Steering sign-off | Fri 9 Oct 2026 | Not started |
| Go-Live | **Fri 16 Oct 2026** | Not started |

---

## 10. Risks, Assumptions & Mitigations

| Risk / Assumption | Type | Likelihood | Impact | Mitigation |
|-------------------|------|------------|--------|------------|
| Scope creep beyond MVP | Operational | High | High | Hold the line on MVP vs R1; scoping gaps tracker; scope freeze with Adrian (discovery plan experiment C1) |
| Stakeholder direction keeps shifting | Stakeholder | High | High | Log every scope shift in decisions-log; surface drift to Adrian early; request scope freeze until Sprint 5 |
| Stakeholder misalignment on success metrics | Stakeholder | Medium | High | Lock alignment with Mark, Adrian, Jacky, Xian Zhang |
| OTG export data quality insufficient for search | Technical | Medium | Medium | 5 of 6 fields confirmed. `formsg_url` still open. |
| C@G deep-link format changes | Technical | Low | Medium | Resilient URL handling; fallback message if broken |
| FormSG webhook missed | Technical | Medium | High | Reconciliation job; clear error state for officers |
| Data pipeline not delivering by end Sprint 1 | Technical | Medium | High | Sprint 2 UI work blocked. Fallback: FE builds against mock data. |
| Sprint 3 cascade risk | Schedule | Medium | Medium | OTEP-133 depends on OTEP-87 and OTEP-127. If either slips, OTEP-133 moves to Sprint 4 |
| Security review monthly cycle | Schedule | Low | High | Must submit by early Sep to hit the Oct go-live window |
| Engineer scope spread | Delivery | Medium | Medium | Watch at planning + mid-sprint; flag to Adrian/Jace if capacity bites |
| MVP without notifications can't drive adoption | Value | Medium | High | Validate with officer interviews (discovery plan experiment A1) |
| "Unified" pitch weakened by SJR deferral | Stakeholder | Medium | Medium | Test narrative with Jace + Adrian before steering (discovery plan experiment C2) |

---

## 11. Decision Tracker

> **Canonical log:** [context/decisions-log.md](../../context/decisions-log.md). This table is synced as of 2026-05-13.

| Decision | Owner | Date | Status |
|----------|-------|------|--------|
| Steering approval to proceed with Opportunities MVP | PS/DS | 2 Apr 2026 | Approved |
| Replace FormSG with OTEP-hosted application flow | Steering | 12 Mar 2026 | Approved |
| Categorisation model: hybrid approach (Option C) | Michelle | 6 May 2026 | Recommended — pending validation |
| Filter scope: type filter + C@G indicator only for MVP | Brief | Apr 2026 | Confirmed |
| Function/Job function mapping deferred to R1 | Michelle | 6 May 2026 | Confirmed |
| Competency levels binary only for MVP | Michelle | 8 May 2026 | Confirmed |
| No "Save for later" in MVP | Michelle | 8 May 2026 | Confirmed |
| Supervisor endorsement — UI copy only, no backend | Michelle | 8 May 2026 | Confirmed |
| Search is in MVP | Michelle | 8 May 2026 | Confirmed |
| Competency match ratio descoped to R1 | Michelle | 8 May 2026 | Confirmed |
| Sprint 2 scope = 5 stories, OTG data only | Michelle | 11 May 2026 | Confirmed |
| Auth flow accepted for MVP | Adrian / Michelle | 12 May 2026 | Confirmed |
| Programme plan: 12 sprints, Go-Live 16 Oct 2026 | Programme | 12 May 2026 | Confirmed |
| R4 focus: opportunity creation & posting (Agency-Owner side) | BO Senior Level | 12 May 2026 | Confirmed |
| MVP apply flow = FormSG for Internal Jobs, STIPs, Gigs. SJR apply deferred. | Michelle | 13 May 2026 | Confirmed |
| Secondment subsumed under SJR | Jacky (BO) | 13 May 2026 | Confirmed |

---

## 12. OTG Field Status (resolved 2026-05-13)

| Field | Status | Impact |
|-------|--------|--------|
| `eligibility` | Not needed | Removes a field dependency from opportunity detail |
| `formsg_url` | **Still unconfirmed** (open item #2) | Blocks STIP/Gig/Internal Job apply flow (Sprint 3) |
| `closing_date` | Confirmed: application closing date | OTEP-85 sort + "Closing soon" label + visibility rule (absorbed from OTEP-129, 2026-05-14) |
| `is_published` | Does not exist | Engineers use `closing_date` > today for visibility |
| `reporting_line` | Not available in OTG export | Remove from detail page design |
| `developmental_outcome` | Confirmed available | "What you'll develop" section can populate |

---

## 13. FormSG Application Fields (Future — post-MVP)

For MVP, no changes to FormSG forms. Below documents the proposed R1 changes per BO:

**Auto-populated from POCDEX (no manual entry):**
- Full Name, Designation, Division & Department, Ministry/Agency, Work Email

**Fields to retain/add:**
- Contact Number
- Reporting Officer's Name and Email (triggers supervisor notification)
- Job Grade (dropdown of MX grades + "Others")
- Main reason for application
- Meet pre-requisites
- Declarations (may differ for STIP vs Gig)
- Custom Questions (per posting — BO request)

**Fields to drop:**
- HR Officer's Name and Email (rarely used, caused confusion)
- "Where did you find out about this opportunity?" (all traffic routes through OTEP)

---

## 14. Open Questions

| Question | Owner | Due Date | Resolution |
|----------|-------|----------|------------|
| ~~Is 'Secondment' a distinct type or sub-type of SJR?~~ | ~~Jacky~~ | — | Resolved 2026-05-13: subsumed under SJR |
| ~~`closing_date` vs `end_date`?~~ | ~~Rama~~ | — | Resolved 2026-05-13: `closing_date` = application closing date |
| ~~`is_published` field?~~ | ~~Rama~~ | — | Resolved 2026-05-13: does not exist; use `closing_date` |
| What about evergreen/long-running postings with old creation dates but recently modified? | Michelle | TBD | Sort key = `posting_date` (Michelle's call). Revisit if officers complain. |
| After FormSG submission, can we redirect users back to OTEP to show success? | Pow Hwee | Before Sprint 4 | Determines confirmation UX — inline vs webhook-dependent |
| Is Organisation/Agency the same master list across OTG and C@G? | Pow Hwee | TBD | |
| What user-friendly labels for source toggle (not "OTG"/"C@G")? | Amber | Before Sprint 5 | |
| Confirm session/auth handling with POCDEX integration owner | Pow Hwee | TBD | |
| Opportunity lifecycle: date-driven or manual close? | Michelle / Pow Hwee | Before Sprint 2 | Proposed rule: `closing_date` > today = visible. Open item #17. |
| Does FormSG support pre-fill via URL params? | Pow Hwee | Before Sprint 3 | Determines whether US-P3 is MVP or R1. Open item #14. |
| Application status source of truth: agency manual? FormSG webhook? Both? | Michelle / Pow Hwee | Before tracking group groomed | Recommend: webhook = "Submitted" (auto); rest = agency manual. |

---

## Appendix

### Workflow Coverage

A full audit of all officer workflows against stories is in [workflow-coverage-audit.md](workflow-coverage-audit.md) (2026-05-13). 11 gaps identified — 4 high severity.

### Related Documents

- **Source PRD:** Epic 4 Confluence doc (Apr 6, 2026)
- **Sprint Plan:** [sprint-allocation.md](../sprint-allocation.md)
- **Sprint Calendar:** [sprint-calendar.md](../../context/sprint-calendar.md)
- **Categorisation Research:** [research/categorisation-research.md](research/categorisation-research.md)
- **User Stories (Index):** [stories/index.md](stories/index.md)
- **User Stories (Profile Dependency):** [stories/profile-dependency.md](stories/profile-dependency.md)
- **User Stories (Filters):** [stories/filters.md](stories/filters.md)
- **User Stories (OTG Lifecycle):** [stories/otg-lifecycle.md](stories/otg-lifecycle.md)
- **User Stories (C@G Handoff):** [stories/cag-handoff.md](stories/cag-handoff.md)
- **User Stories (Tracking):** [stories/tracking.md](stories/tracking.md)
- **Scoping Gaps Tracker:** [scoping-gaps-tracker.md](scoping-gaps-tracker.md)
- **Workflow Coverage Audit:** [workflow-coverage-audit.md](workflow-coverage-audit.md)
- **Decision Log:** [context/decisions-log.md](../../context/decisions-log.md)
- **DoR/DoD Guidelines:** [resources/dor-dod-guidelines.md](../../resources/dor-dod-guidelines.md)
- **Discovery Plan:** [outputs/discovery-plan-2026-05-13.md](../../outputs/discovery-plan-2026-05-13.md)

### Stakeholder Sign-offs

- [ ] Engineering Lead: Pow Hwee
- [ ] Design Lead: Amber
- [ ] Business Owner: Jacky / Xian Zhang
- [ ] PM Manager: Jace / Adrian
