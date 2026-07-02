---
title: "NP-completeness"
source: https://en.wikipedia.org/wiki/NP-completeness
domain: average-case-complexity
license: CC-BY-SA-4.0
tags: average case complexity, distributional problem, planted clique problem, smoothed analysis
fetched: 2026-07-02
---

# NP-completeness

In computational complexity theory, **NP-complete** problems are the hardest of the problems to which *solutions* can be verified *quickly*. Somewhat more precisely, a problem is NP-complete when:

1. It is a decision problem, meaning that for any input to the problem, the output is either "yes" or "no".
2. Each input to the problem is associated with a collection of short (polynomial length) *solutions*, which might or might not validly solve the input. The output is "yes" when at least one of these solutions is valid, and "no" when none of them are.
3. The validity of each solution can be verified quickly (namely, in polynomial time), and a brute-force search algorithm can find a valid solution (if one exists) by trying all possible solutions.
4. The problem can be used to simulate every other problem for which we can verify quickly that a solution is valid. Hence, if we could find valid solutions of some NP-complete problem quickly (when they exist), we could quickly find valid solutions for every other problem in which a given solution can be easily verified.

Problems that meet the first three criteria belong to the class NP, which is short for "nondeterministic polynomial-time". In this name, "nondeterministic" refers to nondeterministic Turing machines, a way of mathematically formalizing the idea of a brute-force search algorithm. Polynomial time refers to an amount of time that is considered "quick" for a deterministic algorithm to check a single solution, or for a nondeterministic Turing machine to perform the whole search. A problem that is in NP and also meets the fourth criterion is said to be "NP-complete". The term "complete" refers to the property of being able to simulate everything in the same complexity class: If some NP-complete problem has a polynomial time algorithm, all problems in NP do.

The set of NP-complete problems is often denoted by **NP-C** or **NPC**.

Although a solution to an NP-complete problem can be *verified* "quickly", there is no known way to *find* a solution quickly. That is, the time required to solve the problem using any currently known algorithm increases rapidly as the size of the problem grows. As a consequence, determining whether it is possible to solve these problems quickly, called the P versus NP problem, is one of the fundamental unsolved problems in computer science today.

While a method for computing the solutions to NP-complete problems quickly remains undiscovered, computer scientists and programmers still frequently encounter NP-complete problems. NP-complete problems are often addressed by using heuristic methods and approximation algorithms.

A decision problem $\scriptstyle C$ is NP-complete if:

1. $\scriptstyle C$ is in NP, and
2. Every problem in NP is reducible to $\scriptstyle C$ in polynomial time.

$\scriptstyle C$ can be shown to be in NP by demonstrating that a candidate solution to $\scriptstyle C$ can be verified in polynomial time.

A decision problem that is solvable in polynomial time belongs to the class P. All problems in P are necessarily in NP. However, it has not been proved that the class NP is actually larger than P. In other words, it is not yet known whether there exist problems in NP that are not in P. The question of whether the classes P and NP are equal or not is known as the P versus NP problem. A consequence of the definition of NP-completeness is that if we had a polynomial time algorithm (on a UTM, or any other Turing-equivalent abstract machine) for $\scriptstyle C$ , we could solve all problems in NP in polynomial time.

A problem is said to be NP-hard if everything in NP can be transformed in polynomial time into it even though it may not be in NP. A problem is NP-complete if it is both in NP and NP-hard. The NP-complete problems are thus, in a sense, the hardest problems in NP.

## Known NP-complete problems

