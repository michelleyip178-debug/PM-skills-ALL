# OTEP-759: Provision Keycloak as a Standalone Service

**Status:** Backlog
**Assignee:** Léo Milbor
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

Context Keycloak is currently embedded inside  otep-service  using development-style configuration ( start-dev ). This is not production-ready — Keycloak is an authentication platform component that requires its own deployment lifecycle, database boundary, observability, and operational runbook. ADR-008 formally decides to extract and provision Keycloak as a first-class standalone service. Goal Extract Keycloak from  otep-service  and provision it as a dedicated ECS service with: Its own deployable artifact, image build, and release lifecycle A dedicated Aurora PostgreSQL database boundary across all environments (dev/qa/uat/prd) Onboarded to the existing shared CI/CD deployment workflow used by  otep-web  and  otep-service Embedded Infinispan clustering with  jdbc-ping  discovery (single region, single cluster) Production-mode runtime ( kc.sh start --optimized ) in all shared environments Full observability, alerting, and operational runbooks Child Tickets Create Dedicated Keycloak Repository / Module Onboard Keycloak to the Shared CI/CD Deployment Workflow Provision Keycloak Database, Secrets, and Network Prerequisites Provision Keycloak ECS Service and Runtime Configuration Implement Realm Bootstrap, Admin Setup, and Migration from Embedded Keycloak Add Keycloak Observability, Alerts, and Runbooks Acceptance Criteria [ ] Keycloak runs as a standalone ECS service, independent of  otep-service [ ]  otep-service  no longer starts, packages, or configures Keycloak [ ] Keycloak uses production mode ( kc.sh start  or  kc.sh start --optimized ) in all shared environments [ ] A dedicated Aurora PostgreSQL database boundary exists for Keycloak in all environments [ ] Keycloak is onboarded to the shared CI/CD deployment workflow [ ] At least one application in dev/qa/uat can authenticate through standalone Keycloak [ ] Singpass and WOG Entra ID brokering is validated in a non-prd environment [ ] Logs, metrics, and alerts are in place before prd go-live [ ] Operational runbook and break-glass admin recovery procedure are documented References ADR-008: Provision Keycloak as a Standalone Production Service Keycloak: Configuring Keycloak for production Keycloak: Running Keycloak in a container Notes Delivery order: Tickets 1 and 2 can proceed in parallel. Ticket 3 (infrastructure prerequisites) must complete before Ticket 4 (ECS service). Ticket 5 (migration) depends on Ticket 4. Ticket 6 (observability) can be done incrementally from Ticket 4 onwards but must be complete before prd go-live.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Adrian Lo** (2026-07-21)
needs to be completed, and decision made.   Then    can be updated and implemented Then    and finally     needs to be last to avoid breaking current keycloak

---

**boonsiangteh** (2026-07-20)
Fanxu Wang  mentioned this issue in  a merge request  of  WOG / PSD / pdo / OTEP / otep-keycloak  on branch  OTEP-760 :   Add standalone Keycloak deployable artifact

---
*Synced from Jira: 2026-07-27*
