---
title: "Meijer G-function"
source: https://en.wikipedia.org/wiki/Meijer_G-function
domain: hypergeometric-functions
license: CC-BY-SA-4.0
tags: hypergeometric function, confluent hypergeometric function, pochhammer symbol, hypergeometric series
fetched: 2026-07-02
---

# Meijer G-function

In mathematics, the **G-function** was introduced by Cornelis Simon Meijer (1936) as a very general function intended to include most of the known special functions as particular cases. This was not the only attempt of its kind: the generalized hypergeometric function and the MacRobert E-function had the same aim, but Meijer's G-function was able to include those as particular cases as well. The first definition was made by Meijer using a series; nowadays the accepted and more general definition is via a line integral in the complex plane, introduced in its full generality by Arthur Erdélyi in 1953.

With the modern definition, the majority of the established special functions can be represented in terms of the Meijer G-function. A notable property is the closure of the set of all G-functions not only under differentiation but also under indefinite integration. In combination with a functional equation that allows to liberate from a G-function *G*(*z*) any factor *z**ρ* that is a constant power of its argument *z*, the closure implies that whenever a function is expressible as a G-function of a constant multiple of some constant power of the function argument, *f*(*x*) = *G*(*cx**γ*), the derivative and the antiderivative of this function are expressible so too.

The wide coverage of special functions also lends power to uses of Meijer's G-function other than the representation and manipulation of derivatives and antiderivatives. For example, the definite integral over the positive real axis of any function *g*(*x*) that can be written as a product *G*1(*cx**γ*)·*G*2(*dx**δ*) of two G-functions with rational *γ*/*δ* equals just another G-function, and generalizations of integral transforms like the Hankel transform and the Laplace transform and their inverses result when suitable G-function pairs are employed as transform kernels.

A still more general function, which introduces additional parameters into Meijer's G-function, is Fox's H-function.

One application of the Meijer G-function has been the particle spectrum of radiation from an inertial horizon in the moving mirror model of the dynamical Casimir effect (Good 2020).

## Definition of the Meijer G-function

A general definition of the Meijer G-function is given by the following line integral in the complex plane (Bateman & Erdélyi 1953, § 5.3-1):

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p}\\b_{1},\dots ,b_{q}\end{matrix}}\;\right|\,z\right)={\frac {1}{2\pi i}}\int _{L}{\frac {\prod _{j=1}^{m}\Gamma (b_{j}-s)\prod _{j=1}^{n}\Gamma (1-a_{j}+s)}{\prod _{j=m+1}^{q}\Gamma (1-b_{j}+s)\prod _{j=n+1}^{p}\Gamma (a_{j}-s)}}\,z^{s}\,ds,$

where Γ denotes the gamma function. This integral is of the so-called Mellin–Barnes type, and may be viewed as an inverse Mellin transform. The definition holds under the following assumptions:

- 0 ≤ *m* ≤ *q* and 0 ≤ *n* ≤ *p*, where *m*, *n*, *p* and *q* are integer numbers
- *a**k* − *b**j* ≠ 1, 2, 3, ... for any combination of {k, j} for which *k* = 1, 2, ..., *n*, and *j* = 1, 2, ..., *m*, which implies that no pole of any Γ(*b**j* − *s*), *j* = 1, 2, ..., *m*, coincides with any pole of any Γ(1 − *a**k* + *s*), *k* = 1, 2, ..., *n*
- *z* ≠ 0

Note that for historical reasons the *first* lower and *second* upper index refer to the *top* parameter row, while the *second* lower and *first* upper index refer to the *bottom* parameter row. One often encounters the following more synthetic notation using vectors:

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p}\\b_{1},\dots ,b_{q}\end{matrix}}\;\right|\,z\right)=G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right).$

Implementations of the G-function in computer algebra systems typically employ separate vector arguments for the four (possibly empty) parameter groups *a*1 ... *a**n*, *a**n*+1 ... *a**p*, *b*1 ... *b**m*, and *b**m*+1 ... *b**q*, and thus can omit the orders *p*, *q*, *n*, and *m* as redundant.

The *L* in the integral represents the path to be followed while integrating. Three choices are possible for this path:

1.

L

runs from −

i

∞ to +

i

∞ such that all poles of Γ(

b

j

−

s

),

j

= 1, 2, ...,

m

, are on the right of the path, while all poles of Γ(1 −

a

k

+

s

),

k

= 1, 2, ...,

n

, are on the left. The integral then converges for |arg

z

| <

δ

π

, where

$\delta =m+n-{\tfrac {1}{2}}(p+q);$

an obvious prerequisite for this is

δ

> 0. The integral additionally converges for |arg

z

| =

δ

π

≥ 0 if (q − p) (

σ

+

1

⁄

2

) > Re(

ν

) + 1, where

σ

represents Re(

s

) as the integration variable

s

approaches both +

i

∞ and −

i

∞, and where

$\nu =\sum _{j=1}^{q}b_{j}-\sum _{j=1}^{p}a_{j}.$

As a corollary, for |arg

z

| =

δ

π

and

p

=

q

the integral converges independent of

σ

whenever Re(

ν

) < −1.

2.

L

is a loop beginning and ending at +∞, encircling all poles of Γ(

b

j

−

s

),

j

= 1, 2, ...,

m

, exactly once in the negative direction, but not encircling any pole of Γ(1 −

a

k

+

s

),

k

= 1, 2, ...,

n

. Then the integral converges for all

z

if

q

>

p

≥ 0; it also converges for

q

=

p

> 0 as long as |

z

| < 1. In the latter case, the integral additionally converges for |

z

| = 1 if Re(

ν

) < −1, where

ν

is defined as for the first path.

3.

L

