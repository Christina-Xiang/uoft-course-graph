#!/usr/bin/env python3
"""
Complete rebuild of courseSkills.ts:
1. Keep rich courses (8) intact from current file
2. For 27 basic courses, replace first skill with properly formatted data from JSON dump
3. Inject socraticFlow/deductiveChain/correctionPair content
"""

import re, json

TS_PATH = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/uoft-kg/src/data/courseSkills.ts"
DATA_PATH = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/uoft-kg/scripts/course_skills_data.json"
BACKUP_PATH = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/courseSkills-backup.ts"

with open(DATA_PATH) as f:
    data = json.load(f)

with open(TS_PATH) as f:
    current = f.read()

with open(BACKUP_PATH) as f:
    backup = f.read()

# Rich courses to keep intact
RICH_COURSES = ["MAT137Y1", "MAT223H1", "MAT224H1", "MAT237Y1", "MAT244H1", "MAT301H1", "MAT315H1", "MAT334H1"]

# Target basic courses
TARGETS = [
    "MAT240H1", "MAT247H1", "MAT267H1", "MAT309H1",
    "STA130H1", "STA237H1", "STA238H1", "STA257H1", "STA261H1",
    "STA302H1", "STA303H1", "STA304H1", "STA314H1", "STA347H1", "STA410H1", "STA414H1",
    "CSC108H1", "CSC148H1", "CSC165H1", "CSC207H1", "CSC209H1",
    "CSC236H1", "CSC263H1", "CSC301H1", "CSC311H1", "CSC369H1", "CSC373H1",
]

# ── Generators (same as inject_skills_data.py) ──────────────────────────

def gen_socratic_flow(skill, course_id):
    label = skill.get("label", "")
    desc = skill.get("description", "")
    levels = skill.get("levels", [])
    tips = skill.get("practiceTips", [])
    q1 = (
        f"We're exploring {label}. Let's start simple: describe what you already understand "
        f"about this concept. No formal definitions — just plain intuition."
    )
    h1 = (
        f"Think back to the core idea of {course_id}. "
        f"What problem does {label} solve? Why was this concept invented?"
    )
    r1 = f"Good. The intuition you just described is exactly what the formal definition captures. {desc} The key is to connect your gut feeling with precise language."
    q2 = "Now let's test the boundary. Here's an edge case: " + (tips[0] if tips else "how does your understanding hold up when conditions change?")
    h2 = "Push your example to its limit. At what point does it break?"
    r2 = "Edge cases reveal the hidden assumptions. That's why the formal definition includes them."
    q3 = f"Here's a common mistake: {levels[1] if len(levels) > 1 else 'people get the direction wrong'}. Why is this tempting but incorrect?"
    h3 = "Trace through the logic step by step. Where does the error first appear?"
    r3 = "The mistake comes from over-generalising a pattern that works in simpler cases. The formal framework protects against this."
    q4 = "Now synthesise: take our three insights and apply them to a new problem. Construct an example where this skill is critical."
    h4 = "What's the simplest non-trivial case where this concept matters?"
    r4 = "You've now moved from recognition to application — the highest level of understanding."
    return [
        {"question": q1, "hint": h1, "resolution": r1},
        {"question": q2, "hint": h2, "resolution": r2},
        {"question": q3, "hint": h3, "resolution": r3},
        {"question": q4, "hint": h4, "resolution": r4},
    ]

def gen_socratic_flow_cn(skill):
    label = skill.get("labelCn", "")
    desc = skill.get("descriptionCn", "")
    levels = skill.get("levelsCn", [])
    return [
        {"question": f"我们来探讨 {label}。从一个简单问题开始：关于这个概念你已经理解了些什么？用大白话说就行，不用正式定义。",
         "hint": "回顾一下这个技能的初衷——它解决了什么问题？为什么需要这个概念？",
         "resolution": f"好。你刚才的直觉正是形式化定义要捕捉的。{desc}关键在于把你的直观感受和精确表达连接起来。"},
        {"question": "现在测试边界情况。你的理解在极端条件下还站得住吗？",
         "hint": "把你的例子推到极限——它在哪开始失效？",
         "resolution": "边界情况揭示了隐藏的假设。这正是形式化定义要覆盖的东西。"},
        {"question": f"这里有个常犯的错误：{levels[1] if len(levels) > 1 else '方向搞反了'}。这个错误看起来很有道理——但为什么不对？",
         "hint": "一步步跟踪逻辑。错误在哪一步开始出现的？",
         "resolution": "这个错误来源于对简单情况下有效模式的过度推广。形式化框架保护我们不受这种直觉陷阱的影响。"},
        {"question": "现在综合运用：结合我们刚才的三个洞见，解决一个新问题。构造一个例子，其中这个技能是关键的。",
         "hint": "这个概念的最简单的非平凡例子是什么？",
         "resolution": "你已从识别上升到应用——这是理解的最高层次。"},
    ]

