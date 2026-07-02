---
title: "Ordinal arithmetic"
source: https://en.wikipedia.org/wiki/Ordinal_arithmetic
domain: ordinal-arithmetic
license: CC-BY-SA-4.0
tags: ordinal arithmetic, ordinal number, transfinite induction, cantor normal form
fetched: 2026-07-02
---

# Ordinal arithmetic

In the mathematical field of set theory, **ordinal arithmetic** includes binary operations on ordinal numbers such as addition, multiplication, and exponentiation. Each can be defined in two different ways: either by constructing an explicit well-ordered set that represents the result of the operation or by using transfinite recursion. In addition to these standard operations for ordinals, there are also the "natural" arithmetic operations, which are usually described using the Cantor normal form for ordinals, and nimber operations.

## Background

Ordinal numbers are like the counting numbers {0, 1, 2, ...} but go to infinity ω and beyond *ω*+1, *ω*+2, ..., *ω*+*ω*, *ω*+*ω*+1, .... The standard arithmetic operations and natural arithmetic operations on the finite ordinals are the same as the corresponding operations on the counting numbers, but arithmetic operations on the infinite ordinals are more complicated.

## Addition

The sum of two well-ordered sets S and T is the ordinal representing the variant of lexicographical order with least significant position first, on the union of the Cartesian products *S* × {0} and *T* × {1}. This way, every element of S is smaller than every element of T, comparisons within S keep the order they already have, and likewise for comparisons within T.

The definition of ordinal addition *α* + *β* can also be given by transfinite recursion on β. When the right addend *β* = 0, addition gives *α* + 0 = *α* for any α. For *β* > 0, the value of *α* + *β* is the smallest ordinal strictly greater than the sum of α and δ for all *δ* < *β*. Writing the successor and limit ordinals cases separately:

- *α* + 0 = *α*
- *α* + *S*(*β*) = *S*(*α* + *β*), where S denotes the *successor* function.
- *α* + *β* = $\bigcup _{\delta <\beta }$ (*α* + *δ*) when β is a limit ordinal.

Ordinal addition on the natural numbers is the same as standard addition. The first transfinite ordinal is ω, the set of all natural numbers, followed by *ω* + 1, *ω* + 2, etc. The ordinal *ω* + *ω* is obtained by two copies of the natural numbers ordered in the usual fashion and the second copy completely to the right of the first. Writing 0′ < 1′ < 2′ < ... for the second copy, *ω* + *ω* looks like

0 < 1 < 2 < 3 < ... < 0

′

< 1

′

< 2

′

< ...

This is different from ω because in ω only 0 does not have a direct predecessor while in *ω* + *ω* the two elements 0 and 0′ do not have direct predecessors.

### Properties

Ordinal addition is, in general, not commutative. For example, 3 + *ω* = *ω* since the order relation for 3 + *ω* is 0 < 1 < 2 < 0′ < 1′ < 2′ < ..., which can be relabeled to ω. In contrast *ω* + 3 is not equal to ω since the order relation 0 < 1 < 2 < ... < 0′ < 1′ < 2′ has a largest element (namely, 2′) and ω does not (ω and *ω* + 3 are equipotent, but not order-isomorphic).

Ordinal addition is still associative; one can see for example that (*ω* + 4) + *ω* = *ω* + (4 + *ω*) = *ω* + *ω*.

Addition is strictly increasing and continuous in the right argument:

α

<

β

⇒

γ

+

α

<

γ

+

β

but the analogous relation does not hold for the left argument; instead we only have:

α

<

β

⇒

α

+

γ

≤

β

+

γ

Ordinal addition is left-cancellative: if *α* + *β* = *α* + *γ*, then *β* = *γ*. Furthermore, one can define left subtraction for ordinals *β* ≤ *α*: there is a unique γ such that *α* = *β* + *γ*. On the other hand, right cancellation does not work:

3 +

ω

= 0 +

ω

=

ω

, but

3 ≠ 0

Nor does right subtraction, even when *β* ≤ *α*: for example, there does not exist any γ such that *γ* + 42 = *ω*.

If the ordinals less than α are closed under addition and contain 0, then α is occasionally called a γ-number (see *Additively indecomposable ordinal*). These are exactly the ordinals of the form *ω**β*.

