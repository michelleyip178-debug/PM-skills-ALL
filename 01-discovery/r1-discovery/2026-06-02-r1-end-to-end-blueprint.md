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

1. **Creation stays in OTG.** Agency-side opportunity creation in OTEP is **deferred to R4** (BO Senior Level, 2026-05-12). In R1, postings are created in OTG/C@G and *ingested* into CareerCompass. CareerCompass does not create opportunities in R1.
2. **The apply mechanism is the ATS fork.** Whether the officer applies *inside* CareerCompass (no redirect) or via FormSG depends on the unresolved **World A vs World B** decision (Conflict C1). This is the single biggest unknown in the chain.
3. **The handoff is the risk.** Submission → routing → manager-dashboard → status-back-to-officer is the seam. In World A the ATS owns it; in World B OTEP builds it. Either way, this is where R1 succeeds or fails.

So "creation → submission" in R1 really means: **OTG creates → CareerCompass ingests, lists, and applies → application routes to the manager → status flows back.** The genuinely new R1 build is the middle and the seam, not creation.

---

## End-to-end chain (both swimlanes)

```
  OTG / C@G          CareerCompass (OTEP)              Posting Manager
  (creation)         (officer-facing)                  (agency-facing)
 ─────────────────────────────────────────────────────────────────────
  1. Create posting
     in OTG  ──ingest──►  2. Posting appears in listing
                          3. Officer discovers (filter/search/saved)
                          4. Officer opens detail page
                          5. Officer clicks Apply
                             │
                    ┌────────┴─── THE FORK (C1) ───────────┐
            World A │ apply in-app (ATS-backed)             │ World B: FormSG redirect
                    └────────┬──────────────────────────────┘
                          6. Application submitted
                             │
                    ════════ THE SEAM (handoff) ════════
                             │
                             ▼
                                              7. Application lands in manager queue
                                              8. Manager reviews (POCDEX profile) ⭐
                                              9. Manager shortlists / updates status
                             ◄──── status sync ────┘
                         10. Officer sees status update
                         11. Decision → notify officer
                                             12. Manager marks filled / closes
```

⭐ = the posting-manager aha moment (structured profile, no HR chase).
The `════ SEAM ════` is the part neither existing journey map owns. **That is what this blueprint exists to interrogate.**

---

## Stage-by-stage: who owns what, and what's unknown

| # | Stage | Owner | R1 status | The open question |
|---|-------|-------|-----------|-------------------|
| 1 | Posting created | OTG/C@G | ✅ Exists today | None — out of OTEP scope until R4 |
| 2 | Ingested + listed | OTEP | 🟢 MVP (Sprint 2/3) | Sync freshness — "where's my posting?" trust risk (manager Stage 2/7) |
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

---

## What you need to kick-start (the gap list)

| # | Need | Why | Owner | When |
|---|------|-----|-------|------|
| 1 | **Resolve the ATS fork (C1)** — World A vs B decision doc | Unblocks stages 7-12; everything downstream is conditional on it | Michelle → Adrian/Barry | 🔴 This sprint (decision due June) |
| 2 | **Seam spike** — define routing + status-return for the chosen world | The OKR and the manager persona live here; currently undesigned | Pow Hwee | After C1, Sprint 4-5 |
| 3 | **Confirm creation is R4** — one-line check with Adrian | Your question implied creation might be R1; current decision says R4. Confirm before assuming | Michelle | 🔴 This week |
| 4 | **Manager-side validation** — is the posting-manager journey a real R1 commitment or aspirational? | The journey map exists but the persona is unserved in World B. Confirm it's funded | Michelle → Adrian | Before R1 grooming |
| 5 | **External profile scope (C3)** — who sees it, what fields | Stage 8 (manager review) depends on it; unresolved | Amber + Pow Hwee | R1 grooming kickoff |
| 6 | **Notification mechanism** — none exists in MVP | Stages 10-11 (status back) need it regardless of World A/B | Pow Hwee | Sprint 4-5 |

The other R1 discovery experiments (Exp 1-6 in the discovery plan) cover the officer half well. **Items 1, 2, and 4 above are the genuinely missing pieces** — they're all on the manager side and the seam, which is exactly the half your two journey maps don't connect.

---

## So what

You don't need a new discovery from scratch — you've already mapped both ends. What's missing is the **seam between them**, and a **forced decision on the ATS fork** that determines whether that seam is an integration (World A) or a build (World B). Force C1 first; everything else sequences off it.

The reframe on your original question: in R1, "creation → submission" is really "**ingestion → submission → routing → review → status-back**." Creation is OTG's job until R4. The new, risky, under-discovered part is the routing-and-status seam — and that's where the next discovery effort should go.

---

*Living document — update when C1 (ATS fork) resolves; that decision rewrites stages 5a-12.*
*Source: synthesis of r1-discovery-plan, journey-map-posting-manager-r1, discovery-plan-ats-pivot, r1-candidate-list (C1-C3), user-personas. Current as of 2026-06-02.*
