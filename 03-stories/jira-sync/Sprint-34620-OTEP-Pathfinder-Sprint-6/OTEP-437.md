# OTEP-437: [FE/BE] Filter by job family

**Status:** To Do
**Assignee:** Hao Eng
**Story Points:** 3
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

As an officer browsing CareerCompass,  I want to filter opportunities by job category and see all relevant listings under the right label — regardless of whether they came from C@G or OTG,  so that I don't miss opportunities just because they came from a different source.   AC1 — C@G opportunities appear under the correct WOG job category filter Given an officer is on the opportunity listing page,  When they filter by a job category (e.g. Finance, Healthcare, Legal, Education & Skills Development),  Then they see C@G opportunities tagged with that category in the results. AC2 — C@G and OTG opportunities appear together under the same filter label Given an officer filters by a WOG job category,  When results load,  Then C@G and OTG opportunities in that category appear together in the same results list. No source label or distinction is shown. AC3 — C@G opportunities without a job category still appear Given a C@G listing has no job category,  When the officer browses the listing without a filter applied,  Then the opportunity is still visible. It is not silently dropped from the results. AC4 — An unrecognised C@G job category does not cause the opportunity to disappear Given C@G introduces a job category not yet mapped to a WOG label,  When the officer browses the listing,  Then the opportunity still appears — it is not missing from results and does not cause an error.   Use the WOG Category as the MASTER.  WOG Category (MASTER) C@G Indus Code(s) OTG Job Family Notes Arts & Culture 0003 Arts/Cultural/Heritage Library & Archives  Corporate Administration 0002 Administration Support; 0025 Others — OTG A–K pending Education & Skills Development 0010 Education; 0034 Training and Development Academic Operations; Education & Skills Devt OTG: L&D not present in OTG opportunity data (BO confirmed 2026-06-25) Emergency Preparedness & Response 0015 Home Team Uniformed Services; 0031 Singapore Armed Forces Emergency Preparedness & Response  Environment & Resources 0020 Landscape/Horticulture Environment & Resources  Finance 0001 Accounting, Audit, Finance Finance and Accounting C@G: BO confirmed all roles stay under Finance — no Audit split (2026-06-25) Governance, Risk & Controls — Governance, Risk & Controls No C@G source Healthcare 0014 Healthcare — WOG category confirmed 2026-06-25. No OTG equivalent in current data. Human Resource 0016 Human Resources Human Resources  Industry & Sector Development — Industry & Sector Development; Industry & Sector Devt No C@G source Infocomm Technology & Smart Systems 0017 InfoComm, Technology, New Media Communications Infocomm Tech & Smart Systems; Infocomm Technology & Smart Systems C@G: BO confirmed New Media Comms stays under ICT (2026-06-25) Internal Audit — Internal Audit C@G: no standalone source — 0001 fully maps to Finance (BO confirmed 2026-06-25) International Relations 0013 Foreign Service; 0018 International Relations — OTG A–K pending Land & Estate Management 0004 Building and Estate Management Land & Estate Mgmt; Land Sales Admin  Legal 0005 Conciliation/Mediation; 0006 Conciliation/Mediation and Statistics; 0021 Law/Legal Services Legal 0006 has ~0 listings Organisation Development 0024 Organisation Development; 0028 Public Service Leadership Organisation Devt  Partnership & Engagement — Partnership & Engagement No C@G source Planning 0007 Corporate Strategy/Top Management Planning  Policy & Planning 0026 Policy Formulation Policy & Planning  Procurement — Procurement No C@G source Programme & Project Management — Programme & Project Mgmt No C@G source Programme Evaluation — Programme Eval No C@G source Public Communications 0022 Marketing/Business Development; 0027 PR/Corp Comms/Psychology; 0035 Translators/Interpreters Public Comms; Strategic Communications C@G: BO confirmed Marketing/Business Development → Public Communications (2026-06-25). 0035 has 0 listings. Regulatory 0011 Enforcement; 0019 Investigation; 0023 Occupational Safety and Health Regulatory  Research & Innovation 0009 Economics/Statistics; 0029 Research and Analysis; 0033 Statistics Research ⚠️; Research & Innovation OTG: "Research" is a legacy code consolidating with Research & Innovation Science, Tech & Engineering 0012 Engineering; 0030 Sciences Science, Tech & Engrg; Technical Capability ⚠️ OTG: Technical Capability could be Infocomm Technology & Smart Systems — confirm with HR Service Delivery 0008 Customer Service Service Delivery  Social & Community Services 0032 Social and Community Development Social & Community Services C@G: 0014 Healthcare moved to WOG Healthcare category (BO confirmed 2026-06-25) Trade & Economy — Trade & Economy No C@G source Urban & Physical Planning — Urban & Physical Planning; Urban Planning and Design ⚠️ OTG: "Urban Planning and Design" is legacy code consolidating with Urban & Physical Planning

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-14*
