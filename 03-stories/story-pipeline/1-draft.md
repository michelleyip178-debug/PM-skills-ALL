# Stage 1: Draft a User Story

## When
Anytime. Write stories as soon as you understand the problem. Don't wait for grooming.

## How

### 1. Pick the right group file
- Profile dependency: `user-stories-profile-dependency.md`
- Discovery & Filters: `user-stories-filters.md`
- OTG Lifecycle: `user-stories-otg-lifecycle.md`
- C@G Handoff: `user-stories-cag-handoff.md`
- Tracking: `user-stories-tracking.md`

### 2. Write the story

```markdown
### US-XX: [Short title]

**As an** [officer / host agency coordinator],
**I want to** [action — what they're trying to do],
**So that** [outcome — why it matters to them].

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]

**Edge cases:**
- [What happens when things go wrong?]

**Priority:** MVP / R1
```

### 3. Self-check before moving on

| Check | Pass? |
|-------|-------|
| Story is about a user outcome, not a system behaviour | |
| AC start with a verb and are testable | |
| At least one edge case is documented | |
| Priority is explicitly MVP or R1 | |
| Dependencies on other stories are noted | |
| No BA language ("the system shall") | |

### 4. Update the index
Add the story to `user-stories.md` (the index file) in the right group table.

## Tools
- Use the `pm-reviewer` agent to check story quality: it validates format, AC, MVP compliance, and sprint readiness.
- Use Dean's `epic-breakdown-advisor/SKILL.md` if you're breaking an epic into stories.

## Done when
Story exists in the group file with AC and edge cases. Index is updated.
