# OTEP-947: [CORE] DTL-04 - Optional unavailable fields omitted (OTEP-84)

**Status:** Done
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Account Account D — padmin2 ·  padmin2@cscollege.gov.sg  · password: Padmin@Cc2026 Data note: Duration cannot be missing in the current catalogue — duration_hours is NOT NULL (min 0.02h), so a course 'missing Duration' does not exist (same gap as LAND-06). This case therefore verifies omission of Competencies and Learning Outcomes. Test Steps Go to the  UAT site  and log in as D. Click "Learning & Courses" on the navigation bar, then "Explore all courses". Search the programme code  3847816  and open "Practical Design Patterns in Swift". Confirm the missing sections are absent (not shown as empty labels). Test Data Search term:  3847816 (the programme code) — returns this one course exactly. Course:  "Practical Design Patterns in Swift" (3847816) has no Competencies and no Learning Outcomes. Expected Result Unavailable fields (Competencies, Learning Outcomes) are omitted entirely — no empty labels or placeholders.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-18)
🎉 Looks good!

---

**Charles Ho** (2026-08-18)
Working as intended

---
*Synced from Jira: 2026-08-25*
