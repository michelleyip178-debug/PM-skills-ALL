# OTEP-127: [Spike] Define ringfencing display contract — OTG rules → CareerCompass listing

**Type:** Spike

**Status:** Backlog

**Assignee:** Michelle Yip

**Story Points:** 1

**Sprint:** OTEP-Pathfinder Sprint 4

**Child stories:** OTEP-408 (BE), OTEP-409 (FE)

---

## Description

**Goal:** Determine how CareerCompass enforces OTG ringfencing rules in the listing display. As-is ringfencing field mapping is known. Null/missing field = treat as open to all (resolved). This spike closes the remaining display UX questions so OTEP-408 (BE) and OTEP-409 (FE) can be estimated for S5.

**Timebox:** 0.5 day

**Questions to answer** *(BO sign-off needed — open-item #43):*

1. Display rule: hide the listing entirely vs show-but-disable the apply CTA for ineligible officers?
2. What is the ineligibility message copy, and how specific can it be?

**Already resolved:**

- OTG ringfencing field mapping — as-is known
- Storage at ingestion time — field on opportunity record
- Null/missing ringfencing field → treat as open to all
- EXCLUDE/blocklist format (MDDI edge case) → follow OTG behaviour: invert the blocklist at ingestion to derive the eligible agency set (all WOG agencies minus blocked list). Ingestion pipeline must handle both INCLUDE and EXCLUDE mode records from `RAW_GIG_AUDIENCE_FILTERS`.

**Expected output:**

- Confirmed display rule (hide vs disable) + message copy, signed off by BO
- Go/no-go on OTEP-408 (BE) and OTEP-409 (FE) for S5

## Out of scope

- POCDEX eligibility check — criteria are set in OTG, not derived from officer profile
- Criteria authoring UI — stays in OTG
- Competency matching (R1)

*Updated: 2026-06-17 — resolved questions removed (field mapping known, null = open to all). 2 open questions remain, both BO-gated. Points 3→1, timebox 2 days→0.5 day.*
