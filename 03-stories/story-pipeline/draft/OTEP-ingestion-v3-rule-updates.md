# OTG Ingestion — v3 Rule Updates (3 stories)

**Source:** I-013, I-014, I-015 ratified at OTG working session 12 Jun 2026

**Parent:** OTEP-192 (OTG data ingestion)

**Target sprint:** S4 or S5 (Léo to size at grooming)

**Type:** Chore (backend validation logic change — no officer-facing UI)

---

## Story 1: Update ingestion validation — job_function field is now optional (I-014)

**Title:** Update OTG ingestion validation: job_function is optional for all opportunity types

**Type:** Chore

**Assignee:** Léo Milbor (suggested)

**Story Points:** TBC at grooming

### Description

As the ingestion pipeline operator,
I want the transform layer to accept OTG rows where job_function is missing or unresolvable,
so that opportunities without a function tag are ingested rather than skipped.

**Context:**
Decision I-014 (ratified 12 Jun 2026) confirmed that job_function is optional and display-only for all opportunity types (Internal Job, Gig, STIP, PSFG). The current OTEP-192 implementation treats a missing or unresolvable job_function as a warning that still allows ingestion — however the original ACs did not reflect this clearly. This story locks in I-014 as the explicit rule and ensures the validation table and unit tests are updated to match.

This unlocked 174 previously blocked opportunities in the v3 analysis.

**Decision reference:** I-014. No UI changes required.

### Acceptance Criteria

**AC1 — Missing job_function does not skip the row**
Given an OTG row where job_function is missing or blank,
When the ingestion pipeline processes the row,
Then the row is ingested with job_function set to null (not skipped, not errored).

**AC2 — Unresolvable job_function does not skip the row**
Given an OTG row where job_function contains a value that cannot be resolved to a known function code,
When the ingestion pipeline processes the row,
Then the row is ingested with job_function set to null and a warning logged.

**AC3 — Run log reflects function-missing rows correctly**
Given a run that includes rows with missing or unresolvable job_function,
When the run summary log is produced,
Then those rows appear under "warnings" (not "skipped" or "errors").

**AC4 — Unit tests updated**
Given the updated validation logic,
When the unit test suite runs,
Then all tests pass and at least one test covers the missing job_function → ingest-with-null path.

**Out of scope:**
- UI display of function field (handled separately)
- C@G ingestion pipeline (separate transform layer)

---

## Story 2: Update ingestion validation — start_date optional for Job and Secondment (I-015)

**Title:** Update OTG ingestion validation: start_date optional for Internal Job and Secondment, required for Gig/STIP/PSFG

**Type:** Chore

**Assignee:** Léo Milbor (suggested)

**Story Points:** TBC at grooming

### Description

As the ingestion pipeline operator,
I want the transform layer to apply start_date validation by opportunity type,
so that Internal Job and Secondment rows without a start date are ingested, while Gig, STIP, and PSFG rows without a start date are still rejected.

**Context:**
Decision I-015 (ratified 12 Jun 2026) confirmed that start_date is optional for Internal Job and Secondment, but required for Gig, STIP, and PSFG. The current OTEP-192 implementation does not branch validation by type for this field. This story adds type-aware branching to the start_date check.

This unlocked approximately 261 previously blocked opportunities in the v3 analysis (combined with I-014).

Note: I-017 resolved 15 Jun 2026 — Secondment falls under Internal Job and is treated identically. No separate type branching required.

**Decision reference:** I-015. No UI changes required.

### Acceptance Criteria

**AC1 — Missing start_date on Internal Job does not skip the row**
Given an OTG row of type Internal Job where start_date is missing or blank,
When the ingestion pipeline processes the row,
Then the row is ingested with start_date set to null (not skipped, not errored).

**AC2 — Missing start_date on Secondment does not skip the row**
Given an OTG row of type Secondment where start_date is missing or blank,
When the ingestion pipeline processes the row,
Then the row is ingested with start_date set to null (not skipped, not errored).

**AC3 — Missing start_date on Gig, STIP, or PSFG still skips the row**
Given an OTG row of type Gig, STIP, or PSFG where start_date is missing or blank,
When the ingestion pipeline processes the row,
Then the row is skipped and logged as an error (behaviour unchanged from OTEP-192).

**AC4 — Run log reflects type-based branching correctly**
Given a run that includes rows of mixed types with missing start_date,
When the run summary log is produced,
Then Internal Job and Secondment rows with missing start_date appear under "warnings" (ingested), and Gig/STIP/PSFG rows with missing start_date appear under "errors" (skipped).

**AC5 — Unit tests updated**
Given the updated type-branching logic,
When the unit test suite runs,
Then all tests pass and tests cover: (a) Internal Job missing start_date → ingest, (b) Gig missing start_date → skip, (c) STIP missing start_date → skip, (d) PSFG missing start_date → skip.

**Out of scope:**
- end_date validation (separate field, not changed by I-015)
- C@G ingestion pipeline
- I-017 Secondment type reclassification (separate story if needed)

---

## Story 3: Update ingestion validation — time_commitment exempt for PSFG (I-013)

