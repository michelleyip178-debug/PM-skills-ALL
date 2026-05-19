# Sprint Grooming Prep — May 7, 2026

Use at: 10:30 Pathfinder Internal Sprint

---

## Part 1: Sprint 1 Status Review (May 4–18)

**Sprint Goal:** Login and navigate to Jobs and Opportunities
**Agreed scope:** Get login working e2e + clarify data dependencies (not build the full pipeline).

### Done
| Ticket | Title |
|--------|-------|
| OTEP-209 | Baseline database conventions with team |
| OTEP-171 | Frontend repo setup |

### In QA
| Ticket | Title | Question for grooming |
|--------|-------|----------------------|
| OTEP-201 | Create ref table schema migration for local dev | Who's reviewing? ETA to merge? |

### In Progress
| Ticket | Title | Question for grooming |
|--------|-------|----------------------|
| OTEP-173 | Exploration: Auth flow and tech | When does exploration end and implementation begin? Is OTEP-190 the answer? |
| OTEP-190 | Implement simple authentication through keycloak | On track for May 16? Any blockers? |

### Still in Backlog (risk)
| Ticket | Title | Why it matters | Question |
|--------|-------|----------------|----------|
| OTEP-183 | [Spike] POCDEX profile lookup integration pattern | Sprint 2 dependency — ringfencing (US-01b) needs this | Is this starting this week? |
| OTEP-193 | Design Data Model for Opportunities | No data model = Sprint 2 can't build listing UI | Who owns this? When does it start? |
| OTEP-192 | Design recurring job to fetch opportunities data | This IS the OTG→OTEP pipeline — Sprint 2 blocker | Same as above |
| OTEP-170 | Base Layout for Opportunity Listing Page | Sprint goal includes "navigate to Jobs" | Design ready — when can this start? |
| OTEP-202 | Create POCDEX seed database for local dev | Engineers need local test data | Sequenced after OTEP-201? |
| OTEP-203 | Create POCDEX mock API stub for local dev | Unblocks frontend auth work | Same |
| OTEP-204 | Seed core entity tables for local dev | Foundation for Sprint 2 | Same |

### Sprint 1 Summary Question to Ask

> "We're at day 4 of 14. Auth is progressing (OTEP-173, 190). We agreed Sprint 1 is about getting login working + landing data decisions — not building the pipeline. But OTEP-192, 193, and 183 are still in backlog. What do we need to unblock the decision-making on those this week?"

---

## Part 2: Sprint 2 Stories to Groom (May 19–30)

**Sprint Goal:** Officers can browse, filter, and view OTG opportunities they're eligible for — and apply via OTG for SJRs and internal jobs.

**Scope (OTG first, no C@G):** US-01, US-01b, US-03, US-04, US-05, US-06, US-09

---

### US-01 / OTEP-85: Unified Opportunity Hub Listing

**Story:** As a Growth-Driven Public Service Officer, I want to see all STIPs, Gigs, SJRs, and Jobs in a single unified hub so that I do not have to navigate multiple channels.

**Key ACs:**
- All types in same listing on load
- Most recent first, ringfenced internal jobs prioritized on top
- Sticky search bar + Back to Top button
- Empty states handled
- Types visually distinguished (not color-only)

**Dependencies:**
- OTEP-71 (auth) — must be logged in
- OTEP-193 (data model) — needs schema defined
- OTEP-192 (data pipeline) — needs opportunity records in the system
- OTEP-170 (base layout) — foundation component

**Open questions for grooming:**
1. How many opportunity records are we expecting at MVP launch? (Affects pagination decisions)

**Decided:**
- Ringfencing = per-opportunity rule (set on each posting, not session-level agency match)
- Sort: ringfenced on top, then by recency. Evergreen (no closing date) pushed to bottom.

**Estimation ready?** Yes — design is ready. Data model still needed but can estimate against design.

---

### US-03 / OTEP-86: Filter by Opportunity Type

**Story:** I want to filter results by types (STIP, Gig, SJR, Internal Jobs) so I can narrow to relevant categories.

**Key ACs:**
- Multi-select filter
- Active filters visible
- Filters persist while browsing
- Clear-all action
- Tooltip explaining each type

**Dependencies:**
- US-01 (operates on the listing)
- Data model must include an `opportunity_type` field

**Scope notes:**
- OTG types only for Sprint 2: STIP, Gig, SJR, Internal Jobs (4 categories)
- No C@G filter option yet (comes when C@G data is flowing)
- No function/job-family filter (deferred — investigate only)

**Open questions for grooming:**
1. **Is "Secondment" a filter option?** Asking BOs at 14:00. Working assumption: sub-type of SJR.
2. Tooltip content — who writes it? PM or content/UX?
3. **Function filter taxonomy mismatch:** OTG uses "Job Functions" (e.g., HR, Finance, IT) while C@G uses what looks like sectoral categorisation (e.g., Arts & Culture, Health & Social). These are different taxonomies. When we eventually build the function filter, do we:
   - Map both into a unified taxonomy?
   - Show two separate filter dimensions (function + sector)?
   - Pick one system's taxonomy as the master and map the other into it?
   - This is a Sprint 1 investigation item — raise with Pow Hwee for technical feasibility.

