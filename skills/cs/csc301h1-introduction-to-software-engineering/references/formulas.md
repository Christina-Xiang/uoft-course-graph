# CSC301H1 — 关键公式与概念速查

## 核心公式/复杂度

| 概念 | 公式/描述 | 说明 |
|------|----------|------|
| SOLID 原则 | SRP, OCP, LSP, ISP, DIP | 面向对象设计五大原则 |
| 单一职责 (SRP) | 一个类只应有一个引起变化的原因 | 高内聚准则 |
| 开闭原则 (OCP) | 对扩展开放, 对修改关闭 | 抽象化设计 |
| Liskov 替换 (LSP) | $S \le T \Rightarrow T$ 对象可被 $S$ 替换 | 继承遵守 |
| 接口隔离 (ISP) | 不强迫客户依赖它们不使用的接口 | 细粒度接口 |
| 依赖反转 (DIP) | 抽象不应依赖细节; 细节依赖抽象 | 解耦准则 |
| 工厂模式 | $\text{Product } p = \text{factory.create}(\text{type})$ | 创建型模式 |
| 观察者模式 | Subject → Observer 一对多通知 | 行为型模式 |
| 策略模式 | 算法族封装, 可互换 | 行为型模式 |
| MVC | Model 数据 + View 展示 + Controller 控制 | 架构模式 |
| RESTful API | $\text{GET/POST/PUT/DELETE}$ 操作资源 | Web API 设计 |
| HTTP 状态码 | 200 OK, 201 Created, 400 Bad Request, 404 Not Found, 500 Server Error | 响应语义 |
| Git 工作流 | clone → branch → commit → push → PR → merge | 版本控制 |
| CI/CD 管道 | 代码提交 → 自动构建 → 自动测试 → 自动部署 | DevOps |
| 测试金字塔 | 单元测试(多) → 集成测试 → E2E测试(少) | 测试策略 |
| TDD | 红 (写测试) → 绿 (写实现) → 重构 | 测试驱动开发 |
| 白盒测试 | 基于代码结构设计测试用例 | 语句/分支/路径覆盖 |
| 黑盒测试 | 基于需求/规约设计测试用例 | 等价类/边界值 |
| 耦合度 | 模块间依赖程度 (低耦合 = 好) | 设计质量指标 |
| 内聚度 | 模块内部元素关联程度 (高内聚 = 好) | 设计质量指标 |
| DDD | 实体、值对象、聚合、仓储、领域服务 | 领域驱动设计 |
| 数据库范式 | 1NF 原子列, 2NF 消除部分依赖, 3NF 消除传递依赖 | 规范化 |

## 课程核心概念

| 概念 | 英文 | 所在单元 |
|------|------|---------|
| 瀑布模型 | Waterfall model | 单元 1 |
| 敏捷方法 | Agile methodology | 单元 1 |
| Scrum框架 | Scrum framework | 单元 1 |
| 冲刺 | Sprints | 单元 1 |
| 用户故事 | User stories | 单元 1 |
| 功能需求 | Functional requirements | 单元 2 |
| 非功能需求 | Non-functional requirements | 单元 2 |
| 用例 | Use cases | 单元 2 |
| 用户故事与验收标准 | User stories & acceptance criteria | 单元 2 |
| 架构模式 | Architectural patterns | 单元 3 |
| 分层架构 | Layered architecture | 单元 3 |
| MVC | MVC | 单元 3 |
| 微服务 | Microservices | 单元 3 |
| API设计 | API design | 单元 3 |
| 代码审查 | Code review | 单元 4 |
| 持续集成/持续部署 | CI/CD | 单元 4 |
| 自动化测试 | Automated testing | 单元 4 |
| 性能测试 | Performance testing | 单元 4 |
| 任务估算 | Task estimation | 单元 5 |
| 风险管理 | Risk management | 单元 5 |
| 燃尽图 | Burndown chart | 单元 5 |
| 团队速度 | Velocity | 单元 5 |
| 职业伦理 | Professional ethics | 单元 6 |
| 隐私与安全 | Privacy & security | 单元 6 |
| 无障碍设计 | Accessibility | 单元 6 |
| 可持续性 | Sustainability | 单元 6 |

---
*Introduction to Software Engineering (CSC301H1) — 公式与概念速查*