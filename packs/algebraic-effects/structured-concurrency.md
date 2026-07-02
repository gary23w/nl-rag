---
title: "Structured concurrency"
source: https://en.wikipedia.org/wiki/Structured_concurrency
domain: algebraic-effects
license: CC-BY-SA-4.0
tags: algebraic effect, effect handler, delimited continuation, one-shot continuation
fetched: 2026-07-02
---

# Structured concurrency

**Structured concurrency** is a programming paradigm aimed at improving the clarity, quality, and development time of a computer program by using a structured approach to concurrent programming.

The core concept is the encapsulation of concurrent threads of execution (here encompassing kernel and userland threads and processes) by way of control flow constructs that have clear entry and exit points and that ensure all spawned threads have completed before exit. Such encapsulation allows errors in concurrent threads to be propagated to the control structure's parent scope and managed by the native error handling mechanisms of each particular computer language. It allows control flow to remain readily evident by the structure of the source code despite the presence of concurrency. To be effective, this model must be applied consistently throughout all levels of the program – otherwise concurrent threads may leak out, become orphaned, or fail to have runtime errors correctly propagated.

Structured concurrency is analogous to structured programming, which uses control flow constructs that encapsulate sequential statements and subroutines.

## History

The fork–join model from the 1960s, embodied by multiprocessing tools like OpenMP, is an early example of a system ensuring all threads have completed before exit. However, Smith argues that this model is not true structured concurrency as the programming language is unaware of the joining behavior, and is thus unable to enforce safety.

The concept was formulated in 2016 by Martin Sústrik (a developer of ZeroMQ) with his C library libdill, with goroutines as a starting point. It was further refined in 2017 by Nathaniel J. Smith, who introduced a "nursery pattern" in his Python implementation called Trio. Meanwhile, Roman Elizarov independently came upon the same ideas while developing an experimental coroutine library for the Kotlin language, which later became a standard library.

In 2021, Swift adopted structured concurrency. Later that year, a draft proposal was published to add structured concurrency to Java.

## Variations

A major point of variation is how an error in one member of a concurrent thread tree is handled. Simple implementations will merely wait until the children and siblings of the failing thread run to completion before propagating the error to the parent scope. However, that could take an indefinite amount of time. The alternative is to employ a general cancellation mechanism (typically a cooperative scheme allowing program invariants to be honored) to terminate the children and sibling threads in an expedient manner.
