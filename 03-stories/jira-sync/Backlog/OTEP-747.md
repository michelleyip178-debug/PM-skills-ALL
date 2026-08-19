# OTEP-747: Configure Keycloak service to use dedicated RDS (replace embedded H2)

**Type:** Task
**Status:** Backlog
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Background OTEP-745 provisions a dedicated PostgreSQL RDS instance for Keycloak. Configuring the Keycloak service to use it is outside the scope of RDS provisioning and is tracked here. Keycloak currently runs on an embedded H2 database, so all realm and session data is lost on task restart. Scope Set KC_DB=postgres and KC_DB_URL / KC_DB_USERNAME / KC_DB_PASSWORD on the Keycloak ECS task definition Inject database credentials from Secrets Manager into the container via the task definition secrets block, not plain environment variables Confirm realm import behaviour on first boot against the empty Postgres database; with persistent storage the import strategy must be deliberate rather than re-import on every restart Roll out per environment, dev first, then QA, UAT, prod Acceptance Criteria Keycloak service configured with KC_DB_* environment variables to connect to the dedicated RDS DB credentials sourced from Secrets Manager via the task definition secrets block Keycloak starts cleanly against Postgres and realm configuration persists across task restarts Approach replicated across all environments (QA, UAT, prod)

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Adrian Lo** (2026-07-21)
This ticket should be superseeded by the below:

---

**boonsiangteh** (2026-07-20)
Context for this ticket in relation to OTEP-759 (Keycloak standalone epic) This ticket is interim work — it wires  KC_DB_*  onto the existing embedded Keycloak task inside  otep-service  to stop data loss during the transition period while the standalone service is being built. The same database wiring will be re-implemented cleanly on the dedicated standalone ECS task definition as part of OTEP-762 (Provision Standalone Keycloak ECS Service). Once the standalone service is live and cutover is complete (OTEP-763), the embedded Keycloak configuration in  otep-service  will be removed. The configuration decisions proven here (which  KC_DB_*  values, Secrets Manager injection pattern) should be carried forward as the reference for OTEP-762.
