# OTEP-748: Update Keycloak image for persistent Postgres: production start mode, realm import strategy, Infinispan/JDBC_PING

**Type:** Task
**Status:** In Progress
**Assignee:** Léo Milbor
**Story Points:** N/A

---

## Description

Background OTEP-745 provisions a dedicated PostgreSQL RDS for Keycloak and OTEP-747 wires KC_DB_* on the ECS task definition. The deployed Keycloak image (otep-service/tools/init-keycloak) currently hardcodes 'start-dev --import-realm'. Moving to persistent Postgres requires image and config changes: startup import skips realms that already exist, so edits to realm-export.json silently stop applying after first boot; and dev mode does not support Infinispan cache clustering, which the HA environments need per the decision on OTEP-745. Scope Switch the image entrypoint from start-dev to start (production mode); make required hostname/proxy configuration explicit Decide and implement the realm import strategy for persistent storage: first-boot bootstrap only, explicit import with override, or admin-console/IaC-managed realm changes Configure Infinispan cache synchronization via JGroups JDBC_PING for HA environments (UAT, prod), using the Keycloak database for discovery Local dev is unaffected: docker-compose uses the upstream image with start-dev, embedded H2, and a volume-mounted realm-export.json Acceptance Criteria Keycloak runs in production mode (start) in all deployed environments Realm import strategy decided and implemented; realm changes have a defined delivery path once storage is persistent realm-export.json remains the single source of truth for realm config; local dev flow (start-dev + H2 + import on boot) unchanged Infinispan cache synchronization via JDBC_PING configured for multi-instance environments (UAT, prod)

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Léo Milbor** (2026-08-19)
According to  keylcoak doc , distributed caching using the db for discovery is the default mode when not running with  start-dev  so no explicit configuration was done. regarding that.

---

**boonsiangteh** (2026-07-20)
Recommendation: complete OTEP-760 first to avoid duplicate work   If OTEP-760 (Create Dedicated Keycloak Repository / Module) can be prioritised ahead of this ticket, the work here — production start mode, realm import strategy, and Infinispan/JDBC_PING config — should be implemented directly in the new standalone Keycloak repo rather than on    the embedded image in otep-service.   Doing it in the standalone repo first means: No porting step later The standalone repo becomes the single source of truth from the start The embedded Keycloak in otep-service can be left as-is until cutover (OTEP-763)   If OTEP-760 is not yet available and this work needs to proceed to unblock other teams, implement it on the embedded image as originally scoped — but ensure the decisions and configuration are documented clearly so they can be carried forward to the standalone repo.
