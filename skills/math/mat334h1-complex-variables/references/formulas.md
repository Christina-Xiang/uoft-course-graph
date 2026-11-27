# MAT334H1 — 关键公式速查

## 一、复变函数基础

| 概念 | 公式 |
|------|------|
| 复数 | $z = x + iy = re^{i\theta}$ |
| 共轭 | $\bar{z} = x - iy = re^{-i\theta}$ |
| 模 | $|z| = \sqrt{x^2 + y^2}$ |
| 辐角 | $\arg z = \theta$ |
| Cauchy-Riemann | $u_x = v_y$, $u_y = -v_x$ |

## 二、复积分

| 定理 | 公式 | 条件 |
|------|------|------|
| Cauchy 积分定理 | $\oint_\gamma f(z)\,dz = 0$ | $f$ 在单连通域解析 |
| Cauchy 积分公式 | $f(a) = \frac{1}{2\pi i}\oint_\gamma \frac{f(z)}{z-a}\,dz$ | $f$ 解析，$a$ 在 $\gamma$ 内 |
| 导数公式 | $f^{(n)}(a) = \frac{n!}{2\pi i}\oint_\gamma \frac{f(z)}{(z-a)^{n+1}}\,dz$ | $f$ 解析 |

## 三、级数展开

| 展开 | 公式 | 收敛域 |
|------|------|--------|
| Taylor | $f(z) = \sum_{n=0}^\infty a_n(z-a)^n$ | $|z-a| < R$ |
| Laurent | $f(z) = \sum_{n=-\infty}^\infty c_n(z-a)^n$ | 环形域 |
| 留数 | $\operatorname{Res}(f,a) = c_{-1}$ |

## 四、留数定理的应用

| 积分类型 | 方法 | 留数计算 |
|----------|------|---------|
| $\int_{-\infty}^\infty R(x)\,dx$ | 上半圆围道 | 上半平面极点留数和 |
| $\int_0^{2\pi} R(\cos\theta,\sin\theta)\,d\theta$ | $z = e^{i\theta}$ 单位圆 | 单位圆内极点留数和 |
| $\int_{-\infty}^\infty R(x)e^{iax}\,dx$ | Jordan 引理 | 上半平面留数 $\times 2\pi i$ |


---
*Complex Variables (MAT334H1) — 公式速查手册*