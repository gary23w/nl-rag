---
title: "Domain decomposition methods"
source: https://en.wikipedia.org/wiki/Domain_decomposition_methods
domain: multigrid-methods
license: CC-BY-SA-4.0
tags: multigrid method, gauss-seidel method, successive over-relaxation, domain decomposition
fetched: 2026-07-02
---

# Domain decomposition methods

In mathematics, numerical analysis, and numerical partial differential equations, **domain decomposition methods** solve a boundary value problem by splitting it into smaller boundary value problems on subdomains and iterating to coordinate the solution between adjacent subdomains. A coarse problem with one or few unknowns per subdomain is used to further coordinate the solution between the subdomains globally. The problems on the subdomains are independent, which makes domain decomposition methods suitable for parallel computing. Domain decomposition methods are typically used as preconditioners for Krylov space iterative methods, such as the conjugate gradient method, GMRES, and LOBPCG.

In overlapping domain decomposition methods, the subdomains overlap by more than the interface. Overlapping domain decomposition methods include the Schwarz alternating method and the additive Schwarz method. Many domain decomposition methods can be written and analyzed as a special case of the abstract additive Schwarz method.

In non-overlapping methods, the subdomains intersect only on their interface. In primal methods, such as Balancing domain decomposition and BDDC, the continuity of the solution across subdomain interface is enforced by representing the value of the solution on all neighboring subdomains by the same unknown. In dual methods, such as FETI, the continuity of the solution across the subdomain interface is enforced by Lagrange multipliers. The FETI-DP method is hybrid between a dual and a primal method.

Non-overlapping domain decomposition methods are also called **iterative substructuring methods**.

Mortar methods are discretization methods for partial differential equations, which use separate discretization on nonoverlapping subdomains. The meshes on the subdomains do not match on the interface, and the equality of the solution is enforced by Lagrange multipliers, judiciously chosen to preserve the accuracy of the solution. In the engineering practice in the finite element method, continuity of solutions between non-matching subdomains is implemented by multiple-point constraints.

Finite element simulations of moderate size models require solving linear systems with millions of unknowns. Several hours per time step is an average sequential run time, therefore, parallel computing is a necessity. Domain decomposition methods embody large potential for a parallelization of the finite element methods, and serve a basis for distributed, parallel computations.

## Applications in Computer Graphics

Domain decomposition methods have been successfully applied to problems ranging from fluid dynamics to elastic simulations. Several studies investigated the decomposition of computational or discretization domains into multiple subdomains and analyzed the resulting discretized couplings independently. The standard and optimized Schwarz methods have been used also in the context of mesh smoothing, concretely in the process of mean curvature flow for general polygonal meshes.

## Example 1: 1D Linear BVP

${\begin{cases}u''(x)=u(x),\\u(0)=0,\\u(1)=1.\end{cases}}$ The exact solution is: $u(x)={\frac {e^{x}-e^{-x}}{e^{1}-e^{-1}}}$ Subdivide the domain into two subdomains, one from $\left[0,{\tfrac {1}{2}}\right]$ and another from $\left[{\tfrac {1}{2}},1\right]$ . In the left subdomain define the interpolating function $v_{1}(x)$ and in the right define $v_{2}(x)$ . At the interface between these two subdomains the following interface conditions shall be imposed: ${\begin{aligned}v_{1}{\left({\frac {1}{2}}\right)}&=v_{2}{\left({\frac {1}{2}}\right)}\\v_{1}'{\left({\frac {1}{2}}\right)}&=v_{2}'{\left({\frac {1}{2}}\right)}\end{aligned}}$ Let the interpolating functions be defined as: ${\begin{aligned}v_{1}(x)&=\sum _{n=0}^{N}u_{n}T_{n}(y_{1}(x))\\v_{2}(x)&=\sum _{n=0}^{N}u_{n+N}T_{n}(y_{2}(x))\\y_{1}(x)&=4x-1\\y_{2}(x)&=4x-3\end{aligned}}$ Where $T_{n}(y)$ is the nth cardinal function of the Chebyshev polynomials of the first kind with input argument y.

If *N*=4 then the following approximation is obtained by this scheme: ${\begin{aligned}u_{1}&=0.06236,&u_{2}&=0.21495,\\u_{3}&=0.37428,&u_{4}&=0.44341,\\u_{5}&=0.51492,&u_{6}&=0.69972,\\u_{7}&=0.90645.\end{aligned}}$ This was obtained with the following MATLAB code.

```mw
clear all
N = 4;
a1 = 0; b1 = 1/2; 

[T D1 D2 E1 E2 x xsub] = cheb(N,a1,b1); % the diff matrices on [0,1/2] are the same
%as those on [1/2 1].
I = eye(N+1);
H = D2-I;
H1 = [[1 zeros(1,N)]; H(2:end-1,:); [zeros(1,N) 1]];
H1 = [H1 [zeros(N,N+1); -[1 zeros(1,N)]]];
H2 = [D1(1,:); H(2:end-1,:); [zeros(1,N) 1]];
H2 = [[-D1(N+1,:); zeros(N,N+1)] H2];
K = [H1; H2];
F = [zeros(2*N+1,1); 1];
u = K\F;
xx = -cos(pi*(0:N)'/N);
x1 = 1/4*(xx+1); x2 = 1/4*(xx+3);
x = [x1; x2];
uex = (exp(x)-exp(-x))./(exp(1)-exp(-1));
```
