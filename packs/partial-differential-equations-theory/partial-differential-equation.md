---
title: "Partial differential equation"
source: https://en.wikipedia.org/wiki/Partial_differential_equation
domain: partial-differential-equations-theory
license: CC-BY-SA-4.0
tags: partial differential equation, heat equation, wave equation, sobolev space
fetched: 2026-07-02
---

# Partial differential equation

In mathematics, a **partial differential equation** (**PDE**) is an equation which involves a multivariable function and one or more of its partial derivatives.

The function is often thought of as an "unknown" that solves the equation. However, it is often impossible to write down explicit formulas for solutions of partial differential equations. Hence there is a vast amount of modern mathematical and scientific research on methods to numerically approximate solutions of partial differential equations using computers. Partial differential equations also occupy a large sector of pure mathematical research, where the focus is on the qualitative features of solutions of various partial differential equations, such as existence, uniqueness, regularity and stability. Among the many open questions are the existence and smoothness of solutions to the Navier–Stokes equations, named as one of the Millennium Prize Problems in 2000.

Partial differential equations occur very widely in mathematically oriented scientific fields, such as physics and engineering. For instance, they are foundational in the modern scientific understanding of sound, heat, diffusion, electrostatics, electrodynamics, thermodynamics, fluid dynamics, elasticity, general relativity, and quantum mechanics (Schrödinger equation, Pauli equation etc.). They also arise from many purely mathematical considerations, such as differential geometry and the calculus of variations; among other notable applications, they are the fundamental tool in the proof of the Poincaré conjecture from geometric topology.

Partly due to this variety of sources, there is a wide spectrum of types of partial differential equations. Many different methods have been developed for dealing with the individual equations which arise. As such, there is no "universal theory" of partial differential equations, with specialist knowledge being divided between several distinct subfields.

Ordinary differential equations can be viewed as a subclass of partial differential equations, corresponding to functions of a single variable. Stochastic partial differential equations and nonlocal equations are widely studied extensions of the "PDE" notion. More classical topics, on which there is still much active research, include elliptic and parabolic partial differential equations, fluid mechanics, Boltzmann equations, and dispersive partial differential equations.

## Introduction and examples

One of the most important partial differential equations, with many applications, is Laplace's equation. For a function *u*(*x*, *y*, *z*) of three variables, Laplace's equation is ${\frac {\partial ^{2}u}{\partial x^{2}}}+{\frac {\partial ^{2}u}{\partial y^{2}}}+{\frac {\partial ^{2}u}{\partial z^{2}}}=0.$ A function that obeys this equation is called a harmonic function. Such functions were widely studied in the 19th century due to their relevance for classical mechanics. For example, the equilibrium temperature distribution of a homogeneous solid is a harmonic function. It is usually a matter of straightforward computation to check whether or not a given function is harmonic. For instance $u(x,y,z)={\frac {1}{\sqrt {x^{2}-2x+y^{2}+z^{2}+1}}},$ $u(x,y,z)=e^{5x}\sin(3y)\cos(4z)$ and $u(x,y,z)=2x^{2}-y^{2}-z^{2}$ are all harmonic, while $u(x,y,z)=\sin(xy)+z$ is not. It may be surprising that these examples of harmonic functions are of such different forms. This is a reflection of the fact that they are not special cases of a "general solution formula" of Laplace's equation. This is in striking contrast to the case of many ordinary differential equations (ODEs), where many introductory textbooks aim to find methods leading to general solutions. For Laplace's equation, as for a large number of partial differential equations, such solution formulas do not exist.

This can also be seen in the case of the following PDE: for a function *v*(*x*, *y*) of two variables, consider the equation ${\frac {\partial ^{2}v}{\partial x\partial y}}=0.$ It can be directly checked that any function v of the form *v*(*x*, *y*) = *f*(*x*) + *g*(*y*), for any single-variable (differentiable) functions f and g whatsoever, satisfies this condition. This is far beyond the choices available in ODE solution formulas, which typically only allow the free choice of some constants. In the study of PDEs, one generally has the free choice of functions.

