# OTEP-313: OTG raw ingest table and source model

**Status:** Done
**Assignee:** Léo Milbor
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

Create the OTG source opportunity staging table and GORM model (sourceOTGOpportunity). This is an append-only table that stores raw JSON payloads from OTG imports for audit and reprocessing. Includes: migration (.up.sql and .down.sql), GORM model with TableName(), and jsonb column for raw data.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Michelle Yip** (2026-05-21)
Uploaded the file here

---
*Synced from Jira: 2026-07-15*
