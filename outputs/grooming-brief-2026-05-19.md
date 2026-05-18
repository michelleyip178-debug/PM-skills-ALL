# Grooming Briefing — 19 May 2026

**Sprint:** Sprint 2 (18–29 May 2026)
**Sprint goal:** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

> ⚠️ **Action before tomorrow:** Paste sprint goal into Jira. Still not set as of 2026-05-18.

---

## Step 2 — Grooming Readiness Score

| Story ID | Title | Story Format | AC Written | AC Language | Design Status | Dependencies | Open Items | Ready? |
|---|---|---|---|---|---|---|---|---|
| OTEP-193 | Design data model for Opportunities | ❌ No story format | ❌ None | N/A | N/A | OTG + C@G sources | #23 (harmonised model), #27 (OTEP-271 sequencing) | ❌ Not ready |
| OTEP-192 | Recurring job to fetch OTG data | ❌ No story format | ❌ None | N/A | N/A | OTEP-193, #24 (which reports) | #24 critical — which Excel reports to ingest | ❌ Not ready |
| OTEP-85 | Display opportunity cards | ✅ | ⚠️ Gap: "Closing soon" ACs missing from must-haves | ✅ Officer-perspective throughout | ✅ Finalised | OTEP-193, OTEP-192 | #24 for real data | ⚠️ Needs AC fix |
| OTEP-128 | View opportunity detail page | ✅ | ⚠️ Two gaps (see below) | ✅ Officer-perspective; API notes correctly separated | ✅ Finalised | OTEP-85 | #22 design lock date | ⚠️ Needs AC fix |
| OTEP-267 | Pagination for listing page | ✅ | ✅ | ✅ Clean | ✅ Finalised | OTEP-85 | None | ✅ Ready |
| OTEP-289 | [Spike] Filter by Functions | ❌ Not a proper spike | ❌ None | N/A | N/A | OTEP-85, OTEP-128 | Design approach TBD | ❌ Not ready |
| OTEP-191 | Handle credential manager and vault | ❌ No content | ❌ None | N/A | N/A | Unknown | Unknown | ❌ Confirm if even Sprint 2 |

---

## Step 3 — Risk Areas

> ⚠️ **OTEP-85** — "Closing soon" label ACs are stranded in the deprecated OTEP-85a section. They did not make it into OTEP-85's must-have list when OTEP-85a was re-absorbed (2026-05-15). The ACs exist — they just need to be moved. Fix this before grooming or Pow Hwee will find the gap.
> → **Action:** Copy "Closing soon" ACs from OTEP-85a into OTEP-85 must-haves.

> ⚠️ **OTEP-128** — Two gaps:
> 1. "Closing soon" label on the detail page is noted as in scope (via OTEP-85a re-absorption) but is not an explicit AC in OTEP-128. Same fix as above — needs to be written in.
> 2. "No apply button in Sprint 2 — should officers see messaging explaining why? Currently silent." This open question will come up in grooming. Make a call before the session: silent (no button, no explanation) or add a note like "Apply opens in Sprint 3"? Decide with Amber.
> → **Action on #1:** Add "Closing soon" AC to OTEP-128. **Action on #2:** Decide and document before grooming.

> ⚠️ **OTEP-267** — Edge case: "When there are no opportunities to show, the page controls disappear." OTEP-268 (empty/error states) is deferred to Sprint 3. In Sprint 2, if the listing has zero records (unlikely with OTG data but possible), what does the officer see? The AC covers the controls disappearing, but there's no Sprint 2 story handling the empty page state. Pow Hwee will ask.
> → **Suggested position:** "Zero-results edge case won't occur in Sprint 2 — OTG import always has data. Empty state is handled in Sprint 3 with filters. We accept the gap for Sprint 2."

> ❌ **OTEP-289** — Not a proper spike. The Jira description reads like a business requirement ("user filters by function, sees matching results"). A spike needs: a time-boxed investigation question, a clear definition of done (decision, proof-of-concept, or doc), and a handoff output. As written, Pow Hwee will flag it as ungroom-able.
> → **Action:** Reframe as: "Spike — how do we map OTG Job Function and C@G category tags to a shared function taxonomy? Done = a mapping recommendation doc + data model note for OTEP-193." Add a time-box (1–2 days).

> ❌ **OTEP-192 + OTEP-193** — Critical path for Sprint 2 (OTEP-85 has no data without them) but both have empty descriptions in Jira and no ACs. OTEP-193 owner is Léo; OTEP-192 has no owner. These must land in W1 or OTEP-85 is blocked.
> → **Action for OTEP-193:** Confirm owner (Léo per Jira, not Pow Hwee as noted locally — verify). Write basic ACs before grooming or agree to groom them in the session.
> → **Action for OTEP-192:** Resolve open item #24 (which OTG Excel reports) before this can move. Michelle owns #24 — share the reports today.

