# OTEP-213: Provision ECS through IaC

**Type:** Sub-task
**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

h1. Networking reference

||Subnet||CIDR (1a / 1b)||ECS relevance||
|{{app_private}}|{{100.100.238.128/28}} / {{100.100.238.144/28}}|*ECS tasks run here*|
|{{internal_alb}}|{{10.188.186.224/28}} / {{10.188.186.240/28}}|Internal ALB (routes to ECS)|
|{{db}}|{{100.100.238.192/28}} / {{100.100.238.208/28}}|RDS — ECS connects here|
|{{vpce}}|{{100.100.238.160/28}} / {{100.100.238.176/28}}|ECR/Secrets/SSM endpoints|

Deployment order

{noformat}Deployment Order

Due to IAM and SG dependencies, stacks must be applied in this order:

| Step | Stack path | Reason | Status (dev) |
|---|---|---|---|
| 1 | `live/{env}/networking` | VPC, subnets, endpoints must exist first | ✅ Applied |
| 2 | `live/{env}/compute/ecs/account-setup` | `AWSServiceRoleForECS` must exist — one-time per AWS account | ✅ Applied |
| 3 | `live/{env}/compute/ecs/cluster` | ECS cluster must exist before services register into it | ✅ Applied |
| 4 | `live/{env}/compute/alb` | ALB security group ID is referenced by service SG ingress rule | ⬜ Next |
| 5 | `live/{env}/compute/ecs/{svc}-shared` | IAM task exec role + log group must exist before task definition | ✅ Applied (`otep-service-shared`) |
| 6 | `live/{env}/compute/ecs/{svc}` | ECS service + task definition (depends on cluster, ALB, shared) | ⬜ Pending ECR image |{noformat}

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang:** having issue where ECS cant pull image from ECR, still checking

!image-20260513-022221.png|width=650,alt="image-20260513-022221.png"!

**Fanxu Wang:** issue resolved, the reason is because our networking configuration having issue.

There are two path involved for ECS get image from ECR:

1st: ECS → app_private NACL → vpce → ECR through ENI, it working. 
2nd: 

image are acutally stored in S3, next ECS need get image from S3, S3 is acess through the S3 gateway instead of ENI, so it doesn’t have private IP address, only public address. 

Our app private NACL only allow outbound IP to vpce pass, but because S3 IP is public, not within vpce range, nacl blocked request. 

Fix is to update the NACL control, for port 443 allow it pass. Then use the route table for control.

**Fanxu Wang:** ECS task is up and running 
[https://ap-southeast-1.console.aws.amazon.com/ecs/v2/clusters?region=ap-southeast-1|https://ap-southeast-1.console.aws.amazon.com/ecs/v2/clusters?region=ap-southeast-1]


!image-20260514-020231.png|width=650,alt="image-20260514-020231.png"!

*Synced from Jira: 2026-06-08*
