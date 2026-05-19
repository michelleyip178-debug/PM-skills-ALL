# User Stories: Application Status Tracking

**Epic:** Opportunities (Epic 4)
**One-pager:** _TODO: Confluence link_
**Status:** Draft — needs grooming
**Dependency:** OTG lifecycle stories (OTEP-87–10) must be functional; FormSG webhook/callback for status updates

---

## Stories

### US-14: View my submitted applications

**As an** officer,
**I want to** see a list of all OTG opportunities I've applied to,
**So that** I can keep track of what I've submitted without relying on email or memory.

**Acceptance Criteria:**
- [ ] When I go to "My Applications", I can see all my OTG submissions — each showing the opportunity title, agency, date I submitted, and current status.
- [ ] If I haven't submitted any applications yet, I see a message guiding me to browse opportunities — not a blank page.
- [ ] If I have more than one application, the most recently submitted one appears at the top.

**Edge cases:**
- Officer applied before OTEP existed (legacy OTG) — are historical applications shown? (Likely out of scope for MVP)
- Application was submitted but FormSG webhook failed — does it show as "submitted" or not appear?

**Priority:** MVP — tracking is a core pillar of "end-to-end OTG lifecycle"

---

### US-15: See the status of an individual application

**As an** officer,
**I want to** see the current status of a specific OTG application,
**So that** I know where it stands without having to follow up manually.

**Acceptance Criteria:**
- [ ] When I click an application in my list, I see its full detail: opportunity summary, date I submitted, current status, and the history of status changes.
- [ ] When my application status has been updated, I see the latest status — not stale data. [ASSUMPTION: status updates come from the agency admin panel or FormSG webhook — source TBD]
- [ ] If my application has reached a final state (accepted, rejected, or withdrawn), the status is clearly marked as final — not ambiguous.

**Edge cases:**
- Status hasn't changed in weeks — should we show "last updated X days ago" to reassure?
- Agency hasn't actioned the application — is there a timeout or reminder mechanism? (Likely out of scope)

**Priority:** MVP — without status visibility, officers will flood agencies with follow-up emails

---

### US-16: Receive notification when application status changes

**As an** officer,
**I want to** be notified when my application status changes,
**So that** I don't have to keep checking OTEP manually.

**Acceptance Criteria:**
- [ ] When one of my application statuses changes, I see a notification indicator in OTEP — for example, a badge on "My Applications."
- [ ] If I have unread status updates, the affected applications are visually highlighted when I open "My Applications."

**Edge cases:**
- Officer hasn't logged in for weeks — do notifications accumulate? Is there an email fallback?
- Multiple status changes happen quickly (e.g. Under Review → Shortlisted same day) — show each or just latest?

**Priority:** MVP — minimal in-app notification. Email/push notifications deferred to R1.

**Note:** MVP scope is in-app notification only (badge/highlight). Email or push notifications are R1.

---

### US-17: Withdraw an OTG application

**As an** officer,
**I want to** withdraw my application for an OTG opportunity,
**So that** I can free up the slot if I'm no longer interested or have accepted another opportunity.

**Acceptance Criteria:**
- [ ] If my application is in Submitted or Under Review status, clicking "Withdraw" shows a confirmation step before anything is cancelled.
- [ ] After I confirm withdrawal, the status changes to "Withdrawn" — this can't be undone.
- [ ] If my application has already reached a final state (accepted or rejected), the withdraw option is not shown.

**Edge cases:**
- Officer withdraws after being shortlisted — does the agency get notified? (Operational process question)
- Can an officer re-apply after withdrawing? (Depends on whether opportunity is still open)

**Priority:** MVP — officers need control over their applications

---

## Status Model (Proposed)

```
Submitted → Under Review → Shortlisted → Accepted / Rejected
                                       ↘ Withdrawn (officer-initiated, from any non-final state)
```

**Open question:** Is this the right set of statuses? Need to validate with Pow Hwee what statuses the backend/FormSG can support.

---

## Open Questions

1. **Status source of truth** — where do status updates come from? Agency manually updates in admin panel? Automated from FormSG? Both?
2. **Status granularity** — how many statuses do agencies actually use? Is "Under Review" vs "Shortlisted" realistic for all agencies?
3. **Historical applications** — do we show applications submitted before OTEP launch (via OTG directly)? Likely no for MVP.
4. **C@G tracking** — since C@G applications happen off-platform, can we show any status? (Likely no — out of our control. State this explicitly in scope.)
5. **Notification channel** — in-app only for MVP. Email/push for R1?
6. **Withdrawal workflow** — does this trigger anything on the agency side, or is it a OTEP-only status change?

## Definition of Ready Checklist (from Eng Manager)

- [ ] Prioritised and able to deliver in a sprint
- [ ] All platform subtasks (including test cases) identified and created
- [ ] UI assets and UX flows designed and linked to all Acceptance Criteria (Amber)
- [ ] Feature flag designed with entry point identified
- [ ] API Contract identified and documented (Pow Hwee)

### Additional checks (PM)

- [ ] Acceptance criteria are clear and testable
- [ ] Dependencies identified
- [ ] Edge cases and error states documented
