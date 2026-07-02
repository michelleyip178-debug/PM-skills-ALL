# OTEP-390: Ringfenced opportunity detail page states (eligible + ineligible)

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

User story:  As a public service officer, I want the opportunity detail page to clearly tell me whether I am eligible for this opportunity, so that I don't waste time pursuing a role I can't apply for — and if I'm not eligible, I can still find something relevant. Sprint 5 scope:  FE detail page states for eligible and ineligible officers, including the ineligible deep-link entry path (EDM or shared URL). Absorbs OTEP-133. Acceptance Criteria Eligible officer (default detail experience) When an eligible officer views a ringfenced opportunity, the detail page renders normally with no additional eligibility notice. The Apply CTA is shown as standard. For ringfenced Internal Jobs only, a subtle indicator is shown (e.g. "Available to you") to acknowledge the officer's eligibility without being intrusive. Design treatment to be confirmed by Amber. Ineligible officer — arrives via direct URL or shared link When an officer who is not eligible for a ringfenced opportunity lands on its detail page (e.g. via a shared URL, EDM, or bookmark), the page loads but displays a clear ineligibility notice: "This opportunity is not available to you." The Apply CTA is hidden. No application path is shown. Below the notice, the page surfaces up to 3 alternative opportunities the officer is eligible for, drawn from the live listing. If no alternatives exist, show the standard empty state copy. A link back to the full listing is always visible. POCDEX unavailable (fallback) If POCDEX data cannot be resolved at the time of the detail page load (lookup failure), the page renders normally without an eligibility indicator. The system does not block access on a failed lookup — degrade silently. Unauthenticated access An unauthenticated officer accessing any opportunity detail page via direct URL is redirected to login first, then returned to the original URL after authentication. Out of Scope (Sprint 5) Competency match ratio on the detail page — deferred to R1 Agency/grade/scheme-level eligibility display (e.g. "Open to MX officers only") — R1+ Personalised alternative opportunity recommendations — basic eligibility match only Open Questions (resolve before Sprint 5 planning) What is the eligible indicator treatment on the detail page? Amber to propose — AC2 is intentionally loose on visual spec. How are "alternative opportunities" selected for the ineligible state? Pure eligibility filter, or also ranked by relevance? Recommend eligibility-only for MVP. Does the EDM deep-link carry a source=edm param for analytics tracking? If yes, confirm with comms/EDM owner. Absorbs OTEP-133 (Access the hub via a deep link from an EDM) — ineligible-via-deep-link scenario fully covered by AC3–6 above. OTEP-133 can be closed.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-02*
