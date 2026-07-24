# OTEP-153: Gitlab 08: Configure IaC Remote State

**Type:** Sub-task
**Status:** Done
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

* *Goal:* Implement secure, remote state management using GitLab's native Managed Terraform State.
* *IM8 Reform Clause:* SC-4 (Information in Shared Resources), CM-2 (Baseline Configuration).
* *Specific Acceptance Criteria:*
** The Terraform state file is visible under the GitLab project's "Infrastructure -> Terraform" menu.
** Running terraform init successfully authenticates using the $CI_JOB_TOKEN over HTTP.
** Triggering two deployment pipelines simultaneously results in the second pipeline pausing or throwing a 423 Locked error, proving state locking is active.
* *Tasks:*
** *Task 1 (Level 0):* Enable GitLab Managed Terraform State.
** *Task 2 (Level 0):* Configure Terraform [backend.tf|http://backend.tf].
** *Task 3 (Level 1):* Execute a concurrent pipeline run to verify state locking.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** Confirmed the use of S3 as the remote state backend, as it is also used in the provided demo IaC repository: [otep-iac repository|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-iac?utm_source=chatgpt.com].

Using S3 for Terraform state also provides additional benefits over GitLab-managed state, including better scalability, centralized access control through AWS IAM, easier integration with compliance and audit requirements, state versioning and recovery support, and tighter alignment with existing AWS infrastructure and security tooling.



|*Aspect*|*AWS S3 Remote State*|*GitLab Managed State*|
|*Scalability*|Highly scalable; ideal for large environments and multiple teams.|Suitable for smaller to medium-scale usage.|
|*Access Control*|Fine-grained control using AWS IAM roles and policies.|Managed through standard GitLab permissions and access controls.|
|*Compliance & Audit*|Easier integration with AWS-native compliance, logging (CloudTrail), and audit tooling.|Limited to GitLab’s built-in auditing and governance features.|
|*State Versioning & Recovery*|Native S3 bucket versioning enables easy rollback and recovery.|Limited recovery and versioning flexibility.|
|*Security Integration*|Integrates well with existing AWS security tooling and encryption controls (e.g., AWS KMS).|Simpler setup but less integrated with AWS-native security controls.|
|*Operational Overhead*|Higher; requires setup and maintenance of S3 buckets, IAM roles, and locking mechanisms.|Lower; much easier to set up and manage directly within the GitLab UI.|
|*State Locking*|Requires additional infrastructure setup (typically an AWS DynamoDB table).|Built-in state locking support out of the box.|
|*Portability*|More cloud/platform agnostic; easier to integrate with external CI/CD tooling.|More tightly coupled to the GitLab ecosystem.|
|*Cost Management*|Costs can grow if storage/access/API calls are not managed properly.|Generally predictable; included within standard GitLab tier/storage limits.|

*Synced from Jira: 2026-07-23*
