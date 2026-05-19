# Categorisation Research: C@G and OTG Filters

**Created:** 2026-05-06
**Owner:** Michelle
**Decision to make:** Should we merge into one unified filter model, or keep two separate taxonomies?
**Due:** May 16 (aim for initial recommendation by May 8 sprint planning)

---

## Research Question

Officers will discover opportunities from both OTG and Careers@Gov in one place. How should we handle filtering when the two sources use different category systems?

---

## Step 1: Map Both Taxonomies

### OTG Filters

_Source: OTG "Refine Your Search" panel (screenshot, May 2026). Shows 130 suggested opportunities._

| Filter | Input Type | Values / Options | Notes |
|--------|-----------|-----------------|-------|
| Find Competencies | Search | Free-text competency lookup | "Find the competencies required for your opportunity and add them to your post for more accurate recommendations" |
| Keywords | Text input | Free-text | Optional |
| Start After | Date picker | Date | Default: today |
| End Before | Date picker | Date | Default: +1 month |
| Opportunity Type | Radio buttons | STIP and Gig / SJR | Only 2 options — mutually exclusive |
| Time Commitment | Dropdown combo | "No more than" + number + hours/day | 3-part filter |
| Agency | Dropdown | List of agencies ("In this Agency") | Likely officer's own agency by default? |
| Work Remotely | Checkbox | Yes/No | Simple boolean |
| Job Family | Dropdown | List of job families | Unknown how many options |
| Function | Dropdown | List of functions | Unknown how many options |

**Key observations:**
- OTG separates "Job Family" and "Function" as distinct dimensions
- Competency-based matching is a primary feature (top of panel)
- Opportunity Type is binary: STIP+Gig (grouped together) vs. SJR
- Time Commitment filter suggests many opportunities are part-time/flexible
- Agency filter suggests cross-agency discovery is possible

### Careers@Gov Filters

_Source: Careers@Gov filter panel (screenshot, May 2026)_

