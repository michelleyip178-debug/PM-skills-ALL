# Epic 1: Officer Profile Page

| Doc Created | 9 Feb 2026 |
|---|---|
| PM | Imelda Mo |
| Tech | Rama Moorthy |
| Designer | Dex Tan |
| Business Owner | Jacky (lead), Xian Zhang (owner) |
| Infra Eng | Fabian PEH |
| Target launch | October 2026 |
| Epic Link | OTEP-67 |
| Figma Link | — |

> **Note to Michelle:** This PRD is owned by Imelda's squad. It is reproduced here for cross-squad visibility on shared dependencies (Auth: OTEP-71/110, POCDEX, WOG AD). Do not make changes without checking with Imelda. Coordination channel: open item #18/#30.

---

## 1. Background & Context

Officers in the Singapore Public Service today lack a single, trustworthy view of their competency profile. Competency data exists across fragmented HR systems (HRPS, Cumulus) and is aggregated in POCDEX, but is not surfaced to officers directly. OTG provides some self-assessment capability but has low visibility and incomplete coverage.

This epic establishes the Officer Profile Page as the authenticated landing page for OTEP. It delivers:
1. A verified identity anchor (officer sees their own name, title, agency)
2. A competency baseline derived from their current role profile and OTG self-assessed data
3. The ability to add and manage competencies

Without this page, officers have no reason to trust OTEP is "about them" — reducing adoption across all other epics.

## 2. Problem Statement

Officers struggle to have a clear snapshot of their current competencies because competency information is incomplete and unclear, resulting in officers not knowing their baseline.

This feature also reduces product adoption risk. Without a profile landing page, users may question whether they're in the right account or whether data is accurate to them.

## 3. Data Analysis & Evidence

*(Section marked for development — no quantitative data captured in PRD at time of writing.)*

## 4. Market / Benchmark Scan

*(Section marked for development.)*

| Organisation | Approach | What works | What doesn't |
|---|---|---|---|

## 5. Target User

Public officers in ESG and PSD (MVP pilot). Specifically officers whose profile is managed in HRPS or Cumulus and whose record is present in POCDEX.

Excluded for MVP: MINDEF and agencies not on POCDEX.

## 6. Hypothesis (Value Proposition)

> If an officer can see a single landing page with their basic profile information and their competencies, they will understand their competency baseline, trust that OTEP is about them, and re-engage more because the platform feels accurate and relevant to them.

## 7. Success Metrics

### 7.1 Outcome Metrics (North Star — Not MVP)

- % of officers/sessions who have updated their profile page (voluntarily edited, updated, added competencies, clicked "save")
- Improved Officer Satisfaction Score

### 7.2 Input Metrics

**Adoption:**
- % of officers that logged in at least once / active within X days
- % of officers who clicked into profile page
- % of officers who added new competencies
- % of officers/sessions who made at least one edit in My Competencies in last X months (tracked via "saves")
- % of officers who have at least X% of system/role competencies assessed

**Funnel:**
- Track user journey from entry to exit
- Track drop-off points
- Track button clicks and page engagement

**Engagement:**
- Rate of return to edit competencies

### 7.3 Guardrail Metrics (Rollback / Pause Triggers)

- Login failure rate — X% failed logins despite valid credentials
- Bounce rate >60% (sessions that exit from profile without another action)
- % of profile load errors
- % of profiles with reported errors (in-web "Report an error in your profile")
- >50% reports an error → pause and audit data quality
- Data freshness — TBC (depends on data architecture)
- Latency/availability P95, page load time — TBC

## 8. Scope (Stories + Success Criteria)

### Auth Stories *(shared with Epic 5 / prd-auth.md — cross-reference before changing ACs)*

