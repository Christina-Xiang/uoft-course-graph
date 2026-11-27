# STA314H1 — 反例速查手册

| # | 反例 | 说明 |
|---|------|------|
| 1 | **K-means 对初始值敏感, 可能收敛到局部最优** |  |
| 2 | **过拟合** | 复杂模型在测试集上表现差 |

## 课程常见陷阱

| # | 陷阱 | 所在单元 |
|---|------|---------|
| 1 | **Using test error for model selection** (用测试误差做模型选择) | 单元 1 |
| 2 | **Features need standardization** (特征需标准化) | 单元 2 |
| 3 | **Data leakage** (数据泄漏) | 单元 3 |
| 4 | **Trees overfit without pruning** (不剪枝的树过拟合) | 单元 4 |
| 5 | **SVM scales poorly with n** (SVM扩展性差) | 单元 5 |
| 6 | **PCA sensitive to scaling** (PCA对缩放敏感) | 单元 6 |

---
*Statistical Methods for Machine Learning I (STA314H1) — 反例速查手册*