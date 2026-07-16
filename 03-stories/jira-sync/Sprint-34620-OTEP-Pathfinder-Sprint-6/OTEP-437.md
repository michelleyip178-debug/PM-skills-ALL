# OTEP-437: [FE/BE] Filter by job family

**Status:** In Progress
**Assignee:** Hao Eng
**Story Points:** 3
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

As an officer browsing CareerCompass,  I want to filter opportunities by job category and see all relevant listings under the right label — regardless of whether they came from C@G or OTG,  so that I don't miss opportunities just because they came from a different source.   AC1 — C@G opportunities appear under the correct WOG job category filter Given an officer is on the opportunity listing page,  When they filter by a job category (e.g. Finance, Healthcare, Legal, Education & Skills Development),  Then they see C@G opportunities tagged with that category in the results. AC2 — C@G and OTG opportunities appear together under the same filter label Given an officer filters by a WOG job category,  When results load,  Then C@G and OTG opportunities in that category appear together in the same results list. No source label or distinction is shown. AC3 — C@G opportunities without a job category still appear Given a C@G listing has no job category,  When the officer browses the listing without a filter applied,  Then the opportunity is still visible. It is not silently dropped from the results. AC4 — An unrecognised C@G job category does not cause the opportunity to disappear Given C@G introduces a job category not yet mapped to a WOG label,  When the officer browses the listing,  Then the opportunity still appears — it is not missing from results and does not cause an error.   Use the WOG Category as the MASTER.  WOG Category (MASTER) C@G Indus Code(s) OTG Job Family Notes Arts & Culture 0003 Arts/Cultural/Heritage Library & Archives  Corporate Administration 0002 Administration Support; 0025 Others —  Education & Skills Development 0010 Education; 0034 Training and Development Academic Operations;  Education & Skills Devt  (not in ref_job_family)  <have to add> OTG: L&D not present in OTG opportunity data (BO confirmed 2026-06-25) Emergency Preparedness & Response 0015 Home Team Uniformed Services; 0031 Singapore Armed Forces Emergency Preparedness & Response  Environment & Resources 0020 Landscape/Horticulture Environment & Resources  (not in ref_job_family) <have to add>  Finance 0001 Accounting, Audit, Finance Finance and Accounting  (closest match Accounting & Finance)     C@G: BO confirmed all roles stay under Finance — no Audit split (2026-06-25) Governance, Risk & Controls — Governance, Risk & Controls No C@G source Healthcare 0014 Healthcare — WOG category confirmed 2026-06-25. No OTG equivalent in current data. Human Resource 0016 Human Resources Human Resources  Industry & Sector Development — Industry & Sector Development; Industry & Sector Devt  (closest match Industry/Sector Development & Programme Management)     No C@G source Infocomm Technology & Smart Systems 0017 InfoComm, Technology, New Media Communications Infocomm Tech & Smart Systems  (not in ref_job_family) ;  <have to map to the below instead> Infocomm Technology & Smart Systems C@G: BO confirmed New Media Comms stays under ICT (2026-06-25) Internal Audit — Internal Audit  (closest match Audit)    C@G: no standalone source — 0001 fully maps to Finance (BO confirmed 2026-06-25) International Relations 0013 Foreign Service; 0018 International Relations —  Land & Estate Management 0004 Building and Estate Management Land & Estate Mgmt;  (not in ref_job_family) Land Sales Admin  (not in ref_job_family) <have to add it as Land & Estate Mgmt.>  Legal 0005 Conciliation/Mediation; 0006 Conciliation/Mediation and Statistics; 0021 Law/Legal Services Legal  (closest match Legal & Parliamentary)    0006 has ~0 listings Organisation Development 0024 Organisation Development; 0028 Public Service Leadership Organisation Devt  (closest match Organisation Development)     Partnership & Engagement — Partnership & Engagement  (closest match Community Devt, Partnership & Engagement)    No C@G source Planning 0007 Corporate Strategy/Top Management Planning  (closest match Policy & Planning)     Policy & Planning 0026 Policy Formulation Policy & Planning  Procurement — Procurement No C@G source Programme & Project Management — Programme & Project Mgmt  (closest match Industry/Sector Development & Programme Management)    No C@G source Programme Evaluation — Programme Eval  (closest match Industry/Sector Development & Programme Management)    No C@G source Public Communications 0022 Marketing/Business Development; 0027 PR/Corp Comms/Psychology; 0035 Translators/Interpreters Public Comms; Strategic Communications  (closest match  Public Communications)    C@G: BO confirmed Marketing/Business Development → Public Communications (2026-06-25). 0035 has 0 listings. Regulatory 0011 Enforcement; 0019 Investigation; 0023 Occupational Safety and Health Regulatory  Research & Innovation 0009 Economics/Statistics; 0029 Research and Analysis; 0033 Statistics Research ⚠️;  (not in ref_job_family) Research & Innovation  (not in ref_job_family)  <have to add as Research & Innovation> OTG: "Research" is a legacy code consolidating with Research & Innovation Science, Tech & Engineering 0012 Engineering; 0030 Sciences Science, Tech & Engrg  (closest match Science, Technology & Engineering)    ; Technical Capability ⚠️ OTG: Technical Capability could be  Infocomm Technology & Smart Systems — confirm with HR Service Delivery 0008 Customer Service Service Delivery  Social & Community Services 0032 Social and Community Development Social & Community Services  (closest match Social Services)  C@G: 0014 Healthcare moved to WOG Healthcare category (BO confirmed 2026-06-25) Trade & Economy — Trade & Economy  (closest match Trades & Labour)  No C@G source Urban & Physical Planning — Urban & Physical Planning;  (not in ref_job_family) Urban Planning and Design ⚠️ (not in ref_job_family)  <have to add as Urban & Physical Planning> OTG: "Urban Planning and Design" is legacy code consolidating with Urban & Physical Planning

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Hao Eng** (2026-07-15)
Understand that OTG job fam shld be exact match to ref_job_family table decision: in opportunity table: happy path: those found in ref_job_family can get its respective job_family_id value else, only the job_family_label and job_family_code are populated without the job_family_id (no FK) there will be new column containing the wog_category_id new table to contain the above ticket mapping: wog_category_id - wog_category_label - source (cag/OTG) - job_fam code -job fam label

---

**Hao Eng** (2026-07-14)
oh yes there is such warning and error in the  source_otg_opportunity  and  source_cag_opportunity  db tables!  are u referring to the upload UI for OTG that “error report” view? or a new output?

---

**Pow Hwee TAN (PSD)** (2026-07-14)
need you to sort out the mapping with Imelda.     for unmatched records, in our ‘error report’, do we show them?   I am thinking of operationally to be able to flag out for followup.  I recall Leo catered for this.

---
*Synced from Jira: 2026-07-16*
