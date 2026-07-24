### OTEP-768 — cft_upload db table status to scope to cft related status
Type: Bug | Assignee: Hao Eng | Labels: []
Description:
It is misleading to show the error message that is related to opportunity upload.To only show error when there is sth wrong with authenticate/download file from CFT (CFT related functions)

---

### OTEP-755 — seed POCDEX ref agency code production table (as of 20 July)
Type: Task | Assignee: unassigned | Labels: []
Description:
To reload the ref agency table with this excel in attachment.for info, Johnny is our ITC colleague handling pocdex api going forward.

---

### OTEP-684 — Refactor ingestion model (split otg /cag importer.SourceRecord)
Type: Sub-task | Assignee: unassigned | Labels: []
Description:
(no description)

---

### OTEP-682 — Autogenerate doc in pipeline
Type: Sub-task | Assignee: unassigned | Labels: []
Description:
(no description)

---

### OTEP-681 — Run integration testing in pipeline
Type: Sub-task | Assignee: unassigned | Labels: []
Description:
(no description)

---

### OTEP-680 — Check with OPS for observability needs
Type: Sub-task | Assignee: Léo Milbor | Labels: []
Description:
Check with Fabian and Fanxu

---

### OTEP-679 — Connectivity between CSC and CareerCompass
Type: Task | Assignee: Fanxu Wang | Labels: []
Description:
(no description)

---

### OTEP-662 — Investigate why we're seeing login error after a redeploy in dev
Type: Sub-task | Assignee: Thomas Huchedé | Labels: []
Description:
We’re seeing a couple of failure to redirect unlogged user. Seems to be happening after a redeploy (but not sure this is the root cause).We need to make sure unlogged user are properly redirected to the login page when we failed to refresh their token.Ref:  

---

### OTEP-659 — Investigate smoke test for pipeline
Type: Sub-task | Assignee: Thomas Huchedé | Labels: []
Description:
(no description)

---

### OTEP-570 — View matched competencies on Gig/STIP detail page
Type: Story | Assignee: unassigned | Labels: []
Description:
User StoryAs an officer browsing a Gig or STIP, I want to see which of the competencies I'd develop from this opportunity I already have, so I can assess my fit and factor growth potential into my decision before applying.Acceptance CriteriaAC1 — "What you'll develop" section renders with match statesGiven an officer views a Gig or STIP detail page,When their competency profile is successfully retrieved from the Core competency endpoint,Then a "What you'll develop" section renders listing each competency associated with the opportunity.Each competency shows one of two states: matched (the competency appears in the officer's profile) or unmatched (it does not).No proficiency level is compared — presence only.AC2 — Matched competencies are visually distinct from unmatchedGiven the "What you'

---

### OTEP-569 — Events
Type: Sub-task | Assignee: unassigned | Labels: []
Description:
As a product/data analyst, I want each authenticated officer's opportunity engagement (what they view, what they apply to, how they found it, and whether they're a returning applicant or a first-timer) tracked in PostHog with event properties and person-level aggregates, so I can segment opportunity behaviour by type, source, and discovery method — and measure OKR 2 (~1,850 officers applied via CareerCompass) without joining to an external data source.Background / ContextOpportunity events fire client-side on the listing and detail pages. The officer is already identified (distinct_id = profileId) via OTEP-488 — this story attaches opportunity-specific properties to their events and person record.User-level aggregates (viewed/applied counts, timestamps) are written via $set on each event s

---

### OTEP-502 — Track opportunity engagement events and person aggregates in PostHog
Type: Story | Assignee: Thomas Huchedé | Labels: []
Description:
Instrument the opportunities journey in PostHog as an event-first funnel (search/filter → impression → click → viewed → applied) so the product/data analyst can measure discovery → interest → conversion, and report OKR 2 ("~1,850 officers applied via CareerCompass") without joining an external data source.WhyThe original story proposed denormalized person-property counters (opportunities_viewed_count, etc.). Those (a) duplicate PostHog's native event aggregation and (b) can't be maintained client-side — the SDK runs flags-disabled (OTEP-488; the deployment blocks /flags), so it can't read a current person value to increment, and PostHog has no atomic increment operator. After PM discussion the model is event-first: counts/CTR/conversion are derived from events; only cheap timestamp person-

---

### OTEP-485 — Run update deps in otep-service
Type: Sub-task | Assignee: Léo Milbor | Labels: []
Description:
(no description)

---

### OTEP-483 — Technical tasks
Type: Story | Assignee: unassigned | Labels: []
Description:
(no description)

---

