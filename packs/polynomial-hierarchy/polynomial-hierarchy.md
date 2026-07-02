---
title: "Polynomial hierarchy"
source: https://en.wikipedia.org/wiki/Polynomial_hierarchy
domain: polynomial-hierarchy
license: CC-BY-SA-4.0
tags: polynomial hierarchy, oracle machine, quantified boolean formula, sigma level
fetched: 2026-07-02
---

# Polynomial hierarchy

In computational complexity theory, the **polynomial hierarchy** (sometimes called the **polynomial-time hierarchy**) is a hierarchy of complexity classes that generalize the classes **NP** and **co-NP**. Each class in the hierarchy is contained within **PSPACE**. The hierarchy can be defined using oracle machines or alternating Turing machines. It is a resource-bounded counterpart to the arithmetical hierarchy and analytical hierarchy from mathematical logic. The union of the classes in the hierarchy is denoted **PH**.

Classes within the hierarchy have complete problems (with respect to polynomial-time reductions) that ask if quantified Boolean formulae hold, for formulae with restrictions on the quantifier order. It is known that equality between classes on the same level or consecutive levels in the hierarchy would imply a "collapse" of the hierarchy to that level.

## Definitions

There are multiple equivalent definitions of the classes of the polynomial hierarchy.

### Oracle definition

For the oracle definition of the polynomial hierarchy, define

$\Delta _{0}^{\mathrm {P} }:=\Sigma _{0}^{\mathrm {P} }:=\Pi _{0}^{\mathrm {P} }:=\mathrm {P} ,$

where P is the set of decision problems solvable in polynomial time. Then for i^n ≥ 0 define

$\Delta _{i+1}^{\mathrm {P} }:=\mathrm {P} ^{\Sigma _{i}^{\mathrm {P} }}$

$\Sigma _{i+1}^{\mathrm {P} }:=\mathrm {NP} ^{\Sigma _{i}^{\mathrm {P} }}$

$\Pi _{i+1}^{\mathrm {P} }:=\mathrm {coNP} ^{\Sigma _{i}^{\mathrm {P} }}$

where $\mathrm {P} ^{\rm {A}}$ is the set of decision problems solvable in polynomial time by a Turing machine augmented by an oracle for some complete problem in class A; the classes $\mathrm {NP} ^{\rm {A}}$ and $\mathrm {coNP} ^{\rm {A}}$ are defined analogously. For example, $\Sigma _{1}^{\mathrm {P} }=\mathrm {NP} ,\Pi _{1}^{\mathrm {P} }=\mathrm {coNP}$ , and $\Delta _{2}^{\mathrm {P} }=\mathrm {P^{NP}}$ is the class of problems solvable in polynomial time by a deterministic Turing machine with an oracle for some NP-complete problem.

### Quantified Boolean formulae definition

For the existential/universal definition of the polynomial hierarchy, let L be a language (i.e. a decision problem, a subset of {0,1}*), let p be a polynomial, and define

$\exists ^{p}L:=\left\{x\in \{0,1\}^{*}\ \left|\ \left(\exists w\in \{0,1\}^{\leq p(|x|)}\right)\langle x,w\rangle \in L\right.\right\},$

where $\langle x,w\rangle \in \{0,1\}^{*}$ is some standard encoding of the pair of binary strings *x* and *w* as a single binary string. The language *L* represents a set of ordered pairs of strings, where the first string *x* is a member of $\exists ^{p}L$ , and the second string *w* is a "short" ( $|w|\leq p(|x|)$ ) witness testifying that *x* is a member of $\exists ^{p}L$ . In other words, $x\in \exists ^{p}L$ if and only if there exists a short witness *w* such that $\langle x,w\rangle \in L$ . Similarly, define

$\forall ^{p}L:=\left\{x\in \{0,1\}^{*}\ \left|\ \left(\forall w\in \{0,1\}^{\leq p(|x|)}\right)\langle x,w\rangle \in L\right.\right\}$

Note that De Morgan's laws hold: $\left(\exists ^{p}L\right)^{\rm {c}}=\forall ^{p}L^{\rm {c}}$ and $\left(\forall ^{p}L\right)^{\rm {c}}=\exists ^{p}L^{\rm {c}}$ , where *L*c is the complement of *L*.

Let C be a class of languages. Extend these operators to work on whole classes of languages by the definition

$\exists ^{\mathrm {P} }{\mathcal {C}}:=\left\{\exists ^{p}L\ |\ p{\text{ is a polynomial and }}L\in {\mathcal {C}}\right\}$

$\forall ^{\mathrm {P} }{\mathcal {C}}:=\left\{\forall ^{p}L\ |\ p{\text{ is a polynomial and }}L\in {\mathcal {C}}\right\}$

