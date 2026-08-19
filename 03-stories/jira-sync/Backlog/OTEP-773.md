# OTEP-773: Implement VPC Lattice security controls

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Context The functional cross-account Lattice path exists (see prerequisite ticket). This ticket hardens it to production standard by applying least-privilege security controls at every layer: security groups, NACLs, IAM task-role permissions, SigV4 request signing, and Lattice network and service auth policies. The path from the previous ticket intentionally has no auth policy attached (open) to allow smoke-testing. This ticket replaces that open state with explicit allow/deny rules and validates that negative cases are correctly blocked. Problem Without these controls, any principal in Account A's VPC can reach Service B with no identity check, requests are unsigned, and there is no auth policy to deny wrong-role or wrong-VPC callers. Proposed Change Implement via infrastructure-as-code. Changes span both accounts. Account A - consumer IAM task role  - add  vpc-lattice-svcs:Invoke  to Service A's ECS task role, scoped to Service B's specific Lattice service ARN. No wildcards. SigV4 signing  - update Service A's HTTP client to sign outbound Lattice requests using task role credentials. Confirm signing is active before applying auth policies. Security group (client)  - allow outbound HTTPS (443) from Service A to the Lattice VPC association prefix only; deny all other Lattice-bound egress. Security group (VPC association)  - allow inbound from Service A's security group only. NACL  - if stateless NACLs are in use, ensure ephemeral port return traffic (1024-65535) is allowed on relevant subnets. Network auth policy  - attach a Lattice network auth policy to Account A's service network that permits authenticated principals from Account A's VPC and denies unauthenticated requests. Account B - provider Security group (targets)  - allow inbound to Service B's ECS tasks from the Lattice managed prefix list only; deny direct access from any other source. Service auth policy  - attach a Lattice service auth policy to Service B allowing only Service A's task role ARN and Account A; deny all other principals explicitly. TLS decision  - document and implement agreed target-hop encryption level (HTTPS to Lattice is required; Lattice-to-target hop per data classification decision). Validation Confirm negative cases: Unsigned request returns 403 Request signed with wrong IAM role returns 403 Request from outside Account A's VPC is blocked Explicitly denied principal returns 403 Health checks still pass (Lattice health checks bypass auth policies) Acceptance Criteria Service A's task role has  vpc-lattice-svcs:Invoke  scoped to Service B's ARN (no wildcards) Service A signs all outbound Lattice requests with SigV4 (confirmed via access logs or test) Service A's security group permits only outbound HTTPS to Lattice prefix; no broader egress VPC association security group permits inbound from Service A's security group only NACL return traffic allowed on Account A subnets if stateless NACLs are in use Lattice network auth policy denies unauthenticated requests on Account A's service network Service B's ECS task security group allows inbound from Lattice prefix only Lattice service auth policy restricts access to Service A's task role and Account A only Target-hop TLS decision documented and implemented Unsigned request returns 403 Request signed with wrong role returns 403 Request from wrong VPC/principal returns 403 Health checks succeed with all controls applied All controls are IaC-managed; no manual console changes Out of Scope Lattice service, listener, target group, RAM share, VPC association, ECS target registration - created in the routing ticket. Access logs, dashboards, alarms, runbook - covered in the observability ticket. Dependencies Routing and ECS plumbing ticket (functional path must exist before auth policies can be tested); identity and certificate decisions from ownership ticket. References Lattice auth policies SigV4 authenticated requests for Lattice Security groups for VPC Lattice VPC Lattice IAM actions

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
