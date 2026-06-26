# OTEP-437: Job category filter shows consistent labels across all opportunity sources

**Type:** Story

**Status:** Backlog

**Assignee:** Léo Milbor (suggested)

**Story Points:** TBC at grooming

**Note:** Bundle with Story 4 (OTG → WOG, OTEP-ingestion-v3-rule-updates.md) at grooming — same build, same sprint.

---

## User Story

As an officer browsing CareerCompass,
I want to filter opportunities by job category and see all relevant listings under the right label — regardless of whether they came from C@G or OTG,
so that I don't miss opportunities just because they came from a different source.

---

## Acceptance Criteria

**AC1 — C@G opportunities appear under the correct WOG job category filter**

Given an officer is on the opportunity listing page,
When they filter by a job category (e.g. Finance, Healthcare, Legal, Education & Skills Development),
Then they see C@G opportunities tagged with that category in the results.

**AC2 — C@G and OTG opportunities appear together under the same filter label**

Given an officer filters by a WOG job category,
When results load,
Then C@G and OTG opportunities in that category appear together in the same results list. No source label or distinction is shown.

**AC3 — C@G opportunities without a job category still appear**

Given a C@G listing has no job category,
When the officer browses the listing without a filter applied,
Then the opportunity is still visible. It is not silently dropped from the results.

**AC4 — An unrecognised C@G job category does not cause the opportunity to disappear**

Given C@G introduces a job category not yet mapped to a WOG label,
When the officer browses the listing,
Then the opportunity still appears — it is not missing from results and does not cause an error.

---

## Job Category Mapping Reference

Both C@G and OTG translate to a WOG filter label at ingestion. The table below shows what maps to each WOG filter. For engineering use — officers see only the WOG label.

C@G source: `cag_field_set.json` (SAP OData v2). OTG source: job_family field in OTG Excel import. Volumes as of May 2026.

| WOG Filter Label | C@G Code(s) | C@G Label(s) | OTG Job Family |
|---|---|---|---|
| Arts & Culture | 0003 | Arts/Cultural/Heritage | Arts & Culture; Library & Archives |
| Corporate Administration | 0002, 0025 | Administration Support; Others | Corporate Administration |
| Education & Skills Development | 0010, 0034 | Education; Training and Development | Academic Operations; Education & Skills Devt |
| Emergency Preparedness & Response | 0015, 0031 | Home Team Uniformed Services; Singapore Armed Forces (inactive) | Emergency Preparedness & Response |
| Environment & Resources | 0020 | Landscape/Horticulture | Environment & Resources |
| Finance | 0001 | Accounting, Audit, Finance | Finance and Accounting |
| Governance, Risk & Controls | — | — | Governance, Risk & Controls |
| Healthcare | 0014 | Healthcare | — |
| Human Resource | 0016 | Human Resources | Human Resources |
| Industry & Sector Development | — | — | Industry & Sector Development; Industry & Sector Devt |
| Infocomm Technology & Smart Systems | 0017 | InfoComm, Technology, New Media Communications | Infocomm Tech & Smart Systems; Infocomm Technology & Smart Systems |
| Internal Audit | — | — | Internal Audit |
| International Relations | 0013, 0018 | Foreign Service; International Relations | Int'l Relations |
| Land & Estate Management | 0004 | Building and Estate Management | Land & Estate Mgmt; Land Sales Admin |
| Legal | 0005, 0006 (inactive), 0021 | Conciliation/Mediation; Conciliation/Mediation and Statistics; Law/Legal Services | Legal |
| Organisation Development | 0024, 0028 | Organisation Development; Public Service Leadership | Corporate Development; Organisation Devt |
| Partnership & Engagement | — | — | Citizen Engagement; Partnership & Engagement |
| Planning | 0007 | Corporate Strategy/Top Management | Planning |
| Policy & Planning | 0026 | Policy Formulation | Policy & Planning |
| Procurement | — | — | Procurement |
| Programme & Project Management | — | — | Programme & Project Mgmt |
| Programme Evaluation | — | — | Programme Eval |
| Public Communications | 0022, 0027, 0035 (inactive) | Marketing/Business Development; Public Relations/Corporate Communications/Psychology; Translators/Interpreters | Public Comms; Strategic Communications |
| Regulatory | 0011, 0019, 0023 | Enforcement; Investigation; Occupational Safety and Health | Compliance & Enforcement; Enforcement; Regulatory |
| Research & Innovation | 0009, 0029, 0033 | Economics/Statistics; Research and Analysis; Statistics | Research; Research & Innovation |
| Science, Tech & Engineering | 0012, 0030 | Engineering; Sciences (life sciences, bio-technology) | Science, Tech & Engrg; Technical Capbability |
| Service Delivery | 0008 | Customer Service | Service Delivery |
| Social & Community Services | 0032 | Social and Community Development | Social & Community Services |
| Trade & Economy | — | — | Trade & Economy |
| Urban & Physical Planning | — | — | Development Services and Planning; Urban & Physical Planning; Urban Planning and Design |

Full mapping reference and BO decision log: `context-library/decisions/wog-taxonomy-mapping.md`

---

## Out of Scope

- OTG job category mapping (Story 4 / OTEP-ingestion-v3-rule-updates.md)
- The filter UI and filter labels (OTEP-318)
- Job category reference table (OTEP-333)
