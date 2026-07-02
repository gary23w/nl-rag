---
title: "Sturm–Liouville theory"
source: https://en.wikipedia.org/wiki/Sturm%E2%80%93Liouville_theory
domain: sturm-liouville-theory
license: CC-BY-SA-4.0
tags: sturm-liouville theory, eigenfunction expansion, oscillation theory, rayleigh quotient
fetched: 2026-07-02
---

# Sturm–Liouville theory

In mathematics and its applications, a **Sturm–Liouville problem** is a second-order linear ordinary differential equation of the form ${\frac {\mathrm {d} }{\mathrm {d} x}}\left[p(x){\frac {\mathrm {d} y}{\mathrm {d} x}}\right]+q(x)y=-\lambda w(x)y$ for given functions $p(x)$ , $q(x)$ and $w(x)$ , together with some boundary conditions at extreme values of x . The goals of a given Sturm–Liouville problem are:

- To find the $\lambda$ for which there exists a non-trivial solution to the problem. Such values $\lambda$ are called the *eigenvalues* of the problem.
- For each eigenvalue $\lambda$ , to find the corresponding solution $y=y(x)$ of the problem. Such functions y are called the *eigenfunctions* associated to each $\lambda$ .

**Sturm–Liouville theory** is the general study of Sturm–Liouville problems. In particular, for a "regular" Sturm–Liouville problem, it can be shown that there are an infinite number of eigenvalues each with a unique eigenfunction, and that these eigenfunctions form an orthonormal basis of a certain Hilbert space of functions.

This theory is important in applied mathematics, where Sturm–Liouville problems occur very frequently, particularly when dealing with separable linear partial differential equations. For example, in quantum mechanics, the one-dimensional time-independent Schrödinger equation is a Sturm–Liouville problem.

Sturm–Liouville theory is named after Jacques Charles François Sturm (1803–1855) and Joseph Liouville (1809–1882), who developed the theory.

## Main results

The main results in Sturm–Liouville theory apply to a Sturm–Liouville problem

| ${\frac {\mathrm {d} }{\mathrm {d} x}}\left[p(x){\frac {\mathrm {d} y}{\mathrm {d} x}}\right]+q(x)y=-\lambda \,w(x)y$ |   | 1 |
|---|---|---|

on a finite interval $[a,b]$ that is "regular". The problem is said to be *regular* if:

- the coefficient functions $p,q,w$ and the derivative $p'$ are all continuous on $[a,b]$ ;
- $p(x)>0$ and $w(x)>0$ for all $x\in [a,b]$ ;
- the problem has separated boundary conditions of the form

| ${\begin{cases}\alpha _{1}y(a)+\alpha _{2}y'(a)&=0,\qquad \alpha _{1},\alpha _{2}{\text{ not both }}0,\\\beta _{1}y(b)+\beta _{2}y'(b)&=0,\qquad \beta _{1},\beta _{2}{\text{ not both }}0.\end{cases}}$ |   | 2 |
|---|---|---|

The function $w=w(x)$ , sometimes denoted $r=r(x)$ , is called the *weight* or *density* function.

The goals of a Sturm–Liouville problem are:

- to find the eigenvalues: those λ for which there exists a non-trivial solution;
- for each eigenvalue λ, to find the corresponding eigenfunction $y=y(x)$ .

For a regular Sturm–Liouville problem, a function $y=y(x)$ is called a *solution* if it is continuously differentiable and satisfies the equation (**1**) at every $x\in (a,b)$ . In the case of more general $p,q,w$ , the solutions must be understood in a weak sense.

The terms eigenvalue and eigenvector are used because the solutions correspond to the eigenvalues and eigenfunctions of a Hermitian differential operator in an appropriate Hilbert space of functions with inner product defined using the weight function. Sturm–Liouville theory studies the existence and asymptotic behavior of the eigenvalues, the corresponding qualitative theory of the eigenfunctions and their completeness in the function space.

The main result of Sturm–Liouville theory states that, for any regular Sturm–Liouville problem:

