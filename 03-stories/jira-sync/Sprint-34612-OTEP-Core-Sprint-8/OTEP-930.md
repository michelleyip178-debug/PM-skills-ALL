# OTEP-930: Role Competencies Update

**Status:** QA
**Assignee:** Kingsley Low
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Goal Change how an officer's role / job competencies are pulled in  ComputeOfficerCompetencies , so the job/agency competencies are keyed off  job_id  (not the family+function+grade triple, as today). This also aligns the competency path with the recommendation path, which already joins on  j.job_id = pji.job_id . Steps Step 1  - pull competencies by  job_id  from the job table: officer's  position_jobinfo.job_id  ->  job.core_competency . Step 2  - pull competencies by  role_id = UPPER(jobFamilyLabel + jobFunctionLabel + jobGradeLabel)  from  role_competency . Combine Step 1 + Step 2 (plus self-declared / OTG) and  de-duplicate  keeping the highest proficiency. Current vs proposed Today Step 1 resolves the job via  GetJobByPositionID  - joins position -> job on the (family, function, grade) triple (LIMIT 1). Proposed: resolve the job by  job_id . Step 2 ( role_competency  by role_id labels) and the merge/dedupe are unchanged. How the role_id labels are formed family/function/grade UUIDs -> ref-table lookup by id ( ref_job_family/function/grade.label ) -> concatenate -> upper-case. The UUIDs are available on  position_jobinfo  directly ( job_family_id ,  job_function_id ,  job_grade_id ), so Step 2 can derive role_id straight from the position, independent of the Step 1 job lookup. Where the change lands Repository ( officer_competency.go ): new  GetJobByJobID  (SELECT job WHERE job_id = ? AND is_active AND not deleted); read  position_jobinfo.job_id  for the position; keep the ref-label + role_competency lookups. Domain ( officer_competency_service.go  /  ComputeOfficerCompetencies ): get the position's job_id; Step 1 via GetJobByJobID; Step 2 via role_id from the position labels; merge +  DeduplicateByCompetencyID . Interface + mock: add the new repo method; regen mock. Tests: step-1-only, step-2-only, overlap (dedupe keeps highest), blank job_id, job_id matching multiple rows. Decisions to confirm job_id  is NOT unique in job (unique key is job_id + agency_id + job_family_id + job_function_id). Scope Step 1 by job_id + the officer's agency, or is job_id effectively unique per agency (prefix e.g. BCAJ...)?  Step 2 labels source: the position's family/function/grade (recommended - reflects the officer's actual role) vs the job-resolved-by-job_id's. position_jobinfo.job_id  can be blank ('') -> Step 1 yields nothing, fall through to Step 2 only. Confirm acceptable. On conflict, keep the highest proficiency (current dedupe rule). Confirm. Notes Branch off  main  - no dependency on OTEP-806/807. All inputs (compute path, GetJobByPositionID, role_competency, position_jobinfo.job_id) already exist in main. Format-agnostic: only changes which job row is read, not how the competency map is parsed - works with main's current format. Small change (~150-200 LOC; 1-2 core files + interface/mock + tests). No migration, no API/contract change. Behavioural: changes which competencies officers see (job-by-job_id vs job-by-triple). Needs local end-to-end verification + officer_competency re-sync. Step 2 is blocked locally by the role_competency grade-FK bug (bug B) until fixed. File overlap with OTEP-806/807 in officer_competency_service.go / officer_competency.go -> minor merge conflict for whichever lands second.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Kingsley Low** (2026-07-30)
This is duplicated ticket of

---
*Synced from Jira: 2026-09-07*
