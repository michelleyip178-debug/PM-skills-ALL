# Grooming Brief — Sprint 3 Backlog Grooming
> Generated: 2026-05-21 | Session: Thu 22 May, 14:00, L11 Anson
> Facilitator: Rama | Content lead: Michelle
> Sprint 3: 1–12 Jun (~9 dev days, Vesak Day 2 Jun)
> Note: Auth stories (OTEP-71/110/304/305) moved to Sprint 4+ today — this brief covers the reallocated Sprint 3 scope.
>
> **Session structure (updated 2026-05-21):** Joint session with OTEP Core Squad. Imelda goes first — 2 tickets from her squad. Michelle takes over for OTEP Pathfinder Sprint 3 stories after Imelda's done.
> ⚠️ **Before session:** Confirm with Imelda what her 2 tickets are. Check for dependencies — especially anything touching reference data (job family, job function, agency, competencies), CSC SSO, or shared infra.

---

## Sprint 3 Goal (propose in session)

By end of Sprint 3, an officer can filter the opportunity listing by type and apply to an Internal Job, STIP, or Gig via FormSG redirect — powered by live OTG data imported automatically.

---

## Readiness Scorecard

| Story ID | Title | Story Format | AC Written | AC Language | Design | Dependencies | Open Items | Ready? |
|---|---|---|---|---|---|---|---|---|
| OTEP-317 | Clear filters and reset view | ✅ | ✅ | ✅ | ✅ | OTEP-86 | — | ✅ |
| OTEP-319 | Apply via FormSG basic redirect | ✅ | ✅ | ✅ | ✅ | OTEP-87, OTEP-131 | #14 (not blocking) | ✅ |
| OTEP-86 | Filter by opportunity type | ⚠️ | ⚠️ Jira has scope bleed | ⚠️ | ✅ | OTEP-85 must close S2 | #9, #16 (not S3) | ⚠️ |
| OTEP-87 | Enhanced detail — apply CTA only | ⚠️ | ⚠️ Jira has competency ACs | ⚠️ | ⚠️ lock date unset (#22) | OTEP-128 (S2), OTEP-319 | #18, #20 | ⚠️ |
| OTEP-131 | Null `formsg_url` fallback | ⚠️ | ❌ Needs rewrite | ⚠️ | ✅ Amber Figma attached | OTEP-319 | #8 🔴 open | ❌ |
| OTEP-192 | Recurring OTG ingest job | ❌ | ❌ No ACs | N/A | N/A | OTEP-193 + OTEP-313 (S2) | — | ❌ |
| OTEP-271 | Local POCDEX database | ❓ no story file | ❓ | ❓ | N/A | First POCDEX project | #31 Daryll | ❓ |
| OTEP-203 | Standalone POCDEX API service | ❓ no story file | ❓ | ❓ | N/A | OTEP-271 | #31 Daryll | ❓ |
| OTEP-318 | Filter by category | ❌ no description | ❌ | N/A | ❓ | OTEP-289 spike output | Spike result TBC | ❌ |
| OTEP-92 | "Tracking" subtask (under OTEP-86) | ❌ no description | ❌ | N/A | N/A | OTEP-86 | Purpose unclear | ❌ |

---

## Fix Before You Walk In

**You have 4 stories that need Jira updates before 14:00. Do them in this order.**

---

### 1. OTEP-86 — Strip scope bleed from Jira ACs

The Jira blob includes three things that are NOT OTEP-86:
- "Filter by Functions / Categorisation" → **OTEP-318** (separate story, conditional)
- "Filters work in combination with keyword search" → **search is not in Sprint 3**
- "I can clear all filters" → **OTEP-317** (already a separate ticket)

Replace the entire Jira AC field with this:

```
- I can filter by opportunity type: Internal Job, SJR, or STIP/Gig. Secondment shows under SJR.
- I can select more than one type at once — selecting two types shows opportunities matching either.
- If I haven't selected any filter, all opportunity types are shown by default.
- If my selected filters return no results, I see "No opportunities found" — not a blank list.
```

Also flag: "have a tooltip to explain each opportunity type" is in the Jira blob but not in the canonical story. Either add it as a good-to-have or confirm with Pow Hwee that it's out of Sprint 3.

---

### 2. OTEP-87 — Strip competency ACs from Jira

Jira currently shows "competencies I already match," "competencies I can develop," and "X / Y competencies matched." All deferred — competency source is now confirmed as Imelda's squad but integration method and timeline are TBC (#18). **Sprint 3 = apply CTA only.**

Replace Jira ACs with:

```
Must-have (Sprint 3):
- If I'm viewing an Internal Job, STIP, or Gig, I see a clear "Apply" button linking to the FormSG form.
- If I'm viewing an SJR, there's no apply action shown.
- If the opportunity has closed, the apply button is not shown and I see "This opportunity is closed."

Out of scope for Sprint 3: competency section, competency match ratio — deferred to Sprint 4+ pending #18 (Imelda's squad owns competency master data).
```

Also confirm with Amber before the session: SJR detail page treatment (open item #20). Design was finalised for the listing card but the detail page treatment isn't confirmed. Pow Hwee will ask.

---

### 3. OTEP-131 — Rewrite the ACs (and resolve #8 first if you can)

Current Jira description opens with "Current - If the FormSG link is unavailable, it will show when I land on the form itself." That's the broken current behaviour — not an AC. The "[Agency POC]" placeholder is also implementation-blocking.

**Chase Rama on #8 (agency contact field name) before the session.** If you get the field name, paste these ACs into Jira:

```
- If the Apply button is tapped and formsg_url is null or empty, the button is disabled.
- Instead of the Apply button, I see: "Application form unavailable — contact [Agency POC field name] directly."
- If I'm on an SJR detail page, no Apply button or fallback message appears — SJRs have no apply flow.
```

If #8 is still unresolved when you walk in, raise it in the session and assign Pow Hwee to confirm the field name from the data model.

**This story must ship before OTEP-319.** No OTEP-131 = OTEP-319 can't close.

---

### 4. OTEP-192 — Write ACs before the session or it won't size

Jira has a title and nothing else. Use this as the discussion-starter in the room:

**Proposed story:**
> As a product team, I want OTG opportunity data to be fetched and refreshed automatically, so that officers always see current listings without a manual trigger.

**Proposed ACs:**
```
- Opportunities data is refreshed from the OTG Excel export on a recurring schedule (confirm: daily? frequency TBC with Pow Hwee).
- When a record in the OTG export is missing any mandatory field (Title, Agency, Type, Posting Date, Closing Date), it is excluded — other valid records are not affected.
- When the OTG export file is unavailable or malformed, the most recently fetched valid data remains displayed — the listing does not go blank.
- A failed run is logged and does not block the next scheduled run.
```

**Hard gate:** OTEP-193 (data model) and OTEP-313 (ingest table) must land in Sprint 2 before this story can start. If either slips, flag to Pow Hwee at the session.

---

## Recommended Grooming Order

| # | Story | Rationale | Time |
|---|-------|-----------|------|
| 1 | **OTEP-317** ✅ | Clean, simple, warm up. | ~5 min |
| 2 | **OTEP-319** ✅ | Core apply action. `formsg_url` confirmed. Anchor for the apply chain. | ~15 min |
| 3 | **OTEP-86** ⚠️ | Filter anchor. Fix Jira ACs before walking in. | ~20 min |
| 4 | **OTEP-87** ⚠️ | Detail page enhancement. Strip competency ACs first. | ~15 min |
| 5 | **OTEP-192** ❌ | Backend critical path. Proposed ACs above as starting point. | ~20 min |
| 6 | **OTEP-271 / OTEP-203** ❓ | POCDEX backend. Let Pow Hwee lead — flag Daryll engagement. | ~15 min |
| 7 | **OTEP-131** ❌ | Must exist before OTEP-319. Resolve #8 or assign in session. | ~10 min |
| 8 | **OTEP-318** ❌ | Only groom if OTEP-289 spike output is confirmed green. Otherwise skip. | ~5 min |
| 9 | **OTEP-92** ❌ | Clarify purpose or close. | ~5 min |

---

## Open Items — Assign an Owner in the Session

| # | Open Item | Suggested Owner | Needed By |
|---|---|---|---|
| #8 | Agency contact field name for OTEP-131 fallback message | Rama | Before Sprint 3 starts |
| #14 | Does FormSG support pre-fill via URL params? | Pow Hwee | Before Sprint 3 ships (OTEP-130) |
| #15 | Email/notification service — existing platform or new build? | Pow Hwee | Before Sprint 3 (US-10) |
| #16 | Search indexing infrastructure for OTEP-86 elastic matching | Pow Hwee | Before Sprint 3 |
| #20 | SJR detail page treatment (no button? "Coming soon"? hide?) | Amber | Before OTEP-87 ships |
| #31 | POCDEX planning session with Daryll — support not settled | Michelle | Before Sprint 4 planning |
| — | OTEP-289 spike output — go/no-go for OTEP-318 | Pow Hwee | Confirm today |

---

## R1 Deflection List

- "Filter counts per type?" → "R1 — type filter lands first, then we see if counts add value."
- "Persist filters across sessions?" → "URL params within-session is sufficient for MVP. Cross-session is R1."
- "Add keyword search in Sprint 3?" → "Search is MVP but Sprint 4. Sprint 3 is type filter + apply — that's Thomas's full load."
- "Can we put the competency section in OTEP-87 now?" → "Competency source is Imelda's squad — integration method and timeline TBC (#18). Sprint 3 = apply CTA only."
- "SJR apply flow?" → "Future release decision from 2026-05-13. All apply flows will go through OTEP eventually — not MVP."
- "Agency admin or RBAC?" → "Sprint 6. Out of scope today."

---

## Pow Hwee Will Probably Ask...

- **On OTEP-86:** "Why is 'filter by Functions/Categorisation' and 'keyword search' in this AC?" → Pre-empt: strip those before entering the room. "Type filter only in Sprint 3."
- **On OTEP-87:** "Are we building the competency section in Sprint 3?" → "No. Competency source is Imelda's squad, integration TBC. Sprint 3 = apply CTA only."
- **On OTEP-192:** "What's the trigger? How often does the job run? What's the data freshness SLA?" → Proposed ACs above. Let him fill in trigger/frequency.
- **On OTEP-131:** "What's the Agency POC field name?" → Chase Rama on #8. If unresolved: "Can you confirm the field name from the data model?"
- **On OTEP-271/203:** "Have we spoken to Daryll about the POCDEX support structure?" → "Not yet — flagging #31. Need a planning session before Sprint 4."
- **On OTEP-318:** "Did the spike run? What was the output?" → Know the answer before the session. If the spike result isn't in your hands, ask Pow Hwee to share it.
- **On OTEP-319:** "Should the redirect include OTEP tracking params — opportunity ID, officer ID?" → "Good catch. Instrumentation story is Sprint 4 (no ticket yet). Basic redirect = no tracking params in Sprint 3."
- **On OTEP-92:** "What's this 'Tracking' subtask?" → "Can you clarify? Is this the analytics story or an artifact we should close?"

---

## Self-Check Before the Room

- [ ] OTEP-86 Jira ACs updated — scope bleed removed (no category filter, no search, no persist)
- [ ] OTEP-87 Jira ACs updated — competency section stripped, apply CTA ACs only
- [ ] OTEP-131 ACs drafted — chased #8 or ready to assign in session
- [ ] OTEP-192 proposed ACs in hand — ready to discuss trigger/frequency with Pow Hwee
- [ ] OTEP-289 spike output confirmed — know whether OTEP-318 is go or no-go
- [ ] SJR detail page treatment confirmed with Amber (#20) before session

---

*Generated: 2026-05-21. Source: sprint-status.md, filters.md, otg-lifecycle.md, open-items.md, risks.md, jira-sync/OTEP-Pathfinder-Sprint-3/.*
