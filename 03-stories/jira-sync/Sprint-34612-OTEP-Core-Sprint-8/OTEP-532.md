# OTEP-532: Filter API

**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

As an officer on the course search page, I need the filter dropdowns (Product Type, Provider, Domain, Competency) populated, so I can narrow the catalogue search. Description  Add the  filter-options  endpoint that drives the search filter dropdowns introduced in OTEP-531. Second of the three stacked PRs (after OTEP-531 search; before OTEP-533 autocomplete). Endpoint  GET /api/v1/course/filters  — returns the options for all four filter facets: Product Type  and  Provider  — fixed  {code, label}  enums (per the CSC course-data spec). Domain  — distinct  course_domain.domain_name  from the active catalogue. Competency  — distinct  course_competency.psd_competency_id  with the resolved competency name ( {code, name} ), from the active catalogue. Acceptance Criteria Response includes the fixed  Product Type  and  Provider  options as  {code, label} . Response includes the  distinct Domain  names tagged on active courses. Response includes the  distinct Competencies  ( {code, name} ) tagged on active courses. Domain/Competency lists are sourced from active, non-deleted courses (consistent with OTEP-531 search). Standard  {data, meta, error}  envelope; controller, domain, repository, messages, mocks, unit tests at the 80% coverage gate; Swagger updated. Out of scope Title autocomplete ( OTEP-533 ) — stacked separately. Applying the filters (that's the OTEP-531 search endpoint); this only supplies the options. Technical notes New code in  course/domain  ( CourseFilters , Product Type/Provider enums,  ListDomains  /  ListCompetencies ),  course/repository  (two distinct queries),  course/controller  ( GetCourseFilters ), plus a  /course/filters  route on the existing course router. Read-only over  course ,  course_domain ,  course_competency ,  competency .  No migration.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-20*
