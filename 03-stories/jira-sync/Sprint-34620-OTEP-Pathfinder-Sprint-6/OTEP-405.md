# OTEP-405: [FE/BE] Keyword Search for Opportunities

**Status:** In Progress
**Assignee:** Thomas Huchedé
**Story Points:** 3
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

As an officer, I want to search for opportunities by keyword so I can quickly find roles relevant to my interests without scrolling through the full listing. Acceptance Criteria: A search box labelled "Search jobs and opportunities" is visible at the top of the listing page, above the filters As I type, the listing updates to show only opportunities whose title and agency matches my keyword Search is not case-sensitive and returns partial matches — typing "data" returns "Data Analyst" and "Senior Data Engineer" If nothing matches, the standard no results state is shown Search and type filters work together — I can search and filter at the same time Clearing the search box brings back the full listing (keeping any active filters) The listing does not update until I click on Search.  Search results are ordered by relevance first, then posting date.   Out of Scope   If a search result matches within the opportunity description (not the title or agency), the card must display a visible snippet or signal indicating why it matched — e.g. highlighted excerpt from the description. Design pattern: follow Google's "match in content" treatment.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-495 | Add queryParam on backend to handle text search | Done |
| OTEP-496 | Wire frontend search bar to backend api | Done |
| OTEP-668 | [BUG] Bugs open for Search opportunities feature | To Do |

---

## Latest Comments

**Rathika Ramalingam** (2026-06-29)
Test Results (in Dev) -

---

**Michelle Yip** (2026-06-17)
Regarding #2,  a. Do we exclude description to search only title and agency <MY> Yes  b. Is the search dynamic as the user keys in or we need to hit Search button (#7) to trigger the search? <MY> need to search button  c. If dynamic, do we have minimum characters before triggering search to filter <MY> N/A  Regarding #8  a. Can we define ‘by relevance’ - is it the weight based on no of occurrence + location + exact match of the search text? <MY? exact match of the search text in title or agency. Is this good enough?

---

**Rathika Ramalingam** (2026-06-17)
I have these questions. Pls clarify. cc:       1. Regarding #2,   a. Do we exclude description to search only title and agency   b. Is the search dynamic as the user keys in or we need to hit Search button (#7) to trigger the search?  c. If dynamic, do we have minimum characters before triggering search to filter   2. Regarding #8  a. Can we define ‘by relevance’ - is it the weight based on no of occurrence + location + exact match of the search text?

---
*Synced from Jira: 2026-07-27*
