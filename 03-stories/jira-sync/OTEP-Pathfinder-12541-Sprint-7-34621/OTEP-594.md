# OTEP-594: Officer is routed to the correct page after WOG AD authentication

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Sprint:** OTEP-Pathfinder Sprint 7 (2026-07-26 → 2026-08-09)

---

## Description

User Story:  As a public officer attempting to log in to Career Compass, I want to be directed to the right page immediately after authentication, so that I either land on my profile or understand that I don't have access. Acceptance Criteria: If I log in successfully, my agency is in the pilot, and I have an active POCDEX profile, I land on my Profile Page — no extra steps. If I log in successfully but my agency isn't in the pilot, I'm taken straight to the unauthorised page (OTEP-111) — not a broken page or a dead end. If I log in successfully, my agency is in the pilot, but I don't have a POCDEX profile yet, I'm taken to a dedicated system-error page — not OTEP-111's unauthorised page. Copy: "Sorry, the system is still setting up your details. Please try logging in again shortly, or use the button below if this keeps happening." The screen includes a "Report issue" CTA, officer-initiated. There is no automatic logging. If I log in successfully but my POCDEX profile is deactivated, I'm taken to the unauthorised page (OTEP-111). If my WOG AD login itself fails, I never reach OTEP's routing logic — WOG AD shows its own error, and OTEP doesn't try to intercept it. If I try to reach any OTEP page directly by typing a URL without being logged in and authorised, I'm not let in — no session starts and I'm redirected appropriately. Dependencies:  Blocks OTEP-71. Depends on OTEP-350 (WOG AD onboarding). Depends on OTEP-111 (unauthorised page must exist before routing can reference it).

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-24*
