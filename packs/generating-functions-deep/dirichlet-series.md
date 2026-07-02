---
title: "Dirichlet series"
source: https://en.wikipedia.org/wiki/Dirichlet_series
domain: generating-functions-deep
license: CC-BY-SA-4.0
tags: generating function, formal power series, umbral calculus, lagrange inversion theorem
fetched: 2026-07-02
---

# Dirichlet series

In mathematics, a **Dirichlet series** is any series of the form $\sum _{n=1}^{\infty }{\frac {a_{n}}{n^{s}}},$ where *s* is complex, and $a_{n}$ is a complex sequence. It is a special case of general Dirichlet series.

Dirichlet series play a variety of important roles in analytic number theory. The most usually seen definition of the Riemann zeta function is a Dirichlet series, as are the Dirichlet *L*-functions. Specifically, the Riemann zeta function *ζ*(*s*) is the Dirichlet series of the **constant unit function** *u*(*n*), namely:

$\zeta (s)=\sum _{n=1}^{\infty }{\frac {1}{n^{s}}}=\sum _{n=1}^{\infty }{\frac {u(n)}{n^{s}}}=D(u,s),$

where *D*(*u*, *s*) denotes the Dirichlet series of *u*(*n*). It is conjectured that the Selberg class of series obeys the generalized Riemann hypothesis. The series is named in honor of Peter Gustav Lejeune Dirichlet.

## Combinatorial importance

Dirichlet series can be used as generating series for counting weighted sets of objects with respect to a weight which is combined multiplicatively when taking Cartesian products.

Suppose that *A* is a set with a function *w* : *A* → **N** assigning a weight to each of the elements of *A*, and suppose additionally that the fibre over any natural number under that weight is a finite set. (We call such an arrangement (*A*, *w*) a weighted set.) Suppose additionally that *an* is the number of elements of *A* with weight *n*. Then we define the formal Dirichlet generating series for *A* with respect to *w* as follows:

${\mathfrak {D}}_{w}^{A}(s)=\sum _{a\in A}{\frac {1}{w(a)^{s}}}=\sum _{n=1}^{\infty }{\frac {a_{n}}{n^{s}}}$

Note that if *A* and *B* are disjoint subsets of some weighted set (*U*, *w*), then the Dirichlet series for their (disjoint) union is equal to the sum of their Dirichlet series:

${\mathfrak {D}}_{w}^{A\uplus B}(s)={\mathfrak {D}}_{w}^{A}(s)+{\mathfrak {D}}_{w}^{B}(s).$

Moreover, if (*A*, *u*) and (*B*, *v*) are two weighted sets, and we define a weight function *w*: *A* × *B* → **N** by

$w(a,b)=u(a)v(b),$

for all *a* in *A* and *b* in *B*, then we have the following decomposition for the Dirichlet series of the Cartesian product:

${\mathfrak {D}}_{w}^{A\times B}(s)={\mathfrak {D}}_{u}^{A}(s)\cdot {\mathfrak {D}}_{v}^{B}(s).$

This follows ultimately from the simple fact that ⁠ $n^{-s}\cdot m^{-s}=(nm)^{-s}$ ⁠.

## Examples

The most famous example of a Dirichlet series is

$\zeta (s)=\sum _{n=1}^{\infty }{\frac {1}{n^{s}}},$

whose analytic continuation to $\mathbb {C}$ (apart from a simple pole at $s=1$ ) is the Riemann zeta function.

Provided that f is real-valued at all natural numbers n, the respective real and imaginary parts of the Dirichlet series F have known formulas where we write $s\equiv \sigma +it$ :

${\begin{aligned}\Re [F(s)]&=\sum _{n\geq 1}{\frac {~f(n)\,\cos(t\log n)~}{n^{\sigma }}}\\\Im [F(s)]&=-\sum _{n\geq 1}{\frac {~f(n)\,\sin(t\log n)~}{n^{\sigma }}}\,.\end{aligned}}$

Treating these as formal Dirichlet series for the time being in order to be able to ignore matters of convergence, note that we have:

