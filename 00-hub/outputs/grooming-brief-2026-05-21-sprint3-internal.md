# Grooming Brief — Sprint 3 Internal Review
## Prep for: Sprint 3 squad grooming before Sprint Planning (Thu 29 May)
## Prepared: 2026-05-21

> Sprint 3 stories were externally groomed today (21 May). This brief is for the internal squad review before Sprint Planning. Several stories have significant gaps that need fixing before planning — OTEP-87 especially.

---

### Sprint 3 Goal (proposed — confirm at planning)
Officer can filter the opportunity listing by type, view an enhanced detail page with a clear Apply CTA, and apply to Internal Jobs, STIPs, and Gigs via FormSG. OTG ingestion job runs in the background. POCDEX plumbing in place for Sprint 4 ringfencing.

---

### Grooming Readiness Scorecard

| Story | Title | Story Format | AC Written | AC Language | Design Status | Dependencies | Open Items | Ready? |
|---|---|---|---|---|---|---|---|---|
| OTEP-319 | Apply via FormSG | ✅ | ✅ | ✅ | N/A | ⚠️ OTEP-87 must land first | #14 (pre-fill) | ✅ |
| OTEP-317 | Clear filters | ❌ no format | ✅ | ✅ | N/A | ⚠️ OTEP-86 must exist | — | ⚠️ |
| OTEP-192 | Recurring OTG job | ✅ | ⚠️ | ❌ mechanism | N/A | OTEP-193 + OTEP-313 | ⚠️ cadence TBD | ⚠️ |
| OTEP-191 | Credential manager | ✅ | ✅ | ✅ | N/A | AWS infra (may be resolved) | Verify if still needed | ⚠️ |
| OTEP-86 | Filter by type | ✅ | ⚠️ | ⚠️ | ❌ unknown | ⚠️ filter infra (#16) | ⚠️ overlap w/ OTEP-318 | ❌ |
| OTEP-87 | Enhanced detail page | ✅ | ✅ | ❌ R1 scope in ACs | ❌ unknown | OTEP-128 Sprint 2 | #18 competency | ❌ |
| OTEP-318 | Filter by category | ❌ | ❌ | ❌ | ❌ | ⚠️ OTEP-289 spike output | ⚠️ conditional | ❌ |

---

### Risk Areas

> ⚠️ **OTEP-87** — **R1 scope baked into ACs. Fix before grooming.**
> The story description says "eligibility, developmental outcomes, competencies I already have, competencies I can develop." Sprint 3 decision (2026-05-21) scopes OTEP-87 to **apply CTA only** — competency section deferred pending open item #18. ACs include:
> - "For Jobs: competency match ratio X/Y matched" — **explicitly descoped to R1 (decision May 8)**
> - "competencies are labelled 'What you'll develop'" — competency display is R1
> → Strip all competency ACs before grooming. Paste only: apply CTA visible above fold, OTEP-87 depends on OTEP-128, null state for missing formsg_url, back-nav preserving filter state.
> Pow Hwee will ask about competencies. Answer: "Competency section is open item #18 — not building it until we know where the data comes from. Sprint 3 is apply CTA only."

> ⚠️ **OTEP-86 + OTEP-318** — **AC overlap. Split must be clean.**
> OTEP-86 AC says "I can filter the listing by Functions / Categorisation" — this is OTEP-318's job. Keep OTEP-86 strictly to **opportunity type** (STIP / Gig / SJR / Internal Job). Category/function filter belongs in OTEP-318 only.
> Also: OTEP-86 has a sub-task OTEP-92 "Tracking" with no description. Either define it (analytics/event tracking?) or remove it before grooming.
> → Define OTEP-92 or close it. Remove categorisation AC from OTEP-86.

> ⚠️ **OTEP-318** — **Empty and conditional. Gate before grooming.**
> No description, no ACs. Depends on OTEP-289 spike (run 19–20 May). Was the spike output green or no-go?
> → Before this hits the grooming room: (1) confirm spike recommendation, (2) if green, write ACs for category filter. If no-go, close OTEP-318 and note in decisions-log. Don't bring an empty story into the room.

> ⚠️ **OTEP-192** — **Cadence placeholder and mechanism ACs.**
> AC says "[Cadence TBD — confirm with Pow Hwee at grooming]" — don't walk into planning without a proposed cadence. Also: ACs are written as system behaviour ("the job reads the designated OTG Excel reports and upserts") not officer-observable outcomes.
> → Propose cadence (daily? every 6h?) before grooming. Rewrite officer-observable AC: "When I open the listing, the opportunities I see reflect the OTG data as of [last N hours]." Pow Hwee decides the implementation.

> ⚠️ **OTEP-86 filter infrastructure (#16)** — **Elastic matching dependency unresolved.**
> Open item #16 (search indexing infrastructure) is not confirmed. If OTEP-86 assumes an Elasticsearch-backed filter, that's a significant infrastructure story that may not be in Sprint 3 scope.
> → Confirm with Pow Hwee: is OTEP-86 type filter backed by a simple SQL WHERE clause (no infra needed) or does it require search indexing? If SQL, #16 isn't a Sprint 3 blocker. If elastic, it is.

---

### Grooming Order (recommended)

1. **OTEP-319** — Apply via FormSG ✅ — cleanest story, warm the room with a win
2. **OTEP-317** — Clear filters ⚠️ — quick fix (just add user story format, confirm edge case: search + filter combo)
3. **OTEP-192** — Recurring OTG job ⚠️ — confirm cadence with Pow Hwee; rewrite ACs
4. **OTEP-191** — Credential manager ⚠️ — quick verification: is AWS infra resolved? Close or carry
5. **OTEP-86** — Filter by type ❌ — remove categorisation AC, define OTEP-92, confirm infra dep
6. **OTEP-87** — Enhanced detail page ❌ — strip to apply CTA only; largest AC rewrite needed
7. **OTEP-318** — Filter by category ❌ — **only groom if OTEP-289 spike was green; otherwise close it**

---

### Open Items — Assign an Owner in the Session

| Open Item | Suggested Owner | Needed By |
|---|---|---|
| OTEP-289 spike output — go/no-go on category filter? | Michelle (chase now; spike was 19–20 May) | Before planning |
| OTEP-192 job cadence | Pow Hwee | Sprint 3 planning |
| OTEP-191 — resolved by AWS infra or still needed? | Pow Hwee | Sprint 3 planning |
| OTEP-86 — SQL filter or elastic infra needed? (open item #16) | Pow Hwee | Sprint 3 planning |
| OTEP-92 "Tracking" sub-task — define or close | Michelle + Pow Hwee | Before grooming |
| Design: OTEP-87 apply CTA layout (CTA above fold, null state) | Amber | Before Sprint 3 dev |
| Design: OTEP-86 filter panel UI | Amber | Before Sprint 3 dev |

---

### R1 Deflection List

- Competency matching on detail page → "Open item #18 — competency data source unconfirmed. OTEP-87 Sprint 3 is apply CTA only."
- Pre-fill via FormSG URL params → "Open item #14, Pow Hwee to confirm. US-P3 stays in limbo until #14 resolves — not blocking Sprint 3."
- Analytics/tracking on apply click → "OTEP-92 scope TBD — define or defer. Core apply flow first."
- Save for later / wishlist → "R1 — logging it."
- Supervisor endorsement → "R1 — UI copy only, no backend."
- Notification on apply → "Sprint 5 — after C@G and FormSG full flow."

---

### Pow Hwee Will Probably Ask...

- **"OTEP-87 mentions competency matching — is that in scope for Sprint 3?"**
  → "No. Sprint 3 is apply CTA only. Competency section is open item #18 — blocked on data source. I'm stripping those ACs before planning."

- **"OTEP-86 says filter by functions/categorisation — isn't that OTEP-318?"**
  → "Yes, that's a mistake. OTEP-86 = type filter only (STIP/Gig/SJR/Job). Categorisation is OTEP-318, conditional on the spike output."

- **"What's OTEP-92 tracking?"**
  → Either: "Analytics event on filter apply — need to define. Can we scope it at planning?" OR close it before the session.

- **"What cadence for OTEP-192? How fresh is the data?"**
  → Have a proposed answer ready: "Daily batch makes sense given OTG exports are daily — open to your view on more frequent."

- **"Does OTEP-86 need Elasticsearch or can we do a simple SQL filter?"**
  → "That's the question. If it's a WHERE clause on type, no infra needed. You tell me — affects whether #16 blocks Sprint 3."

- **"OTEP-318 has nothing in it. Should it even be in Sprint 3?"**
  → "Conditional on the OTEP-289 spike. I'll have the spike output before planning — if it's no-go we close it."

- **"OTEP-319 depends on OTEP-87. If OTEP-87 slips, does OTEP-319 slip too?"**
  → "Yes. OTEP-87 is the gate for OTEP-319. Both are Sprint 3 — plan them in that order."

---

> **Self-check before closing:**
> - [ ] Stripped all competency ACs from OTEP-87 — apply CTA only
> - [ ] Removed "filter by functions/categorisation" from OTEP-86 ACs
> - [ ] Confirmed OTEP-289 spike output (go/no-go for OTEP-318)
> - [ ] Added user story format to OTEP-317
> - [ ] Proposed cadence for OTEP-192
> - [ ] Defined or closed OTEP-92
