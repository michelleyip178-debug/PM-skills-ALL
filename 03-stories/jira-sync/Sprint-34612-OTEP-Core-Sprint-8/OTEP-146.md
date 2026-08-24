# OTEP-146: Gitlab 04 - Infrastructure as Code (IaC) CI Pipeline

**Status:** Done
**Assignee:** Soumya Routa
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Goal:  Automate Terraform validation, security scanning, and remote state management. IM8 Reform Clause:  CM-2 (Baseline Configuration), CM-6 (Configuration Settings). Specific Acceptance Criteria: The infrastructure state file is managed natively within the GitLab project interface with active state locking. The infrastructure pipeline fails if Checkov detects IM8 compliance violations in the code. The pipeline successfully generates a reviewable infrastructure plan. Tasks: Task 1:  Enable S3 and configure backend. Task 2:  Create CI configuration for infrastructure formatting and planning. Task 3:  Verify SHIP-HATS Checkov for IaC security scanning. Once DevSecOps finished, it should be already handled.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa** (2026-05-25)
duplicate card

---
*Synced from Jira: 2026-08-20*
