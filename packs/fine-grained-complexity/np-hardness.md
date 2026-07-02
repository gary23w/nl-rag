---
title: "NP-hardness"
source: https://en.wikipedia.org/wiki/NP-hardness
domain: fine-grained-complexity
license: CC-BY-SA-4.0
tags: fine grained complexity, fine grained reduction, strong exponential time hypothesis, 3sum conjecture
fetched: 2026-07-02
---

# NP-hardness

In computational complexity theory, a computational problem *H* is called **NP-hard** if, for every problem *L* which can be solved in non-deterministic polynomial-time, there is a polynomial-time reduction from *L* to *H*. That is, assuming a solution for *H* takes 1 unit time, *H*'s solution can be used to solve *L* in polynomial time. As a consequence, finding a polynomial time algorithm to solve a single NP-hard problem would give polynomial time algorithms for all the problems in the complexity class NP. As it is suspected, but unproven, that P≠NP, it is unlikely that any polynomial-time algorithms for NP-hard problems exist.

A simple example of an NP-hard problem is the subset sum problem.

Informally, if *H* is NP-hard, then it is at least as difficult to solve as the problems in NP. However, the opposite direction is not true: some problems are undecidable, and therefore even more difficult to solve than all problems in NP, but they are probably not NP-hard (unless P=NP).

## Definition

A decision problem *H* is NP-hard when for every problem *L* in NP, there is a polynomial-time many-one reduction from *L* to *H*.

Another definition is to require that there be a polynomial-time reduction from an NP-complete problem *G* to *H*. As any problem *L* in NP reduces in polynomial time to *G*, *L* reduces in turn to *H* in polynomial time so this new definition implies the previous one. It does not restrict the class NP-hard to decision problems, and it also includes search problems or optimization problems.

## Consequences

If P ≠ NP, then NP-hard problems could not be solved in polynomial time.

Some NP-hard optimization problems can be polynomial-time approximated up to some constant approximation ratio (in particular, those in APX) or even up to any approximation ratio (those in PTAS or FPTAS). There are many classes of approximability, each one enabling approximation up to a different level.

## Examples

All NP-complete problems are also NP-hard (see List of NP-complete problems). For example, the optimization problem of finding the least-cost cyclic route through all nodes of a weighted graph—commonly known as the travelling salesman problem—is NP-hard. The subset sum problem is another example: given a set of integers, does any non-empty subset of them add up to zero? That is a decision problem and happens to be NP-complete.

There are decision problems that are *NP-hard* but not *NP-complete* such as the halting problem. That is the problem which asks "given a program and its input, will it run forever?" That is a *yes*/*no* question and so is a decision problem. It is easy to prove that the halting problem is NP-hard but not NP-complete. For example, the Boolean satisfiability problem can be reduced to the halting problem by transforming it to the description of a Turing machine that tries all truth value assignments and when it finds one that satisfies the formula it halts and otherwise it goes into an infinite loop. It is also easy to see that the halting problem is not in *NP* since all problems in NP are decidable in a finite number of operations, but the halting problem, in general, is undecidable. There are also NP-hard problems that are neither *NP-complete* nor *Undecidable*. For instance, the language of true quantified Boolean formulas is decidable in polynomial space, but not in non-deterministic polynomial time (unless NP = PSPACE).

## NP-naming convention

NP-hard problems do not have to be elements of the complexity class NP. As NP plays a central role in computational complexity, it is used as the basis of several classes:

**NP**

Class of computational decision problems for which any given

yes

-solution can be verified as a solution in polynomial time by a deterministic Turing machine (or

solvable

by a

non-deterministic

Turing machine in polynomial time).

**NP-hard**

Class of problems which are at least as hard as the hardest problems in NP. Problems that are NP-hard do not have to be elements of NP; indeed, they may not even be decidable.

**NP-complete**

Class of decision problems which contains the hardest problems in NP. Each NP-complete problem has to be in NP.

**NP-easy**

At most as hard as NP, but not necessarily in NP.

**NP-equivalent**

Decision problems that are both NP-hard and NP-easy, but not necessarily in NP.

**NP-intermediate**

If P and NP are different, then there exist decision problems in the region of NP that fall between P and the NP-complete problems. (If P and NP are the same class, then NP-intermediate problems do not exist because in this case every NP-complete problem would fall in P, and by definition, every problem in NP can be reduced to an NP-complete problem.)

## Application areas

NP-hard problems are often tackled with rules-based languages in areas including:

- Approximate computing
- Configuration
- Cryptography
- Data mining
- Decision support
- Phylogenetics
- Planning
- Process monitoring and control
- Rosters or schedules
- Routing/vehicle routing
- Scheduling

## NP-hard problems

Problems that are decidable but not NP-complete, often are optimization problems:

- Knapsack optimization problems
- Integer programming
- Travelling salesman optimization problem
- Maximum clique
- Longest simple path
- Graph coloring; an application: register allocation in compilers
