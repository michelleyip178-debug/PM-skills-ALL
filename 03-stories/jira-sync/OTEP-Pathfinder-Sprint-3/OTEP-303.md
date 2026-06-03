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

**Kingsley Low** (2026-05-25)
Q1: Noted  Q2: Yes, understood that Pocdex is the “middle layer” between Cumulus + HRP and OTEP. Also get the context where Cumulus do not have the concept of “main position”. Thus my question is simply asking that, will Pocdex handle main position before passing to OTEP. If not, how should OTEP now which one is the main position if multiple position appeared?

---

**Pow Hwee TAN (PSD)** (2026-05-25)
Q1 - I don't have an answer on this.  I will have to check because it depends on the business decisions that were coded.  Intuitively I would think there shouldn’t be but if that is the case it is a DQ problem on pocdex side.  But I can’t confirm without checking with the current pocdex team.    Is this a blocker to u now? Q2.  You mean you are checking Workday’s own API that they don't have a is_main_position?  The pocdex api provided here is independent of Cumulus or HRP.

---

**Kingsley Low** (2026-05-25)
Hi    , Thanks for the clarification; noted on the implemented changes from the Pocdex side. I just have a couple of points I'd like to clarify regarding  HRP  and  CUMULUS : HRP:  Based on the Position API, if  is_main_position = true , it will be treated as the main position, regardless of whether the employment's  is_primary  is set to  false . Question:  For HRP, is it possible to have multiple records where  is_main_position = true ? CUMULUS:  Since CUMULUS does not have  is_main_position  in their Position API, we will refer to the  is_primary  field in their  Employment API  instead.

*Synced from Jira: 2026-06-03*