## Multiplication

The Cartesian product, *S* × *T*, of two well-ordered sets S and T can be well-ordered by a variant of lexicographical order that puts the least significant position first. Effectively, each element of T is replaced by a disjoint copy of S. The order-type of the Cartesian product is the ordinal that results from multiplying the order-types of S and T.

The definition of ordinal multiplication can also be given by transfinite recursion on β. When the right factor *β* = 0, multiplication gives *α* · 0 = 0 for any α. For *β* > 0, the value of *α* · *β* is the smallest ordinal greater than or equal to (*α* · *δ*) + *α* for all *δ* < *β*. Writing the successor and limit ordinals cases separately:

- *α* · 0 = 0.
- *α* · *S*(*β*) = (*α* · *β*) + *α*, for a successor ordinal *S*(*β*).
- *α* · *β* = $\bigcup _{\delta <\beta }$ (*α* · *δ*), when β is a limit ordinal.

As an example, here is the order relation for *ω* · 2:

0

0

< 1

0

< 2

0

< 3

0

< ...

< 0

1

< 1

1

< 2

1

< 3

1

< ...

,

which has the same order type as *ω* + *ω*. In contrast, 2 · *ω* looks like this:

0

0

< 1

0

< 0

1

< 1

1

< 0

2

< 1

2

< 0

3

< 1

3

< ...

and after relabeling, this looks just like ω. Thus, *ω* · 2 = *ω* + *ω* ≠ *ω* = 2 · *ω*, showing that multiplication of ordinals is not in general commutative, c.f. pictures.

As is the case with addition, ordinal multiplication on the natural numbers is the same as standard multiplication.

### Properties

*α* · 0 = 0 · *α* = 0, and the zero-product property holds: *α* · *β* = 0 implies *α* = 0 or *β* = 0. The ordinal 1 is a multiplicative identity, *α* · 1 = 1 · *α* = *α*. Multiplication is associative, (*α* · *β*) · *γ* = *α* · (*β* · *γ*). Multiplication is strictly increasing and continuous in the right argument: (*α* < *β* and *γ* > 0) implies *γ* · *α* < *γ* · *β*. Multiplication is *not* strictly increasing in the left argument, for example, 1 < 2 but 1 · *ω* = 2 · *ω* = *ω*. However, it is (non-strictly) increasing, i.e. *α* ≤ *β* implies *α* · *γ* ≤ *β* · *γ*.

Multiplication of ordinals is not in general commutative. Specifically, a natural number greater than 1 never commutes with any infinite ordinal, and two infinite ordinals α and β commute if and only if *α**m* = *β**n* for some nonzero natural numbers m and n. The relation "α commutes with β" is an equivalence relation on the ordinals greater than 1, and all equivalence classes are countably infinite.

Distributivity holds, on the left: *α* ⋅ (*β* + *γ*) = *α* ⋅ *β* + *α* ⋅ *γ*. However, the distributive law on the right (*β* + *γ*) ⋅ *α* = *β* ⋅ *α* + *γ* ⋅ *α* is *not* generally true: (1 + 1) · *ω* = 2 · *ω* = *ω* while 1 · *ω* + 1 · *ω* = *ω* + *ω*, which is different. There is a left cancellation law: If *α* > 0 and *α* · *β* = *α* · *γ*, then *β* = *γ*. Right cancellation does not apply, e.g. 1 · *ω* = 2 · *ω* = *ω*, but 1 and 2 are different. A left division with remainder property holds: for all α and β, if *β* > 0, then there are unique γ and δ such that *α* = *β* · *γ* + *δ* and *δ* < *β*. Right division does not work: there is no α such that *α* · *ω* ≤ *ω**ω* ≤ (*α* + 1) · *ω*.

The ordinal numbers form a left near-semiring, but do *not* form a ring. Hence the ordinals are not a Euclidean domain, since they are not even a ring; furthermore the Euclidean "norm" would be ordinal-valued using the left division here.

A δ-number (see *Additively indecomposable ordinal § Multiplicatively indecomposable*) is an ordinal β greater than 1 such that *α* ⋅ *β* = *β* whenever 0 < *α* < *β*. These consist of the ordinal 2 and the ordinals of the form *β* = *ω**ω**γ*.

## Exponentiation

