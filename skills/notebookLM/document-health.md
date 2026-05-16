# Document Health Prompts

Prompts for auditing specs, finding gaps, and checking consistency across sources.

---

## Full health check

> Run a health check across all sources. Find: open decisions, contradictions between documents, vague requirements (TBD, may, could, to be confirmed), and anything needing stakeholder sign-off before dev can start. Sort by urgency.

---

## Finding gaps

> What's missing? Look for: stories without acceptance criteria, features mentioned but not specced, edge cases not covered (empty states, errors, permissions, mobile), and any 'TODO' or 'TBC' markers.

---

## PRD-to-story consistency check

> Compare the PRD against the user stories. Are there requirements in the PRD not covered by any story? Are there stories that don't trace back to a PRD requirement? List every mismatch.

---

## Spec review

> Review [document name] for quality. Check: is every requirement testable? Are edge cases covered? Are dependencies called out? Are success metrics defined? Give a verdict: Ready for dev / Needs work / Not ready.

---

## Contradictions finder

> Find contradictions or inconsistencies between any two or more documents. For each: cite both sources, quote the conflicting statements, and explain which one should take priority based on recency or authority.

---

## Terminology audit

> List every key term or concept used across sources (e.g. "opportunity", "listing", "application", "ringfencing"). For each: is it defined consistently? Are there documents that use a different word for the same thing? Flag any ambiguity that could confuse dev or design.

---

## Definition of Done check

> For each committed story, check whether it has: clear AC, design attached or referenced, technical approach noted, dependencies resolved, and test scenarios defined. Output a table: Story ID | AC | Design | Tech | Dependencies | Tests | Verdict.

---

## Change log since last review

> What's changed across all sources since [date]? List every addition, deletion, or modification. For each: what changed, in which document, and whether the change was discussed in a meeting note or made silently.
