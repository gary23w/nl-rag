---
title: "Thread pool"
source: https://en.wikipedia.org/wiki/Thread_pool
domain: concurrency-patterns
license: CC-BY-SA-4.0
tags: thread pool, lock-free, compare-and-swap, coroutine, synchronization primitive, atomic operation
fetched: 2026-07-02
---

# Thread pool

In computer programming, a **thread pool** is a software design pattern for achieving concurrency of execution in a computer program. Often also called a **replicated workers** or **worker-crew model**, a thread pool maintains multiple threads waiting for tasks to be allocated for concurrent execution by the supervising program. By maintaining a pool of threads, the model increases performance and avoids latency in execution due to frequent creation and destruction of threads for short-lived tasks. Another good property - the ability to limit system load, when we use fewer threads than available. The number of available threads is tuned to the computing resources available to the program, such as a parallel task queue after completion of execution.

## Performance

The size of a thread pool is the number of threads kept in reserve for executing tasks. It is usually a tuneable parameter of the application, adjusted to optimize program performance. Deciding the optimal thread pool size is crucial to optimize performance.

One benefit of a thread pool over creating a new thread for each task is that thread creation and destruction overhead is restricted to the initial creation of the pool, which may result in better performance and better system stability. Creating and destroying a thread and its associated resources can be an expensive process in terms of time. An excessive number of threads in reserve, however, wastes memory, and context-switching between the runnable threads invokes performance penalties. A socket connection to another network host, which might take many CPU cycles to drop and re-establish, can be maintained more efficiently by associating it with a thread that lives over the course of more than one network transaction.

Using a thread pool may be useful even putting aside thread startup time. There are implementations of thread pools that make it trivial to queue up work, control concurrency and sync threads at a higher level than can be done easily when manually managing threads. In these cases the performance benefits of use may be secondary.

Typically, a thread pool executes on a single computer. However, thread pools are conceptually related to server farms in which a master process, which might be a thread pool itself, distributes tasks to worker processes on different computers, in order to increase the overall throughput. Embarrassingly parallel problems are highly amenable to this approach.

The number of threads may be dynamically adjusted during the lifetime of an application based on the number of waiting tasks. For example, a web server can add threads if numerous web page requests come in and can remove threads when those requests taper down. The cost of having a larger thread pool is increased resource usage. The algorithm used to determine when to create or destroy threads affects the overall performance:

- Creating too many threads wastes resources and costs time creating the unused threads.
- Destroying too many threads requires more time later when creating them again.
- Creating threads too slowly might result in poor client performance (long wait times).
- Destroying threads too slowly may starve other processes of resources.

## In languages

In bash implemented by `--max-procs` / `-P` in xargs, for example:

```mw
# Fetch 5 URLs in parallel
urls=(
    "https://example.com/file1.txt"
    "https://example.com/file2.txt"
    "https://example.com/file3.txt"
    "https://example.com/file4.txt"
    "https://example.com/file5.txt"
)

printf '%s\n' "${urls[@]}" | xargs -P 5 -I {} curl -sI {} | grep -i "content-length:"
```

In Go, called worker pool:

```mw
package main

import (
    "fmt"
    "time"
)

func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        fmt.Println("worker", id, "started  job", j)
        time.Sleep(time.Second)
        fmt.Println("worker", id, "finished job", j)
        results <- j * 2
    }
}

func main() {
    const numJobs = 5
    jobs := make(chan int, numJobs)
    results := make(chan int, numJobs)

    for w := 1; w <= 3; w++ {
        go worker(w, jobs, results)
    }

    for j := 1; j <= numJobs; j++ {
        jobs <- j
    }
    close(jobs)

    for a := 1; a <= numJobs; a++ {
        <-results
    }
}
```

It will print:

```mw
$ time go run worker-pools.go 
worker 1 started  job 1
worker 2 started  job 2
worker 3 started  job 3
worker 1 finished job 1
worker 1 started  job 4
worker 2 finished job 2
worker 2 started  job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real    0m2.358s
```
