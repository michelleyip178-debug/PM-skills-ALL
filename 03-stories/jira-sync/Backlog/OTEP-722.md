# OTEP-722: Decouple ECS Environment Variable Management from Terragrunt

**Type:** Story
**Status:** Backlog
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Background Currently, whenever an ECS environment variable needs to be added or updated, developers must inform the infrastructure team. An infrastructure engineer then needs to: Manually update the Terragrunt configuration. Review and apply the infrastructure changes. Redeploy the ECS service so that the new configuration is picked up by the running tasks. This process introduces several challenges. Long turnaround time : Developers must communicate the required changes to the infrastructure and wait for an infrastructure engineer to update Terragrunt and complete the deployment. Dependency on infrastructure engineers : Infrastructure engineers become a blocker for application-level configuration changes, even when no infrastructure resource is being changed. Risk of human error : Configuration details may be communicated incorrectly, added to the wrong environment, or incorrectly configured during the manual Terragrunt update. Delayed testing : Developers cannot continue testing until the infrastructure changes have been applied and the ECS service has been redeployed. Proposal Move application-level environment variable management out of Terragrunt and allow the CD pipeline to manage ECS runtime configuration. Use: AWS Systems Manager Parameter Store for non-sensitive configuration. AWS Secrets Manager for sensitive configuration. A  configuration schema  in each application repository to declare the environment variables required by the application. The CD orchestrator to validate the required configuration and inject the corresponding AWS resource references into the ECS Task Definition. The goal here is application-level configuration values will no longer require a Terragrunt change.  Configuration Schema Each application repository will introduce a configuration declaration file: # deploy/config-schema.yml

parameters:
  API_URL:
    required: true

secrets:
  DATABASE_PASSWORD:
    required: true

  OAUTH_CLIENT_SECRET:
    required: true
 The file must contain configuration names and metadata only. It must not contain actual environment-specific values or secret values. The schema acts as the configuration contract between the application and the CD pipeline. It defines: Which environment variables the application requires. Whether a variable comes from Parameter Store or Secrets Manager. Whether a variable is required or optional. Any applicable type or validation rules.  Flow 1: New or Changed Environment Variable Definition This flow applies when an application introduces a configuration contract change, including: Adding a new environment variable. Removing an existing environment variable. Renaming an environment variable. Changing a variable from Parameter Store to Secrets Manager, or vice versa. Changing an optional variable to required. The developer updates the application code and  config-schema.yml  in the same application Merge Request. Example: parameters:
  API_URL:
    required: true

  NEW_PROVIDER_URL:
    required: true

secrets:
  NEW_PROVIDER_CLIENT_SECRET:
    required: true
 After the Merge Request is merged, CD orchestrator will introduce the following steps before deploying each environment: review-<environment>-config
→ validate-<environment>-config
→ deploy-<environment>
→ verify-<environment>
 For example: review-xx-config
validate-xx-config review-<environment>-config This is a blocking manual gate used when the configuration schema has changed. The job displays the configuration additions or changes that must be prepared for the target environment. Example: New Parameter Store configuration:
- /dev/otep-service/env/NEW_PROVIDER_URL

New Secrets Manager configuration:
- /dev/otep-service/secret/NEW_PROVIDER_CLIENT_SECRET
 The developer or authorized operator prepares the required values before continuing. For non-sensitive values, an approved configuration update mechanism may write the value into Parameter Store. For sensitive values, the  authorized operator  must create or update the value directly in Secrets Manager. Secret values  must not  be entered into ordinary GitLab pipeline inputs or job logs. validate-<environment>-config This job automatically reads  config-schema.yml  and verifies that every required configuration item exists for the target environment. For example: Parameter:
NEW_PROVIDER_URL
→ /dev/otep-service/env/NEW_PROVIDER_URL

