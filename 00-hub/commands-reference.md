# Commands & Skills Reference

> Last updated: 2026-05-18

---

## Slash Commands

These live in `.claude/commands/`. Invoke by name (e.g. "run /daily" or just "/daily").

### Daily Rhythm

| Command | When to use | What it does |
|---|---|---|
| `/daily` | Morning | Schedule, ceremony check, recently completed, open items, top 3 focus, PM growth nudge |
| `/midday` | Midday | Quick pulse check against your morning plan |
| `/endday` | End of day | What got done, carry-forward, reflection, PM growth check |

### Ceremony Prep

| Command | When to use | What it does |
|---|---|---|
| `/groom-prep` | Day before grooming | Story scores, AC completeness, design status, risk areas |
| `/groom` | Morning of grooming | Story readiness, gaps, dependencies, edge cases |
| `/sprint-plan-prep` | Before sprint planning | Draft sprint goal, candidate stories, capacity flags |
| `/mid-sprint-review` | Monday week 2 | Sprint health, blockers, scope creep flags, decisions needed |
| `/retro-prep` | After sprint ends | Demo-able stories, demo order, Signal/Sense/Shift prompts |

### Weekly & Strategic

| Command | When to use | What it does |
|---|---|---|
| `/week` | Monday morning | Decisions needed, stakeholder conversations, spec gaps |
| `/brief` | Before stakeholder meetings | Audience-specific brief (Mark, Jacky, Adrian, etc.) |
| `/decision` | Before scope calls | Pre-decision brief, audit, post-decision conflict check |
| `/retro` | Friday | Signal/Sense/Shift using meeting notes + PM growth lens |
| `/scan` | As needed | Document health: contradictions, undefined reqs, sign-off gaps |
| `/archive` | Mid-sprint + end-sprint | Snapshot context files, move outputs to archive |

---

## Personal OS Skills

These live in `.claude/skills/`. Invoke by name (e.g. "run meeting-prep for Adrian").

| Skill | Argument | What it does |
|---|---|---|
| `meeting-prep` | `[person-name]` | Loads context from people profiles, past notes, action items, decisions needed |
| `weekly-update` | — | Drafts stakeholder email: headline, metrics, progress, blockers, next week |
| `draft-prd-section` | `[section-name] [project-path]` | Writes a PRD section grounded in project research and GOALS.md |
| `synthesize-research` | `[path-to-research-folder]` | Turns raw interview notes into structured insights: findings, patterns, quotes |
| ~~`standup`~~ | — | **Deprecated** — use `/daily` instead |

---

## Plugin Skills

Installed via your PM plugins. Invoke by describing the task or saying the skill name.

### Product Discovery
| Skill | What it does |
|---|---|
| `interview-script` | Customer interview guide using The Mom Test principles |
| `summarize-interview` | Turns interview transcript into structured JTBD insights |
| `brainstorm-ideas-existing` | Ideation from PM, Designer, Engineer perspectives |
| `opportunity-solution-tree` | Maps outcome → opportunities → solutions → experiments (Teresa Torres) |
| `identify-assumptions-existing` | Risky assumptions across Value, Usability, Viability, Feasibility |
| `prioritize-assumptions` | Impact × Risk matrix + experiment suggestions |
| `brainstorm-experiments-existing` | Prototypes, A/B tests, spikes for existing products |
| `analyze-feature-requests` | Categorise and prioritise a batch of feature requests |
| `prioritize-features` | Rank backlog by impact, effort, risk, strategic alignment |
| `metrics-dashboard` | Define North Star, input metrics, health metrics, alert thresholds |

### Product Execution
| Skill | What it does |
|---|---|
| `create-prd` | Full PRD using 8-section template |
| `user-stories` | User stories with 3 C's, INVEST criteria, acceptance criteria |
| `job-stories` | JTBD format: When / I want to / So I can |
| `wwas` | Why-What-Acceptance backlog items |
| `test-scenarios` | Test cases from user stories: happy paths, edge cases, errors |
| `pre-mortem` | Tigers / Paper Tigers / Elephants risk analysis on PRD or launch plan |
| `sprint-plan` | Capacity estimation, story selection, dependency mapping |
| `retro` | Structured retrospective with Signal/Sense/Shift + action items |
| `release-notes` | User-facing release notes from tickets or PRDs |
| `brainstorm-okrs` | Team OKRs aligned with company objectives |
| `stakeholder-map` | Power × Interest grid + communication plan |
| `summarize-meeting` | Meeting transcript → decisions, action items, follow-ups |
| `outcome-roadmap` | Converts feature roadmap into outcome-focused roadmap |
| `prioritization-frameworks` | Reference: RICE, ICE, Kano, MoSCoW, Opportunity Score |

