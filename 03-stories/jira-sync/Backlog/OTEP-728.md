# OTEP-728: Remediation: Replace S3 Wildcard Action in ECS IAM Policy (AWS-1145)

**Type:** Task
**Status:** QA
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Type : Remediation Epic : Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev) Labels : cloud-va, cis-benchmark, compliance, remediation Cloudscape Rule : AWS-1145 — IAM customer managed policies should not grant full access IM8 Clause : AC-1 Resource : iam-pol-psd-otep-dev-otep-service-s3-access (ANPATXYYO2ME3NZGVRFIY)  Context The ECS shared module defines an IAM policy that grants the  otep-service  ECS task role access to S3. The current policy uses  "s3:*" , which violates least-privilege by including dangerous administrative actions such as  s3:DeleteBucket  and  s3:PutBucketPolicy . This was flagged by Cloudscape under rule AWS-1145 and maps to IM8 AC-1 (access control). Problem module/compute/ecs/shared/main.tf  (line 153) grants  "s3:*"  over the configured  s3_bucket_arns . This over-permissive policy is attached to all ECS services that pass  s3_bucket_arns  as an input, currently including  otep-service . Proposed Change Replace the  "s3:*"  action in the IAM policy with an explicit, least-privilege action list scoped to what the application actually requires: actions = [
  "s3:GetObject",
  "s3:PutObject",
  "s3:DeleteObject",
  "s3:ListBucket",
  "s3:GetBucketLocation",
  "s3:AbortMultipartUpload",
  "s3:ListMultipartUploadParts",
] Update  module/compute/ecs/shared/main.tf  at the relevant  aws_iam_policy_document  statement. No changes to the resource ARN bindings are needed. Scope In scope :  module/compute/ecs/shared/main.tf  — the shared ECS IAM policy for S3 access. Affects all ECS services that provide  s3_bucket_arns  input (currently  otep-service  in dev). Out of scope : Other IAM policies unrelated to ECS S3 access; S3 bucket policies themselves. Acceptance Criteria [ ]  "s3:*"  is removed from the IAM policy document in  module/compute/ecs/shared/main.tf . [ ] Explicit least-privilege S3 actions are substituted as listed in the Proposed Change. [ ] Terraform plan and apply are executed successfully in the dev environment with no unrelated changes. [ ] The updated policy version is active on  iam-pol-psd-otep-dev-otep-service-s3-access . [ ] Application functionality (S3 reads, writes, and multipart uploads) is verified in dev after the change. [ ] No unrelated IAM, networking, or logging changes are introduced. Validation # Retrieve the current default policy version ARN
aws iam get-policy --policy-arn arn:aws:iam::<account-id>:policy/iam-pol-psd-otep-dev-otep-service-s3-access

# Inspect the policy document — confirm no "s3:*" is present
aws iam get-policy-version \
  --policy-arn arn:aws:iam::<account-id>:policy/iam-pol-psd-otep-dev-otep-service-s3-access \
  --version-id <latest-version-id> Expected: The  Action  array contains only the explicit actions listed above. No  s3:*  or  s3:Delete*  wildcard is present. Notes If additional S3 actions are required by the application in the future, they must be added explicitly — do not revert to a wildcard. This change affects all ECS services using the shared module with  s3_bucket_arns . Test all affected services (currently  otep-service ) before marking done.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