The definition of exponentiation via order types is most easily explained using Von Neumann's definition of an ordinal as the set of all smaller ordinals. Then, to construct a set of order type *α**β* consider the set of all functions *f* : *β* → *α* such that *f*(*x*) = 0 for all but finitely many elements *x* ∈ *β* (essentially, we consider the functions with finite support). This set is ordered lexicographically with the least significant position first: that is, we write *f* < *g* if and only if *f*(*x*) < *g*(*x*) for the value *x* = max{*y* | *f*(*y*) ≠ *g*(*y*)}. This is a well-ordering and its order type is an ordinal number, *α**β*.

The definition of ordinal exponentiation can also be given by transfinite recursion on the exponent β. When the exponent *β* = 0, exponentiation gives *α*0 = 1 for any α, including *α* = 0. For *β* > 0, the value of *α**β* is the smallest ordinal greater than or equal to *α**δ* · *α* for all *δ* < *β*. Writing the successor and limit ordinals cases separately:

- *α*0 = 1.
- *α**S*(*β*) = (*α**β*) · *α*, for a successor ordinal *S*(*β*).
- *α**β* = $\bigcup _{0<\delta <\beta }$ (*α**δ*), when β is a limit ordinal.

Both definitions simplify considerably if the exponent β is a finite number: *α**β* is then just the product of β copies of α; e.g. *ω*3 = *ω* · *ω* · *ω*, and the elements of *ω*3 can be viewed as triples of natural numbers, ordered lexicographically with least significant position first. This agrees with the ordinary exponentiation of natural numbers.

But for infinite exponents, the definition may not be obvious. For example, *α**ω* can be identified with a set of finite sequences of elements of α, properly ordered. The equation 2*ω* = *ω* expresses the fact that finite sequences of zeros and ones can be identified with natural numbers, using the binary number system. The ordinal *ω**ω* can be viewed as the order type of finite sequences of natural numbers; every element of *ω**ω* (i.e. every ordinal smaller than *ω**ω*) can be uniquely written in the form *ω**n*1 ⋅ *c*1 + *ω**n*2 ⋅ *c*2 + ⋯ + *ω**n**k* ⋅ *c**k*, where k, *n*1, ..., *n**k* are natural numbers, *c*1, ..., *c**k* are nonzero natural numbers, and *n*1 > ... > *n**k*.

The same is true in general: every element of *α**β* (i.e. every ordinal smaller than *α**β*) can be uniquely written in the form *α**b*1 ⋅ *a*1 + *α**b*2 ⋅ *a*2 + ⋯ + *α**b**k* ⋅ *a**k* where k is a natural number, *b*1, ..., *b**k* are ordinals smaller than β with *b*1 > ... > *b**k*, and *a*1, ..., *a**k* are nonzero ordinals smaller than α. This expression corresponds to the function *f* : *β* → *α* which sends *b**i* to *a**i* for *i* = 1, ..., *k* and sends all other elements of β to 0.

While the same exponent notation is used for ordinal exponentiation and cardinal exponentiation, the two operations are quite different and should not be confused. The cardinal exponentiation *A**B* is defined to be the cardinal number of the set of *all* functions *B* → *A*, while the ordinal exponentiation *α**β* only contains the functions *β* → *α* with finite support, typically a set of much smaller cardinality. To avoid confusing ordinal exponentiation with cardinal exponentiation, one can use symbols for ordinals (e.g. ω) in the former and symbols for cardinals (e.g. ℵ0) in the latter.

### Properties

- *α*0 = 1.
- If 0 < *α*, then 0*α* = 0.
- 1*α* = 1.
- *α*1 = *α*.
- *α**β* · *α**γ* = *α**β*+*γ*.
- (*α**β*)*γ* = *α**β*·*γ*.
- There are α, β, and γ for which (*α* · *β*)*γ* ≠ *α**γ* · *β**γ*. For instance, (*ω* · 2)2 = *ω* · 2 · *ω* · 2 = *ω*2 · 2 ≠ *ω*2 · 4.
- Ordinal exponentiation is strictly increasing and continuous in the right argument: If *γ* > 1 and *α* < *β*, then *γ**α* < *γ**β*.
- If *α* < *β*, then *α**γ* ≤ *β**γ*. Note, for instance, that 2 < 3 and yet 2*ω* = 3*ω* = *ω*.
- If *α* > 1 and *α**β* = *α**γ*, then *β* = *γ*. If *α* = 1 or *α* = 0 this is not the case.
- For all α and β, if *β* > 1 and *α* > 0 then there exist unique γ, δ, and ρ such that *α* = *β**γ* · *δ* + *ρ* such that 0 < *δ* < *β* and *ρ* < *β**γ*.

