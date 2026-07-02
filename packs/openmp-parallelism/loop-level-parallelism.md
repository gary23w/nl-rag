---
title: "Loop-level parallelism"
source: https://en.wikipedia.org/wiki/Loop-level_parallelism
domain: openmp-parallelism
license: CC-BY-SA-4.0
tags: openmp parallelism, shared memory parallelism, loop-level parallelism, fork-join model
fetched: 2026-07-02
---

# Loop-level parallelism

**Loop-level parallelism** is a form of parallelism in software programming that is concerned with extracting parallel tasks from loops. The opportunity for loop-level parallelism often arises in computing programs where data is stored in random access data structures. Where a sequential program will iterate over the data structure and operate on indices one at a time, a program exploiting loop-level parallelism will use multiple threads or processes which operate on some or all of the indices at the same time. Such parallelism provides a speedup to overall execution time of the program, typically in line with Amdahl's law.

## Description

For simple loops, where each iteration is independent of the others, loop-level parallelism can be embarrassingly parallel, as parallelizing only requires assigning a process to handle each iteration. However, many algorithms are designed to run sequentially, and fail when parallel processes race due to dependence within the code. Sequential algorithms are sometimes applicable to parallel contexts with slight modification. Usually, though, they require process synchronization. Synchronization can be either implicit, via message passing, or explicit, via synchronization primitives like semaphores.

## Example

Consider the following code operating on a list `l`, where `l.size() == n`.

```mw
for (int i = 0; i < n; ++i) {
    l[i] += 10; // s1
}
```

Each iteration of the loop takes the value from the current index of `l`, and increments it by 10. If statement `s1` takes `T` time to execute, then the loop takes time `n * T` to execute sequentially, ignoring time taken by loop constructs. Now, consider a system with `p` processors where `p > n`. If `n` threads run in parallel, the time to execute all `n` steps is reduced to `T`.

Less simple cases produce inconsistent, i.e. non-serializable outcomes. Consider the following loop operating on the same list `l`.

```mw
for (int i = 0; i < n; ++i) {
    l[i] = l[i - 1] + 10; // s1
}
```

Each iteration sets the current index to be the value of the previous plus ten. When run sequentially, each iteration is guaranteed that the previous iteration will already have the correct value. With multiple threads, process scheduling and other considerations prevent the execution order from guaranteeing an iteration will execute only after its dependence is met. It very well may happen before, leading to unexpected results. Serializability can be restored by adding synchronization to preserve the dependence on previous iterations.

## Dependencies in code

There are several types of dependences that can be found within code.

| Type | Notation | Description |
|---|---|---|
| True (Flow) Dependence | `s1 ->T s2` | A true dependence between s1 and s2 means that s1 writes to a location later read from by s2 |
| Anti Dependence | `s1 ->A s2` | An anti-dependence between s1 and s2 means that s1 reads from a location later written to by s2. |
| Output Dependence | `s1 ->O s2` | An output dependence between s1 and s2 means that s1 and s2 write to the same location. |
| Input Dependence | `s1 ->I s2` | An input dependence between s1 and s2 means that s1 and s2 read from the same location. |

In order to preserve the sequential behaviour of a loop when run in parallel, True Dependence must be preserved. Anti-Dependence and Output Dependence can be dealt with by giving each process its own copy of variables (known as privatization).

### Example of true dependence

```mw
int a, b; // s1
a = 2; // s2
b = a + 40; // s3
```

`s2 ->T s3`, meaning that s2 has a true dependence on s3 because s2 writes to the variable `a`, which s3 reads from.

### Example of anti-dependence

```mw
int a, b = 40; // s1
a = b - 38; // s2
b = -1; // s3
```

`s2 ->A s3`, meaning that s2 has an anti-dependence on s3 because s2 reads from the variable `b` before s3 writes to it.

### Example of output-dependence

```mw
int a, b = 40; // s1
a = b - 38; // s2
a = 2; // s3
```

`s2 ->O s3`, meaning that s2 has an output dependence on s3 because both write to the variable `a`.

