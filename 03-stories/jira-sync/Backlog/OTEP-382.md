# OTEP-382: Pull Job Family, Job Function, Job Grade from Pocdex

**Type:** Task
**Status:** Backlog
**Assignee:** Kingsley Low
**Story Points:** N/A

---

## Description

Implementation Overview Current Implementation (As-Is) Data Sources:  Reliant on static  Role Excel  and  Competency Excel  files. Logic:  * Inserts  Job Family ,  Job Function , and  Job Grade   only  if they exist within the spreadsheets. ⚠️  Issue:  There are currently missing codes for each of these entities. Target Implementation (To-Be) Data Source:  Migrating from  Pocdex  as the single source of truth. Logic:  * Automatically pull the full, centralized list of  Job Family ,  Job Function , and  Job Grade . Directly insert/sync the complete dataset into the database.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
