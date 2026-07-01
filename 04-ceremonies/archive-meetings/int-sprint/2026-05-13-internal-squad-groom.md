# Internal Squad Groom — 13 May 2026

**Sprint:** Sprint 1 → Sprint 2 transition
**Attendees:** Michelle, Pow Hwee, Leo, Thomas, Amber, Rama (facilitator)

---

## Goal of meeting

- Finalize what flows from Sprint 1 → Sprint 2
- Refine and split stories for authentication, opportunities listing, data model, data ingestion, and pagination
- Clarify dependencies and team capacity (design/front-end/back-end)
- Align on ceremonies (stand-ups, grooming, mid-sprint review, planning)

## Authentication & user profile

- Keep authentication minimal for now: check if a user exists (by email) and support a basic profile (name, email).
- Full competency profile is out of scope for Sprint 2 and depends on another team.
- Large profile story to be split into sub-stories; only feasible parts go into Sprint 2.

## Opportunities data model & ingestion

- Need a harmonised opportunities data model that can support OTG (now) and Careers@Gov (later, likely Sprint 3-4).
- Opportunities data to be refreshed daily using OTG reports (Excel).
- Work is split into:
  - Story for designing the data model.
  - Separate story for ingesting OTG data into the DB (via script/manual load/one-off job) and linking it to the display story.

## Opportunities listing (Sprint 2 core)

- Authenticated officer can open OTEP and see OTG opportunities on a listing page.
- Each card shows: title, agency + ministry icon, commitment type, posting date, type label (SJR, STIPs & Gigs, Internal Job; OTG label removed).
- Show only active/published opportunities (closing date > today).
- Default sort: newest first by posting date.
- Desktop layout: 3x5 grid = 15 cards per page. Tablet/mobile layouts follow later; desktop is the firm commitment.
- Visual polish is secondary; functionality first for Sprint 2.

## Pagination

- Separate pagination story for Sprint 2, linked to the listing story.
- 15 cards per page; users can navigate between pages.
- No deep-linking requirement (don't need shareable "page 3" URLs).
- Use a simple spinner/progress indicator while fetching the next page; skeleton loading is a later enhancement.
- Follow LifeSG design system patterns for pagination controls.

## Empty states & error handling

- Support a simple "no results/no opportunities" message when the listing is empty, with layout intact.
- When filters/search return nothing, show a clear no-results state.
- If optional fields (e.g. commitment type) are missing, the card still renders correctly; missing values may be blank.
- More advanced behavior (disabling filters with zero results, showing counts, etc.) deferred to future improvements and may need cross-team + copywriting input.

## Design system & capacity

- Need a dedicated story for design system work so other squads can reuse components and reduce reliance on a single front-end dev.
- Front-end and design capacity are shared across squads; this is a risk and needs alignment with leadership.
- Longer-term expectation: engineers should own vertical slices (front+back) rather than strict front/back split.

## Story / backlog adjustments

- Overly broad stories (profile, opportunities) will be split into smaller, clearer pieces (model vs ingestion vs UI).
- OTG-related stories (e.g. OTEP-85, OTEP-192) will:
  - Specify exactly which OTG reports to ingest (STIPs & Gigs, SJR, audience filters, etc.).
  - Reflect that Sprint 2 listing covers OTG opportunities.
  - Link the ingestion, listing, and pagination stories together.
- Opportunity types on cards to be updated to remove OTG; keep Internal Job / SJR / STIPs & Gigs (apply via FormSG).

## Design lock & reviews

- A design lock date for Sprint 2 will be set; no major design changes after that point.
- Screenshots and design notes will be attached to Jira and backed by a design source of truth (with behavior/edge-case notes).
- There will be a design review for the next sprint review to showcase Sprint 2 work.

## Meetings & cadence

- Keep two-week sprints for now.
- Maintain daily stand-ups, a mid-sprint review (~25 May for Sprint 2), and sprint planning.
- One grooming session in the second week of a sprint to prepare the next sprint's stories.
- Developers get at least 1-1.5 days before sprint planning to break down and size stories.
- Joint meetings with the other squad to be used selectively, to avoid consuming too much development time.

---

## Decisions logged

→ `../../../../PM-OS/outputs/decisions/2026-05-29-W22-decisions-log.md` (9 entries added 2026-05-13 from this session)

## New open items

→ `context/open-items.md` (#22 design lock date, #23 harmonised data model, #24 OTG report specification, #25 profile story split)
