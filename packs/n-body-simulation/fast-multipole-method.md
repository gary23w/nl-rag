---
title: "Fast multipole method"
source: https://en.wikipedia.org/wiki/Fast_multipole_method
domain: n-body-simulation
license: CC-BY-SA-4.0
tags: n-body simulation, barnes-hut simulation, fast multipole method, astrophysical plasma
fetched: 2026-07-02
---

# Fast multipole method

The **fast multipole method** (**FMM**) is a numerical technique that was developed to speed up the calculation of long-ranged forces in the *n*-body problem. It does this by expanding the system Green's function using a multipole expansion, which allows one to group sources that lie close together and treat them as if they were a single source.

The FMM has also been applied in accelerating the iterative solver in the method of moments (MoM) as applied to computational electromagnetics problems, and in particular in computational bioelectromagnetism. The FMM was first introduced in this manner by Leslie Greengard and Vladimir Rokhlin Jr. and is based on the multipole expansion of the vector Helmholtz equation. By treating the interactions between far-away basis functions using the FMM, the corresponding matrix elements do not need to be explicitly stored, resulting in a significant reduction in required memory. If the FMM is then applied in a hierarchical manner, it can improve the complexity of matrix-vector products in an iterative solver from ${\mathcal {O}}(N^{2})$ to ${\mathcal {O}}(N)$ in finite arithmetic, i.e., given a tolerance $\varepsilon$ , the matrix-vector product is guaranteed to be within a tolerance $\varepsilon .$ The dependence of the complexity on the tolerance $\varepsilon$ is ${\mathcal {O}}(\log(1/\varepsilon ))$ , i.e., the complexity of FMM is ${\mathcal {O}}(N\log(1/\varepsilon ))$ . This has expanded the area of applicability of the MOM to far greater problems than were previously possible.

The FMM, introduced by Rokhlin Jr. and Greengard has been said to be one of the top ten algorithms of the 20th century. The FMM algorithm reduces the complexity of matrix-vector multiplication involving a certain type of dense matrix which can arise out of many physical systems.

The FMM has also been applied for efficiently treating the Coulomb interaction in the Hartree–Fock method and density functional theory calculations in quantum chemistry.

## Sketch of the algorithm

In its simplest form, the fast multipole method seeks to evaluate the following function: $f(y)=\sum _{\alpha =1}^{N}{\frac {\phi _{\alpha }}{y-x_{\alpha }}},$ where $x_{\alpha }\in [-1,1]$ are a set of poles, and $\phi _{\alpha }\in \mathbb {C}$ are the corresponding pole weights on a set of points $\{y_{1},\ldots ,y_{M}\}$ with $y_{\beta }\in [-1,1]$ . This is the one-dimensional form of the problem, but the algorithm can be easily generalized to multiple dimensions and kernels other than $(y-x)^{-1}$ .

Naively, evaluating $f(y)$ on M points requires ${\mathcal {O}}(MN)$ operations. The crucial observation behind the fast multipole method is that if the distance between y and x is large enough, then $(y-x)^{-1}$ is well-approximated by a polynomial. Specifically, let $-1<t_{1}<\ldots <t_{p}<1$ be the Chebyshev nodes of order $p\geq 2,$ and let $u_{1}(y),\ldots ,u_{p}(y)$ be the corresponding Lagrange basis polynomials. One can show that the interpolating polynomial ${\frac {1}{y-x}}=\sum _{i=1}^{p}{\frac {1}{t_{i}-x}}u_{i}(y)+\epsilon _{p}(y)$ converges quickly with polynomial order, $|\epsilon _{p(y)}|<5^{-p}$ , provided that the pole is far enough away from the region of interpolation, $|x|\geq 3$ and $|y|<1$ . This is known as the "local expansion".

The speed-up of the fast multipole method derives from this interpolation: provided that all the poles are "far away", we evaluate the sum only on the Chebyshev nodes at a cost of ${\mathcal {O}}(Np)$ , and then interpolate it onto all the desired points at a cost of ${\mathcal {O}}(Mp)$ : $\sum _{\alpha =1}^{N}{\frac {\phi _{\alpha }}{y_{\beta }-x_{\alpha }}}=\sum _{i=1}^{p}u_{i}(y_{\beta })\sum _{\alpha =1}^{N}{\frac {1}{t_{i}-x_{\alpha }}}\phi _{\alpha }.$

Since $p=-\log _{5}\epsilon$ , where $\epsilon$ is the numerical tolerance, the total cost is ${\mathcal {O}}{\big (}(M+N)\log(1/\epsilon ){\big )}$ .

To ensure that the poles are indeed well-separated, one recursively subdivides the unit interval such that only ${\mathcal {O}}(p)$ poles end up in each interval. One then uses the explicit formula within each interval and interpolation for all intervals that are well-separated. This does not spoil the scaling, since one needs at most $\log(1/\epsilon )$ levels within the given tolerance.
