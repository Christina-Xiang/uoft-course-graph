# STA130H1 — 关键公式速查

## 核心公式

| 概念 | 公式 | 说明 |
|------|------|------|
| 样本均值 | $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$ | 集中趋势度量 |
| 样本方差 | $s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i-\bar{x})^2$ | 离散程度 |
| 标准差 | $s = \sqrt{s^2}$ | 同单位度量 |
| IQR | $Q_3 - Q_1$ | 四分位距 |
| 相关系数 | $r = \frac{\text{Cov}(x,y)}{s_x s_y}$ | 标准化相关 |
| 标准误 | $\text{SE}(\bar{x}) = s/\sqrt{n}$ | 均值的标准差 |
| CI (t) | $\bar{x} \pm t_{\alpha/2, n-1} \cdot s/\sqrt{n}$ | 未知 $\sigma$ |
| 单样本 t | $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ | 检验均值 |
| 双样本 t | $t = \frac{\bar{x}_1-\bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}$ | Welch 检验 |

## 课程核心定理

| 定理 | 英文 | 所在单元 |
|------|------|---------|
| conceptual | CLT | 单元 3 |
| conceptual | LLN | 单元 3 |
| 95%CI覆盖解释 | 95% CI coverage | 单元 4 |

## 核心方法

| 方法 | 说明 | 所在单元 |
|------|------|---------|
| ggplot2 pipeline | ggplot2可视化流程 | 单元 1 |
| dplyr workflow | dplyr工作流 | 单元 2 |
| Simulation with replicate()(replicate()模拟) |  | 单元 3 |
| Bootstrap CI | 自助法置信区间 | 单元 4 |
| Permutation test | 置换检验 | 单元 4 |
| lm() fitting(lm()拟合) |  | 单元 5 |
| Predict with model | 模型预测 | 单元 5 |
| R Markdown reports | R Markdown报告 | 单元 6 |

---
*An Introduction to Statistical Reasoning and Data Science (STA130H1) — 公式速查手册*