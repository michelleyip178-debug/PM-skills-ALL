# OTEP-71: Login Authentication using WOG AD

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

User Story: As a public officer from an onboarded agency, I want to log in to OTEP via WOG AD with a single click, so that I can access the platform using my existing government credentials without creating a separate account. Flow: Officer clicks "Log in with WOG AD" -> OTEP authenticates against AD in the background (no login form) -> OTEP loads on success. Acceptance Criteria When I click "Log in with WOG AD" on the login page, I land on the OTEP home page -- no manual credential entry needed. If my agency is not yet on OTEP, I see a message explaining my agency isn't onboarded -- not a generic error. After a successful login, I go straight to OTEP -- there's no additional account creation or registration step. If I'm already logged in on one device and log in via WOG AD on a second device, only one session stays active -- the new login invalidates the prior device's session. If my agency was previously onboarded but is later removed, I see the same "agency not onboarded" message as a never-onboarded agency. Edge cases Handled by WOG AD: account disabled/locked (specific message, not generic failure); network/AD service down (graceful error message). Handled at OTEP level: AD returns only email + SOE-ID -- any profile data (name, job title, unit) must come from POCDEX. Out of scope Invalid-credential error display -- owned by OTEP-110.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-14*
