# OTEP-227: provision required IAM roles through IaC

**Type:** Sub-task
**Status:** Done
**Assignee:** Soumya Routa
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 6 (id 34610, active)

---

## Description

naming convension: iam-role-<agency code>-<project code>-<environment>-<customname> iam-role-psd-otep-dev-ROLENAME roles by purpose: IaC repo: iam-role-psd-otep-dev-TerraformDeployer VPC Subnets Route tables Secuirty groups WAF ECS ECR RDS CloudWatch Secrets Manager IAM ALB S3 SQS NAT Gateway AWS firewall api gateway VPC Peering cloudfront(TBD) Application repo: am-role-psd-otep-dev-AppDeployer Register new ECS task definition update ECS service Read required secret manager iam-role-psd-otep-dev-EcrPusher ECR push Trust Policy/ OIDC role mapping: pipeline jobs to different AWS roles: deploy dev job → DevAppDeployRole deploy qa job → QaAppDeployRole deploy uat job → UatAppDeployRole deploy prod → ProdAppDeployRole

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-23*
