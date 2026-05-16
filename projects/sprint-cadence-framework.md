# OTEP Sprint Cadence Framework

**Squad:** PM · Tech Lead (coding) · Designer · Engineers  
**Facilitation:** Shared — no dedicated Scrum Master  
**Version:** v2.1 (updated 2026-05-14 to match actual cadence from Sprint 2 onward)

---

## What Changed

### v1 → v2 (original design)

| Old | New |
|-----|-----|
| Refinement Mon W2 | Refinement Thu W1 — 4 days before Planning |
| Engineers commit in front of BOs | Engineers commit with PM + TL only |
| No mid-sprint check-in | Mid-Sprint Check-in added |
| BOs in Sprint Planning | BOs in separate BO alignment touchpoint |
| Blocker ownership implicit | Explicit 24-hr SLA: PM owns business, TL owns technical |
| No escalation owner for BO deadlock | Adrian named as escalation owner |
| No Pow Hwee backup defined | Backup protocol defined for all TL roles |
| Retro every 2nd sprint from S1 | Every sprint for S1–S3, then every 2nd sprint |

### v2 → v2.1 (design vs actual — reconciled to sprint-calendar.md)

| v2 design | Actual (from Sprint 2) | Why |
|-----------|----------------------|-----|
| Mid-Sprint Check-in Wed W1 | Mid-Sprint Review Mon W2 | W2 Mon gives a full week of sprint data to review |
| Sprint Planning Mon W2 | Sprint Planning Thu W2 | Thu gives devs 1–1.5 days to break down and size after grooming |
| Sprint Review + Retro Fri W2 | Retro & Demo Mon W1 of next sprint | Combined with sprint start; Fri W2 is finalisation only |
| 1 grooming session (Thu W1) | 2 sessions: Squad Grooming Tue W1 (internal) + Backlog Grooming Thu W1 | Internal groom surfaces gaps before the formal grooming |
| BO Sign-off as separate ceremony | BO alignment via Mon pre-grooming sessions | Per BO working agreement (2026-05-11) — BOs join decision points, not routine ceremonies |
| Squad Sync 3x per sprint | Tue/Fri refocused to dependency syncs (not separately tracked) | Lightweight — not a formal ceremony |

---

## Sprint Calendar (2-week cycle, Sprints 2+)

> Source of truth for dates: [context/sprint-calendar.md](../context/sprint-calendar.md). This section describes the pattern; the calendar has the actual dates.

### Week 1

| Day | Ceremony | Duration | Who |
|-----|----------|----------|-----|
| Mon | Sprint Start + Retro & Demo (previous sprint) | 30 min start + 1 hr retro/demo | Squad + BOs (for demo) |
| Tue | [Internal] Squad Grooming (next sprint) | 1 hr | PM + TL + Engineers + Designer |
| Thu | Backlog Grooming (next sprint) | 1 hr | PM + TL + Engineers + Designer (optional) |
| Fri | Weekly retro (personal PM reflection) | — | PM only |
| Fri | Bi-weekly Steering (every 2 sprints) | 30 min | Pow Hwee + Mark & GK |

### Week 2

| Day | Ceremony | Duration | Who |
|-----|----------|----------|-----|
| Mon | Mid-Sprint Review | 30 min | PM + TL (+ squad if needed) |
| Thu | Sprint Planning (next sprint) | 1 hr | PM + TL + Engineers (no BOs) |
| Fri | Sprint Ends + Finalisation | 30 min | PM + TL |

### Daily

| Ceremony | Duration | Who |
|----------|----------|-----|
| Daily Standup | 15 min | Full squad (no BOs) |

---

## Ceremony Details

