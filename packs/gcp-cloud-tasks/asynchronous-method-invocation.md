---
title: "Asynchronous method invocation"
source: https://en.wikipedia.org/wiki/Asynchronous_method_invocation
domain: gcp-cloud-tasks
license: CC-BY-SA-4.0
tags: gcp cloud tasks, task queue gcp, asynchronous execution gcp, distributed task dispatch
fetched: 2026-07-02
---

# Asynchronous method invocation

In multithreaded computer programming, **asynchronous method invocation** (**AMI**), also known as **asynchronous method calls** or the **asynchronous pattern** is a design pattern in which the call site is not blocked while waiting for the called code to finish. Instead, the calling thread is notified when the reply arrives. Polling for a reply is an undesired option.

## Background

**AMI** is a design pattern for asynchronous invocation of potentially long-running methods of an object. It is equivalent to the IOU ("I owe you") pattern described in 1996 by Allan Vermeulen.

In most programming languages a called method is executed synchronously, i.e. in the thread of execution from which it is invoked. If the method takes a long time to complete, e.g. because it is loading data over the internet, the calling thread is blocked until the method has finished. When this is not desired, it is possible to start a "worker thread" and invoke the method from there. In most programming environments this requires many lines of code, especially if care is taken to avoid the overhead that may be caused by creating many threads. AMI solves this problem in that it augments a potentially long-running ("synchronous") object method with an "asynchronous" variant that returns immediately, along with additional methods that make it easy to receive notification of completion, or to wait for completion at a later time.

One common use of AMI is in the active object design pattern. Alternatives are synchronous method invocation and future objects. An example for an application that may make use of AMI is a web browser that needs to display a web page even before all images are loaded.

Since method is a special case of procedure, **asynchronous method invocation** is a special case of asynchronous procedure call.

## Implementations

### Java class

FutureTask class in Java use events to solve the same problem. This pattern is a variant of AMI whose implementation carries more overhead, but it is useful for objects representing software components.

### .NET Framework

- Asynchronous Programming Model (APM) pattern (used before .NET Framework 2.0)
- Event-based Asynchronous Pattern (EAP) (used in .NET Framework 2.0)
- Task-based Asynchronous Pattern (TAP) (used in .NET Framework 4.0)

#### Example

The following example is loosely based on a standard AMI style used in the .NET Framework. Given a method `Accomplish`, one adds two new methods `BeginAccomplish` and `EndAccomplish`:

```mw
class Example 
{
    Result       Accomplish(args …)
    IAsyncResult BeginAccomplish(args …)
    Result       EndAccomplish(IAsyncResult a)
    …
}
```

Upon calling `BeginAccomplish`, the client immediately receives an object of type `AsyncResult` (which implements the `IAsyncResult` interface), so it can continue the calling thread with unrelated work. In the simplest case, eventually there is no more such work, and the client calls `EndAccomplish` (passing the previously received object), which blocks until the method has completed and the result is available. The `AsyncResult` object normally provides at least a method that allows the client to query whether the long-running method has already completed:

```mw
interface IAsyncResult 
{
    bool HasCompleted()
    …
}
```

One can also pass a callback method to `BeginAccomplish`, to be invoked when the long-running method completes. It typically calls `EndAccomplish` to obtain the return value of the long-running method. A problem with the callback mechanism is that the callback function is naturally executed in the worker thread (rather than in the original calling thread), which may cause race conditions.

In the .NET Framework documentation, the term event-based asynchronous pattern refers to an alternative API style (available since .NET 2.0) using a method named `AccomplishAsync` instead of `BeginAccomplish`. A superficial difference is that in this style the return value of the long-running method is passed directly to the callback method. Much more importantly, the API uses a special mechanism to run the callback method (which resides in an event object of type `AccomplishCompleted`) in the same thread in which `BeginAccomplish` was called. This eliminates the danger of race conditions, making the API easier to use and suitable for software components; on the other hand this implementation of the pattern comes with additional object creation and synchronization overhead.
