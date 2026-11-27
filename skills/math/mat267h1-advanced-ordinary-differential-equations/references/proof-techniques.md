# MAT267H1 — 证明技巧指南

## 一、一阶 ODE 解法选择

### 判定流程
```
给定 dy/dx = F(x,y)
1. 可分离？ F(x,y) = g(x)h(y) → 分离变量
2. 线性？ dy/dx + P(x)y = Q(x) → 积分因子
3. 恰当？ M dx + N dy = 0, M_y = N_x → 求势函数
4. Bernoulli？ y' + P(x)y = Q(x)y^n → u = y^{1-n}
5. 以上都不对 → 尝试积分因子或变换
```

## 二、常系数线性 ODE

### 求解步骤
1. 写出特征方程 $a_n r^n + \ldots + a_0 = 0$
2. 求特征根 $r_1,\ldots,r_n$
3. 根据根的类型写出基解组：
   - 实单根 → $e^{rx}$
   - 实重根 → $e^{rx}, xe^{rx}, \ldots$
   - 复根 → $e^{\alpha x}\cos\beta x, e^{\alpha x}\sin\beta x$

## 三、非齐次方程

### 待定系数法
| $f(x)$ 形式 | $y_p$ 猜测 |
|-------------|----------|
| $P_n(x)$ | $Q_n(x)$ |
| $P_n(x)e^{ax}$ | $Q_n(x)e^{ax}$ |
| $P_n(x)\sin\beta x$ 或 $P_n(x)\cos\beta x$ | $Q_n(x)\sin\beta x + R_n(x)\cos\beta x$ |
| $e^{ax}(\sin\beta x, \cos\beta x)$ | $e^{ax}(A\sin\beta x + B\cos\beta x)$ |

### 参数变易法（通用）
1. 解齐次方程得 $y_h = c_1y_1 + c_2y_2$
2. 设 $y_p = u_1(x)y_1 + u_2(x)y_2$
3. 解 $u_1'y_1 + u_2'y_2 = 0$, $u_1'y_1' + u_2'y_2' = f(x)$


---
*Advanced ODEs (MAT267H1) — 证明技巧指南*