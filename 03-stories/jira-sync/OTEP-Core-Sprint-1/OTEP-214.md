# OTEP-214: Provision RDS through IaC

**Type:** Sub-task
**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

||Decision||Choice||
|Credentials|{{manage_master_user_password = true}} (RDS-managed Secrets Manager)|
|Instance class|{{db.t3.micro}} (TODO: adjust based on load)|
|Storage|{{gp3}}, 20GB, autoscale to 100GB|
|Multi-AZ|{{false}} for dev, variable for stg/prd|
|SG ingress|CIDR from {{app_private}} subnets|



How multi-az replica works behind the scences:

ECS
     ↓
Single RDS endpoint (DNS)
     ↓
     ├── Primary (1a) ←── all traffic normally
     └── Standby (1b) ←── takes over only if primary fails

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang:** Multi-AZ: start from UAT set to true, dev&uat set to false

