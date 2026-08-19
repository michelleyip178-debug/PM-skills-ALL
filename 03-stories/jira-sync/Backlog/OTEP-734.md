# OTEP-734: Remediation: Enable CloudWatch Log Exports for RDS PostgreSQL Instance (AWS-1153)

**Type:** Task
**Status:** QA
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Type : Remediation  Epic : Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev)  Labels : cloud-va, cis-benchmark, compliance, remediation  Cloudscape Rule : AWS-1153 — RDS DB instances should publish logs to CloudWatch Logs  IM8 Clause : LM-5  Resource : rds-psd-otep-dev (db-V5YHNAMMUT2R25FDDVHD2XVTGE)  Context The RDS PostgreSQL instance  rds-psd-otep-dev  does not export any logs to CloudWatch Logs. The RDS module ( module/database/rds/main.tf ) does not set  enabled_cloudwatch_logs_exports  on the  aws_db_instance  resource. Without log exports, database activity, errors, and slow queries are not captured in a centralised, durable log store. This was flagged by Cloudscape under rule AWS-1153 and maps to IM8 LM-5 (database activity logging). Problem rds-psd-otep-dev  produces no CloudWatch log streams. There is no audit trail for database connections, errors, or slow queries in the dev environment. Proposed Change Add  enabled_cloudwatch_logs_exports  to the  aws_db_instance  resource in  module/database/rds/main.tf : enabled_cloudwatch_logs_exports = ["postgresql", "upgrade"] Additionally, add  log_min_duration_statement  to the RDS parameter group to capture slow queries: parameter {
  name  = "log_min_duration_statement"
  value = "1000"  # Log queries taking longer than 1000ms
} Expose  enabled_cloudwatch_logs_exports  as an optional module variable with a sensible default for PostgreSQL so other RDS instances inherit the same control. Scope In scope :  module/database/rds/main.tf  — the  aws_db_instance  resource and associated parameter group. Out of scope : CloudWatch log retention policies (separate ticket if needed); RDS Performance Insights; Aurora clusters (different resource type). Acceptance Criteria [ ]  enabled_cloudwatch_logs_exports = ["postgresql", "upgrade"]  is set on the  aws_db_instance  resource in the module. [ ] CloudWatch log groups  /aws/rds/instance/rds-psd-otep-dev/postgresql  and  /aws/rds/instance/rds-psd-otep-dev/upgrade  are created in the dev account. [ ] Log events are visible in the CloudWatch log groups after a short period. [ ] Terraform plan and apply complete successfully; the RDS instance applies the change without unexpected downtime. [ ] Cloudscape rule AWS-1153 passes for  rds-psd-otep-dev  after re-evaluation. Validation # Verify enabled log exports on the instance
aws rds describe-db-instances \
  --db-instance-identifier rds-psd-otep-dev \
  --query 'DBInstances[0].EnabledCloudwatchLogsExports'

# Expected output: ["postgresql", "upgrade"]

# Confirm log groups exist
aws logs describe-log-groups \
  --log-group-name-prefix /aws/rds/instance/rds-psd-otep-dev Notes Enabling  enabled_cloudwatch_logs_exports  on a running RDS instance triggers a modification and may cause a brief connection interruption during parameter application. Schedule during a low-traffic window or confirm the instance handles this change without requiring a reboot. log_min_duration_statement  requires the parameter group to be in  pending-reboot  state if using a static parameter group. Confirm whether a reboot is required in dev. Consider setting a CloudWatch log retention period (e.g., 90 days) on the new log groups to manage storage costs.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
