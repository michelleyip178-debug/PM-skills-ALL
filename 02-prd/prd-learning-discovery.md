# PRD: Epic 3 — Learning and Course Discovery

> **This PRD is owned by Imelda's squad — cross-squad visibility only.**
> Do not change ACs or scope without checking with Imelda Mo first.
> Coordination via open item #18/#30 (Imelda / OTEP-Core Squad PM sync).

---

| Field | Value |
|---|---|
| **Epic** | TBD (PM to input Jira Epic link) |
| **PM** | Imelda Mo |
| **Tech** | Barry Lim, Rama Moorthy |
| **Designer** | Amber Tong |
| **Business Owners** | Jacky (lead), Xian Zhang (owner) |
| **Infra Eng** | Fabian PEH |
| **Target Launch** | October 2026 |
| **Doc Created** | 23 Feb 2026 |
| **Resource Directory** | Jumpstart Recommendation Engine for DLE — [Week 1 update overview] |

---

## 1. Background & Context

**Strategic Context**

Three WOG workforce goals drive this epic:

1. Enable career discovery, growth and mobility for officers, anchored on competencies
2. Enable talent discovery and agility in talent deployment across WOG, anchored on competencies
3. Enable long-term workforce planning and development for future-proofing

OTEP serves as the unified platform for everything career and growth related. Course discovery is a key lever.

**Current State**

Officers can look for courses across four fragmented systems:

1. **DLE's LEARN** (learn.gov.sg) — 56k+ learning opportunities: CSC (705), ALS (1,193), Harvard Business (28,896), LinkedIn Learning (11,012), Udemy (14,665)
2. **Cumulus/Workday** — agency-specific course catalogs
3. **HRPS/SAP** — agency-specific course catalogs
4. **OTG (Fuel50)** — shows recommended courses based on competencies

This creates a fragmented experience. There is no unified recommendation model to ease discovery and increase take-up. The Jumpstart team (GovTech) has been building a POC to provide course recommendations based on officer profile and learning history ("Similar to you" model using PMI; aimed to launch April 2026). OTEP intends to ingest these recommendations into our MVP.

A CSC service mapping workshop confirmed that officers want personalised recommendations and cite inability to compare programmes across platforms as a key pain point.

**Why Now:**
1. OTEP as a competency-driven platform makes course discovery based on competency gaps a key lever
2. Jumpstart POC1 is ready — good time to incorporate smarter recommendations into MVP

---

## 2. Problem Statement

Officers struggle to confidently choose and understand which learning courses are helpful for their growth because course information is fragmented and existing discovery is not personalised, creating high effort in manual search and comparison, resulting in officers feeling lost, disengaged and lower course take-up.

---

## 3. Data Analysis & Evidence

| Type | Finding | Source |
|---|---|---|
| Discovery | Only 47.5% of officers agree they "have sufficient information on the available development opportunities" on OTG | IB Survey 2025, n=1385 |
| Engagement | [TBC] | |
| Conversion | [TBC] | |

---

## 4. Market / Benchmark Scan

| Organisation | What works | What doesn't |
|---|---|---|
| LinkedIn Learning | Low-friction scanning via hover expansion; bite-sized tile info; swimlanes by different filters ("popular", "because of skills you follow"); "My Library" for personal course tracking; strong professional relevance cues tied to career skills | — |
| N/A patterns | Skip/save/like feedback to build learner preference profile; social proof (X learners, ratings, reviews); "similar courses" or "alternative at higher/lower grade" within course detail | — |
| Coursera | — | Navigation can feel overwhelming; many similar courses makes shortlisting difficult |

---

## 5. Target User

Officers who are:
- Interested in acquiring new skills to develop themselves
- Interested in growing in their careers
- Interested in developing their competencies

---

## 6. Hypothesis

**If** we provide guided personalised discovery on OTEP based on relevant parameters (e.g. competency gaps, learning interest),

**then** officers will be able to quickly discover and confidently shortlist relevant courses,

**leading to** an increase in course detail views and enrolment conversions.

---

## 7. Success Metrics

### 7.1 Outcome Metrics (North Star)

- **User:** Increased course enrolment rate per officer; % of officers who registered for a course in the past 12 months
- **Business/org:** % of course enrolments attributed to OTEP; % of registration click-throughs from OTEP

### 7.2 Input Metrics

| Type | To Track |
|---|---|
| Awareness | % of officers who access the "courses" tab through the nav bar |
| Awareness | % of sessions where officers accessed the "courses" tab through the nav bar |
| Awareness | % of officers who accessed the courses page through the "competency gap analysis page" |
| Awareness | % of sessions where officers accessed the courses page through the "competency gap analysis page" |
| Adoption | Average number of courses browsed per officer within X months |
| Adoption | Average number of courses saved per officer within X months |
| Adoption | % of officers who registered for a course in the past 12 months |
| Adoption | % of officers who saved a course in the past 12 months |
| Adoption | Recommended courses CTR |
| Adoption | Recommended courses save rate |

