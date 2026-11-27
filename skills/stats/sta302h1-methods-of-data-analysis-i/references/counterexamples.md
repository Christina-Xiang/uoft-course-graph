# STA302H1 — 反例速查手册

| # | 反例 | 说明 |
|---|------|------|
| 1 | **异方差** | 标准差低估, 检验失效 |
| 2 | **完全共线性** | $X^TX$ 不可逆 |

## 课程常见陷阱

| # | 陷阱 | 所在单元 |
|---|------|---------|
| 1 | **Correlation ≠ causation** (相关不蕴含因果) | 单元 1 |
| 2 | **Multicollinearity inflates SE** (多重共线性膨胀标准误) | 单元 2 |
| 3 | **Prediction intervals much wider** (预测区间宽得多) | 单元 3 |
| 4 | **Over-transforming** (过度变换) | 单元 4 |
| 5 | **Dummy variable trap** (虚拟变量陷阱) | 单元 5 |
| 6 | **Stepwise inflates Type I error** (逐步法膨胀第一类错误) | 单元 6 |

---
*Methods of Data Analysis I (STA302H1) — 反例速查手册*