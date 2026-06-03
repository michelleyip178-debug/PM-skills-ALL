# OTEP-136: Infra Setup for OTEP

**Type:** Story
**Status:** In Progress
**Assignee:** Fabian PEH
**Story Points:** N/A

---

## Description

As part of the *OTEP* project, we need to provision AWS accounts on GCC (Government Commercial Cloud) for the *Development, QA* and *UAT* environments to support the project's infrastructure setup.

Approval from the Agency Project Manager / AO has already been obtained.

*Background:*

The OTEP project requires dedicated AWS accounts under GCC to ensure proper environment isolation, security compliance, and cost tracking across Development and UAT stages. Each environment will be provisioned separately under the correct Organisational Unit (OU) with the appropriate access controls and GCC Security Baseline applied.

*Scope:*

* Provision a new AWS account for the *Development* environment
* Provision a new AWS account for the *QA* environment
* Provision a new AWS account for the *UAT* environment
* Configure IAM Identity Center (SSO) via TechPass for engineer access across both environments
* Ensure GCC Security Baseline and compliance requirements are met

*Out of Scope:*

* Production environment provisioning (to be handled separately)
* VAPT for Dev and UAT environment (not required) - [~accountid:712020:f1b20f91-0679-4119-a517-0ec77a28c4f8]  please confirm

*Notes:*

* All engineers must have active *TechPass accounts* before access can be provisioned
* VAPT for UAT environment to be confirmed with AO before go-live

*Acceptance Criteria:*

* Both Dev and UAT AWS accounts are provisioned and accessible via GCC Portal
* Engineers can log in successfully via TechPass SSO for both environments
* GCC Security Baseline is applied to both accounts
* All resources are tagged with the correct environment and project labels
* Confluence documentation is updated with account details and access structure

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-151 | Create New AWS Account on GCC (Development Environment) | Done |
| OTEP-152 | Create New AWS Account on GCC (UAT Environment) | Done |
| OTEP-166 | Create New AWS Account on GCC (QA Environment) | Done |
| OTEP-167 | IAC for provisioning the services(Dev) | QA |
| OTEP-168 | IAC for provisioning the services(QA) | In Progress |
| OTEP-169 | IAC for provisioning the services(UAT) | Backlog |
| OTEP-188 | Whitelisting for Working Team | Backlog |
| OTEP-198 | Create New Dev AWS Account for CIE | Done |
| OTEP-199 | Create New QA AWS Account for CIE | Done |
| OTEP-200 | Create New UAT AWS Account for CIE | Done |
| OTEP-211 | Create IaC for OTEP | QA |
| OTEP-215 | Provision S3 for Tfstate  for IaC | QA |
| OTEP-218 | Gitlab OIDC pipeline preparation | QA |
| OTEP-225 | setup required IAM custom role roles for ecs, ecr,s3 | Backlog |
| OTEP-219 | Infra networking set up | Done |
| OTEP-234 | frontend CI set up | Done |
| OTEP-297 | Set up otep-web service | Done |
| OTEP-266 | ALB set up | Done |
| OTEP-213 | Provision ECS through IaC | Done |
| OTEP-214 | Provision RDS through IaC | Done |
| OTEP-227 | provision required IAM roles through IaC | Backlog |
| OTEP-263 | Attach RoleARN into IaC | Done |
| OTEP-269 | Add fmt-check into CI Pipeline (otep-service) | Done |
| OTEP-275 | Update CI Pipeline to push images onto ECR | Done |
| OTEP-277 | Create dev hostname | In Progress |
| OTEP-298 | Set up WAF (Dev + QA) | In Progress |
| OTEP-308 | Research Service Discovery | QA |

---

## Latest Comments

**rama moorthy:** [~accountid:712020:5a4717ac-69a7-49e9-a198-16817e2d37a5] ram will give access matrix

**Adrian Lo:** * OTEP to retain UAT environment.
* OTEP UAT should not connect to CIE PRE-PROD

cc [~accountid:712020:5a4717ac-69a7-49e9-a198-16817e2d37a5]

**Fabian PEH:** As confirmed, dev->qa-> UAT are all NON prod and will NOT hold any production data for OTEP
only Prd is for production.

For CIE, 
Dev->QA are none prod
Pre-prod-> are Prod environment.
As discussed with Victor, there maybe a need to have a 5th environment as well.

*Synced from Jira: 2026-06-03*
