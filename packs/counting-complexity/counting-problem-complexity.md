---
title: "Counting problem (complexity)"
source: https://en.wikipedia.org/wiki/Counting_problem_(complexity)
domain: counting-complexity
license: CC-BY-SA-4.0
tags: counting complexity, permanent computation, toda theorem, counting problem
fetched: 2026-07-02
---

# Counting problem (complexity)

In computational complexity theory and computability theory, a **counting problem** is a type of computational problem that is obtained by strengthening a decision problem.

For example, the SAT problem asks: "Given a Boolean formula, is there a truth-value assignment such that it evaluates to True?". The corresponding counting problem, called #SAT, asks: "Given a Boolean formula, how many truth-value assignments are there such that it evaluates to True?".

And in general, the counting problem corresponding to a decision problem X is called #X, where # is the number sign.

Counting complexity techniques have significant applications in clarifying the relation between complexity classes of P, NP, PH, etc, in circuit complexity, and in interactive proof systems.

## Definition

Let *R* be a search problem, formalised as a binary relation $R(x,y)$ . That is, given a problem instance x , one can proposed solutions. $R(x,y)$ is true iff y is an *admissible* solution to the problem instance.

Let ${\textstyle c_{R}(x)=\vert \{y\mid R(x,y)\}\vert \,}$ be the counting function. That is, it counts the total number of admissible solutions. This is a function problem, not a decision problem.

In order to conform to the standard format in computational complexity theory, we use the standard trick of converting a function problem to a decision problem, using the graph of the function. Let $\#R=\{(x,y)\mid y\leq c_{R}(x)\}$ . That is, it is the set of all points on or below the curve of $c_{R}(x)$ .

While it appears that computing $c_{R}(x)$ is harder than deciding whether some point $(x,y)$ belongs to $\#R$ , in fact $c_{R}$ can be Cook-reduced to $\#R$ using binary search on the value of $c_{R}(x)$ , provided that $c_{R}(x)$ is bounded by $O(2^{{\mathsf {poly}}(|x|)})$ . Concretely, one tests with $(x,0),(x,1),\dots ,(x,2^{n}),\dots ,(x,2^{n^{2}}),\dots$ until one finds an element not in $\#R$ , then backtracks to pinpoint the exact value of $c_{R}(x)$ .

In particular, $c_{R}(x)$ must be bounded by $O(2^{{\mathsf {poly}}(|x|)})$ if it is **FP**, that is, computable in polynomial time by a Turing machine, since otherwise the machine will not have enough time to produce the full output.

Throughout this article, we assume that $c_{R}(x)$ is FP. This then allows us to switch between the decision-formulation with $\#R$ and the function-formulation $c_{R}$ fluidly without further comment.

## Classes

### #P

The most important classes of counting problems is the #P class, the counting problems corresponding to the NP class of decision problems. An NP problem a decision problem that asks, "Given a problem instance, is there at least one solution?", and furthermore, an NP problem comes with a solution-verifier Turing machine that runs in polynomial time.

The corresponding #P problem then asks: "Given a problem instance, how many solutions are there?". More succinctly, #P counts accepting paths of an nondeterministic Turing machine running in polynomial time.

Just as NP has NP-complete problems via many-one reductions, #P has #P-complete problems via polynomial-time parsimonious reductions. Given two search problems $A,B$ , a polynomial-time parsimonious reduction from A to B is a function f , such that

- f is computable in polynomial time.
- For any problem instance $x_{A}$ of A , it maps to a problem instance $f(x_{A})$ of B , such that $x_{A}$ and $f(x_{A})$ have the same number of solutions.

This reduction is reflexive and transitive. Some problems are ♯P-complete under polynomial-time parsimonious counting reduction, such as the #3SAT problem. To show this, one simply takes the standard proof that 3SAT problem is NP-complete, and note that the reduction used in the proof is already parsimonious. More examples are given on the Parsimonious reduction page.

The polynomial-time many-one counting reduction is another, more lenient form of reduction. Given two search problems $A,B$ , a polynomial-time many-one reduction from A to B consists of two functions $f,g$ , such that

- $f,g$ are computable in polynomial time.
- For any problem instance $x_{A}$ of A , f maps to a problem instance $f(x_{A})$ of B , such that the number of solutions to $x_{A}$ is computed by mapping the number of solutions to $f(x_{A})$ using g : $c_{A}(x_{A})=g(c_{B}(f(x_{A})))$

Counting analogs of many natural NP-complete problems are #P-complete, but the opposite is not the case: Some decision problems correspond to #P-complete counting problems, even if they are in P, or even trivially decidable.

