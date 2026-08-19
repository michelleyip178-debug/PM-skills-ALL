# OTEP-732: Suppress AWS-1081 — Network Firewall Policy Has No Associated Rule Groups (Platform Coordination Required)

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Summary Suppress Cloudscape finding AWS-1081 for the Network Firewall policy  networking-psd-otep-dev-intranet-nfw-policy  (b179cc86-31d2-4ad5-91ae-9023d3912b6b). The NFW policy was provisioned as part of the platform networking baseline and associating rule groups requires coordinated planning with the platform team. Type Suppression Epic Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev) Labels cloud-va ,  cis-benchmark ,  compliance ,  suppression IM8 Clause NS-5  Context The Network Firewall policy  networking-psd-otep-dev-intranet-nfw-policy  was provisioned as part of the networking module implementing the VPC contract for the OTEP dev environment.  Live audit (2026-07-14) confirmed this is tagged  ManagedBy: terragrunt  and is app-team owned. The policy currently acts as a placeholder — it is actively associated with a deployed firewall instance but contains zero stateless and zero stateful rule groups, meaning all traffic passes through uninspected. The default actions forward all traffic to the stateful engine ( aws:forward_to_sfe ) which has no rules — effectively a pass-through. Adding rule groups requires coordination with the platform team who owns the Transit Gateway routing that feeds traffic into this firewall. Problem Statement Cloudscape is flagging AWS-1081 (Network Firewall policy should be associated with rule groups) as NON_COMPLIANT for the NFW policy. The finding is technically accurate — no rule groups are currently associated — but resolving this is not a standalone app-team fix. It requires joint planning with the platform team to define the rule group structure, inspection routing, and TGW integration before any rule groups can be safely applied. Justification for Suppression The NFW policy was provisioned as part of the networking contract baseline, not as a standalone app-team resource. Associating rule groups without platform coordination risks disrupting TGW routing and NFW inspection flows. Current network security posture for dev is maintained via security groups and NACLs, which are properly configured. This is a planned enhancement to be scoped jointly with the platform team during the next architecture review cycle, not an immediate remediation item. Suppress pending platform coordination. The finding will be revisited and converted to a remediation ticket once the platform team engagement is complete. Scope In scope:  Suppression of AWS-1081 for  networking-psd-otep-dev-intranet-nfw-policy  in Cloudscape, covering the dev environment. Out of scope:  NFW rule group design, TGW inspection routing changes, or any platform-side firewall configuration — these are captured as a follow-up item. Acceptance Criteria [ ] AWS-1081 finding for  networking-psd-otep-dev-intranet-nfw-policy  (b179cc86-31d2-4ad5-91ae-9023d3912b6b) is submitted for suppression in Cloudscape with documented justification. [ ] Suppression justification references the platform networking baseline, the placeholder policy design, and the requirement for platform team coordination. [ ] Suppression is reviewed and approved by the relevant compliance or security stakeholder. [ ] A follow-up item or separate Jira ticket is raised to track the NFW rule group association work with the platform team. [ ] No unilateral changes are made to the NFW policy or TGW routing as part of this ticket. [ ] Suppression record is retained as evidence for the Cloud VA. Validation / Notes Confirm Cloudscape shows the finding status updated to SUPPRESSED after submission. Capture a screenshot of the suppression record in Cloudscape as VA evidence. The follow-up ticket should be scoped with the platform team to define rule group types (stateless/stateful), rule group priorities, and inspection routing changes in TGW. This suppression covers dev only. The approach for qa/uat/prd should be determined as part of the platform coordination.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