**Estimation ready?** Yes — 4 filter categories, no function filter.

---

### US-04 / OTEP-128: Opportunity Card

**Story:** I want to view a structured card showing type, title, agency, and duration at a glance so I can assess fit before reading details.

**Key ACs:**
- Fixed-size cards: type, title (max 2 lines), agency, commitment
- Relative posting date label
- Ministry icon alongside agency name
- Gigs/STIPs: no competency pills. Jobs: show competency match ratio
- Only open/active opportunities shown

**Dependencies:**
- US-01 (card lives inside the listing)
- Design ready (confirmed)
- Data model fields for: type, title, agency, commitment, created_at, ministry_icon

**Open questions for grooming:**
1. **Competency match ratio on Jobs cards — is this MVP or R1?** My recommendation: descope to R1. For MVP, show competency tags as "What you'll develop" without calculating a ratio. This avoids needing the scoring algorithm in Sprint 2.
2. Ministry icon — where does this asset come from? Is there an existing icon set?
3. "Fixed-size cards" — does Amber's design confirm card dimensions?

**Estimation ready?** Yes if we agree on the competency ratio descope. If not, estimation is much larger.

---

### US-06 / OTEP-129: Open/Closed/Closing Soon States

**Story:** I want to clearly see whether an opportunity is open, closed, or closing soon so I'm not caught off guard.

**Key ACs:**
- Closed/expired hidden from listing and search
- Deep-links to closed postings show "no longer available" + link back
- "Closing soon" label at 7 days or less

**Dependencies:**
- US-01 + US-04 (state displayed on listing and cards)
- Data model needs: `status`, `closing_date` fields
- Opportunity lifecycle logic: who/what marks opportunities closed? (auto by date, or manual?)

**Open questions for grooming:**
1. What timezone for the 7-day calculation?

**Decided:**
- Lifecycle is auto-close by `closing_date` — no admin tooling needed.
- No closing date in OTG → evergreen, pushed to bottom of list.

**Estimation ready?** Yes — lifecycle is date-driven, confirmed.

---

### US-05 / OTEP-87: Opportunity Detail Page

**Story:** I want to view a full detail page showing eligibility, duration, and competency information so I can make an informed decision before applying.

**Key ACs (Sprint 2 scope — simplified):**
- Detail page shows reporting line, duration, "What you'll gain" sections
- Competency tags displayed as "What you'll develop" — no match ratio (descoped to R1)
- Apply CTA clearly visible without scrolling to bottom
- Mandatory fields with no data show "Not specified"
- Back navigation retains listing search/filter state

**Dependencies:**
- US-04 (navigated from card)
- Data model must include detail fields (reporting line, developmental outcomes, competencies)
- Design ready (confirmed from mockups)

**Open questions for grooming:**
1. How many detail fields are mandatory vs optional? (Affects empty state handling)
2. Back-navigation state preservation — is this browser history, or do we need to store filter state in URL params/state?
3. Does the detail page need its own API endpoint, or is it the same data as the card with more fields?

**Estimation ready?** Yes — design confirmed, competency scoring descoped.

---

### US-09 / OTEP-132: Apply via OTG Redirect

**Story:** I want to be redirected to OTG to apply for SJRs and internal jobs so I can complete my application in the right system.

**Key ACs:**
- "Apply via OTG" button navigates to OTG (hardcoded URL)
- Notice informs user they will be taken to OTG and need to re-login before opening in new tab
- Basic profile info (Full Name, Designation, Division, Agency, Work Email) captured on backend

**Dependencies:**
- US-05 (apply button lives on detail page)
- Backend needs officer profile data (from POCDEX or auth session)

**Decided:**
- OTG URL is hardcoded — no dynamic deep-linking to specific postings. Just redirects to OTG.

**Open questions for grooming:**
1. **Profile capture** — is this pulling from POCDEX data already in our system, or calling POCDEX at apply-time?
2. Is the notice a modal/dialog, or inline on the detail page?

**Estimation ready?** Yes — hardcoded URL makes this straightforward.

---

### US-01b / OTEP-127: Ringfencing via POCDEX Profile

**Story:** When I log into the opportunity hub, I want to automatically see only the opportunities I am eligible for based on my profile so I can avoid wasting time on postings I cannot apply for.

**Key ACs:**
- Users must be logged in to view the listing
- Ringfencing criteria applied to all opportunities based on officer's POCDEX data on login
- Opportunities refresh if officer transfers to another agency and logs in again

**Dependencies:**
- US-01 (ringfencing operates on the listing)
- OTEP-183 (POCDEX spike) — must understand POCDEX data structure to implement filtering
- OTEP-72 (account creation) — officer profile data must exist in OTEP
- Ringfencing rule set per-opportunity (confirmed)

