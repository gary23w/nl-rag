---
title: "Task parallelism"
source: https://en.wikipedia.org/wiki/Task_parallelism
domain: grand-central-dispatch
license: CC-BY-SA-4.0
tags: grand central dispatch, dispatch queue, thread pool, task parallelism
fetched: 2026-07-02
---

# Task parallelism

**Task parallelism** (also known as **function parallelism** and **control parallelism**) is a form of parallelization of computer code across multiple processors in parallel computing environments. Task parallelism focuses on distributing tasks—concurrently performed by processes or threads—across different processors. In contrast to data parallelism which involves running the same task on different components of data, task parallelism is distinguished by running many different tasks at the same time on the same data. A common type of task parallelism is pipelining, which consists of moving a single set of data through a series of separate tasks where each task can execute independently of the others.

## Description

In a multiprocessor system, task parallelism is achieved when each processor executes a different thread (or process) on the same or different data. The threads may execute the same or different code. In the general case, different execution threads communicate with one another as they work, but this is not a requirement. Communication usually takes place by passing data from one thread to the next as part of a workflow.

As a simple example, if a system is running code on a 2-processor system (CPUs "a" & "b") in a parallel environment and we wish to do tasks "A" and "B", it is possible to tell CPU "a" to do task "A" and CPU "b" to do task "B" simultaneously, thereby reducing the run time of the execution. The tasks can be assigned using conditional statements as described below.

Task parallelism emphasizes the distributed (parallelized) nature of the processing (i.e. threads), as opposed to the data (data parallelism). Most real programs fall somewhere on a continuum between task parallelism and data parallelism.

**Thread-level parallelism** (**TLP**) is the parallelism inherent in an application that runs multiple threads at once. This type of parallelism is found largely in applications written for commercial servers such as databases. By running many threads at once, these applications are able to tolerate the high amounts of I/O and memory system latency their workloads can incur - while one thread is delayed waiting for a memory or disk access, other threads can do useful work.

The exploitation of thread-level parallelism has also begun to make inroads into the desktop market with the advent of multi-core microprocessors. This has occurred because, for various reasons, it has become increasingly impractical to increase either the clock speed or instructions per clock of a single core. If this trend continues, new applications will have to be designed to utilize multiple threads in order to benefit from the increase in potential computing power. This contrasts with previous microprocessor innovations in which existing code was automatically sped up by running it on a newer/faster computer.

## Example

The pseudocode below illustrates task parallelism:

```
program:
...
if CPU = "a" then
    do task "A"
else if CPU="b" then
    do task "B"
end if
...
end program
```

The goal of the program is to do some net total task ("A+B"). If we write the code as above and launch it on a 2-processor system, then the runtime environment will execute it as follows.

- In an SPMD (single program, multiple data) system, both CPUs will execute the code.
- In a parallel environment, both will have access to the same data.
- The "if" clause differentiates between the CPUs. CPU "a" will read true on the "if" and CPU "b" will read true on the "else if", thus having their own task.
- Now, both CPU's execute separate code blocks simultaneously, performing different tasks simultaneously.

Code executed by CPU "a":

```
program:
...
do task "A"
...
end program
```

Code executed by CPU "b":

```
program:
...
do task "B"
...
end program
```

This concept can now be generalized to any number of processors.

## Language support

Task parallelism can be supported in general-purpose languages by either built-in facilities or libraries. Notable examples include:

- Ada: Tasks (built-in)
- C++ (Intel): Threading Building Blocks
- C++ (Intel): Cilk Plus
- C++ (Open Source/Apache 2.0): RaftLib
- C, C++, Objective-C, Swift (Apple): Grand Central Dispatch
- D: tasks and fibers
- Delphi (System.Threading.TParallel)
- Go: goroutines
- Java: Java concurrency
- .NET: Task Parallel Library

Examples of fine-grained task-parallel languages can be found in the realm of Hardware Description Languages like Verilog and VHDL.
