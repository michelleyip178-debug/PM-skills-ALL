# Confluence REST API Scripts

**Status: Completed**

Scripts to pull and push PRD content to/from Confluence.

## Available scripts

| Script | Purpose | Location |
|---|---|---|
| `pull-confluence-prd.py` | Pull current PRD page content from Confluence into a local .md file | [pull-confluence-prd.py](../../03-stories/scripts/pull-confluence-prd.py) |
| `push-confluence-prd.py` | Push updated local .md content back to Confluence page | [push-confluence-prd.py](../../03-stories/scripts/push-confluence-prd.py) |

## Reference

- Auth: API token (store in `03-stories/.env`, never commit)
- Page ID: find in the Confluence page URL (`?pageId=XXXXXX`)

## Usage

### Pulling a Confluence page
To pull a page from Confluence and save it to the local workspace:
```bash
python3 03-stories/scripts/pull-confluence-prd.py <PAGE_ID> [output_file_path]
```
If `output_file_path` is not provided, it will automatically save as a slugified file name in `02-prd/`.

Example:
```bash
python3 03-stories/scripts/pull-confluence-prd.py 1976550683 02-prd/prd-opportunities.md
```

### Pushing local Markdown back to Confluence
To push updated local Markdown content back to a Confluence page:
```bash
python3 03-stories/scripts/push-confluence-prd.py <PAGE_ID> <local_file.md>
```
The script will perform a pre-flight fetch to automatically grab the page's current version and increment it, as required by the Confluence concurrency model.

Example:
```bash
python3 03-stories/scripts/push-confluence-prd.py 1976550683 02-prd/prd-opportunities.md
```
