# PRD: Epic 2 — My Development Page

> **This PRD is owned by Imelda's squad — cross-squad visibility only.**
> Do not change ACs or scope without checking with Imelda Mo first.
> Coordination via open item #18/#30 (Imelda / OTEP-Core Squad PM sync).

---

| Field | Value |
|---|---|
| **Epic** | OTEP-68 |
| **PM** | Imelda Mo |
| **Tech** | Barry Lim, Rama Moorthy |
| **Designer** | Amber Tong |
| **Business Owners** | Jacky (lead), Xian Zhang (owner) |
| **Infra Eng** | Fabian PEH |
| **Target Launch** | October 2026 |
| **Doc Created** | 9 Feb 2026 |
| **Figma** | https://www.figma.com/design/TTm0tLa93BzjCApKTLAEI4/OTEP-v0.1?node-id=2043-4649 |

---

## 1. Background & Context

**Strategic Context**

Three WOG workforce strategic goals drive this epic:

1. Enable career discovery, growth and mobility for officers, anchored on competencies
2. Enable talent discovery and agility in talent deployment across WOG, anchored on competencies
3. Enable long-term workforce planning and development for future-proofing

**Current State**

OTG (One Talent Gateway, Fuel50 SaaS) is the current platform. Survey data (IB Survey, Jan 2025, n=1385) shows 21% of active OTG users rank competency management as their top-2 priority — second only to opportunities discovery. Despite this, only 9% (8k out of 91k onboarded officers) relogged in during 2025.

The competency gap analysis feature exists in OTG but has poor UX (multiple clicks to access) and incomplete role profile coverage across agencies.

**Why Now**

- Fuel50's limited flexibility required workarounds that harmed UX — self-assessment only works for predefined roles, officers with niche or generic titles see incorrect role options
- No inference capability to represent officer capabilities from working and learning history
- Agency-specific competency frameworks (even when derived from WOG FCs) are an increasing pain point
- 9% relogin rate signals low engagement
- OTEP is being built in-house to give the flexibility Fuel50 can't. This epic tests a foundational hypothesis: if competency gaps are made clear, will officers take action?

**Requested by:** Workforce Development (WD) team

---

## 2. Problem Statement

Officers struggle to identify which competencies to develop and subsequently take action because competency gap information today is unclear, resulting in officers not knowing what career development action to take.

---

## 3. Data Analysis & Evidence

| Type | Finding | Source |
|---|---|---|
| Feature prioritisation | 21% of active OTG users rank competency management as top-2 priority (after opportunities) | IB Survey, Jan 2025, n=1385 |
| Feature prioritisation | 17.8% for non-active OTG users (also top-2 after Opportunities) | IB Survey, Jan 2025, n=1385 |
| Adoption | 9% relogin rate in 2025 amongst 91k onboarded officers | OTG Dashboard |
| Funnel CVR | % drop-off after landing on competency analysis page in OTG | [TBC — check with Chris/XZ] |
| Competency awareness | 64.6% agree/strongly agree they know what competencies to upskill in (27.9% neutral, 8.38% disagree, 2% strongly disagree, 1.16% not aware) | IB Survey, Jan 2025, n=1385 |
| Competency awareness | [TBC] % of officers who clicked into the competency section of OTG in the last 6 months | OTG |
| Competency awareness | [TBC] % of onboarded officers who have added their self-assessed competency in OTG (lifetime) | OTG |
| Action clarity | 56.2% agree/strongly agree they know what action to take to close gaps | IB Survey, Jan 2025, n=1385 |
| Action clarity | % of STIPs/GIGs/Jobs/Courses applied in 2025 (baseline) | WD to provide |
| Action clarity | Average time spent on competency gap page in OTG (baseline) | OTG |

---

## 4. Market / Benchmark Scan

[WIP — Amber to populate. Key questions: how do LinkedIn, Workday, and Coursera present competency gaps vs target role requirements?]

| Organisation | Approach | What works | What doesn't |
|---|---|---|---|
| | | | |

---

## 5. Target User

**Pilot target group:**

- Must-have: Agencies with ready job profiles — by agency because it is operationally easier to get buy-in and control comms
- Good to have: Officers who show signals of being motivated to progress (e.g. re-logged into OTG in the past 12 months) — "The Uncertain" and "The Self-Driven" personas

**Note:** OTG role profiles are grouped by Job Families. Any pilot agency will likely have officers without a matching role profile in OTG. Expect partial data coverage from day one. See Section 11.3 (Data Audit) for details.

---

## 6. Hypothesis

**If** we provide officers with a clear, trustworthy view of their competency gaps,

**then** officers will understand what specific competencies to develop and click through to explore opportunities and courses,

**leading to** increased officer engagement with career development tools and eventually an increase in completed development activities linked to identified gaps.

---

## 7. Success Metrics

### 7.1 Outcome Metrics (North Star)

