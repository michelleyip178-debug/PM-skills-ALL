# OTEP-160: gitlab 15: Set Up Manual Deployment Approval Gates

**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Goal:  Enforce Segregation of Duties (SoD) by requiring manual approval before production deployment. IM8 Reform Clause:  CM-5 (Access Restrictions for Change), AC-3 (Access Enforcement). Specific Acceptance Criteria: The Production environment is marked as protected within the deployment tool. When a pipeline reaches the Production deployment stage, it pauses in a blocked/manual state. Only users explicitly assigned as Approvers can trigger the blocked production job. Tasks: Task 1 (Level 1):  Define Production and Staging environments in GitLab. Task 2 (Level 1):  Mark the Production environment as "Protected." Task 3 (Level 1):  Assign explicit deployment approvers. Task 4 (Level 2) [Optional]:  Integrate ITSM / Change Management ticketing gates.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-20*
