---
title: "Alternating Turing machine"
source: https://en.wikipedia.org/wiki/Alternating_Turing_machine
domain: polynomial-hierarchy
license: CC-BY-SA-4.0
tags: polynomial hierarchy, oracle machine, quantified boolean formula, sigma level
fetched: 2026-07-02
---

# Alternating Turing machine

In computational complexity theory, an **alternating Turing machine** (**ATM**) is a non-deterministic Turing machine (**NTM**) with a rule for accepting computations that generalizes the rules used in the definition of the complexity classes NP and co-NP. The concept of an ATM was set forth by Chandra and Stockmeyer and independently by Kozen in 1976, with a joint journal publication in 1981.

## Definitions

### Informal description

The definition of NP uses the *existential mode* of computation: if *any* choice leads to an accepting state, then the whole computation accepts. The definition of co-NP uses the *universal mode* of computation: only if *all* choices lead to an accepting state does the whole computation accept. An alternating Turing machine (or to be more precise, the definition of acceptance for such a machine) alternates between these modes.

An **alternating Turing machine** is a non-deterministic Turing machine whose states are divided into two sets: **existential states** and **universal states**. An existential state is accepting if some transition leads to an accepting state; a universal state is accepting if every transition leads to an accepting state. (Thus a universal state with no transitions accepts unconditionally; an existential state with no transitions rejects unconditionally). The machine as a whole accepts if the initial state is accepting.

### Formal definition

Formally, a (one-tape) **alternating Turing machine** is a 5-tuple $M=(Q,\Gamma ,\delta ,q_{0},g)$ where

- Q is the finite set of states
- $\Gamma$ is the finite tape alphabet
- $\delta :Q\times \Gamma \rightarrow {\mathcal {P}}(Q\times \Gamma \times \{L,R\})$ is called the transition function (*L* shifts the head left and *R* shifts the head right)
- $q_{0}\in Q$ is the initial state
- $g:Q\rightarrow \{\wedge ,\vee ,accept,reject\}$ specifies the type of each state

If *M* is in a state $q\in Q$ with $g(q)=accept$ then that configuration is said to be *accepting*, and if $g(q)=reject$ the configuration is said to be *rejecting*. A configuration with $g(q)=\wedge$ is said to be accepting if all configurations reachable in one step are accepting, and rejecting if some configuration reachable in one step is rejecting. A configuration with $g(q)=\vee$ is said to be accepting when there exists some configuration reachable in one step that is accepting and rejecting when all configurations reachable in one step are rejecting (this is the type of all states in a classical NTM except the final state). *M* is said to accept an input string *w* if the initial configuration of *M* (the state of *M* is $q_{0}$ , the head is at the left end of the tape, and the tape contains *w*) is accepting, and to reject if the initial configuration is rejecting.

Note that it is impossible for a configuration to be both accepting and rejecting, however, some configurations may be neither accepting or rejecting, due to the possibility of nonterminating computations.

### Resource bounds

When deciding if a configuration of an ATM is accepting or rejecting using the above definition, it is not always necessary to examine all configurations reachable from the current configuration. In particular, an existential configuration can be labelled as accepting if any successor configuration is found to be accepting, and a universal configuration can be labelled as rejecting if any successor configuration is found to be rejecting.

An ATM decides a formal language in time $t(n)$ if, on any input of length n, examining configurations only up to $t(n)$ steps is sufficient to label the initial configuration as accepting or rejecting. An ATM decides a language in space $s(n)$ if examining configurations that do not modify tape cells beyond the $s(n)$ cell from the left is sufficient.

A language that is decided by some ATM in time $c\cdot t(n)$ for some constant $c>0$ is said to be in the class ${\mathsf {ATIME}}(t(n))$ , and a language decided in space $c\cdot s(n)$ is said to be in the class ${\mathsf {ASPACE}}(s(n))$ .

## Example

Perhaps the most natural problem for alternating machines to solve is the quantified Boolean formula problem, which is a generalization of the Boolean satisfiability problem in which each variable can be bound by either an existential or a universal quantifier. The alternating machine branches existentially to try all possible values of an existentially quantified variable and universally to try all possible values of a universally quantified variable, in the left-to-right order in which they are bound. After deciding a value for all quantified variables, the machine accepts if the resulting Boolean formula evaluates to true, and rejects if it evaluates to false. Thus, at an existentially quantified variable the machine is accepting if a value can be substituted for the variable that renders the remaining problem satisfiable, and at a universally quantified variable the machine is accepting if any value can be substituted and the remaining problem is satisfiable.

