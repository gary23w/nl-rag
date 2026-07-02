---
title: "Method of steepest descent"
source: https://en.wikipedia.org/wiki/Method_of_steepest_descent
domain: asymptotic-analysis
license: CC-BY-SA-4.0
tags: asymptotic analysis, asymptotic expansion, steepest descent, borel summation
fetched: 2026-07-02
---

# Method of steepest descent

In mathematics, the **method of steepest descent** or **saddle-point method** is an extension of Laplace's method for approximating an integral, where one deforms a contour integral in the complex plane to pass near a stationary point (saddle point), in roughly the direction of steepest descent or stationary phase. The saddle-point approximation is used with integrals in the complex plane, whereas Laplace’s method is used with real integrals.

The integral to be estimated is often of the form

$\int _{C}f(z)e^{\lambda g(z)}\,dz,$

where *C* is a contour, and λ is large. One version of the method of steepest descent deforms the contour of integration *C* into a new path integration *C′* so that the following conditions hold:

1. *C′* passes through one or more zeros of the derivative *g*′(*z*),
2. the imaginary part of *g*(*z*) is constant on *C′*.

The method of steepest descent was first published by Debye (1909), who used it to estimate Bessel functions and pointed out that it occurred in the unpublished note by Riemann (1863) about hypergeometric functions. The contour of steepest descent has a minimax property, see Fedoryuk (2001). Siegel (1932) described some other unpublished notes of Riemann, where he used this method to derive the Riemann–Siegel formula.

When applied to the distribution of the sum of a large number of independent random variables in statistics, the method of steepest descent is called the saddle-point approximation method. In statistical physics, this approximation is widely used in the thermodynamic limit to evaluate partition functions and free energies.

## Basic idea

The method of steepest descent is a method to approximate a complex integral of the form $I(\lambda )=\int _{C}f(z)e^{\lambda g(z)}\,\mathrm {d} z$ for large $\lambda \rightarrow \infty$ , where $f(z)$ and $g(z)$ are analytic functions of z . Because the integrand is analytic, the contour C can be deformed into a new contour $C'$ without changing the integral. In particular, one seeks a new contour on which the imaginary part, denoted $\Im (\cdot )$ , of $g(z)=\Re [g(z)]+i\,\Im [g(z)]$ is constant ( $\Re (\cdot )$ denotes the real part). Then $I(\lambda )=e^{i\lambda \Im \{g(z)\}}\int _{C'}f(z)e^{\lambda \Re \{g(z)\}}\,\mathrm {d} z,$ and the remaining integral can be approximated with other methods like Laplace's method.

## Etymology

The method is called the method of **steepest descent** because for analytic $g(z)$ , constant phase contours are equivalent to steepest descent contours.

If $g(z)=X(z)+iY(z)$ is an analytic function of $z=x+iy$ , it satisfies the Cauchy–Riemann equations ${\frac {\partial X}{\partial x}}={\frac {\partial Y}{\partial y}}\qquad {\text{and}}\qquad {\frac {\partial X}{\partial y}}=-{\frac {\partial Y}{\partial x}}.$ Then ${\frac {\partial X}{\partial x}}{\frac {\partial Y}{\partial x}}+{\frac {\partial X}{\partial y}}{\frac {\partial Y}{\partial y}}=\nabla X\cdot \nabla Y=0,$ so contours of constant phase are also contours of steepest descent.

## A simple estimate

Let  *f*, *S* : **C***n* → **C** and *C* ⊂ **C***n*. If

$M=\sup _{x\in C}\Re (S(x))<\infty ,$

where $\Re (\cdot )$ denotes the real part, and there exists a positive real number *λ*0 such that

$\int _{C}\left|f(x)e^{\lambda _{0}S(x)}\right|dx<\infty ,$

then the following estimate holds:

$\left|\int _{C}f(x)e^{\lambda S(x)}dx\right|\leqslant {\text{const}}\cdot e^{\lambda M},\qquad \forall \lambda \in \mathbb {R} ,\quad \lambda \geqslant \lambda _{0}.$

Proof of the simple estimate:

${\begin{aligned}\left|\int _{C}f(x)e^{\lambda S(x)}dx\right|&\leqslant \int _{C}|f(x)|\left|e^{\lambda S(x)}\right|dx\\&\equiv \int _{C}|f(x)|e^{\lambda M}\left|e^{\lambda _{0}(S(x)-M)}e^{(\lambda -\lambda _{0})(S(x)-M)}\right|dx\\&\leqslant \int _{C}|f(x)|e^{\lambda M}\left|e^{\lambda _{0}(S(x)-M)}\right|dx&&\left|e^{(\lambda -\lambda _{0})(S(x)-M)}\right|\leqslant 1\\&=\underbrace {e^{-\lambda _{0}M}\int _{C}\left|f(x)e^{\lambda _{0}S(x)}\right|dx} _{\text{const}}\cdot e^{\lambda M}.\end{aligned}}$

## The case of a single non-degenerate saddle point

### Basic notions and notation

Let x be a complex n-dimensional vector, and

$S''{}_{xx}(x)\equiv \left({\frac {\partial ^{2}S(x)}{\partial x_{i}\partial x_{j}}}\right),\qquad 1\leqslant i,\,j\leqslant n,$

denote the Hessian matrix for a function *S*(*x*). If

${\boldsymbol {\varphi }}(x)=(\varphi _{1}(x),\varphi _{2}(x),\ldots ,\varphi _{k}(x))$

is a vector function, then its Jacobian matrix is defined as

${\boldsymbol {\varphi }}_{x}'(x)\equiv \left({\frac {\partial \varphi _{i}(x)}{\partial x_{j}}}\right),\qquad 1\leqslant i\leqslant k,\quad 1\leqslant j\leqslant n.$

A **non-degenerate saddle point**, *z*0 ∈ **C***n*, of a holomorphic function *S*(*z*) is a critical point of the function (i.e., ∇*S*(*z*0) = 0) where the function's Hessian matrix has a non-vanishing determinant (i.e., $\det S''{}_{zz}(z^{0})\neq 0$ ).

The following is the main tool for constructing the asymptotics of integrals in the case of a non-degenerate saddle point:

### Complex Morse lemma

The Morse lemma for real-valued functions generalizes as follows for holomorphic functions: near a non-degenerate saddle point *z*0 of a holomorphic function *S*(*z*), there exist coordinates in terms of which *S*(*z*) − *S*(*z*0) is exactly quadratic. To make this precise, let S be a holomorphic function with domain *W* ⊂ **C***n*, and let *z*0 in W be a non-degenerate saddle point of S, that is, ∇*S*(*z*0) = 0 and $\det S''{}_{zz}(z^{0})\neq 0$ . Then there exist neighborhoods *U* ⊂ *W* of *z*0 and *V* ⊂ **C***n* of *w* = 0, and a bijective holomorphic function ***φ*** : *V* → *U* with ***φ***(0) = *z*0 such that

$\forall w\in V:\qquad S({\boldsymbol {\varphi }}(w))=S(z^{0})+{\frac {1}{2}}\sum _{j=1}^{n}\mu _{j}w_{j}^{2},\quad \det {\boldsymbol {\varphi }}_{w}'(0)=1,$

Here, the *μj* are the eigenvalues of the matrix $S''{}_{zz}(z^{0})$ .

Proof of complex Morse lemma

The following proof is a straightforward generalization of the proof of the real Morse Lemma, which can be found in . We begin by demonstrating

Auxiliary statement.

Let

f

:

C

n

→

C

be

holomorphic

in a neighborhood of the origin and

f

(0) = 0

. Then in some neighborhood, there exist functions

g

i

:

C

n

→

C

such that

$f(z)=\sum _{i=1}^{n}z_{i}g_{i}(z),$

where each

g

i

is

holomorphic

and

$g_{i}(0)=\left.{\tfrac {\partial f(z)}{\partial z_{i}}}\right|_{z=0}.$

From the identity

$f(z)=\int _{0}^{1}{\frac {d}{dt}}f\left(tz_{1},\cdots ,tz_{n}\right)dt=\sum _{i=1}^{n}z_{i}\int _{0}^{1}\left.{\frac {\partial f(z)}{\partial z_{i}}}\right|_{z=(tz_{1},\ldots ,tz_{n})}dt,$

we conclude that

