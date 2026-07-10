# OTEP-105: Port over existing OTG competencies

**Type:** Story
**Status:** Done
**Assignee:** N/A
**Story Points:** N/A

---

## Description

*User Story*

As a logged in officer who has previously used OTG before to add competencies, I want to see the same competencies reflect on OTEP so there is a seamless transition and I do not need to add them back again.

*Acceptance Criteria*

# Users will see all competencies that were self-added previously on OTG reflect on OTEP without needing to manually re-add them.
# Proficiency level is omitted for now
# OTG competencies must be correctly categorised into the three types of competencies and displayed under either:
##  role-based competencies section (which contains Core Competencies and Functional competencies section)
## or the self-declared competencies section
# Competency categorising logic 
## First check if it matches the officer’s role-based core competencies. If yes, display on profile. 
## If no, check if it matches the officers role-based functional competencies. If yes, display on profile
## If no, add to self-declared competency section

*Tech Notes*

* The data file from OTG can be found in the [raw_users_skills excel (Otep2026)|https://gccprod-my.sharepoint.com/:x:/r/personal/michelle_yip_psd_gov_sg/Documents/Microsoft%20Teams%20Chat%20Files/RAW_USER_SKILLS%20Report%20(1).csv?d=w5d53f87356b04e5fbd254730b3db69d7&csf=1&web=1&e=QBupok]
** it only has user_id and competency NAME, not ID
** userID: they are either
*** (1) pocdex ID if their accounts were created through pocdex
*** (2) NRIC or email address if their accounts were created manually. Ignore officers that were created manually as they are not in POCDEX and are deprioritised for OTEP
*** Competency Name  - competencies can also contain CEG competencies (from their own bank) which we want to exclude completely from OTEP
* This means to show and distinguish competencies in OTEP we will need to
** find the officer in our database using POCDEX ID (always starts with P)
** Get the roleID, use it to map to the role profile bank to attain the list of competency IDs assigned to the officer
** use these competency ID to call the competency names on another table
** Compare the competency names of the user from the raw_user_skills doc against the list of the user’s role-based competencies. 
** The delta is then checked against the rest of the competency bank. 
*** If a match is found, then display under the self-declared competencies section. 
*** If no match is found, omit from OTEP as they are Fuel50’s competencies
*** *TO double check: CEG competencies are forever lost*
** Competency names in the Raw_users_skills report are unique

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-01*
