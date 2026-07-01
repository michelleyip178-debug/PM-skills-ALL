# OTEP-159: Gitlab 14: Integrate External Application Secrets

**Type:** Sub-task
**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

* *Goal:* Inject application runtime secrets dynamically; absolutely no hardcoded credentials.
* *IM8 Reform Clause:* IA-5 (Authenticator Management).
* *Specific Acceptance Criteria:*
** The application source code and pipeline variables contain no plaintext sensitive credentials.
** The deployment configuration maps application secrets to external secrets manager identifiers.
** The application successfully connects to required services using runtime-injected environment variables.
* *Tasks:*
** *Task 1 (Level 0):* Store application secrets in AWS Secrets Manager.
** *Task 2 (Level 0):* Update ECS Task Definition to reference SM ARNs.
** *Task 3 (Level 0):* Grant ECS Task Execution Role read permissions.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang:** blocked by AWS access

*Synced from Jira: 2026-07-01*
