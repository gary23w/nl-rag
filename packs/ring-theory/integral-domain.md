---
title: "Integral domain"
source: https://en.wikipedia.org/wiki/Integral_domain
domain: ring-theory
license: CC-BY-SA-4.0
tags: ring theory, commutative ring, ring ideal, polynomial ring
fetched: 2026-07-02
---

# Integral domain

In mathematics, an **integral domain** is a nonzero commutative ring in which the product of any two nonzero elements is nonzero. In an integral domain, every nonzero element *a* has the cancellation property, that is, if *a* ≠ 0, *ab* = *ac* implies *b* = *c*. Integral domains are generalizations of the ring of integers and provide a setting that is useful for studying divisibility.

"Integral domain" is defined almost universally as above, but there is some variation. This article follows the convention that rings have a multiplicative identity, generally denoted 1, but some authors do not follow this, by not requiring integral domains to have a multiplicative identity. Noncommutative integral domains are sometimes admitted. This article, however, follows the much more usual convention of reserving the term "integral domain" for the commutative case and using "domain" for the general case including noncommutative rings.

Some sources, notably Lang, use the term **entire ring** for integral domain.

Some specific kinds of integral domains are given with the following chain of class inclusions:

rngs

⊃

rings

⊃

commutative rings

⊃

integral domains

⊃

integrally closed domains

⊃

GCD domains

⊃

unique factorization domains

⊃

principal ideal domains

⊃

Euclidean domains

⊃

fields

⊃

algebraically closed fields

## Definition

An *integral domain* is a nonzero commutative ring in which the product of any two nonzero elements is nonzero. Equivalently:

- An integral domain is a nonzero commutative ring with no nonzero zero divisors.
- An integral domain is a commutative ring in which the zero ideal {0} is a prime ideal.
- An integral domain is a nonzero commutative ring for which every nonzero element is cancellable under multiplication.
- An integral domain is a ring for which the set of nonzero elements is a commutative monoid under multiplication (because a monoid must be closed under multiplication).
- An integral domain is a nonzero commutative ring in which for every nonzero element *r*, the function that maps each element *x* of the ring to the product *xr* is injective. Elements *r* with this property are called *regular*, so it is equivalent to require that every nonzero element of the ring be regular.
- An integral domain is a ring that is isomorphic to a subring of a field. (Given an integral domain, one can embed it in its field of fractions.)

## Examples

