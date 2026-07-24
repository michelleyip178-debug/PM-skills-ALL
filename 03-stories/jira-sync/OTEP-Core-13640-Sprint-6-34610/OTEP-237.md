# OTEP-237: VPC Lattice VS TGW VS PrivateLink with NLB, what fits best

**Type:** Sub-task
**Status:** Done
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

h4. 

h4. *Key Objectives*

# *Compliance Check:* Verify with the agency's Security/Compliance if {{vpc-lattice:*}} actions are whitelisted in the current GCC 2.0 SCPs.
# *Security Analysis:* Compare IAM-based auth (Lattice) vs. Security Group/NACL (TGW/Peering) for inter-service calls.
# *IP Overlap Mitigation:* Document how Lattice handles communication

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** |{color:#ffffff}Category{color}|{color:#ffffff}VPC Peering{color}|{color:#ffffff}Transit Gateway (TGW){color}|{color:#ffffff}PrivateLink + NLB{color}|{color:#ffffff}AWS VPC Lattice (Modern){color}|
|Architectural Model|Full-mesh; direct L3 peering.|Hub-and-Spoke; centralized.|Consumer-Provider model.|Service-Mesh; logical application layer.|
|Primary Scope|Regional & Inter-regional.|Regional (Inter-region via peering).|Regional only.|Regional (ap-southeast-1).|
|Governance Context|Project-led; decentralized.|The GCC 2.0 Standard.Managed by CTS.|Shared Services (e.g., SHIP-HATS).|Zero Trust Leader. Aligns with GovTech mandates.|
|Setup Complexity|High: Manual route/CIDR management.|High: Requires TGW attachments & route updates.|Medium: Managing endpoints in every VPC.|Low: No route tables; DNS-based discovery.|
|ECS Fargate Integration|Basic; manual target group config.|Standard; requires TGW routing logic.|High isolation; used for specific egress/ingress.|Native: Services register as targets; no internal ALBs.|
|Security Mechanism|SG & NACLs (IP-based).|SGs & Centralized Firewalls.|Fine-grained Endpoint Policies.|IAM Auth Policies (L7).Identity-based auth.|
|Transitive Routing|Not supported.|Supported.|Not applicable.|Abstracted. Service-to-service focus.|
|IP Overlaps|Fails. No overlapping CIDRs allowed.|Fails. Requires complex NAT workarounds.|Supported (NAT-based).|Native Support. No IP conflicts at Layer 7.|
|Latency|Lowest (Direct path).|Slightly higher (Hub hop).|Low (NLB overhead).|Slight Proxy overhead (L7).|
|Cost Optimization|Free (within same AZ).|Pay for attachment + data processed.|High cost per hourly endpoint.|Pay-per-service. Efficient for API-heavy apps.|

*Synced from Jira: 2026-07-23*
