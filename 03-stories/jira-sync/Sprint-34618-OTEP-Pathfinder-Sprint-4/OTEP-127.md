# OTEP-127: [Spike] Define ringfencing display contract — OTG rules → CareerCompass listing

**Status:** Done
**Assignee:** Michelle Yip
**Story Points:** 3.0

---

## Description

Determine how CareerCompass enforces OTG ringfencing rules in the listing display. As-is ringfencing field mapping is known. Null/missing field = treat as open to all (resolved). This spike closes the remaining display UX questions so OTEP-408 (BE) and OTEP-409 (FE) can be estimated for S5. Timebox: 0.5 day Questions to answer (BO sign-off needed — open-item #43): Display rule: hide the listing entirely vs show-but-disable the apply CTA for ineligible officers? What is the ineligibility message copy, and how specific can it be? Already resolved: OTG ringfencing field mapping — as-is known Storage at ingestion time — field on opportunity record Null/missing ringfencing field → treat as open to all Expected output: Confirmed display rule (hide vs disable) + message copy, signed off by BO Go/no-go on OTEP-408 (BE) and OTEP-409 (FE) for S5 Out of scope: POCDEX eligibility check — criteria are set in OTG, not derived from officer profile Criteria authoring UI — stays in OTG Competency matching (R1)

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-01*