- The eigenvalues $\lambda _{1},\lambda _{2},\dots$ are real and can be numbered so that $\lambda _{1}<\lambda _{2}<\cdots <\lambda _{n}<\cdots \to \infty .$
- Corresponding to each eigenvalue $\lambda _{n}$ is a unique eigenfunction $y_{n}=y_{n}(x)$ (up to constant multiple), called the nth *fundamental solution*.
- The normalized eigenfunctions $y_{n}$ form an orthonormal basis under the *w*-weighted inner product in the Hilbert space $L^{2}{\big (}[a,b],w(x)\,\mathrm {d} x{\big )}$ ; that is, $\langle y_{n},y_{m}\rangle =\int _{a}^{b}y_{n}(x)y_{m}(x)w(x)\,\mathrm {d} x=\delta _{nm},$ where $\delta _{nm}$ is the Kronecker delta. Each linear combination of the eigenfunctions are uniformly convergent in the domain $[a,b]$ and term by term differentiation is allowed.

### Comparison Theorems

Some classical results may be established about the oscillation and non-oscillation properties of solutions to certain Sturm-Liouville problems. In particular these establish that linearly independent solutions oscillate "equally rapidly" and the conditions under which solutions oscillate more rapidly.

Consider the Sturm–Liouville problem:

${\frac {\mathrm {d} }{\mathrm {d} x}}\left[p(x){\frac {\mathrm {d} y}{\mathrm {d} x}}\right]-q(x)y=0$

It can be shown that there are no non-trivial solutions to the above equation which have infinitely many zeros on some closed interval ${\textstyle (a,b)}$ . A proof of this result would look something like as follows:

> Suppose - for contradiction - that such a non-trivial solution ${\textstyle u}$ existed, then the set ${\textstyle \{x\in (a,b):u(x)=0\}}$ is infinite. The Bolzano-Weierstrass Theorem tells us that this set has some limit point ${\textstyle c\in [a,b]}$ , ${\textstyle u}$ is a continuous function we have ${\textstyle u(c)=0}$ . By The Mean Value Theorem we have that for all ${\textstyle h>0}$ there exists some ${\textstyle \theta \in [0,1)}$ for which ${\textstyle u(c+h)=u(c)+hu'(c+\theta h)}$ and as ${\textstyle c}$ is a limit point of a sequence of zeros, there's some ${\textstyle h}$ for which ${\textstyle u(c+h)=0}$ and hence for which ${\textstyle u'(c+\theta h)=0}$ . Applying the continuity of ${\textstyle u(x)}$ gives us that ${\textstyle u'(c)=0}$ , from which we obtain that ${\textstyle u(x)=0}$ everywhere.

**Sturm's Separation Theorem**: If ${\textstyle y_{1},y_{2}}$ are linearly independent solutions to the differential equation, and if ${\textstyle y_{1}}$ has two consecutive zeros at ${\textstyle x_{1}}$ and ${\textstyle x_{2}}$ , then ${\textstyle y_{2}}$ equals zero somewhere on the open interval ${\textstyle (x_{1},x_{2})}$ . Informally this means that the zeros of each linearly independent solution fall between the zeros of the other solution.

**Sturm's Fundamental Theorem**: Suppose that ${\textstyle u}$ is a solution of

${\textstyle {\frac {\mathrm {d} }{\mathrm {d} x}}\left[p(x)u'\right]-q_{1}(x)u=0,}$

and ${\textstyle v}$ is a solution of

${\textstyle {\frac {\mathrm {d} }{\mathrm {d} x}}\left[p(x)v'\right]-q_{2}(x)v=0,}$

where ${\textstyle q_{1}(x)>q_{2}(x)}$ . If ${\textstyle x_{1},x_{2}}$ are two consecutive zeros of ${\textstyle u}$ , then ${\textstyle v}$ is zero somewhere on the interval ${\textstyle (x_{1},x_{2})}$ . *In particular if ${\textstyle v}$* is zero whenever ${\textstyle u}$ is zero, v oscillates more rapidly than ${\textstyle u}$ .

## Reduction to Sturm–Liouville form

The differential equation (**1**) is said to be in **Sturm–Liouville form** or **self-adjoint form**. All second-order linear homogenous ordinary differential equations can be recast in the form on the left-hand side of (**1**) by multiplying both sides of the equation by an appropriate integrating factor (although the same is not true of second-order partial differential equations, or if y is a vector). Some examples are below.

### Bessel equation

$x^{2}y''+xy'+\left(x^{2}-\nu ^{2}\right)y=0$ which can be written in Sturm–Liouville form (first by dividing through by x, then by collapsing the first two terms on the left into one term) as $\left(xy'\right)'+\left(x-{\frac {\nu ^{2}}{x}}\right)y=0.$

### Legendre equation

$\left(1-x^{2}\right)y''-2xy'+\nu (\nu +1)y=0$ which can be put into Sturm–Liouville form, since ⁠*d*/*dx*⁠(1 − *x*2) = −2*x*, so the Legendre equation is equivalent to $\left(\left(1-x^{2}\right)y'\right)'+\nu (\nu +1)y=0$

### Example using an integrating factor

$x^{3}y''-xy'+2y=0$

Divide throughout by *x*3: $y''-{\frac {1}{x^{2}}}y'+{\frac {2}{x^{3}}}y=0$

Multiplying throughout by an integrating factor of $\mu (x)=\exp \left(\int -{\frac {dx}{x^{2}}}\right)=e^{{1}/{x}},$ gives $e^{{1}/{x}}y''-{\frac {e^{{1}/{x}}}{x^{2}}}y'+{\frac {2e^{{1}/{x}}}{x^{3}}}y=0$ which can be put into Sturm–Liouville form since ${\frac {d}{dx}}e^{{1}/{x}}=-{\frac {e^{{1}/{x}}}{x^{2}}}$ so the differential equation is equivalent to $\left(e^{{1}/{x}}y'\right)'+{\frac {2e^{{1}/{x}}}{x^{3}}}y=0.$

### Integrating factor for general second-order homogeneous equation

$P(x)y''+Q(x)y'+R(x)y=0$

Multiplying through by the integrating factor $\mu (x)={\frac {1}{P(x)}}\exp \left(\int {\frac {Q(x)}{P(x)}}\,dx\right),$ and then collecting gives the Sturm–Liouville form: ${\frac {d}{dx}}\left(\mu (x)P(x)y'\right)+\mu (x)R(x)y=0,$ or, explicitly: ${\frac {d}{dx}}\left(\exp \left(\int {\frac {Q(x)}{P(x)}}\,dx\right)y'\right)+{\frac {R(x)}{P(x)}}\exp \left(\int {\frac {Q(x)}{P(x)}}\,dx\right)y=0.$

## Sturm–Liouville equations as self-adjoint differential operators

The mapping defined by: $Lu=-{\frac {1}{w(x)}}\left({\frac {d}{dx}}\left[p(x)\,{\frac {du}{dx}}\right]+q(x)u\right)$ can be viewed as a linear operator L mapping a function u to another function Lu, and it can be studied in the context of functional analysis. In fact, equation (**1**) can be written as $Lu=\lambda u.$

This is precisely the eigenvalue problem; that is, one seeks eigenvalues *λ*1, *λ*2, *λ*3,... and the corresponding eigenvectors *u*1, *u*2, *u*3,... of the L operator. The proper setting for this problem is the Hilbert space $L^{2}([a,b],w(x)\,dx)$ with scalar product $\langle f,g\rangle =\int _{a}^{b}{\overline {f(x)}}g(x)w(x)\,dx.$

In this space L is defined on sufficiently smooth functions which satisfy the above regular boundary conditions. Moreover, L is a self-adjoint operator: $\langle Lf,g\rangle =\langle f,Lg\rangle .$

This can be seen formally by using integration by parts twice, where the boundary terms vanish by virtue of the boundary conditions. It then follows that the eigenvalues of a Sturm–Liouville operator are real and that eigenfunctions of L corresponding to different eigenvalues are orthogonal. However, this operator is unbounded and hence existence of an orthonormal basis of eigenfunctions is not evident. To overcome this problem, one looks at the resolvent $\left(L-z\right)^{-1},\qquad z\in \mathbb {R} ,$ where z is not an eigenvalue. Then, computing the resolvent amounts to solving a nonhomogeneous equation, which can be done using the variation of parameters formula. This shows that the resolvent is an integral operator with a continuous symmetric kernel (the Green's function of the problem). As a consequence of the Arzelà–Ascoli theorem, this integral operator is compact and existence of a sequence of eigenvalues αn which converge to 0 and eigenfunctions which form an orthonormal basis follows from the spectral theorem for compact operators. Finally, note that $\left(L-z\right)^{-1}u=\alpha u,\qquad Lu=\left(z+\alpha ^{-1}\right)u,$ are equivalent, so we may take $\lambda =z+\alpha ^{-1}$ with the same eigenfunctions.

If the interval is unbounded, or if the coefficients have singularities at the boundary points, one calls L singular. In this case, the spectrum no longer consists of eigenvalues alone and can contain a continuous component. There is still an associated eigenfunction expansion (similar to Fourier series versus Fourier transform). This is important in quantum mechanics, since the one-dimensional time-independent Schrödinger equation is a special case of a Sturm–Liouville equation.

## Application to inhomogeneous second-order boundary value problems

Consider a general inhomogeneous second-order linear differential equation $P(x)y''+Q(x)y'+R(x)y=f(x)$ for given functions $P(x),Q(x),R(x),f(x)$ . As before, this can be reduced to the Sturm–Liouville form $Ly=f$ : writing a general Sturm–Liouville operator as: $Lu={\frac {p}{w(x)}}u''+{\frac {p'}{w(x)}}u'+{\frac {q}{w(x)}}u,$ one solves the system: $p=Pw,\quad p'=Qw,\quad q=Rw.$

It suffices to solve the first two equations, which amounts to solving (*Pw*)′ = *Qw*, or $w'={\frac {Q-P'}{P}}w:=\alpha w.$

