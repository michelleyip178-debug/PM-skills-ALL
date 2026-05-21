# OTEP-319: Apply via FormSG — basic redirect (Internal Jobs, STIPs, Gigs)

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

As an  officer viewing an Internal Job, STIP, or Gig,  I want to  click "Apply" and be taken to the corresponding FormSG form,  So that  I can submit my application from the opportunity detail page. Acceptance Criteria:   If I'm on an Internal Job, STIP, or Gig detail page and I click "Apply", I'm taken to the FormSG form for that opportunity in a new tab. If the  formsg_url  for an opportunity is missing, I see "Application form unavailable — contact the posting agency" instead of the Apply button. If I'm on an SJR detail page, there's no Apply button.  Edge cases: formsg_url  points to a form that has been closed or deleted — officer sees a FormSG error page (outside OTEP's control). Consider showing "Form may no longer be available" guidance. Officer clicks "Apply" but FormSG is down — new tab shows FormSG's own error. No OTEP-side handling needed for basic redirect. Dependencies: OTEP-87 (detail page must exist) Risks: FormSG form quality is outside OTEP's control — broken or closed forms create a bad officer experience with no OTEP-side fix beyond the fallback error state. Open questions: Does FormSG support pre-fill via URL params? (open item #14, Pow Hwee) — determines if US-P3 lands in MVP Should the redirect include any OTEP tracking params (e.g. opportunity ID, officer ID) for analytics?

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
