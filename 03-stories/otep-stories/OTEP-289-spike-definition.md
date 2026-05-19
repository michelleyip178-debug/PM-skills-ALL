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
