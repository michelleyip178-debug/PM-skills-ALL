# OTEP-942: [CORE] DISC-14 - Pagination: shown only >15 results, 15/page, prev/next disabled states (OTEP-83)

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
# Run a search that returns 15 or fewer courses.
# Run a broader search that returns more than 15 courses.
# Note Previous on the first page; navigate Next → last page; note Next on the last page.

h3. Test Data

* Narrow (≤15): "Leadership" (2) or "Management" (9).
* Broad (>15): "data" (25) or "Test" (83). Default (no query) = 124 courses → paginated.

h3. Expected Result

* Pagination appears only when >15 courses are returned; 15 tiles per page.
* Previous disabled on the first page; Next disabled on the last page.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-18)
🎉 Looks good!

---

**Charles Ho** (2026-08-18)
looks good

---

**Christopher Woo** (2026-08-18)
✅ This is ok

---
*Synced from Jira: 2026-08-24*
