# OTEP-102: Data Design

**Type:** Story
**Status:** Done
**Assignee:** Pow Hwee TAN (PSD)
**Story Points:** N/A

---

## Description

Identify, structure, and classify system data to ensure proper handling, storage, and compliance with IM8 and security requirements.

⸻

📌 Tasks

# Identify Data Entities

* List all key data objects:

* User data

* Transactions

* System logs

* Reference data

* Define relationships between entities

⸻

# Define Data Model (High-Level)

* Draft schema design (for PostgreSQL)

* Identify:

* Tables

* Key fields

* Relationships (FKs)

⸻

# Classify Data (IM8 Alignment)

* Categorise data into:

* Sensitive (e.g., PII)

* Confidential

* Public / non-sensitive

* Tag which components handle sensitive data

⸻

# Define Data Flow

* Map how data moves across:

* Frontend (React)

* Backend (Go services)

* Database (PostgreSQL)

* External systems (if any)

⸻

# Define Data Handling Rules

* Storage rules (e.g., encryption at rest)

* Transmission rules (HTTPS, secure APIs)

* Logging restrictions (no sensitive data in logs)

⸻

# Validate Compliance Requirements

* Ensure:

* IM8 controls are met

* Data handling aligns with security policies

⸻

✅ Acceptance Criteria

* Key data entities and relationships are identified

* High-level schema (PostgreSQL) is defined

* Data classification is completed and documented

* Data flow across system components is clearly mapped

* Data handling rules align with IM8/security requirements

* Reviewed and approved by stakeholders

⸻

📎 Deliverables

* Data model diagram (high-level ERD)

* Data classification document

* Data flow diagram

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-164 | User Profile | Done |
| OTEP-165 | Competencies | Done |

---

## Latest Comments

**Pow Hwee TAN (PSD):** *Scope for Sprint 1 — enable feature development:*

* Schema design: ref tables (OTEP-201) + entity tables (OTEP-224)
* Seed data for local development: ref data (OTEP-207) + entity data (OTEP-204)
* Data conventions & naming alignment with POCDEX
* ER diagram (OTEP-251)

Foundation is in place for feature team to start building on.

*Descoped from this story:*

* *Data flow diagram* — feature team artefact, to be produced when they build the end-to-end integration, if applicable.
* *Data classification* — product-level activity, not data design.
* *IM8 compliance validation* — this is a system-level assessment, not a data design activity. Requires infra controls (encryption at rest, TLS, network segmentation) to be in place and is validated by security assessment.

