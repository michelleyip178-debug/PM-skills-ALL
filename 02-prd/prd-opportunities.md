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
| **OTEP-127** | US-01b - Apply ringfencing criteria to the opportunity listing  As a public service officer, I want the opportunity listing to automatically show only the opportunities I am eligible for, so that I do not waste time on postings I cannot apply for and the hub feels relevant to my situation. | -   I must be logged in to view the listing, else I will be prompted to re-login. [Ref to US on login and SSO]    -   Ringfencing should apply to all opportunities listed on OTEP as per officer’s POCDEX data on login. If officer transferred to another agency, his next login will refresh opportunities displayed as per his new role’s access against ringfencing. |  |  |  |
| **OTEP-91** | US-02 — Search opportunities by keyword    As an officer, I want to search opportunities by keyword, so that I can find relevant postings quickly. | - Search field visible on listing page. - Queries across title, description, and agency at minimum. - Results update on submit (no real-time typeahead for MVP). - Zero-results state displays clearly with prompt to broaden search or clear filters. - Works in combination with filters. - Elastic — partial matches and minor typos return relevant results. | - `search_performed`: % of hub sessions that include at least one keyword search   - `search_to_detail`: % of search result views leading to a detail page view   - `search_zero_results`: % of search queries returning zero results | - Search field placement: top of listing, above filters   - Placeholder text: e.g. “Search by role, agency, or keyword”   - Clear/reset affordance required when search is active   - No autocomplete in MVP | - Log search queries as product instrumentation (anonymised) — informs R1 filter design   - Confirm whether OTG export includes sufficient structured text fields for meaningful search |
| **OTEP-86** / **OTEP-318** | US-03 — Filter opportunities by type and category    As an officer, I want to filter the opportunity listing by type (STIP, Gig, SJR, Internal Jobs, C@G) and by category, so that I can narrow down to mobility opportunities relevant to me. | - I can filter by opportunity type; multiple selections allowed. - When a filter is active, I can see clearly which filters are applied. - My filter selections persist as I browse through pages. - Filters work in combination with keyword search. - A tooltip explains what each opportunity type means. - **(OTEP-318) Filter by category:** officer can filter by opportunity category (ACs TBC — no Jira description yet; confirm at Sprint 3 grooming). | - `filter_applied`: % of hub sessions that apply at least one type filter   - `filter_search_applied`: % of sessions using both search and filter   - `filter_to_detail`: % of filtered listing views resulting in a detail page view | - Type filter + C@G indicator only in MVP — no agency, grade, or commitment filters (R1)   - Confirm with BO whether ‘Secondment’ is a distinct type or sub-type of SJR | - No complex filter logic: flat type match, not faceted search   - Filter state: store in URL params so officers can share filtered views |
| **OTEP-317** | Clear filters and reset view    As an officer, I want to clear all my active filters in one action, so that I can quickly return to the full listing. | - If one or more filters are active, a “Clear all” option is visible. - Clicking “Clear all” removes all filter selections and shows the full listing. - If no filters are active, “Clear all” is hidden. | | | |
| **OTEP-128** | US-04 + US-05 (merged) — View opportunity detail page    As an officer, I want to view the complete details of an opportunity on a dedicated page, so that I can make an informed decision before applying.    *(Note: OTEP-128 was repurposed from the type-badge card story to own the detail page. Card fields are now in OTEP-85.)* | - Detail page shows: title, posting agency, opportunity type, start/end dates, application close date, description, and “What you’ll develop” section. - “About this opportunity” section displays all available fields from the opportunity data. - If a mandatory field has no data, it shows “Not specified”. - For Gigs and STIPs: competencies labelled “What you’ll develop” — no matching logic, no personalisation (competency match ratio is deferred to R1). - Apply CTA is clearly visible without scrolling to the bottom of the page. - Officer can navigate back to the listing with search and filter state preserved (absorbs OTEP-285). - **Detail pages are not publicly accessible — an officer must be logged in to view one.** If an unauthenticated officer opens a deep-link to a specific opportunity, they're sent to log in first, then redirected straight to that opportunity's detail page (not the listing). *(Confirmed by Hao Eng Chua + Léo, Slack, 2026-07-02 — clarifies the existing "loads correctly via bookmark or shared URL" AC, which was silent on the auth gate.)* - Deep-links stay valid as long as the opportunity is still active (not closed or soft-deleted) — see OTEP-129 for the closed/invalid states. | - Card-to-detail rate: % of card views resulting in a detail page view   - Detail-to-apply rate: % of detail page views resulting in an apply action | | - PH note: return-to-page state (formerly OTEP-285) absorbed into this ticket   - Confirm error state for deep-links to missing/unavailable opportunities   - **OTEP-128 is in QA already — verify the built behavior actually redirects post-login to the opportunity page (not the listing) before sign-off; amend the Jira AC if this isn't explicit there.** |
| **OTEP-129 / OTEP-284** | US-06 — See whether an opportunity is open or closed before applying    As an officer, I want to know whether an opportunity is still accepting applications, so that I’m not caught off guard by a posting I can no longer act on. | - OTEP-129: deep-links to closed postings show “This opportunity is no longer available” with a link back to the listing. - OTEP-284 (Sprint 4): “Closing soon” label (≤7 days) on both card and detail page. *(Note: closed postings hidden from listing owned by OTEP-85.)* | | | |
| **OTEP-319** | US-18 — Apply via FormSG — basic redirect (Internal Jobs, STIPs, Gigs)    As an officer viewing an Internal Job, STIP, or Gig, I want to click “Apply” and be taken to the corresponding FormSG form, so that I can submit my application from the opportunity detail page. | - Clicking “Apply” on an Internal Job, STIP, or Gig detail page opens the FormSG form in a new tab. - If `formsg_url` is missing, I see “Application form unavailable — contact the posting agency” instead of the Apply button. - There is no Apply button on SJR detail pages. - Edge case: if FormSG form is closed or deleted, officer sees a FormSG error page — outside OTEP’s control. Consider showing “Form may no longer be available” guidance. | - `click_to_formsg`: % of Internal Job/STIP/Gig detail page views resulting in a FormSG redirect | | - `formsg_url` field confirmed ✓ (2026-05-21)   - Dependency: OTEP-87 (detail page must exist) |
| **OTEP-130** | Apply to OTG opportunity via FormSG (full, with webhook) — Sprint 5    As an officer, I want to apply to a STIP or Gig via FormSG with OTEP receiving confirmation, so that my application is recorded on OTEP. | - Apply button is labelled “Apply via FormSG”. - FormSG opens in a new tab. - A webhook between FormSG and OTEP receives submission confirmation. - On webhook confirmation, OTEP records the submission event against the officer and opportunity ID. - After submission, officer receives an email notification. - Opportunity poster also receives an email notification with applicant details. | - `formsg_webhook_received`: % of FormSG redirects that result in a confirmed webhook callback | | - Webhook setup required between FormSG and OTEP   - Confirm whether FormSG supports pre-fill via URL params (open item #14, Pow Hwee) |
| **OTEP-87** ⚠️ | US-08 — Handle missing or broken FormSG application link    As an officer, I want to see a clear message if the FormSG application link is unavailable, so that I know how to get help rather than facing a broken or missing button. | - If the FormSG link for an opportunity is unavailable, a disabled CTA is shown with: “Application form unavailable — contact [Agency POC] directly”.   ⚠️ **Jira ACs mismatch**: Jira OTEP-87 title is “View Opportunity Detail” and includes competency match ratio scope that has been deferred to R1. Missing-FormSG-link handling may belong to OTEP-131 (confirm at grooming). **Reconcile Jira ACs before Sprint 3 grooming.** | - Missing FormSG link rate: % of STIP/Gig listings where `formsg_url` is null or invalid — feeds data quality monitoring | | |
| **OTEP-132** | US-09 — Apply for an SJR or internal job via OTG redirect    As an officer, I want to be redirected to OTG to apply for SJRs and internal jobs, so that I can complete my application through the correct system. | - SJRs and Internal Jobs have full detail pages on OTEP. - Clicking “Apply via OTG” opens OTG with a direct link to the relevant posting in a new tab. - Before redirect, officer sees: “You’ll be taken to OTG to complete this application. You will need to re-login.” - OTEP captures a click-to-OTG event at the point of redirect. | - Click-to-OTG rate: % of SJR/Internal Job detail page views resulting in an OTG redirect click | | **Deferred to R1.** SJR opportunities also shifted to R1. (Confirmed 2026-06-05.) |
| **OTEP-88** | US-10 — Identify Careers@Gov listings    As an officer, I want to see a clear indicator when a listing comes from Careers@Gov, so that I know upfront where I’ll be directed when I apply or view details. | - All C@G-sourced listings are labelled with “Careers@Gov” on the card. - The label is visible without hovering or clicking into the card. | - C@G listing click-through rate: click-to-C@G events ÷ C@G listing impressions | | |
| **OTEP-89** | US-11	View Careers@Gov opportunity via deep-link      As an officer, I want to click “Apply via Careers@Gov” on the detail page and be taken directly to the opportunity on Careers@Gov, so that I can complete my application through the correct channel without having to search for the role again. | -   C@G detail page in OTEP displays job details sourced from C@G (title, agency, description, duration, and available structure fields)   -   A single prominent CTA is shown: “Apply via Careers@Gov”   -   Clicking the CTA deep-links directly to the specific opportunity on the C@G platform, opening in a new tab.   -   OTEP captures a “click-to-CG” event at the point of redirect.    -   If the opportunity is no longer available on the C@G after the officer clicks through, this is handled entirely on the C@G side - OTEP shows no error state for this scenario.    -   There is no FormSG or OTG application flow for C@G listings. | -   Click-to-C@G rate: % of C@G listing detail page views resulting in a C@G deep-link click |  |  |
| **OTEP-133** ⚠️ | US-12 — Access the hub via a deep link from an EDM    As an officer, I want to be able to click a link in an email and land directly on the relevant opportunity, so that I can act on opportunities shared with me without navigating from scratch. | - If an officer lands on an opportunity they’re not eligible for, they see a clear message that they are not authorised and are shown alternative opportunities on the page. - The look and feel of the page is aligned with the OTEP theme.   ⚠️ **Jira title mismatch**: Jira OTEP-133 title is “Access the hub via a deep link from an EDM” — verify this matches US-12 intent at next sync. | - `edm_to_detail`: deep-link to detail page conversions   - `edm_to_noaccess`: deep-link ineligibility rate | | |

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

**Purpose:** 

| **Risk / Assumption** | **Type** | **Likelihood** | **Impact** | **Mitigation** |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 11. Dependencies & Assumptions

System Dependencies

**Systems depended on: **OTG / WG-managed opportunity lists (Excel input); Careers@Gov (deep-links only, no data return expected at MVP); Email delivery service (Fabian/Infra)

**Teams needed: **

**Policy assumptions: **

**Data availability assumptions: **

 

## 12. Decision Tracker (If needed)

**Purpose:** Make it actionable.

| **Decision required** | **Owner** | **Review date** | **Status** |
|---|---|---|---|
| Steering approval to proceed with Opportunities MVP build | PS/DS | **2 April 2026** | *Approved on 2 April* |
| **US-09 - Apply for a STIP or Gig via FormSG link**<br><br>**Auto-Populated Fields:** The BO also noted that since the officer must log into OTEP before signing up, the system should capture their basic profile information on the backend so they do not have to manually fill it out again. These fields include:<br>- Full Name<br>- Designation<br>- Division & Department<br>- Ministry / Agency<br>- Work Email |  |  |  |
| **Proposed changes for Application fields** (for MVP, we keep it as current ie no changes to the FormSG forms)<br><br>**Fields to Retain / Add:**<br>- **Contact Number**.<br>- **Reporting Officer’s Name and Email:** These are retained specifically to trigger an automated email notifying the supervisor of the application, helping keep the process transparent and combat dropout rates.<br>- **Job Grade:** This replaces the legacy question asking if the officer is an individual contributor or team leader. It will be a dropdown list of MX grades with an "Others" option for non-MX tracks.<br>- **Main reason for application**.<br>- **Meet pre-requisites**.<br>- **Declarations:** Retained, though the BO noted that different sets of declarations may be needed depending on whether the posting is a STIP or a Gig.<br>- **Custom Questions:** The BO requested functionality allowing opportunity posters to add custom questions for their specific postings, similar to the FormSG form builder.<br><br>**Fields to Drop:**<br>- **HR Officer’s Name and Email:** Dropped because this information was rarely utilized and often caused confusion for applicants.<br>- **"Where did you find out about this opportunity?":** Dropped because all traffic will now route centrally through OTEP. |  |  |  |
