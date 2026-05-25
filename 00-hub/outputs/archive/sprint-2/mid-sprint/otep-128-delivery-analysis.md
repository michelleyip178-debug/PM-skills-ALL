# OTEP-128: Delivery Analysis — View Opportunity Detail Page

**Sprint:** Sprint 2 (18–29 May 2026)
**Generated:** 2026-05-18
**Source:** Jira description + Pow Hwee comment (2026-05-18) + local story file (otg-lifecycle.md)

> **Legend:** ✅ Good · ⚠️ Needs Attention · ❌ Critical Gap

---

## 1. User Story & Acceptance Criteria Review

| Category | Analysis & Details |
|---|---|
| ✅ **Story Format** | The "As an officer… so that I can decide whether to apply" wrapper is correctly outcome-oriented. The user goal is clear. |
| ❌ **Mechanism Language** | Every AC in the Jira description opens with "The system must…" — this inverts the contract. Engineers read it as a technical spec and implement to the letter, not to the officer experience. All ACs need to be reframed with the officer as the subject. |
| ❌ | "The system must style the Type label identically to how it appears on the listing card" — this is an implementation instruction, not an outcome. An officer doesn't see styling directives; they see a consistent label. |
| ❌ **Error State Conflation** | The single "Opportunity not found" AC covers two distinct failure modes: a missing record (permanent — 404) and a system load failure (transient — 500). These produce different officer experiences. A 404 needs a "not found" message; a 500 needs a retry path. Pow Hwee's 2026-05-18 comment explicitly calls for the split. One AC cannot cover both. |
| ❌ **Closed Notice Misassigned** | "Display a clear 'This opportunity is closed' notice" belongs entirely to OTEP-129, which owns all open/closed labelling and deep-link state. Including it here creates double-counting and risks divergent implementations if either story ships without the other. Pow Hwee flagged this on 2026-05-18. **Remove from OTEP-128.** |
| ⚠️ **OTEP-285 Absorption Gap** | The local story file defers return-to-page behaviour to OTEP-285 ("Which page I return to is covered by OTEP-285"). OTEP-285 was absorbed into this story on 2026-05-18. Two must-have ACs are currently missing from OTEP-128: back navigation preserving page position via `?page=N`, and stable ordering across pages (posting_date + ID tie-breaker). Neither is in the Jira description. |
| ⚠️ **Mandatory Field Contract** | The local story file specifies: if any mandatory field is missing from the record, the page renders "Opportunity not found" — identical to an invalid ID. This is a contract-first decision with direct BE implications. The API must validate field completeness before returning 200. If this logic sits on the FE instead, every partial record becomes a silent rendering failure. This is absent from the Jira ACs entirely. |

### Refined Acceptance Criteria

| AC Group | Acceptance Criterion |
|---|---|
| ✅ Navigation In | When I click an opportunity card on the listing, I land on that opportunity's dedicated detail page. |
| ✅ Field Display | I can see the opportunity title, agency, posting date, closing date, type, role description, and commitment type on the page. |
| ✅ | If "What you'll develop" content exists for this opportunity, I see it. If it doesn't exist, that section does not appear — no blank header or empty space. |
| ✅ Date Format | All dates appear as full dates (e.g., "12 May 2026"). I do not see relative terms like "2 days ago." |
| ✅ Type Label | I can identify the opportunity type using the same label I see on the listing card. |
| ✅ Loading State | While the page is loading, I see a loading indicator. I do not see a blank page. |
| ✅ Back Navigation | I see a "Back to opportunities" link on the detail page. If I came from page 3 of the listing, clicking it returns me to page 3 — not page 1. |
| ✅ Direct URL Access | If someone shares the page URL with me directly, it opens without requiring me to navigate from the listing first. |
| ✅ Not Found | If the opportunity ID in the URL is invalid or the record does not exist, I see "Opportunity not found" with a link back to the listing. |
| ✅ Load Error | If the page cannot load due to a system error, I see an error message and a "Try again" option that re-attempts the load. |
| ✅ No Apply Action | There is no "Apply" button on this page. |
| ✅ Out of Scope | "This opportunity is closed" notice — owned by OTEP-129. Apply CTA, competency display, save for later, supervisor endorsement, similar opportunities — all deferred. |

---

## 2. Dependency Mapping