- **User:** Increase in % of officers who complete opportunities or courses aligned to their competency gaps
- **Business/org:**
  - Improved Officer Satisfaction Score
  - Officers report increased clarity on what competencies to develop (in-web survey or post-pilot)

### 7.2 Input Metrics

| Type | To Track | Why |
|---|---|---|
| Adoption | % of officers who access the "competency gap analysis" tab | Unique officers interested |
| Adoption | % of sessions where users visited the competency gap analysis page | Visit frequency |
| Engagement | Average time spent on this page | Content interest signal |
| Engagement | Median time spent on this page | |
| Funnel CVR | % drop-off after landing on competency analysis page | Is content valuable? |
| Funnel CVR | % of officers who view gap analysis tab and click through to "opportunities" within the same session | Does gap view prompt action? |
| Funnel CVR | % of officers who view gap analysis tab and click through to "courses" within the same session | Does gap view prompt action? |

### 7.3 Guardrail Metrics

- Drop-off rate exceeds 60% — officers view page and immediately exit
- Error rate: >50% of officers report an error in their competency data → pause and audit data quality
  - In-web mechanic: "Report an error in your competency data" + competency selector
- Data freshness (TBC — depends on data architecture)
- Latency / availability (TBC — depends on data architecture)

---

## 8. Scope (Stories + Acceptance Criteria)

> Jira IDs for Epic 2 stories are not yet assigned. Raise at next grooming with Imelda's squad to get OTEP-NNN tickets.

| **Jira ID** | **Story** | **Acceptance Criteria** | **Instrumentation** | **Notes to Designer** | **Notes to Tech/Other** |
|---|---|---|---|---|---|
| TBD | As an officer, I can compare my current competencies against the competencies in the next job grade in order to know what is expected of me for a promotion | **Current Functional Competencies:** 1. Users understand which are their current functional competencies — must be an exact match with those under "Job role profile" and "Additional competencies" in the profile page. 2. Users will not see Core competencies (from "Job role profile" in profile page) anywhere in the My Dev page — omitted entirely for comparison. **Next Grade Competencies:** 3. Users can see competencies associated to their next job grade. 4. Where only one job role exists at the next grade, those competencies are displayed automatically — no selection needed. 5. Where two or more job role options exist at the next grade, no competencies are shown by default — user must select a role first. Only one role's competencies can be displayed at a time. **Comparison:** 6. Users can easily identify which competencies they already possess vs which they need to develop. 7. No proficiency level comparison is required for MVP. | | Suggested page title: "My Next Progression". Designer to decide: should role selector persist last selection on return visits, or reset to blank? | Exclude OTG Role Profile Bank. Next level logic: job grade minus 1 (e.g. JR10 → JR9; JR11A → JR11). Filter using: 1) officer's agency, then 2) concatenate of Job Family / Function / Next Grade. Multiple similar concatenates possible — TBD how many roles to show. Use designation under "Job" in HRPS and "Job profile name" in Cumulus. WD to confirm if full designation field exists in HRPS. |
| TBD | As an officer, I can compare my current competencies against the competencies of a target job role in order to know what is expected of me should I want to change roles | **Default state:** 1. Users see an empty target role page until a role is selected. **Searching and selecting:** 2. Users can find a role by typing keywords and/or using filters. Keyword + filter can be used simultaneously. 3. Filters: 1) Agency 2) Job Family 3) Job Function 4) Grade. 4. Blank state message if no matching roles found. **Restricted roles (TBC):** 5. Roles at grade MX7 and above are hidden from the dropdown. 6. A brief explanation is shown in the search area: "Roles above director level (MX8 and above) are not available for comparison." **Comparison:** 7. Users can clearly see which competencies are tied to the selected role. 8. Users can compare their current competencies against the target role to identify gaps. 9. No proficiency level comparison required. | | Designer to decide: dropdown for filters (one selection per filter at a time)? Should role selector persist last selection on return visits or reset to blank? | Exclude OTG Role Profile Bank. Filters: 1) agency 2) job fam 3) job func 4) grade. Role naming: add "Agency" at the back. Search logic: "starts with" then "contains". Exclude "next grade" roles from this list. Exclude MX7 and above. |
| TBD | As an officer, I want to be able to see the competency definition so I understand what it represents and how to apply it | 1. Users can see the competency description | | | |
| TBD | As an officer, I can see recommended courses related to my missing competencies so I can take immediate steps to explore how to improve | 1. Users can see a swimlane of recommended courses. 2. Users can click through to the respective course tile to view course details. | | | Course recommendation is rule-based: match 1) officer's missing competencies with 2) courses tagged to those competencies. Courses cannot be duplicated/repeated. If no courses are tagged to the officer's competency set, default to proposing courses matching the next role's competencies. **IMPT:** Need attribution from OTEP to LEARN to track traffic into LEARN — confirm whether we can track all the way down to apply and enrol. |
| TBD | As an officer with no role profile, I have the option of selecting a target role to see areas of development | 1. User will not see "next grade" comparison. 2. User will see the search bar to select a target role. 3. User sees a generic swimlane: "Explore popular courses" | | | "Explore popular courses" — filter by "AI" |

