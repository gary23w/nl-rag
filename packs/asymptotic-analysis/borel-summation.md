---
title: "Borel summation"
source: https://en.wikipedia.org/wiki/Borel_summation
domain: asymptotic-analysis
license: CC-BY-SA-4.0
tags: asymptotic analysis, asymptotic expansion, steepest descent, borel summation
fetched: 2026-07-02
---

# Borel summation

> Borel, then an unknown young man, discovered that his summation method gave the 'right' answer for many classical divergent series. He decided to make a pilgrimage to Stockholm to see Mittag-Leffler, who was the recognized lord of complex analysis. Mittag-Leffler listened politely to what Borel had to say and then, placing his hand upon the complete works by Weierstrass, his teacher, he said in Latin, 'The Master forbids it'.

—

Mark Kac

, quoted by

Reed

&

Simon (1978

, p.

38)

In mathematics, **Borel summation** is a summation method for divergent series, introduced by Émile Borel (1899). It is particularly useful for summing divergent asymptotic series, and in some sense gives the best possible sum for such series. There are several variations of this method that are also called Borel summation, and a generalization of it called Mittag-Leffler summation.

## Definition

There are (at least) three slightly different methods called Borel summation. They differ in which series they can sum, but are consistent, meaning that if two of the methods sum the same series they give the same answer.

Throughout let *A*(*z*) denote a formal power series

$A(z)=\sum _{k=0}^{\infty }a_{k}z^{k},$

and define the **Borel transform** of *A* to be its corresponding exponential series

${\mathcal {B}}A(t)\equiv \sum _{k=0}^{\infty }{\frac {a_{k}}{k!}}t^{k}.$

### Borel's exponential summation method

Let *A**n*(*z*) denote the partial sum

$A_{n}(z)=\sum _{k=0}^{n}a_{k}z^{k}.$

A weak form of Borel's summation method defines the Borel sum of *A* to be

$\lim _{t\rightarrow \infty }e^{-t}\sum _{n=0}^{\infty }{\frac {t^{n}}{n!}}A_{n}(z).$

If this converges at *z* ∈ **C** to some function *a*(*z*), we say that the weak Borel sum of *A* converges at *z*, and write ${\textstyle \sum }a_{k}z^{k}=a(z)\,({\boldsymbol {wB}})$ .

### Borel's integral summation method

Suppose that the Borel transform converges for all positive real numbers to a function growing sufficiently slowly that the following integral is well defined (as an improper integral), the **Borel sum** of *A* is given by

$\int _{0}^{\infty }e^{-t}{\mathcal {B}}A(tz)\,dt,$

representing Laplace transform of ${\mathcal {B}}A(z)$ .

If the integral converges at *z* ∈ **C** to some *a*(*z*), we say that the Borel sum of *A* converges at *z*, and write ${\textstyle \sum }a_{k}z^{k}=a(z)\,({\boldsymbol {B}})$ .

### Borel's integral summation method with analytic continuation

This is similar to Borel's integral summation method, except that the Borel transform need not converge for all *t*, but converges to an analytic function of *t* near 0 that can be analytically continued along the positive real axis.

## Basic properties

### Regularity

The methods (**B**) and (**wB**) are both regular summation methods, meaning that whenever *A*(*z*) converges (in the standard sense), then the Borel sum and weak Borel sum also converge, and do so to the same value. i.e.

$\sum _{k=0}^{\infty }a_{k}z^{k}=A(z)<\infty \quad \Rightarrow \quad {\textstyle \sum }a_{k}z^{k}=A(z)\,\,({\boldsymbol {B}},\,{\boldsymbol {wB}}).$

Regularity of (**B**) is easily seen by a change in order of integration, which is valid due to absolute convergence: if *A*(*z*) is convergent at *z*, then

$A(z)=\sum _{k=0}^{\infty }a_{k}z^{k}=\sum _{k=0}^{\infty }a_{k}\left(\int _{0}^{\infty }e^{-t}t^{k}dt\right){\frac {z^{k}}{k!}}=\int _{0}^{\infty }e^{-t}\sum _{k=0}^{\infty }a_{k}{\frac {(tz)^{k}}{k!}}dt,$

where the rightmost expression is exactly the Borel sum at *z*.

Regularity of (**B**) and (**wB**) imply that these methods provide analytic extensions to *A*(*z*).

### Nonequivalence of Borel and weak Borel summation

Any series *A*(*z*) that is weak Borel summable at *z* ∈ *C* is also Borel summable at *z*. However, one can construct examples of series which are divergent under weak Borel summation, but which are Borel summable. The following theorem characterises the equivalence of the two methods.

Theorem

(

(

Hardy 1992

, 8.5)

).

