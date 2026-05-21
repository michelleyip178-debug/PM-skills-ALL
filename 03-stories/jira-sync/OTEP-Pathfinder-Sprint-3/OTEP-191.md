# OTEP-191: Handle credential manager and vault

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

As a  developer on the OTEP team,  I want  database credentials managed through a centralised vault,  So that  access to production data is controlled, rotated automatically, and auditable — not hardcoded in config files. Acceptance Criteria Database credentials are stored in a centralised credential manager (e.g. AWS Secrets Manager) — not in  .env  files or hardcoded config. The application retrieves credentials at runtime from the vault, not from a static file. Credentials can be rotated without a code deployment. Access to the vault is role-scoped — developers get read access to dev credentials only, not production. A failed vault lookup returns a clear error and prevents the application from starting with stale or missing credentials.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-05-14)
Deprioritising this ticket to Sprint 3 or later. The story and acceptance criteria need to be sharpened before it can be picked up. Note: I recall this was originally intended for developer's database access purposes. This may have already been resolved with the recent AWS infrastructure setup and access provisioning, so we need to verify if this ticket is still necessary during grooming.