Jacobsthal showed that the only solutions of *α**β* = *β**α* with *α* ≤ *β* are given by *α* = *β*, or *α* = 2 and *β* = 4, or α is any limit ordinal and *β* = *ε* ⋅ *α* where ε is an ε-number larger than α.

## Beyond exponentiation

There are ordinal operations that continue the sequence begun by addition, multiplication, and exponentiation, including ordinal versions of tetration and other hyperoperations. See also *Veblen function*.

## Cantor normal form

Every ordinal number *α* can be uniquely written as *ω**β*1 ⋅ *c*1 + *ω**β*2 ⋅ *c*2 + ⋯ + *ω**β**k* ⋅ *c**k*, where k is a natural number, *c*1, *c*2, ..., *c**k* are nonzero natural numbers, and *β*1 > *β*2 > ... > *β**k* ≥ 0 are ordinal numbers. The degenerate case *α* = 0 occurs when *k* = 0 which requires there be no βs nor cs. This decomposition of α is called the **Cantor normal form** of α, and can be considered the base-ω positional numeral system. The highest exponent *β*1 is called the degree of *α*, and satisfies *β*1 ≤ *α*. The equality *β*1 = *α* applies if and only if *α* = *ω**α*. In that case Cantor normal form fails to express the ordinal in terms of smaller ones; this can happen as explained below.

To compare two ordinals written in Cantor normal form, first compare *β*1, then *c*1, then *β*2, then *c*2, and so on. At the first occurrence of inequality, the ordinal that has the larger component is the larger ordinal. If they are the same until one terminates before the other, then the one that terminates first is smaller.

The Cantor normal form allows us to uniquely express—and order—the ordinals α that are built from the natural numbers by a finite number of arithmetical operations of addition, multiplication and exponentiation base-*ω*: in other words, assuming *β*1 < *α* in the Cantor normal form, we can also express the exponents *β**i* in Cantor normal form, and making the same assumption for the *β**i* as for α and so on recursively, we get a system of notation for these ordinals (for example,

ω

ω

ω

7

⋅6+

ω

+42

⋅1729+

ω

9

+88

⋅3 +

ω

ω

ω

⋅5 + 65537

denotes an ordinal).

### Fixed point

The ordinal *ε*0 (epsilon nought) is the set of ordinal values *α* of the finite-length arithmetical expressions of Cantor normal form that are hereditarily non-trivial where non-trivial means *β*1 < *α* when 0 < *α*. It is the smallest ordinal such that *ε*0 = *ω**ε*0, i.e. in Cantor normal form the exponent is not smaller than the ordinal itself. It is the limit of the sequence

0, 1 =

ω

0

,

ω

=

ω

1

,

ω

ω

,

ω

ω

ω

, ...

.

The ordinal *ε*0 is important for various reasons in arithmetic (essentially because it measures the proof-theoretic strength of the first-order Peano arithmetic: that is, Peano's axioms can show transfinite induction up to any ordinal less than *ε*0 but not up to *ε*0 itself).

### Sums

The Cantor normal form also allows us to compute sums and products of ordinals: to compute the sum, for example, one need merely know (see the properties listed in § Addition and § Multiplication) that

ω

β

⋅

c

+

ω

β

′

⋅

c

′

=

ω

β

′

⋅

c

′

,

if *β′* > *β*. If *β′* = *β* one can apply the distributive law on the left and rewrite this as *ω**β*(*c* + *c′*), and if *β′* < *β* the expression is already in Cantor normal form). E.g.

$(\omega ^{2}\cdot 2+\omega \cdot 3+4)+(\omega \cdot 5+6)=\omega ^{2}\cdot 2+\omega \cdot 8+6.$

### Products