is a loop beginning and ending at −∞ and encircling all poles of Γ(1 −

a

k

+

s

),

k

= 1, 2, ...,

n

, exactly once in the positive direction, but not encircling any pole of Γ(

b

j

−

s

),

j

= 1, 2, ...,

m

. Now the integral converges for all

z

if

p

>

q

≥ 0; it also converges for

p

=

q

> 0 as long as |

z

| > 1. As noted for the second path too, in the case of

p

=

q

the integral also converges for |

z

| = 1 when Re(

ν

) < −1.

The conditions for convergence are readily established by applying Stirling's asymptotic approximation to the gamma functions in the integrand. When the integral converges for more than one of these paths, the results of integration can be shown to agree; if it converges for only one path, then this is the only one to be considered. In fact, numerical path integration in the complex plane constitutes a practicable and sensible approach to the calculation of Meijer G-functions.

As a consequence of this definition, the Meijer G-function is an analytic function of *z* with possible exception of the origin *z* = 0 and of the unit circle |*z*| = 1.

### Differential equation

The G-function satisfies the following linear differential equation of order max(*p*,*q*):

$\left[(-1)^{p-m-n}\;z\prod _{j=1}^{p}\left(z{\frac {d}{dz}}-a_{j}+1\right)-\prod _{j=1}^{q}\left(z{\frac {d}{dz}}-b_{j}\right)\right]G(z)=0.$

For a fundamental set of solutions of this equation in the case of *p* ≤ *q* one may take:

$G_{p,q}^{\,1,p}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p}\\b_{h},b_{1},\dots ,b_{h-1},b_{h+1},\dots ,b_{q}\end{matrix}}\;\right|\,(-1)^{p-m-n+1}\;z\right),\quad h=1,2,\dots ,q,$

and similarly in the case of *p* ≥ *q*:

$G_{p,q}^{\,q,1}\!\left(\left.{\begin{matrix}a_{h},a_{1},\dots ,a_{h-1},a_{h+1},\dots ,a_{p}\\b_{1},\dots ,b_{q}\end{matrix}}\;\right|\,(-1)^{q-m-n+1}\;z\right),\quad h=1,2,\dots ,p.$

These particular solutions are analytic except for a possible singularity at *z* = 0 (as well as a possible singularity at *z* = ∞), and in the case of *p* = *q* also an inevitable singularity at *z* = (−1)*p*−*m*−*n*. As will be seen presently, they can be identified with generalized hypergeometric functions *p**F**q*−1 of argument (−1)*p*−*m*−*n* *z* that are multiplied by a power *z**b**h*, and with generalized hypergeometric functions *q**F**p*−1 of argument (−1)*q*−*m*−*n* *z*−1 that are multiplied by a power *z**a**h*−1, respectively.

## Relationship between the G-function and the generalized hypergeometric function

