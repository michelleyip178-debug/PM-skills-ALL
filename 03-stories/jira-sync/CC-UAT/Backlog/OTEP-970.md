# OTEP-970: [PATHFINDER] UAT-OPP-016 — Invalid opportunity ID shows a clean "not found" state (OTEP-128)

**Status:** Backlog
**Assignee:** N/A
**Type:** Task
**Labels:** OTEP-128, Opportunity-Detail, PATHFINDER, uat

---

## Description

h3. Account

*OPP-B1 — Jun Hao Lim · junhao.lim@psd_test.gov.sg · password: Junhao@Cc2026 · Standard active officer; read-only browse account — reused across all cases, never changed.*

h3. Scenario

Invalid opportunity ID shows a clean "not found" state

h3. Pre-conditions

—

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as OPP-B1.
# Access a detail URL with an invalid/nonexistent opportunity ID.

h3. Test Data

Account: OPP-B1 · Malformed or nonexistent opportunity ID

h3. Expected Result

"Opportunity not found" message with a link back to the listing — not a broken page

h3. Reference

UAT-OPP-016 on [Consolidated Test Plan — Pathfinder|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2481753934/Consolidated+Test+Plan+Pathfinder]

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-03*
