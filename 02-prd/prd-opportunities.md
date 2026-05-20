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

**Current State **

Prior to OTEP, all applications went through standalone FormSG links distributed by host agencies or via Careers@Gov. There is no central discovery point. The decision to replace FormSG with an OTEP-hosted application flow was confirmed at the 12 March session.

### **Why Now / What Changed**

| **What has changed** | **Why it creates urgency** |
|---|---|
| Leadership emphasis on competency-driven growth | Mobility participation is increasingly expected. The programme needs infrastructure that matches this expectation. |
| Opportunities visible but fragmented across channels | Officers are actively seeking opportunities but encountering inconsistent information and unequal access. Centralization addresses this directly. |

## 2. Problem Statement

**Purpose:** Clearly define the problem before jumping to solution. 

[User] struggles to [do what] because [root cause], resulting in [negative outcome].

> 

*Officers ***struggle to discover and apply for development opportunities **because they are **fragmented across multiple portals, **resulting in confusion on validity of job postings and friction for officers to have a single view of all short term and long term opportunities.

*Host agencies face the same problem in reverse: no operational visibility into applicants, manual sign-up tracking, and no feedback loop on whether opportunities actually filled. *

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

- 

STIPs: 4,056 vacancies vs 6,411 sign-ups — this is where OTEP’s application standardisation has the biggest impact by volume

- 

Gigs: 696 vacancies vs 686 sign-ups — roughly balanced; concentrated in Q2 with near-zero in Q4

**Data caveat:**

- 

This dataset captures sign-ups/interest, not attendance or confirmed fill rates. Attendance data is incomplete and not tracked centrally.

- 

What we can claim: scale of officer demand and supply capacity. What we cannot claim from this data alone: actual fill rates or conversion to confirmed placements.

- 

FormSG submission volumes (channel baseline for OTEP migration target) still to be pulled by Engineering.

## 4. Market / Benchmark Scan

**Purpose:** Avoid reinventing the wheel. Find out how other teams or companies solves a similar problem. Designers can help with this. 

- 

How do others solve this? 

- 

Known best practices or patterns

- 

What we should copy vs avoid

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

> 

If we provide a unified Opportunities Hub within OTEP *[capability]*, then government officers *[user]* will be able to discover and apply for development opportunities in one place, without relying on informal networks or navigating multiple systems *[new behaviour]*, leading to increased application completion rate and channel migration from FormSG to OTEP *[measurable outcome]*.

## 7. Success Metrics

**Purpose:** Define what “good” looks like across a progression of three stages. Each stage unlocks the next as data and infrastructure mature. MVP is accountable for Stage 1 only - but must build the foundation for Stages 2 and 3. 

**7.1  Outcome Metrics (North Star)**

- 

Application Completion Rate — forms submitted ÷ Apply button clicks × 100

- 

Channel migration: ≥50% of total STIP/Gigs applications submitted via OTEP by Month 3

**7.2  Input Metrics**

- 

% of Click-through rate (listing page → detail page)

- 

% of Apply click rate (detail page → form)

- 

% of Form field drop-off rate: no single field should cause abandonment

**7.3  Guardrail Metrics (Events that will lead to rollback or pause)**

- 

% of Submission error rate → pause and investigate (Engineering)

- 

% of Confirmation email delivery rate → escalate to Infra 

## 8. Scope (Stories + Success Criteria)

### [Segment 1] Foundation - Shared across all opportunity types

### Browser, Search, Filter, Cards, Detail Pages & Instrumentation

