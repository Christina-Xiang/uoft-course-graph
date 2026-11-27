# MAT224H1 — 关键公式速查

## 一、向量空间

| 概念 | 定义 |
|------|------|
| 向量空间 | 集合 $V$ 配加法和标量乘法，满足 8 条公理 |
| 子空间 | $U\subseteq V$ 对加法和标量乘法封闭 |
| 张成 | $\operatorname{span}(S) = \{\sum a_i v_i : v_i\in S\}$ |
| 线性无关 | $\sum a_i v_i = 0 \Rightarrow$ 所有 $a_i = 0$ |
| 基 | 线性无关的张成集 |
| 维数 | $\dim V = $ 基中向量个数 |

## 二、线性变换

| 概念 | 定义 | 矩阵表示 |
|------|------|---------|
| 线性变换 | $T(u+v)=T(u)+T(v)$, $T(cv)=cT(v)$ | $[T] \in \mathbb{F}^{m\times n}$ |
| 核 | $\ker T = \{v: T(v)=0\}$ | $\operatorname{null}(A)$ |
| 像 | $\operatorname{im} T = \{T(v): v\in V\}$ | $\operatorname{col}(A)$ |
| 秩-零化度 | $\dim V = \dim\ker T + \dim\operatorname{im} T$ | $n = \operatorname{nullity} + \operatorname{rank}$ |

## 三、内积空间

| 概念 | 定义 |
|------|------|
| 内积 | $\langle u,v\rangle$ 满足线性、对称、正定 |
| 范数 | $\|v\| = \sqrt{\langle v,v\rangle}$ |
| 正交 | $\langle u,v\rangle = 0$ |
| Gram-Schmidt | $u_k = v_k - \sum_{i<k} \frac{\langle v_k,u_i\rangle}{\|u_i\|^2} u_i$ |
| 投影 | $\operatorname{proj}_U(v) = \sum_i \frac{\langle v,u_i\rangle}{\|u_i\|^2} u_i$ |

## 四、特征值与对角化

| 概念 | 公式 |
|------|------|
| 特征值 | $Av = \lambda v$ 等价于 $\det(A-\lambda I)=0$ |
| 特征多项式 | $\chi_A(\lambda) = \det(A-\lambda I)$ |
| 代数重数 | $m_a(\lambda)$ = 特征多项式中的重数 |
| 几何重数 | $m_g(\lambda)$ = $\dim\ker(A-\lambda I)$ |
| 可对角化 | $m_g(\lambda) = m_a(\lambda)$ 对所有 $\lambda$ |
| 谱分解 | $A = Q\Lambda Q^T$（实对称矩阵）|


---
*Linear Algebra II (MAT224H1) — 公式速查手册*