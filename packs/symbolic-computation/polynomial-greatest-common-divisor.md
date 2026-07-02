---
title: "Polynomial greatest common divisor"
source: https://en.wikipedia.org/wiki/Polynomial_greatest_common_divisor
domain: symbolic-computation
license: CC-BY-SA-4.0
tags: symbolic computation, computer algebra system, grobner basis, symbolic integration
fetched: 2026-07-02
---

# Polynomial greatest common divisor

In algebra, the **greatest common divisor** (frequently abbreviated **GCD** or **gcd**) of two polynomials is a polynomial, of the highest possible degree, which is a factor of both the two original polynomials. This concept is analogous to the greatest common divisor of two integers.

In the important case of univariate polynomials over a field, the polynomial GCD may be computed as for the integer GCD, with the Euclidean algorithm using long division. The polynomial GCD is defined only up to the multiplication by an invertible constant.

The similarity between integer GCD and polynomial GCD allows extending to univariate polynomials all the properties that may be deduced from the Euclidean algorithm and Euclidean division. Moreover, the polynomial GCD has specific properties that make it a fundamental notion in various areas of algebra. Typically, the roots of the GCD of two polynomials are the common roots of the two polynomials, and this provides information on the roots without computing them. For example, the multiple roots of a polynomial are the roots of the GCD of the polynomial and its derivative, and further GCD computations allow computing the square-free factorization of the polynomial, which provides polynomials whose roots are the roots of a given multiplicity of the original polynomial.

The greatest common divisor may be defined and exists, more generally, for multivariate polynomials over a field, over the ring of integers, and over any unique factorization domain. There exist algorithms to compute them as soon as one has a GCD algorithm in the ring of coefficients. These algorithms proceed by a recursion on the number of variables to reduce the problem to a variant of the Euclidean algorithm. They are a fundamental tool in computer algebra, because computer algebra systems use them systematically to simplify fractions: this was the motivation for much of the modern theory of polynomial GCD.

## General definition

Let *p* and *q* be polynomials with coefficients in an integral domain *F*, typically a field or the integers. A **greatest common divisor** of *p* and *q* is a polynomial *d* that divides *p* and *q*, and such that every common divisor of *p* and *q* also divides *d*. Every pair of polynomials (not both zero) has a GCD if and only if *F* is a unique factorization domain.

If *F* is a field and *p* and *q* are not both zero, a polynomial *d* is a greatest common divisor if and only if it divides both *p* and *q*, and it has the greatest degree among the polynomials having this property. If *p* = *q* = 0, the GCD is 0; however some authors consider that it is not defined in this case.

The greatest common divisor of *p* and *q* is usually denoted gcd(*p*, *q*).

The greatest common divisor is unique only up to multiplication by an invertible constant. That is, if *d* is a GCD of *p* and *q*, then the polynomial *c* is another GCD if and only if there is an invertible element *u* of *F* such that $c=ud\quad {\text{ and }}\quad d=u^{-1}c.$ In the case of the integers, this ambiguity may be removed by choosing the unique positive GCD, rather than its negative. For univariate polynomials over a field, one can instead choose the standard GCD to be the unique monic choice (having leading coefficient 1), but over more general coefficient rings there is no standard choice. Therefore, equalities like *d* = gcd(*p*, *q*) or gcd(*p*, *q*) = gcd(*r*, *s*) should be understood to mean "*d* is a GCD of *p* and *q*" and "*p* and *q* have the same set of GCDs as *r* and *s*". In particular, gcd(*p*, *q*) = 1 means that the invertible constants are the only common divisors: in this case, by analogy with the ring of integers, one says that *p* and *q* are **coprime polynomials**.

## Properties

