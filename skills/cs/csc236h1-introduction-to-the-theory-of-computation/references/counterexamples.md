# CSC236H1 — 常见错误与反例

| # | 常见错误 | 说明 |
|---|---------|------|
| 1 | **$O$ vs $\Theta$** | 上界不等于紧界; $n=O(n^2)$ 但 $n\neq\Theta(n^2)$ |
| 2 | **$T(n) = T(n/2) + T(n/2) + 1$ vs $T(n) = 2T(n/2) + 1$** | 前者 $O(n)$, 后者 $O(n)$ |
| 3 | **Master 定理不能直接套用** | $T(n) = T(n/2) + \log n$ 是情形 2 |
| 4 | **$a^nb^n$ 非正则** | 无法用有限状态跟踪计数 |
| 5 | **$a^nb^nc^n$ 非 CFL** | PDA 栈无法同时跟踪三个计数 |
| 6 | **$\{0^{2^n}\}$ 非 CFL** | 不是上下文无关 |
| 7 | **通用语言 $L_u$ 不可判定** | 对角化论证 |
| 8 | **Post Correspondence Problem (PCP) 不可判定** |  |
| 9 | **$\exists x\,P(x) \to Q$ 与 $\forall x\,(P(x)\to Q)$ 不等价 (若 $x$ 在 $Q$ 中自由)** |  |
| 10 | **归纳法错误** | 所有马都是同一颜色的错误证明 (基础 $n=1$ 到 $n=2$ 不成立) |
| 11 | **函数 $f(n) = n^{\sin n}$ 不是单调的, 渐进比较困难** |  |
| 12 | **非确定 vs 确定** | NTM 模拟 DTM 需指数开销 |

## 课程常见陷阱

| # | 陷阱 | 所在单元 |
|---|------|---------|
| 1 | **Weak induction vs strong induction** (弱归纳vs强归纳) | 单元 1 |
| 2 | **Confusing DFA and NFA definition** (混淆DFA与NFA定义) | 单元 2 |
| 3 | **Regular expressions ≠ all patterns** (正则表达式≠所有模式) | 单元 3 |
| 4 | **Left recursion** (左递归) | 单元 4 |
| 5 | **Confusing recognizable with decidable** (可识别与可判定混淆) | 单元 5 |
| 6 | **Reduction direction** (归约方向错误) | 单元 6 |

---
*Introduction to the Theory of Computation (CSC236H1) — 常见错误与反例*