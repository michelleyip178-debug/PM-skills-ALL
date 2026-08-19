# OTEP-736: Remediation: Add AWS Backup Coverage for S3 Buckets (AWS-1095)

**Type:** Task
**Status:** In Progress
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Type : Remediation  Epic : Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev)  Labels : cloud-va, cis-benchmark, compliance, remediation  Cloudscape Rule : AWS-1095 — S3 buckets should be covered by AWS Backup  IM8 Clause : BR-1  Resources : sst-s3-psd-otep-dev-otep-cv, sst-s3-psd-otep-dev-tfstate, sst-s3-psd-otep-dev-tfstate-logs, sst-s3-psd-otep-dev-public-alb-logs, otep-terraform-state-257212470025  Context Five S3 buckets are flagged as not covered by AWS Backup. While most have S3 versioning enabled (providing object-level point-in-time recovery), Cloudscape specifically requires AWS Backup coverage. AWS Backup for S3 provides centralised governance, PITR (continuous backup), and audit-ready reporting. Problem Five S3 buckets lack AWS Backup plan coverage. Cloudscape rule AWS-1095 explicitly checks for AWS Backup plan membership — S3 versioning alone does not satisfy the control. Proposed Change Enable AWS Backup for S3 with continuous backup (PITR). Use the same backup vault as the RDS backup (see  rds-aws-backup-coverage.md ) to avoid vault proliferation. resource "aws_backup_plan" "s3" {
  name = "backup-plan-${local.name_prefix}-s3"

  rule {
    rule_name         = "s3-continuous-backup"
    target_vault_name = aws_backup_vault.this.name
    schedule          = "cron(0 18 * * ? *)"  # Daily at 18:00 UTC (02:00 SGT)

    lifecycle {
      delete_after = 35
    }
  }

  tags = var.tags
}

resource "aws_backup_selection" "s3_buckets" {
  name         = "s3-bucket-selection"
  plan_id      = aws_backup_plan.s3.id
  iam_role_arn = aws_iam_role.backup.arn

  resources = [
    "arn:aws:s3:::sst-s3-psd-otep-dev-otep-cv",
    "arn:aws:s3:::sst-s3-psd-otep-dev-tfstate",
    "arn:aws:s3:::sst-s3-psd-otep-dev-tfstate-logs",
    "arn:aws:s3:::sst-s3-psd-otep-dev-public-alb-logs",
  ]
} Alternatively, use a tag-based selection to automatically cover all app-team S3 buckets: resource "aws_backup_selection" "s3_by_tag" {
  name         = "s3-tag-selection"
  plan_id      = aws_backup_plan.s3.id
  iam_role_arn = aws_iam_role.backup.arn

  selection_tag {
    type  = "STRINGEQUALS"
    key   = "Project-Code"
    value = "otep"
  }
} Scope Shared backup vault + IAM role (coordinate with  rds-aws-backup-coverage.md  — ideally a single backup module) Covers 4 confirmed app-team buckets otep-terraform-state-257212470025 : verify ownership first — if app-team, include; if platform-managed, raise separately Acceptance Criteria [ ] AWS Backup plan exists with S3 resources included [ ] All 4 app-team S3 buckets appear in  aws backup list-protected-resources [ ] Backup jobs complete successfully (verify after first scheduled run) [ ] Cloudscape rule AWS-1095 passes for all covered buckets after re-evaluation [ ]  otep-terraform-state-257212470025  ownership confirmed and either included or escalated [ ] All resources managed in IaC Validation # Confirm S3 buckets are protected
aws backup list-protected-resources \
  --query "Results[?starts_with(ResourceArn, 'arn:aws:s3')]"

# Verify backup plan
aws backup list-backup-plans --query 'BackupPlansList[?BackupPlanName==`backup-plan-psd-otep-dev-s3`]'

# Verify a backup job has completed (after first schedule)
aws backup list-backup-jobs --by-resource-type S3 --by-state COMPLETED Notes AWS Backup for S3 requires "S3 Backup" advanced features to be opted in at the account level. Verify with:  aws backup describe-region-settings --query 'ResourceTypeOptInPreference.S3' . If false, enable it first. S3 versioning remains enabled as a complementary control — it provides immediate object-level undo capability independent of AWS Backup. The backup vault, IAM role, and plan should be shared across resource types (RDS, S3, EC2/EBS) to keep the backup architecture clean. Consider a dedicated  module/compute/backup/  or  live/dev/compute/backup/  stack. AWS Backup compliance mode (vault lock) is not mandated by this ticket — that decision can be made per-environment as needed.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang** (2026-08-14)
hey     It seems this bucket otep-terraform-state-257212470025  it no longer needed. That is the old state management S3 bucket and we moved to new bucket: sst-s3-psd-otep-dev-tfstate. But the ticket proposal changes is still valid for our S3 buckets ( otep-cv ,  tfstate ,  tfstate-logs ,  public-alb-logs ) all still need to be added to an AWS Backup plan/selection — versioning and SSL/logging status don't substitute for AWS Backup coverage, which is what Cloudscape's AWS-1095 rule specifically checks.