${\begin{aligned}\zeta (s)&={\mathfrak {D}}_{\operatorname {id} }^{\mathbb {N} }(s)=\prod _{p{\text{ prime}}}{\mathfrak {D}}_{\operatorname {id} }^{\{p^{n}:n\in \mathbb {N} \}}(s)=\prod _{p{\text{ prime}}}\sum _{n\in \mathbb {N} }{\mathfrak {D}}_{\operatorname {id} }^{\{p^{n}\}}(s)\\&=\prod _{p{\text{ prime}}}\sum _{n\in \mathbb {N} }{\frac {1}{(p^{n})^{s}}}=\prod _{p{\text{ prime}}}\sum _{n\in \mathbb {N} }\left({\frac {1}{p^{s}}}\right)^{n}=\prod _{p{\text{ prime}}}{\frac {1}{1-p^{-s}}}\end{aligned}}$

as each natural number has a unique multiplicative decomposition into powers of primes. It is this bit of combinatorics which inspires the Euler product formula.

Another is:

${\frac {1}{\zeta (s)}}=\sum _{n=1}^{\infty }{\frac {\mu (n)}{n^{s}}}$

where *μ*(*n*) is the Möbius function. This and many of the following series may be obtained by applying Möbius inversion and Dirichlet convolution to known series. For example, given a Dirichlet character *χ*(*n*) one has

${\frac {1}{L(\chi ,s)}}=\sum _{n=1}^{\infty }{\frac {\mu (n)\chi (n)}{n^{s}}}$

where *L*(*χ*, *s*) is a Dirichlet L-function.

If the arithmetic function *f* has a Dirichlet inverse function $f^{-1}(n)$ , i.e., if there exists an inverse function such that the Dirichlet convolution of *f* with its inverse yields the multiplicative identity ${\textstyle \sum _{d|n}f(d)f^{-1}(n/d)=\delta _{n,1}}$ , then the DGF of the inverse function is given by the reciprocal of *F*:

$\sum _{n\geq 1}{\frac {f^{-1}(n)}{n^{s}}}=\left(\sum _{n\geq 1}{\frac {f(n)}{n^{s}}}\right)^{-1}.$

Other identities include

${\frac {\zeta (s-1)}{\zeta (s)}}=\sum _{n=1}^{\infty }{\frac {\varphi (n)}{n^{s}}}$

where $\varphi (n)$ is the totient function,

${\frac {\zeta (s-k)}{\zeta (s)}}=\sum _{n=1}^{\infty }{\frac {J_{k}(n)}{n^{s}}}$

where *Jk* is the Jordan function, and

${\begin{aligned}&\zeta (s)\zeta (s-a)=\sum _{n=1}^{\infty }{\frac {\sigma _{a}(n)}{n^{s}}}\\[6pt]&{\frac {\zeta (s)\zeta (s-a)\zeta (s-2a)}{\zeta (2s-2a)}}=\sum _{n=1}^{\infty }{\frac {\sigma _{a}(n^{2})}{n^{s}}}\\[6pt]&{\frac {\zeta (s)\zeta (s-a)\zeta (s-b)\zeta (s-a-b)}{\zeta (2s-a-b)}}=\sum _{n=1}^{\infty }{\frac {\sigma _{a}(n)\sigma _{b}(n)}{n^{s}}}\end{aligned}}$

where *σ**a*(*n*) is the divisor function. By specialization to the divisor function *d* = *σ*0 we have

${\begin{aligned}\zeta ^{2}(s)&=\sum _{n=1}^{\infty }{\frac {d(n)}{n^{s}}}\\[6pt]{\frac {\zeta ^{3}(s)}{\zeta (2s)}}&=\sum _{n=1}^{\infty }{\frac {d(n^{2})}{n^{s}}}\\[6pt]{\frac {\zeta ^{4}(s)}{\zeta (2s)}}&=\sum _{n=1}^{\infty }{\frac {d(n)^{2}}{n^{s}}}.\end{aligned}}$

The logarithm of the zeta function is given by

$\log \zeta (s)=\sum _{n=2}^{\infty }{\frac {\Lambda (n)}{\log(n)}}{\frac {1}{n^{s}}},\qquad \Re (s)>1$

where Λ(*n*) is the von Mangoldt function. Similarly, we have that

$-\zeta '(s)=\sum _{n=2}^{\infty }{\frac {\log(n)}{n^{s}}},\qquad \Re (s)>1.$

The logarithmic derivative of the zeta function is then

