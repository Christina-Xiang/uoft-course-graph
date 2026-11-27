# MAT309H1 — 证明技巧指南

## 一、命题逻辑证明

### 自然演绎规则
| 规则 | 形式 |
|------|------|
| 合取引入 | $\dfrac{A\quad B}{A\wedge B}$ |
| 合取消去 | $\dfrac{A\wedge B}{A}$ |
| 蕴含消去 | $\dfrac{A\quad A\rightarrow B}{B}$ |
| 反证法 | $\dfrac{\neg A\vdash \bot}{A}$ |

## 二、一阶逻辑证明

### 量词规则
| 规则 | 形式 | 条件 |
|------|------|------|
| 全称引入 | $\dfrac{P(c)}{\forall x\,P(x)}$ | $c$ 不在前提中自由出现 |
| 全称消去 | $\dfrac{\forall x\,P(x)}{P(t)}$ | $t$ 可代入 |
| 存在引入 | $\dfrac{P(t)}{\exists x\,P(x)}$ | $t$ 自由替换 |
| 存在消去 | $\dfrac{\exists x\,P(x)\quad P(c)\vdash Q}{Q}$ | $c$ 新常数 |

## 三、Gödel 不完备定理

### 核心思路
1. Gödel 编码：将公式和证明编码为自然数
2. 自指语句：构造 $G$ = "$G$ 不可证"
3. $G$ 真但不可证 → 系统不完备


---
*Introduction to Mathematical Logic (MAT309H1) — 证明技巧指南*