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

**AC1 — Eligible officer: page renders normally**

Given an eligible officer views a ringfenced opportunity detail page,
When the page loads,
Then the detail page renders as standard — no eligibility indicator or additional notice is shown.
The Apply CTA is visible.

**AC2 — Ineligible officer via direct link: ineligibility notice shown**

Given an officer who is not eligible for a ringfenced opportunity arrives via a direct URL, shared link, or EDM,
When the detail page loads,
Then a clear ineligibility notice is displayed per Amber's confirmed design.
The notice does not block the rest of the page content from loading.

**AC3 — Ineligible officer: Apply CTA is hidden**

Given an ineligible officer is on the ringfenced opportunity detail page,
When the page renders,
Then the Apply CTA is not shown. No application path is available.

**AC4 — Ineligible officer: link back to listing is shown**

Given an ineligible officer is on the ringfenced opportunity detail page,
When the page renders,
Then a link back to the full opportunity listing is visible so the officer can continue browsing.

**AC5 — POCDEX unavailable: fail open**

Given POCDEX data cannot be resolved at the time of the detail page load,
When an officer lands on the page,
Then the page renders normally as if the officer is eligible. Access is not blocked on a failed lookup. No error is shown to the officer.

**AC6 — Unauthenticated officer: redirect to login then return**

Given an unauthenticated officer accesses an opportunity detail page via direct URL,
When they land on the page,
Then they are redirected to login. After successful authentication, they are returned to the original URL.

---

## Out of Scope (Sprint 5)

- Eligible indicator ("Available to you") on the detail page — not in scope, page renders normally for eligible officers
- Alternative opportunity recommendations for ineligible officers — not in scope
- Agency/grade/scheme-level eligibility display (e.g. "Open to MX officers only") — R1+
- Competency match ratio on the detail page — OTEP-570 (S5 separate story)

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

1. Does the EDM deep-link carry a `source` param for analytics tracking? If yes, confirm with comms/EDM owner.
2. Ineligibility notice copy ("This opportunity is not available to you") — confirm BO sign-off received (#43) before dev starts.

---

*Created 2026-06-05. Absorbs OTEP-133. Companion to OTEP-127 (listing ringfencing). Gates: same as OTEP-127 (WOG AD #26, POCDEX #31).*
