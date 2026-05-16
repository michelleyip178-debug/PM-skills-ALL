# PM Conversion — Evidence Tracker

**Updated:** 2026-05-11 (Sprint 1)
**Next update:** Sprint 2 boundary (May 30)

> Update this at every sprint boundary. Ask: "What did I do this sprint that a BA wouldn't have done?"
> Each entry needs: what you did, why it's PM-mode (not BA-mode), and where the artifact lives.

---

## 1. Outcomes Thinking

*Framing work around user/business outcomes before jumping to specs or solutions.*

| Date | What I Did | Why It's PM-Mode | Artifact |
|------|-----------|------------------|----------|
| 2026-05-06 | Wrote PRD hypothesis as "If we provide X, then users will Y, leading to Z" — not a feature list | Anchored the entire PRD to a measurable outcome (channel migration >= 50%) before defining capabilities | [prd.md Section 2](../otep-mvp/prd-opportunities.md) |
| 2026-05-06 | Defined success metrics in 3 tiers: outcome, input, guardrail — each with specific event keys | Moved from "did we build it" to "did it work" — built measurement into the spec, not as an afterthought | [prd.md Section 5](../otep-mvp/prd-opportunities.md) |
| 2026-05-06 | Sprint goals written as officer outcomes ("Officers can browse, filter, and scan all opportunity types") not delivery outputs | Changed the framing from "deliver OTEP-85, OTEP-86, US-03" to what the user can do by sprint end | [otep-mvp-release.md](../../resources/otep-mvp-release.md) |

---

## 2. Stakeholder Influence

*Building a narrative, bringing people along, making recommendations — not just presenting options.*

| Date | What I Did | Why It's PM-Mode | Artifact |
|------|-----------|------------------|----------|
| 2026-05-06 | Researched OTG vs C@G filter taxonomies, evaluated 3 options, recommended Option C (hybrid) with clear rationale | Didn't present "here are three options, what do you think?" — made a call and explained why | [categorisation-research.md](../otep-mvp/research/categorisation-research.md) |
| 2026-05-06 | Mapped validation plan: who to present to (Amber, Pow Hwee, Adrian, Jacky/XZ) and what each person needs to hear | Thought about influence path, not just the recommendation itself | [categorisation-research.md, Step 4](../otep-mvp/research/categorisation-research.md) |
| 2026-05-08 | Recommended descoping competency match ratio to R1 with specific rationale ("high cost for MVP vs low proven value") | Made the call, logged the decision with reasoning — didn't wait to be told | [decisions-log.md](../../context/decisions-log.md) |

---

## 3. Roadmapping and Prioritisation

*Sequencing work against outcomes, saying no, making trade-off calls.*

| Date | What I Did | Why It's PM-Mode | Artifact |
|------|-----------|------------------|----------|
| 2026-05-06 | Built 5-sprint plan sequenced by dependency chain, not feature grouping — Auth → Hub → Discovery → Application → Polish | Sequencing decision: what to build first was driven by what unblocks what, not what's easiest | [otep-mvp-release.md](../../resources/otep-mvp-release.md) |
| 2026-05-08 | Made 5 MVP-vs-R1 scope decisions in one session: binary competencies, no "Save for later", no endorsement backend, FormSG/OTG routing, search in MVP | Said no to things that were reasonable requests. Each had a rationale logged. | [decisions-log.md](../../context/decisions-log.md) |
| 2026-05-11 | Populated scoping gaps tracker with 13 items — 10 open, 3 formally deferred to R1 with decision date and rationale | Scope discipline: every deferral is a conscious decision, not a "we'll get to it" | [scoping-gaps-tracker.md](../otep-mvp/scoping-gaps-tracker.md) |
| 2026-05-11 | Flagged target date discrepancy (Sep vs Dec) as an open decision needing Adrian's call — didn't silently pick one | Owned the ambiguity instead of ignoring it. Raised it as a decision to make, not a problem to report. | [prd.md Section 9](../otep-mvp/prd-opportunities.md) |

---

## 4. Cross-Cutting (PM Operating Behaviour)

*Evidence that doesn't fit neatly into one gap but shows PM-mode operating.*

| Date | What I Did | Why It's PM-Mode | Artifact |
|------|-----------|------------------|----------|
| 2026-05-06 | Built a PM operating system with context files, slash commands, and workflows that enforce PM habits | Designed my own working environment to reinforce the transition — BAs don't build operating systems | This repo |
| 2026-05-07 | Wrote 20 user stories across 5 groups with full AC, edge cases, and DoR checklists | Not just writing stories — organised them by user journey, mapped dependencies, created a pipeline | [user-stories.md](../otep-mvp/stories/index.md) |
| 2026-05-11 | Self-audited the OS, identified that it had more scaffolding than content, and fixed it | The meta-awareness to critique your own system and act on it — that's PM self-management | Conversation record |

---

## How to Update This File

At every sprint boundary (Step 2 of the Sprint Boundary workflow):

1. Ask yourself: "What did I do this sprint that a BA wouldn't have done?"
2. For each item: what's the artifact? Where does it live?
3. Add one row per competency area. Even one entry per sprint compounds.
4. If you can't find anything for a competency area — that's the signal for where to focus next sprint.

Don't manufacture evidence. The best entries come from decisions you made during normal OTEP delivery that happened to demonstrate PM thinking. If you're doing PM work, the evidence creates itself.
