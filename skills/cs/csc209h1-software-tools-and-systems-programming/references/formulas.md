# CSC209H1 — 关键公式与概念速查

## 核心公式/复杂度

| 概念 | 公式/描述 | 说明 |
|------|----------|------|
| Linux 目录 | $/\to /bin, /etc, /home, /usr, /var, /tmp$ | 文件系统层次 |
| 文件权限 | $\text{rwx rwx rwx}$ (属主/组/其他) | 9 位权限位 |
| 管道 | $\text{cmd1} \mid \text{cmd2}$ | 进程间通信 (IPC) |
| 重定向 | $>$, $>>$, $<$, $2>$, $\&>$ | I/O 重定向 |
| 进程状态 | 运行/就绪/阻塞/终止/僵尸 | 状态机模型 |
| fork() | 调用一次, 返回两次: 子进程 PID 给父, 0 给子 | 进程创建 |
| exec() | 替换当前进程内存映像 | 程序加载 |
| pthread_create | $\text{pthread\_create}(\&tid, \text{attr}, \text{start\_routine}, \text{arg})$ | 线程创建 |
| 互斥锁 | $\text{pthread\_mutex\_lock}(\&mtx)$ / $\text{pthread\_mutex\_unlock}(\&mtx)$ | 线程同步 |
| 信号量 | $\text{sem\_wait}(\&sem)$ / $\text{sem\_post}(\&sem)$ | P/V 操作 |
| 条件变量 | $\text{pthread\_cond\_wait}$ / $\text{pthread\_cond\_signal}$ | 等待/通知 |
| 调度算法 | FCFS, SJF, Priority, Round-Robin, MLFQ | CPU 调度 |
| 页面置换 | FIFO, LRU, OPT, Clock (二次机会) | 虚拟内存 |
| 页表 | 虚拟地址 $\to$ 物理地址翻译 | 内存管理单元 (MMU) |
| TLB | 快表缓存页表项, 加速地址翻译 | 命中率 |
| 段页式 | 段号 $\to$ 页表 $\to$ 物理页框 | 分段 + 分页 |
| 磁盘调度 | FCFS, SSTF, SCAN, C-SCAN, LOOK | 磁盘 I/O 优化 |
| 文件分配 | 连续/链接/索引/inode | 存储分配策略 |
| RAID | 0 (条带), 1 (镜像), 5 (奇偶校验), 6 (双重校验) | 冗余磁盘阵列 |
| Cache 层次 | L1 (几十 KB, ~1ns) $\to$ L2 (几百 KB, ~5ns) $\to$ L3 (几 MB, ~15ns) $\to$ 主存 (~100ns) | 存储层次 |
| 时间局部性 | 最近访问的数据可能很快再次访问 | Cache 命中 |
| 空间局部性 | 访问地址附近的数据可能很快被访问 | 预取 |
| 死锁条件 | 互斥 + 持有并等待 + 非剥夺 + 循环等待 | Coffman 条件 |
| 银行家算法 | 安全状态: 存在安全序列 $P_{i_1},\ldots,P_{i_n}$ | 死锁避免 |
| Linux 信号 | $\text{SIGINT}(2), \text{SIGKILL}(9), \text{SIGSEGV}(11), \text{SIGPIPE}(13)$ | 软中断 |

## 课程核心概念

| 概念 | 英文 | 所在单元 |
|------|------|---------|
| C语法 | C syntax | 单元 1 |
| 指针 | Pointers | 单元 1 |
| 内存地址 | Memory addresses | 单元 1 |
| 数组与字符串 | Arrays & strings | 单元 1 |
| 堆vs栈 | Heap vs stack | 单元 2 |
| malloc/free | malloc/free | 单元 2 |
| 内存泄漏 | Memory leaks | 单元 2 |
| 悬空指针 | Dangling pointers | 单元 2 |
| 文件描述符 | File descriptors | 单元 3 |
| open/read/write/close | open/read/write/close | 单元 3 |
| 缓冲vs非缓冲 | Buffered vs unbuffered | 单元 3 |
| fork | Process creation | 单元 4 |
| 进程ID | Process IDs | 单元 4 |
| exec系列 | Exec family | 单元 4 |
| Shell脚本 | Shell scripting | 单元 4 |
| 管道 | Pipes | 单元 5 |
| 信号 | Signals | 单元 5 |
| 信号处理 | Signal handlers | 单元 5 |
| 套接字导论 | Sockets intro | 单元 5 |
| Makefile语法 | Makefile syntax | 单元 6 |
| 编译目标 | Compilation targets | 单元 6 |
| 库链接 | Library linking | 单元 6 |

---
*Software Tools and Systems Programming (CSC209H1) — 公式与概念速查*