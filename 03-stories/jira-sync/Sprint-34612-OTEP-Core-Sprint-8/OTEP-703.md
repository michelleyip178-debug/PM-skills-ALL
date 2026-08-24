# OTEP-703: Your Development - Update Filter Behaviour

**Status:** QA
**Assignee:** Adrian Lo
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

There are currently 3 filters: Agency Job Family Job Function  UI Behaviour changes: Agency - no change (should have no limit) Job Family limit to only 1 selection remove select all Job Function Limit to 5 selections Job Function filter only shows up when Job Family filter is selected remove select all  Backend changes: Display filters only where  display_order  column value > 0 Agency Job Family Job Function Initial load shows only Agency and Job Family Only if a filter is passed in for Job Family, then Job Function filtered by selection is returned

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-20*
