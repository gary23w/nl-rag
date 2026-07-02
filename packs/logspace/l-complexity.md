---
title: "L (complexity)"
source: https://en.wikipedia.org/wiki/L_(complexity)
domain: logspace
license: CC-BY-SA-4.0
tags: logarithmic space, log space reduction, undirected connectivity, symmetric turing machine
fetched: 2026-07-02
---

# L (complexity)

In computational complexity theory, **L** (also known as **LSPACE**, **LOGSPACE** or **DLOGSPACE**) is the complexity class containing decision problems that can be solved by a deterministic Turing machine using a logarithmic amount of writable memory space. Formally, the Turing machine has two tapes, one of which encodes the input and can only be read, whereas the other tape has logarithmic size but can be written as well as read. Logarithmic space is sufficient to hold a constant number of pointers into the input and a logarithmic number of Boolean flags, and many basic logspace algorithms use the memory in this way.

## Complete problems and logical characterization

Every non-trivial problem in **L** is complete under log-space reductions, so weaker reductions are required to identify meaningful notions of **L**-completeness, the most common being first-order reductions.

A 2004 result by Omer Reingold shows that USTCON, the problem of whether there exists a path between two vertices in a given undirected graph, is in **L**, showing that **L** = **SL**, since USTCON is **SL**-complete.

One consequence of this is a simple logical characterization of **L**: it contains precisely those languages expressible in first-order logic with an added commutative transitive closure operator (in graph theoretical terms, this turns every connected component into a clique). This result has application to database query languages: *data complexity* of a query is defined as the complexity of answering a fixed query considering the data size as the variable input. For this measure, queries against relational databases with complete information (having no notion of nulls) as expressed for instance in relational algebra are in **L**.

**L** is a subclass of **NL**, which is the class of languages decidable in logarithmic space on a nondeterministic Turing machine. A problem in **NL** may be transformed into a problem of reachability in a directed graph representing states and state transitions of the nondeterministic machine, and the logarithmic space bound implies that this graph has a polynomial number of vertices and edges, from which it follows that **NL** is contained in the complexity class **P** of problems solvable in deterministic polynomial time. Thus **L** ⊆ **NL** ⊆ **P**. The inclusion of **L** into **P** can also be proved more directly: a decider using *O*(log *n*) space cannot use more than 2*O*(log *n*) = *n**O*(1) time, because this is the total number of possible configurations.

**L** further relates to the class **NC** in the following way: **NC**1 ⊆ **L** ⊆ **NL** ⊆ **NC**2. In words, given a parallel computer *C* with a polynomial number *O*(*n**k*) of processors for some constant *k*, any problem that can be solved on *C* in *O*(log *n*) time is in **L**, and any problem in **L** can be solved in *O*(log2 *n*) time on *C*.

Unsolved problem in computer science

⁠

${\mathsf {L}}{\overset {?}{=}}{\mathsf {P}}$

⁠

More unsolved problems in computer science

Important open problems include whether **L** = **P**, and whether **L** = **NL**. It is not even known whether **L** = **NP**.

The related class of function problems is **FL**. **FL** is often used to define logspace reductions.

## Random versions

Just as how **P** has several random versions: **BPP**, **ZPP**, **PP**, and **RP**, there are several random versions of **L**.

**Bounded-error Probability L** (**BPL**) is defined like **BPP**, as the complexity class of problems solvable with a logspace Turing machine such that:

- Other than the usual tapes of a logspace Turing machine, the machine also takes a tape filled with random bits.
- The randomness is read-only and one-way. That is, the read-head on the random tape can only move in one direction. To reference a previous random bit, the machine must store it in the work tape.
- The Turing machine has to halt for every input and every random tape.
- If the answer is 'yes' then the machine accepts with probability at least 2/3. If the answer is 'no' then the machine rejects with probability at least 2/3.

It is contained in **NC***2*, which is contained in **P**.

**BP•L** is defined the same as **BPL**, except that the machine is allowed to read the random tape both forwards and backwards. It contains **BPL**. It is also exactly equal to the class of languages that are nearly logspace: a language is nearly logspace if, relative to almost every oracle, the language is in **L**.

**ZP•L** is defined like **BP•L**, except that the machine may output "unknown", and must never make an error (i.e. accept when the answer is 'no', and vice versa). The relation of **ZP•L** to **BP•L**, is the same as the relation of **ZPP** to **BPP**. It contains **BPL** and is contained by **BP•L**.

**Randomized L** (**RL**) is defined like **BPL**:

- Other than the usual tapes of a logspace Turing machine, the machine also takes a read-only one-way tape filled with random bits.
- The Turing machine has to halt for every input and every random tape.
- If the answer is 'yes,' accept with probability at least 1/2.
- If the answer is 'no,' always reject.

Also, it must always run in polynomial time (since otherwise we would just get **NL**). It is strongly suspected that **RL** = **L**.

Both **BPL** and **RL** are contained in Steve's Class.

**Probabilistic L** (**PL**) has the same relation to **L** that **PP** has to **P**:

- If the answer is 'yes,' accept with probability at least 1/2.
- If the answer is 'no,' reject with probability at least 1/2.

It contains **BPL**, and is contained by **NC***2*.

## Additional properties

**L** is low for itself, because it can simulate log-space oracle queries (roughly speaking, "function calls which use log space") in log space, reusing the same space for each query.

## Other uses

The main idea of logspace is that one can store a polynomial-magnitude number in logspace and use it to remember pointers to a position of the input.

The logspace class is therefore useful to model computation where the input is too big to fit in the RAM of a computer. Long DNA sequences and databases are good examples of problems where only a constant part of the input will be in RAM at a given time and where we have pointers to compute the next part of the input to inspect, thus using only logarithmic memory.
