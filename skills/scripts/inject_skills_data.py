#!/usr/bin/env python3
"""
Inject socraticFlow, deductiveChain, correctionPair into courseSkills.ts
for all 27 courses that are missing them.
Reads existing skill descriptions and generates pedagogically meaningful content.
"""

import re, json, os

TS_PATH = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/uoft-kg/src/data/courseSkills.ts"
DATA_PATH = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/uoft-kg/scripts/course_skills_data.json"

with open(DATA_PATH) as f:
    data = json.load(f)

with open(TS_PATH) as f:
    ts = f.read()

# ── content generators ──────────────────────────────────────────────────

def gen_socratic_flow(skill, course_id):
    """Generate 4-step socraticFlow from skill description/levels."""
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
    r1 = (
        f"Good. The intuition you just described is exactly what the formal definition captures. "
        f"{desc} The key is to connect your gut feeling with precise language."
    )

    q2 = (
        "Now let's test the boundary. Here's an edge case: "
        + (tips[0] if tips else "how does your understanding hold up when conditions change?")
    )
    h2 = "Push your example to its limit. At what point does it break?"
    r2 = f"Edge cases reveal the hidden assumptions. That's why the formal definition includes them."

    q3 = f"Here's a common mistake: {levels[1] if len(levels) > 1 else 'people get the direction wrong'}. Why is this tempting but incorrect?"
    h3 = "Trace through the logic step by step. Where does the error first appear?"
    r3 = "The mistake comes from over-generalising a pattern that works in simpler cases. The formal framework protects against this."

    q4 = (
        "Now synthesise: take our three insights and apply them to a new problem. "
        "Construct an example where this skill is critical."
    )
    h4 = "What's the simplest non-trivial case where this concept matters?"
    r4 = "You've now moved from recognition to application — the highest level of understanding."

    flow = [
        {"question": q1, "hint": h1, "resolution": r1},
        {"question": q2, "hint": h2, "resolution": r2},
        {"question": q3, "hint": h3, "resolution": r3},
        {"question": q4, "hint": h4, "resolution": r4},
    ]
    return flow


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
        "steps": levels[:5] if len(levels) >= 3 else [
            f"Start from the definition of {label}",
            f"Apply the basic property that follows immediately",
            f"Extend to more complex cases using step 2",
            f"Prove the main theorem by combining steps 1-3",
            f"Verify with concrete examples"
        ],
        "conclusion": f"Therefore, the theorem about {label} follows logically from the definitions alone — no additional assumptions needed."
    }


