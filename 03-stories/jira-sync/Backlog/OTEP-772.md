# OTEP-772: Configure VPC Lattice cross-account sharing and ECS routing

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Context Following the ownership and connectivity decision (prerequisite task), this ticket establishes the functional cross-account data path using Amazon VPC Lattice Model B. Account B creates the Lattice service, listener, and target group pointing at its ECS Fargate tasks, then shares the service to Account A via AWS RAM. Account A creates the service network and associates the shared service and its VPC. The goal is a working end-to-end path with health checks passing. Security controls (IAM, auth policies, security groups, NACLs, TLS enforcement) are applied in the security controls ticket. Problem No cross-account Lattice path exists today. Without this plumbing, the security and observability tickets have nothing to act on, and Service A cannot reach Service B. Proposed Change Implement via infrastructure-as-code (Terraform). Work is split by account. Account B - provider Create a VPC Lattice service for Service B Add an HTTPS listener on port 443 (HTTP on 80 acceptable for initial smoke test; HTTPS required before ticket is closed) Create an IP target group pointing at Service B's ECS task IPs Register ECS tasks as targets; confirm health check path and response code with Service B team Create an AWS RAM share for the Lattice service and share to Account A (by account ID or AWS Organizations principal) Account A - consumer Accept the RAM share invitation (or auto-accept via AWS Organizations if applicable) Create a VPC Lattice service network in Account A Associate the shared Service B with Account A's service network Associate Account A's VPC with the service network Verification From an Account A task, resolve the Lattice-generated service DNS name and confirm it returns an IP Send a test HTTPS request; confirm 200 from Service B Replace an ECS task in Account B; confirm new task IP is registered and old IP deregistered Offboarding test: remove RAM share or association in Account A and verify access is revoked Acceptance Criteria VPC Lattice service, listener, and target group exist in Account B (IaC-managed) RAM share created and accepted in Account A Service network and both associations (service + VPC) exist in Account A (IaC-managed) Service B's Lattice DNS name resolves from Account A Test request from Account A reaches a healthy Service B target and returns 200 ECS task replacement in Account B correctly updates target registration Offboarding test confirms access is revoked when association is removed All resources tagged with owner and cost-allocation tags per decision record Out of Scope Security groups, NACLs, IAM task-role permissions, SigV4 signing, Lattice auth policies - all covered in the security controls ticket. The functional path created here intentionally has no auth policy attached to allow smoke-testing before hardening. Access logs, dashboards, alarms, runbook - covered in the observability ticket. Dependencies Ownership decision ticket must be complete (confirm Model B, account IDs, named owners) before creating any resources. References Sharing Lattice services and service networks VPC Lattice target groups VPC Lattice listeners VPC associations POC: https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-lattice-poc

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
