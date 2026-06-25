# OTEP-437: C@G ingestion: store job category directly (no translation needed)

**Type:** Chore

**Status:** Backlog

**Assignee:** Léo Milbor (suggested)

**Story Points:** TBC at grooming

**Note:** Can be bundled with Story 4 (OTG → C@G Indus translation, OTEP-ingestion-v3-rule-updates.md) or tracked separately. Confirm at grooming — the C@G side is simpler, so bundling likely makes more sense.

---

## Why this exists

CareerCompass uses C@G's 33 job categories as the filter taxonomy (decision: OTEP-289, 2026-06-25). C@G already tags each opportunity with an `Indus` code — the canonical value we want to show in the filter. There's no translation step needed.

This story makes sure we store that value cleanly at ingestion, so C@G opportunities show up in the right filter bucket from day one. OTG opportunities are the ones that need a translation map (Story 4 / OTEP-ingestion-v3-rule-updates). C@G is a straight passthrough.

---

## Story

As an officer browsing CareerCompass,
I want to filter opportunities by job category and see relevant C@G listings under the right label,
so that I don't miss opportunities just because they came from a different source.

---

## Acceptance Criteria

**AC1 — C@G opportunities appear under the correct job category filter**

Given an officer is on the opportunity listing page,
When they filter by a job category (e.g. Healthcare),
Then they see C@G opportunities tagged with that category in the results.

**AC2 — C@G and OTG opportunities appear together under the same filter label**

Given an officer filters by Education,
When results load,
Then they see both C@G Education listings and OTG Education & Skills Development listings in the same results — with no indication of which pipeline each came from.

**AC3 — Opportunities with a missing job category still appear**

Given a C@G listing arrives with no job category,
When the officer browses or filters by Others,
Then the listing is visible — it is not silently dropped from the results.

**AC4 — An unrecognised job category does not break the listing**

Given C@G introduces a new job category code not yet in the system,
When the officer browses the opportunity listing,
Then the listing appears under Others and the officer can still find it — no error, no missing record.

---

## C@G job category reference (35 codes, 33 active)

| Code | Description | Live listings |
|---|---|---|
| 0001 | Accounting, Audit, Finance | high |
| 0002 | Administration Support | 82 |
| 0003 | Arts/Cultural/Heritage | 7 |
| 0004 | Building and Estate Management | 65 |
| 0005 | Conciliation/Mediation | 4 |
| 0006 | Conciliation/Mediation and Statistics | ~0 |
| 0007 | Corporate Strategy/Top Management | 17 |
| 0008 | Customer Service | 32 |
| 0009 | Economics/Statistics | 33 |
| 0010 | Education | high |
| 0011 | Enforcement | high |
| 0012 | Engineering | high |
| 0013 | Foreign Service | 10 |
| 0014 | Healthcare | 31 |
| 0015 | Home Team Uniformed Services | 16 |
| 0016 | Human Resources | high |
| 0017 | InfoComm, Technology, New Media Communications | high |
| 0018 | International Relations | high |
| 0019 | Investigation | ~5 |
| 0020 | Landscape/Horticulture | 7 |
| 0021 | Law/Legal Services | 23 |
| 0022 | Marketing/Business Development | high |
| 0023 | Occupational Safety and Health | 6 |
| 0024 | Organisation Development | high |
| 0025 | Others | — |
| 0026 | Policy Formulation | high |
| 0027 | Public Relations/Corporate Communications/Psychology | high |
| 0028 | Public Service Leadership | 2 |
| 0029 | Research and Analysis | high |
| 0030 | Sciences (e.g. life sciences, bio-technology etc.) | ~10 |
| 0031 | Singapore Armed Forces | 0 |
| 0032 | Social and Community Development | high |
| 0033 | Statistics | ~5 |
| 0034 | Training and Development | ~15 |
| 0035 | Translators/Interpreters | 0 |

Source: `cag_field_set.json` (SAP OData v2). Listing counts as of May 2026.

---

## Not in scope

- OTG job family → C@G Indus translation (Story 4 / OTEP-ingestion-v3-rule-updates.md)
- The filter UI itself (OTEP-318)
- ref_job_family reference table (OTEP-333)
