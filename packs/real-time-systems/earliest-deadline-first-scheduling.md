---
title: "Earliest deadline first scheduling"
source: https://en.wikipedia.org/wiki/Earliest_deadline_first_scheduling
domain: real-time-systems
license: CC-BY-SA-4.0
tags: real-time, rtos, scheduling, preemption, interrupt latency, hard real-time
fetched: 2026-07-02
---

# Earliest deadline first scheduling

**Earliest deadline first** (**EDF**) or **least time to go** is a dynamic priority scheduling algorithm used in real-time operating systems to place processes in a priority queue. Whenever a scheduling event occurs (task finishes, new task released, etc.) the queue will be searched for the process closest to its deadline. This process is the next to be scheduled for execution.

## Description

EDF is an *optimal* scheduling algorithm on preemptive uniprocessors, in the following sense: if a collection of independent *jobs,* each characterized by an arrival time, an execution requirement and a deadline, can be scheduled (by any algorithm) in a way that ensures all the jobs complete by their deadline, the EDF will schedule this collection of jobs so they all complete by their deadline.

With scheduling periodic processes that have deadlines equal to their periods, EDF has a utilization bound of 100%. Thus, the schedulability test for EDF is:

$U=\sum _{i=1}^{n}{\frac {C_{i}}{T_{i}}}\leq 1,$

where the $\left\{C_{i}\right\}$ are the worst-case computation-times of the n processes and the $\left\{T_{i}\right\}$ are their respective inter-arrival periods (assumed to be equal to the relative deadlines).

That is, EDF can guarantee that all deadlines are met provided that the total CPU utilization is not more than 100%. Compared to fixed-priority scheduling techniques like rate-monotonic scheduling, EDF can guarantee all the deadlines in the system at higher loading.

Note that use the schedulability test formula under deadline as period. When deadline is less than period, things are different. Here is an example: The four periodic tasks needs scheduling, where each task is depicted as TaskNo( computation time, relative deadline, period). They are T0(5,13,20), T1(3,7,11), T2(4,6,10) and T3(1,1,20). This task group meets utilization is no greater than 1.0, where utilization is calculated as 5/20+3/11+4/10+1/20 = 0.97 (two digits rounded), but is still unschedulable, check **EDF Scheduling Failure** figure for details.

EDF is also an *optimal* scheduling algorithm on non-preemptive uniprocessors, but only among the class of scheduling algorithms that do not allow inserted idle time. When scheduling periodic processes that have deadlines equal to their periods, a sufficient (but not necessary) schedulability test for EDF becomes:

$U=\sum _{i=1}^{n}{\frac {C_{i}}{T_{i}}}\leq {1-p},$

Where *p* represents the penalty for non-preemption, given by *max* $\left\{C_{i}\right\}$ / *min* $\left\{T_{i}\right\}$ . If this factor can be kept small, non-preemptive EDF can be beneficial as it has low implementation overhead.

However, when the system is overloaded, the set of processes that will miss deadlines is largely unpredictable (it will be a function of the exact deadlines and time at which the overload occurs.) This is a considerable disadvantage to a real time systems designer. The algorithm is also difficult to implement in hardware and there is a tricky issue of representing deadlines in different ranges (deadlines can not be more precise than the granularity of the clock used for the scheduling). If a modular arithmetic is used to calculate future deadlines relative to now, the field storing a future relative deadline must accommodate at least the value of the (("duration" {of the longest expected time to completion} * 2) + "now"). Therefore EDF is not commonly found in industrial real-time computer systems.

Instead, most real-time computer systems use fixed-priority scheduling (usually rate-monotonic scheduling). With fixed priorities, it is easy to predict that overload conditions will cause the low-priority processes to miss deadlines, while the highest-priority process will still meet its deadline.

There is a significant body of research dealing with EDF scheduling in real-time computing; it is possible to calculate worst case response times of processes in EDF, to deal with other types of processes than periodic processes and to use servers to regulate overloads.

## Example

