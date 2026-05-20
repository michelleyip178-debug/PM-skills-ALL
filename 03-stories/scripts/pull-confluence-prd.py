#!/usr/bin/env python3
import os
import sys
import json
import re
import urllib.request
import urllib.parse
from base64 import b64encode
from html.parser import HTMLParser

def normalize_story_text(text):
    # Remove bold, italics, backticks, asterisks, underscores
    text = re.sub(r'[*_`]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Normalize whitespaces to single spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_jira_link_artifacts(text):
    # Matches OTEP-85443f0c76-fa4b-3482-acf8-86ad00c0858bSystem Jira etc.
    pattern = r'[A-Z]+-\d+[0-9a-fA-F\-]{32,}\s*System\s*Jira'
    return re.sub(pattern, '', text)

def extract_story_identifier(text):
    # Search for US-XX, WOG-XX, OTEP-XX, USXX, WOGXX, OTEPXX
    match = re.search(r'\b(US|WOG|OTEP)-?(\d+[a-z]?)\b', text, re.IGNORECASE)
    if match:
        prefix = match.group(1).upper()
        number = match.group(2).lower()
        return f"{prefix}-{number}"
    return None

def extract_jira_id_from_text(text):
    # Look for OTEP-XX or WOG-XX or PROF-XX
    match = re.search(r'\b(OTEP|WOG|PROF)-\d+\b', text, re.IGNORECASE)
    if match:
        return match.group(0).upper()
    return None

def extract_local_jira_ids(filepath):
    story_to_jira = {}
    if not filepath or not os.path.exists(filepath):
        return story_to_jira
        
    print(f"Parsing existing local file {filepath} to extract Jira IDs...")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            in_table = False
            headers = []
            for line in f:
                line = line.strip()
                if line.startswith("|"):
                    cells = [c.strip() for c in line.split("|")[1:-1]]
                    if not in_table:
                        # Header row
                        headers = [re.sub(r'[*_`]', '', h).strip().lower() for h in cells]
                        in_table = True
                    elif cells and all(c.startswith("-") or c == "" for c in cells):
                        # Separator row
                        continue
                    else:
                        # Data row
                        row_dict = dict(zip(headers, cells))
                        # Find Jira ID column value
                        jira_id = ""
                        for k, v in row_dict.items():
                            if k in ["jira id", "jiraid"]:
                                jira_id = re.sub(r'[*_`]', '', v).strip()
                                break
                                
                        story_text = ""
                        for k, v in row_dict.items():
                            if k in ["story", "user story"]:
                                story_text = v.strip()
                                break
                                
                        if story_text and jira_id and "tbd" not in jira_id.lower():
                            cleaned_story = clean_jira_link_artifacts(story_text)
                            norm_story = normalize_story_text(cleaned_story)
                            story_to_jira[norm_story] = jira_id
                            
                            # Also extract by code if available in story text
                            story_id = extract_story_identifier(cleaned_story)
                            if story_id:
                                story_to_jira[story_id] = jira_id
                else:
                    in_table = False
    except Exception as e:
        print(f"Warning: Failed to parse existing local file: {e}")
                
    if story_to_jira:
        print(f"Extracted {len(story_to_jira)} mappings from local file.")
    return story_to_jira

def load_story_id_map():
    story_map = {}
    map_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "story-id-map.md")
    if not os.path.exists(map_path):
        print(f"Global story map not found at {map_path}")
        return story_map
        
    print(f"Loading global mappings from {map_path}...")
    try:
        with open(map_path, "r", encoding="utf-8") as f:
            in_table = False
            headers = []
            for line in f:
                line = line.strip()
                if line.startswith("|"):
                    cells = [c.strip() for c in line.split("|")[1:-1]]
                    if not in_table:
                        headers = [re.sub(r'[*_`]', '', h).strip().lower() for h in cells]
                        in_table = True
                    elif cells and all(c.startswith("-") or c == "" for c in cells):
                        continue
                    else:
                        if len(cells) > 0 and ("~~" in cells[0] or (len(cells) > 2 and "~~" in cells[2])):
                            continue
                        row_dict = dict(zip(headers, cells))
                        
                        jira_id = row_dict.get("jira id", "").strip()
                        jira_id = re.sub(r'[~*_`]', '', jira_id).strip()
                        
                        old_id = row_dict.get("old prd id", row_dict.get("old id", "")).strip()
                        old_id = re.sub(r'[~*_`]', '', old_id).strip()
                        
                        if jira_id and "tbd" not in jira_id.lower():
                            if old_id:
                                norm_old = extract_story_identifier(old_id)
                                if norm_old:
                                    story_map[norm_old] = jira_id
                else:
                    in_table = False
    except Exception as e:
        print(f"Warning: Failed to load global story map: {e}")
                
    if story_map:
        print(f"Loaded {len(story_map)} mappings from global story-id-map.")
    return story_map

