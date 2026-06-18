# OTEP-390: Ringfenced opportunity detail page states

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Sprint:** OTEP-Pathfinder Sprint 5

---

## Description

**User story:** As a public service officer, I want the opportunity detail page to clearly tell me whether I am eligible for this opportunity, so that I don't waste time pursuing a role I can't apply for — and if I'm not eligible, I can still find something relevant.

**Sprint 5 scope:** FE detail page states for eligible and ineligible officers, including the ineligible deep-link entry path (EDM or shared URL). Absorbs OTEP-133 (EDM deep-link ineligibility).

---

## Acceptance Criteria

### Eligible officer (default detail experience)

1. When an eligible officer views a ringfenced opportunity, the detail page renders normally with no additional eligibility notice. The Apply CTA is shown as standard.
2. For ringfenced Internal Jobs only, a subtle indicator is shown (e.g. "Available to you") to acknowledge the officer's eligibility without being intrusive. Design treatment to be confirmed by Amber.

### Ineligible officer — arrives via direct URL or shared link

3. When an officer who is not eligible for a ringfenced opportunity lands on its detail page (e.g. via a shared URL, EDM, or bookmark), the page loads but displays a clear ineligibility notice: "This opportunity is not available to you."
4. The Apply CTA is hidden. No application path is shown.
5. Below the notice, the page surfaces up to 3 alternative opportunities the officer is eligible for, drawn from the live listing. If no alternatives exist, show the standard empty state copy.
6. A link back to the full listing is always visible.

### POCDEX unavailable (fallback)

7. If POCDEX data cannot be resolved at the time of the detail page load (lookup failure), the page renders normally without an eligibility indicator. The system does not block access on a failed lookup — degrade silently.

### Unauthenticated access

8. An unauthenticated officer accessing any opportunity detail page via direct URL is redirected to login first, then returned to the original URL after authentication.

---

## Out of Scope (Sprint 5)

- Competency match ratio on the detail page — deferred to R1
- Agency/grade/scheme-level eligibility display (e.g. "Open to MX officers only") — R1+
- Personalised alternative opportunity recommendations — basic eligibility match only

---

## Dependencies

- OTEP-127 — BE eligibility filter (provides the eligibility signal this story renders)
- WOG AD onboarding (#26, Fabian)
- POCDEX read replica (#31, Daryll)
- OTEP-352 — Load POCDEX production code table
- Design: Amber to spec eligible indicator treatment and ineligible notice layout

---

## Absorbs

- **OTEP-133** (Access the hub via a deep link from an EDM) — the ineligible-via-deep-link scenario is fully covered by AC3–6 above. OTEP-133 can be closed as absorbed. EDM-specific analytics (`edm_to_noaccess`) should be tracked via a `source=edm` param on the deep-link URL if EDM tracking is in scope.

---

## Open questions (resolve before Sprint 5 planning)

1. What is the eligible indicator treatment on the detail page? Amber to propose — AC2 is intentionally loose on visual spec.
2. How are "alternative opportunities" selected for the ineligible state? Pure eligibility filter, or also ranked by relevance? Recommend eligibility-only for MVP.
3. Does the EDM deep-link carry a `source` param for analytics tracking? If yes, confirm with comms/EDM owner.

---

*Created 2026-06-05. Absorbs OTEP-133. Companion to OTEP-127 (listing ringfencing). Gates: same as OTEP-127 (WOG AD #26, POCDEX #31).*