Consider 3 periodic processes scheduled on a preemptive uniprocessor. The execution times and periods are as shown in the following table:

| Process | Execution Time | Period |
|---|---|---|
| P1 | 1 | 8 |
| P2 | 2 | 5 |
| P3 | 4 | 10 |

In this example, the units of time may be considered to be schedulable time slices. The deadlines are that each periodic process must complete within its period.

### Timing diagram

In the timing diagram, the columns represent time slices with time increasing to the right, and the processes all start their periods at time slice 0. The timing diagram's alternating blue and white shading indicates each process's periods, with deadlines at the color changes.

The first process scheduled by EDF is P2, because its period is shortest, and therefore it has the earliest deadline. Likewise, when P2 completes, P1 is scheduled, followed by P3.

At time slice 5, both P2 and P3 have the same deadline, needing to complete before time slice 10, so EDF may schedule either one.

### Utilization

The utilization will be:

$\left({\frac {1}{8}}+{\frac {2}{5}}+{\frac {4}{10}}\right)=\left({\frac {37}{40}}\right)=0.925={\mathbf {92.5\%} }$

Since the least common multiple of the periods is 40, the scheduling pattern can repeat every 40 time slices. But, only 37 of those 40 time slices are used by P1, P2, or P3. Since the utilization, 92.5%, is not greater than 100%, the system is schedulable with EDF.

## Deadline interchange

Undesirable deadline interchanges may occur with EDF scheduling. A process may use a shared resource inside a critical section, to prevent it from being pre-emptively descheduled in favour of another process with an earlier deadline. If so, it becomes important for the scheduler to assign the running process the earliest deadline from among the other processes waiting for the resource. Otherwise the processes with earlier deadlines might miss them.

This is especially important if the process running the critical section has a much longer time to complete and exit from its critical section, which will delay releasing the shared resource. But the process might still be pre-empted in favour of others that have earlier deadlines but do not share the critical resource. This hazard of deadline interchange is analogous to priority inversion when using fixed-priority pre-emptive scheduling.

To speed up the deadline search within the ready queue, the queue entries be sorted according to their deadlines. When a new process or a periodic process is given a new deadline, it is inserted before the first process with a later deadline. This way, the processes with the earliest deadlines are always at the beginning of the queue.

## Heavy traffic analysis for EDF queues with reneging

In a heavy-traffic analysis of the behavior of a single-server queue under an earliest-deadline-first scheduling policy with reneging, the processes have deadlines and are served only until their deadlines elapse. The fraction of "reneged work", defined as the residual work not serviced due to elapsed deadlines, is an important performance measure.

## Comparison with fixed-priority schedulers

It is commonly accepted that an implementation of fixed-priority pre-emptive scheduling (FPS) is simpler than a dynamic priority scheduler, like the EDF. However, when comparing the maximum usage of an optimal scheduling under fixed priority (with the priority of each thread given by the rate-monotonic scheduling), the EDF can reach 100% while the theoretical maximum value for rate-monotonic scheduling is around 69%. In addition, the worst-case overhead of an EDF implementation (fully preemptive or limited/non-preemptive) for periodic and/or sporadic tasks can be made proportional to the logarithm of the largest time representation required by a given system (to encode deadlines and periods) using Digital Search Trees. In practical cases, such as embedded systems using a fixed, 32-bit representation of time, scheduling decisions can be made using this implementation in a small fixed-constant time which is independent of the number of system tasks. In such situations experiments have found little discernible difference in overhead between the EDF and FPS, even for task sets of (comparatively) large cardinality.

Note that EDF does not make any specific assumption on the periodicity of the tasks; hence, it can be used for scheduling periodic as well as aperiodic tasks.

### Critical real-time applications

**Earliest Deadline First** (EDF) scheduling finds its most significant applications in **real-time systems** where missing deadlines can lead to critical consequences. These domains typically require deterministic timing guarantees:

#### Industrial automation and transportation

