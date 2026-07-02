---
title: "Bézout's identity"
source: https://en.wikipedia.org/wiki/Bézout's_identity
domain: extended-euclidean
license: CC-BY-SA-4.0
tags: extended euclidean algorithm, bezout identity, modular multiplicative inverse, chinese remainder theorem
fetched: 2026-07-02
---

# Bézout's identity

In mathematics, **Bézout's identity** (also called **Bézout's lemma**), named after Étienne Bézout who proved it for polynomials, is a theorem which relates two arbitrary integers with their greatest common divisor. The theorem's statement is as follows:

**Bézout's identity**—Let *a* and *b* be integers with greatest common divisor *d*. Then there exist integers *x* and *y* such that *ax* + *by* = *d*. Moreover, the integers of the form *az* + *bt* are exactly the multiples of *d*.

(The greatest common divisor of 0 and 0 is taken to be 0.) The integers *x* and *y* are called **Bézout coefficients** for (*a*, *b*); they are not unique. The extended Euclidean algorithm can be used to compute a minimal pair of Bézout coefficients, meaning they satisfy $|x|\leq |b/d|$ and $|y|<|a/d|$ ; equality occurs only if one of *a* and *b* is a multiple of the other, and otherwise there exist exactly two minimal pairs.

As an example, the greatest common divisor of $a=15$ and $b=69$ is $d=3$ , which can be written as the linear combination $ax+by=15(-9)+69(2)=3$ with Bézout coefficients $(x,y)=(-9,2)$ , which are minimal since $9<69/3=23$ and $2<15/3=5$ . The other minimal Bézout coefficients are $(x,y)=(-9+23,2-5)=(14,-3)$ .

Many other theorems in elementary number theory, such as Euclid's lemma or the Chinese remainder theorem, can be formally deduced from Bézout's identity.

A Bézout domain is an integral domain in which Bézout's identity holds. In particular, Bézout's identity holds in principal ideal domains. Every theorem that results from Bézout's identity is thus true in all principal ideal domains.

## Structure of solutions

If *a* and *b* are not both zero and one pair of Bézout coefficients (*x*, *y*) has been computed (for example, using the extended Euclidean algorithm), all pairs can be represented in the form $\left(x-k{\frac {b}{d}},\ y+k{\frac {a}{d}}\right),$ where *k* is an arbitrary integer, *d* is the greatest common divisor of *a* and *b*, and the fractions simplify to integers.

If a and b are both nonzero and none of them divides the other, then exactly two of the pairs of Bézout coefficients satisfy $|x|<\left|{\frac {b}{d}}\right|\quad {\text{and}}\quad |y|<\left|{\frac {a}{d}}\right|.$ If a and b are both positive, one has $x>0$ and $y<0$ for one of these pairs, and $x<0$ and $y>0$ for the other. If *a* > 0 is a divisor of b (including the case $b=0$ ), then one pair of Bézout coefficients is (1, 0).

This relies on a property of Euclidean division: given two non-zero integers *c* and *d*, if d does not divide c, there is exactly one pair (*q*, *r*) such that *c* = *dq* + *r* and 0 < *r* < |*d*|, and another one such that *c* = *dq* + *r* and −|*d*| < *r* < 0.

The two pairs of minimal Bézout coefficients are obtained from the given one (*x*, *y*) by choosing for k in the above formula either of the two integers nearest to ⁠*x*/*b*/*d*⁠.

The extended Euclidean algorithm always produces one of these two minimal pairs.

### Example

Let *a* = 12 and *b* = 42, then gcd (12, 42) = 6. Then the following Bézout's identities are [had] held, with the Bézout coefficients written in red for the minimal pairs and in blue for the other ones.

${\begin{aligned}\vdots \\12&\times ({\color {blue}{-10}})&+\;\;42&\times \color {blue}{3}&=6\\12&\times ({\color {red}{-3}})&+\;\;42&\times \color {red}{1}&=6\\12&\times \color {red}{4}&+\;\;42&\times ({\color {red}{-1}})&=6\\12&\times \color {blue}{11}&+\;\;42&\times ({\color {blue}{-3}})&=6\\12&\times \color {blue}{18}&+\;\;42&\times ({\color {blue}{-5}})&=6\\\vdots \end{aligned}}$

If (*x*, *y*) = (18, −5) is the original pair of Bézout coefficients, then ⁠18/42/6⁠ ∈ [2, 3] yields the minimal pairs via *k* = 2, respectively *k* = 3; that is, (18 − 2 ⋅ 7, −5 + 2 ⋅ 2) = (4, −1), and (18 − 3 ⋅ 7, −5 + 3 ⋅ 2) = (−3, 1).

