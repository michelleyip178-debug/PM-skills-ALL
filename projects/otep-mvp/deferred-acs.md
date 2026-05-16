# Deferred ACs Backlog

> Should-have / good-to-have / out-of-scope ACs lifted from story files. One source of truth for cut scope.
>
> **What lives here:** every "Good-to-have" line, every "Not in scope" item, every R1 deferral, and full ACs for stories deferred without a Jira ticket (e.g. OTEP-268).
>
> **What does NOT live here:**
> - Must-have ACs — those live in the story files
> - Process / stakeholder backlog — that's [`tasks/backlog.md`](../../tasks/backlog.md)
> - Missing-spec gaps — [`scoping-gaps-tracker.md`](scoping-gaps-tracker.md)
> - Chase items with owners and deadlines — [`context/open-items.md`](../../context/open-items.md)
>
> **Tier meanings:**
> - **Should** — promote-worthy if capacity opens up in the sprint, or first pull into the next sprint
> - **Good** — UI polish or quality-of-life; pull when natural
> - **Edge** — handles edge cases; pull alongside the parent story's hardening
> - **R1** — explicitly post-MVP, gated by a documented decision
>
> *Created 2026-05-15. Maintain by appending — never silently drop a row. If something gets pulled into a sprint, mark Status = Pulled and note the sprint.*

---

## How to read this

Grouped by **parent story**. Each row is one deferred AC. If a whole story is deferred without a Jira ticket, list all its ACs under that story's heading.

| Status legend |
|---|
| 🟡 Open — still deferred, candidate for a future sprint |
| 🟢 Pulled — moved into an active story (note which sprint) |
| 🔴 Dropped — explicitly killed, kept for audit trail |

---

## Sprint 2 stories — deferred ACs

### OTEP-85 — Display opportunity cards

| AC | Tier | Source | Date | Status |
|---|---|---|---|---|
| Long titles wrap to a maximum of 2 lines and trail off with "..." | Good | Good-to-have | 2026-05-14 | 🟡 Open |
| The agency's ministry icon appears next to the agency name | Good | Good-to-have | 2026-05-14 | 🟡 Open |
| The card shows whether the opportunity is full-time, part-time, or project-based | Good | Good-to-have | 2026-05-14 | 🟡 Open |
| Two opportunities posted the same day appear in a consistent order each visit | Good | Good-to-have | 2026-05-14 | 🟡 Open |
| If an opportunity has an unexpected type, the card still shows with a generic label instead of breaking | Edge | Good-to-have | 2026-05-14 | 🟡 Open |
| Filtering | — | Not in scope (Sprint 2) | 2026-05-14 | 🟢 Pulled → OTEP-86 (Sprint 3) |
| Sorting in different directions | Good | Not in scope | 2026-05-14 | 🟡 Open |
| Mobile or tablet layouts | Should | Not in scope (Sprint 2 desktop only) | 2026-05-14 | 🟡 Open — needs sprint placement |

### OTEP-85 (formerly OTEP-85a) — "Closing soon" label

> Re-absorbed into OTEP-85 on 2026-05-15. ACs below preserved for grooming reference. They apply as part of OTEP-85's scope.

