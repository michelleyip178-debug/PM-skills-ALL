> **Updated: 2026-06-16** — OKRs updated to reflect IAA-approved version (8 Apr 2026) with granular OKR roadmap for IB/CBD funding justification.

---

## IAA-Approved High-Level OKRs

**Mission:** Helping public officers grow with clarity and purpose, while giving agencies better competency and workforce-planning visibility.

**OKR 1 — Enable competency growth**
50% of onboarded officers with updated competency profiles and satisfaction score ≥ 3.5/5 for analysis and recommendations by Q4 2027. Benchmark: OTG's 23% active profile interaction.

**OKR 2 — Career development**
1,850 officers applied for development opportunities via OTEP by Q4 2028. Based on FY2025 IB target of 1,470 plus a 25% aspirational uplift.

**OKR 3 — Workforce planning**
80% of onboarded agencies using analytics dashboards and agency satisfaction score ≥ 3.5/5 by Q1 2028.

---

## North Star Metric

By Dec 2028, 50% of onboarded officers should complete at least one development action (course completion or opportunity placement) originating from CareerCompass, tracked on a rolling 12-month basis. Browsing, enrolling, or applying alone does not count — the action must be completed and attributable to CareerCompass.

**Progressive targets:**
- Dec 2026 MVP: Establish baseline for pilot cohort
- Mar 2027 R1: 10%
- Dec 2027 R4: 30%
- Dec 2028 R8: 50%

---

## OKR Roadmap 2026–2027 (Proposed)

| Dimension | Oct 2026 MVP / by Dec 2026 | Q1 2027 R1 / by Mar 2027 | Q2 2027 R2 / by Jun 2027 | Q3 2027 R3 / by Sep 2027 |
|-----------|---------------------------|--------------------------|--------------------------|--------------------------|
| Competency Profiles | ≥40% of onboarded officers with updated competency profiles | — | — | 60% of onboarded officers with updated competency profiles |
| Opportunity Engagement | Establish baselines for profile updates, opportunity applications, and course registrations | 20% of onboarded officers click into at least one course/job opportunity within 6 months of launch | 20% of onboarded officers apply for at least one course/job opportunity within 6 months | 20% of onboarded officers apply for at least one course/job opportunity within 12 months |
| Active Usage | — | — | 20% active login rate over 90 and 180 days | 25% active login rate over 90 and 180 days |
| Features & Platform | — | 50% of required OTG features built on CareerCompass | 80% of required OTG features built on CareerCompass | 100% of required OTG features built on CareerCompass |
| Agency Adoption | — | — | 50% of OTG agencies migrated fully to CareerCompass | 60% of onboarded agencies actively using analytics dashboards monthly by Q4 2027 |
| Experience & Satisfaction | UAT/pilot officer satisfaction score ≥ 3.5/5 | Officer satisfaction score ≥ 3.5/5 | — | Satisfaction score ≥ 3.8/5 from officers and agencies |
| Efficiency / Performance | — | Application status update latency reduced to within 24 hours of hiring-manager action | 25% click-through conversion for course recommendations | — |

*Note: OKR dates intentionally lag release cycles because outcome data needs time after features go live.*

---

## How OKRs Shape Delivery

The Objectives and Key Results (OKRs) outlined in the 2026–2027 Roadmap act as the strategic North Star that dictates what features are prioritized in each release and how we measure the success of the sprints we just planned.

Here is how the OKRs directly shape the OTEP platform delivery and the work outlined in Epics 4 and 5:

**1. Driving the Immediate MVP Scope (Target: Dec '26)**
Our current sprints are heavily focused on Epic 4 (Opportunity Discovery) and Epic 5 (WOG Authentication) to build the MVP's "Essential Officer Experience." The OKRs explicitly mandate what this MVP must achieve by December 2026:
*   **Centralizing Opportunities:** The OKR target to have **"≥80% of job opportunities (STIPs, GIGs, SJR, C@G) are listed on OTEP"** is the direct business driver for Epic 4, which is why our immediate sprints focus on building the Unified Opportunity Hub to aggregate these exact posting types.
*   **Establishing Baselines:** The MVP OKRs require us to establish baselines for the percentage of officers applying for opportunities through OTEP. This ties directly to Epic 4's North Star metric of migrating ≥50% of STIP/Gigs applications from FormSG to OTEP by Month 3. 
*   **Pilot Success:** The OKR demands a **"UAT/Pilot officers satisfaction score ≥ 3.5/5"**. This is why Epic 5 (WOG Authentication) is scoped to first roll out safely to a restricted pilot group before scaling. **MVP pilot = 6 agencies (~5,400 officers): PSD, ESG, MDDI, URA, MCCY, CAAS, onboarded in staggered pairs** (Implementation Details, 2026-06-02). *(Earlier drafts named only ESG + PSD — updated to the confirmed 6.)*

**2. Shaping Release 1 & 2 (Target: Q2 '27)**
As we move past the MVP into the Q2 2027 OKRs ("Partial Completion of required OTG features"), the focus shifts to engagement and operational efficiency:
*   **Application Tracking:** The OKR target to reduce **"application status update latency to within 24 hours"** directly informs the theme of Release 1 ("Seamless Application for Opportunities"), which promises a "Click-apply-track" experience with status tracking and an Intelligence Dashboard.
*   **Agency Posting Creation (moved into R1, 2026-06-02):** R1 now also includes **agency-native opportunity creation** — agency HR authors postings via a structured form inside CareerCompass (the posting lives in OTEP, not OTG). This **supersedes the 2026-05-12 direction that scoped creation to R4** (see decisions-log). It is a material scope expansion ("World B" native path) and pairs the officer-apply experience with the agency-create experience in the same release. ⚠️ Needs BO ratification + a capacity check before R1 grooming; confirm interaction with the ATS decision.
*   **Early Adoption:** The OKR goal for **20% of onboarded officers to have applied** for at least one opportunity within 6 months of launch means our foundational sprints must ensure a frictionless application process (like Epic 4's FormSG and OTG redirects).

**3. Guiding the Long-Term Ecosystem (Target: Q3 - Q4 '27)**
The later OKRs dictate the mature phases of OTEP (Releases 3 through 6):
*   **Competency and Career Planning:** The Q4 2027 OKR requires **40% of onboarded officers to have viewed their competency gap analysis** and clicked through to a recommendation, and 60% to have updated competency profiles. This perfectly aligns with Release 2 ("Purpose-driven Growth") and Releases 5-6 ("Personalised Guidance"), which introduce the Competency Gap Detection Engine, AI Job Matchmaker, and Predictive Action Engine.
*   **Agency Migration:** The Q3 and Q4 2027 OKRs target the **100% full migration of OTG agencies to OTEP** and require 80% of agencies to actively use the analytics dashboards. This long-term goal justifies why building a scalable data ingestion pipeline (OTG to OTEP) is a critical technical dependency right now in Sprint 1.
