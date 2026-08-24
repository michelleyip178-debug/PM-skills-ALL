# OTEP-531: Search API

**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Build the backend search API for the "Learning and courses" page. Officers need to browse and search the course catalogue by keyword and narrow results using the filter sidebar (Provided by, Domain, Class type). The response must also return the recomputed filter options ("facets") so the sidebar always reflects the current search — filter values with no matching courses disappear, and counts update as the user types or filters. Scope New endpoint:   GET /api/v1/course/search Request parameters Param Type Description q string, optional Keyword — case-insensitive substring match on course title provider string[], optional Provider codes (repeatable or comma-separated) — e.g. CSC, HBR, LIL, UDM domain string[], optional Domain names (via  course_domain ) class_type int[], optional Class type =  delivery_method  codes page int, default 1 Page number page_size int, default 20, max 100 Page size Response:   { items, totalCount, page, pageSize, facets } items  — course cards: id, course code, title, provider, class type, duration, paid flag, start date facets  —  provider  /  domain  /  classType , each a list of  { value, count }  for the current search context Behaviour / acceptance criteria Landing  (no keyword, no filters): first page of all live courses sorted by  course_type_start_date  DESC (newest first); facets list every value with ≥1 live course. Keyword  narrows both results and facets to matching courses. Filter combination:  multiple values within one filter = OR; across filters = AND. Disjunctive faceting:  a dimension's own selection does not constrain its own options — selecting "CSC" under Provided by narrows the results and the other facets, but the Provider facet still shows HBR/LIL/UDM so more can be added. Liveness gating  on every result and count:  deleted_at IS NULL AND course_display_status = 1 . Pagination normalised (page ≥ 1; page_size default 20, capped 100);  totalCount  reflects all matches. Technical notes Adds a  pg_trgm  GIN index on  course.course_type_description  so the keyword  ILIKE '%q%'  is index-backed (migration, additive only — no schema changes). Domain filter resolves via  EXISTS  on  course_domain  so courses aren't row-multiplied. 5 queries per request (1 count + 1 page + 3 facet GROUP BYs), all index-friendly. Exact substring matching only — fuzzy/typo tolerance deferred (documented option: exact-first "did you mean" via trigram + Levenshtein).

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-20*
