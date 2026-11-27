# MAT309H1 — 反例速查手册

> 按概念分类，标注反例破坏的条件

## 逻辑反例
| # | 反例 | 破坏概念 | 说明 |
|---|------|----------|------|
| 1 | $p\rightarrow q$ 真但 $p$ 假 | 实质蕴含悖论 | 假前提蕴含一切 |
| 2 | 停机问题 | 不可判定性 | 不存在判定程序是否停机的算法 |
| 3 | Gödel 语句 $G$ | 不完备性 | $G$ 真但不可证 |

## 量词反例
| # | 反例 | 破坏概念 | 说明 |
|---|------|----------|------|
| 4 | $\forall x\exists y\,P(x,y)$ vs $\exists y\forall x\,P(x,y)$ | 量词顺序 | $\forall x\exists y\, x<y$ 真但 $\exists y\forall x\, x<y$ 假 |
| 5 | $\neg\forall x\,P(x)$ 不等价于 $\forall x\,\neg P(x)$ | 量词否定 | 正确的是 $\exists x\,\neg P(x)$ |
| 6 | $\forall x\,(P(x)\lor Q(x))$ 与 $\forall x\,P(x)\lor\forall x\,Q(x)$ | 量词分配 | 前者强于后者: $P$ 偶 $Q$ 奇数在 $\mathbb{N}$ |

## 模型论反例
| # | 反例 | 破坏概念 | 说明 |
|---|------|----------|------|
| 7 | $\mathbb{N}$ vs $\mathbb{N}+\mathbb{Z}$ | 非标准模型 | Peano 算术存在非标准模型 |
| 8 | $\mathbb{Q}$ 和 $\mathbb{R}$ 都满足域公理 | 范畴性 | 一阶理论不能唯一确定无穷模型 |
| 9 | $\langle\mathbb{Q},<\rangle$ 和 $\langle\mathbb{R},<\rangle$ | 初等等价 | 同构于 $\mathbb{Q}$ 的任何稠密无端点线性序 |

## 证明论反例
| # | 反例 | 破坏概念 | 说明 |
|---|------|----------|------|
| 10 | $A\rightarrow B, A\rightarrow\neg B \vdash \neg A$ | 反证法 | 归谬法在直觉主义逻辑中不成立 |
| 11 | 排中律 $A\lor\neg A$ 在直觉主义逻辑中不可证 | 构造性 | 并非所有命题都有构造性证明 |
| 12 | Löb 定理: $\square(\square P\rightarrow P)\rightarrow\square P$ | 可证性逻辑 | 与 Gödel 第二不完备定理相关 |

## 可计算性反例
| # | 反例 | 破坏概念 | 说明 |
|---|------|----------|------|
| 13 | 一阶逻辑的可满足性问题 | 不可判定性 | Church 定理: 无算法判定公式可满足性 |
| 14 | Presburger 算术可判定但指数复杂 | 复杂度下界 | 双指数时间下界 |


---
*Introduction to Mathematical Logic (MAT309H1) — 反例速查手册*