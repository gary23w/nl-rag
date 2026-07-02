---
title: "Jones polynomial"
source: https://en.wikipedia.org/wiki/Jones_polynomial
domain: knot-theory
license: CC-BY-SA-4.0
tags: knot theory, knot invariant, jones polynomial, braid group
fetched: 2026-07-02
---

# Jones polynomial

In the mathematical field of knot theory, the **Jones polynomial** is a knot polynomial discovered by Vaughan Jones in 1984. Specifically, it is an invariant of an oriented knot or link which assigns to each oriented knot or link a Laurent polynomial in the variable $t^{1/2}$ with integer coefficients.

## Definition by the bracket

Suppose we have an oriented link L , given as a knot diagram. We will define the Jones polynomial $V(L)$ by using Louis Kauffman's bracket polynomial, which we denote by $\langle ~\rangle$ . Here the bracket polynomial is a Laurent polynomial in the variable A with integer coefficients.

First, we define the auxiliary polynomial (also known as the normalized bracket polynomial)

$X(L)=(-A^{3})^{-w(L)}\langle L\rangle ,$

where $w(L)$ denotes the writhe of L in its given diagram. The writhe of a diagram is the number of positive crossings ( $L_{+}$ in the figure below) minus the number of negative crossings ( $L_{-}$ ). The writhe is not a knot invariant.

$X(L)$ is a knot invariant since it is invariant under changes of the diagram of L by the three Reidemeister moves. Invariance under type II and III Reidemeister moves follows from invariance of the bracket under those moves. The bracket polynomial is known to change by a factor of $-A^{\pm 3}$ under a type I Reidemeister move. The definition of the X polynomial given above is designed to nullify this change, since the writhe changes appropriately by $+1$ or $-1$ under type I moves.

Now make the substitution $A=t^{-1/4}$ in $X(L)$ to get the Jones polynomial $V(L)$ . This results in a Laurent polynomial with integer coefficients in the variable $t^{1/2}$ .

### Jones polynomial for tangles

This construction of the Jones polynomial for tangles is a simple generalization of the Kauffman bracket of a link. The construction was developed by Vladimir Turaev and published in 1990.

Let k be a non-negative integer and $S_{k}$ denote the set of all isotopic types of tangle diagrams, with $2k$ ends, having no crossing points and no closed components (smoothings). Turaev's construction makes use of the previous construction for the Kauffman bracket and associates to each $2k$ -end oriented tangle an element of the free $\mathrm {R}$ -module $\mathrm {R} [S_{k}]$ , where $\mathrm {R}$ is the ring of Laurent polynomials with integer coefficients in the variable $t^{1/2}$ .

## Definition by braid representation

Jones' original formulation of his polynomial came from his study of operator algebras. In Jones' approach, it resulted from a kind of "trace" of a particular braid representation into an algebra which originally arose while studying certain models, e.g. the Potts model, in statistical mechanics.

Let a link *L* be given. A theorem of Alexander states that it is the trace closure of a braid, say with *n* strands. Now define a representation $\rho$ of the braid group on *n* strands, *Bn*, into the Temperley–Lieb algebra $\operatorname {TL} _{n}$ with coefficients in $\mathbb {Z} [A,A^{-1}]$ and $\delta =-A^{2}-A^{-2}$ . The standard braid generator $\sigma _{i}$ is sent to $A\cdot e_{i}+A^{-1}\cdot 1$ , where $1,e_{1},\dots ,e_{n-1}$ are the standard generators of the Temperley–Lieb algebra. It can be checked easily that this defines a representation.

Take the braid word $\sigma$ obtained previously from L and compute $\delta ^{n-1}\operatorname {tr} \rho (\sigma )$ where $\operatorname {tr}$ is the Markov trace. This gives $\langle L\rangle$ , where $\langle$ $\rangle$ is the bracket polynomial. This can be seen by considering, as Louis Kauffman did, the Temperley–Lieb algebra as a particular diagram algebra.

An advantage of this approach is that one can pick similar representations into other algebras, such as the *R*-matrix representations, leading to "generalized Jones invariants".

## Properties

The Jones polynomial is characterized by taking the value 1 on any diagram of the unknot and satisfies the following skein relation:

$(t^{1/2}-t^{-1/2})V(L_{0})=t^{-1}V(L_{+})-tV(L_{-})\,$

where $L_{+}$ , $L_{-}$ , and $L_{0}$ are three oriented link diagrams that are identical except in one small region where they differ by the crossing changes or smoothing shown in the figure below:

The definition of the Jones polynomial by the bracket makes it simple to show that for a knot K , the Jones polynomial of its mirror image is given by substitution of $t^{-1}$ for t in $V(K)$ . Thus, an amphicheiral knot, a knot equivalent to its mirror image, has palindromic entries in its Jones polynomial. See the article on skein relation for an example of a computation using these relations.

