# Skill 系统全流程构建指南

## 通用框架 — 适用于任何学科领域

> 本指南从零开始，覆盖知识建模 → 知识图谱 → 教学模式 → 网站呈现 → 部署上线的完整流程。
> 适用于任何领域：计算机科学、数学、统计学、金融投资分析、医学、法律等。

---

# 第一部分：全局架构

## 1.1 最终产物

```
your-project/
├── domain-ontology/                  ← 知识图谱源文件
│   ├── BUILD_METHODOLOGY.md          ← 构建方法论文档
│   └── {DOMAIN_ID}-knowledge-graph.json
├── website/ (or frontend/)           ← 前端项目
│   ├── src/
│   │   ├── components/               ← 图谱可视化、技能查看器
│   │   ├── data/                     ← 前端用数据
│   │   └── ...
│   ├── public/                       ← 静态资源（含 graph JSON）
│   └── dist/                         ← 构建产物
├── skills/
│   ├── skill.json                    ← 全局注册表
│   ├── scripts/                      ← 所有生成脚本
│   └── {domain}/
│       └── {skill-dir}/
│           ├── SKILL.md              ← 技能入口
│           ├── socratic.json          ← 苏格拉底模式
│           ├── deductive.json         ← 演绎推导模式
│           ├── correction.json        ← 纠错模式
│           ├── README.md
│           ├── LICENSE
│           └── references/           ← 参考资源
│               ├── {DOMAIN_ID}-knowledge-graph.json
│               ├── formulas.md
│               ├── methodologies.md
│               ├── case-studies.md
│               ├── concept-map.md
│               ├── checklist.md
│               └── applications.md
```

## 1.2 三层架构

```
┌──────────────────────────────────────────────────┐
│                   用户交互层                        │
│  ┌─────────────┐  ┌─────────────┐               │
│  │  Web 网站    │  │  AI 助手     │               │
│  │ (图谱可视化)  │  │ (技能教学)   │               │
│  └──────┬──────┘  └──────┬──────┘               │
└─────────┼────────────────┼──────────────────────┘
          │                │
┌─────────┼────────────────┼──────────────────────┐
│         ▼                ▼                       │
│              数据层                               │
│  ┌──────────────────────────────────────┐       │
│  │      知识图谱 (Knowledge Graph)       │       │
│  │  ┌───────┐ ┌───────┐ ┌──────────┐   │       │
│  │  │ 节点   │ │ 边     │ │ 属性     │   │       │
│  │  │概念/定理│ │依赖关系│ │双语标签  │   │       │
│  │  └───────┘ └───────┘ └──────────┘   │       │
│  └──────────────────────────────────────┘       │
│  ┌──────────────────────────────────────┐       │
│  │      教学模式 (Teaching Modes)        │       │
│  │  ┌──────────┐ ┌──────────┐ ┌──────┐  │       │
│  │  │ Socratic │ │Deductive │ │Correct│  │       │
│  │  │  6步提问  │ │  6步推导  │ │ 6步纠错│  │       │
│  │  └──────────┘ └──────────┘ └──────┘  │       │
│  └──────────────────────────────────────┘       │
└──────────────────────────────────────────────────┘
          │                │
┌─────────┼────────────────┼──────────────────────┐
│         ▼                ▼                       │
│              存储层                               │
│  ├── domain-ontology/*.json   (源知识图谱)        │
│  ├── skills/*/references/*.json (分发 KG)         │
│  ├── skills/*/socratic.json 等 (教学模式)          │
│  ├── public/*-graph.json     (网站用 KG)          │
│  └── skill.json              (全局注册表)          │
└──────────────────────────────────────────────────┘
```

---

# 第二部分：知识建模（Domain Modeling）

## 2.1 定义领域结构

无论什么领域，先回答这四个问题：

