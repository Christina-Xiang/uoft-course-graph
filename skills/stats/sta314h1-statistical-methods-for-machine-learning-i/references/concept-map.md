# STA314H1 — 概念依赖图谱

## 单元 1

- **Foundations of Statistical Learning** (统计学习基础) → 依赖: Supervised vs unsupervised, Training/test error, Bias-variance tradeoff, Overfitting
- **Supervised vs unsupervised** (监督vs非监督) → 依赖: Training/test error
- **Training/test error** (训练/测试误差) → 依赖: Bias-variance tradeoff
- **Bias-variance tradeoff** (偏差-方差权衡) → 依赖: Overfitting
- **Overfitting** (过拟合) → 依赖: Model capacity
- **Model capacity** (模型容量)
- **Bias-variance decomposition** (偏差-方差分解)
- **K-fold cross-validation** (K折交叉验证)
- **Using test error for model selection** (用测试误差做模型选择)
- **Model evaluation** (模型评估)

## 单元 2

- **Linear Methods** (线性方法) → 依赖: Ridge regression, LASSO, Elastic net, Logistic regression
- **Ridge regression** (岭回归) → 依赖: LASSO
- **LASSO** (LASSO) → 依赖: Elastic net
- **Elastic net** (弹性网络) → 依赖: Logistic regression
- **Logistic regression** (逻辑回归) → 依赖: LDA
- **LDA** (线性判别分析) → 依赖: Naive Bayes
- **Naive Bayes** (朴素贝叶斯)
- **Shrinkage properties L1 vs L2** (L1与L2收缩性质)
- **glmnet for regularization** (glmnet正则化)
- **Tuning lambda via CV** (CV调lambda)
- **Features need standardization** (特征需标准化)
- **Regularized regression** (正则化回归)

## 单元 3

- **Resampling & Evaluation** (重抽样与评估) → 依赖: Bootstrap, Bootstrap optimism, ROC curve, AUC
- **Bootstrap** (自助法) → 依赖: Bootstrap optimism
- **Bootstrap optimism** (自助法乐观偏差) → 依赖: ROC curve
- **ROC curve** (ROC曲线) → 依赖: AUC
- **AUC** (AUC)
- **caret::train()(caret::train())** ()
- **Bootstrap CI** (自助法置信区间)
- **Data leakage** (数据泄漏)
- **Classifier evaluation** (分类器评估)

## 单元 4

- **Tree-Based & Ensemble Methods** (基于树与集成方法) → 依赖: Decision tree, Pruning, Random forest, Bagging
- **Decision tree** (决策树) → 依赖: Pruning
- **Pruning** (剪枝) → 依赖: Random forest
- **Random forest** (随机森林) → 依赖: Bagging
- **Bagging** (装袋) → 依赖: Boosting
- **Boosting** (提升) → 依赖: XGBoost
- **XGBoost** (XGBoost)
- **OOB error unbiasedness** (OOB误差无偏性)
- **randomForest()(randomForest())** ()
- **xgboost tuning** (xgboost调参)
- **Trees overfit without pruning** (不剪枝的树过拟合)
- **Ensemble learning** (集成学习)

## 单元 5

- **SVM & Kernel Methods** (支持向量机与核方法) → 依赖: Maximal margin classifier, Support vector, Kernel trick, RBF kernel
- **Maximal margin classifier** (最大间隔分类器) → 依赖: Support vector
- **Support vector** (支持向量) → 依赖: Kernel trick
- **Kernel trick** (核技巧) → 依赖: RBF kernel
- **RBF kernel** (RBF核) → 依赖: Soft margin
- **Soft margin** (软间隔)
- **Representer theorem** (表示定理)
- **e1071::svm()(e1071::svm())** ()
- **Kernel selection** (核选择)
- **SVM scales poorly with n** (SVM扩展性差)
- **Kernel method understanding** (核方法理解)

## 单元 6

- **Unsupervised Learning & Dim Reduction** (无监督学习与降维) → 依赖: PCA, k-means clustering, Hierarchical clustering, Elbow method
- **PCA** (主成分分析) → 依赖: k-means clustering
- **k-means clustering** (k均值聚类) → 依赖: Hierarchical clustering
- **Hierarchical clustering** (层次聚类) → 依赖: Elbow method
- **Elbow method** (肘部法) → 依赖: Silhouette
- **Silhouette** (轮廓系数) → 依赖: t-SNE
- **t-SNE** (t-SNE)
- **PCA = eigendecomposition of covariance** (PCA=协方差特征分解)
- **prcomp()(prcomp())** ()
- **kmeans()(kmeans())** ()
- **PCA sensitive to scaling** (PCA对缩放敏感)
- **Dimensionality reduction** (降维)


---
*Statistical Methods for Machine Learning I (STA314H1) — 概念依赖图谱*