Another remarkable property of this invariant states that the Jones polynomial of an alternating link is an alternating polynomial. This property was proved by Morwen Thistlethwaite in 1987. Another proof of this last property is due to Hernando Burgos-Soto, who also gave an extension of the property to tangles.

The Jones polynomial is not a complete invariant. There exist an infinite number of non-equivalent knots that have the same Jones polynomial. An example of two distinct knots having the same Jones polynomial can be found in the book by Murasugi.

## Colored Jones polynomial

For a positive integer N , the N -colored Jones polynomial $V_{N}(L,t)$ is a generalisation of the Jones polynomial. It is the Reshetikhin–Turaev invariant associated with the $(N+1)$ -irreducible representation of the quantum group $U_{q}({\mathfrak {sl}}_{2})$ . In this scheme, the Jones polynomial is the 1-colored Jones polynomial, the Reshetikhin-Turaev invariant associated to the standard representation (irreducible and two-dimensional) of $U_{q}({\mathfrak {sl}}_{2})$ . One thinks of the strands of a link as being "colored" by a representation, hence the name.

More generally, given a link L of k components and representations $V_{1},\ldots ,V_{k}$ of $U_{q}({\mathfrak {sl}}_{2})$ , the $(V_{1},\ldots ,V_{k})$ -colored Jones polynomial $V_{V_{1},\ldots ,V_{k}}(L,t)$ is the Reshetikhin–Turaev invariant associated to $V_{1},\ldots ,V_{k}$ (here we assume the components are ordered). Given two representations V and W , colored Jones polynomials satisfy the following two properties:

- $V_{V\oplus W}(L,t)=V_{V}(L,t)+V_{W}(L,t)$ ,
- $V_{V\otimes W}(L,t)=V_{V,W}(L^{2},t)$ , where $L^{2}$ denotes the 2-cabling of L .

These properties are deduced from the fact that colored Jones polynomials are Reshetikhin-Turaev invariants.

Let K be a knot. Recall that by viewing a diagram of K as an element of the Temperley-Lieb algebra thanks to the Kauffman bracket, one recovers the Jones polynomial of K . Similarly, the N -colored Jones polynomial of K can be given a combinatorial description using the Jones-Wenzl idempotents, as follows:

- consider the N -cabling $K^{N}$ of K ;
- view it as an element of the Temperley-Lieb algebra;
- insert the Jones-Wenzl idempotents on some N parallel strands.

The resulting element of $\mathbb {Q} (t)$ is the N -colored Jones polynomial. See appendix H of for further details.

## Relationship to other theories

### Link with Chern–Simons theory

As first shown by Edward Witten, the Jones polynomial of a given knot $\gamma$ can be obtained by considering Chern–Simons theory on the three-sphere with gauge group $\mathrm {SU} (2)$ , and computing the vacuum expectation value of a Wilson loop $W_{F}(\gamma )$ , associated to $\gamma$ , and the fundamental representation F of $\mathrm {SU} (2)$ .

### Link with quantum knot invariants

By substituting $e^{h}$ for the variable t of the Jones polynomial and expanding it as the series of h each of the coefficients turn to be the Vassiliev invariant of the knot K . In order to unify the Vassiliev invariants (or, finite type invariants), Maxim Kontsevich constructed the Kontsevich integral. The value of the Kontsevich integral, which is the infinite sum of 1, 3-valued chord diagrams, named the Jacobi chord diagrams, reproduces the Jones polynomial along with the ${\mathfrak {sl}}_{2}$ weight system studied by Dror Bar-Natan.

### Link with the volume conjecture

By numerical examinations on some hyperbolic knots, Rinat Kashaev discovered that substituting the *n*-th root of unity into the parameter of the colored Jones polynomial corresponding to the *n*-dimensional representation, and limiting it as *n* grows to infinity, the limit value would give the hyperbolic volume of the knot complement. (See Volume conjecture.)

### Link with Khovanov homology

In 2000 Mikhail Khovanov constructed a certain chain complex for knots and links and showed that the homology induced from it is a knot invariant (see Khovanov homology). The Jones polynomial is described as the Euler characteristic for this homology.

## Detection of the unknot

It is an open question whether there is a nontrivial knot with Jones polynomial equal to that of the unknot. It is known that there are nontrivial *links* with Jones polynomial equal to that of the corresponding unlinks by the work of Morwen Thistlethwaite. The simplest such example has 15 essential crossings and consists of a trefoil knot linked to a figure-eight knot. Every prime knot with up to 24 crossings, of which there are over three hundred million, is known to have a non-trivial Jones polynomial. This was determined by computing the Jones polynomial of several trillion knot diagrams, and verifying those diagrams with trivial Jones polynomials corresponded to trivial knots. It was shown by Kronheimer and Mrowka that there is no nontrivial knot with Khovanov homology equal to that of the unknot. While no nontrivial knot is known to have the same Jones polynomial as the unknot, two or more knots may have the same Jones polynomial and require other invariants to distinguish them. Examples include the Conway knot and the Kinoshita-Terasaka knot, with 11 crossings.
