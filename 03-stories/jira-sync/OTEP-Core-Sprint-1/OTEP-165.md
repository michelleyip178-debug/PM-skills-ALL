# OTEP-165: Competencies

**Type:** Sub-task
**Status:** Done
**Assignee:** rama moorthy
**Story Points:** N/A

---

## Description

Design the backend data model for competencies and competency proficiency levels based on the agreed Confluence schema and product requirements.

The implementation should support:

* storing competency bank data
* identifying competencies using external competency bank IDs
* supporting different competency sources
* categorising competencies as functional or behavioural
* storing competency definitions
* storing proficiency level descriptions such as PL1 to PL5
* enabling competency search, display, and mapping to user profiles / role profiles

The task should include creation of GORM model structures that reflect the agreed table design.

----

h3. *Scope*

* Review the Confluence page for the agreed competency table structure
* Create GORM structs for:
** {{Competency}}
** {{CompetencyProficiencyLevel}}
* Define relationships between competency and proficiency levels
* Add appropriate GORM tags for:
** primary keys
** foreign keys
** indexes
** unique constraints
** timestamps
* Ensure {{external_id}} is used as the stable competency bank identifier
* Ensure proficiency levels support ordered display from PL1 to PL5
* Align naming conventions with the backend codebase

----

h3. *Acceptance Criteria*

* GORM structs are created based on the Confluence schema
* {{Competency}} model supports external competency bank ID mapping
* {{CompetencyProficiencyLevel}} model is linked to {{Competency}}
* Proficiency levels can be ordered correctly using {{level_order}}
* Structs support competency search and display requirements
* Structs support competency source and category classification
* Code follows backend project conventions
* Changes are reviewed and approved

[https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2198668238/Detailed+Data+Model+-+Competencies|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2198668238/Detailed+Data+Model+-+Competencies|smart-link]

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
