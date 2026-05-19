### **Structured Planning Guide: OTEP Platform Delivery**

> ⚠️ **Superseded for the sprint plan.** This guide predates the OTEP-Pathfinder Sprint Ceremonies v2 doc and the 2026-05-11 scope reconciliation. For the current plan use **[context/sprint-calendar.md](../context/sprint-calendar.md)** (dates + ceremonies — 12 sprints, 4 May – 16 Oct 2026) and **[projects/sprint-allocation.md](../projects/sprint-allocation.md)** (which stories in which sprint). The Sprint Breakdown in Section 4 below is out of date (old Sprint 2 scope, old dates, "buffer to Sep"). Sections 1–3 (alignment, dependencies, release phasing) and 5–7 (gaps, scope concerns, risks) are still broadly useful.

#### **1. High-Level Alignment**
Based on the overarching Roadmap, the current focus is on building the "Essential Officer Experience". The uploaded Epics map to the earliest phase of the rollout:
*   **MVP Milestone (~4 Months) - Theme: "See All Opportunities"**: The primary value proposition is creating a "One-place to see it all". 
    *   **Mapped Epics**: Epic 4 (Opportunity Discovery Hub) and Epic 5 (WOG Authentication). Authentication is the foundational capability that enables personalized discovery.
*   **Release 1 Milestone (~2 Months) - Theme: "Seamless Application for Opportunities"**: Drives the "Click-apply-track" value. 
    *   **Mapped Epics**: The application redirect and tracking components of Epic 4 (e.g., US-07 FormSG Webhooks, OTEP-130 OTG redirects) lay the groundwork for this phase.

#### **2. Dependency Mapping**

**Critical Path (longest chain — 6 stories deep):**
```
OTEP-71a (Auth) → OTEP-72 (Account) → OTEP-85 (Listing) → OTEP-128 (Card) → US-05 (Detail) → US-07/09/11 (Apply)
```

**Cross-Epic Dependencies:**

| Story | Blocked By | Rationale |
| :--- | :--- | :--- |
| OTEP-85 (Hub Listing) | OTEP-71a + data pipelines | Must be authenticated; needs ingested data |
| OTEP-127 (Ringfencing) | OTEP-72 + OTEP-85 | Needs POCDEX profile data + listing to filter against |
| US-05 (Detail — competency match) | OTEP-72 | Needs officer's competency profile |
| OTEP-130 (OTG Redirect) | OTEP-72 + US-05 | Profile auto-populate + detail page CTA |
| OTEP-133 (Email Deep-Link) | US-05 + OTEP-127 | Needs detail page + eligibility logic |

**Within Epic 4:**

| Story | Blocked By |
| :--- | :--- |
| OTEP-86 (Search) | OTEP-85 (operates on listing) |
| US-03 (Filter) | OTEP-85 |
| OTEP-128 (Card) | OTEP-85 |
| US-05 (Detail) | OTEP-128 (navigated from card) |
| OTEP-129 (Open/Closed) | OTEP-85 + OTEP-128 |
| US-07 (FormSG) | US-05 (apply button on detail page) |
| OTEP-87 (Missing Link) | US-07 |
| OTEP-130 (OTG) | US-05 + OTEP-72 |
| US-10 (C@G Indicator) | OTEP-128 |
| OTEP-89 (C@G Deep-Link) | US-05 + US-10 |
| OTEP-133 (Email Deep-Link) | US-05 + OTEP-127 |

#### **3. Release Phasing**
*   **v1.0 (MVP - "See All Opportunities")**: 
    *   Focuses on establishing the foundational infrastructure, Azure AD / WOGAD Single Sign-On (SSO), and the unified Opportunity Hub. 
    *   Delivers the core ability to search, filter by type (STIP, Gig, SJR, Jobs), view fixed-size opportunity cards, and click outward to apply via FormSG, OTG, or Careers@Gov.
*   **v1.1 (Release 1 - "Seamless Application")**: 
    *   Focuses on deeper application tracking, expanding filtering (agency, grade, commitment filters are reserved for Release 1), and launching the Smart Application Assistant.
