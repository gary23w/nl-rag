---
title: "Weighted round robin"
source: https://en.wikipedia.org/wiki/Weighted_round_robin
domain: network-load-balancing
license: CC-BY-SA-4.0
tags: network load balancing, round-robin dns, weighted round robin, failover
fetched: 2026-07-02
---

# Weighted round robin

**Weighted round robin** (**WRR**) is a network scheduler for data flows, but also used to schedule processes.

Weighted round robin is a generalisation of round-robin scheduling. It serves a set of queues or tasks. Whereas round-robin cycles over the queues or tasks and gives one service opportunity per cycle, weighted round robin offers to each a fixed number of opportunities, as specified by the configured weight, which serves to influence the portion of capacity received by each queue or task. In computer networks, a service opportunity is the emission of one packet if the selected queue is non-empty.

If all packets have the same size, WRR is the simplest approximation of generalized processor sharing (GPS). Several variations of WRR exist. The main ones are the *classical* WRR, and the *interleaved* WRR.

## Algorithm

### Principles

WRR is presented in the following as a network scheduler. It can also be used to schedule tasks in a similar way.

A weighted round-robin network scheduler has n input queues, $q_{1},...,q_{n}$ . To each queue $q_{i}$ is associated $w_{i}$ , a positive integer, called the *weight*. The WRR scheduler has a cyclic behavior. In each cycle, each queue $q_{i}$ has $w_{i}$ emissions opportunities.

The different WRR algorithms differ in the distribution of these opportunities in the cycle.

### Classical WRR

In classical WRR the scheduler cycles over the queues. When a queue $q_{i}$ is selected, the scheduler will send packets, up to the emission of the $w_{i}$ packet or the end of the queue.

| **Constant and variables:** const N // Nb of queues const weight[1..N] // weight of each queue queues[1..N] // queues i // queue index c // packet counter **Instructions:** **while** true **do** **for** i **in** 1 .. N **do** c := 0 **while** (not queue[i].empty) and (c<weight[i]) **do** send(queue[i].head()) queue[i].dequeue() c:= c+1 |
|---|

### Interleaved WRR

Let $w_{max}=\max\{w_{i}\}$ , be the maximum weight. In IWRR, each cycle is split into $w_{max}$ rounds. A queue with weight $w_{i}$ can emit one packet at round r only if $r\leq w_{i}$ .

| **Constant and variables:** const N // Nb of queues const weight[1..N] // weight of each queue const w_max queues[1..N] // queues i // queue index r // round counter **Instructions:** **while** true **do** **for** r **in** 1 .. w_max **do** **for** i **in** 1 .. N **do** **if** (**not** queue[i].empty) **and** (weight[i] >= r) **then** send(queue[i].head()) queue[i].dequeue() |
|---|

### Example

Consider a system with three queues $q_{1},q_{2},q_{3}$ and respective weights $w_{1}=5,w_{2}=2,w_{3}=3$ . Consider a situation where there are 7 packets in the first queue, **A,B,C,D,E,F,G**, 3 in the second queue, **U,V,W** and 2 in the third queue **X,Y**. Assume that there are no more packet arrivals.

With classical WRR, in the first cycle, the scheduler first selects $q_{1}$ and transmits the five packets at head of queue,**A,B,C,D,E** (since $w_{1}=5$ ), then it selects the second queue, $q_{2}$ , and transmits the two packets at head of queue, **U,V** (since $w_{2}=2$ ), and last it selects the third queue, which has a weight equals to 3 but only two packets, so it transmits **X,Y**. Immediately after the end of transmission of **Y**, the second cycle starts, and **F,G** from $q_{1}$ are transmitted, followed by **W** from $q_{2}$ .

With interleaved WRR, the first cycle is split into 5 rounds (since $max(w_{1},w_{2},w_{3})=5$ ). In the first one (**r=1**), one packet from each queue is sent (**A,U,X**), in the second round (**r=2**), another packet from each queue is also sent (**B,V,Y**), in the third round (**r=3**), only queues $q_{1},q_{3}$ are allowed to send a packet (**$w_{1}>=r$**, **$w_{2}<r$** and **$w_{3}>=r$**), but since $q_{3}$ is empty, only **C** from $q_{1}$ is sent, and in the fourth and fifth rounds, only **D,E** from $q_{1}$ are sent. Then starts the second cycle, where **F,W,G** are sent.

## Task scheduling

Task or process scheduling can be done in WRR in a way similar to packet scheduling: when considering a set of n active tasks, they are scheduled in a cyclic way, each task $\tau _{i}$ gets $w_{i}$ quantum or slice of processor time .

## Properties

Like round-robin, weighted round robin scheduling is simple, easy to implement, work conserving and starvation-free.

When scheduling packets, if all packets have the same size, then WRR and IWRR are an approximation of Generalized processor sharing: a queue $q_{i}$ will receive a long-term part of the bandwidth equal to ${\frac {w_{i}}{\sum _{j=1}^{n}w_{j}}}$ (if all queues are active) while GPS serves infinitesimal amounts of data from each nonempty queue and offers this part on any interval.

If the queues have packets of variable length, the part of the bandwidth received by each queue depends not only on the weights but also on the packet sizes.

If a mean packets size $s_{i}$ is known for every queue $q_{i}$ , each queue will receive a long-term part of the bandwidth equal to ${\frac {s_{i}\times w_{i}}{\sum _{j=1}^{n}s_{j}\times w_{j}}}$ . If the objective is to give to each queue $q_{i}$ a portion $\rho _{i}$ of link capacity (with $\sum _{i=1}^{n}\rho _{i}=1$ ), one may set $w_{i}={\frac {\rho _{i}}{s_{i}}}$ .

Since IWRR has smaller per-class bursts than WRR, it implies smaller worst-case delays.

## Limitations and improvements

WRR for network packet scheduling was first proposed by Katevenis, Sidiropoulos and Courcoubetis in 1991, specifically for scheduling in ATM networks using fixed-size packets (cells). The primary limitation of weighted round-robin queuing is that it provides the correct percentage of bandwidth to each service class only if all the packets in all the queues are the same size or if the mean packet size is known in advance. In the more general case of IP networks with variable-size packets, to approximate GPS, the weight factors must be adjusted based on the packet size. That requires estimation of the average packet size, which makes a good GPS approximation hard to achieve in practice with WRR.

Deficit round robin is a later variation of WRR that achieves better GPS approximation without knowing the mean packet size of each connection in advance. More effective scheduling disciplines were also introduced, which handle the limitations mentioned above (e.g., weighted fair queuing).

## Use in real-time operating systems

Weighted round robin has been adopted by several real-time operating systems (RTOSes) as a task scheduling strategy, where task weights determine the proportion of CPU time allocated to each thread.

Notable examples include SuperTinyKernel RTOS, a bare-metal C++ RTOS for embedded systems, which implements a *Smooth Weighted Round Robin* (SWRR) strategy. SWRR is an improved variant of classical WRR that distributes CPU time proportionally to task weights while deliberately avoiding execution bursts, ensuring that high-weight tasks do not monopolise the processor in a single scheduling cycle but instead have their additional time quanta spread evenly across the cycle. This results in more uniform CPU utilisation and lower scheduling jitter compared to classical WRR, at the cost of a moderately more complex scheduling calculation per context switch.