| 问题 | 示例：金融投资分析 | 示例：Python 编程 |
|------|-------------------|-------------------|
| 领域有哪些模块？ | 基本面分析、技术分析、风险管理 | 数据类型、控制流、函数、OOP |
| 每个模块的核心概念？ | PE 比率、MACD、夏普比率 | 变量、循环、递归、类 |
| 有哪些定理/方法/模型？ | CAPM、Black-Scholes、DCF | 查找、排序、主定理 |
| 常见错误/陷阱？ | 幸存者偏差、过拟合 | 可变默认参数、== vs = |

## 2.2 节点类型（通用）

| 类型 | 含义 | 金融示例 | 编程示例 | 医学示例 |
|------|------|---------|---------|---------|
| **Unit** | 模块/单元 | 基本面分析 | 数据类型 | 心血管系统 |
| **Concept** | 核心概念 | 贴现现金流 | 变量 | 血压 |
| **Theorem** | 定理/模型 | CAPM 公式 | 主定理 | 弗兰克-斯大林定律 |
| **Method** | 方法/算法 | DCF 估值法 | 二分搜索 | 听诊法 |
| **Technique** | 技巧/策略 | 对冲策略 | 递归回溯 | 触诊技巧 |
| **Pitfall** | 常见错误 | 幸存者偏差 | 无限递归 | 误诊偏差 |
| **Skill** | 需掌握的技能 | 财报分析 | 调试能力 | 病史采集 |
| **LearningMethod** | 学习方法 | 模拟交易 | 代码审查 | 病例讨论 |

## 2.3 边类型（通用）

| 边类型 | 含义 | 示例 |
|--------|------|------|
| **contains** | 包含关系 | Unit 包含 Concept |
| **requires** | 前置依赖 | 微积分 → 期权定价 |
| **develops** | 发展关系 | 基础概念 → 进阶方法 |
| **teaches** | 教学关系 | 案例研究 → 技能掌握 |

---

# 第三部分：知识图谱构建（Knowledge Graph Construction）

## 3.1 JSON 结构

```json
{
  "courseId": "FINANCIAL_ANALYSIS",
  "courseName": "Financial Investment Analysis",
  "courseNameCn": "金融投资分析",
  "nodes": [
    {
      "id": "unit-1",
      "type": "Unit",
      "label": "Fundamental Analysis",
      "labelCn": "基本面分析",
      "description": "Evaluating securities by analyzing financial statements and economic indicators"
    },
    {
      "id": "concept-1",
      "type": "Concept",
      "label": "Price-to-Earnings Ratio",
      "labelCn": "市盈率",
      "unit": "unit-1",
      "difficulty": 1,
      "keywords": ["P/E", "valuation", "stock"]
    },
    {
      "id": "theorem-1",
      "type": "Theorem",
      "label": "CAPM Formula",
      "labelCn": "资本资产定价模型",
      "formula": "E(R_i) = R_f + β_i(E(R_m) - R_f)",
      "unit": "unit-3"
    }
  ],
  "edges": [
    {
      "id": "e-unit-1-concept-1",
      "source": "unit-1",
      "target": "concept-1",
      "type": "contains"
    },
    {
      "id": "e-concept-1-concept-2",
      "source": "concept-1",
      "target": "concept-2",
      "type": "requires"
    }
  ],
  "metadata": {
    "version": "1.0",
    "totalNodes": 50,
    "totalEdges": 72,
    "domains": ["finance", "investment"],
    "difficulty": "intermediate"
  }
}
```

## 3.2 节点 ID 命名规范

```
{prefix}{number}

前缀约定：
  unit-     → Unit 模块
  c         → Concept 概念
  t         → Theorem 定理/模型
  m         → Method 方法
  f         → Formula 公式
  p         → Pitfall 常见错误
  s         → Skill 技能
  l         → LearningMethod 学习方法
```

## 3.3 构建步骤

```
1. 划分模块（Unit）
   ├── 列出该领域的 4-8 个核心模块
   └── 每个模块定义名称（中英双语）
   
2. 列出概念（Concept）
   ├── 每个模块下列出 5-15 个核心概念
   └── 标记难度等级、关联的关键词
   
3. 列出定理/模型（Theorem/Model）
   ├── 该领域的重要公式、模型
   └── 包含公式表达、适用条件
   
4. 列出方法（Method）
   ├── 每个概念相关的分析方法
   └── 步骤化描述
   
5. 列出常见错误（Pitfall）
   ├── 初学者/从业者常犯的错误
   └── 每个错误配一个典型案例
   
6. 连接边
   ├── contains: Unit → 其下所有节点
   ├── requires: 前置依赖关系
   ├── develops: 从基础到进阶
   └── teaches: 理论和实践的联系
```