If the integral converges when evaluated along the second path introduced above, and if no confluent poles appear among the Γ(*b**j* − *s*), *j* = 1, 2, ..., *m*, then the Meijer G-function can be expressed as a sum of residues in terms of generalized hypergeometric functions *p**F**q*−1 (Slater's theorem):

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=\sum _{h=1}^{m}{\frac {\prod _{j=1}^{m}\Gamma (b_{j}-b_{h})^{*}\prod _{j=1}^{n}\Gamma (1+b_{h}-a_{j})\;z^{b_{h}}}{\prod _{j=m+1}^{q}\Gamma (1+b_{h}-b_{j})\prod _{j=n+1}^{p}\Gamma (a_{j}-b_{h})}}\times$

$_{p}F_{q-1}\!\left(\left.{\begin{matrix}1+b_{h}-\mathbf {a_{p}} \\(1+b_{h}-\mathbf {b_{q}} )^{*}\end{matrix}}\;\right|\,(-1)^{p-m-n}\;z\right).$

The star indicates that the term corresponding to *j* = *h* is omitted. For the integral to converge along the second path one must have either *p* < *q*, or *p* = *q* and |*z*| < 1, and for the poles to be distinct no pair among the *b**j*, *j* = 1, 2, ..., *m*, may differ by an integer or zero. The asterisks in the relation remind us to ignore the contribution with index *j* = *h* as follows: In the product this amounts to replacing Γ(0) with 1, and in the argument of the hypergeometric function, if we recall the meaning of the vector notation,

$1+b_{h}-\mathbf {b_{q}} =(1+b_{h}-b_{1}),\,\dots ,\,(1+b_{h}-b_{j}),\,\dots ,\,(1+b_{h}-b_{q}),$

this amounts to shortening the vector length from *q* to *q*−1.

Note that when *m* = 0, the second path does not contain any pole, and so the integral must vanish identically,

$G_{p,q}^{\,0,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=0,$

if either *p* < *q*, or *p* = *q* and |*z*| < 1.

Similarly, if the integral converges when evaluated along the third path above, and if no confluent poles appear among the Γ(1 − *a**k* + *s*), *k* = 1, 2, ..., *n*, then the G-function can be expressed as:

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=\sum _{h=1}^{n}{\frac {\prod _{j=1}^{n}\Gamma (a_{h}-a_{j})^{*}\prod _{j=1}^{m}\Gamma (1-a_{h}+b_{j})\;z^{a_{h}-1}}{\prod _{j=n+1}^{p}\Gamma (1-a_{h}+a_{j})\prod _{j=m+1}^{q}\Gamma (a_{h}-b_{j})}}\times$

$_{q}F_{p-1}\!\left(\left.{\begin{matrix}1-a_{h}+\mathbf {b_{q}} \\(1-a_{h}+\mathbf {a_{p}} )^{*}\end{matrix}}\;\right|\,(-1)^{q-m-n}z^{-1}\right).$

For this, either *p* > *q*, or *p* = *q* and |*z*| > 1 are required, and no pair among the *a**k*, *k* = 1, 2, ..., *n*, may differ by an integer or zero. For *n* = 0 one consequently has:

$G_{p,q}^{\,m,0}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=0,$

if either *p* > *q*, or *p* = *q* and |*z*| > 1.

On the other hand, any generalized hypergeometric function can readily be expressed in terms of the Meijer G-function:

$\;_{p}F_{q}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)={\frac {\Gamma (\mathbf {b_{q}} )}{\Gamma (\mathbf {a_{p}} )}}\;G_{p,\,q+1}^{\,1,\,p}\!\left(\left.{\begin{matrix}1-\mathbf {a_{p}} \\0,1-\mathbf {b_{q}} \end{matrix}}\;\right|\,-z\right)={\frac {\Gamma (\mathbf {b_{q}} )}{\Gamma (\mathbf {a_{p}} )}}\;G_{q+1,\,p}^{\,p,\,1}\!\left(\left.{\begin{matrix}1,\mathbf {b_{q}} \\\mathbf {a_{p}} \end{matrix}}\;\right|\,-z^{-1}\right),$

where we have made use of the vector notation:

$\Gamma (\mathbf {a_{p}} )=\prod _{j=1}^{p}\Gamma (a_{j}).$

This holds unless a nonpositive integer value of at least one of its parameters **a****p** reduces the hypergeometric function to a finite polynomial, in which case the gamma prefactor of either G-function vanishes and the parameter sets of the G-functions violate the requirement *a**k* − *b**j* ≠ 1, 2, 3, ... for *k* = 1, 2, ..., *n* and *j* = 1, 2, ..., *m* from the definition above. Apart from this restriction, the relationship is valid whenever the generalized hypergeometric series *p**F**q*(*z*) converges, i. e. for any finite *z* when *p* ≤ *q*, and for |*z*| < 1 when *p* = *q* + 1. In the latter case, the relation with the G-function automatically provides the analytic continuation of *p**F**q*(*z*) to |*z*| ≥ 1 with a branch cut from 1 to ∞ along the real axis. Finally, the relation furnishes a natural extension of the definition of the hypergeometric function to orders *p* > *q* + 1. By means of the G-function we can thus solve the generalized hypergeometric differential equation for *p* > *q* + 1 as well.

### Polynomial cases

To express polynomial cases of generalized hypergeometric functions in terms of Meijer G-functions, a linear combination of two G-functions is needed in general:

$\;_{p+1}F_{q}\!\left(\left.{\begin{matrix}-h,\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=h!\;{\frac {\prod _{j=n+1}^{p}\Gamma (1-a_{j})\prod _{j=m+1}^{q}\Gamma (b_{j})}{\prod _{j=1}^{n}\Gamma (a_{j})\prod _{j=1}^{m}\Gamma (1-b_{j})}}\times$

$\left[G_{p+1,\,q+1}^{\,m+1,\,n}\!\left(\left.{\begin{matrix}1-\mathbf {a_{p}} ,h+1\\0,1-\mathbf {b_{q}} \end{matrix}}\;\right|\,(-1)^{p-m-n}\;z\right)+(-1)^{h}\;G_{p+1,\,q+1}^{\,m,\,n+1}\!\left(\left.{\begin{matrix}h+1,1-\mathbf {a_{p}} \\1-\mathbf {b_{q}} ,0\end{matrix}}\;\right|\,(-1)^{p-m-n}\;z\right)\right],$

where *h* = 0, 1, 2, ... equals the degree of the polynomial *p*+1*F**q*(*z*). The orders *m* and *n* can be chosen freely in the ranges 0 ≤ *m* ≤ *q* and 0 ≤ *n* ≤ *p*, which allows to avoid that specific integer values or integer differences among the parameters **a****p** and **b****q** of the polynomial give rise to divergent gamma functions in the prefactor or to a conflict with the definition of the G-function. Note that the first G-function vanishes for *n* = 0 if *p* > *q*, while the second G-function vanishes for *m* = 0 if *p* < *q*. Again, the formula can be verified by expressing the two G-functions as sums of residues; no cases of confluent poles permitted by the definition of the G-function need be excluded here.

## Basic properties of the G-function

As can be seen from the definition of the G-function, if equal parameters appear among the **a****p** and **b****q** determining the factors in the numerator and the denominator of the integrand, the fraction can be simplified, and the order of the function thereby be reduced. Whether the order *m* or *n* will decrease depends on the particular position of the parameters in question. Thus, if one of the *a**k*, *k* = 1, 2, ..., *n*, equals one of the *b**j*, *j* = *m* + 1, ..., *q*, the G-function lowers its orders *p*, *q* and *n*:

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},a_{2},\dots ,a_{p}\\b_{1},\dots ,b_{q-1},a_{1}\end{matrix}}\;\right|\,z\right)=G_{p-1,\,q-1}^{\,m,\,n-1}\!\left(\left.{\begin{matrix}a_{2},\dots ,a_{p}\\b_{1},\dots ,b_{q-1}\end{matrix}}\;\right|\,z\right),\quad n,p,q\geq 1.$

For the same reason, if one of the *a**k*, *k* = *n* + 1, ..., *p*, equals one of the *b**j*, *j* = 1, 2, ..., *m*, then the G-function lowers its orders *p*, *q* and *m*:

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p-1},b_{1}\\b_{1},b_{2},\dots ,b_{q}\end{matrix}}\;\right|\,z\right)=G_{p-1,\,q-1}^{\,m-1,\,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p-1}\\b_{2},\dots ,b_{q}\end{matrix}}\;\right|\,z\right),\quad m,p,q\geq 1.$

