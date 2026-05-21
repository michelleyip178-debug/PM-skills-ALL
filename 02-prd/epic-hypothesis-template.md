# Epic Hypothesis Template

Use before writing a PRD section or briefing a discovery cycle.

---

## Template

**Epic name:**

**Problem statement:**
We believe [user type] struggle to [do what] because [root cause].

**Assumption being tested:**
If we [build/change/remove X], then [user type] will [measurable behaviour change].

**Success metric:**
We'll know this worked when [specific, measurable outcome] within [timeframe].

**MVP scope (what's in):**
-
-

**Out of scope for this epic:**
-
-

**Open questions before spec:**
-
-

---

## Example (OTEP — Opportunity Discovery)

**Epic name:** Opportunity listing page

**Problem statement:**
We believe public service officers struggle to find relevant mobility opportunities because the current process requires going through multiple platforms with no unified view.

**Assumption being tested:**
If we surface all opportunity types (STIP, Gig, SJR, C@G) in one searchable list, officers will apply at a higher rate than baseline FormSG submissions.

**Success metric:**
We'll know this worked when ≥30% of logged-in users initiate at least one opportunity view within their first session, measured at MVP launch.

**MVP scope (what's in):**
- Listing page with all 4 opportunity types from OTG
- Basic filters: agency, opportunity type, closing date
- Card view with title, agency, type, closing date

**Out of scope for this epic:**
- AI/recommendation matching
- Saved/bookmarked opportunities
- Application status tracking

- ~~Is `formsg_url` confirmed for all STIP/Gig/Internal Jobs in OTG?~~ — **Yes, confirmed 2026-05-21 (SJRs excluded — no apply flow in MVP)**
- ~~What is the fallback when `formsg_url` is null?~~ — **Resolved: "Application form unavailable — contact the posting agency" (AC in US-18)**
