# CSC236H1 — 关键公式与概念速查

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
| 简单归纳 | Simple induction | 单元 1 |
| 完全归纳 | Complete induction | 单元 1 |
| 结构归纳 | Structural induction | 单元 1 |
| 循环不变式 | Loop invariants | 单元 1 |
| 前置/后置条件 | Pre/post conditions | 单元 1 |
| 确定型有限自动机 | DFA | 单元 2 |
| 非确定型有限自动机 | NFA | 单元 2 |
| ε-NFA | ε-NFA | 单元 2 |
| 正则语言 | Regular language | 单元 2 |
| 封闭性质 | Closure properties | 单元 2 |
| 正则表达式语法 | Regular expression syntax | 单元 3 |
| Kleene星号 | Kleene star | 单元 3 |
| 正则转NFA | Regular expression to NFA | 单元 3 |
| 非正则语言 | Non-regular languages | 单元 3 |
| 上下文无关文法 | CFG | 单元 4 |
| 派生 | Derivation | 单元 4 |
| 解析树 | Parse tree | 单元 4 |
| 下推自动机 | PDA | 单元 4 |
| 歧义性 | Ambiguity | 单元 4 |
| 图灵机定义 | Turing machine definition | 单元 5 |
| 可识别vs可判定 | Recognizable vs decidable | 单元 5 |
| 停机问题 | Halting problem | 单元 5 |
| 不可判定性 | Undecidability | 单元 5 |
| P类 | P class | 单元 6 |
| NP类 | NP class | 单元 6 |
| NP完全性 | NP-completeness | 单元 6 |
| 归约 | Reduction | 单元 6 |
| SAT问题 | SAT problem | 单元 6 |

---
*Introduction to the Theory of Computation (CSC236H1) — 公式与概念速查*