---
title: "Oracle machine"
source: https://en.wikipedia.org/wiki/Oracle_machine
domain: polynomial-hierarchy
license: CC-BY-SA-4.0
tags: polynomial hierarchy, oracle machine, quantified boolean formula, sigma level
fetched: 2026-07-02
---

# Oracle machine

In complexity theory and computability theory, an **oracle machine** is an abstract machine that can query a black box called an **oracle**, which is able to give an answer to any instance of a certain problem ⁠ R ⁠ in a single operation. The problem ⁠ R ⁠ can be of any complexity class, or it can even be an undecidable problem such as the halting problem. If another problem ⁠ $R'$ ⁠ is reducible to ⁠ R ⁠ in polynomial time, then the oracle machine (with the ⁠ R ⁠-oracle) can solve ⁠ $R'$ ⁠ in polynomial time; one can say that ⁠ $R'$ ⁠ is in the **relativized complexity class** ⁠ ${\mathsf {P}}^{R}$ ⁠. Other relativized complexity classes such as ⁠ ${\mathsf {NP}}^{R}$ ⁠ can be defined analogously.

## Oracles

An oracle machine can be conceived as a Turing machine connected to an **oracle**. The oracle, in this context, is an entity capable of solving some problem, which for example may be a decision problem or a function problem. The problem does not have to be computable; the oracle is not assumed to be a Turing machine or computer program. The oracle is simply a "black box" that is able to produce a solution for any instance of a given computational problem:

- A decision problem is represented as a set *A* of natural numbers (or strings). An instance of the problem is an arbitrary natural number (or string). The solution to the instance is "YES" if the number (string) is in the set, and "NO" otherwise.
- A function problem is represented by a binary relation *R* relating natural numbers (or strings) to natural numbers (or strings). An instance of the problem is an input *x* for *R*. A solution is a value related to *x* by *R*.

An oracle machine can perform all of the usual operations of a Turing machine, and can also query the oracle to obtain a solution to any instance of the computational problem for that oracle. For example, if the problem is a decision problem for a set *A* of natural numbers, the oracle machine supplies the oracle with a natural number, and the oracle responds with "yes" or "no" stating whether that number is an element of *A*.

## Definitions

There are many equivalent definitions of oracle Turing machines, as discussed below. The one presented here is from van Melkebeek (2003, p. 43).

An oracle machine, like a Turing machine, includes:

- a **work tape**: a sequence of cells without beginning or end, each of which may contain a B (for blank) or a symbol from the tape alphabet;
- a **read/write head**, which rests on a single cell of the work tape and can read the data there, write new data, and increment or decrement its position along the tape;
- a **control mechanism**, which can be in one of a finite number of **states**, and which will perform different actions (reading data, writing data, moving the read/write head, and changing states) depending on the current state and the data being read.

In addition to these components, an oracle machine also includes:

- an **oracle tape**, which is a semi-infinite tape separate from the work tape. The alphabet for the oracle tape may be different from the alphabet for the work tape.
- an **oracle head** which, like the read/write head, can move left or right along the oracle tape reading and writing symbols;
- two special states: the ASK state and the RESPONSE state.

From time to time, the oracle machine may enter the ASK state. When this happens, the following actions are performed in a single computational step:

- the contents of the oracle tape are viewed as an instance of the oracle's computational problem;
- the oracle is consulted, and the contents of the oracle tape are replaced with the solution to that instance of the problem;
- the oracle head is moved to the first square on the oracle tape;
- the state of the oracle machine is changed to RESPONSE.

The effect of changing to the ASK state is thus to receive, in a single step, a solution to the problem instance that is written on the oracle tape.

### Alternative definitions

There are many alternative definitions to the one presented above. Many of these are specialized for the case where the oracle solves a decision problem. In this case:

