#!/usr/bin/env python3
import os
import sys
import json
import re
import urllib.request
import urllib.parse
from base64 import b64encode

def parse_inline(text):
    # Links: [text](url) -> <a href="url">text</a>
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # Bold: **text** -> <strong>text</strong>
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    # Italic: *text* -> <em>text</em>
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    # Inline code: `text` -> <code>text</code>
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text

def markdown_to_xhtml(md_text):
    # First extract code blocks to protect them from further parsing
    code_blocks = []
    def save_code(match):
        idx = len(code_blocks)
        code_blocks.append(match.group(0))
        return f"__CODE_BLOCK_PLACEHOLDER_{idx}__"
    
    md_text = re.sub(r'```(\w*)\n(.*?)```', save_code, md_text, flags=re.DOTALL)
    
    blocks = md_text.split('\n\n')
    xhtml_blocks = []
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
            
        # Check if placeholder
        if block.startswith('__CODE_BLOCK_PLACEHOLDER_'):
            match = re.match(r'^__CODE_BLOCK_PLACEHOLDER_(\d+)__$', block)
            if match:
                idx = int(match.group(1))
                original_code = code_blocks[idx]
                m = re.match(r'```(\w*)\n(.*?)```', original_code, flags=re.DOTALL)
                if m:
                    lang = m.group(1) or "none"
                    code = m.group(2)
                    xhtml_blocks.append(
                        f'<ac:structured-macro ac:name="code">'
                        f'<ac:parameter ac:name="language">{lang}</ac:parameter>'
                        f'<ac:plain-text-body><![CDATA[{code}]]></ac:plain-text-body>'
                        f'</ac:structured-macro>'
                    )
                continue
                
        # Check if heading
        if block.startswith('#'):
            m = re.match(r'^(#{1,6})\s+(.+)$', block)
            if m:
                level = len(m.group(1))
                inline_content = parse_inline(m.group(2))
                xhtml_blocks.append(f'<h{level}>{inline_content}</h{level}>')
                continue
                
        # Check if table (starts with |)
        if block.startswith('|'):
            table_lines = block.split('\n')
            table_rows = []
            for line in table_lines:
                stripped = line.strip()
                if stripped.startswith('|') and stripped.endswith('|'):
                    cells = [c.strip() for c in stripped.split('|')[1:-1]]
                    if all(re.match(r'^:?-+:?$', cell) for cell in cells):
                        continue
                    table_rows.append(cells)
            if table_rows:
                table_html = ["<table>"]
                for r_idx, row in enumerate(table_rows):
                    table_html.append("<tr>")
                    cell_tag = "th" if r_idx == 0 else "td"
                    for cell in row:
                        inline_cell = parse_inline(cell)
                        table_html.append(f"<{cell_tag}>{inline_cell}</{cell_tag}>")
                    table_html.append("</tr>")
                table_html.append("</table>")
                xhtml_blocks.append("\n".join(table_html))
                continue
                
        # Check if list
        if block.startswith('- ') or block.startswith('* ') or re.match(r'^\d+\.\s+', block):
            list_lines = block.split('\n')
            list_html = []
            current_list_type = None # 'ul' or 'ol'
            
            for line in list_lines:
                line_stripped = line.strip()
                m_ul = re.match(r'^[\-*]\s+(.+)$', line_stripped)
                m_ol = re.match(r'^\d+\.\s+(.+)$', line_stripped)
                
                if m_ul:
                    if current_list_type == 'ol':
                        list_html.append("</ol>")
                    if current_list_type != 'ul':
                        list_html.append("<ul>")
                        current_list_type = 'ul'
                    list_html.append(f"<li>{parse_inline(m_ul.group(1))}</li>")
                elif m_ol:
                    if current_list_type == 'ul':
                        list_html.append("</ul>")
                    if current_list_type != 'ol':
                        list_html.append("<ol>")
                        current_list_type = 'ol'
                    list_html.append(f"<li>{parse_inline(m_ol.group(1))}</li>")
                else:
                    if list_html:
                        prev = list_html.pop()
                        if prev.endswith("</li>"):
                            prev = prev[:-5] + " " + parse_inline(line_stripped) + "</li>"
                        list_html.append(prev)
                        
            if current_list_type == 'ul':
                list_html.append("</ul>")
            elif current_list_type == 'ol':
                list_html.append("</ol>")
                
            xhtml_blocks.append("\n".join(list_html))
            continue
            
        # Paragraph
        xhtml_blocks.append(f'<p>{parse_inline(block)}</p>')
        
    return "\n\n".join(xhtml_blocks)