To compute products, the essential facts are that when 0 < *α* = *ω**β*1 ⋅ *c*1 + ⋯ + *ω**β**k* ⋅ *c**k* is in Cantor normal form and 0 < *β′*, then

α

⋅

ω

β

′

=

ω

β

1

+

β

′

and

α

⋅

n

=

ω

β

1

⋅

c

1

⋅

n

+

ω

β

2

⋅

c

2

+ ⋯ +

ω

β

k

⋅

c

k

,

if n is a non-zero natural number. E.g.

$(\omega ^{3}\cdot 7+\omega +1)\cdot (\omega \cdot 8+9)=\omega ^{4}\cdot 8+\omega ^{3}\cdot 63+\omega +1.$

### Powers

If ωα ≤ β < ωα+1, then βω = ωα·ω. For example,

$(\omega ^{\omega }\cdot 2+\omega \cdot 3+4)^{(\omega ^{2}\cdot 5+2)}=(\omega ^{\omega ^{3}\cdot 5})\cdot (\omega ^{\omega \cdot 2}\cdot 2+\omega ^{\omega +1}\cdot 3+\omega ^{\omega }\cdot 8+\omega \cdot 3+4)$

$=\omega ^{\omega ^{3}\cdot 5+\omega \cdot 2}\cdot 2+\omega ^{\omega ^{3}\cdot 5+\omega +1}\cdot 3+\omega ^{\omega ^{3}\cdot 5+\omega }\cdot 8+\omega ^{\omega ^{3}\cdot 5+1}\cdot 3+\omega ^{\omega ^{3}\cdot 5}\cdot 4$

### Variations

A variation of Cantor normal form is to set all the numbers *c**i* equal to 1 and allow the exponents to be equal. In other words, every ordinal number *α* can be uniquely written as *ω**β*1 + *ω**β*2 + ⋯ + *ω**β**k*, where k is a natural number, and *β*1 ≥ *β*2 ≥ ... ≥ *β**k* ≥ 0 are ordinal numbers.

Another variation of the Cantor normal form is the "base δ expansion", where ω is replaced by any ordinal *δ* ≥ 2 and the coefficients satisfy 1 ≤ *c**i* < *δ*.

## Factorization into primes

Ernst Jacobsthal showed that the ordinals satisfy a form of the unique factorization theorem: every nonzero ordinal can be written as a product of a finite number of prime ordinals. This factorization into prime ordinals is in general not unique, but there is a "minimal" factorization into primes that is unique up to changing the order of finite prime factors (Sierpiński 1958).

A prime ordinal is an ordinal greater than 1 that cannot be written as a product of two smaller ordinals. Some of the first primes are 2, 3, 5, ... , ω, *ω* + 1, *ω*2 + 1, *ω*3 + 1, ..., *ω**ω*, *ω**ω* + 1, *ω**ω*+1 + 1, ... There are three types of prime ordinals:

- The finite primes 2, 3, 5, ...
- The ordinals of the form *ω**ω**α* for any ordinal α. These are the prime ordinals that are limits, and are the delta numbers, the transfinite ordinals that are closed under multiplication.
- The ordinals of the form *ω**α* + 1 for any ordinal *α* > 0. These are the infinite successor primes, and are the successors of gamma numbers, the additively indecomposable ordinals.

Factorization into primes is not unique: for example, 2 ⋅ 3 = 3 ⋅ 2, 2 ⋅ *ω* = *ω*, (*ω* + 1) ⋅ *ω* = *ω* ⋅ *ω* and *ω* ⋅ *ω**ω* = *ω**ω*. However, there is a unique factorization into primes satisfying the following additional conditions:

- Every limit prime must occur before any successor prime
- If two consecutive primes of the prime factorization are both limits or both finite, the second one must be less than or equal to the first one.

This prime factorization can easily be read off using the Cantor normal form as follows:

- First write the ordinal as a product *α* ⋅ *β*, where α is the smallest power of ω in the Cantor normal form and β is a successor.
- If *α* = *ω**γ* then writing γ in Cantor normal form gives an expansion of α as a product of limit primes.
- Now look at the Cantor normal form of β. If *β* = *ω**λ* ⋅ *m* + *ω**μ* ⋅ *n* + smaller terms, then *β* = (*ω**μ* ⋅ *n* + smaller terms) ⋅ (*ω**λ*−*μ* + 1) ⋅ *m* is a product of a smaller ordinal and a prime and a natural number m. Repeating this and factorizing the natural numbers into primes gives the prime factorization of β.

