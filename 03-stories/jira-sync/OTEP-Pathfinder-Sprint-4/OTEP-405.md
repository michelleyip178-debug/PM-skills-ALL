# OTEP-405: [FE/BE] Keyword Search for Opportunities

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** 3

**Sprint:** OTEP-Pathfinder Sprint 4

---

## Description

**User story:**
As an officer, I want to search for opportunities using keywords, so that I can quickly find roles relevant to my interests without scrolling through the full listing.

**Acceptance Criteria:**

1. A text input labelled "Search jobs and opportunities" is displayed at the top of the listing page, above the filter sidebar.
2. As the officer types, the listing results update to show only opportunities where the keyword appears in the title, agency name, or opportunity type.
3. Search is case-insensitive. Partial matches are returned (e.g. "data" returns "Data Analyst", "Senior Data Engineer").
4. If no results match the keyword, the existing empty state (OTEP-268) is shown — no new empty state needed.
5. Keyword search and type filters (OTEP-86) work together — applying both narrows results by both criteria simultaneously.
6. Clearing the search input restores the full listing (respecting any active filters).
7. The search input is debounced — the API is not called on every keystroke. Minimum debounce: 300ms.
8. While results are loading after a search, the loading spinner (OTEP-281) is shown.

**Out of scope:**
- Full-text search across opportunity description body
- Search suggestions or autocomplete
- Search history or saved searches
- Relevance ranking (results sort by posting date, same as default listing)

**Dependencies:**
- OTEP-86 (filter by type) — search must compose with active filters
- OTEP-281 (loading states) — spinner shown during search fetch
- BE: listing API must accept a `q` (query) param and filter results server-side

**Notes for engineer:** Confirm with Pow Hwee whether search is server-side (preferred) or client-side. Server-side is strongly recommended given pagination is in place.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-06-11*