| Dependency Level | Item | Description |
|---|---|---|
| ⚠️ **External** | Amber's Figma design | Confirmed linked in Jira (2026-05-13). Design lock date (open item #22) not yet set — without it, mid-sprint design changes are unconstrained. Agree a lock date at the Design Review on Tue 14:00 before any FE work begins on layout. |
| ⚠️ **External** | OTG data import field shape | "What you'll develop" is confirmed available from OTG but the exact format (plain text, structured list, HTML) is still being confirmed during OTEP-192 import work. BE cannot finalise the field contract for this field until format is known. |
| ⚠️ **Internal** | OTEP-85 listing page + card click handler | The officer cannot reach the detail page until OTEP-85 ships the card component with a click action. OTEP-128 is unreachable end-to-end without it. OTEP-85 is the sequencing dependency for integration testing. |
| ⚠️ **Internal** | OTEP-85 type label component | The type label on the detail page must be visually identical to the listing card. FE must reuse the OTEP-85 component — not rebuild it. This component must be merged before OTEP-128's layout work can be completed. |
| ⚠️ **Internal** | OTEP-267 pagination — `?page=N` param | Pow Hwee's absorbed OTEP-285 ACs specify that back navigation preserves page position via URL query params. The pagination approach (`?page=N`) must be agreed between FE and BE before the "Back to opportunities" link is wired — FE reads the param and constructs the return URL. |
| ❌ **Internal** | OTEP-129 closed-opportunity notice | OTEP-129 owns the "This opportunity is closed" notice. If OTEP-128 ships before OTEP-129, an officer who opens a closed opportunity via direct URL sees a normal-looking page with no indication it is closed and no apply action. The gap is worse than the closed state — the officer has no cue. Sequencing must be confirmed at grooming. |
| ⚠️ **Internal** | OTEP-268 error state component | OTEP-128's 500 error state ("couldn't load this opportunity") and OTEP-268's listing error state may share a component. FE should build the error component to be reusable rather than page-specific. |

---

## 3. Task Breakdown & Effort Estimation

### Front-End (FE) Subtasks

| Task Name | Estimate | Justification |
|---|---|---|
| ⚠️ Detail page route + full layout from Amber's Figma | 1d | Scaffold covers all mandatory field slots, three optional fields with conditional hide logic, and the back-navigation link — the highest-effort FE task on this story. |
| ⚠️ Wire `GET /opportunities/:id` and render 200 response | 0.5d | Standard API integration; field mapping is explicit from the BE contract once it is shared. Blocked until the API contract document is published. |
| ✅ Loading indicator state | 0.25d | Reuse the spinner pattern from OTEP-85's listing page; no new component required. |
| ✅ Optional field conditional rendering (three fields) | 0.25d | Each optional section must suppress its label and container when the API returns null — requires defensive render guards on "What you'll develop," commitment type, and ministry icon. |
| ⚠️ "Back to opportunities" link with `?page=N` preservation | 0.5d | Must read the page query param from the incoming URL context and construct the return link; must default to page 1 when the param is absent (direct-URL-access case). |
| ✅ 404 not-found state | 0.25d | Render "Opportunity not found" with a listing link on API 404 response; single-path component. |
| ✅ 500 load-error state with retry handler | 0.25d | Render error message and re-fetch trigger on API 500; reuse error component from OTEP-268 if available. |
| ⚠️ Type label component reuse from OTEP-85 | 0.25d | Import and render the existing component — no rebuild. Blocked until the OTEP-85 type label component is merged. |
| ✅ FE integration tests: five states + back-nav with and without `?page=N` | 0.5d | Six test scenarios covering 200, 404, 500, direct URL access, back-nav with page param, and back-nav without page param — the last two cover the sequencing gap with OTEP-267. |
| **FE Total** | **~3.75d** | |

### Back-End (BE) Subtasks