### OTEP-409 — [FE] Listing — reflect ringfenced results
Type: Story | Assignee: unassigned | Labels: []
Description:
Listing renders the filtered response from OTEP-408 with no additional FE filtering logicNo visible indicator on cards that ringfencing is active (no "available to you" badge — that's OTEP-390 detail page)Fallback (unfiltered) and filtered states render identically from FE perspective — no special handling needed

---

### OTEP-408 — [BE] Listing API — apply ringfencing eligibility filter
Type: Story | Assignee: unassigned | Labels: []
Description:
Listing API filters by officer's POCDEX data resolved at loginIneligible opportunities excluded from responseEligible ringfenced Internal Jobs pinned to topPOCDEX unavailable → silent fallback to unfiltered listingUnauthenticated officer → redirect to login before data returned

---

### OTEP-404 — Handle different page size on tablet and mobile
Type: Task | Assignee: Thomas Huchedé | Labels: []
Description:
On opportunity listing, the page size on mobile and tablet should be 10 not 15

---

### OTEP-403 — OTG data import hardening
Type: Story | Assignee: Léo Milbor | Labels: []
Description:
OTG Data Import HardeningCurrent ContextConcurrent execution is not catered forNo way to tie an import attempt to corresponding source_otg_opportunity rowNo tracing or metrics, we only have basic default endpoint loggingUnit&Integration testing review according to  Use custom models and repo method instead of refdata package’s.No role base access, every one authenticated can trigger the uploads.Suggested EvolutionConcurrent executionFor now, we run a single instance of otep-service. But this is not guaranteed to always be true. So we cannot just use a worker in service to force sequential operation. We can use postgresql locking mechanism. This would avoid pulling another dependency for queuing import request.Grouping Import per RequestIn otg_importer.go we can create an ID (and either add

---

### OTEP-393 — chore: integrate custom OTEP login theme into Keycloak service
Type: Task | Assignee: unassigned | Labels: []
Description:
Assumption context: These tasks assume OTEP will continue using Keycloak in production.Problem: When officers click "Login with WOG AD" on the Next.js landing page (/auth/login), they are redirected to Keycloak which currently uses its default, unstyled login screen. This creates a jarring visual break — officers leave the OTEP-branded experience and land on an unstyled Keycloak page.Goal: Integrate a custom OTEP login theme into the Keycloak service so the login screen is visually consistent with the OTEP product.Implementation notes:Custom theme must match the OTEP visual style: logo, colour palette, typography, and button treatment per Amber's design spec. Design asset must be linked to this ticket before development starts.Login form fields (username, password) and submit button must r

---

### OTEP-348 — OTG data ingestion — scheduler & observability
Type: Story | Assignee: unassigned | Labels: []
Description:
Companion to OTEP-192. Build the scheduled execution layer and observability for the OTG ingestion pipeline.Acceptance CriteriaThe job runs on a defined recurring schedule (cadence TBC with engineers at planning)Each run produces a summary log: records read, inserted, updated, skipped, and errorsInvalid or incomplete records are skipped and logged; a bad row does not abort the runAlerts or notifications on repeated failures (threshold TBC)

---

### OTEP-336 — Show competency match signal on Gig/STIP listing cards
Type: Story | Assignee: unassigned | Labels: []
Description:
User StoryAs an officer browsing the opportunity listing, I want to see at a glance how many competencies I already have for each Gig or STIP, so I can quickly identify high-fit opportunities without opening every detail page.Acceptance CriteriaAC1 — Competency match count renders on Gig/STIP cardsGiven an officer views the opportunity listing, When their competency profile is successfully retrieved, Then each Gig and STIP card shows a match count (e.g. "3 of 5 competencies match your profile"). No proficiency level is compared — presence only.AC2 — No match indicator when officer has no profileGiven an officer has no competency data in their POCDEX profile, When they view the listing, Then Gig and STIP cards render without a competency match count. No error is shown. The card is otherwise

---

### OTEP-329 — chore: Keycloak Client Secret Externalization
Type: Story | Assignee: Pow Hwee TAN (PSD) | Labels: []
Description:
Currently, the Keycloak client secret (used for NextAuth OIDC flow) is hardcoded in the local development realm-export.json. Furthermore, KEYCLOAK_SECRET is not yet externalized in AWS Secrets Manager or configured for container injection in otep-web.Acceptance CriteriaCreate a secure entry in AWS Secrets Manager for KEYCLOAK_SECRET in each environment (Dev/Staging/Prod).Update otep-web/terragrunt.hcl to map this secret to the KEYCLOAK_SECRET environment variable.Ensure Keycloak bootstrap in staging/production dynamically reads the client secret rather than baking a static credential into configuration/export files.

---

### OTEP-130 — Apply for a STIP or Gig - PostHog Tracking
Type: Story | Assignee: unassigned | Labels: []
Description:
User StoryTBC

---