| AC | Tier | Source | Date | Status |
|---|---|---|---|---|
| The label appears in a consistent position on every card (per Amber's design) | Good | Good-to-have | 2026-05-14 | 🟡 Open |
| Sorting or filtering by "Closing soon" | — | Not in scope | 2026-05-14 | 🟡 Open |
| Email reminders for closing-soon opportunities | R1 | Not in scope | 2026-05-14 | 🟡 Open |
| Custom thresholds (7 days is locked) | R1 | Not in scope | 2026-05-14 | 🟡 Open |

### OTEP-285 — Click-through + return-to-page state

| AC | Tier | Source | Date | Status |
|---|---|---|---|---|
| If I refresh the browser while on page 3, I stay on page 3 | Good | Good-to-have | 2026-05-14 | 🟡 Open |
| If I share the listing link while on page 3, the other person also lands on page 3 | Good | Good-to-have | 2026-05-14 | 🟡 Open |
| Remembering my scroll position | Good | Not in scope | 2026-05-14 | 🟡 Open |
| Remembering filters or search | — | Not in scope | 2026-05-14 | 🟢 Pulled into filter stories (OTEP-86 good-to-have) |
| Remembering state across browser sessions or tabs | R1 | Not in scope | 2026-05-14 | 🟡 Open |

### OTEP-267 — Pagination for listing page

| AC | Tier | Source | Date | Status |
|---|---|---|---|---|
| While the next page is loading, I see a spinner so I know it's working | Good | Good-to-have | 2026-05-13 | 🟡 Open |
| The page controls look and feel consistent with the rest of the platform | Good | Good-to-have | 2026-05-13 | 🟡 Open |
| Sharing a link to a specific page | Good | Not in scope | 2026-05-14 | 🟢 Pulled → OTEP-285 (good-to-have) |
| Placeholder skeleton loading animations | Good | Not in scope (spinner only for S2) | 2026-05-13 | 🟡 Open |
| Infinite scroll | Should | Not in scope | 2026-05-14 | 🟡 Open — decide at R1 |

### OTEP-128 — View opportunity detail page

| AC | Tier | Source | Date | Status |
|---|---|---|---|---|
| The agency's ministry icon appears next to the agency name | Good | Good-to-have | 2026-05-14 | 🟡 Open |
| The opportunity type label looks the same as on the listing card | Good | Good-to-have | 2026-05-14 | 🟡 Open |
| The browser tab shows the opportunity title | Good | Good-to-have | 2026-05-14 | 🟡 Open |
| "Save for later" | R1 | Not in scope | 2026-05-14 | 🟡 Open — per CLAUDE.md MVP guardrails |
| Supervisor endorsement (workflow) | R1 | Not in scope | 2026-05-14 | 🟡 Open — UI copy only in MVP |
| "Similar opportunities" | R1 | Not in scope | 2026-05-14 | 🟡 Open |
| Competency matching | R1 | Not in scope | 2026-05-14 | 🟡 Open |

### OTEP-268 — Empty / error / partial-load states (DEFERRED, UNTICKETED 2026-05-15)

> Whole story sidelined from Sprint 2. ACs preserved here as the only home until it's ticketed again.

| AC | Tier | Source | Date | Status |
|---|---|---|---|---|
| When the page can't load, show "We couldn't load opportunities" + retry button | Should | Was must-have | 2026-05-14 | 🟡 Open — should be in any future error-handling sprint |
| When most cards load but a few don't, render the successful ones; log failures silently | Should | Was must-have | 2026-05-14 | 🟡 Open |
| When a card is missing optional info, hide that piece — don't show blank space or break layout | Should | Was must-have | 2026-05-14 | 🟡 Open |
| Long agency names truncate with "..." + hover tooltip shows full name | Good | Good-to-have | 2026-05-14 | 🟡 Open |
| Automatic retries on failure | R1 | Not in scope | 2026-05-14 | 🟡 Open |
| "No opportunities" empty state | — | Not in scope (Sprint 2) | 2026-05-14 | 🟢 Pulled → Sprint 3 (lands with filters/search) |

---

## Sprint 3 stories — deferred ACs (drafted ahead)

### OTEP-86 — Filter opportunities by type

| AC | Tier | Source | Date | Status |
|---|---|---|---|---|
| Selecting filters and pressing browser back preserves filter selections | Good | Good-to-have (Sprint 3) | 2026-05-13 | 🟡 Open |
| Active filters are visually distinct — clear which types are selected | Good | Good-to-have (Sprint 3) | 2026-05-13 | 🟡 Open |
| If no results, prompt to broaden filters | Good | Good-to-have (Sprint 3) | 2026-05-13 | 🟡 Open |
| Filter counts per type (e.g. "Internal Job (12)") | Should | Not in scope | 2026-05-13 | 🟡 Open |
| Category / function filter | — | Not in scope | 2026-05-13 | 🟢 Tracked as US-03 |
| Competency filter | R1 | Not in scope | 2026-05-08 | 🟡 Open — decision 2026-05-08, competency match ratio descoped to R1 |

### US-05 — Clear filters and reset view

| AC | Tier | Source | Date | Status |
|---|---|---|---|---|
| "Clear all" also resets the URL back to the default unfiltered state | Good | Good-to-have (Sprint 3) | 2026-05-13 | 🟡 Open |
| "Clear all" takes me back to page 1 | Good | Good-to-have (Sprint 3) | 2026-05-13 | 🟡 Open |

### OTEP-87 — Detail page apply CTA + competencies

| AC | Tier | Source | Date | Status |
|---|---|---|---|---|
| I can see required competencies on the detail page | Should | Good-to-have (Sprint 3) | 2026-05-14 | 🟡 Open — blocked on open item #18 (competency data model) |
| If my profile is incomplete, I see a warning before I apply | Good | Good-to-have (Sprint 3) | 2026-05-14 | 🟡 Open — blocked on open item #20 (Amber, where to surface) |

---

## R1 backlog (MVP-excluded by decision)

> Items in CLAUDE.md "Out of MVP scope (R1)" or with explicit deferral decisions. Not tied to one story — these are programme-level.

| Item | Tier | Source decision | Date | Status |
|---|---|---|---|---|
| Competency proficiency levels (beyond binary) | R1 | MVP guardrails — decision 2026-05-08 | 2026-05-08 | 🟡 Open |
| "Save for later" feature across all stories | R1 | MVP guardrails — decision 2026-05-08 | 2026-05-08 | 🟡 Open |
| Supervisor endorsement workflow (backend) | R1 | MVP guardrails — decision 2026-05-08 (UI copy only in MVP) | 2026-05-08 | 🟡 Open |
| Recommendation / AI-matching engine | R1 | MVP guardrails | 2026-05-11 | 🟡 Open |
| Notifications (in-app + email) | R1 | MVP guardrails | 2026-05-11 | 🟡 Open |
| Competency match ratio / scoring | R1 | Decision 2026-05-08 — "What you'll develop" tags only for MVP | 2026-05-08 | 🟡 Open |
| Function / Job function mapping (OTG ↔ C@G) | R1 | Decision 2026-05-06 — non-matching taxonomies, mapping cost high vs unclear ROI | 2026-05-06 | 🟡 Open |
| US-07: Persist filter selections across sessions | R1 | story-id-map.md — within-session URL params sufficient for MVP | 2026-05-11 | 🟡 Open |
| US-P3: Pre-fill application from profile | R1 *(conditional)* | Pending FormSG URL-param support — open item #14 | 2026-05-08 | 🟡 Open — flips to MVP if FormSG supports |

---

## How to maintain this file

1. **When you cut an AC from a must-have during grooming** — copy it here under the parent story, set Tier and Status = 🟡 Open.
2. **When a sprint pulls a deferred AC back in** — change Status to 🟢 Pulled, note which sprint and Jira ticket.
3. **When a decision kills an AC for good** — change to 🔴 Dropped, link the decision in `context/decisions-log.md`.
4. **At Sprint 3 grooming and beyond** — scan this file's "Sprint 3 stories" section + R1 backlog. Pull anything that's earned its way back in.

---

*Created: 2026-05-15. Source files: `filters.md`, `otg-lifecycle.md`, CLAUDE.md MVP guardrails, `context/decisions-log.md`.*