The Cook–Levin theorem states that the Boolean satisfiability problem is NP-complete, establishing for the first time that such problems do exist. In 1972, Richard Karp proved that several other problems were also NP-complete (see Karp's 21 NP-complete problems); thus, there is a class of NP-complete problems, besides Boolean satisfiability. Since these original results, thousands of other problems have been shown to be NP-complete by reductions from other problems previously shown to be NP-complete; many of these problems are collected in Garey & Johnson (1979).

The easiest way to prove that some new problem is NP-complete is first to prove that it is in NP, and then to reduce some known NP-complete problem to it. Therefore, it is useful to know a variety of NP-complete problems. The list below contains some well-known problems that are NP-complete when expressed as decision problems.

- Boolean satisfiability problem (SAT)
- Knapsack problem
- Hamiltonian path problem
- Travelling salesman problem (decision version)
- Subgraph isomorphism problem
- Subset sum problem
- Clique problem
- Vertex cover problem
- Independent set problem
- Dominating set problem
- Graph coloring problem
- Sudoku

To the right is a diagram of some of the problems and the reductions typically used to prove their NP-completeness. In this diagram, problems are reduced from bottom to top. Note that this diagram is misleading as a description of the mathematical relationship between these problems, as there exists a polynomial-time reduction between any two NP-complete problems; but it indicates where demonstrating this polynomial-time reduction has been easiest.

There is often only a small difference between a problem in P and an NP-complete problem. For example, the 3-satisfiability problem, a restriction of the Boolean satisfiability problem, remains NP-complete, whereas the slightly more restricted 2-satisfiability problem is in P (specifically, it is NL-complete), but the slightly more general max. 2-sat. problem is again NP-complete. Determining whether a graph can be colored with 2 colors is in P, but with 3 colors is NP-complete, even when restricted to planar graphs. Determining if a graph is a cycle or is bipartite is very easy (in L), but finding a maximum bipartite or a maximum cycle subgraph is NP-complete. A solution of the knapsack problem within any fixed percentage of the optimal solution can be computed in polynomial time, but finding the optimal solution is NP-complete.

### Intermediate problems

An interesting example is the graph isomorphism problem, the graph theory problem of determining whether a graph isomorphism exists between two graphs. Two graphs are isomorphic if one can be transformed into the other simply by renaming vertices. Consider these two problems:

- Graph Isomorphism: Is graph G1 isomorphic to graph G2?
- Subgraph Isomorphism: Is graph G1 isomorphic to a subgraph of graph G2?

The Subgraph Isomorphism problem is NP-complete. The graph isomorphism problem is suspected to be neither in P nor NP-complete, though it is in NP. This is an example of a problem that is thought to be *hard*, but is not thought to be NP-complete. This class is called NP-Intermediate problems and exists if and only if P≠NP.

## Solving NP-complete problems

At present, all known algorithms for NP-complete problems require time that is superpolynomial in the input size.

The following techniques can be applied to solve computational problems in general, and they often give rise to substantially faster algorithms:

- Approximation: Instead of searching for an optimal solution, search for a solution that is at most a factor from an optimal one.
- Restriction: By restricting the structure of the input (e.g., to planar graphs), faster algorithms are usually possible.
- Parameterization: It can sometimes be possible to find algorithms whose runtimes are a polynomial of the input size multiplied by a superpolynomial function of another parameter describing the input. These can be fast, even for large inputs, when the parameter is bounded.
- Heuristic: An algorithm that works "reasonably well" in many cases, but for which there is no proof that it is both always fast and always produces a good result. Metaheuristic approaches are often used.

## Completeness under different types of reduction

In the definition of NP-complete given above, the term *reduction* was used in the technical meaning of a polynomial-time many-one reduction.

Another type of reduction is polynomial-time Turing reduction. A problem $\scriptstyle X$ is polynomial-time Turing-reducible to a problem $\scriptstyle Y$ if, given a subroutine that solves $\scriptstyle Y$ in polynomial time, one could write a program that calls this subroutine and solves $\scriptstyle X$ in polynomial time. This contrasts with many-one reducibility, which has the restriction that the program can only call the subroutine once, and the return value of the subroutine must be the return value of the program.

If one defines the analogue to NP-complete with Turing reductions instead of many-one reductions, the resulting set of problems won't be smaller than NP-complete; it is an open question whether it will be any larger.

Another type of reduction that is also often used to define NP-completeness is the logarithmic-space many-one reduction which is a many-one reduction that can be computed with only a logarithmic amount of space. Since every computation that can be done in logarithmic space can also be done in polynomial time it follows that if there is a logarithmic-space many-one reduction then there is also a polynomial-time many-one reduction. This type of reduction is more refined than the more usual polynomial-time many-one reductions and it allows us to distinguish more classes such as P-complete. Whether under these types of reductions the definition of NP-complete changes is still an open problem. All currently known NP-complete problems are NP-complete under log space reductions. All currently known NP-complete problems remain NP-complete even under much weaker reductions such as $AC_{0}$ reductions and $NC_{0}$ reductions. Some NP-Complete problems such as SAT are known to be complete even under polylogarithmic time projections. It is known, however, that AC0 reductions define a strictly smaller class than polynomial-time reductions.

## History

The concept of NP-completeness was introduced in 1971 (see Cook–Levin theorem), though the term *NP-complete* was introduced later. At the 1971 STOC conference, there was a fierce debate between the computer scientists about whether NP-complete problems could be solved in polynomial time on a deterministic Turing machine. John Hopcroft brought everyone at the conference to a consensus that the question of whether NP-complete problems are solvable in polynomial time should be put off to be solved at some later date, since nobody had any formal proofs for their claims one way or the other.

The Clay Mathematics Institute named the P versus NP question one of the seven Millennium Prize Problems in 2000.

According to Donald Knuth, the name "NP-complete" was popularized by Alfred Aho, John Hopcroft and Jeffrey Ullman in their celebrated textbook "The Design and Analysis of Computer Algorithms". He reports that they introduced the change in the galley proofs for the book (from "polynomially-complete"), in accordance with the results of a poll he had conducted of the theoretical computer science community. Other suggestions made in the poll included "Herculean", "formidable", Steiglitz's "hard-boiled" in honor of Cook, and Shen Lin's acronym "PET", which stood for "probably exponential time", but depending on which way the P versus NP problem went, could stand for "provably exponential time" or "previously exponential time".

## Common misconceptions

The following misconceptions are frequent.

- *"NP-complete problems are the most difficult known problems."* Since NP-complete problems are in NP, their running time is at most exponential. However, some problems have been proven to require more time, for example Presburger arithmetic. Of some problems, it has even been proven that they can never be solved at all, for example the halting problem.
- *"NP-complete problems are difficult because there are so many different solutions."* On the one hand, there are many problems that have a solution space just as large, but can be solved in polynomial time (for example minimum spanning tree). On the other hand, there are NP-problems with at most one solution that are NP-hard under randomized polynomial-time reduction (see Valiant–Vazirani theorem).
- *"Solving NP-complete problems requires exponential time."* First, this would imply P ≠ NP, which is still an unsolved question. Further, some NP-complete problems actually have algorithms running in superpolynomial, but subexponential time such as O(2√*n**n*). For example, the independent set and dominating set problems for planar graphs are NP-complete, but can be solved in subexponential time using the planar separator theorem.
- *"Each instance of an NP-complete problem is difficult."* Often some instances, or even most instances, may be easy to solve within polynomial time. However, unless P=NP, any polynomial-time algorithm must asymptotically be wrong on more than polynomially many of the exponentially many inputs of a certain size.
- *"If P=NP, all cryptographic ciphers can be broken."* A polynomial-time problem can be very difficult to solve in practice if the polynomial's degree or constants are large enough. In addition, information-theoretic security provides cryptographic methods that cannot be broken even with unlimited computing power.
- *"A large-scale quantum computer would be able to efficiently solve NP-complete problems."* The class of decision problems that can be efficiently solved (in principle) by a fault-tolerant quantum computer is known as BQP. However, BQP is not believed to contain all of NP, and if it does not, then it cannot contain any NP-complete problem.

## Properties

Viewing a decision problem as a formal language in some fixed encoding, the set NPC of all NP-complete problems is **not closed** under:

- union
- intersection
- concatenation
- Kleene star

It is not known whether NPC is closed under complementation, since NPC=co-NPC if and only if NP=co-NP, and since NP=co-NP is an open question.
