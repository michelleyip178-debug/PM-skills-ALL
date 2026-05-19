# OTEP-289: [Spike] Filter Opportunities by Functions

**Status:** Backlog  
**Timebox:** 2 days (19–20 May 2026)  
**Assignee:** Pow Hwee  
**Output due:** Before Sprint 2 grooming, Thu 22 May

---

## Description

C@G and OTG use different tagging schemes — C@G has its own function taxonomy; OTG uses Job Family + Job Function. Before building a filter, we need to know whether these can be normalized into a single unified list. This spike answers that question.

**Cut-line:** If the mapping is partial or messy, the filter is deferred to Sprint 3. The Sprint 2 goal (Listing → Detail end-to-end) does not depend on it.

---

## Acceptance Criteria

- [ ] Pull a real sample of function/category values from live C@G data (not assumed)
- [ ] Pull the distinct Job Family + Job Function values from the OTG Excel export
- [ ] Document the overlap: which values map cleanly, which are partial, which have no equivalent
- [ ] Propose a unified taxonomy — the exact list of filter labels an officer would see in the UI
- [ ] Flag any values that can't be mapped and state the recommended fallback
- [ ] Deliver a go/no-go recommendation: is a clean unified filter achievable for MVP?

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
