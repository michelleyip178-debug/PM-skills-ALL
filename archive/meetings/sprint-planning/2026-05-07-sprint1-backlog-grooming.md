# Sprint Planning + Backlog Grooming — May 7, 2026

**Session:** 14:00–16:00, L11 Anson
**Sprint:** OTEP-Pathfinder Sprint 1 (May 4–18)
**Sprint Goal:** Login and navigate to Jobs and Opportunities

---

## Sprint 1 Progress Summary

We're at day 4 of 14. The agreed Sprint 1 scope is focused: **get login working end-to-end** and **clarify data dependencies** — not build the full opportunity experience.

| Track | Agreed Sprint 1 outcome | Status |
|-------|--------------------------|--------|
| Authentication (login e2e) | Basic login flow working — sign-in, token, session | In progress (keycloak + auth flow exploration) |
| Backend foundations | DB connection, ref table schema, baseline conventions | Done / QA |
| Opportunity listing | Skeleton/base layout only — no real data, filters, or search | Not started (waiting on design) |
| Data model & upstream deps | **Clarify and align** on job family, function model, competency bank — not build | Decision-stage |
| C@G / function filter | **Investigate approach** with Pow Hwee — not implement | Decision-stage |

**What this means for BOs:**
- Officers will be able to log in by end of sprint — on track.
- The opportunity listing will be a skeleton at most — real data and features are Sprint 2.
- Today's session is about **landing the decisions** that let Sprint 2 start building.

---

## Stories for Review

### 1. Login Authentication (OTEP-71)

**What officers get:** Log in with their gov.sg email via WOG AD. Stay logged in across pages. Get logged out after inactivity and can re-login smoothly.

**ACs to validate:**
- Only ESG and PSD officers can log in for MVP — is this still correct?
- Session expires after 30 min inactivity or 12 hours — are BOs comfortable with these thresholds?
- On relogin, user lands on profile page (not where they left off) — is this acceptable for MVP?

**Sprint 1 scope note:** Login UI will be minimal (placeholder, not polished). Functional, not final. Design polish comes later.

**Status:** Actively being built. On track for May 18.

---

### 2. Login Failure (OTEP-110)

**What officers get:** If login fails, they see a clear message explaining why and what to do next.

**ACs to validate:**
- "The reason for the login failure is provided for troubleshooting" — how specific? Do we expose technical errors, or keep it generic ("Something went wrong, try again")?
- Is there a support contact we should surface? Or just "contact your HR"?

**Scope recommendation:** Keep it simple for MVP — generic error + retry button. Detailed error codes are R1.

---

### 3. No Access / Deactivated User (OTEP-111)

**What officers get:** If they're not in the pilot group or their profile is deactivated, they see a clear "you don't have access" message instead of a confusing error.

**ACs to validate:**
- Pilot group = ESG + PSD. How do we define who's "in"? By agency code in POCDEX? Manual whitelist?
- Message: "Oops, you do not seem to have access at the moment. Please contact your HR for more information." — is this the confirmed copy?

**Business question for BOs:**
> Where does the pilot group list come from? Is it maintained by us or pulled from an existing system?

---

### 4. New Officer Account Creation (OTEP-72)

**What officers get:** When a new officer joins public service and logs in for the first time, their account is already there — no sign-up needed.

**ACs to validate:**
- Account created "instantaneously" via POCDEX push — is near-real-time acceptable (minutes), or does it truly need to be instant (sub-second)?
- Default view shows profile details + My Competency section — is this confirmed as the landing experience?

**Business question for BOs:**
> What happens if an officer logs in before POCDEX has pushed their record? (e.g., day-one onboarding, system delay) — show "no access" or show a "profile pending" state?

**Dependency:** POCDEX spike (OTEP-183) is in backlog — the team will investigate the integration pattern this sprint, but full implementation is Sprint 2+.

---

### 5. Opportunity Data — Decisions Needed (OTEP-192 + OTEP-193)

**Context:** Sprint 1 is about **deciding the approach**, not building the pipeline. The team agreed that real data, filters, and search are Sprint 2+. But Sprint 2 can only start building if we land these decisions now.

**Decisions to make today:**

