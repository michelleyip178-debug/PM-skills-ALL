# Michelle's PM OS — Integration Guide

Two repos. One job each.

- **PM-skills-ALL-1** (execution layer) — sprint ops, story writing, ceremonies, daily standups, Jira sync, PRD management. Lives in the *present tense*: what's In Progress, what's blocked, what's due today.
- **Laughing-pmyip** (strategy/discovery layer) — hypotheses, evidence, stakeholder intelligence, decisions with provenance, discovery synthesis. Lives in the *inquiry tense*: what do we believe, why, and how confident are we?

The risk without a clear handoff protocol: decisions get logged in both places, standup notes go into the wrong repo, and neither system stays clean enough to trust.

---

## The Dividing Line

| Moment | Which OS | Why |
|--------|----------|-----|
| Running standup / retro / grooming | PM-skills-ALL-1 | Ceremony output → sprint execution |
| A stakeholder says something surprising in a meeting | Laughing-pmyip `/ingest meeting` | Evidence capture with provenance |
| You make a scope decision | **Both** — log in decisions/ (Laughing-pmyip first, paste short entry into decisions-log.md) | Laughing-pmyip keeps the WHY + evidence trail; PM-skills-ALL-1 keeps the operational record |
| Writing user stories and ACs | PM-skills-ALL-1 | Story format, sprint readiness checks |
| Grooming a hypothesis for next sprint | Laughing-pmyip `/hypothesize` | Builds the belief + confidence before committing |
| Prepping for a steering/BO meeting | Laughing-pmyip `/prep` (stakeholder context) → PM-skills-ALL-1 `meeting-prep` (agenda + asks) | Strategy context first, then operational prep |
| Surfacing a risk | PM-skills-ALL-1 `00-hub/risks.md` | Active sprint risk tracking |
| Investigating WHY something is a risk | Laughing-pmyip `/risk` | Evidence, assumptions, confidence level |

---

## Where They Hand Off

**Laughing-pmyip → PM-skills-ALL-1** (strategy feeds execution):
- A hypothesis graduates to a decision → paste the short decision into `../PM-OS/outputs/decisions/2026-05-29-W22-decisions-log.md`
- Discovery synthesis identifies a user need → becomes a story brief in `03-stories/otep-stories/`
- Stakeholder intelligence surfaces a constraint → add to `00-hub/risks.md`

**PM-skills-ALL-1 → Laughing-pmyip** (execution surfaces learning):
- A standup blocker reveals an assumption worth testing → open a hypothesis file in Laughing-pmyip
- An AC debate in grooming surfaces a belief about user behaviour → `/hypothesize` it
- A decision gets made in ceremony → `/ingest meeting` + log in decisions/

---

## Daily Rhythm

**Morning (PM-skills-ALL-1 primary):**
- `/daily` → orient on sprint state, blockers, today's ceremonies
- Check `inbox.md` → triage captures from yesterday

**During ceremonies (PM-skills-ALL-1 primary):**
- Standup, grooming, planning all drive updates to sprint files

**After a stakeholder conversation (Laughing-pmyip primary):**
- `/ingest meeting` to capture what was said, tag observation vs. interpretation
- If a decision was made: log in decisions/, then paste the short version to PM-skills-ALL-1's decisions-log

**Weekly (Laughing-pmyip primary):**
- `/strategy-check` to assess whether current sprint work is still aligned with top hypotheses
- `/review` to mark hypotheses as validated/invalidated based on sprint learnings

---

## Avoiding Duplication

| Concept | Single source of truth | Notes |
|---------|----------------------|-------|
| Decisions | Laughing-pmyip `decisions/` (full WHY + evidence) | PM-skills-ALL-1 `../PM-OS/outputs/decisions/2026-05-29-W22-decisions-log.md` = short operational record only |
| Stakeholder profiles | Laughing-pmyip `stakeholders/` | PM-skills-ALL-1 `06-skills-and-decisions/stakeholders/people/` = meeting prep only |
| Risks | PM-skills-ALL-1 `00-hub/risks.md` | Move to Laughing-pmyip `/risk` only when you need to interrogate the assumption behind the risk |
| Sprint state | PM-skills-ALL-1 only | Laughing-pmyip doesn't track sprint status |
| Hypotheses | Laughing-pmyip only | PM-skills-ALL-1 doesn't have a hypothesis layer |

---

## You'll Know It's Working When

- Every decision in PM-skills-ALL-1 `../PM-OS/outputs/decisions/2026-05-29-W22-decisions-log.md` has a corresponding entry in Laughing-pmyip `decisions/` with evidence and confidence
- Hypotheses in Laughing-pmyip are getting marked validated/invalidated after sprints (not just accumulating)
- You open Laughing-pmyip at least once per stakeholder meeting, not just before sprints
