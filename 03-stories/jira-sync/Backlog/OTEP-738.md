# OTEP-738: Remediation: Enforce SSL-Only Access on S3 Buckets via Bucket Policy (AWS-1126)

**Type:** Task
**Status:** In Progress
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Type : Remediation  Epic : Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev)  Labels : cloud-va, cis-benchmark, compliance, remediation  Cloudscape Rule : AWS-1126 — S3 buckets should deny non-SSL requests  IM8 Clause : DP-3  Resources : sst-s3-psd-otep-dev-otep-cv, sst-s3-psd-otep-dev-public-alb-logs  Context Two S3 buckets are missing a bucket policy that denies requests made over plain HTTP ( aws:SecureTransport = false ). The S3 module ( module/compute/s3/main.tf ) does not currently attach a default SSL-enforcement policy, so any bucket created from the module lacks this control. This was flagged by Cloudscape under AWS-1126 and maps to IM8 DP-3 (data-in-transit protection). Problem sst-s3-psd-otep-dev-otep-cv  and  sst-s3-psd-otep-dev-public-alb-logs  have no bucket policy denying insecure transport. Clients can access objects over HTTP if credentials permit. Proposed Change Add an  aws_s3_bucket_policy  resource to  module/compute/s3/main.tf  that attaches a  DenyInsecureTransport  statement by default: data "aws_iam_policy_document" "ssl_enforcement" {
  statement {
    sid       = "DenyInsecureTransport"
    effect    = "Deny"
    actions   = ["s3:*"]
    resources = [
      aws_s3_bucket.this.arn,
      "${aws_s3_bucket.this.arn}/*",
    ]
    principals {
      type        = "*"
      identifiers = ["*"]
    }
    condition {
      test     = "Bool"
      variable = "aws:SecureTransport"
      values   = ["false"]
    }
  }
} Important — ALB logs bucket :  sst-s3-psd-otep-dev-public-alb-logs  already has a bucket policy granting ELB log delivery permissions. The SSL-enforcement statement must be merged into the existing policy document (using  aws_iam_policy_document  data source with  source_policy_documents  or  override_policy_documents ), not applied as a separate  aws_s3_bucket_policy  resource. Replacing the existing policy will break ALB log delivery. For the  public-alb-logs  bucket, the fix should be applied in  module/compute/public-alb/main.tf  where the existing bucket policy is managed. Scope In scope :  module/compute/s3/main.tf  (for  otep-cv  bucket) and  module/compute/public-alb/main.tf  (for  public-alb-logs  bucket). Out of scope : S3 buckets not managed by these modules; IAM policies; KMS key policies. Acceptance Criteria [ ]  module/compute/s3/main.tf  attaches a bucket policy with a  DenyInsecureTransport  statement to all managed buckets. [ ]  sst-s3-psd-otep-dev-otep-cv  has the SSL-enforcement statement in its bucket policy. [ ]  sst-s3-psd-otep-dev-public-alb-logs  has the SSL-enforcement statement merged into its existing ELB delivery policy — ELB log delivery continues to function after the change. [ ] Terraform plan and apply complete successfully with no unrelated changes. [ ] Cloudscape rule AWS-1126 passes for both resources after re-evaluation. Validation # Check bucket policy for otep-cv
aws s3api get-bucket-policy --bucket sst-s3-psd-otep-dev-otep-cv

# Check bucket policy for public-alb-logs
aws s3api get-bucket-policy --bucket sst-s3-psd-otep-dev-public-alb-logs

# Confirm ALB log delivery still works after applying the policy change
# (check that new ALB log files appear in the logs bucket after a short period) Expected: Both bucket policies contain a  DenyInsecureTransport  Deny statement with  aws:SecureTransport = false  condition. Notes When merging policies for the ALB logs bucket, use Terraform's  aws_iam_policy_document  data source composition rather than raw JSON concatenation to avoid drift. If new S3 buckets are created from the module in future environments, they will automatically inherit the SSL enforcement policy once the module is updated.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
