# UI Brief Prompt — Clickable Prototype Handoff

Use when you need to hand off a screen idea to Amber (design) or Claude Code (build). Forces you to be specific before the conversation, not during it.

---

## Prompt (paste into Claude Code or share with Amber)

```
Build a clickable prototype for the following screen.

**Screen name:**
[e.g. Opportunity Listing Page]

**User and goal:**
[e.g. Public service officer wants to browse available mobility opportunities and shortlist ones to explore]

**Entry point:**
[How the user arrives here — e.g. "Lands here after logging in via Singpass"]

**What the user sees:**
[Describe the layout — e.g. "A list of opportunity cards, each showing: title, agency, type badge (STIP/Gig/SJR/C@G), closing date, one-line description. A filter bar at the top with: opportunity type, agency, closing date range."]

**Key interactions:**
- [e.g. Clicking a card opens the opportunity detail page]
- [e.g. Applying a filter re-renders the list without page reload]
- [e.g. "Closing soon" badge appears if closing_date ≤ 7 days away]

**Edge cases to handle:**
- [e.g. Empty state: no results matching filters → show "No opportunities found" with a reset filters CTA]
- [e.g. formsg_url is null → hide the Apply button, show "Applications closed"]
- [e.g. Loading state while data fetches]

**What this is NOT:**
- [e.g. Not a final design — just enough to test the flow]
- [e.g. No authentication logic needed in the prototype]

**Success for this prototype:**
A user can complete [task] without asking any questions. We'll test with [who] by [when].

**Design reference:**
[Link to Figma file or describe the visual style — e.g. "Match the existing OTEP design system: Segoe UI, blue primary #0052CC, card-based layout"]
```

---

## Tips

- Fill in every field before handing off. Gaps become design decisions made by the wrong person.
- "What this is NOT" is the most important section — it prevents scope creep in the prototype.
- If you can't fill in "edge cases", you haven't thought through the AC yet. Go back to the story.
- For Claude Code handoffs: add the tech stack to the prompt (e.g. "React, Tailwind, mock JSON data").