**Open questions for grooming:**
1. What POCDEX fields drive eligibility? (Agency? Grade? Scheme of service?)
2. Is ringfencing a backend filter (API only returns eligible opps) or frontend filter (all loaded, filtered client-side)?
3. If an opportunity has no ringfencing rule set, is it visible to everyone?
4. How do we test this with seed data — do we need seed officer profiles with different agencies?

**Estimation ready?** Partially — depends on POCDEX spike clarity. If OTEP-183 hasn't started, this carries unknowns.

---

### ~~US-10 / OTEP-88: Careers@Gov Visual Indicator~~ — MOVED OUT

Removed from Sprint 2. OTG types prioritised first; C@G comes after OTG experience is stable.

---

## Part 3: Estimation

**Why now:** Adrian has asked about sizing. We need story points on Sprint 2 tickets to establish velocity and forecast whether we hit end-of-September ship date.

**Approach:** T-shirt sizes → story points. Use the team's scale:

| Size | Points | Meaning |
|------|--------|---------|
| S | 1–2 | Few hours, single concern, no unknowns |
| M | 3–5 | 1–3 days, clear scope, minor unknowns |
| L | 8 | ~1 week, multiple concerns or cross-cutting |
| XL | 13 | >1 week or significant unknowns — consider splitting |

**Stories to estimate today:**

| Story | My gut estimate | Notes |
|-------|-----------------|-------|
| US-01 / OTEP-85 (Hub listing) | L (8) | Multiple ACs, design ready, suggest breaking down (see below) |
| US-01b / OTEP-127 (Ringfencing) | M–L (5–8) | Depends on POCDEX spike; eligibility filtering per officer profile |
| US-03 / OTEP-86 (Filter by type) | M (3–5) | 4 types (STIP, Gig, SJR, Jobs), no function filter |
| US-04 / OTEP-128 (Opportunity card) | M (3–5) | Fixed design, no competency match ratio |
| US-05 / OTEP-87 (Detail page) | M–L (5–8) | Reporting line, "What you'll gain," competency tags (no scoring), Apply CTA |
| US-06 / OTEP-129 (Open/Closed/Closing Soon) | S–M (2–3) | Auto-close by date, evergreen → bottom. Confirmed. |
| US-09 / OTEP-132 (Apply via OTG) | S (1–2) | Hardcoded OTG URL, notice before redirect, backend profile capture |

**Removed from Sprint 2:**
- ~~US-10 / OTEP-88 (C@G indicator)~~ — OTG first, C@G is fast-follow

**Total (gut):** ~30–38 points for Sprint 2. Ambitious for a 2-week sprint.

**US-01 breakdown suggestion (for team validation):**

| Sub-task | Scope | Size |
|----------|-------|------|
| US-01a: Data fetch + listing render | Fetch from API, render list, most-recent-first sort | M (3) |
| US-01b: Sort logic (ringfenced + evergreen) | Ringfenced on top, evergreen to bottom | S (2) |
| US-01c: Sticky search bar + Back to Top | Scroll behaviour, floating button | S (2) |
| US-01d: Empty states | Zero results handling | S (1) |

**Questions to ask during estimation:**
- "33–42 points in 2 weeks — is this realistic, or do we need to cut something?"
- "US-01b (ringfencing) depends on the POCDEX spike landing in Sprint 1. If it doesn't, what's our plan?"
- "US-05 + US-09 are new additions. Are there unknowns that make these bigger than they look?"
- "Should US-01 be split into sub-tasks so cards and filters can start in parallel?"
- "What's our biggest risk — ringfencing, the detail page, or the OTG redirect integration?"

---

## Grooming Checklist

### Decisions to drive today

| # | Decision | My recommendation | Ask |
|---|----------|-------------------|-----|
| 1 | Competency match ratio (US-04/05) — MVP or R1? | Descope to R1. Show tags only, no scoring algorithm. | "Does anyone see a reason to keep match ratio in MVP?" |
| 2 | Secondment — distinct type or sub-type of SJR? | Assume sub-type for estimation; adjust if Business Owner says otherwise | "Can we estimate US-03 assuming 5 filter categories?" |
| 3 | C@G ingestion method | [Your recommendation: API / file export / scrape] | "I recommend X because Y — objections?" |
| 4 | Sprint 1 realistic scope | Auth likely lands; data decisions are the deliverable | "What do we need to unblock OTEP-192/193 this week?" |
| 5 | Sprint 2 estimation | ~30–38 points (incl. ringfencing, OTG redirect simplified) | "This is ambitious — what do we cut if it doesn't fit?" |

### After grooming — actions to capture
- [ ] Estimation values for US-01, US-03, US-04, US-05, US-06, US-09
- [ ] Decision record: competency match ratio → R1
- [ ] Decision record: US-01 breakdown (split into sub-tasks or keep as one?)
- [ ] US-09: confirm hardcoded URL is sufficient (no deep-link to specific posting)
- [ ] Any new blockers or dependencies surfaced
- [ ] Updated Sprint 2 backlog in Jira with estimates
- [ ] Total Sprint 2 points → baseline for velocity tracking