def load_env():
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ.setdefault(key, val)

def make_auth_header():
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_API_TOKEN")
    if not email or not token:
        sys.exit("Missing environment variables. Please set JIRA_EMAIL and JIRA_API_TOKEN in .env.")
    return "Basic " + b64encode(f"{email}:{token}".encode()).decode()

def main():
    if len(sys.argv) < 3:
        print("Usage: ./push-confluence-prd.py <PAGE_ID> <LOCAL_FILE_PATH>")
        print("Example: ./push-confluence-prd.py 1976550683 02-prd/prd-opportunities.md")
        sys.exit(1)
        
    page_id = sys.argv[1]
    local_file = sys.argv[2]
    
    if not os.path.exists(local_file):
        sys.exit(f"Error: Local file {local_file} does not exist.")
        
    load_env()
    site = os.environ.get("JIRA_SITE")
    if not site:
        sys.exit("Missing environment variable JIRA_SITE in .env.")
        
    base_url = f"https://{site}"
    auth = make_auth_header()
    
    # 1. Fetch current version and title of the page (required for updating)
    url = f"{base_url}/wiki/rest/api/content/{page_id}?expand=version"
    print(f"Fetching current page info for {page_id}...")
    
    req = urllib.request.Request(url, headers={"Authorization": auth, "Accept": "application/json"})
    
    try:
        with urllib.request.urlopen(req) as resp:
            current_data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 401:
            sys.exit("Authentication failed. Check your JIRA_EMAIL and JIRA_API_TOKEN.")
        if e.code == 404:
            sys.exit(f"Page {page_id} not found.")
        sys.exit(f"HTTP {e.code}: {e.reason} — {url}")
    except Exception as e:
        sys.exit(f"Error fetching page info: {e}")
        
    title = current_data.get("title", "Updated PRD")
    current_version = current_data.get("version", {}).get("number", 1)
    next_version = current_version + 1
    
    print(f"Current version: {current_version}. Next version will be: {next_version}")
    
    # 2. Read local Markdown and convert to XHTML
    print(f"Reading and converting {local_file} to Confluence format...")
    with open(local_file, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    # Strip off the main title header if it starts with "# " to avoid double title on Confluence
    if md_content.startswith("# "):
        lines = md_content.split('\n')
        # Extract title from the first line
        title = lines[0].replace("# ", "").strip()
        md_content = "\n".join(lines[1:]).strip()
        
    xhtml_body = markdown_to_xhtml(md_content)
    
    # 3. Perform PUT request to update the page
    update_url = f"{base_url}/wiki/rest/api/content/{page_id}"
    update_data = {
        "id": page_id,
        "type": "page",
        "title": title,
        "version": {
            "number": next_version
        },
        "body": {
            "storage": {
                "value": xhtml_body,
                "representation": "storage"
            }
        }
    }
    
    payload = json.dumps(update_data).encode("utf-8")
    
    print(f"Pushing updates to Confluence for page '{title}'...")
    req = urllib.request.Request(update_url, data=payload, method="PUT")
    req.add_header("Authorization", auth)
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    
    try:
        with urllib.request.urlopen(req) as resp:
            response_data = json.loads(resp.read().decode())
            print(f"Successfully updated Confluence page!")
            print(f"New Version: {response_data.get('version', {}).get('number')}")
    except urllib.error.HTTPError as e:
        error_resp = e.read().decode()
        sys.exit(f"HTTP Error {e.code}: {e.reason}\nResponse: {error_resp}")
    except Exception as e:
        sys.exit(f"Error updating Confluence: {e}")

if __name__ == "__main__":
    main()
