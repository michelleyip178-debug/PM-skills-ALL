# Tags

Tag taxonomy for organizing files in this workspace.

---

## Project Tags

Used in project files to categorize work.

### By Product Area
| Tag | Description |
|-----|-------------|
| `#opportunities` | Opportunities epic (OTG + Careers@Gov) |
| `#wog-auth` | WOG AD authentication |
| `#platform` | Platform / infrastructure work |

(Add more as scope sharpens.)

### By Type
| Tag | Description |
|-----|-------------|
| `#feature` | New feature development |
| `#enhancement` | Improvement to existing feature |
| `#bug` | Bug fix |
| `#tech-debt` | Technical debt reduction |
| `#research` | Research initiative |
| `#experiment` | A/B test or experiment |

---

## Status Tags

### Project Status
| Tag | Description |
|-----|-------------|
| `#status/proposed` | Idea stage, not yet approved |
| `#status/planning` | Approved, in planning |
| `#status/in-progress` | Actively being worked on |
| `#status/blocked` | Blocked on dependency |
| `#status/shipped` | Launched to production |
| `#status/on-hold` | Paused, may resume |
| `#status/canceled` | Will not proceed |

### Document Status
| Tag | Description |
|-----|-------------|
| `#draft` | Work in progress |
| `#review` | Ready for review |
| `#approved` | Approved/finalized |
| `#archived` | No longer current |

---

## Priority Tags

| Tag | Description |
|-----|-------------|
| `#p0` | Critical - must do |
| `#p1` | High priority - should do |
| `#p2` | Medium priority - nice to have |
| `#p3` | Low priority - backlog |

---

## People Tags

| Tag | Description |
|-----|-------------|
| `#team/product` | Product team |
| `#team/engineering` | Engineering team |
| `#team/design` | Design team |
| `#team/leadership` | Leadership |
| `#stakeholder/adrian` | Adrian (Director of PM) |
| `#stakeholder/jace` | Jace (Lead PM) |
| `#stakeholder/pow-hwee` | Pow Hwee (Tech Lead) |
| `#stakeholder/amber` | Amber (Designer) |
| `#stakeholder/leo` | Leo (Engineer) |
| `#stakeholder/thomas` | Thomas (Engineer) |

---

## Time Tags

| Tag | Description |
|-----|-------------|
| `#q1-2026` | Q1 2026 work |
| `#q2-2026` | Q2 2026 work |
| `#h1-2026` | First half 2026 |
| `#2026` | 2026 fiscal year |

---

## Research Tags

| Tag | Description |
|-----|-------------|
| `#research/interview` | User interview |
| `#research/survey` | Survey research |
| `#research/usability` | Usability testing |
| `#research/competitive` | Competitive analysis |
| `#research/data` | Data analysis |

---

## Usage Examples

**PRD frontmatter:**
```yaml
tags:
  - opportunities
  - feature
  - status/planning
  - p0
  - q2-2026
```

**Research file:**
```yaml
tags:
  - research/interview
  - opportunities
  - status/approved
```

**Meeting notes:**
```yaml
tags:
  - stakeholder/adrian
  - team/product
```
