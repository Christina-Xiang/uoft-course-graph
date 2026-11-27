#!/usr/bin/env python3
"""
Fix duplicated injection in MAT240H1, MAT247H1, MAT267H1, MAT309H1.
Pattern: inside correctionPair, between `insight:` and the closing `},`,
there was a full duplicate socratic/deductive/correction section injected.
Remove the duplicate and restore the proper closing.
"""

import re

TS_PATH = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/uoft-kg/src/data/courseSkills.ts"
TARGETS = ["MAT240H1", "MAT247H1", "MAT267H1", "MAT309H1"]

with open(TS_PATH) as f:
    content = f.read()

for cid in TARGETS:
    # Find course
    pattern = r'(\s+"' + re.escape(cid) + r'":\s*\[)'
    match = re.search(pattern, content)
    if not match:
        print(f"  ✗ {cid}: not found")
        continue

    course_start = match.end()

    # Find first skill boundaries using brace matching
    rest = content[course_start:]
    brace_depth = 0
    first_skill_end_abs = -1
    for i, ch in enumerate(rest):
        if ch == '{':
            brace_depth += 1
        elif ch == '}':
            brace_depth -= 1
            if brace_depth == 0:
                first_skill_end_abs = course_start + i + 1
                break

    if first_skill_end_abs < 0:
        print(f"  ✗ {cid}: cannot find first skill end")
        continue

    first_skill = content[course_start:first_skill_end_abs]

    # Check: does this skill have TWO socraticEntry lines (duplicate)?
    socratic_matches = list(re.finditer(r'^\s+socraticEntry:', first_skill, re.MULTILINE))
    if len(socratic_matches) < 2:
        print(f"  - {cid}: no duplicate ({len(socratic_matches)} socraticEntry)")
        continue

    print(f"  ✓ {cid}: found duplicate ({len(socratic_matches)} socraticEntry)")

    # The first socraticEntry is at socratic_matches[0].start()
    # The duplicate starts at socratic_matches[1].start() (within first_skill)
    dup_start = socratic_matches[1].start()

    # Everything between the first correctionPair insight and the proper end of correctionPair
    # should be removed, and then correctionPair closing restored.
    
    # Find the last `},` in first_skill that closes correctionPairCn (first injection)
    # Look for the pattern: insight: "...", then } that closes the nested object, 
    # then }, that we need to keep (correctionPairCn closing)

    # Find all correctionPairCn occurrences in the first skill
    all_cpcn = list(re.finditer(r'^\s+correctionPairCn:', first_skill, re.MULTILINE))
    if len(all_cpcn) < 2:
        print(f"  ✗ {cid}: cannot find original correctionPairCn ({len(all_cpcn)} found)")
        continue
    
    # The last one is the first injection's original correctionPairCn
    orig_cpcn_start = all_cpcn[-1].start()
    
    # Build clean first skill:
    # Keep everything through the first injection's insight,
    # add closing for correctionPair,
    # then keep the original correctionPairCn and skill closing
    clean = first_skill[:dup_start] + "            },\n" + first_skill[orig_cpcn_start:]
    
    # Update content
    new_content = content[:course_start] + clean + content[first_skill_end_abs:]
    
    old_len = len(first_skill)
    new_len = len(clean)
    print(f"    removed {old_len - new_len} chars ({old_len} → {new_len})")
    
    content = new_content

# Verify
opens = content.count('{')
closes = content.count('}')
print(f"\n✓ Brace balance: {opens} open, {closes} close" if opens == closes else f"\n✗ Brace imbalance: {opens} open, {closes} close")

with open(TS_PATH, "w") as f:
    f.write(content)
print(f"  Written ({len(content.splitlines())} lines)")
