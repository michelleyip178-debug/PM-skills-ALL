# OTEP-558: Load & performance testing

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Validate that CareerCompass meets its latency and error SLOs under realistic and peak load before go-live, find the capacity ceiling, and confirm autoscaling behaves. Run against a  prod-sized staging  environment (never prod), exercising the critical officer journeys end-to-end. Background / Context  The app has external dependencies that are common bottlenecks under load — Keycloak (login spikes), the GORM DB connection pool, the PostHog egress path (high-volume  opportunity_impression  events from OTEP-502), and the search queries ( regexp_replace / IN / EXISTS ). These need to be profiled under load and indexed/tuned as required. Results set prod sizing and act as a go-live gate. Acceptance Criteria Load model defined: peak concurrent users / RPS targets + p95/p99 thresholds for the critical journeys (login, profile load, competency edit+save, opportunity list/search/detail, apply). Scripted scenarios run for  steady-state, spike, soak (multi-hour), and stress (to breakpoint) . Known hotspots profiled under load: GORM connection pool, Keycloak token/refresh endpoint, analytics egress (impression volume), search queries — with indexes/tuning applied where needed. Autoscaling validated: ECS scales out/in and RDS handles the connection load; prod sizing derived from results. Acceptance thresholds met  (e.g. p95 within SLO at target RPS, error rate < 0.5%, no memory/connection leaks across the soak window) — recorded as the go-live gate. Tasks Define load model, SLOs, and critical journeys. Set up tooling (k6) + scripted, parameterised journey scenarios. Run steady-state / spike / soak / stress scenarios. Profile the known hotspots under load (DB pool, Keycloak, analytics egress, search) and tune/index. Validate autoscaling + derive capacity sizing. Record acceptance thresholds as the go-live gate. Dependencies:  prod-sized stg environment; Observability story (latency/error metrics needed to measure runs).

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
