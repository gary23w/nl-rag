---
title: "Spectral method"
source: https://en.wikipedia.org/wiki/Spectral_method
domain: spectral-methods
license: CC-BY-SA-4.0
tags: spectral method, pseudo-spectral method, chebyshev polynomials, collocation method
fetched: 2026-07-02
---

# Spectral method

**Spectral methods** are a class of techniques used in applied mathematics and scientific computing to numerically solve certain differential equations. The idea is to write the solution of the differential equation as a sum of certain "basis functions" (for example, as a Fourier series which is a sum of sinusoids) and then to choose the coefficients in the sum in order to satisfy the differential equation as well as possible.

Spectral methods and finite-element methods are closely related and built on the same ideas; the main difference between them is that spectral methods use basis functions that are generally nonzero over the whole domain, while finite element methods use basis functions that are nonzero only on small subdomains (compact support). Consequently, spectral methods connect variables *globally* while finite elements do so *locally*. Partially for this reason, spectral methods have excellent error properties, with the so-called "exponential convergence" being the fastest possible, when the solution is smooth. However, there are no known three-dimensional single-domain spectral shock capturing results (shock waves are not smooth). In the finite-element community, a method where the degree of the elements is very high or increases as the grid parameter *h* increases is sometimes called a spectral-element method.

Spectral methods can be used to solve differential equations (PDEs, ODEs, eigenvalue, etc) and optimization problems. When applying spectral methods to time-dependent PDEs, the solution is typically written as a sum of basis functions with time-dependent coefficients; substituting this in the PDE yields a system of ODEs in the coefficients which can be solved using any numerical method for ODEs. Eigenvalue problems for ODEs are similarly converted to matrix eigenvalue problems .

Spectral methods were developed in a long series of papers by Steven Orszag starting in 1969 including, but not limited to, Fourier series methods for periodic geometry problems, polynomial spectral methods for finite and unbounded geometry problems, pseudospectral methods for highly nonlinear problems, and spectral iteration methods for fast solution of steady-state problems. The implementation of the spectral method is normally accomplished either with collocation or a Galerkin or a Tau approach . For very small problems, the spectral method is unique in that solutions may be written out symbolically, yielding a practical alternative to series solutions for differential equations.

Spectral methods can be computationally less expensive and easier to implement than finite element methods; they shine best when high accuracy is sought in simple domains with smooth solutions. However, because of their global nature, the matrices associated with step computation are dense and computational efficiency will quickly suffer when there are many degrees of freedom (with some exceptions, for example if matrix applications can be written as Fourier transforms). For larger problems and nonsmooth solutions, finite elements will generally work better due to sparse matrices and better modelling of discontinuities and sharp bends.

## Examples of spectral methods

### A concrete, linear example

Here we presume an understanding of basic multivariate calculus and Fourier series. If $g(x,y)$ is a known, complex-valued function of two real variables, and g is periodic in x and y (that is, $g(x,y)=g(x+2\pi ,y)=g(x,y+2\pi )$ ) then we are interested in finding a function *f*(*x*,*y*) so that

$\left({\frac {\partial ^{2}}{\partial x^{2}}}+{\frac {\partial ^{2}}{\partial y^{2}}}\right)f(x,y)=g(x,y)\quad {\text{for all }}x,y$

where the expression on the left denotes the second partial derivatives of *f* in *x* and *y*, respectively. This is the Poisson equation, and can be physically interpreted as some sort of heat conduction problem, or a problem in potential theory, among other possibilities.

If we write *f* and *g* in Fourier series:

${\begin{aligned}f&=:\sum _{j,k}a_{j,k}e^{i(jx+ky)},\\[5mu]g&=:\sum _{j,k}b_{j,k}e^{i(jx+ky)},\end{aligned}}$

and substitute into the differential equation, we obtain this equation:

$\sum _{j,k}-a_{j,k}(j^{2}+k^{2})e^{i(jx+ky)}=\sum _{j,k}b_{j,k}e^{i(jx+ky)}.$

