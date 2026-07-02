---
title: "Rate-monotonic scheduling"
source: https://en.wikipedia.org/wiki/Rate-monotonic_scheduling
domain: real-time-systems
license: CC-BY-SA-4.0
tags: real-time, rtos, scheduling, preemption, interrupt latency, hard real-time
fetched: 2026-07-02
---

# Rate-monotonic scheduling

In computer science, **rate-monotonic scheduling** (**RMS**) is a priority assignment algorithm used in real-time operating systems (RTOS) with a static-priority scheduling class. The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority.

These operating systems are generally preemptive and have deterministic guarantees with regard to response times. Rate monotonic analysis is used in conjunction with those systems to provide scheduling guarantees for a particular application.

## Introduction

A simple version of rate-monotonic analysis assumes that threads have the following properties:

- No resource sharing (processes do not share resources, *e.g.* a hardware resource, a queue, or any kind of semaphore blocking or non-blocking (busy-waits))
- Deterministic deadlines are exactly equal to periods
- Static priorities (the task with the highest static priority that is runnable immediately preempts all other tasks)
- Static priorities assigned according to the *rate monotonic* conventions (tasks with shorter periods/deadlines are given higher priorities)
- Context switch times and other thread operations are free and have no impact on the model

It is a mathematical model that contains a calculated simulation of periods in a closed system, where round-robin and time-sharing schedulers fail to meet the scheduling needs otherwise. Rate monotonic scheduling looks at a run modeling of all threads in the system and determines how much time is needed to meet the guarantees for the set of threads in question.

### Optimality

The rate-monotonic priority assignment is *optimal* under the given assumptions, meaning that if any static-priority scheduling algorithm can meet all the deadlines, then the rate-monotonic algorithm can too. The deadline-monotonic scheduling algorithm is also optimal with equal periods and deadlines, in fact in this case the algorithms are identical; in addition, deadline monotonic scheduling is optimal when deadlines are less than periods. For the task model in which deadlines can be greater than periods, Audsley's algorithm endowed with an exact schedulability test for this model finds an optimal priority assignment.

## Upper bounds on utilization

### Least upper bound

Liu & Layland (1973) proved that for a set of n periodic tasks with unique periods, a feasible schedule that will always meet deadlines exists if the CPU utilization is below a specific bound (depending on the number of tasks). The schedulability test for RMS is:

$U=\sum _{i=1}^{n}{U_{i}}=\sum _{i=1}^{n}{\frac {C_{i}}{T_{i}}}\leq n({2}^{1/n}-1)$

where U is the utilization factor, Ci is the computation time for process i, Ti is the release period (with deadline one period later) for process i, and n is the number of processes to be scheduled. For example, U ≤ 0.8284 for two processes. When the number of processes tends towards infinity, this expression will tend towards:

$\lim _{n\rightarrow \infty }n({\sqrt[{n}]{2}}-1)=\ln 2\approx 0.693147\ldots$

Therefore, a rough estimate when ${n}\geq {10}$ is that RMS can meet all of the deadlines if total CPU utilization, U, is less than 70%. The other 30% of the CPU can be dedicated to lower-priority, non-real-time tasks. For smaller values of n or in cases where U is close to this estimate, the calculated utilization bound should be used.

In practice, for the ${i^{th}}$ process, ${C_{i}}$ should represent the worst-case (i.e. longest) computation time and ${T_{i}}$ should represent the worst-case deadline (i.e. shortest period) in which all processing must occur.

### Relationship to queueing theory

In queueing theory, Ti is called the **interarrival time**, and Ci is called the **service time**. These two parameters are often specified as rates:

$\lambda _{i}={1 \over T_{i}}$

is the

arrival rate

, and

$\mu _{i}={1 \over C_{i}}$

is the

service rate

.

The utilization for each task, denoted ρi, is then:

$\rho _{i}={\lambda _{i} \over \mu _{i}}={C_{i} \over T_{i}}=U_{i}$

as above.

### Upper bound for harmonic task sets

Liu and Layland noted that this bound may be relaxed to the maximum possible value of 1.0, if for tasks ${T_{m}}$ , ${T_{i}}$ where ${T_{m}}{>}{T_{i}}$ and $i=1...m-1$ , ${T_{m}}$ is an integer multiple of ${T_{i}}$ , which is to say that all tasks have a period that is not just a multiple of the shortest period, ${T_{1}}$ , but instead that any task's period is a multiple of all shorter periods. This is known as an harmonic task set. An example of this would be: $[{T_{1}},{T_{2}},{T_{3}},{T_{4}}]=[1,3,6,12]$ . It is acknowledged by Liu and Layland that it is not always feasible to have a harmonic task set and that in practice other mitigation measures, such as buffering for tasks with soft-time deadlines or using a dynamic priority assignment approach may be used instead to allow for a higher bound.

### Generalization to harmonic chains