*   **v1.2 (Release 2 - "Purpose-driven Growth")**: 
    *   Focuses on Dynamic Career Profiling and the Competency Gap Detection Engine.

#### **4. Sprint Breakdown (MVP Kickoff)**
Based on a 2-week sprint cycle with full team capacity (Pow Hwee, Leo, Thomas, Amber). WOGAD is ready for development. **Target ship: Fri 16 Oct 2026** — 12 sprints (Phase 1 Feature Build, Sprints 1–8 to 21 Aug; Phase 2 Compliance & Go-Live, Sprints 9–12). The sprint-by-sprint breakdown below is outdated — see `context/sprint-calendar.md`.

---

**Sprint 1 (4–15 May): Auth + Data Infrastructure**

| Track | Stories | Owner Focus |
| :--- | :--- | :--- |
| Frontend | Login UI, error/denial states (OTEP-71a, 71d, 71e) | Leo/Thomas |
| Backend | WOGAD integration (OTEP-71a, 71b, 71c), POCDEX push (OTEP-72), OTG → OTEP data pipeline | Pow Hwee, Leo/Thomas |
| Design | Finalize Hub UI, opportunity card, and filter designs | Amber |

**Stories:** OTEP-71a, OTEP-71b, OTEP-71c, OTEP-71d, OTEP-111, OTEP-72
**Sprint Goal:** All auth flows working end-to-end; data pipeline delivering opportunity records; C@G ingestion method confirmed.

---

**Sprint 2 (18–29 May): Opportunities Listing Hub** *(scope reconciled 2026-05-11 — see sprint-allocation.md)*

**Stories (5, OTG data only):** OTEP-85 (view all), OTEP-86 (filter by type), OTEP-128 (type on card), OTEP-129 (sort by date), US-05 (clear filters). Ringfencing (OTEP-127), apply-redirects (US-18/19), auth edge-cases, search and category filter (US-03) → Sprint 3. Careers@Gov (US-10) not in Sprint 2 — ingestion unconfirmed.
**Sprint Goal:** Officers can browse and filter every OTG opportunity on one authenticated page, newest first, published-only.

---

**Sprint 3 (Jun 2 – Jun 13): Deep Discovery**

| Track | Stories | Owner Focus |
| :--- | :--- | :--- |
| Frontend | Search bar + results (OTEP-86), detail page layout (US-05), ringfencing UI states (OTEP-127) | Leo/Thomas |
| Backend | Elasticsearch query layer (OTEP-86), eligibility service (OTEP-127), deep-link routing (OTEP-133) | Pow Hwee, Leo/Thomas |
| Design | Application routing UX (FormSG notice, OTG notice, C@G button) | Amber |

**Stories:** OTEP-86, OTEP-127, US-05, OTEP-133
**Sprint Goal:** Officers see personalized, searchable results and can drill into full opportunity details. Email deep-links resolve correctly.

**Risk:** OTEP-133 depends on both US-05 and OTEP-127 completing within this sprint. If either slips, OTEP-133 moves to Sprint 4.

---

**Sprint 4 (Jun 16 – Jun 27): Application Layer**

| Track | Stories | Owner Focus |
| :--- | :--- | :--- |
| Stream A | FormSG webhook + email notifications (US-07), missing link handling (OTEP-87) | Backend-heavy |
| Stream B | OTG redirect + profile auto-populate (OTEP-130) | Frontend + backend |
| Stream C | Careers@Gov deep-link (OTEP-89) | Frontend + URL mapping |

**Stories:** US-07, OTEP-87, OTEP-130, OTEP-89
**Sprint Goal:** All three application routes (FormSG, OTG, C@G) are functional end-to-end. Edge cases handled gracefully.

**Note:** Three independent streams — can be fully parallelized across the team.

---

**Sprint 5 (Jun 30 – Jul 11): Integration & Polish**

