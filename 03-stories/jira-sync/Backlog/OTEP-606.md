# OTEP-606: Tighten Intranet ECS Service Egress SG Rules

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Context ECS services in the Intranet VPC (otep-web, otep-service, keycloak, otep-pocdex) currently have a security group egress rule ( to_tgw ) allowing TCP 443 to  0.0.0.0/0 . While routing and NACLs constrain the actual reachable destinations, the SG itself does not express the intended scope — making it impossible to reason about egress posture by inspecting the SG alone. The reverse proxy (OTEP-529) already demonstrates the tightened pattern:  enable_tgw_egress = false  + targeted  custom_tcp_egress_rules  +  s3_gateway_prefix_list_id . This ticket extends that approach to intranet services. Problem A compromised intranet ECS task with  0.0.0.0/0:443  egress can attempt connections to any HTTPS endpoint. Routing prevents most of these from succeeding, but the SG gives no signal about what's expected vs. anomalous. Security tooling (VPC Flow Logs, GuardDuty) cannot distinguish legitimate egress from exfiltration attempts at the SG layer. Proposed Change Replace the blanket  0.0.0.0/0  TCP 443 egress rule on intranet ECS services with explicit, scoped rules: S3 prefix list  — ECR image layer downloads (already supported via  s3_gateway_prefix_list_id ) VPC endpoint CIDRs  — ECR API, DKR, logs, secretsmanager, kms (already supported via  vpc_cidrs ) TGW destinations  —  10.0.0.0/8  for corporate services (CFT, shared services) instead of  0.0.0.0/0 Internal ALB CIDRs  — for OIDC issuer discovery calls Scope In scope: Decompose  to_tgw  ( 0.0.0.0/0:443 ) into targeted rules for each intranet ECS service Replace with:  10.0.0.0/8  (TGW) + S3 prefix list + VPC endpoint CIDRs + Internal ALB CIDRs Verify each service's actual egress requirements (CFT, Keycloak OIDC, PostHog, etc.) Regression test all 4 services after change Out of scope: Internet VPC services (reverse proxy, egress proxy) — already tightened NACL or route table changes NFW rule changes Acceptance Criteria [ ]  to_tgw  rule no longer uses  0.0.0.0/0  for any intranet ECS service [ ] Each service's SG egress rules explicitly list only the CIDRs/prefix lists it needs [ ]  terragrunt plan  on all 4 intranet service stacks shows only SG rule changes (no service disruption) [ ] End-to-end functionality verified: OIDC flows, CFT API calls, ECR pulls, log delivery all still work [ ] VPC Flow Logs confirm no unexpected denied traffic after apply Risks Risk Impact Mitigation Missing a required destination CIDR  Service loses connectivity to that endpoint  Audit each service's env vars and code for outbound calls before implementation; roll out one service at a time  TGW route propagation adds new CIDRs  New corporate service unreachable from ECS  Use  10.0.0.0/8  as the TGW CIDR (covers all GEN-routable ranges) rather than individual /24s  Regression on token exchange / OIDC  Auth breaks for users  Test full login flow after each service is tightened  AWS Recommended Best Practices AWS recommends using security groups as the  primary  network access control, with NACLs as a coarse secondary layer: "We recommend that you use security group rules to control traffic to your instances, and use network ACL rules as a secondary layer of defense." "Security groups act as a firewall for associated instances, controlling both inbound and outbound traffic at the instance level." The current configuration inverts this — relying on route tables and NACLs to constrain egress while the SG is permissive. This makes the SG layer non-informative for auditing and does not align with AWS's layered security model where SGs should be the tightest control. References: AWS VPC Security Best Practices AWS Security Groups vs NACLs ECS Security Best Practices — Network Security Notes The ECS service module already supports the required variables ( enable_tgw_egress ,  custom_tcp_egress_rules ,  s3_gateway_prefix_list_id ) — no module changes needed Consider using  10.0.0.0/8  instead of  0.0.0.0/0  as an intermediate step — this covers all TGW-reachable destinations without allowing arbitrary internet IPs The  to_services  rule (TCP 1024-65535 to  vpc_cidrs ) and  to_vpce  rule (TCP 443 to  vpc_cidrs ) already target VPC CIDRs specifically — only  to_tgw  is overly broad

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
