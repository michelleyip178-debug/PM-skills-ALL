# User Stories: C@G Deep-link Handoff

**Epic:** Opportunities (Epic 4)
**One-pager:** _TODO: Confluence link_
**Status:** Draft — needs grooming
**Dependency:** C@G API/feed providing opportunity data to OTEP

---

## Stories

### OTEP-89: View C@G opportunity summary on OTEP

**As an** officer,
**I want to** see a summary of a Careers@Gov opportunity on OTEP,
**So that** I can decide whether it's worth exploring further before being redirected.

**Acceptance Criteria:**
- [ ] When I click a C@G opportunity on the listing page, I see a summary with: title, organisation, job function, employment type, and experience level.
- [ ] On the C@G opportunity summary, I can clearly see that applying will take me to Careers@Gov — not an OTEP form.
- [ ] If the C@G listing has expired, I see a clear "no longer available" message — not a broken page.

**Edge cases:**
- C@G data is stale (opportunity closed on C@G but still showing on OTEP) — how often do we sync?
- C@G summary has minimal metadata — what's the minimum viable detail page?

**Priority:** MVP — officers need context before being redirected off-platform

---

### OTEP-133: Redirect to Careers@Gov to apply

**As an** officer,
**I want to** be taken directly to the Careers@Gov listing when I choose to apply,
**So that** I can complete my application on the appropriate platform without searching for it again.

**Acceptance Criteria:**
- [ ] When I click "Apply on Careers@Gov", I'm taken directly to that specific C@G listing in a new tab.
- [ ] When the redirect happens, OTEP briefly tells me I'm leaving the platform before I go.
- [ ] If the deep-link URL is broken or expired, I see a fallback message — for example, "Search for this role on Careers@Gov."

**Edge cases:**
- C@G requires its own login — officer may need to authenticate again on C@G (outside our control)
- Deep-link format changes on C@G side — how resilient are our links?
- Officer uses mobile — does deep-link open in-app browser or external?

**Priority:** MVP — this is the core action of the C@G pipeline

---

### OTEP-88: Understand the difference between OTG and C@G application flows

**As an** officer,
**I want to** clearly understand whether an opportunity will let me apply on OTEP or redirect me elsewhere,
**So that** I'm not surprised or confused when the experience differs between opportunities.

**Acceptance Criteria:**
- [ ] On any opportunity — OTG or C@G — I can tell from the button or surrounding text whether I'll apply on OTEP ("Apply") or be redirected to Careers@Gov ("Apply on Careers@Gov").
- [ ] On the opportunity listing, C@G cards have a visual indicator showing they're external — I can spot them before clicking.

**Edge cases:**
- Officers who don't know what "Careers@Gov" is — do we need an explainer/tooltip?
- First-time user encountering both types — is there an onboarding moment?

**Priority:** MVP — without clarity, the two-pipeline model creates confusion instead of convenience

---

## Open Questions

1. **Detail page depth for C@G** — full detail page or just a card with "View on Careers@Gov"? How much data do we get from C@G to show?
2. **Deep-link reliability** — what's the URL format? How do we handle link rot?
3. **Sync frequency** — how often do we pull C@G listings? Real-time feed vs. nightly batch?
4. **"Leaving OTEP" interstitial** — full modal, toast notification, or just open in new tab with no warning?
5. **Can we track C@G applications?** — Once an officer leaves OTEP, do we know if they applied? (Likely no for MVP)

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