---

# 第四部分：教学模式构建（Teaching Mode Construction）

## 4.1 三种教学模式

| 模式 | 适用场景 | 教学策略 | 步骤数 |
|------|---------|---------|--------|
| **Socratic** | 探索新概念 | 提问引导自行发现 | 6 |
| **Deductive** | 推导定理/方法 | 逻辑推导逐步展开 | 6 |
| **Correction** | 纠正常见错误 | 诊断→分析→修正 | 6 |

## 4.2 通用 JSON Schema

```json
{
  "name": "{DOMAIN_ID} — {Topic}: {Mode}",
  "description": "One-sentence description of the teaching goal",
  "parameters": {
    "type": "object",
    "properties": {
      "domainId": {
        "type": "string",
        "enum": ["{DOMAIN_ID}"]
      },
      "skillId": {
        "type": "string",
        "const": "{DOMAIN_ID}-SKILL-{S|D|C}1"
      },
      "lang": {
        "type": "string",
        "enum": ["en", "zh"]
      }
    },
    "required": ["domainId", "skillId", "lang"]
  },
  "steps": [ ... ],
  "references": [
    "references/formulas.md",
    "references/methodologies.md",
    ...
  ],
  "metadata": {
    "domain": "{domain-name}",
    "domainId": "{DOMAIN_ID}",
    "skillType": "{socratic|deductive|correction}",
    "difficulty": 1-5,
    "relatedUnits": ["unit-1", "unit-2"],
    "version": "1.0",
    "knowledgeGraphNodes": ["unit-1", "concept-1", "concept-2"]
  }
}
```

## 4.3 Socratic 模式 — 6 步结构

```
┌─────────────────────────────────────────────────────────┐
│  Step 1: setup                                          │
│  设定场景，提出一个开放的探索性问题，激发好奇              │
├─────────────────────────────────────────────────────────┤
│  Step 2: question                                       │
│  追问具体例子，引导从直觉走向精确                         │
├─────────────────────────────────────────────────────────┤
│  Step 3: explore                                        │
│  探索边界情况（edge case）和反例（counterexample）        │
├─────────────────────────────────────────────────────────┤
│  Step 4: formalize                                      │
│  总结发现，形成正式定义或公式                             │
├─────────────────────────────────────────────────────────┤
│  Step 5: practice                                       │
│  给出练习，检验理解                                     │
├─────────────────────────────────────────────────────────┤
│  Step 6: insight                                        │
│  关键洞察：点明这个知识为什么重要，它是什么思维方式       │
└─────────────────────────────────────────────────────────┘
```

### Socratic 模板（通用）

```json
{
  "steps": [
    {
      "type": "setup",
      "template_en": "Consider this: {scenario question}. What do you notice? Describe in your own words.",
      "template_zh": "考虑这个情况：{场景问题}。你注意到了什么？用你自己的话描述。"
    },
    {
      "type": "question",
      "template_en": "Now let's look at a specific example: {example}. What pattern do you see? Can you generalize?",
      "template_zh": "现在我们来看一个具体例子：{示例}。你看到了什么规律？能推广吗？"
    },
    {
      "type": "explore",
      "template_en": "What if we change {condition}? Does the pattern still hold? Try {edge case}.",
      "template_zh": "如果我们改变{条件}会怎样？这个规律还成立吗？试试{边界情况}。"
    },
    {
      "type": "formalize",
      "template_en": "Let's formalize what we've discovered: {definition/formula}. Can you see how this captures the intuition we built?",
      "template_zh": "让我们把我们发现的正式写出来：{定义/公式}。你能看到这捕捉了我们建立的直觉吗？"
    },
    {
      "type": "practice",
      "template_en": "Now try applying this: {practice problem}. Walk through your reasoning step by step.",
      "template_zh": "现在尝试应用：{练习题}。逐步说明你的推理过程。"
    },
    {
      "type": "insight",
      "template_en": "Key insight: {key takeaway}. This concept isn't just a definition — it's a way of thinking that lets you reason about {broader context}.",
      "template_zh": "关键洞察：{核心观点}。这个概念不仅仅是一个定义——它是一种思维方式，让你能够推理{更广泛的上下文}。"
    }
  ]
}
```

