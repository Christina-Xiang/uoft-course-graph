# MAT244H1 — 关键公式速查

## 一、一阶 ODE

| 类型 | 标准形 | 解法 |
|------|--------|------|
| 可分离 | $dy/dx = g(x)h(y)$ | $\int dy/h(y) = \int g(x)\,dx$ |
| 线性 | $dy/dx + p(x)y = q(x)$ | $\mu = e^{\int p\,dx}$, $y = \frac{1}{\mu}\int \mu q\,dx$ |
| 恰当 | $M\,dx + N\,dy = 0$, $M_y = N_x$ | $F = \int M\,dx + \int (N-\partial/\partial y\int M\,dx)\,dy$ |
| Bernoulli | $y' + p(x)y = q(x)y^n$ | $u = y^{1-n}$ 化为线性 |

## 二、高阶线性 ODE

| 情形 | 通解 |
|------|------|
| 常系数齐次 | $y = \sum c_i e^{\lambda_i x}$（特征根 $\lambda_i$）|
| 重根 | $y = (c_1 + c_2 x + \ldots)e^{\lambda x}$ |
| 复根 | $y = e^{\alpha x}(c_1\cos\beta x + c_2\sin\beta x)$ |
| 非齐次（待定系数）| $y_p = $ 与 $f(x)$ 同形式 |
| 非齐次（参数变易）| $y_p = \int G(x,t)f(t)\,dt$ |

## 三、Laplace 变换

| 函数 | 变换 |
|------|------|
| $1$ | $1/s$ |
| $t^n$ | $n!/s^{n+1}$ |
| $e^{at}$ | $1/(s-a)$ |
| $\sin(at)$ | $a/(s^2+a^2)$ |
| $\cos(at)$ | $s/(s^2+a^2)$ |
| $f'(t)$ | $sF(s)-f(0)$ |

## 四、相平面与稳定性

| 特征值 | 平衡点类型 | 稳定性 |
|--------|----------|--------|
| 实, 同号 | 结点 | 负→稳定，正→不稳定 |
| 实, 异号 | 鞍点 | 不稳定 |
| 复, Re<0 | 稳定螺线 | 渐近稳定 |
| 复, Re>0 | 不稳定螺线 | 不稳定 |
| 纯虚 | 中心 | Lyapunov 稳定 |


---
*Introduction to ODEs (MAT244H1) — 公式速查手册*