Let

A

(

z

)

be a formal power series, and fix

z

∈

C

, then:

1. If ${\textstyle \sum }a_{k}z^{k}=a(z)\,({\boldsymbol {wB}})$ , then ${\textstyle \sum }a_{k}z^{k}=a(z)\,({\boldsymbol {B}})$ .
2. If ${\textstyle \sum }a_{k}z^{k}=a(z)\,({\boldsymbol {B}})$ , and $\lim _{t\rightarrow \infty }e^{-t}{\mathcal {B}}A(zt)=0,$ then ${\textstyle \sum }a_{k}z^{k}=a(z)\,({\boldsymbol {wB}})$ .

### Relationship to other summation methods

- (**B**) is the special case of Mittag-Leffler summation with α = 1.
- (**wB**) can be seen as the limiting case of generalized Euler summation method (**E**,*q*) in the sense that as *q* → ∞ the domain of convergence of the (**E**,*q*) method converges up to the domain of convergence for (**B**).

## Uniqueness theorems

There are always many different functions with any given asymptotic expansion. However, there is sometimes a best possible function, in the sense that the errors in the finite-dimensional approximations are as small as possible in some region. Watson's theorem and Carleman's theorem show that Borel summation produces such a best possible sum of the series.

### Watson's theorem

Watson's theorem gives conditions for a function to be the Borel sum of its asymptotic series. Suppose that *f* is a function satisfying the following conditions:

- *f* is holomorphic in some region |*z*| < *R*, |arg(*z*)| < π/2 + *ε* for some positive *R* and *ε*.
- In this region *f* has an asymptotic series *a*0 + *a*1*z* + ... with the property that the error

$|f(z)-a_{0}-a_{1}z-\cdots -a_{n-1}z^{n-1}|$

is bounded by

$C^{n+1}n!|z|^{n}$

for all *z* in the region (for some positive constant *C*).

Then Watson's theorem says that in this region *f* is given by the Borel sum of its asymptotic series. More precisely, the series for the Borel transform converges in a neighborhood of the origin, and can be analytically continued to the positive real axis, and the integral defining the Borel sum converges to *f*(*z*) for *z* in the region above.

### Carleman's theorem

Carleman's theorem shows that a function is uniquely determined by an asymptotic series in a sector provided the errors in the finite order approximations do not grow too fast. More precisely it states that if *f* is analytic in the interior of the sector |*z*| < *C*, Re(*z*) > 0 and |*f*(*z*)| < |*b**n**z*|*n* in this region for all *n*, then *f* is zero provided that the series 1/*b*0 + 1/*b*1 + ... diverges.

Carleman's theorem gives a summation method for any asymptotic series whose terms do not grow too fast, as the sum can be defined to be the unique function with this asymptotic series in a suitable sector if it exists. Borel summation is slightly weaker than special case of this when *b**n* =*cn* for some constant *c*. More generally one can define summation methods slightly stronger than Borel's by taking the numbers *b**n* to be slightly larger, for example *b**n* = *cn*log *n* or *b**n* =*cn*log *n* log log *n*. In practice this generalization is of little use, as there are almost no natural examples of series summable by this method that cannot also be summed by Borel's method.

### Example

