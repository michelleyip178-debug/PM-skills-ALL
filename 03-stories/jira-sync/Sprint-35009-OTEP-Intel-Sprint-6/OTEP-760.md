# OTEP-760: Create Dedicated Keycloak Repository / Module

**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 6 (35009)

---

## Description

Context Keycloak is currently embedded inside  otep-service  — its Dockerfile, image, and startup are owned by that service. ADR-008 requires Keycloak to be a first-class standalone service with its own deployable artifact, independent of  otep-service . Scope Create the dedicated Keycloak module/repository structure with the following shape: keycloak/
  Dockerfile
  providers/       # optional custom providers
  themes/          # optional custom themes
  realm-config/
    dev/
    qa/
    uat/
    prd/
  scripts/
    bootstrap-admin.sh
    apply-realm-config.sh
    smoke-test.sh
  docs/
    runbook.md
    upgrade.md
    realm-management.md Dockerfile must use a pinned Keycloak version and run  kc.sh build  during image build Runtime must use  kc.sh start  or  kc.sh start --optimized  —  start-dev  is not used for any shared environment Secrets must not be baked into the image Acceptance Criteria [ ] Keycloak has its own deployable artifact separate from  otep-service [ ] Dockerfile uses a pinned Keycloak version and runs  kc.sh build  during image build [ ] Runtime command uses  kc.sh start  or  kc.sh start --optimized [ ]  start-dev  is not used for dev/qa/uat/prd deployment [ ] Secrets are not baked into the image [ ] Basic local build succeeds [ ] Basic container startup succeeds when required DB/hostname env vars are supplied References Keycloak: Running Keycloak in a container Keycloak: Configuring Keycloak for production Notes This ticket does not provision AWS infrastructure. It only creates the deployable Keycloak artifact. Depends on: none. Blocks: CI/CD onboarding (Ticket 2) and ECS service provisioning (Ticket 4). Epic: OTEP-759.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**boonsiangteh** (2026-07-21)
Fanxu Wang  mentioned this issue in  a commit  of  WOG / PSD / pdo / OTEP / otep-keycloak  on branch  main : Merge branch 'OTEP-760' into 'main'

---

**boonsiangteh** (2026-07-21)
Fanxu Wang  mentioned this issue in  a commit  of  WOG / PSD / pdo / OTEP / otep-keycloak :   Add standalone Keycloak deployable artifact

---

**boonsiangteh** (2026-07-20)
Fanxu Wang  mentioned this issue in  a merge request  of  WOG / PSD / pdo / OTEP / otep-keycloak  on branch  OTEP-760 :   Add standalone Keycloak deployable artifact

---
*Synced from Jira: 2026-07-28*
