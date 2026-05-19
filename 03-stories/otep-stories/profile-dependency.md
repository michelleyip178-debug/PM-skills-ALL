# User Stories: Officer Profile (Critical Path Dependency)

**Epic:** Opportunities (Epic 4) — cross-pillar dependency on Profile
**JTBD:** #12 — Build a profile that represents me well
**Release:** MVP (HR-sourced); R2 (Dynamic Career Profiling)
**Status:** Draft — needs grooming
**Why this exists:** Profile is the start of the critical path. No profile → no pre-fill → no low-friction apply → no status tracking. Three personas downstream (Officer, Agency, Supervisor) are blocked without this.

---

## Stories

### US-P1: View my HR-sourced profile

**As an** officer,
**I want to** see a profile page populated with my HR data (name, agency, scheme of service, grade, current posting),
**So that** I can confirm what the system knows about me before using it to apply for opportunities.

**Acceptance Criteria:**
- [ ] When I go to "My Profile", I can see my name, email, agency, scheme of service, grade, and current posting — all sourced from HR systems. [ASSUMPTION: HR system provides these fields — source TBD, open question #1]
- [ ] All profile fields are populated without me needing to type anything.
- [ ] If a field has no HR data (e.g. posting not mapped), it shows "Not available" — the field doesn't disappear or break the layout.
- [ ] Each field shows when my HR data was last synced — I can tell if the information might be out of date.

**Edge cases:**
- Officer recently transferred — HR data may lag by days/weeks. Show stale data with "last updated" date, not an error.
- Officer has multiple concurrent postings (e.g. concurrent appointment) — show primary posting, flag if secondary exists.
- HR system is down at time of page load — show cached data with a "data may not be current" notice.

**Dependencies:**
- HR data pipeline must be established (source system, refresh cadence, field mapping)
- WOGAD authentication must be functional (OTEP-71)

**Priority:** MVP — officers need to see and trust their data before the platform asks them to act on it

**Open questions:**
1. Which HR system is the source of truth? VITALS? Another system?
2. What is the refresh cadence — real-time, daily, or on-login?
3. Which fields does the HR system actually expose via API?

---

### US-P2: View my competencies

**As an** officer,
**I want to** see the competencies associated with my role and scheme of service,
**So that** I can understand my profile as opportunity owners and matching systems will see it.

**Acceptance Criteria:**
- [ ] In my profile, I can see a list of competencies tagged to my scheme of service.
- [ ] Each competency shows its name, category, and whether I have it — yes or no. [ASSUMPTION: binary competency model for MVP — proficiency levels deferred to R1]
- [ ] If no competencies are mapped to my scheme yet, I see "No competencies mapped yet" with a note that it will be updated — not a blank section.
- [ ] Competencies are grouped by category (e.g. functional, leadership, technical).

**Edge cases:**
- Scheme of service has no competency framework defined yet — show empty state, don't hide the section
- Officer's scheme recently changed — competencies should reflect current scheme, not previous

**Dependencies:**
- Competency data model must be defined (source: COMET or manual mapping)
- Binary competency model confirmed (proficiency levels deferred to R1)

**Priority:** MVP — competencies drive opportunity matching and gap analysis in later releases. Getting the data visible early builds trust and surfaces data quality issues.

**Open questions:**
1. Is COMET the source for competency-to-scheme mapping?
2. How many schemes have competency frameworks defined today?
3. Is "binary" the right MVP model, or do agencies need at least basic/intermediate/advanced?

---

### US-P3: Pre-fill application from profile

**As an** officer,
**I want to** have my profile data (name, email, agency, grade) pre-filled when I start an application,
**So that** I can apply in minutes, not re-enter the same information every time.

**Acceptance Criteria:**
- [ ] When I click "Apply" on an OTG opportunity, the FormSG form opens with my name, email, agency, and grade already filled in from my profile. [ASSUMPTION: FormSG supports pre-fill via URL params — open item #14. This story is MVP only if confirmed; otherwise R1]
- [ ] I can edit any pre-filled field before submitting — pre-fill is a convenience, not a lock.
- [ ] If a profile field is missing (e.g. grade not available from HR), that field is left blank on the form — not filled with placeholder text.
- [ ] When I submit, the form reflects whatever I entered or edited — not the original pre-filled values if I changed them.

**Edge cases:**
- FormSG form fields don't match profile field names — field mapping must be defined per form template
- Officer's profile data changed between opening and submitting the form — use data at time of form load
- FormSG doesn't support pre-fill via URL params or API — this story is blocked; fall back to manual entry and defer to R1

**Dependencies:**
- US-P1 (profile must be viewable and populated)
- OTEP-130 (apply via FormSG must be functional)
- FormSG must support pre-fill mechanism (URL parameters, API, or embedded form)

**Priority:** MVP if FormSG supports pre-fill; R1 if it doesn't. This is the bridge between Profile and Apply — without it, the "low friction" promise is hollow.

**Open questions:**
1. Does FormSG support pre-fill via URL parameters? (Pow Hwee to confirm)
2. Which fields can be pre-filled? (Depends on what FormSG forms expect)
3. Is this an embed (iframe) or redirect (new tab)? Affects how pre-fill data is passed.

---

## How These Stories Fit the Critical Path

```
US-P1 (View profile)
  └→ US-P2 (View competencies)
  └→ US-P3 (Pre-fill from profile)
       └→ OTEP-130 (Apply via FormSG)  ← already has AC
            └→ US-10 (Confirmation)  ← already has AC
                 └→ US-14 (View applications)  ← already has AC
                      └→ US-15 (Status detail)  ← already has AC
```

US-P1 and US-P2 can be developed in parallel. US-P3 depends on both US-P1 and OTEP-130.

---

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
