# Archive Sprint Checkpoint

Archive outputs and a context snapshot at mid-sprint or end-of-sprint.

---

## Steps

### Step 1 — Determine sprint and checkpoint
Read `context/current-sprint.md` to get the sprint number.
Ask the user (or infer from sprint week): is this a **mid-sprint** or **end-sprint** archive?

### Step 2 — Create archive folder
Create: `outputs/archive/sprint-[N]/[checkpoint]/`
Where checkpoint is `mid-sprint` or `end-sprint`.

### Step 3 — Move output files
Move all files from `outputs/` (not archive/) into the checkpoint folder.
These are the briefs, dailies, and prep docs generated during this period.

### Step 4 — Snapshot context files
Copy (not move) the following into the checkpoint folder with a `snapshot-` prefix:
- `context/current-sprint.md` → `snapshot-current-sprint.md`
- `context/open-items.md` → `snapshot-open-items.md`
- `context/decisions-log.md` → `snapshot-decisions-log.md`
- `context/risks.md` → `snapshot-risks.md`

These are frozen records — the originals in context/ remain live for ongoing use.

### Step 5 — End-sprint only: reset context for next sprint
If this is an **end-sprint** archive:
- Clear the committed stories table in `context/current-sprint.md` (keep structure, blank the rows)
- Move resolved items in `context/open-items.md` from Open to Resolved with today's date
- Prompt Michelle to update sprint number, dates, and goal for the next sprint

### Step 6 — Confirm
Print a summary: what was archived, where it lives, and any next actions.

---

## Output format

No output file — this command modifies the workspace directly.
Print a confirmation summary to the console.

---

### Example structure after archiving:
```
outputs/archive/
└── sprint-12/
    ├── mid-sprint/
    │   ├── daily-2026-05-05.md
    │   ├── daily-2026-05-06.md
    │   ├── groom-prep-2026-05-06.md
    │   ├── snapshot-current-sprint.md
    │   ├── snapshot-open-items.md
    │   ├── snapshot-decisions-log.md
    │   └── snapshot-risks.md
    └── end-sprint/
        ├── daily-2026-05-12.md
        ├── sprint-plan-prep-2026-05-12.md
        ├── snapshot-current-sprint.md
        ├── snapshot-open-items.md
        ├── snapshot-decisions-log.md
        └── snapshot-risks.md
```
