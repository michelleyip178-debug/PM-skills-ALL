# OTEP-262: DEVSECOPS pipeline for IAC repo.

**Type:** Sub-task
**Status:** QA
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

[https://sgtechstack.atlassian.net/browse/OTEP-179?search_id=c38745a9-98f3-4e37-b968-7e9e583fa8e4|https://sgtechstack.atlassian.net/browse/OTEP-179?search_id=c38745a9-98f3-4e37-b968-7e9e583fa8e4|smart-link] 

[https://sgtechstack.atlassian.net/browse/OTEP-156?search_id=c364e738-899b-482f-9d4d-33ec7a1b647b|https://sgtechstack.atlassian.net/browse/OTEP-156?search_id=c364e738-899b-482f-9d4d-33ec7a1b647b|smart-link] 

* *Goal:* Embed the full suite of SHIP-HATS and GitLab DevSecOps security scanners into the CI pipelines tailored forIAC code.
* *IM8 Reform Clause:* RA-5 (Vulnerability Scanning), SA-11 (Developer Security Testing), CM-6 (Configuration Settings).
* *Specific Acceptance Criteria:*
** *GitLab Secret Detection:* The pipeline fails if hardcoded credentials or API keys are detected in the repository.
** *GitLab SCA (Dependency Scanning):* The pipeline fails if vulnerable open-source dependencies are detected in the application manifests.
** *SonarQube, GitLab SAST & Linting:* The pipeline fails if static analysis detects critical flaws or code coverage drops below defined thresholds.
** *Checkov (IaC):* The infrastructure pipeline fails if IM8 compliance violations are detected in the infrastructure code.
** *GitLab Container Scanning:* The deployment stage halts if the container image scanner reports any Critical or High vulnerabilities.
* *Tasks:*
** *Task 1 (Level 1) [sd-6]:* Set up GitLab Secret Detection.
** *Task 2 (Level 1) [sd-5]:* Enable GitLab SCA (Dependency Scanning).
** *Task 3 (Level 1) [sd-4]:*  linting, validate  and  kicks SAST.
** *Task 4 (Level 1) [sd-4]:* Integrate SHIP-HATS Checkov for IaC.
** *Task 5 (Level 1) [cs-7]:* Enable GitLab Container Scanning for the registry.(triggers when docker files detects)
** *Task 6 (Level 1) [sd-7]:* Protect/mask CI job environment variables.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** implemented Devsecops, lint, plan, validate jobs

[https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-iac/-/pipelines/19120432|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-iac/-/pipelines/19120432]

!image-20260512-153813.png|width=912,alt="image-20260512-153813.png"!

|*Task ID*|*Task Description*|*Status*|
|*Task 1*|Set up GitLab Secret Detection [sd-6]|*Done*|
|*Task 2*|Enable GitLab SCA / Dependency Scanning [sd-5]|*Done*|
|*Task 3*|Linting, validate  and SAST activation [sd-4]|*Done*|
|*Task 4*|Integrate SHIP-HATS Checkov for IaC [sd-4]|*Done*|
|*Task 5*|Enable GitLab Container Scanning for the registry [cs-7]|*Done*|
|*Task 6*|Protect/mask CI job environment variables [sd-7]|*Done*|
| | | |

**Soumya Routa:** Wiki [https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-iac/-/wikis/IAC-CI-pipeline|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-iac/-/wikis/IAC-CI-pipeline]

*Synced from Jira: 2026-07-01*
