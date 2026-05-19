# Hallway Test: Filter Categorisation

**Created:** 2026-05-06
**Owner:** Michelle
**Goal:** Validate whether C@G's Job function taxonomy resonates with officers, and understand what officers naturally filter by.
**Timeline:** Run before sprint planning (Thu May 8)

---

## Setup

- **Time needed:** 10 min per officer, 3 officers minimum
- **Materials:** OTG and C@G filter screenshots (already captured)
- **Participants:** Pilot/UAT officers (mix if possible: different agencies, seniority)
- **No prep needed from participants** — keep it casual and low-pressure

---

## Script

### Intro (1 min)

> "I'm working on the new Opportunities page in OTEP. I want to understand how you'd search for opportunities. There are no wrong answers — I'm testing the design, not you."

### Q1 — Open (2 min)

> "When you're looking for a new opportunity (STIP, GIG, or job), what's the first thing you'd want to filter by?"

_Don't show anything yet. Just listen to their natural language._

**Capture:** What words do they use? What dimension do they think of first?

### Q2 — Show C@G filter panel (3 min)

> "Here's one possible set of filters. If you were looking for [give a specific scenario, e.g. 'a 3-month policy role at another agency'], which filters would you use? Walk me through it."

_Watch: What do they click first? Do they hesitate? Do they understand "Job function"?_

**Capture:** Which filters they use, which they skip, any confusion on labels.

### Q3 — Show OTG filter panel (3 min)

> "Here's another version. Same task — how would you find that role here?"

_Watch: Do they prefer competency search? Do they use Function or Job Family?_

**Capture:** Which filters they use, how it compares to their C@G behaviour.

### Q4 — Comparison (1 min)

> "Which felt easier? Why?"

**Capture:** Stated preference and reasoning.

---

## Scenarios to Use

Pick 1–2 per session. Vary across officers.

1. "Find a 3-month policy role at another agency"
2. "Find a GIG in engineering that's less than 4 hours/day"
3. "Find a full-time role in healthcare"
4. "Find any opportunity at MHA starting next month"
5. "Find something related to data analytics"

---

## What to Listen For

| Signal | What it means | Implication |
|--------|--------------|-------------|
| They say "agency" first in Q1 | Organisation filter is the hero — taxonomy matters less | Prioritize Organisation as primary filter |
| They struggle with C@G's 34 items | List is too long or labels don't match their mental model | May need to simplify or group the list |
| They prefer OTG's competency search | Officers think in skills, not categories | Consider competency search as a future unified filter (R1) |
| They ignore Function/Job function entirely | This filter may not matter as much as we think | Deprioritize the taxonomy debate — it's not blocking officers |
| They use different words than either list | Both taxonomies may be wrong | Officers have their own language — capture it for future redesign |
| They get confused by the number of options | Cognitive overload | Consider progressive disclosure or fewer top-level options |

---

## Capture Template (per officer)

```
### Officer: [name/role/agency]
**Date:**

**Q1 — What they'd filter by first:**


**Q2 — C@G panel reaction:**
- Filters used:
- Filters skipped:
- Confusion/hesitation:

**Q3 — OTG panel reaction:**
- Filters used:
- Filters skipped:
- Confusion/hesitation:

**Q4 — Preference:**


**Key quote:**


**Surprise/insight:**

```

---

## After the Test

1. Look for patterns across 3+ officers
2. Update [categorisation-research.md](categorisation-research.md) with findings
3. Adjust recommendation if needed
4. Bring findings to sprint planning (even if preliminary: "I spoke to 3 officers and...")

---

## How This Feeds Your Decision

| If you find... | Then recommend... |
|----------------|------------------|
| Officers default to Agency/Organisation | Hybrid model works — Organisation is the hero filter, taxonomy is secondary |
| Officers understand C@G's Job function list | Adopt C@G's taxonomy (Adrian's Option 1) |
| Officers are confused by both | Neither taxonomy works — propose a simplified list for R1 |
| Officers prefer competency/skill search | Flag for R1: competency matching may be the real unified filter |
