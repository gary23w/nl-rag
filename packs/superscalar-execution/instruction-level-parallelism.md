---
title: "Instruction-level parallelism"
source: https://en.wikipedia.org/wiki/Instruction-level_parallelism
domain: superscalar-execution
license: CC-BY-SA-4.0
tags: superscalar execution, out-of-order execution, instruction-level parallelism, tomasulo algorithm
fetched: 2026-07-02
---

# Instruction-level parallelism

**Instruction-level parallelism** (**ILP**) is the parallel or simultaneous execution of a sequence of instructions in a computer program. More specifically, ILP refers to the average number of instructions run per step of this parallel execution.

## Discussion

ILP must not be confused with concurrency. In ILP, there is a single specific thread of execution of a process. On the other hand, concurrency involves the assignment of multiple threads to a CPU's core in a strict alternation, or in true parallelism if there are enough CPU cores, ideally one core for each runnable thread.

There are two approaches to instruction-level parallelism: hardware and software.

ILP was implemented either as Hardware-level dynamic parallelism or software-level ILP static parallelism. With hardware-level parallelism, the processor decides which instructions to execute in parallel, at the time the code is already running, whereas software-level parallelism means the compiler plans, ahead of time, which instructions to execute in parallel. Modern x86 processors use multiple techniques to achieve hardware-level parallelism, while the Itanium architecture made significant software-level parallelism possible, but also relied on it for its code to be efficient.

Consider the following program:

```mw
e = a + b
f = c + d
m = e * f
```

Operation 3 depends on the results of operations 1 and 2, so it cannot be calculated until both of them are completed. However, operations 1 and 2 do not depend on any other operation, so they can be calculated simultaneously. If we assume that each operation can be completed in one unit of time, then these three instructions can be completed in a total of two units of time, giving an ILP of 3/2.

A goal of compiler and processor designers is to identify and take advantage of as much ILP as possible. Ordinary programs are typically written under a sequential execution model where instructions execute one after the other and in the order specified by the programmer. ILP allows the compiler and the processor to overlap the execution of multiple instructions or even to change the order in which instructions are executed.

How much ILP exists in programs is very application-specific. In certain fields, such as graphics and scientific computing, the amount can be very large. However, workloads such as cryptography may exhibit much less parallelism.

Micro-architectural techniques that are used to exploit ILP include:

- Instruction pipelining, where the execution of multiple instructions can be partially overlapped.
- Superscalar execution, VLIW, and the closely related explicitly parallel instruction computing concepts, in which multiple execution units are used to execute multiple instructions in parallel.
- Out-of-order execution where instructions execute in any order that does not violate data dependencies. Note that this technique is independent of both pipelining and superscalar execution. Current implementations of out-of-order execution dynamically (i.e., while the program is executing and without any help from the compiler) extract ILP from ordinary programs. An alternative is to extract this parallelism at compile time and somehow convey this information to the hardware. Due to the complexity of scaling the out-of-order execution technique, the industry has re-examined instruction sets which explicitly encode multiple independent operations per instruction.
- Register renaming, which refers to a technique used to avoid unnecessary serialization of program operations imposed by the reuse of registers by those operations, used to enable out-of-order execution.
- Speculative execution, which allows the execution of complete instructions or parts of instructions before being certain whether this execution should take place. A commonly used form of speculative execution is control flow speculation, where instructions past a control flow instruction (e.g., a branch) are executed before the target of the control flow instruction is determined. Several other forms of speculative execution have been proposed and are in use, including speculative execution driven by value prediction, memory dependence prediction, and cache latency prediction.
- Branch prediction, which is used to avoid stalling for control dependencies to be resolved. Branch prediction is used with speculative execution.

ILP is exploited by both the compiler and hardware, but the compiler also provides inherent and implicit ILP in programs to hardware by compile-time optimizations. Some optimization techniques for extracting available ILP in programs include instruction scheduling, register allocation/renaming, and memory-access optimization.

Dataflow architectures are another class of architectures where ILP is explicitly specified; for a recent example, see the TRIPS architecture.

In recent years, ILP techniques have been used to provide performance improvements in spite of the growing disparity between processor operating frequencies and memory access times (early ILP designs such as the IBM System/360 Model 91 used ILP techniques to overcome the limitations imposed by a relatively small register file). Presently, a cache miss penalty to main memory costs several hundreds of CPU cycles. While in principle it is possible to use ILP to tolerate even such memory latencies, the associated resource and power dissipation costs are disproportionate. Moreover, the complexity and often the latency of the underlying hardware structures results in reduced operating frequency, further reducing any benefits. Hence, the aforementioned techniques prove inadequate to keep the CPU from stalling for the off-chip data. Instead, the industry is heading towards exploiting higher levels of parallelism that can be exploited through techniques such as multiprocessing and multithreading.
