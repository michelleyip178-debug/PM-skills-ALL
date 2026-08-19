# OTEP-727: Remediation: Replace Bastion EC2 with Fargate SSM Access or Add Backup Coverage (AWS-1111, AWS-1003)

**Type:** Task
**Status:** Backlog
**Assignee:** boonsiangteh
**Story Points:** N/A

---

## Description

Type : Remediation Epic : Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev) Labels : cloud-va, cis-benchmark, compliance, remediation Cloudscape Rules : AWS-1111 — EC2 instances should be covered by AWS Backup; AWS-1003 — EBS volumes should be covered by AWS Backup IM8 Clause : BR-1 Resources : i-078843b77c2fccd2c (ec2-psd-otep-dev-bastion), vol-051cb45de1a3c164e, vol-0e770fbe0e9b48956  Context A bastion EC2 instance exists in the dev environment to provide SSM Session Manager port-forwarding access into the intranet VPC. The bastion's IaC already enforces IMDSv2 and SSH is disabled (SSM-only). However, the presence of an EC2 instance materially expands the VAPT audit surface — it introduces CIS controls for EBS encryption, IMDSv2 enforcement, instance roles, OS-level patching, and backup coverage. Cloudscape has flagged both the instance and its two EBS volumes as not covered by AWS Backup under BR-1. Problem The bastion EC2 instance and its EBS volumes are not covered by AWS Backup. More broadly, maintaining an EC2 instance for port-forwarding introduces an ongoing compliance burden across multiple CIS controls when a stateless alternative exists. Proposed Change Option A — Recommended : Replace the bastion with an ECS Fargate task that uses SSM Session Manager for port-forwarding. The Fargate task holds no persistent state, has no EBS volumes, and is excluded from OS-level CIS controls. This eliminates the AWS Backup finding and removes 5+ other CIS controls from audit scope simultaneously. Implementation: Update  module/compute/bastion/  and  live/dev/compute/bastion/  to deploy an ECS Fargate task definition with the SSM agent container image and appropriate IAM task role ( ssm:StartSession ,  ssmmessages:* ). Remove the  aws_instance  and associated EBS volume resources. Option B — If bastion must remain : Add AWS Backup coverage for the instance and its EBS volumes: resource "aws_backup_plan" "bastion" {
  name = "backup-plan-<environment>-bastion"
  rule {
    rule_name         = "daily-backup"
    target_vault_name = aws_backup_vault.this.name
    schedule          = "cron(0 2 * * ? *)"
    lifecycle {
      delete_after = 7
    }
  }
}

resource "aws_backup_selection" "bastion" {
  name         = "backup-sel-<environment>-bastion"
  plan_id      = aws_backup_plan.bastion.id
  iam_role_arn = aws_iam_role.backup.arn
  resources    = [
    "arn:aws:ec2:<region>:<account-id>:instance/i-078843b77c2fccd2c",
  ]
} Scope In scope :  module/compute/bastion/  and  live/dev/compute/bastion/ . Out of scope : Production bastion (separate ticket); other EC2 instances not related to bastion access. Acceptance Criteria If Option A (Fargate replacement) : [ ] The bastion EC2 instance ( i-078843b77c2fccd2c ) and its EBS volumes are terminated and removed from IaC. [ ] An ECS Fargate task with SSM Session Manager capability is deployed and can be used for port-forwarding into the intranet VPC. [ ] SSM port-forwarding functionality is verified end-to-end by a team member before closing. [ ] Cloudscape findings AWS-1111 and AWS-1003 are resolved (resource no longer exists). If Option B (Backup coverage) : [ ] AWS Backup plan and selection covering the bastion instance and its EBS volumes are deployed via IaC. [ ]  aws backup list-protected-resources  confirms the instance and volumes are protected. [ ] Cloudscape rules AWS-1111 and AWS-1003 pass for these resources after re-evaluation. Validation # Option A — confirm EC2 instance is terminated
aws ec2 describe-instances --instance-ids i-078843b77c2fccd2c
# Expected: State = terminated

# Option A — confirm Fargate service is running
aws ecs list-services --cluster <cluster-name>

# Option B — confirm backup coverage
aws backup list-protected-resources \
  --query 'Results[?ResourceArn contains `i-078843b77c2fccd2c`]' Notes Option A is strongly recommended. The bastion holds no persistent state (it is a tunneling hop), so there is no data loss risk in replacing it with Fargate. Removing the EC2 instance eliminates backup, EBS encryption, OS patching, and IMDSv2 findings in a single change. If Option A is chosen, ensure the ECS cluster used by the Fargate task has VPC connectivity to the intranet subnets and that the task's security group allows outbound to the SSM endpoints. If Option B is chosen, a 7-day retention period is appropriate for dev. Increase for production environments.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