A solution is:

$w=\exp \left(\int \alpha \,dx\right),\quad p=P\exp \left(\int \alpha \,dx\right),\quad q=R\exp \left(\int \alpha \,dx\right).$

Given this transformation, one is left to solve: $Ly=f.$

In general, if initial conditions at some point are specified, for example *y*(*a*) = 0 and *y*′(*a*) = 0, a second order differential equation can be solved using ordinary methods and the Picard–Lindelöf theorem ensures that the differential equation has a unique solution in a neighbourhood of the point where the initial conditions have been specified.

But if in place of specifying initial values at a *single point*, it is desired to specify values at *two* different points (so-called boundary values), e.g. *y*(*a*) = 0 and *y*(*b*) = 1, the problem turns out to be much more difficult. Notice that by adding a suitable known differentiable function to y, whose values at a and b satisfy the desired boundary conditions, and injecting inside the proposed differential equation, it can be assumed without loss of generality that the boundary conditions are of the form *y*(*a*) = 0 and *y*(*b*) = 0.

Here, the Sturm–Liouville theory comes in play: indeed, a large class of functions f can be expanded in terms of a series of orthonormal eigenfunctions ui of the associated Liouville operator with corresponding eigenvalues λi: $f(x)=\sum _{i}\alpha _{i}u_{i}(x),\quad \alpha _{i}\in {\mathbb {R} }.$

Then a solution to the proposed equation is evidently: $y=\sum _{i}{\frac {\alpha _{i}}{\lambda _{i}}}u_{i}.$

This solution will be valid only over the open interval *a* < *x* < *b*, and may fail at the boundaries.

### Example: Fourier series

Consider the Sturm–Liouville problem:

| $Lu=-{\frac {d^{2}u}{dx^{2}}}=\lambda u$ |   | 4 |
|---|---|---|

for the unknowns are λ and *u*(*x*). For boundary conditions, we take for example: $u(0)=u(\pi )=0.$

Observe that if k is any integer, then the function $u_{k}(x)=\sin kx$ is a solution with eigenvalue *λ* = *k*2. We know that the solutions of a Sturm–Liouville problem form an orthogonal basis, and we know from Fourier series that this set of sinusoidal functions is an orthogonal basis. Since orthogonal bases are always maximal (by definition) we conclude that the Sturm–Liouville problem in this case has no other eigenvectors.

Given the preceding, let us now solve the inhomogeneous problem $Ly=x,\qquad x\in (0,\pi )$ with the same boundary conditions $y(0)=y(\pi )=0$ . In this case, we must expand *f*(*x*) = *x* as a Fourier series. The reader may check, either by integrating ∫ *e**ikx**x* *dx* or by consulting a table of Fourier transforms, that we thus obtain $Ly=\sum _{k=1}^{\infty }-2{\frac {\left(-1\right)^{k}}{k}}\sin kx.$

This particular Fourier series is troublesome because of its poor convergence properties. It is not clear *a priori* whether the series converges pointwise. Because of Fourier analysis, since the Fourier coefficients are "square-summable", the Fourier series converges in *L*2 which is all we need for this particular theory to function. We mention for the interested reader that in this case we may rely on a result which says that Fourier series converge at every point of differentiability, and at jump points (the function *x*, considered as a periodic function, has a jump at π) converges to the average of the left and right limits (see convergence of Fourier series).

Therefore, by using formula (**4**), we obtain the solution: $y=\sum _{k=1}^{\infty }2{\frac {(-1)^{k}}{k^{3}}}\sin kx={\tfrac {1}{6}}(x^{3}-\pi ^{2}x).$

In this case, we could have found the answer using antidifferentiation, but this is no longer useful in most cases when the differential equation is in many variables.

## Application to partial differential equations

### Normal modes

Certain partial differential equations can be solved with the help of Sturm–Liouville theory. Suppose we are interested in the vibrational modes of a thin membrane, held in a rectangular frame, 0 ≤ *x* ≤ *L*1, 0 ≤ *y* ≤ *L*2. The equation of motion for the vertical membrane's displacement, *W*(*x*,*y*,*t*) is given by the wave equation: ${\frac {\partial ^{2}W}{\partial x^{2}}}+{\frac {\partial ^{2}W}{\partial y^{2}}}={\frac {1}{c^{2}}}{\frac {\partial ^{2}W}{\partial t^{2}}}.$

