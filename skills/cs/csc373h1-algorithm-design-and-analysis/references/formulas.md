# CSC373H1 — 关键公式与概念速查

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
| 主定理 | Master theorem | 单元 1 |
| 递推关系 | Recurrence relations | 单元 1 |
| 归并排序 | Merge sort | 单元 1 |
| 快速排序 | Quick sort | 单元 1 |
| median | Selection | 单元 1 |
| 最近点对 | Closest pair | 单元 1 |
| 最优子结构 | Optimal substructure | 单元 2 |
| 重叠子问题 | Overlapping subproblems | 单元 2 |
| 记忆化 | Memoization | 单元 2 |
| 表格法 | Tabulation | 单元 2 |
| 背包问题 | Knapsack | 单元 2 |
| 编辑距离 | Edit distance | 单元 2 |
| 矩阵链乘 | Chain matrix multiplication | 单元 2 |
| 贪心选择性质 | Greedy choice property | 单元 3 |
| 交换论证 | Exchange argument | 单元 3 |
| 分数背包 | Fractional knapsack | 单元 3 |
| 哈夫曼编码 | Huffman coding | 单元 3 |
| 最小生成树 | Minimum spanning tree | 单元 3 |
| 区间调度 | Interval scheduling | 单元 3 |
| 流网络 | Flow network | 单元 4 |
| Ford-Fulkerson算法 | Ford-Fulkerson algorithm | 单元 4 |
| 最大流=最小割 | Max flow = min cut | 单元 4 |
| Edmonds-Karp | Edmonds-Karp | 单元 4 |
| 二分匹配 | Bipartite matching | 单元 4 |
| P vs NP | P vs NP | 单元 5 |
| NP完全性定义 | NP-completeness definition | 单元 5 |
| SAT问题 | SAT | 单元 5 |
| 3-SAT | 3-SAT | 单元 5 |
| 顶点覆盖 | Vertex cover | 单元 5 |
| 哈密顿路径 | Hamiltonian path | 单元 5 |
| 近似比 | Approximation ratio | 单元 6 |
| PTAS | PTAS | 单元 6 |
| 顶点覆盖近似 | Vertex cover approximation | 单元 6 |
| 随机化QuickSelect | Randomized QuickSelect | 单元 6 |
| 哈希回顾 | Hashing review | 单元 6 |

---
*Algorithm Design and Analysis (CSC373H1) — 公式与概念速查*