Starting from the definition, it is also possible to derive the following properties:

$z^{\rho }\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} +\rho \\\mathbf {b_{q}} +\rho \end{matrix}}\;\right|\,z\right),$

$G_{p+2,\,q}^{\,m,\,n+1}\!\left(\left.{\begin{matrix}\alpha ,\mathbf {a_{p}} ,\alpha '\\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=(-1)^{\alpha '-\alpha }\;G_{p+2,\,q}^{\,m,\,n+1}\!\left(\left.{\begin{matrix}\alpha ',\mathbf {a_{p}} ,\alpha \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right),\quad n\leq p,\;\alpha '-\alpha \in \mathbb {Z} ,$

$G_{p,\,q+2}^{\,m+1,\,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\beta ,\mathbf {b_{q}} ,\beta '\end{matrix}}\;\right|\,z\right)=(-1)^{\beta '-\beta }\;G_{p,\,q+2}^{\,m+1,\,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\beta ',\mathbf {b_{q}} ,\beta \end{matrix}}\;\right|\,z\right),\quad m\leq q,\;\beta '-\beta \in \mathbb {Z} ,$

$G_{p+1,\,q+1}^{\,m,\,n+1}\!\left(\left.{\begin{matrix}\alpha ,\mathbf {a_{p}} \\\mathbf {b_{q}} ,\beta \end{matrix}}\;\right|\,z\right)=(-1)^{\beta -\alpha }\;G_{p+1,\,q+1}^{\,m+1,\,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} ,\alpha \\\beta ,\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right),\quad m\leq q,\;\beta -\alpha =0,1,2,\dots ,$

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=G_{q,p}^{\,n,m}\!\left(\left.{\begin{matrix}1-\mathbf {b_{q}} \\1-\mathbf {a_{p}} \end{matrix}}\;\right|\,z^{-1}\right),$

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)={\frac {h^{1+\nu +(p-q)/2}}{(2\pi )^{(h-1)\delta }}}\;G_{hp,\,hq}^{\,hm,\,hn}\!\left(\left.{\begin{matrix}a_{1}/h,\dots ,(a_{1}+h-1)/h,\dots ,a_{p}/h,\dots ,(a_{p}+h-1)/h\\b_{1}/h,\dots ,(b_{1}+h-1)/h,\dots ,b_{q}/h,\dots ,(b_{q}+h-1)/h\end{matrix}}\;\right|\,{\frac {z^{h}}{h^{h(q-p)}}}\right),\quad h\in \mathbb {N} .$

The abbreviations *ν* and *δ* were introduced in the definition of the G-function above.

### Derivatives and antiderivatives

Concerning derivatives of the G-function, one finds these relationships:

${\frac {d}{dz}}\left[z^{1-a_{1}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)\right]=z^{-a_{1}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1}-1,a_{2},\dots ,a_{p}\\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right),\quad n\geq 1,$

${\frac {d}{dz}}\left[z^{1-a_{p}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)\right]=-z^{-a_{p}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p-1},a_{p}-1\\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right),\quad n<p.$

${\frac {d}{dz}}\left[z^{-b_{1}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)\right]=-z^{-1-b_{1}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\b_{1}+1,b_{2},\dots ,b_{q}\end{matrix}}\;\right|\,z\right),\quad m\geq 1,$

${\frac {d}{dz}}\left[z^{-b_{q}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)\right]=z^{-1-b_{q}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\b_{1},\dots ,b_{q-1},b_{q}+1\end{matrix}}\;\right|\,z\right),\quad m<q,$

From these four, equivalent relations can be deduced by simply evaluating the derivative on the left-hand side and manipulating a bit. One obtains for example:

$z{\frac {d}{dz}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1}-1,a_{2},\dots ,a_{p}\\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)+(a_{1}-1)\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right),\quad n\geq 1.$

Moreover, for derivatives of arbitrary order *h*, one has

$z^{h}{\frac {d^{h}}{dz^{h}}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=G_{p+1,\,q+1}^{\,m,\,n+1}\!\left(\left.{\begin{matrix}0,\mathbf {a_{p}} \\\mathbf {b_{q}} ,h\end{matrix}}\;\right|\,z\right)=(-1)^{h}\;G_{p+1,\,q+1}^{\,m+1,\,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} ,0\\h,\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right),$

$z^{h}{\frac {d^{h}}{dz^{h}}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z^{-1}\right)=G_{p+1,\,q+1}^{\,m+1,\,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} ,1-h\\1,\mathbf {b_{q}} \end{matrix}}\;\right|\,z^{-1}\right)=(-1)^{h}\;G_{p+1,\,q+1}^{\,m,\,n+1}\!\left(\left.{\begin{matrix}1-h,\mathbf {a_{p}} \\\mathbf {b_{q}} ,1\end{matrix}}\;\right|\,z^{-1}\right),$

which hold for *h* < 0 as well, thus allowing to obtain the antiderivative of any G-function as easily as the derivative. By choosing one or the other of the two results provided in either formula, one can always prevent the set of parameters in the result from violating the condition *a**k* − *b**j* ≠ 1, 2, 3, ... for *k* = 1, 2, ..., *n* and *j* = 1, 2, ..., *m* that is imposed by the definition of the G-function. Note that each pair of results becomes unequal in the case of *h* < 0.

From these relationships, corresponding properties of the Gauss hypergeometric function and of other special functions can be derived.

### Recurrence relations

By equating different expressions for the first-order derivatives, one arrives at the following 3-term recurrence relations among contiguous G-functions:

$(a_{p}-a_{1})\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1}-1,a_{2},\dots ,a_{p}\\b_{1},\dots ,b_{q}\end{matrix}}\;\right|\,z\right)+G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p-1},a_{p}-1\\b_{1},\dots ,b_{q}\end{matrix}}\;\right|\,z\right),\quad 1\leq n<p,$

$(b_{1}-b_{q})\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p}\\b_{1}+1,b_{2},\dots ,b_{q}\end{matrix}}\;\right|\,z\right)+G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p}\\b_{1},\dots ,b_{q-1},b_{q}+1\end{matrix}}\;\right|\,z\right),\quad 1\leq m<q,$

$(b_{1}-a_{1}+1)\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1}-1,a_{2},\dots ,a_{p}\\b_{1},\dots ,b_{q}\end{matrix}}\;\right|\,z\right)+G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p}\\b_{1}+1,b_{2},\dots ,b_{q}\end{matrix}}\;\right|\,z\right),\quad n\geq 1,\;m\geq 1,$

$(a_{p}-b_{q}-1)\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right)=G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p-1},a_{p}-1\\b_{1},\dots ,b_{q}\end{matrix}}\;\right|\,z\right)+G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p}\\b_{1},\dots ,b_{q-1},b_{q}+1\end{matrix}}\;\right|\,z\right),\quad n<p,\;m<q.$

Similar relations for the diagonal parameter pairs *a*1, *b**q* and *b*1, *a**p* follow by suitable combination of the above. Again, corresponding properties of hypergeometric and other special functions can be derived from these recurrence relations.

### Multiplication theorems

Provided that *z* ≠ 0, the following relationships hold:

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,wz\right)=w^{b_{1}}\sum _{h=0}^{\infty }{\frac {(1-w)^{h}}{h!}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\b_{1}+h,b_{2},\dots ,b_{q}\end{matrix}}\;\right|\,z\right),\quad m\geq 1,$

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,wz\right)=w^{b_{q}}\sum _{h=0}^{\infty }{\frac {(w-1)^{h}}{h!}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\b_{1},\dots ,b_{q-1},b_{q}+h\end{matrix}}\;\right|\,z\right),\quad m<q,$

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,{\frac {z}{w}}\right)=w^{1-a_{1}}\sum _{h=0}^{\infty }{\frac {(1-w)^{h}}{h!}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1}-h,a_{2},\dots ,a_{p}\\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right),\quad n\geq 1,$

$G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,{\frac {z}{w}}\right)=w^{1-a_{p}}\sum _{h=0}^{\infty }{\frac {(w-1)^{h}}{h!}}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{p-1},a_{p}-h\\\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right),\quad n<p.$

These follow by Taylor expansion about *w* = 1, with the help of the basic properties discussed above. The radii of convergence will be dependent on the value of *z* and on the G-function that is expanded. The expansions can be regarded as generalizations of similar theorems for Bessel, hypergeometric and confluent hypergeometric functions.

## Definite integrals involving the G-function

Among definite integrals involving an arbitrary G-function one has:

$\int _{0}^{\infty }x^{s-1}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,\eta x\right)dx={\frac {\eta ^{-s}\prod _{j=1}^{m}\Gamma (b_{j}+s)\prod _{j=1}^{n}\Gamma (1-a_{j}-s)}{\prod _{j=m+1}^{q}\Gamma (1-b_{j}-s)\prod _{j=n+1}^{p}\Gamma (a_{j}+s)}}.$

Note that the restrictions under which this integral exists have been omitted here. It is, of course, no surprise that the Mellin transform of a G-function should lead back to the integrand appearing in the definition above.

Euler-type integrals for the G-function are given by:

$\int _{0}^{1}x^{-\alpha }\;(1-x)^{\alpha -\beta -1}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,zx\right)dx=\Gamma (\alpha -\beta )\;G_{p+1,\,q+1}^{\,m,\,n+1}\!\left(\left.{\begin{matrix}\alpha ,\mathbf {a_{p}} \\\mathbf {b_{q}} ,\beta \end{matrix}}\;\right|\,z\right),$

$\int _{1}^{\infty }x^{-\alpha }\;(x-1)^{\alpha -\beta -1}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,zx\right)dx=\Gamma (\alpha -\beta )\;G_{p+1,\,q+1}^{\,m+1,\,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} ,\alpha \\\beta ,\mathbf {b_{q}} \end{matrix}}\;\right|\,z\right).$

Extensive restrictions under which these integrals exist can be found on p. 417 of "Tables of Integral Transforms", vol. II(1954), Edited by A. Erdelyi. Note that, in view of their effect on the G-function, these integrals can be used to define the operation of fractional integration for a fairly large class of functions (Erdélyi–Kober operators).

A result of fundamental importance is that the product of two arbitrary G-functions integrated over the positive real axis can be represented by just another G-function (convolution theorem):

$\int _{0}^{\infty }G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,\eta x\right)G_{\sigma ,\tau }^{\,\mu ,\nu }\!\left(\left.{\begin{matrix}\mathbf {c_{\sigma }} \\\mathbf {d_{\tau }} \end{matrix}}\;\right|\,\omega x\right)dx=$

$={\frac {1}{\eta }}\;G_{q+\sigma ,\,p+\tau }^{\,n+\mu ,\,m+\nu }\!\left(\left.{\begin{matrix}-b_{1},\dots ,-b_{m},\mathbf {c_{\sigma }} ,-b_{m+1},\dots ,-b_{q}\\-a_{1},\dots ,-a_{n},\mathbf {d_{\tau }} ,-a_{n+1},\dots ,-a_{p}\end{matrix}}\;\right|\,{\frac {\omega }{\eta }}\right)=$

