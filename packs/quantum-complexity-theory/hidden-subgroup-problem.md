---
title: "Hidden subgroup problem"
source: https://en.wikipedia.org/wiki/Hidden_subgroup_problem
domain: quantum-complexity-theory
license: CC-BY-SA-4.0
tags: quantum complexity theory, quantum query complexity, quantum supremacy, qma class
fetched: 2026-07-02
---

# Hidden subgroup problem

The **hidden subgroup problem** (**HSP**) is a topic of research in mathematics and theoretical computer science. It is a generalization of problems including factoring, discrete logarithm, graph isomorphism, and the shortest vector problem. This makes it especially important in the theory of quantum computing because Shor's algorithms for factoring and finding discrete logarithms in quantum computing are instances of the hidden subgroup problem for finite abelian groups, while the other problems correspond to finite groups that are not abelian.

## Problem statement

Given a group G , a subgroup $H\leq G$ , and a set X , we say a function $f:G\to X$ **hides** the subgroup H if for all $g_{1},g_{2}\in G,f(g_{1})=f(g_{2})$ if and only if $g_{1}H=g_{2}H$ . Equivalently, f is constant on each coset of *H*, while it is different between the different cosets of *H*.

**Hidden subgroup problem**: Let G be a group, X a finite set, and $f:G\to X$ a function that hides a subgroup $H\leq G$ . The function f is given via an oracle, which uses $O(\log |G|+\log |X|)$ bits. Using information gained from evaluations of f via its oracle, determine a generating set for H .

A special case is when X is a group and f is a group homomorphism in which case H corresponds to the kernel of f .

## Motivation

The hidden subgroup problem is especially important in the theory of quantum computing for the following reasons.

- Shor's algorithm for factoring and for finding discrete logarithms (as well as several of its extensions) relies on the ability of quantum computers to solve the HSP for finite abelian groups.
- The existence of efficient quantum algorithms for HSPs for certain non-abelian groups would imply efficient quantum algorithms for two major problems: the graph isomorphism problem and certain shortest vector problems (SVPs) in lattices. More precisely, an efficient quantum algorithm for the HSP for the symmetric group would give a quantum algorithm for the graph isomorphism. An efficient quantum algorithm for the HSP for the dihedral group would give a quantum algorithm for the $\operatorname {poly} (n)$ unique SVP.

## Quantum algorithms

There is an efficient quantum algorithm for solving HSP over finite abelian groups in time polynomial in $\log |G|$ . For arbitrary groups, it is known that the hidden subgroup problem is solvable using a polynomial number of evaluations of the oracle. However, the circuits that implement this may be exponential in $\log |G|$ , making the algorithm not efficient overall; efficient algorithms must be polynomial in the number of oracle evaluations and running time. The existence of such an algorithm for arbitrary groups is open. Quantum polynomial time algorithms exist for certain subclasses of groups, such as semi-direct products of some abelian groups.

### Algorithm for abelian groups

The algorithm for abelian groups uses representations, i.e. homomorphisms from G to $\mathrm {GL} _{k}(\mathbb {C} )$ , the general linear group over the complex numbers. A representation is irreducible if it cannot be expressed as the direct product of two or more representations of G . For an abelian group, all the irreducible representations are the characters, which are the representations of dimension one; there are no irreducible representations of larger dimension for abelian groups.

#### Defining the quantum fourier transform

The quantum fourier transform can be defined in terms of $\mathrm {Z} _{N}$ , the additive cyclic group of order N . Introducing the character $\chi _{j}(k)=\omega _{N}^{jk}=e^{2\pi i{\frac {jk}{N}}},$ the quantum fourier transform has the definition of $F_{N}|j\rangle ={\frac {1}{\sqrt {N}}}\sum _{k=0}^{N-1}\chi _{j}(k)|k\rangle .$ Furthermore, we define $|\chi _{j}\rangle =F_{N}|j\rangle$ . Any finite abelian group can be written as the direct product of multiple cyclic groups $\mathrm {Z} _{N_{1}}\times \mathrm {Z} _{N_{2}}\times \ldots \times \mathrm {Z} _{N_{m}}$ . On a quantum computer, this is represented as the tensor product of multiple registers of dimensions $N_{1},N_{2},\ldots ,N_{m}$ respectively, and the overall quantum fourier transform is $F_{N_{1}}\otimes F_{N_{2}}\otimes \ldots \otimes F_{N_{m}}$ .

#### Procedure

The set of characters of G forms a group ${\widehat {G}}$ called the dual group of G . We also have a subgroup $H^{\perp }\leq {\widehat {G}}$ of size $|G|/|H|$ defined by $H^{\perp }=\{\chi _{g}:\chi _{g}(h)=1{\text{ for all }}h\in H\}$ For each iteration of the algorithm, the quantum circuit outputs an element $g\in G$ corresponding to a character $\chi _{g}\in H^{\perp }$ , and since $\chi _{g}(h)={1}$ for all $h\in H$ , it helps to pin down what H is.

The algorithm is as follows:

1. Start with the state $|0\rangle |0\rangle$ , where the left register's basis states are each element of G , and the right register's basis states are each element of X .
2. Create a superposition among the basis states of G in the left register, leaving the state ${\textstyle {\frac {1}{\sqrt {|G|}}}\sum _{g\in G}|g\rangle |0\rangle }$ .
3. Query the function f . The state afterwards is ${\textstyle {\frac {1}{\sqrt {|G|}}}\sum _{g\in G}|g\rangle |f(g)\rangle }$ .
4. Measure the output register. This gives some $f(s)$ for some $s\in G$ , and collapses the state to ${\textstyle {\frac {1}{\sqrt {|H|}}}\sum _{h\in H}|s+h\rangle |f(s)\rangle }$ because f has the same value for each element of the coset $s+{H}$ . We discard the output register to get ${\textstyle {\frac {1}{\sqrt {|H|}}}\sum _{h\in H}|s+h\rangle }$ .
5. Perform the quantum fourier transform, getting the state ${\textstyle {\frac {1}{\sqrt {|H|}}}\sum _{h\in H}|\chi _{s+h}\rangle }$ .
6. This state is equal to ${\textstyle {\sqrt {\frac {|H|}{|G|}}}\sum _{\chi _{g}\in H^{\perp }}\chi _{g}(s)|g\rangle }$ , which can be measured to learn information about H .
7. Repeat until H (or a generating set for H ) is determined.

The state in step 5 is equal to the state in step 6 because of the following: ${\begin{aligned}{\frac {1}{\sqrt {|H|}}}\sum _{h\in H}|\chi _{s+h}\rangle &={\frac {1}{\sqrt {|H||G|}}}\sum _{h\in H}\sum _{g\in G}\chi _{s+h}(g)|g\rangle \\&={\frac {1}{\sqrt {|H||G|}}}\sum _{g\in G}\chi _{s}(g)\sum _{h\in H}\chi _{h}(g)|g\rangle \\&={\frac {1}{\sqrt {|H||G|}}}\sum _{g\in G}\chi _{g}(s)\left(\sum _{h\in H}\chi _{g}(h)\right)|g\rangle \\&={\sqrt {\frac {|H|}{|G|}}}\sum _{\chi _{g}\in H^{\perp }}\chi _{g}(s)|g\rangle \end{aligned}}$ For the last equality, we use the following identity:

**Theorem**— $\sum _{h\in H}\chi _{g}(h)={\begin{cases}|H|&\chi _{g}\in H^{\perp }\\0&\chi _{g}\notin H^{\perp }\end{cases}}$

Proof

This can be derived from the orthogonality of characters. The characters of G form an orthonormal basis: ${\frac {1}{\vert H\vert }}\sum _{h\in H}\chi _{g}(h)\chi _{g'}(h)={\begin{cases}1&g=g'\\0&g\neq g'\end{cases}}$ We let $\chi _{g'}$ be the trivial representation, which maps all inputs to 1 , to get $\sum _{h\in H}\chi _{g}(h)={\begin{cases}\vert H\vert &g{\text{ is trivial}}\\0&g{\text{ is not trivial}}\end{cases}}$ Since the summation is done over H , $\chi _{g}$ also being trivial only matters for if it is trivial over H ; that is, if $\chi _{g}\in H^{\perp }$ . Thus, we know that the summation will result in $\vert H\vert$ if $\chi _{g}\in H^{\perp }$ and will result in 0 if $\chi _{g}\notin H^{\perp }$ .

Each measurement of the final state will result in some information gained about H since we know that $\chi _{g}(h)=1$ for all $h\in H$ . H , or a generating set for H , will be found after a polynomial number of measurements. The size of a generating set will be logarithmically small compared to the size of G . Let T denote a generating set for H , meaning $\langle T\rangle =H$ . The size of the subgroup generated by T will at least be doubled when a new element $t\notin T$ is added to it, because H and $t+H$ are disjoint and because $H\cup t+H\subseteq \langle \{t\}\cup T\rangle$ . Therefore, the size of a generating set $|T|$ satisfies $|T|\leq \log |H|\leq \log |G|$ Thus a generating set for H will be able to be obtained in polynomial time even if G is exponential in size.

### Instances

Many algorithms where quantum speedups occur in quantum computing are instances of the hidden subgroup problem. The following list outlines important instances of the HSP, and whether or not they are solvable.

| Problem | Quantum Algorithm | Abelian? | Polynomial time solution? |
|---|---|---|---|
| Deutsch's problem | Deutsch's algorithm; Deutsch-Jozsa algorithm | Yes | Yes |
| Simon's problem | Simon's algorithm | Yes | Yes |
| Order finding | Shor's order finding algorithm | Yes | Yes |
| Discrete logarithm | Shor's algorithm § Shor's algorithm for discrete logarithms | Yes | Yes |
| Period finding | Shor's algorithm | Yes | Yes |
| Abelian stabilizer | Kitaev's algorithm | Yes | Yes |
| Graph Isomorphism | None | No | No |
| Shortest vector problem | None | No | No |
