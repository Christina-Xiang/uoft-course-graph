# CSC311H1 — 推理与技巧指南

### 1. 偏差-方差分解: $E[(y-\hat{f})^2] = \text{Bias}^2 + \text{Var} + \sigma^2$

### 2. SVM 对偶: KKT 条件导出支持向量, $w = \sum \alpha_i y_i x_i$

### 3. 梯度下降收敛: 凸函数上 $L(w^{(t)}) - L(w^*) \le O(1/t)$ 固定步长

### 4. SGD 收敛: 递减学习率 $\sum \eta_t = \infty, \sum \eta_t^2 < \infty$ 保证收敛

### 5. 逻辑回归是广义线性模型: $g(\mu) = w^Tx$ 其中 $g$ 是 logit 链接

### 6. PCA 最优性: 最大化方差等价于最小化重构误差

### 7. K-means 收敛: 每次迭代目标函数单调非增, 有限步内收敛

### 8. EM 单调性: $\log L(\theta^{(t+1)}) \ge \log L(\theta^{(t)})$

### 9. 信息增益非负: $H(D) \ge H(D|f)$ 条件熵不大于无条件熵

### 10. VC 维: 模型 $H$ 能打散的最大样本数, 控制泛化能力

### 11. No Free Lunch 定理: 所有算法在所有问题上平均表现相同

## 核心方法

- **Gradient descent** (梯度下降) — 单元 1
- **One-vs-all classification** (一对多分类) — 单元 2
- **Neural network training** (神经网络训练) — 单元 3
- **Random forest training** (随机森林训练) — 单元 4
- **EM for GMM** (高斯混合EM) — 单元 5
- **ML pipeline design** (ML管道设计) — 单元 6

## 编程技巧

- **Feature scaling** (特征缩放) — 单元 1
- **Hyperparameter tuning** (超参数调优) — 单元 2
- **Dropout** (Dropout) — 单元 3
- **Feature importance** (特征重要性) — 单元 4

---
*Introduction to Machine Learning (CSC311H1) — 推理与技巧指南*