$g_{i}(z)=\int _{0}^{1}\left.{\frac {\partial f(z)}{\partial z_{i}}}\right|_{z=(tz_{1},\ldots ,tz_{n})}dt$

and

$g_{i}(0)=\left.{\frac {\partial f(z)}{\partial z_{i}}}\right|_{z=0}.$

Without loss of generality, we translate the origin to *z*0, such that *z*0 = 0 and *S*(0) = 0. Using the Auxiliary Statement, we have

$S(z)=\sum _{i=1}^{n}z_{i}g_{i}(z).$

Since the origin is a saddle point,

$\left.{\frac {\partial S(z)}{\partial z_{i}}}\right|_{z=0}=g_{i}(0)=0,$

we can also apply the Auxiliary Statement to the functions *gi*(*z*) and obtain

| $S(z)=\sum _{i,j=1}^{n}z_{i}z_{j}h_{ij}(z).$ |   | 1 |
|---|---|---|

Recall that an arbitrary matrix A can be represented as a sum of symmetric *A*(*s*) and anti-symmetric *A*(*a*) matrices,

$A_{ij}=A_{ij}^{(s)}+A_{ij}^{(a)},\qquad A_{ij}^{(s)}={\tfrac {1}{2}}\left(A_{ij}+A_{ji}\right),\qquad A_{ij}^{(a)}={\tfrac {1}{2}}\left(A_{ij}-A_{ji}\right).$

The contraction of any symmetric matrix *B* with an arbitrary matrix A is

| $\sum _{i,j}B_{ij}A_{ij}=\sum _{i,j}B_{ij}A_{ij}^{(s)},$ |   | 2 |
|---|---|---|

i.e., the anti-symmetric component of A does not contribute because

$\sum _{i,j}B_{ij}C_{ij}=\sum _{i,j}B_{ji}C_{ji}=-\sum _{i,j}B_{ij}C_{ij}=0.$

Thus, *hij*(*z*) in equation (1) can be assumed to be symmetric with respect to the interchange of the indices i and j. Note that

$\left.{\frac {\partial ^{2}S(z)}{\partial z_{i}\partial z_{j}}}\right|_{z=0}=2h_{ij}(0);$

hence, det(*hij*(0)) ≠ 0 because the origin is a non-degenerate saddle point.

Let us show by induction that there are local coordinates *u* = (*u*1, ... *un*), *z* = ***ψ***(*u*), 0 = ***ψ***(0), such that

| $S({\boldsymbol {\psi }}(u))=\sum _{i=1}^{n}u_{i}^{2}.$ |   | 3 |
|---|---|---|

First, assume that there exist local coordinates *y* = (*y*1, ... *yn*), *z* = ***φ***(*y*), 0 = ***φ***(0), such that

| $S({\boldsymbol {\phi }}(y))=y_{1}^{2}+\cdots +y_{r-1}^{2}+\sum _{i,j=r}^{n}y_{i}y_{j}H_{ij}(y),$ |   | 4 |
|---|---|---|

where *Hij* is symmetric due to equation (2). By a linear change of the variables (*yr*, ... *yn*), we can assure that *Hrr*(0) ≠ 0. From the chain rule, we have

${\frac {\partial ^{2}S({\boldsymbol {\phi }}(y))}{\partial y_{i}\partial y_{j}}}=\sum _{l,k=1}^{n}\left.{\frac {\partial ^{2}S(z)}{\partial z_{k}\partial z_{l}}}\right|_{z={\boldsymbol {\phi }}(y)}{\frac {\partial \phi _{k}}{\partial y_{i}}}{\frac {\partial \phi _{l}}{\partial y_{j}}}+\sum _{k=1}^{n}\left.{\frac {\partial S(z)}{\partial z_{k}}}\right|_{z={\boldsymbol {\phi }}(y)}{\frac {\partial ^{2}\phi _{k}}{\partial y_{i}\partial y_{j}}}$

Therefore:

$S''{}_{yy}({\boldsymbol {\phi }}(0))={\boldsymbol {\phi }}'_{y}(0)^{T}S''{}_{zz}(0){\boldsymbol {\phi }}'_{y}(0),\qquad \det {\boldsymbol {\phi }}'_{y}(0)\neq 0;$

whence,

