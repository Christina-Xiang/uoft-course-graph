# STA261H1 — 关键公式速查

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
| 因子分解定理 | Factorization theorem | 单元 1 |
| Basu定理 | Basu's theorem | 单元 1 |
| Rao-Blackwell定理 | Rao-Blackwell theorem | 单元 1 |
| C-R不等式 | Cramer-Rao inequality | 单元 2 |
| MLE渐近正态 | Asymptotic normality of MLE | 单元 2 |
| N-P引理 | Neyman-Pearson lemma | 单元 3 |
| Karlin-Rubin定理 | Karlin-Rubin theorem | 单元 3 |
| 与检验的对偶性 | Duality with hypothesis tests | 单元 4 |
| MLE相合性 | Consistency of MLE | 单元 5 |
| LRT渐近分布 | Asymptotic distribution of LRT | 单元 5 |

## 核心方法

| 方法 | 说明 | 所在单元 |
|------|------|---------|
| Finding sufficient statistics | 寻找充分统计量 | 单元 1 |
| MLE computation | MLE计算 | 单元 2 |
| Fisher scoring | Fisher得分法 | 单元 2 |
| MP test construction | 最大功效检验构造 | 单元 3 |
| LRT construction | 似然比检验构造 | 单元 3 |
| Pivotal method | 枢轴量法 | 单元 4 |
| Inverting LRT | 反转似然比检验 | 单元 4 |
| Delta method | Delta方法 | 单元 5 |

---
*Probability and Statistics II (STA261H1) — 公式速查手册*