For example, the 01-permanent counting problem is ♯P-complete under polynomial-time many-one counting reduction. This problem is equivalent to counting perfect matchings in a bipartite graph. Deciding whether perfect matchings exist in a bipartite graph is polynomial-time by the Hopcroft–Karp algorithm.

There are some other problems that takes polynomial time to decide, but are #P-complete to count:

- Spanning trees of a graph.
- Eulerian cycles of a directed graph.
- Perfect matchings of a planar graph.

There are some problems that are trivial to decide, but #P-complete to count:

- Satisfying assignments to a monotone Boolean formula (one without negation symbol). There always exists at least one, by setting all variables to True.
- Non-cliques in a graph of size $\lceil n/2\rceil$ , where n is the number of vertices. If the whole graph has any pair of vertices not connected by an edge, then there exists such a non-clique.
- Spanning forests of a bipartite planar graph. There always exists at least one.
- Linear extensions to a partially ordering on a finite set. There always exists at least one.

There are some counting problems known to be #P-hard, but possibly exceeding #P:

- Given two graphs, count the number of graph isomorphisms between them. This is known to be computable in polynomial time given an NP-oracle.
- Given a graph, count the number of subgraphs that are Hamiltonian.

### ModP

ModkP asks: "Given a problem instance, is the number of solutions divisible by *k*?". For all k≥2, ModkP contains the graph isomorphism problem. Further, the graph isomorphism problem is low in ModkP. When *k* is prime, the set of languages low in ModkP is ModkP itself.

⊕P is defined to be Mod2P. It asks: "Given a problem instance, is the number of solutions even or odd?". It is low in itself: $\oplus {\mathsf {P}}^{\oplus {\mathsf {P}}}=\oplus {\mathsf {P}}$ .

### PP

PP, or PPT is the class of decision problems solvable by a probabilistic Turing machine in polynomial time, with an error probability of less than 1/2 for all instances. This is equivalently defined as: "Given a positive problem instance, and a nondeterministic Turing machine in polynomial time, are more than half of the potential solutions actually correct?".

Note that, in order for the question to make sense, one must define the set of "potential solutions". In most cases of NP problems, the set of "potential solutions" is obvious. For example, for the SAT problem, a problem instance is a Boolean formula $\phi$ , and the set of potential solutions is the set of boolean value assignments $V\to \{0,1\}$ , where V is the set of variables in $\phi$ .

### FewP

The **FewP** class ("NP with few witnesses") is defined as a particular class of NP decision problems. Specifically, a decision problem is FewP if there exists a nondeterministic Turing machine that solves it in polynomial time, and for any problem instance x , there are at most ${\mathsf {poly}}(|x|)$ accepting paths for the machine.

Intuitively, this is the class of decision problems that, if false, has no witnesses, and if true, has only polynomially many witnesses (thus "few"). Contrast this with the full class of NP problems, where if true, there could be exponentially many witnesses. An even more restrictive class is UP ("unambiguous NP"), the class of decision problems with at most 1 witness.

The class is quite small, as FewP ⊆ ⊕P, which implies that FewP is low for ⊕P. Also, FewP is low for PP.

### Other classes

GapP is obtained by closing #P under subtraction. That is, it asks: "Given a problem instance, what is the number of solutions minus the number of non-solutions?". Here, the non-solutions must be taken from the set of potential solutions. This is defined in the same way as in the PP class. This difference is called the "gap".

C=P asks: "Given a problem instance, is the gap zero?". It is proven to be the complement of nondeterministic quantum polynomial-time (coNQPT).

#L, C=L, ModkL, ⊕L, etc are the logspace analogs of #P, C=P, ModkP, ⊕P, etc. The matrix determinant function is #L-complete.

### Oracle machines

As for oracle machines using #P-oracles, we have ${\mathsf {PP}}^{\mathsf {PH}}\subset {\mathsf {P}}^{\#{\mathsf {P}}}={\mathsf {P}}^{\mathsf {PP}}\subset {\mathsf {PSPACE}}$ Also, ${\mathsf {PH}}\subset {\mathsf {P}}^{\#{\mathsf {P}}[1]}$ , that is, any problem in the polynomial hierarchy class is solvable in polynomial time, if we allow a *single* call to a #P-oracle. This is called Toda's theorem, and it won Seinosuke Toda the Gödel prize in 1998.

There is strong evidence that many naturally occurring counting classes (PP, C=P, ModkP, etc) are strictly harder than PH, since it is proven that if they are not strictly harder than PH, then the PH collapses, which is widely considered to be unlikely.
