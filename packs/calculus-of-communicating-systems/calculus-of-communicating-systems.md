---
title: "Calculus of communicating systems"
source: https://en.wikipedia.org/wiki/Calculus_of_communicating_systems
domain: calculus-of-communicating-systems
license: CC-BY-SA-4.0
tags: calculus of communicating systems, labelled transition system, process algebra, structural congruence
fetched: 2026-07-02
---

# Calculus of communicating systems

The **calculus of communicating systems** (**CCS**) is a process calculus introduced by Robin Milner around 1980 and the title of a book describing the calculus. Its actions model indivisible communications between exactly two participants. The formal language includes primitives for describing parallel composition, summation between actions and scope restriction. CCS is useful for evaluating the qualitative correctness of properties of a system such as deadlock or livelock.

According to Milner, "There is nothing canonical about the choice of the basic combinators, even though they were chosen with great attention to economy. What characterises our calculus is not the exact choice of combinators, but rather the choice of interpretation and of mathematical framework".

The expressions of the language are interpreted as a labelled transition system. Between these models, bisimilarity is used as a semantic equivalence.

## Syntax

Given a set of action names, the set of CCS processes is defined by the following BNF grammar:

$P::=0\,\,\,|\,\,\,a.P_{1}\,\,\,|\,\,\,$

ref

$A\,\,\,|\,\,\,P_{1}+P_{2}\,\,\,|\,\,\,P_{1}|P_{2}\,\,\,|\,\,\,P_{1}[b/a]\,\,\,|\,\,\,P_{1}{\backslash }a\,\,\,$

The parts of the syntax are, in the order given above

**inactive process**

the inactive process

0

is a valid CCS process

**action**

the process

$a.P_{1}$

can perform an action

a

and continue as the process

$P_{1}$

**process identifier**

define

$A{\overset {\underset {\mathrm {def} }{}}{=}}P_{1}$

, and then use the identifier

A

to refer to the process

$P_{1}$

(which may contain the identifier

A

itself, i.e., recursive definitions are allowed)

**summation**

the process

$P_{1}+P_{2}$

can proceed either as the process

$P_{1}$

or the process

$P_{2}$

**parallel composition**

$P_{1}|P_{2}$

tells that processes

$P_{1}$

and

$P_{2}$

exist simultaneously

**renaming**

$P_{1}[b/a]$

is the process

$P_{1}$

with all actions named

a

renamed as

b

**restriction**

$P_{1}{\backslash }a$

is the process

$P_{1}$

without action

a

- Communicating sequential processes (CSP), developed by Tony Hoare, is a formal language that arose at a similar time to CCS.
- The Algebra of Communicating Processes (ACP) was developed by Jan Bergstra and Jan Willem Klop in 1982, and uses an axiomatic approach (in the style of Universal algebra) to reason about a similar class of processes as CCS.
- The pi-calculus, developed by Robin Milner, Joachim Parrow, and David Walker in the late 80's extends CCS with mobility of communication links, by allowing processes to communicate the names of communication channels themselves.
- PEPA, developed by Jane Hillston introduces activity timing in terms of exponentially distributed rates and probabilistic choice, allowing performance metrics to be evaluated.
- Reversible Communicating Concurrent Systems (RCCS) introduced by Vincent Danos, Jean Krivine, and others, introduces (partial) reversibility in the execution of CCS processes.

Some other languages based on CCS:

- Calculus of broadcasting systems
- Language Of Temporal Ordering Specification (LOTOS)
- Process Calculus for Spatially-Explicit Ecological Models (PALPS) is an extension of CCS with probabilistic choice, locations and attributes for locations
- Java Orchestration Language Interpreter Engine (Jolie)

Models that have been used in the study of CCS-like systems:

- History monoid
- Actor model
