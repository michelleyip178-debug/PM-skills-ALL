# OTEP-71: Login Authentication using WOG AD

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

User Story As a  public officer from an onboarded agency,  I want to  log in to OTEP via WOG AD with a single click,  So that  I can access the platform using my existing government credentials without creating a separate account. Flow:  Officer clicks "Log in with WOG AD" → OTEP authenticates against AD in the background (no login form) → OTEP loads on success. Acceptance Criteria When I click "Log in with WOG AD" on the login page, I land on the OTEP home page — no manual credential entry needed. If my agency is not yet on OTEP, I see a message explaining my agency isn't onboarded — not a generic error. If my WOG AD credentials are invalid (not a public officer), login fails and I see a clear error message. After a successful login, I go straight to OTEP — there's no additional account creation or registration step. Edge cases: Handled by WOG AD Officer's WOG AD account is disabled/locked — should show specific message (not generic failure) (handled by WOG AD) Network/AD service is down — graceful error message needed (handled by WOG AD) Handled at OTEP level AD returns only email + SOE-ID — any profile data (name, job title, unit) must come from POCDEX  Multiple concurrent sessions on different devices — allowed or not? Officer's agency was onboarded but is later removed — what happens on next login?

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---

*Synced from Jira: 2026-07-07 — moved into OTEP-Pathfinder Sprint 6 (34620), live Jira confirms sprint assignment.*

*Prior note (2026-06-04): no sprint assigned in live Jira (plain backlog). Flipped 3× that day: was S4 → synced out → Michelle re-added → now out again.*
