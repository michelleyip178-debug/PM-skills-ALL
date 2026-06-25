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

## Story 4: Filter taxonomy — translate OTG job_family to C@G Indus code at ingestion; C@G Indus stored as-is

**Title:** Filter taxonomy: translate OTG job_family to C@G Indus code at ingest; store C@G Indus directly

**Type:** Chore

**Assignee:** Léo Milbor (suggested)

**Story Points:** TBC at grooming

### Description

As the ingestion pipeline operator,
I want the OTG transform layer to translate each opportunity's `job_family` to the corresponding C@G `Indus` code at ingest, and the C@G transform layer to store its `Indus` code directly without translation,
so that all opportunities share the same canonical filter taxonomy and the opportunity listing category filter shows a consistent set of labels.

**Context:**
C@G's 33 FieldSet `Indus` codes are the canonical filter taxonomy for CareerCompass (decision: 2026-06-25). C@G opportunities already use this taxonomy — their `Indus` code is stored directly as `job_family_code` (passthrough, no translation needed). OTG opportunities use a different taxonomy: 27 HR job family names (e.g. "Finance", "Human Resource"). The OTG ingestion transform layer must translate OTG `job_family` → C@G `Indus` code at ingest time.

The translation dictionary is hardcoded (no config table). A new OTG job family requires a code deploy to update the map.

**Decision reference:** OTEP-289 taxonomy decision, 2026-06-25.

### Acceptance Criteria

**AC1 — OTG job_family translated to C@G Indus code at ingest**

Given an OTG opportunity with a known `job_family` value,
When the ingestion pipeline processes the record,
Then `job_family_code` is stored as the corresponding C@G `Indus` code from the hardcoded map below (not the OTG job_family string, not any WOG label).

Hardcoded translation map (key = OTG `job_family` string, value = C@G `Indus` code):

```go
// otgJobFamilyToCAGIndus maps OTG job_family strings to C@G FieldSet Indus codes.
// Source: HR-confirmed 27-family OTG taxonomy + cag_field_set.json (SAP OData v2).
// C@G taxonomy is the canonical filter layer (decision 2026-06-25).
// HARDCODED: a new OTG job family requires a code deploy to update this map.
var otgJobFamilyToCAGIndus = map[string]string{
    "Arts & Culture":                      "0003", // → Arts/Cultural/Heritage
    "Education & Skills Development":      "0010", // → Education (Training & Development 0034 is a separate C@G code)
    "Emergency Preparedness & Response":   "0015", // → Home Team Uniformed Services (partial)
    "Environment & Resources":             "0025", // → Others (no C@G equivalent)
    "Finance":                             "0001", // → Accounting, Audit, Finance
    "Governance, Risk & Controls":         "0007", // → Corporate Strategy/Top Management (partial)
    "Human Resource":                      "0016", // → Human Resources
    "Industry & Sector Development":       "0022", // → Marketing/Business Development (partial)
    "Infocomm Technology & Smart Systems": "0017", // → InfoComm, Technology, New Media Communications
    "Internal Audit":                      "0001", // → Accounting, Audit, Finance (merged with Finance at code level)
    "International Relations":             "0018", // → International Relations
    "Land & Estate Management":            "0004", // → Building and Estate Management
    "Legal":                               "0021", // → Law/Legal Services
    "Organisation Development":            "0024", // → Organisation Development
    "Planning":                            "0026", // → Policy Formulation (partial; collapses with Policy & Planning)
    "Policy & Planning":                   "0026", // → Policy Formulation
    "Procurement":                         "0002", // → Administration Support (stretch)
    "Programme & Project Management":      "0025", // → Others (no C@G equivalent)
    "Programme Evaluation":                "0029", // → Research and Analysis (partial; collapses with Research & Innovation)
    "Public Communications":               "0027", // → Public Relations/Corporate Communications/Psychology
    "Regulatory":                          "0011", // → Enforcement
    "Research & Innovation":               "0029", // → Research and Analysis
    "Science, Tech & Engineering":         "0012", // → Engineering
    "Service Delivery":                    "0008", // → Customer Service (partial)
    "Social & Community Services":         "0032", // → Social and Community Development
    "Trade & Economy":                     "0009", // → Economics/Statistics (partial)
    "Urban & Physical Planning":           "0004", // → Building and Estate Management (partial; collapses with Land & Estate Management)
}

// otgJobFamilyWarnOnMap flags OTG job families where the C@G mapping is a stretch or results in a collision.
// These fire a warning log even when successfully mapped.
var otgJobFamilyWarnOnMap = map[string]bool{
    "Emergency Preparedness & Response": true, // Home Team Uniformed Services is not an exact fit
    "Environment & Resources":           true, // Falls to Others — no C@G equivalent
    "Governance, Risk & Controls":       true, // Corporate Strategy/Top Management is partial
    "Industry & Sector Development":     true, // Marketing/Business Development is partial
    "Internal Audit":                    true, // Merged with Finance at C@G code level — audit visibility lost in filter
    "Planning":                          true, // Collapses with Policy & Planning under 0026
    "Procurement":                       true, // Administration Support is a stretch
    "Programme & Project Management":    true, // Falls to Others — no C@G equivalent
    "Programme Evaluation":              true, // Collapses with Research & Innovation under 0029
    "Service Delivery":                  true, // Customer Service is partial
    "Trade & Economy":                   true, // Economics/Statistics is partial
    "Urban & Physical Planning":         true, // Collapses with Land & Estate Management under 0004
}
```