class ConfluenceToMarkdownParser(HTMLParser):
    def __init__(self, story_to_jira=None):
        super().__init__()
        self.story_to_jira = story_to_jira if story_to_jira else {}
        self.markdown = []
        self.stack = []
        self.list_stack = []
        self.href_stack = []
        self.in_table = False
        self.table_rows = []
        self.current_row = []
        self.in_cell = False
        self.current_cell_markdown = []
        
        # Code block tracking
        self.in_code_block = False
        self.in_code_language_param = False
        self.code_block_language = ""
        self.code_block_data = []
        
        # Preformatted block tracking
        self.in_pre = False

        # Jira macro tracking
        self.in_jira_macro = False
        self.in_jira_key_param = False
        self.jira_macro_key = ""

    def append_output(self, text):
        if self.in_cell:
            self.current_cell_markdown.append(text)
        elif self.in_code_block:
            self.code_block_data.append(text)
        else:
            self.markdown.append(text)

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.stack.append(tag)
        
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self.append_output(f'\n\n{"#" * level} ')
        elif tag == 'p':
            self.append_output('\n\n')
        elif tag in ['strong', 'b']:
            self.append_output('**')
        elif tag in ['em', 'i']:
            self.append_output('*')
        elif tag == 'code':
            if not self.in_pre:
                self.append_output('`')
        elif tag == 'pre':
            self.in_pre = True
            self.append_output('\n\n```\n')
        elif tag == 'blockquote':
            self.append_output('\n\n> ')
        elif tag == 'ul':
            self.list_stack.append('ul')
            self.append_output('\n')
        elif tag == 'ol':
            self.list_stack.append(1)
            self.append_output('\n')
        elif tag == 'li':
            indent = '  ' * (len(self.list_stack) - 1)
            if self.list_stack:
                state = self.list_stack[-1]
                if state == 'ul':
                    self.append_output(f'{indent}- ')
                else:
                    self.append_output(f'{indent}{state}. ')
                    self.list_stack[-1] += 1
        elif tag == 'a':
            href = attrs_dict.get('href', '')
            self.append_output('[')
            self.href_stack.append(href)
        elif tag == 'br':
            self.append_output('\n')
        elif tag == 'table':
            self.in_table = True
            self.table_rows = []
        elif tag == 'tr':
            self.current_row = []
        elif tag in ['th', 'td']:
            self.in_cell = True
            self.current_cell_markdown = []
        elif tag == 'ac:structured-macro':
            macro_name = attrs_dict.get('ac:name', '')
            if macro_name == 'code':
                self.in_code_block = True
                self.code_block_language = ""
                self.code_block_data = []
            elif macro_name == 'jira':
                self.in_jira_macro = True
                self.in_jira_key_param = False
                self.jira_macro_key = ""
        elif tag == 'ac:parameter':
            param_name = attrs_dict.get('ac:name', '')
            if param_name == 'language':
                self.in_code_language_param = True
            elif param_name == 'key' and self.in_jira_macro:
                self.in_jira_key_param = True

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
            
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.append_output('\n\n')
        elif tag == 'p':
            self.append_output('\n\n')
        elif tag in ['strong', 'b']:
            self.append_output('**')
        elif tag in ['em', 'i']:
            self.append_output('*')
        elif tag == 'code':
            if not self.in_pre:
                self.append_output('`')
        elif tag == 'pre':
            self.in_pre = False
            self.append_output('\n```\n\n')
        elif tag == 'blockquote':
            self.append_output('\n\n')
        elif tag in ['ul', 'ol']:
            if self.list_stack:
                self.list_stack.pop()
            self.append_output('\n')
        elif tag == 'li':
            self.append_output('\n')
        elif tag == 'a':
            href = self.href_stack.pop() if self.href_stack else ''
            self.append_output(f']({href})')
        elif tag == 'table':
            self.in_table = False
            self.render_table()
        elif tag == 'tr':
            if self.in_table:
                self.table_rows.append(self.current_row)
        elif tag in ['th', 'td']:
            self.in_cell = False
            cell_content = "".join(self.current_cell_markdown).strip().replace('\n', ' ')
            self.current_row.append(cell_content)
        elif tag == 'ac:structured-macro':
            if self.in_code_block:
                code_content = "".join(self.code_block_data).strip()
                lang = self.code_block_language
                self.in_code_block = False
                self.append_output(f"\n\n```{lang}\n{code_content}\n```\n\n")
            elif self.in_jira_macro:
                # Emit the clean Jira key (e.g. OTEP-71) as plain text
                if self.jira_macro_key:
                    self.append_output(self.jira_macro_key)
                self.in_jira_macro = False
                self.in_jira_key_param = False
                self.jira_macro_key = ""
        elif tag == 'ac:parameter':
            self.in_code_language_param = False
            self.in_jira_key_param = False

    def handle_data(self, data):
        if self.in_code_language_param:
            self.code_block_language = data.strip()
        elif self.in_jira_key_param:
            # Capture the Jira issue key (e.g. OTEP-71)
            self.jira_macro_key = data.strip()
        elif self.in_jira_macro:
            # Suppress all other data inside a Jira macro (server name, UUID, etc.)
            pass
        else:
            self.append_output(data)

    def render_table(self):
        if not self.table_rows:
            return
        
        headers = self.table_rows[0]
        
        # Detect if this is a scope/stories table
        story_idx = -1
        jira_idx = -1
        
        for i, h in enumerate(headers):
            norm_h = re.sub(r'[*_`]', '', h).strip().lower()
            if norm_h in ['story', 'user story']:
                story_idx = i
            elif norm_h in ['jira id', 'jiraid']:
                jira_idx = i
                
        # If this is a scope table and is missing the Jira ID column, insert it
        if story_idx != -1 and jira_idx == -1:
            headers.insert(0, '**Jira ID**')
            story_idx += 1
            jira_idx = 0
            # Prepend an empty cell for all subsequent rows in table_rows
            for row in self.table_rows[1:]:
                row.insert(0, '')
                
        num_cols = max(len(row) for row in self.table_rows)
        if num_cols == 0:
            return
            
        # Map/enrich/clean each row if it's a scope table
        if story_idx != -1:
            for row_idx in range(1, len(self.table_rows)):
                row = self.table_rows[row_idx]
                while len(row) < num_cols:
                    row.append('')
                    
                story_cell = row[story_idx]
                
                # 1. Clean Confluence XHTML Jira link artifacts from story cell
                cleaned_story = clean_jira_link_artifacts(story_cell).strip()
                
                # 2. Match Jira ID via 4-tier strategy
                jira_id = None
                
                # Tier 1: Confluence Embedded Key (emitted by the Jira macro parser)
                embedded_key = extract_jira_id_from_text(cleaned_story)
                if embedded_key:
                    jira_id = embedded_key
                    # Strip the bare Jira key from the story cell so it doesn't appear as noise
                    cleaned_story = re.sub(
                        r'\s*\b' + re.escape(embedded_key) + r'\b\s*',
                        ' ', cleaned_story
                    ).strip()
                    
                row[story_idx] = cleaned_story
                
                # Tier 2: Local Exact Story Text Match
                if not jira_id:
                    norm_story = normalize_story_text(cleaned_story)
                    jira_id = self.story_to_jira.get(norm_story)
                    
                # Tier 3 & 4: Story ID / Global Map Match
                if not jira_id:
                    story_id = extract_story_identifier(cleaned_story)
                    if story_id:
                        jira_id = self.story_to_jira.get(story_id)
                        
                # 3. Populate Jira ID cell
                if jira_id:
                    if not (jira_id.startswith('**') and jira_id.endswith('**')):
                        jira_id = f"**{jira_id}**"
                    row[jira_idx] = jira_id
                else:
                    # Keep whatever was originally in there if non-empty
                    if not row[jira_idx]:
                        row[jira_idx] = ''
                        
        lines = []
        headers += [''] * (num_cols - len(headers))
        
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("|" + "---|"*num_cols)
        
        for row in self.table_rows[1:]:
            row += [''] * (num_cols - len(row))
            lines.append("| " + " | ".join(row) + " |")
            
        self.markdown.append("\n\n" + "\n".join(lines) + "\n\n")

    def get_markdown(self):
        content = "".join(self.markdown)
        # Clean up excessive newlines
        content = re.sub(r'\n{3,}', '\n\n', content)
        return content.strip()

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
    if len(sys.argv) < 2:
        print("Usage: ./pull-confluence-prd.py <PAGE_ID> [output_file]")
        print("Example: ./pull-confluence-prd.py 1976550683")
        sys.exit(1)
        
    page_id = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    load_env()
    site = os.environ.get("JIRA_SITE")
    if not site:
        sys.exit("Missing environment variable JIRA_SITE in .env.")
        
    base_url = f"https://{site}"
    auth = make_auth_header()
    
    url = f"{base_url}/wiki/rest/api/content/{page_id}?expand=body.storage,version,title"
    print(f"Fetching page {page_id} from {site}...")
    
    req = urllib.request.Request(url, headers={"Authorization": auth, "Accept": "application/json"})
    
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 401:
            sys.exit("Authentication failed. Check your JIRA_EMAIL and JIRA_API_TOKEN in .env.")
        if e.code == 404:
            sys.exit(f"Page {page_id} not found.")
        sys.exit(f"HTTP {e.code}: {e.reason} — {url}")
    except Exception as e:
        sys.exit(f"Error fetching page: {e}")

    title = data.get("title", "Untitled Page")
    storage_body = data.get("body", {}).get("storage", {}).get("value", "")
    
    if not out_file:
        # Generate default slugified file name
        slug = re.sub(r'[^\w\-]', '_', title.lower())
        slug = re.sub(r'_{2,}', '_', slug).strip('_')
        out_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "02-prd", f"{slug}.md")
        
    # Standardize output path to absolute path
    out_file = os.path.abspath(out_file)
    
    # 1. Load global mappings
    global_map = load_story_id_map()
    
    # 2. Extract mappings from existing local target file (if it exists)
    local_map = extract_local_jira_ids(out_file)
    
    # 3. Merge mappings (local takes precedence)
    merged_story_map = {}
    merged_story_map.update(global_map)
    merged_story_map.update(local_map)
    
    print(f"Parsing page content for '{title}'...")
    parser = ConfluenceToMarkdownParser(merged_story_map)
    parser.feed(storage_body)
    markdown_content = parser.get_markdown()
    
    # Prepend title as an H1 if not already there
    if not markdown_content.startswith("# "):
        markdown_content = f"# {title}\n\n{markdown_content}"
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(markdown_content + "\n")
        
    print(f"Successfully saved Confluence page to: {out_file}")

if __name__ == "__main__":
    main()
