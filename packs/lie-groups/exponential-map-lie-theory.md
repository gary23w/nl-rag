---
title: "Exponential map (Lie theory)"
source: https://en.wikipedia.org/wiki/Exponential_map_(Lie_theory)
domain: lie-groups
license: CC-BY-SA-4.0
tags: lie group, lie theory, compact group, maximal torus
fetched: 2026-07-02
---

# Exponential map (Lie theory)

In the theory of Lie groups, the **exponential map** is a map from the Lie algebra ${\mathfrak {g}}$ of a Lie group G to the group, which allows one to recapture the local group structure from the Lie algebra. The existence of the exponential map is one of the primary reasons that Lie algebras are a useful tool for studying Lie groups.

The ordinary exponential function of mathematical analysis is a special case of the exponential map when G is the multiplicative group of positive real numbers (whose Lie algebra is the additive group of all real numbers). The exponential map of a Lie group satisfies many properties analogous to those of the ordinary exponential function, however, it also differs in many important respects.

## Definitions

Let G be a Lie group and ${\mathfrak {g}}$ be its Lie algebra (thought of as the tangent space to the identity element of G ). The **exponential map** is a map

$\exp \colon {\mathfrak {g}}\to G$

which can be defined in several different ways. The typical modern definition is this:

Definition

: The exponential of

$X\in {\mathfrak {g}}$

is given by

$\exp(X)=\gamma (1)$

where

$\gamma \colon \mathbb {R} \to G$

is the unique

one-parameter subgroup

of

G

whose

tangent vector

at the identity is equal to

X

.

It follows easily from the chain rule that $\exp(tX)=\gamma (t)$ . The map $\gamma$ , a group homomorphism from $(\mathbb {R} ,+)$ to G , may be constructed as the integral curve of either the right- or left-invariant vector field associated with X . That the integral curve exists for all real parameters follows by right- or left-translating the solution near zero.

We have a more concrete definition in the case of a matrix Lie group. The exponential map coincides with the matrix exponential and is given by the ordinary series expansion:

$\exp(X)=\sum _{k=0}^{\infty }{\frac {X^{k}}{k!}}=I+X+{\frac {1}{2}}X^{2}+{\frac {1}{6}}X^{3}+\cdots$

,

where I is the identity matrix. Thus, in the setting of matrix Lie groups, the exponential map is the restriction of the matrix exponential to the Lie algebra ${\mathfrak {g}}$ of G .

### Comparison with Riemannian exponential map

If *G* is compact, it has a Riemannian metric invariant under left *and* right translations, then the Lie-theoretic exponential map for *G* coincides with the exponential map of this Riemannian metric.

For a general *G*, there will not exist a Riemannian metric invariant under both left and right translations. Although there is always a Riemannian metric invariant under, say, left translations, the exponential map in the sense of Riemannian geometry for a left-invariant metric will *not* in general agree with the exponential map in the Lie group sense. That is to say, if *G* is a Lie group equipped with a left- but not right-invariant metric, the geodesics through the identity will not be one-parameter subgroups of *G*.

### Other definitions

Other equivalent definitions of the Lie-group exponential are as follows:

- It is the exponential map of a canonical left-invariant affine connection on G , such that parallel transport is given by left translation. That is, $\exp(X)=\gamma (1)$ where $\gamma$ is the unique geodesic with the initial point at the identity element and the initial velocity X (thought of as a tangent vector).
- It is the exponential map of a canonical right-invariant affine connection on G . This is usually different from the canonical left-invariant connection, but both connections have the same geodesics (orbits of 1-parameter subgroups acting by left or right multiplication) so give the same exponential map.
- The Lie group–Lie algebra correspondence also gives the definition: for $X\in {\mathfrak {g}}$ , the mapping $t\mapsto \exp(tX)$ is the unique Lie group homomorphism $(\mathbb {R} ,+)\to G$ corresponding to the Lie algebra homomorphism $\mathbb {R} \to {\mathfrak {g}}$ , $t\mapsto tX.$
- The exponential map is characterized by the differential equation ${\textstyle {\frac {d}{dt}}\exp(tX)=\exp(tX)\cdot X}$ (or, equivalently, ${\textstyle {\frac {d}{dt}}\exp(tX)=X\cdot \exp(tX)}$ ), where the right side uses the translation mapping ${\mathfrak {g}}=T_{e}G\to T_{g}G,\ X\mapsto g\cdot X$ for $g=\exp(tX)$ . In the one-dimensional case, this is equivalent to $\exp '(x)=\exp(x)$ .

## Examples

- The unit circle centered at 0 in the complex plane is a Lie group (called the circle group) whose tangent space at 1 can be identified with the imaginary line in the complex plane, $\{it:t\in \mathbb {R} \}.$ The exponential map for this Lie group is given by

$it\mapsto \exp(it)=e^{it}=\cos(t)+i\sin(t),\,$

that is, the same formula as the ordinary

complex exponential

.

- More generally, for complex torus $X=\mathbb {C} ^{n}/\Lambda$ for some integral lattice $\Lambda$ of rank n (so isomorphic to $\mathbb {Z} ^{n}$ ) the torus comes equipped with a universal covering map

