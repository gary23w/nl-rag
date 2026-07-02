---
title: "What is BullMQ"
source: https://docs.bullmq.io/
domain: bullmq-queue
license: CC-BY-SA-4.0
tags: bullmq queue, redis job queue, background job processing, worker task scheduler
fetched: 2026-07-02
---

# What is BullMQ

For the complete documentation index, see

llms.txt

. This page is also available as

Markdown

.

# What is BullMQ

General description of BullMQ and its features

BullMQ is a library that implements a fast and robust queue system built on top of that helps in resolving many modern age micro-services architectures.

The library is designed so that it will fulfill the following goals:

- Exactly once queue semantics, i.e., attempts to deliver every message exactly one time, but it will deliver at least once in the worst case scenario*.
- Easy to scale horizontally. Add more workers for processing jobs in parallel.
- Consistent.
- High performant. Try to get the highest possible throughput from Redis by combining efficient .lua scripts and pipelining.

View the repository, see open issues, and contribute back !

## **Features**

If you are new to Message Queues, you may wonder why they are needed after all. Queues can solve many different problems in an elegant way, from smoothing out processing peaks to creating robust communication channels between micro-services or offloading heavy work from one server to many smaller workers, and many other use cases. Check the section for getting some inspiration and information about best practices.

### Used by

BullMQ is used by many organizations big and small, here are some notable examples:

Next

Quick Start

Last updated 1 year ago

Was this helpful?
