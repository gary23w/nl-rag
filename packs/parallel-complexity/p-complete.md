---
title: "P-complete"
source: https://en.wikipedia.org/wiki/P-complete
domain: parallel-complexity
license: CC-BY-SA-4.0
tags: parallel complexity, work span model, brent theorem, p complete problem
fetched: 2026-07-02
---

# P-complete

In computational complexity theory, a decision problem is **P-complete** (complete for the complexity class **P**) if it is in **P** and every problem in **P** can be reduced to it by an appropriate reduction.

The notion of **P-complete** decision problems is useful in the analysis of which problems are difficult to parallelize effectively and which problems are difficult to solve in limited space, specifically when stronger notions of reducibility than polytime-reducibility are considered.

The specific type of reduction used varies and may affect the exact set of problems. Generically, reductions stricter than polynomial-time reductions are used, since all languages in **P** (except the empty language and the language of all strings) are **P**-complete under polynomial-time reductions. If we use **NC** reductions, that is, reductions that can operate in polylogarithmic time on a parallel computer with a polynomial number of processors, then all **P**-complete problems lie outside **NC** and so cannot be effectively parallelized, under the unproven assumption that **NC** ≠ **P**. If we use the stronger log-space reduction, this remains true, but additionally we learn that all **P**-complete problems lie outside L under the weaker unproven assumption that **L** ≠ **P**. In this latter case the set **P**-complete may be smaller.

## Motivation

The class **P**, typically taken to consist of all the "tractable" problems for a sequential computer, contains the class **NC**, which consists of those problems that can be efficiently solved on a parallel computer. This is because parallel computers can be simulated on a sequential machine. It is not known whether **NC** = **P**. In other words, it is not known whether there are any tractable problems that are inherently sequential. Just as it is widely suspected that **P** does not equal **NP**, so it is widely suspected that **NC** does not equal **P**.

Similarly, the class **L** contains all problems that can be solved by a sequential computer in logarithmic space. Such machines run in polynomial time because they can only have a polynomial number of different configurations. It is suspected that **L** ≠ **P**; that is, that some problems that can be solved in polynomial time also require more than logarithmic space.

Similarly to the use of NP-complete problems to analyze the **P** = **NP** question, the **P**-complete problems, viewed as the "probably not parallelizable" or "probably inherently sequential" problems, serves in a similar manner to study the **NC** = **P** question. Finding an efficient way to parallelize the solution to some **P**-complete problem would show that **NC** = **P**. It can also be thought of as the "problems requiring superlogarithmic space"; a log-space solution to a **P**-complete problem (using the definition based on log-space reductions) would imply **L** = **P**.

The logic behind this is analogous to the logic that a polynomial-time solution to an **NP**-complete problem would prove **P** = **NP**: if we have a **NC** reduction from any problem in **P** to a problem *A*, and an **NC** solution for *A*, then **NC** = **P**. Similarly, if we have a log-space reduction from any problem in **P** to a problem *A*, and a log-space solution for *A*, then **L** = **P**.

## Reductions

There are many different many-one reductions used when defining **P**-completeness, with variable strengths.

At the lowest level is **NC**1-reduction, then **L**-reduction, then **NC**2-reduction, **NC**3-reduction, and so on. Their union is **NC**-reduction. They are ordered since ${\mathsf {NC}}^{1}\subseteq {\mathsf {L}}\subseteq {\mathsf {NC}}^{2}\subseteq {\mathsf {NC}}^{3}\subseteq \dots \subseteq {\mathsf {NC}}$ .

For **NC***k*-reduction and **NC**-reduction, uniformity is imposed, because the intention of **P**-completeness theory is to prove upper bounds. Non-uniformity is useful for proving lower bounds, but for upper bounds, non-uniformity is unsatisfactory, since they are too powerful for this purpose. The standard uniformity condition is **L**-uniformity, meaning that the circuit family should be constructable by a Turing machine, such that given $1^{n}$ as input, it outputs a description of the n -th circuit using $O(\log n)$ working tape.

Given two languages $L,L'$ , define $L\leq _{m}^{{\mathsf {NC}}^{k}}L'$ if and only if there exists a **L**-uniform **NC***k* Boolean circuit family that together computes a function $f:\{0,1\}^{*}\to \{0,1\}^{*}$ , such that $x\in L$ if and only if $f(x)\in L'$ .

Define $L\leq _{m}^{\mathsf {NC}}L'$ if and only if $L\leq _{m}^{{\mathsf {NC}}^{k}}L'$ for some $k\geq 1$ .

Define $L\leq _{m}^{\mathsf {L}}L'$ if and only if there exists a function $f:\{0,1\}^{*}\to \{0,1\}^{*}$ that is implicitly logspace computable, such that $x\in L$ if and only if $f(x)\in L'$ .

### P-complete