> ${\displaystyle \pi$

from the quotient by the lattice. Since X is locally isomorphic to $\mathbb {C} ^{n}$ as complex manifolds, we can identify it with the tangent space $T_{0}X$ , and the map

> $\pi :T_{0}X\to X$

corresponds to the exponential map for the complex Lie group X .

- In the quaternions $\mathbb {H}$ , the set of quaternions of unit length form a Lie group (isomorphic to the special unitary group *SU*(2)) whose tangent space at 1 can be identified with the space of purely imaginary quaternions, $\{it+ju+kv:t,u,v\in \mathbb {R} \}.$ The exponential map for this Lie group is given by

$\mathbf {w$

This map takes the 2-sphere of radius

R

inside the purely imaginary

quaternions

to

$\{s\in S^{3}\subset \mathbf {H$

, a 2-sphere of radius

$\sin(R)$

(cf.

Exponential of a Pauli vector

). Compare this to the first example above.

- Let *V* be a finite dimensional real vector space and view it as a Lie group under the operation of vector addition. Then $\operatorname {Lie} (V)=V$ via the identification of *V* with its tangent space at 0, and the exponential map

$\operatorname {exp$

is the identity map, that is,

$\exp(v)=v$

.

- In the split-complex number plane $z=x+y\jmath ,\quad \jmath ^{2}=+1,$ the imaginary line $\lbrace \jmath t:t\in \mathbb {R} \rbrace$ forms the Lie algebra of the unit hyperbola group $\lbrace \cosh t+\jmath \ \sinh t:t\in \mathbb {R} \rbrace$ since the exponential map is given by

$\jmath t\mapsto \exp(\jmath t)=\cosh t+\jmath \ \sinh t.$

## Properties

### Elementary properties of the exponential

For all $X\in {\mathfrak {g}}$ , the map $\gamma (t)=\exp(tX)$ is the unique one-parameter subgroup of G whose tangent vector at the identity is X . It follows that:

- $\exp((t+s)X)=\exp(tX)\exp(sX)\,$
- $\exp(-X)=\exp(X)^{-1}.\,$

More generally:

- $\exp(X+Y)=\exp(X)\exp(Y),\quad {\text{if }}[X,Y]=0$ .

The preceding identity does not hold in general; the assumption that X and Y commute is important.

The image of the exponential map always lies in the identity component of G .

### The exponential near the identity

The exponential map $\exp \colon {\mathfrak {g}}\to G$ is a smooth map. Its differential at zero, $\exp _{*}\colon {\mathfrak {g}}\to {\mathfrak {g}}$ , is the identity map (with the usual identifications).

It follows from the inverse function theorem that the exponential map, therefore, restricts to a diffeomorphism from some neighborhood of 0 in ${\mathfrak {g}}$ to a neighborhood of 1 in G .

It is then not difficult to show that if *G* is connected, every element *g* of *G* is a *product* of exponentials of elements of ${\mathfrak {g}}$ : $g=\exp(X_{1})\exp(X_{2})\cdots \exp(X_{n}),\quad X_{j}\in {\mathfrak {g}}$ .

Globally, the exponential map is not necessarily surjective. Furthermore, the exponential map may not be a local diffeomorphism at all points. For example, the exponential map from ${\mathfrak {so}}$ (3) to SO(3) is not a local diffeomorphism; see also cut locus on this failure. See derivative of the exponential map for more information.

### Surjectivity of the exponential

In these important special cases, the exponential map is known to always be surjective:

- G is connected and compact,
- G is connected and nilpotent (for example, G connected and abelian), or
- $G=\operatorname {GL} (n,\mathbb {C} )$ .

For groups not satisfying any of the above conditions, the exponential map may or may not be surjective.

The image of the exponential map of the connected but non-compact group *SL*2(**R**) is not the whole group. Its image consists of $\mathbb {C}$ -diagonalizable matrices with eigenvalues either positive or with modulus 1 , and of non-diagonalizable matrices with a repeated eigenvalue 1 , and the matrix $-I$ . (Thus, the image excludes matrices with real, negative eigenvalues, other than $-I$ .)

### Exponential map and homomorphisms

Let $\phi \colon G\to H$ be a Lie group homomorphism and let $\phi _{*}$ be its derivative at the identity. Then the following diagram commutes:

In particular, when applied to the adjoint action of a Lie group G , since $\operatorname {Ad} _{*}=\operatorname {ad}$ , we have the useful identity:

$\mathrm {Ad} _{\exp X}(Y)=\exp(\mathrm {ad} _{X})(Y)=Y+[X,Y]+{\frac {1}{2!}}[X,[X,Y]]+{\frac {1}{3!}}[X,[X,[X,Y]]]+\cdots$

.

## Logarithmic coordinates

Given a Lie group G with Lie algebra ${\mathfrak {g}}$ , each choice of a basis $X_{1},\dots ,X_{n}$ of ${\mathfrak {g}}$ determines a coordinate system near the identity element e for G , as follows. By the inverse function theorem, the exponential map $\exp :N\xrightarrow {\sim } U$ is a diffeomorphism from some neighborhood $N\subset {\mathfrak {g}}\simeq \mathbb {R} ^{n}$ of the origin to a neighborhood U of $e\in G$ . Its inverse: $\log :U\xrightarrow {\sim } N\subset \mathbb {R} ^{n}$ is then a coordinate system on U . It is called by various names such as logarithmic coordinates, exponential coordinates or normal coordinates. See the closed-subgroup theorem for an example of how they are used in applications.

**Remark**: The open cover $\{Ug\mid g\in G\}$ gives a structure of a real-analytic manifold to G such that the group operation $(g,h)\mapsto gh^{-1}$ is real-analytic.
