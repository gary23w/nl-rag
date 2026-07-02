---
title: "Partial evaluation"
source: https://en.wikipedia.org/wiki/Partial_evaluation
domain: partial-evaluation
license: CC-BY-SA-4.0
tags: partial evaluation, program specialization, binding-time analysis, futamura projection
fetched: 2026-07-02
---

# Partial evaluation

In computing, **partial evaluation** is a technique for several different types of program optimization by specialization. The most straightforward application is to produce new programs that run faster than the originals while being guaranteed to behave in the same way.

A computer program ${\texttt {prog}}$ is seen as a mapping of input data into output data:

${\texttt {prog}}:I_{\text{static}}\times I_{\text{dynamic}}\to O,$

where $I_{\text{static}}$ , the *static data*, is the part of the input data known at compile time.

The partial evaluator transforms $\langle {\texttt {prog}},I_{\text{static}}\rangle$ into ${\texttt {prog}}^{*}:I_{\text{dynamic}}\to O$ by precomputing all static input at compile time. ${\texttt {prog}}^{*}$ is called the "residual program" and should run more efficiently than the original program. The act of partial evaluation is said to "residualize" ${\texttt {prog}}$ to ${\texttt {prog}}^{*}$ .

## Futamura projections

A particularly interesting example of the use of partial evaluation, first described in the 1970s by Yoshihiko Futamura, is when ${\texttt {prog}}$ is an interpreter for a programming language.

If $I_{\text{static}}$ is source code designed to run inside that interpreter, then partial evaluation of the interpreter with respect to this data/program produces ${\texttt {prog}}^{*}$ , a version of the interpreter that only runs that source code, is written in the implementation language of the interpreter, does not require the source code to be resupplied, and runs faster than the original combination of the interpreter and the source. In this case ${\texttt {prog}}^{*}$ is effectively a compiled version of $I_{\text{static}}$ .

This technique is known as the first Futamura projection, of which there are three:

1. Specializing an interpreter for given source code, yielding an executable.
2. Specializing the specializer for the interpreter (as applied in #1), yielding a compiler.
3. Specializing the specializer for itself (as applied in #2), yielding a tool that can convert any interpreter to an equivalent compiler.

They were described by Futamura in Japanese in 1971 and in English in 1983.

PyPy's RPython and GraalVM's Truffle framework are examples of real-world JIT compilers that implement Futamura's first projection.
