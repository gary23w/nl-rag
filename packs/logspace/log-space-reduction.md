---
title: "Log-space reduction"
source: https://en.wikipedia.org/wiki/Log-space_reduction
domain: logspace
license: CC-BY-SA-4.0
tags: logarithmic space, log space reduction, undirected connectivity, symmetric turing machine
fetched: 2026-07-02
---

# Log-space reduction

In computational complexity theory, a **log-space reduction** is a reduction computable by a deterministic Turing machine using logarithmic space. Conceptually, this means the Turing machine can keep a constant number of pointers into the input, along with a logarithmic number of fixed-size integers. It is possible that such a machine may not have space to write down its own output, so the only requirement is that any given bit of the output be computable in log-space. Formally, this reduction is executed via a log-space transducer.

Such a machine has polynomially-many configurations, so log-space reductions are also polynomial-time reductions. However, log-space reductions are probably weaker than polynomial-time reductions; while any non-empty, non-full language in P is polynomial-time reducible to any other non-empty, non-full language in P, a log-space reduction from an NL-complete language to a language in L, both of which would be languages in P, would imply the unlikely L = NL. It is an open question if the NP-complete problems are different with respect to log-space and polynomial-time reductions.

Log-space reductions are normally used on languages in P, in which case it usually does not matter whether many-one reductions or Turing reductions are used, since it has been verified that L, SL, NL, and P are all closed under log-space Turing reductions, meaning that Turing reductions can be used to show a problem is in any of these classes. However, other subclasses of P such as NC may not be closed under Turing reductions, and so many-one reductions must be used.

Just as polynomial-time reductions are useless within P and its subclasses, log-space reductions are useless to distinguish problems in L and its subclasses; in particular, every non-empty, non-full problem in L is trivially L-complete under log-space reductions. While even weaker reductions exist, they are not often used in practice, because complexity classes smaller than L (that is, strictly contained or thought to be strictly contained in L) receive relatively little attention.

The tools available to designers of log-space reductions have been greatly expanded by the result that L = SL; see SL for a list of some SL-complete problems that can now be used as subroutines in log-space reductions.

## Logspace computable function

A function $f:2^{*}\to 2^{*}$ is **(implicitly) logspace computable** if:

- Its output length is polynomially bounded: There exists some $c>0$ such that $f(x)\leq |x|^{c}$ for all $x\in 2^{*}$ .
- $L_{f}=\left\{\langle x,i\rangle \mid f(x)_{i}=1\right\}$ is in complexity class L.
- $L_{f}^{\prime }=\{\langle x,i\rangle \mid i\leq |f(x)|\}$ is in complexity class L.

Intuitively, the first condition states that the function creates outputs that are short enough, such that creating a single pointer on the output will take only logspace. That condition is necessary in order for pointers on the output to exist at all.

The second condition states that any *particular* output location is computable in logspace.

The third condition states that checking if a pointer is a valid pointer is decidable in logspace.

Equivalently, a function $f:2^{*}\to 2^{*}$ is logspace computable if it is computed by a Turing machine with a log-length work tape, that halts on any input, and an output tape that is write-only and write-once, meaning that at each step, the machine may either write nothing, or write a bit and move the write-head forward by one. Such a machine is usually called a **logspace transducer**. Note that such a machine, if it halts, must halt in polynomial steps, since its work tape has log-length. Therefore its output length is polynomially bounded.

One intuition is that such a function can be computed by a program that can only keep a constant number of pointers to the input, and a constant number of counters that can only contain integers of size ${\mathsf {poly}}(n)$ . This is because a counter machine with a constant number of counters that count up to $f(n)$ is equivalent to a Turing machine with space complexity $O(\log f(n))$ .

### Closure

The most important property of logspace computability is that, if functions $f,g$ are logspace computable, then so is their composition $g\circ f$ . This allows the concept of logspace reduction to be transitive.

Given two logspace transducers, their composition is still a logspace transducer: feed the output from one transducer (A→B) to another (B→C). At first glance, this seems incorrect because intuitively, the A→C transducer needs to store the output tape from the A→B transducer onto the work tape, in order to feed it into the B→C reducer, but this is not necessary, by the following construction.

Define the A→C transducer as follows: It simulates the operations of B→C transducer. Every time the B→C transducer needs to make a read, the A→C transducer re-runs the A→B transducer to re-compute only the exact output bit that is needed, and so only one bit of the output of the A→B transducer needs to be stored at any moment.

## Logspace reduction

A language L is **logspace (many-one) reducible** to another language $L'$ , notated as $L\leq _{l}L'$ , if there exists an implicitly logspace computable function f such that $x\in L\iff f(x)\in L'$ . This is a transitive relation, because logspace computability is closed under composition, as previously shown.

A language L is **NL-complete** if it is both in NL and any language in NL is logspace reducible to it.

Most naturally occurring polynomial-time reductions in complexity theory are logspace reductions. In particular, this is true for the standard proof showing that the SAT problem is NP-complete, and that the circuit value problem is P-complete. This is also often the case for showing that the true quantified Boolean formula problem is PSPACE-complete. This is because the need for memory in such reduction constructions is for counting up to $p(n)$ for some polynomial p in the input length n , and this can be done in logarithmic space.

While logspace many-one reduction implies polynomial time many-one reduction, it is unknown whether this is an equivalence, or whether there are problems that are NP-complete under polynomial time reduction, but not under logspace reduction. Any solution to this problem would solve this problem: Are deterministic linear bounded automata equivalent to nondeterministic linear bounded automata?
