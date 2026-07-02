# OTEP-305: Login and Logout (replace keycloak page with actual)

**Status:** QA
**Assignee:** N/A
**Story Points:** 2

---

## Description

As a  logged-in public officer,  I want to  log out of OTEP,  So that  my session is ended and no one else can access my account on this device. Acceptance Criteria Flow:  Officer clicks "Log in with WOG AD" → OTEP authenticates against AD in the background (no login form) → OTEP loads on success. When I click "Log out", my session ends and I'm taken to the login page. After logging out, pressing the browser back button doesn't let me back into OTEP — I'm redirected to login. After logging out, typing any OTEP URL directly into the browser redirects me to the login page.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-369 | Custom login page  | Done |
| OTEP-368 | Automatic redirection to login page when session expires | Done |

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-05-28)
Title updated to cover both login and logout (replacing keycloak page with actual). Current AC covers the logout flow well but login is underspecified — what happens if WOG AD auth fails? What does the officer see? Also: this likely depends on OTEP-350 (Onboard WOG AD) being completed first. Suggest adding that as a dependency.

*Synced from Jira: 2026-07-02*