${\frac {\zeta '(s)}{\zeta (s)}}=-\sum _{n=1}^{\infty }{\frac {\Lambda (n)}{n^{s}}}.$

These last three are special cases of a more general relationship for derivatives of Dirichlet series, given below.

Given the Liouville function *λ*(*n*), one has

${\frac {\zeta (2s)}{\zeta (s)}}=\sum _{n=1}^{\infty }{\frac {\lambda (n)}{n^{s}}}.$

Yet another example involves Ramanujan's sum:

${\frac {\sigma _{1-s}(m)}{\zeta (s)}}=\sum _{n=1}^{\infty }{\frac {c_{n}(m)}{n^{s}}}.$

Another pair of examples involves the Möbius function and the prime omega function:

${\frac {\zeta (s)}{\zeta (2s)}}=\sum _{n=1}^{\infty }{\frac {|\mu (n)|}{n^{s}}}\equiv \sum _{n=1}^{\infty }{\frac {\mu ^{2}(n)}{n^{s}}}.$

${\frac {\zeta ^{2}(s)}{\zeta (2s)}}=\sum _{n=1}^{\infty }{\frac {2^{\omega (n)}}{n^{s}}}.$

We have that the Dirichlet series for the prime zeta function, which is the analog to the Riemann zeta function summed only over indices *n* which are prime, is given by a sum over the Moebius function and the logarithms of the zeta function:

$P(s):=\sum _{p{\text{ prime}}}p^{-s}=\sum _{n\geq 1}{\frac {\mu (n)}{n}}\log \zeta (ns).$

A large tabular catalog listing of other examples of sums corresponding to known Dirichlet series representations is found here.

Examples of Dirichlet series DGFs corresponding to additive (rather than multiplicative) *f* are given here for the prime omega functions $\omega (n)$ and $\Omega (n)$ , which respectively count the number of distinct prime factors of *n* (with multiplicity or not). For example, the DGF of the first of these functions is expressed as the product of the Riemann zeta function and the prime zeta function for any complex *s* with $\Re (s)>1$ :

$\sum _{n\geq 1}{\frac {\omega (n)}{n^{s}}}=\zeta (s)\cdot P(s),\Re (s)>1.$

If *f* is a multiplicative function such that its DGF *F* converges absolutely for all $\Re (s)>\sigma _{a,f}$ , and if *p* is any prime number, we have that

$\left(1+f(p)p^{-s}\right)\times \sum _{n\geq 1}{\frac {f(n)\mu (n)}{n^{s}}}=\left(1-f(p)p^{-s}\right)\times \sum _{n\geq 1}{\frac {f(n)\mu (n)\mu (\gcd(p,n))}{n^{s}}},\forall \Re (s)>\sigma _{a,f},$

where $\mu (n)$ is the Moebius function. Another unique Dirichlet series identity generates the summatory function of some arithmetic *f* evaluated at GCD inputs given by

$\sum _{n\geq 1}\left(\sum _{k=1}^{n}f(\gcd(k,n))\right){\frac {1}{n^{s}}}={\frac {\zeta (s-1)}{\zeta (s)}}\times \sum _{n\geq 1}{\frac {f(n)}{n^{s}}},\forall \Re (s)>\sigma _{a,f}+1.$

We also have a formula between the DGFs of two arithmetic functions *f* and *g* related by Moebius inversion. In particular, if ⁠ $g(n)=(f\ast 1)(n)$ ⁠, then by Moebius inversion we have that ⁠ $f(n)=(g\ast \mu )(n)$ ⁠. Hence, if *F* and *G* are the two respective DGFs of *f* and *g*, then we can relate these two DGFs by the formulas:

$F(s)={\frac {G(s)}{\zeta (s)}},\Re (s)>\max(\sigma _{a,f},\sigma _{a,g}).$

There is a known formula for the exponential of a Dirichlet series. If $F(s)=\exp(G(s))$ is the DGF of some arithmetic *f* with $f(1)\neq 0$ , then the DGF *G* is expressed by the sum

$G(s)=\log(f(1))+\sum _{n\geq 2}{\frac {(f^{\prime }\ast f^{-1})(n)}{\log(n)\cdot n^{s}}},$

where $f^{-1}(n)$ is the Dirichlet inverse of *f* and where the arithmetic derivative of *f* is given by the formula $f^{\prime }(n)=\log(n)\cdot f(n)$ for all natural numbers $n\geq 2$ .

## Analytic properties

Given a sequence $\{a_{n}\}_{n\in \mathbb {N} }$ of complex numbers we try to consider the value of

$f(s)=\sum _{n=1}^{\infty }{\frac {a_{n}}{n^{s}}}$

as a function of the complex variable *s*. In order for this to make sense, we need to consider the convergence properties of the above infinite series:

If $\{a_{n}\}_{n\in \mathbb {N} }$ is a bounded sequence of complex numbers, then the corresponding Dirichlet series *f* converges absolutely on the open half-plane Re(*s*) > 1. In general, if *an* = O(*nk*), the series converges absolutely in the half plane Re(*s*) > *k* + 1.

If the set of sums

$a_{n}+a_{n+1}+\cdots +a_{n+k}$

is bounded for *n* and *k* ≥ 0, then the above infinite series converges on the open half-plane of *s* such that Re(*s*) > 0.

In both cases *f* is an analytic function on the corresponding open half plane.

In general $\sigma$ is the **abscissa of convergence** of a Dirichlet series if it converges for $\Re (s)>\sigma$ and diverges for $\Re (s)<\sigma .$ This is the analogue for Dirichlet series of the radius of convergence for power series. The Dirichlet series case is more complicated, though: absolute convergence and uniform convergence may occur in distinct half-planes.

In many cases, the analytic function associated with a Dirichlet series has an analytic extension to a larger domain.

### Abscissa of convergence

Suppose

$\sum _{n=1}^{\infty }{\frac {a_{n}}{n^{s_{0}}}}$

converges for some $s_{0}\in \mathbb {C} ,\Re (s_{0})>0.$

Proposition 1.

$A(N):=\sum _{n=1}^{N}a_{n}=o(N^{s_{0}}).$

*Proof.* Note that:

$(n+1)^{s}-n^{s}=\int _{n}^{n+1}sx^{s-1}\,dx={\mathcal {O}}(n^{s-1}).$

and define

$B(N)=\sum _{n=1}^{N}{\frac {a_{n}}{n^{s_{0}}}}=\ell +o(1)$

where

$\ell =\sum _{n=1}^{\infty }{\frac {a_{n}}{n^{s_{0}}}}.$

By summation by parts we have

${\begin{aligned}A(N)&=\sum _{n=1}^{N}{\frac {a_{n}}{n^{s_{0}}}}n^{s_{0}}\\&=B(N)N^{s_{0}}+\sum _{n=1}^{N-1}B(n)\left(n^{s_{0}}-(n+1)^{s_{0}}\right)\\&=(B(N)-\ell )N^{s_{0}}+\sum _{n=1}^{N-1}(B(n)-\ell )\left(n^{s_{0}}-(n+1)^{s_{0}}\right)\\&=o(N^{s_{0}})+\sum _{n=1}^{N-1}{\mathcal {o}}(n^{s_{0}-1})\\&=o(N^{s_{0}})\end{aligned}}$

Proposition 2.

Define

$L={\begin{cases}\sum _{n=1}^{\infty }a_{n}&{\text{If convergent}}\\0&{\text{otherwise}}\end{cases}}$

Then:

$\sigma =\limsup _{N\to \infty }{\frac {\ln |A(N)-L|}{\ln N}}=\inf _{\sigma '}\left\{A(N)-L={\mathcal {O}}(N^{\sigma '})\right\}$

