# MAT237Y1 — 证明技巧指南

## 一、可微性证明

### 定义法
要证 $f$ 在 $a$ 可微：
```
证存在线性映射 $L$ 使得
lim_{h→0} |f(a+h) - f(a) - L(h)| / ‖h‖ = 0
```

## 二、极值证明

### 二阶判别法
1. 求临界点 $\nabla f(a) = 0$
2. 计算 Hessian $H_f(a)$
3. 若 $H_f$ 正定→局部极小；负定→局部极大；不定→鞍点

## 三、积分换元

### 换元步骤
1. 选择变换 $\varphi: U\to V$
2. 计算 Jacobian $|\det D\varphi|$
3. 将积分区域和被积函数用新变量表示

## 四、Stokes 型定理

| 定理 | 维度 | 关系 |
|------|------|------|
| Green | 2D | $\oint Pdx+Qdy = \iint (Q_x-P_y)dxdy$ |
| Stokes | 3D | $\int_{\partial S} \mathbf{F}\cdot d\mathbf{r} = \iint_S (\nabla\times\mathbf{F})\cdot d\mathbf{S}$ |
| Divergence | 3D | $\iiint_V \nabla\cdot\mathbf{F}\,dV = \iint_{\partial V} \mathbf{F}\cdot\mathbf{n}\,dS$ |


---
*Multivariable Calculus with Proofs (MAT237Y1) — 证明技巧指南*