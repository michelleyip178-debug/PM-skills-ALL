# Grooming Brief — Sprint 3 Prep
**Date:** 19 May 2026 (Sprint 2 Week 1 — Squad Grooming)
**Target sprint:** Sprint 3 (2 Jun – 13 Jun 2026)
**Session:** Internal squad grooming with Pow Hwee
**Prepared by:** /groom

---

## Pre-Session PM Actions (do before this meeting)

Two open items are explicitly flagged "before Sprint 2 grooming (Tue 19 May)":

| # | Item | Action | Urgency |
|---|---|---|---|
| #28 | OTEP-85 visibility rule conflict — AC currently says "Closing Date >= 7 days" AND "strictly in future." Pow Hwee suspects 7-day rule belongs in OTEP-129, not OTEP-85. | Confirm: OTEP-85 = `closing_date > today` only; OTEP-129 = "Closing soon" badge for <=7 days. Update OTEP-85 AC before session. | 🔴 Blocks Sprint 2 build |
| #29 | OTEP-289 [Spike] Filter Opportunities by Functions — no ACs, no timebox | Write: what is the expected output (recommendation doc, prototype, code spike)? How long is the timebox? Who reviews the output? | 🔴 Engineers can't start without this |

---

## Sprint 3 Story Readiness

| Story | Title | Status | What's missing |
|---|---|---|---|
| OTEP-86 | Filter opportunities by type | ✅ Ready | — |
| US-05 | Clear filters and reset view | ✅ Ready | — |
| US-18 | Apply via FormSG (basic redirect) | 🔴 Blocked | `formsg_url` not confirmed (open item #2, Rama/PSD Ops) — last unconfirmed OTG field. Can't size this story. |
| OTEP-87 | Enhance detail page: apply CTA + competencies | ⚠️ Needs work | Competency section is conditional on open items #18 and #20 — needs to be explicitly tiered as good-to-have (not must-have) before grooming. Apply CTA depends on US-18 (blocked). |
| OTEP-127 | Apply ringfencing criteria | ⚠️ Needs work | No ACs written. Eligibility rules undefined. Need OTEP-183 spike findings from Pow Hwee before we can write a word. |
| US-03 | Filter by category | 🔴 Blocked | Categorisation hybrid model not validated (Amber, Pow Hwee, Adrian, Jacky/XZ). No ACs written. |
| OTEP-110 | Login fail / clear error | ⚠️ Needs work | ACs exist in auth.md but not sharpened. Confirm Sprint 3 placement and scope. |
| WOG-04/05/06 | Auth edge-cases | ⚠️ Needs work | Confirm placement at Sprint 2 mid-sprint review (~26 May). Sprint 3 scope: all three or subset? |
| Search (keyword) | Keyword search (no ticket) | 🔴 Blocked (missing) | **No story exists.** Confirmed MVP requirement, no ACs, no Jira ticket. sprint-allocation.md explicitly flags this. Must be written before Sprint 3 grooming. |

**Headline:** 2 of 9 stories are truly ready to size. 4 are blocked on external inputs. Sprint 3 as drawn in sprint-allocation.md is already flagged as a heavy sprint — expect to push 2–3 stories to Sprint 4 at planning.

---

## Sprint 3 Capacity Note

The same Thomas-as-sole-FE constraint from Sprint 2 applies. Sprint 3 has:
- OTEP-86 + US-05 (filter UI — FE-heavy)
- OTEP-87 (detail page FE additions)
- US-18 (FE redirect logic)
- OTEP-127 (ringfencing — touches listing FE)
- Auth edge-cases (auth FE)

That's 5–6 FE-bound stories through one engineer. If Sprint 2 carry-over adds OTEP-268 or OTEP-193/192, the constraint bites harder. Name the cut-line at the start of grooming, not at the end.

---

## Gaps and Ambiguities

| # | Source | Gap | Risk |
|---|---|---|---|
| 1 | OTEP-127 | No ACs. Eligibility rules undefined — grade? agency type? seniority? POCDEX integration? | Can't size or build until Pow Hwee shares OTEP-183 findings |
| 2 | US-18 | AC literally contains "[ASSUMPTION: `formsg_url` confirmed — open item #2]" | If field doesn't land before Sprint 3, this story blocks OTEP-87's apply CTA too |
| 3 | OTEP-87 | Competency section — good-to-have in deferred-acs but not clearly marked as conditional in the story file | Risk: gets treated as must-have at planning, inflating sprint scope |
| 4 | US-03 | No ACs. "Category filter" is technically the hybrid model (Option C, 2026-05-06) — but what does that mean as a UI? Organisation filter + source toggle? Confirmation from Amber/Adrian needed before writing ACs | Blocked on validation meeting that hasn't been scheduled |
| 5 | Search | No story exists. sprint-allocation.md says "write this before Sprint 3 grooming." | MVP requirement with zero ACs — needs a new ticket, story, and sizing session |
| 6 | SJR card/detail treatment | Open item #20 (Amber) is marked "design finalised 2026-05-13" but the AC status says "confirm treatment at grooming." Which treatment did Amber land on: no button, "Coming soon" text, or hidden? | OTEP-87's SJR AC can't be tested without a confirmed treatment |

---

## Dependencies

| From | Depends on | Type | Status |
|---|---|---|---|
| OTEP-87 (apply CTA) | OTEP-128 (Sprint 2 base detail page) | Hard | On track |
| OTEP-87 (apply CTA) | US-18 (FormSG redirect — provides the CTA URL logic) | Hard | Blocked (#2) |
| US-18 | `formsg_url` confirmed in OTG export (Rama/PSD Ops, open item #2) | Hard external | 🔴 Open |
| OTEP-127 (ringfencing) | OTEP-183 spike results (POCDEX profile lookup, Sprint 1) | Hard internal | Spike done — findings not in any story file |
| US-03 (category filter) | Categorisation hybrid model validated (Amber/Adrian/Jacky/XZ) | Hard internal | Decision made 2026-05-06 but validation meeting outstanding |
| OTEP-86 (type filter) | OTEP-85 (listing page, Sprint 2) | Hard | On track if Sprint 2 ships |
| WOG-04/05/06 | Sprint 2 mid-sprint review confirmation (~26 May) | Soft | TBC |
| Search | Story to be written | Blocking | Nothing exists |

---

## Edge Cases Not Covered in Current ACs

| Story | Uncovered edge case | Recommended AC |
|---|---|---|
| OTEP-86 | OTG adds a new opportunity type not in our filter list | If an opportunity type doesn't match Internal Job, SJR, or STIP/Gig, it renders with a generic label — not blank, not broken |
| OTEP-87 | FormSG URL is valid but the form has been closed or deleted | Officer lands on a FormSG error page — OTEP shows a fallback message "This form may no longer be available" (same as US-18 edge case — carry it forward) |
| OTEP-127 | Ringfencing filters out ALL opportunities for a specific officer | Show "No eligible opportunities" message (not the generic empty state) — so officers know it's their eligibility, not a system issue |
| OTEP-86 + US-03 | Type filter and category filter active simultaneously | Interaction not designed. Two filters narrowing the same list — what happens when both produce zero results? |
| OTEP-110/WOG-04-06 | Auth token expires mid-session while browsing (not at login) | Is this in Sprint 3 scope, or handled by the session management AC? Confirm at grooming |

---

## Deferred ACs Worth Pulling Into Sprint 3

From `deferred-acs.md` — these were good-to-haves in earlier stories. Worth surfacing at grooming to prompt a capacity discussion:

| AC | Parent | Tier | Rationale for Sprint 3 |
|---|---|---|---|
| Active filters are visually distinct — I can see at a glance which types are selected | OTEP-86 | Good | Low FE effort; without it, filter UI feels unfinished |
| If no results, prompt to broaden filters | OTEP-86 | Good | Important once ringfencing lands in Sprint 3 — officers need direction |
| "Clear all" takes me back to page 1 | US-05 | Good | Natural behaviour, trivially included |
| "No opportunities" empty state (was OTEP-268 deferred AC) | OTEP-268 | Should | Makes sense in Sprint 3 once filters can produce empty results — doesn't make sense without filters |

---

## Data Hygiene Note

`sprint-checklists.md` is significantly stale (last updated 2026-05-13). Sprint 2's stories listed there (OTEP-85, OTEP-285, OTEP-128, OTEP-267, OTEP-276) diverge from the live picture:

| What checklists says | Reality (per sprint-status.md 2026-05-18) |
|---|---|
| OTEP-285 as separate Sprint 2 story | Absorbed into OTEP-128 |
| OTEP-276 as Sprint 2 story | Dropped (superseded by OTEP-252 Done) |
| OTEP-129 absorbed into OTEP-85 | Re-added as separate Sprint 2 story by Pow Hwee |
| OTEP-268 removed from Sprint 2 | Re-added to Sprint 2 by Pow Hwee |
| No OTEP-289 | Added to Sprint 2 board |

**Action:** Update sprint-checklists.md Sprint 2 section after this grooming session.

---

## Sprint 3 DoR Blockers (what needs to clear before Sprint 2 ends)

| Blocker | Owner | Status |
|---|---|---|
| `formsg_url` confirmed (gates US-18 and OTEP-87 apply CTA) | Rama + PSD Ops | 🔴 Open — item #2 |
| Categorisation hybrid model validated (gates US-03) | Amber / Pow Hwee / Adrian / Jacky+XZ | 🔴 Open — validation meeting outstanding |
| OTEP-183 spike findings documented (gates OTEP-127 AC writing) | Pow Hwee | 🟡 Spike done, findings undocumented |
| Search story written (gates search from being a gap at Sprint 3 planning) | Michelle | 🔴 Not started |
| SJR treatment confirmed (opens OTEP-87 SJR AC) | Amber | 🟡 Design done, confirmation outstanding (item #20) |
| Auth edge-cases confirmed for Sprint 3 (placement call) | Pow Hwee / Leo | 🟡 Deferred to mid-sprint review (~26 May) |

---

## What to Drive in This Session

1. **Get OTEP-183 findings on the table** — Pow Hwee has the spike results. Without them, OTEP-127 ACs can't be written and the sprint is going into planning with a blank story.
2. **Make the Sprint 3 cut-line explicit now** — US-03 and the Search story are both blocked on external inputs. Name now which stories drop to Sprint 4 if those don't clear by Sprint 3 start. Don't let planning surface this surprise.
3. **Confirm SJR treatment** (open item #20) — one question to Amber, one answer, unblocks OTEP-87 sizing.
