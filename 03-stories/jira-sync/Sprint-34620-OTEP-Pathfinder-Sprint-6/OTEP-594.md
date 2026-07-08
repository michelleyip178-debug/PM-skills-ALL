# OTEP-594: Officer is routed to the correct page after WOG AD authentication

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

User Story: As a public officer attempting to log in to Career Compass, I want to be directed to the right page immediately after authentication, so that I either land on my profile or understand that I don't have access.

Acceptance Criteria:
- If I log in successfully, my agency is in the pilot, and I have an active POCDEX profile, I land on my Profile Page — no extra steps.
- If I log in successfully but my agency isn't in the pilot, I'm taken straight to the unauthorised page (OTEP-111) — not a broken page or a dead end.
- If I log in successfully, my agency is in the pilot, but I don't have a POCDEX profile yet, I'm taken to a dedicated system-error page — not OTEP-111's unauthorised page.
  - Copy: "Sorry, the system is still setting up your details. Please try logging in again shortly, or use the button below if this keeps happening."
  - The screen includes a "Report issue" CTA, officer-initiated. There is no automatic logging.
- If I log in successfully but my POCDEX profile is deactivated, I'm taken to the unauthorised page (OTEP-111).
- If my WOG AD login itself fails, I never reach OTEP's routing logic — WOG AD shows its own error, and OTEP doesn't try to intercept it.
- If I try to reach any OTEP page directly by typing a URL without being logged in and authorised, I'm not let in — no session starts and I'm redirected appropriately.

Dependencies: Blocks OTEP-71. Depends on OTEP-350 (WOG AD onboarding). Depends on OTEP-111 (unauthorised page must exist before routing can reference it).

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---

*Synced from Jira: 2026-07-08 — AC rewritten directly in Jira by Michelle. Decisions #7 (OTEP-111/594 boundary), #8 (system-error copy, decoupled from the 2-day POCDEX sync assumption), and #9 (no auto-logging — "Report issue" CTA instead) all resolved and folded into clean AC. **The system-error screen itself is not built yet** — AC is finalized and ready to build, but this is a build-readiness gap, not a decision gap. Recommend a Jira comment or separate story to track build status so this isn't mistaken for sprint-ready. Full resolution trail: [scoping-gaps-tracker #15](../../scoping-gaps-tracker.md).*

*Prior note (2026-07-07): new to local cache, created from live Jira pull; description referenced open decisions #7/#8/#9 and an unconfirmed 2-day POCDEX sync assumption.*
