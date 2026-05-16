# Plan: Full OS Cleanup

## Context

Projects/ was just reorganised (otep-opportunities + otep-wog-ad-login merged into otep-mvp). That left ~17 stale path references scattered across the OS. Sprint 1 ends May 16 — good time to clean everything before Sprint 2.

## Audit Summary

| Layer | Health | Issues |
|-------|--------|--------|
| context/ | Clean | No stale refs |
| tasks/ | Clean | backlog.md "Last reviewed" date is May 7 |
| projects/ | Clean (just reorganised) | No issues |
| .claude/ | Clean | CLAUDE.md already updated |
| areas/ | Stale refs | 3 files reference old project paths |
| resources/ | Stale refs + stub | 2 files reference old paths; okr-history.md is empty |
| outputs/ | Current | All from today — archive after May 16 |
| archive/ | Clean | Structure working |
| README.md | Stale | Folder structure + links reference old project paths |
| evidence-tracker | Stale | 6 artifact links point to deleted folders |
| os-setup-audit | Stale | References "otep-opportunities/" as if it still exists |

## Changes

### 1. Fix README.md (5 stale references)

**Lines 53-57:** Folder structure lists `otep-opportunities/` and `otep-wog-ad-login/` as separate folders.
- Replace with `otep-mvp/` single entry

**Lines 232-240:** Active projects table + key files links.
- Merge two project rows into one OTEP MVP row
- Fix PRD link: `projects/otep-opportunities/prd.md` → `projects/otep-mvp/prd-opportunities.md`
- Fix PRD link: `projects/otep-wog-ad-login/prd.md` → `projects/otep-mvp/prd-auth.md`
- Fix scoping gaps link: `projects/otep-opportunities/scoping-gaps-tracker.md` → `projects/otep-mvp/scoping-gaps-tracker.md`

### 2. Fix evidence-tracker.md (6 broken artifact links)

All in `projects/pm-conversion/evidence-tracker.md`:
- Line 17: `../otep-opportunities/prd.md` → `../otep-mvp/prd-opportunities.md`
- Line 18: `../otep-opportunities/prd.md` → `../otep-mvp/prd-opportunities.md`
- Line 29: `../otep-opportunities/categorisation-research.md` → `../otep-mvp/research/categorisation-research.md`
- Line 30: `../otep-opportunities/categorisation-research.md` → `../otep-mvp/research/categorisation-research.md`
- Line 43: `../otep-opportunities/scoping-gaps-tracker.md` → `../otep-mvp/scoping-gaps-tracker.md`
- Line 44: `../otep-opportunities/prd.md` → `../otep-mvp/prd-opportunities.md`
- Line 55: `../otep-opportunities/user-stories.md` → `../otep-mvp/stories/index.md`

### 3. Fix areas/product-ops/product.md (2 stale links)

- Line 30: `../../projects/otep-opportunities/prd.md` → `../../projects/otep-mvp/prd-opportunities.md`
- Line 35: `../../projects/otep-wog-ad-login/prd.md` → `../../projects/otep-mvp/prd-auth.md`

### 4. Fix areas/pm-growth/day-in-the-life.md (3 stale references)

- Lines 32-33: Replace two project folder references with single `projects/otep-mvp/`
- Line 133: Replace `projects/otep-opportunities/` with `projects/otep-mvp/`

### 5. Fix resources/workflows/story-pipeline/workflow-spec.md (1 stale reference)

- Line 116: `projects/otep-opportunities/user-stories.md` → `projects/otep-mvp/stories/index.md`

### 6. Fix resources/os-setup-audit.md (1 stale reference + content refresh)

- Line 30: Update "Project-level decision-log.md in otep-opportunities/" to reflect new merged structure
- Add a new section noting the May 11 reorganisation (otep-mvp merge)

### 7. Update tasks/backlog.md review date

- Line 75: "Last reviewed: 2026-05-07" → "Last reviewed: 2026-05-11"

### 8. Archive or flag okr-history.md

`resources/okr-history.md` is an empty template with "To Populate" checklist. Two options:
- Keep as template (it's not harmful, just empty)
- Move to archive if not planning to use this quarter

**Recommendation:** Keep it — it's part of the quarterly-planning workflow. Not stale, just not yet populated.

## Files to modify (8 files)

1. `README.md` — folder structure + project links
2. `projects/pm-conversion/evidence-tracker.md` — 6 artifact links
3. `areas/product-ops/product.md` — 2 PRD links
4. `areas/pm-growth/day-in-the-life.md` — 3 project path references
5. `resources/workflows/story-pipeline/workflow-spec.md` — 1 reference
6. `resources/os-setup-audit.md` — 1 reference + refresh
7. `tasks/backlog.md` — review date
8. `GOALS.md` — no changes (TODOs are intentional living-doc scaffolds)

## What NOT to change

- **Stakeholder profile TODOs** — intentional "fill-as-you-go" pattern per os-setup-audit.md
- **GOALS.md personal dev sections** — living doc, not stale
- **product-ops/company.md empty sections** — skeleton for future, not blocking anything
- **outputs/ files** — all from today, archive after Sprint 1 ends May 16
- **okr-history.md** — empty template, part of quarterly-planning workflow, leave it

## Verification

After all edits:
```
grep -rn "otep-opportunities\|otep-wog-ad-login" . --include="*.md" | grep -v ".claude/plans/" | grep -v "archive/" | grep -v "otep-vision-stories/"
```
Should return zero results (excluding archive which may reference old names in historical context).
