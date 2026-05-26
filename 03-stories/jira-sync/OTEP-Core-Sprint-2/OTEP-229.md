# OTEP-229: Implement Secure Image Promotion Pipeline to Environment-Specific AWS ECRs

**Type:** Sub-task
**Status:** QA
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

h3. *Description*

Establish a secure container image supply chain by separating artifact storage across environments (DEV, QA, UAT, PROD). The CI/CD pipeline will act as a security gate, promoting images from the native GitLab Container Registry to AWS Elastic Container Registry (ECR).

Images will only be pushed to AWS ECR if all SHIP-HATS security scans pass and the image is correctly tagged. To enforce strict release management, the ECR push action must be executed manually.

h3. *Compliance & Security Alignment*

* *IM8 AC-3 (Access Enforcement):* IAM roles strictly enforce push access to specific environment ECRs.
* *IM8 SI-3 (Malicious Code Protection):* Hard dependency on SAST, Secret Detection, Dependency Scanning, and Container Scanning before artifacts enter the AWS environment.
* *IM8 CM-5 (Access Restrictions for Change):* Enforced manual approval gate for image promotion.

h3. *Acceptance Criteria*

# *Environment Separation (ECR & GitLab):*

* Environment-specific ECR repositories exist and follow GCC naming conventions:
** {{ecr-psd-otep-dev-app}}
** {{ecr-psd-otep-qa-app}}
** {{ecr-psd-otep-uat-app}}
** {{ecr-psd-otep-prod-app}}
* GitLab registry logically separates images via paths/tags (e.g., {{/dev/app:v1.0.0}}).

# *IAM Permissions (OIDC Role):*

* The GitLab OIDC IAM Role is granted scoped permissions to push images to the respective ECR repositories ({{ecr:GetAuthorizationToken}}, {{ecr:BatchCheckLayerAvailability}}, {{ecr:PutImage}}, {{ecr:InitiateLayerUpload}}, {{ecr:UploadLayerPart}}, {{ecr:CompleteLayerUpload}}).

# *Strict Security Gates:*

* The image promotion job ({{push-to-ecr}}) implicitly requires the successful execution ("Status: Passed") of the following upstream scan jobs:
** {{gemnasium-dependency_scanning}}
** {{kics-iac-sast}}
** {{secret_detection}}
** {{semgrep-sast}}
** {{container_scanning}}
* If any scan fails, the promotion job must be blocked.

# *Tag Validation:*

* The pipeline validates that the image tag matches the target environment (e.g., Dev uses {{-dev}} suffixes, Prod uses strict Semantic Versioning {{vX.Y.Z}}).

# *Manual Execution:*

* The {{push-to-ecr}} job is configured with {{when: manual}} to ensure explicit human authorization before an image is pushed to AWS.

h3. *Execution Tasks*

* *Task 1 (Level 0): Provision AWS ECR Repositories.* Update Terraform/Bootstrap scripts to create the 4 environment-specific ECR repositories with image scanning on push enabled.
* *Task 2 (Level 0): Configure IAM OIDC Push Permissions.* Attach an inline IAM policy to the deployment role allowing ECR push actions.
* *Task 3 (Level 1): Build the GitLab CI Promotion Job.* Create the {{push-to-ecr}} job in {{.gitlab-ci.yml}}.
** _Implementation Note:_ Use the {{needs:}} array to mandate that all security jobs must pass. Set {{when: manual}}.
* *Task 4 (Level 1): Implement Tag Regex Validation.* Add a script step in the promotion job to verify the image tag aligns with the {{$ENVIRONMENT}} variable before executing {{docker push}}.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** |*Acceptance Criteria*|*Status*|*Implementation Detail / Evidence*|
|# *Environment Separation*
\\
(ECR & GitLab)|*Met*|*AWS ECR:* Handled via the idempotent {{create-tfstate-resources}} script using the {{$ENVIRONMENT}} variable (e.g., {{ecr-psd-otep-dev-app}}).
\\
*GitLab:* The {{build-app-dev}} job dynamically appends the environment to the registry path ({{REGISTRY_IMAGE: "${CI_REGISTRY_IMAGE}/${ENVIRONMENT}/app"}}), forcing GitLab to create isolated logical registries.|
|# *IAM Permissions*
\\
(OIDC Role)|*Met*|The {{bootstrap-oidc-role}} job attaches the {{AmazonEC2ContainerRegistryPowerUser}} policy, granting the exact required data-plane actions ({{ecr:GetAuthorizationToken}}, {{ecr:PutImage}}, {{ecr:UploadLayerPart}}, etc.), scoped to the assumed session.|
|# *Strict Security Gates*
\\
(Hard dependencies)|*Met*|Implemented using GitLab's {{needs:}} keyword in the {{push-to-dev-ecr}} job. It strictly lists {{gemnasium-dependency_scanning}}, {{kics-iac-sast}}, {{secret_detection}}, {{semgrep-sast}}, and {{container_scanning}}. If any fail, the push job is physically blocked from running.|
|# *Tag Validation*
\\
(Regex checking)|*Met*|Addressed via a bash evaluation script within the push job. It uses regex (e.g., {{=~ .*-dev$}}) to strictly compare the {{$IMAGE_TAG}} against the target {{$ENVIRONMENT}} before executing the {{crane copy}} command.|
|# *Manual Execution*
\\
(Human approval)|*Met*|Implemented in the {{push-to-dev-ecr}} job using the {{rules:}} block ({{when: manual}}). The job pauses pipeline execution and waits for a user to click "Play" in the GitLab UI before touching AWS.|



[https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-devops-test/-/pipelines/18963847|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-devops-test/-/pipelines/18963847]


!image-20260507-084901.png|width=912,alt="image-20260507-084901.png"!

**Soumya Routa:** Tested on Original otep=service repo.
[https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-service/-/pipelines/19115672|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-service/-/pipelines/19115672]