## 4.4 Deductive 模式 — 6 步结构

```
┌─────────────────────────────────────────────────────────┐
│  Step 1: principle                                      │
│  陈述要推导的目标定理/结论，回顾需要用到的前提定义       │
├─────────────────────────────────────────────────────────┤
│  Step 2: step1                                          │
│  第一步逻辑推理：从定义出发的第一个结论                   │
├─────────────────────────────────────────────────────────┤
│  Step 3: step2                                          │
│  第二步逻辑推理：基于上一步继续前进                       │
├─────────────────────────────────────────────────────────┤
│  Step 4: step3                                          │
│  第三步逻辑推理：完成推导                                 │
├─────────────────────────────────────────────────────────┤
│  Step 5: conclusion                                     │
│  总结推导结果，强调推导的逻辑链条                         │
├─────────────────────────────────────────────────────────┤
│  Step 6: meta                                           │
│  元认知反思：这个推导揭示了什么思维方式？适用于其他场景？  │
└─────────────────────────────────────────────────────────┘
```

### Deductive 模板（通用）

```json
{
  "steps": [
    {
      "type": "principle",
      "template_en": "We want to derive {theorem/conclusion}. The key assumptions are: {assumptions}. Where should we begin?",
      "template_zh": "我们要推导{定理/结论}。关键假设是：{假设}。我们从哪里开始？"
    },
    {
      "type": "step1",
      "template_en": "Step 1 — From {definition}, we can conclude {intermediate result}. Why? Because {justification}. Before reading on, can you verify this yourself?",
      "template_zh": "第 1 步——从{定义}出发，我们可以得出{中间结果}。为什么？因为{理由}。在继续之前，你能自己验证吗？"
    },
    {
      "type": "step2",
      "template_en": "Step 2 — Using {step1 result} and {additional assumption}, we get {next result}. Check each inference: is every step logically valid?",
      "template_zh": "第 2 步——利用{上一步结果}和{额外假设}，我们得到{下一步结果}。检查每个推理：每一步是否逻辑有效？"
    },
    {
      "type": "step3",
      "template_en": "Step 3 — Combining {previous results}, we arrive at the conclusion: {final result}. The chain of reasoning holds because {reason}.",
      "template_zh": "第 3 步——结合{前面的结果}，我们得出结论：{最终结果}。推理链条成立，因为{原因}。"
    },
    {
      "type": "conclusion",
      "template_en": "Therefore, {theorem} is proven. The logical chain was: {summary}. Each step followed from definitions — no leaps of faith.",
      "template_zh": "因此，{定理}得证。逻辑链是：{总结}。每一步都跟随定义——没有跳跃。"
    },
    {
      "type": "meta",
      "template_en": "Meta-lesson: {theorem} is not an isolated fact — it's a consequence of {deeper principle}. The structure of this proof reveals WHY it's true, not just THAT it's true. This deductive pattern ({pattern name}) applies to other situations like {other examples}.",
      "template_zh": "元认知：{定理}不是孤立的事实——它是{更深层原理}的推论。这个证明的结构揭示了它为什么成立，而不仅仅是它成立。这个演绎模式（{模式名称}）也适用于其他场景，如{其他例子}。"
    }
  ]
}
```

## 4.5 Correction 模式 — 6 步结构

