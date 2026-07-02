---
title: "Method of characteristics"
source: https://en.wikipedia.org/wiki/Method_of_characteristics
domain: partial-differential-equations-theory
license: CC-BY-SA-4.0
tags: partial differential equation, heat equation, wave equation, sobolev space
fetched: 2026-07-02
---

# Method of characteristics

In mathematics, the **method of characteristics** is a technique for solving particular partial differential equations. Typically, it applies to first-order equations, though in general characteristic curves can also be found for hyperbolic and parabolic partial differential equations. The method is to reduce a partial differential equation (PDE) to a family of ordinary differential equations (ODEs) along which the solution can be integrated from some initial data given on a suitable hypersurface.

## Characteristics of first-order partial differential equation

For a first-order PDE, the method of characteristics discovers so called **characteristic curves** along which the PDE becomes an ODE. Once the ODE is found, it can be solved along the characteristic curves and transformed into a solution for the original PDE.

### Two-dimensional quasilinear PDE

For the sake of simplicity, we initially direct our attention to the case of a function of two independent variables *x* and *y*. Consider a quasilinear PDE of the form

| $a(x,y,u){\frac {\partial u}{\partial x}}+b(x,y,u){\frac {\partial u}{\partial y}}=c(x,y,u).$ |   | 1 |
|---|---|---|

For a differentiable function $(x,y)\mapsto u(x,y)$ , consider the graph of *u*, which is the set $\operatorname {gph} (u)=\{(x,y,z)\in \mathbb {R} ^{3}\mid z=u(x,y)\}$ A normal vector to $\operatorname {gph} (u)$ is given by

$n(x,y)=\left({\frac {\partial u}{\partial x}}(x,y),{\frac {\partial u}{\partial y}}(x,y),-1\right).$

Consider the vector field

| $(x,y,z)\mapsto {\begin{bmatrix}a(x,y,z)\\b(x,y,z)\\c(x,y,z)\end{bmatrix}}.$ |   | 2 |
|---|---|---|

The dot product of the vector field (**2**) with the normal vector to $\operatorname {gph} (u)$ at each $(x,y,u(x,y))\in \operatorname {gph} (u)$ is ${\begin{bmatrix}{\dfrac {\partial u}{\partial x}}(x,y)\\{\dfrac {\partial u}{\partial y}}(x,y)\\-1\end{bmatrix}}\cdot {\begin{bmatrix}a{\big (}x,y,u(x,y){\big )}\\b{\big (}x,y,u(x,y){\big )}\\c{\big (}x,y,u(x,y){\big )}\end{bmatrix}}=a{\big (}x,y,u(x,y){\big )}{\frac {\partial u}{\partial x}}(x,y)+b{\big (}x,y,u(x,y){\big )}{\frac {\partial u}{\partial y}}(x,y)-c{\big (}x,y,u(x,y){\big )}.$

Comparing the right-hand side of the above equation with (**1**), it is evident the following statements are equivalent:

- the right-hand side of the above equation is zero;
- u is a solution to (**1**);
- the vector field (**2**) is orthogonal to the normal vectors of $\operatorname {gph} (u)$ at every point $(x,y,z)\in \operatorname {gph} (u)$ ;
- the vector field (**2**) is tangent to the surface $\operatorname {gph} (u)$ at every point $(x,y,z)\in \operatorname {gph} (u)$ ;

In other words, the graph of the solution to (**1**) is the union of integral curves of the vector field (**2**). Each integral curve is called a *characteristic curve* of the PDE (**1**) equation and follow as the solutions of the *characteristic equations*:

$\left\{{\begin{aligned}{\dfrac {dx}{dt}}&=a(x,y,z),\\[4pt]{\dfrac {dy}{dt}}&=b(x,y,z),\\[4pt]{\dfrac {dz}{dt}}&=c(x,y,z).\end{aligned}}\right.$

A parametrization invariant form of the *Lagrange–Charpit equations* is:

${\frac {dx}{a(x,y,z)}}={\frac {dy}{b(x,y,z)}}={\frac {dz}{c(x,y,z)}}.$

### N-dimensional linear and quasilinear PDE

Consider now a PDE of the form

$\sum _{i=1}^{n}a_{i}(x_{1},\dots ,x_{n},u){\frac {\partial u}{\partial x_{i}}}=c(x_{1},\dots ,x_{n},u).$

For this PDE to be linear, the coefficients *a**i* may be functions of the spatial variables only, and independent of *u*. For it to be quasilinear, *a**i* may also depend on the value of the function, but not on any derivatives. The distinction between these two cases is inessential for the discussion here.

For a linear or quasilinear PDE, the characteristic curves are given parametrically by

$(x_{1},\dots ,x_{n},u)=(X_{1}(s),\dots ,X_{n}(s),U(s))$

$u(\mathbf {X} (s))=U(s)$

for some univariate functions $s\mapsto (X_{i}(s))_{i},U(s)$ of one real variable s satisfying the following system of ordinary differential equations

| $X_{i}'=a_{i}(X_{1},\dots ,X_{n},U){\text{ for }}i=1,\dotsc ,n$ |   | 4 |
|---|---|---|

| $U'=c(X_{1},\dots ,X_{n},U).$ |   | 5 |
|---|---|---|

Equations (**4**) and (**5**) give the characteristics of the PDE.

| Proof for quasilinear case |
|---|
| In the quasilinear case, the use of the method of characteristics is justified by Grönwall's inequality. The above equation may be written as $\mathbf {a} (\mathbf {x} ,u)\cdot \nabla u(\mathbf {x} )=c(\mathbf {x} ,u)$ We must distinguish between the solutions to the ODE and the solutions to the PDE, which we do not know are equal *a priori.* Letting capital letters be the solutions to the ODE we find $\mathbf {X} '(s)=\mathbf {a} (\mathbf {X} (s),U(s))$ $U'(s)=c(\mathbf {X} (s),U(s))$ Examining $\Delta (s)=\|u(\mathbf {X} (s))-U(s)\|^{2}$ , we find, upon differentiating that $\Delta '(s)=2{\big (}u(\mathbf {X} (s))-U(s){\big )}{\Big (}\mathbf {X} '(s)\cdot \nabla u(\mathbf {X} (s))-U'(s){\Big )}$ which is the same as $\Delta '(s)=2{\big (}u(\mathbf {X} (s))-U(s){\big )}{\Big (}\mathbf {a} (\mathbf {X} (s),U(s))\cdot \nabla u(\mathbf {X} (s))-c(\mathbf {X} (s),U(s)){\Big )}$ We cannot conclude the above is 0 as we would like, since the PDE only guarantees us that this relationship is satisfied for $u(\mathbf {x} )$ , $\mathbf {a} (\mathbf {x} ,u)\cdot \nabla u(\mathbf {x} )=c(\mathbf {x} ,u)$ , and we do not yet know that $U(s)=u(\mathbf {X} (s))$ . However, we can see that $\Delta '(s)=2{\big (}u(\mathbf {X} (s))-U(s){\big )}{\Big (}\mathbf {a} (\mathbf {X} (s),U(s))\cdot \nabla u(\mathbf {X} (s))-c(\mathbf {X} (s),U(s))-{\big (}\mathbf {a} (\mathbf {X} (s),u(\mathbf {X} (s)))\cdot \nabla u(\mathbf {X} (s))-c(\mathbf {X} (s),u(\mathbf {X} (s))){\big )}{\Big )}$ since by the PDE, the last term is 0. This equals $\Delta '(s)=2{\big (}u(\mathbf {X} (s))-U(s){\big )}{\Big (}{\big (}\mathbf {a} (\mathbf {X} (s),U(s))-\mathbf {a} (\mathbf {X} (s),u(\mathbf {X} (s))){\big )}\cdot \nabla u(\mathbf {X} (s))-{\big (}c(\mathbf {X} (s),U(s))-c(\mathbf {X} (s),u(\mathbf {X} (s))){\big )}{\Big )}$ By the triangle inequality, we have $\|\Delta '(s)\|\leq 2{\big \|}u(\mathbf {X} (s))-U(s){\big \|}{\Big (}{\big \\|}\mathbf {a} (\mathbf {X} (s),U(s))-\mathbf {a} (\mathbf {X} (s),u(\mathbf {X} (s))){\big \\|}\ \\|\nabla u(\mathbf {X} (s))\\|+{\big \|}c(\mathbf {X} (s),U(s))-c(\mathbf {X} (s),u(\mathbf {X} (s))){\big \|}{\Big )}$ Assuming $\mathbf {a} ,c$ are at least $C^{1}$ , we can bound this for small times. Choose a neighborhood $\Omega$ around $\mathbf {X} (0),U(0)$ small enough such that $\mathbf {a} ,c$ are locally Lipschitz. By continuity, $(\mathbf {X} (s),U(s))$ will remain in $\Omega$ for small enough s . Since $U(0)=u(\mathbf {X} (0))$ , we also have that $(\mathbf {X} (s),u(\mathbf {X} (s)))$ will be in $\Omega$ for small enough s by continuity. So, $(\mathbf {X} (s),U(s))\in \Omega$ and $(\mathbf {X} (s),u(\mathbf {X} (s)))\in \Omega$ for $s\in [0,s_{0}]$ . Additionally, $\\|\nabla u(\mathbf {X} (s))\\|\leq M$ for some $M\in \mathbb {R}$ for $s\in [0,s_{0}]$ by compactness. From this, we find the above is bounded as $\|\Delta '(s)\|\leq C\|u(\mathbf {X} (s))-U(s)\|^{2}=C\|\Delta (s)\|$ for some $C\in \mathbb {R}$ . It is a straightforward application of Grönwall's Inequality to show that since $\Delta (0)=0$ we have $\Delta (s)=0$ for as long as this inequality holds. We have some interval $[0,\varepsilon )$ such that $u(X(s))=U(s)$ in this interval. Choose the largest $\varepsilon$ such that this is true. Then, by continuity, $U(\varepsilon )=u(\mathbf {X} (\varepsilon ))$ . Provided the ODE still has a solution in some interval after $\varepsilon$ , we can repeat the argument above to find that $u(X(s))=U(s)$ in a larger interval. Thus, so long as the ODE has a solution, we have $u(X(s))=U(s)$ . |

### Fully nonlinear PDE

Consider the partial differential equation

| $F(x_{1},\dots ,x_{n},u,p_{1},\dots ,p_{n})=0$ |   | 6 |
|---|---|---|

where the variables *p*i are shorthand for the partial derivatives

$p_{i}={\frac {\partial u}{\partial x_{i}}}.$

Let $s\mapsto (x_{1}(s),\dots ,x_{n}(s),u(s),p_{1}(s),\dots ,p_{n}(s))$ be a curve in **R**2n+1. Suppose that *u* is any solution, and that

$u(s)=u(x_{1}(s),\dots ,x_{n}(s)).$

The derivatives with respect to s of $x_{i},$ $u,$ and $p_{i}$ are written as ${\dot {x}}_{i},$ , ${\dot {u}},$ and ${\dot {p}}_{i},$ respectively. Along a solution, differentiating (**6**) with respect to *s* gives

$\sum _{i}(F_{x_{i}}+F_{u}p_{i}){\dot {x}}_{i}+\sum _{i}F_{p_{i}}{\dot {p}}_{i}=0$

${\dot {u}}-\sum _{i}p_{i}{\dot {x}}_{i}=0$

$\sum _{i}({\dot {x}}_{i}dp_{i}-{\dot {p}}_{i}dx_{i})=0.$

The second equation follows from applying the chain rule to a solution *u*, and the third follows by taking an exterior derivative of the relation $du-\sum _{i}p_{i}\,dx_{i}=0$ . Manipulating these equations gives

$\left\{{\begin{aligned}{\dot {x}}_{i}&=\lambda F_{p_{i}},\\[5pt]{\dot {p}}_{i}&=-\lambda (F_{x_{i}}+F_{u}p_{i}),\\[5pt]{\dot {u}}&=\lambda \sum _{i}p_{i}F_{p_{i}}\end{aligned}}\right.$

where λ is a constant. Writing these equations more symmetrically, one obtains the Lagrange–Charpit equations for the characteristic

${\frac {{\dot {x}}_{i}}{F_{p_{i}}}}=-{\frac {{\dot {p}}_{i}}{F_{x_{i}}+F_{u}p_{i}}}={\frac {\dot {u}}{\sum p_{i}F_{p_{i}}}}.$

Geometrically, the method of characteristics in the fully nonlinear case can be interpreted as requiring that the Monge cone of the differential equation should everywhere be tangent to the graph of the solution.

## Example

As an example, consider the advection equation (this example assumes familiarity with PDE notation, and solutions to basic ODEs).

$a{\frac {\partial u}{\partial x}}+{\frac {\partial u}{\partial t}}=0$

where a is constant and u is a function of x and t . We want to transform this linear first-order PDE into an ODE along the appropriate curve; i.e. something of the form

${\frac {d}{ds}}u(x(s),t(s))=F(u,x(s),t(s)),$

where $(x(s),t(s))$ is a characteristic line. First, we find

${\frac {d}{ds}}u(x(s),t(s))={\frac {\partial u}{\partial x}}{\frac {dx}{ds}}+{\frac {\partial u}{\partial t}}{\frac {dt}{ds}}$

by the chain rule. Now, if we set ${\frac {dx}{ds}}=a$ and ${\frac {dt}{ds}}=1$ we get

$a{\frac {\partial u}{\partial x}}+{\frac {\partial u}{\partial t}}$

which is the left hand side of the PDE we started with. Thus

${\frac {d}{ds}}u=a{\frac {\partial u}{\partial x}}+{\frac {\partial u}{\partial t}}=0.$

So, along the characteristic line $(x(s),t(s))$ , the original PDE becomes the ODE $u_{s}=F(u,x(s),t(s))=0$ . That is to say that along the characteristics, the solution is constant. Thus, $u(x_{s},t_{s})=u(x_{0},0)$ where $(x_{s},t_{s})\,$ and $(x_{0},0)$ lie on the same characteristic. Therefore, to determine the general solution, it is enough to find the characteristics by solving the characteristic system of ODEs:

- ${\frac {dt}{ds}}=1$ , letting $t(0)=0$ we know $t=s$ ,
- ${\frac {dx}{ds}}=a$ , letting $x(0)=x_{0}$ we know $x=as+x_{0}=at+x_{0}$ ,
- ${\frac {du}{ds}}=0$ , letting $u(0)=f(x_{0})$ we know $u(x(t),t)=f(x_{0})=f(x-at)$ .

In this case, the characteristic lines are straight lines with slope a , and the value of u remains constant along any characteristic line.

## Characteristics of linear differential operators

Let *X* be a differentiable manifold and *P* a linear differential operator

$P:C^{\infty }(X)\to C^{\infty }(X)$

of order *k*. In a local coordinate system *x**i*,

$P=\sum _{|\alpha |\leq k}P^{\alpha }(x){\frac {\partial }{\partial x^{\alpha }}}$

in which *α* denotes a multi-index. The principal symbol of *P*, denoted *σ**P*, is the function on the cotangent bundle T∗*X* defined in these local coordinates by

$\sigma _{P}(x,\xi )=\sum _{|\alpha |=k}P^{\alpha }(x)\xi _{\alpha }$

where the *ξ**i* are the fiber coordinates on the cotangent bundle induced by the coordinate differentials *dx**i*. Although this is defined using a particular coordinate system, the transformation law relating the *ξ**i* and the *x**i* ensures that *σ**P* is a well-defined function on the cotangent bundle.

The function *σ**P* is homogeneous of degree *k* in the *ξ* variable. The zeros of *σ**P*, away from the zero section of T∗*X*, are the characteristics of *P*. A hypersurface of *X* defined by the equation *F*(*x*) = *c* is called a characteristic hypersurface at *x* if

$\sigma _{P}(x,dF(x))=0.$

Invariantly, a characteristic hypersurface is a hypersurface whose conormal bundle is in the characteristic set of *P*.

## Qualitative analysis of characteristics

Characteristics are also a powerful tool for gaining qualitative insight into a PDE.

One can use the crossings of the characteristics to find shock waves for potential flow in a compressible fluid. Intuitively, we can think of each characteristic line implying a solution to u along itself. Thus, when two characteristics cross, the function becomes multi-valued resulting in a non-physical solution. Physically, this contradiction is removed by the formation of a shock wave, a tangential discontinuity or a weak discontinuity and can result in non-potential flow, violating the initial assumptions.

Characteristics may fail to cover part of the domain of the PDE. This is called a rarefaction, and indicates the solution typically exists only in a weak, i.e. integral equation, sense.

The direction of the characteristic lines indicates the flow of values through the solution, as the example above demonstrates. This kind of knowledge is useful when solving PDEs numerically as it can indicate which finite difference scheme is best for the problem.
