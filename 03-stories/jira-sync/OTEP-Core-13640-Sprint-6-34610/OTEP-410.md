# OTEP-410: API  - Upload resume to Intelligence API and return competencies

**Type:** Sub-task
**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 6 (id 34610, active)

---

## Description

Frontend uploads a resume (docx, max 5MB) via OTEP BE. OTEP BE calls the Intelligence API with pocdex user id. Intelligence API returns competencies. OTEP BE sends filtered(refer to ACs) competencies back to FE Acceptance Criteria BE validates resume file (docx, ≤5MB)  BE sends pocdex user id to Intelligence API along with the file and capacity(how many competencies to be returned) After Getting the competencies from Intellgence The competencies that are recommended are only functional competencies and are only from the WOG FC bank and excludes core and agency-specific competencies pocdex user id is removed from intelligence API response {
   "competencies": [
    {
      "competency_code": "COMP-0001",
      "competency_name": "Stakeholder Management",
      "competency_desc":"blah blah"
      }
      ]
    }
 API Docs:

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-23*
