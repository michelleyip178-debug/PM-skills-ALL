# OTEP-667: [BUG] Open issues for opportunities details page

**Status:** To Do
**Assignee:** N/A
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

DefectId Defect Description Screenshot Severity Status 1 Issue:  When a user navigates back to the opportunities list from an opportunity detail page, the previously applied filter states are lost. Expected Result:  The system should return the user exactly to the list page, with the filter state and newest-first ordering remaining completely intact without reshuffling.  Detail page opens in new page according to new design   Medium NA with new design 2 Issue:  When clicking on a Careers@Gov opportunity link, it opens in the current window instead of a new tab. Expected Result:  The Careers@Gov opportunity link should open in a new tab so the user does not lose their place on the platform.  FIXED   Low CLOSED 3 Issue:  The system allows users to apply for the same opportunity multiple times because the call-to-action (CTA) button does not disable after an initial application. Expected Result:  If a user has previously submitted an application for an opportunity, the CTA button should reflect an "Applied" state and be disabled to prevent duplicate submissions.  Need to check if it is in scope for the MVP first High NA 4 Issue:  The FormSG form link provided for the application is invalid (displaying a "This form is not available" error), and the application sync webhook is reported as "Not built yet". Expected Result:  A valid FormSG link should be provided. Upon submission, the system should receive the webhook and successfully record the submission event against the officer and opportunity ID.  Data issue, need to test with valid data   NA CLOSED 5 Issue:   If a user navigates directly to its URL   of a closed opportunity, the state is not handled (it was working in dev)  Expected Result:  The UI prevents the access of this opportunity details and displays: "This opportunity is no longer available" with a back link  Still NOT the correct message   Medium OPEN (Pending images from design team)

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-17*
