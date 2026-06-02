# Daily Standup Prompt

Use this when you're not in Claude Code and can't run `/daily`.

---

## Prompt (paste into any AI session)

```
You are my PM assistant. Run my daily standup using the context below.

**What I need:**
1. Today's calendar — any ceremonies or key meetings?
2. Recently completed — what got done since my last standup?
3. Open items — what's unresolved and needs a decision or owner?
4. Blockers — anything that's stopping sprint progress?
5. Top 3 focus for today — what should I prioritise?
6. PM growth nudge — one prompt to push me from BA mode to PM mode

**Context to use:**
[paste contents of 00-hub/sprint-status.md]
[paste contents of 00-hub/open-items.md]
[paste contents of 00-hub/tasks-active.md]
[paste contents of 00-hub/risks.md]

**My role:** BA transitioning to PM at PSD. Product is CareerCompass (formerly OTEP — internal talent marketplace for Singapore Public Service). Sprint is 2 weeks. Team: Jace (Lead PM), Pow Hwee (Tech Lead), Amber (Designer), engineers Léo, Thomas, Rathika; Fabian Peh on WOG AD onboarding.

**Push me toward PM mode.** If I'm describing requirements instead of outcomes, name it. Recommend, don't list options.
```

---

## Quick reference: Claude Code commands

| Situation | Command |
|---|---|
| Morning standup | `/daily` |
| End of day | `/endday` |
| Mid-day check | `/midday` |
| Before grooming | `/groom-prep` then `/groom` |
| Before sprint planning | `/sprint-plan-prep` |
| Mid-sprint health | `/mid-sprint-review` |
| Friday retro | `/retro` |
| Before stakeholder meeting | `meeting-prep` skill |
| Stakeholder brief | `/brief` |
| Decision support | `/decision` |
| Weekly email | `weekly-update` skill |
| Write a PRD section | `draft-prd-section` skill |
| Synthesize research | `synthesize-research` skill |
