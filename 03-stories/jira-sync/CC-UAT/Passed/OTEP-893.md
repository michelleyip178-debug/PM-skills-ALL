# OTEP-893: [CORE] [B] CRS-01 — Course swimlane display (OTEP-491)

**Status:** Done
**Assignee:** N/A
**Type:** Task
**Labels:** CORE, OTEP-491, uat

---

## Description

h3. Account

*Account B — Richard Ramos ·* [*Richard_RAMOS_FROM.TP@cscollege.gov.sg*|mailto:Richard_RAMOS_FROM.TP@cscollege.gov.sg] *· Richard@Cc2026*

{panel:bgColor=#fffae6}
SEEDED (tag uat-seed-crs01-REVERTME): B's displayed roles have no eligible courses naturally, so 30 courses were tagged to this role's gap competency (10005485 Business Capability Devt) to produce the multi-page swimlane. Revert: DELETE FROM course_competency WHERE created_by='uat-seed-crs01-REVERTME'.
{panel}

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as B; open 'Your development' → 'Based on your current role'.
# Select the recommended role *"Assistant Director, Senior / Deputy Director (Industry Engagement & Sector Development)"* (80% match).
# Note the "Courses to develop your competencies" swimlane; click right, then left navigation.

h3. Expected Result

The swimlane shows courses (30 eligible, capped at 25), 3 cards at a time → multiple pages. Left nav disabled on the first page, right nav disabled on the last; each click moves by 3.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-21)
🎉 Looks good!

---

**Guo XZ** (2026-08-20)
There are 25 courses in the swimlane. But this role is a 100% match though the test steps says 80%. Can i check if the 80% is a typo?

---

**Alan Lim** (2026-08-20)
🎉 Looks good!

---
*Synced from Jira: 2026-08-24*
