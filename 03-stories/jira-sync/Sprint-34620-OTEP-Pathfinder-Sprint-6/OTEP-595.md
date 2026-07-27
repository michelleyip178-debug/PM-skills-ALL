# OTEP-595: Set Keycloak realm displayName to Career Compass in realm-export.json

**Status:** In Progress
**Assignee:** Pow Hwee TAN (PSD)
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

The Keycloak login page header currently shows the realm displayName set manually in the admin console. To make it reproducible across deploys, set displayName and displayNameHtml to "Career Compass" in tools/init-keycloak/realm-export.json in otep-service.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Rathika Ramalingam** (2026-07-15)
Test:  Still seeing the Keycloak logo Test Case Evidence/Screenshot Status Verify the json updates   PASS Verify in the header Keycloak is replaced by CareerCompass  FAIL

---

**Pow Hwee TAN (PSD)** (2026-07-01)
Merged MR 134 to resolve this:  https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-service/-/merge_requests/134

---
*Synced from Jira: 2026-07-27*
