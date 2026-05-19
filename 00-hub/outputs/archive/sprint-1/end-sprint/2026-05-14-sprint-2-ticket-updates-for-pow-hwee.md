# Sprint 2 ticket updates — for Pow Hwee

**Date:** 2026-05-14
**Context:** Pow Hwee adopting contract-first approach; needs locked ACs by EOD to align with Thomas + Leo tomorrow.

**Sprint 2 scope (revised today):**
- OTEP-85 — Listing (absorbs OTEP-129)
- OTEP-267 — Pagination (already aligned)
- OTEP-268 — Empty / error / partial states (sharpened below)
- OTEP-128 — Detail page (written from scratch — was empty in Jira)
- OTEP-129 — **Closed, absorbed into OTEP-85**
- OTEP-86 (type filter) + US-05 (clear filters) — **Deferred to Sprint 3** to make room for detail page

---

## 1. OTEP-128 — View opportunity detail page

> Written from scratch. Jira ticket was empty ("US04" placeholder only).

**As an** officer,
**I want to** click into an opportunity card and see the full details on a dedicated page,
**So that** I can decide whether to apply without leaving OTEP.

### Acceptance Criteria

**Must-have (story fails without these):**

- [ ] Given I'm on the listing page, when I click an opportunity card, then I'm taken to a detail page for that opportunity
- [ ] On the detail page I can see: title, agency, posting date, closing date, type (Internal Job / SJR / STIPs & Gigs), description of the role, what I'll develop, and commitment type
- [ ] Dates are shown in absolute format ("12 May 2026"), not relative ("2 days ago")
- [ ] If the opportunity is closing within 7 days, a "Closing soon" label is visible
- [ ] I can return to the listing page from a clearly visible "Back to opportunities" link
- [ ] If I open or share the detail page link directly (e.g. from a bookmark), the page loads as expected without me needing to come from the listing first
- [ ] If the opportunity has closed (closing date has passed), I can still see the detail page but a clear notice tells me "This opportunity is closed" and there's no apply action
- [ ] If the opportunity doesn't exist (e.g. broken link), I see an "Opportunity not found" message with a way back to the listing
- [ ] There's no apply button on this page in Sprint 2 — apply flow comes later

**Good-to-have (cut if sprint is squeezed):**

- [ ] Ministry icon shown next to agency name (matches the listing card)
- [ ] Type label styled consistently with the listing card
- [ ] Browser tab title reflects the opportunity name

**Not in scope:**

- Apply button / FormSG redirect (Sprint 3 — US-18)
- "Save for later" (R1)
- Supervisor endorsement workflow (R1)
- "Similar opportunities" panel (R1)
- Competency match scoring (R1)

### What appears where — card vs detail

| Field | On card | On detail page |
|---|---|---|
| Title | ✅ | ✅ |
| Agency | ✅ | ✅ |
| Ministry icon | ✅ (nice-to-have) | ✅ (nice-to-have) |
| Type label | ✅ | ✅ |
| Posting date | ✅ | ✅ |
| Closing date | ❌ | ✅ |
| "Closing soon" label | ✅ (if ≤7 days) | ✅ (if ≤7 days) |
| Commitment type | ✅ (nice-to-have) | ✅ |
| Role description | ❌ | ✅ |
| What you'll develop | ❌ | ✅ |
| ~~Reporting line~~ | ❌ | ❌ (not in OTG data, resolved 2026-05-13) |

### Edge cases (UX)

- Closed opportunity opened directly → page loads with "closed" notice, no apply action
- Broken / invalid link → "not found" message with link back to listing
- Opportunity is missing an optional field (e.g. no "what you'll develop" text) → that section is hidden, page doesn't show an empty header

### Design dependency

Amber's detail page design — needs a lock date (open item #22). Flag at grooming if not ready.

### Risks

