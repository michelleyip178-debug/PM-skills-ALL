# Opportunities Hub — Lo-Fi Figma Wireframe Outline
**Date:** 2026-05-26  
**Epic:** OTEP Epic 4 — Opportunity Discovery  
**Scope:** Listing page · Detail page · Apply flows  
**Fidelity:** Lo-fi wireframe (grey-box, no colour, placeholder text)  
**For:** Amber to build Figma frames / Michelle to validate flow logic before design

---

## 1. Frame Inventory

| Frame ID | Screen name | Stories covered |
|---|---|---|
| F-01 | Listing — Default (all results) | OTEP-85, OTEP-127 |
| F-02 | Listing — Filtered + Search active | OTEP-86, OTEP-317, OTEP-318 |
| F-03 | Listing — Empty state (no results) | OTEP-268 |
| F-04 | Detail — STIP / Gig / Internal Job | OTEP-128, OTEP-129, OTEP-319 |
| F-05 | Detail — SJR | OTEP-128, OTEP-132 |
| F-06 | Detail — Careers@Gov | OTEP-88, OTEP-89 |
| F-07 | Apply overlay — FormSG redirect warning | OTEP-319 |
| F-08 | Apply overlay — missing FormSG link (error) | OTEP-87 |
| F-09 | Apply overlay — C@G redirect warning | OTEP-89 |
| F-10 | Apply overlay — OTG redirect warning | OTEP-132 |
| F-11 | Deep-link landing — Closed opportunity | OTEP-129 |
| F-12 | Deep-link landing — Not authorised (ringfenced) | OTEP-133 |

---

## 2. Prototype Connection Map

```
[F-01 Listing default]
  ├─ Card click ───────────────────────────────► [F-04 Detail — STIP/Gig/InternalJob]
  ├─ Card click (SJR) ─────────────────────────► [F-05 Detail — SJR]
  ├─ Card click (C@G) ─────────────────────────► [F-06 Detail — C@G]
  ├─ Apply filter / type checkbox ─────────────► [F-02 Listing filtered]
  └─ Search returns zero results ──────────────► [F-03 Listing empty]

[F-02 Listing filtered]
  ├─ "Clear all" click ────────────────────────► [F-01 Listing default]
  └─ Card click ───────────────────────────────► [F-04 / F-05 / F-06]

[F-04 Detail — STIP/Gig/InternalJob]
  ├─ "Apply" click ────────────────────────────► [F-07 FormSG overlay]
  ├─ "Apply" (formsg_url null) ────────────────► [F-08 Missing link error]
  └─ "← Back" ─────────────────────────────────► [F-01/F-02 listing, preserved state]

[F-05 Detail — SJR]
  ├─ "Apply via OTG" click ────────────────────► [F-10 OTG redirect overlay]
  └─ "← Back" ─────────────────────────────────► [F-01/F-02 listing, preserved state]

[F-06 Detail — C@G]
  ├─ "Apply via Careers@Gov" click ────────────► [F-09 C@G redirect overlay]
  └─ "← Back" ─────────────────────────────────► [F-01/F-02 listing, preserved state]

[F-07 FormSG overlay]
  ├─ "Continue" ───────────────────────────────► (external tab — no Figma frame)
  └─ "Cancel" ─────────────────────────────────► [F-04 Detail, overlay dismissed]

[F-08 Missing link error]
  └─ "OK" / close ─────────────────────────────► [F-04 Detail, overlay dismissed]

[F-09 C@G redirect overlay]
  ├─ "Continue" ───────────────────────────────► (external tab — no Figma frame)
  └─ "Cancel" ─────────────────────────────────► [F-06 Detail, overlay dismissed]

[F-10 OTG redirect overlay]
  ├─ "Continue" ───────────────────────────────► (external tab — no Figma frame)
  └─ "Cancel" ─────────────────────────────────► [F-05 Detail, overlay dismissed]

[Deep-link entry points]
  ├─ Closed opportunity URL ───────────────────► [F-11 Closed state]
  └─ Ringfenced / ineligible URL ──────────────► [F-12 Not authorised]

[F-11 Closed state]
  └─ "Browse opportunities" ───────────────────► [F-01 Listing default]

[F-12 Not authorised]
  └─ "Browse opportunities" ───────────────────► [F-01 Listing default]
```

---

## 3. Frame Specs

