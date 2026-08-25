# OTEP-868: [CORE] DUP-01 — Agency suffix on duplicate names (OTEP-610)

**Status:** Done
**Assignee:** N/A
**Type:** Task
**Labels:** CORE, OTEP-610, Profile_Page, uat

---

## Description

h3. Account

*Account C — Davien Soh ·* [*Davien_SOH_FROM.TP@cscollege.gov.sg*|mailto:Davien_SOH_FROM.TP@cscollege.gov.sg] *· password:* {{Davien@Cc2026}}

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as A.
# Open Add Competency and search a competency name that exists in more than one agency bank.

h3. Test Data

Account A. Search a duplicated agency competency (e.g. "Contract Oversight").

h3. Expected Result

# An agency competency whose name is duplicated shows the agency acronym in brackets, e.g. "{{Contract Oversight}}".
#  A WOG competency with a unique name shows no suffix. 
# There can be multiple duplicated competencies from the same agency.
# For duplicated agencies across agencies, they are ordered in alphabetical order by agency

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-11)
🎉 Looks good!

---

**Christopher Woo** (2026-08-11)
passed with comments: please ensure test instructions are aligned. account says to use “account C”, test steps and data says “account a”. while i understand there is no material impact which account it is for this ticket, it can still be confusing. thanks!

---

**rama moorthy** (2026-08-11)
(serene) pass

---
*Synced from Jira: 2026-08-24*
