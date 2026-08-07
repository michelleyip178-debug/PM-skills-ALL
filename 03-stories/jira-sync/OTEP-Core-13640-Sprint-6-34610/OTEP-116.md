# OTEP-116: Database Schema & Mapping for POCDEX Employee Data

**Type:** Sub-task
**Status:** Done
**Assignee:** Kingsley Low
**Story Points:** 2.0

---

## Description

Design and implement database schema and field mappings to store employee data retrieved from the POCDEX API.

This task focuses on defining how incoming API data is structured, stored, and maintained within the system database.

*Fields to be stored:*

* First Name
* Last Name
* Employment Title
* Agency
* Job Grade
* Job Family
* Job Function
* NRIC (used as unique identifier)

*Requirements:*

# Design/update database schema to accommodate all required fields.
# Define clear mapping between POCDEX API response fields and database columns.
# Ensure appropriate data types, constraints, and indexing (especially for NRIC as unique identifier).
# Implement data validation rules before persistence.
# Ensure sensitive data (NRIC) is securely stored (e.g., encryption/masking if required).
# Handle null/missing values gracefully.
# Support future extensibility for additional fields.

*Acceptance Criteria:*

* Database schema supports all required employee fields.
* Data from API is correctly mapped and stored without loss or mismatch.
* NRIC is stored securely and can be used reliably for identification.
* Validation rules prevent incorrect or malformed data.
* Mapping logic is documented and consistent with API structure.

*Notes:*

* Align naming conventions with existing database standards.
* Confirm whether updates should overwrite existing records or maintain history/versioning.
* Consider audit fields (created_at, updated_at) if not already present.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Kingsley Low:** Personal Draft, Ignorable:

# Sample API testing (get a few different queries)
# data mapping (find missing/mismatch) with current database design
# validation rules (eg email must have “.com”)
# Encryption rules
# change db if needed

**Kingsley Low:** [~accountid:712020:5a4717ac-69a7-49e9-a198-16817e2d37a5] Since the database contains more fields than the ones listed above for storage, I will proceed with full data storage based on the database schema.

**Kingsley Low:** For now, any Data Nullity check (Fields mentioned above) will return an error by default.

*Synced from Jira: 2026-08-07*
