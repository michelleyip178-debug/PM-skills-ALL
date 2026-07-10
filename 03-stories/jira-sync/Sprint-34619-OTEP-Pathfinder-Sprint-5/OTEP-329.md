# OTEP-329: chore: Keycloak Client Secret Externalization

**Status:** Backlog
**Assignee:** Pow Hwee TAN (PSD)
**Story Points:** 1

---

## Description

Currently, the Keycloak client secret (used for NextAuth OIDC flow) is hardcoded in the local development realm-export.json. Furthermore, KEYCLOAK_SECRET is not yet externalized in AWS Secrets Manager or configured for container injection in otep-web. Acceptance Criteria Create a secure entry in AWS Secrets Manager for KEYCLOAK_SECRET in each environment (Dev/Staging/Prod). Update otep-web/terragrunt.hcl to map this secret to the KEYCLOAK_SECRET environment variable. Ensure Keycloak bootstrap in staging/production dynamically reads the client secret rather than baking a static credential into configuration/export files.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-10*
