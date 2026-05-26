# OTEP-101: Finalise Technology Stack for Sprint start

**Type:** Story
**Status:** Done
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Evaluate and justify the selection of Golang, React SPA, AWS ECS Fargate, and PostgreSQL against system requirements, scalability needs, and GovTech (IM8/PSD) guidelines before final approval.

⸻

📌 Tasks

# Evaluate Backend Technology Options

* Compare Golang with alternatives (e.g., Java, Node.js, Python)

* Assess:

* Performance and concurrency

* Maintainability

* Team expertise

* Document justification for selecting Golang

⸻

# Evaluate Frontend Approach

* Compare SPA (React) vs alternatives (e.g., SSR, Angular)

* Assess:

* User experience

* Integration with backend APIs

* Maintainability

* Document justification for selecting React SPA

⸻

# Evaluate Infrastructure Approach (AWS)

* Compare deployment options:

* ECS Fargate vs EC2 vs Kubernetes (EKS)

* Assess:

* Operational overhead

* Scalability

* Compliance with AWS GCC

* Justify use of ECS Fargate

⸻

# Evaluate Database Options

* Compare:

* PostgreSQL vs NoSQL alternatives

* Assess:

* Data structure requirements

* Consistency needs

* Compliance considerations

* Justify use of PostgreSQL (RDS)

⸻

# Evaluate Supporting Services (if applicable)

* Assess need for:

* S3 (storage)

* SQS (async processing)

* Redis (caching)

* Document when/why each is required

⸻

# Validate Compliance & Constraints

* Ensure selected stack:

* Works within AWS GCC

* Aligns with IM8 controls

* Follows PSD guidelines

⸻

# Document Final Stack & Rationale

* Consolidate all evaluations

* Provide clear justification for:

* Golang + React SPA

* ECS Fargate

* PostgreSQL

⸻

✅ Acceptance Criteria

* Comparative evaluation conducted for:

* Backend

* Frontend

* Infrastructure

* Database

* Final stack selection is:

* Clearly justified

* Documented with trade-offs

* Compliance with AWS GCC, IM8, and PSD is validated

* Architecture + tech stack reviewed and approved by stakeholders

⸻

📎 Deliverables

* Technology evaluation document

* Finalised tech stack summary

* Decision log (with trade-offs and rationale)

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-114 | Tech stack - sharpen Go framework | Done |

---

## Latest Comments

**Pow Hwee TAN (PSD):** I will put subtask under this.  As you mention we can decide most of it esp wrt to SWE practice developer handbook.  But we would want to run this through TWS and sharpen the use and alignment.

