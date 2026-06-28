# OTEP-408: [BE] Listing API — apply ringfencing eligibility filter

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** 8

**Sprint:** OTEP-Pathfinder Sprint 5

**Parent:** OTEP-127 (spike)

---

## Description

**User story:** As the system, I need the listing API to filter opportunities based on the officer's eligibility so that ineligible ringfenced opportunities are not returned in the listing response.

**Acceptance Criteria:**

1. The listing API filters opportunities based on the officer's POCDEX data resolved at login. Ineligible opportunities are excluded from the response — they do not appear in the listing.
2. Ringfenced Internal Jobs for which the officer is eligible are pinned to the top of the listing, above all other opportunity types.
3. If POCDEX data is unavailable at login (lookup fails or returns no result), the listing falls back to showing all opportunities unfiltered. No error is shown to the officer — degrades silently.
4. Ringfencing is re-evaluated on each login. If an officer has transferred agencies since their last session, the listing reflects their new eligibility on next login — not mid-session.
5. Within a session, the eligibility filter does not change even if the officer's POCDEX data changes externally.
6. An unauthenticated officer attempting to access the listing is redirected to login before any opportunity data is returned.

**Out of scope:**
- Competency match ratio on listing cards — R1
- Ringfenced detail page states — OTEP-390
- Real-time POCDEX refresh mid-session

## Dependencies

- OTEP-127 spike output — eligibility contract must be defined first
- WOG AD onboarding (open item #26, Fabian)
- POCDEX read replica (open item #31, Daryll)
- OTEP-352 — Load POCDEX production code table

## Gates (must clear before S5 planning)

- WOG AD domain submission confirmed (#26)
- POCDEX read replica confirmed (#31)
- OTEP-127 spike output reviewed and accepted

*Synced from Jira: 2026-06-26*
