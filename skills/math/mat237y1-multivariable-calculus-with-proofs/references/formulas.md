# MAT237Y1 — 关键公式速查

## 一、多元函数

| 概念 | 定义 |
|------|------|
| 偏导数 | $\frac{\partial f}{\partial x_i}(a) = \lim_{h\to 0} \frac{f(a+he_i)-f(a)}{h}$ |
| 梯度 | $\nabla f = (\partial f/\partial x_1, \ldots, \partial f/\partial x_n)$ |
| 方向导数 | $D_v f(a) = \nabla f(a)\cdot v$ |
| 可微 | $f(a+h) = f(a) + \nabla f(a)\cdot h + o(\|h\|)$ |
| Jacobian | $J_f = [\partial f_i/\partial x_j]$ |
| Hessian | $H_f = [\partial^2 f/\partial x_i\partial x_j]$ |

## 二、多元积分

| 定理 | 公式 |
|------|------|
| Fubini | $\iint_{[a,b]\times[c,d]} f = \int_a^b\int_c^d f(x,y)\,dy\,dx$ |
| 换元 | $\int_{\varphi(U)} f = \int_U (f\circ\varphi)|\det D\varphi|$ |
| Green | $\oint_{\partial D} P\,dx+Q\,dy = \iint_D (Q_x-P_y)\,dx\,dy$ |
| Stokes | $\int_{\partial M} \omega = \int_M d\omega$ |
| Divergence | $\iiint_V \nabla\cdot\mathbf{F}\,dV = \iint_{\partial V} \mathbf{F}\cdot\mathbf{n}\,dS$ |

## 三、极值

| 方法 | 条件 |
|------|------|
| 临界点 | $\nabla f(a) = 0$ |
| 鞍点判别 | $H_f$ 不定 |
| Lagrange 乘数 | $\nabla f = \lambda\nabla g$（约束 $g=0$）|
| 二阶判别 | $H_f$ 正定→极小，负定→极大 |


---
*Multivariable Calculus with Proofs (MAT237Y1) — 公式速查手册*