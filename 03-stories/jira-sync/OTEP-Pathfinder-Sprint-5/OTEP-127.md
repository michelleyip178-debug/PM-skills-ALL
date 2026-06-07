# OTEP-127: Apply ringfencing criteria to the opportunity listing

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Sprint:** OTEP-Pathfinder Sprint 5

---

## Description

**User story:** As a public service officer, I want the opportunity listing to automatically show only the opportunities I am eligible for, so that I don't waste time on postings I can't apply for and the hub feels relevant to my situation.

**Sprint 5 scope:** BE eligibility filter applied to the listing API using POCDEX data. FE listing reflects filtered + pinned results. No competency match display — that is R1.

---

## Acceptance Criteria

### Eligibility filter (BE)

1. The listing API filters opportunities based on the officer's POCDEX data resolved at login. Ineligible opportunities are excluded from the response — they do not appear in the listing.
2. Ringfenced Internal Jobs for which the officer is eligible are pinned to the top of the listing, above all other opportunity types.
3. If POCDEX data is unavailable at login (e.g. POCDEX lookup fails or returns no result), the listing falls back to showing all opportunities unfiltered. No error is shown to the officer — the experience degrades silently to the unfiltered state.

### Session refresh

4. Ringfencing is re-evaluated on each login. If an officer has transferred agencies since their last session, the listing reflects their new eligibility on next login — not mid-session.
5. Within a session, the eligibility filter does not change even if the officer's POCDEX data changes externally.

### Unauthenticated access

6. An unauthenticated officer attempting to access the listing is redirected to login before any opportunity data is returned. (Ref: auth story.)

---

## Out of Scope (Sprint 5)

- Competency match ratio on listing cards — deferred to R1
- Ringfenced detail page states (eligible / ineligible notice) — OTEP-390
- Category or agency filters
- Real-time POCDEX refresh mid-session

---

## Dependencies

- WOG AD onboarding (#26, Fabian) — POCDEX resolution requires authenticated session
- POCDEX read replica confirmation (#31, Daryll) — CP item #2 due 13 Jun
- OTEP-352 — Load POCDEX production code table
- OTEP-390 — Ringfenced detail page states (companion story)

---

## Gates (must clear before Sprint 5 planning)

- WOG AD domain submission confirmed (#26)
- POCDEX read replica confirmed (#31)
- Ringfencing logic from OTG confirmed with Rama (what fields drive eligibility?)

---

*Redrafted 2026-06-05 — original AC was a placeholder. Merged intent of OTEP-127 (listing filter) from PRD. Detail page states split into companion story OTEP-390.*