$={\frac {1}{\omega }}\;G_{p+\tau ,\,q+\sigma }^{\,m+\nu ,\,n+\mu }\!\left(\left.{\begin{matrix}a_{1},\dots ,a_{n},-\mathbf {d_{\tau }} ,a_{n+1},\dots ,a_{p}\\b_{1},\dots ,b_{m},-\mathbf {c_{\sigma }} ,b_{m+1},\dots ,b_{q}\end{matrix}}\;\right|\,{\frac {\eta }{\omega }}\right).$

Restrictions under which the integral exists can be found in Meijer, C. S., 1941: Nederl. Akad. Wetensch, Proc. 44, pp. 82–92. Note how the Mellin transform of the result merely assembles the gamma factors from the Mellin transforms of the two functions in the integrand.

The convolution formula can be derived by substituting the defining Mellin–Barnes integral for one of the G-functions, reversing the order of integration, and evaluating the inner Mellin-transform integral. The preceding Euler-type integrals follow analogously.

### Laplace transform

Using the above convolution integral and basic properties one can show that:

$\int _{0}^{\infty }e^{-\omega x}\;x^{-\alpha }\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,\eta x\right)dx=\omega ^{\alpha -1}\;G_{p+1,\,q}^{\,m,\,n+1}\!\left(\left.{\begin{matrix}\alpha ,\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,{\frac {\eta }{\omega }}\right),$

where Re(*ω*) > 0. This is the Laplace transform of a function *G*(*ηx*) multiplied by a power *x*−*α*; if we put *α* = 0 we get the Laplace transform of the G-function. As usual, the inverse transform is then given by:

$x^{-\alpha }\;G_{p,\,q+1}^{\,m,\,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} ,\alpha \end{matrix}}\;\right|\,\eta x\right)={\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }e^{\omega x}\;\omega ^{\alpha -1}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,{\frac {\eta }{\omega }}\right)d\omega ,$

where *c* is a real positive constant that places the integration path to the right of any pole in the integrand.

Another formula for the Laplace transform of a G-function is:

$\int _{0}^{\infty }e^{-\omega x}\;G_{p,q}^{\,m,n}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,\eta x^{2}\right)dx={\frac {1}{{\sqrt {\pi }}\omega }}\;G_{p+2,\,q}^{\,m,\,n+2}\!\left(\left.{\begin{matrix}0,{\frac {1}{2}},\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\,{\frac {4\eta }{\omega ^{2}}}\right),$

where again Re(*ω*) > 0. Details of the restrictions under which the integrals exist have been omitted in both cases.

## Integral transforms based on the G-function

In general, two functions *k*(*z*,*y*) and *h*(*z*,*y*) are called a pair of transform kernels if, for any suitable function *f*(*z*) or any suitable function *g*(*z*), the following two relationships hold simultaneously:

$g(z)=\int _{0}^{\infty }k(z,y)\,f(y)\;dy,\quad f(z)=\int _{0}^{\infty }h(z,y)\,g(y)\;dy.$

The pair of kernels is said to be symmetric if *k*(*z*,*y*) = *h*(*z*,*y*).

### Narain transform

Roop Narain (1962, 1963a, 1963b) showed that the functions:

$k(z,y)=2\gamma \;(zy)^{\gamma -1/2}\;G_{p+q,\,m+n}^{\,m,\,p}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} ,\mathbf {b_{q}} \\\mathbf {c_{m}} ,\mathbf {d_{n}} \end{matrix}}\;\right|\,(zy)^{2\gamma }\right),$

$h(z,y)=2\gamma \;(zy)^{\gamma -1/2}\;G_{p+q,\,m+n}^{\,n,\,q}\!\left(\left.{\begin{matrix}-\mathbf {b_{q}} ,-\mathbf {a_{p}} \\-\mathbf {d_{n}} ,-\mathbf {c_{m}} \end{matrix}}\;\right|\,(zy)^{2\gamma }\right)$

are an asymmetric pair of transform kernels, where *γ* > 0, *n* − *p* = *m* − *q* > 0, and:

$\sum _{j=1}^{p}a_{j}+\sum _{j=1}^{q}b_{j}=\sum _{j=1}^{m}c_{j}+\sum _{j=1}^{n}d_{j},$

along with further convergence conditions. In particular, if *p* = *q*, *m* = *n*, *a**j* + *b**j* = 0 for *j* = 1, 2, ..., *p* and *c**j* + *d**j* = 0 for *j* = 1, 2, ..., *m*, then the pair of kernels becomes symmetric. The well-known Hankel transform is a symmetric special case of the Narain transform (*γ* = 1, *p* = *q* = 0, *m* = *n* = 1, *c*1 = −*d*1 = *ν*⁄2).

### Wimp transform

Jet Wimp (1964) showed that these functions are an asymmetric pair of transform kernels:

$k(z,y)=G_{p+2,\,q}^{\,m,\,n+2}\!\left(\left.{\begin{matrix}1-\nu +iz,1-\nu -iz,\mathbf {a_{p}} \\\mathbf {b_{q}} \end{matrix}}\;\right|\;y\right),$

$h(z,y)={\frac {i}{\pi }}ye^{-\nu \pi i}\left[e^{\pi y}A(\nu +iy,\nu -iy\,|\,ze^{i\pi })-e^{-\pi y}A(\nu -iy,\nu +iy\,|\,ze^{i\pi })\right],$

where the function *A*(·) is defined as:

$A(\alpha ,\beta \,|\,z)=G_{p+2,\,q}^{\,q-m,\,p-n+1}\!\left(\left.{\begin{matrix}-a_{n+1},-a_{n+2},\dots ,-a_{p},\alpha ,-a_{1},-a_{2},\dots ,-a_{n},\beta \\-b_{m+1},-b_{m+2},\dots ,-b_{q},-b_{1},-b_{2},\dots ,-b_{m}\end{matrix}}\;\right|\,z\right).$

