---
title: "Separation of variables"
source: https://en.wikipedia.org/wiki/Separation_of_variables
domain: partial-differential-equations
license: CC-BY-SA-4.0
tags: partial differential equation, heat equation, wave equation, method of characteristics
fetched: 2026-07-02
---

# Separation of variables

In mathematics, **separation of variables** (also known as the **Fourier method**) is any of several methods for solving ordinary and partial differential equations, in which algebra allows one to rewrite an equation so that each of two variables occurs on a different side of the equation.

## Ordinary differential equations (ODE)

A differential equation for the unknown $f(x)$ is separable if it can be written in the form

${\frac {d}{dx}}f(x)=g(x)h(f(x))$

where g and h are given functions. This is perhaps more transparent when written using $y=f(x)$ as:

${\frac {dy}{dx}}=g(x)h(y).$

So now as long as *h*(*y*) ≠ 0, we can rearrange terms to obtain:

${dy \over h(y)}=g(x)\,dx,$

where the two variables *x* and *y* have been separated. Note *dx* (and *dy*) can be viewed, at a simple level, as just a convenient notation, which provides a handy mnemonic aid for assisting with manipulations. A formal definition of *dx* as a differential (infinitesimal) is somewhat advanced.

### Alternative notation

Those who dislike differentials as separate entities may prefer to write this as

${\frac {1}{h(y)}}{\frac {dy}{dx}}=g(x),$

but that fails to make it quite as obvious why this is called "separation of variables". Integrating both sides of the equation with respect to x , we have

| $\int {\frac {1}{h(y)}}{\frac {dy}{dx}}\,dx=\int g(x)\,dx,$ |   | A1 |
|---|---|---|

or equivalently,

$\int {\frac {1}{h(y)}}\,dy=\int g(x)\,dx$

because of the substitution rule for integrals.

If one can evaluate the two integrals, one can find a solution to the differential equation. Observe that this process effectively allows us to treat the derivative ${\frac {dy}{dx}}$ as a fraction which can be separated. This allows us to solve separable differential equations more conveniently, as demonstrated in the example below.

(Note that we do not need to use two constants of integration, in equation (**A1**) as in

$\int {\frac {1}{h(y)}}\,dy+C_{1}=\int g(x)\,dx+C_{2},$

because a single constant $C=C_{2}-C_{1}$ is equivalent.)

### Example

Population growth is often modeled by the "logistic" differential equation

${\frac {dP}{dt}}=kP\left(1-{\frac {P}{K}}\right)$

where P is the population with respect to time t , k is the rate of growth, and K is the carrying capacity of the environment. Separation of variables now leads to

${\begin{aligned}&\int {\frac {dP}{P\left(1-P/K\right)}}=\int k\,dt\end{aligned}}$

which is readily integrated using partial fractions on the left side yielding

$P(t)={\frac {K}{1+Ae^{-kt}}}$

where A is the constant of integration. We can find A in terms of $P\left(0\right)=P_{0}$ at t=0. Noting $e^{0}=1$ we get

$A={\frac {K-P_{0}}{P_{0}}}.$

### Generalization of separable ODEs to the nth order

Much like one can speak of a separable first-order ODE, one can speak of a separable second-order, third-order or *n*th-order ODE. Consider the separable first-order ODE:

${\frac {dy}{dx}}=f(y)g(x)$

The derivative can alternatively be written the following way to underscore that it is an operator working on the unknown function, *y*:

${\frac {dy}{dx}}={\frac {d}{dx}}(y)$

Thus, when one separates variables for first-order equations, one in fact moves the *dx* denominator of the operator to the side with the *x* variable, and the *d*(*y*) is left on the side with the *y* variable. The second-derivative operator, by analogy, breaks down as follows:

${\frac {d^{2}y}{dx^{2}}}={\frac {d}{dx}}\left({\frac {dy}{dx}}\right)={\frac {d}{dx}}\left({\frac {d}{dx}}(y)\right)$

The third-, fourth- and *n*th-derivative operators break down in the same way. Thus, much like a first-order separable ODE is reducible to the form

${\frac {dy}{dx}}=f(y)g(x)$

a separable second-order ODE is reducible to the form

