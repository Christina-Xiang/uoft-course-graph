# STA304H1 — 概念依赖图谱

## 单元 1

- **Survey Design & Bias** (调查设计与偏差) → 依赖: Target population, Sampling frame, Coverage error, Nonresponse error
- **Target population** (目标总体) → 依赖: Sampling frame
- **Sampling frame** (抽样框) → 依赖: Coverage error
- **Coverage error** (覆盖误差) → 依赖: Nonresponse error
- **Nonresponse error** (无应答误差) → 依赖: Measurement error
- **Measurement error** (测量误差) → 依赖: Questionnaire design
- **Questionnaire design** (问卷设计)
- **Randomized response technique** (随机应答技术)
- **Coverage bias** (覆盖偏差)
- **Survey error identification** (调查误差识别)

## 单元 2

- **Simple Random Sampling** (简单随机抽样) → 依赖: SRS with/without replacement, FPC, Horvitz-Thompson estimator, Unbiasedness of sample mean under SRS
- **SRS with/without replacement** (有放回/无放回SRS) → 依赖: FPC
- **FPC** (有限总体校正) → 依赖: Horvitz-Thompson estimator
- **Horvitz-Thompson estimator** (Horvitz-Thompson估计量)
- **Unbiasedness of sample mean under SRS** (SRS下样本均值无偏性)
- **Sample size determination** (样本量确定)
- **Ignoring FPC** (忽略FPC)
- **SRS estimation** (SRS估计)

## 单元 3

- **Stratified Sampling** (分层抽样) → 依赖: Stratification, Proportional allocation, Neyman allocation, Post-stratification
- **Stratification** (分层) → 依赖: Proportional allocation
- **Proportional allocation** (比例分配) → 依赖: Neyman allocation
- **Neyman allocation** (Neyman分配) → 依赖: Post-stratification
- **Post-stratification** (事后分层)
- **Optimal allocation formula** (最优分配公式)
- **survey::svydesign()(survey::svydesign())** ()
- **Over-stratification** (过度分层)
- **Stratified estimation** (分层估计)

## 单元 4

- **Cluster & Systematic Sampling** (整群与系统抽样) → 依赖: PSU, SSU, Design effect, Intraclass correlation
- **PSU** (初级抽样单元) → 依赖: SSU
- **SSU** (二级抽样单元) → 依赖: Design effect
- **Design effect** (设计效应) → 依赖: Intraclass correlation
- **Intraclass correlation** (组内相关)
- **Relationship deff = 1 +** (m-1)
- **Multi-stage cluster sampling** (多阶段整群抽样)
- **Homogeneous clusters = large deff** (同质群=大设计效应)
- **Complex survey design** (复杂调查设计)

## 单元 5

- **Ratio & Regression Estimation** (比率与回归估计) → 依赖: Ratio estimator, Regression estimator, Auxiliary variable, Approx variance of ratio estimator
- **Ratio estimator** (比率估计量) → 依赖: Regression estimator
- **Regression estimator** (回归估计量) → 依赖: Auxiliary variable
- **Auxiliary variable** (辅助变量)
- **Approx variance of ratio estimator** (比率估计量近似方差)
- **survey::svyratio()(survey::svyratio())** ()
- **Ratio estimator bias in small samples** (小样本偏差)
- **Auxiliary variable utilization** (辅助变量利用)

## 单元 6

- **Observational Data & Causal Inference** (观测数据与因果推断) → 依赖: Confounding, Propensity score, IPW, Matching
- **Confounding** (混杂) → 依赖: Propensity score
- **Propensity score** (倾向得分) → 依赖: IPW
- **IPW** (逆概率加权) → 依赖: Matching
- **Matching** (匹配) → 依赖: Difference-in-differences
- **Difference-in-differences** (双重差分) → 依赖: MCAR/MAR/MNAR
- **MCAR/MAR/MNAR** (缺失数据机制)
- **Rubin causal model** (Rubin因果模型)
- **MatchIt for matching** (MatchIt匹配)
- **Propensity score estimation** (倾向得分估计)
- **Unmeasured confounding** (未测量混杂)
- **Causal reasoning** (因果推理)


---
*Surveys, Sampling and Observational Data (STA304H1) — 概念依赖图谱*