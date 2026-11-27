# MAT315H1 — 证明技巧指南

## 一、同余证明

### 常用技巧
1. 模运算：$a\equiv b\pmod m \Rightarrow a^n\equiv b^n\pmod m$
2. 费马小定理：$a^p\equiv a\pmod p$
3. Euler 定理：$a^{\varphi(m)}\equiv 1\pmod m$ 若 $\gcd(a,m)=1$

## 二、二次互反证明

### Legendre 符号计算
1. 用 Euler 准则 $\left(\frac{a}{p}\right) \equiv a^{(p-1)/2}\pmod p$
2. 用二次互反律化简 $\left(\frac{p}{q}\right)$
3. 用补充公式 $\left(\frac{-1}{p}\right) = (-1)^{(p-1)/2}$, $\left(\frac{2}{p}\right) = (-1)^{(p^2-1)/8}$

## 三、丢番图方程

### 无穷递降法
假设存在正整数解 → 构造更小的正整数解 → 矛盾

### 同余分析法
对方程两边取模，利用模运算的约束排除解


---
*Introduction to Number Theory (MAT315H1) — 证明技巧指南*