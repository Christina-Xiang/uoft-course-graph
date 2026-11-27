# STA238H1 — 关键公式速查

## 核心公式

| 概念 | 公式 | 说明 |
|------|------|------|
| MLE | $\hat{\theta} = \arg\max_\theta \prod f(x_i|\theta)$ | 极大似然 |
| Cram\'er-Rao | $\operatorname{Var}(\hat{\theta}) \ge 1/I(\theta)$ | 效率下界 |
| Wald 统计量 | $z = \hat{\theta}/\text{SE}(\hat{\theta})$ | 渐近正态 |
| LRT | $-2\log\Lambda \xrightarrow{d} \chi^2_k$ | 似然比检验 |
| Wald CI | $\hat{\theta} \pm z_{\alpha/2} \cdot \text{SE}(\hat{\theta})$ | 渐近区间 |

## 课程核心定理

| 定理 | 英文 | 所在单元 |
|------|------|---------|
| 估计量的大数定律 | LLN for estimators | 单元 1 |
| 估计量的CLT | CLT for estimators | 单元 1 |
| MLE渐近正态性 | Asymptotic normality of MLE | 单元 2 |
| C-R下界 | Cramer-Rao lower bound | 单元 2 |
| 枢轴量法 | Pivotal method | 单元 3 |
| N-P引理 | Neyman-Pearson lemma | 单元 4 |
| CI与检验的对偶性 | Duality of CI and test | 单元 4 |
| Wilks定理 | Wilks' theorem | 单元 5 |
| 高斯-马尔可夫定理 | Gauss-Markov theorem | 单元 6 |

## 核心方法

| 方法 | 说明 | 所在单元 |
|------|------|---------|
| Method of Moments | 矩估计法 | 单元 1 |
| Plug-in principle | 代入原理 | 单元 1 |
| MLE via calculus | 微积分求MLE | 单元 2 |
| Numerical optimization | 数值优化 | 单元 2 |
| Wald CI construction | Wald区间构建 | 单元 3 |
| Bootstrap percentile | 自助百分位法 | 单元 3 |
| t-test | t检验 | 单元 4 |
| Permutation test | 置换检验 | 单元 4 |

---
*Probability, Statistics and Data Analysis II (STA238H1) — 公式速查手册*