Such a machine decides quantified Boolean formulas in time $n^{2}$ and space n .

The Boolean satisfiability problem can be viewed as the special case where all variables are existentially quantified, allowing ordinary nondeterminism, which uses only existential branching, to solve it efficiently.

## Complexity classes and comparison to deterministic Turing machines

The following complexity classes are useful to define for ATMs:

- ${\mathsf {AP}}=\bigcup _{k>0}{\mathsf {ATIME}}(n^{k})$ are the languages decidable in polynomial time
- ${\mathsf {APSPACE}}=\bigcup _{k>0}{\mathsf {ASPACE}}(n^{k})$ are the languages decidable in polynomial space
- ${\mathsf {AEXPTIME}}=\bigcup _{k>0}{\mathsf {ATIME}}(2^{n^{k}})$ are the languages decidable in exponential time

These are similar to the definitions of P, PSPACE, and EXPTIME, considering the resources used by an ATM rather than a deterministic Turing machine. Chandra, Kozen, and Stockmeyer proved that, for all $f(n)\geq \log(n)$ and $g(n)\geq \log(n)$ :

- ${\mathsf {ASPACE}}(f(n))=\bigcup _{c>0}{\mathsf {DTIME}}(2^{cf(n)})={\mathsf {DTIME}}(2^{O(f(n))})$
- ${\mathsf {ATIME}}(g(n))\subseteq {\mathsf {DSPACE}}(g(n))$
- ${\mathsf {NSPACE}}(g(n))\subseteq \bigcup _{c>0}{\mathsf {ATIME}}(c\times g(n)^{2}),$

In particular:

- ALOGSPACE = P
- AP = PSPACE
- APSPACE = EXPTIME
- AEXPTIME = EXPSPACE

A more general form of these relationships is expressed by the parallel computation thesis.

## Bounded alternation

### Definition

An **alternating Turing machine with *k* alternations** is an alternating Turing machine that switches from an existential to a universal state or vice versa no more than *k*−1 times. (It is an alternating Turing machine whose states are divided into *k* sets. The states in even-numbered sets are universal and the states in odd-numbered sets are existential (or vice versa). The machine has no transitions between a state in set *i* and a state in set *j* < *i*.)

${\mathsf {ATIME}}(C,j)=\Sigma _{j}{\mathsf {TIME}}(C)$ is the class of languages decidable in time $f\in C$ by a machine beginning in an existential state and alternating at most $j-1$ times. It is called the jth level of the ${\mathsf {TIME}}(C)$ hierarchy.

${\mathsf {coATIME}}(C,j)=\Pi _{j}{\mathsf {TIME}}(C)$ is defined in the same way, but beginning in a universal state; it consists of the complements of the languages in ${\mathsf {ATIME}}(f,j)$ .

${\mathsf {ASPACE}}(C,j)=\Sigma _{j}{\mathsf {SPACE}}(C)$ is defined similarly for space bounded computation.

### Example

Consider the circuit minimization problem: given a circuit *A* computing a Boolean function *f* and a number *n*, determine if there is a circuit with at most *n* gates that computes the same function *f*. An alternating Turing machine, with one alternation, starting in an existential state, can solve this problem in polynomial time (by guessing a circuit *B* with at most *n* gates, then switching to a universal state, guessing an input, and checking that the output of *B* on that input matches the output of *A* on that input).

### Collapsing classes

It is said that a hierarchy *collapses* to level j if every language in level $k\geq j$ of the hierarchy is in its level j.

As a corollary of the Immerman–Szelepcsényi theorem, the logarithmic space hierarchy collapses to its first level. As a corollary the ${\mathsf {SPACE}}(f)$ hierarchy collapses to its first level when $f=\Omega (\log )$ is space constructible.

### Special cases

An alternating Turing machine in polynomial time with *k* alternations, starting in an existential (respectively, universal) state can decide all the problems in the class $\Sigma _{k}^{p}$ (respectively, $\Pi _{k}^{p}$ ). These classes are sometimes denoted $\Sigma _{k}{\rm {P}}$ and $\Pi _{k}{\rm {P}}$ , respectively. See the polynomial hierarchy article for details.

Another special case of time hierarchies is the logarithmic hierarchy.
