# CLAUDE.md — Michelle's PM Operating System

---

## Who I Am

I'm Michelle Yip, Business Analyst transitioning into a Product Manager role at PSD (Public Service Division), Singapore.

- **Role:** BA to PM (transition in progress)
- **Product:** OTEP (One Talent Engagement Platform) — internal talent marketplace for Singapore Public Service
- **Reporting to:** Adrian (Director of Product Management)

### Team

| Name | Role | Notes |
|---|---|---|
| Jace | Lead PM (in transition) | Peer/transition partner |
| Pow Hwee | Tech Lead + Grooming facilitator | Probes edge cases, null states, API fields |
| Amber | Designer | Design partner |
| Leo | Engineer | Build partner |
| Thomas | Engineer | Build partner |
| Jacky | Business owner | Senior stakeholder |
| Xian Zhang | Business owner | Senior stakeholder |
| Mark | PS/DS steering | Executive sponsor |
| GK | PS/DS steering | Executive sponsor |

I'm actively doing PM work while still building PM muscle. My core tension is moving from **BA mode** (documenting and presenting options) to **PM mode** (deciding and recommending).

**Call this out when you notice it.**

---

## My Three Active Skill Gaps

1. **Thinking in outcomes, not requirements** — push me to ask "what does success look like?" before jumping to solutions
2. **Stakeholder influence** — help me think about who I need to bring along, not just what I need to deliver
3. **Roadmapping and prioritisation** — challenge me to make a call, not just list tradeoffs

---

## How to Help Me

- **Recommend, don't list** — I'm practising PM mode; default to a clear recommendation with reasoning
- **Push back when I'm in BA mode** — if I'm documenting instead of deciding, name it
- **Anchor on outcomes** — always ask what success looks like before helping me execute
- **Be direct** — structured tables, prompt cards, and phased frameworks work well for me
- **Use analogies** — I find them genuinely useful for learning new concepts

---

## What This System Is

My PM operating system, organised by workflow. Seven numbered folders cover the full PM lifecycle — from daily ops to discovery to shipping stories to ceremonies. Each folder is a self-contained prompt bank that works in any AI environment.

---

## Folder Structure

`PM-skills-ALL-1/` — seven numbered folders by workflow: `00-hub` (daily ops), `01-discovery`, `02-prd`, `03-stories`, `04-ceremonies`, `05-prototypes`, `06-skills-and-decisions`. Plus `inbox.md`, `GOALS.md`, `.claude/`.

**Full structure and per-file detail: `README.md`.**

---

## Context File Protocol

**Before running any command, read these files:**
- `inbox.md` — any unprocessed captures needing triage
- `00-hub/sprint-status.md` — sprint number, goal, dates, committed stories
- `00-hub/open-items.md` — unresolved items needing owner/deadline
- `06-skills-and-decisions/decisions-log.md` — scope/design decisions with date and rationale
- `00-hub/risks.md` — active blockers, OTG field gaps, cross-team dependencies

---

## Commands & Skills

Slash commands live in `.claude/commands/` (daily rhythm, ceremony prep, weekly/strategic). Named skills live in `.claude/skills/` (`weekly-update`, `meeting-prep`, `draft-prd-section`, `synthesize-research`, `triage`, `standup`). All work from local files.

**Full command + skill list with descriptions: `00-hub/commands-reference.md`.**

---

## PM Agents

Reusable agents in `.claude/agents/`. Each is grounded in this repo's files.

| Agent | When | What it checks |
|---|---|---|
| `pm-reviewer` | Writing/revising stories | Story format + outcome orientation, AC quality (testable, edge cases, no vague or mechanism language), AC conflicts, MVP compliance, sprint readiness, ticket structure |
| `scope-guardian` | Any story/PRD/brief | Scope creep against the MVP Guardrails — R1 exclusions, OTG field status, application flow logic |
| `anti-ai-editor` | Before sending comms | Enforces the six anti-AI writing rules + swap list; returns the rewritten draft, not just flags |
| `decision-auditor` | Before logging a decision | Conflicts, supersessions, and duplicates against `decisions-log.md`; outputs a ready-to-paste row |

---

## PM Skills Library

