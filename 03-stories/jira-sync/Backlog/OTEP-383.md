# OTEP-383: POC for VPC Lattice

**Type:** Task
**Status:** Backlog
**Assignee:** boonsiangteh
**Story Points:** N/A

---

## Description

Purpose This POC is to quickly evaluate whether  AWS VPC Lattice  is a suitable option for enabling service-to-service communication across  ECS services running in different ECS clusters, VPCs, and AWS accounts . The goal is not to build a production-ready setup yet, but to create a small working demonstration that helps the team understand how VPC Lattice behaves in practice, what components are required, and what operational quirks or limitations we may need to consider before deciding whether to adopt it. Background Today, cross-service communication between workloads in different VPCs or AWS accounts typically requires several networking and discovery components, such as Transit Gateway, VPC peering, Route 53 private hosted zones, ALBs, target groups, security group rules, and DNS sharing/association across accounts. VPC Lattice may simplify some of this by providing an application networking layer where services can be published into a service network and consumed by clients from associated VPCs. However, we need to validate how this works specifically for our ECS-based setup and whether it fits our team’s operational model. What We Want to Learn This POC should help answer the following questions: Can ECS services in different clusters, VPCs, and AWS accounts communicate through VPC Lattice with minimal setup? What are the required VPC Lattice components? Service network VPC associations Lattice service Listener Target group ECS service targets Auth policy / resource policy, if applicable How does service discovery work from the client side? What DNS name does the client service use to call the published service? Do we need Route 53 private hosted zones, Cloud Map, or ALBs for this use case? What changes are required in the ECS service/task definition? What changes are required in application code, if any? How does security work? Which VPCs can access the service network? Which services are published? How are IAM/auth policies applied? How are security groups involved? What observability and troubleshooting options are available? CloudWatch metrics Access logs VPC Flow Logs visibility Target health Request failures What are the operational trade-offs compared to our existing approaches such as ALB, Cloud Map, Service Connect, Route 53 private hosted zones, or Transit Gateway-based routing? Scope The POC will focus on a minimal setup involving: AWS Account A
└── VPC A
    └── ECS Cluster A
        └── Client ECS Service

AWS Account B
└── VPC B
    └── ECS Cluster B
        └── Backend ECS Service

Shared / Associated through VPC Lattice
└── VPC Lattice Service Network
    └── Published backend service The client service in Account A should be able to call the backend service in Account B through VPC Lattice. Expected Outcome By the end of the POC, we should have:  A working demo showing one ECS service calling another ECS service across account/VPC boundaries using VPC Lattice.   A clear understanding of the required AWS resources and configuration steps.   Notes on any setup difficulties, limitations, confusing behavior, or operational concerns.   A comparison of whether VPC Lattice simplifies or complicates our current service-to-service communication model.   A recommendation on whether VPC Lattice is worth further evaluation for production use.  Success Criteria The POC is considered successful if:  The client ECS service can successfully call the backend ECS service through VPC Lattice.   The backend service is reachable only when it is explicitly published/associated through VPC Lattice.   Basic access control can be demonstrated or explained.   Logs/metrics are available enough for basic troubleshooting.   The team can clearly identify whether VPC Lattice reduces networking and DNS complexity compared to existing options.  Out of Scope The following are not required for this initial POC:  Production-grade Terraform modules.   Full CI/CD integration.   Full security hardening.   Full observability dashboarding.   Load testing or performance benchmarking.   Migration of existing services.   Production rollout decision.  Notes This POC is intended to surface practical implementation details and operational quirks early, before we commit to a larger design. The main focus is to understand the mechanics of VPC Lattice, how it fits with ECS, and whether it provides a cleaner model for cross-account service-to-service communication.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**boonsiangteh** (2026-06-03)
2 aws accounts were used: otep dev acount → serving as the client which will call other services (call this A) cie dev account → serving as the service to be called by service in otep (call this B)  managed to create  OTEP account vpc lattice service network in A,  create same ecs service A which creates a dummy task A shared lattice service network in otep with cie account via aws ram  create various required security groups  CIE Account created dummy task in ecs cluster  created ecs service to front this dummy task and created target group with listener on 8080 and made the ecs service the target of this target group created vpc lattice service and pointed lattice service to the target group associated lattice service to the shared service network to enable lattice connection between otep and cie account created various required security groups