```
┌─────────────────────────────────────────────────────────┐
│  Step 1: pitfall                                        │
│  呈现一个典型错误（可以是一个学生写的错误代码/推导）      │
├─────────────────────────────────────────────────────────┤
│  Step 2: question                                       │
│  提问：这个错误暴露了什么概念鸿沟？正确的理解是什么？    │
├─────────────────────────────────────────────────────────┤
│  Step 3: explore                                        │
│  深入探索错误根源：被过度推广的模式是什么？边界在哪里？  │
├─────────────────────────────────────────────────────────┤
│  Step 4: insight                                        │
│  关键纠正：正确的推理应该是什么样的？                    │
├─────────────────────────────────────────────────────────┤
│  Step 5: practice                                       │
│  给出类似练习，检验是否真正理解                          │
├─────────────────────────────────────────────────────────┤
│  Step 6: reflection                                     │
│  反思：如何避免今后犯同样错误？这个教训揭示了什么        │
└─────────────────────────────────────────────────────────┘
```

### Correction 模板（通用）

```json
{
  "steps": [
    {
      "type": "pitfall",
      "template_en": "Common error: {description of mistake}. This is NOT a silly mistake — it reveals a conceptual gap. Let's find it.",
      "template_zh": "常见错误：{错误描述}。这不是一个愚蠢的错误——它揭示了一个概念鸿沟。让我们找到它。"
    },
    {
      "type": "question",
      "template_en": "Consider {example showing the error}. What assumption is being made that isn't justified? What's the correct reasoning?",
      "template_zh": "考虑{展示错误的例子}。这里做出了什么不合理的假设？正确的推理应该是什么样的？"
    },
    {
      "type": "explore",
      "template_en": "Let's explore deeper. The error comes from over-generalizing: {overgeneralized pattern}. This pattern works when {condition}, but fails when {counterexample}. The boundary between work and fail defines the precise scope.",
      "template_zh": "让我们更深入地探讨。这个错误来自于过度推广：{被过度推广的模式}。这个模式在{条件}下有效，但在{反例}下失效。有效和无效的边界定义了精确的范围。"
    },
    {
      "type": "insight",
      "template_en": "The correct understanding: {correct reasoning}. The key difference is {key distinction}. Once you see this, the error becomes impossible to make.",
      "template_zh": "正确的理解：{正确推理}。关键区别在于{关键区别}。一旦你看到这一点，这个错误就不会再犯了。"
    },
    {
      "type": "practice",
      "template_en": "Now test yourself: {practice problem}. Identify any hidden assumptions and verify your reasoning.",
      "template_zh": "现在测试自己：{练习题}。识别任何隐藏的假设并验证你的推理。"
    },
    {
      "type": "reflection",
      "template_en": "Reflection: What was the core misconception? How does the corrected understanding change your thinking? The best practitioners don't avoid mistakes — they learn from them by analyzing the gap between intuition and correct reasoning.",
      "template_zh": "反思：核心误解是什么？修正后的理解如何改变了你的思考方式？最好的从业者不会避免错误——他们通过分析直觉与正确推理之间的差距来从中学习。"
    }
  ]
}
```

---

# 第五部分：网站呈现（Website Visualization）

## 5.1 前端技术栈选择

| 组件 | 推荐 | 说明 |
|------|------|------|
| 框架 | React / Vue / Svelte | 任何现代前端框架 |
| 图谱可视化 | D3.js / vis.js / Cytoscape.js | 节点-边图渲染 |
| 构建工具 | Vite / Webpack | 打包和热更新 |
| 部署 | Netlify / Vercel / GitHub Pages | 静态站点托管 |

## 5.2 网站核心功能

```
网站功能架构
│
├── 首页
│   ├── 领域选择（计算机/数学/金融/医学...）
│   └── 课程/技能列表
│
├── 知识图谱查看器
│   ├── 交互式节点-边图渲染
│   ├── 节点点击 → 显示详情（中英双语）
│   ├── 缩放/拖拽/搜索
│   └── 依赖路径高亮
│
├── 技能查看器
│   ├── 三种教学模式切换
│   ├── 步骤分步展示（中英切换）
│   └── 关联知识图谱节点链接
│
└── 参考资源
    ├── 公式表
    ├── 方法论
    ├── 案例研究
    ├── 概念地图
    ├── 检查清单
    └── 实际应用
```

