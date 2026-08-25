# OTEP-965: [PATHFINDER] UAT-OPP-011 — "Clear all" resets every active filter in one action (OTEP-86)

**Status:** Done
**Assignee:** N/A
**Type:** Task
**Labels:** OTEP-86, Opportunity-Filtering, PATHFINDER, uat

---

## Description

h3. Account C:

*C — Login email: Davien_SOH_FROM.TP@cscollege.gov.sg · Password: Davien@Cc2026*

h3. Scenario

"Clear all" resets every active filter in one action

h3. Pre-conditions

One or more filters active

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as C.
# With filters active, click "Clear all."

h3. Test Data

Account: C

h3. Expected Result

All filters removed, full unfiltered listing shown, result count updates, "Clear all" option itself disappears

h3. Reference

UAT-OPP-011 on [Consolidated Test Plan — Pathfinder|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2481753934/Consolidated+Test+Plan+Pathfinder]

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-12)
Minor clarification that you are referring to “Clear” and not “Clear all”

---

**serene** (2026-08-11)
pass

---

**Christopher Woo** (2026-08-11)
passed with comments: quite interesting, “clear all” makes it change sort by “Closing Date” back to “Posting Date” also. not an issue, just an interesting find.

---
*Synced from Jira: 2026-08-24*
