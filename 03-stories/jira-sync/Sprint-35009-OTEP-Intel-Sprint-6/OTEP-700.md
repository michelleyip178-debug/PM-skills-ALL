# OTEP-700: Enable the OTEP-624 regression gate: align eval-gate to the in-VPC RunTask design across cie-backend, intelligence-iac, and config-repo

**Status:** Done
**Assignee:** Benjamin Aw
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 6 (35009)

---

## Description

Title:  Enable the OTEP-624 regression gate: align eval-gate to the in-VPC RunTask design across cie-backend, intelligence-iac, and config-repo Description The CI regression gate (OTEP-624) is code-complete but dark:  EVAL_GATE_ENABLED  is not set in config-repo (verified 2026-07-13). A cross-repo audit found the two halves were built to opposite designs and three defects must be closed before the flag can flip. Proposed ADRs are drafted in each repo: cie-backend  docs/adr/0001 , intelligence-iac  docs/adr/0004 , config-repo  docs/adr/0001 . Why it doesn't work today:  cie-backend's  ci/eval-gate.sh  (OTEP-649) runs the candidate eval inside the GitLab runner with a data-plane role — but OpenSearch and Aurora are VPC-only, unreachable from GitLab Dedicated runners. intelligence-iac's ADR 0003 (OTEP-648) already rejected this and built a control-plane-only role ( gitlab-cie-eval-runner ) for running the eval as an in-VPC  cie-eval  ECS task. Additionally, the  cie-eval  task def runs  python eval/run_eval.py  from the backend-service image, but  inference.Dockerfile  doesn't copy  eval/  — the in-VPC path would also fail today. Scope cie-backend  — Ship  eval/  in the inference image (~2.4 MB). Rewrite  ci/eval-gate.sh  and  ci/promote-champion.sh  as control-plane orchestration: assume eval-runner role → push candidate image to ECR → register candidate  cie-eval  revision → RunTask  run_eval.py --store-mode ci  then  compare.py  via containerOverrides → verdict from exit code, diff from  /ecs/cie-eval  logs; MR-note posting stays in the runner;  cie-evalstore-variant promote  also runs in-VPC. Remove the data-plane CI variable expectations. intelligence-iac  — Split the  ecr/backend-service  lifecycle policy so candidate-tagged images ( candidate-<sha> ) expire aggressively and cannot evict the release images qa/preprd promotion pins depend on (repo keeps last 10 only). Flip ADR 0003 to Accepted once cie-backend conforms. config-repo  — Add to  apps/cie-backend/dev/ci-variables.yml :  EVAL_GATE_ENABLED: "true"  plus control-plane identifiers only (eval-runner role ARN, task family, log group). Explicitly no data-plane variables and no secrets ( EVAL_GATE_TOKEN  stays a masked project variable).

---

## Subtasks

_No subtasks._

---

## Latest Comments

**boonsiangteh** (2026-07-21)
Benjamin AW  mentioned this issue in  a merge request  of  WOG / PSD / pdo / intelligence / config-repo  on branch  OTEP-756 : [Ben]   cie-backend dev ci-variables: add ECS_SERVICE_FEEDBACK / ECS_TASK_DEFINITION_FEEDBACK

---
*Synced from Jira: 2026-07-28*