| **Jira ID** | **User Story** | **Acceptance Criteria** | **Success Metrics / What to Track** | **Notes for Designer** | **Notes for Engineer** |
|---|---|---|---|---|---|
|  | US-01 - View all opportunities in one hub      As an officer, I want to see all STIPs, Gigs, SJRs and Jobs in a single place, so that I don’t have to navigate multiple channels to discover mobility opportunities. | -   When I click on “Jobs & Opportunities”, all opportunity types appear in the same listing view on load.    -   Listings display in a default sort order of most recently posted.   -   Ringfenced internal jobs are prioritized on top of the default listing before other opportunity types; within that group, sort is also by modified timestamp.    -   There are filters or filter panel.    -   A sticky search bar is visible at the top of the page as I scroll.   -   A “Back to Top” button floats on screen and returns me to the search bar when tapped.    -   C@G listings are labelled with “Careers@Gov”.   -   The listing should be refreshed daily.    -   Officers must be authenticated to view the hub: unauthenticated users are redirected to login.    -   [Question] What about evergreen / long-running postings with old creation dates but recently modified? | -   `oppr_list_view`: Time to listing visible on standard government network < 5 secs?   -   `oppr_detail_view`: % of officers who view at least one detail page | -   Default state must handle zero results gracefully (empty state copy needed)   -   Pagination recommended for performance   -   Visual treatment must distinguish opportunity type clearly without relying on colour alone (accessibility) | -   Data source: OTG → OTEP via export (daily delta - confirm with Rama). Rama to confirm data schema and field mapping before build   -   Careers@Gov listings ingested separately — confirm whether via C@G API    -   Confirm session/auth handling with POCDEX integration owner |
| **OTEP-127** | US-01b - Apply ringfencing criteria to the opportunity listing  As a public service officer, I want the opportunity listing to automatically show only the opportunities I am eligible for, so that I do not waste time on postings I cannot apply for and the hub feels relevant to my situation. | -   I must be logged in to view the listing, else I will be prompted to re-login. [Ref to US on login and SSO]    -   Ringfencing should apply to all opportunities listed on OTEP as per officer’s POCDEX data on login. If officer transferred to another agency, his next login will refresh opportunities displayed as per his new role’s access against ringfencing. |  |  |  |
| **OTEP-86** | US-02 - Search opportunities by keyword      As an officer, I want to switch from discovery landing to a full listing of all eligible opportunities, so that I can browse opportunities | -   When a search bar is visible and as I type, i see suggested search terms to help me refine my query.    -   Listings page will refresh after i click search or press enter, not on every keystroke.    -   search works across all oppr titles, description, agency name at minimum.    -   if i select filters with in the search results, search will works in combination with the selected filters and refresh the listing   -   Zero-results state displays clearly with prompt to broaden search or clear filters.    -   i can clear my search and return to full listing easily.    -   Search is elastic - partial matches and minor typos return relevant results. | -   `search_performed`: % of hub sessions that include at least one keyword search    -   `search_to_detail` : % of search result views that lead to a detail page view    -   `search_zero_results` : % of search queries returning zero results | -   Search field placement: top of listing, above filters — do not bury it   -   Placeholder text should set expectations: e.g. 'Search by role, agency, or keyword'   -   Clear/reset affordance required when a search is active   -   No autocomplete or suggested searches in MVP | -   Log search queries as product instrumentation (anonymised) — informs R1 filter design   -   to confirm whether OTG export includes sufficient structured text fields for meaningful search |
|  | US-03 - Filter opportunity by type     As an officer, I want to filter the opportunity listing by type (STIP, Gig, SJR, Internal Jobs, C@G Public Facing jobs ), so that I can narrow down to the categories of mobility relevant to me. | -   I can filter listing by oppr types.   -   I can select more than one at a time   -   When a filter is active, i can see clearly which filters are applied   -   my filter selection remains in place as I browse through pages    -   I can clear all filters in one action and see full listing   -   filters work in combination with keyword search   -   have a tooltip to explain what each opportunity type is. | -   `filter_applied`: % of hub sessions that apply at least one type filter    -   `filter_search_applied`: % of sessions using both search and filter    -   `filter_to_detail`: % of filtered listing views resulting in a detail page view | -   Brief is explicit: type filter + C@G indicator only — no agency, grade, or commitment filters for MVP (these are R1)   -   Confirm with BO whether 'Secondment' is a distinct type or sub-type of SJR - Secondment is a more generic deployment than SJR. | -   No complex filter logic: this is a flat type match, not a faceted search   -   Filter state: store in URL params so officers can share or bookmark filtered views |
| **OTEP-128** | US04 - View structured opportunity card      As an officer, I want each opportunity card to show the key information at a glance (type, title, agency, duration), so that I can assess basic fit before deciding whether to read the full details. | -   each card minimally shows: oppr type, title (max 2 lines), posting agency, commitment.   -   Title truncation is consistent across all cards: max 2 line, ellipsis at overflow.   -   Cards show a relative posting date label based on created timestamp: “Posted today” / “Posted 1 week ago” / “Posted 1 month ago” / “Posted more than 3 months ago”    -   each card display the posting ministry’s icon alongside the agency name.   -   For Gigs and STIPs: competency pills are not shown on the card - competencies surface on the detail page only.    -   For Jobs: competency match ratio (X/Y) on card.   -   cards are of fixed-size or same size.    -   only open / active opportunities will appear in the listing | -   Card-to-detail rate: % of card views resulting in a detail page view | -   Fixed-size cards are a firm brief requirement — detail overflow must go to the View Details page, not expand in-card |  |
|  | US-05 View full opportunity detail page    As an officer, I want to view the complete details of an opportunity on a dedicated page (eligibility, developmental outcomes, competencies I already have, competencies I can develop, commitment, duration window, application window), so that I can make an informed decision before committing to an application. | -   Detail page shows: eligibility criteria, duration, developmental outcomes, competencies i already match, competencies I can develop through this opportunity.    -   “About this opportunity” section will display what is existent in the opportunity loaded in.    -   For Gigs and STIPs: competencies are labelled “What you’ll develop” - no matching logic, no personalisation.     -   For Jobs: detail pages shows competency match ratio “X / Y competencies matched” - binary presence match against officer’s declared competencies; no proficiency levels apply.    -   I can see the apply CTA clearly without scrolling to bottom of the page   -   If a mandatory field has no data, it shows “Not specified”    -   I can navigate back to the listing and my search and filter state is exactly as I left it | -   Detail-to-apply rate: % of detail page views resulting in an apply action –  this is the primary conversion metric for the discovery funnel |  |  |
| **OTEP-129** | US-06 - See whether an opportunity is open or closed before applying.         As an officer, I want to know whether an opportunity is still accepting applications before I click through, so that I'm not caught off guard by a posting I can no longer act on. | -   Closed or expired postings are hidden from the listing and search results - officers cannot see them in the hub.    -   Deep-links to closed postings show a simple posting message: “This opportunity is no longer available” with a link back to the listing.    -   Postings approaching their end date display a “Closing soon” label on both the card and the detail page (threshold will be 7 days or less). |  |  |  |
|  | US-07 - Apply for a STIP or Gig via FormSG link    As an officer, I want to click 'Apply' on a STIP or Gig and be taken directly to the FormSG application form, so that I can submit my application through the correct channel even if it opens outside OTEP. | -   When I click on Apply on a STIP or Gig, I see a brief notice before i gets redirected to FormSG: “You will be taken to FormSG to complete this application”   -   FormSG application URL opens in a new tab    -   Apply button is clearly labelled “Apply via FormSG” so i know where I’m going.    -   A webhook is set up between FormSG and OTEP to receive form submission confirmation - OTEP is notified when an officer successfully submits the FormSG form.    -   On receiving webhook confirmation, OTEP records the submission event against the officer and opportunity ID.    -   After i submit through FormSG, I should receive an email notification.     -   [for MVP] Oppr posters should also receive an email notification that someone applied and with the details or direct the oppr poster to FormSG to view the responses. | -   click_to_formsg rate: % of STIP/Gig detail page views resulting in a FormSG redirect click   -   can track dropoff rate |  | -   After FormSG submission, can we redirect users back to OTEP to show application submission successful? |
| **OTEP-87** | US-08 Handle missing or broken FormSG application link.        As an officer, I want to see a clear message if the FormSG application link is unavailable, so that I know how to get help rather than facing a broken or missing button. | -   Current - If the FormSG link for an opportunity is unavailable, it will show when I land on the form itself.    -   If the FormSG link can be detected removed or unavailable, then the CTA will be disabled and in the details page, to show “Application form unavailable - contact [Agency POC] directly” | -   Missing FormSG link rate: % of STIP/Gig listings where the FormSG URL field is null or invalid – feeds data quality monitoring |  |  |
| **OTEP-130** | US-09 Apply for an SJR or internal job via OTG redirect      As an officer, I want to be redirected to OTG to apply for SJRs and internal jobs, so that I can complete my application through the correct system even though it requires re-authentication. | -   SJRs are included in OTEP with a full detail page - same structure as internal jobs.    -   Click on “Apply via OTG” on an SJR or internal job detail page navigates to OTG with a direct link to the relevant posting.    -   Before redirect, officer is shown a clear notice: “You’ll be taken to OTG to complete this application. You will need to re-login again.”   -   The redirect opens OTG in a new tab.   -   OTEP captures a “click-to-OTG” event at the point of redirect. | -   Click-to-OTG rate : % of SJR/internal Job detail page views resulting in an OTG redirect click – expected to be lower than click-to-embed rate given re-login friction |  | Webhook - Tracking for conversion to application  -tag PH |
|  | US-10	Identify Careers@Gov listings      As an officer, I want to see a clear indicator when a listing comes from Careers@Gov, so that I know upfront where I'll be directed when I apply or view details. | -   All C@G-sourced listings are labelled with a 'Careers@Gov' on the card   -   The label is visible without hovering or clicking into the card. | -   C@G listing click-through rate: click-to-C@G events ÷ C@G listing impressions |  |  |
| **OTEP-89** | US-11	View Careers@Gov opportunity via deep-link      As an officer, I want to click “Apply via Careers@Gov” on the detail page and be taken directly to the opportunity on Careers@Gov, so that I can complete my application through the correct channel without having to search for the role again. | -   C@G detail page in OTEP displays job details sourced from C@G (title, agency, description, duration, and available structure fields)   -   A single prominent CTA is shown: “Apply via Careers@Gov”   -   Clicking the CTA deep-links directly to the specific opportunity on the C@G platform, opening in a new tab.   -   OTEP captures a “click-to-CG” event at the point of redirect.    -   If the opportunity is no longer available on the C@G after the officer clicks through, this is handled entirely on the C@G side - OTEP shows no error state for this scenario.    -   There is no FormSG or OTG application flow for C@G listings. | -   Click-to-C@G rate: % of C@G listing detail page views resulting in a C@G deep-link click |  |  |
| **OTEP-133** | US-12 Access the hub via a deep link from an     As an officer, I want to be able to click a link in an email and land directly on the relevant opportunity so that I can act on opportunities shared with me without navigating from scratch. | -   If an officer lands on an opportunity they’re not eligible: they will see a clear message that they are not authorised to view this opportunity and surface alternative opportunities on the page.     -   The look and feel of the page should be aligned with OTEP theme. | -   edm-to-detail   -   edm-to-noaccess |  |  |

