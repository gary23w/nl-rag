---
title: "Eigenfunction"
source: https://en.wikipedia.org/wiki/Eigenfunction
domain: spectral-theory
license: CC-BY-SA-4.0
tags: spectral theory, spectral theorem, self-adjoint operator, sturm-liouville theory
fetched: 2026-07-02
---

# Eigenfunction

In mathematics, an **eigenfunction** of a linear operator *D* defined on some function space is any non-zero function f in that space that, when acted upon by *D*, is only multiplied by some scaling factor called an eigenvalue. As an equation, this condition can be written as

$Df=\lambda f$ for some scalar eigenvalue $\lambda .$ The solutions to this equation may also be subject to boundary conditions that limit the allowable eigenvalues and eigenfunctions.

An eigenfunction is a type of eigenvector.

## Eigenfunctions

In general, an eigenvector of a linear operator *D* defined on some vector space is a nonzero vector in the domain of *D* that, when *D* acts upon it, is simply scaled by some scalar value called an eigenvalue. In the special case where *D* is defined on a function space, the eigenvectors are referred to as **eigenfunctions**. That is, a function *f* is an eigenfunction of *D* if it satisfies the equation

| $Df=\lambda f,$ |   | 1 |
|---|---|---|

where λ is a scalar. The solutions to Equation (**1**) may also be subject to boundary conditions. Because of the boundary conditions, the possible values of λ are generally limited, for example to a discrete set *λ*1, *λ*2, … or to a continuous set over some range. The set of all possible eigenvalues of *D* is sometimes called its spectrum, which may be discrete, continuous, or a combination of both.

Each value of λ corresponds to one or more eigenfunctions. If multiple linearly independent eigenfunctions have the same eigenvalue, the eigenvalue is said to be degenerate and the maximum number of linearly independent eigenfunctions associated with the same eigenvalue is the eigenvalue's *degree of degeneracy* or geometric multiplicity.

### Derivative example

A widely used class of linear operators acting on infinite dimensional spaces are differential operators on the space **C**∞ of infinitely differentiable real or complex functions of a real or complex argument *t*. For example, consider the derivative operator ${\textstyle {\frac {d}{dt}}}$ with eigenvalue equation

${\frac {d}{dt}}f(t)=\lambda f(t).$

This differential equation can be solved by multiplying both sides by ${\textstyle {\frac {dt}{f(t)}}}$ and integrating. Its solution, the exponential function

$f(t)=f_{0}e^{\lambda t},$

is the eigenfunction of the derivative operator, where *f*0 is a parameter that depends on the boundary conditions. Note that in this case the eigenfunction is itself a function of its associated eigenvalue λ, which can take any real or complex value. In particular, note that for λ = 0 the eigenfunction *f*(*t*) is a constant.

Suppose in the example that *f*(*t*) is subject to the boundary conditions *f*(0) = 1 and ${\textstyle \left.{\frac {df}{dt}}\right|_{t=0}=2}$ . We then find that

$f(t)=e^{2t},$

where λ = 2 is the only eigenvalue of the differential equation that also satisfies the boundary condition.

### Link to eigenvalues and eigenvectors of matrices

Eigenfunctions can be expressed as column vectors and linear operators can be expressed as matrices, although they may have infinite dimensions. As a result, many of the concepts related to eigenvectors of matrices carry over to the study of eigenfunctions.

Define the inner product in the function space on which *D* is defined as

$\langle f,g\rangle =\int _{\Omega }\ f^{*}(t)g(t)dt,$

integrated over some range of interest for *t* called Ω. The *** denotes the complex conjugate.

Suppose the function space has an orthonormal basis given by the set of functions {*u*1(*t*), *u*2(*t*), …, *u**n*(*t*)}, where *n* may be infinite. For the orthonormal basis,

$\langle u_{i},u_{j}\rangle =\int _{\Omega }\ u_{i}^{*}(t)u_{j}(t)dt=\delta _{ij}={\begin{cases}1&i=j\\0&i\neq j\end{cases}},$

where *δ**ij* is the Kronecker delta and can be thought of as the elements of the identity matrix.

Functions can be written as a linear combination of the basis functions,

$f(t)=\sum _{j=1}^{n}b_{j}u_{j}(t),$

