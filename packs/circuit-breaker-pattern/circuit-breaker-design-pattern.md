---
title: "Circuit breaker design pattern"
source: https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern
domain: circuit-breaker-pattern
license: CC-BY-SA-4.0
tags: circuit breaker pattern, fault tolerance resilience, cascading failure prevention, bulkhead isolation pattern
fetched: 2026-07-02
---

# Circuit breaker design pattern

The **Circuit Breaker** is a design pattern commonly used in software development to improve system resilience and fault tolerance. Circuit breaker pattern can prevent cascading failures particularly in distributed systems. In distributed systems, the Circuit Breaker pattern can be used to monitor service health and can detect failures dynamically. Unlike timeout-based methods, which can lead to delayed error responses or the premature failure of healthy requests, the Circuit Breaker pattern can proactively identify unresponsive services and can prevent repeated attempts. This approach can enhance the user experience.

The circuit breaker pattern can be used in conjunction with other patterns, such as retry, fallback, and timeout, to enhance fault tolerance in systems.

## Challenges

According to Marc Brooker, circuit breakers can misinterpret a partial failure as total system failure and inadvertently bring down the entire system. In particular, sharded systems and cell-based architectures are vulnerable to this issue. A workaround is that the server indicates to the client which specific part is overloaded and the client uses a corresponding mini circuit breaker. However, this workaround can be complex and expensive.

## Different states of circuit breaker

- Closed
- Open
- Half-open

### Closed state

When everything is normal, the circuit breakers remain *closed*, and all the requests pass through to the services. If the number of failures increases beyond the threshold, the circuit breaker trips and goes into an *open* state.

### Open state

In this state circuit breaker returns an error immediately without even invoking the services. The Circuit breakers move into the *half-open* state after a timeout period elapses. Usually, it will have a monitoring system where the timeout will be specified.

### Half-open state

In this state, the circuit breaker allows a limited number of requests from the service to pass through and invoke the operation. If the requests are successful, then the circuit breaker will go to the *closed* state. However, if the requests continue to fail, then it goes back to *open* state.
