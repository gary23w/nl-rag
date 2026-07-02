---
title: "Durand–Kerner method"
source: https://en.wikipedia.org/wiki/Durand%E2%80%93Kerner_method
domain: root-finding-methods
license: CC-BY-SA-4.0
tags: root-finding algorithm, bisection method, secant method, brent's method
fetched: 2026-07-02
---

# Durand–Kerner method

In numerical analysis, the **Weierstrass method** or **Durand–Kerner method**, discovered by Karl Weierstrass in 1891 and rediscovered independently by Durand in 1960 and Kerner in 1966, is a root-finding algorithm for solving polynomial equations. In other words, the method can be used to solve numerically the equation *f*(*x*)=0, where *f* is a given polynomial, which can be taken to be scaled so that the leading coefficient is 1.

## Explanation

This explanation considers equations of degree four. It is easily generalized to other degrees.

Let the polynomial *f* be defined by

$f(x)=x^{4}+ax^{3}+bx^{2}+cx+d$

for all *x*. The known numbers *a*, *b*, *c*, *d* are the coefficients.

Let the (potentially complex) numbers *P*, *Q*, *R*, *S* be the roots of this polynomial *f*. Then

$f(x)=(x-P)(x-Q)(x-R)(x-S)$

for all *x*. One can isolate the value *P* from this equation:

$P=x-{\frac {f(x)}{(x-Q)(x-R)(x-S)}}.$

So if used as a fixed-point iteration

$x_{1}:=x_{0}-{\frac {f(x_{0})}{(x_{0}-Q)(x_{0}-R)(x_{0}-S)}},$

it is strongly stable in that every initial point *x*0 ≠ *Q*, *R*, *S* delivers after one iteration the root *P* = *x*1. Furthermore, if one replaces the zeros *Q*, *R* and *S* by approximations *q* ≈ *Q*, *r* ≈ *R*, *s* ≈ *S*, such that *q*, *r*, *s* are not equal to *P*, then *P* is still a fixed point of the perturbed fixed-point iteration

$x_{k+1}:=x_{k}-{\frac {f(x_{k})}{(x_{k}-q)(x_{k}-r)(x_{k}-s)}},$

since

$P-{\frac {f(P)}{(P-q)(P-r)(P-s)}}=P-0=P.$

Note that the denominator is still different from zero. This fixed-point iteration is a contraction mapping for *x* around *P*.

The clue to the method now is to combine the fixed-point iteration for *P* with similar iterations for *Q*, *R*, *S* into a simultaneous iteration for all roots.

Initialize *p*, *q*, *r*, *s*:

p

0

:= (0.4 + 0.9

i

)

0

,

q

0

:= (0.4 + 0.9

i

)

1

,

r

0

:= (0.4 + 0.9

i

)

2

,

s

0

:= (0.4 + 0.9

i

)

3

.

There is nothing special about choosing 0.4 + 0.9*i* except that it is neither a real number nor a root of unity.

Make the substitutions for *n* = 1, 2, 3, ...:

$p_{n}=p_{n-1}-{\frac {f(p_{n-1})}{(p_{n-1}-q_{n-1})(p_{n-1}-r_{n-1})(p_{n-1}-s_{n-1})}},$

$q_{n}=q_{n-1}-{\frac {f(q_{n-1})}{(q_{n-1}-p_{n})(q_{n-1}-r_{n-1})(q_{n-1}-s_{n-1})}},$

$r_{n}=r_{n-1}-{\frac {f(r_{n-1})}{(r_{n-1}-p_{n})(r_{n-1}-q_{n})(r_{n-1}-s_{n-1})}},$

$s_{n}=s_{n-1}-{\frac {f(s_{n-1})}{(s_{n-1}-p_{n})(s_{n-1}-q_{n})(s_{n-1}-r_{n})}}.$

Re-iterate until the numbers *p*, *q*, *r*, *s* essentially stop changing relative to the desired precision. They then have the values *P*, *Q*, *R*, *S* in some order and in the chosen precision. So the problem is solved.

Note that complex number arithmetic must be used, and that the roots are found simultaneously rather than one at a time.

## Variations

This iteration procedure, like the Gauss–Seidel method for linear equations, computes one number at a time based on the already computed numbers. A variant of this procedure, like the Jacobi method, computes a vector of root approximations at a time. Both variants are effective root-finding algorithms.

One could also choose the initial values for *p*, *q*, *r*, *s* by some other procedure, even randomly, but in a way that

- they are inside some not-too-large circle containing also the roots of *f*(*x*), e.g. the circle around the origin with radius $1+\max {\big (}|a|,|b|,|c|,|d|{\big )}$ , (where 1, *a*, *b*, *c*, *d* are the coefficients of *f*(*x*))

and that

- they are not too close to each other,

which may increasingly become a concern as the degree of the polynomial increases.

If the coefficients are real and the polynomial has odd degree, then it must have at least one real root. To find this, use a real value of *p*0 as the initial guess and make *q*0 and *r*0, etc., complex conjugate pairs. Then the iteration will preserve these properties; that is, *p**n* will always be real, and *q**n* and *r**n*, etc., will always be conjugate. In this way, the *p**n* will converge to a real root *P*. Alternatively, make all of the initial guesses real; they will remain so.

