---
title: "Killing form"
source: https://en.wikipedia.org/wiki/Killing_form
domain: lie-algebras
license: CC-BY-SA-4.0
tags: lie algebra, semisimple lie algebra, cartan subalgebra, killing form
fetched: 2026-07-02
---

# Killing form

In mathematics, the **Killing form**, named after Wilhelm Killing, is a symmetric bilinear form that plays a basic role in the theories of Lie groups and Lie algebras. Cartan's criteria (criterion of solvability and criterion of semisimplicity) show that Killing form has a close relationship to the semisimplicity of the Lie algebras.

## History and name

The Killing form was essentially introduced into Lie algebra theory by Élie Cartan (1894) in his thesis. In a historical survey of Lie theory, Borel (2001) has described how the term *"Killing form"* first occurred in 1951 during one of his own reports for the Séminaire Bourbaki; it arose as a misnomer, since the form had previously been used by Lie theorists, without a name attached. Some other authors now employ the term *"Cartan-Killing form"*. At the end of the 19th century, Killing had noted that the coefficients of the characteristic equation of a regular semisimple element of a Lie algebra are invariant under the adjoint group, from which it follows that the Killing form (i.e. the degree 2 coefficient) is invariant, but he did not make much use of the fact. A basic result that Cartan made use of was Cartan's criterion, which states that the Killing form is non-degenerate if and only if the Lie algebra is a direct sum of simple Lie algebras.

## Definition

Consider a Lie algebra ${\mathfrak {g}}$ over a field *K*. Every element *x* of ${\mathfrak {g}}$ defines the adjoint endomorphism ad(*x*) (also written as ad*x*) of ${\mathfrak {g}}$ with the help of the Lie bracket, as

$\operatorname {ad} (x)(y)=[x,y].$

Now, supposing ${\mathfrak {g}}$ is of finite dimension, the trace of the composition of two such endomorphisms defines a symmetric bilinear form

$B(x,y)=\operatorname {trace} (\operatorname {ad} (x)\circ \operatorname {ad} (y)),$

with values in *K*, the **Killing form** on ${\mathfrak {g}}$ .

## Properties

The following properties follow as theorems from the above definition.

- The Killing form *B* is bilinear and symmetric.
- The Killing form is an invariant form, as are all other forms obtained from Casimir operators. The derivation of Casimir operators vanishes; for the Killing form, this vanishing can be written as

$B([x,y],z)=B(x,[y,z])$

where [ , ] is the

Lie bracket

.

- If ${\mathfrak {g}}$ is a complex simple Lie algebra then any invariant symmetric bilinear form on ${\mathfrak {g}}$ is a scalar multiple of the Killing form. This is no longer true if ${\mathfrak {g}}$ is simple but not complex; key concept: absolutely simple Lie algebra.
- The Killing form is also invariant under automorphisms *s* of the algebra ${\mathfrak {g}}$ , that is,

$B(s(x),s(y))=B(x,y)$

for

s

in

$\mathrm {Aut} ({\mathfrak {g}})$

.

- The Cartan criterion states that a Lie algebra is semisimple if and only if the Killing form is non-degenerate.
- The Killing form of a nilpotent Lie algebra is identically zero.
- If *I*, *J* are two ideals in a Lie algebra ${\mathfrak {g}}$ with zero intersection, then *I* and *J* are orthogonal subspaces with respect to the Killing form.
- The orthogonal complement with respect to *B* of an ideal is again an ideal.
- If a given Lie algebra ${\mathfrak {g}}$ is a direct sum of its ideals *I*1,...,*In*, then the Killing form of ${\mathfrak {g}}$ is the direct sum of the Killing forms of the individual summands.

## Matrix elements

Given a basis *ei* of the Lie algebra ${\mathfrak {g}}$ , the matrix elements of the Killing form are given by

$B_{ij}=\mathrm {trace} (\mathrm {ad} (e_{i})\circ \mathrm {ad} (e_{j})).$

Here

$\left({\textrm {ad}}(e_{i})\circ {\textrm {ad}}(e_{j})\right)(e_{k})=[e_{i},[e_{j},e_{k}]]=[e_{i},{c_{jk}}^{m}e_{m}]={c_{im}}^{n}{c_{jk}}^{m}e_{n}$

in Einstein summation notation, where the *c**ij**k* are the structure coefficients of the Lie algebra. The index *k* functions as column index and the index *n* as row index in the matrix ad(*e**i*)ad(*e**j*). Taking the trace amounts to putting *k* = *n* and summing, and so we can write

$B_{ij}={c_{im}}^{n}{c_{jn}}^{m}$

The Killing form is the simplest 2-tensor that can be formed from the structure constants. The form itself is then $B=B_{ij}e^{i}\otimes e^{j}.$

In the above indexed definition, we are careful to distinguish upper and lower indices (*co-* and *contra-variant* indices). This is because, in many cases, the Killing form can be used as a metric tensor on a manifold, in which case the distinction becomes an important one for the transformation properties of tensors. When the Lie algebra is semisimple over a zero-characteristic field, its Killing form is nondegenerate, and hence can be used as a metric tensor to raise and lower indexes. In this case, it is always possible to choose a basis for ${\mathfrak {g}}$ such that the structure constants with all upper indices are completely antisymmetric.

