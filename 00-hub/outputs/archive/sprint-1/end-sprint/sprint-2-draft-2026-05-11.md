# Sprint 2 Draft: Core Hub

**Sprint:** 2
**Dates:** May 19 – May 30 (2 weeks)
**Status:** Draft — for grooming May 19–20

---

## Sprint Goal

Officers can browse, filter by type, and scan all opportunity listings from both pipelines on a single authenticated page.

**What this proves:** The "one place to see it all" promise works. Officers see real OTG and C@G data, can tell the two apart, and narrow by type. No apply flow yet — that's Sprint 3–4.

---

## Candidate Stories

### OTEP-85: View all opportunities in one place

| Field | Value |
|-------|-------|
| Priority | MVP — this IS the core value prop |
| Owner | Leo / Thomas (FE), Pow Hwee (BE) |
| Depends on | OTG → OTEP pipeline delivering records (Sprint 1), C@G ingestion live |
| Design | Hub page layout, card grid, empty state — Amber (Sprint 1 deliverable) |
| DoR status | Blocked — needs pipeline confirmed working + Amber's card designs finalised |

**AC (from story file):**
- Listing page shows opportunities from both OTG and C@G
- Empty state or clear message when no opportunities match officer's profile

**Edge cases to groom:**
- One pipeline down — show the other, don't blank the page
- Officer has no profile yet — what do they see? (Needs decision)
- `is_published` field unconfirmed (open item #4) — how do we know which records to display?

**Sprint 2 scope note:** Ringfencing (filtering by officer's POCDEX profile) is Sprint 3 (OTEP-127). Sprint 2 shows all opportunities to all authenticated users.

---

### OTEP-86: Filter opportunities by type

| Field | Value |
|-------|-------|
| Priority | MVP — without filters, a unified page is unusable at 100+ listings |
| Owner | Leo / Thomas (FE), Pow Hwee (BE) |
| Depends on | OTEP-85 (listing must exist to filter against) |
| Design | Filter UI pattern — Amber (sidebar? chips? dropdown? — open item #9 in discussion) |
| DoR status | Partially ready — AC written, but filter options depend on Secondment decision |

**AC (from story file):**
- Select a type filter → only that type shown
- Clear a filter → full list returns
- Multi-select → OR logic (show any matching type)

**Open decision (blocks grooming):** Is "Secondment" a distinct type or sub-type of SJR? (Open item #12, owner: Jacky). This determines the filter option list: `[STIP, Gig, SJR, Internal Job, C@G]` vs `[STIP, Gig, SJR, Secondment, Internal Job, C@G]`.

**My recommendation:** Default to SJR as a single type for Sprint 2. If Jacky confirms Secondment is distinct, add it as a filter option in Sprint 3. Don't hold the story for this.

---

### OTEP-128: Identify opportunity source (OTG vs C@G)

| Field | Value |
|-------|-------|
| Priority | MVP — two-pipeline model needs visual clarity |
| Owner | Leo / Thomas (FE), Amber (design) |
| Depends on | OTEP-85 (card component) |
| Design | Source label on card + accessibility (not colour-alone) — Amber |
| DoR status | Ready to groom — AC written, no external blockers |

**AC (from story file):**
- Every card shows a clear source indicator
- C@G listings have visual cue that clicking leads off-platform

**Open design question:** What user-friendly labels replace "OTG" / "C@G"? Officers don't know these acronyms. Amber to propose options (e.g. "Internal" vs "Public Service" or "Careers@Gov").

---

### US-05: Clear filters and reset view

| Field | Value |
|-------|-------|
| Priority | MVP — basic UX hygiene |
| Owner | Leo / Thomas (FE) |
| Depends on | OTEP-86 (filter system must exist) |
| Design | "Clear all" button + active filter indicators — Amber |
| DoR status | Ready to groom — straightforward |

**AC (from story file):**
- "Clear all" removes all filters, shows full list
- Active filters are visible to the officer

**Edge case:** Does clearing also reset URL params? (Filter state is stored in URL per PRD Section 7.)

---

### OTEP-129: Sort by recency / posting date

| Field | Value |
|-------|-------|
| Priority | MVP — prevents page from feeling stale |
| Owner | Pow Hwee (BE sorting logic), Leo / Thomas (FE) |
| Depends on | OTEP-85, confirmed date field from OTG export |
| Design | Default sort order + sort control (if any) — Amber |
| DoR status | Blocked — `closing_date` vs `end_date` unconfirmed (open item #3) |

**AC (from story file):**
- "Most recent" sort puts newest first
- OTG and C@G interleaved by date, not grouped by source

**Open question:** OTG and C@G may use different date fields (posted date vs published date). Rama needs to confirm which field OTEP uses for sort. Also: evergreen postings with old creation dates but recently modified — use modified timestamp? (PRD open question #1.)

---

## Recommended OUT of Sprint 2

| Story | Why not Sprint 2 | When instead |
|-------|-------------------|-------------|
| US-03 (Category filter) | Blocked on categorisation model validation — 4 people haven't signed off yet (Amber, Pow Hwee, Adrian, Jacky/XZ) | Sprint 3, after hybrid model confirmed |
| OTEP-130 / Search | Search indexing infrastructure needs a spike first (scoping gap #4) | Sprint 3 |
| US-07 (Persist filters) | Confirmed R1 | R1 |

---

## Sprint 1 Prerequisites (must land by May 16)

These are make-or-break for Sprint 2. If any are red on May 16, Sprint 2 scope shrinks.

| Prerequisite | Status (as of May 11) | Risk |
|-------------|----------------------|------|
| Auth flows end-to-end (OTEP-71a–e) | In progress | Medium — multi-story auth chain |
| OTG → OTEP data pipeline delivering records | In progress | High — no story/ACs written; escalate if not testable by May 12 |
| C@G ingestion method confirmed | Open (Pow Hwee) | High — if unconfirmed, C@G cards can't render in Sprint 2 |
| Hub UI + card designs finalised (Amber) | In progress | Low — on track |
| POCDEX account creation (OTEP-72) | In progress | Medium |

**Escalation trigger:** If the data pipeline is not testable by May 12 (tomorrow), flag to Pow Hwee and Adrian. Sprint 2's listing page has nothing to display without it.

---

## Decisions Needed Before Grooming (May 19)

| # | Decision | Who | Impact if unresolved |
|---|----------|-----|---------------------|
| 1 | `closing_date` vs `end_date` — which does OTEP use? | Rama | OTEP-129 can't be groomed; sort logic undefined |
| 2 | `is_published` field name and values | Rama | OTEP-85 can't determine which records to show |
| 3 | Is Secondment a distinct type or SJR sub-type? | Jacky | OTEP-86 filter options undefined |
| 4 | Filter UI pattern (sidebar / chips / dropdown) | Amber | OTEP-86, US-05 design dependency |
| 5 | User-friendly labels for OTG vs C@G | Amber | OTEP-128 card design |
| 6 | Default sort order | Amber / Michelle | OTEP-129 — most recent? Or something else? |

**What doesn't block Sprint 2 grooming** (despite being marked "Before Sprint 2" in open items): `eligibility`, `formsg_url`, `reporting_line`, `developmental_outcome`. These fields matter for detail pages and apply flows (Sprint 3–4), not the listing page.

---

## Track Assignments

| Track | Stories | Team | Notes |
|-------|---------|------|-------|
| Frontend — Listing | OTEP-85, OTEP-128 | Leo, Thomas | Card component + grid layout + source labels |
| Frontend — Filters | OTEP-86, US-05, OTEP-129 | Leo / Thomas | Filter UI + clear + sort logic |
| Backend — Data | OTEP-85, OTEP-129 | Pow Hwee | API serving opportunity records, sort/filter queries |
| Design | Detail page + search UX | Amber | Sprint 2 design is for Sprint 3 stories |

---

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Data pipeline not delivering by Sprint 2 start | Medium | Critical — listing has nothing to show | Escalate by May 12; fallback: mock data for FE, pipeline catches up mid-sprint |
| C@G ingestion not confirmed | Medium | High — half the "unified" promise is missing | Worst case: Sprint 2 shows OTG-only, C@G added in Sprint 3 |
| Rama field confirmations don't arrive | Medium | Medium — OTEP-129 sort logic blocked | Proceed with `posted_date` assumption; adjust when confirmed |
| Filter UI not designed by May 19 | Low | Medium — OTEP-86 can't start FE work | Amber is on track; escalate if no design by May 16 |

---

## Sprint 2 Success Criteria

How will we know Browse & Discover is working before the apply flow exists?

| Signal | Measurement | Target |
|--------|------------|--------|
| Page renders with real data | Manual QA — listings from both pipelines visible | 100% of test accounts see listings |
| Filters work | Apply type filter → correct subset shown | All filter options return correct results |
| Source distinction is clear | Hallway test — can 3 officers tell OTG from C@G? | 3/3 identify correctly without prompting |
| Performance | Page load on government network | < 5s initial load |
| Empty state | Remove all matching records → empty state renders | No blank page |

---

## Story Numbering Flag

The release plan ([otep-mvp-release.md](../resources/otep-mvp-release.md)) uses different story IDs from the PRD. For example, the release plan's "US-03" maps to "OTEP-86" in the PRD (Filter by type), and "US-10" in the release plan maps to "OTEP-128" in the PRD (C@G indicator). This will cause confusion in grooming. Recommend aligning to PRD numbering as the canonical source before Sprint 2 grooming.

---

## Pre-Grooming Checklist (Michelle's actions by May 16)

- [ ] Chase Rama on items #1–4 (field confirmations) — only #3 and #4 actually block Sprint 2
- [ ] Chase Jacky on Secondment classification (#12) — or propose default (SJR only)
- [ ] Confirm with Amber: filter UI pattern + source labels ready for grooming?
- [ ] Confirm with Pow Hwee: pipeline testable? C@G ingestion method?
- [ ] Decide default sort order (recommend: most recent first)
- [ ] Align release plan story IDs to PRD numbering

---

*Draft: 2026-05-11 | Author: Michelle (with Claude)*
