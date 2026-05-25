# Sprint Allocation Analysis — 2026-05-21
> Post-grooming. Incorporates WOG AD domain confirmation, CSC SSO dependency (Imelda), POCDEX go-live risk (Daryll).
> Constraint: Security/Compliance = September (S09+). Feature build window = S01–S08, ending Fri 21 Aug.

---

## The single structural risk: Sprint 4 is entirely hostage to WOG AD

Sprint 4 (15–26 Jun) currently carries 7 stories: 4 auth (OTEP-71/110/304/305), ringfencing (OTEP-127), first-time login (WOG-06), POCDEX seed (OTEP-202). Every one of them requires WOG AD onboarding to be complete. There is no contingency stream. If WOG AD slips by 2–3 weeks, Sprint 4 delivers nothing.

---

## 6-Week SSO Chain: Three Scenarios

> ⚠️ Updated: WOG AD is a formal onboarding process. 2 weeks is the **minimum** (clean run, no errors). Back and forth on errors adds time — realistic is 2.5–4 weeks. Domain `careercompass.gov.sg` is confirmed; that was the gate. Clock starts on Adrian's approval, not on the ping.

| Scenario | Adrian responds | WOG AD duration | WOG AD done | CSC SSO done | Auth sprint | CSC sprint | Verdict |
|---|---|---|---|---|---|---|---|
| **Best case** | This week (22 May) | 2 wks, clean | ~5 Jun (mid S03) | ~3 Jul | S04 ✓ | S05 tight | ✅ Holds — needs clean run |
| **Realistic** | End of May (29 May) | 3 wks, some back/forth | ~19 Jun (S04 W1) | ~17 Jul | S05 | S06 | ⚠️ Auth slips to S05; C@G/FormSG displaced |
| **Delay + errors** | Mid-June (15 Jun) | 3–4 wks | ~6–13 Jul (S05/S06) | ~3–10 Aug | S06 🔴 | S07/S08 🔴 | 🔴 Feature Freeze at serious risk |

**The best case requires both Adrian responding this week AND a clean onboarding with no errors.** That's two things that must go right simultaneously. Treat the realistic scenario (auth in S05) as the working assumption and plan S04 with a contingency stream.

**Every day Adrian delays = same delay to CSC SSO.** In the realistic scenario, CSC SSO lands in Sprint 6, displacing admin login and instrumentation. In the delay+errors scenario, CSC SSO isn't done until the testing sprint or UAT sprint — Feature Freeze fails.

---

## Sprint-by-Sprint: Updated View

### S02 — 18–29 May — Listing → Detail E2E
- **Risk:** None from new dependencies. Pre-auth.
- **Action now:** Ping Adrian today. That's the only sprint 2 PM action that affects the whole chain.
- **Status:** ✅ On track

---

### S03 — 1–12 Jun — Filters + OTG Ingestion + POCDEX Plumbing
| Story | Owner | Risk |
|---|---|---|
| OTEP-192 — recurring OTG ingest job | Leo | Depends on OTEP-193 data model landing in S02 |
| OTEP-271 — local POCDEX DB | Leo | Plumbing. Unblocks S04 ringfencing. |
| OTEP-203 — standalone POCDEX API service | Pow Hwee | Plumbing. |
| OTEP-86 — filter by type | — | FE: Thomas |
| OTEP-317 — clear filters | — | FE: Thomas |
| OTEP-318 — filter by category | — | ⚠️ Conditional on OTEP-289 spike. FE: Thomas |
| OTEP-87 — enhanced detail + apply CTA | — | FE: Thomas |
| OTEP-319 — apply via FormSG redirect | — | FE: Thomas |

**⚠️ Thomas FE overload.** He has 5 FE-touching stories in 9 dev days (Vesak Day 2 Jun = 1 dev day lost). Historical velocity: ~2–3 FE stories per sprint. **Recommend scoping S03 to OTEP-86 + OTEP-317 + OTEP-319 as the FE core. Defer OTEP-87 (enhanced detail) to S04 and OTEP-318 to S04 if spike is green.**

**Missing story:** OTEP-131 (null `formsg_url` fallback) — apply CTA needs it before OTEP-319 ships. Add to S03.

**Status:** ⚠️ Overloaded on Thomas. Needs a cut-line decision before Sprint Planning (29 May).

---

### S04 — 15–26 Jun — Auth + Ringfencing + Onboarding
| Story | Owner | Dependency |
|---|---|---|
| OTEP-71 — WOG AD login | Pow Hwee | WOG AD onboarding complete ← **the gate** |
| OTEP-110 — login fail | Thomas | Same |
| OTEP-304 — stay logged in | — | Same |
| OTEP-305 — log out | — | Same |
| OTEP-127 — ringfencing | Thomas/Leo | WOG AD + Sprint 3 POCDEX plumbing |
| OTEP-202 — POCDEX seed DB | Leo | Needed for ringfencing UAT |
| WOG-06 — first-time login | Thomas | POCDEX dep |

**🔴 Single-dependency sprint. No contingency.**
If WOG AD isn't done by 15 Jun, all 7 stories are blocked. Mitigation: add a parallel C@G ingestion stream to S04 so the sprint isn't empty if auth slips. C@G API integration is currently unassigned in S05 — pull it forward as a contingency track.

**Also needed before Sprint 4 planning:** Daryll (POCDEX team lead) session must happen first — OTEP-271/203 can't be validated without his team engaged, and OTEP-127 ringfencing depends on that validation.

