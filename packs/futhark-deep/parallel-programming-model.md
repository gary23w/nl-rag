---
title: "Parallel programming model"
source: https://en.wikipedia.org/wiki/Parallel_programming_model
domain: futhark-deep
license: CC-BY-SA-4.0
tags: futhark language, data parallelism, parallel programming model, purely functional programming, gpu computing
fetched: 2026-07-02
---

# Parallel programming model

In computing, a **parallel programming model** is an abstraction of parallel computer architecture, with which it is convenient to express algorithms and their composition in programs. The value of a programming model can be judged on its *generality*: how well a range of different problems can be expressed for a variety of different architectures, and its *performance*: how efficiently the compiled programs can execute. The implementation of a parallel programming model can take the form of a library invoked from a programming language, as an extension to an existing languages.

Consensus around a particular programming model is important because it leads to different parallel computers being built with support for the model, thereby facilitating portability of software. In this sense, programming models are referred to as *bridging* between hardware and software.

## Classification of parallel programming models

Classifications of parallel programming models can be divided broadly into two areas: process interaction and problem decomposition.

### Process interaction

Process interaction relates to the mechanisms by which parallel processes are able to communicate with each other. The most common forms of interaction are shared memory and message passing, but interaction can also be implicit (invisible to the programmer).

#### Shared memory

Shared memory is an efficient means of passing data between processes. In a shared-memory model, parallel processes share a global address space that they read and write to asynchronously. Asynchronous concurrent access can lead to race conditions, and mechanisms such as locks, semaphores and monitors can be used to avoid these. Conventional multi-core processors directly support shared memory, which many parallel programming languages and libraries, such as Cilk, OpenMP and Threading Building Blocks, are designed to exploit.

#### Message passing

In a message-passing model, parallel processes exchange data through passing messages to one another. These communications can be asynchronous, where a message can be sent before the receiver is ready, or synchronous, where the receiver must be ready. The Communicating sequential processes (CSP) formalisation of message passing uses synchronous communication channels to connect processes, and led to important languages such as Occam, Limbo and Go. In contrast, the actor model uses asynchronous message passing and has been employed in the design of languages such as D, Scala and SALSA.

#### Partitioned global address space

Partitioned Global Address Space (PGAS) models provide a middle ground between shared memory and message passing. PGAS provides a global memory address space abstraction that is logically partitioned, where a portion is local to each process. Parallel processes communicate by asynchronously performing operations (e.g. reads and writes) on the global address space, in a manner reminiscent of shared memory models. However by semantically partitioning the global address space into portions with affinity to a particular processes, they allow programmers to exploit locality of reference and enable efficient implementation on distributed memory parallel computers. PGAS is offered by many parallel programming languages and libraries, such as Fortran 2008, Chapel, UPC++, and SHMEM.

#### Implicit interaction

In an implicit model, no process interaction is visible to the programmer and instead the compiler and/or runtime is responsible for performing it. Two examples of implicit parallelism are with domain-specific languages where the concurrency within high-level operations is prescribed, and with functional programming languages because the absence of side-effects allows non-dependent functions to be executed in parallel. However, this kind of parallelism is difficult to manage and functional languages such as Concurrent Haskell and Concurrent ML provide features to manage parallelism explicitly and correctly.

### Problem decomposition

A parallel program is composed of simultaneously executing processes. Problem decomposition relates to the way in which the constituent processes are formulated.

#### Task parallelism

A task-parallel model focuses on processes, or threads of execution. These processes will often be behaviourally distinct, which emphasises the need for communication. Task parallelism is a natural way to express message-passing communication. In Flynn's taxonomy, task parallelism is usually classified as MIMD/MPMD or MISD.

#### Data parallelism

A data-parallel model focuses on performing operations on a data set, typically a regularly structured array. A set of tasks will operate on this data, but independently on disjoint partitions. In Flynn's taxonomy, data parallelism is usually classified as MIMD/SPMD or SIMD.

#### Stream Parallelism

Stream parallelism, also known as pipeline parallelism, focuses on dividing a computation into a sequence of stages, where each stage processes a portion of the input data. Each stage operates independently and concurrently, and the output of one stage serves as the input to the next stage. Stream parallelism is particularly suitable for applications with continuous data streams or pipelined computations.

#### Implicit parallelism

As with implicit process interaction, an implicit model of parallelism reveals nothing to the programmer as the compiler, the runtime or the hardware is responsible. For example, in compilers, automatic parallelization is the process of converting sequential code into parallel code, and in computer architecture, superscalar execution is a mechanism whereby instruction-level parallelism is exploited to perform operations in parallel.

## Terminology

Parallel programming models are closely related to models of computation. A model of parallel computation is an abstraction used to analyze the cost of computational processes, but it does not necessarily need to be practical, in that it can be implemented efficiently in hardware and/or software. A programming model, in contrast, does specifically imply the practical considerations of hardware and software implementation.

A parallel programming language may be based on one or a combination of programming models. For example, High Performance Fortran is based on shared-memory interactions and data-parallel problem decomposition, and Go provides mechanism for shared-memory and message-passing interaction.

## Example parallel programming models

| Name | Class of interaction | Class of decomposition | Example implementations |
|---|---|---|---|
| Actor model | Asynchronous message passing | Task | D, Erlang, Scala, SALSA |
| Bulk synchronous parallel | Shared memory | Task | Apache Giraph, Apache Hama, BSPlib |
| Communicating sequential processes | Synchronous message passing | Task | Ada, Occam, VerilogCSP, Go |
| Circuits | Message passing | Task | Verilog, VHDL |
| Dataflow | Message passing | Task | Lustre, TensorFlow, Apache Flink |
| Functional | Message passing | Task | Concurrent Haskell, Concurrent ML |
| LogP machine | Synchronous message passing | Not specified | None |
| Parallel random access machine | Shared memory | Data | Cilk, CUDA, OpenMP, Threading Building Blocks, XMTC |
| SPMD PGAS | Partitioned global address space | Data | Fortran 2008, Unified Parallel C, UPC++, SHMEM |
| Global-view Task parallelism | Partitioned global address space | Task | Chapel, X10 |
