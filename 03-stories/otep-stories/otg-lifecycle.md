# User Stories: OTG Application Lifecycle

**Epic:** Opportunities (Epic 4)

**One-pager:** _TODO: Confluence link_

**Status:** Draft — needs grooming

**Dependency:** WOG AD Login (officers must be authenticated to apply)

---

## Stories

### OTEP-128: View opportunity detail page (Sprint 2)

> **Repurposed 2026-05-14.** Was "Identify opportunity type on card" — that function absorbed into OTEP-85. Now the Detail Page story. Written from scratch. Sprint 2 base; OTEP-87 (Sprint 3) enhances with apply CTA and competencies.

**As an** officer,
**I want to** click into an opportunity card and see the full details on a dedicated page,
**So that** I can decide whether to apply without leaving OTEP.

**Acceptance Criteria:**

*Must-have:*
- [ ] When I click an opportunity card, I'm taken to that opportunity's detail page.
- [ ] I can see all mandatory fields from the field table below on the detail page.
- [ ] I see dates as full dates (e.g. "12 May 2026"), not relative terms like "2 days ago."
- [ ] I see a "Back to opportunities" link that takes me back to the listing. (Which page I return to is covered by OTEP-285.)
- [ ] If someone shares the page link with me, it opens directly — I don't need to start from the listing first.
- [ ] If the opportunity has already closed, I still see the details, but a notice tells me "This opportunity is closed" — no apply action shown.
- [ ] If the link is broken or the opportunity doesn't exist, I see "Opportunity not found" with a link back to the listing.
- [ ] While the page is loading, I see a spinner — not a blank page.
- [ ] I don't see an "Apply" button on this page. [DEFERRED to Sprint 3 — OTEP-87]

*Good-to-have:*
- [ ] The agency's ministry icon appears next to the agency name
- [ ] The opportunity type label looks the same as on the listing card
- [ ] The browser tab shows the opportunity title

*Not in scope:* Apply button (Sprint 3). "Save for later." Supervisor endorsement. "Similar opportunities." Competency matching.
*Now in scope (re-absorbed 2026-05-15):* "Closing soon" label on detail page (was OTEP-85a, now part of OTEP-85).

**Detail page field rendering rules:**

The page needs all mandatory fields to render. If a mandatory field is missing, the page shows "Opportunity not found" (same as a broken link) and the team logs it for review. Optional fields hide cleanly — no blank sections or empty headers.

| Field | Required? | If missing |
|---|---|---|
| Title | Yes | Page doesn't render |
| Agency | Yes | Page doesn't render |
| Type | Yes | Page doesn't render |
| Posting date | Yes | Page doesn't render |
| Closing date | Yes | Page doesn't render (drives "closed" banner logic) |
| Role description | Yes | Page doesn't render (the core content of the page) |
| What I'll develop | No | Section hidden — no empty header shown |
| Whether it's full-time / part-time / project | No | Field hidden |
| Ministry icon | No | Icon hidden; agency name still shows |
| ~~Reporting line~~ | No | Not in OTG data — field doesn't exist |

**API contract intent (for Pow Hwee):**
- Endpoint: `GET /opportunities/:id`
- Response: single opportunity object with all detail fields above
- Status codes: 200 (found), 404 (not found), 500 (server error → frontend shows error state per OTEP-268)
- Closed opportunities still load (with closed banner) — visibility rule applies to listing, not detail

**Subtasks:**

