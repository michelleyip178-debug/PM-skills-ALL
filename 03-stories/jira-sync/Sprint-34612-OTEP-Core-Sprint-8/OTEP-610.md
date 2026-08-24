# OTEP-610: Add agency suffix to duplicated competencies

**Status:** QA
**Assignee:** Kingsley Low
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

User Story As an officer, I want duplicated competency names to be clearly distinguished so that I can identify and select the correct competency without having to open each competency description. Acceptance Criteria The system shall identify competency names that exist across multiple competency IDs. For competencies belonging to the  WOG competency bank , the competency name shall remain unchanged with  no suffix  appended. For competencies belonging to the  Agency competency bank , append the owning agency acronym to the competency name in the format  (<Agency Acronym>) , for example: Audit Administration (ESG) The agency suffix shall only be applied to agency competencies whose competency names have more than one occurrence in the  Agency FCs  worksheet of the competency bank. Where both WOG and Agency competencies share the same competency name: the WOG competency shall be displayed without a suffix; each Agency competency shall display its corresponding agency suffix. In competency selection dropdowns, duplicated competency names shall be ordered as follows: WOG competency (no suffix) first. Agency competencies afterwards, sorted alphabetically by agency acronym. Example: Audit Administration Audit Administration (BCA) Audit Administration (ESG) Audit Administration (MAS) The updated competency naming convention shall be consistently reflected throughout the platform wherever competency names are displayed, including but not limited to: My Profile Your Development Competency selection dropdowns Search results Any other page displaying competency names Existing functionality for searching, selecting, adding, and removing competencies shall continue to work using the underlying competency ID and shall not be affected by the display name change.  Notes Source of truth for agency acronyms:  Column C in Agency FCs  worksheet in the competency bank. The suffix is a  display-only  change and does not modify the underlying competency ID.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-20*