### 🚀 Sprint Start + Retro & Demo
- **When:** Mon W1 (combined session — sprint start, then previous sprint's demo and retro)
- **Duration:** 30 min start + up to 1 hr retro/demo
- **Facilitator:** PM (opens sprint + coordinates demo) + Engineers (demo their own work)
- **Objective:** Formally open the sprint. Then demo previous sprint's completed work and run retro.
- **Attendees:** PM (required) · Tech Lead (required) · Engineers (required) · Designer (optional) · BO (required for demo, excluded from retro)
- **Outputs:** Sprint goal confirmed · Story ownership assigned · Demo feedback captured · Retro actions committed
- **Rules:**
  - Sprint Start is hard 30-min — alignment only, not replanning
  - Scope changes after Sprint Start require PM decision and a story swap
  - Only done stories are demoed — nothing partial
  - Retro: at least one improvement action with owner and due date

---

### 🌡️ Mid-Sprint Review
- **When:** Mon W2
- **Duration:** 30 min
- **Facilitator:** PM
- **Objective:** Temperature check on sprint health with a full week of data. Surface at-risk stories before they become blockers.
- **Attendees:** PM (required) · Tech Lead (required) · Engineers (optional) · BO (excluded)
- **Outputs:** At-risk stories identified · Blockers logged with 24-hr SLA triggered · Sprint goal status (on track / at risk / off track)
- **Rules:**
  - Hard 30-min limit
  - Unresolved blockers at 24hr escalate per SLA rules
  - Run `/mid-sprint-review` + `/archive` (mid checkpoint)

---

### 🔍 Squad Grooming (internal) + Backlog Grooming

Two grooming sessions per sprint. The internal session surfaces gaps; the formal session refines for commitment.

**[Internal] Squad Grooming**
- **When:** Tue W1
- **Duration:** 1 hr
- **Facilitator:** PM (primary) + Tech Lead (technical questions)
- **Objective:** Internal dry run. Walk through candidate stories, surface AC gaps, missing designs, and edge cases before the formal grooming.
- **Attendees:** PM (required) · Tech Lead (required) · Engineers (required) · Designer (required)
- **Outputs:** Story gaps identified · AC rewrites queued · Design follow-ups flagged
- **Rules:**
  - Internal only — no BOs
  - Run `/groom-prep` before, `/groom` morning of

**Backlog Grooming**
- **When:** Thu W1
- **Duration:** 1 hr
- **Facilitator:** PM (primary) + Tech Lead (technical questions)
- **Objective:** Candidate stories clarified, estimated, and broken into tasks. Engineers leave ready to commit at Thu W2 Sprint Planning.
- **Attendees:** PM (required) · Tech Lead (required) · Engineers (required) · Designer (optional) · BO (optional — only if story blocked on business rule)
- **Outputs:** Refined, estimated stories with tasks · ACs agreed per story · Open questions logged with owner · Unready stories returned to backlog
- **Rules:**
  - Stories without clear ACs are not estimated — returned to PM
  - Hard 1-hr limit — incomplete items deferred
  - Open questions must have a resolution owner before leaving the session
  - Run `/groom-prep` (Wed) then `/groom` morning of

---

### 🎯 Sprint Planning
- **When:** Thu W2
- **Duration:** 1 hr
- **Facilitator:** Tech Lead (commitment) + PM (goal)
- **Objective:** Engineers formally commit to the sprint with PM and Tech Lead. No BOs — commitment made free from stakeholder pressure. Thu placement gives devs 1–1.5 days after grooming to break down and size.
- **Attendees:** PM (required) · Tech Lead (required) · Engineers (required) · Designer (optional) · BO (excluded)
- **Outputs:** Sprint commitment declared by engineers · Stories and tasks confirmed
- **Rules:**
  - BOs do not attend — commitment integrity requires no stakeholder pressure
  - Hard 1-hr limit
  - Engineers commit to what they can confidently deliver — PM does not push for more
  - Run `/sprint-plan-prep` (Wed) then refresh morning of

---

### ✅ BO Alignment
- **When:** Mon W1 pre-grooming sessions (primary touchpoint) + Sprint Demo (Mon W1)
- **Duration:** Varies
- **Facilitator:** PM
- **Objective:** BOs stay aligned at decision points without attending routine grooming, sizing, or engineering discussions. Per BO working agreement (2026-05-11).
- **Attendees:** PM (required) · Tech Lead (optional) · BO (required)
- **Outputs:** Sprint goal awareness · Priority confirmed · Scope changes logged for PM + TL assessment
- **Rules:**
  - BOs join for problem framing, scope/priority decisions, and sprint goals
  - BOs stay out of routine grooming/sizing and engineering discussions unless a business decision is needed
  - If BOs cannot align on priority: PM logs conflict and escalates to Adrian within 24hr

---

### ⚡ Daily Standup
- **When:** Daily Mon–Fri
- **Duration:** 15 min
- **Facilitator:** Rotating — any team member
- **Objective:** Synchronise daily. Surface blockers early. Peer coordination — not a status report.
- **Attendees:** Engineers (required) · Tech Lead (required) · PM (required) · Designer (optional) · BO (excluded — never)
- **Outputs:** Sprint board current · Blockers logged — 24-hr SLA triggered
- **Rules:**
  - Hard 15-min limit — no problem-solving in standup
  - Blockers get offline follow-up within 2hr
  - Engineers update sprint board before standup — not during it

---

### 🏁 Sprint Ends + Finalisation
- **When:** Fri W2
- **Duration:** 30 min
- **Facilitator:** PM + Tech Lead
- **Objective:** Formally close the sprint. Confirm ACs met. Tidy board, log carry-overs, update decision tracker.
- **Attendees:** PM (required) · Tech Lead (required) · Engineers (excluded) · BO (excluded)
- **Outputs:** Sprint board closed · Carry-overs logged with rationale · Sprint summary posted to Confluence · Decision tracker updated
- **Rules:**
  - Engineers not required — admin is PM + Tech Lead
  - Sprint summary posted same day — not carried over to Monday
  - Run `/archive` (end checkpoint) then `/retro-prep` for Monday

---

## Attendance Matrix

| Role | Sprint Start + Retro & Demo (Mon W1) | Squad Groom (Tue W1) | Backlog Groom (Thu W1) | Mid-Sprint (Mon W2) | Sprint Planning (Thu W2) | Sprint End (Fri W2) | Standup |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Product Manager | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Tech Lead | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Engineers | ✓ | ✓ | ✓ | ○ | ✓ | ✕ | ✓ |
| Designer | ○ | ✓ | ○ | ✕ | ○ | ✕ | ○ |
| Business Owner | ✓ (demo only) | ✕ | ○ | ✕ | ✕ | ✕ | ✕ |

✓ Required · ○ Optional · ✕ Excluded

---

## Roles and Responsibilities

### Product Manager (Michelle)
- Sets the sprint goal — originates from PM, not the team
- Owns and prioritises the product backlog
- Facilitates Squad Grooming (Tue W1), Backlog Grooming (Thu W1), and coordinates Demo (Mon W1)
- Receives engineer commitment in Sprint Planning (Thu W2) — aligns BOs via pre-grooming sessions and Demo
- Owns business blocker resolution — 24-hr SLA from point of identification
- Posts sprint summary and decision log to Confluence on Sprint End day (Fri W2)

### Tech Lead (Pow Hwee)
- Codes alongside engineers — carries sprint stories like the rest of the team
- Co-facilitates both grooming sessions; leads Sprint Planning commitment (Thu W2)
- Attends Mid-Sprint Review (Mon W2) — owns technical blocker resolution (24-hr SLA)
- Final call on technical approach and architecture
- Flags velocity risks and cross-squad dependencies to PM early
- Sends async sprint update to Barry after each Sprint Planning
- Named backup protocol defined — PM covers ceremonies if Pow Hwee is unavailable

### Engineers
- Attend Refinement — clarify, estimate, break into tasks
- Declare sprint commitment in Sprint Planning with PM + TL only — no BO pressure
- Update sprint board daily before standup
- Raise blockers in standup immediately — triggers 24-hr SLA
- Do not attend: BO Sign-off, Squad Sync, Mid-Sprint Check-in, Sprint End
- Rotate Retrospective facilitation (every 2nd sprint)
- Demo their own completed work in Sprint Review

### Designer (Amber)
- Delivers design assets minimum 1 sprint ahead of dev
- Attends Refinement when UX stories are in scope
- Available during sprint for dev clarification questions
- Participates in Sprint Review — presents UX outcomes
- Attends Squad Sync if shared design system decisions need cross-squad alignment
- Flags design dependencies that could block engineers early

### Business Owner (Jacky / Xian)
- Joins Mon pre-grooming sessions for problem framing, scope/priority decisions, and sprint goals
- Attends Demo (Mon W1 of next sprint) — required, not optional
- Receives sprint commitment as a done deal — not a negotiation
- Scope change requests go to PM + Tech Lead for capacity assessment before actioning
- Responds to business decisions within 48 business hours when escalated by PM
- Does not attend: Squad Grooming, Backlog Grooming, Sprint Planning, Standup, Retro, Mid-Sprint Review, Sprint End

---

## Operating Rules

### Blocker Ownership

| Rule | Owner | SLA |
|------|-------|-----|
| Business blockers | PM (Michelle) | 24hr to resolve from identification |
| Technical blockers | Tech Lead (Pow Hwee) | 24hr to resolve from identification |
| Cross-squad blockers | PM (Michelle) | Raised at Fri Squad Sync — escalate to Adrian if unresolved in 48hr |
| Unresolved at 48hr | PM | Escalate to Adrian. No blocker sits silent. |

### Scope Protection

| Rule | Owner | Detail |
|------|-------|--------|
| Post-planning scope changes | PM + TL | BOs cannot add stories without PM + TL capacity assessment |
| Sprint Start scope freeze | PM | Any change after Sprint Start requires a story swap — no net additions |
| Commitment integrity | Tech Lead | Engineers commit in Sprint Planning without BOs present |
| BO pre-read | PM | Sprint goal + candidate stories shared with BOs via async Confluence/Jira view (open item #21) |

### Engineer Time Protection

| Rule | Owner | Detail |
|------|-------|--------|
| Squad Sync | PM | Engineers never attend — PM represents the squad |
| BO Sign-off | PM | Engineers do not attend — commitment already made |
| Mid-Sprint Check-in | PM + TL | PM + Tech Lead only — engineers stay heads-down |
| Sprint End | PM + TL | Engineers done after Retro — admin is PM + Tech Lead |

### Ceremony Time Limits

| Ceremony | Hard Cap |
|----------|----------|
| Sprint Start + Retro & Demo (Mon W1) | 30 min start + 1 hr retro/demo |
| Squad Grooming (Tue W1) | 1 hr |
| Backlog Grooming (Thu W1) | 1 hr |
| Mid-Sprint Review (Mon W2) | 30 min |
| Sprint Planning (Thu W2) | 1 hr |
| Sprint End + Finalisation (Fri W2) | 30 min |
| Daily Standup | 15 min |

---

## Escalation Owner (Adrian)

| Trigger | Owner | SLA |
|---------|-------|-----|
| BO priority deadlock | Adrian | PM logs in BO Sign-off, escalates within 24hr. Sprint does not start without resolution. |
| Cross-squad unresolved blocker | Adrian | Unresolved at 48hr → PM escalates directly to Adrian |
| Scope dispute (PM vs BO) | Adrian | If PM and BO cannot agree on must-have vs nice-to-have |
| Sprint goal conflict | Adrian | If sprint goal challenged post sign-off — Adrian holds final decision authority |

---

## Pow Hwee Backup Protocol

| Role | Backup | Detail |
|------|--------|--------|
| Sprint Planning facilitation | PM | If Pow Hwee unavailable: PM facilitates. Engineers self-organise sizing. |
| Mid-Sprint Check-in | PM | PM runs solo. Flags technical risks async to Barry. |
| Technical blocker resolution | Senior Engineer | Most senior engineer takes temporary ownership. Barry notified. |
| Sprint End ticket closure | PM | PM closes with available info. Pow Hwee reviews on return. |
| Barry visibility | Pow Hwee | Async update to Barry after each Sprint Planning — sprint goal, commitment, key risks. No new meeting. |

---

## PM Time Budget Per Sprint

| Category | Hours/sprint |
|----------|-------------|
| Ceremonies (required) | ~9 hr |
| Pre-ceremony prep | ~4.25 hr |
| Post-ceremony follow-up | ~1.75 hr |
| Backlog management | ~4 hr |
| Stakeholder management | ~1.5 hr |
| Design + delivery coordination | ~2 hr |
| **Total structured work** | **~22 hr** |
| Unstructured / reactive | ~18 hr |
| **Sprint total (40hr fortnight)** | **~40 hr** |

> ⚠️ PM is in structured work for ~55% of the sprint. Story writing and AC prep are the highest-risk prep tasks — if blocked on business rules or designs, these slip and cascade into Refinement quality.

---

## Key Prep Deadlines (every sprint)

| Task | Due |
|------|-----|
| ACs complete for internal groom | EOD Mon W1 |
| ACs sharpened for formal groom | EOD Wed W1 |
| Sprint plan prep | Wed W2 |
| Demo script ready | EOD Fri W2 (for Mon W1 demo) |
| Sprint summary posted to Confluence | Fri W2 same day as Sprint End |

---

_Source: michelle-product-os/resources/cadence/sprint-cadence-framework.md · Updated 14 May 2026 (v2.1 — reconciled to sprint-calendar.md)_
