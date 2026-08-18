# OTEP-305: Login and Logout (replace keycloak page with actual)

**Status:** QA
**Assignee:** Thomas Huchedé
**Story Points:** 2
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

As a  logged-in public officer,  I want to  log out of OTEP,  So that  my session is ended and no one else can access my account on this device. Acceptance Criteria Flow:  Officer clicks "Log in with WOG AD" → OTEP authenticates against keycloak  OTEP authenticates against AD in the background (no login form)  → OTEP loads on success. When I click "Log out", my session ends and I'm taken to the login page. After logging out, pressing the browser back button doesn't let me back into OTEP — I'm redirected to login. After logging out, typing any OTEP URL directly into the browser redirects me to the login page. Edit: the authentication against the  AD (“no login form”) will be addressed in

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-369 | Custom login page  | Done |
| OTEP-368 | Automatic redirection to login page when session expires | Done |

---

## Latest Comments

**Thomas Huchedé** (2026-07-28)
Yes     should take care of the AD part.  For this story, we’ll only look at the login page and the logout flow.

---

**Amber Tong** (2026-07-23)
The "Having trouble? Contact  careercompass@psd.gov.sg " text and email link have been removed from the login page. cc

---

**Rathika Ramalingam** (2026-07-15)
Hi   , I can’t see the login form replaced. Is this implementation (no login form) NOT for qa env ?

---
*Synced from Jira: 2026-08-18*