### 7.3 Guardrail Metrics

- Drop-off rates exceed XX% — officers land and immediately exit
- Error rates — officer's course profile is inaccurate
- Complaints / support tickets
- Data freshness issues
- Latency / availability

---

## 8. Scope (Stories + Acceptance Criteria)

**MVP Priority Summary:**

| Priority | Feature |
|---|---|
| MUST-HAVE | Course tile + course detail page + redirect to LEARN to apply or start |
| MUST-HAVE | Search for courses and apply basic filters (course catalog, attributes) |
| MUST-HAVE | Recommended for you (Jumpstart POC1) |
| GOOD TO HAVE | Course recommender in gap-analysis page (My Dev page → Courses link) |
| GOOD TO HAVE | More filtered swimlanes (Top 10, Popular — currently local logic inside DLE; not callable via API today) |
| NEXT RELEASE | Learning history to display on profile page |

---

| **Jira ID** | **Story** | **Acceptance Criteria** | **Instrumentation** | **Notes to Designer** | **Notes to Tech/Other** |
|---|---|---|---|---|---|
| **OTEP-82** | As an officer with learning history on DLE, I can see the courses recommended to me as a swimlane based on comparative profiling and learning history so that I can discover relevant courses faster | 1. Users can browse through a swimlane of recommended courses. 2. Users can click into a selected course tile to see more course details. | | Swimlane with "view more"? Consider arrows to slide through options (Netflix-style). Header: "Recommended for you" | Courses recommended via Jumpstart POC1 "Similar to you" model — based on job profile (agency/department/job function/designation) and learning history (enrol/completion) [PMI model]. Call from DLE directly (not JS directly) since DLE applies accessibility/agency filters already. |
| **OTEP-82 (variant)** | As an officer with competencies in my role profile, I can see courses relevant to my competency gaps so I do not have to manually search | 1. Users can browse through a swimlane of courses recommended based on their missing competencies. 2. Users can click on the selected course tile to see more course details. | | Header: "Based on your development areas". Note: if no courses tagged to officer's competency set, show no swimlane (do not fall back to next-grade competencies here — that logic is in My Dev page). | Competency gaps are based on user's current competencies vs next grade job competencies. Competencies matched to courses with competencies tagged. Courses are de-duplicated (a course can have many competencies). No ranking needed for display order for now. |
| **OTEP-323** | As an officer, I can see a summary of key course details in the course tile in order to get preliminary info for discovery efficiency | 1. Course tile shows (from LEARN): Name of course, Product Type, Course start date, Course duration, Course provider. 2. Users can click into the course tile to see course details. | | | Confirm "new" attribute availability from DLE SFTP. Product types: Classroom, Digital Learning, Digital Learning (pay-per-use), Digital Resources, Events, Milestones. |
| **OTEP-84** | As an officer, I want to click into a course tile to see comprehensive course information and have the option to apply/start | 1. Course detail page shows: a) Course Title, b) Course overview, c) Course outline, d) Learning Outcomes, e) Programme code, f) CTA button "Learn more", g) Product type, h) Duration, i) Start and end date, j) Minimum and maximum capacity, k) Domain and Competencies (omit proficiency level details), l) Course Provider. 2. Clicking "apply" / "Learn more" brings officer to LEARN platform and lands on the course detail page in LEARN. | | Get sample data to study field examples (reference LEARN course detail page). Design does not need to mirror LEARN exactly — ensure similar info and seamless UX (per PSC NOM 6Jan26). | Pending SFTP file from DLE on all course details. Fields to pull: Programme Title, Overview, Outline, Product Type, Duration, Provider, Domain & Competency, Target Audience. Tiles with no cost/run date = free programme (DLDR included in subscription) or no planned runs yet. |
| **OTEP-83** | As an officer, I can browse and search across the entire catalog to find a course I am interested in | 1. CTA button on Courses landing page: "Explore more courses". 2. Leads to search experience page with filters: a) Product Type, b) Domain, c) Competency, d) Provided by. 3. "Clear all filters" available. 4. For Domain and Competency filters, add a search bar with autocomplete (logic: "contains") so officers can find without scrolling. 5. Search results show all courses whose name, description and outline contain the keyword. 6. All filters unchecked on landing. 7. Courses sorted alphabetically by default. | | Product type options: Classroom, Digital Learning, Digital Learning (pay-per-use), Digital Resources, Events, Milestones. Course Provider options: CSC, Harvard Business (HBR), LinkedIn Learning, Udemy. | Confirm "new" attribute from DLE. Search autocomplete: pulls from course name, logic "contains". |
| TBD | As an officer who has no learning history or competency gaps, I want to still be able to see and browse the course catalog | Cases: 1. No role profile → no competency-based swimlane. 2. No learning history → no Jumpstart recommendations swimlane. 3. Both absent → go straight to Search and Browse page. | | | |

