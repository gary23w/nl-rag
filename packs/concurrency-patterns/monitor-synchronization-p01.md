---
title: "Monitor (synchronization) (part 1/2)"
source: https://en.wikipedia.org/wiki/Monitor_(synchronization)
domain: concurrency-patterns
license: CC-BY-SA-4.0
tags: thread pool, lock-free, compare-and-swap, coroutine, synchronization primitive, atomic operation
fetched: 2026-07-02
part: 1/2
---

# Monitor (synchronization)

In concurrent programming, a **monitor** is a synchronization construct that prevents threads from concurrently accessing a shared object's state *and* allows them to wait for the state to change. They provide a mechanism for threads to temporarily give up exclusive access in order to wait for some condition to be met, before regaining exclusive access and resuming their task. A monitor consists of a mutex (lock) and at least one condition variable. A **condition variable** is explicitly 'signalled' when the object's state is modified, temporarily passing the mutex to another thread 'waiting' on the condition variable.

Another definition of **monitor** is a **thread-safe** object, class, or module that contains and uses a mutex to safely allow access to its methods or variables by more than one thread. The defining characteristic of a monitor is that its methods are executed with mutual exclusion: at each point in time, at most one thread may be executing any of the monitor's methods. By using one or more condition variables it can also provide the ability for threads to wait on a certain condition (thus using the first definition of a "monitor"). For the rest of this article, this sense of "monitor" will be referred to as a "thread-safe object/class/module."

Monitors were invented by Per Brinch Hansen and C. A. R. Hoare, and were first implemented in Brinch Hansen's Concurrent Pascal language.


## Mutual exclusion

While a thread is executing a method of a thread-safe object, it is said to *occupy* the object, by holding its mutex (lock). Thread-safe objects are implemented to enforce that *at any point in time, at most one thread may occupy the object*. The lock, which is initially unlocked, is locked at the start of each public method, and is unlocked at each return from each public method.

Upon calling one of the methods, a thread must wait until no other thread is executing any of the thread-safe object's methods before starting execution of its method. Note that without this mutual exclusion, two threads could cause data races and logical errors. For example, two threads withdrawing 1000 from the account could both return true, while causing the balance to drop by only 1000, as follows: first, both threads fetch the current balance, find it greater than 1000, and subtract 1000 from it; then, both threads store the balance and return.
