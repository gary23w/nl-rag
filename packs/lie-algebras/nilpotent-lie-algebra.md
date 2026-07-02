---
title: "Nilpotent Lie algebra"
source: https://en.wikipedia.org/wiki/Nilpotent_Lie_algebra
domain: lie-algebras
license: CC-BY-SA-4.0
tags: lie algebra, semisimple lie algebra, cartan subalgebra, killing form
fetched: 2026-07-02
---

# Nilpotent Lie algebra

In mathematics, a Lie algebra ${\mathfrak {g}}$ is **nilpotent** if its lower central series terminates in the zero subalgebra. The *lower central series* is the sequence of subalgebras

${\mathfrak {g}}\supseteq [{\mathfrak {g}},{\mathfrak {g}}]\supseteq [{\mathfrak {g}},[{\mathfrak {g}},{\mathfrak {g}}]]\supseteq [{\mathfrak {g}},[{\mathfrak {g}},[{\mathfrak {g}},{\mathfrak {g}}]]]\supseteq ...$

We write ${\mathfrak {g}}_{0}={\mathfrak {g}}$ , and ${\mathfrak {g}}_{n}=[{\mathfrak {g}},{\mathfrak {g}}_{n-1}]$ for all $n>0$ . If the lower central series eventually arrives at the zero subalgebra, then the Lie algebra is called nilpotent. The lower central series for Lie algebras is analogous to the lower central series in group theory, and nilpotent Lie algebras are analogs of nilpotent groups.

The nilpotent Lie algebras are precisely those that can be obtained from abelian Lie algebras, by successive central extensions.

Note that the definition means that, viewed as a non-associative non-unital algebra, a Lie algebra ${\mathfrak {g}}$ is nilpotent if it is nilpotent as an ideal.

## Definition

Let ${\mathfrak {g}}$ be a Lie algebra. One says that ${\mathfrak {g}}$ is **nilpotent** if the lower central series terminates, i.e. if ${\mathfrak {g}}_{n}=0$ for some $n\in \mathbb {N} .$

Explicitly, this means that

