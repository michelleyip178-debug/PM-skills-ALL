# OTEP-211: Create IaC for OTEP

**Type:** Sub-task
**Status:** Done
**Assignee:** boonsiangteh
**Story Points:** N/A

---

## Description

h1. AWS Components:

h2. dev:

Networking: [https://sgtechstack.atlassian.net/browse/OTEP-219|https://sgtechstack.atlassian.net/browse/OTEP-219|smart-link] 
ECS:[https://sgtechstack.atlassian.net/browse/OTEP-213|https://sgtechstack.atlassian.net/browse/OTEP-213|smart-link] 

ALB: [https://sgtechstack.atlassian.net/browse/OTEP-266|https://sgtechstack.atlassian.net/browse/OTEP-266|smart-link] 

RDS: [https://sgtechstack.atlassian.net/browse/OTEP-214|https://sgtechstack.atlassian.net/browse/OTEP-214|smart-link] 

IAM roles for IaC:[https://sgtechstack.atlassian.net/browse/OTEP-227?search_id=b6c44521-a0f2-4c7f-967d-69ec91a44d3e&referrer=quick-find|https://sgtechstack.atlassian.net/browse/OTEP-227?search_id=b6c44521-a0f2-4c7f-967d-69ec91a44d3e&referrer=quick-find|smart-link] 



h2. QA:

ticket not create yet. 


IaC CI/ID pipeline:
IaC CI:[https://sgtechstack.atlassian.net/browse/OTEP-235|https://sgtechstack.atlassian.net/browse/OTEP-235|smart-link] 

IaC CD:








*Phase 1 — Finish RDS , test connection from ALB ->ECS*

# terragrunt apply in rds ← you're here
# Wire master_user_secret_arn from RDS output into otep-service-shared so the ECS task role can read DB credentials
# Bring up simple lambda to trigger ALB, to test connection from ALB->ECS->vpce success

*Phase 2 — Decouple image from IaC*

# Add lifecycle { ignore_changes = [container_definitions] } to the ECS service module's task definition resource — so terragrunt apply stops reverting images deployed by the CD pipeline
# Replace the hardcoded SHA256 in otep-service/terragrunt.hcl with a stable seed image (:latest tag) — only used on first provision, CD takes over after that

*Phase 3 — CD pipeline in app repo*

# Add GitHub Actions workflow: build → push to ECR → register new task definition → update ECS service
# Verify the OIDC role has ecr:PutImage, ecs:RegisterTaskDefinition, ecs:UpdateService, iam:PassRole permissions

*Phase 4 — otep-web* 

* 1. App repo produces an otep-web image → trigger CD → remove placeholder from otep-web/terragrunt.hcl → apply

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Adrian Lo:** Tag all related infra cards / Jira tickets to this one

**Adrian Lo:** [~accountid:712020:4c101a3f-bd57-44f2-90a8-f36ea3d3ddb4] Please fill in the description of the ticket

*Synced from Jira: 2026-07-23*
