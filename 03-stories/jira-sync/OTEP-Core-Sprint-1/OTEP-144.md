# OTEP-144: Gitlab 02: Infrastructure as Code (IaC) & Cloud Integration ( configure GitLab to AWS OIDC Integration)

**Type:** Sub-task
**Status:** QA
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

* *Goal:* Set up OpenID Connect (OIDC) between GitLab and the GCC AWS account to eliminate static IAM keys.
* *IM8 Reform Clause:* IA-1 (Identification and Authentication - Must-Have).
* *Specific Acceptance Criteria:*
** The AWS IAM Trust Policy for the deployment role explicitly contains a StringLike condition restricting assumption to the specific GitLab project path and branch (e.g., project_path:Agency/Project/*:ref_type:branch:ref:main).
** The GitLab CI/CD pipeline logs demonstrate a successful sts:AssumeRoleWithWebIdentity call and retrieve a temporary session token.
** An audit of the deployment IAM user/role in AWS confirms exactly zero static, long-lived access keys are generated or active.
* *Tasks:*
** *Task 1 (Level 0):* Configure the AWS OIDC identity provider.
** *Task 2 (Level 0):* Create IAM roles with strict trust policies.
** *Task 3 (Level 1):* Validate authentication via test pipeline.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** * *OTEP-144:* Configure GitLab to AWS OIDC Integration [~accountid:5d5b77777b9a8f0cf55f9d1d] 
* *OTEP-146:* Infrastructure as Code (IaC) Pipeline DevSecOps [~accountid:5d5b77777b9a8f0cf55f9d1d]  others [~accountid:712020:4c101a3f-bd57-44f2-90a8-f36ea3d3ddb4] 
* *OTEP-153:* Configure IaC Remote State, study whether use S3 or gitlab. [~accountid:712020:4c101a3f-bd57-44f2-90a8-f36ea3d3ddb4] 
* *OTEP-154:* Configure ECS Authentication for GitLab Container Registry [~accountid:5d5b77777b9a8f0cf55f9d1d] 
* *OTEP-161:* Implement Infrastructure Drift Detection [~accountid:712020:4c101a3f-bd57-44f2-90a8-f36ea3d3ddb4] 
* *OTEP-147*: create multiple env & environment segregation  [~accountid:712020:4c101a3f-bd57-44f2-90a8-f36ea3d3ddb4]

**Soumya Routa:** h3. *Acceptance Criteria Validation*

[https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-devops-test/-/pipelines/18960888|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-devops-test/-/pipelines/18960888]

!image-20260507-080516.png|width=445,alt="image-20260507-080516.png"!



||Criteria||Result||Evidence||
|*IAM Trust Policy StringLike*|*Pass*|Restricted to {{project_path:wog/psd/pdo/otep/*}} and {{ref:main}}.|
|*Pipeline STS Success*|*Pass*|Logs confirm {{sts:AssumeRoleWithWebIdentity}} was successful.|
|*Zero Static Keys*|*Pass*|OIDC token used; no static IAM User keys present in logs or configuration.|

