# OTEP-796: Implement VPC Lattice security controls

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Context With cross-account connectivity established, this ticket enforces least-privilege access and encryption across the Lattice path. The security model spans multiple layers: security groups, IAM/SigV4 signing, Lattice auth policies, TLS, and application authorization. Problem The connectivity path from the previous ticket is functional but not secured. Without these controls: Any principal in the associated VPC could invoke Service B Traffic may traverse unencrypted on the Lattice-to-target hop No identity-based authorization exists at the Lattice layer Security groups and NACLs may be overly permissive Proposed Change Security groups and NACLs: Configure client security group on Service A tasks (outbound to Lattice) Configure VPC association security group (controls which traffic enters Lattice) Configure target security group on Service B tasks (inbound from Lattice prefixes) Verify stateless NACL rules allow request and return traffic IAM and SigV4: 
5. Grant  vpc-lattice-svcs:Invoke  to Service A's ECS task role
6. Implement SigV4 request signing in the client (Service A)
7. Verify unsigned requests are rejected Lattice auth policies: 
8. Create network auth policy on Account A's service network (coarse allow)
9. Create service auth policy on Account B's service (fine-grained: restrict to Service A's task role ARN)
10. Verify that wrong-role, wrong-VPC, and explicitly denied requests fail Encryption: 
11. Configure HTTPS listener with appropriate certificate
12. Decide and implement target-hop encryption (HTTP vs HTTPS between Lattice and Service B)
13. Document the TLS decision and rationale Acceptance Criteria Authorized signed traffic from Service A succeeds end-to-end Unsigned requests are rejected (403) Requests from wrong task role are rejected Requests from wrong/unassociated VPC are rejected Explicitly denied principals in auth policy are rejected Return-path traffic works (stateless NACL verification) Health checks pass with security controls active Target-hop TLS decision is documented All security controls provisioned via IaC (Terraform) References Lattice auth policies  - policy structure and evaluation logic SigV4 signed requests to Lattice  - signing implementation details Security groups for Lattice  - which SGs apply at each layer Lattice managed prefix lists  - prefix list for target SG rules Notes Depends on: Configure cross-account RAM sharing and ECS routing Blocked by: identity decisions (which task role), certificate provisioning, data-classification decisions Every applicable auth policy must ALLOW - network policy AND service policy are both evaluated Application-level authorization (end-user/business logic) remains Service B's responsibility and is out of scope

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
