# /scan — Document Scan

Read these files before generating output:
- All story files in `projects/otep-mvp/stories/` (index.md, filters.md, otg-lifecycle.md, cag-handoff.md, profile-dependency.md, tracking.md, auth.md)
- `context/decisions-log.md` — all decisions
- `context/open-items.md` — all open items
- `projects/otep-mvp/scoping-gaps-tracker.md` — spec gaps
- `projects/otep-mvp/workflow-coverage-audit.md` — workflow gaps
- `projects/otep-mvp/sprint-checklists.md` — DoR blockers
- `projects/sprint-allocation.md` — sprint scope
- `.claude/CLAUDE.md` — MVP guardrails and application flow logic

Run a full document health check across these local files:

1. **Open decisions** — List every decision that appears unresolved or open.
   Cross-reference decisions-log.md (look for "TBD", "pending", superseded entries) against open-items.md.
   For each: what it's about, which story group it affects, and why it seems unresolved.

2. **Contradictions** — Identify any contradictions or inconsistencies between files.
   Check: story ACs vs MVP guardrails, sprint-allocation vs story-id-map sprint assignments, open-items status vs sprint-checklists DoR blockers, story risks vs risks.md.
   For each: cite both files and explain the conflict precisely.

3. **Undefined or ambiguous requirements** — Scan story ACs and edge cases for anything vague or undefined.
   Look for: "may", "could", "TBD", "to be confirmed", missing AC, concept-level features with no detail, unaddressed edge cases.
   Cross-reference scoping-gaps-tracker.md and workflow-coverage-audit.md for known gaps.

4. **What needs sign-off** — Identify decisions or assumptions requiring explicit stakeholder approval before development can proceed.
   For each: what needs approval, who the decision-maker is, and urgency (blocks next sprint / blocks later sprint / nice to resolve early).
   Sort by urgency.

Format as a document health report I can use to triage before planning.

Save as: `outputs/scan-YYYY-MM-DD.md`