$0\neq \det S''{}_{yy}({\boldsymbol {\phi }}(0))=2^{r-1}\det \left(2H_{ij}(0)\right).$

The matrix (*Hij*(0)) can be recast in the Jordan normal form: (*Hij*(0)) = *LJL*−1, were L gives the desired non-singular linear transformation and the diagonal of J contains non-zero eigenvalues of (*Hij*(0)). If *Hij*(0) ≠ 0 then, due to continuity of *Hij*(*y*), it must be also non-vanishing in some neighborhood of the origin. Having introduced ${\tilde {H}}_{ij}(y)=H_{ij}(y)/H_{rr}(y)$ , we write

${\begin{aligned}S({\boldsymbol {\varphi }}(y))=&y_{1}^{2}+\cdots +y_{r-1}^{2}+H_{rr}(y)\sum _{i,j=r}^{n}y_{i}y_{j}{\tilde {H}}_{ij}(y)\\=&y_{1}^{2}+\cdots +y_{r-1}^{2}+H_{rr}(y)\left[y_{r}^{2}+2y_{r}\sum _{j=r+1}^{n}y_{j}{\tilde {H}}_{rj}(y)+\sum _{i,j=r+1}^{n}y_{i}y_{j}{\tilde {H}}_{ij}(y)\right]\\=&y_{1}^{2}+\cdots +y_{r-1}^{2}+H_{rr}(y)\left[\left(y_{r}+\sum _{j=r+1}^{n}y_{j}{\tilde {H}}_{rj}(y)\right)^{2}-\left(\sum _{j=r+1}^{n}y_{j}{\tilde {H}}_{rj}(y)\right)^{2}\right]+H_{rr}(y)\sum _{i,j=r+1}^{n}y_{i}y_{j}{\tilde {H}}_{ij}(y)\end{aligned}}$

Motivated by the last expression, we introduce new coordinates *z* = ***η***(*x*), 0 = ***η***(0),

$x_{r}={\sqrt {H_{rr}(y)}}\left(y_{r}+\sum _{j=r+1}^{n}y_{j}{\tilde {H}}_{rj}(y)\right),\qquad x_{j}=y_{j},\quad \forall j\neq r.$

The change of the variables *y* ↔ *x* is locally invertible since the corresponding Jacobian is non-zero,

$\left.{\frac {\partial x_{r}}{\partial y_{k}}}\right|_{y=0}={\sqrt {H_{rr}(0)}}\left[\delta _{r,\,k}+\sum _{j=r+1}^{n}\delta _{j,\,k}{\tilde {H}}_{jr}(0)\right].$

Therefore,

| $S({\boldsymbol {\eta }}(x))={x}_{1}^{2}+\cdots +{x}_{r}^{2}+\sum _{i,j=r+1}^{n}{x}_{i}{x}_{j}W_{ij}(x).$ |   | 5 |
|---|---|---|

Comparing equations (4) and (5), we conclude that equation (3) is verified. Denoting the eigenvalues of $S''{}_{zz}(0)$ by *μj*, equation (3) can be rewritten as

| $S({\boldsymbol {\varphi }}(w))={\frac {1}{2}}\sum _{j=1}^{n}\mu _{j}w_{j}^{2}.$ |   | 6 |
|---|---|---|

Therefore,

| $S''{}_{ww}({\boldsymbol {\varphi }}(0))={\boldsymbol {\varphi }}'_{w}(0)^{T}S''{}_{zz}(0){\boldsymbol {\varphi }}'_{w}(0),$ |   | 7 |
|---|---|---|

From equation (6), it follows that $\det S''{}_{ww}({\boldsymbol {\varphi }}(0))=\mu _{1}\cdots \mu _{n}$ . The Jordan normal form of $S''{}_{zz}(0)$ reads $S''{}_{zz}(0)=PJ_{z}P^{-1}$ , where *Jz* is an upper diagonal matrix containing the eigenvalues and det *P* ≠ 0; hence, $\det S''{}_{zz}(0)=\mu _{1}\cdots \mu _{n}$ . We obtain from equation (7)

