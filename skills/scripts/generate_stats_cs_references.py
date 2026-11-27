#!/usr/bin/env python3
"""Generate rich reference files for STA and CS courses using domain tables."""

import json, os, re

SKILLS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(SKILLS_DIR)
DATA_JSON = os.path.join(PROJECT_DIR, "scripts", "course_skills_data.json")
TABLES_JSON = os.path.join(PROJECT_DIR, "scripts", "stats_cs_domain_tables.json")

with open(DATA_JSON) as f:
    skills_data = json.load(f)
with open(TABLES_JSON) as f:
    domain_tables = json.load(f)

COURSES = {
    "STA130H1": {"name": "An Introduction to Statistical Reasoning and Data Science", "domain": "stats-intro", "area": "stats"},
    "STA237H1": {"name": "Probability, Statistics and Data Analysis I", "domain": "stats-probability", "area": "stats"},
    "STA238H1": {"name": "Probability, Statistics and Data Analysis II", "domain": "stats-inference", "area": "stats"},
    "STA257H1": {"name": "Probability and Statistics I", "domain": "stats-probability", "area": "stats"},
    "STA261H1": {"name": "Probability and Statistics II", "domain": "stats-inference", "area": "stats"},
    "STA302H1": {"name": "Methods of Data Analysis I", "domain": "stats-regression", "area": "stats"},
    "STA303H1": {"name": "Methods of Data Analysis II", "domain": "stats-regression", "area": "stats"},
    "STA304H1": {"name": "Surveys, Sampling and Observational Data", "domain": "stats-surveys", "area": "stats"},
    "STA314H1": {"name": "Statistical Methods for Machine Learning I", "domain": "stats-ml", "area": "stats"},
    "STA347H1": {"name": "Probability", "domain": "stats-probability", "area": "stats"},
    "STA410H1": {"name": "Statistical Computation", "domain": "stats-computation", "area": "stats"},
    "STA414H1": {"name": "Statistical Methods for Machine Learning II", "domain": "stats-ml", "area": "stats"},
    "CSC108H1": {"name": "Introduction to Computer Programming", "domain": "cs-intro", "area": "cs"},
    "CSC148H1": {"name": "Introduction to Computer Science", "domain": "cs-data-structures", "area": "cs"},
    "CSC165H1": {"name": "Mathematical Expression and Reasoning for CS", "domain": "cs-theory", "area": "cs"},
    "CSC207H1": {"name": "Software Design", "domain": "cs-software", "area": "cs"},
    "CSC209H1": {"name": "Software Tools and Systems Programming", "domain": "cs-systems", "area": "cs"},
    "CSC236H1": {"name": "Introduction to the Theory of Computation", "domain": "cs-theory", "area": "cs"},
    "CSC263H1": {"name": "Data Structures and Analysis", "domain": "cs-data-structures", "area": "cs"},
    "CSC301H1": {"name": "Introduction to Software Engineering", "domain": "cs-software", "area": "cs"},
    "CSC311H1": {"name": "Introduction to Machine Learning", "domain": "cs-ml", "area": "cs"},
    "CSC369H1": {"name": "Operating Systems", "domain": "cs-systems", "area": "cs"},
    "CSC373H1": {"name": "Algorithm Design and Analysis", "domain": "cs-algorithms", "area": "cs"},
}

def dir_name(cid, course):
    slug = re.sub(r"[^a-z0-9]+", "-", course["name"].lower()).strip("-")
    return cid.lower() + "-" + slug

def get_skills(cid):
    entry = skills_data.get(cid, {})
    return entry.get("skills", [])

def formulas_md(cid, course):
    name = course["name"]
    domain = course["domain"]
    lines = [f"# {cid} — 关键公式速查\n"]
    dt = domain_tables.get(domain, {})
    formulas = dt.get("formulas", [])
    if formulas:
        lines.append("## 核心公式\n")
        lines.append("| 概念 | 公式 | 说明 |")
        lines.append("|------|------|------|")
        for f in formulas:
            parts = f if isinstance(f, list) else [f, "", ""]
            lines.append(f"| {parts[0]} | {parts[1]} | {parts[2] if len(parts) > 2 else ''} |")
        lines.append("")
    # Course-specific from skills data
    entry = skills_data.get(cid, {})
    skills = entry.get("skills", [])
    if skills:
        lines.append("## 课程重点\n")
        for s in skills[:5]:
            label = s.get("label", "")
            if label:
                lines.append(f"- **{label}**: {s.get('description', '')}")
        lines.append("")
    lines.extend(["", "---", f"*{name} ({cid}) — 公式速查手册*"])
    return "\n".join(lines)

