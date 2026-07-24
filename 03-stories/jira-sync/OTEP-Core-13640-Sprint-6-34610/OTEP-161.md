# OTEP-161: Gitlab 16: Implement Infrastructure Drift Detection

**Type:** Sub-task
**Status:** Backlog
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

* *Goal:* Ensure the actual AWS environment hasn't been manually altered via ClickOps.
* *IM8 Reform Clause:* CM-3 (Configuration Change Control).
* *Specific Acceptance Criteria:*
** A scheduled pipeline is configured to run automatically.
** If the scheduled pipeline detects differences between the infrastructure codebase and the live AWS environment, the pipeline fails.
** A notification is delivered to the designated communication channel indicating the drift.
* *Tasks:*
** *Task 1 (Level 2) [Optional]:* Create a scheduled GitLab pipeline for infrastructure drift checks.

*Task 2 (Level 2) [Optional]:* Configure drift notification alerts via webhook.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-23*
