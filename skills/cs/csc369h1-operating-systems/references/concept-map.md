# CSC369H1 — 概念依赖图谱

## 单元 1

- **OS Overview & Processes** (操作系统概述与进程) → 依赖: OS abstractions, Process states, PCB, Context switch
- **OS abstractions** (OS抽象) → 依赖: Process states
- **Process states** (进程状态) → 依赖: PCB
- **PCB** (进程控制块) → 依赖: Context switch
- **Context switch** (上下文切换)
- **Process API (fork** ()
- **exec** ()
- **wait)** (进程API)
- **System call tracing** (系统调用追踪)
- **Fork bombing** (Fork炸弹)
- **OS conceptual understanding** (OS概念理解)
- **Process lifecycle simulation** (进程生命周期模拟)

## 单元 2

- **Threads & Concurrency** (线程与并发) → 依赖: Thread vs process, Race conditions, Mutex locks, Semaphores
- **Thread vs process** (线程vs进程) → 依赖: Race conditions
- **Race conditions** (竞态条件) → 依赖: Mutex locks
- **Mutex locks** (互斥锁) → 依赖: Semaphores
- **Semaphores** (信号量) → 依赖: Deadlock
- **Deadlock** (死锁) → 依赖: Condition variables
- **Condition variables** (条件变量)
- **Deadlock necessary conditions** (死锁必要条件)
- **Pthreads programming** (Pthreads编程)
- **Lock-free programming** (无锁编程)
- **Deadlock due to lock ordering** (锁顺序死锁)
- **Concurrent programming** (并发编程)
- **Mutex/condition variable lab** (互斥锁/条件变量实验)

## 单元 3

- **CPU Scheduling** (CPU调度) → 依赖: Scheduling criteria, FCFS, SJF, Round Robin
- **Scheduling criteria** (调度准则) → 依赖: FCFS
- **FCFS** (先来先服务) → 依赖: SJF
- **SJF** (短作业优先) → 依赖: Round Robin
- **Round Robin** (时间片轮转) → 依赖: RR
- **RR** (RR) → 依赖: MLFQ
- **MLFQ** (多级反馈队列)
- **Scheduling algorithm comparison** (调度算法比较)
- **Convoy effect** (护航效应)
- **Scheduling analysis** (调度分析)
- **Scheduling simulation** (调度模拟)

## 单元 4

- **Memory Management** (内存管理) → 依赖: Virtual memory, Paging, TLB, Page replacement
- **Virtual memory** (虚拟内存) → 依赖: Paging
- **Paging** (分页) → 依赖: TLB
- **TLB** (TLB) → 依赖: Page replacement
- **Page replacement** (页面置换) → 依赖: Segmentation
- **Segmentation** (分段)
- **Working set model** (工作集模型)
- **Page table implementation** (页表实现)
- **LRU approximation** (LRU近似)
- **Thrashing** (系统抖动)
- **Memory system understanding** (内存系统理解)
- **Page replacement simulation** (页面置换模拟)

## 单元 5

- **File Systems** (文件系统) → 依赖: File system architecture, Inode, Directory structure, Journaling
- **File system architecture** (文件系统架构) → 依赖: Inode
- **Inode** (Inode) → 依赖: Directory structure
- **Directory structure** (目录结构) → 依赖: Journaling
- **Journaling** (日志) → 依赖: Disk scheduling
- **Disk scheduling** (磁盘调度)
- **fsck and recovery** (fsck与恢复)
- **Inode exhaustion** (Inode耗尽)
- **File system internals** (文件系统内部)
- **Filesystem implementation lab** (文件系统实现实验)

## 单元 6

- **I/O Systems** (I/O系统) → 依赖: Memory-mapped I/O, DMA, Interrupts, Device drivers
- **Memory-mapped I/O** (内存映射I/O) → 依赖: DMA
- **DMA** (直接内存访问) → 依赖: Interrupts
- **Interrupts** (中断) → 依赖: Device drivers
- **Device drivers** (设备驱动)
- **I/O performance analysis** (I/O性能分析)
- **mmap usage** (mmap使用)
- **Busy waiting** (忙等待)
- **I/O subsystem understanding** (I/O子系统理解)
- **I/O benchmarking** (I/O基准测试)


---
*Operating Systems (CSC369H1) — 概念依赖图谱*