**Title:** Update OTG ingestion validation: time_commitment not required for PSFG (formerly agilePSD)

**Type:** Chore

**Assignee:** Léo Milbor (suggested)

**Story Points:** TBC at grooming

### Description

As the ingestion pipeline operator,
I want the transform layer to skip the time_commitment validation check for PSFG opportunities,
so that PSFG rows without a time_commitment value are ingested rather than skipped.

**Context:**
Decision I-013 (ratified 12 Jun 2026) confirmed that time_commitment (TC) is required for Gig and STIP only. PSFG (formerly agilePSD, reclassified under I-013) is TC-exempt — agilePSD opportunities do not carry a TC field and never did. The current OTEP-192 implementation was treating agilePSD/PSFG TC as TBC, which blocked all 29 PSFG rows. This story applies the confirmed rule.

This unlocked 29 previously blocked PSFG opportunities in the v3 analysis.

Note: The type name in the OTG source data may still appear as "agilePSD" — confirm with Léo whether the transform layer maps this to "PSFG" already (from OTEP-192 type-prefix logic) or whether a label update is also needed.

**Decision reference:** I-013. No UI changes required.

### Acceptance Criteria

**AC1 — Missing time_commitment on PSFG does not skip the row**
Given an OTG row of type PSFG (or source label agilePSD, mapped to PSFG) where time_commitment is missing or blank,
When the ingestion pipeline processes the row,
Then the row is ingested with time_commitment set to null (not skipped, not errored).

**AC2 — Missing time_commitment on Gig still skips the row**
Given an OTG row of type Gig where time_commitment is missing or blank,
When the ingestion pipeline processes the row,
Then the row is skipped and logged as an error (behaviour unchanged from OTEP-192).

**AC3 — Missing time_commitment on STIP still skips the row**
Given an OTG row of type STIP where time_commitment is missing or blank,
When the ingestion pipeline processes the row,
Then the row is skipped and logged as an error (behaviour unchanged from OTEP-192).

**AC4 — Run log reflects PSFG TC exemption correctly**
Given a run that includes PSFG rows without time_commitment,
When the run summary log is produced,
Then those rows do not appear under "errors" or "skipped" due to TC.

**AC5 — Unit tests updated**
Given the updated TC exemption logic,
When the unit test suite runs,
Then all tests pass and tests cover: (a) PSFG missing TC → ingest, (b) Gig missing TC → skip, (c) STIP missing TC → skip.

**Out of scope:**
- Internal Job and Secondment TC handling (TC not applicable to these types)
- C@G ingestion pipeline
- agilePSD → PSFG label remapping if already handled in OTEP-192 type-prefix logic

---

---

## Story 4: Filter taxonomy — translate OTG job_family to WOG job category at ingest

**Title:** Filter taxonomy: translate OTG job_family to WOG job category at ingest

**Type:** Chore

**Assignee:** Léo Milbor (suggested)

**Story Points:** TBC at grooming

### Description

As the ingestion pipeline operator,
I want the OTG transform layer to translate each opportunity's `job_family` to the corresponding WOG job category at ingest time,
so that OTG opportunities appear under the correct filter label in CareerCompass alongside C@G opportunities.

**Context:**
CareerCompass uses a 29-category WOG taxonomy as the canonical filter layer (decision: 2026-06-25). Both OTG and C@G translate their native classification to a WOG category at ingestion and store it as `wog_job_category`. This story covers the OTG side. C@G translation is in OTEP-437.

The translation dictionary is hardcoded — a new OTG job family requires a code deploy to update it. OTG A–K job families are pending confirmation; the map below covers L–Z only (confirmed 2026-06-25).

Full mapping reference: `context-library/decisions/wog-taxonomy-mapping.md`

**Decision reference:** OTEP-289 taxonomy decision (updated 2026-06-25 — WOG replaces C@G Indus as canonical).

### Acceptance Criteria

**AC1 — OTG job_family translated to WOG category at ingest**

Given an OTG opportunity with a known `job_family` value,
When the ingestion pipeline processes the record,
Then `wog_job_category` is stored as the corresponding WOG category from the hardcoded map.

