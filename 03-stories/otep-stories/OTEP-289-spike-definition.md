# OTEP-289: [Spike] Filter Opportunities by Functions

**Status:** Backlog  

**Timebox:** 2 days from start  

**Assignee:** Pow Hwee

---

## Description

C@G and OTG use different tagging schemes — C@G has its own function taxonomy; OTG uses Job Family + Job Function. Before building a filter, we need to know whether these can be normalized into a single unified list. This spike answers that question.

**Cut-line:** If the mapping is partial or messy, the filter is deferred to Sprint 3. The Sprint 2 goal (Listing → Detail end-to-end) does not depend on it.

---

## Acceptance Criteria

- [ ] A unified filter taxonomy is proposed — the exact values an officer would see — OR a documented recommendation to defer with rationale
- [ ] All unmapped values between C@G and OTG are identified with a handling recommendation
- [ ] A go/no-go decision on MVP feasibility is documented

---

## Expected Output

A written recommendation containing:
1. Mapping table: C@G value → OTG value → unified label
2. List of unmapped values + proposed fallback handling
3. Go/no-go call with rationale

No prototype required at this stage. Build decisions follow once the mapping is confirmed.

---

## Out of Scope

- Building the filter UI
- Implementing any taxonomy normalization logic
- SJR function tagging (SJR apply flow deferred to post-MVP)

---

*Defined: 2026-05-19. Owner: Pow Hwee. PM: Michelle.*

---

## PM Note — 2026-06-25: C@G Taxonomy as Canonical Filter Layer

