# OTEP-975: [PATHFINDER] E2E — Ringfencing: Blocked vs Eligible Views (by Agency)

**Status:** Done
**Assignee:** N/A
**Story Points:** N/A

---

## Description

E2E Test Case: Ringfencing — Blocked vs Eligible Views  Personas: Richard_RAMOS_FROM.TP@cscollege.gov.sg Richard@Cc2026 michelle_yip@psd.gov.sg michelleyip Preconditions Opportunity R = [UAT-RF-006] Restricted Direct-Link Opportunity — ringfencing active, Agency filter: EXCLUDE = Enterprise Singapore. Officer A (Richard Ramos, Enterprise Singapore): excluded by ringfencing, does not meet criteria for [UAT-RF-006]. Officer B (Michelle, MDDI): not excluded, meets criteria for [UAT-RF-006]. Test Steps # Step Expected Result 1 Log in as Richard Ramos (Enterprise Singapore, ineligible) and open the [UAT-RF-006] page Details and Apply button are restricted/hidden. Message shown: "This opportunity isn't available based on your current profile. Explore other opportunities that may be a better match." with an "Explore opportunities" button linking back to the full listing.   2 Log in as Richard Ramos (Enterprise Singapore, ineligible), then direct-link to  https://uat.careercompass.gov.sg/opportunities/019fe00a-dc21-77e0-86f8-c7cb0062b858?ms=search Details and Apply button are restricted/hidden. Message shown: "This opportunity isn't available based on your current profile. Explore other opportunities that may be a better match." with an "Explore opportunities" button linking back to the full listing.   3 Log in as Michelle (MDDI, eligible) and open the same [UAT-RF-006] page Page loads normally; Apply button is visible and clickable; no restriction message is shown     Related Tickets   — source story; this E2E test validates its Acceptance Criteria (eligible + ineligible detail page states).   — ineligible-via-deep-link scenario (Step 2) is absorbed into OTEP-390's AC per that ticket; OTEP-133 itself is Done.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-18)
Works for Michelle, can’t open for Richard Ramos

---
*Synced from Jira: 2026-08-25*