**A. Data freshness — how stale can opportunity listings be?**
- Real-time sync (complex, higher infra cost)
- Daily sync (simpler, acceptable lag for MVP)
- Weekly (too stale?)

**My recommendation:** Daily sync for MVP. Real-time is R1.

**B. Careers@Gov ingestion method:**

| Option | What it means | Trade-off |
|--------|---------------|-----------|
| API | Real-time sync from C@G system | Cleanest, but requires C@G team to provide access |
| File export | Periodic data dump (daily/weekly) | Simple, but data can be stale |
| Scrape | Pull from C@G website | No dependency on C@G team, but fragile and may break |

**My recommendation:** Start OTG pipeline first (no dependencies, clear path). For C@G, push for API access as default; fall back to file export if C@G team can't support within our timeline. Decouple the two — one decision shouldn't block the other.

**C. Function filter / categorization:**
- The team agreed to **investigate, not implement** in Sprint 1.
- **Key issue discovered:** OTG and C@G use different taxonomies:
  - OTG = "Job Functions" (HR, Finance, IT, Policy, etc.)
  - C@G = Sectoral categorisation (Arts & Culture, Health & Social, Environment & Sustainability, etc.)
- These don't map 1:1. When we build the function filter, we need to decide: unified taxonomy, two separate filters, or pick one as master?
- Need to clarify with Pow Hwee: is taxonomy mapping feasible, or should we defer function filter to R1?

---

### 6. Listing Page Foundation (OTEP-170)

**What officers get:** The page where all opportunities will be displayed — the "hub" in Sprint 2.

**Sprint 1 scope:** Skeleton/base layout only. No user-facing functionality — just the structural shell.

**ACs to validate:**
- Do BOs have a view on page layout priorities? (e.g., search prominent vs. filters prominent)

**Status:** In backlog. Design is ready — can start anytime.

---

### 7. FormSG Integration Discovery (OTEP-194)

**What officers get:** No direct officer impact yet. This is early discovery for Sprint 4's application layer.

**Why it's in Sprint 1:** Reduces risk. If we discover FormSG webhook limitations now, we have time to design around them.

**Question for BOs:**
> Do we have a FormSG contact who can confirm webhook capabilities? Or do we need to test independently?

**Status:** In backlog. Low priority relative to auth and data decisions.

---

## Decisions Needed from BOs Today

### Must-have today (blocks Sprint 2 start)

| # | Decision | My recommendation | Why it matters |
|---|----------|-------------------|---------------|
| 1 | **C@G ingestion method** — how do we get Careers@Gov listings into OTEP? | API access; decouple from OTG pipeline. OTG types first, C@G is fast-follow. | Decision needed now so C@G work can be sequenced — but it won't block Sprint 2 (OTG only) |
| 2 | **Data freshness requirement** — how stale can opportunity listings be? | Daily sync acceptable for MVP; real-time is R1 | Determines pipeline architecture and whether "Closing soon" labels are reliable |
| 3 | ~~**Mock data acceptable for Sprint 2?**~~ | DECIDED: Yes — build UI against seed data, swap to live pipeline when ready | Confirmed — Sprint 2 is unblocked regardless of pipeline status |

### Needed by end of Sprint 1 (blocks implementation, not planning)

| # | Decision | My recommendation | Why it matters |
|---|----------|-------------------|---------------|
| 4 | **Is Secondment a separate opportunity type?** | Treat as sub-type of SJR for MVP | Determines filter categories in US-03 (4 types or 5?) |
| 5 | ~~**What does "ringfenced" mean?**~~ | DECIDED: Ringfencing rule tied to each opportunity (set per-posting) | Confirmed — no session-level logic needed |
| 6 | ~~**Opportunity lifecycle**~~ | DECIDED: Auto-close by date. No closing date → evergreen, pushed to bottom of list | Confirmed — no admin tooling needed |
| 7 | **Pilot group definition** — how do we determine who has access? | Pull from POCDEX agency code (ESG/PSD) | Determines how OTEP-111 is built — manual list vs. system-driven |
| 8 | **Edge case: officer logs in before POCDEX push** | Show "profile pending, check back shortly" message | Avoids confusing "no access" for a legitimate new officer |

---

## Scope Conversation