The nature of this choice varies from PDE to PDE. To understand it for any given equation, existence and uniqueness theorems are usually important organizational principles. In many introductory textbooks, the role of existence and uniqueness theorems for ODE can be somewhat opaque; the existence half is usually unnecessary, since one can directly check any proposed solution formula, while the uniqueness half is often only present in the background to ensure that a proposed solution formula is as general as possible. By contrast, for PDEs, existence and uniqueness theorems are often the only means by which one can navigate through the plethora of different solutions at hand. For this reason, they are also fundamental when carrying out a purely numerical simulation, as one must have an understanding of what data is to be prescribed by the user and what is to be left to the computer to calculate.

To discuss such existence and uniqueness theorems, it is necessary to be precise about the domain of the "unknown function". Otherwise, speaking only in terms such as "a function of two variables", it is impossible to meaningfully formulate the results. That is, the domain of the unknown function must be regarded as part of the structure of the PDE itself.

The following provides two classic examples of such existence and uniqueness theorems. Even though the two PDEs in question are so similar, there is a major difference in behavior: for the first PDE, one has the free prescription of a single function, while for the second PDE, one has the free prescription of two functions.

- Let B denote the unit-radius disk around the origin in the plane. For any continuous function U on the unit circle, there is exactly one function u on B such that ${\frac {\partial ^{2}u}{\partial x^{2}}}+{\frac {\partial ^{2}u}{\partial y^{2}}}=0$ and whose restriction to the unit circle is given by U.
- For any functions f and g on the real line **R**, there is exactly one function u on **R** × (−1, 1) such that ${\frac {\partial ^{2}u}{\partial x^{2}}}-{\frac {\partial ^{2}u}{\partial y^{2}}}=0$ and with *u*(*x*, 0) = *f*(*x*) and ⁠∂*u*/∂*y*⁠(*x*, 0) = *g*(*x*) for all values of x.

Even more phenomena are possible. For instance, the following PDE, arising naturally in the field of differential geometry, illustrates an example where there is a simple and completely explicit solution formula, but with the free choice of only three numbers and not even one function.

- If u is a function on **R**2 with ${\frac {\partial }{\partial x}}{\frac {\frac {\partial u}{\partial x}}{\sqrt {1+\left({\frac {\partial u}{\partial x}}\right)^{2}+\left({\frac {\partial u}{\partial y}}\right)^{2}}}}+{\frac {\partial }{\partial y}}{\frac {\frac {\partial u}{\partial y}}{\sqrt {1+\left({\frac {\partial u}{\partial x}}\right)^{2}+\left({\frac {\partial u}{\partial y}}\right)^{2}}}}=0,$ then there are numbers a, b, and c with *u*(*x*, *y*) = *ax* + *by* + *c*.

In contrast to the earlier examples, this PDE is **nonlinear**, owing to the square roots and the squares. A **linear** PDE is one such that, if it is homogeneous, the sum of any two solutions is also a solution, and any constant multiple of any solution is also a solution.

## Definition

A partial differential equation is an equation that involves an unknown function of $n\geq 2$ variables and (some of) its partial derivatives. That is, for the unknown function $u:U\rightarrow \mathbb {R} ,$ of variables $x=(x_{1},\dots ,x_{n})$ belonging to the open subset U of $\mathbb {R} ^{n}$ , the $k^{th}$ -order partial differential equation is defined as $F[D^{k}u,D^{k-1}u,\dots ,Du,u,x]=0,$ where $F:\mathbb {R} ^{n^{k}}\times \mathbb {R} ^{n^{k-1}}\dots \times \mathbb {R} ^{n}\times \mathbb {R} \times U\rightarrow \mathbb {R} ,$ and D is the derivative operator.

### Notation

Working in $\mathbb {R} ^{n}$ , the partial derivatives of a function u can be denoted by ${\frac {\partial u}{\partial x_{i}}}$ or with a subscript $u_{x_{i}}.$

