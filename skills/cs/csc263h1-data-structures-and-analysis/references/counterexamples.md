# CSC263H1 — 常见错误与反例

| # | 常见错误 | 说明 |
|---|---------|------|
| 1 | **Dijkstra 负边** | 负权边导致已确定的 $d[v]$ 可能被后续更新推翻, 需 Bellman-Ford |
| 2 | **贪心非最优** | 0-1 背包问题贪心按价值/重量比选择不一定最优 |
| 3 | **0-1 背包 vs 分数背包** | 分数背包可贪心 (物品可分), 0-1 不行 |
| 4 | **Floyd-Warshall 负环** | 顶点到自身距离 $<0$ 说明存在负环 |
| 5 | **Kruskal 大图** | $E$ 远大于 $V$ 时排序边成本高, Prim 可能更好 |
| 6 | **最大流非唯一** | 同一网络可能有多个不同最大流 |
| 7 | **Ford-Fulkerson 整数流** | 若容量非整数或无理数, 可能不终止 |
| 8 | **贪心最小顶点覆盖** | 选最大度顶点不是 2-近似? 实际是 $\ln n$ 近似 |
| 9 | **哈密顿路径 vs 欧拉路径** | 前者 NP-Complete, 后者多项式 |
| 10 | **P=NP 猜想** | 如果成立则所有 NPC 问题有多项式算法 |
| 11 | **0-1 背包的 $O(nW)$ 不是多项式算法** | $W$ 是输入值的指数 |
| 12 | **归约方向错误** | 要证明 $L$ 是 NPC, 需 $L'\le_p L$ ($L'$ 是已知的 NPC) |
| 13 | **Bellman-Ford 检测负环** | 第 $|V|$ 轮仍有更新则存在负环 |
| 14 | **并查集不按秩合并** | 最坏 $O(n)$ 每次, 退化成链表 |

## 课程常见陷阱

| # | 陷阱 | 所在单元 |
|---|------|---------|
| 1 | **Confusing heap with BST** (堆与BST混淆) | 单元 1 |
| 2 | **Forgetting to rebalance** (忘记重新平衡) | 单元 2 |
| 3 | **Poor hash function selection** (差哈希函数选择) | 单元 3 |
| 4 | **Not implementing path compression** (未实现路径压缩) | 单元 4 |
| 5 | **Negative edges with Dijkstra** (Dijkstra负边) | 单元 5 |
| 6 | **Confusing amortized with average case** (摊还与平均情况混淆) | 单元 6 |

---
*Data Structures and Analysis (CSC263H1) — 常见错误与反例*