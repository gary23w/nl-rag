---
title: "Job scheduler"
source: https://en.wikipedia.org/wiki/Job_scheduler
domain: gcp-cloud-scheduler
license: CC-BY-SA-4.0
tags: gcp cloud scheduler, managed cron gcp, job scheduling gcp, cron as a service
fetched: 2026-07-02
---

# Job scheduler

A **job scheduler** is a computer application for controlling unattended background program execution of jobs. This is commonly called **batch scheduling**, as execution of non-interactive jobs is often called batch processing, though traditional *job* and *batch* are distinguished and contrasted; see that page for details. Other synonyms include **batch system**, **distributed resource management system** (**DRMS**), **distributed resource manager** (**DRM**), and, commonly today, **workload automation** (**WLA**). The data structure of jobs to run is known as the job queue.

Modern job schedulers typically provide a graphical user interface and a single point of control for definition and monitoring of background executions in a distributed network of computers. Increasingly, job schedulers are required to orchestrate the integration of real-time business activities with traditional background IT processing across different operating system platforms and business application environments.

*Job scheduling* should not be confused with process scheduling, which is the assignment of currently running processes to CPUs by the operating system.

## Overview

Basic features expected of job scheduler software include:

- interfaces which help to define workflows and/or job dependencies
- automatic submission of executions
- interfaces to monitor the executions
- priorities and/or queues to control the execution order of unrelated jobs

If software from a completely different area includes all or some of those features, this software can be considered to have job scheduling capabilities.

Most operating systems, such as Unix and Windows, provide basic job scheduling capabilities, notably by at and batch, cron, and the Windows Task Scheduler. Web hosting services provide job scheduling capabilities through a control panel or a webcron solution. Many programs such as DBMS, backup, ERPs, and BPM also include relevant job-scheduling capabilities. Operating system ("OS") or point program supplied job-scheduling will not usually provide the ability to schedule beyond a single OS instance or outside the remit of the specific program. Organizations needing to automate unrelated IT workload may also leverage further advanced features from a job scheduler, such as:

- real-time scheduling based on external, unpredictable events
- automatic restart and recovery in event of failures
- alerting and notification to operations personnel
- generation of incident reports
- audit trails for regulatory compliance purposes

These advanced capabilities can be written by in-house developers but are more often provided by suppliers who specialize in systems-management software.

## Main concepts

There are many concepts that are central to almost every job scheduler implementation and that are widely recognized with minimal variations: jobs, dependencies, job streams, and users.

Beyond the basic, single OS instance scheduling tools there are two major architectures that exist for Job Scheduling software.

- Master/Agent architecture — the historic architecture for job scheduling software. The job scheduling software is installed on a single machine (Master), while on production machines only a very small component (Agent) is installed that awaits commands from the Master, executes them, then returns the exit code back to the Master.
- Cooperative architecture — a decentralized model where each machine is capable of helping with scheduling and can offload locally scheduled jobs to other cooperating machines. This enables dynamic workload balancing to maximize hardware resource utilization and high availability to ensure service delivery.

## History

Job scheduling has a long history. Job schedulers have been one of the major components of IT infrastructure since the early mainframe systems. At first, stacks of punched cards were processed one after the other, hence the term "batch processing".

From a historical point of view, we can distinguish two main eras about Job schedulers:

1. The mainframe era
  - Job Control Language (JCL) on IBM mainframes. Initially based on JCL functionality to handle dependencies, this era is typified by the development of sophisticated scheduling solutions (such as Job Entry Subsystem 2/3) forming part of the systems management and automation toolset on the mainframe.
2. The open systems era
  - Modern schedulers on a variety of architectures and operating systems. With standard scheduling tools limited to commands such as at and batch, the need for mainframe standard job schedulers has grown with the increased adoption of distributed computing environments.

In terms of the type of scheduling, there are also distinct eras:

1. Batch processing - the traditional date and time based execution of background tasks based on a defined period during which resources were available for batch processing (the batch window). In effect, the original mainframe approach transposed onto the open systems environment.
2. Event-driven process automation - where background processes cannot be simply run at a defined time, either because the nature of the business demands that workload is based on the occurrence of external events (such as the arrival of an order from a customer or a stock update from a store branch), or because there is no / insufficient batch window.
3. Service Oriented job scheduling - recent developments in Service Oriented Architecture (SOA) have seen a move towards deploying job scheduling as a reusable IT infrastructure service that can play a role in the integration of existing business application workload with new Web Services based real-time applications.

## Scheduling

Various schemes are used to decide which particular job to run. Parameters that might be considered include:

- Job priority
- Computer resource availability
- License key if job is using licensed software
- Execution time allocated to user
- Number of simultaneous jobs allowed for a user
- Estimated execution time
- Elapsed execution time
- Availability of peripheral devices
- Occurrence of prescribed events
- Job dependency
- File dependency
- Operator prompt dependency