So the factorization of the Cantor normal form ordinal

ω

α

1

⋅

n

1

+ ⋯ +

ω

α

k

⋅

n

k

(with

α

1

> ... >

α

k

)

into a minimal product of infinite primes and natural numbers is

(

ω

ω

β

1

⋅ ⋯ ⋅

ω

ω

β

m

) ⋅

n

k

⋅ (

ω

α

k

−1

−α

k

+ 1) ⋅

n

k

−1

⋅ ⋯ ⋅ (

ω

α

1

−

α

2

+ 1) ⋅

n

1

where each *n**i* should be replaced by its factorization into a non-increasing sequence of finite primes and

α

k

=

ω

β

1

+ ⋯ +

ω

β

m

with

β

1

≥ ... ≥

β

m

.

## Large countable ordinals

As discussed above, the Cantor normal form of ordinals below *ε*0 can be expressed in an alphabet containing only the function symbols for addition, multiplication and exponentiation, as well as constant symbols for each natural number and for ω. We can do away with the infinitely many numerals by using just the constant symbol 0 and the operation of successor, *S* (for example, the natural number 3 may be expressed as *S*(*S*(*S*(0))). This describes an *ordinal notation*: a system for naming ordinals over a finite alphabet. This particular system of ordinal notation is called the collection of *arithmetical* ordinal expressions, and can express all ordinals below *ε*0, but cannot express *ε*0. There are other ordinal notations capable of capturing ordinals well past *ε*0, but because there are only countably many finite-length strings over any finite alphabet, for any given ordinal notation there will be ordinals below *ω*1 (the first uncountable ordinal) that are not expressible. Such ordinals are known as large countable ordinals.

The operations of addition, multiplication and exponentiation are all examples of primitive recursive ordinal functions, and more general primitive recursive ordinal functions can be used to describe larger ordinals.

## Natural operations

The **natural sum** and **natural product** operations on ordinals were defined in 1906 by Gerhard Hessenberg, and are sometimes called the **Hessenberg sum** (or product) (Sierpiński 1958). The natural sum of α and β is often denoted by *α* ⊕ *β* or *α* # *β*, and the natural product by *α* ⊗ *β* or *α* ⨳ *β*.

The natural sum and product are defined as follows. Let *α* = *ω**α*1 + ⋯ + *ω**α**k* and *β* = *ω**β*1 + ⋯ + *ω**β**ℓ* be in Cantor normal form (i.e. *α*1 ≥ ... ≥ *α**k* and *β*1 ≥ ... ≥ *β**ℓ*). Let *γ*1, ..., *γ**k*+*ℓ* be the exponents *α*1, ..., *α**k*, *β*1, ..., *β**ℓ* sorted in nonincreasing order. Then *α* ⊕ *β* is defined as

α

⊕

β

=

ω

γ

1

+ ⋯ +

ω

γ

k

+

ℓ

.

The natural product of *α* and *β* is defined as

α

⊗

β

=

$\bigoplus _{\begin{aligned}&1\leq i\leq k\\&1\leq j\leq \ell \end{aligned}}$

ω

α

i

⊕

β

j

.

For example, suppose *α* = *ω**ω**ω* + *ω* and *β* = *ω**ω* + *ω*5. Then *α* ⊕ *β* = *ω**ω**ω* + *ω**ω* + *ω*5 + *ω*, whereas *α* + *β* = *ω**ω**ω* + *ω**ω* + *ω*5. And *α* ⊗ *β* = *ω**ω**ω*+*ω* + *ω**ω**ω*+5 + *ω**ω*+1 + *ω*6, whereas *α* ⋅ *β* = *ω**ω**ω*+*ω* + *ω**ω**ω*+5.

The natural sum and product are commutative and associative, and natural product distributes over natural sum. The operations are also monotonic, in the sense that if *α* < *β* then *α* ⊕ *γ* < *β* ⊕ *γ*; if *α* ≤ *β* then *α* ⊗ *γ* ≤ *β* ⊗ *γ*; and if *α* < *β* and *γ* > 0 then *α* ⊗ *γ* < *β* ⊗ *γ*.

We have $\underbrace {\alpha \oplus \cdots \oplus \alpha } _{n}=\alpha \otimes n$ .

We always have *α* + *β* ≤ *α* ⊕ *β* and *α* ⋅ *β* ≤ *α* ⊗ *β*. If both *α* < *ω**γ* and *β* < *ω**γ* then *α* ⊕ *β* < *ω**γ*. If both *α* < *ω**ω**γ* and *β* < *ω**ω**γ* then *α* ⊗ *β* < *ω**ω**γ*.

Natural sum and product are not continuous. For example, if natural sum were continuous then lim*n*<*ω* (1 ⊕ *n*) = 1 ⊕ *ω*, but the left-hand side equals ω and the right-hand side equals *ω* + 1. Similarly, if natural product were continuous lim*n*<*ω* (2 ⊗ *n*) = 2 ⊗ *ω*, but the left-hand side equals ω and the right-hand side equals (*ω*0 + *ω*0) ⊗ *ω*1 = *ω*1 + *ω*1 = *ω* · 2.

The natural sum and product are the same as the addition and multiplication (restricted to ordinals) of John Conway's field of surreal numbers.

The natural operations come up in the theory of well partial orders; given two well partial orders *S* and *T*, of types (maximum linearizations) *o*(*S*) and *o*(*T*), the type of the disjoint union is *o*(*S*) ⊕ *o*(*T*), while the type of the direct product is *o*(*S*) ⊗ *o*(*T*). One may take this relation as a definition of the natural operations by choosing S and T to be ordinals α and β; so *α* ⊕ *β* is the maximum order type of a total order extending the disjoint union (as a partial order) of α and β; while *α* ⊗ *β* is the maximum order type of a total order extending the direct product (as a partial order) of α and β. A useful application of this is when α and β are both subsets of some larger total order; then their union has order type at most *α* ⊕ *β*. If they are both subsets of some ordered abelian group, then their sum has order type at most *α* ⊗ *β*.

We can also define the natural sum *α* ⊕ *β* by simultaneous transfinite recursion on α and β, as the smallest ordinal strictly greater than the natural sum of α and γ for all *γ* < *β* and of γ and β for all *γ* < *α*. Similarly, we can define the natural product *α* ⊗ *β* by simultaneous transfinite recursion on α and β, as the smallest ordinal γ such that (*α* ⊗ *δ*) ⊕ (*ε* ⊗ *β*) < *γ* ⊕ (*ε* ⊗ *δ*) for all *ε* < *α* and *δ* < *β*. Also, see the article on surreal numbers for the definition of natural multiplication in that context; however, it uses surreal subtraction, which is not defined on ordinals.

The natural sum is associative and commutative. It is always greater or equal to the usual sum, but it may be strictly greater. For example, the natural sum of ω and 1 is *ω* + 1 (the usual sum), but this is also the natural sum of 1 and ω. The natural product is associative and commutative and distributes over the natural sum. The natural product is always greater or equal to the usual product, but it may be strictly greater. For example, the natural product of ω and 2 is *ω* · 2 (the usual product), but this is also the natural product of 2 and ω.

Under natural addition, the ordinals can be identified with the elements of the free commutative monoid generated by the gamma numbers *ω**α*. Under natural addition and multiplication, the ordinals can be identified with the elements of the free commutative semiring generated by the delta numbers *ω**ω**α*. The ordinals do not have unique factorization into primes under the natural product. While the full polynomial ring does have unique factorization, the subset of polynomials with non-negative coefficients does not: for example, if x is any delta number, then

x

5

+

x

4

+

x

3

+

x

2

+

x

+ 1 = (

x

+ 1) (

x

4

+

x

2

+ 1) = (

x

2

+

x

+ 1) (

x

3

+ 1)

has two incompatible expressions as a natural product of polynomials with non-negative coefficients that cannot be decomposed further.

## Nimber arithmetic

There are arithmetic operations on ordinals by virtue of the one-to-one correspondence between ordinals and nimbers. Three common operations on nimbers are nimber addition, nimber multiplication, and minimum excluded value (mex). Nimber addition is a generalization of the bitwise exclusive or operation on natural numbers. The mex of a set of ordinals is the smallest ordinal *not* present in the set.