| **Jira ID** | **Story** | **Acceptance Criteria** | **Instrumentation** | **Notes to Designer** | **Notes to Tech/Other** |
|---|---|---|---|---|---|
| **OTEP-71** | As an officer, I want to login using a secure authentication method so that I can access my account and know my information is secure. | 1. Only officers in ESG and PSD can log in to OTEP for MVP. 2. Users see the WOGAD login page. 3. Users login through WOGAD. 4. If accessing OTEP through the main URL, users land on the profile page. 5. If accessing a direct link (e.g. bookmarked), users land on the target page. | Login success; Login attempt | — | [TBC] Users must have "agency ID": PSD — "13001308-A", ESG — "S10012020". Singpass Unique Identifier = NRIC/FIN. We will use Azure AD (not ADFS). Azure only accessible via COMET, not GSIB. WOGAD approval process 2–4 weeks. Tech effort for Singpass/WOGAD is similar; what's time-consuming is the approval process. Discovery needed (Rama): Can DLE support WOGAD integration for redirection? |
| **OTEP-304** | As an officer, I want to directly access any OTEP page without having to login again if I have already authenticated for that browser session. | 1. If accessing the main URL before session expires, SSO applied — lands on landing page without re-login. 2. If accessing a bookmarked OTEP page during authenticated session, SSO applied — lands on target page. | — | — | Session: 12 hours duration, 30 mins inactivity. Reference: IM8 Low Risk Cloud security plan. |
| **OTEP-72** | As a new officer joining public service, I need to be able to login to OTEP smoothly after onboarding. | 1. User logs in using WOGAD. 2. On first login, they see the default landing view: profile details + My Competency section. | — | — | When a new officer onboards, profile is created by agency HR in HRPS or Cumulus → pushed into POCDEX → into OTEP (instantaneously). Account is created on OTEP. |
| **OTEP-110** ⚠️ | As an officer who should have access to OTEP, I want to see clear instructions on what to do if I failed to login so I can troubleshoot. | 1. If user is part of pilot group and authentication fails, they should be prompted to retry or troubleshoot. ⚠️ **Jira ACs mismatch**: Jira OTEP-110 states only "Authentication failure will be handled at WOG AD" — significantly simpler than above. Confirm before Sprint 4 grooming: does OTEP show any error messaging or does WOG AD handle all error states? | Login failed — reason; Retry attempts | — | Reference: Singpass error response docs. |
| **OTEP-111** | As an officer with no access or deactivated status, I want to see a clear message so I am not left wondering. | 1. These user groups cannot log in: users not in pilot, users who have left service/gone on long-leave, users whose profile is inactive/deactivated in POCDEX. 2. Message: "Oops, you do not seem to have access at the moment. Please contact your HR for more information." | Login attempt failed — access denied | — | [TBC] Backend check for "agency name" or "agency ID". |

### Navigation

| **Jira ID** | **Story** | **Acceptance Criteria** | **Instrumentation** | **Notes to Designer** | **Notes to Tech/Other** |
|---|---|---|---|---|---|
| **OTEP-106** | As an officer, I want to see a clear navigation bar so I can navigate across all key pages. | 1. OTEP logo (WIP). 2. "Home" → Officer profile page. 3. "Jobs & Opportunities" → Jobs landing page. 4. "Learning & Courses" → Courses landing page. 5. "My Development" → My Development landing page. 6. Avatar (first letter of first name; cannot be changed by officer). Clicking avatar shows dropdown with single "Log Out" option. | Home_logo; Nav_profile; Nav_Jobs; Nav_courses; Nav_Mydev; Avatar; Logout | — | — |
| *(no Jira)* | As an officer, I can view the standard footer. | [TBC] waiting for design | — | Standard GovTech footer. Michelle Chen suggested using design components outside of Flagship. | See LifeSG design system reference. |

### Profile Page Stories

