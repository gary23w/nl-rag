---
title: "Ring of integers"
source: https://en.wikipedia.org/wiki/Ring_of_integers
domain: algebraic-number-theory
license: CC-BY-SA-4.0
tags: algebraic number theory, ring of integers, ideal class group, dedekind domain
fetched: 2026-07-02
---

# Ring of integers

In mathematics, the **ring of integers** of an algebraic number field K (also sometimes called the **number ring** corresponding to number field *K*) is the ring of all algebraic integers contained in K . An algebraic integer is a root of a monic polynomial with integer coefficients: $x^{n}+c_{n-1}x^{n-1}+\cdots +c_{0}$ . This ring is often denoted by $O_{K}$ or ${\mathcal {O}}_{K}$ . Since any integer belongs to K and is an integral element of K , the ring $\mathbb {Z}$ is always a subring of $O_{K}$ .

The ring of integers $\mathbb {Z}$ is the simplest possible ring of integers. Namely, $\mathbb {Z} =O_{\mathbb {Q} }$ where $\mathbb {Q}$ is the field of rational numbers. And indeed, in algebraic number theory the elements of $\mathbb {Z}$ are often called the "rational integers" because of this.

The next simplest example is the ring of Gaussian integers $\mathbb {Z} [i]$ , consisting of complex numbers whose real and imaginary parts are integers. It is the ring of integers in the number field $\mathbb {Q} (i)$ of Gaussian rationals, consisting of complex numbers whose real and imaginary parts are rational numbers. Like the rational integers, $\mathbb {Z} [i]$ is a Euclidean domain.

The ring of integers of an algebraic number field is the unique maximal order in the field. It is always a Dedekind domain.

## Properties

The ring of integers O*K* is a finitely-generated $\mathbb {Z}$ -module. Indeed, it is a free $\mathbb {Z}$ -module, and thus has an **integral basis**, that is a basis *b*1, ..., *b**n* ∈ O*K* of the $\mathbb {Q}$ -vector space K such that each element x in O*K* can be uniquely represented as

$x=\sum _{i=1}^{n}a_{i}b_{i},$

with $a_{i}\in \mathbb {Z}$ . The rank n of O*K* as a free $\mathbb {Z}$ -module is equal to the degree of K over $\mathbb {Q}$ .

## Examples

### Computational tool

A useful tool for computing the integral closure of the ring of integers in an algebraic field $K/\mathbb {Q}$ is the discriminant. If *K* is of degree *n* over $\mathbb {Q}$ , and $\alpha _{1},\ldots ,\alpha _{n}\in {\mathcal {O}}_{K}$ form a basis of K over $\mathbb {Q}$ , set $d=\Delta _{K/\mathbb {Q} }(\alpha _{1},\ldots ,\alpha _{n})$ . Then, ${\mathcal {O}}_{K}$ is a submodule of the $\mathbb {Z}$ -module spanned by $\alpha _{1}/d,\ldots ,\alpha _{n}/d$ . pg. 33 In fact, if *d* is square-free, then $\alpha _{1},\ldots ,\alpha _{n}$ forms an integral basis for ${\mathcal {O}}_{K}$ . pg. 35

### Cyclotomic extensions

If p is a prime, *ζ* is a pth root of unity and $K=\mathbb {Q} (\zeta )$ is the corresponding cyclotomic field, then an integral basis of ${\mathcal {O}}_{K}=\mathbb {Z} [\zeta ]$ is given by (1, *ζ*, *ζ* 2, ..., *ζ* *p*−2).

### Quadratic extensions

If d is a square-free integer and $K=\mathbb {Q} ({\sqrt {d}}\,)$ is the corresponding quadratic field, then ${\mathcal {O}}_{K}$ is a ring of quadratic integers and its integral basis is given by $\left(1,{\frac {1+{\sqrt {d}}}{2}}\right)$ if *d* ≡ 1 (mod 4) and by $(1,{\sqrt {d}})$ if *d* ≡ 2, 3 (mod 4). This can be found by computing the minimal polynomial of an arbitrary element $a+b{\sqrt {d}}\in \mathbb {Q} ({\sqrt {d}})$ where $a,b\in \mathbb {Q}$ .

## Multiplicative structure

In a ring of integers, every element has a factorization into irreducible elements, but the ring need not have the property of unique factorization: for example, in the ring of integers $\mathbb {Z} [{\sqrt {-5}}]$ , the element 6 has two essentially different factorizations into irreducibles:

$6=2\cdot 3=(1+{\sqrt {-5}})(1-{\sqrt {-5}}).$

A ring of integers is always a Dedekind domain, and so has unique factorization of ideals into prime ideals.

The units of a ring of integers *O**K* is a finitely generated abelian group by Dirichlet's unit theorem. The torsion subgroup consists of the roots of unity of *K*. A set of torsion-free generators is called a set of *fundamental units*.

## Generalization

One defines the ring of integers of a non-archimedean local field *F* as the set of all elements of *F* with absolute value ≤ 1; this is a ring because of the strong triangle inequality. If *F* is the completion of an algebraic number field, its ring of integers is the completion of the latter's ring of integers. The ring of integers of an algebraic number field may be characterised as the elements which are integers in every non-archimedean completion.

For example, the p-adic integers $\mathbb {Z} _{p}$ are the ring of integers of the p-adic numbers $\mathbb {Q} _{p}$ .
