# MAT315H1 — 关键公式速查

## 一、整除与同余

| 概念 | 定义 |
|------|------|
| 整除 | $a\mid b \iff \exists k: b = ak$ |
| 同余 | $a\equiv b\pmod m \iff m\mid (a-b)$ |
| gcd | $\gcd(a,b)$ = 最大公因数 |
| Bezout | $\exists x,y:\, ax+by = \gcd(a,b)$ |
| Euler 定理 | $a^{\varphi(m)} \equiv 1\pmod m$ 若 $\gcd(a,m)=1$ |
| 中国剩余定理 | 同余方程组 $x\equiv a_i\pmod{m_i}$ 有唯一解模 $\prod m_i$ |

## 二、二次互反

| 符号 | 定义 |
|------|------|
| Legendre 符号 | $\left(\frac{a}{p}\right) = a^{(p-1)/2}\pmod p$ |
| Euler 准则 | $\left(\frac{a}{p}\right) \equiv a^{(p-1)/2}\pmod p$ |
| 二次互反律 | $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}$ |

## 三、素数分布

| 定理 | 公式 |
|------|------|
| 素数定理 | $\pi(x) \sim x/\ln x$ |
| Dirichlet 定理 | $\gcd(a,d)=1$ 则 $a\bmod d$ 有无穷多素数 |
| Chebyshev 估计 | $0.9\cdot x/\ln x < \pi(x) < 1.1\cdot x/\ln x$（充分大 $x$）|


---
*Introduction to Number Theory (MAT315H1) — 公式速查手册*