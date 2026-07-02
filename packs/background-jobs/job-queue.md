---
title: "Job queue"
source: https://en.wikipedia.org/wiki/Job_queue
domain: background-jobs
license: CC-BY-SA-4.0
tags: background jobs, job queue, scheduled task, batch processing
fetched: 2026-07-02
---

# Job queue

In system software, a **job queue** (a.k.a. **batch queue**, **input queue**), is a data structure maintained by job scheduler software containing jobs to run.

Users submit their programs that they want executed, "jobs", to the queue for batch processing. The scheduler software maintains the queue as the pool of jobs available for it to run.

Multiple batch queues might be used by the scheduler to differentiate types of jobs depending on parameters such as:

- job priority
- estimated execution time
- resource requirements

The use of a batch queue gives these benefits:

- sharing of computer resources among many users
- time-shifts job processing to when the computer is less busy
- avoids idling the compute resources without minute-by-minute human supervision
- allows around-the-clock high utilization of expensive computing resources

Any process that comes to the CPU should wait in a queue.
