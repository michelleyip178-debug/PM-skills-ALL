# OTEP-330: Environment IAM Scoping & Secrets Isolation Audit

**Type:** Task
**Status:** Backlog
**Assignee:** Pow Hwee TAN (PSD)
**Story Points:** N/A

---

## Description

Verify that IAM Task Execution roles are tightly scoped to prevent cross-environment access (e.g., ensuring dev execution roles cannot read production secrets). Acceptance Criteria Audit Terragrunt IAM configurations for otep-service and otep-web across all deployment environments (Dev/Staging/Prod). Ensure the dev execution roles have zero permission to read production/staging Secrets Manager ARNs. Remove wildcard resource scopes in IAM configurations for staging/production (e.g., transition from nextauth-secret-psd-otep-dev-otep-web* to precise resource ARNs).

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