No new user stories. Focus:
- End-to-end testing across all application routes
- Performance optimization (<5s load on government networks)
- Pull FormSG baseline submission metrics
- State preservation: search/filter state retained on back-navigation (US-05 AC)
- Edge case hardening: empty states, closed deep-links, session expiry mid-flow
- Bug fixes from internal QA

---

**Phase 2: Compliance & Go-Live (Sprints 9–12, 24 Aug – 16 Oct)** — replaces the old "buffer to Sep"
- Sprint 8 ends Fri 21 Aug = ⭐ Feature Freeze
- Sprints 9–12: security review submission (monthly cycle — submit early Sep), pen testing, compliance sign-off, UAT with pilot officers (ESG + PSD), fixes, launch prep + monitoring
- Final Steering sign-off Fri 9 Oct · **🚀 Go-Live Fri 16 Oct 2026**

---

#### **5. Gaps — Stories Needed But Not Written**

| Gap | Impact | Action Required |
| :--- | :--- | :--- |
| **OTG → OTEP data pipeline** | Sprint 1 infrastructure; no ACs defined | Write story with sync frequency, schema mapping, failure handling |
| **Careers@Gov → OTEP ingestion** | US-10/11 assume C@G data exists | Confirm method (API vs other); write story |
| **Email/notification service** | US-07 references email on submission; OTEP-133 references email with deep-link | Clarify: existing platform service or new build? |
| **Search indexing infrastructure** | OTEP-86 assumes elastic matching | Story or spike for index provisioning and refresh strategy |
| **Opportunity lifecycle (admin)** | OTEP-129 hides closed postings | Who/what marks opportunities closed? Automatic (date) or manual? |
| **Officer competency data model** | OTEP-128/05 reference competency match | Where does opportunity competency data come from? Part of OTG export? |

#### **6. Scope Concerns — Consider Deferring to Release 1**

| Item | Story | Concern | Recommendation |
| :--- | :--- | :--- | :--- |
| **Competency match ratio** | US-05 | Requires structured taxonomy + scoring algorithm. High cost for MVP. | Descope to R1. For MVP, show competency tags as "What you'll develop" without calculating a match. |
| **Auto-populate OTG form fields** | OTEP-130 | If programmatic field injection into OTG's form — heavy integration. | Clarify with Pow Hwee: is this backend capture only, or actual form pre-fill? |
| **Webhook submission tracking** | US-07 | Receiving the webhook is MVP. Storing + displaying status to users is R1 (application tracking). | Keep webhook receipt for metrics. Defer user-facing status to R1. |
| **Email deep-link generation** | OTEP-133 | If OTEP must generate + send notification emails — that's a notification system. | Clarify: is the email manually composed with a link, or does OTEP auto-send? |

#### **7. Potential Risks & Missing Details in PRDs**

**Technical & Schedule Risks:**
*   **Security Review Cycle:** Reviews only happen once a month. Must submit by early September to avoid slipping past end-of-month ship date.
*   **Azure AD Prerequisites:** Verify whether ESG is onboarded onto COMET, as Azure can only be accessed using COMET.
*   **Sprint 3 Cascade Risk:** OTEP-133 depends on two other Sprint 3 stories (US-05, OTEP-127). Any slip cascades to Sprint 4.
*   **Data Pipeline Readiness:** If OTG → OTEP pipeline is not delivering records by end of Sprint 1, Sprint 2 cannot start core UI work.

**Gaps in Requirements (PRDs):**
*   **Careers@Gov Data Architecture:** The PRD notes that C@G listings are ingested separately, but it is unconfirmed whether this will be via the C@G API.
*   **Business Logic Clarification:** We need the Business Owner to clarify if "Secondment" is considered a distinct type or a sub-type of SJR, as this impacts the US-03 filtering logic.
*   **Baseline Metrics:** Engineering still needs to pull the current FormSG submission volumes to establish the baseline for our North Star metric (Channel migration target of ≥50%).
*   **Session Redirect Handling:** Epic 5 notes there is "additional effort to link them back to their original page instead of homepage" upon session timeout relogin. This edge case needs a dedicated technical spike or a specific sub-task ticket.