### Generalized Laplace transform

The Laplace transform can be generalized in close analogy with Narain's generalization of the Hankel transform:

$g(s)=2\gamma \int _{0}^{\infty }(st)^{\gamma +\rho -1/2}\;G_{p,\,q+1}^{\,q+1,\,0}\!\left(\left.{\begin{matrix}\mathbf {a_{p}} \\0,\mathbf {b_{q}} \end{matrix}}\;\right|\,(st)^{2\gamma }\right)f(t)\;dt,$

$f(t)={\frac {\gamma }{\pi i}}\int _{c-i\infty }^{c+i\infty }(ts)^{\gamma -\rho -1/2}\;G_{p,\,q+1}^{\,1,\,p}\!\left(\left.{\begin{matrix}-\mathbf {a_{p}} \\0,-\mathbf {b_{q}} \end{matrix}}\;\right|\,-(ts)^{2\gamma }\right)g(s)\;ds,$

where *γ* > *0*, *p* ≤ *q*, and:

$(q+1-p)\,{\rho \over 2\gamma }=\sum _{j=1}^{p}a_{j}-\sum _{j=1}^{q}b_{j},$

and where the constant *c* > 0 places the second integration path to the right of any pole in the integrand. For *γ* = 1⁄2, *ρ* = 0 and *p* = *q* = 0, this corresponds to the familiar Laplace transform.

### Meijer transform

Two particular cases of this generalization were given by C.S. Meijer in 1940 and 1941. The case resulting for *γ* = 1, *ρ* = −*ν*, *p* = 0, *q* = 1 and *b*1 = *ν* may be written (Meijer 1940):

$g(s)={\sqrt {2/\pi }}\int _{0}^{\infty }(st)^{1/2}\,K_{\nu }(st)\,f(t)\;dt,$

$f(t)={\frac {1}{{\sqrt {2\pi }}\,i}}\int _{c-i\infty }^{c+i\infty }(ts)^{1/2}\,I_{\nu }(ts)\,g(s)\;ds,$

and the case obtained for *γ* = 1⁄2, *ρ* = −*m* − *k*, *p* = *q* = 1, *a*1 = *m* − *k* and *b*1 = 2*m* may be written (Meijer 1941a):

$g(s)=\int _{0}^{\infty }(st)^{-k-1/2}\,e^{-st/2}\,W_{k+1/2,\,m}(st)\,f(t)\;dt,$

$f(t)={\frac {\Gamma (1-k+m)}{2\pi i\,\Gamma (1+2m)}}\int _{c-i\infty }^{c+i\infty }(ts)^{k-1/2}\,e^{ts/2}\,M_{k-1/2,\,m}(ts)\,g(s)\;ds.$

Here *I**ν* and *K**ν* are the modified Bessel functions of the first and second kind, respectively, *M**k*,*m* and *W**k*,*m* are the Whittaker functions, and constant scale factors have been applied to the functions *f* and *g* and their arguments *s* and *t* in the first case.

## Representation of other functions in terms of the G-function

The following list shows how the familiar elementary functions result as special cases of the Meijer G-function:

$e^{x}=G_{0,1}^{\,1,0}\!\left(\left.{\begin{matrix}-\\0\end{matrix}}\;\right|\,-x\right),\qquad \forall x$

$\cos x={\sqrt {\pi }}\;G_{0,2}^{\,1,0}\!\left(\left.{\begin{matrix}-\\0,{\frac {1}{2}}\end{matrix}}\;\right|\,{\frac {x^{2}}{4}}\right),\qquad \forall x$

$\sin x={\sqrt {\pi }}\;G_{0,2}^{\,1,0}\!\left(\left.{\begin{matrix}-\\{\frac {1}{2}},0\end{matrix}}\;\right|\,{\frac {x^{2}}{4}}\right),\qquad {\frac {-\pi }{2}}<\arg x\leq {\frac {\pi }{2}}$

$\cosh x={\sqrt {\pi }}\;G_{0,2}^{\,1,0}\!\left(\left.{\begin{matrix}-\\0,{\frac {1}{2}}\end{matrix}}\;\right|\,-{\frac {x^{2}}{4}}\right),\qquad \forall x$

$\sinh x=-{\sqrt {\pi }}i\;G_{0,2}^{\,1,0}\!\left(\left.{\begin{matrix}-\\{\frac {1}{2}},0\end{matrix}}\;\right|\,-{\frac {x^{2}}{4}}\right),\qquad -\pi <\arg x\leq 0$

$\arcsin x={\frac {-i}{2{\sqrt {\pi }}}}\;G_{2,2}^{\,1,2}\!\left(\left.{\begin{matrix}1,1\\{\frac {1}{2}},0\end{matrix}}\;\right|\,-x^{2}\right),\qquad -\pi <\arg x\leq 0$

$\arctan x={\frac {1}{2}}\;G_{2,2}^{\,1,2}\!\left(\left.{\begin{matrix}{\frac {1}{2}},1\\{\frac {1}{2}},0\end{matrix}}\;\right|\,x^{2}\right),\qquad {\frac {-\pi }{2}}<\arg x\leq {\frac {\pi }{2}}$

$\operatorname {arccot} x={\frac {1}{2}}\;G_{2,2}^{\,2,1}\!\left(\left.{\begin{matrix}{\frac {1}{2}},1\\{\frac {1}{2}},0\end{matrix}}\;\right|\,x^{2}\right),\qquad {\frac {-\pi }{2}}<\arg x\leq {\frac {\pi }{2}}$

$\ln(1+x)=G_{2,2}^{\,1,2}\!\left(\left.{\begin{matrix}1,1\\1,0\end{matrix}}\;\right|\,x\right),\qquad \forall x$

