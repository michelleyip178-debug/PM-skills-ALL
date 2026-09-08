# OTEP-905: Access Control : download_load_competency_service.go

**Status:** QA
**Assignee:** Kingsley Low
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Line 221: if err := os.MkdirAll(filepath.Dir(outputPath), 0755); err != nil {   Permission should not be 5 for group and others. but remove this line if it’s not need

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-09-07*