| **Jira ID** | **Story** | **Acceptance Criteria** | **Instrumentation** | **Notes to Designer** | **Notes to Tech/Other** |
|---|---|---|---|---|---|
| **OTEP-74** | As a logged-in officer, I can view my profile information right after login so I can confirm my identity and role context. | Users can see: Avatar icon (initials of first name); First name; Last name; Email; Employment title; Agency. | Profile viewed — load success and load fail | What happens if officer sees wrong role assigned? | Mandatory POCDEX fields: employmentID, source system, primary position. Designation: if HRPS use "employment title"; if Cumulus use "business title". Personnelarea/personnelsubarea = secondary filters (not needed for MVP). Profile information from POCDEX is pre-loaded for MVP. |
| **OTEP-75** | As a logged-in officer, I can view My Competencies so I can track and build my competencies for future career growth. | **Default View:** 1. Page titled "My Competencies". 2. Two sections: "Functional Competencies" and "Core Competencies" under Job Role Competencies; followed by Self-declared Competencies below. **Job Role Competencies:** 3. Sourced from HR systems. Users see competencies in two categories: Our Core Competencies and Functional Competencies. Descriptor: "These competencies are pre-populated based on your current job role." **Self-declared Competencies:** 4. Manually added by the user. Only contains functional competencies. Descriptor: "These are self-declared competencies to reflect skills and experience beyond those linked to your current role." 5. User must be able to read the description for each competency. **Edge case — no role profile and no OTG competencies:** 6a. Both sections empty. 6b. Feedback mechanism shown ("Why are my competencies not showing?"). Click → "Something seems wrong, let us check and fix this for you." **Edge case — no role profile but has OTG competencies:** 7a. Only self-declared competencies section populated. 7b. Job role competencies section empty. 7c. These are previously self-added competencies from OTG (see OTEP-105). 7d. Feedback mechanism shown (same as 6b). | tooltip clicked_role; tooltip clicked_additional | Before deleting competency, design for confirmation pop-up/message. | **Mapping POCDEX → HR Systems:** 1. Identify officer via NRIC or email. 2. Obtain Job ID. 3. Look up Job ID in HR systems for expected competencies. HRPS: one officer can have multiple Job IDs (max 3 job family/function each). Cumulus: one job ID, unlimited job family/function. **Mapping POCDEX → OTG Role Profile Bank:** 1. Get officer job family, function and grade from POCDEX. 2. String to form roleID e.g. "AcademicOperationsTechnicalOperationsJR10". 3. Lookup roleID in OTG Profile bank file. 4. Column J "skillsIds" = competencies assigned to the role. 5. Map skillsIds to WOG FC Bank → get competency name and description. Role Profile Bank: pending WD to send over. Consists of: OTG Profile bank + role profiles from Cumulus and HRPS, tagged with competencies. |
| **OTEP-105** | As a logged-in officer who previously used OTG to add competencies, I want to see the same competencies reflect on OTEP so there is a seamless transition. | 1. All competencies self-added previously on OTG reflect on OTEP without manual re-add. 2. Proficiency level omitted for now. 3. OTG competencies must be correctly categorised into the three types and displayed under: a. Job role competencies section (Core + Functional), or b. Self-declared competencies section. | Need to know which competencies were ported from OTG. | — | OTG data file: raw_users_skills excel (Otep2026). Only has user_id and competency NAME (not ID). userID: (1) POCDEX ID if account created through POCDEX; (2) NRIC or email if created manually (ignore — not in POCDEX, deprioritised for OTEP). Competency Name can also contain CEG competencies (from their own bank) — exclude from OTEP completely. Matching flow: find officer in DB using POCDEX ID (always starts with "P") → get roleID → map to role profile bank → get competency IDs → call competency names on another table → map names from raw_user_skills doc against role profile competencies → assign under Role Competencies. Any delta: check against rest of competency bank. If match → "Additional Competencies". If no match → omit (CEG competencies). Competency names in Raw_users_skills report are unique. |
| **OTEP-112** | As a logged-in officer, I can search for a specific competency to add to my profile so I can build a comprehensive list. | This story covers keyword search only (methods 2 and 3 covered by OTEP-205). **Search and save:** 1. User clicks "+" icon to trigger keyword search. 2. User types a word to search WOG competency bank (WOG to agency-specific comps). 3. Suggestions matching competency names appear as dropdown. 4. User can scroll to browse matching competencies. 5. Click a competency → indicated as selected; can continue searching and selecting before saving. 6. Can add as many competencies as desired. 7. Click Save → selected competencies added to My Competency section. 8. "No results" shown when keyword returns no matches. **Displaying saved competencies:** 8. Competencies already in My Competencies may still appear in search results; can be selected/saved but de-duplicated in backend — only one entry shown. 9. Auto-categorised and displayed under the relevant section. 10. If job role competency → parked under Our Core or Functional Competencies (depending on type). 11. If not a job role competency → parked under Self-declared Competencies automatically. | competency_added; competency_id; competency_name; source (resume/search/text); type (role/additional). When deletes: competency_removed; competency_id; competency_name; type. User Properties: competency_count; competency_name_additional; competency_name_role | Track keywords searched, position of competency added, role competencies deleted and added back; search_comp_submitted; search_comp_no_result | Competency bank source for "add competencies": pending WD. Will include all 8 types: WOG OCC; WOG FC; OTG Agency OCC; OTG Agency FC; HRPS Agency OCC; HRPS Agency FC; Cumulus Agency OCC; Cumulus Agency FC. |
| **OTEP-205** | As a logged-in officer, I can use the inference tool to suggest competencies to add to my profile so there is less friction. | **"Upload CV" — Inference through CV:** 1. Users can upload a .docx document. 2. Drag and drop or click "Upload CV" to select file. 3. Clicking "Generate" triggers CIE → returns top 8 most relevant competencies sorted by relevance. No confidence score shown. 4. Recommendations are functional competencies from WOG FC bank only (not entire competency bank). 5. All 8 pre-selected. Click Save → all 8 added. 6. Users can tap to deselect; deselected are not added. 7. Added competencies auto-sorted into Job Role or Self-declared Competencies. 8. If expected competency not in list → search function available within same flow. 9. Search mirrors OTEP-112 keyword search. 10. Copy: "Can't find a competency you expect? Try searching to add it." **"Describe Work Experience" — Inference through blob of text:** 1. Users type or paste text. 2. Maximum character limit: XXX [TBC]. 3. Clicking "Generate" triggers CIE → top 8 competencies. Rest of experience same as "Upload CV". **Unaccepted file format / error handling:** File not readable → "Unsupported file type, please upload a .docx file." Other errors (password protected, cannot be read) → "An error occurred in the upload, please try again." | Upon uploading CV or using text box → list of top 8 inferred competencies shown. | — | CIE requirements: file type .docx; 2MB file limit; CIE handles text extraction/OCR. **Note: CIE is only trained with WOG FC bank** — recommendations limited to WOG FC, not agency-specific competencies. |
| **OTEP-126** | As an officer, I can delete selected competencies from my profile so I have the flexibility to build a relevant profile. | **Deleting job role competencies:** 1. Click "pen" icon to edit Core and Functional competencies. 2. See fixed list of core and functional competencies assigned to their role. 3. Can select/deselect to show or hide from profile. 4. Cannot add competencies outside this list into Core/Functional sections. **Removing self-declared competencies:** 1. Click "pen" icon. 2. See list of self-declared competencies. 3. Deselect those to remove. 4. Click "Save" → changes reflected. 5. Once removed, permanently removed — must use one of 3 methods to re-add. | competency_deleted_role; competency_deleted_additional | — | — |
| **OTEP-77** | As an officer who changed role or got a promotion, I will still see my old role competencies plus new role competencies. | 1. Officer sees competency profile automatically updated upon next login. 2. New role's competencies added under My Competencies, categorised under core or functional respectively. 3. Outdated competencies no longer relevant to current role moved to "Additional Competencies". | What kind of tracking? | Prompt needed to alert officers of a new competency added. Consider prompt to let officers know old competency has moved to a new section — set a one-time dismiss trigger. | Profile changes only made if there is a new role update from HR systems. Officers on short-term GIG or temporary job posting will NOT have profile updated with new competencies. My Competencies section (MVP scope): current role's competencies (FCs only — not OCCs) + additional competencies. Future: lifetime competency record including all self-assessed, past roles, and course-attained competencies. |
| **OTEP-79** | As an officer, I want guidance on how to interpret the information on this page so I am not confused. | [TBC] Waiting for design. | — | Suggestion: "Keep your competency profile up to date. Review and add competencies that reflect your skills and experience to get personalised recommendations." | — |
| **OTEP-78** | As an officer, I can provide feedback and suggestions through the WOGAA widget so I help improve my own experience using OTEP. | 1. Users can click on the WOGAA feedback widget, complete it and submit their responses. | — | — | Use WOGAA widget for feedback. Register at https://wogaa.sg/. |

