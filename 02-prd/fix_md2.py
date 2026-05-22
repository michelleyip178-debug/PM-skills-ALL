import re

file_path = '/Users/michelleyip/Library/Mobile Documents/com~apple~CloudDocs/Documents/PM-skills-ALL-1/02-prd/prd-opportunities.md'
with open(file_path, 'r') as f:
    content = f.read()

# Fix remaining double newlines after bullets (some might have matched with \n\n instead of \n\s*\n)
content = re.sub(r'(- .*?)\n\n\s*(?=- )', r'\1\n', content)
content = re.sub(r'(- .*?)\n\n\s*(?=  - )', r'\1\n', content)
content = re.sub(r'(  - .*?)\n\n\s*(?=    - )', r'\1\n', content)
content = re.sub(r'(    - .*?)\n\n\s*(?=    - )', r'\1\n', content)
content = re.sub(r'(    - .*?)\n\n\s*(?=- )', r'\1\n', content)

# A more generic pass for list spacing
lines = content.split('\n')
new_lines = []
for i, line in enumerate(lines):
    if line.strip() == '' and i > 0 and i < len(lines) - 1:
        prev = lines[i-1].lstrip()
        nxt = lines[i+1].lstrip()
        if prev.startswith('- ') and nxt.startswith('- '):
            continue
    new_lines.append(line)

with open(file_path, 'w') as f:
    f.write('\n'.join(new_lines))

print("Done")
