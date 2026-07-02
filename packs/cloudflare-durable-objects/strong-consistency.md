---
title: "Strong consistency"
source: https://en.wikipedia.org/wiki/Strong_consistency
domain: cloudflare-durable-objects
license: CC-BY-SA-4.0
tags: cloudflare durable objects, durable objects, stateful edge, actor model
fetched: 2026-07-02
---

# Strong consistency

**Strong consistency** is one of the consistency models used in the domain of concurrent programming (e.g., in distributed shared memory, distributed transactions).

The protocol is said to support strong consistency if:

1. All accesses are seen by all parallel processes (or nodes, processors, etc.) in the same order (sequentially)

Therefore, only one consistent state can be observed, as opposed to weak consistency, where different parallel processes (or nodes, etc.) can perceive variables in different states.
