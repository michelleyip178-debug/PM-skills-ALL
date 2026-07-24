# OTEP-151: Create New AWS Account on GCC (Development Environment)

**Type:** Sub-task
**Status:** Done
**Assignee:** Fabian PEH
**Story Points:** N/A

---

## Description

*Description:*

As part of the *OTEP* project, we need to provision a new AWS account under GCC (Government Commercial Cloud) for the *Development Environment*. Approval from the Agency Project Manager / AO has already been obtained.

*Tasks:*

# Raise a request via the *GCC Portal* to provision a new AWS account under the *Development OU*
# Link the account under the correct *Agency Organisational Unit (OU)* and tag it as a Dev environment
# Verify that *CloudTrail, Config, and GuardDuty* are enabled (or centrally managed by GovTech)
# Apply the mandatory *GCC Security Baseline* configurations
# Set up a *VPC* with appropriate subnets for OTEP development workloads — ensure it is isolated from staging and production
# Configure *AWS IAM Identity Center (SSO)* integrated with TechPass for engineer access
# Assign engineers to appropriate permission sets (e.g., PowerUser, DevOps, Read-Only)
# Set up *billing alerts and budget thresholds* to avoid unexpected costs
# Tag all resources with {{environment: dev}} and {{project: OTEP}} for cost tracking
# Document account details and access structure in *Confluence* and update the agency cloud inventory

*Notes:*

* All engineers must have active *TechPass accounts* before access can be provisioned
* Engineers on personal devices must be onboarded to *SEED*

*Acceptance Criteria:*

* New AWS dev account is provisioned and accessible via GCC Portal
* Engineers can log in successfully via TechPass SSO
* GCC Security Baseline is applied
* Billing alerts are configured
* Confluence documentation is updated

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Adrian Lo:** OTEP Core team members confirmed able to access account

*Synced from Jira: 2026-07-23*
