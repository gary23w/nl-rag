---
title: "Protothread"
source: https://en.wikipedia.org/wiki/Protothread
domain: contiki-os
license: CC-BY-SA-4.0
tags: contiki os, contiki ng, protothread model, micro ip stack
fetched: 2026-07-02
---

# Protothread

A **protothread** is a low-overhead mechanism for concurrent programming.

Protothreads function as stackless, lightweight threads, or coroutines, providing a blocking context cheaply using minimal memory per protothread (on the order of single bytes).

Protothreads are used to accomplish a non-preempted form of concurrency known as cooperative multitasking and, therefore, do not incur context switch when yielding to another thread. Within a protothread, yielding is accomplished by utilizing Duff's device within a thread's function and an external variable used in within the switch statement. This allows jumping (resuming) from a yield upon another function call. In order to block threads, these yields may be guarded by a conditional so that successive calls to the same function will yield unless the guard conditional is true.

A feature of protothreads relative to other implementations of coroutines, or proper threads, is that they are stackless. This has advantages and disadvantages. A disadvantage is that local variables within the protothread cannot be trusted to have retained their values across a yield to another context. They must retain their state through the use of static or external, often global, variables. An advantage is that they are very lightweight and therefore useful on severely memory constrained systems like small microcontrollers where other solutions are impractical or less desirable.

Tom Duff, of Duff's device fame, had this to say about the shortcomings of the method: "a similar trick for interrupt-driven state machines that is too horrible to go into. [...] I never thought it was an adequate general-purpose coroutine implementation because it’s not easy to have multiple simultaneous activations of a coroutine and it’s not possible using this method to have coroutines give up control anywhere but in their top-level routine. A simple assembly-language stack-switching library lets you do both of those."

The protothread concept was developed by Adam Dunkels and Oliver Schmidt, based on prior work by Simon Tatham and Tom Duff.
