# MCP Configuration

Model Context Protocol (MCP) servers configured for this workspace.

---

## Active MCPs

None configured. MCP servers are blocked by GovTech managed settings (`allowedMcpServers: []`, `enableAllProjectMcpServers: false`). Check with IT if access becomes available.

---

## Planned MCPs

### Google Calendar

**Server:** `google-calendar`
**Status:** Not configured — requires OAuth + IT approval
**Purpose:** Access calendar events for meeting prep and scheduling context.

**Capabilities:**
- List upcoming events
- Get event details (attendees, description, location)
- Check availability

**Workaround:** Screenshot calendar or paste day's schedule into conversation.

---

### Granola

**Server:** `granola`
**Status:** Not configured
**Purpose:** Access meeting transcripts and notes from Granola.

**Capabilities:**
- Search past meeting transcripts
- Get meeting summaries
- Find mentions of topics/people across meetings

**Workaround:** Manually paste meeting notes into `Meetings/` folder.

---

### Linear (Planned)

**Server:** `linear`
**Status:** Not configured

**Purpose:** Interact with Linear tickets and projects.

**Planned Capabilities:**
- List tickets in a project
- Create/update tickets
- Sync ticket status

**Workaround:** Manual copy-paste from Linear. Tasks tracked in `Tasks/active.md`.

---

## Configuration Location

MCP servers are configured in Claude Code settings:
- **Project:** `.claude/settings.json` → `mcpServers`
- **User:** `~/.claude/settings.json`

**Note:** GovTech managed settings currently block all MCP servers. If this changes, update this file and configure in settings.

---

## Adding New MCPs

1. Confirm MCP servers are allowed in managed settings
2. Find or build MCP server for the service
3. Add configuration to `.claude/settings.json`
4. Test connection
5. Document in this file with capabilities and use cases
6. Update relevant skills to use the MCP
