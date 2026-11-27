# STA414H1 — 概念依赖图谱

## 单元 1

- **Probabilistic Models & Exponential Families** (概率模型与指数族) → 依赖: Natural parameters, Sufficient statistics, Log-partition function, Conjugate priors
- **Natural parameters** (自然参数) → 依赖: Sufficient statistics
- **Sufficient statistics** (充分统计量) → 依赖: Log-partition function
- **Log-partition function** (对数配分函数) → 依赖: Conjugate priors
- **Conjugate priors** (共轭先验) → 依赖: MLE in exponential families
- **MLE in exponential families** (指数族MLE)
- **E[suff stat] = ∇A** (η)
- **Exponential family fitting** (指数族拟合)
- **Natural parameters not identifiable** (自然参数不可识别)
- **Probabilistic modeling** (概率建模)

## 单元 2

- **Directed Graphical Models** (有向图模型) → 依赖: Bayesian network, d-separation, Plate notation, HMM
- **Bayesian network** (贝叶斯网络) → 依赖: d-separation
- **d-separation** (d-分离) → 依赖: Plate notation
- **Plate notation** (平板表示法) → 依赖: HMM
- **HMM** (隐马尔可夫模型) → 依赖: Probabilistic PCA
- **Probabilistic PCA** (概率PCA)
- **Factorization ⇔ d-separation** (分解⇔d-分离)
- **Forward-backward algorithm** (前向后向算法)
- **Viterbi decoding** (Viterbi解码)
- **Direction does not imply causation** (方向不蕴含因果)
- **Graphical model reasoning** (图模型推理)

## 单元 3

- **Undirected Graphical Models** (无向图模型) → 依赖: Markov random field, CRF, Potential function, Partition function
- **Markov random field** (马尔可夫随机场) → 依赖: CRF
- **CRF** (条件随机场) → 依赖: Potential function
- **Potential function** (势函数) → 依赖: Partition function
- **Partition function** (配分函数) → 依赖: Ising model
- **Ising model** (Ising模型)
- **Hammersley-Clifford theorem** (Hammersley-Clifford定理)
- **Pseudo-likelihood** (伪似然)
- **Contrastive divergence** (对比散度)
- **Partition function intractability** (配分函数难解)
- **Undirected model inference** (无向图推断)

## 单元 4

- **Exact Inference & Message Passing** (精确推断与消息传递) → 依赖: Variable elimination, Sum-product algorithm, Max-sum algorithm, Junction tree
- **Variable elimination** (变量消元) → 依赖: Sum-product algorithm
- **Sum-product algorithm** (和积算法) → 依赖: Max-sum algorithm
- **Max-sum algorithm** (最大和算法) → 依赖: Junction tree
- **Junction tree** (联合树) → 依赖: Treewidth
- **Treewidth** (树宽)
- **Correctness of sum-product on trees** (树上和积算法正确性)
- **BP implementation** (BP实现)
- **BP on loopy graphs may not converge** (环图BP可能不收敛)
- **Message passing inference** (消息传递推断)

## 单元 5

- **Approximate Inference** (近似推断) → 依赖: Variational inference, ELBO, Mean-field, SVI
- **Variational inference** (变分推断) → 依赖: ELBO
- **ELBO** (证据下界) → 依赖: Mean-field
- **Mean-field** (平均场) → 依赖: SVI
- **SVI** (随机变分推断) → 依赖: Reparameterization trick
- **Reparameterization trick** (重参数化技巧) → 依赖: VAE
- **VAE** (变分自编码器)
- **ELBO = log p** (x)
- **VI for conjugate models** (共轭模型VI)
- **VAE implementation** (VAE实现)
- **Mean-field underestimates variance** (平均场低估方差)
- **Variational methods** (变分方法)

## 单元 6

- **Deep Generative Models** (深度生成模型) → 依赖: GAN, Normalizing flows, Autoregressive models, Diffusion models
- **GAN** (生成对抗网络) → 依赖: Normalizing flows
- **Normalizing flows** (归一化流) → 依赖: Autoregressive models
- **Autoregressive models** (自回归模型) → 依赖: Diffusion models
- **Diffusion models** (扩散模型) → 依赖: Latent variable models
- **Latent variable models** (潜变量模型)
- **GAN training** (GAN训练)
- **Flow-based modeling** (流模型)
- **Mode collapse in GANs** (GAN模式坍塌)
- **Deep generative modeling** (深度生成建模)


---
*Statistical Methods for Machine Learning II (STA414H1) — 概念依赖图谱*