### Product Strategy
| Skill | What it does |
|---|---|
| `product-strategy` | 9-section Strategy Canvas: vision → defensibility |
| `product-vision` | Inspiring, achievable vision statement |
| `value-proposition` | 6-part JTBD template: Who / Why / What before / How / What after / Alternatives |
| `lean-canvas` | Lean startup canvas |
| `business-model` | Business Model Canvas (9 blocks) |
| `startup-canvas` | Product Strategy + Business Model combined |
| `swot-analysis` | Strengths, Weaknesses, Opportunities, Threats + recommendations |
| `pestle-analysis` | Political, Economic, Social, Technological, Legal, Environmental |
| `porters-five-forces` | Competitive rivalry, supplier/buyer power, substitutes, new entrants |
| `ansoff-matrix` | Growth strategies: penetrate / develop / diversify |
| `monetization-strategy` | 3–5 revenue models with risks and validation experiments |
| `pricing-strategy` | Pricing models, competitive analysis, willingness-to-pay |

### Go-to-Market
| Skill | What it does |
|---|---|
| `gtm-strategy` | Marketing channels, messaging, success metrics, launch timeline |
| `beachhead-segment` | First market segment: burning pain, WTP, winnable share, referral potential |
| `ideal-customer-profile` | ICP from research data: demographics, behaviours, JTBD |
| `growth-loops` | Viral, Usage, Collaboration, UGC, Referral loop design |
| `gtm-motions` | Inbound, Outbound, Paid, Community, Partners, ABM, PLG |
| `competitive-battlecard` | Sales-ready battlecard: positioning, objection handling, win/loss |

### Market Research
| Skill | What it does |
|---|---|
| `competitor-analysis` | Competitive landscape: strengths, weaknesses, differentiation |
| `market-sizing` | TAM / SAM / SOM — top-down and bottom-up |
| `market-segments` | 3–5 customer segments with demographics, JTBD, product fit |
| `user-personas` | 3 personas from research data: JTBD, pains, gains |
| `user-segmentation` | Segment users by behaviour, JTBD, and needs |
| `customer-journey-map` | End-to-end journey: stages, touchpoints, emotions, pain points |
| `sentiment-analysis` | Sentiment scores, JTBD patterns from feedback data |

### Data & Analytics
| Skill | What it does |
|---|---|
| `sql-queries` | SQL from natural language — BigQuery, PostgreSQL, MySQL |
| `ab-test-analysis` | Statistical significance, sample size, ship/extend/stop recommendation |
| `cohort-analysis` | Retention curves, feature adoption, engagement trends |

### Toolkit
| Skill | What it does |
|---|---|
| `review-resume` | PM resume review against 10 best practices |
| `grammar-check` | Grammar, logic, and flow check — targeted fixes only |
| `draft-nda` | NDA draft between two parties |
| `privacy-policy` | Privacy policy covering GDPR and compliance requirements |

### File Output Skills
| Skill | What it does |
|---|---|
| `docx` | Create or edit Word documents (.docx) |
| `pptx` | Create or edit PowerPoint decks (.pptx) |
| `xlsx` | Create or edit Excel spreadsheets (.xlsx) |
| `pdf` | Extract, create, merge, or split PDFs |

---

## How to Invoke

- **Commands** — say the command name: `/daily`, `/groom`, `/retro`
- **Personal skills** — say the skill name with context: "run meeting-prep for Jacky", "draft-prd-section for the search feature"
- **Plugin skills** — describe what you need and I'll pick the right one, or name it explicitly: "run a pre-mortem on this PRD", "use the opportunity-solution-tree skill"
- **File skills** — mention the file type: "save this as a Word doc", "create a slide deck for this"