We have exchanged partial differentiation with an infinite sum, which is legitimate if we assume for instance that *f* has a continuous second derivative. By the uniqueness theorem for Fourier expansions, we must then equate the Fourier coefficients term by term, giving

| $a_{j,k}=-{\frac {b_{j,k}}{j^{2}+k^{2}}}$ |   | * |
|---|---|---|

which is an explicit formula for the Fourier coefficients *a**j*,*k*.

With periodic boundary conditions, the Poisson equation possesses a solution only if *b*0,0 = 0. Therefore, we can freely choose *a*0,0 which will be equal to the mean of the resolution. This corresponds to choosing the integration constant.

To turn this into an algorithm, only finitely many frequencies are solved for. This introduces an error which can be shown to be proportional to $h^{n}$ , where $h:=1/n$ and n is the highest frequency treated.

#### Algorithm

1. Compute the Fourier transform (*b**j*,*k*) of *g*.
2. Compute the Fourier transform (*a**j*,*k*) of *f* via the formula (*****).
3. Compute *f* by taking an inverse Fourier transform of (*aj,k*).

Since we're only interested in a finite window of frequencies (of size *n*, say) this can be done using a fast Fourier transform algorithm. Therefore, globally the algorithm runs in time *O*(*n* log *n*).

### Nonlinear example

We wish to solve the forced, transient, nonlinear Burgers' equation using a spectral approach.

Given $u(x,0)$ on the periodic domain $x\in \left[0,2\pi \right)$ , find $u\in {\mathcal {U}}$ such that ${\frac {\partial u}{\partial t}}+u{\frac {\partial u}{\partial x}}=\rho {\frac {\partial ^{2}u}{\partial x^{2}}}+f\quad \forall x\in \left[0,2\pi \right),\forall t>0$ where *ρ* is the viscosity coefficient. In weak conservative form this becomes $\left\langle {\frac {\partial u}{\partial t}},\,v\right\rangle =\left\langle {\frac {\partial }{\partial x}}{\left(-{\frac {u^{2}}{2}}+\rho {\frac {\partial u}{\partial x}}\right)},\,v\right\rangle +\left\langle f,v\right\rangle \quad \forall v\in {\mathcal {V}},\forall t>0$ where following inner product notation. Integrating by parts and using periodicity grants $\left\langle {\frac {\partial u}{\partial t}},v\right\rangle =\left\langle {\frac {u^{2}}{2}}-\rho {\frac {\partial u}{\partial x}},{\frac {\partial v}{\partial x}}\right\rangle +\left\langle f,v\right\rangle \quad \forall v\in {\mathcal {V}},\forall t>0.$

To apply the Fourier–Galerkin method, choose both ${\mathcal {U}}^{N}:={\biggl \{}u:u(x,t)=\sum _{k=-N/2}^{N/2-1}{\hat {u}}_{k}(t)e^{ikx}{\biggr \}}$ and ${\mathcal {V}}^{N}:=\operatorname {span} \left\{e^{ikx}:k\in -{\tfrac {1}{2}}N,\dots ,{\tfrac {1}{2}}N-1\right\}$ where ${\hat {u}}_{k}(t):={\frac {1}{2\pi }}\langle u(x,t),e^{ikx}\rangle$ . This reduces the problem to finding $u\in {\mathcal {U}}^{N}$ such that $\langle \partial _{t}u,e^{ikx}\rangle =\left\langle {\tfrac {1}{2}}u^{2}-\rho \partial _{x}u,\partial _{x}e^{ikx}\right\rangle +\left\langle f,e^{ikx}\right\rangle \quad \forall k\in \left\{-{\tfrac {1}{2}}N,\dots ,{\tfrac {1}{2}}N-1\right\},\forall t>0.$