### 8.2 Out of MVP Scope (R1 / Deferred)

- Bookmarking / saving courses (Feature Backlog — TBD requirement)
- Returning to saved courses (Feature Backlog — TBD requirement)
- Persistent search bar on Courses page (omit for now)
- Filter bar on Courses page as a standalone feature (omit for now; search + filters handled in OTEP-83 search experience page)
- More filtered swimlanes (Top 10, Popular) — local DLE logic, not callable via API today; GOOD TO HAVE
- Learning history display on profile page — NEXT RELEASE

---

## 9. Go-To-Market Plan

[WIP — Imelda to populate]

- Target launch group: TBD (which agency/persona first)
- Comms plan: TBD
- Training / enablement: TBD
- Change management: TBD
- Support model: TBD
- Phases: Pilot / Scale / Steady state — dates TBD

---

## 10. Risks, Assumptions & Mitigations

| Risk/Assumption | Type | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| DLE has clean course metadata and links to each course | Tech | — | Critical — necessary to link officers to course detail page in LEARN | Get sample SFTP dataset from DLE early; validate field completeness before build |
| SFTP from DLE not yet received | Tech | High | High | Pending — Imelda to chase DLE; no build on OTEP-84/323 until sample data confirmed |
| DLE API not available until Q3 2026 | Tech | Confirmed | Medium | Use SFTP for MVP; plan migration to API post-Q3 2026 |
| Tagging incomplete for 3rd-party courses | Data | High | Medium | 3rd-party courses tagged once (by provider); newer courses may be untagged. Competency-based swimlane will have gaps for these courses. |
| Calling Jumpstart directly vs via DLE | Tech | Medium | Medium | DLE applies accessibility/agency filters after calling POC1. Sy En's recommendation: call from DLE directly to avoid errors when officers click into courses unavailable to them. |
| Agency subscription access to LEARN | Ops | Low | Low | Almost all agencies on base subscription (except MOE and DSTA — limited licences). POC1 recommendation applicable to all for classroom; DLDR needs base subscription. |

---

## 11. Dependencies & Assumptions

**Systems:**
- DLE LEARN — course catalog via SFTP (no API until Q3 2026). Fields: Programme Title, Overview, Outline, Product Type, Duration, Provider, Domain & Competency, Target Audience
- Jumpstart (GovTech) — POC1 recommendations via DLE (call DLE, not Jumpstart directly)
- POCDEX — officer identity for personalisation inputs to Jumpstart
- OTG Competency Bank — competency-tagged courses matching for My Dev → Courses link (OTEP-82 variant / GOOD TO HAVE)
- HRPS/Cumulus — SSO identity (NRIC or email preferred over LearnerId; FIN edge case noted)

**Teams needed:** DLE (Cherilynn's team), Jumpstart (GovTech), WD team, Fabian (infra)

**Policy assumptions:**
- OTEP attribution tracking in LEARN is needed to measure enrolment conversions — confirm with DLE if feasible
- SSO: NRIC or email as learner identifier preferred; FIN-to-citizen conversion edge case needs resolution

**Data availability assumptions:**
- DLE SFTP data contains clean programme links for LEARN deep-link redirect
- Jumpstart POC1 provides fallback generic recommendations for officers with no learning history (confirmed: classroom recommendation available even without learning history; DLDR needs base subscription)

---

## 12. Decision Tracker

| Date | Decision | Rationale | Owner |
|---|---|---|---|
| TBD | Call Jumpstart via DLE (not direct) | DLE applies agency/accessibility filters; calling JS directly risks officers seeing unavailable courses | Imelda + Barry |
| TBD | SSO identifier for LEARN: NRIC vs email vs LearnerId | FIN edge case for non-citizen conversion | Barry + DLE |
| TBD | Confirm OTEP attribution tracking in LEARN | Needed for enrolment CVR metric | Imelda + DLE |

---

## 13. Feature Backlog (Post-MVP)

| Story | Notes |
|---|---|
| Officers can save / bookmark courses | TBD requirement |
| Officers can return to saved / bookmarked courses | TBD requirement |
| Persistent search bar on Courses page | Omit for now |
| Filter bar as standalone feature | Omit for now (covered in OTEP-83 search page) |
| More filtered swimlanes (Top 10, Popular) | GOOD TO HAVE — depends on DLE exposing these as callable attributes |
| Learning history display on profile page | NEXT RELEASE |
| Jumpstart POC2 — competency-based recommendation model | Timeline and scope to be discussed with Jumpstart |
| Opportunity recommender (R1) | Hypotheses and interview questions for scoping: [2026-06-05-W23-opportunity-recommender-hypotheses.md](../../PM-OS/outputs/research-synthesis/2026-06-05-W23-opportunity-recommender-hypotheses.md) |