### F-01 — Listing page (Default)

**Canvas size:** 1440 × 900 (desktop)

**Layout (top → bottom):**

```
┌─────────────────────────────────────────────────────────────────┐
│  OTEP Nav bar                                                    │
│  [Logo]   My Development | Opportunities [active]   [Avatar]    │
├─────────────────────────────────────────────────────────────────┤
│  Page header                                                     │
│  H1: "Opportunities"                                             │
│  Body: "Discover short-term postings, gigs, and roles           │
│         across the public service."                              │
├────────────────────┬────────────────────────────────────────────┤
│  LEFT SIDEBAR      │  MAIN CONTENT AREA                         │
│  [Search bar]      │                                            │
│  Placeholder:      │  Row 1: [Card] [Card] [Card]               │
│  "Search by role,  │                                            │
│   agency or        │  Row 2: [Card] [Card] [Card]               │
│   keyword"         │                                            │
│  [Clear icon]      │  Row 3: [Card] [Card] [Card]               │
│                    │                                            │
│  ── Filter by type │  Row 4: [Card] [Card] [Card]               │
│  ☐ STIP            │                                            │
│  ☐ Gig             │  Row 5: [Card] [Card] [Card]               │
│  ☐ SJR             │                                            │
│  ☐ Internal Job    │  ─────────────────────────────────────     │
│  ☐ Careers@Gov     │  Pagination: [← Prev] Page 1 of 5 [Next →]│
│                    │                                            │
│  ── Filter by      │                                            │
│     category       │                                            │
│  [TBC — Sprint 3]  │                                            │
└────────────────────┴────────────────────────────────────────────┘
```

**Opportunity card anatomy (each card):**
```
┌────────────────────────────────┐
│  [Type badge]  e.g. "STIP"     │  ← pill label, no colour reliance
│                                │
│  [Opportunity Title]           │  ← max 2 lines, ellipsis overflow
│  Max 2 lines of text here      │
│                                │
│  Posted by: [Agency Name]      │
│  Duration: [X weeks / months]  │
│                                │
│  [Closing soon] ← only if ≤7d  │
└────────────────────────────────┘
```

**Notes for Amber:**
- 3-column grid, 16px gutter
- Pinned "Internal Jobs" cards go at top row — add a "Pinned" indicator (e.g. pin icon, no colour)
- C@G cards: add "Careers@Gov" label visually distinct from type badge
- Type badge must distinguish opportunity type without colour alone — use shape or label prefix
- Card hover state: border or shadow change (clickable affordance)
- Sort: posting date descending (no sort toggle in MVP)

**Annotations:**
- `A1` — Ringfencing applied on login; officer only sees eligible listings. No UI indicator needed on cards.
- `A2` — Auth gate: unauthenticated users never reach this screen (login redirect handles it upstream).

---

### F-02 — Listing page (Filtered + Search active)

**Differs from F-01:**
- One or more filter checkboxes checked (e.g. ☑ STIP, ☑ Gig)
- Search bar contains query text (e.g. "data analytics")
- Active filter pills appear above card grid: `STIP ✕` `Gig ✕` `"data analytics" ✕`
- "Clear all" link visible to the right of filter pills
- Card grid shows filtered results only
- Tooltip on filter type label — "?" icon next to e.g. "STIP" triggers tooltip explaining opportunity type

**Notes for Amber:**
- Filter pills strip should sit between page header and card grid
- "Clear all" right-aligned in pill row
- Tooltip: small popover, 1–2 sentences max per type

---

### F-03 — Listing page (Empty state)

**Differs from F-01:**
- Card grid area replaced with empty state block

**Empty state block:**
```
┌──────────────────────────────────────────┐
│                                          │
│    [Illustration placeholder — box]      │
│                                          │
│    "No opportunities available           │
│     right now."                          │
│                                          │
│    "Try adjusting your filters or        │
│     check back later."                   │
│                                          │
└──────────────────────────────────────────┘
```

- Pagination hidden
- Sidebar filters still shown so officer can reset

**Notes for Amber:** Design empty state illustration; keep consistent with OTEP design system.

---

### F-04 — Detail page (STIP / Gig / Internal Job)

**Canvas size:** 1440 × 900

