#!/usr/bin/env python3
import os
import sys
import json
import csv
import urllib.request
import urllib.parse
from base64 import b64encode

def load_env():
    """Load credentials from the .env file in the parent directory."""
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if line.strip() and not line.strip().startswith('#'):
                    key, val = line.strip().split('=', 1)
                    os.environ[key] = val

def fetch_jira_issues(jql, max_results=100):
    """Fetch issues from Jira using the provided JQL query."""
    load_env()
    site = os.environ.get('JIRA_SITE')
    email = os.environ.get('JIRA_EMAIL')
    token = os.environ.get('JIRA_API_TOKEN')

    if not all([site, email, token]):
        print("Missing Jira credentials in .env file. Please ensure JIRA_SITE, JIRA_EMAIL, and JIRA_API_TOKEN are set.")
        sys.exit(1)

    auth_str = f"{email}:{token}"
    b64_auth = b64encode(auth_str.encode('ascii')).decode('ascii')
    
    url = f"https://{site}/rest/api/3/search"
    params = {
        'jql': jql,
        'maxResults': max_results,
        'fields': 'summary,status,project,assignee,created,updated'
    }
    
    req = urllib.request.Request(f"{url}?{urllib.parse.urlencode(params)}")
    req.add_header('Authorization', f'Basic {b64_auth}')
    req.add_header('Accept', 'application/json')
    
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: ./pull_jira_data.py \"<JQL_QUERY>\" [output_file]")
        print("Example: ./pull_jira_data.py \"project = JIRATEST ORDER BY created DESC\" output.csv")
        sys.exit(1)
        
    jql = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    print(f"Fetching issues for JQL: {jql} ...")
    data = fetch_jira_issues(jql)
    issues = data.get('issues', [])
    
    print(f"Found {len(issues)} issues.")
    
    if not issues:
        return
        
    if out_file:
        if out_file.endswith('.csv'):
            with open(out_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Key', 'Summary', 'Status', 'Project', 'Assignee', 'Created'])
                for i in issues:
                    fields = i.get('fields', {})
                    assignee = fields.get('assignee')
                    assignee_name = assignee.get('displayName') if assignee else 'Unassigned'
                    writer.writerow([
                        i.get('key'),
                        fields.get('summary'),
                        fields.get('status', {}).get('name'),
                        fields.get('project', {}).get('name'),
                        assignee_name,
                        fields.get('created')
                    ])
            print(f"Data successfully saved to {out_file}")
        elif out_file.endswith('.json'):
            with open(out_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            print(f"Data successfully saved to {out_file}")
        else:
            print(f"Unsupported file format for {out_file}. Please use .csv or .json")
    else:
        # Just print the results if no output file is provided
        print("-" * 60)
        for i in issues:
            fields = i.get('fields', {})
            print(f"[{i.get('key')}] {fields.get('summary')} ({fields.get('status', {}).get('name')})")
        print("-" * 60)

if __name__ == '__main__':
    main()
