# R1 Capacity Reality-Check — Can We Build Creation + Apply + The Seam?

**Date:** 2026-06-02  
**Owner:** Michelle Yip  
**Audience:** Adrian (+ BO, since this touches a BO-level scope call)  
**Decision needed:** R1 now contains three net-new builds after creation moved from R4 (D 2026-06-02). Is that deliverable in the R1 window with current capacity, or does something move?  
**Ask of the reader:** Pick a scope option (below) before R1 grooming. This is a forcing function, not an FYI.

---

## The "so what" (read this first)

Moving opportunity creation from R4 into R1 was the right *product* ambition — it closes the loop so agencies post, receive, review, and close all in CareerCompass. But it turned R1 from one big build into **three net-new builds landing in the same ~3-month window**, owned by **one front-end engineer**:

1. **Native apply** — officers apply inside CareerCompass (replaces FormSG redirect)
2. **The seam** — application routing + status-back (the 24-hr OKR lives here)
3. **Native creation** — agencies author postings in OTEP (just moved from R4; zero discovery until today)

The question isn't whether each is valuable. It's whether all three fit. My read: **not at current capacity without descoping something or adding an engineer.** This doc lays out the math and three options so the trade-off is made deliberately, not discovered in August.

---

## What changed

| | Before 2026-06-02 | After |
|---|---|---|
| R1 net-new builds | 2 (native apply + seam) | **3** (+ native creation) |
| Creation | R4 (BO direction 2026-05-12) | R1 (supersedes that direction) |
| Creation discovery | n/a (was R4) | **None until today's first-pass journey map** |
| FE capacity | Thomas (sole FE) | Unchanged — still one FE |

Creation didn't replace anything in R1. It was *added on top*. And it's the least-understood of the three — the other two have months of discovery (Exp 1-6, the seam analysis); creation has one day.

---

## The capacity math (rough, deliberately conservative)

**Window:** R1 ≈ 3 months. Programme dates: MVP Go-Live 16 Oct 2026; R1 targets Jan 2027 (~Q1'27). Realistic build sprints for R1 ≈ 5-6 two-week sprints.

**The three builds, sized in relative terms** (not story points — orders of magnitude, to be refined at grooming):

| Build | Front-end | Back-end | New data model? | External dependency | Discovery state |
|---|---|---|---|---|---|
| Native apply | Heavy (5 form types, pre-fill UI) | Medium | Application record | ATS (World A) or none (World B) | Good (Exp 1, 3, 4, 5) |
| The seam | Light | **Heavy** (routing, status state machine, webhooks) | Status/event model | ATS webhook + vendor agreement (A9/A14) | Partial (seam analysis) |
| Native creation | **Heavy** (admin UI, preview, validation) | Medium | Posting/creation model | ATS (if World A owns creation) | **Minimal (1 day)** |

**The bottleneck is front-end.** Two of the three builds are FE-heavy (native apply + native creation), and there is **one** FE engineer. Even if back-end keeps pace, the FE work for apply + creation alone plausibly fills the entire R1 window — leaving the seam (the OKR-bearing build) underserved.

**Compounding factors:**
- **Feature Freeze end of Sprint 8 (21 Aug)** and **VAPT from early Aug** sit *before* R1's heaviest build period — the calendar is already compressed.
- **Design dependency:** Amber must design three net-new surfaces (apply, creation, manager dashboard). Design-lock is already flagged as Thomas's biggest week-1 risk for MVP; triple that surface area for R1.
- **The ATS fork (C1) is unresolved.** Until it's decided, neither apply *nor* creation can be finalised — World A and World B are different builds. Every week C1 stays open compresses the build window further.

---

## Three options (pick one)

### Option A — Build all three, add front-end capacity 🟢 *recommended if creation is firm*
Keep creation in R1, but resource it. One FE dev cannot own three net-new FE-heavy builds in 3 months. Add a second FE engineer (or contractor) for R1, scoped to the creation lane.
- **Pro:** Delivers the full loop; honours the product ambition.
- **Con:** Headcount/budget ask; onboarding lag for a new dev.
- **Decision owner:** Adrian + BO (resourcing).

### Option B — Phase creation: discovery in R1, build early R2 🟡 *recommended if capacity is fixed*
Keep apply + seam as R1's committed build (they have discovery and carry the OKR). Run **creation discovery** in R1 (journey map done; add assumptions + a pilot-agency validation), and **build creation first thing in R2**. Creation lands ~1 quarter later but enters R2 fully discovered and de-risked.
- **Pro:** Protects the OKR-bearing builds; creation still arrives soon, better-scoped.
- **Con:** Reverses the just-made "creation in R1" call — needs BO re-ratification.
- **Decision owner:** Michelle proposes, BO ratifies.

### Option C — Build all three at current capacity, accept the risk 🔴 *not recommended*
Commit all three to R1 with one FE. Most likely outcome: the seam (least FE-visible, most BE-complex) slips or ships thin, and the 24-hr latency OKR misses — the one OKR creation doesn't even serve.
- **Pro:** No scope or headcount conversation now.
- **Con:** Sets up an August scramble; highest chance of a missed OKR and a quality compromise on the loop.
- **Decision owner:** default if no decision is made — which is why this doc exists.

---

## My recommendation

**Option B if capacity is fixed; Option A if creation is genuinely non-negotiable for R1.** Either way, *something has to give* — the one path I'd actively flag against is Option C (drift into it by not deciding).

The cleanest sequence regardless of option:
1. **Confirm creation-in-R1 with BO** (it reverses their own R4 call — make the ratification explicit).
2. **Force the ATS decision (C1)** — it gates the buildability of both apply and creation.
3. **Then pick A or B** with the ATS answer in hand.

---

## What I need from this conversation

- [ ] **BO:** ratify (or revisit) creation-in-R1 — you set it to R4 on 2026-05-12
- [ ] **Adrian:** decide Option A (add FE) vs B (phase creation to R2)
- [ ] **Adrian + Barry:** resolve the ATS fork (C1) — it's been open since 2026-05-12 and now blocks two of three builds
- [ ] **If Option A:** start the FE hiring/contractor conversation now (onboarding lag)

---

*Decision-forcing brief. Pairs with the end-to-end blueprint (the three builds) and the create-posting journey map (the new lane). Numbers are deliberately rough — the point is the shape of the trade-off, not precise estimates. Refine at grooming once C1 and the scope option are settled.*
