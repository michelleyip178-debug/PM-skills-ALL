# OTEP PM OS — Changelog

> The history layer behind `inbox.md`: what came in, what got routed where, what got deleted, plus notable structural changes to the OS. When a triage pass clears items, log it here so nothing is lost.
>
> **How to use:** after each inbox triage (morning routine), append to — or extend — today's dated entry: what was captured, what was routed to which file, what was deleted, what's still pending. One entry per date. Newest first. Don't prune.

---

## 2026-05-15

**Triage (inbox):**
- **OTEP-202 / OTEP-271 (local POCDEX DB + seed)** → `context/open-items.md` #27 — confirm whether OTEP-271 lands in Sprint 2 carry-over vs backlog (Leo / Pow Hwee split; parent OTEP-99).
- **Sharpen Sprint 2 ACs (Pow Hwee)** → `tasks/active.md` "Up Next".
- **Share OTG Excel reports** → removed from inbox only; action remains in `tasks/active.md` (wording updated: complete Fri 15 May if not done before Thu 14 groom).
- **Ceremony Prep** in `inbox.md` → updated for Fri 15 May: Thu 14 groom/plan past tense; Sprint 1 finalisation today → `/archive` + `/retro-prep` after sign-off.

## 2026-05-14

**OS changes (for the record):**
- Archived 8 stale Sprint 1 outputs to `archive/outputs/`: `daily-2026-05-11/12/13.md`, `endday-2026-05-11/13.md`, `mid-sprint-review-2026-05-11.md`, `discovery-plan-2026-05-13.md`, `grooming-brief-2026-05-13.md` (superseded by today's v4 post-reshuffle grooming brief). `outputs/` now holds only today's 6 Sprint 2 prep files; tomorrow's `/archive` run picks those up after Sprint 1 finalisation sign-off.
- Folder-wide scan also flagged `projects/sprint-calendar.md` (MVP release calendar, 12 sprints) and `context/sprint-calendar.md` (ceremony cadence) as a filename collision — different content, left as-is.

## 2026-05-12 — *inbox last cleared today*

**Triage:**
- **Restructured `inbox.md`:** `## Raw Capture` (`### From …` channel headers for new items) → `## Triaged — pending routing` (D/A/I staging area) → `## Parking Lot`. The changelog moved out to this file.
- **Routed the D/A/I batch** (12-May team standup · PM Weekly 11-May notes · Product × BO Senior Level notes):
  - auth-flow sign-off · R4-priority · programme plan adopted (12 sprints / Feature Freeze end of Sprint 8 / Go-Live 16 Oct) → `context/decisions-log.md`
  - "is a competency page in MVP scope?" → `context/open-items.md` #19
  - OKRs→NotebookLM · loop Diana into opportunities decisions · clarify OTG test-cases request → `tasks/active.md` Up Next; Tue/Fri → "squad sync" rename (pending Jace) → `tasks/active.md` Waiting On
  - stakeholder-direction volatility · engineer scope-spread → `context/risks.md` (new Team & Delivery Risks section)
  - job-posting-as-end-to-end-journey · Adrian+Barry ATS discussion → `inbox.md` Parking Lot; Pow Hwee/Kingsley competency modeling → already `open-items.md` #18; Adrian/Imelda's own actions · Monday pre-grooming walkthroughs · JIRA-early planning → deleted (FYI / already in the OS)
- **Still pending in inbox:** the apply-flow scope decision — Michelle's to call (all opportunities → FormSG except C@G, or just Internal Jobs + the STIP/Gig already on FormSG?).

**OS changes (for the record):**
- Sprint plan reconciled to **OTEP-Pathfinder Sprint Ceremonies v2** — 12 sprints, 4 May – 16 Oct 2026; Feature Freeze end of Sprint 8 (21 Aug); Go-Live end of Sprint 12 (16 Oct); compliance phase = Sprints 9–12. Sprint 1 keeps its combined Backlog-Grooming + Sprint-Planning Thursday; Sprints 2+ split them (Backlog Grooming Thu W1, Sprint Planning Thu W2). Propagated across `sprint-calendar.md`, `CLAUDE.md`, `sprint-allocation.md`, `sprint-prep-rhythm.md`, `ceremony-prep.md`, `README.md`, `GOALS.md`, `otep-mvp-release.md`. Open item #13 (Sep vs Dec launch) closed → Go-Live 16 Oct.
- Google Calendar connected; `/daily`, `/midday`, `meeting-prep` now pull from it. Fixed two stale calendar event descriptions (Thu 14 May planning, Mon 18 May retro). Created 9 calendar markers: Feature Freeze (21 Aug), Go-Live (16 Oct), Steering ×4 (22 May, 19 Jun, 17 Jul, 14 Aug), Sprint 2's Squad Groom (19 May) / Mid-Sprint (25 May) / Sprint Ends (29 May).
- `/daily` + `/endday` commands redesigned: yesterday's-carries loop (with age + escalation flag), outcome pulse, single status-&-moves table, "not today" deferral, concrete PM rep.
- README updated: channel-capture examples per source; morning-routine step to log triage here.

## 2026-05-11

**Triage:**
- **Captured into inbox:** 12-May team standup (Slack) · PM Weekly Catch Up notes · Product × BO Senior Level notes.
- **Routed (earlier triage):** OTEP-190 (auth) + OTEP-170 (navbar / design system) → `areas/stakeholders/people/leo.md` / `context/current-sprint.md`; OTG user access & account review → `projects/otg-ops/task-log.md` #1; Mid-Sprint Review prep → done.

**OS changes (for the record):**
- Sprint 2 scope decided: 5 stories, OTG data only (OTEP-85/86/128/129/US-05) — logged in `decisions-log.md`; reconciled across `sprint-allocation.md`, `sprint-checklists.md`, `story-readiness.md`, `sprint-calendar.md`.
- `outputs/` cleanup: archived two superseded Sprint 2 drafts; fixed wrong dates (Sprint 1 ends Fri 15 May, not 16) across daily / grooming / sprint-plan briefs and `current-sprint.md`.
