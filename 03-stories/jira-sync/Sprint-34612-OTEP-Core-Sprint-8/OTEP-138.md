# OTEP-138: Gitlab 01 -  Governance, Security & Compliance (Repository & Branch Governance)

**Status:** Done
**Assignee:** Adrian Lo
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Goal:  Create the initial repositories for App and IaC in SHIP-HATS and establish secure baseline branch policies. IM8 Reform Clause:  SC-1 (System and Communications Protection), SD-2 (Source Code Management). Specific Acceptance Criteria: Attempting a direct git push or git push --force from a local machine to the main branch results in a rejection error from GitLab. Creating a Merge Request (MR) against main displays a required approval rule (minimum 1 eligible peer reviewer). The MR cannot be merged until approved. Committing a plaintext secret (e.g., a dummy AWS access key) to a local branch and attempting to push it is immediately blocked by GitLab Push Rules. (Optional L2)  Attempting to push a commit without a verified GPG/SSH signature is rejected by GitLab. Tasks: Task 1 (Level 1) [sc-1]:  Host App and IaC codebases in central SHIP-HATS repositories. ✅ Task 2 (Level 1) [sd-2]:  Configure GitLab Protected Branches for the default branch. ✅ Task 3 (Level 1) [sc-3]:  Enforce Merge Request (MR) Approvals. ✅ Task 4 (Level 1) [sd-1]:  Enable GitLab push rules to reject secrets. ✅ Task 5 (Level 2) [sc-2] [Optional]:  Enable push rules to reject unsigned commits. ✅ Task 6 (Level 2) [sc-9] [Optional]:  Configure repository visibility for InnerSourcing. ✅

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang** (2026-05-04)
verification will be

---

**Fanxu Wang** (2026-05-04)
We dont have permisison to create groups and repo settings

---

**Soumya Routa** (2026-04-28)
OTEP-138:  Repository & Branch Governance        OTEP-155:  CI & Quality Scans         OTEP-156:  Integrate DevSecOps Tools & Quality Scanners     OTEP-159:  Integrate External Application Secrets     OTEP-157:  Generate and Store SBOMs (Software Bill of Materials)   DevSecOps controls implementation will be handle by     Other than that will be handle by    : Build pipeline, testing pipeline, release and deployment pipeline,  etc

---
*Synced from Jira: 2026-09-07*
