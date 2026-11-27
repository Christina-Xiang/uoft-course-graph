# STA314H1 — 关键公式速查

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
| 偏差-方差分解 | Bias-variance decomposition | 单元 1 |
| L1与L2收缩性质 | Shrinkage properties L1 vs L2 | 单元 2 |
| OOB误差无偏性 | OOB error unbiasedness | 单元 4 |
| 表示定理 | Representer theorem | 单元 5 |
| PCA=协方差特征分解 | PCA = eigendecomposition of covariance | 单元 6 |

## 核心方法

| 方法 | 说明 | 所在单元 |
|------|------|---------|
| K-fold cross-validation | K折交叉验证 | 单元 1 |
| glmnet for regularization | glmnet正则化 | 单元 2 |
| Tuning lambda via CV | CV调lambda | 单元 2 |
| caret::train()(caret::train()) |  | 单元 3 |
| Bootstrap CI | 自助法置信区间 | 单元 3 |
| randomForest()(randomForest()) |  | 单元 4 |
| xgboost tuning | xgboost调参 | 单元 4 |
| e1071::svm()(e1071::svm()) |  | 单元 5 |

---
*Statistical Methods for Machine Learning I (STA314H1) — 公式速查手册*