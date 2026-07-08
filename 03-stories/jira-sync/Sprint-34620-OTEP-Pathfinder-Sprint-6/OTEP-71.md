# OTEP-71: Login Authentication using WOG AD

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

User Story As a public officer from an onboarded agency, I want to log in to OTEP via WOG AD with a single click, So that I can access the platform using my existing government credentials without creating a separate account.

Flow: Officer clicks "Log in with WOG AD" → OTEP authenticates against AD in the background (no login form) → OTEP loads on success.

Acceptance Criteria:
- When I click "Log in with WOG AD" on the login page, I land on the OTEP home page — no manual credential entry needed.
- If my agency is not yet on OTEP, I see a message explaining my agency isn't onboarded — not a generic error.
- After a successful login, I go straight to OTEP — there's no additional account creation or registration step.
- If I'm already logged in on one device and log in via WOG AD on a second device, only one session stays active — the new login invalidates the prior device's session.
- If my agency was previously onboarded but is later removed, I see the same "agency not onboarded" message as a never-onboarded agency.

Out of scope: invalid-credential handling is entirely WOG AD's responsibility — OTEP does not render any UI for this case.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---

*Synced from Jira: 2026-07-08 — AC updated directly in Jira by Michelle (concurrent-session and agency-de-onboarding open questions resolved; invalid-credential handling clarified as out of OTEP's scope, resolving prior overlap with OTEP-110).*

*Prior note (2026-07-07): moved into OTEP-Pathfinder Sprint 6 (34620), live Jira confirms sprint assignment. Prior note (2026-06-04): no sprint assigned in live Jira (plain backlog). Flipped 3× that day: was S4 → synced out → Michelle re-added → now out again.*
