# STA347H1 — 关键公式速查

## 核心公式

| 概念 | 公式 | 说明 |
|------|------|------|
| 条件概率 | $P(A|B) = \frac{P(A\cap B)}{P(B)}$ | 条件化 |
| 全概率 | $P(A) = \sum_i P(A|B_i)P(B_i)$ | 完备事件组 |
| Bayes | $P(B_i|A) = \frac{P(A|B_i)P(B_i)}{\sum_j P(A|B_j)P(B_j)}$ | 后验概率 |
| 期望 | $E[X] = \sum x\,p(x)$ 或 $\int x\,f(x)\,dx$ | 加权平均 |
| 方差 | $\operatorname{Var}(X) = E[X^2] - \mu^2$ | 离散程度 |
| 矩母函数 | $M_X(t) = E[e^{tX}]$ | 生成矩 |

## 课程核心定理

| 定理 | 英文 | 所在单元 |
|------|------|---------|
| Kolmogorov公理 | Kolmogorov axioms | 单元 1 |
| 概率连续性 | Continuity of probability | 单元 1 |
| CDF性质 | Properties of CDF | 单元 2 |
| 勒贝格分解 | Lebesgue decomposition | 单元 2 |
| 全期望公式 | Law of total expectation | 单元 3 |
| 全方差公式 | Law of total variance | 单元 3 |
| Jensen不等式 | Jensen's inequality | 单元 4 |
| 柯西-施瓦茨 | Cauchy-Schwarz | 单元 4 |
| MGF/CF唯一性 | Uniqueness of MGF/CF | 单元 4 |
| Kolmogorov强大数定律 | Kolmogorov SLLN | 单元 5 |

## 核心方法

| 方法 | 说明 | 所在单元 |
|------|------|---------|
| Counting principles | 计数原理 | 单元 1 |
| Probability integral transform | 概率积分变换 | 单元 2 |
| Jacobian transformation | 雅可比变换 | 单元 3 |
| MGF for moment computation | MGF求矩 | 单元 4 |
| MGF convergence for CLT | MGF收敛证CLT | 单元 5 |
| Process simulation | 过程模拟 | 单元 6 |

---
*Probability (STA347H1) — 公式速查手册*