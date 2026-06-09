# Post-MVP: Personalised listing states (E1/E2 — incomplete officer profile)

**Type:** Story (placeholder — not yet in Jira)

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Scope:** Post-MVP / R1

---

## Background

Descoped from MVP on 2026-06-08 after confirming personalisation is not in MVP scope (OTEP-87 Out of Scope: "Personalisation of any kind").

E1/E2 were designed as listing-page states for officers with incomplete POCDEX profiles, where the listing falls back to an unfiltered feed + nudge banner. These states only make sense once the personalisation engine exists — without it, every officer sees an unfiltered listing regardless of profile completeness. Showing a "complete your profile" banner when profile data doesn't affect the listing yet is a trust problem.

## User story

As an officer with an incomplete POCDEX profile, I want to see a nudge to complete my profile when I land on the opportunities listing, so I understand why my results aren't personalised and know what to do about it.

## States

**E1 — No POCDEX profile data:**
- Unfiltered listing + persistent non-dismissible banner: "Complete your profile to get personalised matches" with CTA to profile page

**E2 — Partial POCDEX profile data:**
- Unfiltered listing + dismissible banner: "Your profile is incomplete. Update it to see better matches." — stays dismissed for the session

## Prerequisites before this can be built

- Personalisation engine in place (ranking/filtering listing based on POCDEX profile)
- Officer profile page built (CTA destination)
- POCDEX profile completeness API flag confirmed with Daryll's team
- Minimum viable profile fields defined (which fields = "complete enough" to trigger personalised results)
- Open item #18 resolved (competency data model, schema, method)
- Open item #41 resolved (competency dependencies + API calls)

## Design notes

- E1/E2 are banner variants, not new page states — the listing grid is unchanged
- Amber to spec the banner component (non-dismissible vs dismissible) when prerequisites above are met
- Related: OTEP-336 (competency matching on detail page) — both depend on POCDEX profile data being available

---

*Parked: 2026-06-08. Raise for R1 sprint planning once personalisation engine is scoped.*
