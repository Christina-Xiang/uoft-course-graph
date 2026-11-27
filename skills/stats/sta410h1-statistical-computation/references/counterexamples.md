# STA410H1 — 反例速查手册

| # | 反例 | 说明 |
|---|------|------|
| 1 | **EM 可能收敛到局部最优** |  |
| 2 | **MCMC 可能混合不良 (高维后验)** |  |

## 课程常见陷阱

| # | 陷阱 | 所在单元 |
|---|------|---------|
| 1 | **Poor PRNG quality** (PRNG质量差) | 单元 1 |
| 2 | **Importance weight degeneracy** (重要性权重退化) | 单元 2 |
| 3 | **Solving X'X directly is unstable** (直接求解X'X不稳定) | 单元 3 |
| 4 | **Newton diverges far from optimum** (牛顿法远离最优值发散) | 单元 4 |
| 5 | **EM may converge to local optimum** (EM可能收敛到局部最优) | 单元 5 |
| 6 | **Poor mixing** (high autocorrelation) | 单元 6 |

---
*Statistical Computation (STA410H1) — 反例速查手册*