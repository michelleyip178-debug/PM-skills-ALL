# OTEP-84: Course detail page

**Status:** QA
**Assignee:** Pei Ern Lim
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

User Story As an officer, I want to view detailed information about a course so that I can determine whether it is suitable before proceeding to learn more or apply. Acceptance Criteria Course Details When an officer clicks a course tile, the course detail page opens in a new browser tab. The page displays the following course information, where available from LEARN: Course title - “Course_Type_Description” Course overview - “Extended_Course_text” Course outline - “Outline” Learning outcomes - “Learning_Outcomes” Product type - “ProductType” Duration - “Duration_Hours” Course start and end date - “Course_Type_start_date” ( 21/8 update exclude start and end date for all e-learning courses) Domain(s) - “DomainName” Competencies, where available - “PSD_CompetencyID” Course provider- “Provider” Programme code - “Course_Type_Abbreviation” Proficiency level information for competencies is not displayed. Any optional fields that are unavailable in LEARN are omitted without leaving empty labels or placeholders. Learn More CTA A  Learn more  CTA is displayed prominently on the page. Clicking  Learn more  opens the corresponding course page in LEARN in a new browser tab, using field “Web_Link” General Behaviour The page supports vertical scrolling when the course content exceeds the viewport height. If the course details cannot be retrieved, an appropriate error state is displayed with an option for the officer to navigate back. Edge case In the event where the sftp is refreshed but the officer still clicks on an “old” or expired course tile, they will be led to an error page where course details cannot be found  Header: This course is no longer available Subheader: Check out other courses you may be interested in

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-715 | UI for Course Details | Done |

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-09-07*
