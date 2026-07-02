---
title: "pthreads"
source: https://en.wikipedia.org/wiki/POSIX_Threads
domain: autosar-adaptive
license: CC-BY-SA-4.0
tags: autosar adaptive, adaptive platform, posix automotive, service-oriented vehicle
fetched: 2026-07-02
---

# pthreads

(Redirected from

POSIX Threads

)

In computing, **POSIX Threads**, commonly known as **pthreads** (after its header **<pthread.h>**), is an execution model that exists independently from a programming language, as well as a parallel execution model. It allows a program to control multiple different flows of work that overlap in time. Each flow of work is referred to as a *thread*, and creation and control over these flows is achieved by making calls to the POSIX Threads API. POSIX Threads is an API defined by the Institute of Electrical and Electronics Engineers (IEEE) standard *POSIX.1c, Threads extensions (IEEE Std 1003.1c-1995)*.

Implementations of the API are available on many Unix-like POSIX-conformant operating systems such as FreeBSD, NetBSD, OpenBSD, Linux, macOS, Android, Solaris, Redox, QNX, and AUTOSAR Adaptive, typically bundled as a library **libpthread**. DR-DOS and Microsoft Windows implementations also exist: within the SFU/SUA subsystem which provides a native implementation of a number of POSIX APIs, and also within third-party packages such as *pthreads-w32*, which implements pthreads on top of existing Windows API.

pthreads defines a set of C programming language types, functions and constants. It is implemented with a `pthread.h` header and a thread library.

There are around 100 threads procedures, all prefixed `pthread_` and they can be categorized into five groups:

- Thread management – creating, joining threads etc.
- Mutexes
- Condition variables
- Synchronization between threads using read write locks and barriers
- Spinlocks

The POSIX semaphore API works with POSIX threads but is not part of the threads standard, having been defined in the *POSIX.1b, Real-time extensions (IEEE Std 1003.1b-1993)* standard. Consequently, the semaphore procedures are prefixed by `sem_` instead of `pthread_`.

## Example

An example illustrating the use of pthreads in C:

```mw
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_THREADS 5

void* perform_work(void* arguments){
    int index = *((int*)arguments);
    int sleep_time = 1 + rand() % NUM_THREADS;
    printf("Thread %d: Started.\n", index);
    printf("Thread %d: Will be sleeping for %d seconds.\n", index, sleep_time);
    sleep(sleep_time);
    printf("Thread %d: Ended.\n", index);
    return NULL;
}

int main(void) {
    pthread_t threads[NUM_THREADS];
    int thread_args[NUM_THREADS];
    int result_code;
  
    //create all threads one by one
    for (int i = 0; i < NUM_THREADS; i++) {
        printf("In main: Creating thread %d.\n", i);
        thread_args[i] = i;
        result_code = pthread_create(&threads[i], NULL, perform_work, &thread_args[i]);
        assert(!result_code);
    }

    printf("In main: All threads are created.\n");

    // wait for each thread to complete
    for (int i = 0; i < NUM_THREADS; i++) {
        result_code = pthread_join(threads[i], NULL);
        assert(!result_code);
        printf("In main: Thread %d has ended.\n", i);
    }

    printf("Main program has ended.\n");
    return 0;
}
```

This program creates five threads, each executing the function *perform_work* that prints the unique number of this thread to standard output. If a programmer wanted the threads to communicate with each other, this would require defining a variable outside of the scope of any of the functions, making it a global variable. This program can be compiled using the gcc compiler with the following command:

```
gcc pthreads_demo.c -pthread -o pthreads_demo
```

Here is one of the many possible outputs from running this program.

```mw
In main: Creating thread 0.
In main: Creating thread 1.
In main: Creating thread 2.
In main: Creating thread 3.
Thread 0: Started.
In main: Creating thread 4.
Thread 3: Started.
Thread 2: Started.
Thread 0: Will be sleeping for 3 seconds.
Thread 1: Started.
Thread 1: Will be sleeping for 5 seconds.
Thread 2: Will be sleeping for 4 seconds.
Thread 4: Started.
Thread 4: Will be sleeping for 1 seconds.
In main: All threads are created.
Thread 3: Will be sleeping for 4 seconds.
Thread 4: Ended.
Thread 0: Ended.
In main: Thread 0 has ended.
Thread 2: Ended.
Thread 3: Ended.
Thread 1: Ended.
In main: Thread 1 has ended.
In main: Thread 2 has ended.
In main: Thread 3 has ended.
In main: Thread 4 has ended.
Main program has ended.
```

## POSIX Threads for Windows

Windows does not support the pthreads standard natively; therefore, the Pthreads4w project seeks to provide a portable and open-source wrapper implementation. It can also be used to port Unix software (which uses pthreads) with little or no modification to the Windows platform. Pthreads4w version 3.0.0 or later, released under the Apache Public License v2.0, is compatible with 64-bit or 32-bit Windows systems. Version 2.11.0, released under the LGPLv3 license, is also 64-bit or 32-bit compatible.

The Mingw-w64 project also contains a wrapper implementation of 'pthreads, **winpthreads**, which tries to use more native system calls than the Pthreads4w project.

Interix environment subsystem available in the Windows Services for UNIX/Subsystem for UNIX-based Applications package provides a native port of the pthreads API, i.e. not mapped on Win32 API but built directly on the operating system syscall interface.