### Example of input-dependence

```mw
int a, b, c = 2; // s1
a = c - 1; // s2
b = c + 1; // s3
```

`s2 ->I s3`, meaning that s2 has an input dependence on s3 because s2 and s3 both read from variable `c`.

## Dependence in loops

### Loop-carried vs loop-independent dependence

Loops can have two types of dependence:

- Loop-carried dependence
- Loop-independent dependence

In loop-independent dependence, loops have inter-iteration dependence, but do not have dependence between iterations. Each iteration may be treated as a block and performed in parallel without other synchronization efforts.

In the following example code used for swapping the values of two array of length n, there is a loop-independent dependence of `s1 ->T s3`.

```mw
for (int i = 1; i < n; ++i) {
    tmp = a[i]; // s1
    a[i] = b[i]; // s2
    b[i] = tmp; // s3
}
```

In loop-carried dependence, statements in an iteration of a loop depend on statements in another iteration of the loop. Loop-Carried Dependence uses a modified version of the dependence notation seen earlier.

Example of loop-carried dependence where `s1[i] ->T s1[i + 1]`, where `i` indicates the current iteration, and `i + 1` indicates the next iteration.

```mw
for (int i = 1; i < n; ++i) {
    a[i] = a[i - 1] + 1; // s1
}
```

### Loop carried dependence graph

A Loop-carried dependence graph graphically shows the loop-carried dependencies between iterations. Each iteration is listed as a node on the graph, and directed edges show the true, anti, and output dependencies between each iteration.

## Types

There are a variety of methodologies for parallelizing loops.

- DISTRIBUTED Loop
- DOALL Parallelism
- DOACROSS Parallelism
- HELIX
- DOPIPE Parallelism

Each implementation varies slightly in how threads synchronize, if at all. In addition, parallel tasks must somehow be mapped to a process. These tasks can either be allocated statically or dynamically. Research has shown that load-balancing can be better achieved through some dynamic allocation algorithms than when done statically.

The process of parallelizing a sequential program can be broken down into the following discrete steps. Each concrete loop-parallelization below implicitly performs them.

| Type | Description |
|---|---|
| Decomposition | The program is broken down into tasks, the smallest exploitable unit of concurrence. |
| Assignment | Tasks are assigned to processes. |
| Orchestration | Data access, communication, and synchronization of processes. |
| Mapping | Processes are bound to processors. |

### DISTRIBUTED loop

When a loop has a loop-carried dependence, one way to parallelize it is to distribute the loop into several different loops. Statements that are not dependent on each other are separated so that these distributed loops can be executed in parallel. For example, consider the following code.

```mw
for (int i = 1; i < n; ++i) {
    a[i] = a[i - 1] + b[i]; // s1
    c[i] += d[i]; // s2
}
```

The loop has a loop carried dependence `s1[i] ->T s1[i + 1]` but s2 and s1 do not have a loop-independent dependence so we can rewrite the code as follows.

```mw
// loop1
for (int i = 1; i < n; ++i) {
    a[i] = a[i - 1] + b[i]; // s1
}

// loop2
for (int i = 1; i < n; ++i) {
    c[i] += d[i]; // s2
}
```

Note that now loop1 and loop2 can be executed in parallel. Instead of single instruction being performed in parallel on different data as in data level parallelism, here different loops perform different tasks on different data. Let's say the time of execution of s1 and s2 be $T_{s_{1}}$ and $T_{s_{2}}$ then the execution time for sequential form of above code is $n\cdot (T_{s_{1}}+T_{s_{2}})$ , Now because we split the two statements and put them in two different loops, gives us an execution time of $n\cdot T_{s_{1}}+T_{s_{2}}$ . We call this type of parallelism either function or task parallelism.

### DOALL parallelism

DOALL parallelism exists when statements within a loop can be executed independently (situations where there is no loop-carried dependence). For example, the following code does not read from the array `a`, and does not update the arrays `b, c`. No iterations have a dependence on any other iteration.

