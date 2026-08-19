# OTEP-605: Refactor internal ALB module to separate ingress and egress CIDRs

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

The module/compute/alb uses a single vpc_cidrs variable for both ingress rules (who can reach the ALB) and egress rules (where the ALB can forward traffic). This creates over-permissive egress rules when CIDRs are added solely for ingress purposes. Current issue: Adding Internet VPC proxy-private CIDRs (100.108.253.96/28, 100.108.253.112/28) to vpc_cidrs for the reverse proxy to reach the Internal ALB (ingress on 443) also creates dead egress rules to those CIDRs on container ports 3000/8888 where nothing listens. Proposed fix: Split vpc_cidrs into two variables: ingress_cidrs — CIDRs allowed to reach the ALB on listener ports (80/443) egress_cidrs — CIDRs the ALB forwards traffic to on target group ports This allows adding the proxy-private CIDRs to ingress only, without polluting egress. Acceptance criteria: ALB module accepts separate ingress and egress CIDR inputs Existing live stacks produce zero plan changes after migration Dead egress rules to proxy-private subnets are removed

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