## Example

This example is from the reference Jacoby (1992). The equation solved is *x*3 − 3*x*2 + 3*x* − 5 = 0. The first 4 iterations move *p*, *q*, *r* seemingly chaotically, but then the roots are located to 1 decimal. After iteration number 5 we have 4 correct decimals, and the subsequent iteration number 6 confirms that the computed roots are fixed. This general behaviour is characteristic for the method. Also notice that, in this example, the roots are used as soon as they are computed in each iteration. In other words, the computation of each second column uses the value of the previous computed columns.

| it.-no. | p | q | r |
|---|---|---|---|
| 0 | +1.0000 + 0.0000i | +0.4000 + 0.9000i | −0.6500 + 0.7200i |
| 1 | +1.3608 + 2.0222i | −0.3658 + 2.4838i | −2.3858 − 0.0284i |
| 2 | +2.6597 + 2.7137i | +0.5977 + 0.8225i | −0.6320−1.6716i |
| 3 | +2.2704 + 0.3880i | +0.1312 + 1.3128i | +0.2821 − 1.5015i |
| 4 | +2.5428 − 0.0153i | +0.2044 + 1.3716i | +0.2056 − 1.3721i |
| 5 | +2.5874 + 0.0000i | +0.2063 + 1.3747i | +0.2063 − 1.3747i |
| 6 | +2.5874 + 0.0000i | +0.2063 + 1.3747i | +0.2063 − 1.3747i |

Note that the equation has one real root and one pair of complex conjugate roots, and that the sum of the roots is 3.

## Derivation of the method via Newton's method

For every *n*-tuple of complex numbers, there is exactly one monic polynomial of degree *n* that has them as its zeros (keeping multiplicities). This polynomial is given by multiplying all the corresponding linear factors, that is

$g_{\vec {z}}(X)=(X-z_{1})\cdots (X-z_{n}).$

This polynomial has coefficients that depend on the prescribed zeros,

$g_{\vec {z}}(X)=X^{n}+g_{n-1}({\vec {z}})X^{n-1}+\cdots +g_{0}({\vec {z}}).$

Those coefficients are, up to a sign, the elementary symmetric polynomials $\alpha _{1}({\vec {z}}),\dots ,\alpha _{n}({\vec {z}})$ of degrees *1,...,n*.

To find all the roots of a given polynomial $f(X)=X^{n}+c_{n-1}X^{n-1}+\cdots +c_{0}$ with coefficient vector $(c_{n-1},\dots ,c_{0})$ simultaneously is now the same as to find a solution vector to the Vieta's system

${\begin{matrix}c_{0}&=&g_{0}({\vec {z}})&=&(-1)^{n}\alpha _{n}({\vec {z}})&=&(-1)^{n}z_{1}\cdots z_{n}\\c_{1}&=&g_{1}({\vec {z}})&=&(-1)^{n-1}\alpha _{n-1}({\vec {z}})\\&\vdots &\\c_{n-1}&=&g_{n-1}({\vec {z}})&=&-\alpha _{1}({\vec {z}})&=&-(z_{1}+z_{2}+\cdots +z_{n}).\end{matrix}}$

The Durand–Kerner method is obtained as the multidimensional Newton's method applied to this system. It is algebraically more comfortable to treat those identities of coefficients as the identity of the corresponding polynomials, $g_{\vec {z}}(X)=f(X)$ . In the Newton's method one looks, given some initial vector ${\vec {z}}$ , for an increment vector ${\vec {w}}$ such that $g_{{\vec {z}}+{\vec {w}}}(X)=f(X)$ is satisfied up to second and higher order terms in the increment. For this one solves the identity

$f(X)-g_{\vec {z}}(X)=\sum _{k=1}^{n}{\frac {\partial g_{\vec {z}}(X)}{\partial z_{k}}}w_{k}=-\sum _{k=1}^{n}w_{k}\prod _{j\neq k}(X-z_{j}).$

If the numbers $z_{1},\dots ,z_{n}$ are pairwise different, then the polynomials in the terms of the right hand side form a basis of the *n*-dimensional space $\mathbb {C} [X]_{n-1}$ of polynomials with maximal degree *n* − 1. Thus a solution ${\vec {w}}$ to the increment equation exists in this case. The coordinates of the increment ${\vec {w}}$ are simply obtained by evaluating the increment equation

$-\sum _{k=1}^{n}w_{k}\prod _{j\neq k}(X-z_{j})=f(X)-\prod _{j=1}^{n}(X-z_{j})$

at the points $X=z_{k}$ , which results in

$-w_{k}\prod _{j\neq k}(z_{k}-z_{j})=-w_{k}g_{\vec {z}}'(z_{k})=f(z_{k})$

, that is

$w_{k}=-{\frac {f(z_{k})}{\prod _{j\neq k}(z_{k}-z_{j})}}.$

## Root inclusion via Gerschgorin's circles

