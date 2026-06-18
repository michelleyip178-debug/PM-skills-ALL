# OTEP-127: [Spike] Define ringfencing display contract — OTG rules → CareerCompass listing

**Status:** Backlog

**Assignee:** Michelle Yip

**Story Points:** 2

---

## Description

Determine how CareerCompass reads ringfencing criteria from OTG ingestion and enforces them in the listing display. Opportunity creation and criteria-setting stays in OTG — this spike defines the read-and-display contract only.

**Timebox:** 1 day

**Questions to answer:**
1. What field(s) in the OTG export carry ringfencing criteria, and what values do they take?
2. How does CareerCompass store the ringfencing criteria at ingestion time?
3. Display rule: hide entirely vs show-but-disable apply CTA for ineligible officers? *(Needs BO answer — open-item #43)*
4. What is the ineligibility message copy? *(Needs BO answer — open-item #43)*
5. Null/missing ringfencing field in OTG export — treat as unrestricted?

**Expected output:** OTG field mapping, confirmed display rule + message copy (BO sign-off), null behaviour documented, go/no-go on OTEP-408/409 for S5.

**Out of scope:** POCDEX eligibility check, criteria authoring UI (stays in OTG), competency matching (R1).

*Updated: 2026-06-17 — scope narrowed: creation/criteria stays in OTG, CareerCompass display only. 3→2 pts, 2 days→1 day.*

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