is the abscissa of convergence of the Dirichlet series.

*Proof.* From the definition,

$\forall \varepsilon >0\qquad A(N)-L={\mathcal {O}}(N^{\sigma +\varepsilon })$

so that

${\begin{aligned}\sum _{n=1}^{N}{\frac {a_{n}}{n^{s}}}&=A(N)N^{-s}+\sum _{n=1}^{N-1}A(n)(n^{-s}-(n+1)^{-s})\\&=(A(N)-L)N^{-s}+\sum _{n=1}^{N-1}(A(n)-L)(n^{-s}-(n+1)^{-s})\\&={\mathcal {O}}(N^{\sigma +\varepsilon -s})+\sum _{n=1}^{N-1}{\mathcal {O}}(n^{\sigma +\varepsilon -s-1})\end{aligned}}$

which converges as $N\to \infty$ whenever $\Re (s)>\sigma .$ Hence, for every s such that ${\textstyle \sum _{n=1}^{\infty }a_{n}n^{-s}}$ diverges, we have $\sigma \geq \Re (s),$ and this finishes the proof.

Proposition 3.

If

$\sum _{n=1}^{\infty }a_{n}$

converges then

$f(\sigma +it)=o\left({\tfrac {1}{\sigma }}\right)$

as

$\sigma \to 0^{+}$

