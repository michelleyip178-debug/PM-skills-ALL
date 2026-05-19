# A Day in the Life of a Claude Code Native PM

A practical rhythm for Michelle to build PM habits using this OS. Not aspirational — designed to be doable even on chaotic days.

---

## Morning Block (9:00–10:00)

### 1. Update your schedule (2 min)
Check your calendar. Note today's meetings mentally or paste names into inbox.md.

### 2. Run `/daily` (1 min)
Read your briefing — schedule, ceremony, what's in motion, top 3, PM nudge. Identify your **#1 thing** — the one task that, if you only did this today, would still count as a good day.

### 3. Check: Am I building or reacting today? (2 min)
Look at your calendar:
- **Lots of meetings?** → Your job today is to steer conversations toward decisions. Bring a recommendation to each one.
- **Open blocks?** → Deep work day. Protect the time. Work on your #1 thing.

Write your #1 thing at the top of a sticky note or text file. Come back to it when you get pulled into Slack.

---

## Before Meetings

Run `/meeting-prep` with the attendee names. Go in with:
- One thing you want to **get out of** this meeting (a decision, an answer, an alignment)
- One recommendation you're prepared to make

**Context Claude pulls for you:**
- `06-skills-and-decisions/stakeholders/people/` — who you're meeting, what they care about, how to communicate with them
- `03-stories/otep-stories/` — latest research, decisions, blockers (auth + opportunities merged)
- `00-hub/tasks-active.md` — what you're working on that's relevant

---

## During Meetings

Don't just take notes. Listen for:
- **Decisions made** → drop into decision log after
- **Scope creep** → check MVP guardrails in CLAUDE.md — is this MVP or R1?
- **Action items that land on you** → write them down, don't rely on memory

### Specific meeting playbooks

