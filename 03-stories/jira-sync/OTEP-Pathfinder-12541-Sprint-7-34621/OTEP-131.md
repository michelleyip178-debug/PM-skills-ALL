# OTEP-131: Handle missing or broken FormSG application link.

**Status:** Backlog
**Assignee:** Thomas Huchedé
**Story Points:** 2
**Sprint:** OTEP-Pathfinder Sprint 7 (2026-07-26 → 2026-08-09)

---

## Description

As an officer, I want to see a clear message if the application link is unavailable so I know how to get help rather than facing a broken or missing button. Acceptance Criteria If  formsg_url  is missing or empty for an Internal Job, STIP, or Gig, the Apply button is not shown — it is replaced with "Application form unavailable — contact the posting agency" The message is shown in the same position as the Apply button would be — no layout shift If  formsg_url  is present but the FormSG form is down or closed, the officer lands on FormSG's own error page — CareerCompass shows no additional error state for this case Out of scope:   Detecting whether a FormSG URL is live/reachable before rendering the button agency POC email or contact details (requires payload field confirmation) SJR detail pages show neither an Apply button nor this error message (no application flow for SJRs in MVP)

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Rathika Ramalingam** (2026-07-15)
does this mean the actual implementation is blocked by data? Anyways, I move the task to In progress.

---

**Thomas Huchedé** (2026-06-25)
As discussed today, the POC is missing in the source excel file so we have nothing to display.  We’ll keep the placeholder for now just to display something for the demo.

---

**Amber Tong** (2026-05-13)
Figma link  here .

---
*Synced from Jira: 2026-07-28*
