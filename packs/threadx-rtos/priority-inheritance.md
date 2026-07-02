---
title: "Priority inheritance"
source: https://en.wikipedia.org/wiki/Priority_inheritance
domain: threadx-rtos
license: CC-BY-SA-4.0
tags: threadx rtos, azure rtos, preemptive scheduler, priority inheritance
fetched: 2026-07-02
---

# Priority inheritance

In real-time computing, **priority inheritance** is a method for eliminating unbounded priority inversion. Using this programming method, a process scheduling algorithm increases the priority of a process (A) to the maximum priority of any other process waiting for any resource on which A has a resource lock (if it is higher than the original priority of A).

The basic idea of the priority inheritance protocol is that when a job blocks one or more high-priority jobs, it ignores its original priority assignment and executes its critical section at an elevated priority level. After executing its critical section and releasing its locks, the process returns to its original priority level.

## Example

Consider three jobs:

| Job Name | Priority |
|---|---|
| H | High |
| M | Medium |
| L | Low |

Suppose that both H and L require some shared resource. If L acquires this shared resource (entering a critical section), and H subsequently requires it, H will block until L releases it (leaving its critical section). Without priority inheritance, process M could preempt process L during the critical section and delay its completion, in effect causing the lower-priority process M to indirectly preempt the high-priority process H. This is a priority inversion bug.

With priority inheritance, L will execute its critical section at H's high priority whenever H is blocked on the shared resource. As a result, M will be unable to preempt L and will be blocked. That is, the higher-priority job M must wait for the critical section of the lower priority job L to be executed, because L has inherited H's priority. When L exits its critical section, it regains its original (low) priority and awakens H (which was blocked by L). H, having high priority, preempts L and runs to completion. This enables M and L to resume in succession and run to completion without priority inversion.

## Operating systems supporting priority inheritance

- Windows
- Linux
- ERIKA Enterprise
- FreeRTOS
- Eclipse ThreadX
- VxWorks
- iRMX
