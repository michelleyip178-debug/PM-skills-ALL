# OTEP-154: Gitlab 09: Configure ECS Authentication for GitLab Container Registry

**Type:** Sub-task
**Status:** QA
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

* *Goal:* Authorize Fargate tasks in private subnets to securely pull container images from the native GitLab Registry.
* *IM8 Reform Clause:* AC-3 (Access Enforcement), IA-5 (Authenticator Management).
* *Specific Acceptance Criteria:*
** A GitLab Deploy Token exists with only the read_registry scope enabled.
** The Deploy Token credentials are confirmed to be stored in AWS Secrets Manager as a JSON payload.
** The ECS Task Definition JSON explicitly references the Secrets Manager ARN in the repositoryCredentialsblock.
** ECS CloudWatch events show tasks successfully transitioning from PENDING to RUNNING without "CannotPullContainerError" failures.
* *Tasks:*
** *Task 1 (Level 1):* Generate a GitLab Deploy Token.
** *Task 2 (Level 0):* Store the token securely in AWS Secrets Manager.(tOKEN STORED IN GITLAB CICD secret variables)
** *Task 3 (Level 0):* Configure ECS Task Execution IAM Role and Task Definitions.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** Duplicate card.

