---
title: "Ramification (mathematics)"
source: https://en.wikipedia.org/wiki/Ramification_(mathematics)
domain: algebraic-number-theory
license: CC-BY-SA-4.0
tags: algebraic number theory, ring of integers, ideal class group, dedekind domain
fetched: 2026-07-02
---

# Ramification (mathematics)

In geometry, **ramification** is 'branching out', in the way that the square root function, for complex numbers, can be seen to have two *branches* differing in sign. The term is also used from the opposite perspective (branches coming together) as when a covering map degenerates at a point of a space, with some collapsing of the fibers of the mapping.

Ramification is the main object of study in **ramification theory**.

## In complex analysis

In complex analysis, the basic model can be taken as the *z* → *z**n* mapping in the complex plane, near *z* = 0. This is the standard local picture in Riemann surface theory, of ramification of order *n*. It occurs for example in the Riemann–Hurwitz formula for the effect of mappings on the genus.

## In algebraic topology

In a covering map the Euler–Poincaré characteristic should multiply by the number of sheets; ramification can therefore be detected by some dropping from that. The *z* → *z**n* mapping shows this as a local pattern: if we exclude 0, looking at 0 < |*z*| < 1 say, we have (from the homotopy point of view) the circle mapped to itself by the *n*-th power map (Euler–Poincaré characteristic 0), but with the whole disk the Euler–Poincaré characteristic is 1, *n* − 1 being the 'lost' points as the *n* sheets come together at *z* = 0.

In geometric terms, ramification is something that happens in *codimension two* (like knot theory, and monodromy); since *real* codimension two is *complex* codimension one, the local complex example sets the pattern for higher-dimensional complex manifolds. In complex analysis, sheets can't simply fold over along a line (one variable), or codimension one subspace in the general case. The ramification set (branch locus on the base, double point set above) will be two real dimensions lower than the ambient manifold, and so will not separate it into two 'sides', locally―there will be paths that trace round the branch locus, just as in the example. In algebraic geometry over any field, by analogy, it also happens in algebraic codimension one.

## In algebraic number theory

### In algebraic extensions of the rational numbers

Ramification in algebraic number theory means a prime ideal factoring in an extension so as to give some repeated prime ideal factors. Namely, let ${\mathcal {O}}_{K}$ be the ring of integers of an algebraic number field K , and ${\mathfrak {p}}$ a prime ideal of ${\mathcal {O}}_{K}$ . For a field extension $L/K$ we can consider the ring of integers ${\mathcal {O}}_{L}$ (which is the integral closure of ${\mathcal {O}}_{K}$ in L ), and the ideal ${\mathfrak {p}}{\mathcal {O}}_{L}$ of ${\mathcal {O}}_{L}$ . This ideal may or may not be prime, but for finite $[L:K]$ , it has a factorization into prime ideals:

${\mathfrak {p}}\cdot {\mathcal {O}}_{L}={\mathfrak {p}}_{1}^{e_{1}}\cdots {\mathfrak {p}}_{k}^{e_{k}}$

where the ${\mathfrak {p}}_{i}$ are distinct prime ideals of ${\mathcal {O}}_{L}$ . Then ${\mathfrak {p}}$ is said to **ramify** in L if $e_{i}>1$ for some i ; otherwise it is **unramified**. In other words, ${\mathfrak {p}}$ ramifies in L if the **ramification index** $e_{i}$ is greater than one for some ${\mathfrak {p}}_{i}$ . An equivalent condition is that ${\mathcal {O}}_{L}/{\mathfrak {p}}{\mathcal {O}}_{L}$ has a non-zero nilpotent element: it is not a product of finite fields. The analogy with the Riemann surface case was already pointed out by Richard Dedekind and Heinrich M. Weber in the nineteenth century.

The ramification is encoded in K by the relative discriminant and in L by the relative different. The former is an ideal of ${\mathcal {O}}_{K}$ and is divisible by ${\mathfrak {p}}$ if and only if some ideal ${\mathfrak {p}}_{i}$ of ${\mathcal {O}}_{L}$ dividing ${\mathfrak {p}}$ is ramified. The latter is an ideal of ${\mathcal {O}}_{L}$ and is divisible by the prime ideal ${\mathfrak {p}}_{i}$ of ${\mathcal {O}}_{L}$ precisely when ${\mathfrak {p}}_{i}$ is ramified.

The ramification is **tame** when the ramification indices $e_{i}$ are all relatively prime to the residue characteristic *p* of ${\mathfrak {p}}$ , otherwise **wild**. This condition is important in Galois module theory. A finite generically étale extension $B/A$ of Dedekind domains is tame if and only if the trace $\operatorname {Tr} :B\to A$ is surjective.

### In local fields

The more detailed analysis of ramification in number fields can be carried out using extensions of the p-adic numbers, because it is a *local* question. In that case a quantitative measure of ramification is defined for Galois extensions, basically by asking how far the Galois group moves field elements with respect to the metric. A sequence of ramification groups is defined, reifying (amongst other things) *wild* (non-tame) ramification. This goes beyond the geometric analogue.

## In algebra

In valuation theory, the ramification theory of valuations studies the set of extensions of a valuation of a field *K* to an extension field of *K*. This generalizes the notions in algebraic number theory, local fields, and Dedekind domains.

## In algebraic geometry

There is also corresponding notion of unramified morphism in algebraic geometry. It serves to define étale morphisms.

Let $f:X\to Y$ be a morphism of schemes. The support of the quasicoherent sheaf $\Omega _{X/Y}$ is called the **ramification locus** of f and the image of the ramification locus, $f\left(\operatorname {Supp} \Omega _{X/Y}\right)$ , is called the **branch locus** of f . If $\Omega _{X/Y}=0$ we say that f is **formally unramified** and if f is also of locally finite presentation we say that f is **unramified** (see Vakil 2017).
