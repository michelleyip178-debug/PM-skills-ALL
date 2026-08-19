# OTEP-737: Remediation: Enable Server Access Logging on S3 Buckets (AWS-1063)

**Type:** Task
**Status:** In Progress
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Type : Remediation  Epic : Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev)  Labels : cloud-va, cis-benchmark, compliance, remediation  Cloudscape Rule : AWS-1063 — S3 buckets should have server access logging enabled  IM8 Clause : LM-7  Resources : sst-s3-psd-otep-dev-otep-cv, sst-s3-psd-otep-dev-tfstate-logs, sst-s3-psd-otep-dev-public-alb-logs, otep-terraform-state-257212470025  Context Four S3 buckets in the dev account do not have server access logging enabled. Two are app-team managed buckets ( otep-cv ,  public-alb-logs ), and two are Terraform state-related buckets. The S3 module ( module/compute/s3/main.tf ) does not configure  aws_s3_bucket_logging . This was flagged by Cloudscape under rule AWS-1063 and maps to IM8 LM-7 (logging of resource access). Problem Without server access logging, there is no record of who accessed objects in these buckets, which prevents audit trail reconstruction and violates LM-7 requirements. Proposed Change Add an optional  aws_s3_bucket_logging  resource to  module/compute/s3/main.tf  controlled by a new input variable: resource "aws_s3_bucket_logging" "this" {
  count         = var.enable_access_logging ? 1 : 0
  bucket        = aws_s3_bucket.this.id
  target_bucket = var.logging_target_bucket
  target_prefix = "${local.bucket_name}/"
} Enable access logging in  live/dev/compute/s3/terragrunt.hcl  for the app-team managed buckets, using the existing  sst-s3-psd-otep-dev-tfstate-logs  bucket as the log target (or a dedicated access logs bucket if preferred). For the Terraform state buckets, verify ownership and apply the same pattern if app-team managed. Scope In scope :  module/compute/s3/main.tf  (module change),  live/dev/compute/s3/terragrunt.hcl  (enabling the variable for  otep-cv  and  public-alb-logs ). Out of scope :  otep-terraform-state-257212470025  — ownership must be confirmed before remediating (see Notes). CloudTrail data event logging (separate control). Acceptance Criteria [ ]  module/compute/s3/main.tf  includes an  aws_s3_bucket_logging  resource gated on  var.enable_access_logging . [ ]  sst-s3-psd-otep-dev-otep-cv  has server access logging enabled, targeting a designated logs bucket. [ ]  sst-s3-psd-otep-dev-public-alb-logs  has server access logging enabled. [ ] Terraform plan and apply complete successfully with no unrelated changes. [ ] Cloudscape rule AWS-1063 passes for all app-team managed buckets after re-evaluation. Validation # Check logging configuration for each bucket
aws s3api get-bucket-logging --bucket sst-s3-psd-otep-dev-otep-cv
aws s3api get-bucket-logging --bucket sst-s3-psd-otep-dev-public-alb-logs

# Expected output contains LoggingEnabled with TargetBucket and TargetPrefix fields Notes otep-terraform-state-257212470025  uses a different naming convention from the app-team standard ( sst-s3-psd-* ). Verify whether this bucket is platform-managed (e.g., by TLZ or StackSets) before remediating. If platform-managed, raise a suppression with justification rather than modifying directly. The logging target bucket ( sst-s3-psd-otep-dev-tfstate-logs ) must have the S3 log delivery service granted write permissions. Confirm the bucket ACL or policy allows  logging.s3.amazonaws.com  to write objects. Server access logs may take up to an hour to begin appearing after enabling.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
