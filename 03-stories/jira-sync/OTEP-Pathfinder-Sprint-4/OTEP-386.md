# OTEP-386: Officers clicks on tooltip link to view a page/popup on the different opportunity types

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** 2

---

## Description

**User story:** As an officer, I want to understand what each opportunity type means before I apply a filter, so I can make an informed choice without leaving OTEP.

**Context:** OTEP-86 introduced type filters (STIP, Gig, Internal Job, SJR) with a tooltip on each type label. This ticket delivers the tooltip content and the in-app "Learn more" experience — a page or modal within OTEP that explains the opportunity types, replacing the previous plan to link out to the EOM Microsite.

**Decision:** Link-out to EOM Microsite is removed. Explanation of opportunity types lives within OTEP.

**Acceptance Criteria:**

1. Each opportunity type label in the filter sidebar (STIP, Gig, Internal Job, SJR) has an info icon that is visible at all times — not on hover only.
2. Tapping or clicking the icon opens a tooltip or small popover with a one-line plain-English description of that opportunity type.
3. The popover includes a "Learn more" link that opens an in-app page or modal explaining all opportunity types in full.
4. The in-app page or modal covers all four types with their descriptions. Copy:
   - **Internal Job** — "A full-time role open to eligible officers across the Public Service."
   - **STIP** — "A short-term attachment (weeks to months) to build skills in a new area."
   - **Gig** — "A project-based task you can take on alongside your current role."
   - **SJR** — "A secondment or job rotation — an extended placement in a different role or agency."
5. The tooltip closes when the officer clicks/taps outside it or presses Escape. The in-app page/modal has a visible close action.
6. The tooltip does not interfere with filter selection — tapping the type label still applies the filter; only tapping the icon opens the tooltip.
7. The tooltip icon and in-app page are accessible: icon has an `aria-label`, content is keyboard-navigable, and focus returns to the icon on close.

**Out of scope:**

- Link-out to EOM Microsite or any external site
- Tooltip on the opportunity card or detail page (filter sidebar only)

**Open item before grooming:** Confirm with Amber — is the "Learn more" destination a modal overlay or a dedicated `/opportunity-types` page? This determines routing and back-navigation behaviour.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---

*Synced from Jira: 2026-06-11*

*Synced from Jira: 2026-06-11*
