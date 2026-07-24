# OTEP-261: Devsecops pipeline for WEB 

**Type:** Sub-task
**Status:** Done
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

* *Goal:* Embed the full suite of SHIP-HATS and GitLab DevSecOps security scanners into the CI pipelines tailored for web code(node, nextjs).
* *IM8 Reform Clause:* RA-5 (Vulnerability Scanning), SA-11 (Developer Security Testing), CM-6 (Configuration Settings).
* *Specific Acceptance Criteria:*
** *GitLab Secret Detection:* The pipeline fails if hardcoded credentials or API keys are detected in the repository.
** *GitLab SCA (Dependency Scanning):* The pipeline fails if vulnerable open-source dependencies are detected in the application manifests.
** *SonarQube, GitLab SAST & Linting:* The pipeline fails if static analysis detects critical flaws or code coverage drops below defined thresholds.
** *Checkov (IaC):* The infrastructure pipeline fails if IM8 compliance violations are detected in the infrastructure code.
** *GitLab Container Scanning:* The deployment stage halts if the container image scanner reports any Critical or High vulnerabilities.
** *GitLab DAST:* (If configured) The dynamic scanner successfully generates a vulnerability report against the deployed Staging environment.
* *Tasks:*
** *Task 1 (Level 1) [sd-6]:* Set up GitLab Secret Detection.
** *Task 2 (Level 1) [sd-5]:* Enable GitLab SCA (Dependency Scanning).
** *Task 3 (Level 1) [sd-4]:* Integrate SHIP-HATS SonarQube, linting, and GitLab SAST.
** *Task 4 (Level 1) [sd-4]:* Integrate SHIP-HATS Checkov for IaC.
** *Task 5 (Level 1) [cs-7]:* Enable GitLab Container Scanning for the registry.
** *Task 6 (Level 1) [sd-7]:* Protect/mask CI job environment variables.
** *Task 7 (Level 2) [Optional]:* Configure GitLab DAST for runtime Staging scans.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** [https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-web/-/pipelines/19179416|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-web/-/pipelines/19179416]
wiki:[https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-web/-/wikis/OTEP-WEB-ci-pipeline-design|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-web/-/wikis/OTEP-WEB-ci-pipeline-design]

!image-20260514-061415.png|width=465,alt="image-20260514-061415.png"!

*Synced from Jira: 2026-07-23*
