# Skill 包生成工作流

从零到部署的完整流程。

---

## 一、前置准备

### 1.1 目录结构

```
uoft-kg/
├── course-ontology/          ← 知识图谱源文件（手动/半自动维护）
│   ├── SKG-methodology.md    ← 共享方法论文档
│   └── {courseId}-knowledge-graph.json
├── skills/
│   ├── skill.json            ← 主注册表（所有 skill 的索引）
│   ├── scripts/              ← 生成脚本
│   ├── {cs|math|stats}/
│   │   └── {course-dir}/
│   │       ├── SKILL.md      ← Skill 入口文件
│   │       ├── socratic.json      ← 苏格拉底模式
│   │       ├── deductive.json     ← 演绎推导模式
│   │       ├── correction.json     ← 纠错模式
│   │       ├── README.md
│   │       ├── LICENSE
│   │       └── references/   ← 参考资源
│   │           ├── {courseId}-knowledge-graph.json
│   │           ├── formulas.md
│   │           ├── proof-techniques.md
│   │           ├── counterexamples.md
│   │           ├── concept-map.md
│   │           ├── checklist.md
│   │           └── applications.md
├── dist/                     ← Vite 构建输出
└── public/                   ← 静态资源
```

### 1.2 关键概念

| 概念 | 说明 |
|------|------|
| course-ontology KG | 知识图谱源文件，包含节点（概念/定理/方法等）和边（依赖关系） |
| references/ KG | 从 course-ontology 拷贝到 skill 目录下的子集 |
| skill.json | 所有 35 课程 × 3 模式 = 105 个 entry 的注册表 |
| 3 种教学模式 | socratic（苏格拉底式提问）、deductive（演绎推导）、correction（纠错） |
| 每文件 6 步 | 每种模式固定 6 个步骤，双语（template_en + template_zh） |

---

## 二、知识图谱创建

### 2.1 创建 course-ontology KG

```json
{
  "courseId": "CSC108H1",
  "courseName": "Introduction to Computer Programming",
  "nodes": [
    {
      "id": "unit-1",
      "type": "Unit",
      "label": "Python Basics",
      "labelCn": "Python基础"
    },
    {
      "id": "concept-1",
      "type": "Concept",
      "label": "Variable",
      "labelCn": "变量",
      "unit": "unit-1"
    }
    // ... 更多节点
  ],
  "edges": [
    {
      "id": "e-unit-1-concept-1",
      "source": "unit-1",
      "target": "concept-1",
      "type": "contains"
    }
  ]
}
```

**节点类型：** Unit, Concept, Theorem, Method, Technique, Pitfall, Skill, LearningMethod

**边类型：** contains, requires, develops, teaches

### 2.2 节点 ID 命名规范

| 类型 | 命名 | 示例 |
|------|------|------|
| Unit | `unit-N` | `unit-1`, `unit-2` |
| Concept | `cN` 或 `concept-N` | `c1`, `concept-2` |
| Theorem | `tN` | `t1`, `t2` |
| Method | `mN` | `m1` |
| Formula | `fN` | `f1` |
| Pitfall | `pN` | `p1` |
| Skill | `sN` | `s1` |
| LearningMethod | `lN` | `l1` |

**重要：** JSON 文件中的 `metadata.knowledgeGraphNodes` 必须引用真实存在的节点 ID，否则会导致孤立引用错误。

---

## 三、Skill 包生成

### 3.1 运行生成脚本

```bash
# 为主课程生成 reference 文件
python3 skills/scripts/generate_math_references.py     # MATH 课程
python3 skills/scripts/generate_stats_cs_references.py  # STA/CS 课程

# 生成 skill JSON 文件（socratic/deductive/correction）
python3 skills/scripts/enrich_all_remaining.py
```

### 3.2 生成的文件结构

每个课程目录下生成：
- `socratic.json` — 6 steps, types: `setup`, `question`, `explore`, `formalize`, `practice`, `insight`
- `deductive.json` — 6 steps, types: `principle`, `step1`, `step2`, `step3`, `conclusion`, `meta`
- `correction.json` — 6 steps, types: `pitfall`, `question`, `explore`, `insight`, `practice`, `reflection`
- `references/*-knowledge-graph.json` — 从 course-ontology 拷贝
- `references/*.md` — 6 个参考文档

### 3.3 SKILL.md 模板

