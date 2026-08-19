# OTEP-794: Confirm VPC Lattice connectivity and ownership decision

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Context ADR-009 proposes VPC Lattice Model B (provider-owned service shared to consumer-owned service network) for cross-account ECS connectivity. Before implementation begins, stakeholders must formally confirm this approach and document ownership boundaries. Problem The ADR is in Proposed status. Implementation cannot proceed until: The connectivity method (VPC Lattice vs TGW) is confirmed The sharing model (Model B vs alternatives) is ratified Account-level ownership and operational responsibilities are assigned Any traffic that should not use Lattice (and should use TGW or another method) is identified Proposed Change Convene architecture, application, platform, security, and FinOps stakeholders Review ADR-009 alternatives and decision matrix Confirm or revise the Model B recommendation Document: Account A responsibilities (service network, VPC association, client signing, network policy, network logs) Account B responsibilities (Lattice service, target group, ECS targets, service policy, service telemetry) Operational owners for each responsibility Chargeback model for Lattice costs Traffic types that remain on TGW or other connectivity Update ADR-009 status from Proposed to Accepted (or document the alternative) Acceptance Criteria Decision records Account A and Account B responsibilities explicitly Confirms Model B or documents reason for selecting another model Names operational owners for each responsibility area Identifies any traffic excluded from Lattice (to remain on TGW or other) Chargeback/cost ownership documented ADR-009 status updated to reflect the decision References VPC Lattice sharing models  - explains RAM sharing options and constraints VPC Lattice pricing  - service-hours, data processing, and request costs Transit Gateway pricing  - for comparison Notes This is a prerequisite for all subsequent implementation tickets Dependencies: architecture, application, platform, security, and FinOps input POC results validated RAM sharing, associations, DNS, and ECS targets - use these to inform the decision

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