## 5.3 图谱 JSON 格式（前端用）

```json
{
  "courseId": "FINANCIAL_ANALYSIS",
  "courseName": "Financial Investment Analysis",
  "nodes": [
    {
      "id": "unit-1-concepts1",
      "type": "Concept",
      "label": "Price-to-Earnings Ratio",
      "labelCn": "市盈率",
      "unit": "unit-1",
      "order": 1,
      "difficulty": 1
    }
  ],
  "edges": [
    {
      "id": "e-1",
      "source": "unit-1-concepts1",
      "target": "unit-1-concepts2",
      "type": "requires"
    }
  ],
  "skillProgressionPaths": []
}
```

**注意：** 前端用的 `public/*-graph.json` 格式与 `domain-ontology/*-knowledge-graph.json` 格式不同。前者节点 ID 是 `unit-1-concepts1` 格式，后者是 `c1` 格式。需要编写转换脚本。

## 5.4 构建和部署

```bash
# 开发
npm run dev          # 启动本地开发服务器

# 构建
npm run build        # tsc + vite build
                     # 自动将 public/ 拷贝到 dist/

# 预览
npm run preview      # 预览构建产物

# 部署（Netlify 示例）
# 连接 GitHub 仓库 → Netlify 自动部署
# 或手动:
npx netlify deploy --prod --dir=dist
```

---

# 第六部分：全流程流水线（Pipeline）

## 6.1 从零到上线完整流程

```
PHASE 0: 前期准备
├── 确定领域范围
├── 搭建项目骨架（frontend + skills 目录）
└── 安装依赖（npm install）

        ▼
PHASE 1: 知识建模 (1-2 周)
├── 列出领域模块 (Unit)
├── 列出核心概念 (Concept)
├── 列出定理/模型 (Theorem)
├── 列出方法 (Method)
├── 列出常见陷阱 (Pitfall)
├── 列出技能 (Skill)
├── 列出学习方法 (LearningMethod)
└── 连接依赖关系 (Edge)

        ▼
PHASE 2: 知识图谱构建 (3-5 天)
├── 创建 domain-ontology/{DOMAIN_ID}-knowledge-graph.json
│   └── 包含所有节点 + 边
├── 验证图谱结构
│   └── 确保无孤立节点、边指向有效节点
└── 编写转换脚本 → public/{DOMAIN_ID}-graph.json

        ▼
PHASE 3: 参考资源编写 (1-2 周)
├── formulas.md          ← 核心公式/定义
├── methodologies.md     ← 方法论指导
├── case-studies.md      ← 案例研究/反例
├── concept-map.md       ← 概念依赖图
├── checklist.md         ← 检查清单
└── applications.md      ← 实际应用

        ▼
PHASE 4: 教学模式生成 (2-3 周)
├── 为每个 Unit 编写 Socratic 模式 (6 步)
│   └── 以提问引导探索核心概念
├── 为每个核心定理编写 Deductive 模式 (6 步)
│   └── 从定义出发逐步推导
├── 为每个常见错误编写 Correction 模式 (6 步)
│   └── 诊断 → 分析 → 修正
├── 编写 SKILL.md
│   └── Instructions + Mode Data Files + References
└── 更新 skill.json 注册表

        ▼
PHASE 5: 验证 (1-2 天)
├── JSON 语法正确性
├── 每文件 6 步
├── 步骤类型匹配模式标准
├── 双语模板完整
├── skillId 命名规范
├── KG 节点引用有效
├── SKILL.md 完整性
├── skill.json 完整性
└── course-ontology courseId 一致性

        ▼
PHASE 6: 前端开发 (2-4 周)
├── 图谱可视化组件
├── 教学步骤查看器
├── 参考资源页面
├── 中英切换
└── 响应式设计

        ▼
PHASE 7: 部署 (1-2 天)
├── npm run build
├── 部署到 Netlify / Vercel
├── 配置自定义域名（可选）
└── 测试线上环境

        ▼
PHASE 8: 安装到 OpenCode (持续)
├── cp -r skills/{domain}/{skill-dir} ~/.opencode/agent/skills/
├── 重启 opencode
└── agent use 调用
```