## Existence proof

Given any nonzero integers a and b, let *S* = {*ax* + *by* | *x*, *y* ∈ **Z** and *ax* + *by* > 0}. The set S is nonempty since it contains either a or –*a* (with *x* = ±1 and *y* = 0). Since S is a nonempty set of positive integers, it has a minimum element *d* = *as* + *bt*, by the well-ordering principle. To prove that d is the greatest common divisor of a and b, it must be proven that d is a common divisor of a and b, and that for any other common divisor c, one has *c* ≤ *d*.

The Euclidean division of a by d may be written as $a=dq+r\quad {\text{with}}\quad 0\leq r<d.$ The remainder r is in *S* ∪ {0}, because ${\begin{aligned}r&=a-qd\\&=a-q(as+bt)\\&=a(1-qs)-bqt.\end{aligned}}$ Thus r is of the form *ax* + *by*, and hence *r* ∈ *S* ∪ {0}. However, 0 ≤ *r* < *d*, and d is the smallest positive integer in S: the remainder r can therefore not be in S, making r necessarily 0. This implies that d is a divisor of a. Similarly d is also a divisor of b, and therefore d is a common divisor of a and b.

Now, let c be any common divisor of a and b; that is, there exist u and v such that *a* = *cu* and *b* = *cv*. One has thus ${\begin{aligned}d&=as+bt\\&=cus+cvt\\&=c(us+vt).\end{aligned}}$ That is, c is a divisor of d. Since *d* > 0, this implies *c* ≤ *d*.

## Corollaries

### Writing any integer as a linear combination

An immediate corollary of Bézout's identity is that *any* integer n can be written as a linear combination of *any* two coprime integers. Indeed, if a and b are coprime, then Bézout's identity guarantees the existence of integers x and y such that *ax* + *by* = 1. Multiplying both sides by n gives $a(xn)+b(yn)=n$ .

## Generalizations

### For three or more integers

Bézout's identity can be extended to more than two integers: if $\gcd(a_{1},a_{2},\ldots ,a_{n})=d$ then there are integers $x_{1},x_{2},\ldots ,x_{n}$ such that $d=a_{1}x_{1}+a_{2}x_{2}+\cdots +a_{n}x_{n}$ has the following properties:

- *d* is the smallest positive integer of this form
- every number of this form is a multiple of *d*

### For polynomials

Bézout's identity does not always hold for polynomials with coefficients in a ring. For example, when working in the polynomial ring with integer coefficients: the greatest common divisor of 2*x* and *x*2 is *x*, but there are no integer-coefficient polynomials $p(x)$ and $q(x)$ satisfying $2xp(x)+x^{2}q(x)=x$ .

However, Bézout's identity works for univariate polynomials with coefficients in a field, exactly as for the original case of integers. In particular the Bézout's coefficients and the greatest common divisor may be computed with the extended Euclidean algorithm.

As the common roots of two polynomials are the roots of their greatest common divisor, Bézout's identity and the fundamental theorem of algebra imply the following result:

For univariate polynomials

$a(x)$

and

$b(x)$

with coefficients in a field, there exist polynomials

$p(x)$

and

$q(x)$

such that

$a(x)p(x)+b(x)q(x)=1$

if and only if

$a(x)$

and

$b(x)$

have no common root in any

algebraically closed field

(commonly the field of

complex numbers

).

The generalization of this result to any number of polynomials and indeterminates is Hilbert's Nullstellensatz.

### For principal ideal domains

As noted in the introduction, Bézout's identity works not only in the ring of integers, but also in any other principal ideal domain (PID). That is, if *R* is a PID, and a and b are elements of *R*, and d is a greatest common divisor of a and b, then there are elements *x* and *y* in *R* such that *ax* + *by* = *d*. The reason is that the ideal *Ra* + *Rb* is principal and equal to *Rd*.

An integral domain in which Bézout's identity holds is called a Bézout domain.

## History and attribution

The French mathematician Étienne Bézout (1730–1783) proved this identity for polynomials. The statement for integers can be found already in the work of an earlier French mathematician, Claude Gaspard Bachet de Méziriac (1581–1638). Andrew Granville traced the association of Bézout's name with the identity to Bourbaki, arguing that it is a misattribution since the identity is implicit in Euclid's *Elements*.
