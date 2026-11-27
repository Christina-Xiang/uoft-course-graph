# CSC148H1 — 关键公式与概念速查

## 核心公式/复杂度

| 概念 | 公式/描述 | 说明 |
|------|----------|------|
| 递归复杂度 | $T(n) = T(n-1) + O(1) \implies O(n)$ | 线性递归 |
| 树递归 | $T(n) = 2T(n-1) + O(1) \implies O(2^n)$ | 指数爆炸 |
| 分治 | $T(n) = 2T(n/2) + O(n) \implies O(n \log n)$ | 归并/快排 |
| 二分递归 | $T(n) = T(n/2) + O(1) \implies O(\log n)$ | 二分搜索 |
| 链表查找 | $O(n)$ | 线性遍历 |
| 哈希表(平均) | 均摊 $O(1)$ | 查找/插入/删除 |
| 哈希表(最坏) | $O(n)$ | 大量碰撞 |
| BST 查找 | $O(h)$ 平均 $O(\log n)$ 最坏 $O(n)$ | 取决于平衡 |
| 堆 | $O(\log n)$ 插入/删除最小 | 完全二叉树 |
| 快速排序(平均) | $O(n \log n)$, 最坏 $O(n^2)$ | 分区基准选择 |
| 归并排序 | $O(n \log n)$ 稳定 | 分治合并 |
| ADT 操作 | 创建、插入、删除、查找、遍历 | 抽象数据类型 |
| 继承 | 子类 IS-A 父类 | 代码复用 + 多态 |
| 多态 | 同一接口不同实现 | 动态绑定 |
| 重写 | 子类覆盖父类方法 | 运行时多态 |
| UML 关系 | 关联、聚合、组合、继承、依赖 | 类图建模 |
| Big-O 定义 | $\exists c,n_0: \forall n\ge n_0, f(n)\le c\cdot g(n)$ | 上界 |
| Big-Omega 定义 | $\exists c,n_0: \forall n\ge n_0, f(n)\ge c\cdot g(n)$ | 下界 |
| Big-Theta 定义 | $f=O(g) \land f=\Omega(g)$ | 紧界 |

## 课程核心概念

| 概念 | 英文 | 所在单元 |
|------|------|---------|
| 继承 | Inheritance | 单元 1 |
| 多态 | Polymorphism | 单元 1 |
| 抽象类 | Abstract classes | 单元 1 |
| 双下方法 | Dunder methods | 单元 1 |
| 组合vs继承 | Composition vs inheritance | 单元 1 |
| 递归定义 | Recursive definition | 单元 2 |
| 基本情况 | Base case | 单元 2 |
| 递归情况 | Recursive case | 单元 2 |
| 堆栈追踪 | Stack trace | 单元 2 |
| 栈 | Stack | 单元 3 |
| 队列 | Queue | 单元 3 |
| 树 | Tree | 单元 3 |
| 二叉树 | Binary tree | 单元 3 |
| 二叉搜索树 | BST | 单元 3 |
| 链表 | Linked list | 单元 3 |
| 大O表示 | Big-O notation | 单元 4 |
| 时间复杂度 | Time complexity | 单元 4 |
| 空间复杂度 | Space complexity | 单元 4 |
| 最好/平均/最坏情况 | Best/average/worst case | 单元 4 |
| 单元测试 | Unit testing | 单元 5 |
| 测试用例 | Test cases | 单元 5 |
| 断言 | Assertions | 单元 5 |
| doctest | doctest | 单元 5 |
| 异常处理回顾 | Exception handling review | 单元 6 |
| 文件I/O回顾 | File I/O review | 单元 6 |
| CSV数据处理 | CSV data processing | 单元 6 |

---
*Introduction to Computer Science (CSC148H1) — 公式与概念速查*