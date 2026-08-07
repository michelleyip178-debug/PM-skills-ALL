# OTEP-437: [FE/BE] Filter by job family

**Status:** QA
**Assignee:** Hao Eng
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

As an officer browsing CareerCompass,  I want to filter opportunities by job category and see all relevant listings under the right label — regardless of whether they came from C@G or OTG,  so that I don't miss opportunities just because they came from a different source.   AC1 — C@G opportunities appear under the correct WOG job category filter Given an officer is on the opportunity listing page,  When they filter by a job category (e.g. Finance, Healthcare, Legal, Education & Skills Development),  Then they see C@G opportunities tagged with that category in the results. AC2 — C@G and OTG opportunities appear together under the same filter label Given an officer filters by a WOG job category,  When results load,  Then C@G and OTG opportunities in that category appear together in the same results list. No source label or distinction is shown. AC3 — C@G opportunities without a job category still appear Given a C@G listing has no job category,  When the officer browses the listing without a filter applied,  Then the opportunity is still visible. It is not silently dropped from the results. AC4 — An unrecognised C@G job category does not cause the opportunity to disappear Given C@G introduces a job category not yet mapped to a WOG label,  When the officer browses the listing,  Then the opportunity still appears — it is not missing from results and does not cause an error.   Use the WOG Category as the MASTER.  Series of decisions :   16 Jul : confirmed to use WOG Job Family instead of WOG functional area as WOG Category 22 Jul Avoid adding “missing” OTG job family values to ref_job_family table. Will have our own opportunity category job family table (db tablename:  opportunity_category_job_family ) to maintain this mapping since some of the OTG job fam not found in ref_job_family.  WOG Category (MASTER) Opportunity Category (try following ref_job_family) C@G Indus Code(s) OTG Job Family Notes Arts & Culture Library & Archives 0003 Arts/Cultural/Heritage Library & Archives  Corporate Administration Corporate Administration 0002 Administration Support; 0025 Others —  Education & Skills Development Academic Operations  — Academic Operations;   OTG: L&D not present in OTG opportunity data (BO confirmed 2026-06-25)  Education & Skills Development 0010 Education; 0034 Training and Development Education & Skills Devt   (closest match Education & Skills Development)   Emergency Preparedness & Response Emergency Preparedness & Response 0015 Home Team Uniformed Services; 0031 Singapore Armed Forces Emergency Preparedness & Response  Environment & Resources <NEW> Environment & Resources 0020 Landscape/Horticulture Environment & Resources  (not in ref_job_family) <have to add>  Finance Accounting & Finance 0001 Accounting, Audit, Finance Finance and Accounting  (closest match Accounting & Finance)     C@G: BO confirmed all roles stay under Finance — no Audit split (2026-06-25) Governance, Risk & Controls <NEW> Governance, Risk & Controls — Governance, Risk & Controls No C@G source Healthcare Healthcare 0014 Healthcare — WOG category confirmed 2026-06-25. No OTG equivalent in current data. Human Resource Human Resources 0016 Human Resources Human Resources  Industry & Sector Development Industry/Sector Development & Programme Management — Industry & Sector Development; Industry & Sector Devt  (closest match Industry/Sector Development & Programme Management)     No C@G source Infocomm Technology & Smart Systems Infocomm Technology & Smart Systems 0017 InfoComm, Technology, New Media Communications Infocomm Tech & Smart Systems  (not in ref_job_family) ;  <have to map to the below instead> Infocomm Technology & Smart Systems C@G: BO confirmed New Media Comms stays under ICT (2026-06-25) Internal Audit Audit — Internal Audit  (closest match Audit)    C@G: no standalone source — 0001 fully maps to Finance (BO confirmed 2026-06-25) International Relations International Relations 0013 Foreign Service; 0018 International Relations —  Land & Estate Management <NEW> Land & Estate Management 0004 Building and Estate Management Land & Estate Mgmt;  (not in ref_job_family) Land Sales Admin  (not in ref_job_family) <have to add it as Land & Estate Mgmt.>  Legal Legal & Parliamentary 0005 Conciliation/Mediation; 0006 Conciliation/Mediation and Statistics; 0021 Law/Legal Services Legal  (closest match Legal & Parliamentary)    0006 has ~0 listings Organisation Development Organisation Development 0024 Organisation Development; 0028 Public Service Leadership Organisation Devt  (closest match Organisation Development)     Partnership & Engagement Community Devt, Partnership & Engagement — Partnership & Engagement  (closest match Community Devt, Partnership & Engagement)    No C@G source Planning Policy & Planning 0007 Corporate Strategy/Top Management Planning  (closest match Policy & Planning)     Policy & Planning Policy & Planning 0026 Policy Formulation Policy & Planning  Procurement Procurement — Procurement No C@G source Programme & Project Management Industry/Sector Development & Programme Management — Programme & Project Mgmt  (closest match Industry/Sector Development & Programme Management)    No C@G source Programme Evaluation Industry/Sector Development & Programme Management — Programme Eval  (closest match Industry/Sector Development & Programme Management)    No C@G source Public Communications Public Communications 0022 Marketing/Business Development; 0027 PR/Corp Comms/Psychology; 0035 Translators/Interpreters Public Comms; Strategic Communications  (closest match  Public Communications)    C@G: BO confirmed Marketing/Business Development → Public Communications (2026-06-25). 0035 has 0 listings. Regulatory Regulatory 0011 Enforcement; 0019 Investigation; 0023 Occupational Safety and Health Regulatory  Research & Innovation <NEW> Research & Innovation 0009 Economics/Statistics; 0029 Research and Analysis; 0033 Statistics Research ⚠️;  (not in ref_job_family) Research & Innovation  (not in ref_job_family)  <have to add as Research & Innovation> OTG: "Research" is a legacy code consolidating with Research & Innovation Science, Tech & Engineering Science, Technology & Engineering 0012 Engineering; 0030 Sciences Science, Tech & Engrg  (closest match Science, Technology & Engineering)    ; Technical Capability ⚠️ OTG: Technical Capability could be  Infocomm Technology & Smart Systems — confirm with HR 16 Jul: can ignore Service Delivery Service Delivery 0008 Customer Service Service Delivery  Social & Community Services Social Services 0032 Social and Community Development Social & Community Services  (closest match Social Services)  C@G: 0014 Healthcare moved to WOG Healthcare category (BO confirmed 2026-06-25) Trade & Economy Trades & Labour — Trade & Economy  (closest match Trades & Labour)  No C@G source Urban & Physical Planning <NEW> Urban & Physical Planning — Urban & Physical Planning;  (not in ref_job_family) Urban Planning and Design ⚠️ (not in ref_job_family)  <have to add as Urban & Physical Planning> OTG: "Urban Planning and Design" is legacy code consolidating with Urban & Physical Planning

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-824 | [BUG] Open items for function filter | Backlog |

---

## Latest Comments

**boonsiangteh** (2026-07-21)
Hao Eng CHUA  mentioned this issue in  a commit  of  WOG / PSD / pdo / OTEP / otep-web : feat:    filter by wog category (function)

---

**boonsiangteh** (2026-07-21)
Hao Eng CHUA  mentioned this issue in  a commit  of  WOG / PSD / pdo / OTEP / otep-web : feat:    added zod validation and added unit test

---

**boonsiangteh** (2026-07-21)
Hao Eng CHUA  mentioned this issue in  a commit  of  WOG / PSD / pdo / OTEP / otep-web : fix:    remove wog wording

---
*Synced from Jira: 2026-08-07*