$\det S''{}_{ww}({\boldsymbol {\varphi }}(0))=\left[\det {\boldsymbol {\varphi }}'_{w}(0)\right]^{2}\det S''{}_{zz}(0)\Longrightarrow \det {\boldsymbol {\varphi }}'_{w}(0)=\pm 1.$

If $\det {\boldsymbol {\varphi }}'_{w}(0)=-1$ , then interchanging two variables assures that $\det {\boldsymbol {\varphi }}'_{w}(0)=+1$ .

### The asymptotic expansion in the case of a single non-degenerate saddle point

Assume

1. *f* (*z*) and *S*(*z*) are holomorphic functions in an open, bounded, and simply connected set Ω*x* ⊂ **C***n* such that the *Ix* = Ω*x* ∩ **R***n* is connected;
2. $\Re (S(z))$ has a single maximum: $\max _{z\in I_{x}}\Re (S(z))=\Re (S(x^{0}))$ for exactly one point *x*0 ∈ *Ix*;
3. *x*0 is a non-degenerate saddle point (i.e., ∇*S*(*x*0) = 0 and $\det S''{}_{xx}(x^{0})\neq 0$ ).

Then, the following asymptotic holds

| $I(\lambda )\equiv \int _{I_{x}}f(x)e^{\lambda S(x)}dx=\left({\frac {2\pi }{\lambda }}\right)^{\frac {n}{2}}e^{\lambda S(x^{0})}\left(f(x^{0})+O\left(\lambda ^{-1}\right)\right)\prod _{j=1}^{n}(-\mu _{j})^{-{\frac {1}{2}}},\qquad \lambda \to \infty ,$ |   | 8 |
|---|---|---|

where *μj* are eigenvalues of the Hessian $S''{}_{xx}(x^{0})$ and $(-\mu _{j})^{-{\frac {1}{2}}}$ are defined with arguments

| $\left\|\arg {\sqrt {-\mu _{j}}}\right\|<{\tfrac {\pi }{4}}.$ |   | 9 |
|---|---|---|

This statement is a special case of more general results presented in Fedoryuk (1987).

Derivation of equation (8)

First, we deform the contour *Ix* into a new contour $I'_{x}\subset \Omega _{x}$ passing through the saddle point *x*0 and sharing the boundary with *Ix*. This deformation does not change the value of the integral *I*(*λ*). We employ the Complex Morse Lemma to change the variables of integration. According to the lemma, the function ***φ***(*w*) maps a neighborhood *x*0 ∈ *U* ⊂ Ω*x* onto a neighborhood Ω*w* containing the origin. The integral *I*(*λ*) can be split into two: *I*(*λ*) = *I*0(*λ*) + *I*1(*λ*), where *I*0(*λ*) is the integral over $U\cap I'_{x}$ , while *I*1(*λ*) is over $I'_{x}\setminus (U\cap I'_{x})$ (i.e., the remaining part of the contour *I′x*). Since the latter region does not contain the saddle point *x*0, the value of *I*1(*λ*) is exponentially smaller than *I*0(*λ*) as *λ* → ∞; thus, *I*1(*λ*) is ignored. Introducing the contour *Iw* such that $U\cap I'_{x}={\boldsymbol {\varphi }}(I_{w})$ , we have

| $I_{0}(\lambda )=e^{\lambda S(x^{0})}\int _{I_{w}}f[{\boldsymbol {\varphi }}(w)]\exp \left(\lambda \sum _{j=1}^{n}{\tfrac {\mu _{j}}{2}}w_{j}^{2}\right)\left\|\det {\boldsymbol {\varphi }}_{w}'(w)\right\|dw.$ |   | 10 |
|---|---|---|

Recalling that *x*0 = ***φ***(0) as well as $\det {\boldsymbol {\varphi }}_{w}'(0)=1$ , we expand the pre-exponential function $f[{\boldsymbol {\varphi }}(w)]$ into a Taylor series and keep just the leading zero-order term

| $I_{0}(\lambda )\approx f(x^{0})e^{\lambda S(x^{0})}\int _{\mathbf {R} ^{n}}\exp \left(\lambda \sum _{j=1}^{n}{\tfrac {\mu _{j}}{2}}w_{j}^{2}\right)dw=f(x^{0})e^{\lambda S(x^{0})}\prod _{j=1}^{n}\int _{-\infty }^{\infty }e^{{\frac {1}{2}}\lambda \mu _{j}y^{2}}dy.$ |   | 11 |
|---|---|---|

