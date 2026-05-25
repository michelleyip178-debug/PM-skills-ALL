## Mid-Sprint Review — 25 May 2026 | Sprint 2, Week 2

> Updated after Jira sync at ~11:00 SGT — 4 story changes detected.

### Sprint Health
**Status:** 🟡 At risk

**Sprint goal:** Officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — Listing → Detail end-to-end.

**Stories:** 5 Done · 7 In Progress · 3 QA · 10 Backlog (25 total)

**Why 🟡 and not 🔴:** OTEP-85 (sprint goal 1) moved to In Progress since the last sync — the team is moving. Léo started OTEP-334 (backend detail endpoint) and OTEP-313 (OTG ingest table), signalling the OTEP-128 chain is being set up. OTEP-128 itself is still Backlog with no assignee, but the backend work feeding it is live. Achievable if the team commits today — not achievable if decisions slip to Wednesday.

---

### Current Board State

| Status | Stories |
|---|---|
| In Progress (7) | OTEP-325, OTEP-326 (Thomas), OTEP-322 (Rathika), **OTEP-85** (no assignee), **OTEP-268** (no assignee), **OTEP-313** (Léo), **OTEP-334** (Léo) |
| QA (3) | OTEP-170 (Thomas), OTEP-320 (Léo), OTEP-303 (Pow Hwee) |
| Done (5) | OTEP-193, OTEP-288, OTEP-296, OTEP-252, OTEP-194 |
| Backlog (10) | OTEP-128 ⚠️, OTEP-267, OTEP-129, OTEP-295, OTEP-314, OTEP-316, OTEP-327, OTEP-332, OTEP-276, OTEP-289 |

---

### Blockers to Raise in the Session

| Blocker | Story affected | Owner | Action needed |
|---|---|---|---|
| OTEP-85 In Progress but no parent assignee | OTEP-85 | — | Assign in the session — who owns the parent story to Done? |
| OTEP-170 (layout) and OTEP-320 (real DB) still in QA | OTEP-85 | Thomas / Léo | Are these merging today? OTEP-85 can't close without both sub-tasks merged |
| OTEP-268 In Progress but no assignee | OTEP-268 | — | OTEP-325/326 sub-tasks are Thomas's — confirm who closes the parent |
| OTEP-128 still Backlog, no assignee, 4 days left | OTEP-128 | — | Either assign + commit today, or formally carry to Sprint 3 |
| OTEP-295 still Backlog alongside OTEP-334 | OTEP-128 | Léo | OTEP-334 and OTEP-295 are separate stories both feeding OTEP-128. Confirm sequencing: does OTEP-334 finish before OTEP-295 starts, or are they parallel? |
| OTEP-314 and OTEP-327 (Thomas FE detail page work) still Backlog | OTEP-128 | Thomas | Thomas can't start these until OTEP-325/326 ship. Ask: when does that happen? |

---

### Scope Creep Flags

- **OTEP-334 added mid-sprint** — "Backend endpoint for opportunity detail" (Léo, In Progress). Confirmed separate from OTEP-295. Both feed OTEP-128. Not in original sprint commitment — confirm sequencing with Léo.
- **OTEP-332 added mid-sprint** — "Implement shared reference data repository" (Pow Hwee, Backlog). Not sprint goal work. Blocks Imelda's squad MR !44. Recommend carry to Sprint 3 — ask Pow Hwee explicitly.
- **OTEP-322 (Playwright E2E framework)** — Rathika Ramalingam, In Progress. Not in original committed story list. Confirm this was a deliberate addition and has a finishing condition before Friday.

---

### PM Decisions Needed Before Sprint End

| Decision | Waiting on Michelle for | By when |
|---|---|---|
| Cut-line: what carries to Sprint 3? | Propose the list (see below) and get confirmation in the session today | Today — end of Mid-Sprint Review |
| OTEP-128 go/no-go | If no assignee and OTEP-334 isn't finishing the backend today → formally mark as Sprint 3 carry-over. Don't leave it ambiguous. | Today EOD |
| OTEP-128 assignee — still unknown | No one has claimed ownership of the parent sprint goal story. Either assign it in the session today or formally carry to Sprint 3. The backend work (OTEP-334, OTEP-295) is moving; the FE work (OTEP-314, OTEP-327) and the parent story have no owner. | Today — do not leave the session without a name or a carry decision |
| OTEP-276 spike removal | Still showing in Backlog. PM to remove from Sprint 2 board in Jira. | Today |
| Open item #23 closure | OTEP-193 Done confirms data model built. Confirm with Pow Hwee: does it hold for OTG + C@G? If yes, close. | Today in session |
| Open item #14 closure | OTEP-194 spike confirmed FormSG pre-fill via URL params. PM to formally close #14. | Today |
| Sprint 3 board prep | OTEP-192, OTEP-271, OTEP-203, OTEP-86, OTEP-317, OTEP-87 still not added to Sprint 3 board in Jira | Before Thu 29 May (Sprint Planning) |

---

### Recommended Cut-Line (propose in session, not after)

| Story | Recommendation | Rationale |
|---|---|---|
| OTEP-85 | Protect — sprint goal | In Progress, backend work (OTEP-313, OTEP-334) moving. Needs OTEP-170/320 to merge. |
| OTEP-128 | Carry to Sprint 3 | Still Backlog, no assignee. Thomas can't start FE work (OTEP-314/327) until OTEP-325/326 ship. Forcing it risks quality. |
| OTEP-268 | May complete | Sub-tasks OTEP-325/326 In Progress (Thomas). Parent needs assignee. If Thomas finishes both today, this can close. |
| OTEP-267 | Carry to Sprint 3 | Pagination — Thomas overloaded, not started |
| OTEP-129 | Carry to Sprint 3 | Open/closed badge — Thomas overloaded, not started |
| OTEP-332 | Carry to Sprint 3 | Mid-sprint addition, not sprint goal, splits Pow Hwee focus |

---

### Michelle's Key Question for the Session

> "OTEP-334 and OTEP-295 are both moving toward OTEP-128. The backend is being built. Who is picking up the parent story and the FE work — and if no one can commit today, do we formally carry OTEP-128 to Sprint 3?"

The backend chain is live but the front-end (OTEP-314, OTEP-327) and the parent story have no owner. A vague "we'll try" is not a decision. The session should end with either a name on OTEP-128 or a formal carry-over call.