Define a language L in **P** to be **P**-complete relative to **NC***k*-reduction if and only if for any language $L'$ in **P**, $L'\leq _{m}^{{\mathsf {NC}}^{k}}L$ . Similarly for the other cases.

Usually for **P**-completeness, **NC**-reduction is meant by default, though many results in the literature concerning **P**-completeness still holds even under the strongest assumption of **NC**1-reduction.

**P**-completeness is usually used thus: First, a problem is shown to be **P**-complete relative to **NC***k*-reduction. Next, assuming that the **L**-uniform **NC**k complexity class is strictly smaller than the **P** class, one immediately conclude that all **P**-complete and **P**-hard problems (assuming the same reduction type) are impossible to solve by **L**-uniform **NC**k circuit families. In other words, such problems cannot be parallelized, for a certain sense of "parallelization".

## **P**-complete problems

The most basic **P**-complete problem under logspace many-one reductions is the following: given a Turing machine M , an input for that machine *x*, and a number *T* (written in unary), $\langle M,x,T\rangle$ does that machine halt on that input within the first *T* steps? To reduce an $L\in {\mathsf {P}}$ to this problem, take a Turing Machine $M_{L}$ deciding L in time bounded by the polynomial *p*. Then for any $x\in L$ , output the encoding of $M_{L}$ , the encoding of *x* itself, and a number of steps $T=p(|x|)$ . The machine *M* halts on *x* within $p(|x|)$ steps if and only if *x* is in *L*.

Clearly, if we can parallelize a general simulation of a sequential computer (i.e. the Turing machine simulation of Turing machines), then we will be able to parallelize any program that runs on that computer. If this problem is in **NC**, then so is every other problem in **P**. If the number of steps is written in binary, the problem is EXPTIME-complete. This problem illustrates a common trick in the theory of **P**-completeness. We aren't really interested in whether a problem can be solved quickly on a parallel machine. We're just interested in whether a parallel machine solves it *much more* quickly than a sequential machine. Therefore, we have to reword the problem so that the sequential version is in **P**. That is why this problem required *T* to be written in unary. If a number *T* is written as a binary number (a string of *n* ones and zeros, where *n* = log *T*), then the obvious sequential algorithm can take time 2*n*. On the other hand, if *T* is written as a unary number (a string of *n* ones, where *n* = *T*), then it only takes time *n*. By writing *T* in unary rather than binary, we have reduced the obvious sequential algorithm from exponential time to linear time. That puts the sequential problem in **P**. Then, it will be in **NC** if and only if it is parallelizable.

Many other problems have been proved to be **P**-complete, and therefore are widely believed to be inherently sequential. These include the following problems that are **P**-complete under at least logspace reductions, either as given, or in a decision-problem form:

- Circuit value problem (CVP) – given a circuit, the inputs to the circuit, and one gate in the circuit, calculate the output of that gate.
- Restricted case of CVP – like CVP, except each gate has two inputs and two outputs (F and Not F), every other layer is just AND gates, the rest are OR gates (or, equivalently, all gates are NAND gates, or all gates are NOR gates), the inputs of a gate come from the immediately preceding layer
- Linear programming – maximize a linear function subject to linear inequality constraints
- Lexicographically first depth-first search ordering – given a graph with fixed ordered adjacency lists, and nodes *u* and *v*, is vertex *u* visited before vertex *v* in a depth-first search induced by the order of the adjacency lists?
- Context free grammar membership – given a context-free grammar and a string, can that string be generated by that grammar?
- Horn-satisfiability – given a set of Horn clauses, is there a variable assignment that satisfies them? This is **P'**s version of the Boolean satisfiability problem.
- Game of life – given an initial configuration of Conway's Game of Life, a particular cell, and a time *T* (in unary), is that cell alive after *T* steps?
- LZW (algorithm) (1978 paradigm) data compression – given strings *s* and *t*, will compressing *s* with an LZ78 method add *t* to the dictionary? (Note that for LZ77 compression such as gzip, this is much easier, as the problem reduces to "Is *t* in *s*?".)
- Type inference for partial types – given an untyped term from the lambda calculus, determine whether this term has a partial type.

Most of the languages above are **P**-complete under even stronger notions of reduction, such as uniform $AC^{0}$ many-one reductions, DLOGTIME reductions, or polylogarithmic projections.

In order to prove that a given problem in **P** is **P**-complete, one typically tries to reduce a known **P**-complete problem to the given one.

In 1999, Jin-Yi Cai and D. Sivakumar, building on work by Ogihara, showed that if there exists a sparse language that is **P**-complete, then **L** = **P**.

**P**-complete problems may be solvable with different time complexities. For instance, the circuit value problem can be solved in linear time by a topological sort. Of course, because the reductions to a **P**-complete problem may have different time complexities, this fact does not imply that all the problems in **P** can also be solved in linear time.
