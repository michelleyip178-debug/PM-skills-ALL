# OTEP-702: Deploy jobs base new task definitions on family-latest revision; stale terragrunt env list can silently wipe live env vars

**Type:** Bug
**Status:** Backlog
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Context The orchestrator deploy jobs (.deploy-ecs-base and .run-data-tasks-base in otep-deployment/.gitlab-ci.yml) fetch their base task definition with: aws ecs describe-task-definition --task-definition "$ECS_TASK_FAMILY" When only the family name is passed, AWS returns the newest registered revision, which is not necessarily the revision the service is running. The job then swaps the image and ships that revision, including its entire environment and secrets block. What is already handled use_current_image (2a664fc) fixed the image half of this problem: a routine terragrunt apply no longer registers a revision with a stale image. Good fix. The remaining gap Environment variables still render entirely from the environment_variables list in terragrunt.hcl. If an apply runs while that file is behind the live task definition, Terraform registers a revision that is missing the newer variables. Because of ignore_changes = [task_definition], the apply does not repoint the service, so nothing visibly changes and nobody is alerted. The stale revision sits as family-latest until the next pipeline deploy adopts it as the base and silently removes those variables from the running service. Concrete example from 9 July 11:57, rev 358 of ecs-td-psd-otep-dev-otep-service was registered manually to add HTTP_PROXY, HTTPS_PROXY and NO_PROXY (env count 41 to 44) during the egress proxy fix. 12:48, the next pipeline deploy (revs 360/361) inherited the three variables only because family-latest happened to be rev 359 at that moment. Until the IaC change landed, terragrunt.hcl still carried the 41-variable list. Any terragrunt apply on the otep-service stack in that window would have registered a 41-variable revision as family-latest. The next pipeline deploy would then have removed the proxy fix from the running service, and the breakage would have surfaced under whoever merged next, hours after the apply. This mechanism is the most likely cause of the past cases where CFT_* and other variables disappeared after unrelated deployments. Proposed fix In .deploy-ecs-base and .run-data-tasks-base, resolve the base task definition from the revision the service is actually running, instead of family-latest: BASE_TD_ARN=$(aws ecs describe-services --cluster "$ECS_CLUSTER" --services "$ECS_SERVICE" \
  --query "services[0].taskDefinition" --output text)
aws ecs describe-task-definition --task-definition "$BASE_TD_ARN" ... A stale registration then has no effect unless someone deliberately deploys it. Acceptance criteria Deploy and data jobs base the new revision on the revision the service is currently running. A terragrunt apply or manual registration with a different env list does not change the env set of subsequent pipeline deploys. Convention documented: env var changes go into terragrunt.hcl and are rolled out by triggering a deploy after the apply.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