| # | Task | Track | Notes |
|---|------|-------|-------|
| 1 | `GET /opportunities/:id` endpoint with full field set | Backend | |
| 2 | Detail page route + layout (Amber's design) | Frontend | |
| 3 | Wire route to API + handle 200/404/500 | Frontend | |
| 4 | "Back to opportunities" navigation | Frontend | |
| 5 | Closed-opportunity banner state | Frontend | |
| 6 | Test: load by ID, closed banner, not-found state, direct URL access | Test | |

**Edge cases (UX):**
- Closed opportunity opened directly → page loads with "closed" notice, no apply action
- Broken / invalid link → "not found" message with link back to listing
- Opportunity missing an optional field (e.g. no "what you'll develop" text) → that section is hidden, page doesn't show an empty header
- No apply button in Sprint 2 → should officers see messaging explaining why? Currently silent — could confuse. Decide with Amber.

**Design dependency:** Amber's detail page design — finalised. Needs lock date (open item #22).

**Depends on:** OTEP-85 (listing page + card click handler must exist)

**Priority:** MVP

**Risks:**
- "What you'll develop" content shape — confirmed available from OTG (resolved 2026-05-13), but exact format being confirmed during import work
- Design lock date not yet set (open item #22)

---

### OTEP-87: Enhance detail page with apply CTA + competencies (Sprint 3)

> **Updated 2026-05-14.** Builds on OTEP-128 (Sprint 2 base). Adds: apply CTA (for Internal Jobs/STIPs/Gigs), SJR no-apply treatment, competency display. Only ACs NOT already in OTEP-128 are listed here.
>
> **⚠️ Jira ACs mismatch (2026-05-21 sync):** Jira title is "View Opportunity Detail" and ACs include competency match ratio ("X / Y competencies matched") and a competency section — scope we've deferred from Sprint 3. Reconcile Jira story before grooming: Sprint 3 scope = apply CTA only. Competency section is Sprint 4+.

**As an** officer,
**I want to** see how to apply and what competencies an opportunity requires,
**So that** I can decide whether to apply and understand the fit.

**Acceptance Criteria:** [DEFERRED to Sprint 3]

*Must-have (Sprint 3 additions only):*
- [ ] If I'm viewing an Internal Job, STIP, or Gig, I see a clear "Apply" button that links to the FormSG form.
- [ ] If I'm viewing an SJR, there's no apply action. [DEFERRED to future release — decision 2026-05-13]
- [ ] If the opportunity has closed, the apply button is not shown and I see "This opportunity is closed" instead.

*Good-to-have (Sprint 3):*
- [ ] I can see required competencies on the detail page. [ASSUMPTION: competency data model confirmed — open item #18]
- [ ] If my profile is incomplete, I see a warning before I apply. [ASSUMPTION: design decision on where to surface this TBD with Amber — open item #20]

**Dependencies:** OTEP-128 (base detail page), OTEP-319 (FormSG redirect), competency data model (#18)

**Priority:** MVP

---

### OTEP-319: Apply via FormSG — basic redirect (Internal Jobs, STIPs, Gigs) *(was US-18)*

> **Ticketed 2026-05-21 (Sprint 3 Jira sync).** `formsg_url` confirmed in OTG Export — 2026-05-21.

**As an** officer viewing an Internal Job, STIP, or Gig,
**I want to** click "Apply" and be taken to the corresponding FormSG form,
**So that** I can submit my application from the opportunity detail page.

**Acceptance Criteria:** [DEFERRED to Sprint 3]
- [ ] If I'm on an Internal Job, STIP, or Gig detail page and I click "Apply", I'm taken to the FormSG form for that opportunity in a new tab. [`formsg_url` confirmed in OTG export — 2026-05-21]
- [ ] If the `formsg_url` for an opportunity is missing, I see "Application form unavailable — contact the posting agency" instead of the Apply button.
- [ ] If I'm on an SJR detail page, there's no Apply button. [DEFERRED to future release — decision 2026-05-13]

**Edge cases:**
- `formsg_url` points to a form that has been closed or deleted — officer sees a FormSG error page (outside OTEP's control). Consider showing "Form may no longer be available" guidance.
- Officer clicks "Apply" but FormSG is down — new tab shows FormSG's own error. No OTEP-side handling needed for basic redirect.

**Dependencies:**
- OTEP-87 (detail page must exist)
- `formsg_url` field confirmed in OTG export (2026-05-21 — Rama + PSD Ops ✔). Field present for Internal Jobs, STIPs, Gigs. SJRs excluded (no apply flow in MVP — decision 2026-05-13).

**Sprint:** 3

**Jira:** OTEP-319 (ticketed 2026-05-21)

**Priority:** MVP — this is the core apply action for three of four opportunity types

**Risks:**
- FormSG form quality is outside OTEP's control — broken or closed forms create a bad officer experience with no OTEP-side fix beyond the fallback error state.

**Open questions:**
1. Does FormSG support pre-fill via URL params? (open item #14, Pow Hwee) — determines if US-P3 lands in MVP
2. Should the redirect include any OTEP tracking params (e.g. opportunity ID, officer ID) for analytics?

---

### OTEP-130: Apply to an OTG opportunity via FormSG (full, with webhook)

> **Sprint 4.** Builds on OTEP-319 (Sprint 3 basic redirect). OTEP-319 handles the redirect; OTEP-130 adds the webhook integration that makes OTEP aware a submission happened — enabling "already applied" state and the confirmation flow (US-10). These two stories must be groomed together.
>
> **Integration model decision needed before grooming:** OTEP-319 opens FormSG in a new tab. OTEP-130 assumes OTEP receives a webhook from FormSG on submission. If FormSG does not support outbound webhooks, the "already applied" indicator and US-10 confirmation screen cannot fire — the fallback is officer-declared confirmation (officer clicks "I've applied" on return to OTEP). Pow Hwee to confirm webhook support before Sprint 4 grooming.

**As an** officer,
**I want** OTEP to know when I've submitted a FormSG application,
**So that** I see an "already applied" indicator and can trust my application was received.

**Acceptance Criteria:**

*Must-have:*
- [ ] After I submit a FormSG application and return to the OTEP detail page, I see a "You've applied" indicator — the Apply button is no longer shown. [ASSUMPTION: OTEP receives a FormSG webhook on submission. If webhooks aren't available, see fallback AC below.]
- [ ] The "You've applied" indicator shows the date I submitted — not just a generic badge.
- [ ] If OTEP has not received the webhook within a reasonable window (e.g. 30 seconds), the Apply button is replaced with "Submitted via FormSG — check My Applications to confirm." Officers are not left with a stale Apply button.
- [ ] My submitted application appears in "My Applications" (US-14) as soon as OTEP receives the webhook — not on a delay.
- [ ] If I try to navigate back to the same opportunity and click Apply again, the Apply button is not shown — the "You've applied" state persists across sessions.

*Fallback (if FormSG webhooks are not available — confirm with Pow Hwee):*
- [ ] After I submit and return to OTEP, I see a prompt: "Did you complete your application on FormSG?" with a "Yes, I applied" button. Clicking this records my application in OTEP and shows "You've applied."
- [ ] This fallback is a temporary MVP workaround — document as tech debt in decisions-log.md.

*Not in scope:* Pre-fill from profile (US-P3 — R1 unless FormSG supports URL params). Email confirmation (open item #15 — R1). Duplicate submission prevention on FormSG side (outside OTEP's control).

**Edge cases:**
- [ ] Webhook arrives but opportunity has since closed — record the application anyway; don't reject on closed state.
- [ ] Webhook arrives for an officer whose session has expired — associate it with their profile via the officer ID in the payload; don't lose the submission.
- [ ] Officer submits the same FormSG form twice (duplicate) — OTEP records both if webhooks fire twice. Flag as an open question: does OTEP or FormSG deduplicate? (open question #3)
- [ ] Webhook payload is malformed or missing the opportunity ID — log and alert; show officer the fallback message above rather than a broken state.

**Dependencies:**
- OTEP-319 (FormSG basic redirect — must ship first; OTEP-130 adds webhook layer on top)
- FormSG webhook support confirmed (Pow Hwee — pre-grooming blocker)
- OTEP-71 (WOG AD auth — officer identity needed for webhook association)

**Sprint:** 4

**Priority:** MVP — without this, OTEP has no record of applications and tracking is impossible

**API contract intent (for Pow Hwee):**
- Inbound webhook: `POST /api/formsg/webhook`
- Payload (expected from FormSG): `{ opportunity_id, officer_id, submitted_at, form_response_id }`
- OTEP response: 200 on success; 400 on malformed payload; 500 logged internally
- OTEP stores: officer_id, opportunity_id, submitted_at, form_response_id, status = "Submitted"
- `GET /opportunities/:id` response must include `officer_applied: true/false` based on stored record

**Subtasks:**

| # | Task | Track | Notes |
|---|------|-------|-------|
| 1 | Inbound FormSG webhook endpoint (`POST /api/formsg/webhook`) | Backend | Confirm payload shape with Pow Hwee before Sprint 4 W1 |
| 2 | Application record model: officer_id, opportunity_id, submitted_at, form_response_id, status | Backend | Foundation for US-14–17 tracking group |
| 3 | `GET /opportunities/:id` — include `officer_applied` field in response | Backend | Drives "You've applied" UI state |
| 4 | "You've applied" indicator on detail page (replaces Apply button) | Frontend | Per Amber's design — confirm design exists before ticket moves to Ready |
| 5 | Fallback flow: "Did you apply?" prompt if no webhook received within 30s | Frontend | Only build if webhook not supported — confirm with Pow Hwee |
| 6 | Feature flag: `formsg_webhook_integration` (off = fallback mode) | Frontend/Backend | Flag controls which path is active |
| 7 | Test: webhook received → "You've applied" shown; My Applications updated | Test | |
| 8 | Test: webhook not received → fallback prompt shown | Test | |
| 9 | Test: officer returns to detail page in new session → "You've applied" persists | Test | |

**Design dependency:** Amber — "You've applied" detail page state + fallback prompt. Needs to be designed before this story is Ready.

**Risks:**
- If FormSG doesn't support outbound webhooks, the fallback (officer-declared confirmation) is a significant UX downgrade — and tracking (US-14–17) relies on OTEP having the application record. Resolve this before Sprint 4 grooming.
- Application record model built here is the foundation for the entire tracking group. Getting the schema wrong now means refactoring in Sprint 5.

**Open questions:**
1. Does FormSG support outbound webhooks? What's the payload shape? (Pow Hwee — pre-grooming blocker)
2. Does OTEP or FormSG deduplicate submissions if an officer submits twice?
3. How does the webhook authenticate to OTEP? (Shared secret, HMAC signature, IP allowlist?)

---

## Open Questions

1. **FormSG integration model** — embed (iframe) vs. redirect (new tab) vs. deep-link? Each has UX and technical trade-offs. (Pow Hwee + Amber). US-18 (Sprint 3) assumes basic redirect (new tab); OTEP-130 (Sprint 4) may embed.
2. **Pre-fill from profile** — can we pre-fill FormSG fields with officer data (name, email, agency)? Reduces friction. Blocked on open item #14.
3. **Application deduplication** — who handles this? OTEP or FormSG?
4. **Closed opportunity handling** — do we hide closed opportunities, grey them out, or show them with "closed" badge? Visibility rule confirmed: `closing_date` > today (2026-05-13).
5. **SJR card treatment** — SJRs are visible in listing but have no apply action in MVP. What does the card/detail page show? (open item #20, Amber)

## Definition of Ready Checklist (from Eng Manager)

- [ ] Prioritised and able to deliver in a sprint
- [ ] All platform subtasks (including test cases) identified and created
- [ ] UI assets and UX flows designed and linked to all Acceptance Criteria (Amber)
- [ ] Feature flag designed with entry point identified
- [ ] API Contract identified and documented (Pow Hwee)

### Additional checks (PM)

- [ ] Acceptance criteria are clear and testable
- [ ] Dependencies identified
- [ ] Edge cases and error states documented
