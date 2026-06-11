# OTEP-392: chore: implement Keycloak federated logout in otep-web

**Type:** Task

**Status:** Backlog

**Assignee:** N/A

**Story Points:** 2

**Sprint:** OTEP-Pathfinder Sprint 4

---

## Description

**Assumption context:** These tasks assume OTEP will continue using Keycloak in production. A change in identity brokers is unlikely — Keycloak shields both otep-web and otep-service from direct dependencies on WOG AD and Singpass.

**Problem:** The current client-side logout in otep-web only clears NextAuth session cookies locally but leaves the Keycloak SSO session active. The Keycloak session cookie (KEYCLOAK_IDENTITY) remains active, meaning a user who logs out can be silently re-authenticated on next visit without re-entering credentials.

**Goal:** Implement federated logout so that logging out of OTEP also terminates the Keycloak SSO session.

---

## Acceptance Criteria

1. When an officer clicks "Log out" in OTEP, both the NextAuth session cookie and the Keycloak SSO session (KEYCLOAK_IDENTITY cookie) are terminated in the same logout flow.
2. After logout, if the officer navigates back to OTEP or any Keycloak-protected route, they are shown the login screen — they are not silently re-authenticated.
3. The federated logout calls Keycloak's end-session endpoint as part of the NextAuth signOut flow. No additional manual step is required from the officer.
4. If the Keycloak end-session call fails (e.g. network error), the NextAuth session is still cleared and the officer is redirected to the login page. The failure is logged server-side but not surfaced to the officer.
5. The logout flow works consistently across all supported browsers (Chrome, Edge, Safari).

**Out of scope:**

- Logging out of WOG AD / Singpass sessions — OTEP only terminates the Keycloak session
- Multi-device logout (terminating sessions on other devices)

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-06-11*
