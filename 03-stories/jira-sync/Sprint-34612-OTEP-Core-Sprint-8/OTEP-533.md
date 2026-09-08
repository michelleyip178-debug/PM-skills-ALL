# OTEP-533: Autocomplete API

**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

As an officer typing in the course search bar, I want title suggestions as I type, so I can quickly jump to a course without typing the full name. Description  Add the  typeahead/autocomplete  endpoint for the course search bar. Third and final of the stacked PRs (after OTEP-531 search and OTEP-532 filters). Endpoint  GET /api/v1/course/autocomplete?q=…  — returns course  title  suggestions matching the keyword. Titles that  start with  the keyword are ranked  before  titles that merely  contain  it. Results capped at  10 . A  blank  query returns  no  suggestions. Reads  course  only (read-only). Acceptance Criteria Given a partial keyword, returns courses whose  title  matches it (case-insensitive). Prefix matches  (title starts with the keyword) ordered before  substring matches  (title contains the keyword). Results capped at a small number ( 10 ). A  blank/empty   q  returns an empty suggestion list. Only active, non-deleted courses are suggested (consistent with OTEP-531/532). Standard  {data, meta, error}  envelope; controller, domain, repository, messages, mocks, unit tests at the 80% coverage gate; Swagger updated. Out of scope Full keyword search across  name / description / outline  — that's the OTEP-531 search endpoint. Autocomplete matches  title only . Filters (OTEP-532).

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-09-07*