In the quotient ring (algebra) of residue classes modulo ƒ(*X*), the multiplication by *X* defines an endomorphism that has the zeros of ƒ(*X*) as eigenvalues with the corresponding multiplicities. Choosing a basis, the multiplication operator is represented by its coefficient matrix *A*, the companion matrix of ƒ(*X*) for this basis.

Since every polynomial can be reduced modulo ƒ(*X*) to a polynomial of degree *n* − 1 or lower, the space of residue classes can be identified with the space of polynomials of degree bounded by *n* − 1. A problem-specific basis can be taken from Lagrange interpolation as the set of *n* polynomials

$b_{k}(X)=\prod _{1\leq j\leq n,\;j\neq k}(X-z_{j}),\quad k=1,\dots ,n,$

where $z_{1},\dots ,z_{n}\in \mathbb {C}$ are pairwise different complex numbers. Note that the kernel functions for the Lagrange interpolation are $L_{k}(X)={\frac {b_{k}(X)}{b_{k}(z_{k})}}$ .

For the multiplication operator applied to the basis polynomials one obtains from the Lagrange interpolation

| $X\cdot b_{k}(X)\mod f(X)=X\cdot b_{k}(X)-f(X)$ | $=\sum _{j=1}^{n}{\Big (}z_{j}\cdot b_{k}(z_{j})-f(z_{j}){\Big )}\cdot {\frac {b_{j}(X)}{b_{j}(z_{j})}}$ |
|---|---|
|   | $=z_{k}\cdot b_{k}(X)+\sum _{j=1}^{n}w_{j}\cdot b_{j}(X)$ , |

where $w_{j}=-{\frac {f(z_{j})}{b_{j}(z_{j})}}$ are again the Weierstrass updates.

The companion matrix of ƒ(*X*) is therefore

$A=\mathrm {diag} (z_{1},\dots ,z_{n})+{\begin{pmatrix}1\\\vdots \\1\end{pmatrix}}\cdot \left(w_{1},\dots ,w_{n}\right).$

From the transposed matrix case of the Gershgorin circle theorem it follows that all eigenvalues of *A*, that is, all roots of ƒ(*X*), are contained in the union of the disks $D(a_{k,k},r_{k})$ with a radius $r_{k}=\sum _{j\neq k}{\big |}a_{j,k}{\big |}$ .

Here one has $a_{k,k}=z_{k}+w_{k}$ , so the centers are the next iterates of the Weierstrass iteration, and radii $r_{k}=(n-1)\left|w_{k}\right|$ that are multiples of the Weierstrass updates. If the roots of ƒ(*X*) are all well isolated (relative to the computational precision) and the points $z_{1},\dots ,z_{n}\in \mathbb {C}$ are sufficiently close approximations to these roots, then all the disks will become disjoint, so each one contains exactly one zero. The midpoints of the circles will be better approximations of the zeros.

Every conjugate matrix $TAT^{-1}$ of *A* is as well a companion matrix of ƒ(*X*). Choosing *T* as diagonal matrix leaves the structure of *A* invariant. The root close to $z_{k}$ is contained in any isolated circle with center $z_{k}$ regardless of *T*. Choosing the optimal diagonal matrix *T* for every index results in better estimates (see ref. Petkovic et al. 1995).

## Convergence results

The connection between the Taylor series expansion and Newton's method suggests that the distance from $z_{k}+w_{k}$ to the corresponding root is of the order $O{\big (}|w_{k}|^{2}{\big )}$ , if the root is well isolated from nearby roots and the approximation is sufficiently close to the root. So after the approximation is close, Newton's method converges *quadratically*; that is, the error is squared with every step (which will greatly reduce the error once it is less than 1). In the case of the Durand–Kerner method, convergence is quadratic if the vector ${\vec {z}}=(z_{1},\dots ,z_{n})$ is close to some permutation of the vector of the roots of *f*.

For the conclusion of linear convergence there is a more specific result (see ref. Petkovic et al. 1995). If the initial vector ${\vec {z}}$ and its vector of Weierstrass updates ${\vec {w}}=(w_{1},\dots ,w_{n})$ satisfies the inequality

$\max _{1\leq k\leq n}|w_{k}|\leq {\frac {1}{5n}}\min _{1\leq j<k\leq n}|z_{k}-z_{j}|,$

then this inequality also holds for all iterates, all inclusion disks $D{\big (}z_{k}+w_{k},(n-1)|w_{k}|{\big )}$ are disjoint, and linear convergence with a contraction factor of 1/2 holds. Further, the inclusion disks can in this case be chosen as

$D\left(z_{k}+w_{k},{\tfrac {1}{4}}|w_{k}|\right),\quad k=1,\dots ,n,$

each containing exactly one zero of *f*.

## Failing general convergence

The Weierstrass / Durand-Kerner method is not generally convergent: in other words, it is not true that for every polynomial, the set of initial vectors that eventually converges to roots is open and dense. In fact, there are open sets of polynomials that have open sets of initial vectors that converge to periodic cycles other than roots (see Reinke et al.)
