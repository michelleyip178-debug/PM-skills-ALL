# Stage 4: Backlog Groom

## When
Thursday of sprint week 2. Full team, 2 hours. Rama facilitates, Michelle leads content.

## Before the session (30 min)

Run `/groom-prep` with the stories for next sprint. Review the readiness scores.

Prepare:
- [ ] Stories prioritised — highest priority first
- [ ] Large stories broken down into sprint-sized items
- [ ] AC, designs, API contracts attached where available
- [ ] Dependencies identified
- [ ] A ready answer for "why this priority?" per item
- [ ] R1 deflection list — ready responses for out-of-scope topics

## During the session

### For each story:
1. Present: story, AC, design (if available), dependencies
2. Pow Hwee validates: edge cases, error states, API feasibility
3. Team estimates: story points or T-shirt size
4. Confirm: can this be delivered in one sprint?
5. Flag: anything still blocking DoR

### Track:

| Story | Estimated? | Blockers? | DoR status |
|-------|-----------|-----------|------------|

### When scope questions come up
Someone will ask "what about [feature X]?" for something out of MVP scope. Be ready:
- "That's R1 — we're logging it. For MVP, we're doing [simpler version]."
- Check `06-skills-and-decisions/decisions-log.md` — has this been decided already? Reference the decision.
- If it hasn't been decided, log it as a new open item. Don't decide in the room unless you're confident.

## After the session (10 min)

- Update story files with estimation results and any AC refinements
- Add new open questions to `00-hub/open-items.md`
- Log any scope decisions to `06-skills-and-decisions/decisions-log.md`
- Update the index: estimated stories → DoR: Ready (if all checklist items green)
- Stories not ready → note what's missing and who owns it

## Done when
All presented stories are either estimated with clear DoR status, or have a documented blocker with owner and deadline.
