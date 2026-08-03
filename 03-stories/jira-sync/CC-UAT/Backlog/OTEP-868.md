# OTEP-868: [CORE] DUP-01 — Agency suffix on duplicate names (OTEP-610)

**Status:** Backlog
**Assignee:** N/A
**Type:** Task
**Labels:** CORE, OTEP-610, Profile_Page, uat

---

## Description

h3. Account

*Account A — Wei Ming Tan · weiming.tan@psd_test.gov.sg · password: Weiming@Cc2026 · (Profile filled; has role + self-declared competencies)*

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as A.
# Open Add Competency and search a competency name that exists in more than one agency bank.

h3. Test Data

Account A. Search a duplicated agency competency (e.g. "Gives guidance").

h3. Expected Result

# An agency competency whose name is duplicated shows the agency acronym in brackets, e.g. "Gives guidance (MOE)".
#  A WOG competency with a unique name shows no suffix. 
# There can be multiple duplicated competencies from the same agency.
# For duplicated agencies across agencies, they are ordered in alphabetical order by agency

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-03*
