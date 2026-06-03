# OTEP-145: Gitlab 03 - CI/CD Pipeline Core & Automation (Application Pipeline (Frontend & Backend))

**Type:** Sub-task
**Status:** QA
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

* *Goal:* Automate the build, scan, and registry push processes for the application.
* *IM8 Reform Clause:* SD-3 (Continuous Integration), RA-5 (Vulnerability Scanning).
* *Specific Acceptance Criteria:*
** The pipeline triggers automatically upon a push and verifies pinned dependency versions.
** GitLab Secret Detection, SCA, SonarQube, and SAST scanners run successfully. The pipeline fails if critical vulnerabilities or code coverage drops are detected.
** A standard SBOM is generated and available as a pipeline artifact.
** The compiled image is pushed to the GitLab Container Registry, and Container Scanning verifies it is free of critical OS-level CVEs.
* *Tasks:*
** *Task 1:* Create CI configuration for compilation and test execution. yes
** *Task 2:* Integrate SHIP-HATS SonarQube, linting, and GitLab SAST. yes
** *Task 3:* Enable GitLab SCA (Dependency Scanning) and SBOM generation. yes
** *Task 4:* Enable GitLab Container Scanning for the registry. yes
** Task 5: Configure CD pipeline for Frontend and Backend.  yes

h3.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** [https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-deployment/-/pipelines/19374491|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-deployment/-/pipelines/19374491]
First set of the CD pipeline is ready for merge.

**Soumya Routa:** Two way CD 
From spoke to hub [https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-deployment/-/pipelines/19435992|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-deployment/-/pipelines/19435992]
from hub to spoke
[https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-deployment/-/pipelines/19438578|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-deployment/-/pipelines/19438578]

**Soumya Routa:** [https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-deployment/-/blob/main/README.md?ref_type=heads|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-deployment/-/blob/main/README.md?ref_type=heads] readme.md and [https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2288354635/App+path+to+production|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2288354635/App+path+to+production|smart-link]  confluence  file

!image-20260522-054159.png|width=397,alt="image-20260522-054159.png"!

*Synced from Jira: 2026-06-03*
