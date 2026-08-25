# OTEP-970: [PATHFINDER] UAT-OPP-016 — Invalid opportunity ID shows a clean "not found" state (OTEP-128)

**Status:** Done
**Assignee:** N/A
**Type:** Task
**Labels:** OTEP-128, Opportunity-Detail, PATHFINDER, uat

---

## Description

h3. Account C:

*C — Login email: Davien_SOH_FROM.TP@cscollege.gov.sg · Password: Davien@Cc2026*

h3. Scenario

Invalid opportunity ID shows a clean "not found" state

h3. Pre-conditions

—

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as C.
# Access a detail URL with an invalid/nonexistent opportunity ID.
## [https://uat.careercompass.gov.sg/opportunities/019fe00a-dc171e6-9c83-1de61483bf59?ms=browse|https://uat.careercompass.gov.sg/opportunities/019fe00a-dc171e6-9c83-1de61483bf59?ms=browse]

h3. Test Data

Account: C · Malformed or nonexistent opportunity ID

h3. Expected Result

"Something went wrong" message with a “Refresh” button. 

h3. Reference

UAT-OPP-016 on [https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/edit-v2/2508489043|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/edit-v2/2508489043|smart-link]

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-24*
