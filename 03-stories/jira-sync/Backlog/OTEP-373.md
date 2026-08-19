# OTEP-373: Tech Debt: Migrate keycloak to its own repo (otep-keycloak)

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Currently the Keycloak Docker image is built within the otep-service CI pipeline (from tools/init-keycloak/Dockerfile) and the deployment orchestrator uses a custom SRC_IMAGE override to pull from otep-service/keycloak subpath. This deviates from the team convention of one-repo-one-deployable-one-ECR. To align with convention, create a dedicated otep-keycloak repository with its own Dockerfile, .gitlab-ci.yml (build + push + ping orchestrator), and simplify the orchestrator to use the standard .push-to-ecr-base template without overrides. Acceptance criteria: 1) otep-keycloak repo exists with CI pipeline, 2) orchestrator uses standard TARGET_APP pattern for keycloak, 3) keycloak image no longer built in otep-service pipeline.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
