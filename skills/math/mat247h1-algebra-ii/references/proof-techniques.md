# MAT247H1 — 证明技巧指南

## 一、群论证明

### 子群判定
要证 $H\subseteq G$ 是子群：对任意 $a,b\in H$，有 $ab^{-1}\in H$

### 同态基本定理
1. 构造同态 $\varphi: G\to H$
2. 证 $\ker\varphi \trianglelefteq G$
3. 由 $G/\ker\varphi \cong \operatorname{im}\varphi$ 得到同构

### 正规子群证明
要证 $N\trianglelefteq G$：对任意 $g\in G, n\in N$，有 $gng^{-1}\in N$

## 二、环论证明

### 理想判定
要证 $I\subseteq R$ 是理想：
1. $I$ 是加法子群
2. 对任意 $r\in R, a\in I$，有 $ra\in I$ 且 $ar\in I$

### 商环同构
利用 $R/I \cong S$ 通过构造满同态 $\varphi: R\to S$，证 $\ker\varphi = I$

## 三、模论技巧

### 循环模分解
有限生成 $\mathbb{F}[x]$-模 → 不变因子 → 循环子模直和分解

### Jordan 标准形构造
1. 将 $V$ 视为 $\mathbb{F}[x]$-模（$x\cdot v = T(v)$）
2. 分解为循环子模
3. 每个循环子模对应一个 Jordan 块


---
*Algebra II (MAT247H1) — 证明技巧指南*