## 8.2 Key Out of Scope Features

1. Double-hatting information — not included in MVP.

## 9. Go-To-Market Plan

*(WIP — section not yet developed in source PRD.)*

- Target launch group: Which agency/persona first?
- Comms plan: TBC
- Training / enablement: TBC
- Change management: TBC
- Support model: TBC

**Phases:**
- Pilot: TBC
- Scale: TBC
- Steady state: TBC

## 10. Risks, Assumptions & Mitigations

| Risk/Assumption | Type | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| Officer information for required fields wrong or unavailable in POCDEX | Tech | Low | High | "Report incorrect info" mechanism to alert team to check with WD |
| Exposing personal data fields beyond policy/intended | Tech | Low | Critical | Whitelist fields; self-access only for MVP |
| No integration with CAM for MVP (account suspended after 90 days inactivity) | Tech | Low | Low | Rely on SGID and POCDEX to offboard officers for now; proper CAM integration in future releases |
| Officers unable to find a competency they want to add | Ops | Medium | Medium | Short-term (not MVP): feedback mechanism to alert WD to consider adding to bank. Long-term: UI dashboard to manage competencies directly in OTEP. |
| OTG self-assessed competencies showing on both OTG and OTEP confuses officers | Ops | Medium | High | Ask whether OTG can block display of self-assessed info on OTG (action: @Michelle Yip / Imelda to chase). Clear comms needed. |
| Inaccurate role profile matching (double-hat officers, wrong tagging in HR system) | Ops | Medium | Medium | Comms: officers who see incorrect competencies can remove and re-add. Feedback mechanism to surface to WD. |