每个课程需要 SKILL.md，包含：
- YAML frontmatter（name, description, metadata）
- Instructions（AI 的角色设定）
- 3~6 个教学模式描述（Goal + 步骤）
- Mode Data Files 表格（关联 JSON 文件）
- References 表格（关联 references/ 目录文件）
- 必须包含 `{courseId}-knowledge-graph.json` 的引用

---

## 四、验证清单

### 4.1 核心验证（运行 comprehensive_validation.py）

```python
# 每个检查项
✓ JSON 语法正确         # 所有 105 文件可解析
✓ 步骤数为 6             # 每文件恰好 6 steps
✓ steps 有 type 字段     # type 不为空且符合规范
✓ 双语模板非空           # template_en和template_zh都有内容且足够长
✓ skillId 格式正确       # {courseId}-SKILL-{S|D|C}1
✓ KG 节点引用有效        # knowledgeGraphNodes 全部存在
✓ references 文件存在     # JSON 中列出的文件都存在
✓ skill.json 完整         # 105 entries，无缺失无重复
✓ SKILL.md 有 KG 引用     # 35 个文件都引用 knowledge-graph.json
✓ course-ontology courseId 与文件名一致
```

### 4.2 常见问题及修复

| 问题 | 症状 | 修复 |
|------|------|------|
| **孤立 KG 节点** | `knowledgeGraphNodes` 引用了不存在的 ID | 运行验证找到孤立引用，替换为真实节点 ID |
| **courseId 错误** | `courseId` 为 `concept-XX` 而非课程代码 | 在 course-ontology 和 references 中修复为 `STA130H1` 等 |
| **skillId 不规范** | 如 `MAT137Y1-SKILL-A1` 而非 `-S1` | 统一为 `-SKILL-{S\|D\|C}1` 格式，同时更新 skill.json |
| **步骤数不对** | socratic/deductive/correction 步骤数不为 6 | 少于 6 步则补充步骤，多于 6 步则合并（`question+hint+resolution` → 一步）|
| **中文模板过短** | `template_zh` 不足 20 字符 | 扩充中文翻译至与英文同等详细程度 |
| **SKILL.md 缺失 KG** | 参考资料表没有 `knowledge-graph.json` 行 | 添加 KG 行到 References 表格 |

---

## 五、安装与部署

### 5.1 安装到 OpenCode

```bash
# 复制技能目录
cp -r skills/{domain}/{course-dir} ~/.opencode/agent/skills/

# 验证
ls ~/.opencode/agent/skills/{course-dir}/
# 应输出: LICENSE  README.md  SKILL.md  correction.json  deductive.json  references/  socratic.json
```

### 5.2 使用技能

```bash
# 方式 1：直接引用 SKILL.md
agent use skills/{domain}/{course-dir}/SKILL.md

# 方式 2：重启 opencode 后自动加载
```

### 5.3 部署到网站

```bash
npm run build
# Vite 自动将 public/ 拷贝到 dist/
# dist/*-graph.json 提供给前端渲染
```

注意：`public/*-graph.json` 是外部手动生成的，不是脚本自动生成的。如需更新，需要单独编写转换脚本从 `course-ontology/` 生成。

---

## 六、完整流程速查

```
course-ontology/*-knowledge-graph.json
  │
  ├──(generate_math_references.py / generate_stats_cs_references.py)
  │
  └── skills/{domain}/{course-dir}/references/*-knowledge-graph.json
  │
  ├──(enrich_all_remaining.py)
  │
  └── skills/{domain}/{course-dir}/{socratic,deductive,correction}.json
  │
  ├──(validate: step count, KG refs, bilingual, skillId, skill.json)
  │
  ├──(fix issues: orphaned nodes, courseId, step counts, templates)
  │
  └── cp -r → ~/.opencode/agent/skills/
        │
        └── agent use → 开始教学
```

---

## 七、关键原则

1. **CourseId 一致性** — 文件名、course-ontology、references、skill.json、JSON 内 `courseId` 字段必须全部一致
2. **每模式 6 步** — 少于补全，多于合并，类型匹配标准 schema
3. **双语全覆盖** — 所有步骤必须有 `template_en` 和 `template_zh`，长度匹配
4. **KG 节点可追溯** — `knowledgeGraphNodes` 必须全部存在于对应 KG 文件中
5. **skill.json 同步** — 任何 skillId 变更必须同步更新 skill.json
6. **SKILL.md 完整** — 必须包含 Instructions、Mode Data Files、References（含 KG）三大部分
