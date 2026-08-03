# OTEP-947: [CORE] DTL-04 - Optional unavailable fields omitted (OTEP-84)

**Status:** Backlog
**Assignee:** N/A
**Type:** Task
**Labels:** CORE, OTEP-84, uat

---

## Description

h3. Account

*Account LC1 - Wen Jie Sim - wenjie.sim@psd_test.gov.sg - password: Wenjie@Cc2026 - (Standard officer; no course recommendations (Jumpstart POC not live). Read-only - all Courses UAT is browse/search/view, so this account is stable/immutable.)*

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and Log in as LC1.
# Open a course whose LEARN record is missing some optional fields.

h3. Test Data

Account LC1. A course missing e.g. outline or dates.

h3. Expected Result

Unavailable optional fields are omitted entirely - no empty labels or placeholders are shown.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-03*