for example through a Fourier expansion of *f*(*t*). The coefficients *b**j* can be stacked into an *n* by 1 column vector *b* = [*b*1 *b*2 … *b**n*]T. In some special cases, such as the coefficients of the Fourier series of a sinusoidal function, this column vector has finite dimension.

Additionally, define a matrix representation of the linear operator *D* with elements

$A_{ij}=\langle u_{i},Du_{j}\rangle =\int _{\Omega }\ u_{i}^{*}(t)Du_{j}(t)dt.$

We can write the function *Df*(*t*) either as a linear combination of the basis functions or as *D* acting upon the expansion of *f*(*t*),

$Df(t)=\sum _{j=1}^{n}c_{j}u_{j}(t)=\sum _{j=1}^{n}b_{j}Du_{j}(t).$

Taking the inner product of each side of this equation with an arbitrary basis function *u**i*(*t*),

${\begin{aligned}\sum _{j=1}^{n}c_{j}\int _{\Omega }\ u_{i}^{*}(t)u_{j}(t)dt&=\sum _{j=1}^{n}b_{j}\int _{\Omega }\ u_{i}^{*}(t)Du_{j}(t)dt,\\c_{i}&=\sum _{j=1}^{n}b_{j}A_{ij}.\end{aligned}}$

This is the matrix multiplication *Ab* = *c* written in summation notation and is a matrix equivalent of the operator *D* acting upon the function *f*(*t*) expressed in the orthonormal basis. If *f*(*t*) is an eigenfunction of *D* with eigenvalue λ, then *Ab* = *λb*.

### Eigenvalues and eigenfunctions of Hermitian operators

Many of the operators encountered in physics are Hermitian. Suppose the linear operator *D* acts on a function space that is a Hilbert space with an orthonormal basis given by the set of functions {*u*1(*t*), *u*2(*t*), …, *u**n*(*t*)}, where *n* may be infinite. In this basis, the operator *D* has a matrix representation *A* with elements

$A_{ij}=\langle u_{i},Du_{j}\rangle =\int _{\Omega }dt\ u_{i}^{*}(t)Du_{j}(t).$

integrated over some range of interest for *t* denoted Ω.

By analogy with Hermitian matrices, *D* is a Hermitian operator if *A**ij* = *A**ji**, or:

${\begin{aligned}\langle u_{i},Du_{j}\rangle &=\langle Du_{i},u_{j}\rangle ,\\[-1pt]\int _{\Omega }dt\ u_{i}^{*}(t)Du_{j}(t)&=\int _{\Omega }dt\ u_{j}(t)[Du_{i}(t)]^{*}.\end{aligned}}$

Consider the Hermitian operator *D* with eigenvalues *λ*1, *λ*2, ... and corresponding eigenfunctions *f*1(*t*), *f*2(*t*), …. This Hermitian operator has the following properties:

- Its eigenvalues are real, *λ**i* = *λ**i**
- Its eigenfunctions obey an orthogonality condition, $\langle f_{i},f_{j}\rangle =0$ if *i* ≠ *j*

The second condition always holds for *λ**i* ≠ *λ**j*. For degenerate eigenfunctions with the same eigenvalue *λ**i*, orthogonal eigenfunctions can always be chosen that span the eigenspace associated with *λ**i*, for example by using the Gram-Schmidt process. Depending on whether the spectrum is discrete or continuous, the eigenfunctions can be normalized by setting the inner product of the eigenfunctions equal to either a Kronecker delta or a Dirac delta function, respectively.

For many Hermitian operators, notably Sturm–Liouville operators, a third property is

- Its eigenfunctions form a basis of the function space on which the operator is defined

As a consequence, in many important cases, the eigenfunctions of the Hermitian operator form an orthonormal basis. In these cases, an arbitrary function can be expressed as a linear combination of the eigenfunctions of the Hermitian operator.

## Applications

### Vibrating strings

Let *h*(*x*, *t*) denote the transverse displacement of a stressed elastic chord, such as the vibrating strings of a string instrument, as a function of the position x along the string and of time t. Applying the laws of mechanics to infinitesimal portions of the string, the function h satisfies the partial differential equation

