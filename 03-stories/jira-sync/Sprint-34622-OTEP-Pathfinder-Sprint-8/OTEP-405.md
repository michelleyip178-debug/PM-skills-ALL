# OTEP-405: [FE/BE] Keyword Search for Opportunities

**Status:** Done
**Assignee:** Thomas Huchedé
**Story Points:** 3
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

As an officer, I want to search for opportunities by keyword so I can quickly find roles relevant to my interests without scrolling through the full listing. Acceptance Criteria: A search box labelled "Search jobs and opportunities" is visible at the top of the listing page, above the filters As I type, the listing updates to show only opportunities whose title and agency matches my keyword Search is not case-sensitive and returns partial matches — typing "data" returns "Data Analyst" and "Senior Data Engineer" If nothing matches, the standard no results state is shown Search and type filters work together — I can search and filter at the same time Clearing the search box brings back the full listing (keeping any active filters) The listing does not update until I click on Search.  Search results are ordered by relevance first, then posting date.   Out of Scope   If a search result matches within the opportunity description (not the title or agency), the card must display a visible snippet or signal indicating why it matched — e.g. highlighted excerpt from the description. Design pattern: follow Google's "match in content" treatment.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-495 | Add queryParam on backend to handle text search | Done |
| OTEP-496 | Wire frontend search bar to backend api | Done |
| OTEP-668 | [BUG] Bugs open for Search opportunities feature | QA |

---

## Latest Comments

**Thomas Huchedé** (2026-08-13)
Moving back to QA lane since all the subtask have been completed and the fix of the search logic will be done in a separate ticket

---

**Pow Hwee TAN (PSD)** (2026-08-11)
- is this ticket completed?  If so just update it will do, thanks.  Am checking through if we have outstanding features.

---

**Rathika Ramalingam** (2026-06-29)
Test Results (in Dev) -

---
*Synced from Jira: 2026-08-19*