- Some definitions, instead of writing the answer to the oracle tape, have two special states YES and NO in addition to the ASK state. When the oracle is consulted, the next state is chosen to be YES if the contents of the oracle tape are in the oracle set, and chosen to be NO if the contents are not in the oracle set.
- Some definitions eschew the separate oracle tape. When the oracle state is entered, a tape symbol is specified. The oracle is queried with the number of times that this tape symbol appears on the work tape. If that number is in the oracle set, the next state is the YES state; if it is not, the next state is the NO state.
- Another alternative definition makes the oracle tape read-only, and eliminates the ASK and RESPONSE states entirely. Before the machine is started, the indicator function of the oracle set is written on the oracle tape using symbols 0 and 1. The machine is then able to query the oracle by scanning to the correct square on the oracle tape and reading the value located there.

These definitions are equivalent from the point of view of Turing computability: a function is oracle-computable from a given oracle under all of these definitions if it is oracle-computable under any of them. The definitions are not equivalent, however, from the point of view of computational complexity. A definition such as the one by van Melkebeek, using an oracle tape that may have its own alphabet, is required in general.

## Complexity classes of oracle machines

The complexity class of decision problems solvable by an algorithm in class *A* with an oracle for a language *L* is called *A**L*. For example, PSAT is the class of problems solvable in polynomial time by a deterministic Turing machine with an oracle for the Boolean satisfiability problem. The notation AB can be extended to a set of languages *B* (or a complexity class *B*), by using the following definition:

$A^{B}=\bigcup _{L\in B}A^{L}$

When a language *L* is complete for some class *B*, then *A**L*=*A**B* provided that machines in *A* can execute reductions used in the completeness definition of class *B*. In particular, since SAT is NP-complete with respect to polynomial time reductions, PSAT=PNP. However, if *A* = DLOGTIME, then *A*SAT may not equal *A*NP. (The definition of $A^{B}$ given above is not completely standard. In some contexts, such as the proof of the time and space hierarchy theorems, it is more useful to assume that the abstract machine defining class A only has access to a single oracle for one language. In this context, $A^{B}$ is not defined if the complexity class B does not have any complete problems with respect to the reductions available to A .)

It is understood that NP ⊆ PNP, but the question of whether NPNP, PNP, NP, and P are equal remains tentative at best. It is believed they are different, and this leads to the definition of the polynomial hierarchy.

Oracle machines are useful for investigating the relationship between complexity classes P and NP, by considering the relationship between P*A* and NP*A* for an oracle *A*. In particular, it has been shown there exist languages *A* and *B* such that P*A*=NP*A* and P*B*≠NP*B*. The fact the P = NP question relativizes both ways is taken as evidence that answering this question is difficult, because any proof technique that *relativizes* (i.e., is unaffected by the addition of an oracle) will not answer the P = NP question. Most proof techniques relativize.

One may consider the case where an oracle is chosen randomly from among all possible oracles (an infinite set). It has been shown in this case, that with probability 1, P*A*≠NP*A*. When a question is true for almost all oracles, it is said to be true *for a random oracle*. This choice of terminology is justified by the fact that random oracles support a statement with probability 0 or 1 only. (This follows from Kolmogorov's zero–one law.) This is only weak evidence that P≠NP, since a statement may be true for a random oracle but false for ordinary Turing machines; for example, IP*A*≠PSPACE*A* for a random oracle *A* but IP = PSPACE.

## Oracles and halting problems

A machine with an oracle for the halting problem can determine whether particular Turing machines will halt on particular inputs, but it cannot determine, in general, whether oracle machines like itself (i.e. equipped with an oracle for the halting problem) will halt. This creates a hierarchy of machines, each with a more powerful halting oracle and an even harder halting problem. This hierarchy of machines can be used to define the *arithmetical hierarchy*.

## Applications to cryptography

In cryptography, oracles are used to make arguments for the security of cryptographic protocols where a hash function is used. A security reduction (proof of security) for the protocol is given in the case where, instead of a hash function, a random oracle answers each query randomly but consistently; the oracle is assumed to be available to all parties including the attacker, as the hash function is. Such a proof shows that unless the attacker solves the hard problem at the heart of the security reduction, they must make use of some interesting property of the hash function to break the protocol; they cannot treat the hash function as a black box (i.e., as a random oracle).