Again, De Morgan's laws hold: $\mathrm {co} \exists ^{\mathrm {P} }{\mathcal {C}}=\forall ^{\mathrm {P} }\mathrm {co} {\mathcal {C}}$ and $\mathrm {co} \forall ^{\mathrm {P} }{\mathcal {C}}=\exists ^{\mathrm {P} }\mathrm {co} {\mathcal {C}}$ , where $\mathrm {co} {\mathcal {C}}=\left\{L^{c}|L\in {\mathcal {C}}\right\}$ .

The classes **NP** and **co-NP** can be defined as $\mathrm {NP} =\exists ^{\mathrm {P} }\mathrm {P}$ , and $\mathrm {coNP} =\forall ^{\mathrm {P} }\mathrm {P}$ , where **P** is the class of all feasibly (polynomial-time) decidable languages. The polynomial hierarchy can be defined recursively as

$\Sigma _{0}^{\mathrm {P} }:=\Pi _{0}^{\mathrm {P} }:=\mathrm {P}$

$\Sigma _{k+1}^{\mathrm {P} }:=\exists ^{\mathrm {P} }\Pi _{k}^{\mathrm {P} }$

$\Pi _{k+1}^{\mathrm {P} }:=\forall ^{\mathrm {P} }\Sigma _{k}^{\mathrm {P} }$

Note that $\mathrm {NP} =\Sigma _{1}^{\mathrm {P} }$ , and $\mathrm {coNP} =\Pi _{1}^{\mathrm {P} }$ .

This definition reflects the close connection between the polynomial hierarchy and the arithmetical hierarchy, where **R** and **RE** play roles analogous to **P** and **NP**, respectively. The analytic hierarchy is also defined in a similar way to give a hierarchy of subsets of the real numbers.

### Alternating Turing machines definition

An alternating Turing machine is a non-deterministic Turing machine with non-final states partitioned into existential and universal states. It is eventually accepting from its current configuration if: it is in an existential state and can transition into some eventually accepting configuration; or, it is in a universal state and every transition is into some eventually accepting configuration; or, it is in an accepting state.

We define $\Sigma _{k}^{\mathrm {P} }$ to be the class of languages accepted by an alternating Turing machine in polynomial time such that the initial state is an existential state and every path the machine can take swaps at most *k* – 1 times between existential and universal states. We define $\Pi _{k}^{\mathrm {P} }$ similarly, except that the initial state is a universal state.

If we omit the requirement of at most *k* – 1 swaps between the existential and universal states, so that we only require that our alternating Turing machine runs in polynomial time, then we have the definition of the class **AP**, which is equal to **PSPACE**.

## Relations between classes in the polynomial hierarchy

The union of all classes in the polynomial hierarchy is the complexity class **PH**.

The definitions imply the relations:

$\Sigma _{i}^{\mathrm {P} }\subseteq \Delta _{i+1}^{\mathrm {P} }\subseteq \Sigma _{i+1}^{\mathrm {P} }$

$\Pi _{i}^{\mathrm {P} }\subseteq \Delta _{i+1}^{\mathrm {P} }\subseteq \Pi _{i+1}^{\mathrm {P} }$

$\Sigma _{i}^{\mathrm {P} }=\mathrm {co} \Pi _{i}^{\mathrm {P} }$

Unlike the arithmetic and analytic hierarchies, whose inclusions are known to be proper, it is an open question whether any of these inclusions are proper, though it is widely believed that they all are. If any $\Sigma _{k}^{\mathrm {P} }=\Sigma _{k+1}^{\mathrm {P} }$ , or if any $\Sigma _{k}^{\mathrm {P} }=\Pi _{k}^{\mathrm {P} }$ , then the hierarchy *collapses to level k*: for all $i>k$ , $\Sigma _{i}^{\mathrm {P} }=\Sigma _{k}^{\mathrm {P} }$ . In particular, we have the following implications involving unsolved problems:

- **P** = **NP** if and only if **P** = **PH**.
- If **NP** = **co-NP** then **NP** = **PH**. (**co-NP** is $\Pi _{1}^{\mathrm {P} }$ .)

The case in which **NP** = **PH** is also termed as a *collapse* of the **PH** to *the second level*. The case **P** = **NP** corresponds to a collapse of **PH** to **P**.

Unsolved problem in computer science

⁠

$\mathrm {P} {\overset {?}{=}}\mathrm {NP}$

⁠

More unsolved problems in computer science

The question of collapse to the first level is generally thought to be extremely difficult. Most researchers do not believe in a collapse, even to the second level.

## Relationships to other classes

Unsolved problem in computer science

⁠

$\mathrm {PH} {\overset {?}{=}}\mathrm {PSPACE}$

⁠

More unsolved problems in computer science

The polynomial hierarchy is an analogue (at much lower complexity) of the exponential hierarchy and arithmetical hierarchy.

It is known that PH is contained within PSPACE, but it is not known whether the two classes are equal. One useful reformulation of this problem is that PH = PSPACE if and only if second-order logic over finite structures gains no additional power from the addition of a transitive closure operator over relations of relations (i.e., over the second-order variables).

