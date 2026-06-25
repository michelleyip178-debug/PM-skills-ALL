# OTEP-392: chore: implement Keycloak federated logout in otep-web

**Status:** In Progress
**Assignee:** N/A
**Story Points:** 2

---

## Description

Assumption context:  These tasks assume OTEP will continue using Keycloak in production. A change in identity brokers is unlikely — Keycloak shields both otep-web and otep-service from direct dependencies on WOG AD and Singpass. Problem:  The current client-side logout in otep-web only clears NextAuth session cookies locally but leaves the Keycloak SSO session active. The Keycloak session cookie (KEYCLOAK_IDENTITY) remains active, meaning a user who logs out can be silently re-authenticated on next visit without re-entering credentials. Goal:  Implement federated logout so that logging out of OTEP also terminates the Keycloak SSO session. Implementation notes: Both the NextAuth session cookie and the Keycloak SSO session (KEYCLOAK_IDENTITY cookie) must be terminated in the same logout flow. After logout, officers navigating back to OTEP or any Keycloak-protected route must see the login screen — no silent re-authentication. Call Keycloak's end-session endpoint as part of the NextAuth signOut flow. No additional manual step required from the officer. If the Keycloak end-session call fails (e.g. network error), the NextAuth session must still be cleared and officer redirected to login. Failure logged server-side only. Verify logout works consistently across Chrome, Edge, Safari. Out of scope: Logging out of WOG AD / Singpass sessions — OTEP only terminates the Keycloak session Multi-device logout (terminating sessions on other devices)

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