def gen_deductive(skill):
    label = skill.get("label", "")
    levels = skill.get("levels", [])
    return {
        "from": f"Definition and basic properties related to {label}",
        "principle": f"The logical structure of {label}: each step follows from the definition and previously established facts.",
        "steps": levels[:5] if len(levels) >= 3 else [f"Start from the definition of {label}", f"Apply the basic property that follows immediately", f"Extend to more complex cases", f"Prove the main theorem", f"Verify with concrete examples"],
        "conclusion": f"Therefore, the theorem about {label} follows logically from the definitions alone — no additional assumptions needed."
    }

def gen_deductive_cn(skill):
    label = skill.get("labelCn", "")
    levels = skill.get("levelsCn", [])
    return {
        "from": f"关于 {label} 的定义和基本性质",
        "principle": f"{label} 的逻辑结构：每一步都从定义和已知事实推导而来",
        "steps": levels[:5] if len(levels) >= 3 else [f"从 {label} 的定义出发", "应用定义直接推导出的基本性质", "将上一步推广到更复杂的情形", "结合前面的步骤证明主要定理", "用具体例子验证"],
        "conclusion": f"因此，关于 {label} 的定理完全从定义出发逻辑推导而来——不需要额外假设。"
    }

def gen_correction(skill):
    label = skill.get("label", "")
    levels = skill.get("levels", [])
    common_error = levels[1] if len(levels) > 1 else f"Over-generalising {label} beyond its valid scope"
    return {
        "pitfall": f"Common error: {common_error}. This mistake is natural — it comes from extending a pattern that works in simple cases to situations where it no longer applies.",
        "socraticQuestion": f"Let's check with a concrete counterexample. Walk through your reasoning step by step. Where exactly does the pattern break? What assumption changed?",
        "insight": f"The key is to understand not just the pattern but its conditions. {common_error} fails because a hidden assumption no longer holds."
    }

def gen_correction_cn(skill):
    label = skill.get("labelCn", "")
    levels = skill.get("levelsCn", [])
    common_error = levels[1] if len(levels) > 1 else f"不恰当地推广了 {label} 的适用范围"
    return {
        "pitfall": f"常见错误：{common_error}。这个错误很自然——它是将简单情况下有效的模式推广到了不适用的情况。",
        "socraticQuestion": f"让我们用一个具体的反例来验证。一步步跟踪你的推理——模式在哪里开始失效？哪个假设变了？",
        "insight": f"关键不只是理解模式本身，而是理解它的适用条件。{common_error} 之所以失败，是因为一个隐藏的假设不再成立。"
    }

def gen_entry(skill):
    label = skill.get("label", "")
    desc = skill.get("description", "")
    return f"Let's explore {label}. {desc[:100]}"

def gen_entry_cn(skill):
    label = skill.get("labelCn", "")
    desc = skill.get("descriptionCn", "")
    return f"我们来探索 {label}。{desc[:100]}"


def fmt_ts_value(v, indent=0):
    """Format a Python value as TypeScript literal with proper indentation."""
    sp = "  " * indent
    if isinstance(v, dict):
        items = []
        for k, val in v.items():
            items.append(f"{sp}  {k}: {fmt_ts_value(val, indent+1)}")
        return "{\n" + ",\n".join(items) + f"\n{sp}}}"
    elif isinstance(v, list):
        if not v:
            return "[]"
        items = [fmt_ts_value(item, indent+1) for item in v]
        if len(items) <= 2 and all(len(item) < 80 for item in items):
            return f"[{', '.join(items)}]"
        return "[\n" + ",\n".join(items) + f"\n{sp}]"
    elif isinstance(v, str):
        # JSON-escape the string for TS
        escaped = v.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
        return f'"{escaped}"'
    elif v is None:
        return "null"
    return str(v)