For multiple derivatives, multi-index notation can be used. Thus if $\alpha =(\alpha _{1},\dots ,\alpha _{n})$ , the length of $\alpha$ is denoted by $|\alpha |=\alpha _{1}+\cdots +\alpha _{n}$ and the iterated partial is denoted by $D^{\alpha }u={\frac {\partial ^{k}u}{\partial x_{1}^{\alpha _{1}}\cdots \partial x_{n}^{\alpha _{n}}}}.$

In the above definition of a partial differential equation the powers of D are the tensors whose components are the partial derivatives of u ; for example $D^{k}u$ is a tensor having $n^{k}$ components that that are an arrangement of the set $\{D^{\alpha }u\mid |\alpha |=k\}$ after accounting for commutativity of partial derivatives.

The Greek letter Δ denotes the Laplace operator; if u is a function of n variables, then $\Delta u=u_{11}+u_{22}+\cdots +u_{nn}.$ In the physics literature, the Laplace operator is often denoted by ∇2; in the mathematics literature, ∇2*u* may also denote the Hessian matrix of u, which is here denoted by $D^{2}u$ .

## Classification

### Linear and nonlinear equations

A PDE is called **linear** if it is linear in the unknown and its derivatives. For example, for a function u of x and y, a second order linear PDE is of the form $a_{1}(x,y)u_{xx}+a_{2}(x,y)u_{xy}+a_{3}(x,y)u_{yx}+a_{4}(x,y)u_{yy}+a_{5}(x,y)u_{x}+a_{6}(x,y)u_{y}+a_{7}(x,y)u=f(x,y)$ where *ai* and *f* are functions of the independent variables x and y only. (Often the mixed-partial derivatives *uxy* and *uyx* will be equated, but this is not required for the discussion of linearity.) If the *ai* are constants (independent of x and y) then the PDE is called **linear with constant coefficients**. If *f* is zero everywhere then the linear PDE is **homogeneous**, otherwise it is **inhomogeneous**. (This is separate from asymptotic homogenization, which studies the effects of high-frequency oscillations in the coefficients upon solutions to PDEs.)

Nearest to linear PDEs are **semi-linear** PDEs, where only the highest order derivatives appear as linear terms, with coefficients that are functions of the independent variables. The lower order derivatives and the unknown function may appear arbitrarily. For example, a general second order semi-linear PDE in two variables is $a_{1}(x,y)u_{xx}+a_{2}(x,y)u_{xy}+a_{3}(x,y)u_{yx}+a_{4}(x,y)u_{yy}+f(u_{x},u_{y},u,x,y)=0$

In a **quasilinear** PDE the highest order derivatives likewise appear only as linear terms, but with coefficients possibly functions of the unknown and lower-order derivatives: $a_{1}(u_{x},u_{y},u,x,y)u_{xx}+a_{2}(u_{x},u_{y},u,x,y)u_{xy}+a_{3}(u_{x},u_{y},u,x,y)u_{yx}+a_{4}(u_{x},u_{y},u,x,y)u_{yy}+f(u_{x},u_{y},u,x,y)=0$ Many of the fundamental PDEs in physics are quasilinear, such as the Einstein equations of general relativity and the Navier–Stokes equations describing fluid motion.

A PDE without any linearity properties is called **fully nonlinear**, and possesses nonlinearities on one or more of the highest-order derivatives. An example is the Monge–Ampère equation, which arises in differential geometry.

### Second order equations

The elliptic/parabolic/hyperbolic classification provides a guide to appropriate initial- and boundary conditions and to the smoothness of the solutions. Assuming *uxy* = *uyx*, the general linear second-order PDE in two independent variables has the form $Au_{xx}+2Bu_{xy}+Cu_{yy}+\cdots {\mbox{(lower order terms)}}=0,$ where the coefficients A, B, C... may depend upon x and y. If *A*2 + *B*2 + *C*2 > 0 over a region of the xy-plane, the PDE is second-order in that region. This form is analogous to the equation for a conic section: $Ax^{2}+2Bxy+Cy^{2}+\cdots =0.$

More precisely, replacing ∂*x* by X, and likewise for other variables (formally this is done by a Fourier transform), converts a constant-coefficient PDE into a polynomial of the same degree, with the terms of the highest degree (a homogeneous polynomial, here a quadratic form) being most significant for the classification.