### 8.2 Out of MVP Scope (R1 / Deferred)

- Proficiency level comparison (binary match only for MVP — levels deferred to R1)
- Editing self-assessed competencies within OTEP (OTG remains the write source in MVP)
- Learning history display on profile page (Next Release — per Epic 3 priority table)
- WD Upskilling team rationalisation of agency-specific FCs with WOG FCs (ongoing policy work, not OTEP MVP scope)

---

## 9. Go-To-Market Plan

[WIP — Imelda to populate]

- Target launch group: Agency with highest % of officers with ready role profiles in OTG Central Role Profiles Bank
- Comms plan: TBD
- Training / enablement: TBD
- Change management: Key risk — officers seeing self-assessed data on both OTG and OTEP simultaneously (see Section 10)
- Phases: Pilot / Scale / Steady state — dates TBD

---

## 10. Risks, Assumptions & Mitigations

| Risk/Assumption | Type | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| OTG Central Role Profile Bank is updated and usable | Data | Low | Medium | — |
| No API to pull self-assessed competencies from OTG | Tech | High | Low | Data export/import process. Determine refresh cadence. |
| Pilot officers get confused seeing self-assessed data on both OTG and OTEP | Tech/Policy | High | Critical | Option A: Block competency profiles from OTG. Option B: GTM comms are very clear on platform usage. Barry note: one-time pull only — data will diverge over time. OTEP will not have editing abilities for self-assessed in MVP; OTG remains the write source. |
| Review with pilot agencies on suitability does not go well | Adoption | Medium | Critical | Discuss back-up options with WD |
| Gap analysis is accurate but officers don't find it meaningful | Product Market Fit | — | — | Post-pilot survey to validate |

**Transition Considerations:**
1. Pilot officers see self-assessed data in both OTG and OTEP — decision needed on whether to block OTG competency view for pilot cohort
2. Barry's note: one-time data pull — data will differ over time as officers update OTG

---

## 11. Dependencies & Assumptions

**Systems:**
- POCDEX — officer identity (employmentID, primary position, job grade)
- OTG Role Profile Bank — 750+ role profiles across ~17 job families
- OTG Competency Bank — ~938 codes (WOG FC bank ~539 + agency-level ~400)
- OTG self-assessed competencies — export/import only, no API
- HRPS/Cumulus — designation field for role naming (WD to confirm availability)
- DLE LEARN — course catalog for recommended courses swimlane (SFTP, no API until Q3 2026)

**Teams needed:** WD team, pilot agency HR, Chris (OTG data), Fabian (infra), Jumpstart (if POC2 in scope)

**Policy assumptions:**
- Agency-specific competency codes that overlap with WOG FC bank will be rationalised over time (WD upskilling direction)
- CEG competencies are excluded from OTEP entirely (agency-specific codes not in WOG FC or agency FC bank)

### 11.3 Data Audit

**Role Profiles:**
- OTG Central Role Profiles Bank: 750+ complete profiles across ~17 job families + agency-requested additions
- Each profile includes: job family, function, role level (needs grade mapping), Competency ID, competency name, skillsID (= WOG FC), skills name, proficiency levels
- 7 job families created by Functional Leaders (cross-agency); agencies may create their own if FL profiles not relevant
- Grade mapping: "Role Level" in OTG Central Role Profiles Bank → MX levels (via Proxy & Job Grade Mapping file)

**Competency Bank:**
- OTG master competency bank: ~938 codes
- WOG FC Bank: ~539 codes
- Delta of ~400 codes = agency-level competency codes (confirmed with Chris)
- OTG comp bank = WOG FC bank + agency-uploaded competencies (may also be in HRPS/Cumulus, or OTG-only)
- WD currently has oversight of WOG FC bank only; direction is to eventually gain sight of agency-specific codes too (CDGO direction)
- Process for agencies to add comps: quarterly liaising with CEG; WD checks for duplication with WOG FC bank

---

## 12. Decision Tracker

| Date | Decision | Rationale | Owner |
|---|---|---|---|
| TBD | Whether to block OTG competency view for pilot cohort | Avoid confusion from dual systems | Imelda + WD |
| TBD | Refresh cadence for self-assessed competency data pull from OTG | No API — export/import only | Barry + Rama |
| TBD | How many role options to surface when multiple concatenates exist at next grade | Chris to provide count of duplicates against pilot population | Imelda + Chris |

---

## 13. Phase 2 Must-Haves

1. Role profiles for the remaining ~10 job families — enabled once the Competency Inference Engine (CIE) is live
2. Self-editing of self-assessed competencies within OTEP (currently OTG-only)
3. Proficiency level comparison (deferred from MVP)
