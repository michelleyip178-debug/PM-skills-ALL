# OTEP-729: Remediation: Replace SQS Wildcard Action in ECS IAM Policy (AWS-1145)

**Type:** Task
**Status:** QA
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Type : Remediation  Epic : Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev)  Labels : cloud-va, cis-benchmark, compliance, remediation  Cloudscape Rule : AWS-1145 — IAM customer managed policies should not grant full access  IM8 Clause : AC-1  Resource : iam-pol-psd-otep-dev-otep-service-sqs-access (ANPATXYYO2MEVNBGJEJJW)  Context The ECS shared module defines an IAM policy that grants the  otep-service  ECS task role access to SQS queues. The current policy uses  "sqs:*" , which violates least-privilege by including destructive management actions such as  sqs:DeleteQueue  and  sqs:SetQueueAttributes . This was flagged by Cloudscape under rule AWS-1145 and maps to IM8 AC-1 (access control). Problem module/compute/ecs/shared/main.tf  (line 103) grants  "sqs:*"  over the configured  sqs_queue_arns . This over-permissive policy is attached to all ECS services that pass  sqs_queue_arns  as an input. Proposed Change Replace the  "sqs:*"  action in the IAM policy with an explicit, least-privilege action list scoped to standard producer/consumer operations: actions = [
  "sqs:SendMessage",
  "sqs:ReceiveMessage",
  "sqs:DeleteMessage",
  "sqs:GetQueueAttributes",
  "sqs:GetQueueUrl",
  "sqs:ChangeMessageVisibility",
] Update  module/compute/ecs/shared/main.tf  at the relevant  aws_iam_policy_document  statement. No changes to the resource ARN bindings are needed. Scope In scope :  module/compute/ecs/shared/main.tf  — the shared ECS IAM policy for SQS access. Affects all ECS services that provide  sqs_queue_arns  input. Out of scope : SQS queue policies; other IAM policies unrelated to ECS SQS access. Acceptance Criteria [ ]  "sqs:*"  is removed from the IAM policy document in  module/compute/ecs/shared/main.tf . [ ] Explicit least-privilege SQS actions are substituted as listed in the Proposed Change. [ ] Terraform plan and apply are executed successfully in the dev environment with no unrelated changes. [ ] The updated policy version is active on  iam-pol-psd-otep-dev-otep-service-sqs-access . [ ] SQS message processing (send, receive, delete) is verified as functional in dev after the change. [ ] No unrelated IAM, networking, or logging changes are introduced. Validation # Retrieve the current default policy version ARN
aws iam get-policy --policy-arn arn:aws:iam::<account-id>:policy/iam-pol-psd-otep-dev-otep-service-sqs-access

# Inspect the policy document — confirm no "sqs:*" is present
aws iam get-policy-version \
  --policy-arn arn:aws:iam::<account-id>:policy/iam-pol-psd-otep-dev-otep-service-sqs-access \
  --version-id <latest-version-id> Expected: The  Action  array contains only the explicit actions listed above. No  sqs:*  wildcard is present. Notes If the application requires additional SQS actions (e.g.,  sqs:ListQueues  for discovery), add them explicitly rather than reverting to a wildcard. This change affects all ECS services using the shared module with  sqs_queue_arns . Verify all affected services are functioning before marking done. Coordinate with the iam-policy-s3-wildcard ticket — both are in the same file ( main.tf ) and can be fixed in a single PR.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
