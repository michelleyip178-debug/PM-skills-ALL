# Personal OS — Setup Audit

What's left to set up in this OS, ranked by leverage. Captured 2026-05-06, updated 2026-05-07.

The structure is in place. Core content is now populated. Remaining work is incremental.

---

## 1. Populate `tasks/active.md` with this sprint's commitments

**Status:** Done (May 7, updated May 11). Sprint 1 tasks, blockers, waiting-on, and completed items are live.

## 2. Connect the team's source-of-truth tool

**Status:** Blocked by GovTech managed settings. MCP servers not currently allowed.
**Workaround:** Tasks tracked manually in `tasks/active.md`. Calendar shared via screenshot.
**To revisit:** If IT opens MCP access, connect Linear and Google Calendar first.

## 3. Harmonize `/weekly-update` and `/meeting-prep` to PM-mode

**Status:** Not started. `/daily` is already PM-mode (the old `standup` skill was merged into it on May 11).
**Why:** Same shape across all three — drive outcomes, recommend over present, build stakeholder influence, scope-creep watch. Otherwise I'll have one PM-mode skill and two BA-mode ones.

## 4. Fill in People stubs incrementally

**Status:** Partially done (May 11). Adrian, Pow Hwee, Amber have "What they care about" and "Recent context" filled. Jace, Leo, Thomas have basic info. Communication style TODOs remain — fill after 1:1s.

## 5. Decide on a decision log

**Status:** Done (May 11). Canonical log is `context/decisions-log.md` with 11 entries. Project-level decision-log was deprecated and deleted. Projects reorganised May 11: `otep-opportunities/` + `otep-wog-ad-login/` merged into `otep-mvp/`.

## 6. Collapse the sprint-scope files (do at the next sprint boundary)

**Why:** "Which stories are in sprint N" had no owner — it was restated in six docs that drifted (`sprint-allocation.md`, `sprint-calendar.md`, `story-readiness.md`, `sprint-checklists.md`, `story-id-map.md`, plus generated briefs in `outputs/`); the May 11 reorg only landed in some. On May 11 we made `projects/sprint-allocation.md` the single source of truth and synced everyone's *Sprint 2* statements to it (5-story listing hub; ringfencing/apply-redirects/auth-polish → Sprint 3). The structural fix — so they can't drift again — is to stop the other docs carrying the scope fact at all.

**Status:** Partial. Source-of-truth declared and Sprint 2 synced (May 11). Structural collapse pending — do it during the sprint-boundary workflow.

**Remaining steps:**
1. **Merge `projects/otep-mvp/sprint-checklists.md` into `tasks/story-readiness.md`** — one board per story: pipeline stage (Draft → Groom-ready → DoR met → Committed) + DoR-blocker status. Delete `sprint-checklists.md`.
2. **Anchor the DoR-blocker tracking to the team's official Story DoR**, not a home-grown list: *prioritised & sprint-sized · all platform subtasks incl. test cases identified & created · UI/UX designed & linked to all AC · feature flag designed with entry point · API contract identified & documented* (5 ✓/✗ columns per story). Epic DoR is the longer separate checklist — keep it for epics.
3. **Strip the per-sprint "Ships:" lists out of `context/sprint-calendar.md`** — keep dates, ceremonies, holidays only.
4. **Strip the "Sprint N scope" declarations out of the story-group files** (`projects/otep-mvp/stories/filters.md`, `auth.md`, etc.) — they own AC content; sprint assignment is `sprint-allocation.md`'s call. Each links to it.
5. **`story-id-map.md`** keeps its Sprint column but it *mirrors* `sprint-allocation.md` (already noted there as of May 11).
6. **Reconcile the downstream sprint IDs** (Sprints 4–11) in `sprint-allocation.md` against `story-id-map.md` — left as a provisional sketch on May 11.
7. **Archive the stale generated briefs** in `outputs/` (`sprint-2-draft-*`, duplicate `sprint-plan-brief-*`) — they're disposable; they cite the plan, don't compete with it.
8. **Update `/groom-prep`'s scorecard** so "What's blocking" points at which of the 5 DoR criteria isn't met, not a free-form note.

**Result:** scope lives in `sprint-allocation.md`; readiness lives in `story-readiness.md`; story content lives in the story files; dates live in the calendar. Nothing carries a fact owned elsewhere.

---

## What's NOT a blocker

- **Remaining people TODOs** (communication style, cadence) — fill after 1:1s and interactions.
- **Reference content TODOs** (company.md detail, okr-history.md) — reference, not load-bearing.
- **Workflow placeholders** (stakeholder-preferences.md, gather-metrics.md) — needed when running that workflow, not before.

---

## Open questions

- Want to harmonize `/weekly-update` and `/meeting-prep` to PM-mode now, or leave them?
- Any plans to put this OS on GitHub? (Privacy implications worth thinking through given GovTech context.)

---

*Revisit at the end of Sprint 1 (May 16) to check what's landed.*
