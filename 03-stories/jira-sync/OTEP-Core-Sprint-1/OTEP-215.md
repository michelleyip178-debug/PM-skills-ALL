# OTEP-215: Provision S3 for Tfstate  for IaC

**Type:** Sub-task
**Status:** QA
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

h3. *Description*

Provision the backend infrastructure required to host Terraform state files for the OTEP project. This task ensures that the state is stored securely, supports team collaboration via state locking, and adheres to strict *Government Cloud (GCC)*standards for naming and access control.

h3. *Technical Implementation Details*

* *Identity Federation:* Established OIDC trust between GitLab Dedicated ({{sgts.gitlab-dedicated.com}}) and AWS to eliminate the need for long-lived IAM access keys.
* *Infrastructure-as-Code (IaC) Ready:* Integrated the bootstrap process into the GitLab CI/CD pipeline using SHIP-HATS templates.
* *Security Controls:* * Implemented an *Explicit Deny* guardrail policy to prevent accidental deletion of the state bucket or version history.
** Enabled *AES256 Server-Side Encryption* and *Bucket Versioning* for disaster recovery.
** Enforced *Public Access Block* to ensure the bucket is not reachable via the internet.

h3. *Acceptance Criteria*

# *GCC Naming Alignment:* All resources must follow the {{<prefix>-<service>-<agency>-<project>-<env>-<custom>}} format.
#* *S3 Bucket:* {{sst-s3-psd-otep-dev-tfstate}}
#* *DynamoDB Table:* {{sst-db-psd-otep-dev-tfstate-lock}}
#* *IAM Role:* {{iam-role-psd-otep-dev-gitlab-oidc}}
# *State Locking:* A DynamoDB table with a {{LockID}} partition key must be provisioned to prevent state corruption during concurrent pipeline runs.
# *Standardized Tagging:* Mandatory GCC tags ({{Agency-Code}}, {{Project-Code}}, {{Environment}}, {{Zone}}, {{Tier}}) must be applied to all provisioned resources.
# *Least Privilege Access:* The OIDC Role must be scoped to the specific GitLab project path {{wog/psd/pdo/otep/*}} and restricted from destructive actions on the state backend.
# *Verified Connectivity:* Successful validation via {{aws sts get-caller-identity}} and {{aws s3 ls}} within the CI/CD environment.

h3. *Success Definition (Definition of Done)*

* [x] OIDC Role bootstrapped with full-stack managed policies (VPC, ECS, RDS, WAF, etc.).
* [x] S3 State Bucket created with Versioning and Encryption.
* [x] DynamoDB Table created for State Locking.
* [x] Inline guardrail policies attached to the IAM Role.
* [x] Pipeline successfully executes {{static-test}} stage with assumed credentials.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** Created the S3 Terraform state bucket using AssumeRole with the necessary compliance requirements configured.

[https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-devops-test/-/pipelines/18960888|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-devops-test/-/pipelines/18960888]

!image-20260507-075613.png|width=473,alt="image-20260507-075613.png"!

**Soumya Routa:** |*Acceptance Criteria*|*Status*|*Implementation Detail / Evidence*|
|# *GCC Naming Alignment*
\\
(S3, DynamoDB, IAM Role)|*Met*|Variables were used in the pipeline to construct names strictly adhering to the GCC standard: {{sst-s3-psd-otep-dev-tfstate}}, {{sst-db-psd-otep-dev-tfstate-lock}}, and {{iam-role-psd-otep-dev-gitlab-oidc}}.|
|# *Security Controls*
\\
(Encryption, Versioning, Access Block)|*Met*|*Encryption & Recovery:* Applied {{AES256}} Server-Side Encryption and enabled Bucket Versioning via {{aws s3api}}.
\\
*Network Isolation:* Set {{BlockPublicAcls}}, {{IgnorePublicAcls}}, {{BlockPublicPolicy}}, and {{RestrictPublicBuckets}} to {{true}} to guarantee no internet exposure.|
|# *State Locking*
\\
(DynamoDB with LockID)|*Met*|The {{create-tfstate-resources}} job successfully provisioned the DynamoDB table using {{--attribute-definitions AttributeName=LockID,AttributeType=S}} and {{--key-schema AttributeName=LockID,KeyType=HASH}}.|
|# *Standardized Tagging*
\\
(Mandatory GCC Tags)|*Met*|The {{--tags}} and {{--tagging}} parameters were injected into all {{aws iam create-role}}, {{s3api create-bucket}}, and {{dynamodb create-table}} commands, applying {{Agency-Code}}, {{Project-Code}}, {{Environment}}, {{Zone}}, and {{Tier}} keys.|
|# *Least Privilege Access*
\\
(OIDC Scope & Guardrails)|*Met*|*Scope:* Trust policy restricted via {{StringLike}} to {{project_path:wog/psd/pdo/otep/*:ref_type:branch:ref:main}}.
\\
*Guardrails:* Inline IAM policy attached explicitly denying {{s3:DeleteBucket}}, {{s3:DeleteObjectVersion}}, and {{dynamodb:DeleteTable}}.|
|# *Verified Connectivity*
\\
(Pipeline Validation)|*Met*|The {{test-infrastructure-access}} job passed successfully. Pipeline logs confirm the {{sts:AssumeRoleWithWebIdentity}} was achieved and the role successfully executed {{aws s3 ls}}against the state bucket.|

**Soumya Routa:** *State Management Update:* With the adoption of Terraform v1.15+, we have eliminated the use of DynamoDB for state locking. We now leverage the built-in S3 native state lock feature. This architectural simplification reduces AWS costs, shrinks our IAM attack surface, and streamlines the CI/CD pipeline.
[https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-devops-test/-/pipelines/18967594|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-devops-test/-/pipelines/18967594]

deleted the orphaned dynamodb and updated the job permissions and state lock mechanism. 

!image-20260507-094507.png|width=912,alt="image-20260507-094507.png"!

