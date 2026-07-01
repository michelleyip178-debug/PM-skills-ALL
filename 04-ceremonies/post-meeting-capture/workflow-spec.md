# Post-Meeting Capture — Workflow Spec

## Purpose

Route meeting outputs to the right files in under 2 minutes. Meetings produce three things: decisions, action items, and open questions. Each has a home. Without this workflow, they pile up in inbox.md or get lost entirely.

## When

Immediately after any meeting. The 2-minute window matters — if you wait until end of day, you'll forget the nuance. Do it while context is fresh.

## Process Overview

```
Meeting ends
     |
Step 1: Dump raw notes (30 sec)
     |
Step 2: Triage into 3 buckets (1 min)
     |
Step 3: Route to the right files (30 sec)
```

---

## Step 1: Dump Raw Notes (30 sec)

Paste raw notes anywhere — `inbox.md`, a scratch buffer, or directly into the triage below. Don't format. Don't polish. Just capture before you forget.

Include: who was there, what was discussed, any verbatim phrases that matter.

## Step 2: Triage into 3 Buckets (1 min)

Scan your notes. Tag each item:

| Tag | What it is | Example |
|-----|-----------|---------|
| **D** — Decision | Something was decided. A path was chosen over alternatives. | "We agreed to defer competency matching to R1" |
| **A** — Action item | Someone (including you) committed to doing something by a date. | "Pow Hwee to confirm C@G API by Friday" |
| **Q** — Open question | Something was raised but not resolved. Needs an owner and a deadline. | "Is Secondment a distinct type or sub-type of SJR?" |
| **I** — Info only | Useful context but no action needed. | "Leo mentioned Keycloak realm is deployed" |

Most items are **I** (info only). Let those go — they're in your memory and the meeting happened. Only route D, A, and Q.

## Step 3: Route to the Right Files (30 sec)

| Tag | Route to | Format |
|-----|----------|--------|
| **D** — Decision | `../../../PM-OS/outputs/decisions/2026-05-29-W22-decisions-log.md` | Date, Decision, Rationale, Owner |
| **A** — Action item (mine) | `00-hub/tasks-active.md` | Add to In Progress or Up Next |
| **A** — Action item (theirs) | `00-hub/open-items.md` | Item, Owner, Needed By, Impacts/why, Status |
| **Q** — Open question | `00-hub/open-items.md` | Item, Owner, Needed By, Impacts/why, Status |
| **I** — Info only | Nowhere (or update a people profile if relevant) | — |

### Special cases

- **Scope decision** → also check: does this affect `../../../PM-OS/outputs/decisions/2026-05-29-W22-decisions-log.md` AND the PRD decision tracker (Section 11)?
- **New risk or dependency** → add to `00-hub/risks.md`
- **Design direction** → update the relevant story file's AC or designer notes
- **Stakeholder insight** → update the person's profile in `06-skills-and-decisions/stakeholders/people/`

## Meeting-Specific Playbooks

| Meeting | What you'll typically capture |
|---------|------------------------------|
| Standup | Blockers (→ active.md), status changes (→ current-sprint.md if story status changed) |
| Design review (Amber) | Design decisions (→ decisions-log), AC updates (→ story files) |
| Internal groom | Edge cases (→ story files), open questions (→ open-items), scope calls (→ decisions-log) |
| BO sync (Jacky/XZ) | Scope direction (→ decisions-log), requirements clarification (→ story files or open-items) |
| Steering (Mark/GK) | Strategic decisions (→ decisions-log), new asks (→ check MVP guardrails first) |
| 1:1 (Adrian) | Feedback (→ person profile), priorities (→ active.md), career guidance (→ pm-growth notes) |

---

## Archive

If the meeting produced substantive notes (grooming, planning, steering), also save the raw dump to `04-ceremonies/archive-meetings/` with the date:
```
04-ceremonies/archive-meetings/{subfolder}/YYYY-MM-DD-{meeting-name}.md
```

Don't archive standup notes or 1:1s unless something significant happened.

---

## Quality Check

After routing, verify:
- No decisions sitting unlogged
- No action items assigned to you that aren't in `active.md`
- No open questions without an owner

## Done when

`inbox.md` raw capture is empty. Every D, A, and Q is in its proper file. Total time: under 2 minutes.
