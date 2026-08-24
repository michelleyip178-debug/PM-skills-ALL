# OTEP-699: Job Position data import 1 to many

**Status:** QA
**Assignee:** Kingsley Low
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Summary  Implement job family–function relation ingestion and efficient job loading pipeline. Description This change introduces a new  job_family_function_relation  table that captures valid job family ↔ job function pairings from the masterlist Excel file. It also refactors the job ingestion pipeline to use these relations as a gate for inserting job records. Changes Created  job_family_function_relation  table with a unique constraint on  (job_family_id, job_function_id) Enabled the previously disabled  IngestDataTypeJobFamilyAndFunction  pipeline, which now populates  ref_job_family ,  ref_job_function , and  job_family_function_relation  from the masterlist Refactored job sheet processing (HRPS and Cumulus) to pre-load reference maps once per sheet instead of querying the DB per row, reducing query overhead significantly Multiline family/function cell values are now split and expanded into a cartesian product; only pairs that exist in  job_family_function_relation  produce a job insert Fixed a local debug port issue ( DB_PORT ) by switching  godotenv.Load  to  godotenv.Overload  so  .env  always takes precedence over shell environment Acceptance Criteria Running the job family/function ingest populates  job_family_function_relation Running the role ingest only creates  job  rows for valid family–function pairs All unit tests pass

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Kingsley Low** (2026-07-29)
This ticket is resolved in  OTEP-806

---

**Kingsley Low** (2026-07-15)
Pending confirmation from stakeholder for changing family and function name to code

---
*Synced from Jira: 2026-08-20*