$x=\mathrm {sgn} (x)\!\left[{\frac {3}{4\pi }}G_{1,3}^{3,0}\!\left(x^{2}\;{\Bigg |}\;{\begin{matrix}{\frac {3}{2}}\\[4pt]-{\frac {1}{2}},\,0,\,1\end{matrix}}\right)+{\frac {3}{8\pi x^{2}}}G_{1,3}^{3,0}\!\left(x^{2}\;{\Bigg |}\;{\begin{matrix}{\frac {5}{2}}\\[4pt]0,\,{\tfrac {1}{2}},\,2\end{matrix}}\right)+{\frac {\pi }{4}}G_{2,4}^{2,0}\!\left(x^{2}\;{\Bigg |}\;{\begin{matrix}-{\tfrac {1}{2}},\,{\tfrac {1}{2}}\\[4pt]-1,\,0,\,-{\tfrac {1}{2}},\,-{\tfrac {1}{2}}\end{matrix}}\right)-{\frac {\pi }{2}}G_{2,4}^{2,0}\!\left(x^{2}\;{\Bigg |}\;{\begin{matrix}-{\tfrac {1}{2}},\,{\tfrac {1}{2}}\\[4pt]-1,\,1,\,-{\tfrac {1}{2}},\,-{\tfrac {1}{2}}\end{matrix}}\right)+{\frac {\pi }{8}}G_{2,4}^{2,0}\!\left(x^{2}\;{\Bigg |}\;{\begin{matrix}-{\tfrac {1}{2}},\,{\tfrac {3}{2}}\\[4pt]0,\,0,\,-{\tfrac {1}{2}},\,-{\tfrac {1}{2}}\end{matrix}}\right)-{\frac {\pi }{4}}G_{2,4}^{2,0}\!\left(x^{2}\;{\Bigg |}\;{\begin{matrix}-{\tfrac {1}{2}},\,{\tfrac {3}{2}}\\[4pt]0,\,1,\,-{\tfrac {1}{2}},\,-{\tfrac {1}{2}}\end{matrix}}\right)\right],\qquad \forall x$

$H(1-|x|)=G_{1,1}^{\,1,0}\!\left(\left.{\begin{matrix}1\\0\end{matrix}}\;\right|\,x\right),\qquad \forall x$

$H(|x|-1)=G_{1,1}^{\,0,1}\!\left(\left.{\begin{matrix}1\\0\end{matrix}}\;\right|\,x\right),\qquad \forall x$

Here, *H* denotes the Heaviside step function.

The subsequent list shows how some higher functions can be expressed in terms of the G-function:

$\gamma (\alpha ,x)=G_{1,2}^{\,1,1}\!\left(\left.{\begin{matrix}1\\\alpha ,0\end{matrix}}\;\right|\,x\right),\qquad \forall x$

$\Gamma (\alpha ,x)=G_{1,2}^{\,2,0}\!\left(\left.{\begin{matrix}1\\\alpha ,0\end{matrix}}\;\right|\,x\right),\qquad \forall x$

$J_{\nu }(x)=G_{0,2}^{\,1,0}\!\left(\left.{\begin{matrix}-\\{\frac {\nu }{2}},{\frac {-\nu }{2}}\end{matrix}}\;\right|\,{\frac {x^{2}}{4}}\right),\qquad {\frac {-\pi }{2}}<\arg x\leq {\frac {\pi }{2}}$

$Y_{\nu }(x)=G_{1,3}^{\,2,0}\!\left(\left.{\begin{matrix}{\frac {-\nu -1}{2}}\\{\frac {\nu }{2}},{\frac {-\nu }{2}},{\frac {-\nu -1}{2}}\end{matrix}}\;\right|\,{\frac {x^{2}}{4}}\right),\qquad {\frac {-\pi }{2}}<\arg x\leq {\frac {\pi }{2}}$

$I_{\nu }(x)=i^{-\nu }\;G_{0,2}^{\,1,0}\!\left(\left.{\begin{matrix}-\\{\frac {\nu }{2}},{\frac {-\nu }{2}}\end{matrix}}\;\right|\,-{\frac {x^{2}}{4}}\right),\qquad -\pi <\arg x\leq 0$

$K_{\nu }(x)={\frac {1}{2}}\;G_{0,2}^{\,2,0}\!\left(\left.{\begin{matrix}-\\{\frac {\nu }{2}},{\frac {-\nu }{2}}\end{matrix}}\;\right|\,{\frac {x^{2}}{4}}\right),\qquad {\frac {-\pi }{2}}<\arg x\leq {\frac {\pi }{2}}$

$\Phi (x,n,a)=G_{n+1,\,n+1}^{\,1,\,n+1}\!\left(\left.{\begin{matrix}0,1-a,\dots ,1-a\\0,-a,\dots ,-a\end{matrix}}\;\right|\,-x\right),\qquad \forall x,\;n=0,1,2,\dots$

$\Phi (x,-n,a)=G_{n+1,\,n+1}^{\,1,\,n+1}\!\left(\left.{\begin{matrix}0,-a,\dots ,-a\\0,1-a,\dots ,1-a\end{matrix}}\;\right|\,-x\right),\qquad \forall x,\;n=0,1,2,\dots$

Even the derivatives of γ(*α*,*x*) and Γ(*α*,*x*) with respect to *α* can be expressed in terms of the Meijer G-function. Here, γ and Γ are the lower and upper incomplete gamma functions, *J**ν* and *Y**ν* are the Bessel functions of the first and second kind, respectively, *I**ν* and *K**ν* are the corresponding modified Bessel functions, and Φ is the Lerch transcendent.
