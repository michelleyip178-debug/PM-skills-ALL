# OTEP-959: [PATHFINDER] UAT-OPP-005 — Pagination controls are fully hidden when everything fits on one page (OTEP-85)

**Status:** Done
**Assignee:** N/A
**Type:** Task
**Labels:** OTEP-85, Opportunity-Listing, PATHFINDER, uat

---

## Description

h3. Account C:

*C — Login email: Davien_SOH_FROM.TP@cscollege.gov.sg · Password: Davien@Cc2026*

h3. Scenario

Pagination controls are fully hidden when everything fits on one page

h3. Pre-conditions

Listing has ≤15 open opportunities

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as C.
# Load the listing.
# Do a random search with randomised text

h3. Test Data

Account: C · ≤15 open opportunities

h3. Expected Result

Pagination controls entirely absent, not just disabled

h3. Reference

UAT-OPP-005 on [https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/edit-v2/2508489043|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/edit-v2/2508489043|smart-link]

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Christopher Woo** (2026-08-11)
passed with comments: clarified with Michelle, pagination should be there, just disabled. i.e. <1> will show but arrows cannot be clicked.

---

**rama moorthy** (2026-08-11)
(serene) pass

---
*Synced from Jira: 2026-08-24*
