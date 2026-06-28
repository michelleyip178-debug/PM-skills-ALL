# OTEP-409: [FE] Listing — reflect ringfenced and pinned results

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** 3

**Sprint:** OTEP-Pathfinder Sprint 5

**Parent:** OTEP-127 (spike)

---

## Description

**User story:** As an officer, I want the opportunity listing to show only opportunities I'm eligible for, with relevant ringfenced roles surfaced at the top, so the listing feels relevant to my situation without me having to filter manually.

**Acceptance Criteria:**

1. The listing renders the filtered response from OTEP-127-B with no additional FE filtering logic — eligibility is fully determined by the BE.
2. Pinned eligible ringfenced Internal Jobs appear at the top of the listing, above all other opportunity types, as returned by the API.
3. The fallback (unfiltered) and filtered states render identically from the FE perspective — no special visual treatment needed for the fallback state.
4. No card-level eligibility indicator is shown on the listing (e.g. no "Available to you" badge on listing cards) — that treatment is on the detail page only (OTEP-390).

## Out of scope

- Competency match indicators on cards — R1
- "Available to you" badge on listing cards — R1
- Any FE eligibility logic — BE owns all filtering

## Dependencies

- OTEP-408 (BE eligibility filter) — must be complete before FE can be built
- OTEP-390 — Ringfenced detail page states (companion story)

*Synced from Jira: 2026-06-26*