def proof_techniques_md(cid, course):
    name = course["name"]
    domain = course["domain"]
    lines = [f"# {cid} — 证明技巧指南\n"]
    dt = domain_tables.get(domain, {})
    proofs = dt.get("proofs", [])
    if proofs:
        lines.append("## 核心证明\n")
        for i, p in enumerate(proofs, 1):
            lines.append(f"{i}. {p}")
        lines.append("")
    # Course-specific from data
    entry = skills_data.get(cid, {})
    deduction = entry.get("deductiveChain", {})
    steps = deduction.get("steps", []) if isinstance(deduction, dict) else []
    if steps:
        lines.append("## 课程推演\n")
        for s in steps[:3]:
            lines.append(f"- {s.get('description', '')}")
        lines.append("")
    lines.extend(["", "---", f"*{name} ({cid}) — 证明技巧指南*"])
    return "\n".join(lines)

def counterexamples_md(cid, course):
    name = course["name"]
    domain = course["domain"]
    lines = [f"# {cid} — 反例速查手册\n"]
    dt = domain_tables.get(domain, {})
    ces = dt.get("counterexamples", [])
    if ces:
        lines.append("| # | 反例 | 说明 |")
        lines.append("|---|------|------|")
        for i, ce in enumerate(ces, 1):
            parts = ce.split(": ", 1)
            if len(parts) == 2:
                lines.append(f"| {i} | {parts[0]} | {parts[1]} |")
            else:
                lines.append(f"| {i} | {ce} | |")
        lines.append("")
    lines.extend(["", "---", f"*{name} ({cid}) — 反例速查手册*"])
    return "\n".join(lines)

def applications_md(cid, course):
    name = course["name"]
    domain = course["domain"]
    lines = [f"# {cid} — 实际应用\n"]
    dt = domain_tables.get(domain, {})
    apps = dt.get("applications", [])
    if apps:
        lines.append("## 领域应用\n")
        for a in apps:
            lines.append(f"- {a}")
        lines.append("")
    lines.extend(["", "---", f"*{name} ({cid}) — 实际应用*"])
    return "\n".join(lines)

def checklist_md(cid, course):
    name = course["name"]
    skills = get_skills(cid)
    lines = [f"# {cid} — 学习进度检查表\n"]
    if skills:
        lines.append("| 核心概念 | L1 理解 | L2 识别 | L3 应用 | L4 掌握 | L5 精通 |")
        lines.append("|----------|---------|---------|---------|---------|---------|")
        for s in skills[:8]:
            label = s.get("label", "")
            lines.append(f"| {label} | ☐ | ☐ | ☐ | ☐ | ☐ |")
        lines.append("")
    else:
        lines.append("*技能数据待补充*\n")
    lines.extend(["", "---", f"*{name} ({cid}) — 学习进度检查表*"])
    return "\n".join(lines)

def concept_map_md(cid, course):
    name = course["name"]
    domain = course["domain"]
    lines = [f"# {cid} — 概念依赖图谱\n"]
    lines.append(f"## 领域: {domain}\n")
    dt = domain_tables.get(domain, {})
    formulas = dt.get("formulas", [])
    if formulas:
        lines.append("| 概念 | 前置知识 |")
        lines.append("|------|---------|")
        for f in formulas[:6]:
            concept = f[0] if isinstance(f, list) else f
            lines.append(f"| {concept} | 基础数学与逻辑推理 |")
        lines.append("")
    lines.extend(["", "---", f"*{name} ({cid}) — 概念依赖图谱*"])
    return "\n".join(lines)

def main():
    for cid, course in COURSES.items():
        d = dir_name(cid, course)
        ref_dir = os.path.join(SKILLS_DIR, course["area"], d, "references")
        if not os.path.exists(ref_dir):
            print(f"  \\u2717 {cid}: no references dir, skipping")
            continue
        out = {}
        out["formulas.md"] = formulas_md(cid, course)
        out["proof-techniques.md"] = proof_techniques_md(cid, course)
        out["counterexamples.md"] = counterexamples_md(cid, course)
        out["applications.md"] = applications_md(cid, course)
        out["checklist.md"] = checklist_md(cid, course)
        out["concept-map.md"] = concept_map_md(cid, course)
        for fname, content in out.items():
            path = os.path.join(ref_dir, fname)
            with open(path, "w") as f:
                f.write(content)
            lines = content.count("\n")
            print(f"  \\u2713 {cid}/{fname} ({lines} lines)")

if __name__ == "__main__":
    main()