## 9. Go-To-Market Plan (To be discussed)

**Purpose:** Shipping ≠ adoption. Think of what you need to do to drive adoption and scale. 

- 

Target launch group: 1-2 Agencies that actively post Gigs

  - 

prefer agencies with:

    - 

higher posting volume

    - 

willing HR partner

- 

Comms plan:

- 

Training / enablement:

- 

Change management:

- 

Support model:

**Phases:**

- 

Pilot: When

- 

Scale: When

- 

Steady state: When 

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
| **US-09 - Apply for a STIP or Gig via FormSG link**    **Auto-Populated Fields:** The BO also noted that since the officer must log into OTEP before signing up, the system should capture their basic profile information on the backend so they do not have to manually fill it out again. These fields include:   -   Full Name   -   Designation   -   Division & Department   -   Ministry / Agency   -   Work Email |  |  |  |
| ## ** Proposed changes for Application fields (for MVP, we keep it as current ie no changes to the FormSG forms)    **Fields to Retain / Add:**   -   **Contact Number**.   -   **Reporting Officer’s Name and Email:** These are retained specifically to trigger an automated email notifying the supervisor of the application, helping keep the process transparent and combat dropout rates.   -   **Job Grade:** This replaces the legacy question asking if the officer is an individual contributor or team leader. It will be a dropdown list of MX grades with an "Others" option for non-MX tracks.   -   **Main reason for application**.   -   **Meet pre-requisites**.   -   **Declarations:** Retained, though the BO noted that different sets of declarations may be needed depending on whether the posting is a STIP or a Gig.   -   **Custom Questions:** The BO requested functionality allowing opportunity posters to add custom questions for their specific postings, similar to the FormSG form builder.      **Fields to Drop:**   -   **HR Officer’s Name and Email:** Dropped because this information was rarely utilized and often caused confusion for applicants.   -   **"Where did you find out about this opportunity?":** Dropped because all traffic will now route centrally through OTEP. |  |  |  |