| Task Name | Estimate | Justification |
|---|---|---|
| ✅ `GET /opportunities/:id` endpoint — single record lookup | 0.5d | Primary-key lookup; response shape maps directly from the agreed field contract. Straightforward query, but the field contract document must be completed before FE integration begins. |
| ⚠️ Mandatory field validation — return 404 if any required field is null | 0.5d | Contract-first guarantee: BE validates all six mandatory fields before returning 200. Requires explicit null-checks and a structured error body on failure; the field completeness test is the highest-value BE test on this story. |
| ⚠️ Closed opportunity handling — return 200 for past-`closing_date` records | 0.25d | Detail endpoint intentionally diverges from the listing visibility rule: a closed record is still accessible by ID and must return 200. This divergence must be explicit in code to avoid the listing filter being accidentally applied to the detail query. |
| ❌ API contract document: 200, 404, 500 response shapes | 0.25d | Three distinct shapes must be published and shared with FE before FE wiring begins. An undocumented shape forces FE to guess — this step unblocks FE earlier than waiting for the full endpoint. Must be done first. |
| ✅ Ordering guarantee — `posting_date` + ID tie-breaker | 0.25d | Consistent page position on back-navigation requires the listing to sort stably. Confirm the tie-breaker from OTEP-85's listing query is documented; no new logic if OTEP-85 already applies it. |
| ✅ BE unit tests: valid ID, invalid ID, mandatory field missing, closed record, server error path | 0.5d | Five test cases; the mandatory-field-missing test is the most critical — it validates the contract-first guarantee before FE integration begins and prevents a class of silent rendering failures in production. |
| **BE Total** | **~2.25d** | |

---

## 4. Technical Risks & Edge Cases

| Risk Category | Description & Impact | Mitigation |
|---|---|---|
| ❌ **Contract boundary — mandatory field gap** | A record can exist in the database with a null mandatory field (e.g., role description missing after a partial OTG import). The API returns 200 with a null in the response body. The FE either crashes, renders an empty page, or silently hides the core content — all of which look like a broken product to the officer without surfacing an actionable error. The listing will show the card (OTEP-85's visibility rule checks `closing_date`, not field completeness), so the officer can reach a broken detail page from a visible card. | BE validates all six mandatory fields before returning 200. If any are null, return 404 with a structured body and log the opportunity ID for data team review. The FE handles a partial record the same way it handles an invalid ID — "Opportunity not found." This is the contract-first guarantee: the FE must never be asked to decide what a null mandatory field means. |
| ⚠️ **Back-navigation with no page context** | An officer arrives at the detail page via a shared URL — no `?page=N` param exists in their URL. If the FE attempts to read a missing param without a defined default, the "Back to opportunities" link produces a malformed URL or navigates to an unexpected state. Impact is low-frequency but produces a broken navigation for a common sharing scenario. | FE reads `?page=N` as an optional param. When the param is absent, the back link defaults to page 1. The officer loses no context they came with — they arrived without page context and return without it. Document the default behaviour in the API contract so both FE and BE handle this case consistently. |
| ❌ **OTEP-128 / OTEP-129 delivery gap** | OTEP-129 owns the "This opportunity is closed" notice for the detail page. If OTEP-128 ships to a test environment before OTEP-129 is built, a closed opportunity accessed via direct URL shows a fully rendered detail page with no indication of closure and no apply action. An officer sees what appears to be an active opportunity they cannot act on — the silence is more confusing than a clear closed state. | Resolve sequencing at grooming: either OTEP-128 and OTEP-129 are committed to ship in the same sprint iteration (preferred), or OTEP-128 ships a minimal closed indicator scoped only to the direct-URL access case, which OTEP-129 then owns and refines. Do not ship OTEP-128 to production without a decision on this gap documented in both tickets. |

---

## Quick Reference — What to Action Before Grooming

| Action | Owner | Urgency |
|---|---|---|
| ❌ Remove "This opportunity is closed" AC from OTEP-128 Jira; note it belongs to OTEP-129 | Michelle | Before 10am Tue 19 May |
| ❌ Add two missing OTEP-285 ACs to OTEP-128: back-nav page preservation + stable ordering | Michelle | Before 10am Tue 19 May |
| ❌ Confirm OTEP-128 + OTEP-129 sprint sequencing — do they ship together? | Pow Hwee at grooming | In session |
| ⚠️ Agree design lock date (open item #22) with Amber | Michelle + Amber | Tue 14:00 Design Review |
| ⚠️ Publish BE API contract document (200/404/500 shapes) before FE wiring begins | Pow Hwee / Léo | Sprint 2 W1 |

---

*Generated: 2026-05-18 | Source: OTEP-128 Jira + Pow Hwee comment 2026-05-18 + otg-lifecycle.md*
