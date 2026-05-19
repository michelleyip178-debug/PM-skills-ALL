# Internal Grooming Framework

A reusable structure for the internal squad groom (Wed W1). Michelle leads content, Rama facilitates. The goal: walk out with a committed sprint scope the team is confident they can ship.

**Order matters:** capacity first, then readiness, then scope, then commitment. Don't start with "here are 9 stories" before establishing "we have 5 FE-days."

---

## Phase 1: Close the Previous Sprint (10 min)

Get the facts before planning the next one. What overflows directly affects capacity.

| Question | Who answers | What you're looking for |
|----------|------------|------------------------|
| Which stories are done, which carry over, which are still in backlog? | Pow Hwee / engineers | Clear done/carry-over/dropped for each item |
| For carry-over items — how many days do they take into the new sprint? | Engineer who owns it | A number, not "a bit more work" |
| Are there Sprint N blockers that become Sprint N+1 blockers if they don't land by Friday? | Squad | Identify which carry-over items are on the critical path |
| Any decisions from Sprint N that change what we planned for Sprint N+1? | Michelle | Scope shifts, field confirmations, stakeholder direction changes |

**Output:** Carry-over list with estimated days. Update `context/current-sprint.md` carry-over table.

---

## Phase 2: Establish Capacity (5 min)

Do this before showing stories. The team should know the budget before they see the menu.

| Question | Who answers | What you're looking for |
|----------|------------|------------------------|
| Who's available for the full sprint? Any leave, public holidays, training? | Everyone | Days lost. Mark on a whiteboard or shared doc. |
| Any cross-squad pulls or dependencies from other teams? | Engineers | Thomas-type risks — sole FE, external requests eating capacity |
| How many dev-days do we actually have, after carry-over and ceremonies? | Pow Hwee | A realistic number. 3 engineers x 8 working days = 24 max, minus ceremonies (~2 days each), minus carry-over days. |
| Does carry-over work change anyone's availability for new stories? | Engineers | If someone is finishing Sprint N work for 3 days, they have 5 days for Sprint N+1, not 8. |

**Output:** Available capacity in dev-days. Write it on the board. Every story you add has to fit within this number.

---

## Phase 3: Story Readiness (per story, 5-15 min each)

Walk each candidate story against Rama's DoR. Don't estimate until readiness is confirmed.

### Per-story checklist

| DoR item | Question to ask | If not met |
|----------|----------------|------------|
| Story format + ACs | "Are the ACs clear and testable?" | Rewrite in the room or defer |
| Subtasks + test cases | "Are all subtasks identified, including test cases?" | Create in the room (this is a grooming output, not pre-work) |
| UI/UX designs | "Amber — are designs linked to every AC?" | Groom on wireframes/defaults. Note design dependency. |
| Feature flag | "Is the feature flag identified with an entry point?" | Define in the room |
| API contract | "Pow Hwee — is the API contract documented?" | Define in the room or log as a day-1 Sprint task |
| Dependencies | "What does this story need from outside the squad before dev starts?" | Confirmed = green. Assumed = state the fallback. Unknown = risk. |
| Open items | "Are there unresolved questions that block dev?" | Resolve in the room, or state the default and move on |

### Questions that sharpen stories

- "What's the simplest version of this story that still delivers value?"
- "What edge cases will Pow Hwee probe?" (pre-empt them)
- "What does Rethna need to write test scripts for this?" (ACs must be testable)
- "Is this one story or two? Can it be split into a smaller shippable slice?"

---

## Phase 4: Scope and Priority (10 min)

This is where you make the call. Not "what should we build" but "what do we commit to."

| Question | Purpose |
|----------|---------|
| "What's the sprint goal in one sentence?" | Anchors every scoping decision. If a story doesn't serve the goal, it's a candidate for deferral. |
| "What's the minimum set of stories that proves the sprint goal?" | Separates must-haves from nice-to-haves |
| "If we can only ship X of these Y stories, which ones do we cut?" | Forces ranking. Don't let the team treat all stories as equal priority. |
| "Is there anything in here that doesn't contribute to the sprint goal?" | Catches scope creep disguised as "while we're at it" |
| "Are any stories covering the same ground? Can we absorb one into another?" | Catches overlap (e.g. OTEP-129 absorbed into OTEP-85) |

### Priority tiers

Assign each story before estimating:

| Tier | Definition | Rule |
|------|-----------|------|
| **Must** | Sprint goal fails without it | Commit. If this slips, sprint goal is missed. |
| **Should** | Significantly improves the sprint but goal technically works without it | Commit if capacity allows. First to defer if overloaded. |
| **Could** | Nice to have, low risk to defer | Include only if capacity is comfortable. First to cut. |

---

## Phase 5: Risk and Fallback (5 min)

| Question | Purpose |
|----------|---------|
| "What's the biggest thing that could go wrong this sprint?" | Name the risk out loud so it's shared, not just in your head |
| "If [dependency] doesn't land by day 3, what do we do?" | Define the fallback now, not mid-sprint in a panic |
| "Which story is most likely to slip, and what does that cascade into?" | Identify the domino — usually the full-stack story everything else depends on |
| "Is there a story we should flag as contingency — in if capacity allows, out if it doesn't?" | Gives the team a clean cut point without re-scoping mid-sprint |

---

## Phase 6: Commitment (5 min)

Close the session with explicit agreement, not assumed consensus.

| Question | Purpose |
|----------|---------|
| "Our Sprint N+1 commitment is [list stories]. Is everyone confident this is achievable in 2 weeks?" | Direct ask. Wait for answers. |
| "What would make you say no?" | Surfaces hidden concerns. Engineers often stay silent unless directly asked. |
| "If something comes up mid-sprint, which story do we drop first?" | Pre-agreed cut order. Saves a meeting later. |
| "Who picks up what?" | Engineers self-select, but confirm no story is unowned. |

**Output:** Committed story list, priority tiers, pre-agreed cut order, story owners.

---

## Phase 7: Deflection List (2 min)

Prepare 3-5 ready responses for topics that will come up but are out of scope. Say them once, move on.

Format: "[Topic] — that's Sprint N+2 / R1. Logging it, not grooming it."

---

## After Grooming

- [ ] Update `context/current-sprint.md` with confirmed Sprint N+1 scope
- [ ] Update `projects/sprint-allocation.md` if stories moved
- [ ] Log decisions in `context/decisions-log.md`
- [ ] Add new open items to `context/open-items.md`
- [ ] Update `projects/otep-mvp/sprint-checklists.md` with DoR status
- [ ] Share committed stories + ACs with Rethna for QA review prep

---

## Quick Reference: Session Flow

```
1. Close previous sprint          (10 min)  — carry-over, blockers
2. Establish capacity             ( 5 min)  — dev-days available
3. Story readiness (per story)    (30 min)  — DoR checklist, subtasks
4. Scope and priority             (10 min)  — must/should/could tiers
5. Risk and fallback              ( 5 min)  — biggest risk, cut order
6. Commitment                     ( 5 min)  — explicit yes from team
7. Deflection list                ( 2 min)  — out-of-scope responses
                            Total: ~65 min
```

---

*Created 2026-05-13. Review and adjust after each sprint's retro — what worked, what was missing, what took too long.*
