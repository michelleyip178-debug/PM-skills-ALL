# OTEP-393: chore: integrate custom OTEP login theme into Keycloak service

**Type:** Task

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Sprint:** OTEP-Pathfinder Sprint 4

---

## Description

**Assumption context:** These tasks assume OTEP will continue using Keycloak in production.

**Problem:** When officers click "Login with WOG AD" on the Next.js landing page (/auth/login), they are redirected to Keycloak which currently uses its default, unstyled login screen. This creates a jarring visual break — officers leave the OTEP-branded experience and land on an unstyled Keycloak page.

**Goal:** Integrate a custom OTEP login theme into the Keycloak service so the login screen is visually consistent with the OTEP product.

---

## Acceptance Criteria

1. When an officer is redirected from OTEP to Keycloak to enter credentials, the Keycloak login page displays the custom OTEP theme — not the default Keycloak UI.
2. The custom theme matches the OTEP visual style: logo, colour palette, typography, and button treatment per Amber's design spec. Design asset must be linked to this ticket before development starts.
3. The login form fields (username, password) and submit button are fully functional — the theme is purely visual and does not alter Keycloak's authentication behaviour.
4. The custom theme is deployed as part of the Keycloak service configuration, not hardcoded in otep-web.
5. If the custom theme fails to load (e.g. asset missing), Keycloak falls back to its default theme — login remains functional.
6. The themed login page is verified in staging before merging.

**Out of scope:**

- Custom themes for Keycloak's error or registration pages — login page only for MVP
- Any changes to the authentication flow itself

**Dependency:** Design asset (OTEP login theme) must be provided by Amber before development can start. Confirm asset status before grooming.

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-06-10*
