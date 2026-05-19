# Grooming Briefing — 19 May 2026
**Sprint 2 Week 1 — Squad Grooming (internal)**
**Target sprint:** Sprint 3 (2 Jun – 13 Jun 2026)
**Facilitator:** Rama | **Content lead:** Michelle

---

## Sprint Goal
> **Sprint 2:** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

Sprint 3 goal is TBD (set at Sprint 2 mid-point). Provisional: *Officers see only eligible opportunities, can open a full detail page, and can route to apply.*

> ⚠️ **Action before tomorrow:** Paste sprint goal into Jira. Still not set as of 2026-05-18.

---

## Story Readiness Scorecard

| Story ID | Title | Story Format | AC Written | AC Language | Design Status | Dependencies | Open Items | Ready? |
|---|---|---|---|---|---|---|---|---|
| US-05 | Clear filters and reset view | ✅ | ✅ | ✅ | ✅ Finalised | Pairs with OTEP-86 | None | ✅ **Ready** |
| OTEP-86 | Filter by opportunity type | ✅ | ✅ | ✅ | ✅ Finalised | OTEP-85 must ship (S2) | None | ✅ **Ready** |
| WOG-05 | Log out of OTEP | ✅ | ✅ | ✅ | ✅ Assumed | None | None | ✅ **Ready** |
| OTEP-110 | Login fail / clear error | ✅ | ✅ | ✅ | ✅ Assumed | None | None | ✅ **Ready** |
| WOG-04 | Stay logged in during session | ✅ | ⚠️ | ✅ | ✅ Assumed | None | Session timeout TBD | ⚠️ **1 gap** |
| WOG-06 | First-time login experience | ✅ | ⚠️ | ✅ | ⚠️ Needs lock | OTEP-183 findings | Mandatory fields TBD | ⚠️ **2 gaps** |
| OTEP-87 | Detail page: apply CTA + competencies | ✅ | ⚠️ | ✅ | ✅ Finalised | OTEP-128 (S2), US-18 | #18, #20 | ⚠️ **Conditional** |
| US-18 | Apply via FormSG basic redirect | ✅ | ⚠️ | ✅ | ✅ Finalised | `formsg_url` confirmed | #2 (open) | 🔴 **Blocked** |
| OTEP-127 | Apply ringfencing criteria | ✅ | ❌ | — | ❌ None | OTEP-183 findings | Eligibility rules undefined | 🔴 **Not ready** |
| US-03 | Filter by category | ✅ | ❌ | — | ❌ None | Hybrid model validation | Validation outstanding | 🔴 **Blocked** |
| Search (TBD) | Keyword search | ❌ | ❌ | — | ❌ None | — | Missing story entirely | 🔴 **Missing** |

**Score: 4 ready · 3 conditional/gapped · 4 blocked or missing**

---

## AC Language Flags

All written ACs passed the mechanism-language test — no "the system will / the API returns / the component renders" found. Two literal TBDs to resolve before sizing:

**WOG-04:** `"If I've been idle for more than [X minutes — TBD]..."` — government-mandated session timeout is unknown. Either get the compliance answer before Sprint 3, or flag it explicitly at sizing so eng knows the value is a placeholder.

**WOG-06:** `"I'm asked to enter my name and agency — [ASSUMPTION: mandatory fields TBD with team]"` — agreed at internal groom (2026-05-13) that basic profile = name + agency. Confirm this is still the position and kill the TBD in the room.

---

## Risk Areas

> ⚠️ **OTEP-86** — No AC covers an unrecognised opportunity type. If OTG exports a type not in the list (Internal Job / SJR / STIP/Gig), the card will either break or disappear.
> → **Pre-empt:** Add AC — "If an opportunity type isn't recognised, the card renders with a generic type label — it doesn't break or disappear."

> ⚠️ **OTEP-87** — "I see a clear Apply button that links to the FormSG form" — but OTEP-87's must-haves don't carry forward US-18's null-URL fallback. Pow Hwee will ask: what if `formsg_url` is missing?
> → **Pre-empt:** Add AC — "If the FormSG URL is missing on an Internal Job, STIP, or Gig, I see 'Application form unavailable — contact the posting agency' instead of the Apply button."

> ⚠️ **WOG-04** — Session timeout value is a literal TBD in the AC. He will ask.
> → **Position:** "We need the government compliance answer. Pow Hwee, do you know who owns this — is it the infra team or security team?"

> ⚠️ **WOG-06** — OTEP-183 spike (POCDEX profile lookup) is done. If POCDEX can return officer name and agency from SOE-ID, the first-time login story changes significantly — officer doesn't need to type those fields manually.
> → **Drive:** "What did OTEP-183 tell us about POCDEX? If name and agency are available, we don't need to collect them at first login." Get this answer in the room.

> ❌ **OTEP-127** — No ACs exist. Nothing to groom.
> → **Approach:** Open the discussion with "What did OTEP-183 find?" and write ACs live in the session if Pow Hwee has the answers. Otherwise agree explicitly that OTEP-127 can't be sized until eligibility rules are documented.

> ❌ **Search** — No story, no Jira ticket. Confirmed MVP requirement. sprint-allocation.md calls it out as a "Missing Story."
> → **Action:** Acknowledge in session, commit to a date to write it (before Sprint 3 planning Thu 11 Jun).

---

## Grooming Order (recommended)

