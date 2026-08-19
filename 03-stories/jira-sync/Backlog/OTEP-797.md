# OTEP-797: Add VPC Lattice observability and operational readiness

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Context With connectivity and security in place, this ticket makes failures detectable and supportable across both accounts. Cross-account services require coordinated observability since neither team has full visibility in isolation. Problem Without observability: Policy denials, target health failures, and TLS errors are invisible Incident responders cannot determine which account/layer is causing a failure No alarms exist for degraded connectivity No runbook guides cross-account troubleshooting Cost attribution and quota monitoring are absent Proposed Change Access logs: Enable service access logs on Service B (Account B) - captures request details, auth decisions, target responses Enable network access logs on the service network (Account A) - captures network-level routing Configure log retention policies appropriate to compliance requirements Verify request-ID correlation across both log streams Metrics and alarms: 
5. Create CloudWatch dashboards in both accounts showing: Request count, latency (p50/p95/p99), error rates (4xx/5xx) Target health status Auth policy allow/deny counts Create alarms for: Elevated 5xx rate or zero healthy targets Elevated auth-policy denials (potential misconfiguration or unauthorized access attempts) Latency threshold breaches Operational readiness: 
7. Review CloudTrail for Lattice management events (association changes, policy updates)
8. Write runbook covering: Policy denial diagnosis (which policy, which principal) Target health failure diagnosis Timeout and connection failure diagnosis TLS/certificate failure diagnosis Escalation path between Account A and Account B teams Apply cost allocation tags to all Lattice resources Document current quota usage and set up quota monitoring Validation: 
11. Run synthetic requests and verify they appear in access logs
12. Trigger a controlled failure (e.g., unhealthy target) and verify alarms fire
13. Walk through the runbook with both teams Acceptance Criteria Synthetic requests appear in both service and network access logs Request-ID can be correlated across Account A and Account B log streams Alarms fire within expected threshold during controlled failure test Responders can diagnose policy, target, timeout, and TLS failures using the runbook Both Account A and Account B owners acknowledge and sign off on the runbook Cost tags applied; Lattice costs attributable in billing Quota usage documented; alerts set for approaching limits References VPC Lattice monitoring overview  - available metrics, logs, and CloudTrail events Lattice access logs  - log format, fields, and destinations Lattice quotas  - current limits for services, associations, and targets Notes Depends on: Configure cross-account RAM sharing and ECS routing AND Implement VPC Lattice security controls Blocked by: logging destination decisions (S3/CloudWatch/Firehose), incident process alignment Access logs can go to CloudWatch Logs, S3, or Firehose - choose based on retention/query requirements Lattice does not remove the need for ECS-level, application-level, or network-level troubleshooting

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
