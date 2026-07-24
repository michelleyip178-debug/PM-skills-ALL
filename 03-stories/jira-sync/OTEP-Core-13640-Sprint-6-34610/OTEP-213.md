# OTEP-213: Provision ECS through IaC

**Type:** Sub-task
**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 6 (id 34610, active)

---

## Description

Networking reference Subnet CIDR (1a / 1b) ECS relevance app_private 100.100.238.128/28  /  100.100.238.144/28 ECS tasks run here internal_alb 10.188.186.224/28  /  10.188.186.240/28 Internal ALB (routes to ECS) db 100.100.238.192/28  /  100.100.238.208/28 RDS — ECS connects here vpce 100.100.238.160/28  /  100.100.238.176/28 ECR/Secrets/SSM endpoints Deployment order Deployment Order

Due to IAM and SG dependencies, stacks must be applied in this order:

| Step | Stack path | Reason | Status (dev) |
|---|---|---|---|
| 1 | `live/{env}/networking` | VPC, subnets, endpoints must exist first | ✅ Applied |
| 2 | `live/{env}/compute/ecs/account-setup` | `AWSServiceRoleForECS` must exist — one-time per AWS account | ✅ Applied |
| 3 | `live/{env}/compute/ecs/cluster` | ECS cluster must exist before services register into it | ✅ Applied |
| 4 | `live/{env}/compute/alb` | ALB security group ID is referenced by service SG ingress rule | ⬜ Next |
| 5 | `live/{env}/compute/ecs/{svc}-shared` | IAM task exec role + log group must exist before task definition | ✅ Applied (`otep-service-shared`) |
| 6 | `live/{env}/compute/ecs/{svc}` | ECS service + task definition (depends on cluster, ALB, shared) | ⬜ Pending ECR image |

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-23*
