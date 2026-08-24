# OTEP-602: Course landing page and tile design

**Status:** QA
**Assignee:** Pei Ern Lim
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

User Story As an officer, I want a Learning & Courses landing page so that I can quickly access recommended courses or navigate to the full course search experience as well as see key information about a course in the tile to quickly determine whether it is relevant. Acceptance Criteria Landing page The landing page displays a search bar at the top of the page. Running a search within the search bar navigates the officer to the Search & Discovery page. Triggered by: clicking “Search” clicking enter after a keyword is input clicking any option in the auto complete dropdown When course recommendations are available, a  Recommended for you  swimlane is displayed. The recommendations for this swimlane will be by the Jumpstart POC 1 engine - ticket     The swimlane displays a maximum of 25 recommended courses. Left and right navigation controls allow the officer to browse the recommended courses where applicable. Clicking anywhere on a course tile opens the Course Detail page in a new browser tab. If no course recommendations are available, the officer is automatically redirected to the Search & Discovery page when they click “Learning and Courses” on the navigation bar. Clicking  Explore all courses  navigates the officer to the Search & Discovery page Course tile design Each course tile displays the following information sourced from LEARN: Course name - “Course_Type_Description” Product type - “ProductType” Course provider - “Provider” Course duration (if available) - “Duration_Hours” No pricing The following fields are displayed only when the corresponding data is available. If a value is unavailable, that field is omitted from the course tile in accordance with the approved design. Course duration Provider Change course tile design to make it more compact The course tile layout adapts correctly to the different combinations of optional fields as specified in the approved UI designs. All course information displayed on the course tile matches the corresponding data from the course catalogue SFTP file from LEARN

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-713 | UI for Course Landing | Done |

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-20*
