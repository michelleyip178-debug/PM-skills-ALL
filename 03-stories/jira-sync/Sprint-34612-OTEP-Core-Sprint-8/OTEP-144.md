# OTEP-144: Gitlab 02: Infrastructure as Code (IaC) & Cloud Integration ( configure GitLab to AWS OIDC Integration)

**Status:** Done
**Assignee:** Soumya Routa
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Goal:  Set up OpenID Connect (OIDC) between GitLab and the GCC AWS account to eliminate static IAM keys. IM8 Reform Clause:  IA-1 (Identification and Authentication - Must-Have). Specific Acceptance Criteria: The AWS IAM Trust Policy for the deployment role explicitly contains a StringLike condition restricting assumption to the specific GitLab project path and branch (e.g., project_path:Agency/Project/*:ref_type:branch:ref:main). The GitLab CI/CD pipeline logs demonstrate a successful sts:AssumeRoleWithWebIdentity call and retrieve a temporary session token. An audit of the deployment IAM user/role in AWS confirms exactly zero static, long-lived access keys are generated or active. Tasks: Task 1 (Level 0):  Configure the AWS OIDC identity provider. Task 2 (Level 0):  Create IAM roles with strict trust policies. Task 3 (Level 1):  Validate authentication via test pipeline.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa** (2026-05-07)
Acceptance Criteria Validation https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-devops-test/-/pipelines/18960888   Criteria Result Evidence IAM Trust Policy StringLike Pass Restricted to  project_path:wog/psd/pdo/otep/*  and  ref:main . Pipeline STS Success Pass Logs confirm  sts:AssumeRoleWithWebIdentity  was successful. Zero Static Keys Pass OIDC token used; no static IAM User keys present in logs or configuration.

---

**Soumya Routa** (2026-04-28)
OTEP-144:  Configure GitLab to AWS OIDC Integration     OTEP-146:  Infrastructure as Code (IaC) Pipeline DevSecOps     others     OTEP-153:  Configure IaC Remote State, study whether use S3 or gitlab.     OTEP-154:  Configure ECS Authentication for GitLab Container Registry     OTEP-161:  Implement Infrastructure Drift Detection     OTEP-147 : create multiple env & environment segregation

---
*Synced from Jira: 2026-08-20*
