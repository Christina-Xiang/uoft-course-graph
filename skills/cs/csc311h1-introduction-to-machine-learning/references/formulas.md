# CSC311H1 — 关键公式与概念速查

## 核心公式/复杂度

| 概念 | 公式/描述 | 说明 |
|------|----------|------|
| 线性回归 | $y = w^Tx + b$ | 最小二乘 MSE |
| MSE 损失 | $\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$ | 回归损失 |
| Logistic 回归 | $p(y=1|x) = \sigma(w^Tx)$ 其中 $\sigma(z)=1/(1+e^{-z})$ | 二分类 |
| 交叉熵损失 | $-\sum [y\log\hat{p} + (1-y)\log(1-\hat{p})]$ | 分类损失 |
| Softmax | $p(y=k|x) = e^{z_k}/\sum_j e^{z_j}$ | 多分类 |
| SVM (硬间隔) | $\min \frac{1}{2}\|w\|^2$ s.t. $y_i(w^Tx_i+b)\ge 1$ | 最大间隔 |
| SVM (软间隔) | $\min \frac{1}{2}\|w\|^2 + C\sum \xi_i$ s.t. $y_i(w^Tx_i+b)\ge 1-\xi_i$ | 允许错误 |
| Kernel 技巧 | $K(x_i,x_j) = \phi(x_i)^T\phi(x_j)$ | 隐式高维映射 |
| RBF Kernel | $K(x_i,x_j) = \exp(-\gamma\|x_i-x_j\|^2)$ | 高斯核 |
| 神经网络前向 | $a^{(l)} = \sigma(W^{(l)}a^{(l-1)} + b^{(l)})$ | 多层感知机 |
| 反向传播 | $\delta^{(l)} = (W^{(l+1)})^T\delta^{(l+1)} \odot \sigma'(z^{(l)})$ | 链式法则 |
| 梯度下降 | $w := w - \eta\nabla_w L(w)$ | 一阶优化 |
| 动量 | $v := \beta v + \nabla_w L;\; w := w - \eta v$ | 加速收敛 |
| AdaGrad | $w := w - \frac{\eta}{\sqrt{G + \epsilon}} \odot g$ | 自适应学习率 |
| Adam | $m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t;\; v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2$ | 自适应矩估计 |
| PCA | $\Sigma = Q\Lambda Q^T$, 选择前 $k$ 大特征值对应特征向量 | 降维 |
| K-means | $c_i = \arg\min_j \|x_i - \mu_j\|^2;\; \mu_j = \frac{1}{|C_j|}\sum_{i\in C_j} x_i$ | 聚类 |
| GMM | $p(x) = \sum_{k=1}^K \pi_k \mathcal{N}(x|\mu_k,\Sigma_k)$ | 软聚类 |
| EM 算法 | E: $\gamma_{ik} = \frac{\pi_k \mathcal{N}(x_i|\mu_k,\Sigma_k)}{\sum_j \pi_j \mathcal{N}(x_i|\mu_j,\Sigma_j)}$; M: 更新 $\pi_k,\mu_k,\Sigma_k$ | 潜变量模型 |
| 决策树 | 信息增益 $\text{IG}(D, f) = H(D) - H(D|f)$ | CART/ID3 |
| 随机森林 | $\hat{y} = \text{mode}(h_1(x),\ldots,h_T(x))$ | Bagging + 特征随机 |
| 提升 (Boosting) | $F_T(x) = \sum_{t=1}^T \alpha_t h_t(x)$ | Adaboost/XGBoost |
| 偏差-方差 | $E[(y-\hat{f})^2] = \text{Bias}[\hat{f}]^2 + \text{Var}[\hat{f}] + \sigma^2$ | 泛化误差分解 |
| Bias-Variance Tradeoff | 模型复杂度 $\uparrow$ → Bias $\downarrow$, Var $\uparrow$ | 选择最优复杂度 |
| F1 Score | $2 \cdot \frac{P \cdot R}{P + R}$ | PR 调和平均 |
| AUC-ROC | TPR vs FPR 曲线下面积 | 分类器排序质量 |
| 交叉验证 | K-Fold: 数据分 K 份, K-1 训练 1 验证 | 模型选择 |
| L1 正则化 | $L(w) + \lambda\|w\|_1$ → 稀疏解 | 特征选择 |
| L2 正则化 | $L(w) + \lambda\|w\|_2^2$ → 权重衰减 | 防止过拟合 |

## 课程核心概念

| 概念 | 英文 | 所在单元 |
|------|------|---------|
| 线性回归回顾 | Linear regression review | 单元 1 |
| 岭回归 | Ridge regression | 单元 1 |
| LASSO | LASSO | 单元 1 |
| 多项式特征 | Polynomial features | 单元 1 |
| 基扩展 | Basis expansion | 单元 1 |
| 逻辑回归 | Logistic regression | 单元 2 |
| Softmax回归 | Softmax regression | 单元 2 |
| 决策边界 | Decision boundary | 单元 2 |
| K近邻 | KNN | 单元 2 |
| 朴素贝叶斯 | Naive Bayes | 单元 2 |
| 感知机 | Perceptron | 单元 3 |
| 多层感知机 | MLP | 单元 3 |
| 反向传播 | Backpropagation | 单元 3 |
| 激活函数 | Activation functions | 单元 3 |
| 正则化 | Regularization | 单元 3 |
| 决策树 | Decision tree | 单元 4 |
| 随机森林 | Random forest | 单元 4 |
| 梯度提升 | Gradient boosting | 单元 4 |
| 装袋vs提升 | Bagging vs boosting | 单元 4 |
| K均值聚类 | K-means clustering | 单元 5 |
| 层次聚类 | Hierarchical clustering | 单元 5 |
| 主成分分析 | PCA | 单元 5 |
| 高斯混合模型 | Gaussian mixture model | 单元 5 |
| 交叉验证 | Cross-validation | 单元 6 |
| 偏差-方差权衡 | Bias-variance tradeoff | 单元 6 |
| 数据泄漏 | Data leakage | 单元 6 |
| 模型评估指标 | Model evaluation metrics | 单元 6 |

---
*Introduction to Machine Learning (CSC311H1) — 公式与概念速查*