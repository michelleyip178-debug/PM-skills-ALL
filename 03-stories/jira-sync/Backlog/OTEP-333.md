# OTEP-333: Add ref_job_family and ref_job_function to shared refdata repository after upstream taxonomy is finalised

**Type:** Story
**Status:** Backlog
**Assignee:** Pow Hwee TAN (PSD)
**Story Points:** N/A

---

## Description

Context OTEP-332 creates the shared refdata repository for stable reference tables (ref_agency, ref_employment_type, ref_opportunity_type, ref_id_type). Job family and job function tables are deferred because business is considering revamping the taxonomy. The current definitions follow POCDEX, but any changes to the taxonomy are an upstream job (POCDEX team). Scope Once the upstream POCDEX team finalises the new job family/function taxonomy, add GORM models and read-only repository methods for ref_job_family and ref_job_function to the shared refdata package (internal/shared/refdata/) Include ingestion/sync path from POCDEX for these tables Also include ref_job_grade if needed at that point Dependencies OTEP-332 (shared refdata repository must exist first) Upstream: POCDEX team to confirm finalised job family/function taxonomy Needed For Release 1: Ringfencing criteria (OTEP-127) — filter opportunities by job family/function

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
