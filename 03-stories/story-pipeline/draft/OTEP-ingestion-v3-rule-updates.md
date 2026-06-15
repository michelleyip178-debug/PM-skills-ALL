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

## Grooming notes

- All three stories are chores — no officer-facing UI, no design needed, no BO UAT gate
- Dependencies: OTEP-192 merged to main before these are started (they modify the same transform layer)
- I-017 resolved 15 Jun 2026: Secondment = Internal Job. Story 2 branching logic is final — no further dependency.
- Suggest sizing together at one grooming session; Léo is the right person to estimate
- Target sprint: S4 if Léo has capacity after QA carry-ins close; S5 otherwise

*Draft by Michelle · 15 Jun 2026 · Pending grooming*