The Killing form for some Lie algebras ${\mathfrak {g}}$ are (for *X*, *Y* in ${\mathfrak {g}}$ viewed in their fundamental matrix representation):

| ${\mathfrak {g}}$ | $B(X,Y)$ | Classification | Dual coxeter number |
|---|---|---|---|
| ${\mathfrak {gl}}(n,\mathbb {R} )$ | $2n{\text{tr}}(XY)-2{\text{tr}}(X){\text{tr}}(Y)$ | - | - |
| ${\mathfrak {sl}}(n,\mathbb {R} ),n\geq 2$ | $2n{\text{tr}}(XY)$ | $A_{n-1}$ | n |
| ${\mathfrak {su}}(n),n\geq 2$ | $2n{\text{tr}}(XY)$ | $A_{n-1}$ | n |
| ${\mathfrak {so}}(n),n\geq 2$ | $(n-2){\text{tr}}(XY)$ | $B_{m},n=2m+1$ for n odd. $D_{m},n=2m$ for n even. | $n-2$ |
| ${\mathfrak {so}}(n,\mathbb {C} ),n\geq 2$ | $(n-2){\text{tr}}(XY)$ | $B_{m},n=2m+1$ for n odd. $D_{m},n=2m$ for n even. | $n-2$ |
| ${\mathfrak {sp}}(2n,\mathbb {R} ),n\geq 1$ | $2(n+1){\text{tr}}(XY)$ | $C_{n}$ | $n+1$ |
| ${\mathfrak {sp}}(2n,\mathbb {C} ),n\geq 1$ | $2(n+1){\text{tr}}(XY)$ | $C_{n}$ | $n+1$ |

The table shows that the Dynkin index for the adjoint representation is equal to twice the dual Coxeter number.

## Connection with real forms

Suppose that ${\mathfrak {g}}$ is a semisimple Lie algebra over the field of real numbers $\mathbb {R}$ . By Cartan's criterion, the Killing form is nondegenerate, and can be diagonalized in a suitable basis with the diagonal entries ±1. By Sylvester's law of inertia, the number of positive entries is an invariant of the bilinear form, i.e. it does not depend on the choice of the diagonalizing basis, and is called the **index** of the Lie algebra ${\mathfrak {g}}$ . This is a number between 0 and the dimension of ${\mathfrak {g}}$ which is an important invariant of the real Lie algebra. In particular, a real Lie algebra ${\mathfrak {g}}$ is called **compact** if the Killing form is negative definite (or negative semidefinite if the Lie algebra is not semisimple). Note that this is one of two inequivalent definitions commonly used for compactness of a Lie algebra; the other states that a Lie algebra is compact if it corresponds to a compact Lie group. The definition of compactness in terms of negative definiteness of the Killing form is more restrictive, since using this definition it can be shown that under the Lie correspondence, compact Lie algebras correspond to compact semisimple Lie groups.

If ${\mathfrak {g}}_{\mathbb {C} }$ is a semisimple Lie algebra over the complex numbers, then there are several non-isomorphic real Lie algebras whose complexification is ${\mathfrak {g}}_{\mathbb {C} }$ , which are called its **real forms**. It turns out that every complex semisimple Lie algebra admits a unique (up to isomorphism) compact real form ${\mathfrak {g}}$ . The real forms of a given complex semisimple Lie algebra are frequently labeled by the positive index of inertia of their Killing form.

For example, the complex special linear algebra ${\mathfrak {sl}}(2,\mathbb {C} )$ has two real forms, the real special linear algebra, denoted ${\mathfrak {sl}}(2,\mathbb {R} )$ , and the special unitary algebra, denoted ${\mathfrak {su}}(2)$ . The first one is noncompact, the so-called **split real form**, and its Killing form has signature (2, 1). The second one is the compact real form and its Killing form is negative definite, i.e. has signature (0, 3). The corresponding Lie groups are the noncompact group $\mathrm {SL} (2,\mathbb {R} )$ of 2 × 2 real matrices with the unit determinant and the special unitary group $\mathrm {SU} (2)$ , which is compact.

## Trace forms

Let ${\mathfrak {g}}$ be a finite-dimensional Lie algebra over the field K , and ${\displaystyle \rho$ be a Lie algebra representation. Let ${\text{Tr}}_{V}:{\text{End}}(V)\rightarrow K$ be the trace functional on V . Then we can define the trace form for the representation $\rho$ as

${\text{Tr}}_{\rho }:{\mathfrak {g}}\times {\mathfrak {g}}\rightarrow K,$

${\text{Tr}}_{\rho }(X,Y)={\text{Tr}}_{V}(\rho (X)\rho (Y)).$

Then the Killing form is the special case that the representation is the adjoint representation, ${\text{Tr}}_{\text{ad}}=B$ .

It is easy to show that this is symmetric, bilinear and invariant for any representation $\rho$ .

If furthermore ${\mathfrak {g}}$ is simple and $\rho$ is irreducible, then it can be shown ${\text{Tr}}_{\rho }=I(\rho )B$ where $I(\rho )$ is the index of the representation.
