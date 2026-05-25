# OTEP-303: Pocdex Field check

**Status:** QA
**Assignee:** Pow Hwee TAN (PSD)
**Story Points:** N/A

---

## Description

Summary:  Align Pocdex API data fields and ordering logic for HRP/CUMULUS sources Description:   As a  consuming system downstream, Pocdex endpoints to return consistent source system names, synchronized flags, and deterministic array ordering,  so that  Core Team can process employment and position data accurately without discrepancies. getOfficer  =  GET /v1/officers/{pocdex_uid} getEmployment  =  GET /v1/officers/{pocdex_uid}/employments getPosition  =  GET /v1/officers/{pocdex_uid}/employments/{employment_id}/position Acceptance Criteria (Pocdex team to check, confirm and change): source_system  in  getOfficer ,  getEmployment , and  getPosition  returns  "HRP"  or  "CUMULUS"  (never "pocdex"). References to "HRPS" are updated to  "HRP" . For HRP records:   is_primary  ( getOfficer ) and  is_main_position  ( getPosition ) are always synchronized (both true or both false). For CUMULUS records:  The  getEmployment  endpoint guarantees a stable sequence where the first element is always the primary/main employment. getPosition  should have  job_id

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-05-24)
Hi Kingsley, *What is implemented:* * Source System: * We will update `source_system` across our endpoints to reflect the original source exactly as it appears in the upstream data (`HRP` or `CUMULUS`) instead of generically returning "pocdex”.  Note that we are returning it as is and not reformatting to otep-only.    * Job ID: *  `job_id` is exposed in `getPosition` payload,     *What we cannot implement* * Flag Synchronization: * `is_primary` and `is_main_position` are passed through exactly as they come from HRP. We cannot artificially synchronize them because real-world HR data edge cases occasionally cause them to diverge. For example, when an officer is on secondment, their primary employment contract remains with their home agency (`is_primary=true`), but the actual position they occupy is at the seconded agency, meaning their home agency position is no longer their active main position (`is_main_position=false`). OTEP must handle this logic and prioritize the correct record. * CUMULUS Array Ordering: * We will not guarantee that the primary employment is always at `[0]` in the `getEmployment` array. This is presentation/consumer logic. OTEP should filter the array on your end for the record where `is_primary == true`. I have created the MRs for these changes (cc    ) https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-pocdex/-/merge_requests/2 https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-service/-/merge_requests/49