Secret:
NEW_PROVIDER_CLIENT_SECRET
→ /dev/otep-service/secret/NEW_PROVIDER_CLIENT_SECRET
 The job retrieves only the Parameter Store and Secrets Manager metadata required to generate the ECS Task Definition. It does not need to read secret values. If any required configuration is missing, the deployment must stop before the ECS service is updated. ECS deployment Once validation succeeds, the CD pipeline generates a new ECS Task Definition containing: The new application image. Parameter Store references. Secrets Manager references. Example: {
  "name": "NEW_PROVIDER_URL",
  "valueFrom": "arn:aws:ssm:ap-southeast-1:123456789012:parameter/dev/otep-service/env/NEW_PROVIDER_URL"
}
 {
  "name": "NEW_PROVIDER_CLIENT_SECRET",
  "valueFrom": "arn:aws:secretsmanager:ap-southeast-1:123456789012:secret:/dev/otep-service/secret/NEW_PROVIDER_CLIENT_SECRET-AbCdEf"
}
 The image and the required configuration references are deployed together in one ECS rolling deployment.  Flow 2: Updating the Value of an Existing Environment Variable This flow applies when the configuration key already exists in  config-schema.yml  and only its environment-specific value needs to be changed. Examples: LOG_LEVEL=info → debug
REQUEST_TIMEOUT=30 → 60
API_URL=https://old.example.com → https://new.example.com
 Because the application configuration contract has not changed: No application Merge Request is required. No new application image needs to be built. No new ECS Task Definition revision is required, provided that the existing Parameter Store or Secrets Manager reference remains unchanged. A separate config-only promotion pipeline will be introduced to promote the configuration change through: Dev
→ QA
→ UAT
→ Production
 Pipeline Inputs The config-only pipeline should accept: Application
Configuration key
Change reason or ticket reference
 The pipeline must not allow the developer to freely choose whether the configuration belongs to Parameter Store or Secrets Manager. The configuration source must be derived from the application's  config-schema.yml . For example: parameters:
  REQUEST_TIMEOUT:
    required: true

secrets:
  OAUTH_CLIENT_SECRET:
    required: true
 If  REQUEST_TIMEOUT  is selected, the pipeline determines that the value must be managed through Parameter Store. If  OAUTH_CLIENT_SECRET  is selected, the pipeline determines that the value must be managed through Secrets Manager.  Parameter Store Value Update This flow applies to non-sensitive configuration values. Examples include: LOG_LEVEL
REQUEST_TIMEOUT
API_URL
FEATURE_ENABLED
 For each environment, the pipeline will stop at a manual configuration review gate. The authorized developer provides the new non-sensitive value through the approved GitLab configuration update job. The pipeline then performs the following actions: Validate that the configuration key exists in  config-schema.yml . Validate that the key is declared under  parameters . Update the corresponding Parameter Store value. Confirm that the Parameter Store parameter exists and is accessible. Trigger an ECS forced deployment. Wait for the ECS service to become stable. Run smoke tests or deployment verification. Example Parameter Store path: /dev/otep-service/env/REQUEST_TIMEOUT
 Example flow: Review Dev configuration
→ Update Dev Parameter Store value
→ Validate Dev parameter
→ Redeploy Dev
→ Verify Dev
 The same process is repeated for QA, UAT, and Production. The pipeline should not automatically copy the Dev value into the other environments. Each environment may require a different value.  Secrets Manager Value Update This flow applies to sensitive configuration values. Examples include: DATABASE_PASSWORD
OAUTH_CLIENT_SECRET
API_TOKEN
PRIVATE_KEY
 The actual secret value must not be entered into GitLab pipeline inputs, job logs, artifacts, or ordinary CI/CD variables. For each environment, the pipeline will stop at a blocking manual secret review gate. The gate should display the expected Secrets Manager name, for example: /dev/otep-service/secret/OAUTH_CLIENT_SECRET
 An authorized operator updates the value directly in AWS Secrets Manager. After the secret has been updated, the authorized operator approves or executes the manual gate. The pipeline then performs the following actions: Validate that the configuration key exists in  config-schema.yml . Validate that the key is declared under  secrets . Validate that the corresponding Secrets Manager secret exists. Validate that the secret metadata can be accessed. Trigger an ECS forced deployment. Wait for the ECS service to become stable. Run smoke tests or deployment verification. The pipeline does not retrieve, display, or print the actual secret value. New ECS tasks will retrieve the latest secret version associated with  AWSCURRENT  during startup. Example flow: Review Dev secret configuration
