# STA302H1 — 概念依赖图谱

## 单元 1

- **EDA & Simple Linear Regression** (探索性数据分析与简单线性回归) → 依赖: Scatterplot, Pearson correlation, Simple linear model, Least squares estimation
- **Scatterplot** (散点图) → 依赖: Pearson correlation
- **Pearson correlation** (皮尔逊相关) → 依赖: Simple linear model
- **Simple linear model** (简单线性模型) → 依赖: Least squares estimation
- **Least squares estimation** (最小二乘估计) → 依赖: Fitted value
- **Fitted value** (拟合值) → 依赖: Residual
- **Residual** (残差)
- **Gauss-Markov theorem** (高斯-马尔可夫定理)
- **lm() in R(R的lm())** ()
- **Residual plot** (残差图)
- **Correlation ≠ causation** (相关不蕴含因果)
- **SLR interpretation** (简单线性回归解释)

## 单元 2

- **Multiple Linear Regression** (多元线性回归) → 依赖: Multiple regression model, Matrix notation, OLS in matrix form, Partial regression coefficient
- **Multiple regression model** (多元回归模型) → 依赖: Matrix notation
- **Matrix notation** (矩阵表示) → 依赖: OLS in matrix form
- **OLS in matrix form** (矩阵最小二乘) → 依赖: Partial regression coefficient
- **Partial regression coefficient** (偏回归系数) → 依赖: Adjusted R-squared
- **Adjusted R-squared** (调整R平方) → 依赖: Multicollinearity
- **Multicollinearity** (多重共线性)
- **Frisch-Waugh-Lovell** (FWL定理)
- **summary** (lm()
- **VIF computation** (VIF计算)
- **Multicollinearity inflates SE** (多重共线性膨胀标准误)
- **Matrix algebra for regression** (回归矩阵代数)

## 单元 3

- **Inference & ANOVA** (推断与方差分析) → 依赖: t-test for coefficients, F-test, Partial F-test, Confidence interval for coefficients
- **t-test for coefficients** (系数t检验) → 依赖: F-test
- **F-test** (F检验) → 依赖: Partial F-test
- **Partial F-test** (偏F检验) → 依赖: Confidence interval for coefficients
- **Confidence interval for coefficients** (系数置信区间) → 依赖: Prediction interval
- **Prediction interval** (预测区间)
- **ANOVA decomposition** (SST=SSR+SSE)
- **confint()(confint())** ()
- **predict()(predict())** ()
- **Prediction intervals much wider** (预测区间宽得多)
- **Statistical inference for regression** (回归推断)

## 单元 4

- **Model Diagnostics** (模型诊断) → 依赖: Residual analysis, Q-Q plot, Homoscedasticity, Leverage
- **Residual analysis** (残差分析) → 依赖: Q-Q plot
- **Q-Q plot** (Q-Q图) → 依赖: Homoscedasticity
- **Homoscedasticity** (方差齐性) → 依赖: Leverage
- **Leverage** (杠杆值) → 依赖: Cook's distance
- **Cook's distance** (Cook距离) → 依赖: Outlier
- **Outlier** (异常值)
- **Properties of residuals under correct model** (正确模型残差性质)
- **plot** (lm_obj)
- **Box-Cox transformation** (Box-Cox变换)
- **Over-transforming** (过度变换)
- **Diagnostic interpretation** (诊断解读)

## 单元 5

- **Interactions & Categorical Predictors** (交互作用与分类预测变量) → 依赖: Dummy variable, Reference category, Interaction term, Slope dummy vs intercept dummy
- **Dummy variable** (虚拟变量) → 依赖: Reference category
- **Reference category** (参照类别) → 依赖: Interaction term
- **Interaction term** (交互项) → 依赖: Slope dummy vs intercept dummy
- **Slope dummy vs intercept dummy** (斜率虚拟variable vs截距虚拟)
- **Equivalence of t-test and dummy regression** (t检验与虚拟回归等价)
- **lm** (y ~ x1 * x2)
- **emmeans post-hoc** (emmeans事后检验)
- **Dummy variable trap** (虚拟变量陷阱)
- **Interaction interpretation** (交互项解释)

## 单元 6

- **Model Building & Selection** (模型构建与选择) → 依赖: Stepwise selection, AIC, BIC, Cross-validation
- **Stepwise selection** (逐步选择) → 依赖: AIC
- **AIC** (AIC) → 依赖: BIC
- **BIC** (BIC) → 依赖: Cross-validation
- **Cross-validation** (交叉验证) → 依赖: Train/test split
- **Train/test split** (训练/测试分割) → 依赖: LASSO
- **LASSO** (LASSO)
- **AIC = -2logL + 2k** (AIC公式)
- **step() for selection(step()选择)** ()
- **K-fold CV** (K折交叉验证)
- **Stepwise inflates Type I error** (逐步法膨胀第一类错误)
- **Model validation** (模型验证)


---
*Methods of Data Analysis I (STA302H1) — 概念依赖图谱*