---
title: "Multi-stage programming"
source: https://en.wikipedia.org/wiki/Multi-stage_programming
domain: terra-language
license: CC-BY-SA-4.0
tags: terra language, lua language, multi stage programming, llvm backend, ahead of time compilation
fetched: 2026-07-02
---

# Multi-stage programming

**Multi-stage programming** (**MSP**) is a variety of metaprogramming in which compilation is divided into a series of intermediate phases, allowing typesafe run-time code generation. Statically defined types are used to verify that dynamically constructed types are valid and do not violate the type system.

In MSP languages, expressions are qualified by notation that specifies the phase at which they are to be evaluated. By allowing the specialization of a program at run-time, MSP can optimize the performance of programs: it can be considered as a form of partial evaluation that performs computations at compile-time as a trade-off to increase the speed of run-time processing.

Multi-stage programming languages support constructs similar to the Lisp construct of quotation and `eval`, except that scoping rules are taken into account.
