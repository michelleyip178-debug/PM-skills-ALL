# OTEP-977: [PATHFINDER] UAT-OPP-022 — Officer with competencies but zero overlap sees 0/5, not an error or blank state (OTEP-128)

**Status:** Backlog
**Assignee:** N/A
**Type:** Task
**Labels:** OTEP-128, Opportunity-Detail, PATHFINDER, uat

---

## Description

h3. Account

*OPP-C3 — Nurul Aisyah · nurul.aisyah@psd_test.gov.sg · Nurul@Cc2026 · has competencies but none of the 5 → 0/5. Read-only; competencies to be provisioned in Compass.*

h3. Scenario

Officer with competencies but zero overlap sees 0/5, not an error or blank state

h3. Pre-conditions

Some Competencies Officer (P6), with a specific opportunity they have zero matching skills for

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as OPP-C3.
# Navigate to the OPP_MAX_COMP_MATCH opportunity.

h3. Test Data

Account: OPP-C3
 · Opportunity: OPP_MAX_COMP_MATCH (same as UAT-OPP-020)

h3. Expected Result

Opportunity displays "0/5" competency match — not a blank field or error

h3. Note

We dont need POCDEX profile but we need Compass mock user with Competencies.




  to share the uer accoumnt and competencies

h3. Reference

UAT-OPP-022 on [Consolidated Test Plan — Pathfinder|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2481753934/Consolidated+Test+Plan+Pathfinder]

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-03*
