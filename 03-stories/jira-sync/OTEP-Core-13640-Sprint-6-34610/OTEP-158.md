# OTEP-158: Gitlab 13: Establish Artifact Immutability Strategy

**Type:** Sub-task
**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

* *Goal:* Ensure the exact Go binary and image tested in Staging is deployed to Production.
* *IM8 Reform Clause:* CM-5 (Access Restrictions for Change).
* *Specific Acceptance Criteria:*
** The different env deployment process does not perform any compilation or build steps.
** Both Staging and Production task definitions reference the exact same container image unique identifier, proving the application was only compiled once.
* *Tasks:*
** *Task 1 (Level 1):* Tag container builds with unique source control identifiers.
** *Task 2 (Level 1):* Configure CD stages to reference the exact same unique tag.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang:** [https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2251654208/Image+tagging+strategy|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2251654208/Image+tagging+strategy|smart-link] 

Strategy implemented as above, please review [~accountid:70121:9d369513-d725-4e3d-a2b8-675d4d862e3a] [~accountid:5d5b77777b9a8f0cf55f9d1d]

**Adrian Lo:** Pending document review

*Synced from Jira: 2026-07-23*