```
┌─────────────────────────────────────────────────────────────────┐
│  OTEP Nav bar                                                    │
├─────────────────────────────────────────────────────────────────┤
│  ← Back to Opportunities                                        │
├───────────────────────────────────────┬─────────────────────────┤
│  MAIN CONTENT (left ~70%)             │  STICKY RIGHT PANEL     │
│                                       │                         │
│  [Type badge]                         │  ┌───────────────────┐  │
│  H1: Opportunity Title                │  │ Application closes │  │
│                                       │  │ DD MMM YYYY        │  │
│  Posted by: [Agency Name]             │  │                    │  │
│  Duration: [Start – End dates]        │  │ [Apply] ← primary  │  │
│  Application closes: [date]           │  │  CTA button        │  │
│                                       │  └───────────────────┘  │
│  ── About this opportunity ──         │                         │
│  [Description text block]             │                         │
│  Field: Value                         │                         │
│  Field: Not specified  ← if null      │                         │
│                                       │                         │
│  ── What you'll develop ──            │                         │
│  · [Competency 1]                     │                         │
│  · [Competency 2]                     │                         │
│  · [Competency 3]                     │                         │
│  (No match ratio — R1)                │                         │
│                                       │                         │
└───────────────────────────────────────┴─────────────────────────┘
```

**CTA label:** "Apply" (opens FormSG overlay → F-07)  
**If formsg_url null:** CTA replaced by disabled state → F-08  
**"Closing soon" label:** if ≤ 7 days to close, show inline badge near closing date

**Notes for Amber:**
- Apply CTA must be visible without scrolling — sticky right panel handles this
- "Not specified" is the fallback text for any null mandatory field — style it distinctly (greyed text)

---

### F-05 — Detail page (SJR)

**Same layout as F-04, two differences:**

1. **No Apply button.** Right panel shows:
   ```
   ┌──────────────────────────────────┐
   │  To apply, visit OTG directly.   │
   │                                  │
   │  [Apply via OTG]  ← secondary    │
   │                     CTA          │
   └──────────────────────────────────┘
   ```
   CTA triggers F-10 (OTG redirect overlay).

2. **Section label change:** "What you'll develop" section may still appear if competency data available.

**Annotation:** SJR has no FormSG apply in MVP. The redirect to OTG is the application path (OTEP-132, sprint TBC).

---

### F-06 — Detail page (Careers@Gov)

**Same layout as F-04, differences:**

1. **Type badge:** "Careers@Gov" label visible
2. **CTA label:** "Apply via Careers@Gov" — triggers F-09 (C@G redirect overlay)
3. **No FormSG, no OTG apply path**
4. **Right panel:**
   ```
   ┌──────────────────────────────────┐
   │  [Apply via Careers@Gov] ← CTA  │
   └──────────────────────────────────┘
   ```

**Annotation:** If C@G listing expires after OTEP ingestion, the resulting error is on C@G's side — OTEP shows no error state for this.

---

### F-07 — Apply overlay (FormSG redirect warning)

**Type:** Modal overlay on F-04

```
┌──────────────────────────────────────────────────┐
│                                                  │
│  You're leaving OTEP                             │
│                                                  │
│  You'll be taken to FormSG to complete your      │
│  application. The form opens in a new tab.       │
│                                                  │
│  [Cancel]              [Continue to FormSG →]    │
│                                                  │
└──────────────────────────────────────────────────┘
```

- "Continue to FormSG" → opens external tab (no Figma frame), closes modal
- "Cancel" → dismisses modal, returns to F-04

**Notes for Amber:** Modal is centred, darkened scrim behind. Keep copy short — officer has already decided to apply.

---

### F-08 — Apply error (missing FormSG link)

**Type:** Disabled CTA state + inline message on F-04 (not a modal)

```
[Apply form unavailable]  ← disabled button, greyed

Below button:
"Application form unavailable — contact [Agency Name] directly."
```

No modal, no redirect. Static inline fallback.

---

### F-09 — Apply overlay (C@G redirect warning)

**Type:** Modal overlay on F-06

```
┌──────────────────────────────────────────────────┐
│                                                  │
│  You're leaving OTEP                             │
│                                                  │
│  You'll be taken to Careers@Gov to complete      │
│  your application. The listing opens in a        │
│  new tab.                                        │
│                                                  │
│  [Cancel]          [Continue to Careers@Gov →]   │
│                                                  │
└──────────────────────────────────────────────────┘
```

