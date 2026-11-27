# MAT223H1 — 证明技巧指南

## 一、向量空间证明

### 子空间判定
要证 $U\subseteq V$ 是子空间：
1. $0\in U$
2. 对加法封闭：$u_1+u_2\in U$ 对所有 $u_1,u_2\in U$
3. 对标量乘法封闭：$cu\in U$ 对所有 $c\in\mathbb{F}, u\in U$

### 线性无关证明
要证 $\{v_1,\ldots,v_n\}$ 线性无关：
```
设 ∑a_i v_i = 0，证明所有 a_i = 0
常用技巧：应用线性变换、取内积、代入特殊值
```

## 二、线性变换证明

### 核与像技巧
| 目标 | 方法 |
|------|------|
| 证单射 | 证 $\ker T = \{0\}$ |
| 证满射 | 证 $\operatorname{im} T = W$（对目标空间）|
| 维数关系 | 用秩-零化度定理 $\dim V = \dim\ker T + \dim\operatorname{im} T$ |

## 三、对角化证明

### 可对角化判定
1. 求特征值 $\lambda_1,\ldots,\lambda_k$
2. 对每个 $\lambda_i$，求 $m_g(\lambda_i) = \dim\ker(A-\lambda_i I)$
3. 若 $\sum m_g(\lambda_i) = n$，则可对角化

## 四、内积空间技巧

### Gram-Schmidt 正交化
1. $u_1 = v_1$
2. $u_k = v_k - \sum_{i<k} \langle v_k, u_i\rangle/\|u_i\|^2 \cdot u_i$
3. 归一化：$e_k = u_k/\|u_k\|$


---
*Linear Algebra I (MAT223H1) — 证明技巧指南*