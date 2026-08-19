# OTEP-731: Suppress AWS-1213 — IAM Role tlz_organization_account_access_role Uses Allow-All Policy (Platform-Managed, TLZ)

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Summary Suppress Cloudscape finding AWS-1213 for the IAM role  tlz_organization_account_access_role  in account 257212470025. This is the TLZ (Tenant Landing Zone) organisation account access role created during account provisioning and is outside the app team's ownership boundary. Type Suppression Epic Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev) Labels cloud-va ,  cis-benchmark ,  compliance ,  suppression IM8 Clause AC-1  Context The  tlz_organization_account_access_role  is provisioned automatically during GCC Tenant Landing Zone account provisioning. The  tlz_  prefix is a known platform-managed naming convention used across all TLZ-onboarded accounts. This role enables organisation-level administration by the platform team and is not managed or owned by the application team. It does not appear in any app-team IaC. Problem Statement Cloudscape is flagging AWS-1213 (IAM roles should not use policies that allow all actions) as NON_COMPLIANT for  arn:aws:iam::257212470025:role/tlz_organization_account_access_role . The broad policy on this role is an intentional platform-level design to support TLZ organisation administration. The app team has no ownership or permissions to modify this role. Justification for Suppression The  tlz_  prefix is a recognised naming convention for GCC Tenant Landing Zone platform-managed roles. This role is provisioned during account onboarding as part of the TLZ baseline and does not appear in app-team IaC. The allow-all policy is a deliberate platform design required for organisation-level account access. Modifying it would break TLZ administration workflows. The app team does not have the permissions or mandate to change this role. Suppression is the correct disposition. Reference: GCC Tenant Landing Zone infrastructure documentation. Scope In scope:  Suppression of AWS-1213 for  arn:aws:iam::257212470025:role/tlz_organization_account_access_role  in Cloudscape. Out of scope:  Any modification to the role or its attached policies, which remains a TLZ platform responsibility. Acceptance Criteria [ ] AWS-1213 finding for  tlz_organization_account_access_role  is submitted for suppression in Cloudscape with documented justification. [ ] Suppression justification references the GCC Tenant Landing Zone platform-managed role and account provisioning process. [ ] Suppression is reviewed and approved by the relevant compliance or security stakeholder. [ ] No app-team IaC changes are made as part of this ticket. [ ] Suppression record is retained as evidence for the Cloud VA. Validation / Notes Confirm Cloudscape shows the finding status updated to SUPPRESSED after submission. Capture a screenshot of the suppression record in Cloudscape as VA evidence. If GCC TLZ documentation references the organisation account access role pattern, attach the link to this Jira ticket. Related ticket: iam-role-stacksets-exec-allow-all.md (AWS-1213,  stacksets-exec-* ) — same finding, same platform-managed justification.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
