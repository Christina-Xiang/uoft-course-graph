# CSC209H1 — 推理与技巧指南

### 1. 互斥: Peterson 算法满足互斥、前进、有限等待

### 2. 饥饿: 优先级调度中低优先级进程可能永远得不到 CPU

### 3. 死锁必要条件: 四个 Coffman 条件同时满足是死锁的必要条件

### 4. 银行家算法正确性: 安全状态保证所有进程最终完成

### 5. LRU 是最优的在线页面置换算法 (Belady 异常不适用于 LRU)

### 6. FIFO 可能产生 Belady 异常: 增加物理页框数反而增加缺页

### 7. Cache 命中率: 容量 $\uparrow$ 命中率 $\uparrow$ 但边际效益递减

### 8. RAID 可靠性: RAID 1 两盘故障概率 $p^2$, RAID 5 三盘 $p^3$

### 9. 信号量机制: 同步原语可解决任意数量的并发同步问题

### 10. 管程: 条件变量 + 锁实现高级同步抽象

### 11. Bounded Buffer: 信号量正确实现生产者-消费者

### 12. Readers-Writers: 读者优先 vs 写者优先的公平性权衡

## 核心方法

- **Compiling with gcc** (gcc编译) — 单元 1
- **Valgrind usage** (Valgrind使用) — 单元 2
- **System call error handling** (系统调用错误处理) — 单元 3
- **Bash scripting** (Bash脚本) — 单元 4
- **pipe() system call(pipe()系统调用)** () — 单元 5
- **Modular compilation** (模块编译) — 单元 6

## 编程技巧

- **Debugging with GDB** (GDB调试) — 单元 1
- **Safe memory patterns** (安全内存模式) — 单元 2
- **Pipeline construction** (管道构建) — 单元 4
- **Signal handling patterns** (信号处理模式) — 单元 5

---
*Software Tools and Systems Programming (CSC209H1) — 推理与技巧指南*