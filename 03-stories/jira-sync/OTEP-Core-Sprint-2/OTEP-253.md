# OTEP-253: IAC code organisation strategy  

**Type:** Task
**Status:** QA
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

*Description:* The {{Ootep-iac}} repository should transition from a monolithic setup into independent micro-stacks to improve scalability, maintainability, and security. The *CROP method* should be applied to identify these stack boundaries based on Cohesion, Risk, Ownership, and Pattern of Change. This architecture should isolate stable foundational networking (Core-infra) from the frequently changing infrastructure required for the *Go backend (Ootep-service)* and *Next.js frontend (Ootep-web)*.

*Key Requirements:*

* *Implement Micro-Stacks:* Infrastructure should be broken into smaller, independent Terraform stacks based on logical components like networking and compute.
* *Apply CROP Principles:* Resource grouping should follow Cohesion (logical grouping), Risk (isolating critical assets), Ownership (aligning with team accountability), and Pattern of Change (separating stable from volatile resources).
* *Establish Configuration Structure:* A separate configuration layout should be implemented within {{Ootep-iac}} to host environment-specific backend and variable files for the *dev*, *qa*, *pre_prod*, and *prod* environments.
* *Manage Dependencies via Variables:* Inter-stack communication should be handled by passing outputs from the core stack as input variables to application stacks to ensure clean separation without hard state coupling.
* *Standardize with Modules:* Reusable shared Terraform modules should be utilized to enforce baked-in best practices, such as security, tagging, and logging across all environments.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** [https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2253488991/IAC+code+organisation|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2253488991/IAC+code+organisation|smart-link]