- The archetypical example is the ring $\mathbb {Z}$ of all integers.
- Every field is an integral domain. For example, the field $\mathbb {R}$ of all real numbers is an integral domain. Conversely, every Artinian integral domain is a field. In particular, all finite integral domains are finite fields (more generally, by Wedderburn's little theorem, finite domains are finite fields). The ring of integers $\mathbb {Z}$ provides an example of a non-Artinian infinite integral domain that is not a field, possessing infinite descending sequences of ideals such as: $\mathbb {Z} \supset 2\mathbb {Z} \supset \cdots \supset 2^{n}\mathbb {Z} \supset 2^{n+1}\mathbb {Z} \supset \cdots$
- Rings of polynomials are integral domains if the coefficients come from an integral domain. For instance, the ring $\mathbb {Z} [x]$ of all polynomials in one variable with integer coefficients is an integral domain; so is the ring $\mathbb {C} [x_{1},\ldots ,x_{n}]$ of all polynomials in *n*-variables with complex coefficients.
- The previous example can be further exploited by taking quotients from prime ideals. For example, the ring $\mathbb {C} [x,y]/(y^{2}-x(x-1)(x-2))$ corresponding to a plane elliptic curve is an integral domain. Integrality can be checked by showing $y^{2}-x(x-1)(x-2)$ is an irreducible polynomial.
- The ring $\mathbb {Z} [x]/(x^{2}-n)\cong \mathbb {Z} [{\sqrt {n}}]$ is an integral domain for any non-square integer n . If $n>0$ , then this ring is always a subring of $\mathbb {R}$ , otherwise, it is a subring of $\mathbb {C} .$
- The ring of *p*-adic integers $\mathbb {Z} _{p}$ is an integral domain.
- The ring of formal power series of an integral domain is an integral domain.
- If U is a connected open subset of the complex plane $\mathbb {C}$ , then the ring ${\mathcal {H}}(U)$ consisting of all holomorphic functions is an integral domain. The same is true for rings of analytic functions on connected open subsets of analytic manifolds.
- A regular local ring is an integral domain. In fact, a regular local ring is a UFD.

## Non-examples

The following rings are *not* integral domains.

- The zero ring (the ring in which $0=1$ ).
- The quotient ring $\mathbb {Z} /m\mathbb {Z}$ when *m* is a composite number. To show this, choose a proper factorization $m=xy$ (meaning that x and y are not equal to 1 or m ). Then $x\not \equiv 0{\bmod {m}}$ and $y\not \equiv 0{\bmod {m}}$ , but $xy\equiv 0{\bmod {m}}$ .
- A product of two nonzero commutative rings. In such a product $R\times S$ , one has $(1,0)\cdot (0,1)=(0,0)$ .
- The quotient ring $\mathbb {Z} [x]/(x^{2}-n^{2})$ for any $n\in \mathbb {Z}$ . The images of $x+n$ and $x-n$ are nonzero, while their product is 0 in this ring.
- The ring of *n* × *n* matrices over any nonzero ring when *n* ≥ 2. If M and N are matrices such that the image of N is contained in the kernel of M , then $MN=0$ . For example, this happens for $M=N=({\begin{smallmatrix}0&1\\0&0\end{smallmatrix}})$ .
- The quotient ring $k[x_{1},\ldots ,x_{n}]/(fg)$ for any field k and any non-constant polynomials $f,g\in k[x_{1},\ldots ,x_{n}]$ . The images of *f* and *g* in this quotient ring are nonzero elements whose product is 0. This argument shows, equivalently, that $(fg)$ is not a prime ideal. The geometric interpretation of this result is that the zeros of *fg* form an affine algebraic set that is not irreducible (that is, not an algebraic variety) in general. The only case where this algebraic set may be irreducible is when *fg* is a power of an irreducible polynomial, which defines the same algebraic set.
- The ring of continuous functions on the unit interval. Consider the functions $f(x)={\begin{cases}1-2x&x\in \left[0,{\tfrac {1}{2}}\right]\\0&x\in \left[{\tfrac {1}{2}},1\right]\end{cases}}\qquad g(x)={\begin{cases}0&x\in \left[0,{\tfrac {1}{2}}\right]\\2x-1&x\in \left[{\tfrac {1}{2}},1\right]\end{cases}}$

Neither

f

nor

g

is everywhere zero, but

$fg$

is.

- The tensor product $\mathbb {C} \otimes _{\mathbb {R} }\mathbb {C}$ . This ring has two non-trivial idempotents, $e_{1}={\tfrac {1}{2}}(1\otimes 1)-{\tfrac {1}{2}}(i\otimes i)$ and $e_{2}={\tfrac {1}{2}}(1\otimes 1)+{\tfrac {1}{2}}(i\otimes i)$ . They are orthogonal, meaning that $e_{1}e_{2}=0$ , and hence $\mathbb {C} \otimes _{\mathbb {R} }\mathbb {C}$ is not a domain. In fact, there is an isomorphism $\mathbb {C} \times \mathbb {C} \to \mathbb {C} \otimes _{\mathbb {R} }\mathbb {C}$ defined by $(z,w)\mapsto z\cdot e_{1}+w\cdot e_{2}$ . Its inverse is defined by $z\otimes w\mapsto (zw,z{\overline {w}})$ . This example shows that a fiber product of irreducible affine schemes need not be irreducible.

## Divisibility, prime elements, and irreducible elements

In this section, *R* is an integral domain.

Given elements *a* and *b* of *R*, one says that *a* *divides* *b*, or that *a* is a *divisor* of *b*, or that *b* is a *multiple* of *a*, if there exists an element *x* in *R* such that *ax* = *b*.

The *units* of *R* are the elements that divide 1; these are precisely the invertible elements in *R*. Units divide all other elements.

If *a* divides *b* and *b* divides *a*, then *a* and *b* are **associated elements** or **associates**. Equivalently, *a* and *b* are associates if *a* = *ub* for some unit *u*.

An *irreducible element* is a nonzero non-unit that cannot be written as a product of two non-units.

A nonzero non-unit *p* is a *prime element* if, whenever *p* divides a product *ab*, then *p* divides *a* or *p* divides *b*. Equivalently, an element *p* is prime if and only if the principal ideal (*p*) is a nonzero prime ideal.

Both notions of irreducible elements and prime elements generalize the ordinary definition of prime numbers in the ring $\mathbb {Z} ,$ if one considers as prime the negative primes.

Every prime element is irreducible. The converse is not true in general: for example, in the quadratic integer ring $\mathbb {Z} \left[{\sqrt {-5}}\right]$ the element 3 is irreducible (if it factored nontrivially, the factors would each have to have norm 3, but there are no norm 3 elements since $a^{2}+5b^{2}=3$ has no integer solutions), but not prime (since 3 divides $\left(2+{\sqrt {-5}}\right)\left(2-{\sqrt {-5}}\right)$ without dividing either factor). In a unique factorization domain (or more generally, a GCD domain), an irreducible element is a prime element.

While unique factorization does not hold in $\mathbb {Z} \left[{\sqrt {-5}}\right]$ , there is unique factorization of ideals. See Lasker–Noether theorem.

## Properties

- A commutative ring *R* is an integral domain if and only if the ideal (0) of *R* is a prime ideal.
- If *R* is a commutative ring and *P* is an ideal in *R*, then the quotient ring *R/P* is an integral domain if and only if *P* is a prime ideal.
- Let *R* be an integral domain. Then the polynomial rings over *R* (in any number of indeterminates) are integral domains. This is in particular the case if *R* is a field.
- The cancellation property holds in any integral domain: for any *a*, *b*, and *c* in an integral domain, if *a* ≠ *0* and *ab* = *ac* then *b* = *c*. Another way to state this is that the function *x* ↦ *ax* is injective for any nonzero *a* in the domain.
- The cancellation property holds for ideals in any integral domain: if *xI* = *xJ*, then either *x* is zero or *I* = *J*.
- An integral domain is equal to the intersection of its localizations at maximal ideals.
- An inductive limit of integral domains is an integral domain.
- If *A*, *B* are integral domains over an algebraically closed field *k*, then *A* ⊗*k* *B* is an integral domain. This is a consequence of Hilbert's nullstellensatz, and, in algebraic geometry, it implies the statement that the coordinate ring of the product of two affine algebraic varieties over an algebraically closed field is again an integral domain.

## Field of fractions

The field of fractions *K* of an integral domain *R* is the set of fractions *a*/*b* with *a* and *b* in *R* and *b* ≠ 0 modulo an appropriate equivalence relation, equipped with the usual addition and multiplication operations. It is "the smallest field containing *R*" in the sense that there is an injective ring homomorphism *R* → *K* such that any injective ring homomorphism from *R* to a field factors through *K*. The field of fractions of the ring of integers $\mathbb {Z}$ is the field of rational numbers $\mathbb {Q} .$ The field of fractions of a field is isomorphic to the field itself.

## Algebraic geometry

Integral domains are characterized by the condition that they are reduced (that is *x*2 = 0 implies *x* = 0) and irreducible (that is there is only one minimal prime ideal). The former condition ensures that the nilradical of the ring is zero, so that the intersection of all the ring's minimal primes is zero. The latter condition is that the ring have only one minimal prime. It follows that the unique minimal prime ideal of a reduced and irreducible ring is the zero ideal, so such rings are integral domains. The converse is clear: an integral domain has no nonzero nilpotent elements, and the zero ideal is the unique minimal prime ideal.

This translates, in algebraic geometry, into the fact that the coordinate ring of an affine algebraic set is an integral domain if and only if the algebraic set is an algebraic variety.

More generally, a commutative ring is an integral domain if and only if its spectrum is an integral affine scheme.

## Characteristic and homomorphisms

The characteristic of an integral domain is either 0 or a prime number.

If *R* is an integral domain of prime characteristic *p*, then the Frobenius endomorphism *x* ↦ *x**p* is injective.
