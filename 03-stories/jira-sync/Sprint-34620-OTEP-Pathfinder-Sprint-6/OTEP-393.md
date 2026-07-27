# OTEP-393: chore: integrate custom OTEP login theme into Keycloak service

**Status:** Backlog
**Assignee:** N/A
**Story Points:** 2
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

Assumption context:  These tasks assume OTEP will continue using Keycloak in production. Problem:  When officers click "Login with WOG AD" on the Next.js landing page (/auth/login), they are redirected to Keycloak which currently uses its default, unstyled login screen. This creates a jarring visual break — officers leave the OTEP-branded experience and land on an unstyled Keycloak page. Goal:  Integrate a custom OTEP login theme into the Keycloak service so the login screen is visually consistent with the OTEP product. Implementation notes: Custom theme must match the OTEP visual style: logo, colour palette, typography, and button treatment per Amber's design spec. Design asset must be linked to this ticket before development starts. Login form fields (username, password) and submit button must remain fully functional — the theme is purely visual and must not alter Keycloak's authentication behaviour. Deploy the custom theme as part of the Keycloak service configuration, not hardcoded in otep-web. If the custom theme fails to load (e.g. asset missing), Keycloak must fall back to its default theme — login remains functional. Verify the themed login page in staging before merging. BLOCKER:  Design asset (OTEP login theme) must be provided by Amber before development can start. Confirm asset status before grooming. Out of scope: Custom themes for Keycloak's error or registration pages — login page only for MVP Any changes to the authentication flow itself

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Thomas Huchedé** (2026-06-25)
We don’t have AzureAD or anything to login so for now we need to keep the keycloak page.  I don’t think we should spend time designing and building a theme for keycloak when ultimately this page should not appear when using AzureAD to login

---
*Synced from Jira: 2026-07-27*
