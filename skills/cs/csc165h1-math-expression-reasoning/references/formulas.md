# CSC165H1 — 关键公式与概念速查

## 核心公式/复杂度

| 概念 | 公式/描述 | 说明 |
|------|----------|------|
| Big-O | $\exists c>0,n_0>0: \forall n\ge n_0, f(n) \le c\cdot g(n)$ | 渐进上界 |
| Big-Omega | $\exists c>0,n_0>0: \forall n\ge n_0, f(n) \ge c\cdot g(n)$ | 渐进下界 |
| Big-Theta | $f=O(g) \land f=\Omega(g)$ | 渐进紧界 |
| Master 定理 | $T(n) = aT(n/b) + f(n)$, 比较 $f(n)$ 与 $n^{\log_b a}$ | 分治递推 |
| Stirling 近似 | $\log(n!) = n\log n - n + O(\log n)$ | 阶乘渐近 |
| DFA 定义 | $M = (Q,\Sigma,\delta,q_0,F)$ | 有限状态自动机 |
| NFA 定义 | $M = (Q,\Sigma,\delta,q_0,F)$, $\delta: Q\times\Sigma_\epsilon\to\mathcal{P}(Q)$ | 非确定自动机 |
| 正则语言 | $L$ 被 DFA/NFA/正则表达式描述 | Chomsky 3 型 |
| Pumping Lemma (RL) | $\forall w\in L,|w|\ge p: w = xyz, |xy|\le p, |y|\ge 1$, $xy^kz\in L$ | 正则语言必要条件 |
| CFG 定义 | $G = (V,\Sigma,R,S)$ | 上下文无关文法 |
| PDA 定义 | $M = (Q,\Sigma,\Gamma,\delta,q_0,Z_0,F)$ | 下推自动机 |
| Pumping Lemma (CFL) | $\forall w\in L,|w|\ge p: w=uvxyz$, $|vxy|\le p$, $|vy|\ge 1$, $uv^kxy^kz\in L$ | CFL 必要条件 |
| TM 定义 | $M = (Q,\Sigma,\Gamma,\delta,q_0,q_{\text{accept}},q_{\text{reject}})$ | 图灵机 |
| NP 定义 | 非确定 TM 多项式时间可解 | 验证阶段 $O(n^k)$ |
| NP-Complete | $L \in NP \land \forall L'\in NP: L'\le_p L$ | 最难的 NP 问题 |
| Cook-Levin | SAT 是 NP-Complete | 第一个 NPC 问题 |
| 3-CNF 逻辑 | $(x_1 \lor x_2 \lor \bar{x}_3) \land (\bar{x}_1 \lor x_3 \lor x_4)$ | 合取范式 |
| De Morgan 律 | $\overline{P\land Q} = \bar{P}\lor\bar{Q}$, $\overline{P\lor Q} = \bar{P}\land\bar{Q}$ | 逻辑等价 |
| 蕴含 | $P\to Q \equiv \bar{P}\lor Q$ | 条件语句 |
| 量词否定 | $\neg\forall x\,P(x) \equiv \exists x\,\neg P(x)$ | 量词对偶 |
| 数学归纳法 | $P(1) \land [P(k)\to P(k+1)] \implies \forall n\,P(n)$ | 自然数证明 |
| 完全归纳 | $[\forall i<k\,P(i)] \to P(k) \implies \forall n\,P(n)$ | 强归纳 |
| 结构归纳 | 递归定义结构的良基归纳 | 树/列表证明 |
| 鸽巢原理 | 若 $n$ 个物品放入 $m$ 个盒子且 $n>m$, 则至少有一个盒子有 $\ge 2$ 个 | 计数论证 |

## 课程核心概念

| 概念 | 英文 | 所在单元 |
|------|------|---------|
| 命题 | Proposition | 单元 1 |
| 逻辑连接词 | Logical connectives | 单元 1 |
| 真值表 | Truth tables | 单元 1 |
| 重言式/矛盾 | Tautology/contradiction | 单元 1 |
| 全称量词∀ | Universal quantifier ∀ | 单元 2 |
| 存在量词∃ | Existential quantifier ∃ | 单元 2 |
| 嵌套量词 | Nested quantifiers | 单元 2 |
| 量词否定 | Negation of quantifiers | 单元 2 |
| 直接证明 | Direct proof | 单元 3 |
| 逆否证明 | Proof by contrapositive | 单元 3 |
| 反证法 | Proof by contradiction | 单元 3 |
| 归纳法证明 | Proof by induction | 单元 3 |
| 存在性证明 | Existence proof | 单元 3 |
| 整除性 | Divisibility | 单元 4 |
| 最大公约数 | GCD | 单元 4 |
| 欧几里得算法 | Euclidean algorithm | 单元 4 |
| 模运算 | Modular arithmetic | 单元 4 |
| 扩展欧几里得算法 | Extended Euclidean algorithm | 单元 4 |
| 最坏情况复杂度 | Worst-case complexity | 单元 5 |
|  | Asymptotic notation (O | 单元 5 |
|  | Ω | 单元 5 |
| 渐近符号 | Θ) | 单元 5 |
| 循环不变式 | Loop invariants | 单元 5 |
| 图定义 | Graph definitions | 单元 6 |
| 树的性质 | Tree properties | 单元 6 |
| 二分图 | Bipartite graphs | 单元 6 |
| 图着色 | Graph coloring | 单元 6 |

---
*Mathematical Expression and Reasoning for Computer Science (CSC165H1) — 公式与概念速查*