**AC2 — Unknown OTG job_family falls to "0025" (Others) with warning log**

Given an OTG opportunity with a `job_family` value not present in the map,
When the ingestion pipeline processes the record,
Then `job_family_code` is stored as `"0025"` (Others) and a warning is logged with the source job_family string and opportunity ID.
The record is not skipped.

**AC3 — Partial-fit OTG families fire a warning even when mapped**

Given an OTG opportunity whose `job_family` is one of the partial-fit values in `otgJobFamilyWarnOnMap`,
When the ingestion pipeline processes the record,
Then the record is ingested normally AND a warning is logged flagging it as a stretch or collision mapping.

**AC4 — C@G Indus code stored as-is (passthrough)**

Given a C@G opportunity with an `Indus` code,
When the ingestion pipeline processes the record,
Then `job_family_code` is stored directly as the `Indus` value — no translation applied. C@G values are the canonical taxonomy.

**AC5 — Warning log distinguishes OTG unmappable from OTG null job_family**

Given a run log containing both OTG unmappable warnings and OTG null job_family warnings,
When the run summary is reviewed,
Then the two event types are distinguishable by event label (e.g. `OTG_JOB_FAMILY_UNMAPPED` vs `OTG_JOB_FAMILY_NULL`).

**AC6 — Unit tests cover key cases**

Given the updated OTG transform layer,
When the unit test suite runs,
Then tests cover: (a) known OTG job_family → correct C@G Indus code, (b) unknown OTG job_family → "0025" + warning, (c) partial-fit job_family → mapped code + warning, (d) C@G record → Indus code stored as-is.

**Out of scope:**
- Building OTEP-333 (ref_job_family reference table) — that is a separate story
- C@G filter UI (OTEP-318)
- WOG canonical translation — C@G taxonomy is the display layer (not WOG)

---

## Grooming notes

- All four stories are chores — no officer-facing UI, no design needed, no BO UAT gate
- Dependencies: OTEP-192 merged to main before Stories 1–3 are started (they modify the same OTG transform layer)
- Story 4 OTG side touches the same OTG transform layer as Stories 1–3 — batch in the same sprint if possible
- Story 4 C@G side requires C@G ingestion pipeline to be established (OTEP-88 parent) — confirm with Léo before sizing
- I-017 resolved 15 Jun 2026: Secondment = Internal Job. Story 2 branching logic is final — no further dependency.
- Suggest sizing together at one grooming session; Léo is the right person to estimate
- Target sprint: S4 if Léo has capacity after QA carry-ins close; S5 otherwise. Story 4 C@G side is S5 at earliest.

*Draft by Michelle · 15 Jun 2026 · Updated 2026-06-25 — Story 4 added; updated to C@G as canonical filter taxonomy (OTG → C@G Indus translation at ingestion)*
