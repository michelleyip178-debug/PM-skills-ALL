# OTEP-143: Telemetry + Metrics

**Type:** Sub-task
**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** N/A

---

## Description

*I want* to integrate OpenTelemetry for distributed tracing and custom metrics, *So that* we can monitor service health ("Golden Signals") and trace cross-service requests in our ECS environment.

|*Requirement*|*Technical Specification*|*Checked*|
|*OTel Standards*|Use {{go.opentelemetry.io/otel}}.
Boot strap this at startup| |
|*Tracing*|Instrument incoming HTTP requests (middleware) and database queries.| |
|*Metrics*|Expose standard metrics (Latency, Error Rate, Request Count) via OTLP.| |
|*Context Propagation*|Ensure full support for W3C TraceContext propagation across HTTP calls.| |
|*Exporter*|Configure to export via OTLP (gRPC/HTTP) to an external collector (sidecar pattern).| |

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-23*
