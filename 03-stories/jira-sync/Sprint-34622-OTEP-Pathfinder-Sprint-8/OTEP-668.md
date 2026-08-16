# OTEP-668: [BUG] Bugs open for Search opportunities feature

**Status:** QA
**Assignee:** Thomas Huchedé
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

DefectId Defect Description Screenshot Severity Status 1 Issue:  The "No Results" state UI does not match the Figma design when a search yields no matches (e.g., searching for non-existent text like "xyzqwerty"). Expected Result:  The standard "no results" state and illustration to be displayed exactly as specified in the Figma designs.  Low OPEN 2 Issue:  Clearing the search query (by deleting text) fails to restore the original opportunity listing. Expected Result:  The search box should empty and the listing should immediately restore all relevant roles, retaining any applied filters while removing only the keyword constraint.   Medium OPEN 3 Issue:  The search keyword state is not persisted when a user navigates back to the search listing from an opportunity detail page. Expected Result:  The listing page should load with the exact previous state, retaining the search keyword in the box, any active filters, and the user's previous scroll position.  Invalid with the recent design to open details page in new tab Medium NA 4 Issue:  The search input does not handle extremely long strings (500+ random characters) gracefully, leading to improper failure handling. Expected Result:  The system must not crash or display an unstyled error page. It should either gracefully restrict the character limit in the UI or return the standard "no results" state.   FIXED By IMPLEMENTING MAXIMUM CHAR LIMIT ON SEARCH BAR  https://qa.careercompass.gov.sg/opportunities?search=The+Government+Technology+Agency+(Govtech)+is+a+statutory+board+of+the+Government+of+Singapore%2C+under+the+Prime+Minister's+Office.+GovTech+plays+a+vital+role+in+materialising+Singapore’s+Smart+Nation+vision+through+the+five+capability+centers+established&sort_by=closing_date  The Government Technology Agency (Govtech) is a statutory board of the Government of Singapore, under the Prime Minister's Office. GovTech plays a vital role in materialising Singapore’s Smart Nation vision through the five capability centers established to strengthen Public Sector engineering expertise. Each center is tasked to develop and deliver innovative citizen-centric products and services across the whole-of-government, collaborating within the Ministries and Statutory Boards Low CLOSED 5 Issue:  The search logic returns incorrect or empty results when a user's search query combines text from both the agency name and the opportunity title. Expected Result:  The search algorithm should correctly parse multi-term queries and return relevant opportunities that match combinations of agency and title keywords.    High OPEN

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Thomas Huchedé** (2026-08-13)
We now have a custom illustration for the “no result” error state, figma has not been updated with the newer design yet. Clearing the search will still require the “search” button to be clicked to retrigger the search (ref:    ) NA NA has bee moved to it’s own bug ticket

---
*Synced from Jira: 2026-08-17*
