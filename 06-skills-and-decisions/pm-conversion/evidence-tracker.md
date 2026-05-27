# PM Conversion — Evidence Tracker

**Updated:** 2026-05-27 (Sprint 2 — draft rows added; finalise at sprint boundary 29–30 May)
**Next update:** Sprint 3 boundary (13 Jun)

> Update this at every sprint boundary. Ask: "What did I do this sprint that a BA wouldn't have done?"
> Each entry needs: what you did, why it's PM-mode (not BA-mode), and where the artifact lives.

---

## 1. Outcomes Thinking

*Framing work around user/business outcomes before jumping to specs or solutions.*

| Date | What I Did | Why It's PM-Mode | Artifact |
|------|-----------|------------------|----------|
| 2026-05-06 | Wrote PRD hypothesis as "If we provide X, then users will Y, leading to Z" — not a feature list | Anchored the entire PRD to a measurable outcome (channel migration >= 50%) before defining capabilities | [prd.md Section 2](../otep-mvp/prd-opportunities.md) |
| 2026-05-06 | Defined success metrics in 3 tiers: outcome, input, guardrail — each with specific event keys | Moved from "did we build it" to "did it work" — built measurement into the spec, not as an afterthought | [prd.md Section 5](../otep-mvp/prd-opportunities.md) |
| 2026-05-06 | Sprint goals written as officer outcomes ("Officers can browse, filter, and scan all opportunity types") not delivery outputs | Changed the framing from "deliver OTEP-85, OTEP-86, US-03" to what the user can do by sprint end | [otep-mvp-release.md](../../02-prd/otep-mvp-release.md) |
| 2026-05-21 | Decided to exclude SJRs from MVP ingestion entirely, rather than ingesting them with no apply action | The BA move would be to document the UX problem with SJR cards and wait for a decision. I made the call: no card beats a confusing card with no action. The outcome framing — "officers shouldn't see something they can't act on" — drove the technical scope decision. | [decisions-log.md](../decisions-log.md) — 2026-05-21 entry |
| 2026-05-21 | Deferred auth epic (OTEP-71/110/304/305) from Sprint 3 with a product risk rationale: "shipping auth without a test environment is a go-live risk, not a delivery slip" | Didn't treat the WOG AD UAT gap as a planning problem. Framed it as: what outcome breaks if we ship unvalidated auth? That reframe turned a schedule decision into a product quality decision. | [decisions-log.md](../decisions-log.md) — 2026-05-21 entry |
| 2026-05-27 | Caught that OTEP-192 was written with mechanism-only ACs ("the job reads OTG exports and upserts records") before Sprint 3 planning — rewrote it as a user story with testable criteria covering ingestion, lifecycle, validation, scheduling, and failure handling | A BA surfaces the gap in a ticket comment. A PM fixes it before the team walks into planning and sizes a story nobody can test. The story would have been built; whether it was built to the right outcomes was the question. | [jira-sync/OTEP-Pathfinder-Sprint-3/OTEP-192.md](../../03-stories/jira-sync/OTEP-Pathfinder-Sprint-3/OTEP-192.md) |

---

## 2. Stakeholder Influence

*Building a narrative, bringing people along, making recommendations — not just presenting options.*

