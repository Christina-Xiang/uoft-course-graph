# STA410H1 — 概念依赖图谱

## 单元 1

- **Random Variate Generation** (随机变量生成) → 依赖: PRNG, LCG, Mersenne Twister, Inverse CDF method
- **PRNG** (伪随机数生成器) → 依赖: LCG
- **LCG** (线性同余生成器) → 依赖: Mersenne Twister
- **Mersenne Twister** (梅森旋转) → 依赖: Inverse CDF method
- **Inverse CDF method** (逆CDF法) → 依赖: Acceptance-rejection sampling
- **Acceptance-rejection sampling** (接受-拒绝抽样) → 依赖: Box-Muller
- **Box-Muller** (Box-Muller变换)
- **Inverse CDF implementation** (逆CDF实现)
- **Rejection sampling** (拒绝抽样)
- **Poor PRNG quality** (PRNG质量差)
- **Random generation** (随机生成)

## 单元 2

- **Monte Carlo Methods** (蒙特卡洛方法) → 依赖: Monte Carlo integration, MC error estimation, Importance sampling, Control variates
- **Monte Carlo integration** (MC积分) → 依赖: MC error estimation
- **MC error estimation** (MC误差估计) → 依赖: Importance sampling
- **Importance sampling** (重要性抽样) → 依赖: Control variates
- **Control variates** (控制变量法) → 依赖: Antithetic variates
- **Antithetic variates** (对偶变量法) → 依赖: Rao-Blackwellization
- **Rao-Blackwellization** (Rao-Blackwell化)
- **√n convergence of MC** (MC的√n收敛)
- **Importance sampling implementation** (重要性抽样实现)
- **Control variate regression** (控制变量回归)
- **Importance weight degeneracy** (重要性权重退化)
- **Variance reduction** (方差缩减)

## 单元 3

- **Numerical Linear Algebra** (数值线性代数) → 依赖: LU decomposition, QR decomposition, Cholesky decomposition, SVD
- **LU decomposition** (LU分解) → 依赖: QR decomposition
- **QR decomposition** (QR分解) → 依赖: Cholesky decomposition
- **Cholesky decomposition** (Cholesky分解) → 依赖: SVD
- **SVD** (奇异值分解) → 依赖: Condition number
- **Condition number** (条件数) → 依赖: Woodbury identity
- **Woodbury identity** (Woodbury恒等式)
- **QR for least squares** (QR最小二乘)
- **solve() vs qr()(solve() vs qr())** ()
- **Cholesky for MVN sampling** (Cholesky多元正态抽样)
- **Solving X'X directly is unstable** (直接求解X'X不稳定)
- **Matrix computation** (矩阵计算)

## 单元 4

- **Optimization for Statistics** (统计优化) → 依赖: Newton-Raphson, Fisher scoring, BFGS, Nelder-Mead
- **Newton-Raphson** (牛顿-拉夫森) → 依赖: Fisher scoring
- **Fisher scoring** (Fisher得分法) → 依赖: BFGS
- **BFGS** (BFGS) → 依赖: Nelder-Mead
- **Nelder-Mead** (Nelder-Mead) → 依赖: Coordinate descent
- **Coordinate descent** (坐标下降) → 依赖: SGD
- **SGD** (随机梯度下降)
- **Quadratic convergence of Newton** (牛顿二次收敛)
- **optim() in R(R的optim())** ()
- **IRLS for GLMs** (GLM的IRLS)
- **Newton diverges far from optimum** (牛顿法远离最优值发散)
- **Numerical optimization** (数值优化)

## 单元 5

- **EM Algorithm & Missing Data** (EM算法与缺失数据) → 依赖: EM algorithm, E-step, M-step, Missing data mechanisms
- **EM algorithm** (EM算法) → 依赖: E-step
- **E-step** (E步) → 依赖: M-step
- **M-step** (M步) → 依赖: Missing data mechanisms
- **Missing data mechanisms** (缺失数据机制) → 依赖: Mixture models via EM
- **Mixture models via EM** (EM混合模型) → 依赖: Censored data
- **Censored data** (删失数据)
- **EM monotonically increases likelihood** (EM单调增似然)
- **EM for Gaussian mixtures** (高斯混合EM)
- **EM may converge to local optimum** (EM可能收敛到局部最优)
- **EM derivation** (EM推导)

## 单元 6

- **MCMC & Bayesian Computation** (MCMC与贝叶斯计算) → 依赖: Markov chain theory, Metropolis-Hastings, Gibbs sampling, Hamiltonian Monte Carlo
- **Markov chain theory** (马尔可夫链理论) → 依赖: Metropolis-Hastings
- **Metropolis-Hastings** (Metropolis-Hastings) → 依赖: Gibbs sampling
- **Gibbs sampling** (Gibbs抽样) → 依赖: Hamiltonian Monte Carlo
- **Hamiltonian Monte Carlo** (哈密顿蒙特卡洛) → 依赖: Convergence diagnostics
- **Convergence diagnostics** (收敛诊断)
- **Detailed balance => stationary** (细致平衡=>平稳分布)
- **MH implementation** (MH实现)
- **coda for diagnostics** (coda诊断)
- **Poor mixing** (high autocorrelation)
- **MCMC methodology** (MCMC方法论)


---
*Statistical Computation (STA410H1) — 概念依赖图谱*