# OTEP-761: Onboard Keycloak to the Shared CI/CD Deployment Workflow

**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 6 (35009)

---

## Description

Context Keycloak is being extracted as a standalone service (see OTEP-759). As a first-class service, it should be onboarded to the existing shared CI/CD deployment workflow already used by  otep-web  and  otep-service , rather than having a bespoke pipeline built from scratch. Scope Extend the existing shared workflow to support Keycloak: Add Keycloak as a deployable service target in the shared workflow Configure the Keycloak image build stage using the Keycloak Dockerfile Wire environment-specific configuration for dev, qa, uat, and prd Configure post-deployment smoke test for Keycloak Image build conventions to follow (same as other services): Pinned Keycloak base image version Immutable image tags (commit SHA) No secrets baked into the image Post-deployment smoke test must verify at minimum: Keycloak health endpoint (internal) OIDC discovery endpoint Token endpoint reachability Admin path is not publicly reachable Acceptance Criteria Keycloak is a recognised deployable target in the shared CI/CD workflow Pipeline can build and push the Keycloak image to ECR Pipeline can deploy the selected image tag to the Keycloak ECS service Pipeline supports environment-specific variables for dev, qa, uat, and prd Pipeline does not expose secrets in logs Pipeline produces immutable image tags Post-deployment smoke test passes the above minimum checks Notes May initially target dev only; promotion to qa, uat, and prd follows once infrastructure is ready. Depends on: Keycloak module creation (Ticket 1). Epic: OTEP-759.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang** (2026-07-24)
It seems the scope of this ticket required three repo changes:  otep-keycloak otep-deployment otep-iac

---
*Synced from Jira: 2026-08-07*