```mw
for (int i = 0; i < n; ++i) {
    a[i] = b[i] + c[i]; // s1
}
```

Let's say the time of one execution of s1 be $T_{s_{1}}$ then the execution time for sequential form of above code is $n\cdot T_{s_{1}}$ , Now because DOALL Parallelism exists when all iterations are independent, speed-up may be achieved by executing all iterations in parallel which gives us an execution time of $T_{s_{1}}$ , which is the time taken for one iteration in sequential execution.

The following example, using a simplified pseudo code, shows how a loop might be parallelized to execute each iteration independently.

```mw
beginParallelism();

for (int i = 0; i < n; ++i) {
    a[i] = b[i] + c[i]; // s1
    endParallelism();
}

block();
```

### DOACROSS parallelism

DOACROSS Parallelism exists where iterations of a loop are parallelized by extracting calculations that can be performed independently and running them simultaneously.

Synchronization exists to enforce loop-carried dependence.

Consider the following, synchronous loop with dependence `s1[i] ->T s1[i + 1]`.

```mw
for (int i = 1; i < n; ++i) {
    a[i] = a[i - 1] + b[i] + 1;
}
```

Each loop iteration performs two actions

- Calculate `a[i - 1] + b[i] + 1`
- Assign the value to `a[i]`

Calculating the value `a[i - 1] + b[i] + 1`, and then performing the assignment can be decomposed into two lines (statements s1 and s2):

```mw
int tmp = b[i] + 1; // s1
a[i] = a[i - 1] + tmp; // s2
```

The first line, `int tmp = b[i] + 1;`, has no loop-carried dependence. The loop can then be parallelized by computing the temp value in parallel, and then synchronizing the assignment to `a[i]`.

```mw
post(0);
for (int i = 1; i < n; ++i) {
    int tmp = b[i] + 1; // s1
    wait(i - 1);

    a[i] = a[i - 1] + tmp; // s2
    post(i);
}
```

Let's say the time of execution of s1 and s2 be $T_{s_{1}}$ and $T_{s_{2}}$ then the execution time for sequential form of above code is $n\cdot (T_{s_{1}}+T_{s_{2}})$ , Now because DOACROSS Parallelism exists, speed-up may be achieved by executing iterations in a pipelined fashion which gives us an execution time of $T_{s_{1}}+n\cdot T_{s_{2}}$ .

### DOPIPE parallelism

DOPIPE Parallelism implements pipelined parallelism for loop-carried dependence where a loop iteration is distributed over multiple, synchronized loops. The goal of DOPIPE is to act like an assembly line, where one stage is started as soon as there is sufficient data available for it from the previous stage.

Consider the following, synchronous code with dependence `s1[i] ->T s1[i + 1]`.

```mw
for (int i = 1; i < n; ++i) {
    a[i] = a[i - 1] + b[i]; // s1
    c[i] += a[i]; // s2
}
```

s1 must be executed sequentially, but s2 has no loop-carried dependence. s2 could be executed in parallel using DOALL Parallelism after performing all calculations needed by s1 in series. However, the speedup is limited if this is done. A better approach is to parallelize such that the s2 corresponding to each s1 executes when said s1 is finished.

Implementing pipelined parallelism results in the following set of loops, where the second loop may execute for an index as soon as the first loop has finished its corresponding index.

```mw
for (int i = 1; i < n; ++i) {
    a[i] = a[i - 1] + b[i]; // s1
    post(i);
}

for (int i = 1; i < n; i++) {
    wait(i);
    c[i] += a[i]; // s2
}
```

Let's say the time of execution of s1 and s2 be $T_{s_{1}}$ and $T_{s_{2}}$ then the execution time for sequential form of above code is $n\cdot (T_{s_{1}}+T_{s_{2}})$ , Now because DOPIPE Parallelism exists, speed-up may be achieved by executing iterations in a pipelined fashion which gives us an execution time of $n\cdot T_{s_{1}}+({\frac {n}{p}})\cdot T_{s_{2}}$ , where p is the number of processor in parallel.