Kuo and Mok showed that for a task set made up of K harmonic task subsets (known as *harmonic chains*), the least upper bound test becomes:

$U=\sum _{i=1}^{n}{\frac {C_{i}}{T_{i}}}\leq K({2}^{1/K}-1)$

In the instance where for each task, its period is an exact multiple of every other task that has a shorter period, the task set can be thought of as being composed of n harmonic task subsets of size 1 and therefore ${K}{=}{n}$ , which makes this generalization equivalent to Liu and Layland's least upper bound. When ${K}{=}{1}$ , the upper bound becomes 1.0, representing full utilization.

### Stochastic bounds

It has been shown that a randomly generated periodic task system will usually meet all deadlines when the utilization is 88% or less, however this fact depends on knowing the exact task statistics (periods, deadlines) which cannot be guaranteed for all task sets, and in some cases the authors found that the utilization reached the least upper bound presented by Liu and Layland.

### Hyperbolic bound

The hyperbolic bound is a tighter sufficient condition for schedulability than the one presented by Liu and Layland:

$\prod _{i=1}^{n}(U_{i}+1)\leq 2$

,

where Ui is the CPU utilization for each task. It is the tightest upper bound that can be found using only the individual task utilization factors.

## Resource sharing

In many practical applications, resources are shared and the unmodified **RMS** will be subject to priority inversion and deadlock hazards. In practice, this is solved by disabling preemption or by priority inheritance. Alternative methods are to use lock-free algorithms or avoid the sharing of a mutex/semaphore across threads with different priorities. This is so that resource conflicts cannot result in the first place.

### Disabling of preemption

- The `OS_ENTER_CRITICAL()` and `OS_EXIT_CRITICAL()` primitives that lock CPU interrupts in a real-time kernel, e.g. MicroC/OS-II
- The `splx()` family of primitives which nest the locking of device interrupts (FreeBSD 5.x/6.x),

### Priority inheritance

- The *basic priority inheritance protocol* promotes the priority of the task that holds the resource to the priority of the task that requests that resource at the time the request is made. Upon release of the resource, the original priority level before the promotion is restored. This method does not prevent deadlocks and suffers from *chained blocking*. That is, if a high priority task accesses multiple shared resources in sequence, it may have to wait (block) on a lower priority task for each of the resources. The real-time patch Archived 2020-10-13 at the Wayback Machine to the Linux kernel includes an implementation of this formula.

- The priority ceiling protocol enhances the basic priority inheritance protocol by assigning a *ceiling priority* to each semaphore, which is the priority of the highest job that will ever access that semaphore. A job cannot preempt a lower priority critical section if its priority is lower than the ceiling priority for that section. This method prevents deadlocks and bounds the blocking time to at most the length of one lower priority critical section. This method can be suboptimal, in that it can cause unnecessary blocking. The priority ceiling protocol is available in the VxWorks real-time kernel. It is also known as *Highest Locker's Priority Protocol* (HLP).

Priority inheritance algorithms can be characterized by two parameters. First, is the inheritance lazy (only when essential) or immediate (boost priority before there is a conflict). Second is the inheritance optimistic (boost a minimum amount) or pessimistic (boost by more than the minimum amount):

|   | pessimistic | optimistic |
|---|---|---|
| immediate | `OS_ENTER_CRITICAL()` / `OS_EXIT_CRITICAL()` | `splx()`, highest locker |
| lazy |   | priority ceiling protocol, basic priority inheritance protocol |

In practice there is no mathematical difference (in terms of the Liu-Layland system utilization bound) between the lazy and immediate algorithms, and the immediate algorithms are more efficient to implement, and so they are the ones used by most practical systems.

An example of usage of basic priority inheritance is related to the "Mars Pathfinder reset bug" which was fixed on Mars by changing the creation flags for the semaphore so as to enable the priority inheritance.

## Interrupt service routines

All interrupt service routines (ISRs), whether they have a hard real-time deadline or not should be included in RMS analysis to determine schedulability in cases where ISRs have priorities above all scheduler-controlled tasks. An ISR may already be appropriately prioritized under RMS rules if its processing period is shorter than that of the shortest, non-ISR process. However, an ISR with a period/deadline longer than any non-ISR process period with a critical deadline results in a violation of RMS and prevents the use of the calculated bounds for determining schedulability of a task set.

### Mitigating mis-prioritized ISRs