- **Industrial robotics**: In automated manufacturing environments, EDF ensures precise timing for robotic arm movements and assembly operations, where even microsecond delays could cause production errors or equipment collisions.
- **Autonomous vehicles**: Advanced Driver Assistance Systems (ADAS) utilize EDF to prioritize safety-critical tasks like obstacle detection and emergency braking, where response times under 100ms are often required.
- **Avionics systems**: Aircraft flight control systems and drones employ EDF for processing time-sensitive sensor data (e.g., GPS, altimeter readings) to maintain stable navigation.

#### Telecommunications and data processing

- **Real-time media streaming**: Video conferencing and live streaming services use EDF to prioritize transmission of key video frames and audio packets, minimizing latency and buffer delays.
- **5G and medical IoT**: Connected medical devices like pacemakers rely on EDF to ensure immediate transmission of critical health alerts while maintaining regular monitoring functions.

#### Safety-critical embedded systems

- **Medical devices**: Patient ventilators and cardiac monitors implement EDF to guarantee processing of life-critical signals (e.g., oxygen saturation alerts) within strict deadlines.
- **Industrial safety systems**: Nuclear power plants and chemical processing facilities use EDF for emergency shutdown mechanisms requiring microsecond-level response times.

## Kernels implementing EDF scheduling

Although EDF implementations are not common in commercial real-time kernels, here are a few links of open-source and real-time kernels implementing EDF:

- SHARK: The SHaRK RTOS, implementing various versions of EDF scheduling and resource reservation scheduling algorithms
- ERIKA Enterprise: ERIKA Enterprise, which provides an implementation of EDF optimized for small microcontrollers with an API similar to the OSEK API.
- The Everyman Kernel: The Everyman Kernel implements either EDF or Deadline Monotonic scheduling depending on the user's configuration.
- MaRTE OS: MaRTE OS acts as a runtime for Ada applications and implements a wide range of scheduling algorithms including EDF.
- The AQuoSA project constitutes a modification to the Linux kernel enriching the process scheduler with EDF scheduling capabilities. The timing of the scheduling cannot be as precise as in the case of the above hard real-time Operating Systems, yet it is sufficiently precise so as to greatly enhance predictability, and thus fulfill the real-time requirements, of multimedia applications. AQuoSA is one of a few projects that provides real-time scheduling capabilities to unprivileged users on a system in a controlled way, by means of a properly designed access-control model.
- The Linux kernel has an earliest deadline first implementation named `SCHED DEADLINE` which is available since the release 3.14.
- The real-time scheduler developed in the context of the IRMOS European Project is a multi-processor real-time scheduler for the Linux kernel, particularly suitable for temporal isolation and provisioning of QoS guarantees to complex multi-threaded software components and also entire virtual machines. For example, when using Linux as host OS and KVM as hypervisor, IRMOS can be used to provide scheduling guarantees to individual VMs and at the same time isolate their performance so as to avoid undesired temporal interferences. IRMOS features a combined EDF/FP hierarchical scheduler. At the outer level there is a partitioned EDF scheduler on the available CPUs. However, reservations are multi-CPU, and global FP over multi-processors is used at the inner level in order to schedule the threads (and/or processes) attached to each outer EDF reservation.
- Xen has had an EDF scheduler for some time now.
- The Plan 9 OS from Bell Labs incorporates EDFI, a "lightweight real-time scheduling protocol that combines EDF with deadline inheritance over shared resources."
- RTEMS: The EDF scheduler will be available in version 4.11.
- Litmus-RT: A real-time extension of the Linux kernel with a focus on multiprocessor real-time scheduling and synchronization. Its set of real-time algorithms include Partitioned-EDF, Global-EDF, and Clustered-EDF schedulers.
- XNU Clutch Scheduler: As of 2018, Apple's XNU kernel implements the EDF algorithm in its Clutch Scheduler with the goal of improving responsiveness.
- SuperTinyKernel RTOS: A lightweight, high-performance RTOS designed for embedded systems with ARM Cortex-M or RISC-V MCUs. Since version 1.1.2, STK provides an EDF scheduler for hard real-time applications, enabling predictable timing on resource-constrained devices.
