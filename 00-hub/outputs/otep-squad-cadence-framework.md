# OTEP Squad Cadence Framework

> **For:** Pow Hwee
> **From:** Michelle
> **Date:** 19 May 2026
> **Purpose:** How often we should run our squad ceremonies across a 2-week sprint cycle

---

## TL;DR

We're on **2-week sprints**. Most ceremonies are **biweekly** (once per sprint), anchored to the same days each cycle. Daily standups are the only daily touchpoint.

**Total meeting time per sprint: ~7 hrs** (incl. standups). Non-standup ceremony time: ~4.5 hrs. Everything else is async.

---

## 🔁 Daily

| Ceremony | Time | Duration | Purpose |
|----------|------|----------|---------|
| Team Standup | 11am, every day | **15 min** | Blockers + priority changes only — no status reports |

---

## 📅 Week 1 of Each Sprint

| Day | Ceremony | Duration | Attendees | Purpose |
|-----|----------|----------|-----------|---------|
| **Monday** | Retro + Demo *(prev sprint)* | **45 min** | Full team | Demo: 15 min · Retro: 30 min. Strict timebox. |
| **Tuesday** | Story Refinement *(internal)* | **45 min** | Dev + PM | **Rough pass only.** Flag AC gaps, unknowns, dependencies. No full stories needed yet. |
| **Thursday** | Backlog Grooming *(DoR sign-off)* | **60 min** | Full team | **Formal DoR gate.** Stories that passed Tue refinement get final AC review + team sign-off. Hard stop at 60. |
| **Friday** | OTEP Squad Sync | **30 min** | Full team | Blockers only — async if nothing is red. |

---

## 📅 Week 2 of Each Sprint

| Day | Ceremony | Duration | Attendees | Purpose |
|-----|----------|----------|-----------|---------|
| **Monday** | Late-Sprint Check-in *(Day 8 of 10)* | **30 min** | Full team | At-risk items + scope changes only. No deep dives. Last realistic window to descope. |
| **Thursday** | Sprint Planning | **60 min** | Full team | Stories must be DoR-ready before entering this room. No DoR = story deferred, no exceptions. |
| **Friday** | Sprint End + Finalisation | *Async* | PM only | Archive + retro prep. No meeting needed. |

---

## 📆 Other Fixed Cadences

| Meeting | When | Duration | Cadence | Notes |
|---------|------|----------|---------|-------|
| BO Sync (Jacky / Xian Zhang) | Monday, 4pm | **30 min** | Weekly | 1 update · 1 blocker · 1 ask |
| Design Review (Amber) | Tuesday | **30 min** | Weekly | Bring ACs + specific decision needed |
| Steering (Mark / GK) | Biweekly | **30 min** | Every 2nd sprint | Progress, risks, one ask |

---

## 🔄 Retro Cadence

| Sprints | Retro? | Rationale |
|---------|--------|----------|
| S01 – S06 | ✅ Full retro **every sprint** | Team is still forming. Retro is the primary self-correction mechanism. Don't throttle it early. |
| S07 onwards | ✅ Every **2nd sprint** (S07, S09, S11) | Team is stable. Throttle only when the team is high-performing and asks to. |
| Off-retro sprints | 📝 PM async check-in instead | Written summary + one action item. Not a skip — a lighter-weight version. |

> **Why not S04?** Skipping retros at sprint 4 is too early. The team isn't high-performing yet and won't have had enough reps to self-correct without the structured forum.

---

## Sprint Calendar at a Glance

| Sprint | Phase | Dates |
|--------|-------|-------|
| S01 | MVP | 04 May – 15 May |
| S02 | MVP | 18 May – 29 May *(current)* |
| S03 | MVP | 01 Jun – 12 Jun |
| S04 | MVP | 15 Jun – 26 Jun |
| S05 | MVP | 29 Jun – 10 Jul |
| S06 | MVP | 13 Jul – 24 Jul |
| S07 | MVP | 27 Jul – 07 Aug |
| S08 | MVP — Feature Freeze | 11 Aug – 21 Aug |
| S09 | Compliance + Security | 24 Aug – 04 Sep |
| S10 | Compliance + Security | 07 Sep – 18 Sep |
| S11 | Compliance + Security | 21 Sep – 02 Oct |
| S12 | Compliance + Security — **GO-LIVE** | 05 Oct – 16 Oct |

---

## How Ceremonies Fit Together

```
WEEK 1                              WEEK 2
Mon     Tue     Wed     Thu     Fri     Mon     Tue     Wed     Thu     Fri
─────   ─────   ─────   ─────   ─────   ─────   ─────   ─────   ─────   ─────
Start   Squad   (prep)  Backlog Squad   Mid-            (prep)  Sprint  End +
+Retro  Groom           Groom   Sync    Sprint          day     Plan    Archive
                                        Review
```

**Facilitation:** Michelle facilitates ceremonies and owns pre-reads. Pow Hwee focuses on technical leadership in-session, not process management.

---

## ⏱️ Meeting Budget Per Sprint

| Ceremony | Duration | Frequency | Total | Cancellable? |
|----------|----------|-----------|-------|--------------|
| Daily Standup | 15 min | 10x | 150 min | ✅ End early if no blockers |
| Retro + Demo | 45 min | 1x | 45 min | ❌ Always runs |
| Story Refinement | 45 min | 1x | 45 min | ✅ Async if all stories are green |
| Backlog Grooming | 60 min | 1x | 60 min | ❌ Always runs |
| Squad Sync | 30 min | 1x | 30 min | ✅ Async if nothing is red |
| Late-Sprint Check-in | 30 min | 1x | 30 min | ✅ Async if nothing is at risk |
| Sprint Planning | 60 min | 1x | 60 min | ❌ Always runs |
| **Total** | | | **~7 hrs** | *(~4.5 hrs excl. standups)* |

> **Note on standups:** If there are no blockers, standup can end in 5–10 min. The 15-min slot is a ceiling, not a target.

### Ground Rules to Keep Meetings Lean

- **No story-writing in sessions.** ACs must be drafted before grooming — engineers don't wait for PM to think out loud.
- **Async-first for green items.** If nothing is at risk, Squad Sync and Late-Sprint Check-in can be cancelled. Replace with a 3-line Slack update.
- **Hard stops.** Every ceremony has a timebox. Overflow → park in Jira comment, not more meeting time.
- **Pre-reads required.** Grooming brief sent 24 hrs in advance by Michelle. If brief isn't ready, the meeting moves — not the engineer's problem.
- **DoR is a hard gate.** Stories that aren't DoR-ready do not enter sprint planning. No exceptions, no in-session triage.

---

*Generated from OTEP sprint-prep-rhythm.md + team.md · 2026-05-19*
