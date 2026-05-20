# R1 Candidate List — Phase 1 Consolidation

**Created:** 2026-05-20
**Sources:** `sprint-allocation.md` (Deferred to R1), `decisions-log.md`, `scoping-gaps-tracker.md`, CareerCompass OKR Review & Roadmap deck
**Owner:** Michelle
**Status:** Draft — pending reconciliation with Adrian

> This is the Phase 1 output of R1 discovery. It consolidates every R1 item across local files and the deck, flags conflicts, and surfaces what needs a decision before R1 grooming can begin.

---

## Section 1: Deck-Confirmed R1 Scope

These 5 items are explicitly in scope for R1 per the revised roadmap deck (Slide 10). They form the "Seamless Application" release.

| # | Feature | Description | Conflict with local files? |
|---|---------|-------------|---------------------------|
| D1 | Pre-filled job applications | Auto-populate STIP/GIG/SJR/C@G/Internal Job applications from officer profile. Includes ability to post jobs on ATS. | ⚠️ Local files defer FormSG pre-fill (scoping-gaps #12) — but deck goes further, replacing FormSG with in-app application entirely |
| D2 | In-app application (no redirects) | Officers apply within CareerCompass; no external handoff to FormSG or other portals | ⚠️ **Core conflict** — MVP is building FormSG redirect (Sprint 3). Deck assumes this is replaced in R1. Steering decision (2026-03-12) confirms this was always the intent. Needs ATS named. |
| D3 | End-to-end status tracking | Application status synced from ATS within 24 hours of hiring manager action | ⚠️ **New dependency** — which ATS? Not named in deck. Adrian + Barry discussing with HR IT (decisions-log 2026-05-12). Unresolved. |
| D4 | Saved Jobs | Officers can save opportunities and resume application later | ✅ Aligns with deferred "Save for later" (decisions-log 2026-05-08). Same feature, different name. |
| D5 | External-facing officer profile (read-only) | Officer profile visible during application process | ⚠️ Not in local files as R1 item. New from deck. Scope unclear — whose view? Hiring manager? |

---

## Section 2: Local-File R1 Items — Not in Deck

These were formally deferred to R1 in decisions-log or sprint-allocation, but don't appear in the deck's revised R1 scope. They are likely R2+ — but need confirmation from Adrian.

| # | Item | Source | Deferred decision date | Likely release |
|---|------|---------|----------------------|----------------|
| L1 | Agency, grade, commitment filters | sprint-allocation, decisions-log | 2026-04-xx | R2+ |
| L2 | Function/Job function taxonomy mapping (OTG vs C@G) | decisions-log, scoping-gaps #7 | 2026-05-06 | R2 (needed before full C@G migration) |
| L3 | Competency proficiency levels (beyond binary) | decisions-log, sprint-allocation | 2026-05-08 | R2 — deck puts this in R2 (Competency Proficiency Levelling) ✅ |
| L4 | Supervisor endorsement backend | decisions-log | 2026-05-08 | R3 — deck aligns (Build Plans Together) ✅ |
| L5 | Competency match ratio / scoring | decisions-log, sprint-allocation, scoping-gaps #11 | 2026-05-08 | R2+ — deck deprioritised from R1 ✅ |
| L6 | Auto-populate OTG form fields from POCDEX | scoping-gaps #12 | 2026-05-08 | Superseded by D2 (in-app application replaces FormSG) |
| L7 | Persist filter selections across sessions | sprint-allocation, scoping-gaps #13 | 2026-05-08 | R2 |
| L8 | Autocomplete / suggested search | sprint-allocation | — | R2 |
| L9 | Rich onboarding tutorial | sprint-allocation | — | R2+ |
| L10 | Granular roles (beyond officer/admin) | sprint-allocation | — | R4 — deck aligns ✅ |
| L11 | AI / recommendation matching engine | sprint-allocation | — | R5 — deck aligns ✅ |
| L12 | Custom questions on FormSG | sprint-allocation | — | Superseded by D2 (in-app replaces FormSG) |

---

## Section 3: Deck Items Deprioritised OUT of R1

These were in the original R1 proposal but were cut in the revised deck. Treat as R2 candidates.

| # | Item | Original intent | Why cut |
|---|------|----------------|---------|
| X1 | Smart Assistant (auto-populate strengths) | Reduce application effort | Improves quality, not completion rate — R2 territory |
| X2 | Gap Radar (insights for target roles) | Help officers assess fit before applying | Downstream of primary conversion bottleneck |
| X3 | Intelligence Dashboard (usage patterns) | Track engagement | R3/R4 — agency analytics layer |

---

## Section 4: Conflicts Requiring a Decision

These need resolution before R1 discovery can proceed to Phase 2.

### Conflict 1 — FormSG vs ATS (🔴 Blocker)

**What the deck says:** R1 delivers in-app application with no redirects, ATS integration for status tracking.
**What local files say:** MVP (Sprint 3) is building FormSG redirect as the apply mechanism. SJR apply was deferred to "future release."
**Steering decision (2026-03-12):** FormSG is the MVP vehicle only; OTEP owns the long-term apply experience.

The conflict isn't a contradiction — it's a sequencing question. FormSG redirect in Sprint 3 is the stepping stone; R1 replaces it. But two things are still unresolved:
1. **Which ATS?** Deck doesn't name it. Adrian + Barry are discussing with HR IT (decisions-log 2026-05-12) — what's the outcome?
2. **Does R1 include SJR apply?** Deck says "pre-filled STIPs, GIGs, SJR, C@G, Internal Jobs." MVP deferred SJR apply entirely. This is new R1 scope and needs a BO decision.

**Action needed:** Confirm ATS identity and SJR apply inclusion with Adrian before R1 discovery Phase 2.

---

### Conflict 2 — Saved Jobs naming (✅ Minor)

Local files call it "Save for later" (deferred 2026-05-08). Deck calls it "Saved Jobs." Same feature — just align naming before writing stories.

---

### Conflict 3 — External-facing profile scope (🟡 Unclear)

Deck adds "External Facing Profile page — allow officer profile page to be accessed during application and displayed as read-only." This doesn't appear in local files as an R1 item. Questions:
- Who sees the read-only profile — the hiring manager, the officer, or both?
- Does this require a separate profile page route, or is it the existing profile with a view-only mode?
- What fields are shown? Full profile or a curated "application card"?

**Action needed:** Clarify with Amber (design) and Pow Hwee (technical feasibility) at R1 grooming kickoff.

---

## Section 5: Open Dependencies from Scoping Gaps Tracker

These gaps from `scoping-gaps-tracker.md` are still unresolved and directly block R1 features.

| Gap # | Item | Blocks | Owner | Status |
|-------|------|--------|-------|--------|
| #2 | C@G ingestion method | D1 (pre-filled C@G apps) | Pow Hwee | Open |
| #3 | Email/notification service | Status tracking confirmation emails | Pow Hwee | Open |
| #6 | Officer competency data model | D5 (profile page), D2 (pre-fill) | Pow Hwee | Open |
| #10 | FormSG pre-fill support | Superseded by D2 if ATS replaces FormSG | Pow Hwee | Open — may close |

---

## Summary: What R1 Actually Is

If the deck scope holds, R1 = **5 features, 3-month window, one strategic objective: close the loop between discovery and application.**

| Feature | Status | Key risk |
|---------|--------|----------|
| Pre-filled applications | Confirmed in deck | ATS identity unknown |
| In-app application (no redirect) | Confirmed in deck | ATS identity unknown; replaces Sprint 3 FormSG work |
| Status tracking | Confirmed in deck | ATS integration = significant technical dep |
| Saved Jobs | Confirmed in deck | Low risk — straightforward feature |
| External-facing profile | Confirmed in deck | Scope unclear — needs design definition |

**North Star target at R1:** 10% of onboarded officers complete a development action by Mar '27.

---

## Next Steps (Phase 2 onwards)

- [ ] Resolve Conflict 1 (ATS identity + SJR apply) with Adrian — **do this before anything else**
- [ ] Clarify external-facing profile scope with Amber and Pow Hwee
- [ ] Use `pm-product-discovery:interview-script` to build officer interview guide for Phase 2 user research
- [ ] Use `pm-execution:stakeholder-map` to map R1 sign-off owners before Phase 3

---

*Living doc — update as conflicts are resolved and scope is confirmed.*