def build_skill_ts(skill, cid):
    """Build full TypeScript for a skill with injected fields."""
    indent = "      "
    inner = "        "
    lines = []
    lines.append(f"{indent}{{")
    
    # Basic fields
    fields = [
        ("id", skill["id"]),
        ("label", skill["label"]),
        ("labelCn", skill["labelCn"]),
        ("category", skill["category"]),
        ("categoryName", skill["categoryName"]),
        ("categoryNameCn", skill["categoryNameCn"]),
        ("difficulty", skill["difficulty"]),
        ("relatedUnits", skill.get("relatedUnits", [])),
        ("description", skill["description"]),
        ("descriptionCn", skill["descriptionCn"]),
        ("levels", skill["levels"]),
        ("levelsCn", skill["levelsCn"]),
        ("practiceTips", skill.get("practiceTips", [])),
        ("practiceTipsCn", skill.get("practiceTipsCn", [])),
    ]
    
    for name, val in fields:
        lines.append(f"{inner}{name}: {fmt_ts_value(val, 2)},")
    
    # Injected fields
    socratic_entry = gen_entry(skill)
    socratic_entry_cn = gen_entry_cn(skill)
    socratic_flow = gen_socratic_flow(skill, cid)
    socratic_flow_cn = gen_socratic_flow_cn(skill)
    deductive = gen_deductive(skill)
    deductive_cn = gen_deductive_cn(skill)
    correction = gen_correction(skill)
    correction_cn = gen_correction_cn(skill)
    
    injected = [
        ("socraticEntry", socratic_entry),
        ("socraticEntryCn", socratic_entry_cn),
        ("socraticFlow", socratic_flow),
        ("socraticFlowCn", socratic_flow_cn),
        ("deductiveChain", deductive),
        ("deductiveChainCn", deductive_cn),
        ("correctionPair", correction),
        ("correctionPairCn", correction_cn),
    ]
    
    for name, val in injected:
        lines.append(f"{inner}{name}: {fmt_ts_value(val, 2)},")
    
    lines.append(f"{indent}}},")
    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────

def find_array_end(content, start):
    """Given the position right after `[`, find the matching `]` position."""
    depth = 1
    i = start
    while i < len(content) and depth > 0:
        if content[i] == '[':
            depth += 1
        elif content[i] == ']':
            depth -= 1
        i += 1
    return i

def find_first_skill_end(content, array_start):
    """Find where the first skill object ends within a course array."""
    depth = 0
    for i in range(array_start, len(content)):
        c = content[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i + 1  # position after the closing }
    return array_start

def find_course_id(content, pos):
    """Find course ID at or near position pos."""
    # Look backward for a quoted word followed by ": ["
    m = re.search(r'"(\w+)"\s*:\s*\[', content[max(0,pos-50):pos+10])
    if m:
        return m.group(1)
    return None

# Find all course entries in the file (in order)
course_pattern = re.compile(r'"(\w+H?\d*)"\s*:\s*\[')
all_matches = list(course_pattern.finditer(current))

result = ""
last_end = 0

for m in all_matches:
    cid = m.group(1)
    start = m.start()
    array_start = m.end()
    array_end = find_array_end(current, array_start)
    
    print(f"  {cid}: pos {start}-{array_end} ({array_end-start} chars)", end="")
    
    if start > last_end:
        # Add content between previous course and this one
        result += current[last_end:start]
    
    if cid in RICH_COURSES:
        # Keep intact
        result += current[start:array_end]
        print(" → kept intact")
    elif cid in TARGETS:
        # Rebuild with injected data
        entry = data.get(cid)
        if entry and entry.get("skills"):
            skills = entry["skills"]
            first_skill_end = find_first_skill_end(current, array_start)
            
            course_content = f'  "{cid}": [\n'
            course_content += build_skill_ts(skills[0], cid) + "\n"
            # Add remaining skills from current file (after first skill)
            remaining = current[first_skill_end:array_end].strip()
            if remaining.startswith(","):
                remaining = remaining[1:].lstrip()
            if remaining:
                course_content += remaining + "\n"
            course_content += "  ]"
            
            result += course_content
            print(" → rebuilt")
        else:
            result += current[start:array_end]
            print(" → no data, kept original")
    else:
        # Unknown course, keep intact
        result += current[start:array_end]
        print(" → unknown, kept intact")
    
    last_end = array_end

# Add remaining content
result += current[last_end:]

# Write
with open(TS_PATH, "w") as f:
    f.write(result)

# Verify
opens = result.count('{')
closes = result.count('}')
print(f"\nBrace balance: {opens} open, {closes} close" + (" ✓" if opens == closes else " ✗"))
print(f"Written ({len(result.splitlines())} lines)")
