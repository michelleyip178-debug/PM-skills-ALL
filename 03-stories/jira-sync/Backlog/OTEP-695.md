# OTEP-695: Harden migrate/seed one-off ECS tasks in otep-deployment pipeline (leak + silent-skip risk)

**Type:** Task
**Status:** Backlog
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

The dev-data-service job runs /migrate and /seed as one-off Fargate tasks (aws ecs run-task + wait tasks-stopped) and gates every otep-service deploy. It has no failure-path handling. Risk If the task never stops (e.g. command override ignored and the server boots, or goose blocks on a lock), the wait times out and the task leaks — runs indefinitely with old code and stale secrets. Happened twice: tasks 1609f0da (Jun 30) and 7fb07f7e (Jul 1), pipelines 20729328 / 20745969, still running 10 days later. If the override is silently ignored, that deploy's migrations never ran — and since goose (OTEP-592) is the only migration path (nothing runs at service startup), this silently ships new code on an old schema. Fix On wait failure/timeout: aws ecs stop-task on the started ARN before the job exits. Assert the container ran /migrate (not the server) and exited 0; fail the deploy otherwise. One-off: stop the two orphaned tasks in ecs-psd-otep-dev-app.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
