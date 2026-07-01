# OTEP-227: provision required IAM roles through IaC

**Type:** Sub-task
**Status:** Backlog
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

naming convension:

iam-role-<agency code>-<project code>-<environment>-<customname>

iam-role-psd-otep-dev-ROLENAME

h2. roles by purpose:

IaC repo:

* iam-role-psd-otep-dev-TerraformDeployer
** VPC
** Subnets
** Route tables
** Secuirty groups
** WAF
** ECS
** ECR
** RDS
** CloudWatch
** Secrets Manager
** IAM
** ALB
** S3
** SQS
** NAT Gateway
** AWS firewall
** api gateway
** VPC Peering
** cloudfront(TBD)



Application repo:

* am-role-psd-otep-dev-AppDeployer
** Register new ECS task definition
** update ECS service
** Read required secret manager
* iam-role-psd-otep-dev-EcrPusher
** ECR push



h2. Trust Policy/ OIDC role mapping:

*pipeline jobs to different AWS roles:*

deploy dev job → DevAppDeployRole

deploy qa job → QaAppDeployRole

deploy uat job → UatAppDeployRole

deploy prod → ProdAppDeployRole

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** duplicate card

*Synced from Jira: 2026-07-01*
