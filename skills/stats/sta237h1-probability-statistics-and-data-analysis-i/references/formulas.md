# STA237H1 — 关键公式速查

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
| 贝叶斯定理 | Bayes' theorem | 单元 1 |
| LOTUS定理 | LOTUS | 单元 2 |
| 期望线性性 | Linearity of expectation | 单元 2 |
| CDF求导得PDF | PDF from CDF | 单元 3 |
| 分解判据 | Factorization criterion | 单元 4 |
| Chebyshev | WLLN | 单元 5 |
| Lindeberg-Levy | CLT | 单元 5 |

## 核心方法

| 方法 | 说明 | 所在单元 |
|------|------|---------|
| Combinatorial probability | 组合概率计算 | 单元 1 |
| MGF derivation | MGF推导 | 单元 2 |
| Univariate transformation | 单变量变换 | 单元 3 |
| Quantile function | 分位数函数 | 单元 3 |
| Jacobian transformation | 雅可比变换 | 单元 4 |
| Normal approximation | 正态逼近 | 单元 5 |
| Simulation of sampling distributions | 抽样分布模拟 | 单元 6 |

---
*Probability, Statistics and Data Analysis I (STA237H1) — 公式速查手册*