```go
// otgToWOG maps OTG job_family strings to WOG job categories.
// WOG taxonomy is the canonical filter layer (decision 2026-06-25).
// HARDCODED: a new OTG job family requires a code deploy to update this map.
// Duplicate/abbreviated OTG variants are included as separate entries — match exact strings from source.
var otgToWOG = map[string]string{
    "Academic Operations":              "Education & Skills Development",
    "Arts & Culture":                   "Arts & Culture",
    "Citizen Engagement":               "Partnership & Engagement",
    "Compliance & Enforcement":         "Regulatory",
    // "Consultancy" — not present in OTG opportunity data (confirmed 2026-06-25); omit
    "Corporate Administration":         "Corporate Administration",
    "Corporate Development":            "Organisation Development",
    "Development Services and Planning": "Urban & Physical Planning",
    "Education & Skills Devt":          "Education & Skills Development", // abbreviated variant
    "Emergency Preparedness & Response": "Emergency Preparedness & Response",
    "Enforcement":                      "Regulatory",
    "Environment & Resources":          "Environment & Resources",
    "Finance and Accounting":           "Finance",
    "Governance, Risk & Controls":      "Governance, Risk & Controls",
    "Human Resources":                  "Human Resource",
    "Industry & Sector Development":    "Industry & Sector Development",
    "Industry & Sector Devt":           "Industry & Sector Development", // abbreviated variant
    "Infocomm Tech & Smart Systems":    "Infocomm Technology & Smart Systems", // abbreviated variant
    "Infocomm Technology & Smart Systems": "Infocomm Technology & Smart Systems",
    "Int'l Relations":                  "International Relations",       // abbreviated variant
    "Internal Audit":                   "Internal Audit",
    "Land & Estate Mgmt":               "Land & Estate Management",
    "Land Sales Admin":                 "Land & Estate Management",
    // "Learning & Development" — not present in OTG opportunity data (confirmed 2026-06-25); omit
    "Legal":                            "Legal",
    "Library & Archives":               "Arts & Culture",
    "Organisation Devt":                "Organisation Development",
    "Partnership & Engagement":         "Partnership & Engagement",
    "Planning":                         "Planning",
    "Policy & Planning":                "Policy & Planning",
    "Procurement":                      "Procurement",
    "Programme & Project Mgmt":         "Programme & Project Management",
    "Programme Eval":                   "Programme Evaluation",
    "Public Comms":                     "Public Communications",
    "Regulatory":                       "Regulatory",
    "Research":                         "Research & Innovation",          // legacy code; see otgWarnOnMap
    "Research & Innovation":            "Research & Innovation",
    "Science, Tech & Engrg":            "Science, Tech & Engineering",
    "Service Delivery":                 "Service Delivery",
    "Social & Community Services":      "Social & Community Services",
    "Strategic Communications":         "Public Communications",
    "Technical Capbability":            "Science, Tech & Engineering",    // typo in OTG source — map as-is; see otgWarnOnMap
    "Trade & Economy":                  "Trade & Economy",
    "Urban & Physical Planning":        "Urban & Physical Planning",
    "Urban Planning and Design":        "Urban & Physical Planning",      // legacy code; see otgWarnOnMap
}

// otgWarnOnMap flags OTG families with ambiguous, legacy, or data-quality issues.
// These fire a warning log on successful ingest for human review.
var otgWarnOnMap = map[string]bool{
    "Research":                  true, // legacy code — consolidates with Research & Innovation
    "Technical Capbability":     true, // typo in OTG source data
    "Urban Planning and Design": true, // legacy code — consolidates with Urban & Physical Planning
}
```

**AC2 — Unknown OTG job_family falls to null with warning log**

Given an OTG opportunity with a `job_family` value not in the map,
When the ingestion pipeline processes the record,
Then `wog_job_category` is stored as null and a warning is logged with the source job_family string and opportunity ID.
The record is not skipped.

**AC3 — Ambiguous OTG families fire a warning even when mapped**

Given an OTG opportunity whose `job_family` is in `otgWarnOnMap`,
When the ingestion pipeline processes the record,
Then the record is ingested normally AND a warning is logged for human review.

**AC4 — Warning log distinguishes unmapped from null job_family**

Given a run log containing both unmapped and null job_family warnings,
When the run summary is reviewed,
Then the two event types are distinguishable by event label (e.g. `OTG_JOB_FAMILY_UNMAPPED` vs `OTG_JOB_FAMILY_NULL`).

**AC5 — Unit tests cover key cases**

Given the updated OTG transform layer,
When the unit test suite runs,
Then tests cover: (a) known OTG job_family → correct WOG category, (b) unknown OTG job_family → null + warning, (c) ambiguous job_family → mapped WOG category + warning.

**Out of scope:**
- C@G Indus → WOG translation (OTEP-437)
- Filter UI (OTEP-318)
- ref_job_family reference table (OTEP-333)
- OTG A–K job families (add to map when confirmed)

---

## Grooming notes

- All four stories are chores — no officer-facing UI, no design needed, no BO UAT gate
- Dependencies: OTEP-192 merged to main before Stories 1–3 are started (they modify the same OTG transform layer)
- Story 4 touches the same OTG transform layer as Stories 1–3 — batch in the same sprint if possible
- Story 4 C@G side (OTEP-437) requires C@G ingestion pipeline to be established (OTEP-88 parent) — confirm with Léo before sizing
- Bundle Story 4 + OTEP-437 at grooming — they share the WOG category enum; put constants in one file
- I-017 resolved 15 Jun 2026: Secondment = Internal Job. Story 2 branching logic is final.
- Suggest sizing together at one grooming session; Léo is the right person to estimate
- Target sprint: S5. OTG A–K mapping must be confirmed before Story 4 is done.

*Draft by Michelle · 15 Jun 2026 · Updated 2026-06-25 — Story 4 rewritten: WOG taxonomy replaces C@G Indus as canonical filter layer (decision 2026-06-25). OTG → WOG map replaces OTG → C@G Indus map.*