def gen_deductive_cn(skill):
    label = skill.get("labelCn", "")
    levels = skill.get("levelsCn", [])
    return {
        "from": f"关于 {label} 的定义和基本性质",
        "principle": f"{label} 的逻辑结构：每一步都从定义和已知事实推导而来",
        "steps": levels[:5] if len(levels) >= 3 else [
            f"从 {label} 的定义出发",
            f"应用定义直接推导出的基本性质",
            f"将第 2 步推广到更复杂的情形",
            f"结合 1-3 步证明主要定理",
            f"用具体例子验证"
        ],
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


# ── JSON → TS formatter ────────────────────────────────────────────────

def fmt_json(obj, indent=0):
    """Format a Python object as TypeScript-compatible literal string."""
    sp = "  " * indent
    sp1 = "  " * (indent + 1)
    if isinstance(obj, dict):
        items = []
        for k, v in obj.items():
            val = fmt_json(v, indent + 1)
            items.append(f"{sp1}{k}: {val}")
        return "{\n" + ",\n".join(items) + f"\n{sp}}}"
    elif isinstance(obj, list):
        items = [fmt_json(item, indent + 1) for item in obj]
        if len(items) <= 2:
            inner = ", ".join(items)
            return f"[{inner}]"
        return "[\n" + ",\n".join(items) + f"\n{sp}]"
    elif isinstance(obj, str):
        escaped = obj.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
        return f'"{escaped}"'
    elif obj is None:
        return "null"
    else:
        return str(obj)


# ── injection ───────────────────────────────────────────────────────────

def inject_section(source, course_id, section_name, new_lines):
    """Find the insertion point after the last top-level field in the first skill."""
    pattern = r'(\s+"' + re.escape(course_id) + r'":\s*\[)'
    match = re.search(pattern, source)
    if not match:
        print(f"  ✗ {course_id}: not found in courseSkills.ts")
        return source, False

    course_start = match.end()
    rest = source[course_start:]

    # Find first skill boundaries via brace matching
    brace_depth = 0
    first_skill_end = -1
    for i, ch in enumerate(rest):
        if ch == '{':
            brace_depth += 1
        elif ch == '}':
            brace_depth -= 1
            if brace_depth == 0:
                first_skill_end = i + 1
                break
    if first_skill_end < 0:
        print(f"  ✗ {course_id}: cannot find first skill closing brace")
        return source, False

    first_skill = rest[:first_skill_end]

    # Check if socraticEntry already exists in first_skill
    if re.search(r'^\s+(?:")?socraticEntry(?:")?:', first_skill, re.MULTILINE):
        return source, True

    # Find the closing of the skill object (last `}` at depth 1)
    # Insert new fields right before it
    depth = 0
    last_top_level_close = -1
    
    for i, ch in enumerate(first_skill):
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                last_top_level_close = i
    
    if last_top_level_close < 0:
        print(f"  ✗ {course_id}: cannot find skill object closing")
        return source, False

    insert_abs = course_start + last_top_level_close

    # Check if the last field before } has a trailing comma
    before_close = source[course_start:insert_abs].rstrip()
    if before_close and before_close[-1] != ',':
        # No trailing comma — add one, then newlines + injected content
        prefix = ",\n"
    else:
        prefix = "\n"
    
    source = source[:insert_abs] + prefix + new_lines + "\n" + source[insert_abs:]
    print(f"  ✓ {course_id}: {section_name} injected")
    return source, True

    last_field = fields[-1]

    # Build regex: find the last field and its value extending to the next top-level field or object close
    field_name_re = r'(?:"' + re.escape(last_field) + r'"|' + re.escape(last_field) + r')'
    value_re = (
        r'^ {0,' + str(base_indent + 2) + r'}' + field_name_re + r':'
        r'[\s\S]*?(?=\n {0,' + str(base_indent + 2) + r'}"?\w+"?\s*:|\n\s*\},|\Z)'
    )
    value_match = re.search(value_re, first_skill_text)
    if not value_match:
        # Fallback: match everything from last field to end
        value_re2 = r'^.*?' + field_name_re + r':[\s\S]*'
        value_match = re.search(value_re2, first_skill_text)
        if not value_match:
            print(f"  ✗ {course_id}: cannot locate last field '{last_field}'")
            return source, False

    field_end = course_start + value_match.end()
    line_end = source.find("\n", field_end)
    if line_end == -1:
        line_end = len(source)

    insert_pos = line_end + 1

    # Ensure the previous field line ends with a comma (it was last before injection)
    prev_line_start = source.rfind("\n", 0, insert_pos - 2)
    if prev_line_start >= 0:
        prev_line = source[prev_line_start:insert_pos]
        stripped = prev_line.rstrip()
        if not stripped.endswith(","):
            # Add comma at end of previous field's value
            source = source[:insert_pos - 1] + "," + source[insert_pos - 1:]
            insert_pos += 1

    source = source[:insert_pos] + "\n" + new_lines + source[insert_pos:]
    print(f"  ✓ {course_id}: {section_name} injected (after '{last_field}')")
    return source, True


def process_course(source, cid):
    entry = data.get(cid)
    if not entry:
        print(f"  ✗ {cid}: no data in JSON dump")
        return source

    skills = entry.get("skills", [])
    if not skills:
        print(f"  ✗ {cid}: no skills in data")
        return source

    first = skills[0]

    # Check if rich course data exists in JSON dump
    soc = entry.get("socratic", {})
    ded = entry.get("deductive", {})
    corr = entry.get("correction", {})
    has_rich_data = bool(soc.get("flow")) and bool(ded.get("chain")) and bool(corr.get("pair"))

    if has_rich_data:
        # Use real data from JSON dump
        socratic_entry = soc.get("entry", gen_entry(first))
        socratic_entry_cn = soc.get("entryCn", gen_entry_cn(first))
        socratic_flow = soc.get("flow", gen_socratic_flow(first, cid))
        socratic_flow_cn = soc.get("flowCn", gen_socratic_flow_cn(first))
        deductive = ded.get("chain", gen_deductive(first))
        deductive_cn = ded.get("chainCn", gen_deductive_cn(first))
        correction = corr.get("pair", gen_correction(first))
        correction_cn = corr.get("pairCn", gen_correction_cn(first))
    else:
        # Generate content
        socratic_entry = gen_entry(first)
        socratic_entry_cn = gen_entry_cn(first)
        socratic_flow = gen_socratic_flow(first, cid)
        socratic_flow_cn = gen_socratic_flow_cn(first)
        deductive = gen_deductive(first)
        deductive_cn = gen_deductive_cn(first)
        correction = gen_correction(first)
        correction_cn = gen_correction_cn(first)

    parts = [
        f"      socraticEntry: {fmt_json(socratic_entry)},",
        f"      socraticEntryCn: {fmt_json(socratic_entry_cn)},",
        f"      socraticFlow: {fmt_json(socratic_flow, 6)},",
        f"      socraticFlowCn: {fmt_json(socratic_flow_cn, 6)},",
        f"      deductiveChain: {fmt_json(deductive, 6)},",
        f"      deductiveChainCn: {fmt_json(deductive_cn, 6)},",
        f"      correctionPair: {fmt_json(correction, 6)},",
        f"      correctionPairCn: {fmt_json(correction_cn, 6)},",
    ]
    new_section = "\n".join(parts)

    source, ok = inject_section(source, cid, "socratic/deductive/correction", new_section)
    return source


RICH_COURSES = [
    "MAT137Y1", "MAT223H1", "MAT224H1", "MAT237Y1",
    "MAT244H1", "MAT301H1", "MAT315H1", "MAT334H1",
]

BASIC_COURSES = [
    "MAT240H1", "MAT247H1", "MAT267H1", "MAT309H1",
    "STA130H1", "STA237H1", "STA238H1", "STA257H1", "STA261H1",
    "STA302H1", "STA303H1", "STA304H1", "STA314H1", "STA347H1", "STA410H1", "STA414H1",
    "CSC108H1", "CSC148H1", "CSC165H1", "CSC207H1", "CSC209H1",
    "CSC236H1", "CSC263H1", "CSC301H1", "CSC311H1", "CSC369H1", "CSC373H1",
]

TARGETS = RICH_COURSES + BASIC_COURSES

def main():
    source = ts
    print("Injecting missing socraticFlow/deductiveChain/correctionPair:\n")
    for cid in TARGETS:
        source = process_course(source, cid)

    with open(TS_PATH, "w") as f:
        f.write(source)

    print(f"\nVerification: TypeScript file written ({len(source.splitlines())} lines)")

if __name__ == "__main__":
    main()