Using the orthogonality relation $\langle e^{ilx},e^{ikx}\rangle =2\pi \delta _{lk}$ where $\delta _{lk}$ is the Kronecker delta, we simplify the above three terms for each k to see $\left\langle \partial _{t}u,e^{ikx}\right\rangle ={\biggl \langle }\partial _{t}\sum _{l}{\hat {u}}_{l}e^{ilx},e^{ikx}{\biggr \rangle }={\biggl \langle }\sum _{l}\partial _{t}{\hat {u}}_{l}e^{ilx},e^{ikx}{\biggr \rangle }=2\pi \partial _{t}{\hat {u}}_{k},$ $\left\langle f,e^{ikx}\right\rangle ={\biggl \langle }\sum _{l}{\hat {f}}_{\!l}e^{ilx},e^{ikx}{\biggr \rangle }=2\pi {\hat {f}}_{\!k},$ and ${\begin{aligned}\left\langle {\tfrac {1}{2}}u^{2}-\rho \partial _{x}u,\partial _{x}e^{ikx}\right\rangle &={\biggl \langle }{\tfrac {1}{2}}{\Bigl (}\sum _{p}{\hat {u}}_{p}e^{ipx}{\Bigr )}{\Bigl (}\sum _{q}{\hat {u}}_{q}e^{iqx}{\Bigr )}-\rho \partial _{x}\sum _{l}{\hat {u}}_{l}e^{ilx},\partial _{x}e^{ikx}{\biggr \rangle }\\&={\biggl \langle }{\tfrac {1}{2}}\sum _{p}\sum _{q}{\hat {u}}_{p}{\hat {u}}_{q}e^{i\left(p+q\right)x},ike^{ikx}{\biggr \rangle }-{\biggl \langle }\rho i\sum _{l}l{\hat {u}}_{l}e^{ilx},ike^{ikx}{\biggr \rangle }\\&=-{\tfrac {1}{2}}ik{\biggl \langle }\sum _{p}\sum _{q}{\hat {u}}_{p}{\hat {u}}_{q}e^{i\left(p+q\right)x},e^{ikx}{\biggr \rangle }-\rho k{\biggl \langle }\sum _{l}l{\hat {u}}_{l}e^{ilx},e^{ikx}{\biggr \rangle }\\&=-i\pi k\sum _{p+q=k}{\hat {u}}_{p}{\hat {u}}_{q}-2\pi \rho {}k^{2}{\hat {u}}_{k}.\end{aligned}}$

Assemble the three terms for each k to obtain $2\pi {\frac {\partial {\hat {u}}_{k}}{\partial t}}=-i\pi k\sum _{p+q=k}{\hat {u}}_{p}{\hat {u}}_{q}-2\pi \rho {}k^{2}{\hat {u}}_{k}+2\pi {\hat {f}}_{\!k}\quad k\in \left\{-{\tfrac {1}{2}}N,\dots ,{\tfrac {1}{2}}N-1\right\},\forall t>0.$ Dividing through by $2\pi$ , we finally arrive at ${\frac {\partial {\hat {u}}_{k}}{\partial t}}=-{\frac {ik}{2}}\sum _{p+q=k}{\hat {u}}_{p}{\hat {u}}_{q}-\rho {}k^{2}{\hat {u}}_{k}+{\hat {f}}_{\!k}\quad k\in \left\{-{\tfrac {1}{2}}N,\dots ,{\tfrac {1}{2}}N-1\right\},\forall t>0.$ With Fourier transformed initial conditions ${\hat {u}}_{k}(0)$ and forcing ${\hat {f}}_{k}(t)$ , this coupled system of ordinary differential equations may be integrated in time (using, e.g., a Runge Kutta technique) to find a solution. The nonlinear term is a convolution, and there are several transform-based techniques for evaluating it efficiently. See the references by Boyd and Canuto et al. for more details.

## A relationship with the spectral element method

One can show that if g is infinitely differentiable, then the numerical algorithm using Fast Fourier Transforms will converge faster than any polynomial in the grid size h. That is, for any n>0, there is a $C_{n}<\infty$ such that the error is less than $C_{n}h^{n}$ for all sufficiently small values of h . We say that the spectral method is of order n , for every n>0.

Because a spectral element method is a finite element method of very high order, there is a similarity in the convergence properties. However, whereas the spectral method is based on the eigendecomposition of the particular boundary value problem, the finite element method does not use that information and works for arbitrary elliptic boundary value problems.
