# OTEP-134: Backend repo setup

**Status:** In Progress
**Assignee:** Adrian Lo
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

References: Prototype repository:  https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-proto/-/tree/main Will be split into Backend and Frontend repositories This is only for the Backend Backend prototype feedback:     Other notes: Use manual DI

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
| OTEP-144 | Gitlab 02: Infrastructure as Code (IaC) & Cloud Integration ( configure GitLab to AWS OIDC Integration) | Done |
| OTEP-145 | Gitlab 03 - CI/CD Pipeline Core & Automation (Application Pipeline (Frontend & Backend)) | Done |
| OTEP-162 | Gitlab 17: Automate Releases and Semantic Versioning | Backlog |
| OTEP-147 | Gitlab 05 - Deployment & Environment Segregation for Service. | Done |
| OTEP-146 | Gitlab 04 - Infrastructure as Code (IaC) CI Pipeline | Done |
| OTEP-160 | gitlab 15: Set Up Manual Deployment Approval Gates | Done |
| OTEP-159 | Gitlab 14: Integrate External Application Secrets | Done |
| OTEP-155 | Gitlab 10: Continuous Integration (CI) & Quality Scans | Done |
| OTEP-148 | Gitlab 06 - Documentation & Compliance (Doc-as-Code) | Backlog |
| OTEP-149 | Gitlab 07 - Observability/Monitoring & Standards Integration(DORA Metrics & Pipeline Analytics) | Backlog |
| OTEP-150 | OpenSpec integration into repository | Done |
| OTEP-153 | Gitlab 08: Configure IaC Remote State | Done |
| OTEP-154 | Gitlab 09: Configure ECS Authentication for GitLab Container Registry | Done |
| OTEP-156 | Integrate DevSecOps Tools & Quality Scanners for service repo | Done |
| OTEP-157 | Gitlab 12: Generate and Store SBOMs (Software Bill of Materials) | Backlog |
| OTEP-161 | Gitlab 16: Implement Infrastructure Drift Detection | QA |
| OTEP-229 | Implement Secure Image Promotion Pipeline to Environment-Specific AWS ECRs | Done |
| OTEP-158 | Gitlab 13: Establish Artifact Immutability Strategy | Done |
| OTEP-237 | VPC Lattice VS TGW VS PrivateLink with NLB, what fits best | Done |
| OTEP-261 | Devsecops pipeline for WEB  | Done |
| OTEP-262 | DEVSECOPS pipeline for IAC repo. | Done |
| OTEP-270 | change the internet docker image to kaniko or other coe images.  | Done |
| OTEP-272 | Add Plan and deploy to Dev stage to the IAC pipeline.  | Done |
| OTEP-278 | Pass the coverage report artifact to the SonarQube job. | Done |
| OTEP-280 | fix sonarqube job error on web/service repo(No report of dashboard) | Done |
| OTEP-293 | Gitlab 05 - Deployment & Environment Segregation for Web. | Backlog |
| OTEP-294 | Gitlab 05 - Deployment & Environment Segregation for IAC. | Backlog |
| OTEP-306 | Verify the env is not impacted with Mini Shai-Hulud" and lock the env to strictly use the locked versions only. | Done |

---

## Latest Comments

**rama moorthy** (2026-04-27)
are the approval reviewers for merging the feature into main branch

---
*Synced from Jira: 2026-08-20*
