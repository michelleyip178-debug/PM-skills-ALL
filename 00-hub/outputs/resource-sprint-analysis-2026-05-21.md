# Sprint Allocation × Resources × MVP Scope — Analysis
> Generated: 2026-05-21. Current: Sprint 2 Week 1.
> Feature build window: S1–S8 (4 May – 21 Aug). Feature Freeze: Fri 21 Aug.

---

## Team

| Person | Role | Constraint |
|--------|------|------------|
| Thomas | Frontend engineer | **Sole FE developer. Fielding cross-squad pulls. Single point of failure for all UI work.** |
| Leo (Léo) | Backend engineer | Primary backend dev. Carries data model, ingest, POCDEX, auth backend. |
| Pow Hwee | Tech lead | Grooming facilitator + architecture decisions + code reviews + POCDEX API + C@G ingestion. |
| Amber | Designer | Shared across squads. Design lock date still unset (#22). |
| Michelle | PM | Owns backlog, ceremonies, stakeholder chain. |

**Net dev days per sprint (2-week sprint after public holidays):**

| Sprint | Dev days | Holiday impact |
|--------|----------|----------------|
| S2 (18–29 May) | ~9 | Hari Raya Haji 27 May |
| S3 (1–12 Jun) | ~9 | Vesak Day 2 Jun |
| S4 (15–26 Jun) | 10 | — |
| S5 (29 Jun–10 Jul) | 10 | — |
| S6 (13–24 Jul) | 10 | — |
| S7 (27 Jul–7 Aug) | 10 | — |
| S8 (11–21 Aug) | ~9 | National Day 11 Aug (in lieu) |

---

## The Binding Constraint: Thomas (FE)

All user-visible work goes through Thomas. There is no second FE developer.

### FE story count by sprint

| Sprint | FE stories for Thomas | Workload classification |
|--------|----------------------|------------------------|
| S2 | OTEP-170 (in progress), OTEP-85, OTEP-128, OTEP-267, OTEP-268, OTEP-129, OTEP-314 sub-task = **6–7** | 🔴 Very heavy |
| S3 | OTEP-86, OTEP-317, OTEP-87, OTEP-319, OTEP-131 + OTEP-318 (conditional) = **5–6** | 🔴 Overloaded |
| S4 | OTEP-130, OTEP-88, instrumentation + auth (if WOG AD clean): OTEP-71/110/304/305, WOG-06 = **3 (no auth) / 8 (auth)** | ⚠️ Fine without auth / 🔴 Overloaded with auth |
| S5 | Auth (realistic: OTEP-71/110/304/305, WOG-06) + C@G (OTEP-89, US-10) = **7** | 🔴 Overloaded — worst sprint |
| S6 | CSC SSO (some FE), OTEP-133, WOG-02, WOG-07 = **4** | ⚠️ Heavy |
| **Total S2–S6** | **~25–32 FE stories** | — |

### FE capacity vs demand

| Metric | Number |
|--------|--------|
| FE-touching MVP stories (S2–S6) | ~28 |
| Heavy stories (~2.5 dev-days each) | ~10 |
| Medium stories (~1.5 dev-days each) | ~10 |
| Light stories (~0.5 dev-days each) | ~8 |
| **Estimated FE dev-days needed** | **~38–42 days** |
| **Thomas's capacity S2–S6** (9–10 days/sprint × 5 sprints, minus meetings/reviews ~15%) | **~38–43 days** |

**The math is technically possible — but only with:**
- Zero cross-squad pulls
- No design changes after lock date (design lock date still not set — #22)
- No rework
- Every estimate being accurate (they rarely are)
- Thomas at full capacity every sprint

**Evidence it's already slipping:** OTEP-170 (base listing layout) was started in Sprint 1, carried to Sprint 2, and is still In Progress at Sprint 2 Week 1. That's one story taking 2+ sprints.

### The Sprint 5 collapse scenario

If WOG AD slips (working assumption), auth lands in Sprint 5 alongside C@G. Thomas would have:
- Auth UI: OTEP-71 (login screen), OTEP-110 (fail states), OTEP-304 (session), OTEP-305 (logout), WOG-06 (onboarding)
- C@G: OTEP-89 (C@G detail page), US-10 (confirmation)

That's **7 FE stories in 10 dev days.** It cannot be delivered by one person. Something must move.

---

## Backend Load: Leo + Pow Hwee

More manageable — two people with clear ownership split. Risks are sequencing, not volume.

### Leo's story load

| Sprint | Stories | Risk |
|--------|---------|------|
| S2 | OTEP-193 (data model), OTEP-288 (stub — done), OTEP-295 (mock endpoint), OTEP-313 (ingest table), OTEP-316 (real DB query) | Heavy but clear sequence |
| S3 | OTEP-192 (recurring ingest job), OTEP-271 (POCDEX local DB) | Manageable |
| S4 | OTEP-202 (POCDEX seed DB), ringfencing backend if auth lands (OTEP-127 part) | OK |
| S5 | OTEP-127 (ringfencing BE — realistic) | OK |

**Leo's sequencing risk:** OTEP-316 (real DB query) depends on OTEP-193 (data model) AND OTEP-313 (ingest table) — both in Sprint 2. If either slips, OTEP-316 can't start. OTEP-192 (Sprint 3 ingest job) also depends on OTEP-193 landing cleanly.

### Pow Hwee's story load

| Sprint | Stories | Risk |
|--------|---------|------|
| S3 | OTEP-203 (POCDEX API service) | OK — architecture decision owner |
| S4 | Story D (C@G ingestion setup), auth backend (OTEP-71 BE if clean) | C@G ingestion story is unwritten — scope unknown |
| S5 | OTEP-71 BE (auth — realistic) | OK |

**Pow Hwee overhead:** Tech lead reviews, grooming facilitation, architecture calls, POCDEX/Daryll engagement. This isn't counted in story points but consumes ~30% of sprint capacity.

---

## Sprint-by-Sprint Load Table

| Sprint | Thomas (FE) | Leo (BE) | Pow Hwee (BE/TL) | WOG AD status | Key risk |
|--------|-------------|----------|-------------------|---------------|----------|
| S2 | 6–7 stories 🔴 | 5 stories ⚠️ | Tech lead + C@G spike | Not started | Thomas volume; Leo dependency chain |
| S3 | 5–6 stories 🔴 | 2 stories ✓ | POCDEX API service | Onboarding in progress (if Adrian responds) | Thomas overload; Vesak Day |
| S4 | 3 (no auth) / 8 (auth) 🔴 | 1–2 stories ✓ | C@G ingestion + auth if clean | WOG AD done (best case) or not | Entire sprint hostage to WOG AD if no contingency |
| S5 | 7 stories 🔴 (auth + C@G) | 2 stories ✓ | Auth BE + support | WOG AD done (realistic) | **Worst sprint — Thomas collapses under auth + C@G combined** |
| S6 | 4 stories ⚠️ | 1 story ✓ | CSC SSO + admin | CSC SSO integrating | Still heavy for Thomas |
| S7 | Testing only ✓ | Testing only ✓ | Testing only ✓ | Done | OK if S4–S6 hit |
| S8 | UAT ✓ | UAT ✓ | UAT ✓ | Done | OK if Feature Freeze holds |

---

## Gap Analysis: What Doesn't Fit

Based on Thomas's capacity of ~38–42 FE dev-days and ~38–42 days of demand, the plan is at capacity with **zero margin.**

These stories are at highest risk of not fitting:

| Story | Sprint | FE weight | Risk reason |
|-------|--------|-----------|-------------|
| OTEP-318 — filter by category | S3 | Medium | Already conditional; will push Thomas over the S3 limit |
| OTEP-89 — C@G detail page | S5 | Heavy | Competes with auth UI if auth lands in S5 |
| WOG-06 — first-time login | S5 | Medium | Same |
| US-10 — application confirmation | S4/S5 | Light–Medium | May slip if auth + FormSG fill S4 |
| WOG-07 — RBAC | S6 | Medium | Admin login + RBAC in same sprint may be too much |
| OTEP-133 — EDM deep-link | S6 | Light | Low risk individually, but adds to S6 pile |
| Instrumentation | S4 | Light | Often deprioritised under delivery pressure |

### Stories with no Jira ticket yet (create before Sprint Planning 29 May)

| Priority | Story | Needed by |
|----------|-------|-----------|
| 🔴 Now | Story B — CSC SSO integration | Before S5 planning |
| 🔴 Now | Story D — C@G API ingestion setup | Before S4 planning |
| 🔴 Now | OTEP-131 — null `formsg_url` fallback | S3 |
| 🟡 Soon | US-10 — Application confirmation | S4 planning |
| 🟡 Soon | WOG-06 — First-time login (ticket) | S4/S5 planning |
| 🟡 Soon | Instrumentation story | S4 planning |
| 🟡 Before S4 | WOG-10 — Resolve agency from AD identity | S4 planning |
| 🟡 Before S4 | WOG-17 — Complete logout shared devices | S4 planning |
| 🟡 Before S6 | WOG-02 — Admin login (ticket) | S6 planning |
| 🟡 Before S6 | WOG-07 — RBAC (ticket) | S6 planning |

---

## Three Things That Must Be Resolved to Make This Plan Work

### 1. Thomas FE overload — raise with Pow Hwee now
The S5 collapse scenario (auth + C@G on Thomas in same sprint) is undeliverable. Mitigation options:
- **Option A:** Split S5 — auth UI in S5, C@G UI deferred to S6. S6 gets even heavier but avoids the S5 crash.
- **Option B:** Vertical slice. Leo or Pow Hwee picks up light FE tasks (simple redirect, disabled state) to relieve Thomas.
- **Option C:** Descope OTEP-89 (C@G detail) from MVP — officer taps C@G card and goes directly to Careers@Gov site (deep-link only, no OTEP detail page). Reduces FE by 1 heavy story.
- **Option D:** Get a second FE resource. This is the real fix. One FE developer for 52 stories is structurally insufficient.

### 2. Design lock date (#22) — overdue, set with Amber this week
Every design change mid-sprint = Thomas rework = FE velocity drops. At current capacity, there is no room for rework. Open item #22 has been open since Sprint 2 Week 1.

### 3. Split Sprint 5 before it arrives
Even if auth lands in S4 (best case), Sprint 5 carries C@G + FormSG webhook + confirmation. That's still 4 medium-heavy stories. Define the S5 cut-line now — not at Sprint 4 planning when you're already under pressure.

---

## Summary Verdict

| Dimension | Verdict | Headline |
|-----------|---------|----------|
| Scope | ⚠️ Tight | 52 stories, 10 without tickets. Scope is MVP-sized but has no slack. |
| Thomas (FE) | 🔴 At capacity | 28 FE stories in 5 sprints with zero margin. S5 (auth + C@G combined) is undeliverable as currently planned. |
| Leo (BE) | ✓ Manageable | Load is sequencing-sensitive, not volume-constrained. Key: OTEP-193 landing clean in S2. |
| Pow Hwee (TL) | ⚠️ Overhead risk | Story load is fine but tech lead overhead (reviews, POCDEX, Daryll, auth) consumes ~30% capacity not counted in Jira. |
| Auth timing | 🔴 High risk | Working assumption = S5. Best case = S4. Both require WOG AD onboarding to start this week. |
| CSC SSO | 🔴 Untracked | No Jira story. External 4-week process. Michelle owns. |
| Feature Freeze (21 Aug) | ⚠️ Achievable, not guaranteed | Holds in the best case. Fails if WOG AD delays past June AND Thomas gets cross-squad pulls AND design lock isn't set. |

**The plan is deliverable if three things go right: WOG AD starts this week, Thomas has no cross-squad pulls, and design locks before Sprint 3. None of those are currently confirmed.**

---

*Generated: 2026-05-21. Source: sprint-allocation.md, story-id-map.md, mvp-scope-2026-05-21.md, sprint-status.md, risks.md.*
