# OTEP-87: View Careers@Gov Opportunity Detail

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

---

## Description

**User story:** As an officer, I want to view the full details of a Careers@Gov opportunity so I can decide whether to apply and be taken directly to the C@G platform to do so.

**Sprint 3 scope:** C@G detail page display + Apply CTA deep-link. Competency section deferred — see Out of Scope.

---

## Acceptance Criteria

### Detail page display

1. The detail page renders the C@G opportunity payload sourced from the C@G API (via OTEP-377). Fields displayed: title, agency, description, duration, and all available structured fields returned by the C@G payload.
2. If any display field has no data, show “Not specified.” Do not hide the field label.
3. The page is consistent in layout with the OTG detail page (OTEP-128) — same card structure, same “Not specified” fallback, same back-navigation behaviour.

### Apply CTA

4. A single prominent CTA is shown: **”Apply via Careers@Gov”**.
5. Clicking the CTA opens the specific C@G opportunity in a new tab, deep-linking directly to that posting on the Careers@Gov platform (OTEP-89).
6. OTEP captures a `click-to-cag` event at the point of redirect.
7. If the opportunity is no longer available on C@G after the officer clicks through, that is handled entirely on the C@G side — OTEP shows no error state for this scenario.
8. There is no FormSG redirect and no OTG apply flow for C@G listings.

### Navigation

9. When the officer navigates back to the listing using the in-page “back” link (not the browser back button), their filter and pagination state is exactly as they left it.

---

## Out of Scope (Sprint 3)

- Competency match section — deferred pending open item #18 (officer competency data model, Imelda’s squad)
- Proficiency-level matching
- Personalisation of any kind
- SJR apply handling (no C@G SJR flow in MVP)

---

## Dependencies

- OTEP-377 — Fetch C@G specific payload in detail API (BE)
- OTEP-378 — Map C@G payload to Detail Page UI (FE)
- OTEP-379 — Automated tests for C@G detail rendering
- OTEP-89 — Deep-link CTA behaviour

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-377 | Fetch C@G specific payload in detail API | Backlog |
| OTEP-378 | Map C@G payload to Detail Page UI | Backlog |
| OTEP-379 | Automated tests for C@G detail rendering | Backlog |

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-06-02)
Hi   , while the title is correct, the details of this ticket currently talk mostly about click to apply. Could you please amend the description and scope to ensure it fully covers showing the actual opportunity details?

---

**Pow Hwee TAN (PSD)** (2026-05-28)
Title has been updated to "View Careers@Gov Opportunity Detail" since Internal Jobs/STIPs/Gigs detail is done in Sprint 2 (OTEP-128/327/314). However, the AC still references FormSG redirect and "Internal Jobs, STIPs, Gigs". Suggest revising AC to reflect C@G behaviour — the Apply CTA should deep-link to Careers@Gov platform (per OTEP-89), not trigger FormSG.
