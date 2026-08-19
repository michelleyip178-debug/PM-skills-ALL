# OTEP-741: Remediation: Configure AWS Shield Advanced Protection Group (AWS-1266)

**Type:** Task
**Status:** UAT
**Assignee:** boonsiangteh
**Story Points:** N/A

---

## Description

Summary Create an AWS Shield Advanced protection group covering all internet-facing resources in account 257212470025. Depends on Shield Advanced subscription being enabled first (AWS-1265). Type Remediation Epic Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev) Labels cloud-va ,  cis-benchmark ,  compliance ,  remediation IM8 Clause NS-5  Context Once Shield Advanced is subscribed (AWS-1265), protection groups must be configured to define which resources are collectively monitored for DDoS events. Protection groups allow AWS to correlate traffic patterns across multiple protected resources and detect distributed attacks that might not trigger on any single resource individually. Cloudscape requires at least one protection group to be present. Problem No Shield Advanced protection group exists in the account. Even after subscription is enabled, resources are only individually protected — there is no grouped detection or coordinated mitigation configured. Proposed Change First, protect internet-facing resources individually: resource "aws_shield_protection" "public_alb" {
  name         = "shield-psd-otep-dev-public-alb"
  resource_arn = dependency.public_alb.outputs.alb_arn
} Then create a protection group covering all protected resources: resource "aws_shield_protection_group" "all" {
  protection_group_id = "shield-pg-psd-otep-dev-all"
  aggregation         = "MAX"
  pattern             = "ALL"
} Alternatively, use  pattern = "BY_RESOURCE_TYPE"  with  resource_type = "APPLICATION_LOAD_BALANCER"  if you want to scope detection to ALBs only. Scope New Terraform resources in a  live/dev/compute/shield/  stack (or co-located with the  public-alb  stack) Blocked by :  shield-advanced-subscription.md  (AWS-1265) must be completed first Acceptance Criteria [ ] At least one Shield Advanced protection is created for the public ALB [ ] At least one protection group exists (pattern =  ALL  or  BY_RESOURCE_TYPE ) [ ]  aws shield describe-protection-group --protection-group-id <id>  returns valid config [ ] Cloudscape rule AWS-1266 passes after re-evaluation [ ] Resources are managed in IaC Validation # List protections
aws shield list-protections --query 'Protections[].{Name:Name,ARN:ResourceArn}'

# Describe protection group
aws shield describe-protection-group --protection-group-id shield-pg-psd-otep-dev-all
# Expected: valid response with Pattern and Aggregation fields Notes This ticket is  blocked by  the Shield Advanced subscription ticket (AWS-1265). Do not attempt until subscription is confirmed active. pattern = "ALL"  automatically includes newly created protected resources — low maintenance approach. The protection group uses  aggregation = "MAX" , meaning the highest traffic metric across all members is used for detection. This is the recommended default for web applications. Propagation to qa/uat/prd: same IaC pattern, deploy after Shield subscription is enabled in each account.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
