# OTEP-774: Add VPC Lattice observability and operational readiness

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Context The cross-account Lattice path is functional and security controls are applied (see prerequisite tickets). This ticket makes the path production-operable: failures must be detectable from both accounts, diagnosable without console access, and the escalation process must be agreed before go-live. Problem Without observability and a runbook, failures in Account A (auth policy, VPC association) and Account B (target health, service policy, TLS) are invisible to the other account's team. Incident responders cannot distinguish between a Lattice policy denial, target health failure, TLS error, or quota breach. There is no agreed escalation path when the failing resource is owned by a different team. Proposed Change Account A - service network logs and metrics Network access logs  - enable access logging on Account A's service network; send to CloudWatch Logs with 90-day retention. Log group:  /aws/vpc-lattice/network/<service-network-name> CloudWatch alarms  - create alarms on  4XXCount  (auth policy denials or client errors),  5XXCount  (target or Lattice errors), and  RequestCount  dropping to zero during business hours Request-ID correlation  - document how to join Account A network logs with Account B service logs using  x-amzn-lattice-request-id Account B - service logs and target health Service access logs  - enable access logging on Lattice Service B; send to CloudWatch Logs with 90-day retention Target health alarm  - CloudWatch alarm on  HealthyHostCount  for Service B's target group; alarm when healthy targets fall below threshold CloudWatch alarms  -  4XXCount  and  5XXCount  at the service level for independent visibility Shared CloudTrail review  - confirm existing trails in both accounts capture  vpc-lattice  management events; document findings Cost and quota tags  - confirm all Lattice resources carry cost-allocation tags from the ownership decision record; add any missing tags Quota check  - document current utilisation vs limits for service networks, VPC associations, services, and targets per Region; flag any dimension above 70% Runbook  - write and publish a runbook covering: How to diagnose a 4XX (auth policy? wrong role? missing signing?) How to diagnose a 5XX (target unhealthy? TLS failure? all targets down?) How to check target health in Account B's target group How to correlate a request across accounts using  x-amzn-lattice-request-id Offboarding steps with access revocation verification Escalation contacts for Account A and Account B Runbook sign-off  - both Account A and Account B operational owners must acknowledge the runbook before go-live Synthetic test  - scheduled synthetic request from Account A to Service B's Lattice DNS; confirm it appears in both account access log groups Acceptance Criteria Network access logs enabled on Account A's service network; log group with retention set Service access logs enabled on Account B's Lattice service; log group with retention set Synthetic test request appears in both Account A network log and Account B service log x-amzn-lattice-request-id  correlation documented and demonstrated CloudWatch alarms exist in Account A for 4XX, 5XX, and zero-request conditions CloudWatch alarm exists in Account B for unhealthy target count CloudTrail management events for  vpc-lattice  confirmed active in both accounts All Lattice resources carry cost-allocation tags per decision record Quota utilisation documented; no dimension above 70% of limit Runbook published covering four failure modes: policy denial, target health, TLS, quota Account A and Account B operational owners have acknowledged the runbook Controlled alarm test: simulate target health failure and confirm alarm fires Out of Scope Lattice service, listener, target group, RAM share, VPC association - created in the routing ticket. IAM, auth policies, security groups, NACLs, TLS - enforced in the security controls ticket. Dependencies Routing and ECS plumbing ticket (log sources must exist); security controls ticket (auth events must be present for full coverage); logging destination decisions and incident escalation process from ownership decision record. References VPC Lattice monitoring overview Lattice CloudWatch metrics Lattice access logs Lattice quotas

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
