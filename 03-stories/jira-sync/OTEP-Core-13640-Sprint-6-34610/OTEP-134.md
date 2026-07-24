# OTEP-134: Backend repo setup

**Type:** Story
**Status:** In Progress
**Assignee:** Adrian Lo
**Story Points:** N/A

---

## Description

h2. References:

* Prototype repository: [https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-proto/-/tree/main|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-proto/-/tree/main]
** Will be split into Backend and Frontend repositories
** This is only for the Backend
* Backend prototype feedback: [https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2209284949/Feedback+from+OTEP+engineers+for+structure+and+setup|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2209284949/Feedback+from+OTEP+engineers+for+structure+and+setup|smart-link] 
** Other notes:
*** Use manual DI

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-137 | Base setup | Done |
| OTEP-195 | OpenAPI integration | Done |
| OTEP-139 | Database integration | Done |
| OTEP-140 | HTTP client | Done |
| OTEP-141 | Logging | Done |
| OTEP-142 | Dockerfile & docker-compose | Done |
| OTEP-143 | Telemetry + Metrics | Done |
| OTEP-138 | Gitlab 01 -  Governance, Security & Compliance (Repository & Branch Governance) | Done |
| OTEP-144 | Gitlab 02: Infrastructure as Code (IaC) & Cloud Integration ( configure GitLab to AWS OIDC Integration) | QA |
| OTEP-145 | Gitlab 03 - CI/CD Pipeline Core & Automation (Application Pipeline (Frontend & Backend)) | QA |
| OTEP-162 | Gitlab 17: Automate Releases and Semantic Versioning | Backlog |
| OTEP-147 | Gitlab 05 - Deployment & Environment Segregation for Service. | In Progress |
| OTEP-146 | Gitlab 04 - Infrastructure as Code (IaC) CI Pipeline | QA |
| OTEP-155 | Gitlab 10: Continuous Integration (CI) & Quality Scans | Done |
| OTEP-148 | Gitlab 06 - Documentation & Compliance (Doc-as-Code) | Backlog |
| OTEP-149 | Gitlab 07 - Observability/Monitoring & Standards Integration(DORA Metrics & Pipeline Analytics) | Backlog |
| OTEP-150 | OpenSpec integration into repository | Done |
| OTEP-153 | Gitlab 08: Configure IaC Remote State | QA |
| OTEP-154 | Gitlab 09: Configure ECS Authentication for GitLab Container Registry | QA |
| OTEP-156 | Integrate DevSecOps Tools & Quality Scanners for service repo | QA |
| OTEP-157 | Gitlab 12: Generate and Store SBOMs (Software Bill of Materials) | Backlog |
| OTEP-159 | Gitlab 14: Integrate External Application Secrets | Backlog |
| OTEP-161 | Gitlab 16: Implement Infrastructure Drift Detection | Backlog |
| OTEP-229 | Implement Secure Image Promotion Pipeline to Environment-Specific AWS ECRs | QA |
| OTEP-158 | Gitlab 13: Establish Artifact Immutability Strategy | Done |
| OTEP-160 | gitlab 15: Set Up Manual Deployment Approval Gates | QA |
| OTEP-237 | VPC Lattice VS TGW VS PrivateLink with NLB, what fits best | Backlog |
| OTEP-261 | Devsecops pipeline for WEB  | QA |
| OTEP-262 | DEVSECOPS pipeline for IAC repo. | QA |
| OTEP-270 | change the internet docker image to kaniko or other coe images.  | QA |
| OTEP-272 | Add Plan and deploy to Dev stage to the IAC pipeline.  | QA |
| OTEP-278 | Pass the coverage report artifact to the SonarQube job. | QA |
| OTEP-280 | fix sonarqube job error on web/service repo(No report of dashboard) | QA |
| OTEP-293 | Gitlab 05 - Deployment & Environment Segregation for Web. | Backlog |
| OTEP-294 | Gitlab 05 - Deployment & Environment Segregation for IAC. | Backlog |
| OTEP-306 | Verify the env is not impacted with Mini Shai-Hulud" and lock the env to strictly use the locked versions only. | QA |

---

## Latest Comments

**rama moorthy:** [~accountid:70121:9d369513-d725-4e3d-a2b8-675d4d862e3a]  [~accountid:712020:1e85df8f-f956-44c6-954e-7f6e11d1a6fc]  [~accountid:712020:5a4717ac-69a7-49e9-a198-16817e2d37a5]  are the approval reviewers for merging the feature into main branch

*Synced from Jira: 2026-07-23*