## 6.2 生成脚本参考

```python
# scripts/generate_skill_package.py (通用框架)
import json, os

def build_knowledge_graph(domain_id, units, concepts, theorems, methods, pitfalls):
    """构建知识图谱"""
    pass

def build_socratic_steps(topic, questions, examples):
    """构建苏格拉底模式步骤"""
    pass

def build_deductive_steps(theorem, assumptions, proof_steps):
    """构建演绎推导模式步骤"""
    pass

def build_correction_steps(error, correct_understanding, practice):
    """构建纠错模式步骤"""
    pass

def build_skill_md(domain_id, domain_name, modes, references):
    """构建 SKILL.md"""
    pass

def validate_all(skill_dir):
    """全套验证"""
    pass
```

---

# 第七部分：验证清单（Checklist）

## 7.1 必须检查项

```
□ 所有 JSON 文件语法正确
□ 每个 JSON 的 steps 数组长度为 6
□ Socratic 的 step types: setup, question, explore, formalize, practice, insight
□ Deductive 的 step types: principle, step1, step2, step3, conclusion, meta
□ Correction 的 step types: pitfall, question, explore, insight, practice, reflection
□ 每个 step 都有非空的 template_en 和 template_zh（英文 ≥ 30字符，中文 ≥ 20字符）
□ skillId 格式: {DOMAIN_ID}-SKILL-{S|D|C}1
□ metadata.knowledgeGraphNodes 全部存在于对应 KG 文件中
□ references 数组指向的文件都存在
□ SKILL.md 包含 knowledge-graph 引用
□ skill.json 注册表完整、无重复 ID
□ domain-ontology 中的 courseId 与文件名一致
□ public/ 和 dist/ 的 graph JSON 已同步
```

## 7.2 常见陷阱

| 陷阱 | 症状 | 修复 |
|------|------|------|
| domainId 不一致 | 文件名、文件内、文件夹名三个地方不一样 | 统一到一个规范名称 |
| 孤立 KG 节点 | JSON 引用了不存在的节点 ID | 检查所有 knowledgeGraphNodes |
| 步骤类型拼写错 | `setup` 写成了 `set-up` | 严格使用预定义 types |
| 中文模板过短 | 英文 200 字，中文只有 10 字 | 中文翻译需要同等详细程度 |
| 忘记更新 registry | 新增了 skill 但没加到 skill.json | 每次增删改都同步更新 |
| 网站 KG 格式不对 | 前端渲染不出图 | node ID 需用 `unit-N-concept-M` 格式 |
| SKILL.md 不完整 | AI 无法正确加载 | 确保包含 Instructions + 表格 + References |

---

# 第八部分：各领域适配举例

## 8.1 金融投资分析

| 元素 | 内容 |
|------|------|
| Domain ID | `FINANCIAL_ANALYSIS` |
| Units | 基本面分析、技术分析、风险管理、投资组合理论 |
| Concepts | PE 比率、β 系数、夏普比率、MACD、KDJ |
| Theorems | CAPM、Black-Scholes、有效市场假说 |
| Methods | DCF 估值法、技术形态识别、蒙特卡洛模拟 |
| Pitfalls | 幸存者偏差、过度交易、确认偏误 |
| Skills | 财报解读、风险管理、心态控制 |

## 8.2 机器学习

| 元素 | 内容 |
|------|------|
| Domain ID | `MACHINE_LEARNING` |
| Units | 监督学习、无监督学习、深度学习、模型评估 |
| Concepts | 过拟合、偏差-方差权衡、梯度下降、正则化 |
| Theorems | No Free Lunch Theorem、VC 维、贝叶斯定理 |
| Methods | 随机森林、SVM、K-means、反向传播 |
| Pitfalls | 数据泄露、类别不平衡、特征选择偏差 |
| Skills | 特征工程、超参数调优、模型解释 |

## 8.3 医学诊断

