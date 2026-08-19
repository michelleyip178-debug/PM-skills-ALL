# OTEP-733: Remediation: Add AWS Backup Coverage for RDS Instance (AWS-1008)

**Type:** Task
**Status:** QA
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Summary Add AWS Backup plan coverage for RDS instance  rds-psd-otep-dev  to satisfy Cloudscape AWS-1008. The instance already has native 7-day automated backups, but AWS Backup provides centralised backup governance, cross-account copy capability, and satisfies the Cloudscape compliance check. Type Remediation Epic Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev) Labels cloud-va ,  cis-benchmark ,  compliance ,  remediation IM8 Clause BR-1  Context The RDS instance  rds-psd-otep-dev  has native automated backups configured ( backup_retention_period = 7 ). However, Cloudscape requires coverage by AWS Backup specifically — native RDS snapshots alone do not satisfy the rule. AWS Backup provides centralised backup management, policy enforcement, and audit-ready reporting that Cloudscape validates against. Problem Cloudscape rule AWS-1008 requires RDS instances to be protected by an AWS Backup plan. The instance is not currently covered by any AWS Backup plan, vault, or selection resource. Proposed Change Create an AWS Backup vault, plan, and selection for the RDS instance: resource "aws_backup_vault" "this" {
  name = "backup-vault-${local.name_prefix}"
  tags = var.tags
}

resource "aws_backup_plan" "rds" {
  name = "backup-plan-${local.name_prefix}-rds"

  rule {
    rule_name         = "daily-rds-backup"
    target_vault_name = aws_backup_vault.this.name
    schedule          = "cron(0 17 * * ? *)"  # Daily at 17:00 UTC (01:00 SGT)

    lifecycle {
      delete_after = 35
    }
  }

  tags = var.tags
}

resource "aws_iam_role" "backup" {
  name = "iam-role-${local.name_prefix}-backup"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Action    = "sts:AssumeRole"
      Principal = { Service = "backup.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "backup" {
  role       = aws_iam_role.backup.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForBackup"
}

resource "aws_iam_role_policy_attachment" "restore" {
  role       = aws_iam_role.backup.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForRestores"
}

resource "aws_backup_selection" "rds" {
  name         = "rds-selection"
  plan_id      = aws_backup_plan.rds.id
  iam_role_arn = aws_iam_role.backup.arn

  resources = [
    aws_db_instance.this.arn
  ]
} Scope New resources in  module/database/rds/  or a dedicated  module/compute/backup/  module Consider making the backup module reusable so it can also cover S3 and EC2 (see  s3-backup-coverage.md  and  bastion-ec2-removal.md ) Acceptance Criteria [ ] AWS Backup vault exists in the account [ ] AWS Backup plan is active with a daily schedule and appropriate retention [ ] RDS instance  rds-psd-otep-dev  is listed in  aws backup list-protected-resources [ ] Backup jobs complete successfully (verify after first scheduled run) [ ] Cloudscape rule AWS-1008 passes after re-evaluation [ ] All resources managed in IaC Validation # Confirm RDS is protected
aws backup list-protected-resources \
  --query "Results[?ResourceArn=='arn:aws:rds:ap-southeast-1:257212470025:db:rds-psd-otep-dev']"

# Check backup plan exists
aws backup list-backup-plans --query 'BackupPlansList[].BackupPlanName'

# Verify a backup job has run (after first schedule)
aws backup list-backup-jobs --by-resource-arn arn:aws:rds:ap-southeast-1:257212470025:db:rds-psd-otep-dev Notes Native RDS automated backups (7-day retention) remain in place as a complementary mechanism — do not remove them. The backup vault should be shared across resource types (RDS, S3, EC2) to avoid vault proliferation. Consider creating a single backup module that other stacks reference. AWS Backup compliance mode (vault lock) is optional and can be adjusted per environment — this ticket enables backup coverage without mandating compliance mode.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