Just as one classifies conic sections and quadratic forms into parabolic, hyperbolic, and elliptic based on the discriminant *B*2 − 4*AC*, the same can be done for a second-order PDE at a given point. However, the discriminant in a PDE is given by *B*2 − *AC* due to the convention of the xy term being 2*B* rather than B; formally, the discriminant (of the associated quadratic form) is (2*B*)2 − 4*AC* = 4(*B*2 − *AC*), with the factor of 4 dropped for simplicity.

1. *B*2 − *AC* < 0 (*elliptic partial differential equation*): Solutions of elliptic PDEs are as smooth as the coefficients allow, within the interior of the region where the equation and solutions are defined. For example, solutions of Laplace's equation are analytic within the domain where they are defined, but solutions may assume boundary values that are not smooth. The motion of a fluid at subsonic speeds can be approximated with elliptic PDEs, and the Euler–Tricomi equation is elliptic where *x* < 0. By a change of variables, the equation can always be expressed in the form: $u_{xx}+u_{yy}+\cdots =0,$ where x and y correspond to changed variables. This justifies Laplace equation as an example of this type.
2. *B*2 − *AC* = 0 (*parabolic partial differential equation*): Equations that are parabolic at every point can be transformed into a form analogous to the heat equation by a change of independent variables. Solutions smooth out as the transformed time variable increases. The Euler–Tricomi equation has parabolic type on the line where *x* = 0. By change of variables, the equation can always be expressed in the form: $u_{xx}+\cdots =0,$ where x correspond to changed variables. This justifies the heat equation, which is of the form ${\textstyle u_{t}-u_{xx}+\cdots =0}$ , as an example of this type.
3. *B*2 − *AC* > 0 (*hyperbolic partial differential equation*): hyperbolic equations retain any discontinuities of functions or derivatives in the initial data. An example is the wave equation. The motion of a fluid at supersonic speeds can be approximated with hyperbolic PDEs, and the Euler–Tricomi equation is hyperbolic where *x* > 0. By change of variables, the equation can always be expressed in the form: $u_{xx}-u_{yy}+\cdots =0,$ where x and y correspond to changed variables. This justifies the wave equation as an example of this type.

If there are n independent variables *x*1, *x*2 , …, *x**n*, a general linear partial differential equation of second order has the form $Lu=\sum _{i=1}^{n}\sum _{j=1}^{n}a_{i,j}{\frac {\partial ^{2}u}{\partial x_{i}\partial x_{j}}}\quad +{\text{lower-order terms}}=0.$

The classification depends upon the signature of the eigenvalues of the coefficient matrix *a**i*,*j*.

1. Elliptic: the eigenvalues are all positive or all negative.
2. Parabolic: the eigenvalues are all positive or all negative, except one that is zero.
3. Hyperbolic: there is only one negative eigenvalue and all the rest are positive, or there is only one positive eigenvalue and all the rest are negative.
4. Ultrahyperbolic: there is more than one positive eigenvalue and more than one negative eigenvalue, and there are no zero eigenvalues.

The theory of elliptic, parabolic, and hyperbolic equations have been studied for centuries, largely centered around or based upon the standard examples of the Laplace equation, the heat equation, and the wave equation.

However, the classification only depends on linearity of the second-order terms and is therefore applicable to semi- and quasilinear PDEs as well. The basic types also extend to hybrids such as the Euler–Tricomi equation; varying from elliptic to hyperbolic for different regions of the domain, as well as higher-order PDEs, but such knowledge is more specialized.

### Systems of first-order equations and characteristic surfaces

