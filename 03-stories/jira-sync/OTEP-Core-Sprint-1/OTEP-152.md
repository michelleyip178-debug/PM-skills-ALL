# OTEP-152: Create New AWS Account on GCC (UAT Environment)

**Type:** Sub-task
**Status:** Done
**Assignee:** Fabian PEH
**Story Points:** N/A

---

## Description

As part of the *OTEP* project, we need to provision a new AWS account under GCC (Government Commercial Cloud) for the *UAT Environment*. Approval from the Agency Project Manager / AO has already been obtained.

*Tasks:*

# Raise a request via the *GCC Portal* to provision a new AWS account under the *UAT OU*
# Link the account under the correct *Agency Organisational Unit (OU)* and tag it as a UAT environment
# Verify that *CloudTrail, Config, and GuardDuty* are enabled (or centrally managed by GovTech) - Fabian needs to help.
# Apply the mandatory *GCC Security Baseline* configurations
# Set up a *VPC* with appropriate subnets for OTEP UAT workloads — ensure it is isolated from dev and production
# Configure *AWS IAM Identity Center (SSO)* integrated with TechPass for engineer access
# Assign engineers to appropriate permission sets — UAT should have *more restrictive permissions* compared to dev (e.g., ReadOnly for most, PowerUser for DevOps only)
# Set up *billing alerts and budget thresholds* to avoid unexpected costs
# Tag all resources with {{environment: uat}} and {{project: OTEP}} for cost tracking
# Document account details and access structure in *Confluence* and update the agency cloud inventory

*Notes:*

* All engineers must have active *TechPass accounts* before access can be provisioned
* Engineers on personal devices must be onboarded to *SEED*
* Ensure UAT environment mirrors production configuration as closely as possible for accurate testing

*Acceptance Criteria:*

* New AWS UAT account is provisioned and accessible via GCC Portal
* Engineers can log in successfully via TechPass SSO
* GCC Security Baseline is applied
* Billing alerts are configured
* UAT environment is isolated from Dev and Production
* Confluence documentation is updated

---

## Subtasks

_No subtasks._

---

## Latest Comments

**rama moorthy:** [~accountid:712020:f1b20f91-0679-4119-a517-0ec77a28c4f8]  Do we need VAPT for UAT environment ?

**Adrian Lo:** OTEP Core team members confirmed able to access account