### What's on track for May 18
- Login authentication working e2e (basic UI, token flow, session handling) — in progress
- Backend foundations done: repo, DB conventions, schema migration in QA
- Decisions clarified: data model approach, C@G method, function filter direction

### What's explicitly NOT Sprint 1 (agreed with team)
- Full opportunity listing with real data — Sprint 2
- Filters, sorting, search — Sprint 2+
- Function filter implementation — Sprint 2+ (investigate only in Sprint 1)
- Full data model / competency bank design — we clarify and escalate dependencies, not own the build

### What Sprint 2 will deliver

By end of Sprint 2 (May 30), officers will be able to:
- Log in with gov.sg email
- See a listing of **OTG opportunity types** (STIPs, Gigs, SJRs, Internal Jobs) with structured cards
- **Only see opportunities they're eligible for** — ringfencing applied based on their POCDEX profile
- Filter by opportunity type (STIP, Gig, SJR, Internal Jobs — no function filter)
- Sort by posted date or closing date
- See "Closing soon" labels
- Click into a **full detail page** showing reporting line, "What you'll gain," and competency tags
- **Apply via OTG** redirect for SJRs and internal jobs

**What Sprint 2 will NOT deliver:**
- **Function filter** — removed from Sprint 2 scope per team agreement
- **Competency match ratio** — detail page shows competency tags only ("What you'll develop"), no scoring/matching
- **Careers@Gov listings** — OTG types prioritised first. C@G indicator (US-10) and deep-link (US-11) come after OTG is stable.
- **Live OTG data** — Sprint 2 builds against seed/mock data. Live pipeline is a fast-follow.
- **FormSG application route** — Sprint 3+ (STIPs and Gigs apply flow comes later)

**What this means:** Sprint 2 delivers a **functional hub for OTG opportunities** — but likely running on seed data, not production data. C@G is a fast-follow once the OTG experience is stable. Think of it as "the experience works for OTG first, then we layer in C@G."

### What Sprint 2 needs from us by May 18
For Sprint 2 to start building, we need these by end of sprint:
1. Auth working (so Sprint 2 can build behind login) — on track
2. Data model direction decided — **needs decision today**
3. C@G approach decided — **needs decision today**
4. Base layout started or design ready — design ready, can start

**Question for BOs:**
> Are you comfortable with Sprint 2 delivering the hub UI against seed data, with live OTG data and C@G listings flowing in Sprint 3? Or is live data a hard requirement for Sprint 2?

---

## Priority Call

If we can only deliver a subset by May 18, what's the priority order?

1. _____ (suggest: Login authentication — gates everything)
2. _____ (suggest: Data decisions landed — gates Sprint 2 build)
3. _____ (suggest: POCDEX spike started — gates account creation)
4. _____ (suggest: Listing page skeleton — head start for Sprint 2)
5. _____ (suggest: Error states — can harden in Sprint 2)
6. _____ (suggest: FormSG discovery — Sprint 4 dependency, can wait)

---

## After Session — Decisions Captured

### Confirmed today (May 7)
- [x] Mock data acceptable for Sprint 2 → Yes
- [x] Ringfencing — per-opportunity rule (set on each posting), prioritised at top of listing
- [x] Opportunity lifecycle — auto-close by date; no date → evergreen, pushed to bottom
- [x] Competency match — NOT in Sprint 2. Competencies ready Sprint 3/4.
- [x] No competency match ratio shown in Sprint 2 (just tags as "What you'll develop")
- [x] SJRs without FormSG URL — don't show in OTEP / bring user to OTG instead
- [x] IJRs — requires comms to pilot agency to create FormSG for their IJRs

### Still open
- [ ] Decision: C@G ingestion method
- [ ] Decision: Data freshness requirement (daily / real-time)
- [ ] Decision: Secondment — separate type or sub-type of SJR?
- [ ] Decision: Pilot group source (POCDEX vs. manual)
- [ ] Decision: Edge case handling for pre-POCDEX login
- [ ] Decision: Function filter approach (defer / combine / separate)

### Actions required
- [ ] **Comms to pilot agency** re: creating FormSG for IJRs — **BOs own this**. Follow up by when?
- [ ] Confirm: SJRs without FormSG URL → redirect to OTG or hide entirely?
