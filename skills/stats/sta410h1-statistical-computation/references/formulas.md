# STA410H1 — 关键公式速查

## 核心公式

| 概念 | 公式 | 说明 |
|------|------|------|
| Newton-Raphson | $\theta^{(k+1)} = \theta^{(k)} - f(\theta^{(k)})/f'(\theta^{(k)})$ |  |
| EM | E: $Q(\theta|\theta^{(t)})$, M: $\theta^{(t+1)} = \arg\max Q$ |  |
| MH | $\alpha = \min(1, \frac{\pi(\theta')q(\theta|\theta')}{\pi(\theta)q(\theta'|\theta)})$ |  |

## 课程核心定理

| 定理 | 英文 | 所在单元 |
|------|------|---------|
| MC的√n收敛 | √n convergence of MC | 单元 2 |
| QR最小二乘 | QR for least squares | 单元 3 |
| 牛顿二次收敛 | Quadratic convergence of Newton | 单元 4 |
| EM单调增似然 | EM monotonically increases likelihood | 单元 5 |
| 细致平衡=>平稳分布 | Detailed balance => stationary | 单元 6 |

## 核心方法

| 方法 | 说明 | 所在单元 |
|------|------|---------|
| Inverse CDF implementation | 逆CDF实现 | 单元 1 |
| Rejection sampling | 拒绝抽样 | 单元 1 |
| Importance sampling implementation | 重要性抽样实现 | 单元 2 |
| Control variate regression | 控制变量回归 | 单元 2 |
| solve() vs qr()(solve() vs qr()) |  | 单元 3 |
| Cholesky for MVN sampling | Cholesky多元正态抽样 | 单元 3 |
| optim() in R(R的optim()) |  | 单元 4 |
| IRLS for GLMs | GLM的IRLS | 单元 4 |

---
*Statistical Computation (STA410H1) — 公式速查手册*