Same pattern as F-07.

---

### F-10 — Apply overlay (OTG redirect warning)

**Type:** Modal overlay on F-05

```
┌──────────────────────────────────────────────────┐
│                                                  │
│  You're leaving OTEP                             │
│                                                  │
│  You'll be taken to OTG to complete your         │
│  application. You will need to re-login on OTG.  │
│                                                  │
│  [Cancel]              [Continue to OTG →]       │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

### F-11 — Deep-link landing (Closed opportunity)

**Standalone full-page state (no listing visible)**

```
┌─────────────────────────────────────────────────┐
│  OTEP Nav bar                                   │
├─────────────────────────────────────────────────┤
│                                                 │
│  [Icon placeholder — closed/expired]            │
│                                                 │
│  "This opportunity is no longer available."     │
│                                                 │
│  "The posting you followed may have closed      │
│   or been removed."                             │
│                                                 │
│  [Browse open opportunities →]  ← links to F-01│
│                                                 │
└─────────────────────────────────────────────────┘
```

---

### F-12 — Deep-link landing (Not authorised / ringfenced out)

**Standalone full-page state**

```
┌─────────────────────────────────────────────────┐
│  OTEP Nav bar                                   │
├─────────────────────────────────────────────────┤
│                                                 │
│  [Icon placeholder — lock / restricted]         │
│                                                 │
│  "This opportunity isn't available to you."     │
│                                                 │
│  "It may be ringfenced to specific agencies     │
│   or grades. Browse opportunities you're        │
│   eligible for below."                          │
│                                                 │
│  ── Opportunities you may like ──               │
│  [Card] [Card] [Card]  ← 3 alternative cards   │
│                                                 │
│  [Browse all opportunities →]  ← links to F-01 │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 4. Figma Build Checklist (for Amber / Michelle)

### Setup
- [ ] Create new Figma page: "Opportunities Hub — Lo-Fi Wireframe"
- [ ] Set frame size: 1440 × 900 (Desktop)
- [ ] Use 12-column grid (80px columns, 16px gutters, 120px margins)
- [ ] Colour palette: grey only — `#F5F5F5` background, `#E0E0E0` card fill, `#333` text, `#999` placeholder text

### Frames to build (in order)
- [ ] F-01 — Listing default (build the card component first, reuse across frames)
- [ ] F-02 — Listing filtered (duplicate F-01, modify)
- [ ] F-03 — Listing empty state (duplicate F-01, swap card grid for empty block)
- [ ] F-04 — Detail: STIP/Gig/Internal Job
- [ ] F-05 — Detail: SJR (duplicate F-04, modify CTA)
- [ ] F-06 — Detail: C@G (duplicate F-04, modify CTA + badge)
- [ ] F-07 — FormSG overlay (overlay component on F-04)
- [ ] F-08 — Missing link error (inline state on F-04 — no separate frame needed)
- [ ] F-09 — C@G overlay (duplicate F-07, modify copy)
- [ ] F-10 — OTG overlay (duplicate F-07, modify copy)
- [ ] F-11 — Closed opportunity
- [ ] F-12 — Not authorised

### Prototype connections (use Figma Prototype panel)
Wire each connection from the map in Section 2. Key connections:
- Card → Detail (use "On Click → Navigate to")
- Filter checkbox → F-02 (On Click → Navigate to)
- Apply button → Overlay (On Click → Open overlay)
- Back button → Listing (On Click → Back / Navigate to)
- Deep-link states: set as separate start flows in Figma

### Annotations layer
Add a separate "Annotations" frame layer. Reference the `A1`, `A2` notes in this doc — paste them as sticky notes beside relevant frames.

---

## 5. What This Prototype Does NOT Cover (Out of MVP scope)

| Excluded | Reason |
|---|---|
| Login / SSO screen | Upstream — handled by WOG AD / Keycloak |
| Competency match ratio | R1 — deferred |
| Save for later | R1 — deferred |
| Supervisor endorsement UI | R1 — deferred |
| FormSG form itself | External — owned by FormSG |
| Notification flows | R1 — deferred |
| My Applications view | Not in Epic 4 scope |
| Pagination (functional) | OTEP-267 — wire as static "Page 1 of 5" label |
| Category filter (full) | OTEP-318 — ACs TBC, placeholder filter in sidebar only |
