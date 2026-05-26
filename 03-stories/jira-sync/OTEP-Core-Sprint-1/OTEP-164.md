# OTEP-164: User Profile

**Type:** Sub-task
**Status:** Done
**Assignee:** rama moorthy
**Story Points:** N/A

---

## Description

Design the backend data model for user profiles, employment details, and user competencies based on the agreed Confluence schema and product requirements.

The implementation should align with the product needs for:

* displaying officer profile information
* supporting role mapping from employment attributes
* storing next role and target role selection
* managing role-default and manually added competencies
* supporting soft delete for removed competencies
* supporting future endorsement metadata

The task should include creation of GORM model structures that reflect the agreed table design.

----

h3. *Scope*

* Review the Confluence page for the agreed database table structure
* Create GORM structs for:
** {{UserProfile}}
** {{UserProfileEmployment}}
** {{UserCompetency}}
* Define relationships between the structs
* Add appropriate GORM tags for:
** primary keys
** foreign keys
** indexes
** nullable fields
** timestamps
* Ensure sensitive fields such as NRIC are handled carefully in struct design and logging
* Align naming conventions with the backend codebase

----

h3. *Acceptance Criteria*

* GORM structs are created based on the Confluence schema
* Struct relationships are correctly defined
* Field names and types align with product requirements
* Structs support role mapping using employment attributes
* Structs support role-default and manually added competencies
* Soft delete behaviour is supported for user competencies
* Code follows backend project conventions
* Changes are reviewed and approved

[https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2206433658/Detailed+Data+Model+-+User+Profile|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2206433658/Detailed+Data+Model+-+User+Profile|smart-link]

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Kingsley Low:** FMI

