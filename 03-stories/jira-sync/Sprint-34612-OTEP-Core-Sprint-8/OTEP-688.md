# OTEP-688: [BUG] Open issues for navigation bar

**Status:** QA
**Assignee:** Pei Ern Lim
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

DefectId Defect Description Screenshot Reference Severity Status 1 Issue:  The active page indicator in the navigation bar is NOT displaying in an orangish-red color    Expected Result:  The currently viewed page should be clearly visually distinguished in the navigation bar, and the active state should shift correctly as the user navigates between pages. FIXED  ISSUE  Low CLOSED 2 Issue:  When the user is in search mode, clicking the OTEP logo fails to redirect to the actual home page. Additionally, clicking the logo while already on the home page triggers a redirect that has no noticeable effect on the frontend.   Expected Result:  Clicking the OTEP logo should consistently return the user to the Home (profile) page, and the URL should append the  /home  parameter. FIXED - REOPENED There is jerk in the page when redirecting   ISSUE   Medium REOPEN 3 Issue:  The navigation bar is not responsive to viewport constraints correctly. It shrinks and collapses into the mobile hamburger menu way too early (at a 1200px width) instead of waiting for the standard tablet breakpoint of 768px.   Expected Result:  The navigation bar should scale gracefully upon window resizing without elements overlapping, and it should only collapse into a hamburger menu at smaller breakpoints (e.g., 768px). FIXED  ISSUE  Note: Pls confirm if it is an issue here Medium CLOSED 4 Issue:  When a user bypasses clicks and enters the direct URL path  /home , the system returns an error page. However, the "Home" link still incorrectly highlights in the navigation bar as if the page loaded successfully.   Expected Result:  Bypassing clicks via direct URL entry should correctly route the user to the Home page without errors, and the active state logic should correctly highlight the Home link based on successful navigation. FIXED     ISSUE  High CLOSED 5 Issue:  The profile/logout dropdown container is attached to the nav bar, which does not reflect the intended UI layout.   Expected Result:  The container must be detached from the nav bar to perfectly align with Figma specifications.  (Note: Ensure the container size remains responsive to handle long POCDEX email IDs).  Low CLOSED 6 Issue:  A vertical blue bar is erroneously displaying at the bottom left of the profile/logout dropdown menu.   Expected Result:  The UI must align to Figma specifications; the stray vertical blue bar should be removed from the dropdown container. FIXED   ISSUE   Low CLOSED 7 Issue:  The "Logout" text inside the profile dropdown menu lacks the correct styling.   Expected Result:  The "Logout" text must be highlighted in blue to perfectly align with the provided Figma specifications. FIXED   ISSUE    Low CLOSED

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pei Ern Lim** (2026-08-11)
Hi    , this has been fixed. Once deployment done please verify again.

---
*Synced from Jira: 2026-08-20*
