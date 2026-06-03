# OTEP-156: Integrate DevSecOps Tools & Quality Scanners for service repo

**Type:** Sub-task
**Status:** QA
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

* *Goal:* Embed the full suite of SHIP-HATS and GitLab DevSecOps security scanners into the CI pipelines tailored for Go code.
* *IM8 Reform Clause:* RA-5 (Vulnerability Scanning), SA-11 (Developer Security Testing), CM-6 (Configuration Settings).
* *Specific Acceptance Criteria:*
** *GitLab Secret Detection:* The pipeline fails if hardcoded credentials or API keys are detected in the repository.
** *GitLab SCA (Dependency Scanning):* The pipeline fails if vulnerable open-source dependencies are detected in the application manifests.
** *SonarQube, GitLab SAST & Linting:* The pipeline fails if static analysis detects critical flaws or code coverage drops below defined thresholds.
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

**Soumya Routa:** SAST, secret scanning, SCA, container scanning, DAST API, and DAST web URL scans are configured in the *otep-devops-tests* repository (mirrored from the original repository).

For testing the DAST-related custom jobs, sample Nginx images and API specifications are used.

The container scanning job scans images hosted in the GitLab Container Registry.

The KICS IaC scan job analyzes Dockerfiles for infrastructure-as-code vulnerabilities.

Semgrep is used for SAST scanning of Go source files.

Gymnasium dependency scanning is used for SCA.

All scan jobs are defined in a local configuration file:
[https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-service/-/jobs/124777886|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-service/-/jobs/124777886]

*Synced from Jira: 2026-06-03*