Here, we have substituted the integration region *Iw* by **R***n* because both contain the origin, which is a saddle point, hence they are equal up to an exponentially small term. The integrals in the r.h.s. of equation (11) can be expressed as

| ${\mathcal {I}}_{j}=\int _{-\infty }^{\infty }e^{{\frac {1}{2}}\lambda \mu _{j}y^{2}}dy=2\int _{0}^{\infty }e^{-{\frac {1}{2}}\lambda \left({\sqrt {-\mu _{j}}}y\right)^{2}}dy=2\int _{0}^{\infty }e^{-{\frac {1}{2}}\lambda \left\|{\sqrt {-\mu _{j}}}\right\|^{2}y^{2}\exp \left(2i\arg {\sqrt {-\mu _{j}}}\right)}dy.$ |   | 12 |
|---|---|---|

From this representation, we conclude that condition (9) must be satisfied in order for the r.h.s. and l.h.s. of equation (12) to coincide. According to assumption 2, $\Re \left(S''{}_{xx}(x^{0})\right)$ is a negatively defined quadratic form (viz., $\Re (\mu _{j})<0$ ) implying the existence of the integral ${\mathcal {I}}_{j}$ , which is readily calculated

${\mathcal {I}}_{j}={\frac {2}{{\sqrt {-\mu _{j}}}{\sqrt {\lambda }}}}\int _{0}^{\infty }e^{-{\frac {\xi ^{2}}{2}}}d\xi ={\sqrt {\frac {2\pi }{\lambda }}}(-\mu _{j})^{-{\frac {1}{2}}}.$

Equation (8) can also be written as

| $I(\lambda )=\left({\frac {2\pi }{\lambda }}\right)^{\frac {n}{2}}e^{\lambda S(x^{0})}\left(\det(-S''{}_{xx}(x^{0}))\right)^{-{\frac {1}{2}}}\left(f(x^{0})+O\left(\lambda ^{-1}\right)\right),$ |   | 13 |
|---|---|---|

where the branch of

${\sqrt {\det \left(-S''{}_{xx}(x^{0})\right)}}$

is selected as follows

${\begin{aligned}\left(\det \left(-S''{}_{xx}(x^{0})\right)\right)^{-{\frac {1}{2}}}&=\exp \left(-i{\text{ Ind}}\left(-S''{}_{xx}(x^{0})\right)\right)\prod _{j=1}^{n}\left|\mu _{j}\right|^{-{\frac {1}{2}}},\\{\text{Ind}}\left(-S''{}_{xx}(x^{0})\right)&={\tfrac {1}{2}}\sum _{j=1}^{n}\arg(-\mu _{j}),&&|\arg(-\mu _{j})|<{\tfrac {\pi }{2}}.\end{aligned}}$

Consider important special cases:

- If *S*(*x*) is real valued for real x and *x*0 in **R***n* (aka, the **multidimensional Laplace method**), then ${\text{Ind}}\left(-S''{}_{xx}(x^{0})\right)=0.$
- If *S*(*x*) is purely imaginary for real x (i.e., $\Re (S(x))=0$ for all x in **R***n*) and *x*0 in **R***n* (aka, the **multidimensional stationary phase method**), then ${\text{Ind}}\left(-S''{}_{xx}(x^{0})\right)={\frac {\pi }{4}}{\text{sign }}S''{}_{xx}(x_{0}),$ where ${\text{sign }}S''{}_{xx}(x_{0})$ denotes the signature of matrix $S''{}_{xx}(x_{0})$ , which equals to the number of negative eigenvalues minus the number of positive ones. It is noteworthy that in applications of the stationary phase method to the multidimensional WKB approximation in quantum mechanics (as well as in optics), Ind is related to the Maslov index see, e.g., Chaichian & Demichev (2001) and Schulman (2005).

## The case of multiple non-degenerate saddle points

If the function *S*(*x*) has multiple isolated non-degenerate saddle points, i.e.,

$\nabla S\left(x^{(k)}\right)=0,\quad \det S''{}_{xx}\left(x^{(k)}\right)\neq 0,\quad x^{(k)}\in \Omega _{x}^{(k)},$

where

$\left\{\Omega _{x}^{(k)}\right\}_{k=1}^{K}$

