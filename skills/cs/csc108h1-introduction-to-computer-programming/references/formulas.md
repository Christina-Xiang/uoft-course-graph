# CSC108H1 — 关键公式与概念速查

## 核心公式/复杂度

| 概念 | 公式/描述 | 说明 |
|------|----------|------|
| 变量赋值 | $x \leftarrow \text{value}$ | Python 动态类型 |
| 算术运算符 | $+,\,-,\,*,\,/,\,//,\,\%,\,**$ | 基础运算 |
| 字符串拼接 | $\text{str1} + \text{str2}$ | 字符串连接 |
| 列表索引 | $\text{lst}[i] \quad (0 \le i < n)$ | 0-indexed 访问 |
| 切片 | $\text{lst}[i:j:k]$ | 子列表提取 |
| 条件 | $\text{if } P:\ldots\text{ elif } Q:\ldots\text{ else}:\ldots$ | 分支控制 |
| while 循环 | $\text{while } B:\ldots$ | 条件循环 |
| for 循环 | $\text{for } x \in S:\ldots$ | 可迭代遍历 |
| 函数定义 | $\text{def } f(p_1,\ldots,p_n):\ldots$ | 参数传递 |
| 文件读写 | $\text{open}(f, 'r')/\text{open}(f, 'w')$ | I/O 操作 |
| 异常处理 | $\text{try:}\ldots\text{ except } E:\ldots$ | 错误捕获 |
| 列表推导式 | $[f(x) \text{ for } x \text{ in } S \text{ if } P(x)]$ | 函数式构造 |
| 字典 | $\{k_1:v_1,\ldots,k_n:v_n\}$ | 键值映射 |
| 集合 | $\{x_1,\ldots,x_n\}$ | 无序无重复 |
| 模块导入 | $\text{import } M \; / \; \text{from } M \text{ import } f$ | 代码复用 |
| 线性搜索 | $T(n) = O(n)$ | 最坏情况比较次数 |
| 二分搜索 | $T(n) = O(\log n)$ (需要排序) | 分治查找 |
| 选择排序 | $T(n) = O(n^2)$ | 简单排序 |
| 归并排序 | $T(n) = O(n \log n)$ | 分治排序 |
| 递归基础 | $T(n) = T(n-1) + O(1) \implies O(n)$ | 线性递归 |

## 课程核心概念

| 概念 | 英文 | 所在单元 |
|------|------|---------|
| 变量与类型 | Variables & types | 单元 1 |
| 表达式 | Expressions | 单元 1 |
| 输入/输出 | Input/output | 单元 1 |
| 布尔逻辑 | Boolean logic | 单元 1 |
| 条件语句 | if/elif/else | 单元 2 |
| for循环 | for loops | 单元 2 |
| while循环 | while loops | 单元 2 |
| 嵌套循环 | Nested loops | 单元 2 |
| 函数定义 | Function definition | 单元 3 |
| 参数与实参 | Parameters & arguments | 单元 3 |
| 返回值 | Return values | 单元 3 |
| 作用域 | Scope | 单元 3 |
| 字符串 | Strings | 单元 4 |
| 列表 | Lists | 单元 4 |
| 元组 | Tuples | 单元 4 |
| 字典 | Dictionaries | 单元 4 |
| 嵌套数据结构 | Nested data structures | 单元 4 |
| 文件读取 | File reading | 单元 5 |
| 文件写入 | File writing | 单元 5 |
| 异常处理 | try/except | 单元 5 |
| CSV解析 | CSV parsing | 单元 5 |
| 类定义 | Class definition | 单元 6 |
| 构造函数__init__ | Constructor __init__ | 单元 6 |
| 实例方法 | Instance methods | 单元 6 |
| str方法 | str method | 单元 6 |

---
*Introduction to Computer Programming (CSC108H1) — 公式与概念速查*