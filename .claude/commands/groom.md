# /groom — Pre-Grooming Brief

Read these files before generating output:
- `context/current-sprint.md` — sprint goal and committed stories
- `projects/otep-mvp/sprint-checklists.md` — per-story grooming readiness and DoR blockers
- `projects/sprint-allocation.md` — which stories are in the target sprint
- `projects/otep-mvp/story-id-map.md` — ID reconciliation
- `context/open-items.md` — active blockers with owners
- `context/decisions-log.md` — recent scope decisions
- The story files for stories in the target sprint (check sprint-checklists.md for links)

Run these analyses in sequence and compile the results into a single grooming brief:

1. **Story readiness** — For each user story in the target sprint, assess readiness:
   - Has a clear user persona
   - Has a defined outcome (not just a feature)
   - Has acceptance criteria with testable verbs
   - Has no unresolved dependencies or open items blocking it
   - Design assets are finalised (check DoR blockers in sprint-checklists.md)
   Rate each story as: Ready / Needs work / Blocked. For Needs work or Blocked, say what's missing in one line.

2. **Gaps and ambiguities** — Scan ACs and edge cases for words like "may", "could", "TBD", or "to be confirmed". Cross-reference open-items.md. List each gap with source and a one-line explanation of why it's a risk.

3. **Dependencies** — Identify dependencies between stories (check the Depends on / Dependencies fields in story files). For each: Story A depends on Story B for [reason], and whether it's hard or soft.

4. **Edge cases** — For each story, flag potential edge cases not covered in acceptance criteria (empty states, permissions, failure states, null fields, mobile vs desktop). Cross-reference the Risks line on each story.

Format the output as a grooming brief I can bring into the session with Pow Hwee.

Save as: `outputs/grooming-brief-YYYY-MM-DD-groom.md`