The classification of partial differential equations can be extended to systems of first-order equations, where the unknown u is now a vector with m components, and the coefficient matrices Aν are m by m matrices for *ν* = 1, 2, …, *n*. The partial differential equation takes the form $Lu=\sum _{\nu =1}^{n}A_{\nu }{\frac {\partial u}{\partial x_{\nu }}}+B=0,$ where the coefficient matrices Aν and the vector B may depend upon x and u. If a hypersurface S is given in the implicit form $\varphi (x_{1},x_{2},\ldots ,x_{n})=0,$ where φ has a non-zero gradient, then S is a **characteristic surface** for the operator L at a given point if the characteristic form vanishes: $Q\left({\frac {\partial \varphi }{\partial x_{1}}},\ldots ,{\frac {\partial \varphi }{\partial x_{n}}}\right)=\det \left[\sum _{\nu =1}^{n}A_{\nu }{\frac {\partial \varphi }{\partial x_{\nu }}}\right]=0.$

The geometric interpretation of this condition is as follows: if data for u are prescribed on the surface S, then it may be possible to determine the normal derivative of u on S from the differential equation. If the data on S and the differential equation determine the normal derivative of u on S, then S is non-characteristic. If the data on S and the differential equation *do not* determine the normal derivative of u on S, then the surface is **characteristic**, and the differential equation restricts the data on S: the differential equation is *internal* to S.

1. A first-order system *Lu* = 0 is *elliptic* if no surface is characteristic for L: the values of u on S and the differential equation always determine the normal derivative of u on S.
2. A first-order system is *hyperbolic* at a point if there is a **spacelike** surface S with normal ξ at that point. This means that, given any non-trivial vector η orthogonal to ξ, and a scalar multiplier λ, the equation *Q*(*λξ* + *η*) = 0 has m real roots *λ*1, *λ*2, …, *λ**m*. The system is **strictly hyperbolic** if these roots are always distinct. The geometrical interpretation of this condition is as follows: the characteristic form *Q*(*ζ*) = 0 defines a cone (the normal cone) with homogeneous coordinates ζ. In the hyperbolic case, this cone has nm sheets, and the axis *ζ* = *λξ* runs inside these sheets: it does not intersect any of them. But when displaced from the origin by η, this axis intersects every sheet. In the elliptic case, the normal cone has no real sheets.

## Analytical solutions

### Separation of variables

Linear PDEs can be reduced to systems of ordinary differential equations by the important technique of separation of variables. This technique rests on a feature of solutions to differential equations: if one can find any solution that solves the equation and satisfies the boundary conditions, then it is *the* solution (this also applies to ODEs). We assume as an ansatz that the dependence of a solution on the parameters space and time can be written as a product of terms that each depend on a single parameter, and then see if this can be made to solve the problem.

In the method of separation of variables, one reduces a PDE to a PDE in fewer variables, which is an ordinary differential equation if in one variable – these are in turn easier to solve.

This is possible for simple PDEs, which are called separable partial differential equations, and the domain is generally a rectangle (a product of intervals). Separable PDEs correspond to diagonal matrices – thinking of "the value for fixed x" as a coordinate, each coordinate can be understood separately.

This generalizes to the method of characteristics, and is also used in integral transforms.

### Method of characteristics

The characteristic surface in *n* = *2*-dimensional space is called a **characteristic curve**. In special cases, one can find characteristic curves on which the first-order PDE reduces to an ODE – changing coordinates in the domain to straighten these curves allows separation of variables, and is called the method of characteristics.

More generally, applying the method to first-order PDEs in higher dimensions, one may find characteristic surfaces.

### Integral transform

An integral transform may transform the PDE to a simpler one, in particular, a separable PDE. This corresponds to diagonalizing an operator.

An important example of this is Fourier analysis, which diagonalizes the heat equation using the eigenbasis of sinusoidal waves.

If the domain is finite or periodic, an infinite sum of solutions such as a Fourier series is appropriate, but an integral of solutions such as a Fourier integral is generally required for infinite domains. The solution for a point source for the heat equation given above is an example of the use of a Fourier integral.

### Change of variables

