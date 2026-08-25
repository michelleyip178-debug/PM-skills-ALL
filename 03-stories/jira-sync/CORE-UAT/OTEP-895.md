# OTEP-895: [CORE] [N] CRS-03 Course recommendation logic

**Status:** Done
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Account Account N — Mary Lee ·  mary_lee@caas.test.gov.sg  · mary_lee SEEDED (tag uat-seed-crs03-REVERTME): mary_lee's natural roles are all 0% match with 1-2 courses, so the 3→2→1 tiers were engineered — a role_competency + course_competency tags (Gen Z Bootcamp→3 gaps, Hidden Data Scientist→2, Risk Mgmt→1). Revert: DELETE FROM course_competency/role_competency WHERE created_by='uat-seed-crs03-REVERTME'. Test Steps Go to the  UAT site  and log in as N. Go to Your Development Select the role  "[UAT CRS-03] 3-2-1 gap-course ranking" Observe the order of the courses in the swimlane. Expected Result Courses are ranked by the number of the role's missing ("To develop") competencies each matches: "Gen Z Bootcamp" (matches 3) → "Hidden Data Scientist Spy School" (matches 2) → "Risk Management in Government" (matches 1). Clicking a card opens the Course Detail in a new tab; switching roles updates the recommendations.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-20)
🎉 Looks good!

---

**Christopher Woo** (2026-08-20)
🎉 Looks good!

---

**rama moorthy** (2026-08-20)
This was due to excluding the WOG Role Fix, please try now

---
*Synced from Jira: 2026-08-25*
