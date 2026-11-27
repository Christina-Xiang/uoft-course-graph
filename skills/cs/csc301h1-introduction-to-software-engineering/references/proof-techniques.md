# CSC301H1 — 推理与技巧指南

### 1. LSP 推导: 若 $S\le T$, 则 $\forall P: T\text{ 使用的性质对 }S\text{ 也成立}$

### 2. 依赖反转: 高层模块通过抽象接口调用低层, 而非直接依赖具体实现

### 3. 合约式设计 (DbC): 前置条件 $\to$ 后置条件 $\land$ 不变量

### 4. 测试覆盖: 分支覆盖 $\implies$ 语句覆盖, 路径覆盖 $\implies$ 分支覆盖

### 5. 输入验证: 所有外部输入需在信任边界验证

### 6. 最小权限: 每个模块只有完成其功能所需的最小权限

### 7. 封装: 隐藏实现细节, 公开稳定接口

### 8. 重构等价性: 行为保持变换 (不改变功能只改进结构)

## 核心方法

- **Agile planning** (敏捷规划) — 单元 1
- **Requirements elicitation** (需求获取) — 单元 2
- **Architecture decision records** (架构决策记录) — 单元 3
- **Code review checklist** (代码审查清单) — 单元 4
- **Scrum ceremonies** (Scrum仪式) — 单元 5
- **Ethical analysis framework** (伦理分析框架) — 单元 6

## 编程技巧

- **Estimation techniques** (估算技术) — 单元 1
- **API specification** (OpenAPI) — 单元 3
- **CI pipeline setup** (CI管道搭建) — 单元 4

---
*Introduction to Software Engineering (CSC301H1) — 推理与技巧指南*