| Date | What I Did | Why It's PM-Mode | Artifact |
|------|-----------|------------------|----------|
| 2026-05-06 | Researched OTG vs C@G filter taxonomies, evaluated 3 options, recommended Option C (hybrid) with clear rationale | Didn't present "here are three options, what do you think?" — made a call and explained why | [categorisation-research.md](../otep-mvp/research/categorisation-research.md) |
| 2026-05-06 | Mapped validation plan: who to present to (Amber, Pow Hwee, Adrian, Jacky/XZ) and what each person needs to hear | Thought about influence path, not just the recommendation itself | [categorisation-research.md, Step 4](../otep-mvp/research/categorisation-research.md) |
| 2026-05-08 | Recommended descoping competency match ratio to R1 with specific rationale ("high cost for MVP vs low proven value") | Made the call, logged the decision with reasoning — didn't wait to be told | [decisions-log.md](../decisions-log.md) |
| 2026-05-11 | Structured the BO involvement model: BOs join for problem framing, scope decisions, and sprint goals — out of routine grooming and sizing unless a business decision is needed | Stakeholder management, not stakeholder reporting. Defined the terms of engagement so BOs stayed informed without becoming a sprint bottleneck. The boundary held through Sprint 2 grooming. | [decisions-log.md](../decisions-log.md) — 2026-05-11 entry; [archive-meetings/one-offs/2026-05-11-bo-involvement-model.md](../../04-ceremonies/archive-meetings/one-offs/2026-05-11-bo-involvement-model.md) |
| 2026-05-21 | Identified `careercompass.gov.sg` as the unblocking domain for WOG AD onboarding, briefed Adrian with two named asks, and got the intranet URL submitted — starting the 2-week approval clock | The risk had been logged for weeks with no movement. I found the specific unblocking action (the domain name), framed it as two concrete asks for Adrian rather than a general "we need WOG AD", and moved it forward. A BA writes the risk down. A PM removes it. | [open-items.md](../../00-hub/open-items.md) — #26; [decisions-log.md](../decisions-log.md) — 2026-05-21 and 2026-05-22 entries |
| 2026-05-22 | Set a design lock date with Amber (2026-05-22) — the first time the sprint had a clear design cut-off | BAs track design status. PMs negotiate the boundary that prevents design from becoming a mid-sprint moving target. Framing it as "protecting Amber from last-minute AC changes" made it a shared interest, not a constraint I imposed on her. | [decisions-log.md](../decisions-log.md) — 2026-05-22 entry |

---

## 3. Roadmapping and Prioritisation

*Sequencing work against outcomes, saying no, making trade-off calls.*

| Date | What I Did | Why It's PM-Mode | Artifact |
|------|-----------|------------------|----------|
| 2026-05-06 | Built 5-sprint plan sequenced by dependency chain, not feature grouping — Auth → Hub → Discovery → Application → Polish | Sequencing decision: what to build first was driven by what unblocks what, not what's easiest | [otep-mvp-release.md](../../02-prd/otep-mvp-release.md) |
| 2026-05-08 | Made 5 MVP-vs-R1 scope decisions in one session: binary competencies, no "Save for later", no endorsement backend, FormSG/OTG routing, search in MVP | Said no to things that were reasonable requests. Each had a rationale logged. | [decisions-log.md](../decisions-log.md) |
| 2026-05-11 | Populated scoping gaps tracker with 13 items — 10 open, 3 formally deferred to R1 with decision date and rationale | Scope discipline: every deferral is a conscious decision, not a "we'll get to it" | [scoping-gaps-tracker.md](../otep-mvp/scoping-gaps-tracker.md) |
| 2026-05-11 | Flagged target date discrepancy (Sep vs Dec) as an open decision needing Adrian's call — didn't silently pick one | Owned the ambiguity instead of ignoring it. Raised it as a decision to make, not a problem to report. | [prd.md Section 9](../otep-mvp/prd-opportunities.md) |
| 2026-05-21 | Rebuilt Sprint 3 from scratch when the WOG AD UAT blocker surfaced — replaced auth stories with filter work (OTEP-86/317/318) and the apply loop (OTEP-87/319), sequenced by what was actually ready | A BA updates the sprint log. I looked at what was groomed, what had live dependencies, and what would deliver value without auth — then restructured the sprint goal around that. Sprint 3 still delivers officer-facing value; it just doesn't depend on an environment we don't have. | [decisions-log.md](../decisions-log.md) — 2026-05-21 entry; [sprint-status.md](../../00-hub/sprint-status.md) |
| 2026-05-20 | Decided to stagger POCDEX plumbing (OTEP-271/203) into Sprint 3 rather than Sprint 4, to unblock Sprint 4 ringfencing — a forward-looking sequencing call that doesn't show up in any Sprint 3 deliverable | The risk was that Sprint 4 would block on POCDEX infra not existing. I sequenced the backend plumbing one sprint ahead of the feature that needs it. Nobody asked me to think two sprints ahead; I noticed the dependency and acted on it. | [decisions-log.md](../decisions-log.md) — 2026-05-20 entry |
| 2026-05-26 | Dropped FormSG pre-fill from MVP scope — defended the boundary with a rationale tied to the 2026-03-12 steering direction (OTEP owns the apply experience end-to-end; FormSG is the MVP vehicle, not the long-term solution) | Pre-fill is a reasonable thing to want. But it adds complexity to a path we're going to deprecate in R1. I didn't say "too hard." I said "building the right thing for a throwaway path is the wrong investment" — and tied it back to a steering decision that predated me. That's scope discipline with a narrative. | [decisions-log.md](../decisions-log.md) — 2026-05-26 entry; [open-items.md](../../00-hub/open-items.md) — #14 resolved |

