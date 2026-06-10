# OTEP-319: Apply via FormSG — basic redirect (Internal Jobs, STIPs, Gigs)

**Status:** Backlog
**Assignee:** Thomas Huchedé
**Story Points:** N/A

---

## Description

User story:  As an officer viewing an Internal Job, STIP, or Gig, I want to click Apply and be taken to the FormSG form so I can submit my application. Acceptance Criteria Clicking Apply on an Internal Job, STIP, or Gig detail page opens the opportunity's FormSG form in a new tab. The redirect uses  formsg_url  directly — no pre-fill or URL parameters added.  (Pre-fill dropped from MVP — Squad Sync decision 2026-05-26.) If  formsg_url  is missing: show "Application form unavailable — contact the posting agency" in place of the Apply button. If FormSG is down or the form is closed: the officer sees FormSG's own error page. No OTEP-side handling needed. Open Question (resolve before build) Should the redirect append any OTEP tracking params (e.g. opportunity ID) for analytics? Engineering to confirm whether appending params could break FormSG form submission. Out of Scope FormSG pre-fill via URL params — dropped from MVP (Squad Sync 2026-05-26, open item #14 resolved) Webhook on form submission — OTEP-130, Sprint 4 On an SJR detail page: no Apply button shown, R1 Dependencies OTEP-87 (Apply CTA must exist on the detail page) formsg_url  confirmed present in OTG data ✅ (2026-05-21)

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-05-28)
Open question on tracking params should be resolved before sprint starts. Otherwise AC looks good.

*Synced from Jira: 2026-06-10*
