---
title: "Speedup"
source: https://en.wikipedia.org/wiki/Speedup
domain: parallel-complexity
license: CC-BY-SA-4.0
tags: parallel complexity, work span model, brent theorem, p complete problem
fetched: 2026-07-02
---

# Speedup

In computer architecture, **speedup** is a number that measures the relative performance of two systems processing the same problem. More technically, it is the improvement in speed of execution of a task executed on two similar architectures with different resources. The notion of speedup was established by Amdahl's law, which was particularly focused on parallel processing. However, speedup can be used more generally to show the effect on performance after any resource enhancement.

## Definitions

Speedup can be defined for two different types of quantities: *latency* and *throughput*.

*Latency* of an architecture is the reciprocal of the execution speed of a task:

$L={\frac {1}{v}}={\frac {T}{W}},$

where

- *v* is the execution speed of the task;
- *T* is the execution time of the task;
- *W* is the execution workload of the task.

*Throughput* of an architecture is the execution rate of a task:

$Q=\rho vA={\frac {\rho AW}{T}}={\frac {\rho A}{L}},$

where

- *ρ* is the execution density (e.g., the number of stages in an instruction pipeline for a pipelined architecture);
- *A* is the execution capacity (e.g., the number of processors for a parallel architecture).

Latency is often measured in seconds per unit of execution workload. Throughput is often measured in units of execution workload per second. Another unit of throughput is instructions per cycle (IPC) and its reciprocal, cycles per instruction (CPI), is another unit of latency.

Speedup is dimensionless and defined differently for each type of quantity so that it is a consistent metric.

### Speedup in latency

Speedup in *latency* is defined by the following formula:

$S_{\text{latency}}={\frac {L_{1}}{L_{2}}}={\frac {T_{1}W_{2}}{T_{2}W_{1}}},$

where

- *S*latency is the speedup in latency of the architecture 2 with respect to the architecture 1;
- *L*1 is the latency of the architecture 1;
- *L*2 is the latency of the architecture 2.

Speedup in latency can be predicted from Amdahl's law or Gustafson's law.

### Speedup in throughput

Speedup in *throughput* is defined by the formula:

$S_{\text{throughput}}={\frac {Q_{2}}{Q_{1}}}={\frac {\rho _{2}A_{2}T_{1}W_{2}}{\rho _{1}A_{1}T_{2}W_{1}}}={\frac {\rho _{2}A_{2}}{\rho _{1}A_{1}}}S_{\text{latency}},$

where

- *S*throughput is the speedup in throughput of the architecture 2 with respect to the architecture 1;
- *Q*1 is the throughput of the architecture 1;
- *Q*2 is the throughput of the architecture 2.

## Examples

### Using execution times

We are testing the effectiveness of a branch predictor on the execution of a program. First, we execute the program with the standard branch predictor on the processor, which yields an execution time of 6.75 seconds. Next, we execute the program with our modified (and hopefully improved) branch predictor on the same processor, which produces an execution time of 4.50 seconds. In both cases the execution workload is the same. Using our speedup formula, we know

$S_{\text{latency}}={\frac {L_{\text{old}}}{L_{\text{new}}}}={\frac {6.75~\mathrm {s} }{4.50~\mathrm {s} }}=1.5.$

Our new branch predictor has provided a 1.5x speedup over the original.

### Using cycles per instruction and instructions per cycle

We can also measure speedup in cycles per instruction (CPI) which is a latency. First, we execute the program with the standard branch predictor, which yields a CPI of 3. Next, we execute the program with our modified branch predictor, which yields a CPI of 2. In both cases the execution workload is the same and both architectures are not pipelined nor parallel. Using the speedup formula gives

$S_{\text{latency}}={\frac {L_{\text{old}}}{L_{\text{new}}}}={\frac {3~{\text{CPI}}}{2~{\text{CPI}}}}=1.5.$

We can also measure speedup in instructions per cycle (IPC), which is a throughput and the inverse of CPI. Using the speedup formula gives

$S_{\text{throughput}}={\frac {Q_{\text{new}}}{Q_{\text{old}}}}={\frac {0.5~{\text{IPC}}}{0.33~{\text{IPC}}}}=1.5.$

We achieve the same 1.5x speedup, though we measured different quantities.

## Additional details

Let *S* be the speedup of execution of a task and *s* the speedup of execution of the part of the task that benefits from the improvement of the resources of an architecture. *Linear speedup* or *ideal speedup* is obtained when *S* = *s*. When running a task with linear speedup, doubling the local speedup doubles the overall speedup. As this is ideal, it is considered very good scalability.

*Efficiency* is a metric of the utilization of the resources of the improved system defined as

$\eta ={\frac {S}{s}}.$

Its value is typically between 0 and 1. Programs with linear speedup and programs running on a single processor have an efficiency of 1, while many difficult-to-parallelize programs have efficiency such as 1/ln(*s*) that approaches 0 as the number of processors *A* = *s* increases.

In engineering contexts, efficiency curves are more often used for graphs than speedup curves, since

- all of the area in the graph is useful (whereas in speedup curves half of the space is wasted);
- it is easy to see how well the improvement of the system is working;
- there is no need to plot a "perfect speedup" curve.

In marketing contexts, speedup curves are more often used, largely because they go up and to the right and thus appear better to the less-informed.

## Super-linear speedup

Sometimes a speedup of more than *A* when using *A* processors is observed in parallel computing, which is called *super-linear speedup*. Super-linear speedup rarely happens and often confuses beginners, who believe the theoretical maximum speedup should be *A* when *A* processors are used.

One possible reason for super-linear speedup in low-level computations is the cache effect resulting from the different memory hierarchies of a modern computer: in parallel computing, not only do the numbers of processors change, but so does the size of accumulated caches from different processors. With the larger accumulated cache size, more or even all of the working set can fit into caches and the memory access time reduces dramatically, which causes the extra speedup in addition to that from the actual computation.

An analogous situation occurs when searching large datasets, such as the genomic data searched by BLAST implementations. There the accumulated RAM from each of the nodes in a cluster enables the dataset to move from disk into RAM thereby drastically reducing the time required by e.g. mpiBLAST to search it.

Super-linear speedups can also occur when performing backtracking in parallel: an exception in one thread can cause several other threads to backtrack early, before they reach the exception themselves.

Super-linear speedups can also occur in parallel implementations of branch-and-bound for optimization: the processing of one node by one processor may affect the work other processors need to do for the other nodes.
