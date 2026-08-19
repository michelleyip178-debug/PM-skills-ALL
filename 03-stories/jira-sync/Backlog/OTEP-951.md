# OTEP-951: [CORE] DTL-08 - Expired course tile error page (OTEP-84)

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Account Account D — padmin2 ·  padmin2@cscollege.gov.sg  · password: Padmin@Cc2026 Precondition: needs a Compass course that has been removed from LEARN. This can't be verified from the UAT DB alone — coordinate with the team to identify (or stage) such a course before running. Test Steps Go to the  UAT site  and log in as D. Click "Learning & Courses" on the navigation bar, then "Explore all courses". Open a course that appears on Compass but no longer exists on LEARN. Test Data Requires a course present on Compass whose LEARN record has been removed — a data/environment precondition (cannot be produced by a read-only check). Expected Result An error page is shown — header "This course is no longer available", subheader "Check out other courses you may be interested in", CTA button "Explore courses".

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