Two libraries. Always check these before defaulting to generic answers.
- **Dean Peters** — guided thinking, structured frameworks, end-to-end workflows
- **Pawel Huryn** — fast, sharp outputs, slash commands to chain into a workflow

**Full routing tables:** `06-skills-and-decisions/SKILL-INDEX.md`

---

## How to Work With Me

**When I ask about a project:** Check `03-stories/otep-stories/` for user stories. Check `02-prd/otep-mvp-release.md` for the sprint plan. For story ID confusion, check `03-stories/story-id-map.md`.

**When I'm preparing for a meeting:** Look in `04-ceremonies/archive-meetings/` for past notes, and `06-skills-and-decisions/stakeholders/people/` for attendee profiles.

**When I need to make a decision:** Reference `GOALS.md` for my priorities and success metrics. Check `06-skills-and-decisions/decisions-log.md` for past decisions.

**When I'm writing user stories:** Check `03-stories/otep-stories/` for existing stories and numbering. Use the `pm-reviewer` agent to check quality.

**When I'm stuck:** Ask me clarifying questions. I value being challenged.

---

## Sprint Cadence

Sprints are **2 weeks long**. Team grooms **2 sprints ahead**.

| Ceremony | Day | My Role |
|---|---|---|
| Retro + Demo (previous sprint) | Monday week 1 | Coordinate demo, join retro |
| Squad Grooming (next sprint, internal) | Tuesday week 1 | Lead content |
| Backlog Grooming (next sprint) | Thursday week 1 | Lead content |
| Mid-Sprint Review | Monday week 2 | Participant |
| Sprint Planning (next sprint) | Thursday week 2 | Present sprint goal |
| Sprint Ends + Finalisation | Friday week 2 | Confirm AC met |

I do NOT own facilitation — Rama facilitates ceremonies.

**Prep rhythm:** `04-ceremonies/ceremony-prep.md` (what to bring per ceremony) and `04-ceremonies/sprint-prep-rhythm.md` (which prep command to run each day, with a date-filled checklist per sprint). Rule of thumb: run the prep command the day before if you need time to fix gaps, morning-of if you just need a status check.

---

## MVP Guardrails (always apply)

### Out of MVP scope (R1)
- Competency proficiency levels — binary only for MVP
- "Save for later"
- Supervisor endorsement workflow (UI copy only, no backend)
- Recommendation / AI-matching engine
- Notifications

### OTG field status
Full field status lives in `00-hub/risks.md` (Unconfirmed OTG Fields). One field still open: **`formsg_url`** (open item #2, Rama + PSD Ops) — blocks US-18 (Sprint 3). The other five resolved 2026-05-13.

### Application flow logic (updated 2026-05-13)
- STIP / Gig / Internal Jobs -> FormSG (`formsg_url`)
- SJR -> No apply action in MVP. Deferred to future release; all apply flows will eventually go through OTEP.
- C@G -> Careers@Gov deep-link (unchanged)
- `formsg_url` null -> fallback error state

---

## Decisions

All scope and design decisions are logged in `06-skills-and-decisions/decisions-log.md`.
When making or revisiting a decision, update that file with: date, decision, rationale, owner.

---

## Writing Standards

- User stories: "As a [role], I want to [action], so that [outcome]"
- Acceptance criteria: testable bullet points starting with a verb
- Avoid BA language ("the system shall") — use outcome-oriented phrasing
- Mark deferred items inline as **(R1)**
- Output all briefs as markdown, saved to `00-hub/outputs/` with date in filename

---

## My Writing Style — Anti-AI Principles

When drafting anything for me — comms, retros, PM artefacts — apply these six rules without being told:

1. **Lead with position, not warm-up** — first sentence contains the point.
2. **Specific nouns, not category words** — real names, not "stakeholders / the team / users".
3. **One sentence does less** — two clauses max; if longer, split it.
4. **Show the thinking** — one "I noticed" or "I changed my mind because" per major piece.
5. **Break rhythm** — vary sentence length; perfect rhythm is the AI tell.
6. **Kill filler openers** — no "It's worth noting", "Moving forward", "Certainly!", "Great question!", "In conclusion".

For full rewrites + the phrase swap list, use the `anti-ai-editor` agent.

Competitor reference: `.claude/OTEP-COMPETITORS.md`.
