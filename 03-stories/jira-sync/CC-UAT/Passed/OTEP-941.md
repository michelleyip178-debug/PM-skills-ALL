# OTEP-941: [CORE] DISC-010 - Filters (Class Type / Domain / Provided By) narrow results (OTEP-83)

**Status:** Done
**Assignee:** N/A
**Type:** Task
**Labels:** CORE, OTEP-83, uat

---

## Description

h3. Account

*Account D — padmin2 ·* [*padmin2@cscollege.gov.sg*|mailto:padmin2@cscollege.gov.sg] *· password: Padmin@Cc2026*

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as D.
# Click "Explore all courses" from the Learning & Courses landing page.
# Open each filter category and select one value; observe the result count narrow.
# Remove the filter and confirm the full list returns.

h3. Test Data

* Default (no filter): 124 live courses.
* Class Type: Classroom (27) or E-Learning (97).
* Provided By: Civil Service College (72), Udemy (8), LinkedIn Learning (6), Harvard Business Publishing (5).
* Domain: e.g. "Test Domain 1" (23).

h3. Expected Result

Selecting any filter value narrows the results to only matching courses and the count updates accordingly.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-18)
🎉 Looks good!

---

**Christopher Woo** (2026-08-18)
✅ This is ok

---

**Charles Ho** (2026-08-18)
Class Type numbers working as intended Provided by numbers working as intended Test domain number working as intended

---
*Synced from Jira: 2026-08-24*