| 元素 | 内容 |
|------|------|
| Domain ID | `MEDICAL_DIAGNOSIS` |
| Units | 病史采集、体格检查、辅助检查、鉴别诊断 |
| Concepts | 灵敏度、特异度、预测值、似然比 |
| Theorems | 贝叶斯定理在诊断中的应用 |
| Methods | 系统回顾、SOAP 记录、临床决策树 |
| Pitfalls | 锚定偏误、可用性启发、过早闭合 |
| Skills | 鉴别诊断思维、循证医学实践 |

---

# 附录：关键文件模板

## A. SKILL.md 通用模板

```markdown
---
name: {domain-id}-{skill-name}
description: {description for skill listing}
license: MIT
metadata:
  domainId: {DOMAIN_ID}
  domain: {domain-name}
  skill-count: "{count}"
  difficulty: "{1-5}"
  version: "1.0"
---

{Socratic|Deductive|Correction} teaching · {topic}

## Instructions

You are a {DOMAIN_NAME} instructor. When a student invokes this skill, identify the mode they need and follow the corresponding protocol.

### Mode 1 — Socratic Discovery ({topic 1})
... (6 steps)

### Mode 2 — Deductive Derivation ({topic 2})
... (6 steps)

### Mode 3 — Correction Attribution ({topic 3})
... (6 steps)

## Context

This skill covers {domain overview}.

## Mode Data Files

| File | Mode | Content |
|------|------|---------|
| `socratic.json` | Socratic Discovery ({topic}) | Guided questioning sequence |
| `deductive.json` | Deductive Derivation ({topic}) | Step-by-step logical derivation |
| `correction.json` | Correction ({topic}) | Pitfall → question → insight → practice cycle |

## References

All supporting documents are in the `references/` directory:

| File | Purpose | Use When |
|------|---------|----------|
| `formulas.md` | Key formulas and definitions | Student needs formula lookup |
| `methodologies.md` | Methodological guidance | Student stuck on methodology |
| `case-studies.md` | Case studies and counterexamples | Student asks "what if?" |
| `concept-map.md` | Concept dependencies overview | Student wants the big picture |
| `checklist.md` | Progress tracking | Student wants to self-assess |
| `applications.md` | Real-world applications | Student wants practical motivation |
| `{DOMAIN_ID}-knowledge-graph.json` | Full knowledge graph — {N} concepts, theorems, methods | Student needs concept relationships |

## Skill Taxonomy

For detailed level descriptors and practice strategies, consult `references/checklist.md`.
```

## B. 转换脚本框架

```python
# scripts/convert_for_website.py
# 将 domain-ontology/*-knowledge-graph.json 转为 public/*-graph.json
#（因为两种格式不同）

import json

def convert_kg_for_frontend(input_path, output_path):
    with open(input_path) as f:
        data = json.load(f)
    
    new_nodes = []
    node_counter = {}
    
    for node in data["nodes"]:
        unit = node.get("unit", "unit-0")
        node_type = node["type"]
        if node_type not in node_counter:
            node_counter[node_type] = 0
        node_counter[node_type] += 1
        
        new_node = {
            "id": f"{unit}-{node_type.lower()}s{node_counter[node_type]}",
            "type": node_type,
            "label": node["label"],
            "labelCn": node.get("labelCn", ""),
            "unit": unit,
            "order": node_counter[node_type],
            "difficulty": node.get("difficulty", 1)
        }
        new_nodes.append(new_node)
    
    output = {
        "courseId": data["courseId"],
        "courseName": data["courseName"],
        "nodes": new_nodes,
        "edges": data.get("edges", []),
        "skillProgressionPaths": []
    }
    
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Converted: {input_path} → {output_path}")
```

---

> **最后一条建议：** 构建 skill 系统最难的不是技术，而是**领域知识的结构化**。把模糊的"我知道这个领域"变成精确的节点和边、问题和答案、错误和修正，这个过程本身就迫使你深入理解这个领域。开始的时候不用追求完美，先做出第一个版本的 Socratic 模式，测试一下，然后迭代。
