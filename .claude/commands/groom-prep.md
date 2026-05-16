# Backlog Grooming Prep

Prepare Michelle for the upcoming squad grooming session.
Rama facilitates — Michelle leads content.

Read CLAUDE.md, context/current-sprint.md, and the backlog file passed
as argument before generating output.

---

## Steps

### Step 1 — Parse backlog file
Extract all user stories. For each, identify:
- Story ID and title
- Acceptance criteria (present or missing)
- Design status (if noted)
- Dependencies and open items

### Step 2 — Score grooming readiness
| Story ID | Title | Story Format | AC Written | Design Status | Dependencies | Open Items | Ready? |
|---|---|---|---|---|---|---|---|

Scoring: ✅ confirmed | ⚠️ incomplete | ❌ missing

### Step 3 — Flag risk areas
Stories Pow Hwee is likely to probe. Cross-check unconfirmed OTG fields
from CLAUDE.md. Format as:
> ⚠️ **[Story ID]** — [Risk] → [Suggested action]

### Step 4 — Recommend grooming order
Prioritise:
1. Sprint-ready stories (all ✅)
2. Stories with external dependencies needing early resolution
3. Stories tied to the sprint goal

### Step 5 — Generate briefing

---
## Grooming Briefing — [Date]

### Sprint Goal
[From context/current-sprint.md or flag if unclear]

### Grooming Order (recommended)
[Ordered list with readiness status]

### Open Items — Assign an Owner in the Session
| Open Item | Suggested Owner | Needed By |
|---|---|---|

### R1 Deflection List
Ready responses for out-of-scope topics that will come up:
- [topic] → "Logging as R1 — great idea for post-MVP"

### Pow Hwee Will Probably Ask...
Pre-empted tech questions so Michelle isn't caught off guard:
- [question / edge case]

---

Save as: `outputs/grooming-brief-YYYY-MM-DD.md`
