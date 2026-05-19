# Story Pipeline — Workflow Spec

## Purpose

Get user stories from "idea in my head" to "ready for sprint planning" with quality gates that prevent Pow Hwee from finding gaps at grooming. This is the core PM delivery workflow for Sprints 2–5.

## When

Ongoing. Stories need to be **2 sprints ahead** of build. If Sprint 3 starts Jun 2, those stories need to be DoR-ready by Sprint 2 week 2 (late May).

| Lead time | Stories should be at... |
|-----------|------------------------|
| 2 weeks before build | Draft (AC written, priority clear) |
| 1 week before build | Refined (designs in progress, requirements clear) |
| Sprint planning day | DoR met (designs done, API contract, subtasks, test cases) |

## Pipeline Stages

```
1. DRAFT            Michelle writes story + AC
     |
2. INTERNAL GROOM   Squad reviews (Tue week 1)
     |
3. REFINE           Amber designs, Pow Hwee reviews API
     |
4. BACKLOG GROOM    Full team reviews (Thu week 2)
     |
5. DOR MET          All checklist items green
     |
6. SPRINT PLANNING  Story committed to sprint
     |
7. JIRA             Ticket created in Jira with Confluence link
```

---

## Stage 1: Draft

See `1-draft.md`

Michelle writes the story in the appropriate group file (`user-stories-*.md`):
- [ ] Story in "As a / I want / So that" format
- [ ] Acceptance criteria (testable, verb-first)
- [ ] Edge cases identified
- [ ] Priority: MVP or R1
- [ ] Dependencies noted

**Quality gate:** Can you explain what "done" looks like for this story in one sentence?

## Stage 2: Internal Groom (Tuesday week 1)

See `2-internal-groom.md`

Run `/groom-prep` before the session. In the session:
- [ ] Walk through each story with the squad
- [ ] Capture Pow Hwee's technical questions and edge cases
- [ ] Identify what needs design (flag for Amber)
- [ ] Identify what needs API contract (flag for Pow Hwee)
- [ ] Note any open questions that block estimation

**Quality gate:** Every story either advances to Refine or gets a clear blocker logged.

## Stage 3: Refine

See `3-refine.md`

Between internal groom and backlog groom:
- [ ] Amber designs UX for flagged stories, links assets to AC
- [ ] Pow Hwee documents API contract for flagged stories
- [ ] Michelle updates AC based on groom feedback
- [ ] Michelle resolves open questions (chase owners in `open-items.md`)
- [ ] Feature flag + entry point identified

**Quality gate:** Design and API contract both attached. No open questions blocking estimation.

## Stage 4: Backlog Groom (Thursday week 2)

See `4-backlog-groom.md`

Run `/groom-prep` before the session. Full team reviews:
- [ ] Validate AC completeness — Pow Hwee probes edge cases
- [ ] Estimate (story points or T-shirt)
- [ ] Confirm priority order
- [ ] Flag any remaining blockers

**Quality gate:** Stories are estimated and have no unresolved blockers.

## Stage 5: DoR Met

The DoR checklist (from Pow Hwee):
- [ ] Prioritised and deliverable in a sprint
- [ ] All platform subtasks (including test cases) identified and created
- [ ] UI assets and UX flows designed and linked to all AC (Amber)
- [ ] Feature flag designed with entry point identified
- [ ] API contract identified and documented (Pow Hwee)

PM additions:
- [ ] AC are clear and testable
- [ ] Dependencies identified and unblocked
- [ ] Edge cases and error states documented

**Quality gate:** Every checkbox green. If any are red, the story doesn't go to sprint planning.

## Stage 6: Sprint Planning (Thursday week 2)

Story is committed to the sprint with owner assigned.

## Stage 7: Jira

Create ticket in Jira. Link Confluence one-pager. Story is now the engineering team's to build.

---

## Tracking

In `03-stories/otep-stories/` (the story index), the DoR column tracks pipeline stage:
- Pending = Draft or earlier
- In progress = Stages 2–4
- Ready = DoR met

## Failure Modes

| Failure | Prevention |
|---------|-----------|
| Showing up to groom with vague AC | Run `/groom-prep` the day before — it scores readiness |
| Designs not ready for sprint planning | Flag design-needed stories at internal groom (2 weeks before planning) |
| Pow Hwee finds edge cases at planning | Internal groom exists specifically to catch these early |
| Stories pile up in Draft | The 2-sprint-ahead rule creates natural pressure — if Sprint 3 stories aren't moving, escalate |
| Scope creep into stories | Check each AC against MVP guardrails in CLAUDE.md |