- As stated above, the GCD of two polynomials exists if the coefficients belong either to a field, the ring of the integers, or more generally to a unique factorization domain.
- If *c* is any common divisor of *p* and *q*, then *c* divides their GCD.
- $\gcd(p,q)=\gcd(q,p).$
- $\gcd(p,q)=\gcd(q,p+rq)$ for any polynomial *r*. This property is at the basis of the proof of Euclidean algorithm.
- For any invertible element *k* of the ring of the coefficients, $\gcd(p,q)=\gcd(p,kq)$ .
- Hence $\gcd(p,q)=\gcd(a_{1}p+b_{1}q,a_{2}p+b_{2}q)$ for any scalars $a_{1},b_{1},a_{2},b_{2}$ such that $a_{1}b_{2}-a_{2}b_{1}$ is invertible.
- If $\gcd(p,r)=1$ , then $\gcd(p,q)=\gcd(p,qr)$ .
- If $\gcd(q,r)=1$ , then $\gcd(p,qr)=\gcd(p,q)\,\gcd(p,r)$ .
- For two univariate polynomials *p* and *q* over a field, there exist polynomials *a* and *b*, such that $\gcd(p,q)=ap+bq$ and $\gcd(p,q)$ divides every such linear combination of *p* and *q* (Bézout's identity).
- The greatest common divisor of three or more polynomials may be defined similarly as for two polynomials. It may be computed recursively from GCD's of two polynomials by the identities: $\gcd(p,q,r)=\gcd(p,\gcd(q,r)),$ and $\gcd(p_{1},p_{2},\dots ,p_{n})=\gcd(p_{1},\gcd(p_{2},\dots ,p_{n})).$

## GCD by hand computation

There are several ways to find the greatest common divisor of two polynomials. Two of them are:

1. *Factorization of polynomials*, in which one finds the factors of each expression, then selects the set of common factors held by all from within each set of factors. This method may be useful only in simple cases, as factoring is usually more difficult than computing the greatest common divisor.
2. The *Euclidean algorithm*, which can be used to find the GCD of two polynomials in the same manner as for two numbers.

### Factoring

To find the GCD of two polynomials using factoring, simply factor the two polynomials completely. Then, take the product of all common factors. At this stage, we do not necessarily have a monic polynomial, so finally multiply this by a constant to make it a monic polynomial. This will be the GCD of the two polynomials as it includes all common divisors and is monic.

Example one: Find the GCD of *x*2 + 7*x* + 6 and *x*2 − 5*x* − 6.

x

2

+ 7

x

+ 6 = (

x

+ 1)(

x

+ 6)

x

2

− 5

x

− 6 = (

x

+ 1)(

x

− 6)

Thus, their GCD is *x* + 1.

### Euclidean algorithm

Factoring polynomials can be difficult, especially if the polynomials have a large degree. The Euclidean algorithm is a method that works for any pair of polynomials. It makes repeated use of Euclidean division. When using this algorithm on two numbers, the size of the numbers decreases at each stage. With polynomials, the degree of the polynomials decreases at each stage. The last nonzero remainder, made monic if necessary, is the GCD of the two polynomials.

More specifically, for finding the gcd of two polynomials *a*(*x*) and *b*(*x*), one can suppose *b* ≠ 0 (otherwise, the GCD is *a*(*x*)), and $\deg(b(x))\leq \deg(a(x))\,.$

The Euclidean division provides two polynomials *q*(*x*), the *quotient* and *r*(*x*), the *remainder* such that $a(x)=q_{0}(x)b(x)+r_{0}(x)\quad {\text{and}}\quad \deg(r_{0}(x))<\deg(b(x))$

A polynomial *g*(*x*) divides both *a*(*x*) and *b*(*x*) if and only if it divides both *b*(*x*) and *r*0(*x*). Thus $\gcd(a(x),b(x))=\gcd(b(x),r_{0}(x)).$ Setting $a_{1}(x)=b(x),b_{1}(x)=r_{0}(x),$ one can repeat the Euclidean division to get new polynomials *q*1(*x*), *r*1(*x*), *a*2(*x*), *b*2(*x*) and so on. At each stage we have $\deg(a_{k+1})+\deg(b_{k+1})<\deg(a_{k})+\deg(b_{k}),$ so the sequence will eventually reach a point at which $b_{N}(x)=0$ and one has got the GCD: $\gcd(a,b)=\gcd(a_{1},b_{1})=\cdots =\gcd(a_{N},0)=a_{N}.$

**Example:** finding the GCD of *x*2 + 7*x* + 6 and *x*2 − 5*x* − 6:

x

2

+ 7

x

+ 6

= 1 ⋅

(

x

2

− 5

x

− 6)

+

(12

x

+ 12)

x

2

− 5

x

− 6

=

(12

x

+ 12)

(

⁠

1

/

12

⁠

x

−

⁠

1

/

2

⁠

) + 0

Since 12 *x* + 12 is the last nonzero remainder, it is a GCD of the original polynomials, and the monic GCD is *x* + 1.

In this example, it is not difficult to avoid introducing denominators by factoring out 12 before the second step. This can always be done by using pseudo-remainder sequences, but, without care, this may introduce very large integers during the computation. Therefore, for computer computation, other algorithms are used, that are described below.

This method works only if one can test the equality to zero of the coefficients that occur during the computation. So, in practice, the coefficients must be integers, rational numbers, elements of a finite field, or must belong to some finitely generated field extension of one of the preceding fields. If the coefficients are floating-point numbers that represent real numbers that are known only approximately, then one must know the degree of the GCD for having a numerically stable result; in this case other techniques may be used, usually based on singular value decomposition.

## Univariate polynomials with coefficients in a field

The basic case of univariate polynomials over a field is especially important. It is the simplest example beyond the ring of integers, and this analogy is the source of the notion of Euclidean domain. The theory and algorithms for the multivariate case and for coefficients in a unique factorization domain depend heavily on the basic case. Polynomial GCD algorithms and derived algorithms allow one to get useful information on the roots of a polynomial, without computing them.

### Euclidean division

Euclidean division of polynomials, which is used in Euclid's algorithm for computing GCDs, is very similar to Euclidean division of integers. Its existence is based on the following theorem: Given two univariate polynomials ${\textstyle a}$ and $b\neq 0$ defined over a field, there exist two polynomials q (the *quotient*) and r (the *remainder*) which satisfy $a=bq+r$ and $\deg(r)<\deg(b),$ where "deg(...)" denotes the degree and the degree of the zero polynomial is defined as being negative. Moreover, *q* and *r* are uniquely defined by these relations.

The difference from Euclidean division of the integers is that, for the integers, the degree is replaced by the absolute value, and that to have uniqueness one has to suppose that *r* is non-negative. The rings for which such a theorem exists are called Euclidean domains.

Like for the integers, the Euclidean division of the polynomials may be computed by the long division algorithm. This algorithm is usually presented for paper-and-pencil computation, but it works well on computers when formalized as follows (note that the names of the variables correspond exactly to the regions of the paper sheet in a pencil-and-paper computation of long division). In the following computation "deg" stands for the degree of its argument (with the convention deg(0) < 0), and "lc" stands for the leading coefficient, the coefficient of the highest degree of the variable.

**Euclidean division**

***Input:*** *a* and *b* ≠ 0 two polynomials in the variable *x*; ***Output:*** *q*, the quotient, and *r*, the remainder;

***begin***

```
   q := 0
   r := a
   d := deg(b)
   c := lc(b)
   while deg(r) ≥ d do
       s := (lc(r)/c) ⋅ xdeg(r)−d
       q := q + s
       r := r − sb
   end do
   return (q, r)
```

***end***

The proof of the validity of this algorithm relies on the fact that during the whole "while" loop, we have *a* = *bq* + *r* and deg(*r*) is a non-negative integer that decreases at each iteration. Thus the proof of the validity of this algorithm also proves the validity of the Euclidean division.

### Euclid's algorithm

As for the integers, the Euclidean division allows us to define Euclid's algorithm for computing GCDs.

Starting from two polynomials *a* and *b*, Euclid's algorithm consists of recursively replacing the pair (*a*, *b*) by (*b*, rem(*a*, *b*)) (where "rem(*a*, *b*)" denotes the remainder of the Euclidean division, computed by the algorithm of the preceding section), until *b* = 0. The GCD is the last non zero remainder.

Euclid's algorithm may be formalized in the recursive programming style as: $\gcd(a,b):={\begin{cases}a&{\text{if }}b=0\\\gcd(b,\operatorname {rem} (a,b))&{\text{otherwise}}.\end{cases}}$

In the imperative programming style, the same algorithm becomes, giving a name to each intermediate remainder:

*r*0 := *a* *r*1 := *b*

***for*** (*i* := 1; *ri* ≤ 0; *i* := *i* + 1) ***do***

```
   ri+1 := rem(ri−1, ri)
```

***end do***

***return*** *r**i*-1.

The sequence of the degrees of the *ri* is strictly decreasing. Thus after, at most, deg(*b*) steps, one get a null remainder, say *rk*. As (*a*, *b*) and (*b*, rem(*a*,*b*)) have the same divisors, the set of the common divisors is not changed by Euclid's algorithm and thus all pairs (*ri*, *r**i*+1) have the same set of common divisors. The common divisors of a and b are thus the common divisors of *r**k*−1 and 0. Thus *r**k*−1 is a GCD of a and b. This not only proves that Euclid's algorithm computes GCDs but also proves that GCDs exist.

### Bézout's identity and extended GCD algorithm

Bézout's identity is a GCD related theorem, initially proved for the integers, which is valid for every principal ideal domain. In the case of the univariate polynomials over a field, it may be stated as follows.

If

g

is the greatest common divisor of two polynomials

a

and

b

(not both zero), then there are two polynomials

u

and

v

such that

$au+bv=g$

(Bézout's identity)

and either *u* = 1, *v* = 0, or *u* = 0, *v* = 1, or

$\deg(u)<\deg(b)-\deg(g),\quad \deg(v)<\deg(a)-\deg(g).$

The interest of this result in the case of the polynomials is that there is an efficient algorithm to compute the polynomials u and v. This algorithm differs from Euclid's algorithm by a few more computations done at each iteration of the loop. It is therefore called **extended GCD algorithm**. Another difference with Euclid's algorithm is that it also uses the quotient, denoted "quo", of the Euclidean division instead of only the remainder. This algorithm works as follows.

**Extended GCD** algorithm

***Input:*** *a*, *b*, univariate polynomials

***Output:***

```
   g, the GCD of a and b
   u, v, as in above statement
   a1, b1, such that
       a = g a1
       b = g b1
```

***Begin***

```
   (r0, r1) := (a, b)
   (s0, s1) := (1, 0)
   (t0, t1) := (0, 1)
 
   for (i := 1; ri ≠ 0; i := i+1) do
       q := quo(ri−1, ri)
       ri+1 := ri−1 − qri
       si+1 := si−1 − qsi
       ti+1 := ti−1 − qti
   end do
   g := ri−1
   u := si−1
   v := ti−1
   a1 := (−1)i−1 ti
   b1 := (−1)i si
```

***End***

The proof that the algorithm satisfies its output specification relies on the fact that, for every i we have $r_{i}=as_{i}+bt_{i}$ $s_{i}t_{i+1}-t_{i}s_{i+1}=s_{i}t_{i-1}-t_{i}s_{i-1},$ the latter equality implying $s_{i}t_{i+1}-t_{i}s_{i+1}=(-1)^{i}.$ The assertion on the degrees follows from the fact that, at every iteration, the degrees of *si* and *ti* increase at most as the degree of *ri* decreases.

An interesting feature of this algorithm is that, when the coefficients of Bezout's identity are needed, one gets for free the quotient of the input polynomials by their GCD.

#### Arithmetic of algebraic extensions

An important application of the extended GCD algorithm is that it allows one to compute division in algebraic field extensions.

Let L an algebraic extension of a field K, generated by an element whose minimal polynomial f has degree n. The elements of L are usually represented by univariate polynomials over K of degree less than n.

The addition in L is simply the addition of polynomials: $a+_{L}b=a+_{K[X]}b.$

The multiplication in L is the multiplication of polynomials followed by the division by f: $a\cdot _{L}b=\operatorname {rem} (a._{K[X]}b,f).$

The inverse of a non zero element a of L is the coefficient u in Bézout's identity *au* + *fv* = 1, which may be computed by extended GCD algorithm. (The GCD is 1 because the minimal polynomial f is irreducible.) The degree inequality in the specification of extended GCD algorithm shows that a further division by f is not needed to get deg(u) < deg(f).

### Subresultants

In the case of univariate polynomials, there is a strong relationship between greatest common divisors and resultants. More precisely, the resultant of two polynomials *P*, *Q* is a polynomial function of the coefficients of *P* and *Q* which has the value zero if and only if the GCD of *P* and *Q* is not constant.

The theory of subresultantsis a generalization of this property that allows characterizing generically the GCD of two polynomials, and the resultant is the 0-th subresultant polynomial.

The i-th *subresultant polynomial* *Si*(*P*, *Q*) of two polynomials *P* and *Q* is a polynomial of degree at most i whose coefficients are polynomial functions of the coefficients of *P* and *Q*, and the i-th *principal subresultant coefficient* *si*(*P*, *Q*) is the coefficient of degree i of *Si*(*P*, *Q*). They have the property that the GCD of *P* and *Q* has a degree d if and only if $s_{0}(P,Q)=\cdots =s_{d-1}(P,Q)=0,\ s_{d}(P,Q)\neq 0.$

In this case, *Sd*(*P*, *Q*) is a GCD of *P* and *Q* and $S_{0}(P,Q)=\cdots =S_{d-1}(P,Q)=0.$

Every coefficient of the subresultant polynomials is defined as the determinant of a submatrix of the Sylvester matrix of *P* and *Q*. This implies that subresultants "specialize" well. More precisely, subresultants are defined for polynomials over any commutative ring *R*, and have the following property.

Let *φ* be a ring homomorphism of *R* into another commutative ring *S*. It extends to another homomorphism, denoted also *φ* between the polynomials rings over *R* and *S*. Then, if *P* and *Q* are univariate polynomials with coefficients in *R* such that $\deg(P)=\deg(\varphi (P))$ and $\deg(Q)=\deg(\varphi (Q)),$ then the subresultant polynomials and the principal subresultant coefficients of *φ*(*P*) and *φ*(*Q*) are the image by *φ* of those of *P* and *Q*.

The subresultants have two important properties which make them fundamental for the computation on computers of the GCD of two polynomials with integer coefficients. Firstly, their definition through determinants allows bounding, through Hadamard inequality, the size of the coefficients of the GCD. Secondly, this bound and the property of good specialization allow computing the GCD of two polynomials with integer coefficients through modular computation and Chinese remainder theorem (see below).

#### Technical definition

Let $P=p_{0}+p_{1}X+\cdots +p_{m}X^{m},\quad Q=q_{0}+q_{1}X+\cdots +q_{n}X^{n}.$ be two univariate polynomials with coefficients in a field *K*. Let us denote by ${\mathcal {P}}_{i}$ the *K* vector space of dimension i of polynomials of degree less than i. For non-negative integer i such that *i* ≤ *m* and *i* ≤ *n*, let $\varphi _{i}:{\mathcal {P}}_{n-i}\times {\mathcal {P}}_{m-i}\rightarrow {\mathcal {P}}_{m+n-i}$ be the linear map such that $\varphi _{i}(A,B)=AP+BQ.$

The resultant of *P* and *Q* is the determinant of the Sylvester matrix, which is the (square) matrix of $\varphi _{0}$ on the bases of the powers of *X*. Similarly, the *i*-subresultant polynomial is defined in term of determinants of submatrices of the matrix of $\varphi _{i}.$

Let us describe these matrices more precisely;

Let *p**i* = 0 for *i* < 0 or *i* > *m*, and *q**i* = 0 for *i* < 0 or *i* > *n*. The Sylvester matrix is the (*m* + *n*) × (*m* + *n*)-matrix such that the coefficient of the *i*-th row and the *j*-th column is *p**m*+*j*−*i* for *j* ≤ *n* and *q**j*−*i* for *j* > *n*: $S={\begin{pmatrix}p_{m}&0&\cdots &0&q_{n}&0&\cdots &0\\p_{m-1}&p_{m}&\cdots &0&q_{n-1}&q_{n}&\cdots &0\\p_{m-2}&p_{m-1}&\ddots &0&q_{n-2}&q_{n-1}&\ddots &0\\\vdots &\vdots &\ddots &p_{m}&\vdots &\vdots &\ddots &q_{n}\\\vdots &\vdots &\cdots &p_{m-1}&\vdots &\vdots &\cdots &q_{n-1}\\p_{0}&p_{1}&\cdots &\vdots &q_{0}&q_{1}&\cdots &\vdots \\0&p_{0}&\ddots &\vdots &0&q_{0}&\ddots &\vdots \\\vdots &\vdots &\ddots &p_{1}&\vdots &\vdots &\ddots &q_{1}\\0&0&\cdots &p_{0}&0&0&\cdots &q_{0}\end{pmatrix}}.$

The matrix *Ti* of $\varphi _{i}$ is the (*m* + *n* − *i*) × (*m* + *n* − 2*i*)-submatrix of *S* which is obtained by removing the last *i* rows of zeros in the submatrix of the columns 1 to *n* − *i* and *n* + 1 to *m* + *n* − *i* of *S* (that is removing *i* columns in each block and the *i* last rows of zeros). The *principal subresultant coefficient* *si* is the determinant of the *m* + *n* − 2*i* first rows of *Ti*.

Let *Vi* be the (*m* + *n* − 2*i*) × (*m* + *n* − *i*) matrix defined as follows. First we add (*i* + 1) columns of zeros to the right of the (*m* + *n* − 2*i* − 1) × (*m* + *n* − 2*i* − 1) identity matrix. Then we border the bottom of the resulting matrix by a row consisting in (*m* + *n* − *i* − 1) zeros followed by *Xi*, *X**i*−1, ..., *X*, 1: $V_{i}={\begin{pmatrix}1&0&\cdots &0&0&0&\cdots &0\\0&1&\cdots &0&0&0&\cdots &0\\\vdots &\vdots &\ddots &\vdots &\vdots &\ddots &\vdots &0\\0&0&\cdots &1&0&0&\cdots &0\\0&0&\cdots &0&X^{i}&X^{i-1}&\cdots &1\end{pmatrix}}.$

With this notation, the *i*-th *subresultant polynomial* is the determinant of the matrix product *ViTi*. Its coefficient of degree *j* is the determinant of the square submatrix of *Ti* consisting in its *m* + *n* − 2*i* − 1 first rows and the (*m* + *n* − *i* − *j*)-th row.

#### Sketch of the proof

It is not obvious that, as defined, the subresultants have the desired properties. Nevertheless, the proof is rather simple if the properties of linear algebra and those of polynomials are put together.

As defined, the columns of the matrix *Ti* are the vectors of the coefficients of some polynomials belonging to the image of $\varphi _{i}$ . The definition of the *i*-th subresultant polynomial *Si* shows that the vector of its coefficients is a linear combination of these column vectors, and thus that *Si* belongs to the image of $\varphi _{i}.$

If the degree of the GCD is greater than *i*, then Bézout's identity shows that every non zero polynomial in the image of $\varphi _{i}$ has a degree larger than *i*. This implies that *Si* = 0.

If, on the other hand, the degree of the GCD is *i*, then Bézout's identity again allows proving that the multiples of the GCD that have a degree lower than *m* + *n* − *i* are in the image of $\varphi _{i}$ . The vector space of these multiples has the dimension *m* + *n* − 2*i* and has a base of polynomials of pairwise different degrees, not smaller than *i*. This implies that the submatrix of the *m* + *n* − 2*i* first rows of the column echelon form of *Ti* is the identity matrix and thus that *si* is not 0. Thus *Si* is a polynomial in the image of $\varphi _{i}$ , which is a multiple of the GCD and has the same degree. It is thus a greatest common divisor.

### GCD and root finding

#### Square-free factorization

Most root-finding algorithms behave badly with polynomials that have multiple roots. It is therefore useful to detect and remove them before calling a root-finding algorithm. A GCD computation allows detection of the existence of multiple roots, since the multiple roots of a polynomial are the roots of the GCD of the polynomial and its derivative.

After computing the GCD of the polynomial and its derivative, further GCD computations provide the complete *square-free factorization* of the polynomial, which is a factorization $f=\prod _{i=1}^{\deg(f)}f_{i}^{i}$ where, for each *i*, the polynomial *f**i* either is 1 if *f* does not have any root of multiplicity *i* or is a square-free polynomial (that is a polynomial without multiple root) whose roots are exactly the roots of multiplicity *i* of *f* (see Yun's algorithm).

Thus the square-free factorization reduces root-finding of a polynomial with multiple roots to root-finding of several square-free polynomials of lower degree. The square-free factorization is also the first step in most polynomial factorization algorithms.

#### Sturm sequence

The *Sturm sequence* of a polynomial with real coefficients is the sequence of the remainders provided by a variant of Euclid's algorithm applied to the polynomial and its derivative. For getting the Sturm sequence, one simply replaces the instruction $r_{i+1}:=\operatorname {rem} (r_{i-1},r_{i})$ of Euclid's algorithm by $r_{i+1}:=-\operatorname {rem} (r_{i-1},r_{i}).$

Let *V*(*a*) be the number of changes of signs in the sequence, when evaluated at a point *a*. Sturm's theorem asserts that *V*(*a*) − *V*(*b*) is the number of real roots of the polynomial in the interval [*a*, *b*]. Thus the Sturm sequence allows computing the number of real roots in a given interval. By subdividing the interval until every subinterval contains at most one root, this provides an algorithm that locates the real roots in intervals of arbitrary small length.

## GCD over a ring and its field of fractions

In this section, we consider polynomials over a unique factorization domain *R*, typically the ring of the integers, and over its field of fractions *F*, typically the field of the rational numbers, and we denote *R*[*X*] and *F*[*X*] the rings of polynomials in a set of variables over these rings.

### Primitive part–content factorization

The *content* of a polynomial *p* ∈ *R*[*X*], denoted "cont(*p*)", is the GCD of its coefficients. A polynomial *q* ∈ *F*[*X*] may be written $q={\frac {p}{c}}$ where *p* ∈ *R*[*X*] and *c* ∈ *R*: it suffices to take for *c* a multiple of all denominators of the coefficients of *q* (for example their product) and *p* = *cq*. The *content* of *q* is defined as: $\operatorname {cont} (q)={\frac {\operatorname {cont} (p)}{c}}.$ In both cases, the content is defined up to the multiplication by a unit of *R*.

The *primitive part* of a polynomial in *R*[*X*] or *F*[*X*] is defined by $\operatorname {primpart} (p)={\frac {p}{\operatorname {cont} (p)}}.$

In both cases, it is a polynomial in *R*[*X*] that is *primitive*, which means that 1 is a GCD of its coefficients.

Thus every polynomial in *R*[*X*] or *F*[*X*] may be factorized as $p=\operatorname {cont} (p)\,\operatorname {primpart} (p),$ and this factorization is unique up to the multiplication of the content by a unit of *R* and of the primitive part by the inverse of this unit.

Gauss's lemma implies that the product of two primitive polynomials is primitive. It follows that $\operatorname {primpart} (pq)=\operatorname {primpart} (p)\operatorname {primpart} (q)$ and $\operatorname {cont} (pq)=\operatorname {cont} (p)\operatorname {cont} (q).$

### Relation between the GCD over *R* and over *F*

The relations of the preceding section imply a strong relation between the GCD's in *R*[*X*] and in *F*[*X*]. To avoid ambiguities, the notation "*gcd*" will be indexed, in the following, by the ring in which the GCD is computed.

If *q*1 and *q*2 belong to *F*[*X*], then $\operatorname {primpart} (\gcd _{F[X]}(q_{1},q_{2}))=\gcd _{R[X]}(\operatorname {primpart} (q_{1}),\operatorname {primpart} (q_{2})).$

If *p*1 and *p*2 belong to *R*[*X*], then $\gcd _{R[X]}(p_{1},p_{2})=\gcd _{R}(\operatorname {cont} (p_{1}),\operatorname {cont} (p_{2}))\gcd _{R[X]}(\operatorname {primpart} (p_{1}),\operatorname {primpart} (p_{2})),$ and $\gcd _{R[X]}(\operatorname {primpart} (p_{1}),\operatorname {primpart} (p_{2}))=\operatorname {primpart} (\gcd _{F[X]}(p_{1},p_{2})).$

Thus the computation of polynomial GCD's is essentially the same problem over *F*[*X*] and over *R*[*X*].

For univariate polynomials over the rational numbers, one may think that Euclid's algorithm is a convenient method for computing the GCD. However, it involves simplifying a large number of fractions of integers, and the resulting algorithm is not efficient. For this reason, methods have been designed to modify Euclid's algorithm for working only with polynomials over the integers. They consist of replacing the Euclidean division, which introduces fractions, by a so-called *pseudo-division*, and replacing the remainder sequence of the Euclid's algorithm by so-called *pseudo-remainder sequences* (see below).

### Proof that GCD exists for multivariate polynomials

In the previous section we have seen that the GCD of polynomials in *R*[*X*] may be deduced from GCDs in *R* and in *F*[*X*]. A closer look on the proof shows that this allows us to prove the existence of GCDs in *R*[*X*], if they exist in *R* and in *F*[*X*]. In particular, if GCDs exist in *R*, and if *X* is reduced to one variable, this proves that GCDs exist in *R*[*X*] (Euclid's algorithm proves the existence of GCDs in *F*[*X*]).

A polynomial in n variables may be considered as a univariate polynomial over the ring of polynomials in (*n* − 1) variables. Thus a recursion on the number of variables shows that if GCDs exist and may be computed in *R*, then they exist and may be computed in every multivariate polynomial ring over *R*. In particular, if *R* is either the ring of the integers or a field, then GCDs exist in *R*[*x*1, ..., *xn*], and what precedes provides an algorithm to compute them.

The proof that a polynomial ring over a unique factorization domain is also a unique factorization domain is similar, but it does not provide an algorithm, because there is no general algorithm to factor univariate polynomials over a field (there are examples of fields for which there does not exist any factorization algorithm for the univariate polynomials).

## Pseudo-remainder sequences

In this section, we consider an integral domain *Z* (typically the ring **Z** of the integers) and its field of fractions *Q* (typically the field **Q** of the rational numbers). Given two polynomials *A* and *B* in the univariate polynomial ring *Z*[*X*], the Euclidean division (over *Q*) of *A* by *B* provides a quotient and a remainder which may not belong to *Z*[*X*].

For, if one applies Euclid's algorithm to the following polynomials $X^{8}+X^{6}-3X^{4}-3X^{3}+8X^{2}+2X-5$ and $3X^{6}+5X^{4}-4X^{2}-9X+21,$ the successive remainders of Euclid's algorithm are ${\begin{aligned}&-{\tfrac {5}{9}}X^{4}+{\tfrac {1}{9}}X^{2}-{\tfrac {1}{3}},\\&-{\tfrac {117}{25}}X^{2}-9X+{\tfrac {441}{25}},\\&{\tfrac {233150}{19773}}X-{\tfrac {102500}{6591}},\\&-{\tfrac {1288744821}{543589225}}.\end{aligned}}$ One sees that, despite the small degree and the small size of the coefficients of the input polynomials, one has to manipulate and simplify integer fractions of rather large size.

The *pseudo-division* has been introduced to allow a variant of Euclid's algorithm for which all remainders belong to *Z*[*X*].

If $\deg(A)=a$ and $\deg(B)=b$ and *a* ≥ *b*, the **pseudo-remainder** of the pseudo-division of *A* by *B*, denoted by prem(*A*,*B*) is $\operatorname {prem} (A,B)=\operatorname {rem} (\operatorname {lc} (B)^{a-b+1}A,B),$ where lc(*B*) is the leading coefficient of *B* (the coefficient of *X**b*).

The pseudo-remainder of the pseudo-division of two polynomials in *Z*[*X*] belongs always to *Z*[*X*].

A **pseudo-remainder sequence** is the sequence of the (pseudo) remainders *r**i* obtained by replacing the instruction $r_{i+1}:=\operatorname {rem} (r_{i-1},r_{i})$ of Euclid's algorithm by $r_{i+1}:={\frac {\operatorname {prem} (r_{i-1},r_{i})}{\alpha }},$ where *α* is an element of *Z* that divides exactly every coefficient of the numerator. Different choices of *α* give different pseudo-remainder sequences, which are described in the next subsections.

As the common divisors of two polynomials are not changed if the polynomials are multiplied by invertible constants (in *Q*), the last nonzero term in a pseudo-remainder sequence is a GCD (in *Q*[*X*]) of the input polynomials. Therefore, pseudo-remainder sequences allows computing GCD's in *Q*[*X*] without introducing fractions in *Q*.

In some contexts, it is essential to control the sign of the leading coefficient of the pseudo-remainder. This is typically the case when computing resultants and subresultants, or for using Sturm's theorem. This control can be done either by replacing lc(*B*) by its absolute value in the definition of the pseudo-remainder, or by controlling the sign of α (if α divides all coefficients of a remainder, the same is true for −*α*).

### Trivial pseudo-remainder sequence

The simplest (to define) remainder sequence consists in taking always *α* = 1. In practice, it is not interesting, as the size of the coefficients grows exponentially with the degree of the input polynomials. This appears clearly on the example of the preceding section, for which the successive pseudo-remainders are $-15\,X^{4}+3\,X^{2}-9,$ $15795\,X^{2}+30375\,X-59535,$ $1254542875143750\,X-1654608338437500,$ $12593338795500743100931141992187500.$ The number of digits of the coefficients of the successive remainders is more than doubled at each iteration of the algorithm. This is typical behavior of the trivial pseudo-remainder sequences.

### Primitive pseudo-remainder sequence

The *primitive pseudo-remainder sequence* consists in taking for α the content of the numerator. Thus all the *r**i* are primitive polynomials.

The primitive pseudo-remainder sequence is the pseudo-remainder sequence, which generates the smallest coefficients. However it requires to compute a number of GCD's in *Z*, and therefore is not sufficiently efficient to be used in practice, especially when *Z* is itself a polynomial ring.

With the same input as in the preceding sections, the successive remainders, after division by their content are $-5\,X^{4}+X^{2}-3,$ $13\,X^{2}+25\,X-49,$ $4663\,X-6150,$ $1.$ The small size of the coefficients hides the fact that a number of integers GCD and divisions by the GCD have been computed.

### Subresultant pseudo-remainder sequence

A subresultant sequence can be also computed with pseudo-remainders. The process consists in choosing α in such a way that every *r**i* is a subresultant polynomial. Surprisingly, the computation of α is very easy (see below). On the other hand, the proof of correctness of the algorithm is difficult, because it should take into account all the possibilities for the difference of degrees of two consecutive remainders.

The coefficients in the subresultant sequence are rarely much larger than those of the primitive pseudo-remainder sequence. As GCD computations in *Z* are not needed, the subresultant sequence with pseudo-remainders gives the most efficient computation.

With the same input as in the preceding sections, the successive remainders are $15\,X^{4}-3\,X^{2}+9,$ $65\,X^{2}+125\,X-245,$ $9326\,X-12300,$ $260708.$ The coefficients have a reasonable size. They are obtained without any GCD computation, only exact divisions. This makes this algorithm more efficient than that of primitive pseudo-remainder sequences.

The algorithm computing the subresultant sequence with pseudo-remainders is given below. In this algorithm, the input (*a*, *b*) is a pair of polynomials in *Z*[*X*]. The *r**i* are the successive pseudo remainders in *Z*[*X*], the variables *i* and *d**i* are non negative integers, and the Greek letters denote elements in *Z*. The functions `deg()` and `rem()` denote the degree of a polynomial and the remainder of the Euclidean division. In the algorithm, this remainder is always in *Z*[*X*]. Finally the divisions denoted / are always exact and have their result either in *Z*[*X*] or in *Z*.

*r*0 := *a* *r*1 := *b* ***for*** (*i* := 1; *r**i* ≠ 0; *i* := *i*+1) ***do***

```
   di := deg(ri−1) − deg(ri)
   γi := lc(ri)
   if i = 1 then
       β1 := (−1)d1+1
       ψ1 := −1
   else
       ψi := (−γi−1)di−1 / ψi−1di−1−1
       βi := −γi−1ψidi
   end if
   ri+1 := rem(γidi+1 ri−1, ri) / βi
```

***end for***

Note: "lc" stands for the leading coefficient, the coefficient of the highest degree of the variable.

This algorithm computes not only the greatest common divisor (the last non zero *r**i*), but also all the subresultant polynomials: The remainder *r**i* is the (deg(*r**i*−1) − 1)-th subresultant polynomial. If deg(*r**i*) < deg(*r**i*−1) − 1, the deg(*r**i*)-th subresultant polynomial is lc(*r**i*)deg(*r**i*−1)−deg(*r**i*)−1*r**i*. All the other subresultant polynomials are zero.

### Sturm sequence with pseudo-remainders

One may use pseudo-remainders for constructing sequences having the same properties as Sturm sequences. This requires to control the signs of the successive pseudo-remainders, in order to have the same signs as in the Sturm sequence. This may be done by defining a modified pseudo-remainder as follows.

If $\deg(A)=a$ and $\deg(B)=b$ and *a* ≥ *b*, the modified pseudo-remainder prem2(*A*, *B*) of the pseudo-division of *A* by *B* is $\operatorname {prem2} (A,B)=-\operatorname {rem} (\left|\operatorname {lc} (B)\right|^{a-b+1}A,B),$ where |lc(*B*)| is the absolute value of the leading coefficient of *B* (the coefficient of *X**b*).

For input polynomials with integer coefficients, this allows retrieval of Sturm sequences consisting of polynomials with integer coefficients. The subresultant pseudo-remainder sequence may be modified similarly, in which case the signs of the remainders **coincide** with those computed over the rationals.

Note that the algorithm for computing the subresultant pseudo-remainder sequence given above will compute wrong subresultant polynomials if one uses $-\mathrm {prem2} (A,B)$ instead of $\operatorname {prem} (A,B)$ .

## Modular GCD algorithm

If *f* and *g* are polynomials in *F*[*x*] for some finitely generated field *F*, the Euclidean Algorithm is the most natural way to compute their GCD. However, modern computer algebra systems only use it if *F* is finite because of a phenomenon called intermediate expression swell. Although degrees keep decreasing during the Euclidean algorithm, if *F* is not finite then the bit size of the polynomials can increase (sometimes dramatically) during the computations because repeated arithmetic operations in *F* tends to lead to larger expressions. For example, the addition of two rational numbers whose denominators are bounded by *b* leads to a rational number whose denominator is bounded by *b*2, so in the worst case, the bit size could nearly double with just one operation.

To expedite the computation, take a ring *D* for which *f* and *g* are in *D*[*x*], and take an ideal *I* such that *D*/*I* is a finite ring. Then compute the GCD over this finite ring with the Euclidean Algorithm. Using reconstruction techniques (Chinese remainder theorem, rational reconstruction, etc.) one can recover the GCD of *f* and *g* from its image modulo a number of ideals *I*. One can prove that this works provided that one discards modular images with non-minimal degrees, and avoids ideals *I* modulo which a leading coefficient vanishes.

Suppose $F=\mathbb {Q} ({\sqrt {3}})$ , $D=\mathbb {Z} [{\sqrt {3}}]$ , $f={\sqrt {3}}x^{3}-5x^{2}+4x+9$ and $g=x^{4}+4x^{2}+3{\sqrt {3}}x-6$ . If we take $I=(2)$ then $D/I$ is a finite ring (not a field since I is not maximal in D ). The Euclidean algorithm applied to the images of $f,g$ in $(D/I)[x]$ succeeds and returns 1. This implies that the GCD of $f,g$ in $F[x]$ must be 1 as well. Note that this example could easily be handled by any method because the degrees were too small for expression swell to occur, but it illustrates that if two polynomials have GCD 1, then the modular algorithm is likely to terminate after a single ideal I .