${\frac {\partial ^{2}h}{\partial t^{2}}}=c^{2}{\frac {\partial ^{2}h}{\partial x^{2}}},$

which is called the (one-dimensional) wave equation. Here c is a constant speed that depends on the tension and mass of the string.

This problem is amenable to the method of separation of variables. If we assume that *h*(*x*, *t*) can be written as the product of the form *X*(*x*)*T*(*t*), we can form a pair of ordinary differential equations:

${\frac {d^{2}}{dx^{2}}}X=-{\frac {\omega ^{2}}{c^{2}}}X,\qquad {\frac {d^{2}}{dt^{2}}}T=-\omega ^{2}T.$

Each of these is an eigenvalue equation with eigenvalues

${\textstyle -{\frac {\omega ^{2}}{c^{2}}}}$ and −*ω*2, respectively. For any values of ω and c, the equations are satisfied by the functions

$X(x)=\sin \left({\frac {\omega x}{c}}+\varphi \right),\qquad T(t)=\sin(\omega t+\psi ),$ where the phase angles φ and ψ are arbitrary real constants.

If we impose boundary conditions, for example that the ends of the string are fixed at *x* = 0 and *x* = *L*, namely *X*(0) = *X*(*L*) = 0, and that *T*(0) = 0, we constrain the eigenvalues. For these boundary conditions, sin(*φ*) = 0 and sin(*ψ*) = 0, so the phase angles *φ* = *ψ* = 0, and

$\sin \left({\frac {\omega L}{c}}\right)=0.$

This last boundary condition constrains ω to take a value *ωn* = ⁠*ncπ*/*L*⁠, where n is any integer. Thus, the clamped string supports a family of standing waves of the form

$h(x,t)=\sin \left({\frac {n\pi x}{L}}\right)\sin(\omega _{n}t).$

In the example of a string instrument, the frequency *ωn* is the frequency of the n-th harmonic, which is called the (*n* − 1)-th overtone.

### Schrödinger equation

In quantum mechanics, the Schrödinger equation

$i\hbar {\frac {\partial }{\partial t}}\Psi (\mathbf {r} ,t)=H\Psi (\mathbf {r} ,t)$

with the Hamiltonian operator

$H=-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}+V(\mathbf {r} ,t)$ can be solved by separation of variables if the Hamiltonian does not depend explicitly on time. In that case, the wave function Ψ(**r**,*t*) = *φ*(**r**)*T*(*t*) leads to the two differential equations,

| $H\varphi (\mathbf {r} )=E\varphi (\mathbf {r} ),$ |   | 2 |
|---|---|---|

| $i\hbar {\frac {\partial T(t)}{\partial t}}=ET(t).$ |   | 3 |
|---|---|---|

Both of these differential equations are eigenvalue equations with eigenvalue E. As shown in an earlier example, the solution of Equation (**3**) is the exponential $T(t)=e^{{-iEt}/{\hbar }}.$

Equation (**2**) is the time-independent Schrödinger equation. The eigenfunctions φk of the Hamiltonian operator are stationary states of the quantum mechanical system, each with a corresponding energy Ek. They represent allowable energy states of the system and may be constrained by boundary conditions.

The Hamiltonian operator H is an example of a Hermitian operator whose eigenfunctions form an orthonormal basis. When the Hamiltonian does not depend explicitly on time, general solutions of the Schrödinger equation are linear combinations of the stationary states multiplied by the oscillatory *T*(*t*), ${\textstyle \Psi (\mathbf {r} ,t)=\sum _{k}c_{k}\varphi _{k}(\mathbf {r} )e^{{-iE_{k}t}/{\hbar }}}$ or, for a system with a continuous spectrum,

$\Psi (\mathbf {r} ,t)=\int dE\,c_{E}\varphi _{E}(\mathbf {r} )e^{{-iEt}/{\hbar }}.$

The success of the Schrödinger equation in explaining the spectral characteristics of hydrogen is considered one of the greatest triumphs of 20th century physics.

### Signals and systems

In the study of signals and systems, an eigenfunction of a system is a signal *f*(*t*) that, when input into the system, produces a response *y*(*t*) = *λf*(*t*), where λ is a complex scalar eigenvalue.