## 11. Dependencies & Assumptions

- **POCDEX** — mandatory fields: employmentID, source system, primary position. Personnelarea/personnelsubarea needed for MVP filtering (stored but not displayed for now).
- **OTG Role Profile Bank** — pending WD to send over. Role profiles sit in an Excel today, must be uploaded into OTEP.
- **WOG FC Bank** — for competency names and descriptions.
- **HRPS / Cumulus** — source systems for designation and job ID mapping.
- **CIE (Competency Inference Engine)** — only trained on WOG FC bank; agency-specific competencies not covered.
- For MVP, ONLY POCDEX-covered officers in scope (not MINDEF etc.). Subsequent phases: start with CPF for non-POCDEX agencies.
- Role Profile upload and updating: version history with timestamp must be tracked. When a new competency is added to a role profile, it should be added and updated on the officer's profile page.
- Competency and proficiency must be stored as **two separate fields** in the database (reason: future HR search for officers tagged with specific competencies for recruitment).

## 12. Decision Tracker

| Decision | Owner | Date | Notes |
|---|---|---|---|
| Will use Azure AD (not ADFS) for auth | Imelda / Rama | Feb 2026 | ADFS intranet-only; Azure needs COMET |
| Double-hatting not included in MVP | Imelda | Feb 2026 | Out of scope (Section 8.2) |
| OTG CEG competencies excluded from OTEP | Imelda / Rama | Feb 2026 | Not in WOG FC or agency FC bank |
| Profile info pre-loaded from POCDEX for MVP | Imelda | Feb 2026 | Dynamic loading considered for future |