**Status:** 🔴 Structural risk. Needs contingency plan + Daryll session before Sprint 4 planning (5 Jun).

---

### S05 — 29 Jun–10 Jul — C@G + Full FormSG Integration
| Story | Notes |
|---|---|
| OTEP-130 — FormSG full (webhook + status sync) | FormSG Phase 2. Heavy integration. |
| OTEP-89 — C@G opportunity detail + apply CTA | Depends on C@G API ingestion working. |
| OTEP-133 — email deep-link redirect | Depends on OTEP-127 (ringfencing) + US-05. |
| OTEP-88 — OTG vs C@G visual distinction | |
| **CSC SSO integration** | **⚠️ MISSING STORY.** Best case CSC is done ~3 Jul. Story needed here. |

**Two problems:**
1. No CSC SSO integration story exists anywhere in the plan. Create the placeholder story now. It belongs in S05 at best case, S06 if WOG AD slips.
2. S05 is already heavy with C@G + FormSG Phase 2. Adding CSC SSO on top makes this the second over-committed sprint. Consider splitting: pull OTEP-133 to S06 (it's the most dependent story — ringfencing + US-05 both needed).

**Status:** 🔴 Missing CSC SSO story. Over-scoped if SSO lands here.

---

### S06 — 13–24 Jul — Admin Login + Instrumentation
| Story | Notes |
|---|---|
| WOG-02 — admin login | |
| WOG-07 — role-based access control | |
| Instrumentation | All success metrics tracked |
| Bug fixes S02–S05 | |
| **CSC SSO (realistic scenario)** | Lands here if WOG AD slips to end of May |

In the realistic scenario, CSC SSO integration lands in S06 — displacing some instrumentation/admin work. That's manageable. In the delay scenario, CSC SSO hasn't even finished the 4-week process yet when S06 starts.

**Status:** ⚠️ SSO absorb risk if WOG AD delays.

---

### S07 — 27 Jul–7 Aug — E2E Testing / Stabilisation
**This sprint is the buffer.** If anything from S04–S06 slips, it lands here. In the delay scenario, CSC SSO *finishes externally* on ~27 Jul — meaning integration work would overlap with E2E testing.

Feature freeze is Fri 21 Aug (end of S08). For Feature Freeze to hold, **everything must be dev-complete by end of S07** — S08 is UAT, not development.

**Status:** ⚠️ Absorbs slippage. Do not commit it to new stories.

---

### S08 — 11–21 Aug — UAT + ⭐ Feature Freeze
UAT requires auth working end-to-end. If WOG AD + CSC SSO aren't both production-ready by S07, UAT is incomplete and Feature Freeze is notional.

National Day (Mon 11 Aug in lieu) → sprint starts Tue 12 Aug. 9 dev days.

**Status:** ✅ Plan is sound IF S04–S07 hit. Dependent on no slippage from auth chain.

---

## Stories Missing from the Plan

| Story | Sprint | Why it's needed |
|---|---|---|
| CSC SSO integration | S05 (best) / S06 (realistic) | 4-week external process + integration work. No story exists. |
| OTEP-131 (null `formsg_url` fallback) | S03 | Required before OTEP-319 ships. Apply CTA needs the error state. |
| WOG AD onboarding placeholder | S04 | Pow Hwee asked for dependency stories in Jira. Track the process. |
| CSC SSO placeholder | S05 | Same ask. |
| C@G API ingestion | S04 (contingency) / S05 | No story for the actual ingestion setup. Assumed to exist but unwritten. |

---

## Three Decisions to Make Before Sprint 3 Planning (29 May)

1. **Sprint 3 FE cut-line** — Confirm with Pow Hwee: is OTEP-87 (enhanced detail) in S03 or S04? Thomas can't carry 5 FE stories. Recommend: 86 + 317 + 319 in S03, 87 + 318 in S04.

2. **Sprint 4 contingency track** — What does Sprint 4 do if WOG AD isn't ready by 15 Jun? Add C@G API ingestion (unwritten story) as a parallel stream so the sprint doesn't stall.

3. **Create CSC SSO story now** — Even a placeholder with "WOG AD must close first, 4-week CSC lead time, owner TBC." Assign it to S05 provisionally. Don't let it float outside the plan again.

---

## Summary Verdict

| Phase | Status | Critical blocker |
|---|---|---|
| S02 (current) | ✅ On track | None — action = ping Adrian today |
| S03 | ⚠️ Thomas overloaded | Cut OTEP-87 and OTEP-318 before 29 May |
| S04 | 🔴 Hostage to WOG AD | Contingency track needed; Daryll session must happen first |
| S05 | 🔴 Missing CSC SSO | Create story now; scope is too heavy without pruning |
| S06 | ⚠️ Absorb risk | Manageable if S04-S05 hit |
| S07 | ⚠️ Buffer | Don't assign new stories |
| S08 | ✅ Sound if chain holds | |
| S09+ (Sep) | ✅ Compliance confirmed | Feature Freeze (21 Aug) must hold |

**The feature freeze (21 Aug) is achievable in the best case. It's at risk in the realistic case. It fails in the delay scenario.**

The single most important action today: ping Adrian with `careercompass.gov.sg`. That starts the 6-week clock.

---

*Generated: 2026-05-21 post-grooming. Based on sprint-allocation.md, sprint-calendar.md, risks.md, open-items.md.*