| Filter | Input Type | Values / Options |
|--------|-----------|-----------------|
| Employment type | Chips (multi-select) | Full-time, Traineeship, Internship, Contract, Others |
| Relevant experience required | Chips (multi-select) | 0–1 year, 1–3 years, 4–6 years, 7–9 years, >10 years |
| Organisations | Searchable checkbox list | Government agencies (Accountant-General's Dept, ACRA, A*STAR, AGC, AGO, Board of Architects, etc.) |
| Job function | Searchable checkbox list | 34 options (see below) |

**Job function values (full list):**
1. Accounting, Audit, Finance
2. Administration Support
3. Arts/Cultural/Heritage
4. Building and Estate Management
5. Conciliation/Mediation
6. Conciliation/Mediation and Statistics
7. Corporate Strategy/Top Management
8. Customer Service
9. Economics/Statistics
10. Education
11. Enforcement
12. Engineering
13. Foreign Service
14. Healthcare
15. Home Team Uniformed Services
16. International Relations
17. Investigation
18. Landscape/Horticulture
19. Law/Legal Services
20. Marketing/Business Development
21. Occupational Safety and Health
22. Organisation Development
23. Others
24. Policy Formulation
25. Public Relations/Corporate Communications/Psychology
26. Public Service Leadership
27. Research and Analysis
28. Sciences (e.g. life sciences, bio-technology etc.)
29. Singapore Armed Forces
30. Social and Community Development
31. Statistics
32. Training and Development
33. Translators/Interpreters

**Key observations:**
- C@G has a flat, explicit "Job function" list (34 items) — very detailed and public-sector specific
- No competency-based matching (unlike OTG's primary feature)
- "Employment type" is a C@G-only concept (OTG uses "Opportunity Type": STIP+Gig vs SJR)
- "Relevant experience" is C@G-only — OTG doesn't filter by experience level
- "Organisations" ≈ OTG's "Agency" — same concept, different label
- No time commitment filter (unlike OTG's hours/day model)
- No date range filter visible (unlike OTG's Start After / End Before)
- No remote work filter

---

## Step 2: Comparison

### Direct Overlaps (same concept, different label)

| OTG filter | C@G filter | Proposed unified label | Notes |
|-----------|-----------|----------------------|-------|
| Agency | Organisations | Organisation / Agency | Same concept — list of gov agencies. Likely same master list. |
| Function | Job function | Job function | OTG has "Function" dropdown; C@G has 34-item "Job function" checklist. Unknown if OTG's "Function" values match C@G's list. **Needs validation with Pow Hwee.** |
| Job Family | _(no equivalent)_ | — | OTG has "Job Family" as a separate dimension from "Function". C@G only has "Job function". These may overlap or be hierarchical (Job Family → Function). **Key question for unified model.** |

### Unique to OTG

| Filter | Notes |
|--------|-------|
| Find Competencies (search) | Primary matching mechanism. C@G has no equivalent. Tied to officer competency profiles. |
| Opportunity Type (STIP+Gig / SJR) | C@G doesn't have this — it's an OTG-specific categorisation. In OTEP, this becomes the "source/pipeline" indicator. |
| Time Commitment (hours/day) | Makes sense for STIPs/GIGs which are often part-time. C@G jobs are typically full-time roles. |
| Start After / End Before (dates) | OTG opportunities have clear time windows. C@G jobs are ongoing postings. |
| Work Remotely (checkbox) | C@G doesn't offer this filter. |

### Unique to C@G

| Filter | Notes |
|--------|-------|
| Employment type (Full-time, Traineeship, Internship, Contract, Others) | C@G concept — doesn't apply to OTG (STIPs/GIGs/SJRs are their own employment model). |
| Relevant experience required (year bands) | C@G filters by seniority. OTG relies on competency matching instead. |

### Conflicts (same label, different meaning)

| Label | OTG meaning | C@G meaning | Risk |
|-------|-------------|-------------|------|
| "Function" vs "Job function" | Different values — **confirmed NOT matching** C@G's list | 34 explicit public-sector job functions | OTG uses a different taxonomy for the same concept. Cannot simply unify by sharing the same dropdown. Mapping or reconciliation required. |

**Key finding (confirmed May 6):** OTG's "Function" dropdown values do **NOT** match C@G's 34-item "Job function" list. This means:
- The one filter dimension we hoped was directly unifiable is NOT a simple merge
- Any "unified Job function filter" would require a mapping layer between OTG and C@G taxonomies
- Alternatively, we show pipeline-specific function/job filters (simpler but less "unified")

---

## Step 2b: Summary of Filter Landscape

| Dimension | OTG | C@G | Unifiable? |
|-----------|-----|-----|-----------|
| What type of opportunity | Opportunity Type (STIP+Gig / SJR) | Employment type (Full-time / Traineeship / etc.) | **No** — fundamentally different models. Need a "source" or "type" meta-filter. |
| Which organisation | Agency | Organisations | **Yes** — same concept, likely same master list |
| What kind of work | Function + Job Family | Job function (34 items) | **No** — confirmed: OTG Function values do not match C@G's list. Mapping required or keep separate. |
| Seniority / experience | _(not available)_ | Relevant experience (year bands) | **No** — C@G only |
| Skills / fit | Find Competencies | _(not available)_ | **No** — OTG only |
| Time / duration | Time Commitment + Date range | _(not available)_ | **No** — OTG only |
| Location / mode | Work Remotely | _(not available)_ | **No** — OTG only |

---

## Step 3: Evaluate Options

### Option A: Unified taxonomy

One set of filters that maps both OTG and C@G opportunities into a single model.

| Criteria | Assessment |
|----------|-----------|
| Officer mental model | Good — officers see one simple system |
| Technical complexity | **High** — requires building a mapping layer between OTG Function and C@G Job function (confirmed they don't match). Also need to reconcile Opportunity Type vs Employment type. |
| MVP scope / speed | **Slow** — mapping work + data normalization before anything is usable |
| Future-proofing (Phase 4 migration) | Best long-term — clean unified model for when all agencies are on OTEP |

**Pros:**
- Cleanest officer experience — one filter system, no cognitive load about "sources"
- Sets up well for Phase 4 full migration
- Feels like "one platform" not "two systems duct-taped together"

**Cons:**
- Requires creating and maintaining a mapping between two mismatched taxonomies
- High upfront investment before MVP can ship
- Risk of bad mappings confusing officers more than separate lists would
- Who owns the mapping? Ongoing maintenance burden.

### Option B: Two separate filter models

Officers see different filter options depending on which pipeline they're browsing (or a "source" toggle).

| Criteria | Assessment |
|----------|-----------|
| Officer mental model | Weaker — officers must understand they're dealing with two systems |
| Technical complexity | **Low** — pass through each system's native filters as-is |
| MVP scope / speed | **Fast** — no mapping needed, can ship what exists |
| Future-proofing (Phase 4 migration) | Poor — creates tech debt. When OTG retires in Phase 4, filters need rework. |

**Pros:**
- Fastest to ship — no taxonomy mapping work
- No risk of bad mappings
- Each pipeline's filters are already tested with users
- Lower engineering effort

**Cons:**
- Officers experience two different filter systems on one page — confusing
- Undermines the "discoverable in one place" narrative (it's one page but two experiences)
- Creates tech debt for Phase 4 migration
- Doesn't encourage convergence

### Option C: Hybrid (recommended direction)

Unified where the data aligns; pipeline-specific where it doesn't. Officers get a consistent base experience with contextual extras.

| Criteria | Assessment |
|----------|-----------|
| Officer mental model | Good — shared filters feel unified; extras feel like "more detail" not "different system" |
| Technical complexity | **Medium** — one real unification (Organisation) + contextual display logic |
| MVP scope / speed | **Moderate** — faster than full unification, slightly more than pass-through |
| Future-proofing (Phase 4 migration) | Good — Organisation is unified now; Function mapping can be tackled in R1 when there's more data |

**Structure:**

```
Shared filters (always visible):
├── Organisation / Agency        ← unified (same master list)
├── Source (OTG / C@G / All)     ← new meta-filter to toggle pipelines
└── Keywords / Search            ← common to both

Contextual filters (shown based on source selection or opportunity type):
├── If OTG:
│   ├── Opportunity Type (STIP+Gig / SJR)
│   ├── Time Commitment
│   ├── Start After / End Before
│   ├── Work Remotely
│   ├── Job Family
│   └── Function (OTG's own list)
└── If C@G:
    ├── Employment type (Full-time / Traineeship / etc.)
    ├── Relevant experience
    └── Job function (C@G's 34-item list)

If "All" selected:
└── Only shared filters active (Organisation, Keywords)
    with results from both pipelines interleaved
```

**Pros:**
- Ships faster than full unification — Organisation is the only real merge
- Officer still sees "one place" (shared page, shared org filter, source toggle)
- Contextual filters feel like "drilling deeper" not "switching systems"
- Function/Job function mapping can be deferred to R1 without blocking MVP
- Clear path forward: unify more dimensions as data allows

**Cons:**
- "All" view has fewer filter options — could feel limited
- Requires design work on how contextual filters appear/disappear (Amber)
- Source toggle adds one extra concept officers need to understand

---

## Step 4: Recommendation

**Recommended approach:** Option C — Hybrid model

**Rationale:**
1. Full unification (Option A) is too expensive for MVP — the Function/Job function taxonomies don't match and building a mapping layer is non-trivial with unclear ROI until we have usage data.
2. Full separation (Option B) undermines our MVP target of "discoverable in one place" — it's just two systems on one page.
3. Hybrid gives us the "one place" experience (shared Organisation filter, source toggle, interleaved results) while being honest that these are two pipelines with different metadata. It's shippable for Dec '26.

**What this unblocks:**
- Design can start on the filter UX (Amber) — she knows the structure now
- Eng can build with a clear data model — shared Organisation, contextual per-pipeline
- US-03 acceptance criteria can be sharpened: "Job function" filters are pipeline-specific in MVP
- Defers Function mapping to R1 (one of the 13 scoping gap items → formally resolved as "deferred")

**What to validate next:**
- [ ] Confirm with Pow Hwee: is Organisation/Agency the same master list across both systems?
- [ ] Review with Amber: how does contextual filter show/hide feel in the UI? (tabs? accordion? progressive disclosure?)
- [ ] Confirm with Adrian: is "Source toggle" (OTG/C@G/All) acceptable as an officer-facing concept, or do we need friendlier labels?
- [ ] Check with Jacky/Xian Zhang: does this align with what steering expects from "unified"?

---

## Open Questions

1. ~~Where to pull OTG category list?~~ → Done (screenshot captured)
2. ~~Where to pull C@G category list?~~ → Done (screenshot captured)
3. Do officers currently think of these as "two different systems" or "one pool of opportunities"?
4. Is Organisation/Agency the same master list in both systems? (ask Pow Hwee)
5. What user-friendly labels should we use instead of "OTG" and "C@G" for the source toggle?
6. Should "All" view show zero contextual filters, or show a merged subset?

---

## Validation Plan

- [ ] Review with Amber (design feasibility)
- [ ] Review with Pow Hwee (technical feasibility)
- [ ] Present recommendation at sprint planning (Thu May 8)
