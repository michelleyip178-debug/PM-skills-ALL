# OTEP-620: Evaluation store (RDS + S3 raw blobs) & result emission

**Status:** Done
**Assignee:** Benjamin Aw
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 6 (35009)

---

## Description

As a  CIE team,  we want  one canonical store receiving every inference/eval/judge record  so that  all quality questions are answered from one queryable place. Acceptance criteria Schema v1 (tables above) created via versioned migrations (Alembic or equivalent) owned in cie-backend, applied through the intelligence-iac deployment path. Record shape extends the  eval/results  report to per-request granularity; ranked predictions stored as JSONB. Both inference paths emit records best-effort async; emission failure never fails an inference (metric + log on drop). Raw input documents land in the S3 raw bucket keyed by  request_id ; rows carry  s3_raw_key . A documented SQL query returns per-variant daily P@5.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-629 | Schema v1 + migrations; cie.core.evalstore access layer (psycopg/SQLAlchemy, pooled, short timeouts).  | Done |
| OTEP-630 | RDS access for task roles (security group + IAM DB auth or secret), migration execution step in deploy, S3 raw-blob bucket + lifecycle/retention, task-role S3 write.  | Done |
| OTEP-631 | Emitter in cie.inference (shared by app + worker): async/batched, swallow-and-log, env-gated (EVAL_EMIT_ENABLED). Decision recorded: direct writes vs SQS buffer. | Done |
| OTEP-632 | Raw input archiving to S3 + s3_raw_key on the record.  | Done |
| OTEP-633 | SQL query pack + runbook in eval/README.md; Grafana/QuickSight datasource panel for per-variant trends. | Done |

---

## Latest Comments

**boonsiangteh** (2026-07-24)
Benjamin AW  mentioned this issue in  a merge request  of  WOG / PSD / pdo / intelligence / intelligence-iac  on branch  OTEP-825 : [Ben]   qa/preprod: port eval platform from dev + drift alignment

---
*Synced from Jira: 2026-07-28*
