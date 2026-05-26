# OTEP-147: Gitlab 05 - Deployment & Environment Segregation for Service.

**Type:** Sub-task
**Status:** In Progress
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

* *Goal:* Automate the secure delivery of container images and infrastructure to physically segregated AWS environments.
* *IM8 Reform Clause:* SD-4 (Continuous Deployment), SC-7 (Boundary Protection / Environment Segregation).
* *Specific Acceptance Criteria:*
** The Staging and Production deployment jobs authenticate to completely separate AWS Account IDs.
** Dynamic state isolation ensures Staging and Production state files remain strictly separate.
** The pipeline automates the infrastructure deployment and container updates successfully with zero manual intervention required.
* *Tasks:*
** *Task 1 (Level 1) [sc-5]:* Create CD stages for infrastructure and ECS updates.
** *Task 2 (Level 1) [sd-8]:* Parameterize pipelines for segregated AWS accounts via OIDC.
** *Task 3 (Level 1):* Configure dynamic Terraform state isolation.
** *Task 4 (Level 1) [sc-6]:* Ensure CD deploys only exact pinned versions.
** *Task 5 (Level 2) [sc-7] [Optional]:* Implement container image signing.
** *Task 6 (Level 2) [sc-8] [Optional]:* Verify image signature before deployment.
** *Task 7 (Level 2) [Optional]:* Implement Post-Deployment Automated Smoke Tests.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang:** [~accountid:712020:4c101a3f-bd57-44f2-90a8-f36ea3d3ddb4]

