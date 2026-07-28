# OTEP-670: CIE-Hotfix: 100-token chunk cap truncates long compound bullets 

**Status:** Backlog
**Assignee:** Benjamin Aw
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 6 (35009)

---

## Description

— tail content is lost Location: src/cie/cv/chunk.py:209-213, _truncate at lines 119-132  Options:Implement sentence-level splitting before the token gate so multi-sentence bullets produce multiple chunks rather than being truncated

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-28*