| Order | Story | Status | Time |
|---|---|---|---|
| 1 | US-05 — Clear filters | ✅ Ready | 5 min |
| 2 | OTEP-86 — Filter by type | ✅ Ready | 15 min |
| 3 | WOG-05 — Log out | ✅ Ready | 10 min |
| 4 | OTEP-110 — Login fail | ✅ Ready | 10 min |
| 5 | WOG-04 — Stay logged in | ⚠️ 1 gap | 15 min — table session timeout gap explicitly |
| 6 | WOG-06 — First-time login | ⚠️ 2 gaps | 15 min — get OTEP-183 findings here |
| 7 | OTEP-87 — Detail page CTA | ⚠️ Conditional | 20 min — must-haves only; declare competency as good-to-have |
| 8 | US-18 — FormSG redirect | 🔴 Blocked | 5 min — confirm blocked, agree on Rama chase |
| 9 | OTEP-127 — Ringfencing | 🔴 No ACs | 10 min — write from OTEP-183 findings or surface the gap |
| 10 | US-03 + Search | 🔴 Missing/blocked | 10 min — acknowledge, commit to write-dates |

---

## Open Items — Assign an Owner in the Session

| Open Item | Suggested Owner | Needed By |
|---|---|---|
| `formsg_url` confirmed (#2) — last unconfirmed OTG field | Rama + PSD Ops | Before Sprint 3 start (1 Jun) |
| Session timeout policy — government-mandated idle timeout | Pow Hwee (flag to compliance/security) | Before Sprint 3 WOG-04 build |
| WOG-06 mandatory fields: name + agency is the call? | Close in session — Michelle + Pow Hwee | Today |
| OTEP-183 spike findings: POCDEX pre-fill of name/agency from SOE-ID? | Pow Hwee to share findings | Today / immediately after |
| SJR card/detail treatment — which design did Amber land on? (#20) | Amber to confirm | Before OTEP-87 build |
| Categorisation hybrid model validation (gates US-03) | Michelle — schedule with Adrian/Jacky/XZ | Before Sprint 3 grooming (Thu 22 May) |
| Search story — write ACs and create Jira ticket | Michelle | Before Sprint 3 planning (Thu 11 Jun) |
| OTEP-127 eligibility rules — write ACs from OTEP-183 findings | Michelle + Pow Hwee | Before Sprint 3 planning |

---

## R1 Deflection List

| Topic | Response |
|---|---|
| Competency match scoring | "Competency match ratio is R1 — decision 2026-05-08. Sprint 3 shows 'What you'll develop' tags only." |
| Agency/grade/commitment filters | "Type filter only for MVP — agency, grade, commitment filters are R1 per the brief." |
| Save / bookmark an opportunity | "R1. Not in MVP." |
| Supervisor endorsement workflow | "UI copy only in MVP — backend workflow is R1 (decision 2026-05-08)." |
| FormSG pre-fill from officer profile | "Conditional on open item #14. If FormSG supports URL params, US-P3 gets pulled in. If not, officers fill manually." |
| SJR apply flow | "SJR apply is deferred to a future release — decision 2026-05-13. Visible in listing but no apply action in MVP." |
| Notifications | "R1 per MVP guardrails." |
| Function/Job-function taxonomy mapping | "R1 — decision 2026-05-06. Non-matching taxonomies, mapping cost high vs unclear ROI." |

---

## Pow Hwee Will Probably Ask...

**On OTEP-86:**
> *"What happens if the API returns an opportunity with a type we don't recognise?"*
→ Pre-empt: add the generic-label AC before the session (see Risk Areas above).

**On OTEP-87:**
> *"What does the apply button show if `formsg_url` is null on an Internal Job?"*
→ Pre-empt: carry US-18's fallback forward — add the missing-URL AC to OTEP-87 before the session.

**On WOG-04:**
> *"What's the session timeout value?"*
→ "TBD — government compliance hasn't confirmed. Pow Hwee, do you know who owns this?"

**On WOG-06:**
> *"Can POCDEX pre-populate name and agency from SOE-ID? If yes, officers don't need to type it."*
→ "That's exactly what OTEP-183 should tell us. What did the spike find?"

**On OTEP-127:**
> *"What are the eligibility rules? Grade? Agency? Both?"*
→ "That depends on OTEP-183. Walk me through what POCDEX returned." — then write ACs from the answer.

**On Sprint 3 capacity:**
> *"This is a heavy sprint — OTEP-86, OTEP-87, OTEP-127, US-18, auth polish, search. Thomas still can't do everything."*
→ "Agreed. My read: US-03 and Search move to Sprint 4 unless blockers clear by 1 Jun. OTEP-127 depends on today's POCDEX conversation. What's your view on Thomas's capacity across the FE stories?"

---

## Self-Check Before Walking In

- [ ] Open item #28 resolved: OTEP-85 visibility rule = `closing_date > today`; "Closing soon" badge (<=7 days) is OTEP-129
- [ ] Open item #29 resolved: OTEP-289 spike has ACs, timebox, and expected output defined
- [ ] OTEP-86: defensive AC for unrecognised type added to story file
- [ ] OTEP-87: null-formsg_url fallback AC added to story file
- [ ] OTEP-183 spike findings: remind Pow Hwee to bring them — WOG-06 and OTEP-127 both depend on this

---

*Generated: 2026-05-19 | Sprint 2 Week 1 | Covers Sprint 3 stories*
