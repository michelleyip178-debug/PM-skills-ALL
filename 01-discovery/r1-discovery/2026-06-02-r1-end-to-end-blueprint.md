# R1 Service Blueprint — Opportunity Creation → Application Submission → Review

**Date:** 2026-06-02  
**Product:** CareerCompass (OTEP) — internal talent platform, Singapore Public Service  
**Owner:** Michelle Yip  
**State:** R1 reality (Q1'27 target). Maps the chain as it will actually work in R1, given current decisions.  
**Purpose:** The connective tissue between the two existing journey maps. The officer-apply plan and the posting-manager journey each cover one end; this shows the **full chain and the handoff seam** where an application leaves the officer and lands in the manager's queue — the exact point where the World A/B (ATS) fork lives and where integration risk concentrates.

> **Reads with:** [`2026-05-20-r1-discovery-plan.md`](2026-05-20-r1-discovery-plan.md) (officer side), [`journey-map-posting-manager-r1.md`](journey-map-posting-manager-r1.md) (manager side), [`discovery-plan-ats-pivot-2026-05-19.md`](../discovery-plan-ats-pivot-2026-05-19.md) (the ATS fork), [`r1-candidate-list.md`](r1-candidate-list.md) (Conflict C1).

---

## The R1 reality, stated plainly

Three constraints shape the entire chain. None are negotiable for R1:

1. **Creation moves into R1 (changed 2026-06-02).** Agencies now author postings via an **OTEP-native creation form** — the posting lives in OTEP's DB, not OTG. This **supersedes the 2026-05-12 R4 deferral** (see decisions-log). It's the "World B" native path: net-new agency-admin UI, a creation data model, and a validate/publish workflow. Existing OTG/C@G postings still flow in via ingestion alongside it. ⚠️ Material scope expansion — needs BO ratification + a capacity check.
2. **The apply mechanism is the ATS fork.** Whether the officer applies *inside* CareerCompass (no redirect) or via FormSG depends on the unresolved **World A vs World B** decision (Conflict C1). This is the single biggest unknown in the chain — and it now also touches *creation* (native form vs ATS-owned creation are different builds).
3. **The handoff is the risk.** Submission → routing → manager-dashboard → status-back-to-officer is the seam. In World A the ATS owns it; in World B OTEP builds it. Either way, this is where R1 succeeds or fails.

So "creation → submission" in R1 now genuinely means end-to-end inside OTEP: **agency creates (native form) → CareerCompass lists → officer applies → application routes to the manager → status flows back.** Existing OTG/C@G postings still ingest in parallel. The new R1 build is now *both* ends (creation + the seam), not just the middle.

---

## End-to-end chain (both swimlanes)

```
  Agency / OTG          CareerCompass (OTEP)            Posting Manager
  (creation)            (officer-facing)               (agency-facing)
 ──────────────────────────────────────────────────────────────────────

  1a. Agency authors ─native─► 2. Posting appears in listing
      posting in OTEP form              ▲
  1b. OTG/C@G posting ──ingest──────────┘
                        3. Officer discovers (filter / search / saved)
                        4. Officer opens detail page
                        5. Officer clicks Apply
                              │
              ┌───────────────┴─── THE FORK (C1) ───────────────┐
        World A: apply in-app (ATS-backed)      World B: FormSG redirect
              └───────────────┬─────────────────────────────────┘
                              │
                        6. Application submitted
                              │
              ═══════════════ THE SEAM (handoff) ═══════════════
                              │
                              ▼
                                          7. Lands in manager queue
                                          8. Manager reviews profile ⭐
                                          9. Shortlist / update status
                              ┌──── status sync ◄────┘
                              ▼
                       10. Officer sees status update
                       11. Decision → notify officer
                                         12. Manager marks filled / closes
```

**1a is the new R1 work** — agencies create postings natively in OTEP (was R4). 1b (ingest existing OTG/C@G postings) continues in parallel.

⭐ = the posting-manager aha moment (structured profile, no HR chase).  
The `════ SEAM ════` is the part neither existing journey map owns. **That is what this blueprint exists to interrogate.**

---

## Stage-by-stage: who owns what, and what's unknown

| # | Stage | Owner | R1 status | The open question |
|---|-------|-------|-----------|-------------------|
| **1a** | **Posting authored (native form)** | **OTEP (agency HR)** | 🔴 **NEW R1 build** (was R4) | **Net-new: agency-admin UI, creation data model, validate/publish workflow. Native vs ATS-owned? Who can post? Field schema across types?** |
| 1b | Posting ingested (existing) | OTG/C@G → OTEP | 🟢 MVP | Continues in parallel with 1a; sync freshness trust risk |
| 2 | Listed | OTEP | 🟢 MVP (Sprint 2/3) | Native + ingested postings must look consistent in one listing |
| 3 | Discovery (filter/saved) | OTEP | 🟡 R1 (Saved Jobs, filter persistence) | Activation feature for the Passive Watcher persona |
| 4 | Detail page | OTEP | 🟢 MVP | C@G detail overlap (OTEP-87/319) |
| 5 | Apply CTA | OTEP | 🟢 MVP redirect stub | Fake-door signal for A1 (channel choice) |
| **5a** | **Apply mechanism** | **OTEP or ATS** | 🔴 **Forked (C1)** | **World A (in-app) vs World B (FormSG). Unresolved until June.** |
| 6 | Submission | OTEP or FormSG | 🔴 Forked | Pre-fill quality (A2), schema mapping (A11) |
| **7** | **Routing → manager queue** | **❓ THE SEAM** | 🔴 **Undefined** | **In A: ATS receives. In B: where does a FormSG submission go? Email inbox = manager journey doesn't exist.** |
| 8 | Manager review | OTEP (agency dashboard) | 🟡 R1, ATS-gated | POCDEX profile surfacing — the manager aha. Blocked if World B. |
| 9 | Shortlist / status | OTEP or ATS | 🔴 Forked | Audit trail (manager Stage 4 churn risk) |
| 10 | Status back to officer | ❓ THE SEAM | 🔴 Undefined | The 24-hr latency OKR lives here. Needs webhook (A9) + vendor agreement (A14, Exp 6) |
| 11 | Officer notified | OTEP | 🟡 R1 | Notification mechanism — none in MVP |
| 12 | Close / mark filled | OTEP or ATS | 🟡 R1, ATS-gated | Auto-close fallback (manager Stage 6) |

---

## The seam, examined (the actual gap)

The two existing journey maps both go quiet at exactly the same point. The officer plan ends at "submission." The manager journey *starts* at "a posting already exists and officers are applying." **Nobody owns stages 7 and 10 — routing in, and status back.** That's not an oversight in those docs; it's because the seam's behaviour is undecided.

What has to be true for the seam to work:

- **World A (ATS confirmed):** Submission posts to the ATS; ATS is the system of record; manager dashboard reads from ATS; status events webhook back to OTEP (A9) under a signed access agreement (A14/Exp 6). Risk = integration depth + vendor agreement lead time.
- **World B (no ATS):** OTEP must build the application record store, the routing logic, the manager queue, and the status state machine itself. The posting-manager journey **only exists in World B if OTEP builds this** — otherwise FormSG submissions land in email inboxes and the manager persona is unserved until R2 (the explicit warning in the manager journey's "So What").

**This is the decision that unblocks the whole chain.** Until C1 resolves, stages 7-12 can't be designed, and half the manager journey is conditional.

---

## What this blueprint surfaces that the separate maps don't

1. **The manager persona's existence is conditional on the apply mechanism.** World B without an OTEP-built record store = no manager journey at all. The two docs never connect this; read together they do.
2. **The 24-hr latency OKR depends on the seam, not the apply flow.** Teams tend to over-invest in the visible apply UX (stage 5a) and under-invest in stage 10 (status back). The OKR lives in the invisible half.
3. **Three "leap of faith" assumptions cluster on the seam, not the officer experience.** A9 (webhook), A14 (vendor agreement), and the World A/B fork all sit at stages 7/10. The officer-facing assumptions (A1, A2) are real but better understood. **The seam is where discovery effort should concentrate.**
4. **SJR drops out cleanly.** With SJR excluded from MVP ingestion (D 2026-05-21), it never enters this chain at stage 1. If R1 re-adds it (open Scope Concern #3), it's a *new entry at stage 1* — a full lane, not a tweak.
5. **Creation (stage 1a) is now the biggest undiscovered lane.** Moving it from R4 into R1 (2026-06-02) added agency-native authoring with zero existing discovery — no journey map, no assumptions, no experiments — on top of an already-tight R1. Combined with native apply and the seam, this is the central delivery-capacity risk: one FE dev, three months, three net-new builds.

---

## What you need to kick-start (the gap list)

| # | Need | Why | Owner | When |
|---|------|-----|-------|------|
| 1 | **BO ratification + capacity check for creation-in-R1** | Reverses a BO call and is a 2-3x scope add against a 3-month window with one FE dev. Confirm it's real and feasible before anything else | Michelle → Adrian/BO | 🔴 This week |
| 2 | **Creation-side discovery** — net-new, currently zero | Stage 1a has no journey map, no assumptions, no experiments. Who posts? What fields? Native vs ATS? Approval/publish workflow? | Michelle | 🔴 Before R1 grooming |
| 3 | **Resolve the ATS fork (C1)** — World A vs B decision doc | Unblocks stages 7-12 *and* decides native-vs-ATS creation; everything is conditional on it | Michelle → Adrian/Barry | 🔴 This sprint (due June) |
| 4 | **Seam spike** — define routing + status-return for the chosen world | The 24-hr OKR and the manager persona live here; currently undesigned | Pow Hwee | After C1, Sprint 4-5 |
| 5 | **Manager-side validation** — is the posting-manager journey funded in R1? | Journey map exists but persona is unserved in World B; now even more load-bearing since agencies also create | Michelle → Adrian | Before R1 grooming |
| 6 | **External profile scope (C3)** — who sees it, what fields | Stage 8 (manager review) depends on it; unresolved | Amber + Pow Hwee | R1 grooming kickoff |
| 7 | **Notification mechanism** — none exists in MVP | Stages 10-11 (status back) need it regardless of World A/B | Pow Hwee | Sprint 4-5 |

**Items 1 and 2 are the new top priority.** Moving creation into R1 added a whole lane (stage 1a) that has *no discovery at all* — no journey map, no assumption register, no experiments. The officer half (Exp 1-6) is well covered; the seam (items 4-5) was the previous gap; **creation is now a second, larger gap on top.** Before R1 grooming you need a creation-side discovery pass and a hard capacity reality-check, because one FE dev building native creation + native apply + the seam in three months is the central delivery risk.

---

## So what

With creation now in R1, the shape of the work changed. You'd mapped both *ends* of the apply chain, but creation-in-OTEP is a **third, net-new lane (stage 1a) with no discovery behind it** — and it's the largest single addition. The two previous gaps (the seam, and forcing the ATS fork) still stand. So three things now sequence:

1. **Confirm creation-in-R1 is real and feasible** (BO ratification + capacity check) — it reverses a BO call and is a 2-3x scope add.
2. **Run a creation-side discovery pass** — who posts, what fields, native vs ATS, the publish workflow. None of this exists yet.
3. **Force the ATS fork (C1)** — it now decides both the apply seam *and* whether creation is native or ATS-owned.

The reframe on your original question: in R1, "creation → submission" really is end-to-end inside OTEP now — agency-native create → list → apply → route → review → status-back. That's the right ambition, but it roughly doubles the R1 build. The honest next step isn't more mapping; it's a **capacity reality-check** before grooming, because one FE dev cannot build native creation, native apply, and the seam in a 3-month R1 without something giving.

---

*Living document — update when C1 (ATS fork) resolves; that decision rewrites stages 5a-12.*  
*Source: synthesis of r1-discovery-plan, journey-map-posting-manager-r1, discovery-plan-ats-pivot, r1-candidate-list (C1-C3), user-personas. Current as of 2026-06-02.*