is an open cover of Ω*x*, then the calculation of the integral asymptotic is reduced to the case of a single saddle point by employing the partition of unity. The partition of unity allows us to construct a set of continuous functions *ρk*(*x*) : Ω*x* → [0, 1], 1 ≤ *k* ≤ *K*, such that

${\begin{aligned}\sum _{k=1}^{K}\rho _{k}(x)&=1,&&\forall x\in \Omega _{x},\\\rho _{k}(x)&=0&&\forall x\in \Omega _{x}\setminus \Omega _{x}^{(k)}.\end{aligned}}$

Whence,

$\int _{I_{x}\subset \Omega _{x}}f(x)e^{\lambda S(x)}dx\equiv \sum _{k=1}^{K}\int _{I_{x}\subset \Omega _{x}}\rho _{k}(x)f(x)e^{\lambda S(x)}dx.$

Therefore as *λ* → ∞ we have:

$\sum _{k=1}^{K}\int _{{\text{a neighborhood of }}x^{(k)}}f(x)e^{\lambda S(x)}dx=\left({\frac {2\pi }{\lambda }}\right)^{\frac {n}{2}}\sum _{k=1}^{K}e^{\lambda S\left(x^{(k)}\right)}\left(\det \left(-S''{}_{xx}\left(x^{(k)}\right)\right)\right)^{-{\frac {1}{2}}}f\left(x^{(k)}\right),$

where equation (13) was utilized at the last stage, and the pre-exponential function  *f* (*x*) at least must be continuous.

## The other cases

When ∇*S*(*z*0) = 0 and $\det S''{}_{zz}(z^{0})=0$ , the point *z*0 ∈ **C***n* is called a **degenerate saddle point** of a function *S*(*z*).

Calculating the asymptotic of

$\int f(x)e^{\lambda S(x)}dx,$

when *λ* → ∞,  *f* (*x*) is continuous, and *S*(*z*) has a degenerate saddle point, is a very rich problem, whose solution heavily relies on the catastrophe theory. Here, the catastrophe theory replaces the Morse lemma, valid only in the non-degenerate case, to transform the function *S*(*z*) into one of the multitude of canonical representations. For further details see, e.g., Poston & Stewart (1978) and Fedoryuk (1987).

Integrals with degenerate saddle points naturally appear in many applications including optical caustics and the multidimensional WKB approximation in quantum mechanics.

The other cases such as, e.g.,  *f* (*x*) and/or *S*(*x*) are discontinuous or when an extremum of *S*(*x*) lies at the integration region's boundary, require special care (see, e.g., Fedoryuk (1987) and Wong (1989)).

## Extensions and generalizations

An extension of the steepest descent method is the so-called *nonlinear stationary phase/steepest descent method*. Here, instead of integrals, one needs to evaluate asymptotically solutions of Riemann–Hilbert factorization problems.

Given a contour *C* in the complex sphere, a function *f* defined on that contour and a special point, say infinity, one seeks a function *M* holomorphic away from the contour *C*, with prescribed jump across *C*, and with a given normalization at infinity. If *f* and hence *M* are matrices rather than scalars this is a problem that in general does not admit an explicit solution.

An asymptotic evaluation is then possible along the lines of the linear stationary phase/steepest descent method. The idea is to reduce asymptotically the solution of the given Riemann–Hilbert problem to that of a simpler, explicitly solvable, Riemann–Hilbert problem. Cauchy's theorem is used to justify deformations of the jump contour.

The nonlinear stationary phase was introduced by Deift and Zhou in 1993, based on earlier work of the Russian mathematician Alexander Its. A (properly speaking) nonlinear steepest descent method was introduced by Kamvissis, K. McLaughlin and P. Miller in 2003, based on previous work of Lax, Levermore, Deift, Venakides and Zhou. As in the linear case, steepest descent contours solve a min-max problem. In the nonlinear case they turn out to be "S-curves" (defined in a different context back in the 80s by Stahl, Gonchar and Rakhmanov).

The nonlinear stationary phase/steepest descent method has applications to the theory of soliton equations and integrable models, random matrices and combinatorics.

Another extension is the Method of Chester–Friedman–Ursell for coalescing saddle points and uniform asymptotic extensions.
