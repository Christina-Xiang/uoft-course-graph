# CSC263H1 — 推理与技巧指南

### 1. Dijkstra 正确性: 贪心选择保持不变量 — $d[v]$ 是源到 $v$ 的最短路径 (对所有已提取顶点)

### 2. DP 最优子结构: 问题的最优解包含其子问题的最优解

### 3. DP 重叠子问题: 递归求解反复遇到相同子问题, 缓存复用

### 4. 贪心选择性质: 局部最优选择最终得到全局最优解

### 5. Kruskal 正确性: 安全边引理 — 最小权重边连接两个不同连通分量是安全的

### 6. Prim 正确性: 割性质 — 连接已选集合与未选集合的最小边安全

### 7. Ford-Fulkerson 正确性: 残留网络中无增广路径 $\iff$ 当前流是最大流

### 8. Max-Flow Min-Cut 定理: 最大流值等于最小割容量

### 9. Edmonds-Karp 单调性: 每次增广后顶点距离单调递增

### 10. 0-1 背包最优子结构: $dp[i][w]$ 包含或不包含第 $i$ 个物品的最优值

### 11. LCS 最优子结构: $X_i=Y_j$ 则 LCS 包含它; 否则至少一个不在 LCS 中

### 12. 并查集势能分析: 路径压缩使后续操作更便宜, 均摊 $\alpha(n)$

### 13. 归约传递性: $A\le_p B \land B\le_p C \implies A\le_p C$

### 14. Cook-Levin 定理: SAT 是 NP-Complete

### 15. 3-SAT $\le_p$ CLIQUE 正确性: 原公式可满足 $\iff$ 图有 $k$-clique

### 16. 3-SAT $\le_p$ SUBSET-SUM 正确性: 数字构造编码变量赋值

## 核心方法

- **Heap implementation** (堆实现) — 单元 1
- **AVL insertion/deletion** (AVL插入/删除) — 单元 2
- **Hash table implementation** (哈希表实现) — 单元 3
- **Kruskal's MST** (Kruskal最小生成树) — 单元 4
- **Graph representation** (图表示) — 单元 5
- **Potential function design** (势能函数设计) — 单元 6

## 编程技巧

- **Amortized analysis** (摊还分析) — 单元 1
- **Tree rotation patterns** (树旋转模式) — 单元 2
- **Double hashing** (双重哈希) — 单元 3
- **Graph search patterns** (图搜索模式) — 单元 5

---
*Data Structures and Analysis (CSC263H1) — 推理与技巧指南*