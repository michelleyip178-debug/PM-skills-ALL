# OTEP-795: Configure cross-account RAM sharing and ECS routing

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Context With the connectivity decision confirmed, this ticket establishes the functional cross-account path between Service A (Account A, consumer) and Service B (Account B, provider) using VPC Lattice Model B. Problem No cross-account service connectivity exists yet. The following must be provisioned: Account B: VPC Lattice service, HTTPS listener, target group with ECS targets, RAM share Account A: Service network, VPC association, service association (from RAM share) The POC validated these components work together. This ticket implements them in production-grade IaC with proper lifecycle management. Proposed Change Account B (provider): Create VPC Lattice service for Service B Create HTTPS listener on the service Create target group (ECS/IP type) with health check configuration Register ECS Fargate targets (validate ECS task replacement updates targets) Create RAM resource share for the Lattice service Share to Account A (via AWS Organizations or invitation acceptance) Account A (consumer): Create VPC Lattice service network Associate VPC with the service network Accept/associate the shared service from Account B's RAM share Verify service DNS resolution from Service A tasks Validate end-to-end connectivity (Service A -> Lattice -> Service B) Offboarding test: 
6. Remove the RAM share or service association and verify access is revoked Acceptance Criteria Service A resolves the Lattice-generated service DNS name Service A reaches a healthy Service B target via the Lattice path Association ownership matches Model B (B owns service, A owns network) ECS task replacement (deploy/scale) correctly updates Lattice targets Offboarding test: removing association or RAM share revokes connectivity All resources provisioned via IaC (Terraform) Health check configuration validated (target group reports healthy) References VPC Lattice getting started  - end-to-end setup walkthrough Creating a Lattice service  - service, listener, and target group configuration RAM sharing for Lattice  - sharing rules and association behaviour ECS target registration  - ECS/IP target type registration Notes Depends on: Confirm VPC Lattice connectivity and ownership decision Blocked by: existing IaC foundation, ECS deployment pipeline, application health endpoint Removing a RAM share does NOT automatically remove existing associations - offboarding must explicitly delete associations Provider VPC does not need a service-network association just to receive Lattice traffic

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
