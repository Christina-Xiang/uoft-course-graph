# MAT137Y1 — 关键公式速查

## 一、极限与连续

| 概念 | 公式 | 条件 |
|------|------|------|
| 极限定义 | $\lim_{x\to a} f(x) = L \iff \forall\varepsilon>0,\;\exists\delta>0$ 使得 $0<|x-a|<\delta \Rightarrow |f(x)-L|<\varepsilon$ | $f$ 在 $a$ 附近有定义 |
| 夹逼定理 | 若 $g(x)\le f(x)\le h(x)$ 且 $\lim g = \lim h = L$，则 $\lim f = L$ | 在 $a$ 的去心邻域内 |
| 连续定义 | $\lim_{x\to a} f(x) = f(a)$ | $f$ 在 $a$ 处有定义 |
| IVT | 若 $f\in C[a,b]$ 且 $y$ 介于 $f(a),f(b)$ 之间，则 $\exists c\in(a,b): f(c)=y$ | $f$ 在闭区间连续 |
| EVT | 若 $f\in C[a,b]$，则 $f$ 在 $[a,b]$ 上取得最大值和最小值 | $f$ 在闭区间连续 |

## 二、微分学

| 规则 | 公式 |
|------|------|
| 导数定义 | $f'(a) = \lim_{h\to 0} \frac{f(a+h)-f(a)}{h}$ |
| 乘积法则 | $(fg)' = f'g + fg'$ |
| 链式法则 | $(f\circ g)'(x) = f'(g(x))\,g'(x)$ |
| 商法则 | $(f/g)' = (f'g - fg')/g^2$ |
| MVT | $f(b)-f(a) = f'(c)(b-a)$ 对某 $c\in(a,b)$ | $f$ 在 $[a,b]$ 连续，$(a,b)$ 可导 |
| L'Hôpital | $\lim\frac{f}{g} = \lim\frac{f'}{g'}$ 若 $0/0$ 或 $\pm\infty/\pm\infty$ | 极限存在且 $g'(x)\neq0$ |

## 三、积分学

| 定理 | 公式 |
|------|------|
| FTC I | $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$ | $f$ 连续 |
| FTC II | $\int_a^b f(x)\,dx = F(b)-F(a)$ | $F' = f$ |
| 分部积分 | $\int u\,dv = uv - \int v\,du$ |
| 换元法 | $\int_a^b f(g(x))g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$ |

## 四、级数

| 测试 | 条件 | 结论 |
|------|------|------|
| 比值法 | $\lim |a_{n+1}/a_n| = L$ | $L<1$ 收敛，$L>1$ 发散 |
| 根值法 | $\lim \sqrt[n]{|a_n|} = L$ | $L<1$ 收敛，$L>1$ 发散 |
| 交错级数 | $b_n\searrow 0$ | $\sum (-1)^n b_n$ 收敛 |
| 积分法 | $\int_1^\infty f(x)\,dx$ 收敛 | $\sum f(n)$ 收敛 |
| p-级数 | $\sum 1/n^p$ | $p>1$ 收敛，$p\le 1$ 发散 |

## 五、泰勒展开

| 函数 | 麦克劳林展开 | 收敛域 |
|------|------------|--------|
| $e^x$ | $\sum_{n=0}^\infty x^n/n!$ | $\mathbb{R}$ |
| $\sin x$ | $\sum_{n=0}^\infty (-1)^n x^{2n+1}/(2n+1)!$ | $\mathbb{R}$ |
| $\cos x$ | $\sum_{n=0}^\infty (-1)^n x^{2n}/(2n)!$ | $\mathbb{R}$ |
| $\ln(1+x)$ | $\sum_{n=1}^\infty (-1)^{n-1} x^n/n$ | $(-1,1]$ |
| $(1+x)^\alpha$ | $\sum_{n=0}^\infty \binom{\alpha}{n} x^n$ | $(-1,1)$ |


---
*Calculus with Proofs (MAT137Y1) — 公式速查手册*