and where it is meromorphic (

$f(s)$

has no poles on

$\Re (s)=0$

).

*Proof.* Note that

$n^{-s}-(n+1)^{-s}=sn^{-s-1}+O(n^{-s-2})$

and $A(N)-f(0)\to 0$ we have by summation by parts, for $\Re (s)>0$

${\begin{aligned}f(s)&=\lim _{N\to \infty }\sum _{n=1}^{N}{\frac {a_{n}}{n^{s}}}\\&=\lim _{N\to \infty }A(N)N^{-s}+\sum _{n=1}^{N-1}A(n)(n^{-s}-(n+1)^{-s})\\&=s\sum _{n=1}^{\infty }A(n)n^{-s-1}+\underbrace {{\mathcal {O}}\left(\sum _{n=1}^{\infty }A(n)n^{-s-2}\right)} _{={\mathcal {O}}(1)}\end{aligned}}$

Now find *N* such that for *n* > *N*, $|A(n)-f(0)|<\varepsilon$

$s\sum _{n=1}^{\infty }A(n)n^{-s-1}=\underbrace {sf(0)\zeta (s+1)+s\sum _{n=1}^{N}(A(n)-f(0))n^{-s-1}} _{={\mathcal {O}}(1)}+\underbrace {s\sum _{n=N+1}^{\infty }(A(n)-f(0))n^{-s-1}} _{<\varepsilon |s|\int _{N}^{\infty }x^{-\Re (s)-1}\,dx}$

and hence, for every $\varepsilon >0$ there is a C such that for $\sigma >0$ :

$|f(\sigma +it)|<C+\varepsilon |\sigma +it|{\frac {1}{\sigma }}.$

## Formal Dirichlet series

A formal Dirichlet series over a ring *R* is associated to a function *a* from the positive integers to *R*

$D(a,s)=\sum _{n=1}^{\infty }a(n)n^{-s}\$

with addition and multiplication defined by

$D(a,s)+D(b,s)=\sum _{n=1}^{\infty }(a+b)(n)n^{-s}\$

$D(a,s)\cdot D(b,s)=\sum _{n=1}^{\infty }(a*b)(n)n^{-s}\$

where

$(a+b)(n)=a(n)+b(n)\$

is the pointwise sum and

$(a*b)(n)=\sum _{k\mid n}a(k)b(n/k)\$

is the Dirichlet convolution of *a* and *b*.

The formal Dirichlet series form a ring Ω, indeed an *R*-algebra, with the zero function as additive zero element and the function *δ* defined by *δ*(1) = 1, *δ*(*n*) = 0 for *n* > 1 as multiplicative identity. An element of this ring is invertible if *a*(1) is invertible in *R*. If *R* is commutative, so is Ω; if *R* is an integral domain, so is Ω. The non-zero multiplicative functions form a subgroup of the group of units of Ω.

The ring of formal Dirichlet series over **C** is isomorphic to a ring of formal power series in countably many variables.

## Derivatives

Given

$F(s)=\sum _{n=1}^{\infty }{\frac {f(n)}{n^{s}}}$

it is possible to show that

$F'(s)=-\sum _{n=1}^{\infty }{\frac {f(n)\log(n)}{n^{s}}}$

assuming the right hand side converges. For a completely multiplicative function *f*(*n*), and assuming the series converges for Re(*s*) > *σ*0, then one has that

${\frac {F^{\prime }(s)}{F(s)}}=-\sum _{n=1}^{\infty }{\frac {f(n)\Lambda (n)}{n^{s}}}$

converges for Re(*s*) > *σ*0. Here, Λ(*n*) is the von Mangoldt function.

## Products

Suppose

$F(s)=\sum _{n=1}^{\infty }f(n)n^{-s}$

and

$G(s)=\sum _{n=1}^{\infty }g(n)n^{-s}.$

If both *F*(*s*) and *G*(*s*) are absolutely convergent for *s* > *a* and *s* > *b* then we have

${\frac {1}{2T}}\int _{-T}^{T}\,F(a+it)G(b-it)\,dt=\sum _{n=1}^{\infty }f(n)g(n)n^{-a-b}{\text{ as }}T\sim \infty .$

If *a* = *b* and *f*(*n*) = *g*(*n*), we have

${\frac {1}{2T}}\int _{-T}^{T}|F(a+it)|^{2}\,dt=\sum _{n=1}^{\infty }[f(n)]^{2}n^{-2a}{\text{ as }}T\sim \infty .$