→ Authorized operator updates Dev Secrets Manager value
→ Approve Dev secret gate
→ Validate Dev secret
→ Redeploy Dev
→ Verify Dev
 The same process is repeated for QA, UAT, and Production, with stricter permissions and approvals for higher environments.  Config-Only Promotion Pipeline Flow The config-only pipeline will follow this sequence: Validate configuration key and source

→ Review Dev configuration
→ Update or confirm Dev value
→ Validate Dev configuration
→ Redeploy Dev
→ Verify Dev

→ Review QA configuration
→ Update or confirm QA value
→ Validate QA configuration
→ Redeploy QA
→ Verify QA

→ Review UAT configuration
→ Update or confirm UAT value
→ Validate UAT configuration
→ Redeploy UAT
→ Verify UAT

→ Review Production configuration
→ Update or confirm Production value
→ Validate Production configuration
→ Production approval
→ Redeploy Production
→ Verify Production
 For Parameter Store values, the GitLab pipeline may update the value directly through an approved and controlled job. For Secrets Manager values, the authorized operator must update the value directly in AWS Secrets Manager before approving the corresponding manual gate.  ECS Redeployment Because the environment variable already exists in the current ECS Task Definition and its AWS resource reference remains unchanged, changing only the value does not require a new Task Definition revision. The ECS service can be restarted using a forced deployment: aws ecs update-service \
  --cluster "$ECS_CLUSTER" \
  --service "$ECS_SERVICE" \
  --force-new-deployment
 The forced deployment starts new ECS tasks using the existing Task Definition. During startup, the new tasks retrieve the latest values from: AWS Systems Manager Parameter Store
AWS Secrets Manager AWSCURRENT version
 The existing running tasks continue using the values that were loaded during their startup until they are replaced by the rolling deployment.  Exceptions A new ECS Task Definition revision is still required when the configuration contract or reference changes, including: Adding a new environment variable
Removing an environment variable
Renaming an environment variable
Changing a key from Parameter Store to Secrets Manager
Changing a key from Secrets Manager to Parameter Store
Changing the Parameter Store or Secrets Manager resource name or ARN
 These changes must follow the normal application release flow and include an update to  config-schema.yml .  Responsibilities Application repository Responsible for: Application source code. config-schema.yml . Declaring which configuration keys are required. Declaring whether each key is a parameter or a secret. AWS Parameter Store Responsible for: Non-sensitive environment-specific configuration values. Examples include URLs, timeouts, log levels, and feature settings. AWS Secrets Manager Responsible for: Sensitive environment-specific configuration values. Examples include passwords, API tokens, OAuth client secrets, and private keys. CD orchestrator Responsible for: Reading the application configuration schema. Validating configuration readiness. Resolving Parameter Store and Secrets Manager ARNs. Generating ECS Task Definitions. Redeploying ECS services. Managing environment promotion and approval gates.  Expected Outcome This change will: Remove infrastructure engineers as a blocker for application-level configuration changes. Reduce manual Terragrunt updates. Allow developers to prepare and validate configuration earlier. Prevent ECS deployments when required configuration is missing. Keep sensitive values outside Git and ordinary GitLab pipeline inputs. Improve configuration consistency across Dev, QA, UAT, and Production. Preserve environment promotion and approval controls. Reduce the risk of human error.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-724 | Move non-sensitive env variables from IaC into parameter Store | Backlog |
| OTEP-725 | Create a new CD pipeline for env variable value update | Backlog |
| OTEP-726 | Update existing CD pipeline to inject new env variables  | Backlog |

---

## Latest Comments

_No comments._
