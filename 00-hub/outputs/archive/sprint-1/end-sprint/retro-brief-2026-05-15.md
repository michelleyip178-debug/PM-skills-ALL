# Retro + Demo Brief — 15 May 2026 | Sprint 1 End

**Audience for demo:** Squad retro Mon morning + stakeholder walkthrough (Jacky, Mark) same afternoon.
**Sprint 1 outcome:** Auth working end-to-end. Foundation laid. 5 of 6 OTG field questions resolved. C@G ingestion method confirmed. Sprint 2 unblocked on field questions; still blocked on OTG file import (carries forward).

---

## 🎬 Demo

### Sprint 1 narrative
"Sprint 1 was Login + Foundation + Discovery. We wanted authenticated officers to be able to navigate into Jobs and Opportunities, with the data plumbing in place. Here's what we built."

### Stories to show

| Story | 1-sentence setup | Who demos |
|---|---|---|
| **OTEP-190** — Simple auth through Keycloak | "Officers can now log in through Keycloak — auth runs end-to-end against our test environment." | Pow Hwee / Leo |
| **OTEP-170** — Base layout for Opportunity Listing Page | "Here's the shell of where Sprint 2's opportunity cards will land — navbar, layout, design system wired in." | Thomas |
| **OTEP-223** — Prepare data for OTG ingestion | "We've structured the OTG data so Sprint 2's listing has something to render. Walk through the data model briefly." | Michelle (with Pow Hwee on standby) |

**Mention but don't deep-demo:**
- OTEP-173, OTEP-183 (spikes — output is the decision, not a screen)
- OTEP-209 / 171 / 201 / 207 / 204 / 224 (foundation/DB — call out as "infrastructure in place" without showing schemas)

### Demo order rationale
1. **Auth first** — most tangible, "we can log in now" is the headline for Mark/Jacky who don't care about DB seeds.
2. **Listing page shell second** — naturally sets up the Sprint 2 demo audience ("next sprint, this page fills up").
3. **Data prep third** — the technical bridge between Sprint 1 (plumbing) and Sprint 2 (visible product).

### What NOT to show
- OTEP-202 / OTEP-203 (POCDEX work in progress — incomplete, save for Sprint 2 mid-sprint)
- OTEP-193 / OTEP-192 (not started — explicit acknowledgement in retro, not demo)
- Auth edge cases (OTEP-110, WOG-04/05/06) — sign-off was partial; flag as carry-over, not demo

---

## 🔁 Retro — Signal → Sense → Shift

### Signals (starter prompts — add your own before the session)

1. **Field confirmations from Rama landed 9 days into the sprint (May 13)** — 5 of 6 cleared in one pass, but the lateness blocked Sprint 2 grooming until then.
2. **Sprint 2 scope reshuffled mid-Sprint 1 (May 14)** — necessary call (Pow Hwee's contract-first push + detail-page gap) but consumed Thursday-Friday grooming bandwidth.
3. **The apply-flow decision flipped between May 8 and May 13** — STIP/Gig via FormSG + SJR via OTG redirect → all flows via FormSG, SJR deferred. Driven by BO senior-level direction.
4. **Sprint 2 Jira board didn't match my OS today** — OTEP-85a re-absorbed, OTEP-268 unticketed, OTEP-276 added without me knowing. Discovered at end-of-sprint reconciliation, not before.
5. **Thomas is sole FE and was pulled into cross-squad work** — affected OTEP-170 cadence; binding constraint going into Sprint 2.
6. **OTEP-193 (data model) and OTEP-192 (file import) never started in Sprint 1** — both Sprint 2 critical blockers now.

### Sense check

| Signal | One-off or pattern? | Why it matters |
|---|---|---|
| Late field confirmations from Rama | **Pattern** — already in risks.md as "Rama OTG field mapping" | Upstream dependencies on critical-path items are systemic. Recurs whenever a new sprint needs Rama's input. |
| Sprint 2 mid-sprint scope reshuffle | **One-off (probably)** — driven by a specific contract-first conversation, not a rhythm | But: it's the second scope shift in two sprints. If it happens again Sprint 2 → Sprint 3, it's a pattern. |
| Apply-flow decision flip | **Pattern** — flagged in risks.md as "senior-stakeholder direction shifts frequently" | Scope instability has compounding cost. The longer this goes unaddressed the more rework piles up. |
| Jira ↔ OS drift discovered at end of sprint | **One-off — but only because nobody checks** | If left as-is, will keep happening. There's no recurring reconciliation step. |
| Thomas sole-FE capacity | **Pattern** — already in risks.md, raised at internal groom 2026-05-13 | Won't resolve without leadership intervention. Worth surfacing at retro so the team validates the constraint. |
| Sprint 1 backlog (OTEP-192, 193) didn't move | **Pattern** — same Pow Hwee dependency that caused field-confirmation lag | Pow Hwee carrying too much: auth, POCDEX, data model, file import, FormSG discovery all on his name. |

### Shift — action items for next sprint

| Action | Owner | How we'll know it worked |
|---|---|---|
| **Weekly Jira ↔ OS reconciliation.** Friday afternoon (before next-sprint planning), spend 15 min comparing the upcoming-sprint Jira board against `current-sprint.md` and `story-id-map.md`. Catch ID changes / rename / scope splits before they become drift. | Michelle | At Sprint 2 finalisation, zero unknown Jira IDs and zero missing OS references. |
| **Pow Hwee load check at Sprint 2 planning.** Explicitly count how many stories have Pow Hwee as primary owner. If >3 critical-path stories, flag as a capacity risk before planning ends — not at mid-sprint. | Michelle to raise, Pow Hwee to confirm | At Sprint 2 mid-sprint review, Pow Hwee's stories all in progress (not "not started"). |
| **Log every scope decision flip within 24h with the rationale.** If steering or a BO meeting changes a previous call, the new decision lands in `decisions-log.md` same-day with explicit supersede note. | Michelle | At Sprint 2 retro, count of decisions flipped without same-day log = 0. |

**Pick 1 to commit to** — running all three dilutes focus. **Recommended:** the Jira ↔ OS reconciliation. Smallest effort, highest leverage, and it would have caught today's surprises before retro.

---

## Michelle's Retro Mindset

You're a participant here — not a facilitator, not a defender. Rama facilitates.

**Three things to resist:**
1. **Don't justify the Sprint 2 reshuffle.** If someone raises it as churn, listen first. The call was right; the surfacing of *why* it was needed (no detail page in the original scope) is more valuable than your defence.
2. **Don't soften the carry-over count.** Six stories carry to Sprint 2 plus four auth edge-cases. That's a lot. Name it. Don't pre-explain.
3. **Don't propose multiple shifts.** You're practising PM mode — pick one shift, recommend it, defend it if challenged. Coming with three options is BA mode.

**PM growth lens (from GOALS.md):**
- *Thinking in outcomes* — Sprint 1 sprint goal was outcome-shaped ("officers can log in and navigate to Jobs and Opportunities"). It mostly held. Notice that.
- *Stakeholder influence* — the apply-flow flip is the test case. Did you bring Adrian or Mark along *before* the decision changed, or react to it after? Same question for Sprint 2's scope reshuffle. Honest answer in your own head — not the retro.
- *Roadmapping and prioritisation* — the Sprint 2 cut-line call (OTEP-285 first if cut) is the kind of pre-decision you want to be making more of. Good.

---

*Generated: 2026-05-15. Source files: `context/current-sprint.md` (post-archive), `context/decisions-log.md`, `context/risks.md`, `context/open-items.md`, `outputs/archive/sprint-1/end-sprint/` snapshots.*
