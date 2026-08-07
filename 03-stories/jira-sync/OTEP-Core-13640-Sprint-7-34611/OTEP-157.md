# OTEP-157: Gitlab 12: Generate and Store SBOMs (Software Bill of Materials)

**Type:** Sub-task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

* *Goal:* Create an inventory of all open-source Go modules via SCA for supply chain compliance.
* *IM8 Reform Clause:* SR-2 (Supply Chain Risk Management).
* *Specific Acceptance Criteria:*
** The pipeline executes a designated SBOM generation job upon successful build.
** A file formatted to the CycloneDX standard is generated, listing all application dependencies.
** The SBOM file is visible and downloadable from the pipeline artifacts.
* *Tasks:*
** *Task 1 (Level 1):* Configure GitLab SCA/dependency scanning to output SBOM.
** *Task 2 (Level 1):* Expose SBOM as a downloadable artifact.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-08-07*
