# OTEP-998: Sequential promotion pipeline with mandatory peer approval: qa then prd

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Background Today, every merge to  main  in cie-backend opens promotion MRs for qa and preprd  simultaneously  via  open-promotion-mr.sh . Neither MR requires a specific approver - qa has a broad 4-approver pool and preprd is self-serve. The desired model is: Sequential gates  - the prd promotion MR only opens after the qa promotion MR is merged (i.e. qa is confirmed deployed), not at the same time Mandatory peer approval  - both the qa and prd promotion MRs must be approved by someone other than the author before they can be merged; a specific approver (e.g. Victor) should be a required reviewer This gives a clear, auditable promotion chain:  main merge -> qa deploy -> prd deploy , with a human gate at each step. Current flow main merge (cie-backend)
  └─> open-promotion-mr.sh
        ├─> config-repo MR: qa    (opens immediately)
        └─> config-repo MR: preprd (opens immediately, in parallel) PROMOTE_ENVS: "qa preprd"  in  .gitlab-ci.yml  drives this. Target flow main merge (cie-backend)
  └─> open-promotion-mr.sh
        └─> config-repo MR: qa  (opens immediately, requires peer approval)
              └─> qa MR merges
                    └─> config-repo pipeline job: open-prd-promotion-mr
                          └─> config-repo MR: prd  (requires peer approval) Technical approach Step 1 - Mandatory peer approval on the qa MR When  open-promotion-mr.sh  creates the MR via the GitLab API (already using  glab / curl ), extend it to also set: approvals_required: 1 prevent_author_approval: true A named approval rule with the required reviewer(s) (e.g.  victor  by user ID, or a GitLab group) This can be done via  POST /projects/:id/merge_requests/:mr_iid/approval_rules  after the MR is opened. Step 2 - Trigger prd MR from config-repo on qa merge Add a CI job in config-repo that runs when the qa branch is updated (i.e. when the qa promotion MR merges): open-prd-promotion-mr:
  rules:
    - if: $CI_COMMIT_BRANCH == "main" && $CI_PIPELINE_SOURCE == "push"
      changes:
        - apps/cie-backend/qa/**
  trigger:
    project: <cie-backend project path>
    strategy: depend Or alternatively: config-repo job runs  open-promotion-mr.sh prd  directly (the script already knows how to open one env at a time). The config-repo job needs a pipeline trigger token or project access token scoped to cie-backend to call back. The simpler path is to keep all MR-opening logic in  open-promotion-mr.sh  and call it from config-repo's pipeline. Step 3 - Mandatory peer approval on the prd MR Same as step 1 - the prd MR is created with  approvals_required: 1 ,  prevent_author_approval: true , and named approver(s). On controlling who triggers a pipeline GitLab supports two mechanisms: MR approval rules  (used here) - the deploy only runs when someone with the right role approves and merges. This is the right gate for this workflow - the approver is signing off on what gets deployed, not just that the button was clicked. Protected environments  (GitLab EE) - a job targeting a protected environment requires specific people to approve in the pipeline UI before the job runs. An additional option if deeper runtime control is needed. Design decision: sequential vs parallel Sequential promotion is the right model here because: prd should only receive an image that has been confirmed working in qa It prevents a scenario where prd is promoted before qa has even been reviewed The cost is a small delay (one qa deploy cycle) which is appropriate for production The preprd environment (used for integration/load testing) can remain as-is or be folded into this chain later. Acceptance criteria A merge to  main  opens a qa promotion MR with  approvals_required: 1 ,  prevent_author_approval: true , and a named required reviewer The prd promotion MR does  not  open until the qa promotion MR is merged The prd promotion MR also has  approvals_required: 1 ,  prevent_author_approval: true , and a named required reviewer The named required reviewer(s) are configurable (not hardcoded - read from a variable or config file) The promotion chain is documented in  ci/open-promotion-mr.sh  header comment

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
