# STA257H1 — 关键公式速查

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
| LOTUS定理 | LOTUS | 单元 2 |
| 马尔可夫不等式 | Markov inequality | 单元 2 |
| 无记忆性 | Memoryless property | 单元 3 |
| 柯西-施瓦茨不等式 | Cauchy-Schwarz inequality | 单元 4 |
| MGF唯一性定理 | MGF uniqueness | 单元 5 |
| 和MGF=积 | MGF of sum = product | 单元 5 |
| Chebyshev | WLLN | 单元 6 |
| Lindeberg-Levy | CLT | 单元 6 |

## 核心方法

| 方法 | 说明 | 所在单元 |
|------|------|---------|
| Combinatorial counting | 组合计数 | 单元 1 |
| Moment generating function | 矩生成函数 | 单元 2 |
| Change of variable | 变量变换法 | 单元 3 |
| Probability integral transform | 概率积分变换 | 单元 3 |
| Jacobian | 雅可比变换 | 单元 4 |
| Double integration | 二重积分 | 单元 4 |
| MGF derivation | MGF推导 | 单元 5 |
| CLT approximation | CLT逼近 | 单元 6 |

---
*Probability and Statistics I (STA257H1) — 公式速查手册*