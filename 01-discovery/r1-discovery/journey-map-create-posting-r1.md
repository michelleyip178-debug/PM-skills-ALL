# Customer Journey Map — Create a Posting (Agency-Native, R1)

**Persona:** Posting Manager — HR Executive/Officer at Ministry or Statutory Board (Persona 3)  
**State:** R1 (Q1'27). Covers the **authoring** half of the agency experience — the prequel to [`journey-map-posting-manager-r1.md`](journey-map-posting-manager-r1.md), which covers review→close.  
**Created:** 2026-06-02  
**Why this exists:** Opportunity creation moved from R4 into R1 (D 2026-06-02). Agencies now author postings via an OTEP-native form. That lane had **no discovery** — this map is the first pass at it.

> **Reads with:** the end-to-end blueprint (stage 1a), the posting-manager journey (stages after publish), and the ATS-pivot discovery (idea #7, "creation as a simple form"). **Open dependency:** if the ATS owns creation (World A), this native-form journey is replaced by an ATS hand-off — see Scope Concern below.

---

## Today's reality (the baseline we're replacing)

The Posting Manager creates development postings **in OTG today** — a separate legacy system. They fill OTG's posting form, it publishes to the OTG marketplace, and applications come back via FormSG email. CareerCompass currently ingests those OTG postings read-only.

R1 changes the front of this: the Posting Manager authors the posting **in CareerCompass**, and it lives in OTEP. The pain they feel today isn't really *creation* (OTG's form works) — it's the disconnect between where they post (OTG) and where everything else now lives (CareerCompass). Native creation closes that loop.

**So the value prop for native creation is narrower than "a better form":** it's *one system for the whole cycle* — post, receive, review, close, all in CareerCompass, instead of OTG-to-post + email-to-receive + spreadsheet-to-track.

---

## Journey Stages

### Stage 1 — Trigger
**A programme cycle opens; the manager needs to post an opportunity**

| | Detail |
|---|---|
| **Touchpoint** | Programme calendar / agency HR directive: "STIP cycle opens, post your roles" |
| **User action** | Logs into CareerCompass agency view; clicks "Create Posting" |
| **Thoughts** | "Is this instead of OTG now, or as well as? I don't want to post twice." |
| **Emotion** | 😐 Neutral, slightly wary — new place to do a familiar task |
| **Pain (today)** | Posts in OTG; no link to where applications are tracked |
| **Opportunity** | Make "this replaces OTG for your agency" unmistakable. Dual-posting (OTG *and* CareerCompass) is the failure mode that kills trust and doubles their work. |

---

### Stage 2 — Authoring the posting
**Filling the creation form**

| | Detail |
|---|---|
| **Touchpoint** | Structured creation form — type (STIP/GIG/C@G/Internal), title, description, competencies, duration, closing date, agency |
| **User action** | Fills fields; some pre-filled from agency profile (agency name, contact) |
| **Thoughts** | "This is more fields than OTG had" / "Good, the competency tags match what officers see" |
| **Emotion** | 🙂 if fast, 😩 if it feels like more work than OTG |
| **Pain (today)** | OTG form is freeform; descriptions vary wildly in quality, which hurts officer discovery downstream |
| **Opportunity** | Structured fields (esp. competencies) improve listing quality *and* feed the future applicant-competency-filter this persona wants most. Templates per posting type reduce blank-page friction. |

---

### Stage 3 — Validation + preview
**⭐ Aha moment — "I can see exactly what the officer will see"**

| | Detail |
|---|---|
| **Touchpoint** | Preview pane showing the posting as it'll appear in the officer-facing detail page |
| **User action** | Reviews the preview; catches a vague description; edits before publishing |
| **Thoughts** | "Oh — this is what they see. Let me make the competencies clearer." |
| **Emotion** | 😌 Confident — control they never had in the OTG-to-FormSG disconnect |
| **Pain (today)** | In OTG, they post blind — no preview of the officer experience |
| **Opportunity** | The preview is the moment native creation beats OTG. It closes the author↔officer gap. Inline validation (required fields, closing-date sanity) prevents bad postings reaching officers. |

---

### Stage 4 — Publish
**Posting goes live into the listing**

| | Detail |
|---|---|
| **Touchpoint** | "Publish" action → confirmation → posting appears in the officer listing |
| **User action** | Publishes; optionally schedules a future go-live date |
| **Thoughts** | "Is it live now? Can officers see it? Did it also need OTG approval?" |
| **Emotion** | 😊 Satisfied if instant + visible; 😟 anxious if there's an opaque approval step |
| **Pain (today)** | OTG publish has approval lag; managers don't know when their posting is actually visible |
| **Opportunity** | Immediate "live now, X officers in pilot agencies can see it" confirmation. **Open question: is there an approval/review gate before publish?** (agency policy may require it — see Scope Concern) |

---

### Stage 5 — Handoff to the review cycle
**The posting now exists — review journey begins**

| | Detail |
|---|---|
| **Touchpoint** | The posting appears in the manager's dashboard with an application counter |
| **User action** | Returns later to review applicants (→ continues in the posting-manager review journey) |
| **Thoughts** | "Now I wait for applications — and this time they come *here*, not my email." |
| **Emotion** | 🙂 Settled — closed loop |
| **This is the seam to the other journey** | Create (this map) → exists → [review/shortlist/close](journey-map-posting-manager-r1.md) |

---

## Critical Moments

| Moment | Stage | What happens |
|---|---|---|
| ⭐ Aha | Stage 3 — Preview | Manager sees the officer-facing view before publishing; control OTG never gave them |
| 🔑 Moment of truth | Stage 1 — Trigger | If it's unclear whether this replaces OTG, they dual-post or revert. Trust dies here. |
| ⚠️ Churn trigger | Stage 2 — Authoring | If the form is heavier than OTG's with no visible payoff, they resist adoption |
| ⚠️ Churn trigger | Stage 4 — Publish | An opaque or slow approval gate recreates the exact OTG pain they're escaping |

---

## Prioritised Build (what stage 1a actually requires)

**Must-have (the form doesn't work without these):**
1. Creation form with structured fields per posting type (the data model)
2. Officer-view preview (the aha; also the quality mechanism)
3. Publish → appears in listing (the core loop)
4. Agency-scoped auth — a manager posts only for their own agency

**High-value:**
5. Per-type templates (reduce authoring friction vs OTG)
6. Inline validation (required fields, closing-date sanity)
7. Edit / unpublish an existing posting

**Deferable to R2:**
8. Approval/review workflow (if agency policy needs it — confirm)
9. Scheduled future go-live
10. Applicant competency filter (the persona's most-wanted — but it's a review-side feature)

---

## Scope Concerns (must resolve before grooming)

1. **Native form vs ATS-owned creation (C1).** If the ATS (World A) owns posting creation, this native-form journey is replaced by an ATS authoring flow. **This map assumes World B (OTEP-native).** The ATS decision rewrites it. Resolve C1 first.
2. **Is there an approval gate?** Government posting often needs HR sign-off before going public. If so, stage 4 needs an approval sub-flow — a meaningful build addition. Confirm with a pilot agency (WSG/PA/MSF).
3. **OTG dual-posting during transition.** If pilot agencies still post some roles in OTG and some in CareerCompass, officers see a split. Decide: hard cut-over for pilot agencies, or parallel run? This is a change-management decision, not just technical.
4. **Who can post?** One HR manager per agency, or many? Role/permission model needed. Affects the auth scope.

---

## So What

Native creation's value isn't "a nicer form than OTG" — OTG's form is fine. It's **closing the loop**: post, receive, review, and close all in one system instead of OTG-plus-email-plus-spreadsheet. The aha is the preview (stage 3); the risk is making authoring feel heavier than OTG with the payoff hidden downstream.

But the honest headline: **this is a net-new build with four unresolved scope questions, landing in R1 on top of native apply and the seam.** The journey is mappable; whether it's *buildable* in the R1 window is the capacity question — see the capacity reality-check.

---

*Living document — rewritten if C1 resolves to ATS-owned creation (World A). Created 2026-06-02 as the first discovery pass on the creation lane.*  
*Source: Persona 3 (Posting Manager), ATS-pivot discovery idea #7, end-to-end blueprint stage 1a.*
