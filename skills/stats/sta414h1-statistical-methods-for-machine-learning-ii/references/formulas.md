# STA414H1 — 关键公式速查

## 核心公式

| 概念 | 公式 | 说明 |
|------|------|------|
| 线性回归 | $y = w^Tx + b$ | $(y - \hat{y})^2$ |
| Logistic | $p(y=1|x) = \sigma(w^Tx)$ | 交叉熵 |
| SVM | $\min \frac{1}{2}\|w\|^2$ s.t. $y_i(w^Tx_i+b) \ge 1$ | Hinge loss |
| PCA | $\Sigma = Q\Lambda Q^T$ | 特征值分解 |
| F1 | $2\cdot\frac{P\cdot R}{P+R}$ | PR 均衡 |

## 课程核心定理

| 定理 | 英文 | 所在单元 |
|------|------|---------|
| η | E[suff stat] = ∇A | 单元 1 |
| 分解⇔d-分离 | Factorization ⇔ d-separation | 单元 2 |
| Hammersley-Clifford定理 | Hammersley-Clifford theorem | 单元 3 |
| 树上和积算法正确性 | Correctness of sum-product on trees | 单元 4 |
| x | ELBO = log p | 单元 5 |

## 核心方法

| 方法 | 说明 | 所在单元 |
|------|------|---------|
| Exponential family fitting | 指数族拟合 | 单元 1 |
| Forward-backward algorithm | 前向后向算法 | 单元 2 |
| Viterbi decoding | Viterbi解码 | 单元 2 |
| Pseudo-likelihood | 伪似然 | 单元 3 |
| Contrastive divergence | 对比散度 | 单元 3 |
| BP implementation | BP实现 | 单元 4 |
| VI for conjugate models | 共轭模型VI | 单元 5 |
| VAE implementation | VAE实现 | 单元 5 |

---
*Statistical Methods for Machine Learning II (STA414H1) — 公式速查手册*