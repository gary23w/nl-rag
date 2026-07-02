---
title: "CPU time"
source: https://en.wikipedia.org/wiki/CPU_time
domain: use-method
license: CC-BY-SA-4.0
tags: utilization saturation errors, resource driven analysis, system performance checklist, bottleneck diagnosis
fetched: 2026-07-02
---

# CPU time

**CPU time** (or **process time**) is the amount of time that a central processing unit (CPU) was used for processing a specific set of instructions of a computer program or operating system, as opposed to *total* time from start to finish, where the CPU might have spent time on *other* processes. See the figure. CPU time is measured in clock ticks or seconds. Sometimes it is useful to convert CPU time into a percentage of the CPU capacity, giving the **CPU usage**.

Measuring CPU time for two functionally identical programs that process identical inputs can indicate which program is faster, but it is a common misunderstanding that CPU time can be used to compare *algorithms*. Comparing programs by their CPU time compares specific *implementations* of algorithms. (It is possible to have both efficient and inefficient implementations of the same algorithm.) Algorithms are more commonly compared using measures of time complexity and space complexity.

Typically, the CPU time used by a program is measured by the operating system, which schedules all of the work of the CPU. Modern multitasking operating systems run hundreds of processes. (A process is a running program.) Upon starting a process, the operating system records the time using an internal timer. When the process is suspended or terminated, the operating system again records the time. The total time that a process spent running is its CPU time, as shown in the figure.

## User and System time

The process "accounting" done by the Unix family of operating systems includes two components of **CPU time**. User time and System time reflect the fact that most programs make requests to the operating system while they execute. Input/output operations, such as reading a file or writing to the screen, are done by issuing requests to the operating system, possibly through system calls. I/O and other operations performed by the operating system on behalf of a process constitute system time.

- **User time** is the amount of time the CPU is busy executing code in user space.
- **System time** is the amount of time the CPU is busy executing code in kernel space. This value represents the amount of time the kernel performs work on behalf of the executing process.

Other operating systems such as Microsoft Windows similarly has separate accounting for "kernel time", which is a very similar concept as "system time".

In contrast, elapsed real time (or simply real time, or wall-clock time) is the time taken from the start of a computer program until the end as measured by an ordinary clock. Elapsed real time includes User time, System time, plus time that the process was not running for any reason, such as when its execution was preempted.

## Unix commands for CPU time

### Unix command *top*

The Unix command top provides CPU time, priority, elapsed real time, and other information for all processes and updates it in real time.

### Unix command *time*

The Unix command time prints CPU time and elapsed real time for the execution of a Unix command (or pipeline). Note that many command-line shells have their own implementation of this command. To run the Unix program **`time`**, we provide its full path, **`/usr/bin/time`**:

```mw
$ gcc nextPrimeNumber.c -o nextPrimeNumber -lm
$ /usr/bin/time ./nextPrimeNumber 300000070034
Prime number greater than 300000070034 is 300000070043
        0.01user 0.00system 0:00.01elapsed 100%CPU
$
```

This process took a total of 0.02 seconds of CPU time (User + System). The reported System time is 0.00 seconds, indicating that the amount of System time used was less than the printed resolution of 0.01 seconds. Elapsed real time was 0.08 seconds.

The following is the source code of the application nextPrimeNumber which was used in the above example.

```mw
// nextPrimeNumber.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int isPrimeNumber(unsigned long int n) {
    unsigned long int limit = ceil(sqrt(n));
    for (int i = 2; i <= limit ; ++i)
        if (n % i == 0) return 0;
    return 1;
}

int main(int argc, char *argv[]) {
    unsigned long int argument = strtoul(argv[1], NULL, 10), n = argument;
    while (!isPrimeNumber(++n));

    printf("Prime number greater than %lu is %lu\n", argument, n);
    return 0;
}
```

## Functions to get CPU time

Modern CPUs have several clocks and counters, such as the Time Stamp Counter, the High Precision Event Timer, and the Real-time Clock, each with a specialized use. When a program wants to time its own operation, it can use a function like the POSIX **`clock()`** function, which returns the **CPU time** used by the program. POSIX allows this clock to start at an arbitrary value, so to measure elapsed time, a program calls **`clock()`**, does some work, then calls **`clock()`** again. The difference is the time needed to do the work.

The POSIX function **`getrusage()`** returns more than just the CPU time consumed by a process in a POSIX environment. It returns many measurements of a process, often including approximate memory usage and Context switch (scheduling) event counts. Functionality varies across operating systems.

## Total CPU time

On multi-processor and multi-core machines, a program can use two or more processors simultaneously in what is called parallel processing. In such situations, a measure of *total CPU time* is useful, which is the sum of CPU time consumed by all of the processors utilized by the program.

## CPU time and elapsed real time

In computing, **elapsed real time**, **real time**, **wall-clock time**, **wall time**, or **walltime** is the actual time taken from the start of a computer program to the end. In other words, it is the difference between the time at which a task finishes and the time at which the task started. Wall time is thus different from CPU time, which measures only the time during which the processor is actively working on a certain task or process. The difference between the two can arise from architecture and run-time dependent factors, e.g. programmed delays or waiting for system resources to become available.

Elapsed real time is always greater than or equal to the CPU time for computer programs which use only one CPU for processing. If no waiting occurs, such as for I/O, and the program's execution is never preempted, elapsed real time and CPU time will be virtually identical.

### CPU time and elapsed real time for parallel processing

If a program uses parallel processing, total CPU time for that program is typically more than its elapsed real time. For a program that is able to evenly divide its work across two processors with no overhead in doing so, the value (Total CPU time)/(Number of processors) will be virtually identical to elapsed real time. Here, a *processor* may be a (single-core) CPU or one core in a multi-core CPU.

Example: A software application executed on a four-core processor creates four Unix processes. If each process is able to execute on a separate processor core, computation proceeds on four processor cores simultaneously. The total CPU time would be, ideally, four times the elapsed real time.

In reality, parallel processing rarely achieves a linear speedup, where the amount of computation per unit time scales up with the number of processors in use. Some embarrassingly parallel problems admit such solutions, but for most, additional work is required to divide up the computation when the program starts, and to combine the results from each processor at the end. The additional work adds to the total CPU time. Frequently, a process finds itself waiting for data from another process before it can continue, which also adds to the total time.
