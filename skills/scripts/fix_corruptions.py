#!/usr/bin/env python3
"""
Fix corrupted practiceTipsCn arrays by extracting correct values from the backup file.
"""

import re

TS_PATH = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/uoft-kg/src/data/courseSkills.ts"
BACKUP_PATH = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/courseSkills-backup.ts"

with open(TS_PATH) as f:
    current = f.read()

with open(BACKUP_PATH) as f:
    backup = f.read()

TARGETS = [
    "MAT240H1", "MAT247H1", "MAT267H1", "MAT309H1",
    "STA130H1", "STA237H1", "STA238H1", "STA257H1", "STA261H1",
    "STA302H1", "STA303H1", "STA304H1", "STA314H1", "STA347H1", "STA410H1", "STA414H1",
    "CSC108H1", "CSC148H1", "CSC165H1", "CSC207H1", "CSC209H1",
    "CSC236H1", "CSC263H1", "CSC301H1", "CSC311H1", "CSC369H1", "CSC373H1",
]

def get_first_skill_ptc(content, cid):
    """Find the practiceTipsCn value (including field name through closing ]) in the FIRST skill."""
    pattern = r'(\s+"' + re.escape(cid) + r'":\s*\[)'
    match = re.search(pattern, content)
    if not match:
        return None
    
    course_start = match.end()
    rest = content[course_start:]
    
    # Find first skill
    depth = 0
    first_skill_end = -1
    for i, ch in enumerate(rest):
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                first_skill_end = i + 1
                break
    
    if first_skill_end < 0:
        return None
    
    first_skill = rest[:first_skill_end]
    
    # Find practiceTipsCn field
    ptc_pattern = r'(^\s*"?practiceTipsCn"?\s*:\s*)\[([\s\S]*?)(\]\s*,?\s*$)'
    ptc_match = re.search(ptc_pattern, first_skill, re.MULTILINE)
    if ptc_match:
        return ptc_match.group(0)  # Full match including field name
    
    # Try multiline array
    for pattern in [
        r'("?practiceTipsCn"?\s*:\s*\[[\s\S]*?\])',
        r'(practiceTipsCn\s*:\s*\[[\s\S]*?\])'
    ]:
        m = re.search(pattern, first_skill)
        if m:
            return m.group(1)
    
    return None

# Extract correct practiceTipsCn values from backup for each target
correct_values = {}
for cid in TARGETS:
    val = get_first_skill_ptc(backup, cid)
    if val:
        correct_values[cid] = val
    else:
        print(f"  ✗ {cid}: no practiceTipsCn in backup")

print(f"Found {len(correct_values)} practiceTipsCn values in backup")

# Now fix the current file
fixes = 0
for cid, correct_ptc in correct_values.items():
    pattern = r'(\s+"' + re.escape(cid) + r'":\s*\[)'
    match = re.search(pattern, current)
    if not match:
        print(f"  ✗ {cid}: not found in current")
        continue
    
    course_start = match.end()
    rest = current[course_start:]
    
    # Find first skill
    depth = 0
    first_skill_end = -1
    for i, ch in enumerate(rest):
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                first_skill_end = i + 1
                break
    
    if first_skill_end < 0:
        print(f"  ✗ {cid}: cannot find first skill")
        continue
    
    first_skill = rest[:first_skill_end]
    
    # Find corrupted practiceTipsCn
    corr_patterns = [
        r'(practiceTipsCn\s*:\s*)\[\s*\n+\s*(socraticEntry)',
        r'("practiceTipsCn"\s*:\s*)\[\s*\n+\s*(socraticEntry)',
    ]
    
    corr_match = None
    for pat in corr_patterns:
        corr_match = re.search(pat, first_skill)
        if corr_match:
            break
    
    if not corr_match:
        print(f"  - {cid}: not corrupted")
        continue
    
    # Fix: replace from practiceTipsCn to socraticEntry
    ptc_start_abs = course_start + corr_match.start(1)
    socratic_start_abs = course_start + corr_match.start(2)
    
    # The correct ptc ends with ], - remove the trailing comma if present
    clean_ptc = correct_ptc.rstrip().rstrip(',')
    
    # Remove the field name part from correct_ptc to avoid doubling
    # It already includes the field name and value
    
    # Replace: from ptc field to the start of socraticEntry
    # Insert: correct_ptc + , + newline
    replacement = current[:ptc_start_abs] + clean_ptc + ",\n" + current[socratic_start_abs:]
    current = replacement
    fixes += 1
    print(f"  ✓ {cid}: fixed")

print(f"\nTotal fixes: {fixes}")

# Verify
opens = current.count('{')
closes = current.count('}')
print(f"Brace balance: {opens} open, {closes} close" + (" ✓" if opens == closes else " ✗"))

with open(TS_PATH, "w") as f:
    f.write(current)

print(f"Written ({len(current.splitlines())} lines)")