> ⚠️ **OTEP-191** — No description, no owner, no context. Cannot groom.
> → **Action:** Confirm with Pow Hwee whether this is Sprint 2 scope. If yes, get a description. If no, remove from the board.

**Pow Hwee's refinement pattern to pre-empt:**
He caught the OTEP-85a re-absorption slip last sprint (mechanism vs outcome, and ticket structure). He will look for:
1. AC rule conflicts → "Closing soon" gap in both OTEP-85 and OTEP-128
2. Ungroom-able spikes → OTEP-289 as currently written
3. Critical path work with no content → OTEP-192, OTEP-193

---

## Step 4 — Recommended Grooming Order

1. **OTEP-193** (data model) — unblock everything else; agree scope and owner in the room
2. **OTEP-192** (file import) — depends on #24; share reports before the session
3. **OTEP-85** — foundation story, but fix "Closing soon" AC gap first (**do this today**)
4. **OTEP-128** — fix two gaps before grooming (see above)
5. **OTEP-267** — clean, fastest to groom; do this last
6. **OTEP-289** — reframe as a proper spike first; groom only if time allows
7. **OTEP-191** — confirm scope with Pow Hwee before placing in the order

---

## Grooming Briefing — 19 May 2026

### Sprint Goal
By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

### Grooming Order (recommended)
1. OTEP-193 — Data model ❌ (agree scope + owner in session)
2. OTEP-192 — File import job ❌ (share OTG reports first — open item #24)
3. OTEP-85 — Opportunity cards ⚠️ (fix "Closing soon" ACs before session)
4. OTEP-128 — Detail page ⚠️ (fix "Closing soon" AC + decide "no apply" messaging)
5. OTEP-267 — Pagination ✅ (clean — quick)
6. OTEP-289 — Functions spike ❌ (reframe before grooming)
7. OTEP-191 — Credentials ❌ (confirm scope first)

### Open Items — Assign an Owner in the Session

| Open Item | Suggested Owner | Needed By |
|---|---|---|
| #24 — Which OTG Excel reports to ingest for OTEP-192 | Michelle → share reports before session | Before OTEP-192 can start |
| #23 — Harmonised data model (OTG now, C@G later) | Pow Hwee to confirm feasibility in OTEP-193 | Before OTEP-193 dev |
| #27 — OTEP-271 (POCDEX) placement: Sprint 2 or Sprint 3? | Michelle + Pow Hwee | Sprint 2 start |
| #22 — Design lock date for Sprint 2 | Michelle + Amber | W1 |
| #26 — Auth test outcome without AzureAD | Pow Hwee + Leo | Sprint 2 start |
| OTEP-191 scope — Sprint 2 or not? | Pow Hwee to confirm | Before next board update |
| OTEP-193 owner — Léo (Jira) vs Pow Hwee (local context) | Confirm in session | Today |

### R1 Deflection List
- "Can we add a search bar?" → "Search is MVP but Sprint 3 — not this sprint."
- "What about filtering by type?" → "OTEP-86 is Sprint 3. Sprint 2 is unfiltered OTG listing only."
- "Can officers save opportunities?" → "R1. Not in MVP."
- "What about the apply button?" → "Sprint 3 — OTEP-87 and US-18. Sprint 2 detail page has no apply action."
- "Can we show C@G listings too?" → "C@G lands Sprint 3–4 after ingestion is confirmed. Sprint 2 is OTG-only."

### Pow Hwee Will Probably Ask...
- "Where are the ACs for 'Closing soon' on OTEP-85?" — **pre-empt:** move them from OTEP-85a into OTEP-85 before the session.
- "What does the officer see when there are no opportunities?" — **position:** zero-results won't occur in Sprint 2 with OTG data; empty state is Sprint 3 with filters.
- "What does the detail page show instead of an apply button — just nothing?" — **make a call before the session:** silent (no button) or placeholder copy.
- "What's the spike actually investigating in OTEP-289? What does done look like?" — **reframe it before grooming.**
- "What are the ACs for OTEP-192 and OTEP-193?" — **share the OTG reports (open item #24) before the session so the import job can be scoped.**
- "Who owns OTEP-193 — Léo or me?" — **verify before the session; mixed signals between Jira and local context.**

> **Self-check before closing:** Have you fixed the "Closing soon" AC gap in OTEP-85 and OTEP-128? Have you resolved the "no apply button" open question with Amber? Have you shared the OTG reports for open item #24? Have you reframed OTEP-289 as a proper spike?

---

*Generated: 2026-05-19 | Sprint 2 | Next grooming: Tue 19 May (squad internal) → Thu 21 May (backlog grooming)*