Often a PDE can be reduced to a simpler form with a known solution by a suitable change of variables. For example, the Black–Scholes equation ${\frac {\partial V}{\partial t}}+{\tfrac {1}{2}}\sigma ^{2}S^{2}{\frac {\partial ^{2}V}{\partial S^{2}}}+rS{\frac {\partial V}{\partial S}}-rV=0$ is reducible to the heat equation ${\frac {\partial u}{\partial \tau }}={\frac {\partial ^{2}u}{\partial x^{2}}}$ by the change of variables ${\begin{aligned}V(S,t)&=v(x,\tau ),\\x&=\ln \left(S\right),\\\tau &={\tfrac {1}{2}}\sigma ^{2}(T-t),\\v(x,\tau )&=e^{-\alpha x-\beta \tau }u(x,\tau ).\end{aligned}}$

### Fundamental solution

Inhomogeneous equations can often be solved (for constant coefficient PDEs, always be solved) by finding the fundamental solution (the solution for a point source $P(D)u=\delta$ ), then taking the convolution with the boundary conditions to get the solution.

This is analogous in signal processing to understanding a filter by its impulse response.

### Superposition principle

The superposition principle applies to any linear system, including linear systems of PDEs. A common visualization of this concept is the interaction of two waves in phase being combined to result in a greater amplitude, for example sin *x* + sin *x* = 2 sin *x*. The same principle can be observed in PDEs where the solutions may be real or complex and additive. If *u*1 and *u*2 are solutions of linear PDE in some function space R, then *u* = *c*1*u*1 + *c*2*u*2 with any constants *c*1 and *c*2 are also a solution of that PDE in the same function space.

### Methods for non-linear equations

There are no generally applicable analytical methods to solve nonlinear PDEs. Still, existence and uniqueness results (such as the Cauchy–Kowalevski theorem) are often possible, as are proofs of important qualitative and quantitative properties of solutions (getting these results is a major part of analysis).

Nevertheless, some techniques can be used for several types of equations. The h-principle is the most powerful method to solve underdetermined equations. The Riquier–Janet theory is an effective method for obtaining information about many analytic overdetermined systems.

The method of characteristics can be used in some very special cases to solve nonlinear partial differential equations.

In some cases, a PDE can be solved via perturbation analysis in which the solution is considered to be a correction to an equation with a known solution. Alternatives are numerical analysis techniques from simple finite difference schemes to the more mature multigrid and finite element methods. Many interesting problems in science and engineering are solved in this way using computers, sometimes high performance supercomputers.

### Lie group method

From 1870 Sophus Lie's work put the theory of differential equations on a more satisfactory foundation. He showed that the integration theories of the older mathematicians can, by the introduction of what are now called Lie groups, be referred, to a common source; and that ordinary differential equations which admit the same infinitesimal transformations present comparable difficulties of integration. He also emphasized the subject of transformations of contact.

A general approach to solving PDEs uses the symmetry property of differential equations, the continuous infinitesimal transformations of solutions to solutions (Lie theory). Continuous group theory, Lie algebras and differential geometry are used to understand the structure of linear and nonlinear partial differential equations for generating integrable equations, to find its Lax pairs, recursion operators, Bäcklund transform and finally finding exact analytic solutions to the PDE.

Symmetry methods have been recognized to study differential equations arising in mathematics, physics, engineering, and many other disciplines.

### Semi-analytical methods

The Adomian decomposition method, the Lyapunov artificial small parameter method, and his homotopy perturbation method are all special cases of the more general homotopy analysis method. These are series expansion methods, and except for the Lyapunov method, are independent of small physical parameters as compared to the well known perturbation theory, thus giving these methods greater flexibility and solution generality.

## Numerical solutions

The three most widely used numerical methods to solve PDEs are the finite element method (FEM), finite volume methods (FVM) and finite difference methods (FDM), as well other kind of methods called meshfree methods, which were made to solve problems where the aforementioned methods are limited. The FEM has a prominent position among these methods and especially its exceptionally efficient higher-order version hp-FEM. Other hybrid versions of FEM and Meshfree methods include the generalized finite element method (GFEM), extended finite element method (XFEM), spectral finite element method (SFEM), meshfree finite element method, discontinuous Galerkin finite element method (DGFEM), element-free Galerkin method (EFGM), interpolating element-free Galerkin method (IEFGM), etc.

### Finite element method

