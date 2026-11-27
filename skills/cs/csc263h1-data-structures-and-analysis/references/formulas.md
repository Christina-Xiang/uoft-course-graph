# CSC263H1 — 关键公式与概念速查

## 核心公式/复杂度

| 概念 | 公式/描述 | 说明 |
|------|----------|------|
| Master 定理 | $T(n) = aT(n/b) + f(n)$ | 分治递推 |
| 情形 1 | $f(n) = O(n^{\log_b a - \epsilon}) \implies T(n) = \Theta(n^{\log_b a})$ | 叶主导 |
| 情形 2 | $f(n) = \Theta(n^{\log_b a} \log^k n) \implies T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$ | 叶-根均衡 |
| 情形 3 | $f(n) = \Omega(n^{\log_b a + \epsilon})$ 且 $af(n/b) \le cf(n) \implies T(n) = \Theta(f(n))$ | 根主导 |
| Dijkstra | $d[v] = \min(d[v], d[u] + w(u,v))$ 使用优先队列 $O((V+E)\log V)$ | 单源最短路径 |
| Bellman-Ford | $d[v] = \min(d[v], d[u] + w(u,v))$ 重复 $|V|-1$ 次, $O(VE)$ | 支持负边 |
| Floyd-Warshall | $d_{ij}^{(k)} = \min(d_{ij}^{(k-1)}, d_{ik}^{(k-1)} + d_{kj}^{(k-1)})$, $O(V^3)$ | 全源最短路径 |
| Kruskal | 排序 $E$ 边权重 $\to$ 并查集选最小不形成环, $O(E\log V)$ | 最小生成树 |
| Prim | 从起点开始每次选最小权重边连接未访问顶点, $O(E\log V)$ | 最小生成树 |
| 0-1 背包 DP | $dp[i][w] = \max(dp[i-1][w], dp[i-1][w-w_i] + v_i)$, $O(nW)$ | 伪多项式 |
| LCS DP | $dp[i][j] = dp[i-1][j-1]+1$ if equal else $\max(dp[i-1][j], dp[i][j-1])$, $O(mn)$ | 最长公共子序列 |
| Edit Distance DP | $dp[i][j] = \min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + \text{cost})$, $O(mn)$ | 编辑距离 |
| 链式矩阵乘法 DP | $dp[i][j] = \min_{i\le k<j} (dp[i][k] + dp[k+1][j] + p_{i-1}p_kp_j)$, $O(n^3)$ | 最优括号化 |
| Rod Cutting DP | $r_n = \max_{1\le i\le n} (p_i + r_{n-i})$, $O(n^2)$ | 切割收益最大化 |
| 最大流 (Ford-Fulkerson) | 每条增广路径增加流量直到没有 $s\to t$ 路径, $O(E\cdot f)$ | 增广路径 |
| Edmonds-Karp | BFS 找最短增广路径, $O(VE^2)$ | FF 的 BFS 变种 |
| 最小割 (Max-Flow Min-Cut) | 最大流值 = 最小割容量 | 对偶定理 |
| Bipartite Matching | 构建源 $\to$ 左 $\to$ 右 $\to$ 汇网络求最大流 | 匈牙利算法 |
| Amortized 分析 (Union-Find) | 按秩合并 + 路径压缩: 均摊 $\alpha(n)$ | 几乎常数 |
| Amortized 分析 (Stack) | Push $O(1)$, Multipop $O(k)$ 均摊 $O(1)$ | 聚合分析 |
| Amortized 分析 (Binary Counter) | Increment 翻转 $k$ 位, 均摊 $O(1)$ | 势能法 |
| NP-Complete 证明 | 归约: $L'\le_p L$ 且 $L'$ 是 NPC | 多项式多对一归约 |
| SAT $\to$ 3-SAT | 子句 $(a_1\lor a_2\lor\cdots\lor a_k)$ 拆成 $k-2$ 个 3-CNF 子句 | 引入新变量 |
| 3-SAT $\to$ CLIQUE | 构造 $k$ 个三元素组, 边连接不同组中相容文字 | 图构造 |
| 3-SAT $\to$ VERTEX-COVER | 构造 $(\bar{x})$ 三角形 + 子句-变量边 | NP-C 证明链 |

## 课程核心概念

| 概念 | 英文 | 所在单元 |
|------|------|---------|
| 二叉堆 | Binary heap | 单元 1 |
| 堆操作 | Heap operations | 单元 1 |
| 建堆 | Heapify | 单元 1 |
| 二项堆 | Binomial heap | 单元 1 |
| 斐波那契堆 | Fibonacci heap | 单元 1 |
| AVL树 | AVL tree | 单元 2 |
| 旋转操作 | Rotation operations | 单元 2 |
| 红黑树 | Red-black tree | 单元 2 |
| B树 | B-tree | 单元 2 |
| 哈希函数设计 | Hash function design | 单元 3 |
| 冲突解决 | Collision resolution | 单元 3 |
| 链地址法 | Chaining | 单元 3 |
| 开放地址法 | Open addressing | 单元 3 |
| 负载因子 | Load factor | 单元 3 |
| 并查集ADT | Union-Find ADT | 单元 4 |
| 路径压缩 | Path compression | 单元 4 |
| 按秩合并 | Union by rank | 单元 4 |
| 广度优先搜索 | BFS | 单元 5 |
| 深度优先搜索 | DFS | 单元 5 |
| 拓扑排序 | Topological sort | 单元 5 |
| Dijkstra算法 | Dijkstra's algorithm | 单元 5 |
|  | MST (Prim | 单元 5 |
| 最小生成树 | Kruskal) | 单元 5 |
| 聚合法 | Aggregate method | 单元 6 |
| 记账法 | Accounting method | 单元 6 |
| 势能法 | Potential method | 单元 6 |
| amortized | Dynamic array | 单元 6 |

---
*Data Structures and Analysis (CSC263H1) — 公式与概念速查*