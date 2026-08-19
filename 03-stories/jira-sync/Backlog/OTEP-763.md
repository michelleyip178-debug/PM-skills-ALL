# OTEP-763: Bootstrap Admin, Realm Config, and Migrate from Embedded Keycloak

**Type:** Task
**Status:** In Progress
**Assignee:** Léo Milbor
**Story Points:** N/A

---

## Description

Context OTEP-748 handles the production start mode and realm import strategy within the current embedded Keycloak setup. This ticket covers the remaining migration work: bootstrapping proper admin access, defining per-environment realm config, validating IdP brokering (Singpass, WOG Entra ID), and executing the cutover from embedded Keycloak in  otep-service  to the standalone service. Scope Inventory current config in  otep-service : Realm name, clients, client secrets, redirect URIs Identity providers, mappers, roles, groups Users, themes, custom providers if applicable Bootstrap admin setup: Start Keycloak with temporary bootstrap admin credentials from a secure secret Create permanent admin group/service account with least privilege Configure MFA/access restrictions for human admins Remove bootstrap admin credentials from normal runtime config Redeploy without bootstrap credentials Realm config promotion: Define per-environment realm config files (dev/qa/uat/prd) Transform environment-specific values during CI/CD Apply realm config through reviewed automation (not destructive import on a live cluster) Validation: Validate Singpass broker configuration in dev, qa, or uat Validate WOG Entra ID broker configuration in dev, qa, or uat Confirm at least one application can authenticate through standalone Keycloak Cutover: Document cutover and rollback steps Remove Keycloak startup/configuration from  otep-service  after successful migration Acceptance Criteria [ ] Existing embedded Keycloak configuration is inventoried [ ] Realm config represented in the standalone Keycloak module [ ] Bootstrap admin process documented and tested [ ] Permanent admin access created with least privilege [ ] Bootstrap admin credentials removed from normal runtime config [ ] Singpass brokering validated in dev, qa, or uat [ ] WOG Entra ID brokering validated in dev, qa, or uat [ ] At least one application authenticates through standalone Keycloak in dev/qa/uat [ ] Cutover and rollback steps documented [ ]  otep-service  no longer starts or packages Keycloak after cutover References Keycloak: Bootstrapping and recovering an admin account Keycloak: Importing and exporting realms Notes prd cutover should only proceed after validation in dev, qa, and uat. Depends on: standalone ECS service ticket. Epic: OTEP-759.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-1325 | Handle cutover and rollback steps with documentation | Backlog |
| OTEP-1326 | Handle admin access & credentials | Backlog |

---

## Latest Comments

**Léo Milbor** (2026-08-19)
[x] Existing embedded Keycloak configuration is inventoried [x] Realm config represented in the standalone Keycloak module [ ] Bootstrap admin process documented and tested [ ] Permanent admin access created with least privilege [ ] Bootstrap admin credentials removed from normal runtime config [ ] Singpass brokering validated in dev, qa, or uat  This is not part of MVP. [x] WOG Entra ID brokering validated in dev, qa, or uat [x] At least one application authenticates through standalone Keycloak in dev/qa/uat [ ] Cutover and rollback steps documented [x]  otep-service  no longer starts or packages Keycloak after cutover
