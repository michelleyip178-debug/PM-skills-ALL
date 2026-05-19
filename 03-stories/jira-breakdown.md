# CLAUDE.md — Jira Sprint Issue Exporter

> **Note:** The logic below has been fully implemented in `scripts/jira-sync.py`. You can execute that script directly rather than running this workflow manually through the AI.

## Overview
When asked to sync Jira issues, extract all issues from the active sprint and write one markdown file per issue into the correct sprint folder.

---

## Environment Variables
These must be set in your shell before running Claude Code:

```bash
export JIRA_EMAIL="you@yourdomain.com"
export JIRA_API_TOKEN="your-api-token-here"
```

Get your API token at: https://id.atlassian.com/manage-profile/security/api-tokens

---

## Configuration
Update these values to match your workspace:

| Variable        | Value                                      |
|-----------------|--------------------------------------------|
| `JIRA_BASE_URL` | `https://<your-domain>.atlassian.net`      |
| `PROJECT_KEY`   | e.g. `PROF`, `OTEP`                        |
| `BOARD_ID`      | Found in your Jira board URL: `/boards/ID` |

---

## Folder Structure
```
jira-sync/
└── Sprint-<number>-<sprint-name>/
    ├── ISSUE-101.md
    ├── ISSUE-102.md
    └── ISSUE-103.md
```

Example: `jira-sync/Sprint-4-OTEP-Epic4/PROF-101.md`

- Sanitise sprint names for folder use: replace spaces with `-`, remove special characters
- Create folders if they don't exist
- Overwrite existing files on re-sync

---

## API Calls — Step by Step

### Step 1: Get the active sprint
```
GET /rest/agile/1.0/board/<BOARD_ID>/sprint?state=active
Authorization: Basic base64(<JIRA_EMAIL>:<JIRA_API_TOKEN>)
```
Extract: `id` (sprint ID), `name` (sprint name)

If no active sprint is found, ask the user: _"No active sprint found. Please provide a sprint ID to target."_

---

### Step 2: Get all issues in the sprint
```
GET /rest/agile/1.0/sprint/<SPRINT_ID>/issue?maxResults=100&fields=summary,status,assignee,story_points,subtasks,description
```
Extract the `issues[]` array.

---

### Step 3: Get full issue details (per issue)
```
GET /rest/api/3/issue/<ISSUE_KEY>
```
Fields to extract:

| Field            | JSON path                                  |
|------------------|--------------------------------------------|
| Summary          | `fields.summary`                           |
| Status           | `fields.status.name`                       |
| Assignee         | `fields.assignee.displayName`              |
| Story Points     | `fields.story_points` or `fields.customfield_10016` |
| Description      | `fields.description` (ADF format — see below) |
| Subtasks         | `fields.subtasks[]`                        |

---

## ADF Description Parsing
Jira descriptions use Atlassian Document Format (ADF). Extract plain text by recursively walking `content[].content[].text`.

Pseudo-logic:
```
function extractText(node):
  if node.text exists → return node.text
  if node.content exists → return node.content.map(extractText).join(" ")
  return ""
```

---

## Markdown Template per Issue

Write each issue as `<ISSUE-KEY>.md` using this template:

```markdown
# <ISSUE-KEY>: <Summary>

**Status:** <status>
**Assignee:** <assignee displayName or N/A>
**Story Points:** <story points or N/A>

---

## Description

<plain text extracted from ADF description, or "No description provided.">

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| <subtask-key> | <subtask summary> | <subtask status> |
```

- If there are no subtasks, write: `_No subtasks._`
- If any field is missing, write: `N/A`

---

## Error Handling
- If `JIRA_EMAIL` or `JIRA_API_TOKEN` are not set → stop and print: _"Missing environment variables. Please set JIRA_EMAIL and JIRA_API_TOKEN."_
- If an API call returns 401 → print: _"Authentication failed. Check your JIRA_EMAIL and JIRA_API_TOKEN."_
- If an API call returns 404 → skip the issue and log: _"Issue <KEY> not found — skipped."_
- If description parsing fails → write: `_Description could not be parsed._`

---

## Trigger Phrase
When the user says **"sync Jira issues"** or **"export sprint issues"**, execute all steps above from Step 1 through file creation.
