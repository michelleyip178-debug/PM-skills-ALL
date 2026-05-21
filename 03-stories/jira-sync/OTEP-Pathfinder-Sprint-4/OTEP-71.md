# OTEP-71: Login Authentication using WOG AD

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

User Story As a  public officer from an onboarded agency,  I want to  log in to OTEP via WOG AD with a single click,  So that  I can access the platform using my existing government credentials without creating a separate account. Flow:  Officer clicks "Log in with WOG AD" → OTEP authenticates against AD in the background (no login form) → OTEP loads on success. Acceptance Criteria When I click "Log in with WOG AD" on the login page, I land on the OTEP home page — no manual credential entry needed. If my agency is not yet on OTEP, I see a message explaining my agency isn't onboarded — not a generic error. If my WOG AD credentials are invalid (not a public officer), login fails and I see a clear error message. After a successful login, I go straight to OTEP — there's no additional account creation or registration step. Edge cases: Handled by WOG AD Officer's WOG AD account is disabled/locked — should show specific message (not generic failure) (handled by WOG AD) Network/AD service is down — graceful error message needed (handled by WOG AD) Handled at OTEP level AD returns only email + SOE-ID — any profile data (name, job title, unit) must come from POCDEX  Multiple concurrent sessions on different devices — allowed or not? Officer's agency was onboarded but is later removed — what happens on next login?

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