If the polynomial hierarchy has any complete problems, then it has only finitely many distinct levels. Since there are PSPACE-complete problems, we know that if PSPACE = PH, then the polynomial hierarchy must collapse, since a PSPACE-complete problem would be a $\Sigma _{k}^{\mathrm {P} }$ -complete problem for some *k*.

Each class in the polynomial hierarchy contains $\leq _{\rm {m}}^{\mathrm {P} }$ -complete problems (problems complete under polynomial-time many-one reductions). Furthermore, each class in the polynomial hierarchy is *closed under $\leq _{\rm {m}}^{\mathrm {P} }$ -reductions*: meaning that for a class C in the hierarchy and a language $L\in {\mathcal {C}}$ , if $A\leq _{\rm {m}}^{\mathrm {P} }L$ , then $A\in {\mathcal {C}}$ as well. These two facts together imply that if $K_{i}$ is a complete problem for $\Sigma _{i}^{\mathrm {P} }$ , then $\Sigma _{i+1}^{\mathrm {P} }=\mathrm {NP} ^{K_{i}}$ , and $\Pi _{i+1}^{\mathrm {P} }=\mathrm {coNP} ^{K_{i}}$ . For instance, $\Sigma _{2}^{\mathrm {P} }=\mathrm {NP} ^{\mathrm {SAT} }$ . In other words, if a language is defined based on some oracle in C, then we can assume that it is defined based on a complete problem for C. Complete problems therefore act as "representatives" of the class for which they are complete.

- Sipser–Lautemann theorem: $\mathrm {BPP} \subset \Sigma _{2}^{\mathrm {P} }\cap \Pi _{2}^{\mathrm {P} }$ .
- Kannan's theorem: $\forall k,\Sigma _{2}\not \subset \mathrm {SIZE} (n^{k})$ . It is an open question whether $\Sigma _{2}\not \subset \bigcup _{k}\mathrm {SIZE} (n^{k})=\mathrm {P/poly}$ .
- Toda's theorem: $\mathrm {PH} \subset \mathrm {P} ^{\mathrm {\#P} }$ .

There is some evidence that BQP, the class of problems solvable in polynomial time by a quantum computer, is not contained in PH; however, it is also believed that PH is not contained in BQP.

## Problems

- An example of a natural problem in $\Sigma _{2}^{\mathrm {P} }$ is *circuit minimization*: given a number *k* and a circuit *A* computing a Boolean function *f*, determine if there is a circuit with at most *k* gates that computes the same function *f*. Let C be the set of all boolean circuits. The language $L=\left\{\langle A,k,B,x\rangle \in {\mathcal {C}}\times \mathbb {N} \times {\mathcal {C}}\times \{0,1\}^{*}\left|B{\text{ has at most }}k{\text{ gates, and }}A(x)=B(x)\right.\right\}$ is decidable in polynomial time. The language ${\mathit {CM}}=\left\{\langle A,k\rangle \in {\mathcal {C}}\times \mathbb {N} \left|{\begin{matrix}{\text{there exists a circuit }}B{\text{ with at most }}k{\text{ gates }}\\{\text{ such that }}A{\text{ and }}B{\text{ compute the same function}}\end{matrix}}\right.\right\}$ is the circuit minimization language. ${\mathit {CM}}\in \Sigma _{2}^{\mathrm {P} }(=\exists ^{\mathrm {P} }\forall ^{\mathrm {P} }\mathrm {P} )$ because L is decidable in polynomial time and because, given $\langle A,k\rangle$ , $\langle A,k\rangle \in {\mathit {CM}}$ if and only if *there exists* a circuit B such that *for all* inputs x, $\langle A,k,B,x\rangle \in L$ .
- A complete problem for $\Sigma _{k}^{\mathrm {P} }$ is **satisfiability for quantified Boolean formulas with *k* – 1 alternations of quantifiers** (abbreviated **QBFk** or **QSATk**). This is the version of the boolean satisfiability problem for $\Sigma _{k}^{\mathrm {P} }$ . In this problem, we are given a Boolean formula *f* with variables partitioned into *k* sets *X*1, ..., *Xk*. We have to determine if it is true that $\exists X_{1}\forall X_{2}\exists X_{3}\ldots f$ That is, is there an assignment of values to variables in *X*1 such that, for all assignments of values in *X*2, there exists an assignment of values to variables in *X*3, ... *f* is true? The variant above is complete for $\Sigma _{k}^{\mathrm {P} }$ . The variant in which the first quantifier is "for all", the second is "exists", etc., is complete for $\Pi _{k}^{\mathrm {P} }$ . Each language is a subset of the problem obtained by removing the restriction of *k* – 1 alternations, the **PSPACE**-complete problem TQBF.
- A Garey/Johnson-style list of problems known to be complete for the second and higher levels of the polynomial hierarchy can be found in this Compendium.
