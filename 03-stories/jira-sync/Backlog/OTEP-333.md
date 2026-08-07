# OTEP-333: Add ref_job_family and ref_job_function to shared refdata repository after upstream taxonomy is finalised

**Type:** Story

**Status:** Done

**Assignee:** Pow Hwee TAN (PSD)

**Story Points:** N/A

---

## Description

Context OTEP-332 creates the shared refdata repository for stable reference tables (ref_agency, ref_employment_type, ref_opportunity_type, ref_id_type). Job family and job function tables are deferred because business is considering revamping the taxonomy. The current definitions follow POCDEX, but any changes to the taxonomy are an upstream job (POCDEX team). Scope Once the upstream POCDEX team finalises the new job family/function taxonomy, add GORM models and read-only repository methods for ref_job_family and ref_job_function to the shared refdata package (internal/shared/refdata/) Include ingestion/sync path from POCDEX for these tables Also include ref_job_grade if needed at that point Dependencies OTEP-332 (shared refdata repository must exist first) Upstream: POCDEX team to confirm finalised job family/function taxonomy Needed For Release 1: Ringfencing criteria (OTEP-127) — filter opportunities by job family/function

---

## PM Note — 2026-06-25

**Upstream taxonomy blocker resolved.**

The finalised job family taxonomy (27 families, HR source) was confirmed on 2026-06-25. POCDEX is adopting this taxonomy. OTG tags opportunities using the same 27 names. This removes the upstream dependency blocking this story.

**Confirmed 27 job families:** Arts & Culture, Education & Skills Development, Emergency Preparedness & Response, Environment & Resources, Finance, Governance Risk & Controls, Human Resource, Industry & Sector Development, Infocomm Technology & Smart Systems, Internal Audit, International Relations, Land & Estate Management, Legal, Organisation Development, Planning, Policy & Planning, Procurement, Programme & Project Management, Programme Evaluation, Public Communications, Regulatory, Research & Innovation, Science Tech & Engineering, Service Delivery, Social & Community Services, Trade & Economy, Urban & Physical Planning

**Next step:** Pow Hwee to assess readiness for S5 or S6 intake.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-08-07*