## Coefficient inversion (integral formula)

For all positive integers $x\geq 1$ , the function *f* at *x*, $f(x)$ , can be recovered from the Dirichlet generating function (DGF) *F* of *f* (or the Dirichlet series over *f*) using the following integral formula whenever $\sigma >\sigma _{a,f}$ , the abscissa of absolute convergence of the DGF *F*

$f(x)=\lim _{T\rightarrow \infty }{\frac {1}{2T}}\int _{-T}^{T}x^{\sigma +it}F(\sigma +it)dt.$

It is also possible to invert the Mellin transform of the summatory function of *f* that defines the DGF *F* of *f* to obtain the coefficients of the Dirichlet series (see section below). In this case, we arrive at a complex contour integral formula related to Perron's theorem. Practically speaking, the rates of convergence of the above formula as a function of *T* are variable, and if the Dirichlet series *F* is sensitive to sign changes as a slowly converging series, it may require very large *T* to approximate the coefficients of *F* using this formula without taking the formal limit.

Another variant of the previous formula stated in Apostol's book provides an integral formula for an alternate sum in the following form for $c,x>0$ and any real $\Re (s)\equiv \sigma >\sigma _{a,f}-c$ where we denote $\Re (s):=\sigma$ :

${\sum _{n\leq x}}^{\prime }{\frac {f(n)}{n^{s}}}={\frac {1}{2\pi i}}\int _{c-i\infty }^{c+i\infty }D_{f}(s+z){\frac {x^{z}}{z}}dz.$

## Integral and series transformations

The inverse Mellin transform of a Dirichlet series, divided by s, is given by Perron's formula. Additionally, if ${\textstyle F(z):=\sum _{n\geq 0}f_{n}z^{n}}$ is the (formal) ordinary generating function of the sequence of $\{f_{n}\}_{n\geq 0}$ , then an integral representation for the Dirichlet series of the generating function sequence, $\{f_{n}z^{n}\}_{n\geq 0}$ , is given by

$\sum _{n\geq 0}{\frac {f_{n}z^{n}}{(n+1)^{s}}}={\frac {(-1)^{s-1}}{(s-1)!}}\int _{0}^{1}\log ^{s-1}(t)F(tz)\,dt,\ s\geq 1.$

Another class of related derivative and series-based generating function transformations on the ordinary generating function of a sequence which effectively produces the left-hand-side expansion in the previous equation are respectively defined in.

## Relation to power series

The sequence *an* generated by a Dirichlet series generating function corresponding to:

$\zeta (s)^{m}=\sum _{n=1}^{\infty }{\frac {a_{n}}{n^{s}}}$

where *ζ*(*s*) is the Riemann zeta function, has the ordinary generating function:

$\sum _{n=1}^{\infty }a_{n}x^{n}=x+{m \choose 1}\sum _{a=2}^{\infty }x^{a}+{m \choose 2}\sum _{a=2}^{\infty }\sum _{b=2}^{\infty }x^{ab}+{m \choose 3}\sum _{a=2}^{\infty }\sum _{b=2}^{\infty }\sum _{c=2}^{\infty }x^{abc}+{m \choose 4}\sum _{a=2}^{\infty }\sum _{b=2}^{\infty }\sum _{c=2}^{\infty }\sum _{d=2}^{\infty }x^{abcd}+\cdots$

## Relation to the summatory function of an arithmetic function via Mellin transforms

If *f* is an arithmetic function with corresponding DGF *F*, and the summatory function of *f* is defined by

$S_{f}(x):={\begin{cases}\sum _{n\leq x}f(n),&x\geq 1;\\0,&0<x<1,\end{cases}}$

then we can express *F* by the Mellin transform of the summatory function at $-s$ . Namely, we have that

$F(s)=s\cdot \int _{1}^{\infty }{\frac {S_{f}(x)}{x^{s+1}}}dx,\Re (s)>\sigma _{a,f}.$

For $\sigma :=\Re (s)>0$ and any natural numbers $N\geq 1$ , we also have the approximation to the DGF *F* of *f* given by

$F(s)=\sum _{n\leq N}f(n)n^{-s}-{\frac {S_{f}(N)}{N^{s}}}+s\cdot \int _{N}^{\infty }{\frac {S_{f}(y)}{y^{s+1}}}dy.$
