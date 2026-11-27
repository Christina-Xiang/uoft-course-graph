#!/usr/bin/env python3
"""Fix missing commas before socraticEntry fields in courseSkills.ts"""

TS_PATH = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/uoft-kg/src/data/courseSkills.ts"

with open(TS_PATH) as f:
    content = f.read()

import re

# Pattern: line ending with ] or " (end of value) followed by newline + socraticEntry
# Missing comma between them
count = 0

# Fix: add comma before \n\s+socraticEntry: if previous line doesn't end with comma
# Or more precisely: find lines ending with `]` followed by `\n\s+socraticEntry:`
pattern = r'(\]\n)(\s+socraticEntry:)'
replacement = r'],\n\2'
new_content, count = re.subn(pattern, replacement, content)
print(f"Fixed {count} missing commas before socraticEntry")

# Also check for other injected fields like socraticFlow, deductiveChain, etc.
for field in ['socraticEntryCn', 'socraticFlow', 'socraticFlowCn', 'deductiveChain', 'deductiveChainCn', 'correctionPair', 'correctionPairCn']:
    pattern = r'(\]\n)(\s+' + re.escape(field) + r':)'
    sub_count = 0
    new_content, sub_count = re.subn(pattern, new_content, replacement)
    if sub_count:
        print(f"Fixed {sub_count} missing commas before {field}")

# Also fix `}\n\s+field:` patterns (for objects ending with })
pattern2 = r'(\}\n)(\s+socraticEntry:)'
replacement2 = r'},\n\2'
new_content, count2 = re.subn(pattern2, new_content, replacement2)
print(f"Fixed {count2} missing commas after }}")

for field in ['socraticEntryCn', 'socraticFlow', 'socraticFlowCn', 'deductiveChain', 'deductiveChainCn', 'correctionPair', 'correctionPairCn']:
    pattern = r'(\}\n)(\s+' + re.escape(field) + r':)'
    sub_count = 0
    new_content, sub_count = re.subn(pattern, new_content, replacement2)
    if sub_count:
        print(f"Fixed {sub_count} missing commas after }} before {field}")

# Verify brace balance
opens = new_content.count('{')
closes = new_content.count('}')
print(f"\nBrace balance: {opens} open, {closes} close" + (" ✓" if opens == closes else " ✗"))

with open(TS_PATH, "w") as f:
    f.write(new_content)

print(f"Written ({len(new_content.splitlines())} lines)")
