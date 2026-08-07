# OTEP-321: Course Catalog Ingestion from Cumulus

**Type:** Story
**Status:** QA
**Assignee:** N/A
**Story Points:** 1.0
**Sprint:** OTEP-Core Sprint 7

---

## Description

Acceptance Criteria  CFTP is set up and accessible for CSC team to upload course data files Webhook configuration is completed to receive file upload notifications Webhook API successfully receives and validates incoming payload Course XML files (classroom and digital) are received and accessible Database schema is created to support course data storage XML data is parsed and stored correctly in the database Initial full load of course data is completed successfully Delta updates (new, updated, deleted courses) are processed correctly Course data is upserted and kept in sync with source Errors during ingestion are logged and traceable End-to-end flow (upload → notification → ingestion → storage) is working

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-07*