One method for mitigating a mis-prioritized ISR is to adjust the analysis by reducing the ISR's period to be equal to that of the shortest period, if possible. Imposing this shorter period results in prioritization that conforms to RMS, but also results in a higher utilization factor for the ISR and therefore for the total utilization factor, which may still be below the allowable bound and therefore schedulability can be proven. As an example, consider a hardware ISR that has a computation time, ${C_{isr}}$ of 500 microseconds and a period, ${T_{isr}}$ , of 4 milliseconds. If the shortest scheduler-controlled task has a period, ${T_{1}}$ of 1 millisecond, then the ISR would have a higher priority, but a lower rate, which violates RMS. For the purposes of proving schedulability, set ${T_{isr}}={T_{1}}$ and recalculate the utilization factor for the ISR (which also raises the total utilization factor). In this case, ${U_{isr}}{=}{C_{isr}}/{T_{isr}}$ will change from ${0.5ms}/{4ms}{=}0.125$ to ${0.5ms}/{1ms}{=}0.5$ . This utilization factor would be used when adding up the total utilization factor for the task set and comparing to the upper bound to prove schedulability. It should be emphasized that adjusting the period of the ISR is for analysis only and that the true period of the ISR remains unchanged.

Another method for mitigating a mis-prioritized ISR is to use the ISR to only set a new semaphore/mutex while moving the time-intensive processing to a new process that has been appropriately prioritized using RMS and will block on the new semaphore/mutex. When determining schedulability, a margin of CPU utilization due to ISR activity should be subtracted from the least upper bound. ISRs with negligible utilization may be ignored.

## Examples

### Example 1

| Process | Computation time *C* | Release period *T* | Priority |
|---|---|---|---|
| P1 | 1 | 8 | 2 |
| P2 | 2 | 5 | 1 |
| P3 | 2 | 10 | 3 |

Under RMS, P2 has the highest release rate (i.e. the shortest release period) and so would have the highest priority, followed by P1 and finally P3.

#### Least upper bound

The utilization will be:

$U={\frac {1}{8}}+{\frac {2}{5}}+{\frac {2}{10}}=0.725$

.

The sufficient condition for $3\,$ processes, under which we can conclude that the system is schedulable is:

${U_{lub}}=3(2^{\frac {1}{3}}-1)=0.77976$

Because $U<U_{lub}$ , and because being below the Least Upper Bound is a sufficient condition, the system is guaranteed to be schedulable.

### Example 2

| Process | Computation time *C* | Release period *T* | Priority |
|---|---|---|---|
| P1 | 3 | 16 | 3 |
| P2 | 2 | 5 | 1 |
| P3 | 2 | 10 | 2 |

Under RMS, P2 has the highest release rate (i.e. the shortest release period) and so would have the highest priority, followed by P3 and finally P1.

#### Least upper bound

Using the Liu and Layland bound, as in Example 1, the sufficient condition for $3\,$ processes, under which we can conclude that the task set is schedulable, remains:

${U_{lub}}=3(2^{\frac {1}{3}}-1)=0.77976$

The total utilization will be:

$U={\frac {3}{16}}+{\frac {2}{5}}+{\frac {2}{10}}=0.7875$

.

Since $U>U_{lub}$ , the system is determined *not* to be guaranteed to be schedulable by the Liu and Layland bound.

#### Hyperbolic bound

Using the tighter Hyperbolic bound as follows:

$\prod _{i=1}^{n}(U_{i}+1)=({\frac {3}{16}}+1)*({\frac {2}{5}}+1)*({\frac {2}{10}}+1)=1.995\leq 2$

it is found that the task set *is* schedulable.

### Example 3

| Process | Computation time *C* | Release period *T* | Priority |
|---|---|---|---|
| P1 | 7 | 32 | 3 |
| P2 | 2 | 5 | 1 |
| P3 | 2 | 10 | 2 |

Under RMS, P2 has the highest rate (i.e. the shortest period) and so would have the highest priority, followed by P3 and finally P1.

#### Least upper bound

Using the Liu and Layland bound, as in Example 1, the sufficient condition for $3\,$ processes, under which we can conclude that the task set is schedulable, remains:

${U_{lub}}=3(2^{\frac {1}{3}}-1)=0.77976$

The total utilization will be:

$U={\frac {7}{32}}+{\frac {2}{5}}+{\frac {2}{10}}=0.81875$

.

Since $U>U_{lub}$ , the system is determined *not* to be guaranteed to be schedulable by the Liu and Layland bound.

#### Hyperbolic bound

Using the tighter Hyperbolic bound as follows:

$\prod _{i=1}^{n}(U_{i}+1)=({\frac {7}{32}}+1)*({\frac {2}{5}}+1)*({\frac {2}{10}}+1)=2.0475$

Since $2.0{<}2.0475$ the system is determined to *not* be guaranteed to be schedulable by the Hyperbolic bound.

#### Harmonic task set analysis

Because ${T_{3}}={2{T_{2}}}$ , tasks 2 and 3 can be considered a harmonic task subset. Task 1 forms its own harmonic task subset. Therefore, the number of harmonic task subsets, K, is 2.

${U_{lub,harmonic}}=K(2^{\frac {1}{K}}-1)=2(2^{\frac {1}{2}}-1)=0.828$

Using the total utilization factor calculated above (0.81875), since $0.81875<0.828$ the system is determined to be schedulable.
