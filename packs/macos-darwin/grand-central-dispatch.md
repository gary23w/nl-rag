---
title: "Grand Central Dispatch"
source: https://en.wikipedia.org/wiki/Grand_Central_Dispatch
domain: macos-darwin
license: CC-BY-SA-4.0
tags: macos internals, darwin operating system, xnu kernel, grand central dispatch
fetched: 2026-07-02
---

# Grand Central Dispatch

**Grand Central Dispatch** (**GCD** or **libdispatch**) is a technology developed by Apple Inc. to optimize application support for systems with multi-core processors and other symmetric multiprocessing systems. It is an implementation of task parallelism based on the thread pool pattern. The fundamental idea is to move the management of the thread pool out of the hands of the developer, and closer to the operating system. The developer injects "work packages" into the pool oblivious of the pool's architecture. This model improves simplicity, portability and performance.

GCD was first released with Mac OS X 10.6, and is also available with iOS 4 and above. The name "Grand Central Dispatch" is a reference to Grand Central Terminal.

The source code for the library that provides the implementation of GCD's services, *libdispatch*, was released by Apple under the Apache License on September 10, 2009. It has been ported to FreeBSD 8.1+, MidnightBSD 0.3+, Linux, and Solaris. Attempts in 2011 to make libdispatch work on Windows were not merged into upstream. Apple has its own port of libdispatch.dll for Windows shipped with Safari and iTunes, but no SDK is provided.

Since around 2017, the original libdispatch repository hosted by Nick Hutchinson was deprecated in favor of a version that is part of the Swift core library created in June 2016. The new version supports more platforms, notably including Windows.

## Design

GCD works by allowing specific tasks in a program that can be run in parallel to be queued up for execution and, depending on availability of processing resources, scheduling them to execute on any of the available processor cores (referred to as "routing" by Apple).

A task can be expressed either as a function or as a "block." Blocks are an extension to the syntax of C, C++, and Objective-C programming languages that encapsulate code and data into a single object in a way similar to a closure. GCD can still be used in environments where blocks are not available.

Grand Central Dispatch still uses threads at the low level but abstracts them away from the programmer, who will not need to be concerned with as many details. Tasks in GCD are lightweight to create and queue; Apple states that 15 instructions are required to queue up a work unit in GCD, while creating a traditional thread could easily require several hundred instructions.

## Features

The dispatch framework declares several data types and functions to create and manipulate them:

- *Dispatch Queues* are objects that maintain a queue of *tasks*, either anonymous code blocks or functions, and execute these tasks in their turn. The library automatically creates several queues with different priority levels that execute several tasks concurrently, selecting the optimal number of tasks to run based on the operating environment. A client to the library may also create any number of serial queues, which execute tasks in the order they are submitted, one at a time. Because a serial queue can only run one task at a time, each task submitted to the queue is critical with regard to the other tasks on the queue, and thus a serial queue can be used instead of a lock on a contended resource.
- *Dispatch Sources* are objects that allow the client to register blocks or functions to execute asynchronously upon system events, such as a socket or file descriptor being ready for reading or writing, or a POSIX signal.
- *Dispatch Groups* are objects that allow several tasks to be grouped for later joining. Tasks can be added to a queue as a member of a group, and then the client can use the group object to wait until all of the tasks in that group have completed.
- *Dispatch Semaphores* are objects that allow a client to permit only a certain number of tasks to execute concurrently.

Libdispatch comes with its own object model, *OS Object*, that is partially compatible with the Objective-C model. As a result, its objects can be bridged *toll-free* to ObjC objects.

## Applications

GCD is used throughout macOS (beginning with 10.6 Snow Leopard), and Apple has encouraged its adoption by macOS application developers. FreeBSD developer Robert Watson announced the first adaptation of a major open source application, the Apache HTTP Server, to use GCD via the Apache GCD MPM (Multi-Processing Module) on May 11, 2010, in order to illustrate the programming model and how to integrate GCD into existing, large-scale multi-threaded, applications. His announcement observed that the GCD MPM had one third to half the number of lines as other threaded MPMs.

## Internals

GCD is implemented by libdispatch, with support from pthreads non-POSIX extensions developed by Apple. Apple has changed the interface since its inception (in OS X 10.5) through the official launch of GCD (10.6), Mountain Lion (10.8) and Mavericks (10.9). The latest changes involve making the code supporting pthreads, both in user mode and kernel, private (with kernel pthread support reduced to shims only, and the actual *workqueue* implementation moved to a separate kernel extension).
