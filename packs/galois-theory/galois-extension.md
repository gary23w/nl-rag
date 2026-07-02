---
title: "Galois extension"
source: https://en.wikipedia.org/wiki/Galois_extension
domain: galois-theory
license: CC-BY-SA-4.0
tags: galois theory, galois group, field extension, solvable group
fetched: 2026-07-02
---

# Galois extension

In mathematics, a **Galois extension** is an algebraic field extension *E*/*F* that is normal and separable; or equivalently, *E*/*F* is algebraic, and the field fixed by the automorphism group Aut(*E*/*F*) is precisely the base field *F*. The significance of being a Galois extension is that the extension has a Galois group and obeys the fundamental theorem of Galois theory.

A result of Emil Artin allows one to construct Galois extensions as follows: If *E* is a given field, and *G* is a finite group of automorphisms of *E* with fixed field *F*, then *E*/*F* is a Galois extension.

The property of an extension being Galois behaves well with respect to field composition and intersection.

## Characterization of Galois extensions

An important theorem of Emil Artin states that for a finite extension $E/F$ , each of the following statements is equivalent to the statement that $E/F$ is Galois:

- $E/F$ is a normal extension and a separable extension.
- E is a splitting field of a set of separable polynomials with coefficients in F .
- $|\!\operatorname {Aut} (E/F)|=[E:F]$ , that is, the number of automorphisms equals the degree of the extension.

Other equivalent statements are:

- Every irreducible polynomial in $F[x]$ with at least one root in E splits over E and is separable.
- $|\!\operatorname {Aut} (E/F)|\geq [E:F]$ , that is, the number of automorphisms is at least the degree of the extension.
- F is the fixed field of a subgroup of $\operatorname {Aut} (E)$ .
- F is the fixed field of $\operatorname {Aut} (E/F)$ .
- There is a one-to-one correspondence between subfields of $E/F$ and subgroups of $\operatorname {Aut} (E/F)$ .

An infinite field extension $E/F$ is Galois if and only if E is the union of finite Galois subextensions $E_{i}/F$ indexed by an (infinite) index set I , i.e. $E=\bigcup _{i\in I}E_{i}$ and the Galois group is an inverse limit $\operatorname {Aut} (E/F)=\varprojlim _{i\in I}{\operatorname {Aut} (E_{i}/F)}$ where the inverse system is ordered by field inclusion $E_{i}\subset E_{j}$ .

## Examples

There are two basic ways to construct examples of Galois extensions.

- Take any field E , any finite subgroup of $\operatorname {Aut} (E)$ , and let F be the fixed field.
- Take any field F , any separable polynomial in $F[x]$ , and let E be its splitting field.

Adjoining to the rational number field the square root of 2 gives a Galois extension, while adjoining the cubic root of 2 gives a non-Galois extension. Both these extensions are separable, because they have characteristic zero. The first of them is the splitting field of $x^{2}-2$ ; the second has normal closure that includes the complex cubic roots of unity, and so is not a splitting field. In fact, it has no automorphism other than the identity, because it is contained in the real numbers and $x^{3}-2$ has just one real root. For more detailed examples, see the page on the fundamental theorem of Galois theory.

An algebraic closure ${\bar {K}}$ of an arbitrary field K is Galois over K if and only if K is a perfect field.
