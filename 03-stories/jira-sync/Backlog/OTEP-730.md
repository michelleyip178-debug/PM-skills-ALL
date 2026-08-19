# OTEP-730: Suppress AWS-1213 — IAM Role stacksets-exec-* Uses Allow-All Policy (Platform-Managed, StackSets)

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Summary Suppress Cloudscape finding AWS-1213 for the IAM role  stacksets-exec-04defcb04e1c96aa20d661b8b768c3b0  in account 257212470025. This role is provisioned by AWS CloudFormation StackSets during account bootstrapping and is outside the app team's ownership boundary. Type Suppression Epic Cloud VA — CIS Benchmark Remediation and Compliance Closure (Dev) Labels cloud-va ,  cis-benchmark ,  compliance ,  suppression IM8 Clause AC-1  Context AWS CloudFormation StackSets creates execution roles in member accounts using the  stacksets-exec-*  naming convention during account bootstrapping. These roles are required for cross-account StackSet operations and are provisioned and managed entirely by the GCC/TLZ (Tenant Landing Zone) platform. They are not part of the application team's IaC and cannot be modified by the app team without breaking platform-level administration workflows. Problem Statement Cloudscape is flagging AWS-1213 (IAM roles should not use policies that allow all actions) as NON_COMPLIANT for  arn:aws:iam::257212470025:role/stacksets-exec-04defcb04e1c96aa20d661b8b768c3b0 . The broad policy attached to this role is intentional and required by the AWS StackSets service for cross-account execution. The app team has no ownership over this role. Justification for Suppression The  stacksets-exec-*  naming convention is a well-known AWS pattern for CloudFormation StackSets execution roles, created automatically during account bootstrapping. This role is platform-managed infrastructure provisioned by GCC/TLZ StackSets. It does not appear in app team IaC. The allow-all policy on this role is a platform-level design decision required for StackSet cross-account operations. Modifying it would break platform administration. The app team does not have the permissions or mandate to change this role. Suppression is the correct disposition. Reference: GCC/TLZ platform-managed infrastructure. Scope In scope:  Suppression of AWS-1213 for  arn:aws:iam::257212470025:role/stacksets-exec-04defcb04e1c96aa20d661b8b768c3b0  in Cloudscape. Out of scope:  Any modification to the role or its attached policies, which remains a platform responsibility. Acceptance Criteria [ ] AWS-1213 finding for  stacksets-exec-04defcb04e1c96aa20d661b8b768c3b0  is submitted for suppression in Cloudscape with documented justification. [ ] Suppression justification references the GCC/TLZ StackSets platform-managed role and the account bootstrapping process. [ ] Suppression is reviewed and approved by the relevant compliance or security stakeholder. [ ] No app-team IaC changes are made as part of this ticket. [ ] Suppression record is retained as evidence for the Cloud VA. Validation / Notes Confirm Cloudscape shows the finding status updated to SUPPRESSED after submission. Capture a screenshot of the suppression record in Cloudscape as VA evidence. If GCC/TLZ platform documentation references the StackSets execution role pattern, attach the link to this Jira ticket. Related ticket: iam-role-tlz-org-access-allow-all.md (AWS-1213,  tlz_organization_account_access_role ) — same finding, same platform-managed justification.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
