# OTEP-983: Wire prd environment into the CIE promotion pipeline (config-repo + cie-backend)

**Status:** Done
**Assignee:** Brian Noel Kesuma
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 7 (35010)

---

## Description

The CIE backend pipeline currently promotes images to two environments after every merge to  main : qa  - MR opened in config-repo, owner-gated (1 of 4 approvers required) preprd  - MR opened in config-repo, self-serve prd is not in the promotion chain at all. The Terraform code for prd ECS services and ECR repos was written in OTEP-523 (merged 2026-06-23), but two critical pieces were explicitly excluded and do not exist in the repo today: live/prd/cicd/gitlab-deployer/  -  not written  (excluded from OTEP-523, never landed) live/prd/data/opensearch/  -  not written  (prd has no OpenSearch stack) Without the deployer role, config-repo CI has no IAM role to assume for prd. Without OpenSearch, the prd task-definition cannot carry a valid  OPENSEARCH_HOST  env var - any task-def copied from preprd would carry preprd's OpenSearch endpoint, which is wrong. The prd account is  774667857284 . Verified state (as of 2026-07-30) Layer Status prd ECS service + ECR Terraform code (OTEP-523) Written, merged - not yet applied live/prd/cicd/gitlab-deployer/  Terraform Does not exist - needs to be written live/prd/data/opensearch/  Terraform Does not exist - needs to be written Eval platform port to prd Not done - OTEP-825 explicitly excluded prd config-repo  apps/cie-backend/prd/ Does not exist cie-backend  PROMOTE_ENVS "qa preprd"  only Prerequisite ordering (IAC work, tracked in linked IAC ticket) Before any CI wiring can happen, the following must be done in the IAC repo and applied to AWS, in order: Write and apply  live/prd/data/opensearch/intelligence-search/cluster/  and  live/prd/data/opensearch/intelligence-search/index/competency-bank-v1/  - without this there is no  OPENSEARCH_HOST  value for the task-def Write and apply  live/prd/compute/services/backend-service/  IAM updates (OpenSearch FGAC reader mapping for the task role) Write and apply  live/prd/cicd/gitlab-deployer/  - the OIDC IAM role config-repo CI assumes to deploy Run bank ingest against prd OpenSearch to populate the competency bank index Once those are applied, the IAC team provides: prd ECR repo URLs,  gitlab-deployer  role ARN, prd OpenSearch host. CI wiring work config-repo changes Create  apps/cie-backend/prd/task-definition.json  - copy preprd's, substitute prd account ID  774667857284 , prd role ARNs, prd ECR URL, and prd  OPENSEARCH_HOST Create  apps/cie-backend/prd/ci-variables.yml  - prd ECR URLs, prd  gitlab-deployer  role ARN Add  deploy:prd  job to config-repo  .gitlab-ci.yml  (same  .deploy-base  pattern as the existing  deploy:preprd  job) CODEOWNERS - prd falls under the default  /apps/  owner-gated rule; no change needed cie-backend changes Add  prd  to  PROMOTE_ENVS: "qa preprd prd"  in  .gitlab-ci.yml Add  prd)  ECR case to  ecr_for_env()  in  ci/open-promotion-mr.sh  using the prd account ECR URL Note on sequential vs parallel promotion The current design (one MR per env, all openable independently, owner approval gates prd) is the right approach for a lean team. Sequential promotion - blocking preprd MR until qa is healthy, blocking prd MR until preprd is healthy - adds polling complexity with no concrete benefit given the team size. Owner approval on prd is the sufficient human gate. Acceptance criteria A merge to  cie-backend  main opens 3 promotion MRs: qa, preprd, prd Merging the prd MR in config-repo triggers  deploy:prd  which rolls the new image onto the prd ECS service The prd MR requires owner approval before it can be merged prd  ecr_for_env  returns the correct prd account ECR URL The prd task-def carries the correct prd  OPENSEARCH_HOST  (not preprd's endpoint)  E2E verification: IaC applied - apply:prd provisioned ECS cluster, OpenSearch cluster, eval-store-migrator, gitlab-deployer, opensearch-migrator (intelligence-iac pipeline, 2026-07-31) config-repo deploy:prd triggered - merging apps/cie-backend/prd/task-definition.json to main fired the job. OIDC assumed gitlab-cie-deployer (774667857284), image copied from GitLab registry to prd ECR, task-def :2 registered, ECS service rolled. (config-repo pipeline, 2026-08-05) Promotion MR created - cie-backend merge to main opened a prd promotion MR in config-repo with image tag <sha>

---

## Subtasks

_No subtasks._

---

## Latest Comments

**boonsiangteh** (2026-08-05)
Brian N KESUMA  mentioned this issue in  a commit  of  WOG / PSD / pdo / intelligence / apps / CIE backend  on branch  main : Merge branch 'OTEP-983' into 'main'

---

**boonsiangteh** (2026-08-05)
Benjamin AW  mentioned this issue in  a commit  of  WOG / PSD / pdo / intelligence / config-repo  on branch  main : Merge branch 'OTEP-983' into 'main'

---

**boonsiangteh** (2026-08-04)
Brian N KESUMA  mentioned this issue in  a merge request  of  WOG / PSD / pdo / intelligence / apps / CIE backend  on branch  OTEP-983 : ci: add prd to promotion pipeline

---
*Synced from Jira: 2026-08-31*
