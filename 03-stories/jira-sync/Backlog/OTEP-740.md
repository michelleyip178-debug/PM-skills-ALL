# OTEP-740: Remediation: Enable AWS Shield Advanced Subscription (AWS-1265)

**Type:** Task
**Status:** UAT
**Assignee:** boonsiangteh
**Story Points:** N/A

---

## Description

Summary Enable AWS Shield Advanced subscription with auto-renewal on account 257212470025. The billing cost is covered by the parent GCC organisation, but enablement must be performed at the individual account level by the app team. Type Remediation Epic Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev) Labels cloud-va ,  cis-benchmark ,  compliance ,  remediation IM8 Clause NS-5  Context GCC covers the Shield Advanced monthly subscription fee at the organisation level, but each member account must independently enable and subscribe to Shield Advanced. The subscription is not automatically inherited — each account needs to opt in. The live audit confirmed  aws shield describe-subscription  returns  ResourceNotFoundException , confirming Shield Advanced is not currently active on this account. Problem Shield Advanced is not enabled on account 257212470025. Without it, internet-facing resources (the public ALB, Route 53 hosted zones) only have Shield Standard's basic volumetric DDoS protection. Shield Advanced provides: Layer 7 (application-layer) DDoS detection AWS Shield Response Team (SRT) 24/7 access DDoS cost protection (scaling credits during attacks) Enhanced CloudWatch metrics for DDoS events Integration with WAF for automatic mitigation Proposed Change Enable Shield Advanced via IaC: resource "aws_shield_subscription" "this" {
  auto_renew = "ENABLED"
} After subscription is active, protect internet-facing resources: resource "aws_shield_protection" "public_alb" {
  name         = "shield-psd-otep-dev-public-alb"
  resource_arn = aws_lb.public.arn
} Scope New Terraform resource(s) — either a dedicated  live/dev/compute/shield/  stack or added to the existing  public-alb  stack Applies to account 257212470025 (dev). Same enablement needed for qa/uat/prd accounts during propagation. Acceptance Criteria [ ]  aws shield describe-subscription  returns a valid subscription with  AutoRenew: ENABLED [ ] Shield Advanced subscription is managed in IaC (not console-only) [ ] Terraform plan/apply completes without error [ ] Dependent ticket (shield-protection-group.md) can proceed once subscription is active Validation # Confirm subscription is active
aws shield describe-subscription --query 'Subscription.AutoRenew'
# Expected: "ENABLED" Notes Shield Advanced subscription is a prerequisite for creating protection groups (AWS-1266). Complete this ticket before working on the protection group ticket. The billing is covered by the GCC parent org — no additional cost impact to the project. Shield Advanced subscription is account-wide and cannot be scoped to specific resources — only the subsequent  aws_shield_protection  resources target individual ARNs. Related:  shield-protection-group.md  (AWS-1266) — depends on this ticket.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
