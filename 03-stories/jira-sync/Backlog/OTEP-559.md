# OTEP-559: Operations & resilience

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Establish the operational readiness to run CareerCompass in production safely — how the team deploys, rolls back, responds to incidents, and recovers from failure. This is what turns "it's deployed" into "it's operable." Background / Context  Runs on AWS ECS behind ALBs with RDS. We need a zero-downtime deploy + rollback strategy, a tested DR plan, and the human processes (runbooks, on-call, incident response) before go-live. The recent silent-failure incidents (egress-proxy  204 , stale deploy) are exactly the kind of thing runbooks + on-call should catch and resolve quickly. Acceptance Criteria Deploy & rollback:  zero-downtime deploy on ECS (rolling/blue-green or canary) with a tested, documented  rollback trigger and procedure . DR plan:  defined  RTO/RPO , backup + restore (RDS PITR)  tested , and a documented recovery procedure for loss of an AZ / the DB / a service. Runbooks:  operational runbooks for the top failure modes (service down, RDS saturation, Keycloak/auth outage, egress-proxy failure, bad deploy) — each linked from its alert. On-call & incident process:  on-call rotation, severity definitions, escalation paths, and an incident/postmortem process documented and agreed. A  go-live runbook  exists (cutover steps, smoke tests, monitoring window, comms, rollback decision criteria) and has been dry-run on stg. Tasks Define + implement the ECS deploy/rollback strategy (blue-green or canary) and document the rollback procedure. Write the DR plan (RTO/RPO), enable +  test  RDS backup/PITR restore. Author runbooks for the top failure modes, linked from alerts. Stand up on-call rotation, severity/escalation, and incident/postmortem process. Write the go-live cutover runbook and dry-run it on stg. Dependencies:  Production infrastructure (IaC); Observability (alerts link to runbooks).

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
