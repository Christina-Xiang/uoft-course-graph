# CSC236H1 — 推理与技巧指南

### 1. 停机问题不可判定: 对角化证明, 假设判定器 $H$ 存在, 构造 $D(x) = \text{loop if } H(x,x)=\text{halt}$, 导出矛盾

### 2. Master 定理三种情形: 比较 $f(n)$ 与 $n^{\log_b a}$ (小于/等于/大于)

### 3. Pumping Lemma 证明非正则: $a^nb^n$ 不可能被 DFA 识别

### 4. Pumping Lemma 证明非 CFL: $a^nb^nc^n$ 不是上下文无关

### 5. 归纳法证明程序正确性: 循环不变量 + 基础情况 + 归纳步

### 6. 对偶性: DFA/NFA 等价性 — 子集构造法

### 7. Church-Turing 论题: TM 可计算 = 直觉可计算

### 8. 多项式归约: $A\le_p B$ 意味着 $B$ 至少和 $A$ 一样难

### 9. SAT 归约到 3-SAT: 子句拆分引入新变量

### 10. 3-SAT 归约到 CLIQUE: 构造 $(\bar{x}_i\lor\bar{x}_j)$ 对应边

### 11. 3-SAT 归约到 VERTEX-COVER: 构造 $(\bar{x}_i)$ 三角形 + 边连接

### 12. 3-SAT 归约到 SUBSET-SUM: 数字构造编码变量赋值

### 13. 3-SAT 归约到 HAMILTONIAN-PATH: 变量/子句子图

### 14. 含等式逻辑: 使用替换规则保持真值

### 15. CYK 算法: CFG 成员性问题的动态规划解法 $O(n^3)$

## 核心方法

- **Program correctness proof** (程序正确性证明) — 单元 1
- **DFA construction** (DFA构造) — 单元 2
- **NFA to DFA conversion** (NFA转DFA) — 单元 2
- **Regex to NFA** (Thompson) — 单元 3
- **CFG construction** (CFG构造) — 单元 4
- **PDA design** (PDA设计) — 单元 4
- **TM construction** (图灵机构造) — 单元 5
- **Polynomial reduction** (多项式归约) — 单元 6

## 编程技巧

- **Loop invariant discovery** (循环不变式发现) — 单元 1
- **NP-completeness proof** (NP完全性证明) — 单元 6

---
*Introduction to the Theory of Computation (CSC236H1) — 推理与技巧指南*