The function *f*(*z*) = exp(–1/*z*) has the asymptotic series 0 + 0*z* + ... with an error bound of the form above in the region |arg(*z*)| < *θ* for any *θ* < π/2, but is not given by the Borel sum of its asymptotic series. This shows that the number π/2 in Watson's theorem cannot be replaced by any smaller number (unless the bound on the error is made smaller).

## Examples

### The geometric series

Consider the geometric series

$A(z)=\sum _{k=0}^{\infty }z^{k},$

which converges (in the standard sense) to 1/(1 − *z*) for |*z*| < 1. The Borel transform is

${\mathcal {B}}A(tz)\equiv \sum _{k=0}^{\infty }{\frac {z^{k}}{k!}}t^{k}=e^{zt},$

from which we obtain the Borel sum

$\int _{0}^{\infty }e^{-t}{\mathcal {B}}A(tz)\,dt=\int _{0}^{\infty }e^{-t}e^{tz}\,dt={\frac {1}{1-z}}$

which converges in the larger region Re(*z*) < 1, giving an analytic continuation of the original series.

Considering instead the weak Borel transform, the partial sums are given by *A**N*(*z*) = (1 − z*N*+1)/(1 − *z*), and so the weak Borel sum is

$\lim _{t\rightarrow \infty }e^{-t}\sum _{n=0}^{\infty }{\frac {1-z^{n+1}}{1-z}}{\frac {t^{n}}{n!}}=\lim _{t\rightarrow \infty }{\frac {e^{-t}}{1-z}}{\big (}e^{t}-ze^{tz}{\big )}={\frac {1}{1-z}},$

where, again, convergence is on Re(*z*) < 1. Alternatively this can be seen by appealing to part 2 of the equivalence theorem, since for Re(*z*) < 1,

$\lim _{t\rightarrow \infty }e^{-t}({\mathcal {B}}A)(zt)=e^{t(z-1)}=0.$

### An alternating factorial series

Consider the series

$A(z)=\sum _{k=0}^{\infty }k!(-1)^{k}\cdot z^{k},$

then *A*(*z*) does not converge for any nonzero *z* ∈ **C**. The Borel transform is

${\mathcal {B}}A(t)\equiv \sum _{k=0}^{\infty }\left(-t\right)^{k}={\frac {1}{1+t}}$

for |*t*| < 1, which can be analytically continued to all *t* ≥ 0. So the Borel sum is

$\int _{0}^{\infty }e^{-t}{\mathcal {B}}A(tz)\,dt=\int _{0}^{\infty }{\frac {e^{-t}}{1+tz}}\,dt={\frac {1}{z}}\cdot e^{1/z}\cdot \Gamma \left(0,{\frac {1}{z}}\right)$

(where Γ is the incomplete gamma function).

This integral converges for all *z* ≥ 0, so the original divergent series is Borel summable for all such *z*. This function has an asymptotic expansion as *z* tends to 0 that is given by the original divergent series. This is a typical example of the fact that Borel summation will sometimes "correctly" sum divergent asymptotic expansions.

Again, since

$\lim _{t\rightarrow \infty }e^{-t}({\mathcal {B}}A)(zt)=\lim _{t\rightarrow \infty }{\frac {e^{-t}}{1+zt}}=0,$

for all *z*, the equivalence theorem ensures that weak Borel summation has the same domain of convergence, *z* ≥ 0.

### An example in which equivalence fails

The following example extends on that given in (Hardy 1992, 8.5). Consider

$A(z)=\sum _{k=0}^{\infty }\left(\sum _{\ell =0}^{\infty }{\frac {(-1)^{\ell }(2\ell +2)^{k}}{(2\ell +1)!}}\right)z^{k}.$

After changing the order of summation, the Borel transform is given by

${\begin{aligned}{\mathcal {B}}A(t)&=\sum _{\ell =0}^{\infty }\left(\sum _{k=0}^{\infty }{\frac {{\big (}(2\ell +2)t{\big )}^{k}}{k!}}\right){\frac {(-1)^{\ell }}{(2\ell +1)!}}\\&=\sum _{\ell =0}^{\infty }e^{(2\ell +2)t}{\frac {(-1)^{\ell }}{(2\ell +1)!}}\\&=e^{t}\sum _{\ell =0}^{\infty }{\big (}e^{t}{\big )}^{2\ell +1}{\frac {(-1)^{\ell }}{(2\ell +1)!}}\\&=e^{t}\sin(e^{t}).\end{aligned}}$

At *z* = 2 the Borel sum is given by

$\int _{0}^{\infty }e^{t}\sin(e^{2t})\,dt=\int _{1}^{\infty }\sin(u^{2})\,du={\sqrt {\frac {\pi }{8}}}-S(1)<\infty ,$

where *S*(*x*) is the Fresnel integral. Via the convergence theorem along chords, the Borel integral converges for all *z* ≤ 2 (the integral diverges for *z* > 2).

For the weak Borel sum we note that

$\lim _{t\rightarrow \infty }e^{(z-1)t}\sin(e^{zt})=0$

holds only for *z* < 1, and so the weak Borel sum converges on this smaller domain.

## Existence results and the domain of convergence

### Summability on chords

If a formal series *A*(*z*) is Borel summable at *z*0 ∈ **C**, then it is also Borel summable at all points on the chord O*z*0 connecting *z*0 to the origin. Moreover, there exists a function *a*(*z*) analytic throughout the disk with radius O*z*0 such that

${\textstyle \sum }a_{k}z^{k}=a(z)\,({\boldsymbol {B}}),$

for all *z* = θ*z*0, θ ∈ [0,1].

An immediate consequence is that the domain of convergence of the Borel sum is a star domain in **C**. More can be said about the domain of convergence of the Borel sum, than that it is a star domain, which is referred to as the Borel polygon, and is determined by the singularities of the series *A*(*z*).

### The Borel polygon

Suppose that *A*(*z*) has strictly positive radius of convergence, so that it is analytic in a non-trivial region containing the origin, and let *S**A* denote the set of singularities of *A*. This means that *P* ∈ *S**A* if and only if *A* can be continued analytically along the open chord from 0 to *P*, but not to *P* itself. For *P* ∈ *SA*, let *LP* denote the line passing through *P* which is perpendicular to the chord *OP*. Define the sets

$\Pi _{P}=\{z\in \mathbb {C} \,\colon \,/[Oz/]\cap L_{P}=\varnothing \},$

the set of points which lie on the same side of *LP* as the origin. The Borel polygon of *A* is the set

$\Pi _{A}=\operatorname {cl} \left(\bigcap _{P\in S_{A}}\Pi _{P}\right).$

An alternative definition was used by Borel and Phragmén (Sansone & Gerretsen 1960, 8.3). Let $S\subset \mathbb {C}$ denote the largest star domain on which there is an analytic extension of *A*, then $\Pi _{A}$ is the largest subset of S such that for all $P\in \Pi _{A}$ the interior of the circle with radius *OP* is contained in S . Referring to the set $\Pi _{A}$ as a polygon is something of a misnomer, since the set need not be polygonal at all; if, however, *A*(*z*) has only finitely many singularities then $\Pi _{A}$ will in fact be a polygon.

The following theorem, due to Borel and Phragmén provides convergence criteria for Borel summation.

Theorem

(

Hardy 1992

, 8.8)

.

The series

A

(

z

)

is

(

B

)

summable at all

$z\in \operatorname {int} (\Pi _{A})$

, and is

(

B

)

divergent at all

$z\in \mathbb {C} \setminus \Pi _{A}$

.

Note that (**B**) summability for $z\in \partial \Pi _{A}$ depends on the nature of the point.

#### Example 1

Let ωi ∈ **C** denote the *m*-th roots of unity, *i* = 1, ..., *m*, and consider

${\begin{aligned}A(z)&=\sum _{k=0}^{\infty }(\omega _{1}^{k}+\cdots +\omega _{m}^{k})z^{k}\\&=\sum _{i=1}^{m}{\frac {1}{1-\omega _{i}z}},\end{aligned}}$

which converges on *B*(0,1) ⊂ **C**. Seen as a function on **C**, *A*(*z*) has singularities at *SA* = {*ω**i* : *i* = 1, ..., *m*}, and consequently the Borel polygon $\Pi _{A}$ is given by the regular *m*-gon centred at the origin, and such that 1 ∈ **C** is a midpoint of an edge.

#### Example 2

The formal series

$A(z)=\sum _{k=0}^{\infty }z^{2^{k}},$

converges for all $|z|<1$ (for instance, by the comparison test with the geometric series). It can however be shown that *A* does not converge for any point *z* ∈ **C** such that *z*2*n* = 1 for some *n*. Since the set of such *z* is dense in the unit circle, there can be no analytic extension of *A* outside of *B*(0,1). Subsequently, the largest star domain to which *A* can be analytically extended is *S* = *B*(0,1) from which (via the second definition) one obtains $\Pi _{A}=B(0,1)$ . In particular one sees that the Borel polygon is not polygonal.

### A Tauberian theorem

A Tauberian theorem provides conditions under which convergence of one summation method implies convergence under another method. The principal Tauberian theorem for Borel summation provides conditions under which the weak Borel method implies convergence of the series.

Theorem

(

Hardy 1992

, 9.13)

. If

A

is

(

wB

)

summable at

z

0

∈

C

,

${\textstyle \sum }a_{k}z_{0}^{k}=a(z_{0})\,({\boldsymbol {wB}})$

, and

$a_{k}z_{0}^{k}=O(k^{-1/2}),\qquad \forall k\geq 0,$

then

$\sum _{k=0}^{\infty }a_{k}z_{0}^{k}=a(z_{0})$

, and the series converges for all

|

z

|

<

|

z

0

|

.

## Applications

Borel summation finds application in perturbation expansions in quantum field theory. In particular in 2-dimensional Euclidean field theory the Schwinger functions can often be recovered from their perturbation series using Borel summation (Glimm & Jaffe 1987, p. 461). Some of the singularities of the Borel transform are related to instantons and renormalons in quantum field theory (Weinberg 2005, 20.7).

## Generalizations

Borel summation requires that the coefficients do not grow too fast: more precisely, *a**n* has to be bounded by *n*!*C**n*+1 for some *C*. There is a variation of Borel summation that replaces factorials *n*! with (*kn*)! for some positive integer *k*, which allows the summation of some series with *a**n* bounded by (*kn*)!*C**n*+1 for some *C*. This generalization is given by Mittag-Leffler summation.

In the most general case, Borel summation is generalized by Nachbin resummation, which can be used when the bounding function is of some general type (psi-type), instead of being exponential type.
