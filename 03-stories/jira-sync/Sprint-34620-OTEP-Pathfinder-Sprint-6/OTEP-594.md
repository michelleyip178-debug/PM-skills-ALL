# OTEP-594: Officer is routed to the correct page after WOG AD authentication

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

User Story: As a public officer attempting to log in to Career Compass, I want to be directed to the right page immediately after authentication, so that I either land on my profile or understand that I don't have access.

Acceptance Criteria (per live Jira, 2026-07-02):
- If I log in successfully, my agency is in the pilot, and I have an active POCDEX profile, I land on my Profile Page — no extra steps.
- If I log in successfully but my agency isn't in the pilot, I'm taken straight to the unauthorised page (OTEP-111) — not a broken page or a dead end.
- If I log in successfully, my agency is in the pilot, but I don't have a POCDEX profile yet, I'm taken to a system-error page, not the generic unauthorised page. [NEEDS RE-SCOPE: decision #7/#8/#9 — see new scenario below]
- If I log in successfully but my POCDEX profile is deactivated, I'm taken to the unauthorised page (OTEP-111).
- If my WOG AD login itself fails, I never reach OTEP's routing logic — WOG AD shows its own error, and OTEP doesn't try to intercept it.
- If I try to reach any OTEP page directly by typing a URL without being logged in and authorised, I'm not let in — no session starts and I'm redirected appropriately. (Rama, Squad Sync — route-guard NFR, decision #11)

New scenario to add — pilot agency, no POCDEX profile yet (system error, not access-denied):
- If my agency is in the pilot but POCDEX hasn't synced my profile yet, I don't see the generic "you don't have access" message — I see a message that makes clear this is temporary, not a rejection.
- Proposed copy (Imelda, pending confirmation): "Sorry the system is still onboarding your details. We have logged your case and please try logging in again in 2 days." [ASSUMPTION: 2-day POCDEX sync lag — confirm with Rama/Pow Hwee]
- Screen is not ready for this state before committing to the copy/flow above.

Dependencies (per live Jira):
- Blocks OTEP-71 (WOG AD login)
- Depends on OTEP-350 (WOG AD onboarding)
- Depends on OTEP-111 (unauthorised page must exist before routing can reference it)

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---

*Synced from Jira: 2026-07-07 — new to local cache, created from live Jira pull. Note: description references open decisions #7/#8/#9 and an unconfirmed 2-day POCDEX sync assumption — flag both as sprint risks, don't treat as resolved.*
