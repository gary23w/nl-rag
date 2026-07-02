---
title: "Idle (CPU)"
source: https://en.wikipedia.org/wiki/Idle_(CPU)
domain: requestidlecallback
license: CC-BY-SA-4.0
tags: request idle callback, idle period scheduling, background task deadline, cooperative task chunking
fetched: 2026-07-02
---

# Idle (CPU)

**Idle** is a state that a computer processor is in when it is not being used by any program.

Every program or task that runs on a computer system occupies a certain amount of processing time on the CPU. If the CPU has completed all tasks it is idle.

Modern processors use idle time to save power. Common methods are reducing the clock speed along with the CPU voltage and sending parts of the processor into a sleep state. On processors that have a halt instruction that stops the CPU until an interrupt occurs, such as x86's HLT instruction, it may save significant amounts of power and heat if the idle task consists of a loop which repeatedly executes that instruction.

Many operating systems, for example Windows, Linux, and macOS will run an **idle task**, which is a special task loaded by the OS scheduler on a CPU when there is nothing for the CPU to do. The idle task can be hard-coded into the scheduler, or it can be implemented as a separate task with the lowest possible priority. An advantage of the latter approach is that programs monitoring the system status can see the idle task along with all other tasks; an example is Windows NT's System Idle Process.

Some programs are designed to appear to make use of CPU idle time, meaning that they run at a low priority (but slightly higher than idle priority) so as not to impact programs that run at normal priority. This allows non-crucial background programs to only run when it would not affect the performance of other applications.
