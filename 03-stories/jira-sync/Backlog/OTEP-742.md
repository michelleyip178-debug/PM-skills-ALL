# OTEP-742: Remediation: Move WAF Rules from Count to Block Mode and Add Managed Rule Groups (AWS-1273)

**Type:** Task
**Status:** QA
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Type : Remediation  Epic : Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev)  Labels : cloud-va, cis-benchmark, compliance, remediation  Cloudscape Rule : AWS-1273 — WAF Web ACL should have protection rules implemented (not all in Count mode)  IM8 Clause : NS-5  Resources : waf-acl-psd-otep-dev-public-alb, waf-acl-psd-otep-dev-alb  Context Two WAF Web ACLs are flagged by Cloudscape under AWS-1273. The public ALB WAF ( waf-acl-psd-otep-dev-public-alb ) has SQLi and KnownBadInputs rules in Block mode but is missing additional AWS Managed Rule groups such as IP reputation lists. The internal ALB WAF ( waf-acl-psd-otep-dev-alb ) has 22 CRS sub-rules overridden to Count mode, covering XSS, LFI, RFI, and SSRF rules — these were set to Count to avoid breaking intranet traffic patterns. Both WAFs require remediation, but the approach differs by surface. Problem Public WAF : Likely near-compliant but missing  AWSManagedRulesAmazonIpReputationList  and  AWSManagedRulesAnonymousIpList  managed rule groups, which Cloudscape may be using as part of its compliance check. Internal WAF : 22 rules in Count mode provide no actual blocking protection. XSS, LFI, RFI, and SSRF attack patterns targeting the intranet surface are detected but not blocked. Proposed Change Public WAF  ( live/dev/compute/public-waf/terragrunt.hcl ):  Add the following AWS Managed Rule groups to the Web ACL in Block mode: AWSManagedRulesAmazonIpReputationList AWSManagedRulesAnonymousIpList These do not require traffic baselining and can be enabled directly in Block mode. Internal WAF  ( live/dev/compute/waf/terragrunt.hcl ):  Use a phased approach to move overrides from Count to Block: Phase 1 (this ticket): Move SSRF and RFI rule overrides to Block mode — these are least likely to produce false positives on internal traffic patterns. Phase 2 (follow-up ticket): Review CloudWatch WAF metrics for remaining XSS and LFI rules in Count mode; promote to Block once false-positive rate is acceptable. Both changes are in  module/compute/waf/main.tf  and their respective Terragrunt input files. Scope In scope :  live/dev/compute/public-waf/terragrunt.hcl ,  live/dev/compute/waf/terragrunt.hcl ,  module/compute/waf/main.tf . Out of scope : WAF logging configuration; Shield Advanced integration; WAF rule tuning beyond what is listed above. Acceptance Criteria [ ]  AWSManagedRulesAmazonIpReputationList  and  AWSManagedRulesAnonymousIpList  are added to  waf-acl-psd-otep-dev-public-alb  in Block mode. [ ] Cloudscape rule AWS-1273 passes for  waf-acl-psd-otep-dev-public-alb  after re-evaluation. [ ] SSRF and RFI rule overrides on  waf-acl-psd-otep-dev-alb  are changed from Count to Block mode. [ ] Terraform plan and apply complete successfully for both WAF ACLs with no unrelated changes. [ ] WAF CloudWatch metrics are monitored for at least 24 hours post-change to confirm no false positive blocking of legitimate traffic. [ ] A follow-up ticket is created to address remaining XSS and LFI Count-mode overrides on the internal WAF (Phase 2). Validation # Inspect public WAF managed rule groups and override actions
aws wafv2 get-web-acl \
  --name waf-acl-psd-otep-dev-public-alb \
  --scope REGIONAL \
  --id <public-alb-web-acl-id>

# Inspect internal WAF rule overrides — confirm SSRF/RFI rules are no longer Count
aws wafv2 get-web-acl \
  --name waf-acl-psd-otep-dev-alb \
  --scope REGIONAL \
  --id <internal-alb-web-acl-id>

# Check WAF metrics for blocked/allowed counts post-change
aws cloudwatch get-metric-statistics \
  --namespace AWS/WAFV2 \
  --metric-name BlockedRequests \
  --dimensions Name=WebACL,Value=waf-acl-psd-otep-dev-alb Name=Region,Value=ap-southeast-1 \
  --start-time <change-time> \
  --end-time <change-time+24h> \
  --period 3600 \
  --statistics Sum Notes Before changing any rule override from Count to Block on the internal WAF, review the sampled requests in the WAF console to confirm no legitimate intranet traffic patterns would be blocked. The 22 Count-mode overrides on the internal WAF are a known gap. A documented remediation plan (this phased approach) satisfies the Cloudscape finding for the current audit cycle while the full fix is tracked. Phase 2 follow-up ticket should cover XSS ( CrossSiteScripting_* ) and LFI ( LFI_* ) rule overrides on  waf-acl-psd-otep-dev-alb .

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
