---
title: "PSPACE"
source: https://en.wikipedia.org/wiki/PSPACE
domain: interactive-proofs
license: CC-BY-SA-4.0
tags: interactive proof system, arthur merlin protocol, ip pspace theorem, public coin protocol
fetched: 2026-07-02
---

# PSPACE

Unsolved problem in computer science

⁠

${\mathsf {P{\overset {?}{=}}PSPACE}}$

⁠

More unsolved problems in computer science

In computational complexity theory, **PSPACE** is the set of all decision problems that can be solved by a Turing machine using a polynomial amount of space.

## Formal definition

If we denote by ${\mathsf {SPACE}}(f(n))$ the set of all problems that can be solved by Turing machines using $O(f(n))$ space for some function f of the input size n , then we can define ${\mathsf {PSPACE}}$ formally as

${\mathsf {PSPACE}}=\bigcup _{k\in \mathbb {N} }{\mathsf {SPACE}}(n^{k}).$

It turns out that allowing the Turing machine to be nondeterministic does not add any extra power. Because of Savitch's theorem, ${\mathsf {NPSPACE}}$ is equivalent to ${\mathsf {PSPACE}}$ , because a deterministic Turing machine can simulate a nondeterministic Turing machine while roughly squaring the amount of space, and squaring takes polynomials to (bigger) polynomials. Also, the complements of all problems in ${\mathsf {PSPACE}}$ are also in ${\mathsf {PSPACE}}$ , meaning that ${\mathsf {coPSPACE}}={\mathsf {PSPACE}}$ .

## Relation among other classes

The following relations are known between PSPACE and the complexity classes NL, P, NP, PH, EXPTIME and EXPSPACE (we use here $\subset$ to denote strict containment, meaning a proper subset, whereas $\subseteq$ includes the possibility that the two sets are the same):

${\begin{array}{l}{\mathsf {NL\subseteq P\subseteq NP\subseteq PH\subseteq PSPACE}}\\{\mathsf {PSPACE\subseteq EXPTIME\subseteq EXPSPACE}}\\{\mathsf {NL\subset PSPACE\subset EXPSPACE}}\\{\mathsf {P\subset EXPTIME}}\end{array}}$

From the third line, it follows that both in the first and in the second line, at least one of the set containments must be strict, but it is not known which. It is widely suspected that all are strict.

The containments in the third line are both known to be strict. The first follows from direct diagonalization (the space hierarchy theorem, NL ⊂ NPSPACE) and the fact that PSPACE = NPSPACE via Savitch's theorem. The second follows simply from the space hierarchy theorem.

The hardest problems in PSPACE are the PSPACE-complete problems. See PSPACE-complete for examples of problems that are suspected to be in PSPACE but not in NP.

## Closure properties

The class PSPACE is closed under operations union, complementation, and Kleene star.

## Other characterizations

An alternative characterization of PSPACE is the set of problems decidable by an alternating Turing machine in polynomial time, sometimes called APTIME or just AP.

A logical characterization of PSPACE from descriptive complexity theory is that it is the set of problems expressible in second-order logic with the addition of a transitive closure operator. A full transitive closure is not needed; a commutative transitive closure and even weaker forms suffice. It is the addition of this operator that (possibly) distinguishes PSPACE from PH.

A major result of complexity theory is that PSPACE can be characterized as all the languages recognizable by a particular interactive proof system, the one defining the class IP. In this system, there is an all-powerful prover trying to convince a randomized polynomial-time verifier that a string is in the language. It should be able to convince the verifier with high probability if the string is in the language, but should not be able to convince it except with low probability if the string is not in the language.

PSPACE can be characterized as the quantum complexity class QIP.

PSPACE is also equal to PCTC, problems solvable by classical computers using closed timelike curves, as well as to BQPCTC, problems solvable by quantum computers using closed timelike curves.

## PSPACE-completeness

A language *B* is *PSPACE-complete* if it is in PSPACE and it is PSPACE-hard, which means for all *A* ∈ PSPACE, $A\leq _{\text{P}}B$ , where $A\leq _{\text{P}}B$ means that there is a polynomial-time many-one reduction from *A* to *B*. PSPACE-complete problems are of great importance to studying PSPACE problems because they represent the most difficult problems in PSPACE. Finding a simple solution to a PSPACE-complete problem would mean we have a simple solution to all other problems in PSPACE because all PSPACE problems could be reduced to a PSPACE-complete problem.

An example of a PSPACE-complete problem is the quantified Boolean formula problem (usually abbreviated to **QBF** or **TQBF**; the **T** stands for "true").
