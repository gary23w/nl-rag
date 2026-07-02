---
title: "Fork–join model"
source: https://en.wikipedia.org/wiki/Fork%E2%80%93join_model
domain: openmp-parallelism
license: CC-BY-SA-4.0
tags: openmp parallelism, shared memory parallelism, loop-level parallelism, fork-join model
fetched: 2026-07-02
---

# Fork–join model

In parallel computing, the **fork–join model** is a way of setting up and executing parallel programs, such that execution branches off in parallel at designated points in the program, to "join" (merge) at a subsequent point and resume sequential execution. Parallel sections may fork recursively until a certain task granularity is reached. Fork–join can be considered a parallel design pattern. It was formulated as early as 1963.

By nesting fork–join computations recursively, one obtains a parallel version of the divide and conquer paradigm, expressed by the following generic pseudocode:

```
solve(problem):
    if problem is small enough:
        solve problem directly (sequential algorithm)
    else:
        for part in subdivide(problem)
            fork subtask to solve(part)
        join all subtasks spawned in previous loop
        return combined results
```

## Examples

The simple parallel merge sort of CLRS is a fork–join algorithm.

```
mergesort(A, lo, hi):
    if lo < hi:                     // at least one element of input
        mid = ⌊lo + (hi - lo) / 2⌋
        fork mergesort(A, lo, mid)  // process (potentially) in parallel with main task
        mergesort(A, mid, hi)       // main task handles second recursion
        join
        merge(A, lo, mid, hi)
```

The first recursive call is "forked off", meaning that its execution may run in parallel (in a separate thread) with the following part of the function, up to the join that causes all threads to synchronize. While the join may look like a barrier, it is different because the threads will continue to work after a barrier, while after a join only one thread continues.

The second recursive call is not a fork in the pseudocode above; this is intentional, as forking tasks may come at an expense. If both recursive calls were set up as subtasks, the main task would not have any additional work to perform before being blocked at the join.

## Implementations

Implementations of the fork–join model will typically fork *tasks*, *fibers* or *lightweight threads*, not operating-system-level "heavyweight" threads or processes, and use a thread pool to execute these tasks: the fork primitive allows the programmer to specify *potential* parallelism, which the implementation then maps onto actual parallel execution. The reason for this design is that creating new threads tends to result in too much overhead.

The lightweight threads used in fork–join programming will typically have their own scheduler (typically a work stealing one) that maps them onto the underlying thread pool. This scheduler can be much simpler than a fully featured, preemptive operating system scheduler: general-purpose thread schedulers must deal with blocking for locks, but in the fork–join paradigm, threads only block at the join point.

Fork–join is the main model of parallel execution in the OpenMP framework, although OpenMP implementations may or may not support nesting of parallel sections. It is also supported by the Java concurrency framework, the Task Parallel Library for .NET, and Intel's Threading Building Blocks (TBB). The Cilk programming language has language-level support for fork and join, in the form of the `spawn` and `sync` keywords, or `cilk_spawn` and `cilk_sync` in Cilk Plus.
