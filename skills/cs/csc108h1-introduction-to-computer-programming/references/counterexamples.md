# CSC108H1 — 常见错误与反例

| # | 常见错误 | 说明 |
|---|---------|------|
| 1 | **$==$ vs $=$** | 赋值 vs 比较 |
| 2 | **死循环** | 缺少终止条件 |
| 3 | **可变默认参数** | $\text{def } f(x=[])$ 导致共享状态 |
| 4 | **列表别名** | $b = a$ 不复制, 修改 $b$ 影响 $a$ |
| 5 | **浅拷贝 vs 深拷贝** | 嵌套列表仅复制引用 |
| 6 | **字符串不可变** | $s[0] = 'a'$ 报错 |
| 7 | **整数溢出** | Python 无上限, 但浮点有精度损失 |
| 8 | **文件忘记关闭** | 资源泄漏 |
| 9 | **异常吞噬** | $\text{except: pass}$ 隐藏错误 |
| 10 | **变量作用域** | 函数内修改全局变量需 $\text{global}$ |
| 11 | **切片边界** | $\text{lst}[n:]$ 不会越界, 返回空列表 |
| 12 | **类型错误** | $\text{str} + \text{int}$ 报 TypeError |

## 课程常见陷阱

| # | 陷阱 | 所在单元 |
|---|------|---------|
| 1 | **Type confusion** (类型混淆) | 单元 1 |
| 2 | **Off-by-one errors** (差一错误) | 单元 2 |
| 3 | **Modifying global variables** (修改全局变量) | 单元 3 |
| 4 | **Mutable vs immutable** (可变vs不可变) | 单元 4 |
| 5 | **Forgetting to close files** (忘记关闭文件) | 单元 5 |
| 6 | **Self parameter forgotten** (忘记self参数) | 单元 6 |

---
*Introduction to Computer Programming (CSC108H1) — 常见错误与反例*