$[X_{1},[X_{2},[\cdots [X_{n},Y]\cdots ]]=\mathrm {ad} _{X_{1}}\mathrm {ad} _{X_{2}}\cdots \mathrm {ad} _{X_{n}}Y=0$

$\forall X_{1},X_{2},\ldots ,X_{n},Y\in {\mathfrak {g}},\qquad (1)$

so that ad*X*1ad*X*2 ⋅⋅⋅ ad*X**n* = 0.

## Equivalent conditions

A very special consequence of (1) is that

$[X,[X,[\cdots [X,Y]\cdots ]={\mathrm {ad} _{X}}^{n}Y\in {\mathfrak {g}}_{n}=0\quad \forall X,Y\in {\mathfrak {g}}.\qquad (2)$

Thus (ad*X*)*n* = 0 for all $X\in {\mathfrak {g}}$ . That is, ad*X* is a nilpotent endomorphism in the usual sense of linear endomorphisms (rather than of Lie algebras). We call such an element *X* in ${\mathfrak {g}}$ **ad-nilpotent**.

Remarkably, if ${\mathfrak {g}}$ is finite dimensional, the apparently much weaker condition (2) is actually equivalent to (1), as stated by

Engel's theorem

: A finite dimensional Lie algebra

${\mathfrak {g}}$

is nilpotent if and only if all elements of

${\mathfrak {g}}$

are ad-nilpotent,

which we will not prove here.

A somewhat easier equivalent condition for the nilpotency of ${\mathfrak {g}}$  : ${\mathfrak {g}}$ is nilpotent if and only if $\mathrm {ad} \,{\mathfrak {g}}$ is nilpotent (as a Lie algebra). To see this, first observe that (1) implies that $\mathrm {ad} \,{\mathfrak {g}}$ is nilpotent, since the expansion of an (*n* − 1)-fold nested bracket will consist of terms of the form in (1). Conversely, one may write

$[[\cdots [X_{n},X_{n-1}],\cdots ,X_{2}],X_{1}]=\mathrm {ad} [\cdots [X_{n},X_{n-1}],\cdots ,X_{2}](X_{1}),$

and since ad is a Lie algebra homomorphism,

${\begin{aligned}\mathrm {ad} [\cdots [X_{n},X_{n-1}],\cdots ,X_{2}]&=[\mathrm {ad} [\cdots [X_{n},X_{n-1}],\cdots X_{3}],\mathrm {ad} _{X_{2}}]\\&=\ldots =[\cdots [\mathrm {ad} _{X_{n}},\mathrm {ad} _{X_{n-1}}],\cdots \mathrm {ad} _{X_{2}}].\end{aligned}}$

If $\mathrm {ad} \,{\mathfrak {g}}$ is nilpotent, the last expression is zero for large enough *n*, and accordingly the first. But this implies (1), so ${\mathfrak {g}}$ is nilpotent.

Also, a finite-dimensional Lie algebra is nilpotent if and only if there exists a descending chain of ideals ${\mathfrak {g}}={\mathfrak {g}}_{0}\supset {\mathfrak {g}}_{1}\supset \cdots \supset {\mathfrak {g}}_{n}=0$ such that $[{\mathfrak {g}},{\mathfrak {g}}_{i}]\subset {\mathfrak {g}}_{i+1}$ .

## Examples

### Strictly upper triangular matrices

If ${\mathfrak {gl}}(k,\mathbb {R} )$ is the set of *k × k* matrices with entries in $\mathbb {R}$ , then the subalgebra consisting of strictly upper triangular matrices is a nilpotent Lie algebra.

### Heisenberg algebras

A Heisenberg algebra is nilpotent. For example, in dimension 3, the commutator of two matrices

> $\left[{\begin{bmatrix}0&a&b\\0&0&c\\0&0&0\end{bmatrix}},{\begin{bmatrix}0&a'&b'\\0&0&c'\\0&0&0\end{bmatrix}}\right]={\begin{bmatrix}0&0&a''\\0&0&0\\0&0&0\end{bmatrix}}$

where $a''=ac'-a'c$ .

### Cartan subalgebras

A Cartan subalgebra ${\mathfrak {c}}$ of a Lie algebra ${\mathfrak {l}}$ is nilpotent and self-normalizing page 80. The self-normalizing condition is equivalent to being the normalizer of a Lie algebra. This means ${\mathfrak {c}}=N_{\mathfrak {l}}({\mathfrak {c}})=\{x\in {\mathfrak {l}}:[x,c]\subset {\mathfrak {c}}{\text{ for }}c\in {\mathfrak {c}}\}$ . This includes all diagonal matrices ${\mathfrak {d}}(n)$ in ${\mathfrak {gl}}(n)$ .

### Other examples

If a Lie algebra ${\mathfrak {g}}$ has an automorphism of prime period with no fixed points except at 0, then ${\mathfrak {g}}$ is nilpotent.

## Properties

### Nilpotent Lie algebras are solvable

Every nilpotent Lie algebra is solvable. This is useful in proving the solvability of a Lie algebra since, in practice, it is usually easier to prove nilpotency (when it holds!) rather than solvability. However, in general, the converse of this property is false. For example, the subalgebra of ${\mathfrak {gl}}(k,\mathbb {R} )$ (*k* ≥ 2) consisting of upper triangular matrices, ${\mathfrak {b}}(k,\mathbb {R} )$ , is solvable but not nilpotent.

### Subalgebras and images

If a Lie algebra ${\mathfrak {g}}$ is nilpotent, then all subalgebras and homomorphic images are nilpotent.

### Nilpotency of the quotient by the center

If the quotient algebra ${\mathfrak {g}}/Z({\mathfrak {g}})$ , where $Z({\mathfrak {g}})$ is the center of ${\mathfrak {g}}$ , is nilpotent, then so is ${\mathfrak {g}}$ . This is to say that a central extension of a nilpotent Lie algebra by a nilpotent Lie algebra is nilpotent.

### Engel's theorem

Engel's theorem: A finite dimensional Lie algebra ${\mathfrak {g}}$ is nilpotent if and only if all elements of ${\mathfrak {g}}$ are ad-nilpotent.

### Zero Killing form

The Killing form of a nilpotent Lie algebra is 0.

### Have outer automorphisms

A nonzero nilpotent Lie algebra has an outer automorphism, that is, an automorphism that is not in the image of Ad.

### Derived subalgebras of solvable Lie algebras

The derived subalgebra of a finite dimensional solvable Lie algebra over a field of characteristic 0 is nilpotent.
