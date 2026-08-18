# OTEP-803: Investigate date timezone

**Status:** Done
**Assignee:** Thomas Huchedé
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

We have a few instance where date are parsed using UTC and compared to a  NOW()  in DB.  Those dates are meaningful from a Singapore context (closing date, posted date) and should probably be parsed and treated as a date with the proper TZ

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-18*
