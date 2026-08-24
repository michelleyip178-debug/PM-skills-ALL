# OTEP-804: Update Master Job Family and Job Function with master data 

**Status:** QA
**Assignee:** Kingsley Low
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

ref_job_family  (upsert keyed on  code ) Excel column Header → DB column Notes B HRPS job family code ref_job_family.code Conflict key  —  ON CONFLICT (code) . Blank → row skipped A Job Family ref_job_family.label Updated on conflict ( SET label = EXCLUDED.label ) — — created_by  /  updated_by 'system' — — id ,  version ,  status ,  is_active ,  description , timestamps DB defaults ref_job_function  (upsert keyed on  code ) Excel column Header → DB column Notes E HRPS job function code ref_job_function.code Conflict key  —  ON CONFLICT (code) . Blank → row skipped D Job Function (Description) ref_job_function.label Updated on conflict — — created_by  /  updated_by 'system' — — id , defaults, timestamps DB defaults FK link —  ref_job_function.job_family_id  (unchanged from 806, still runs) Source → DB column Notes Col  B  (family code) + Col  E  (function code) ref_job_function.job_family_id SetJobFunctionJobFamily  resolves the family by its code and sets the FK on the function.  Not  touched by the by-code upserts Key point:  the two matching keys are  Col B  (family) and  Col E  (function) — both HRPS codes. Labels (Col A / Col D) are the  payload  that gets written/reconciled, not the match criteria. That's the whole intent of the ticket: match/upsert  by code , not by name.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-20*
