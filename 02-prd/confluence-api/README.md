# Confluence REST API Scripts

**Status: Pending**

Scripts to pull and push PRD content to/from Confluence are not yet built.

## Planned scripts

| Script | Purpose |
|---|---|
| `pull-confluence-prd.py` | Pull current PRD page content from Confluence into a local .md file |
| `push-confluence-prd.py` | Push updated local .md content back to Confluence page |

## Reference

- Confluence REST API docs: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/
- Auth: API token (store in `.env`, never commit)
- Page ID: find in the Confluence page URL (`?pageId=XXXXXX`)

## When built, add to 03-stories/scripts/ for Jira equivalents

See `03-stories/scripts/` for the Jira REST API scripts as a reference pattern.
