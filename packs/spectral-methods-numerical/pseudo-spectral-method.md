---
title: "Pseudo-spectral method"
source: https://en.wikipedia.org/wiki/Pseudo-spectral_method
domain: spectral-methods-numerical
license: CC-BY-SA-4.0
tags: spectral method, pseudo-spectral method, galerkin method, collocation method
fetched: 2026-07-02
---

# Pseudo-spectral method

**Pseudo-spectral methods**, also known as discrete variable representation (DVR) methods, are a class of numerical methods used in applied mathematics and scientific computing for the solution of partial differential equations. They are closely related to spectral methods, but complement the basis by an additional pseudo-spectral basis, which allows representation of functions on a quadrature grid. This simplifies the evaluation of certain operators, and can considerably speed up the calculation when using fast algorithms such as the fast Fourier transform.

## Motivation with a concrete example

Take the initial-value problem

$i{\frac {\partial }{\partial t}}\psi (x,t)={\Bigl [}-{\frac {\partial ^{2}}{\partial x^{2}}}+V(x){\Bigr ]}\psi (x,t),\qquad \qquad \psi (t_{0})=\psi _{0}$

with periodic conditions $\psi (x+1,t)=\psi (x,t)$ . This specific example is the Schrödinger equation for a particle in a potential $V(x)$ , but the structure is more general. In many practical partial differential equations, one has a term that involves derivatives (such as a kinetic energy contribution), and a multiplication with a function (for example, a potential).

In the spectral method, the solution $\psi$ is expanded in a suitable set of basis functions, for example plane waves,

$\psi (x,t)={\frac {1}{\sqrt {2\pi }}}\sum _{n}c_{n}(t)e^{2\pi inx}.$

Insertion and equating identical coefficients yields a set of ordinary differential equations for the coefficients,

$i{\frac {d}{dt}}c_{n}(t)=(2\pi n)^{2}c_{n}+\sum _{k}V_{n-k}c_{k},$

where the elements $V_{n-k}$ are calculated through the explicit Fourier-transform

$V_{n-k}=\int _{0}^{1}V(x)\ e^{2\pi i(k-n)x}dx.$

The solution would then be obtained by truncating the expansion to N basis functions, and finding a solution for the $c_{n}(t)$ . In general, this is done by numerical methods, such as Runge–Kutta methods. For the numerical solutions, the right-hand side of the ordinary differential equation has to be evaluated repeatedly at different time steps. At this point, the spectral method has a major problem with the potential term $V(x)$ .

In the spectral representation, the multiplication with the function $V(x)$ transforms into a vector-matrix multiplication, which scales as $N^{2}$ . Also, the matrix elements $V_{n-k}$ need to be evaluated explicitly before the differential equation for the coefficients can be solved, which requires an additional step.

In the pseudo-spectral method, this term is evaluated differently. Given the coefficients $c_{n}(t)$ , an inverse discrete Fourier transform yields the value of the function $\psi$ at discrete grid points $x_{j}=2\pi j/N$ . At these grid points, the function is then multiplied, $\psi '(x_{i},t)=V(x_{i})\psi (x_{i},t)$ , and the result Fourier-transformed back. This yields a new set of coefficients $c'_{n}(t)$ that are used instead of the matrix product $\sum _{k}V_{n-k}c_{k}(t)$ .

It can be shown that both methods have similar accuracy. However, the pseudo-spectral method allows the use of a fast Fourier transform, which scales as $O(N\ln N)$ , and is therefore significantly more efficient than the matrix multiplication. Also, the function $V(x)$ can be used directly without evaluating any additional integrals.

## Technical discussion

In a more abstract way, the pseudo-spectral method deals with the multiplication of two functions $V(x)$ and $f(x)$ as part of a partial differential equation. To simplify the notation, the time-dependence is dropped. Conceptually, it consists of three steps:

1. $f(x),{\tilde {f}}(x)=V(x)f(x)$ are expanded in a finite set of basis functions (this is the spectral method).
2. For a given set of basis functions, a quadrature is sought that converts scalar products of these basis functions into a weighted sum over grid points.
3. The product is calculated by multiplying $V,f$ at each grid point.

### Expansion in a basis

The functions $f,{\tilde {f}}$ can be expanded in a finite basis $\{\phi _{n}\}_{n=0,\ldots ,N}$ as

$f(x)=\sum _{n=0}^{N}c_{n}\phi _{n}(x)$

${\tilde {f}}(x)=\sum _{n=0}^{N}{\tilde {c}}_{n}\phi _{n}(x)$

For simplicity, let the basis be orthogonal and normalized, $\langle \phi _{n},\phi _{m}\rangle =\delta _{nm}$ using the inner product $\langle f,g\rangle =\int _{a}^{b}f(x){\overline {g(x)}}dx$ with appropriate boundaries $a,b$ . The coefficients are then obtained by

$c_{n}=\langle f,\phi _{n}\rangle$

${\tilde {c}}_{n}=\langle {\tilde {f}},\phi _{n}\rangle$

A bit of calculus yields then

${\tilde {c}}_{n}=\sum _{m=0}^{N}V_{n-m}c_{m}$

with $V_{n-m}=\langle V\phi _{m},\phi _{n}\rangle$ . This forms the basis of the spectral method. To distinguish the basis of the $\phi _{n}$ from the quadrature basis, the expansion is sometimes called Finite Basis Representation (FBR).