---

## 4. Cross-Cutting (PM Operating Behaviour)

*Evidence that doesn't fit neatly into one gap but shows PM-mode operating.*

| Date | What I Did | Why It's PM-Mode | Artifact |
|------|-----------|------------------|----------|
| 2026-05-06 | Built a PM operating system with context files, slash commands, and workflows that enforce PM habits | Designed my own working environment to reinforce the transition — BAs don't build operating systems | This repo |
| 2026-05-07 | Wrote 20 user stories across 5 groups with full AC, edge cases, and DoR checklists | Not just writing stories — organised them by user journey, mapped dependencies, created a pipeline | [user-stories.md](../otep-mvp/stories/index.md) |
| 2026-05-11 | Self-audited the OS, identified that it had more scaffolding than content, and fixed it | The meta-awareness to critique your own system and act on it — that's PM self-management | Conversation record |
| 2026-05-21 | Before Sprint 2 finalisation, identified 12 Jira board actions needed (stories to move, add, remove, or verify) across Sprint 2, Sprint 3, and Sprint 4+ — proactively cleared the board before planning | A BA waits for the ceremony to surface these. I audited the board before the ceremony so the room could spend its time on decisions, not hygiene. The board was clean going into planning. | [sprint-status.md](../../00-hub/sprint-status.md) — Jira board cleanup section |
| 2026-05-27 | Audited all Sprint 3 candidate stories against DoR the day before planning — caught two AC conflicts (OTEP-128 "closed" notice duplicating OTEP-129; OTEP-129 visibility rule duplicating OTEP-85), resolved both in Jira before the session | Pow Hwee had flagged these conflicts in grooming comments three weeks earlier. Nobody had acted on them. If they'd surfaced in the planning room, it would have been 20 minutes of scope re-litigation. Closing them beforehand is PM housekeeping with sprint velocity consequences. | [jira-sync Sprint 2 OTEP-128.md](../../03-stories/jira-sync/Sprint-34616-OTEP-Pathfinder-Sprint-2/OTEP-128.md); [OTEP-129.md](../../03-stories/jira-sync/Sprint-34616-OTEP-Pathfinder-Sprint-2/OTEP-129.md) |

---

## How to Update This File

At every sprint boundary (Step 2 of the Sprint Boundary workflow):

1. Ask yourself: "What did I do this sprint that a BA wouldn't have done?"
2. For each item: what's the artifact? Where does it live?
3. Add one row per competency area. Even one entry per sprint compounds.
4. If you can't find anything for a competency area — that's the signal for where to focus next sprint.

Don't manufacture evidence. The best entries come from decisions you made during normal OTEP delivery that happened to demonstrate PM thinking. If you're doing PM work, the evidence creates itself.
