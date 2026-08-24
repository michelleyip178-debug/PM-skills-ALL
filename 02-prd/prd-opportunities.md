# Epic 4: Opportunity Discovery (MVP - STIPs, Gigs, SJRs, Internal Jobs, External Jobs - C@G)

| Doc Created |  |
|---|---|
| PM |  |
| Tech |  |
| Designer | Amber Tong |
| Business Owner | Jacky (lead), Xian Zhang (owner) |
| Infra Eng |  |
| Target launch | Date |
| Epic Link | Link to Jira Epic (PM to input) |
| Figma Link |  |
|  |  |

**Resource Directory:**

<Put in STIPs and Gigs MIRO> | [https://folk-false-94042272.figma.site](https://folk-false-94042272.figma.site)  

## Background & Context

**Purpose:** Help the reader understand why this exists now.

OTEP is positioned as the platform for officer development - the front-door discovery hub for courses and opportunities across the Singapore public service. The Opportunities pillar (aggregating STIPs, Gigs, SJRs, internal jobs and C@G public facing jobs job rotations) is one of two confirmed MVP pillars alongside “My Development.”

**Current State**

Prior to OTEP, all applications went through standalone FormSG links distributed by host agencies or via Careers@Gov. There is no central discovery point. The decision to replace FormSG with an OTEP-hosted application flow was confirmed at the 12 March session.

### **Why Now / What Changed**

| **What has changed** | **Why it creates urgency** |
|---|---|
| Leadership emphasis on competency-driven growth | Mobility participation is increasingly expected. The programme needs infrastructure that matches this expectation. |
| Opportunities visible but fragmented across channels | Officers are actively seeking opportunities but encountering inconsistent information and unequal access. Centralization addresses this directly. |

## 2. Problem Statement

**Purpose:** Clearly define the problem before jumping to solution. 

[User] struggles to [do what] because [root cause], resulting in [negative outcome].

> *Officers **struggle to discover and apply for development opportunities** because they are **fragmented across multiple portals**, resulting in confusion on validity of job postings and friction for officers to have a single view of all short term and long term opportunities.*

> *Host agencies face the same problem in reverse: no operational visibility into applicants, manual sign-up tracking, and no feedback loop on whether opportunities actually filled.*

## 3. Data Analysis & Evidence 

**Purpose:** Show this is not opinion-driven. What proof do we have that this is real and worth solving?

**The below is for STIPs and Gigs.** 

| **7,097**    Total sign-ups (annual) | **4,752**    Total vacancies (annual) | **+49%**    Demand exceeds supply |
|---|---|---|

[STIP/Gig] Demand consistently exceeds supply across the year. This is not a discovery problem caused by lack of interest — officers already want these opportunities. OTEP’s job is to make that demand visible and reduce the friction between interest and application.

| **Quarter** | **Vacancies**    (published in OTG) | **Sign-ups (Responses from FormSG)** | **Demand gap** | **Note** |
|---|---|---|---|---|
| Q1 | 635 | 877 | +242 |  |
| Q2 | 876 | 1,334 | +458 | *Gig spike (478 vacancies)* |
| Q3 | 1,064 | 1,825 | +761 |  |
| Q4 | **2,177** | **3,061** | **+884** | *Peak season — heaviest load* |

 

**STIP vs Gig split:**

- STIPs: 4,056 vacancies vs 6,411 sign-ups — this is where OTEP’s application standardisation has the biggest impact by volume
- Gigs: 696 vacancies vs 686 sign-ups — roughly balanced; concentrated in Q2 with near-zero in Q4

**Data caveat:**

- This dataset captures sign-ups/interest, not attendance or confirmed fill rates. Attendance data is incomplete and not tracked centrally.
- What we can claim: scale of officer demand and supply capacity. What we cannot claim from this data alone: actual fill rates or conversion to confirmed placements.
- FormSG submission volumes (channel baseline for OTEP migration target) still to be pulled by Engineering.

## 4. Market / Benchmark Scan

**Purpose:** Avoid reinventing the wheel. Find out how other teams or companies solves a similar problem. Designers can help with this. 

- How do others solve this? 
- Known best practices or patterns
- What we should copy vs avoid

**Table (optional):**

| Organisation | Approach | What works | What doesn’t |
|---|---|---|---|
|  |  |  |  |

## 5. Target User

**Purpose:** Clarify who is your target user.

| **#** | **User** | **Primary need** |
|---|---|---|
| **1 — Primary** | Government officer seeking development opportunities (STIPs, Gigs, SJRs, job rotations) | Discover what’s available without relying on informal networks; apply without friction |
| **2 — Secondary** | Host agency coordinator posting opportunities and tracking applicants | Reach eligible officers at scale; track sign-ups without manual overhead |

## 6. Hypothesis (Value Proposition)

**Purpose:** Make your belief explicit and testable.

> If we provide a unified Opportunities Hub within OTEP *[capability]*, then government officers *[user]* will be able to discover and apply for development opportunities in one place, without relying on informal networks or navigating multiple systems *[new behaviour]*, leading to increased application completion rate and channel migration from FormSG to OTEP *[measurable outcome]*.

## 7. Success Metrics

**Purpose:** Define what “good” looks like across a progression of three stages. Each stage unlocks the next as data and infrastructure mature. MVP is accountable for Stage 1 only - but must build the foundation for Stages 2 and 3. 

**7.1  Outcome Metrics (North Star)**

- Application Completion Rate — forms submitted ÷ Apply button clicks × 100
- Channel migration: ≥50% of total STIP/Gigs applications submitted via OTEP by Month 3

**7.2  Input Metrics**

- % of Click-through rate (listing page → detail page)
- % of Apply click rate (detail page → form)
- % of Form field drop-off rate: no single field should cause abandonment

**7.3  Guardrail Metrics (Events that will lead to rollback or pause)**

- % of Submission error rate → pause and investigate (Engineering)
- % of Confirmation email delivery rate → escalate to Infra 

## 8. Scope (Stories + Success Criteria)

### [Segment 1] Foundation - Shared across all opportunity types

### Browser, Search, Filter, Cards, Detail Pages & Instrumentation

| **Jira ID** | **User Story** | **Acceptance Criteria** | **Success Metrics / What to Track** | **Notes for Designer** | **Notes for Engineer** |
|---|---|---|---|---|---|
| **OTEP-85** | US-01a — Display opportunity cards with real/mock OTG data    As an officer, I want to see all STIPs, Gigs, SJRs and Internal Jobs in a card-based listing, so that I can browse all eligible opportunities in one place. | - Cards are displayed in a 3-column grid layout. - Each card shows: opportunity type, title (max 2 lines, ellipsis on overflow), posting agency, and commitment/duration. - Listing is sorted by posting date descending; ties broken by opportunity ID. - Closed or expired listings (closing_date in the past) do not appear. - “Careers@Gov” label appears on C@G cards. - Ringfenced Internal Jobs are pinned to the top for eligible officers. - Officers must be authenticated; unauthenticated users are redirected to login. - Page loads a maximum of 15 cards at a time (see OTEP-267 for pagination). | - `oppr_list_view`: time to listing visible on standard government network < 5 secs   - `oppr_detail_view`: % of officers who view at least one detail page | - Default state must handle zero results gracefully (empty state copy — see OTEP-268)   - Visual treatment must distinguish opportunity type without relying on colour alone (accessibility) | - Data source: OTG → OTEP via daily export; confirm schema with Rama   - C@G listings ingested separately — confirm via C@G API   - Confirm session/auth handling with POCDEX integration owner |
| **OTEP-267** | Pagination for the listing page    As an officer, I want to navigate between pages of the opportunity listing, so that I can browse all results beyond the first page. | - Next and Previous controls are shown when results exceed 15 per page. - A page counter is displayed (e.g. “Page 1 of 5”). - Pagination controls are hidden when there are 0 results. - Filter and search selections are retained across pages. | | | |
| **OTEP-268** | Empty, error, and partial-load states    As an officer, I want to see clear feedback when the listing has no results or fails to load, so that I know what happened and what to do next. | - Empty state (no results): display “No opportunities available right now”. - Error state (load failure): display “We couldn’t load opportunities” with a Retry button. - If optional fields are missing on a card, the card renders gracefully without broken layout. | | - Design empty and error state illustrations; keep consistent with OTEP design system | |
| **OTEP-127** ✅ Done (spike) / **OTEP-390, 408, 409** (build) | US-01b - Apply ringfencing criteria to the opportunity listing  As a public service officer, I want the opportunity listing to automatically show only the opportunities I am eligible for, so that I do not waste time on postings I cannot apply for and the hub feels relevant to my situation. | -   I must be logged in to view the listing, else I will be prompted to re-login. [Ref to US on login and SSO]    -   Ringfencing should apply to all opportunities listed on OTEP as per officer’s POCDEX data on login. If officer transferred to another agency, his next login will refresh opportunities displayed as per his new role’s access against ringfencing. | | | OTEP-127 is the completed spike ("Define ringfencing display contract — OTG rules → CareerCompass"). OTEP-390 (detail page states), OTEP-408 (BE eligibility filter), and OTEP-409 (FE reflect ringfenced results) are the runtime build against that contract, currently In Progress/Backlog. OTEP-390's scope explicitly absorbs OTEP-133 (EDM deep-link entry path, ineligible-officer messaging) — see OTEP-390's own row-note below and the now-superseded OTEP-133 row. |
| **OTEP-405** | US-02 — Search opportunities by keyword    As an officer, I want to search opportunities by keyword, so that I can find relevant postings quickly. | - Search field visible on listing page. - Queries across title, description, and agency at minimum. - Results update on submit (no real-time typeahead for MVP). - Zero-results state displays clearly with prompt to broaden search or clear filters. - Works in combination with filters. - Elastic — partial matches and minor typos return relevant results. | - `search_performed`: % of hub sessions that include at least one keyword search   - `search_to_detail`: % of search result views leading to a detail page view   - `search_zero_results`: % of search queries returning zero results | - Search field placement: top of listing, above filters   - Placeholder text: e.g. “Search by role, agency, or keyword”   - Clear/reset affordance required when search is active   - No autocomplete in MVP | - Log search queries as product instrumentation (anonymised) — informs R1 filter design   - Confirm whether OTG export includes sufficient structured text fields for meaningful search |
| **OTEP-86** / **OTEP-437** | US-03 — Filter opportunities by type and category    As an officer, I want to filter the opportunity listing by type (STIP, Gig, SJR, Internal Jobs, C@G) and by category, so that I can narrow down to mobility opportunities relevant to me. | - I can filter by opportunity type; multiple selections allowed. - When a filter is active, I can see clearly which filters are applied. - My filter selections persist as I browse through pages. - Filters work in combination with keyword search. - A tooltip explains what each opportunity type means. - **(OTEP-437) Filter by job family:** officer can filter by WOG job category/family (C@G Indus taxonomy as canonical layer). *(OTEP-318, the earlier category-filter ticket, was superseded by OTEP-437 and deleted from Jira 2026-07-27.)* | - `filter_applied`: % of hub sessions that apply at least one type filter   - `filter_search_applied`: % of sessions using both search and filter   - `filter_to_detail`: % of filtered listing views resulting in a detail page view | - Type filter + C@G indicator only in MVP — no agency, grade, or commitment filters (R1)   - Confirm with BO whether ‘Secondment’ is a distinct type or sub-type of SJR | - No complex filter logic: flat type match, not faceted search   - Filter state: store in URL params so officers can share filtered views |
| **OTEP-317** | Clear filters and reset view    As an officer, I want to clear all my active filters in one action, so that I can quickly return to the full listing. | - If one or more filters are active, a “Clear all” option is visible. - Clicking “Clear all” removes all filter selections and shows the full listing. - If no filters are active, “Clear all” is hidden. | | | |
| **OTEP-128** | US-04 + US-05 (merged) — View opportunity detail page    As an officer, I want to view the complete details of an opportunity on a dedicated page, so that I can make an informed decision before applying.    *(Note: OTEP-128 was repurposed from the type-badge card story to own the detail page. Card fields are now in OTEP-85.)* | - Detail page shows: title, posting agency, opportunity type, start/end dates, application close date, description, and “What you’ll develop” section. - “About this opportunity” section displays all available fields from the opportunity data. - If a mandatory field has no data, it shows “Not specified”. - For Gigs and STIPs: competencies labelled “What you’ll develop” — see OTEP-570 below for per-competency match-state rendering, now confirmed MVP scope (was previously noted here as deferred to R1; corrected 2026-07-27). - Apply CTA is clearly visible without scrolling to the bottom of the page. - Officer can navigate back to the listing with search and filter state preserved (absorbs OTEP-285). - **Detail pages are not publicly accessible — an officer must be logged in to view one.** If an unauthenticated officer opens a deep-link to a specific opportunity, they're sent to log in first, then redirected straight to that opportunity's detail page (not the listing). *(Confirmed by Hao Eng Chua + Léo, Slack, 2026-07-02 — clarifies the existing "loads correctly via bookmark or shared URL" AC, which was silent on the auth gate.)* - Deep-links stay valid as long as the opportunity is still active (not closed or soft-deleted) — see OTEP-129 for the closed/invalid states. | - Card-to-detail rate: % of card views resulting in a detail page view   - Detail-to-apply rate: % of detail page views resulting in an apply action | | - PH note: return-to-page state (formerly OTEP-285) absorbed into this ticket   - Confirm error state for deep-links to missing/unavailable opportunities   - **OTEP-128 is in QA already — verify the built behavior actually redirects post-login to the opportunity page (not the listing) before sign-off; amend the Jira AC if this isn't explicit there.** |
| **OTEP-129 / OTEP-284** | US-06 — See whether an opportunity is open or closed before applying    As an officer, I want to know whether an opportunity is still accepting applications, so that I’m not caught off guard by a posting I can no longer act on. | - OTEP-129: deep-links to closed postings show “This opportunity is no longer available” with a link back to the listing. - OTEP-284 (Sprint 4): “Closing soon” label (≤7 days) on both card and detail page. *(Note: closed postings hidden from listing owned by OTEP-85.)* | | | |
| **OTEP-336** / **OTEP-570** ⚠️ MVP, confirmed 2026-07-27 | Competency match signal on Gig/STIP cards and detail page    As an officer browsing or viewing a Gig/STIP, I want to see at a glance (card) and in detail (detail page) how many of the listed competencies I already have, so that I can quickly identify high-fit opportunities and assess growth potential before applying. | - OTEP-336: competency match count renders on Gig/STIP listing cards when the officer's competency profile is successfully retrieved. - OTEP-570: the "What you'll develop" section on the Gig/STIP detail page renders per-competency match states (have / don't have), not just a flat list. | | | Both currently Backlog as of 2026-07-27 — **confirmed MVP scope**, supersedes the earlier "deferred to R1" note on OTEP-128. Blocking dependency: REQ-X2 (competency-to-opportunity matching, agency-code resolution) is unresolved in the RTM — resolve before these can ship. Also note the RTM's REQ-20 currently (incorrectly) shows this as "✅ Done" — needs correcting to reflect actual Backlog status and MVP scope. |
| **OTEP-319** | US-18 — Apply via FormSG — basic redirect (Internal Jobs, STIPs, Gigs)    As an officer viewing an Internal Job, STIP, or Gig, I want to click “Apply” and be taken to the corresponding FormSG form, so that I can submit my application from the opportunity detail page. | - Clicking “Apply” on an Internal Job, STIP, or Gig detail page opens the FormSG form in a new tab. - If `formsg_url` is missing, I see “Application form unavailable — contact the posting agency” instead of the Apply button. - There is no Apply button on SJR detail pages. - Edge case: if FormSG form is closed or deleted, officer sees a FormSG error page — outside OTEP’s control. Consider showing “Form may no longer be available” guidance. | - `click_to_formsg`: % of Internal Job/STIP/Gig detail page views resulting in a FormSG redirect | | - `formsg_url` field confirmed ✓ (2026-05-21)   - Dependency: OTEP-128 (detail page must exist) — corrected 2026-07-27, was previously miscited as OTEP-87, which is actually the unrelated C@G detail page story |
| ~~OTEP-130~~ **DELETED** | ~~Apply to OTG opportunity via FormSG (full, with webhook) — Sprint 5~~ | Removed from Sprint 4 scope 2026-06-10 (webhook not a must-have; application tracking is an R1 concern — see decisions-log.md 2026-06-10). Ticket key was later reused for a different, unrelated PostHog-tracking scope, then deleted outright from Jira 2026-08-19. This row is kept for historical traceability of the original FormSG-webhook idea only — do not action against the OTEP-130 key, it no longer exists. | — | | Superseded by OTEP-319 (basic redirect, MVP) for the apply path; webhook confirmation remains an open gap — see Section 10 risk: "FormSG remains the completion channel with no webhook confirmation at MVP." |
| **OTEP-131** | US-08 — Handle missing or broken FormSG application link    As an officer, I want to see a clear message if the application link is unavailable, so that I know how to get help rather than facing a broken or missing button. | - If `formsg_url` is missing or empty for an Internal Job, STIP, or Gig, the Apply button is not shown — replaced with “Application form unavailable — contact the posting agency”. - The message is shown in the same position the Apply button would be — no layout shift. - If `formsg_url` is present but the FormSG form is down or closed, the officer lands on FormSG’s own error page — CareerCompass shows no additional error state. | - Missing FormSG link rate: % of STIP/Gig listings where `formsg_url` is null or invalid — feeds data quality monitoring | | Corrected 2026-07-27 — this row was previously miscited as OTEP-87. OTEP-87 is actually "View Careers@Gov Opportunity Detail" (QA status), an unrelated C@G story — see the Careers@Gov section of this table. In Progress as of live Jira pull. |
| **OTEP-132** | US-09 — Apply for an SJR or internal job via OTG redirect    As an officer, I want to be redirected to OTG to apply for SJRs and internal jobs, so that I can complete my application through the correct system. | - SJRs and Internal Jobs have full detail pages on OTEP. - Clicking “Apply via OTG” opens OTG with a direct link to the relevant posting in a new tab. - Before redirect, officer sees: “You’ll be taken to OTG to complete this application. You will need to re-login.” - OTEP captures a click-to-OTG event at the point of redirect. | - Click-to-OTG rate: % of SJR/Internal Job detail page views resulting in an OTG redirect click | | **Deferred to R1.** SJR opportunities also shifted to R1. (Confirmed 2026-06-05.) |
| **OTEP-88** | US-10 — Identify Careers@Gov listings    As an officer, I want to see a clear indicator when a listing comes from Careers@Gov, so that I know upfront where I’ll be directed when I apply or view details. | - All C@G-sourced listings are labelled with “Careers@Gov” on the card. - The label is visible without hovering or clicking into the card. | - C@G listing click-through rate: click-to-C@G events ÷ C@G listing impressions | | |
| **OTEP-87** | View Careers@Gov Opportunity Detail    As an officer actively exploring career moves, I want to view the full details of a Careers@Gov opportunity so I can assess whether it's the right fit and apply directly on the C@G platform. | - Detail page renders the C@G opportunity payload sourced from the C@G API (via OTEP-377). - Fields displayed: title, agency, description, duration, and all available structured job-info fields from the C@G payload. - Responsibilities and pre-requisites are NOT shown inline — officer is directed to click “Apply via Careers@Gov” to find out more, even if the C@G payload includes those fields. - If any displayed field has no data, show “Not specified.” — do not hide the field label. - Layout is consistent with the OTG detail page (OTEP-128). | | | Added 2026-07-27 — this ticket previously had no row of its own; content that belongs here was mistakenly attached to OTEP-131's row (now corrected). QA status as of live Jira pull. Dedicated QA page for this epic is empty — see Section 10 risk table and NEW-18..27 gap cases. |
| **OTEP-89** | US-11	View Careers@Gov opportunity via deep-link      As an officer, I want to click “Apply via Careers@Gov” on the detail page and be taken directly to the opportunity on Careers@Gov, so that I can complete my application through the correct channel without having to search for the role again. | -   C@G detail page in OTEP displays job details sourced from C@G (title, agency, description, duration, and available structure fields)   -   A single prominent CTA is shown: “Apply via Careers@Gov”   -   Clicking the CTA deep-links directly to the specific opportunity on the C@G platform, opening in a new tab.   -   OTEP captures a “click-to-CG” event at the point of redirect.    -   If the opportunity is no longer available on the C@G after the officer clicks through, this is handled entirely on the C@G side - OTEP shows no error state for this scenario.    -   There is no FormSG or OTG application flow for C@G listings. | -   Click-to-C@G rate: % of C@G listing detail page views resulting in a C@G deep-link click |  |  |
| **OTEP-133** ✅ Done, superseded | US-12 — Access the hub via a deep link from an EDM    As an officer, I want to be able to click a link in an email and land directly on the relevant opportunity, so that I can act on opportunities shared with me without navigating from scratch. | - If an officer lands on an opportunity they’re not eligible for, they see a clear message that they are not authorised and are shown alternative opportunities on the page. - The look and feel of the page is aligned with the OTEP theme. | - `edm_to_detail`: deep-link to detail page conversions   - `edm_to_noaccess`: deep-link ineligibility rate | | Corrected 2026-07-27 — the previous "Jira title mismatch" flag was stale/wrong; there is no title mismatch. Per OTEP-133's own Jira description: scope was absorbed into OTEP-390 ("Ringfenced opportunity detail page states") as of 2026-06-05, and OTEP-133 itself is marked Done as a closed/superseded ticket, not an open story. Kept as a row here for US-12/EDM traceability and the two metrics, which remain relevant — but OTEP-390 is the ticket to track for actual build status. |

### Out of scope (MVP) — confirmed 2026-07-27

These live in Jira under Epic 4 but are confirmed **not** part of MVP. Listed here so they read as deliberate deferrals, not gaps the PRD missed.

| Ticket | Feature | Target |
|---|---|---|
| OTEP-197, OTEP-425 | Bookmarking (view/save bookmarked opportunities) | R1 |
| OTEP-281 | Listing — data-fetching loading states | Post-MVP polish |
| OTEP-282 | Listing — truncate long opportunity titles | Post-MVP polish |
| OTEP-404 | Listing — responsive page sizing for tablet/mobile | Post-MVP polish |
| OTEP-614, OTEP-615 | Advanced/competency-based filters; suggested search after 3 characters | Future scope — both still at spike/discovery stage, no story written yet |

*(OTEP-336/OTEP-570 — competency match signal — moved back into scope, confirmed MVP 2026-07-27. See the OTEP-336/570 row in the scope table above.)*

---

## 9. Go-To-Market Plan (To be discussed)

**Purpose:** Shipping ≠ adoption. Think of what you need to do to drive adoption and scale. 

- Target launch group: 1-2 Agencies that actively post Gigs
  - prefer agencies with:
    - higher posting volume
    - willing HR partner
- Comms plan:
- Training / enablement:
- Change management:
- Support model:

**Phases:**

- Pilot: When
- Scale: When
- Steady state: When 

## 10. Risks, Assumptions & Mitigations

**Purpose:** Surface what could go wrong or what we're assuming is true, before it becomes a launch-week surprise. Populated 2026-07-27 from the launch checklist, RTM open items, Pow Hwee's Coverage Targets assessment, and this week's scope decisions — not hypothetical, all traced to a live source.

### Risks

| **Risk** | **Type** | **Likelihood** | **Impact** | **Mitigation** |
|---|---|---|---|---|
| VAPT timeline likely pushes go-live past the stated Oct 19–23 target — the 23 Jun readiness review puts VAPT + remediation at up to 2 months post-code-freeze, pushing realistic go-live to November | Timeline | High | High | Escalate now to Adrian/Jace with a clear recommendation — don't wait for the date to slip visibly. |
| OTG UAT read-replica data is too unclean for meaningful test data — blocks both testing and data alignment | Data quality | High (already confirmed unclean) | High — UAT results become unreliable | Daryll/Pow Hwee resolve before UAT starts (open item #33). |
| Ringfencing behavior against incomplete/partial POCDEX profile data is untested | Coverage gap | High (no test case exists yet) | Medium-High — silent wrong-access at scale | Write an explicit test case for officers with partial/missing POCDEX data before UAT; reserve the 3 ringfencing test personas (eligible/ineligible/incomplete-profile) — RTM open item 7. |
| Ringfencing correctness may share a root cause with an open jobID/competency data bug (flagged as "currently being investigated by Rama" in the Confluence Success Criteria appendix) | Data integrity | Unknown — status unconfirmed, not corroborated anywhere else in RTM/UAT tracking | Potentially High if still live | Confirm current status with Rama before treating this as either resolved or an active blocker. |
| C@G apply flow (OTEP-88/87) has zero QA test coverage — the dedicated QA page is empty, despite this being a P0 officer-facing feature | Coverage gap | Confirmed (0 cases exist) | High | Prioritize the 10 drafted gap cases (NEW-18..27, Pow Hwee's Coverage Targets doc). |
| Category filter (OTEP-437) sits in QA with zero cases written — blocks the ticket's exit from QA | Coverage gap | Confirmed | High — blocking | Prioritize the 14 drafted gap cases (NEW-04..17). |
| REQ-X2 (competency-to-opportunity agency-code resolution) is unresolved — now a real MVP blocker since OTEP-336/570 were confirmed in scope 2026-07-27 | Technical dependency | Confirmed unresolved | High — blocks confirmed MVP scope, not just future work | Escalate REQ-X2 resolution now that it gates a committed MVP feature, not deferred scope. |
| No documented rollback plan for the data pipeline or ringfencing (R1 has one; Opportunities doesn't) | Operational readiness | Confirmed gap | High if a post-launch failure occurs | Decide and document before go-live. Draft criteria exist: ringfencing blocking eligible officers → disable ringfencing, show unfiltered listing with a banner, escalate to Pow Hwee; ingestion pipeline failure → fall back to last-known-good cached listing, alert Engineering. |
| Guardrail metrics (submission error rate, confirmation email delivery rate) are defined in Section 7.3 but have no assigned owner or numeric threshold | Operational readiness | Confirmed gap | Medium — a real failure could go unwatched | Assign explicit owners and numeric thresholds before UAT, not launch week. |
| Missing-`formsg_url` test data may not exist in the UAT dataset — Sprint 5 comments flagged the source Excel was missing POC data for many opportunities | Data availability | Medium-High | Medium — one specific edge case untestable, not systemic | Confirm this data state is genuinely reproducible in the reserved UAT dataset before handing the corresponding test case to a BO. |
| No named end-to-end launch readiness owner | Ownership gap | Confirmed as of launch checklist | High — cross-stream gaps (UAT/VAPT/data/onboarding/comms) likely repeat without one | Name an owner this week. |

### Assumptions

| **Assumption** | **Risk if wrong** |
|---|---|
| POCDEX profile data (agency, job family) is accurate and current at login time | Ringfencing silently shows wrong opportunities to officers — no error surfaces to flag it |
| OTG export contains sufficient structured title/description fields for meaningful keyword search | Search returns false negatives silently, not visible errors |
| C@G data return is not expected at MVP (deep-links only, no confirmation loop back to OTEP) | If a C@G posting goes stale between syncs, officers click through to a dead or wrong posting with no OTEP-side detection |
| FormSG remains the completion channel with no webhook confirmation at MVP (OTEP-130 deferred) | OTEP has no ground truth on whether an application actually completed — undermines verifying the North Star's "completed development action" definition for this channel |
| The 6-agency staged pilot (PSD, ESG, MDDI, URA, MCCY, CAAS) is representative enough to validate before wider rollout | Issues specific to non-pilot agencies' data or org structure only surface after wider launch |

## 11. Dependencies & Assumptions

System Dependencies

**Systems depended on: **OTG / WG-managed opportunity lists (Excel input); Careers@Gov (deep-links only, no data return expected at MVP); Email delivery service (Fabian/Infra)

**OTG ingestion status (as of 2026-07-27):** the base pipeline is built and done (OTEP-192 data ingestion, OTEP-223 opportunity-type prep, plus 3 completed spikes on nil-date handling, Excel upload flow, and ingestion-logic tightening). Two hardening items remain open and unscheduled: OTEP-348 (scheduler & observability) and OTEP-403 (import hardening). Neither blocks MVP launch, but both are directly relevant to the OTG UAT read-replica data-quality risk already flagged in the launch checklist (open item #33) — unclean UAT test data traces back to this same pipeline.

**Teams needed:** Pathfinder squad (build); QA (test coverage — see Coverage Targets doc for current gaps); Infra/Fabian (email delivery); Rama (POCDEX/ringfencing data alignment, and the open jobID/competency bug referenced in Section 10); Pow Hwee (data quality, VAPT scope, rollback plan ownership per launch checklist); Data Office (approval, blocking deploy per launch checklist open item).

**Policy assumptions:** *(not yet populated — needs input from BO/policy owner, no source document in this workspace addresses this directly. Do not treat as confirmed until filled.)*

**Data availability assumptions:** POCDEX profile data (agency, job family) assumed accurate and current at login — see Section 10 assumptions table for the risk if this doesn't hold. OTG export assumed to carry sufficient structured title/description fields for search. C@G data assumed one-way (deep-link only, no return sync) for MVP. Missing-`formsg_url` test data assumed to exist in the UAT dataset — **unconfirmed, flagged as a risk in Section 10.**

 

## 12. Decision Tracker (If needed)

**Purpose:** Make it actionable.

| **Decision required** | **Owner** | **Review date** | **Status** |
|---|---|---|---|
| Steering approval to proceed with Opportunities MVP build | PS/DS | **2 April 2026** | *Approved on 2 April* |
| **US-09 - Apply for a STIP or Gig via FormSG link**<br><br>**Auto-Populated Fields:** The BO also noted that since the officer must log into OTEP before signing up, the system should capture their basic profile information on the backend so they do not have to manually fill it out again. These fields include:<br>- Full Name<br>- Designation<br>- Division & Department<br>- Ministry / Agency<br>- Work Email |  |  |  |
| **Proposed changes for Application fields** (for MVP, we keep it as current ie no changes to the FormSG forms)<br><br>**Fields to Retain / Add:**<br>- **Contact Number**.<br>- **Reporting Officer’s Name and Email:** These are retained specifically to trigger an automated email notifying the supervisor of the application, helping keep the process transparent and combat dropout rates.<br>- **Job Grade:** This replaces the legacy question asking if the officer is an individual contributor or team leader. It will be a dropdown list of MX grades with an "Others" option for non-MX tracks.<br>- **Main reason for application**.<br>- **Meet pre-requisites**.<br>- **Declarations:** Retained, though the BO noted that different sets of declarations may be needed depending on whether the posting is a STIP or a Gig.<br>- **Custom Questions:** The BO requested functionality allowing opportunity posters to add custom questions for their specific postings, similar to the FormSG form builder.<br><br>**Fields to Drop:**<br>- **HR Officer’s Name and Email:** Dropped because this information was rarely utilized and often caused confusion for applicants.<br>- **"Where did you find out about this opportunity?":** Dropped because all traffic will now route centrally through OTEP. |  |  |  |

---

# Success Criteria for Epic 4 — Opportunities

**Format:** Per feature/epic, two tiers:
- **Standard success criteria** — the happy-path outcome that proves the feature does its core job
- **Edge case / data success criteria** — the boundary conditions and data states that must also hold, separate from the happy path because they usually get missed if only the standard criteria are checked

## Epic: Opportunities Listing (OTEP-85, 267, 268)

**Standard success criteria:**
- An officer logs in and sees a 3-column grid of open opportunity cards, sorted newest-first, up to 15 per page.
- Each card shows Title, Agency, Posting Date (absolute format), and Type.
- Pagination controls appear only when there are more than 15 open opportunities.

**Edge case / data success criteria:**
- Closed opportunities never appear in the listing, regardless of how recently they closed.
- With exactly 15 or fewer opportunities, pagination controls are fully absent (not shown-but-disabled).
- With zero open opportunities, the officer sees a clear "no opportunities available" message — not a blank page or error.
- Data dependency: listing data must carry accurate `closing_date` values; a stale or missing closing date silently breaks the closed-opportunity exclusion rule above.

## Epic: Filtering (OTEP-86, 437, 317)

**Standard success criteria:**
- Selecting a single opportunity type (Jobs, STIPs, Gigs) narrows the listing to only that type.
- Selecting multiple types shows the union of those types.

**Edge case / data success criteria:**
- An active filter persists correctly when the officer pages forward/backward.
- A filter combination matching zero opportunities shows the same empty state as the zero-results listing case, not a broken or blank view.
- "Clear all" resets every active filter in one action and disappears from view once nothing is filtered.
- "Clear all" must not appear at all when no filters are active.
- Data dependency: category/job-family filtering runs through OTEP-437 (C@G Indus taxonomy as canonical layer). *(OTEP-318, the earlier category-filter ticket referenced in an older draft of this page, was superseded by OTEP-437 and deleted from Jira 2026-07-27 — success criteria above are written against OTEP-437.)*

## Epic: Search (OTEP-405)

**Standard success criteria:**
- Search returns opportunities matching the entered keyword, case-insensitive, including partial matches.
- Search UI is placed consistently and doesn't shift other page layout.

**Edge case / data success criteria:**
- A search with zero matches shows the standard empty state, not an error.
- Search combined with an active filter returns the intersection of both, not just one or the other.
- Data dependency: search relies on OTG opportunity data carrying complete, correctly-indexed title/description fields — incomplete OTG payloads will silently produce false negatives, not visible errors.

## Epic: Opportunity Detail Page (OTEP-128, 129, 284)

**Standard success criteria:**
- Clicking into an opportunity from the listing shows full detail: Title, Agency, Posting Date, Closing Date, Type, Description, "What you'll develop," Commitment type.
- "Back to opportunities" returns the officer to the listing.
- The detail page loads correctly via a direct or bookmarked URL, not only via listing click-through.

**Edge case / data success criteria:**
- An invalid or nonexistent opportunity ID shows a clean "not found" state with a link back to the listing — never a broken page.
- A deep link to an opportunity that has since closed shows a clear "no longer available" message, not the normal detail view.
- The "Closing soon" badge appears only when closing within 7 days and strictly in the future — never for evergreen (no closing date) opportunities.
- Data dependency: badge logic depends on accurate `closing_date`; a null or malformed date must default to "no badge," not a crash or false badge.

## Epic: Ringfencing (OTEP-127, 390, 408, 409)

**Standard success criteria:**
- An eligible officer sees the full detail page for a ringfenced opportunity as normal.
- An ineligible officer sees a distinct ringfenced/ineligible state on the same opportunity, not the standard detail view.

**Edge case / data success criteria:**
- Ringfencing rules (Master Switch, Include/Exclude by agency) apply correctly when combined — e.g. Master Switch off should show all opportunities regardless of include/exclude rules underneath.
- Not yet testable: officer personas for "incomplete profile data" and "explicitly ineligible" are not yet defined or reserved — this is a real gap, not a documentation gap. Success criteria above can't be verified end-to-end until these two persona types exist in the UAT dataset. *(Matches RTM open item 7 — corroborated independently.)*
- Data dependency: ringfencing correctness depends on the officer's profile carrying accurate agency/competency data. **Open question, unresolved as of this draft:** an earlier version of this page linked this to "the same structural dependency flagged in a jobID/competency bug currently being investigated by Rama" — confirm this is still live and current before treating it as resolved or stale; it doesn't appear in the RTM or UAT tracking docs, so it may be a genuinely untracked risk.

## Epic: Apply — Careers@Gov (OTEP-88, 89, 87)

**Standard success criteria:**
- A C@G-sourced opportunity's detail page shows title, agency, description, duration, and available structured fields in the same layout as an OTG opportunity.
- "Apply via Careers@Gov" opens a new tab that deep-links directly to that specific posting — never the C@G homepage.

**Edge case / data success criteria:**
- Responsibilities and pre-requisite fields present in the C@G payload are intentionally NOT shown in CareerCompass, even when the data exists — officer must be directed to Careers@Gov for that detail.
- If a C@G posting is taken down after the officer clicks through, CareerCompass shows no additional error state — this is handled entirely by Careers@Gov.
- The C@G detail page shows exactly one apply path (Apply via Careers@Gov) — no FormSG or OTG-native apply CTA should ever appear alongside it.
- Data dependency: this epic's dedicated QA page (OTEP-88/87) is empty — success criteria above are defined but unverified as of this draft. 10 gap cases are drafted (NEW-18..27) to close this.

## Epic: Apply — FormSG / CareerCompass-Native (OTEP-319, 131)

**Standard success criteria:**
- Clicking "Apply" opens the correct FormSG form for that specific opportunity in a new tab.
- Each opportunity's Apply button opens its own form — never a form belonging to a different opportunity.

**Edge case / data success criteria:**
- An opportunity with no `formsg_url` configured shows a clear fallback message ("Application form unavailable — contact the posting agency") in place of the Apply button, with no layout shift.
- If the FormSG form itself is down or closed, the officer sees FormSG's own error page — CareerCompass shows no additional error state.
- Data dependency: this is the highest-risk data gap in the whole plan. Sprint 5 comments flagged that the source Excel was missing POC data for many opportunities — before the missing-URL fallback case can be considered testable, confirm this data state is genuinely reproducible in the UAT dataset, not assumed.
- **SJR note:** confirmed 2026-07-27 that there will be no SJRs — the prior OTEP-128/OTEP-131 contradiction over SJR apply-button treatment is moot. Update RTM open item 11 to reflect this.
