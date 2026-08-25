# OTEP-936: [CORE] LAND-06 - Course tile content and optional fields (OTEP-602)

**Status:** Done
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Account Account D — padmin2 ·  padmin2@cscollege.gov.sg  · password: Padmin@Cc2026 Where to look: all 30 of account D's “Recommended for you” tiles are full-data (every one has a provider and duration), so the no-provider tile does NOT appear in the landing swimlane. The course tile is the same component on the “Explore all courses” search results page, where the whole catalogue renders — verify the optional-field behaviour (combo b) there. Data gap: across the catalogue 91 are full and 33 have no provider; 0 have no duration (duration_hours is NOT NULL with a min of 0.02h), so combos (c)/(d) are not testable until such courses exist in the LEARN source. No data changes made. Test Steps Go to the  UAT site  and log in as D. On the landing page, look at a “Recommended for you” tile with the full set of information (course name, product type, provider, and duration all present) — e.g. “Gen Z Bootcamp” (H67HYB0) or “Risk Management in Government” (P33VDVD). Click “Explore all courses”, then locate a tile with no provider (duration present) — e.g. DL Prog for Playwright ALS (0.5h). (This combo appears in the catalogue/search, not in D's recommended swimlane.) Look for a tile with no duration (provider present). Look for a tile with no provider and no duration. Test Data (a) full data  — all 30 of D's recommended tiles are full-data (e.g. H67HYB0, P33VDVD); 91 across the catalogue. (b) no provider  — 33 in the catalogue, e.g.  DL Prog for Playwright ALS (0.5h) (c) no duration  — 0 courses (not testable). (d) no provider and no duration  — 0 courses (not testable). Expected Result Every tile shows Course name and Product type (always present). Provider and Duration each appear only when available and are omitted entirely when missing. Combo (a) is verifiable on D's landing swimlane; combo (b) on the Explore/search results page; combos (c)/(d) are not testable with the current data.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-18)
🎉 Looks good!

---

**Alan Lim** (2026-08-18)
ok but Recommended for you only 25 instead of 30

---
*Synced from Jira: 2026-08-25*
