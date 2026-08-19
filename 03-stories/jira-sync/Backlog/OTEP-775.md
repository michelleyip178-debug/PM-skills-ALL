# OTEP-775: Confirm VPC Lattice connectivity and ownership decision

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Context ADR-009 recommends Amazon VPC Lattice (Model B) for cross-account ECS service-to-service connectivity. Before any infrastructure work begins, the team must formally align on this decision and document resource ownership, operational responsibilities, and cost accountability across Account A and Account B. This is a decision and alignment task - no infrastructure is created here. Its output unblocks all subsequent tickets (OTEP-772, OTEP-773, OTEP-774). Problem Without a signed-off decision record, infrastructure teams in Account A and Account B cannot proceed, ownership of Lattice resources is ambiguous, incident escalation paths are undefined, and cost chargeback has no agreed owner. Proposed Change Convene a decision review with architecture, application, platform, security, and FinOps stakeholders. Produce a written decision record covering: Connectivity method - confirm VPC Lattice over TGW for the current HTTP API use case, or document the reason for a different choice Sharing model - confirm Model B (Account B owns and shares Service B; Account A owns the service network) or document the reason for Model A/C/D Resource ownership - who owns what in each account: service network, VPC association, RAM share, Lattice Service B, listener and target group, ECS targets Traffic boundary - which traffic uses Lattice vs TGW Operational owners - named individuals or teams for each account's resources, incident response, and offboarding Cost chargeback - which team absorbs Lattice service-hours, processed data, and request charges Acceptance Criteria Decision record written and stored in team docs/wiki Connectivity method confirmed with reasoning Sharing model confirmed; Model B is the default per ADR-009 Resource ownership table complete with named account and team for every Lattice resource Operational owners named for Account A and Account B Traffic boundary documented Cost chargeback owner identified Decision record acknowledged by architecture, security, and FinOps Out of Scope RAM share creation, VPC associations, security groups, IAM, auth policies, observability - all covered in OTEP-772, OTEP-773, OTEP-774. References ADR-009: adr/009-proposed-adr-vpc-lattice-cross-account-service-connectivity.md Sharing Lattice services: https://docs.aws.amazon.com/vpc-lattice/latest/ug/sharing.html Lattice pricing: https://aws.amazon.com/vpc/lattice/pricing/ Lattice quotas: https://docs.aws.amazon.com/vpc-lattice/latest/ug/quotas.html POC: https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-lattice-poc

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
