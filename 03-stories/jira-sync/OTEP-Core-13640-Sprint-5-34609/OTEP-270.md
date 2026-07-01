# OTEP-270: change the internet docker image to kaniko or other coe images. 

**Type:** Sub-task
**Status:** QA
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

*Description*
Update CI pipelines in 3 repositories to remove externally sourced Docker images and replace them with:

* Kaniko for container builds
* Internal/COE-approved base images for all CI jobs

This change is required to:

* improve supply chain security
* reduce dependency on public registries
* align with platform governance and compliance standards
* to avoid using DIND and root

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** For web fixed [https://sgtechstack.atlassian.net/browse/OTEP-262?search_id=4042b18b-979a-428a-b402-32ca8d165661|https://sgtechstack.atlassian.net/browse/OTEP-262?search_id=4042b18b-979a-428a-b402-32ca8d165661]  and same for Services. 

wiki [https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-web/-/wikis/OTEP-WEB-ci-pipeline-design|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-web/-/wikis/OTEP-WEB-ci-pipeline-design]



!image-20260514-063711.png|width=465,alt="image-20260514-063711.png"!

*Synced from Jira: 2026-07-01*
