---
title: "Dirichlet problem"
source: https://en.wikipedia.org/wiki/Dirichlet_problem
domain: greens-functions
license: CC-BY-SA-4.0
tags: green's function, fundamental solution, method of images, propagator function
fetched: 2026-07-02
---

# Dirichlet problem

In mathematics, a **Dirichlet problem** asks for a function which solves a specified partial differential equation (PDE) in the interior of a given region that takes prescribed values on the boundary of the region.

The Dirichlet problem can be solved for many PDEs, although originally it was posed for Laplace's equation. In that case the problem can be stated as follows:

Given a function

f

that has values everywhere on the boundary of a region in

$\mathbb {R} ^{n}$

, is there a unique

continuous function

u

twice continuously differentiable in the interior and continuous on the boundary, such that

u

is

harmonic

in the interior and

$u=f$

on the boundary?

This requirement is called the Dirichlet boundary condition. The main issue is to prove the existence of a solution; uniqueness can be proven using the maximum principle.

## History

The Dirichlet problem goes back to George Green, who studied the problem on general domains with general boundary conditions in his *Essay on the Application of Mathematical Analysis to the Theories of Electricity and Magnetism*, published in 1828. He reduced the problem into a problem of constructing what we now call Green's functions, and argued that Green's function exists for any domain. His methods were not rigorous by today's standards, but the ideas were highly influential in the subsequent developments.

The next steps in the study of the Dirichlet's problem were taken by Karl Friedrich Gauss, William Thomson (Lord Kelvin) and Peter Gustav Lejeune Dirichlet, after whom the problem was named, and the solution to the problem (at least for the ball) using the Poisson kernel was known to Dirichlet (judging by his 1850 paper submitted to the Prussian academy). Lord Kelvin and Dirichlet suggested a solution to the problem by a variational method based on the minimization of "Dirichlet's energy".

According to Hans Freudenthal (in the *Dictionary of Scientific Biography*, vol. 11), Bernhard Riemann was the first mathematician who solved this variational problem based on a method which he called Dirichlet's principle. The existence of a unique solution is very plausible by the "physical argument": any charge distribution on the boundary should, by the laws of electrostatics, determine an electrical potential as solution. However, Karl Weierstrass found a flaw in Riemann's argument, and a rigorous proof of existence was found only in 1900 by David Hilbert, using his direct method in the calculus of variations. It turns out that the existence of a solution depends delicately on the smoothness of the boundary and the prescribed data.

## General solution

For a domain D having a sufficiently smooth boundary $\partial D$ , the general solution to the Dirichlet problem is given by

$u(x)=\int _{\partial D}\nu (s){\frac {\partial G(x,s)}{\partial n}}\,ds,$

where $G(x,y)$ is the Green's function for the partial differential equation, and

${\frac {\partial G(x,s)}{\partial n}}={\widehat {n}}\cdot \nabla _{s}G(x,s)=\sum _{i}n_{i}{\frac {\partial G(x,s)}{\partial s_{i}}}$

is the derivative of the Green's function along the inward-pointing unit normal vector ${\widehat {n}}$ . The integration is performed on the boundary, with measure $ds$ . The function $\nu (s)$ is given by the unique solution to the Fredholm integral equation of the second kind,

$f(x)=-{\frac {\nu (x)}{2}}+\int _{\partial D}\nu (s){\frac {\partial G(x,s)}{\partial n}}\,ds.$

The Green's function to be used in the above integral is one which vanishes on the boundary:

$G(x,s)=0$

for $s\in \partial D$ and $x\in D$ . Such a Green's function is usually a sum of the free-field Green's function and a harmonic solution to the differential equation.

### Existence

The Dirichlet problem for harmonic functions always has a solution, and that solution is unique, when the boundary is sufficiently smooth and $f(s)$ is continuous. More precisely, it has a solution when

$\partial D\in C^{1,\alpha }$

for some $\alpha \in (0,1)$ , where $C^{1,\alpha }$ denotes the Hölder condition.

## Example: the unit disk in two dimensions

In some simple cases the Dirichlet problem can be solved explicitly. For example, the solution to the Dirichlet problem for the unit disk in **R**2 is given by the Poisson integral formula.

If f is a continuous function on the boundary $\partial D$ of the open unit disk D , then the solution to the Dirichlet problem is $u(z)$ given by

$u(z)={\begin{cases}\displaystyle {\frac {1}{2\pi }}\int _{0}^{2\pi }f(e^{i\psi }){\frac {1-|z|^{2}}{|1-ze^{-i\psi }|^{2}}}\,d\psi &{\text{if }}z\in D,\\f(z)&{\text{if }}z\in \partial D.\end{cases}}$

The solution u is continuous on the closed unit disk ${\bar {D}}$ and harmonic on $D.$

The integrand is known as the Poisson kernel; this solution follows from the Green's function in two dimensions:

$G(z,x)=-{\frac {1}{2\pi }}\log |z-x|+\gamma (z,x),$

where $\gamma (z,x)$ is harmonic ( $\Delta _{x}\gamma (z,x)=0$ ) and chosen such that $G(z,x)=0$ for $x\in \partial D$ .

## Methods of solution

For bounded domains, the Dirichlet problem can be solved using the Perron method, which relies on the maximum principle for subharmonic functions. This approach is described in many text books. It is not well-suited to describing smoothness of solutions when the boundary is smooth. Another classical Hilbert space approach through Sobolev spaces does yield such information.

The solution of the Dirichlet problem using Sobolev spaces for planar domains can be used to prove the smooth version of the Riemann mapping theorem. Bell (1992) has outlined a different approach for establishing the smooth Riemann mapping theorem, based on the reproducing kernels of Szegő and Bergman, and in turn used it to solve the Dirichlet problem. The classical methods of potential theory allow the Dirichlet problem to be solved directly in terms of integral operators, for which the standard theory of compact and Fredholm operators is applicable. The same methods work equally for the Neumann problem.

## Generalizations

Dirichlet problems are typical of elliptic partial differential equations, and potential theory, and the Laplace equation in particular. Other examples include the biharmonic equation and related equations in elasticity theory.

They are one of several types of classes of PDE problems defined by the information given at the boundary, including Neumann problems and Cauchy problems.

## Example: equation of a finite string attached to one moving wall

Consider the Dirichlet problem for the wave equation describing a string attached between walls with one end attached permanently and the other moving with the constant velocity i.e. the d'Alembert equation on the triangular region of the Cartesian product of the space and the time:

${\frac {\partial ^{2}}{\partial t^{2}}}u(x,t)-{\frac {\partial ^{2}}{\partial x^{2}}}u(x,t)=0,$

$u(0,t)=0,$

$u(\lambda t,t)=0.$

As one can easily check by substitution, the solution fulfilling the first condition is

$u(x,t)=f(t-x)-f(x+t).$

Additionally we want

$f(t-\lambda t)-f(\lambda t+t)=0.$

Substituting

$\tau =(\lambda +1)t,$

we get the condition of self-similarity

$f(\gamma \tau )=f(\tau ),$

where

$\gamma ={\frac {1-\lambda }{\lambda +1}}.$

It is fulfilled, for example, by the composite function

$\sin[\log(e^{2\pi }x)]=\sin[\log(x)]$

with

$\lambda =e^{2\pi }=1^{-i},$

thus in general

$f(\tau )=g[\log(\gamma \tau )],$

where g is a periodic function with a period $\log(\gamma )$ :

$g[\tau +\log(\gamma )]=g(\tau ),$

and we get the general solution

$u(x,t)=g[\log(t-x)]-g[\log(x+t)].$
