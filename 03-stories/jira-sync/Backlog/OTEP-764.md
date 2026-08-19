# OTEP-764: Add Keycloak Observability, Alerts, and Runbooks

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Context Keycloak is being provisioned as a standalone production service (OTEP-759). Before prd go-live, it must have the same operational visibility as other production services: centralised logs, metrics, alerts, and runbooks for common failure modes. Scope Dashboards and alerts: ECS: desired vs running task count, task restart count, CPU/memory, deployment failures ALB: target health, 4xx/5xx error rates, latency Keycloak: health endpoint, login/token error rate, request latency, cluster size ( vendor_cluster_size ), JVM memory/CPU if exported Database: Aurora CPU, DB connections, latency, failover events, storage/backup status Runbooks to create: Keycloak task unhealthy Infinispan cluster not forming Aurora unavailable Login failures Singpass/WOG Entra ID broker failure Admin lockout / break-glass admin recovery Restore or rollback Keycloak version upgrade Acceptance Criteria [ ] Keycloak logs shipped centrally [ ] Health and metrics collection configured [ ] Alert exists for ECS task count mismatch [ ] Alert exists for ALB unhealthy targets [ ] Alert exists for high 5xx or login/token failures [ ] Alert exists for DB connection saturation or DB unavailability [ ] Cluster health verifiable from logs or  vendor_cluster_size  metric [ ] Runbook exists for common failure modes [ ] Upgrade procedure documented [ ] Break-glass admin recovery procedure documented Notes Can be done incrementally once the dev deployment exists, but must be complete before prd go-live. Depends on: standalone ECS service ticket. Epic: OTEP-759.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