**Architecture (confirmed 2026-06-25):**
- Canonical taxonomy = C@G's 33 FieldSet `Indus` codes and descriptions
- C@G: passthrough — `Indus` code stored directly as `job_family_code`, no translation needed
- OTG 27 → C@G Indus at ingestion via Dictionary 1 (hardcoded map)
- Frontend filter shows C@G Indus descriptions — source-agnostic from officer's perspective
- WOG 29 is NOT the display layer (Pow Hwee's architecture pattern accepted; canonical layer updated to C@G)

**Why C@G over WOG 29:** C@G taxonomy includes Healthcare (31 listings) as a distinct category. Under WOG 29, Healthcare had no home and fell to Others. C@G as the canonical layer makes Healthcare visible with no additional mapping work.

**WOG 29 reference list (retained for context, not used as display layer):** Arts & Culture, Corporate Administration, Education & Skills Development, Emergency Preparedness & Response, Environment & Resources, Finance, Governance Risk & Controls, Human Resource, Industry & Sector Development, Infocomm Technology & Smart Systems, Internal Audit, International Relations, Land & Estate Management, Legal, Organisation Development, Partnership & Engagement, Planning, Policy & Planning, Procurement, Programme & Project Management, Programme Evaluation, Public Communications, Regulatory, Research & Innovation, Science Tech & Engineering, Service Delivery, Social & Community Services, Trade & Economy, Urban & Physical Planning

---

### Dictionary 1: OTG 27 → C@G Indus

OTG uses 27 HR job family names. These must be translated to C@G Indus codes at ingestion. 13 clean matches, 12 partial, 2 with no C@G equivalent (fall to `0025` Others).

| OTG Job Family | C@G Indus | C@G Description | Match |
|---|---|---|---|
| Arts & Culture | 0003 | Arts/Cultural/Heritage | ✅ Clean |
| Education & Skills Development | 0010 | Education | ✅ Clean |
| Emergency Preparedness & Response | 0015 | Home Team Uniformed Services | ⚠️ Partial |
| Environment & Resources | 0025 | Others | ❌ No equivalent |
| Finance | 0001 | Accounting, Audit, Finance | ✅ Clean |
| Governance, Risk & Controls | 0007 | Corporate Strategy/Top Management | ⚠️ Partial |
| Human Resource | 0016 | Human Resources | ✅ Clean |
| Industry & Sector Development | 0022 | Marketing/Business Development | ⚠️ Partial |
| Infocomm Technology & Smart Systems | 0017 | InfoComm, Technology, New Media Communications | ✅ Clean |
| Internal Audit | 0001 | Accounting, Audit, Finance | ⚠️ Partial (merged with Finance) |
| International Relations | 0018 | International Relations | ✅ Clean |
| Land & Estate Management | 0004 | Building and Estate Management | ✅ Clean |
| Legal | 0021 | Law/Legal Services | ✅ Clean |
| Organisation Development | 0024 | Organisation Development | ✅ Clean |
| Planning | 0026 | Policy Formulation | ⚠️ Partial (collapses with Policy & Planning) |
| Policy & Planning | 0026 | Policy Formulation | ✅ Clean |
| Procurement | 0002 | Administration Support | ⚠️ Partial |
| Programme & Project Management | 0025 | Others | ❌ No equivalent |
| Programme Evaluation | 0029 | Research and Analysis | ⚠️ Partial (collapses with Research & Innovation) |
| Public Communications | 0027 | Public Relations/Corporate Communications/Psychology | ✅ Clean |
| Regulatory | 0011 | Enforcement | ✅ Clean |
| Research & Innovation | 0029 | Research and Analysis | ✅ Clean |
| Science, Tech & Engineering | 0012 | Engineering | ✅ Clean |
| Service Delivery | 0008 | Customer Service | ⚠️ Partial |
| Social & Community Services | 0032 | Social and Community Development | ✅ Clean |
| Trade & Economy | 0009 | Economics/Statistics | ⚠️ Partial |
| Urban & Physical Planning | 0004 | Building and Estate Management | ⚠️ Partial (collapses with Land & Estate Management) |

**Engineering note:** Dictionary 1 is a hardcoded Go map in the OTG transform layer. Full code in OTEP-ingestion Story 4. Accepted collapses: Finance + Internal Audit → 0001; Planning + Policy & Planning → 0026; Land & Estate Management + Urban & Physical Planning → 0004; Research & Innovation + Programme Evaluation → 0029; Environment & Resources + Programme & Project Management → 0025 (Others).

---

### Dictionary 2: C@G → C@G (Passthrough)

No translation. C@G `Indus` code is stored directly as `job_family_code`. All 33 C@G job functions are valid filter values. Healthcare (0014, 31 listings) is now visible in the filter.

**Engineering note:** No map needed for C@G. Store `Indus` value as-is.

---

### C@G Codes with No OTG Equivalent

These filter labels will only surface C@G opportunities — no OTG opportunities map to them.

| C@G Indus | Description | Listings |
|---|---|---|
| 0014 | Healthcare | 31 (was invisible under WOG 29) |
| 0013 | Foreign Service | 10 |
| 0034 | Training and Development | ~15 |
| 0020 | Landscape/Horticulture | 7 |
| 0023 | Occupational Safety and Health | 6 |
| 0005 | Conciliation/Mediation | 4 |
| 0028 | Public Service Leadership | 2 |
| 0031 | Singapore Armed Forces | 0 |
| 0035 | Translators/Interpreters | 0 |

---

### Go/No-Go Recommendation

**Go. C@G taxonomy as canonical filter layer, OTG → C@G Indus translation at ingestion.**

- Architecture: Pow Hwee's pattern (translation at ingestion, source-agnostic frontend) accepted. Canonical layer is C@G, not WOG 29.
- Dictionary 1 (OTG → C@G): 13 clean, 12 partial, 2 no-match. Hardcoded Go map, minimal engineering complexity.
- Dictionary 2 (C@G → C@G): passthrough, zero engineering work.
- Healthcare gap (WOG 29 approach): resolved. Healthcare (31 listings) now has its own filter category.
- Residual Others: Environment & Resources and Programme & Project Management (OTG-only families) fall to 0025 Others. Low officer impact.
- Warning log: `OTG_JOB_FAMILY_UNMAPPED` for unknown OTG values, `OTG_JOB_FAMILY_WARN` for partial-fit, `OTG_JOB_FAMILY_NULL` for blank, `CAG_INDUS_NULL` for missing C@G Indus — all distinct event types.

**What this unblocks:** OTEP-408 and OTEP-409 (ringfencing) continue using OTG Job Family directly — no dependency on this canonical layer. Dictionary 1 (OTG → C@G) must be wired before OTG opportunities appear in the filter alongside C@G opportunities (Sprint 4/5).

**Open: map ownership.** Who owns Dictionary 1 initial build and maintenance when OTG adds new job families? → @Michelle to confirm before S4 grooming.

---

*Updated: 2026-06-25. Architecture updated: C@G taxonomy as canonical filter layer (not WOG 29). Sources: HR-confirmed 27 OTG job families, cag_field_set.json (SAP OData v2), WOG 29 list (2026-06-25, reference only).*
