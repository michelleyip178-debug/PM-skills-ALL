# OTEP-138: Gitlab 01 -  Governance, Security & Compliance (Repository & Branch Governance)

**Type:** Sub-task
**Status:** Done
**Assignee:** Adrian Lo
**Story Points:** N/A

---

## Description

* *Goal:* Create the initial repositories for App and IaC in SHIP-HATS and establish secure baseline branch policies.
* *IM8 Reform Clause:* SC-1 (System and Communications Protection), SD-2 (Source Code Management).
* *Specific Acceptance Criteria:*
** Attempting a direct git push or git push --force from a local machine to the main branch results in a rejection error from GitLab.
** Creating a Merge Request (MR) against main displays a required approval rule (minimum 1 eligible peer reviewer). The MR cannot be merged until approved.
** Committing a plaintext secret (e.g., a dummy AWS access key) to a local branch and attempting to push it is immediately blocked by GitLab Push Rules.
** _(Optional L2)_ Attempting to push a commit without a verified GPG/SSH signature is rejected by GitLab.
* *Tasks:*
** *Task 1 (Level 1) [sc-1]:* Host App and IaC codebases in central SHIP-HATS repositories. ✅
** *Task 2 (Level 1) [sd-2]:* Configure GitLab Protected Branches for the default branch. ✅
** *Task 3 (Level 1) [sc-3]:* Enforce Merge Request (MR) Approvals. ✅
** *Task 4 (Level 1) [sd-1]:* Enable GitLab push rules to reject secrets. ✅
** *Task 5 (Level 2) [sc-2] [Optional]:* Enable push rules to reject unsigned commits. ✅
** *Task 6 (Level 2) [sc-9] [Optional]:* Configure repository visibility for InnerSourcing. ✅

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** * *OTEP-138:* Repository & Branch Governance [~accountid:5d5b77777b9a8f0cf55f9d1d] [~accountid:70121:9d369513-d725-4e3d-a2b8-675d4d862e3a] 
* *OTEP-155:* CI & Quality Scans [~accountid:5d5b77777b9a8f0cf55f9d1d]  [~accountid:712020:4c101a3f-bd57-44f2-90a8-f36ea3d3ddb4] 
* *OTEP-156:* Integrate DevSecOps Tools & Quality Scanners [~accountid:5d5b77777b9a8f0cf55f9d1d] 
* *OTEP-159:* Integrate External Application Secrets [~accountid:712020:4c101a3f-bd57-44f2-90a8-f36ea3d3ddb4] 
* *OTEP-157:* Generate and Store SBOMs (Software Bill of Materials)





DevSecOps controls implementation will be handle by [~accountid:5d5b77777b9a8f0cf55f9d1d] 

Other than that will be handle by [~accountid:712020:4c101a3f-bd57-44f2-90a8-f36ea3d3ddb4] : Build pipeline, testing pipeline, release and deployment pipeline,  etc

**Fanxu Wang:** [~accountid:70121:9d369513-d725-4e3d-a2b8-675d4d862e3a] We dont have permisison to create groups and repo settings

**Fanxu Wang:** verification will be [~accountid:5d5b77777b9a8f0cf55f9d1d]

*Synced from Jira: 2026-07-23*