${\frac {d^{2}y}{dx^{2}}}=f\left(y'\right)g(x)$

and an nth-order separable ODE is reducible to

${\frac {d^{n}y}{dx^{n}}}=f\!\left(y^{(n-1)}\right)g(x)$

### Example

Consider the simple nonlinear second-order differential equation: $y''=(y')^{2}.$ This equation is an equation only of *y''* and *y'*, meaning it is reducible to the general form described above and is, therefore, separable. Since it is a second-order separable equation, collect all *x* variables on one side and all *y'* variables on the other to get: ${\frac {d(y')}{(y')^{2}}}=dx.$ Now, integrate the right side with respect to *x* and the left with respect to *y'*: $\int {\frac {d(y')}{(y')^{2}}}=\int dx.$ This gives $-{\frac {1}{y'}}=x+C_{1},$ which simplifies to: $y'=-{\frac {1}{x+C_{1}}}~.$ This is now a simple integral problem that gives the final answer: $y=C_{2}-\ln |x+C_{1}|.$

## Partial differential equations

The method of separation of variables is also used to solve a wide range of linear partial differential equations with boundary and initial conditions, such as the heat equation, wave equation, Laplace equation, Helmholtz equation and biharmonic equation.

The analytical method of separation of variables for solving partial differential equations has also been generalized into a computational method of decomposition in invariant structures that can be used to solve systems of partial differential equations.

### Example: homogeneous case

Consider the one-dimensional heat equation. The equation is

| ${\frac {\partial u}{\partial t}}-\alpha {\frac {\partial ^{2}u}{\partial x^{2}}}=0$ |   | 1 |
|---|---|---|

The variable *u* denotes temperature. The boundary condition is homogeneous, that is

| $u{\big \|}_{x=0}=u{\big \|}_{x=L}=0$ |   | 2 |
|---|---|---|

Let us attempt to find a nontrivial solution satisfying the boundary conditions but with the following property: *u* is a product in which the dependence of *u* on *x*, *t* is separated, that is:

| $u(x,t)=X(x)T(t).$ |   | 3 |
|---|---|---|

Substituting *u* back into equation (**1**) and using the product rule,

| ${\frac {T'(t)}{\alpha T(t)}}={\frac {X''(x)}{X(x)}}=-\lambda ,$ |   | 4 |
|---|---|---|

where *λ* must be constant since the right hand side depends only on *x* and the left hand side only on *t*. Thus:

| $T'(t)=-\lambda \alpha T(t),$ |   | 5 |
|---|---|---|

and

| $X''(x)=-\lambda X(x).$ |   | 6 |
|---|---|---|

−*λ* here is the eigenvalue for both differential operators, and *T*(*t*) and *X*(*x*) are corresponding eigenfunctions.

We will now show that solutions for *X*(*x*) for values of *λ* ≤ 0 cannot occur:

Suppose that *λ* < 0. Then there exist real numbers *B*, *C* such that

$X(x)=Be^{{\sqrt {-\lambda }}\,x}+Ce^{-{\sqrt {-\lambda }}\,x}.$

From (**2**) we get

| $X(0)=0=X(L),$ |   | 7 |
|---|---|---|

and therefore *B* = 0 = *C* which implies *u* is identically 0.

Suppose that *λ* = 0. Then there exist real numbers *B*, *C* such that

$X(x)=Bx+C.$

From (**7**) we conclude in the same manner as in 1 that *u* is identically 0.

Therefore, it must be the case that *λ* > 0. Then there exist real numbers *A*, *B*, *C* such that

$T(t)=Ae^{-\lambda \alpha t},$

and

$X(x)=B\sin({\sqrt {\lambda }}\,x)+C\cos({\sqrt {\lambda }}\,x).$

From (**7**) we get *C* = 0 and that for some positive integer *n*,

${\sqrt {\lambda }}=n{\frac {\pi }{L}}.$

This solves the heat equation in the special case that the dependence of *u* has the special form of (**3**).

In general, the sum of solutions to (**1**) which satisfy the boundary conditions (**2**) also satisfies (**1**) and (**3**). Hence a complete solution can be given as

$u(x,t)=\sum _{n=1}^{\infty }D_{n}\sin {\frac {n\pi x}{L}}\exp \left(-{\frac {n^{2}\pi ^{2}\alpha t}{L^{2}}}\right),$

where *D**n* are coefficients determined by initial condition.

Given the initial condition

| $u{\big \|}_{t=0}=f(x),$ |   | 8 |
|---|---|---|

we can get

$f(x)=\sum _{n=1}^{\infty }D_{n}\sin {\frac {n\pi x}{L}}.$

This is the Fourier sine series expansion of *f*(*x*) which is amenable to Fourier analysis. Multiplying both sides with ${\textstyle \sin {\frac {n\pi x}{L}}}$ and integrating over [0, *L*] results in

$D_{n}={\frac {2}{L}}\int _{0}^{L}f(x)\sin {\frac {n\pi x}{L}}\,dx.$

This method requires that the eigenfunctions *X*, here ${\textstyle \left\{\sin {\frac {n\pi x}{L}}\right\}_{n=1}^{\infty }}$ , are orthogonal and complete. In general this is guaranteed by Sturm–Liouville theory.

### Example: nonhomogeneous case

Suppose the equation is nonhomogeneous,

| ${\frac {\partial u}{\partial t}}-\alpha {\frac {\partial ^{2}u}{\partial x^{2}}}=h(x,t)$ |   | 8 |
|---|---|---|

with the boundary condition the same as (**2**) and initial condition same as (**8**).

Expand *h*(*x,t*), *u*(*x*,*t*) and *f*(*x*) into

| $h(x,t)=\sum _{n=1}^{\infty }h_{n}(t)\sin {\frac {n\pi x}{L}},$ |   | 9 |
|---|---|---|

| $u(x,t)=\sum _{n=1}^{\infty }u_{n}(t)\sin {\frac {n\pi x}{L}},$ |   | 10 |
|---|---|---|

| $f(x)=\sum _{n=1}^{\infty }b_{n}\sin {\frac {n\pi x}{L}},$ |   | 11 |
|---|---|---|

where *h**n*(*t*) and *b**n* can be calculated by integration, while *u**n*(*t*) is to be determined.

Substitute (**9**) and (**10**) back to (**8**) and considering the orthogonality of sine functions we get

$u'_{n}(t)+\alpha {\frac {n^{2}\pi ^{2}}{L^{2}}}u_{n}(t)=h_{n}(t),$

which are a sequence of linear differential equations that can be readily solved with, for instance, Laplace transform, or Integrating factor. Finally, we can get

$u_{n}(t)=e^{-\alpha {\frac {n^{2}\pi ^{2}}{L^{2}}}t}\left(b_{n}+\int _{0}^{t}h_{n}(s)e^{\alpha {\frac {n^{2}\pi ^{2}}{L^{2}}}s}\,ds\right).$

If the boundary condition is nonhomogeneous, then the expansion of (**9**) and (**10**) is no longer valid. One has to find a function *v* that satisfies the boundary condition only, and subtract it from *u*. The function *u-v* then satisfies homogeneous boundary condition, and can be solved with the above method.

### Example: mixed derivatives

For some equations involving mixed derivatives, the equation does not separate as easily as the heat equation did in the first example above, but nonetheless separation of variables may still be applied. Consider the two-dimensional biharmonic equation

${\frac {\partial ^{4}u}{\partial x^{4}}}+2{\frac {\partial ^{4}u}{\partial x^{2}\partial y^{2}}}+{\frac {\partial ^{4}u}{\partial y^{4}}}=0.$

Proceeding in the usual manner, we look for solutions of the form

$u(x,y)=X(x)Y(y)$

and we obtain the equation

${\frac {X^{(4)}(x)}{X(x)}}+2{\frac {X''(x)}{X(x)}}{\frac {Y''(y)}{Y(y)}}+{\frac {Y^{(4)}(y)}{Y(y)}}=0.$

Writing this equation in the form

$E(x)+F(x)G(y)+H(y)=0,$

Taking the derivative of this expression with respect to x gives $E'(x)+F'(x)G(y)=0$ which means $G(y)=const.$ or $F'(x)=0$ and likewise, taking derivative with respect to y leads to $F(x)G'(y)+H'(y)=0$ and thus $F(x)=const.$ or $G'(y)=0$ , hence either *F*(*x*) or *G*(*y*) must be a constant, say −λ. This further implies that either $-E(x)=F(x)G(y)+H(y)$ or $-H(y)=E(x)+F(x)G(y)$ are constant. Returning to the equation for *X* and *Y*, we have two cases

${\begin{aligned}X''(x)&=-\lambda _{1}X(x)\\X^{(4)}(x)&=\mu _{1}X(x)\\Y^{(4)}(y)-2\lambda _{1}Y''(y)&=-\mu _{1}Y(y)\end{aligned}}$

and

${\begin{aligned}Y''(y)&=-\lambda _{2}Y(y)\\Y^{(4)}(y)&=\mu _{2}Y(y)\\X^{(4)}(x)-2\lambda _{2}X''(x)&=-\mu _{2}X(x)\end{aligned}}$

which can each be solved by considering the separate cases for $\lambda _{i}<0,\lambda _{i}=0,\lambda _{i}>0$ and noting that $\mu _{i}=\lambda _{i}^{2}$ .

### Curvilinear coordinates

In orthogonal curvilinear coordinates, separation of variables can still be used, but in some details different from that in Cartesian coordinates. For instance, regularity or periodic condition may determine the eigenvalues in place of boundary conditions. See spherical harmonics for example.

## Applicability

### Partial differential equations

For many PDEs, such as the wave equation, Helmholtz equation and Schrödinger equation, the applicability of separation of variables is a result of the spectral theorem. In some cases, separation of variables may not be possible. Separation of variables may be possible in some coordinate systems but not others, and which coordinate systems allow for separation depends on the symmetry properties of the equation. Below is an outline of an argument demonstrating the applicability of the method to certain linear equations, although the precise method may differ in individual cases (for instance in the biharmonic equation above).

Consider an initial boundary value problem for a function $u(x,t)$ on $D=\{(x,t):x\in [0,l],t\geq 0\}$ in two variables:

$(Tu)(x,t)=(Su)(x,t)$

where T is a differential operator with respect to x and S is a differential operator with respect to t with boundary data:

$(Tu)(0,t)=(Tu)(l,t)=0$

for

$t\geq 0$

$(Su)(x,0)=h(x)$

for

$0\leq x\leq l$

where h is a known function.

We look for solutions of the form $u(x,t)=f(x)g(t)$ . Dividing the PDE through by $f(x)g(t)$ gives

${\frac {Tf}{f}}={\frac {Sg}{g}}$

The right hand side depends only on x and the left hand side only on t so both must be equal to a constant K , which gives two ordinary differential equations

$Tf=Kf,Sg=Kg$

which we can recognize as eigenvalue problems for the operators for T and S . If T is a compact, self-adjoint operator on the space $L^{2}[0,l]$ along with the relevant boundary conditions, then by the Spectral theorem there exists a basis for $L^{2}[0,l]$ consisting of eigenfunctions for T . Let the spectrum of T be E and let $f_{\lambda }$ be an eigenfunction with eigenvalue $\lambda \in E$ . Then for any function which at each time t is square-integrable with respect to x , we can write this function as a linear combination of the $f_{\lambda }$ . In particular, we know the solution u can be written as

$u(x,t)=\sum _{\lambda \in E}c_{\lambda }(t)f_{\lambda }(x)$

For some functions $c_{\lambda }(t)$ . In the separation of variables, these functions are given by solutions to $Sg=Kg$

Hence, the spectral theorem ensures that the separation of variables will (when it is possible) find all the solutions.

For many differential operators, such as ${\frac {d^{2}}{dx^{2}}}$ , we can show that they are self-adjoint by integration by parts. While these operators may not be compact, their inverses (when they exist) may be, as in the case of the wave equation, and these inverses have the same eigenfunctions and eigenvalues as the original operator (with the possible exception of zero).

## Matrices

The matrix form of the separation of variables is the Kronecker sum.

As an example we consider the 2D discrete Laplacian on a regular grid:

$L=\mathbf {D_{xx}} \oplus \mathbf {D_{yy}} =\mathbf {D_{xx}} \otimes \mathbf {I} +\mathbf {I} \otimes \mathbf {D_{yy}} ,\,$

where $\mathbf {D_{xx}}$ and $\mathbf {D_{yy}}$ are 1D discrete Laplacians in the *x*- and *y*-directions, correspondingly, and $\mathbf {I}$ are the identities of appropriate sizes. See the main article Kronecker sum of discrete Laplacians for details.

## Software

Some mathematical programs are able to do separation of variables: Xcas among others.
