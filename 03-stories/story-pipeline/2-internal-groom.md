# Stage 2: Internal Groom

## When
Tuesday of sprint week 1. This is the squad groom — smaller group, less formal than backlog groom.

## Before the session (15 min)

Run `/groom-prep` with the stories you're bringing. It produces:
- Readiness score per story
- Risk areas Pow Hwee is likely to probe
- Open items that need an owner

Review the output. For each story:
- Can you explain the outcome in one sentence?
- Do you have a recommendation on any open design/scope questions?
- Are there MVP guardrail items to pre-empt?

## During the session

### For each story:
1. Read the story and AC aloud (30 seconds)
2. Ask: "What's unclear? What am I missing?"
3. Capture Pow Hwee's questions — he'll probe null states, API fields, error handling
4. Flag for Amber if design is needed
5. Flag for Pow Hwee if API contract is needed
6. Note open questions with owner and deadline

### Track outcomes per story:

| Story | Advances to Refine? | Design needed? | API contract needed? | Open questions |
|-------|---------------------|----------------|---------------------|----------------|

## After the session (5 min)

- Update the story files with new edge cases and AC refinements from the discussion
- Add open questions to `00-hub/open-items.md` with owner and deadline
- Log any scope decisions to `../../../PM-OS/outputs/decisions/2026-05-29-W22-decisions-log.md`
- Update the index: stories that advanced → DoR: In progress

## Done when
Every story discussed either moves to Refine stage or has a documented blocker.