### Quadrature

For a given basis $\{\phi _{n}\}$ and number of $N+1$ basis functions, one can try to find a quadrature, i.e., a set of $N+1$ points and weights such that

$\langle \phi _{n},\phi _{m}\rangle =\sum _{i=0}^{N}w_{i}\phi _{n}(x_{i}){\overline {\phi _{m}(x_{i})}}\qquad \qquad n,m=0,\ldots ,N$

Special examples are the Gaussian quadrature for polynomials and the Discrete Fourier Transform for plane waves. It should be stressed that the grid points and weights, $x_{i},w_{i}$ are a function of the basis *and* the number N .

The quadrature allows an alternative numerical representation of the function $f(x),{\tilde {f}}(x)$ through their value at the grid points. This representation is sometimes denoted Discrete Variable Representation (DVR), and is completely equivalent to the expansion in the basis.

$f(x_{i})=\sum _{n=0}^{N}c_{n}\phi _{n}(x_{i})$

$c_{n}=\langle f,\phi _{n}\rangle =\sum _{i=0}^{N}w_{i}f(x_{i}){\overline {\phi _{n}(x_{i})}}$

### Multiplication

The multiplication with the function $V(x)$ is then done at each grid point,

${\tilde {f}}(x_{i})=V(x_{i})f(x_{i}).$

This generally introduces an additional approximation. To see this, we can calculate one of the coefficients ${\tilde {c}}_{n}$ :

${\tilde {c}}_{n}=\langle {\tilde {f}},\phi _{n}\rangle =\sum _{i}w_{i}{\tilde {f}}(x_{i}){\overline {\phi _{n}(x_{i})}}=\sum _{i}w_{i}V(x_{i})f(x_{i}){\overline {\phi _{n}(x_{i})}}$

However, using the spectral method, the same coefficient would be ${\tilde {c}}_{n}=\langle Vf,\phi _{n}\rangle$ . The pseudo-spectral method thus introduces the additional approximation

$\langle Vf,\phi _{n}\rangle \approx \sum _{i}w_{i}V(x_{i})f(x_{i}){\overline {\phi _{n}(x_{i})}}.$

If the product $Vf$ can be represented with the given finite set of basis functions, the above equation is exact due to the chosen quadrature.

## Special pseudospectral schemes

### The Fourier method

If periodic boundary conditions with period $[0,L]$ are imposed on the system, the basis functions can be generated by plane waves,

$\phi _{n}(x)={\frac {1}{\sqrt {L}}}e^{-\imath k_{n}x}$

with $k_{n}=(-1)^{n}\lceil n/2\rceil 2\pi /L$ , where $\lceil \cdot \rceil$ is the ceiling function.

The quadrature for a cut-off at $n_{\text{max}}=N$ is given by the discrete Fourier transformation. The grid points are equally spaced, $x_{i}=i\Delta x$ with spacing $\Delta x=L/(N+1)$ , and the constant weights are $w_{i}=\Delta x$ .

For the discussion of the error, note that the product of two plane waves is again a plane wave, $\phi _{a}+\phi _{b}=\phi _{c}$ with $c\leq a+b$ . Thus, qualitatively, if the functions $f(x),V(x)$ can be represented sufficiently accurately with $N_{f},N_{V}$ basis functions, the pseudo-spectral method gives accurate results if $N_{f}+N_{V}$ basis functions are used.

An expansion in plane waves often has a poor quality and needs many basis functions to converge. However, the transformation between the basis expansion and the grid representation can be done using a Fast Fourier transform, which scales favorably as $N\ln N$ . As a consequence, plane waves are one of the most common expansion that is encountered with pseudo-spectral methods.

### Polynomials

Another common expansion is into classical polynomials. Here, the Gaussian quadrature is used, which states that one can always find weights $w_{i}$ and points $x_{i}$ such that

$\int _{a}^{b}w(x)p(x)dx=\sum _{i=0}^{N}w_{i}p(x_{i})$

holds for any polynomial $p(x)$ of degree $2N+1$ or less. Typically, the weight function $w(x)$ and ranges $a,b$ are chosen for a specific problem, and leads to one of the different forms of the quadrature. To apply this to the pseudo-spectral method, we choose basis functions $\phi _{n}(x)={\sqrt {w(x)}}P_{n}(x)$ , with $P_{n}$ being a polynomial of degree n with the property

$\int _{a}^{b}w(x)P_{n}(x)P_{m}(x)dx=\delta _{mn}.$

Under these conditions, the $\phi _{n}$ form an orthonormal basis with respect to the scalar product $\langle f,g\rangle =\int _{a}^{b}f(x){\overline {g(x)}}dx$ . This basis, together with the quadrature points can then be used for the pseudo-spectral method.

For the discussion of the error, note that if f is well represented by $N_{f}$ basis functions and V is well represented by a polynomial of degree $N_{V}$ , their product can be expanded in the first $N_{f}+N_{V}$ basis functions, and the pseudo-spectral method will give accurate results for that many basis functions.

Such polynomials occur naturally in several standard problems. For example, the quantum harmonic oscillator is ideally expanded in Hermite polynomials, and Jacobi-polynomials can be used to define the associated Legendre functions typically appearing in rotational problems.