The method of separation of variables suggests looking first for solutions of the simple form *W* = *X*(*x*) × *Y*(*y*) × *T*(*t*). For such a function W the partial differential equation becomes ⁠*X*″/*X*⁠ + ⁠*Y*″/*Y*⁠ = ⁠1/*c*2⁠ ⁠*T*″/*T*⁠. Since the three terms of this equation are functions of *x*, *y*, *t* separately, they must be constants. For example, the first term gives *X*″ = *λX* for a constant λ. The boundary conditions ("held in a rectangular frame") are *W* = 0 when *x* = 0, *L*1 or *y* = 0, *L*2 and define the simplest possible Sturm–Liouville eigenvalue problems as in the example, yielding the "normal mode solutions" for W with harmonic time dependence, $W_{mn}(x,y,t)=A_{mn}\sin \left({\frac {m\pi x}{L_{1}}}\right)\sin \left({\frac {n\pi y}{L_{2}}}\right)\cos \left(\omega _{mn}t\right)$ where m and n are non-zero integers, Amn are arbitrary constants, and $\omega _{mn}^{2}=c^{2}\left({\frac {m^{2}\pi ^{2}}{L_{1}^{2}}}+{\frac {n^{2}\pi ^{2}}{L_{2}^{2}}}\right).$

The functions Wmn form a basis for the Hilbert space of (generalized) solutions of the wave equation; that is, an arbitrary solution W can be decomposed into a sum of these modes, which vibrate at their individual frequencies ωmn. This representation may require a convergent infinite sum.

### Second-order linear equation

Consider a linear second-order differential equation in one spatial dimension and first-order in time of the form: $f(x){\frac {\partial ^{2}u}{\partial x^{2}}}+g(x){\frac {\partial u}{\partial x}}+h(x)u={\frac {\partial u}{\partial t}}+k(t)u,$ $u(a,t)=u(b,t)=0,\qquad u(x,0)=s(x).$

Separating variables, we assume that $u(x,t)=X(x)T(t).$ Then our above partial differential equation may be written as: ${\frac {{\hat {L}}X(x)}{X(x)}}={\frac {{\hat {M}}T(t)}{T(t)}}$ where ${\hat {L}}=f(x){\frac {d^{2}}{dx^{2}}}+g(x){\frac {d}{dx}}+h(x),\qquad {\hat {M}}={\frac {d}{dt}}+k(t).$

Since, by definition, L̂ and *X*(*x*) are independent of time t and M̂ and *T*(*t*) are independent of position x, then both sides of the above equation must be equal to a constant: ${\hat {L}}X(x)=\lambda X(x),\qquad X(a)=X(b)=0,\qquad {\hat {M}}T(t)=\lambda T(t).$

The first of these equations must be solved as a Sturm–Liouville problem in terms of the eigenfunctions *Xn*(*x*) and eigenvalues *λn*. The second of these equations can be analytically solved once the eigenvalues are known.

${\frac {d}{dt}}T_{n}(t)={\bigl (}\lambda _{n}-k(t){\bigr )}T_{n}(t)$ $T_{n}(t)=a_{n}\exp \left(\lambda _{n}t-\int _{0}^{t}k(\tau )\,d\tau \right)$ $u(x,t)=\sum _{n}a_{n}X_{n}(x)\exp \left(\lambda _{n}t-\int _{0}^{t}k(\tau )\,d\tau \right)$ $a_{n}={\frac {{\bigl \langle }X_{n}(x),s(x){\bigr \rangle }}{{\bigl \langle }X_{n}(x),X_{n}(x){\bigr \rangle }}}$

where ${\bigl \langle }y(x),z(x){\bigr \rangle }=\int _{a}^{b}y(x)z(x)w(x)\,dx,$ $w(x)={\frac {\exp \left(\int {\frac {g(x)}{f(x)}}\,dx\right)}{f(x)}}.$

## Representation of solutions and numerical calculation

The Sturm–Liouville differential equation (**1**) with boundary conditions may be solved analytically, which can be exact or provide an approximation, by the Rayleigh–Ritz method, or by the matrix-variational method of Gerck et al.

Numerically, a variety of methods are also available. In difficult cases, one may need to carry out the intermediate calculations to several hundred decimal places of accuracy in order to obtain the eigenvalues correctly to a few decimal places.

- Shooting methods
- Finite difference method
- Spectral parameter power series method

### Shooting methods

Shooting methods proceed by guessing a value of λ, solving an initial value problem defined by the boundary conditions at one endpoint, say, a, of the interval [*a*,*b*], comparing the value this solution takes at the other endpoint b with the other desired boundary condition, and finally increasing or decreasing λ as necessary to correct the original value. This strategy is not applicable for locating complex eigenvalues.

### Spectral parameter power series method

The spectral parameter power series (SPPS) method makes use of a generalization of the following fact about homogeneous second-order linear ordinary differential equations: if y is a solution of equation (**1**) that does not vanish at any point of [*a*,*b*], then the function $y(x)\int _{a}^{x}{\frac {dt}{p(t)y(t)^{2}}}$ is a solution of the same equation and is linearly independent from y. Further, all solutions are linear combinations of these two solutions. In the SPPS algorithm, one must begin with an arbitrary value *λ*∗ 0 (often *λ*∗ 0 = 0; it does not need to be an eigenvalue) and any solution *y*0 of (**1**) with *λ* = *λ*∗ 0 which does not vanish on [*a*,*b*]. (Discussion below of ways to find appropriate *y*0 and *λ*∗ 0.) Two sequences of functions *X*(*n*)(*t*), *X̃*(*n*)(*t*) on [*a*,*b*], referred to as *iterated integrals*, are defined recursively as follows. First when *n* = 0, they are taken to be identically equal to 1 on [*a*,*b*]. To obtain the next functions they are multiplied alternately by ⁠1/*py*2 0⁠ and *wy*2 0 and integrated, specifically, for *n* > 0:

| $X^{(n)}(t)={\begin{cases}\displaystyle -\int _{a}^{x}X^{(n-1)}(t)p(t)^{-1}y_{0}(t)^{-2}\,dt&n{\text{ odd}},\\[6pt]\displaystyle \quad \int _{a}^{x}X^{(n-1)}(t)y_{0}(t)^{2}w(t)\,dt&n{\text{ even}}\end{cases}}$ |   | 5 |
|---|---|---|

| ${\tilde {X}}^{(n)}(t)={\begin{cases}\displaystyle \quad \int _{a}^{x}{\tilde {X}}^{(n-1)}(t)y_{0}(t)^{2}w(t)\,dt&n{\text{ odd}},\\[6pt]\displaystyle -\int _{a}^{x}{\tilde {X}}^{(n-1)}(t)p(t)^{-1}y_{0}(t)^{-2}\,dt&n{\text{ even.}}\end{cases}}$ |   | 6 |
|---|---|---|

The resulting iterated integrals are now applied as coefficients in the following two power series in *λ*: $u_{0}=y_{0}\sum _{k=0}^{\infty }\left(\lambda -\lambda _{0}^{*}\right)^{k}{\tilde {X}}^{(2k)},$ $u_{1}=y_{0}\sum _{k=0}^{\infty }\left(\lambda -\lambda _{0}^{*}\right)^{k}X^{(2k+1)}.$ Then for any λ (real or complex), *u*0 and *u*1 are linearly independent solutions of the corresponding equation (**1**). (The functions *p*(*x*) and *q*(*x*) take part in this construction through their influence on the choice of *y*0.)

Next one chooses coefficients *c*0 and *c*1 so that the combination *y* = *c*0*u*0 + *c*1*u*1 satisfies the first boundary condition (**2**). This is simple to do since *X*(*n*)(*a*) = 0 and *X̃*(*n*)(*a*) = 0, for *n* > 0. The values of *X*(*n*)(*b*) and *X̃*(*n*)(*b*) provide the values of *u*0(*b*) and *u*1(*b*) and the derivatives *u*′0(*b*) and *u*′0(*b*), so the second boundary condition (**3**) becomes an equation in a power series in λ. For numerical work one may truncate this series to a finite number of terms, producing a calculable polynomial in λ whose roots are approximations of the sought-after eigenvalues.

When *λ* = *λ*0, this reduces to the original construction described above for a solution linearly independent to a given one. The representations (**5**) and (**6**) also have theoretical applications in Sturm–Liouville theory.

### Construction of a nonvanishing solution

The SPPS method can, itself, be used to find a starting solution *y*0. Consider the equation (*py*′)′ = *μqy*; i.e., q, w, and λ are replaced in (**1**) by 0, −*q*, and μ respectively. Then the constant function 1 is a nonvanishing solution corresponding to the eigenvalue *μ*0 = 0. While there is no guarantee that *u*0 or *u*1 will not vanish, the complex function *y*0 = *u*0 + *iu*1 will never vanish because two linearly-independent solutions of a regular Sturm–Liouville equation cannot vanish simultaneously as a consequence of the Sturm separation theorem. This trick gives a solution *y*0 of (**1**) for the value *λ*0 = 0. In practice if (**1**) has real coefficients, the solutions based on *y*0 will have very small imaginary parts which must be discarded.
