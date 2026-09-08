# OTEP-807: Update Competency for Job Family, Job Function , Agency, Job Grade with master data

**Status:** QA
**Assignee:** Kingsley Low
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Sheets in scope:  WOG OCCs ,  Agency OCCs ,  WOG FCs ,  Agency FCs  (all identical layout). AC-M1 — Competency Code (Col K →  competency.competency_code )  Given a competency row, when it is imported, then  Col K (Competency Code)  is stored (trimmed) as  competency.competency_code  — the competency's own identity (UNIQUE; upsert key). AC-M2 — Source (Col A →  competency.source )  Given a row, when it is imported, then  Col A (Source System)  is stored  UPPER-cased  as  competency.source  (must be one of HRPS / CUMULUS / OTG). AC-M3 — Agency (Col C →  competency.agency_id )  Given a row, when it is imported, then  Col C (POCDEX Agency Code)  is resolved against  ref_agency.code  and stored as  competency.agency_id . When Col C is  blank ,  agency_id  is stored  NULL ; when Col C has a value that  does not match , the competency is  skipped + reported . AC-M4 — Job Family (Col G →  competency.job_family_id )  Given a row, when it is imported, then  Col G (Job Family IDs)  is resolved against  ref_job_family.code  and stored as  competency.job_family_id .  Blank → NULL ;  present-but-unmatched → skip + report . AC-M5 — Job Function (Col I →  competency.job_function_id )  Given a row, when it is imported, then  Col I (Job Function IDs)  is resolved against  ref_job_function.code  and stored as  competency.job_function_id .  Blank → NULL ;  present-but-unmatched → skip + report . AC-M6 — Competency Type (Col E →  competency.competency_type )  Given a row, when it is imported, then  Col E (Core / Functional)  maps to  competency.competency_type :  Functional  →  FUNC , otherwise  CORE . AC-M7 — Competency Name (Col J →  competency.competency_name )  Given a row, when it is imported, then  Col J (Competency)  is stored as  competency.competency_name . AC-M8 — Definition (Col L →  competency.definition )  Given a row, when it is imported, then  Col L (Definition)  is stored as  competency.definition  (default  NA  when blank). AC-M9 — Proficiency scale (Cols M–Q →  competency.min_scale  /  max_scale )  Given a row, when it is imported, then  Cols M–Q (Proficiency Level 1–5)  determine  competency.min_scale  and  competency.max_scale  (from the first/last populated level; default 1–5). AC-M10 — Proficiency descriptions (Cols M–Q →  ref_competency_proficiency_description )  Given a row that passes the code gates, when it is imported, then the per-level text in  Cols M–Q  is written to  ref_competency_proficiency_description  (one row per  competency_code  + level). AC-M11 — Agency-specific flag (sheet →  competency.is_agency_specific )  Given a row, when it is imported, then  competency.is_agency_specific  is derived from the  sheet :  Agency OCCs  /  Agency FCs  →  true ;  WOG OCCs  /  WOG FCs  →  false  (not from any column). AC-M12 — Label-only columns not stored  Given a row, when it is imported, then  Col B, Col D (agency name/description), Col F (Job Family name), Col H (Job Function name), Col R (Rating Scale)  are  not  persisted on  competency  — only the code columns (C/G/I) are authoritative. AC-M13 — System-set columns  Given a row is imported, then  competency.id  =  uuidv7() ,  proficiency_level  = placeholder  PL1 ,  is_active  = true,  created_by / updated_by  =  "system" ,  version  = 1, timestamps =  NOW()  — none sourced from Excel. AC-M14 — No fan-out, no grade  Given a competency row, when it is imported, then it produces  exactly one   competency  record (Cols C/G/I are single-valued), and  no Job Grade  is read or required.  Column-mapping summary (for reference) DB column ( competency ) Excel col Header competency_code K Competency Code source A Source System agency_id C POCDEX Agency Code job_family_id G Job Family IDs job_function_id I Job Function IDs competency_type E Core / Functional competency_name J Competency definition L Definition min_scale  /  max_scale M–Q Proficiency Level 1–5 is_agency_specific (sheet) WOG* → false, Agency* → true (not stored) B, D, F, H, R labels / not mapped Rule (both C/G/I):  resolved read-only by code —  blank → NULL, present-but-unmatched → skip + report, never create master data.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-09-07*
