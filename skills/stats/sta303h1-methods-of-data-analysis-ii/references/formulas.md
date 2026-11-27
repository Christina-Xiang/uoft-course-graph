# STA303H1 — 关键公式速查

## 核心公式

| 概念 | 公式 | 说明 |
|------|------|------|
| OLS | $\hat{\beta} = (X^TX)^{-1}X^TY$ | 最小二乘 |
| 拟合值 | $\hat{Y} = X\hat{\beta} = HY$ | 帽子矩阵 |
| MSE | $\hat{\sigma}^2 = \frac{e^Te}{n-p-1}$ | 误差方差 |
| $R^2$ | $1 - \text{SS}_{\text{res}}/\text{SS}_{\text{tot}}$ | 决定系数 |
| Cook 距离 | $D_i = \frac{e_i^2}{p\hat{\sigma}^2}\frac{h_{ii}}{(1-h_{ii})^2}$ | 强影响点 |
| VIF | $1/(1-R_j^2)$ | 多重共线性 |

## 课程核心定理

| 定理 | 英文 | 所在单元 |
|------|------|---------|
| 方差分析=回归 | ANOVA = regression | 单元 1 |
| BLUP推导 | BLUP derivation | 单元 3 |
| GLM估计渐近正态 | Asymptotic normality of GLM estimates | 单元 4 |
| 拉普拉斯近似 | Laplace approximation | 单元 5 |
| Kenward-Roger自由度近似 | Kenward-Roger df approximation | 单元 6 |

## 核心方法

| 方法 | 说明 | 所在单元 |
|------|------|---------|
| aov() in R(R的aov()) |  | 单元 1 |
| emmeans for post-hoc | emmeans事后检验 | 单元 1 |
| dplyr pipeline | dplyr管道 | 单元 2 |
| ggplot2 best practices | ggplot2最佳实践 | 单元 2 |
| lmer() in lme4(lme4的lmer()) |  | 单元 3 |
| LRT for random effects | 随机效应LRT | 单元 3 |
| glm() with family(glm()族参数) |  | 单元 4 |
| IRLS algorithm | IRLS算法 | 单元 4 |

---
*Methods of Data Analysis II (STA303H1) — 公式速查手册*