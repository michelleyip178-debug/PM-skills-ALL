# OTEP-127: [Spike] Define ringfencing eligibility contract

**Type:** Spike

**Status:** Backlog

**Assignee:** Michelle Yip

**Story Points:** 3

**Sprint:** OTEP-Pathfinder Sprint 4

**Child stories:** OTEP-408 (BE), OTEP-409 (FE)

---

## Description

**Goal:** Define the eligibility contract that drives ringfencing — what POCDEX fields determine whether an officer is eligible for a given opportunity, and what the listing API contract looks like. This unblocks OTEP-127-B and OTEP-127-C.

**Timebox:** 2 days

**Questions to answer:**

1. What POCDEX fields drive eligibility for each opportunity type (Internal Job, Gig, STIP, SJR)?
2. What does the eligibility check look like at the API level — what does the listing API receive, and what does it return?
3. Are there edge cases in the eligibility matrix (e.g. grade bands, agency exceptions, scheme-of-service rules) that need to be scoped in or explicitly deferred?
4. What happens if POCDEX returns partial data — is an officer eligible, ineligible, or treated as unfiltered?

**Expected output:**

- Written eligibility matrix: POCDEX field → opportunity type → eligible/ineligible rule
- Draft API contract for the listing endpoint (what params, what filter logic)
- List of edge cases with in/out scope decisions
- Go/no-go recommendation on whether 127-B can start in S5 as planned

## Out of scope

- Implementation — spike output only
- Competency matching (separate concern, R1)

*Synced from Jira: 2026-06-11*
