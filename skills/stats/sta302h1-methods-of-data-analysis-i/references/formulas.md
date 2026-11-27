# STA302H1 — 关键公式速查

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
| 高斯-马尔可夫定理 | Gauss-Markov theorem | 单元 1 |
| FWL定理 | Frisch-Waugh-Lovell | 单元 2 |
| SST=SSR+SSE | ANOVA decomposition | 单元 3 |
| 正确模型残差性质 | Properties of residuals under correct model | 单元 4 |
| t检验与虚拟回归等价 | Equivalence of t-test and dummy regression | 单元 5 |
| AIC公式 | AIC = -2logL + 2k | 单元 6 |

## 核心方法

| 方法 | 说明 | 所在单元 |
|------|------|---------|
| lm() in R(R的lm()) |  | 单元 1 |
| summary | lm( | 单元 2 |
| VIF computation | VIF计算 | 单元 2 |
| confint()(confint()) |  | 单元 3 |
| predict()(predict()) |  | 单元 3 |
| plot | lm_obj | 单元 4 |
| Box-Cox transformation | Box-Cox变换 | 单元 4 |
| lm | y ~ x1 * x2 | 单元 5 |

---
*Methods of Data Analysis I (STA302H1) — 公式速查手册*