- Detail page design not yet locked (open item #22)
- "What you'll develop" content shape — confirmed available from OTG (resolved 2026-05-13), but exact format is being confirmed during import work

**Priority:** MVP

---

## 2. OTEP-85 — Display opportunity cards with real OTG data (UPDATED — absorbs OTEP-129)

> Changes vs current filters.md version: card is now clickable (links to detail page), "Closing soon" label promoted from OTEP-129, sort ACs absorbed.

**As an** officer,
**I want to** see OTG opportunities displayed as cards on the listing page,
**So that** I can scan what's available and click into ones I want to learn more about.

### Acceptance Criteria

**Must-have:**

- [ ] Given I'm logged in, when I navigate to the Opportunities page, then I see opportunity cards
- [ ] Each card shows me: title, agency, posting date (absolute format: "12 May 2026"), and a type label (Internal Job / SJR / STIPs & Gigs)
- [ ] I only see opportunities that are still open (closing date hasn't passed)
- [ ] **The newest opportunities appear first** (absorbed from OTEP-129)
- [ ] **Different opportunity types are mixed together by date, not grouped by type** (absorbed from OTEP-129)
- [ ] **If an opportunity is closing within 7 days, the card shows a "Closing soon" label** (absorbed from OTEP-129)
- [ ] On desktop, I see 15 cards on screen arranged as 3 columns × 5 rows
- [ ] **When I click a card, I'm taken to the detail page for that opportunity** (changed from view-only)
- [ ] I can tell the opportunity type at a glance without relying on colour alone — there's a clear label

**Good-to-have:**

- [ ] Long titles wrap to a maximum of 2 lines and trail off with "…"
- [ ] Ministry icon shown next to agency name
- [ ] Commitment type shown on the card
- [ ] **When two opportunities have the same posting date, they appear in a consistent order each time the page loads** (absorbed from OTEP-129)
- [ ] If an opportunity has an unrecognised type, the card still renders with a generic label (doesn't break)

**Not in scope:** Filter UI (OTEP-86, Sprint 3). Bidirectional sort. Mobile/tablet layouts.

**Priority:** MVP

---

## 3. OTEP-268 — Empty, error, and partial-load states for the listing

> Sharpened with concrete copy and behaviour. PM-mode decisions made on retry, partial loads, and message tone.

**As an** officer,
**I want to** see clear guidance when there are no opportunities or when something goes wrong,
**So that** I'm not confused by a blank or broken page.

### Acceptance Criteria

**Must-have:**

- [ ] **When there are no open opportunities to show:**
  - I see a heading: "No opportunities available right now"
  - Body text: "Check back soon — new opportunities are posted regularly."
  - An illustration accompanies the message (per Amber's design)
  - There is no "try again" button (this isn't an error — it's just empty)

- [ ] **When the page fails to load (e.g. server problem or no connection):**
  - I see a heading: "We couldn't load opportunities"
  - Body text: "Something went wrong on our end. Please try again."
  - A "Try again" button is shown, and clicking it reloads the opportunities
  - An illustration accompanies the message (per Amber's design)

- [ ] **When the page mostly loads but one or two individual cards can't render:**
  - The cards that loaded successfully are shown as normal
  - I do **not** see a broken / error screen
  - I do **not** see a warning that something failed (the failure is logged behind the scenes, not surfaced to me)
  - Pagination still shows the total number of opportunities, not just the rendered count

- [ ] **When a card is missing an optional piece of information** (e.g. no commitment type, no ministry icon):
  - The missing item is hidden, not shown as an empty space or placeholder text
  - The rest of the card looks normal

**Good-to-have:**

- [ ] If an agency name is very long, the card truncates it with "…" and shows the full name when I hover

**Not in scope:** Auto-retry on intermittent failures. Disabling filters with zero results (no filters in Sprint 2). Filter counts.

### PM-mode decisions made here (call out if you disagree)

1. **No retry button on the empty state.** Empty is a valid result, not a failure. A retry button would signal "something's broken" — wrong message.
2. **Partial failures render silently.** Don't tell the officer "1 record failed to load" — they'll wonder if they're missing the one they want. Engineering logs it instead.
3. **One generic error message.** Officers don't need to distinguish between different types of failures. "Something went wrong, try again" covers all of them.
4. **Government-tone copy, not chatty.** "We couldn't load opportunities" — not "Oops! 😅". Matches LifeSG tone.

**Priority:** MVP

---

## Suggested reply to Pow Hwee

Hi Pow Hwee,

Thanks for the heads-up on contract-first — agreed it's the right approach to decouple Thomas and Leo.

Three things in response:

**On scope.** You're right that Sprint 2 should deliver Listing → Detail end-to-end. I've adjusted the sprint to make room: OTEP-86 (type filter) and US-05 (clear filters) move to Sprint 3, OTEP-129 gets absorbed into OTEP-85 (sort and "Closing soon" label are already in scope there). Net Sprint 2: OTEP-85, OTEP-267, OTEP-268, OTEP-128 (detail page), and the existing type-badge requirement folded into OTEP-85.

**On the three tickets.** All three are sharpened in the attached doc:
- OTEP-85 — updated with the locked decisions (3×5 grid, type labels, sort, visibility) plus click-through to detail and the absorbed OTEP-129 ACs.
- OTEP-128 — written from scratch as the Detail Page story. Jira description was empty. Includes a card-vs-detail field comparison you can use to scope the data shape.
- OTEP-268 — concrete copy and behaviour for empty / error / partial-load states. I've made PM-mode calls on retry behaviour and partial-load handling; flag if any don't work for you.

ACs are written from the officer's perspective — what they see and do. I've deliberately kept implementation choices (endpoints, response shape, status codes) out of the tickets so you, Thomas, and Leo can shape that in tomorrow's contract sync.

**One risk to flag before tomorrow.** Open item #24 — the list of OTG Excel reports to ingest — is still open between us. Contract-first works as long as we have testable OTG data by Day 3-4 of Sprint 2. If #24 isn't closed by Friday, frontend will be mocking against the contract longer than we'd want. Can we close #24 in tomorrow's sync alongside the contract discussion?

Tickets updated in Jira by EOD today.

Michelle

---

## decisions-log.md entry (already added)

| 2026-05-14 | Sprint 2 scope reshuffled to deliver Listing → Detail end-to-end. Added OTEP-128 (Detail Page, was empty); absorbed OTEP-129 into OTEP-85; deferred OTEP-86 (type filter) and US-05 (clear filters) to Sprint 3. | Pow Hwee proposed contract-first approach to decouple FE/BE; end-to-end journey was the right S2 goal but original 5-story scope didn't include detail page. Filters can wait — they're discoverability polish, not the core "browse → see details" journey. | Michelle |
