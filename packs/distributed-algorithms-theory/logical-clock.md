---
title: "Logical clock"
source: https://en.wikipedia.org/wiki/Logical_clock
domain: distributed-algorithms-theory
license: CC-BY-SA-4.0
tags: distributed algorithm, consensus problem, byzantine fault tolerance, leader election
fetched: 2026-07-02
---

# Logical clock

A **logical clock** is a mechanism for capturing chronological and causal relationships in a distributed system. Often, distributed systems may have no physically synchronous global clock. In many applications (such as distributed GNU make), if two processes never interact, the lack of synchronization is unobservable and in these applications it is enough for the processes to agree on the event ordering (i.e., logical clock) rather than the wall-clock time. The idea of logical clocks is due to Leslie Lamport, who introduced it in 1978 with his system of timestamps.

## Local vs global time

In logical clock systems each process has two data structures: *logical local time* and *logical global time*. Logical local time is used by the process to mark its own events, and logical global time is the local information about global time. A special protocol is used to update logical local time after each local event, and logical global time when processes exchange data.

## Applications

Logical clocks are useful in computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.

## Algorithms

Some noteworthy logical clock algorithms are:

- Lamport timestamps, which are monotonically increasing software counters.
- Vector clocks, that allow for partial ordering of events in a distributed system.
- Version vectors, order replicas, according to updates, in an optimistic replicated system.
- Matrix clocks, an extension of vector clocks that also contains information about other processes' views of the system.