The finite element method (FEM) (its practical application often known as finite element analysis (FEA)) is a numerical technique for approximating solutions of partial differential equations (PDE) as well as of integral equations using a finite set of functions. The solution approach is based either on eliminating the differential equation completely (steady state problems), or rendering the PDE into an approximating system of ordinary differential equations, which are then numerically integrated using standard techniques such as Euler's method, Runge–Kutta, etc.

### Finite difference method

Finite-difference methods are numerical methods for approximating the solutions to differential equations using finite difference equations to approximate derivatives.

### Finite volume method

Similar to the finite difference method or finite element method, values are calculated at discrete places on a meshed geometry. "Finite volume" refers to the small volume surrounding each node point on a mesh. In the finite volume method, surface integrals in a partial differential equation that contain a divergence term are converted to volume integrals, using the divergence theorem. These terms are then evaluated as fluxes at the surfaces of each finite volume. Because the flux entering a given volume is identical to that leaving the adjacent volume, these methods conserve mass by design.

### Neural networks

Physics-informed neural networks have been used to solve partial differential equations in both forward and inverse problems in a data driven manner. One example is the reconstructing fluid flow governed by the Navier-Stokes equations. Using physics informed neural networks does not require the often expensive mesh generation that conventional CFD methods rely on. It is evident that geometric and physical constraints have a synergistic effect on neural PDE surrogates, thereby enhancing their efficacy in predicting stable and super long rollouts.

## Weak solutions

Weak solutions are functions that satisfy the PDE, yet in other meanings than regular sense. The meaning for this term may differ with context, and one of the most commonly used definitions is based on the notion of distributions.

An example for the definition of a weak solution is as follows:

Consider the boundary-value problem given by: ${\begin{aligned}Lu&=f\quad {\text{in }}U,\\u&=0\quad {\text{on }}\partial U,\end{aligned}}$ where $Lu=-\sum _{i,j}\partial _{j}(a^{ij}\partial _{i}u)+\sum _{i}b^{i}\partial _{i}u+cu$ denotes a second-order partial differential operator in **divergence form**.

We say a $u\in H_{0}^{1}(U)$ is a weak solution if $\int _{U}{\bigg [}\sum _{i,j}a^{ij}(\partial _{i}u)(\partial _{j}v)+\sum _{i}b^{i}(\partial _{i}u)v+cuv{\bigg ]}dx=\int _{U}fvdx$ for every $v\in H_{0}^{1}(U)$ , which can be derived by a formal integral by parts.

An example for a weak solution is as follows: $\phi (x)={\frac {1}{4\pi }}{\frac {1}{|x|}}$ is a weak solution satisfying $\nabla ^{2}\phi =\delta {\text{ in }}R^{3}$ in distributional sense, as formally, $\int _{R^{3}}\nabla ^{2}\phi (x)\psi (x)dx=\int _{R^{3}}\phi (x)\nabla ^{2}\psi (x)dx=\psi (0){\text{ for }}\psi \in C_{c}^{\infty }(R^{3}).$

## Theoretical studies

In pure mathematics, the theoretical studies of PDEs focus on the criteria for a solution to exist and the properties of a solution while finding its formula is often secondary.

### Well-posedness

Well-posedness refers to a common schematic package of information about a PDE. To say that a PDE is well-posed, one must have:

- an existence and uniqueness theorem, asserting that by the prescription of some freely chosen functions, one can single out one specific solution of the PDE
- by continuously changing the free choices, one continuously changes the corresponding solution

This is, by the necessity of being applicable to several different PDE, somewhat vague. The requirement of "continuity", in particular, is ambiguous, since there are usually many inequivalent means by which it can be rigorously defined. It is, however, somewhat unusual to study a PDE without specifying a way in which it is well-posed.

### Regularity

Regularity refers to the integrability and differentiability of weak solutions, which can often be represented by Sobolev spaces.

This problem arise due to the difficulty in searching for classical solutions. Researchers often tend to find weak solutions at first and then find out whether it is smooth enough to be qualified as a classical solution.

Results from functional analysis are often used in this field of study.
