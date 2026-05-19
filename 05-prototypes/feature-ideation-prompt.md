# Feature Ideation Prompt — 6-Idea Generator

Use when you have a validated problem and need to explore the solution space before committing to a direction.

---

## Prompt (paste into any AI session)

```
You are a product strategist. Generate exactly 6 feature concepts for the problem below.

**Problem statement:**
[Paste your problem statement or epic hypothesis here]

**User:**
[Who is the primary user — e.g. "Public service officer browsing internal mobility opportunities"]

**Constraints:**
- MVP only — no AI matching, no complex workflows
- Must work with existing OTG data pipeline
- No new backend infrastructure unless essential
- [Add any other constraints]

**For each of the 6 ideas, give me:**
1. Feature name (5 words max)
2. One-sentence description of what it does
3. The user outcome it enables
4. Why it's worth building (the insight or behaviour it unlocks)
5. Biggest tradeoff or risk
6. MVP scope: what's the smallest shippable version?

**Spread the ideas across this spectrum:**
- 2x safe bets: obvious, low-risk, incremental
- 2x interesting plays: moderate effort, clear value, some novelty
- 2x bold moves: high potential, requires assumptions, could fail

After listing all 6, recommend one and say why.
```

---

## How to use the output

1. Review all 6 — note which ones prompt questions, not just agreement
2. Run the bold moves through the epic hypothesis template (`02-prd/epic-hypothesis-template.md`) to surface assumptions
3. Bring the recommended idea to your next `/decision` session with the constraint: "what would make me change my mind about this?"
4. If going to design, use `05-prototypes/ui-brief-prompt.md` to hand off to Amber or Claude Code
