# OTEP-566: Implement VPC-based OpenSearch index provisioning using Lambda migrator

**Type:** Task
**Status:** Backlog
**Assignee:** Benjamin Aw
**Story Points:** N/A

---

## Description

We need a secure and repeatable way to provision OpenSearch indices, templates, and aliases for the private intranet OpenSearch cluster. The OpenSearch domain is only reachable from within the intranet VPC, so local machines and external CI runners cannot reliably provision OpenSearch resources directly. Based on the agreed ADR, we should implement a  VPC-attached Lambda index migrator  that can be triggered through CI/CD or manually via AWS APIs. Reference:     Scope Implement the initial Lambda-based OpenSearch migration framework, including: VPC-attached Lambda function with access to the private OpenSearch endpoint IAM role and security group rules for the migrator Initial migration script structure for OpenSearch templates, indices, and aliases CI/CD or documented manual trigger mechanism to invoke the migrator Logging of migration execution result in CloudWatch Acceptance Criteria Lambda migrator is deployed via IaC and attached to the correct private subnets. OpenSearch security group allows HTTPS access from the Lambda migrator SG. Existing backend ECS task access to OpenSearch is not broken. Lambda migrator can successfully connect to the private OpenSearch endpoint. Migration logic is idempotent and safe to rerun. Initial index/template/alias provisioning flow is implemented and tested in dev. Migration execution logs include environment, migration version/name, success/failure status, and error details if any. Trigger mechanism is documented, including how to run the migrator from CI/CD or manually. Required permissions are scoped to the migrator role and do not grant unnecessary broad admin access. README or runbook is added with setup, deployment, and troubleshooting notes. Out of Scope Self-hosted GitLab Runner in intranet ECS SSM port forwarding as the primary provisioning mechanism Large reindexing or backfill jobs Full OpenSearch migration framework beyond the initial index provisioning baseline

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
