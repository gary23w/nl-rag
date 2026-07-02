---
title: "crossbeam"
source: https://docs.rs/crossbeam/latest/crossbeam/
domain: crossbeam-rust
license: CC-BY-SA-4.0
tags: crossbeam concurrency, rust lock-free, concurrent channels rust, crossbeam channel
fetched: 2026-07-02
---

# Crate crossbeam

Source

Expand description

Tools for concurrent programming.

### §Atomics

- `AtomicCell`, a thread-safe mutable memory location.
- `AtomicConsume`, for reading from primitive atomic types with “consume” ordering.

### §Data structures

- `deque`, work-stealing deques for building task schedulers.
- `ArrayQueue`, a bounded MPMC queue that allocates a fixed-capacity buffer on construction.
- `SegQueue`, an unbounded MPMC queue that allocates small buffers, segments, on demand.

### §Memory management

- `epoch`, an epoch-based garbage collector.

### §Thread synchronization

- `channel`, multi-producer multi-consumer channels for message passing.
- `Parker`, a thread parking primitive.
- `ShardedLock`, a sharded reader-writer lock with fast concurrent reads.
- `WaitGroup`, for synchronizing the beginning or end of some computation.

### §Utilities

- `Backoff`, for exponential backoff in spin loops.
- `CachePadded`, for padding and aligning a value to the length of a cache line.
- `scope`, for spawning threads that borrow local variables from the stack.

## Modules

**atomic**

Atomic types.

**channel**

Multi-producer multi-consumer channels for message passing.

**deque**

Concurrent work-stealing deques.

**epoch**

Epoch-based memory reclamation.

**queue**

Concurrent queues.

**sync**

Thread synchronization primitives.

**thread**

Threads that can borrow variables from the stack.

**utils**

Miscellaneous utilities.

## Macros

**select**

Selects from a set of channel operations.

## Functions

**scope**

Creates a new scope for spawning threads.
