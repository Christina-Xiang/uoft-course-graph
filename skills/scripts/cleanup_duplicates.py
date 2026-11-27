#!/usr/bin/env python3
"""Remove duplicated socratic/deductive/correction sections from 4 math courses in courseSkills.ts"""

TS_PATH = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/uoft-kg/src/data/courseSkills.ts"
TARGETS = ["MAT240H1", "MAT247H1", "MAT267H1", "MAT309H1"]

with open(TS_PATH) as f:
    content = f.read()

import re

for cid in TARGETS:
    # Find the course
    pattern = r'(\s+"' + re.escape(cid) + r'":\s*\[)'
    match = re.search(pattern, content)
    if not match:
        print(f"  ✗ {cid}: not found")
        continue

    course_start = match.end()
    rest = content[course_start:]

    # Find first skill: brace count to find full first skill text
    brace_depth = 0
    first_skill_end = -1
    for i, ch in enumerate(rest):
        if ch == '{':
            brace_depth += 1
        elif ch == '}':
            brace_depth -= 1
        if brace_depth == 0 and i > 0:
            first_skill_end = i + 1  # include the closing comma if any
            break

    if first_skill_end < 0:
        print(f"  ✗ {cid}: cannot find first skill end")
        continue

    first_skill = rest[:first_skill_end]

    # Find the second socraticEntry (the duplicated one)
    socratic_indices = [m.start() for m in re.finditer(r'^\s+socraticEntry:', first_skill, re.MULTILINE)]
    if len(socratic_indices) < 2:
        print(f"  - {cid}: no duplicate found ({len(socratic_indices)} socraticEntry)")
        continue

    # Find "},$" (closing of first skill) that is more than 4 chars from end
    # Actually, find the second-to-last }, before the next skill
    
    # The duplicated section starts at the second socraticEntry
    dup_start = socratic_indices[1]

    # The duplicated section should end before the first skill's proper closing: "    },\n    {"
    # Find the next skill start or array end
    skill_close_match = re.search(r'\n\s*\},\s*\n\s*\{', first_skill[dup_start:])
    if skill_close_match:
        dup_end = dup_start + skill_close_match.start()
    else:
        dup_end = len(first_skill)

    # Remove the duplicated section
    new_first_skill = first_skill[:dup_start] + first_skill[dup_end:]
    
    # Now the first skill should end with correctionPairCn's closing "}," followed by "    },\n    {"
    # Let's verify: look for the pattern of correctionPairCn closing + skill closing with no extra fields

    # Update content
    abs_end = course_start + len(new_first_skill)
    new_content = content[:course_start] + new_first_skill + content[course_start + first_skill_end:]

    # Count changes
    old_len = len(first_skill)
    new_len = len(new_first_skill)
    print(f"  ✓ {cid}: removed {old_len - new_len} characters ({len(first_skill.splitlines())} - {len(new_first_skill.splitlines())} lines)")

    content = new_content

# Verify TypeScript syntax
# Quick check: count opening/closing braces
opens = content.count('{')
closes = content.count('}')
if opens == closes:
    print(f"\n✓ Brace balance: {opens} open, {closes} close")
else:
    print(f"\n✗ Brace imbalance: {opens} open, {closes} close")

with open(TS_PATH, "w") as f:
    f.write(content)

print(f"\n  Written ({len(content.splitlines())} lines)")