| Meeting | Your PM job | Command to prep |
|---------|------------|-----------------|
| OTEP Standup (daily) | Unblock the team, steer toward sprint goals | `/daily` (gives you what's in motion + blockers) |
| Design review with Amber | Give clear product direction, validate against outcomes | `meeting-prep` skill |
| Sprint planning (Thu) | Prioritize, say no, bring user stories ready for grooming | `/groom-prep` to prep |
| PM weekly catchup | Share progress, ask for help on blockers | `weekly-update` skill |
| Steering with Mark/GK | Concise + detailed, hold scope line, get decisions | `meeting-prep` skill + MVP guardrails for any new asks |
| 1:1 with Adrian | Show outcomes-thinking, ask for PM coaching | Share a recent PM reflection |

### After the meeting (2 min)
Paste raw notes into inbox.md or directly into `04-ceremonies/archive-meetings/`. Don't format. Just dump. The point is capture, not perfection.

---

## Deep Work Blocks

### What Claude can do for you during deep work

| Task | How to use Claude | Command/Skill |
|------|-------------------|---------------|
| Write user stories from a feature idea | Describe the outcome, Claude generates stories with acceptance criteria | Pawel: `pm-execution` library |
| Research a design decision | Share screenshots/data, Claude maps comparisons and trade-offs | Paste + ask |
| Challenge a scope request | Describe what was asked, check against MVP guardrails in CLAUDE.md | Review `06-skills-and-decisions/decisions-log.md` + MVP guardrails |
| Synthesize interview/research notes | Dump raw notes, Claude extracts patterns and insights | `synthesize-research` skill |
| Draft a PRD section | Give context, Claude writes a section grounded in your project docs | `draft-prd-section` skill |
| Prepare a recommendation | Describe the options, Claude helps you structure the argument | Ask "help me recommend..." |

### The PM work that matters (and that BAs don't do)

| Activity | BA version | PM version |
|----------|-----------|------------|
| Writing user stories | "The system shall..." | "As an officer, so that [outcome]..." → Pawel `pm-execution` library |
| Responding to a feature request | Document it, pass it along | Check MVP guardrails in CLAUDE.md → recommend MVP or R1, reply with a trade-off |
| Preparing for sprint planning | Compile the ticket list | Come with priorities, trade-offs, and what to say no to |
| Sharing an update | "Here's what happened" | "Here's what it means and what's next" → `/weekly-update` |
| Receiving feedback from steering | Write it down, do what they said | Ask "what outcome does this serve?" then decide if it changes the plan |
| Scoping work | Accept all requirements | Check MVP guardrails, propose what's MVP vs R1, document in decision log |
| Tracking progress | Report status | Connect status to outcomes: "we shipped X, which unblocks Y metric" |

### When you catch yourself in BA mode
Stop and ask: **"Am I describing, or am I recommending?"**
- Describing = BA mode (what happened, what the options are, what people said)
- Recommending = PM mode (what we should do, why, and what we're trading off)

It's OK to describe first. But always end with a recommendation.

---

## Afternoon Check-in (5 min, after last meeting)

### Quick sweep:
1. Any decisions made today? → Log in [decisions-log.md](../decisions-log.md)
2. Any scope requests? → Did you apply the MVP/R1 filter?
3. Any blockers surfaced? → Add to Waiting On table in `00-hub/tasks-active.md`
4. Did you make progress on your #1 thing?
5. Any user stories need updating based on today's conversations?

---

## End of Day (5–10 min)

### 1. Update active.md (2 min)
One line per task. Even "no progress — blocked on X" is useful.

### 2. PM reflection (5 min)
Score your day. The point isn't to be harsh — it's to notice patterns:
- Where did you lead with outcomes?
- Where did you default to BA mode?
- What's one thing to try differently tomorrow?

### 3. Set tomorrow's intention (30 sec)
Write one sentence: "Tomorrow I will ___." Make it specific. Examples:
- "Tomorrow I will bring a recommendation to the design review, not just questions."
- "Tomorrow I will push back on Mark's idea using the scope-check framework."
- "Tomorrow I will ask Pow Hwee for technical constraints before writing the story."
- "Tomorrow I will draft the OTG lifecycle stories."

---

## Friday Additions

### Weekly update (15 min)
Run `/weekly-update`. Review the draft. Adjust tone per stakeholder preferences. Send to Jace/Adrian.

Claude uses:
- `00-hub/tasks-active.md` for progress
- `03-stories/otep-stories/` for details
- `resources/workflows/weekly-stakeholder-update/stakeholder-preferences.md` for tone
- `resources/workflows/weekly-stakeholder-update/draft-template.md` for format

### Sprint end sweep (if applicable)
- Move completed tasks → archive with impact notes
- Pull from `00-hub/tasks-backlog.md` → active for next sprint
- Update scoping gaps tracker
- Update decision log with sprint decisions

### Weekly reflection
Look at your PM reflection scores for the week:
- What's your average? Is it trending up?
- What pattern keeps showing up?
- What artifact did you produce this week that demonstrates PM thinking?

---

## Your Full Command Reference

| Command/Skill | Trigger | What Claude reads | What you get |
|---------|---------|-------------------|-------------|
| `/daily` | Morning | 00-hub/tasks-active.md, sprint-prep-rhythm.md, your pasted calendar | Schedule + PM moves, ceremony check, what's in motion, open items, top 3 focus, PM nudge |
| `meeting-prep` skill | Before meetings | 06-skills-and-decisions/stakeholders/people/, 03-stories/, 02-prd/, 04-ceremonies/archive-meetings/ | Context, talking points, recommendations to bring |
| `weekly-update` skill | Friday | 00-hub/tasks-active.md, 03-stories/, 02-prd/, stakeholder-preferences.md | Draft email for Jace/Adrian |
| `draft-prd-section` skill | Writing specs | 03-stories/, 02-prd/, GOALS.md | PRD section grounded in research |
| `synthesize-research` skill | After research | Your raw notes | Structured insights, patterns, gaps |
| `/endday` | End of day | 00-hub/tasks-active.md, your input | What got done, carry-forward, reflection |

---

## The Habits That Compound

| Week 1 | What you'll notice |
|--------|-------------------|
| Running `/daily` every morning | You stop feeling overwhelmed — priorities are clear |
| Logging decisions | You can answer "why did we do this?" without digging |
| Running PM reflections | You start catching BA-mode in the moment, not just in reflection |

| Month 1 | What changes |
|---------|-------------|
| Scope-checking requests | You stop saying "yes" to everything — you trade off |
| Recommending in meetings | People start asking "what do you think?" more |
| Having artifacts (stories, decision logs, research) | Your PM conversion case writes itself |

| Quarter 1 | What's different |
|-----------|-----------------|
| You operate as a PM | The title is a formality at that point |

---

## When You're Overwhelmed

If the full routine feels like too much, do only this:

1. `/daily` in the morning
2. Update `active.md` at end of day
3. Ask yourself one question: **"Did I recommend or just describe today?"**

That's it. Everything else is amplification.

---

## The One Rule

**Every interaction with Claude should leave you with an artifact or a decision — not just information.**

- Don't ask "what are the options?" → Ask "which option should I recommend and why?"
- Don't ask "what happened?" → Ask "what does this mean for my MVP timeline?"
- Don't ask "can you summarize?" → Ask "what should I do next based on this?"

Claude is not your note-taker. Claude is your thinking partner. Use it to make you bolder, not just more organized.

---

*This is a living doc. Update it as you find what works and what doesn't.*
