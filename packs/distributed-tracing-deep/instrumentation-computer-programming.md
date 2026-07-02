---
title: "Instrumentation (computer programming)"
source: https://en.wikipedia.org/wiki/Instrumentation_(computer_programming)
domain: distributed-tracing-deep
license: CC-BY-SA-4.0
tags: distributed tracing, span context propagation, trace sampling, request correlation
fetched: 2026-07-02
---

# Instrumentation (computer programming)

In computer programming, **instrumentation** is the act of modifying software so that analysis can be performed on it.

Generally, instrumentation either modifies source code or binary code. Execution environments like the JVM provide separate interfaces to add instrumentation to program executions, such as the JVMTI, which enables instrumentation during program start.

Instrumentation enables profiling: measuring dynamic behavior during a test run. This is useful for properties of a program that cannot be analyzed statically with sufficient precision, such as performance and alias analysis.

Instrumentation can include:

- Logging events such as failures and operation start and end
- Measuring and logging the duration of operations

## Limitations

Instrumentation is limited by execution coverage. If the program never reaches a particular point of execution, then instrumentation at that point collects no data. For instance, if a word processor application is instrumented, but the user never activates the print feature, then the instrumentation can say nothing about the routines which are used exclusively by the printing feature.

Instrumentation increases the execution time of a program. In some contexts, this increase might be dramatic and hence limit the application of instrumentation to debugging contexts. The instrumentation overhead differs depending on the used instrumentation technology.
