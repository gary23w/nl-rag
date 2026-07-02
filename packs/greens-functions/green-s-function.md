---
title: "Green's function"
source: https://en.wikipedia.org/wiki/Green%27s_function
domain: greens-functions
license: CC-BY-SA-4.0
tags: green's function, fundamental solution, method of images, propagator function
fetched: 2026-07-02
---

# Green's function

In mathematics, a **Green's function** (or **Green function**) is the impulse response of an inhomogeneous linear differential operator defined on a domain with specified initial conditions or boundary conditions.

This means that if L is a linear differential operator, then

- the Green's function G is the solution of the equation $LG=\delta ,$ where $\delta$ is Dirac's delta function;
- the solution of the inhomogeneous problem $Ly=f$ is the convolution, $y=(G\ast f).$

By the superposition principle, given a linear ordinary differential equation (ODE), $Ly=f$ , one can first solve $LG=\delta _{s}$ , for each s. If the source is a sum of delta functions, then the solution is a sum of Green's functions as well due to linearity of L. This means that the integral, viewed as a continuous sum, can reconstruct a wide class of sources, f , through the convolution integral. Whenever the integral of f with G converges, then the solution to the inhomogeneous equation, $Ly=f$ , is given by $y=G\ast f$ .

Green's functions are named after the British mathematician George Green, who first developed the concept in the 1820s. In the modern study of linear partial differential equations, Green's functions are studied largely from the point of view of fundamental solutions instead, which take into account the modern language of the theory of distributions or generalized functions.

Building off of the superposition principle in many-body theory, the term is also used in physics and engineering, specifically in quantum field theory, aerodynamics, aeroacoustics, electrodynamics, seismology and statistical field theory, to refer to various types of correlation functions, even those that do not fit the mathematical definition. In quantum field theory, Green's functions take the role of propagators, also referred to as two-point (correlation) functions.

## Definition and uses

A Green's function, *G*(*x*,*s*), of a linear differential operator *L* = *L*(*x*) acting on distributions over a subset of the Euclidean space $\mathbb {R} ^{n}$ , at a point s, is any solution of

| $L\,G(x,s)=\delta (s-x)\,,$ |   | 1 |
|---|---|---|

where δ is the Dirac delta function. This property of a Green's function can be exploited to solve differential equations of the form

| $L\,u(x)=f(x)\,.$ |   | 2 |
|---|---|---|

If the kernel of *L* is non-trivial, then the Green's function is not unique. However, in practice, some combination of symmetry, boundary conditions and/or other externally imposed criteria will give a unique Green's function. Green's functions may be categorized by a Green's function number according to the type of boundary conditions being satisfied. Green's functions are not necessarily functions of a real variable but are generally understood in the sense of distributions.

Green's functions are also useful tools in solving wave equations and diffusion equations. In quantum mechanics, Green's function of the Hamiltonian is a key concept with important links to the concept of density of states.

The Green's function as used in physics is usually defined with the opposite sign, instead. That is, $LG(x,s)=\delta (x-s)\,.$ This definition does not significantly change any of the properties of Green's function due to the evenness of the Dirac delta function.

If the operator is translation invariant, that is, when L has constant coefficients with respect to x, then the Green's function can be taken to be a convolution kernel, that is, $G(x,s)=G(x-s)\,.$ In this case, Green's function is the same as the impulse response of linear time-invariant system theory.

## Motivation

Loosely speaking, if such a function G can be found for the operator *L*, then, if we multiply **equation 1** for the Green's function by *f*(*s*), and then integrate with respect to s, we obtain, $\int LG(x,s)\,f(s)\,ds=\int \delta (x-s)\,f(s)\,ds=f(x)\,.$ Because the operator $L=L(x)$ is linear and acts only on the variable x (and *not* on the variable of integration s), one may take the operator L outside of the integration, yielding $L\left(\int G(x,s)\,f(s)\,ds\right)=f(x)\,.$ This means that

| $u(x)=\int G(x,s)\,f(s)\,ds$ |   | 3 |
|---|---|---|

is a solution to the equation $Lu(x)=f(x)\,.$

Thus, one may obtain the function *u*(*x*) through knowledge of the Green's function in **equation 1** and the source term on the right-hand side in **equation 2**. This process relies upon the linearity of the operator *L*.

In other words, the solution of **equation 2**, *u*(*x*), can be determined by the integration given in **equation 3**. Although *f*(*x*) is known, this integration cannot be performed unless G is also known. The problem now lies in finding the Green's function G that satisfies **equation 1**. For this reason, the Green's function is also sometimes called the fundamental solution associated to the operator *L*.

Not every operator L admits a Green's function. A Green's function can also be thought of as a right inverse of *L*. Aside from the difficulties of finding a Green's function for a particular operator, the integral in **equation 3** may be quite difficult to evaluate. However the method gives a theoretically exact result.

This can be thought of as an expansion of f according to a Dirac delta function basis (projecting f over $\delta (x-s)$ ; and a superposition of the solution on each projection. Such an integral equation is known as a Fredholm integral equation, the study of which constitutes Fredholm theory.

## Green's functions for solving non-homogeneous boundary value problems

The primary use of Green's functions in mathematics is to solve non-homogeneous boundary value problems. In modern theoretical physics, Green's functions are also usually used as propagators in Feynman diagrams; the term *Green's function* is often further used for any correlation function.

### Framework

Let L be a Sturm–Liouville operator, a linear differential operator of the form $L={\dfrac {d}{dx}}\left[p(x){\dfrac {d}{dx}}\right]+q(x)$ and let $\mathbf {D}$ be the vector-valued boundary conditions operator $\mathbf {D} u={\begin{bmatrix}\alpha _{1}u'(0)+\beta _{1}u(0)\\\alpha _{2}u'(\ell )+\beta _{2}u(\ell )\end{bmatrix}}\,.$

Let $f(x)$ be a continuous function in $[0,\ell ]\,$ . Further suppose that the problem ${\begin{aligned}Lu&=f\\\mathbf {D} u&=\mathbf {0} \end{aligned}}$ is regular, i.e., the only solution for $f(x)=0$ for all x is $u(x)=0$ .

### Theorem

There is one and only one solution $u(x)$ that satisfies ${\begin{aligned}Lu&=f\\\mathbf {D} u&=\mathbf {0} \end{aligned}}$ and it is given by $u(x)=\int _{0}^{\ell }f(s)\,G(x,s)\,ds\,,$ where $G(x,s)$ is a Green's function satisfying the following conditions:

1. $G(x,s)$ is continuous in x and s .
2. For $x\neq s\,$ ,   $LG(x,s)=0$ .
3. For $s\neq 0\,$ ,   $\mathbf {D} G(x,s)=\mathbf {0}$ .
4. Derivative "jump":   $G'(s_{0+},s)-G'(s_{0-},s)=1/p(s)\,$ .
5. Symmetry:   $G(x,s)=G(s,x)\,$ .

### Advanced and retarded Green's functions

Green's function is not necessarily unique since the addition of any solution of the homogeneous equation to one Green's function results in another Green's function. Therefore, if the homogeneous equation has nontrivial solutions, multiple Green's functions exist. Certain boundary value or initial value problems involve finding a Green's function that is nonvanishing only for $s\leq x$ ; in this case, the solution is sometimes called a retarded Green's function. Similarly, a Green's function that is nonvanishing only for $s\geq x$ is called an advanced Green's function. In such cases, any linear combination of the two Green's functions is also a valid Green's function. Both the advanced and retarded Green's functions are called one-sided, while a Green's function that is nonvanishing for all x in the domain of definition is called two-sided.

The terminology advanced and retarded is especially useful when the variable x corresponds to time. In such cases, the solution provided by the use of the retarded Green's function depends only on the past sources and is causal whereas the solution provided by the use of the advanced Green's function depends only on the future sources and is acausal. In these problems, it is often the case that the causal solution is the physically important one. However, the advanced Green's function is useful in finding solutions to certain inverse problems where sources are to be found from boundary data. The use of advanced and retarded Green's function is especially common for the analysis of solutions of the inhomogeneous electromagnetic wave equation.

## Finding Green's functions

### Eigenvalue expansions

If a differential operator *L* admits a set of eigenvectors Ψ*n*(*x*) (i.e., a set of functions Ψ*n* and scalars *λ**n* such that *L*Ψ*n* = *λ**n* Ψ*n* ) that is complete, then it is possible to construct a Green's function from these eigenvectors and eigenvalues.

"Complete" means that the set of functions {Ψ*n*} satisfies the following completeness relation, $\delta (x-x')=\sum _{n=0}^{\infty }\Psi _{n}^{\dagger }(x')\Psi _{n}(x).$

Then the following holds,

$G(x,x')=\sum _{n=0}^{\infty }{\dfrac {\Psi _{n}^{\dagger }(x')\Psi _{n}(x)}{\lambda _{n}}},$

where $\dagger$ represents complex conjugation.

Applying the operator *L* to each side of this equation results in the completeness relation, which was assumed.

The general study of Green's function written in the above form, and its relationship to the function spaces formed by the eigenvectors, is known as Fredholm theory.

There are several other methods for finding Green's functions, including the method of images, separation of variables, and Laplace transforms.

### Representations in terms of the Wronskian

Let L be the general linear second-order differential operator defined on $[a,b]\in \mathbb {R}$ . We write

$Lu(x)=\alpha (x){\frac {d^{2}}{dx^{2}}}u(x)+\beta (x){\frac {d}{dx}}u(x)+\gamma (x)u(x)=f(x).$

Suppose that $u_{1}$ and $u_{2}$ together form a basis of linearly independent solutions to the homogeneous problem $Lu=0.$ Given homogeneous boundary conditions for the Green's function $G(a,s)=G(b,s)=0$ , we may construct $G(x,s)$ by requiring $u_{1}(a)=0$ and $u_{2}(b)=0.$ The Green's function satisfying these conditions, alongside the continuity of G and its derivative "jump", can be written as

$G(x,s)={\begin{cases}{\dfrac {u_{1}(x)u_{2}(s)}{\alpha (s){\mathcal {W(s)}}}},&a\leq x<s\\{\dfrac {u_{2}(x)u_{1}(s)}{\alpha (s){\mathcal {W}}(s)}},&s<x\leq b\end{cases}}$

where ${\mathcal {W}}(x)=u_{1}(x)u'_{2}(x)-u_{1}'(x)u_{2}(x)$ is known as the Wronskian determinant of $u_{1}$ and $u_{2}$ . Though this is a somewhat limited case, the Wronskian frequently appears in other sets of boundary value problems that require a one-sided (advanced/retarded) Green's function as well, including those with conditions on boundary derivatives (Neumann conditions) or a pair of conditions on a function and its normal derivative on a single boundary (Cauchy conditions).

### Combining Green's functions

If the differential operator L can be factored as $L=L_{1}L_{2}$ then the Green's function of L can be constructed from the Green's functions for $L_{1}$ and $L_{2}$ : $G(x,s)=\int G_{2}(x,s_{1})\,G_{1}(s_{1},s)\,ds_{1}.$ The above identity follows immediately from taking $G(x,s)$ to be the representation of the right operator inverse of L , analogous to how for the invertible linear operator C , defined by $C=(AB)^{-1}=B^{-1}A^{-1}$ , is represented by its matrix elements $C_{i,j}$ .

A further identity follows for differential operators that are scalar polynomials of the derivative, $L=P_{N}(\partial _{x})$ . The fundamental theorem of algebra, combined with the fact that $\partial _{x}$ commutes with itself, guarantees that the polynomial can be factored, putting L in the form: $L=\prod _{i=1}^{N}\left(\partial _{x}-z_{i}\right),$ where $z_{i}$ are the zeros of $P_{N}(z)$ . Taking the Fourier transform of $LG(x,s)=\delta (x-s)$ with respect to both x and s gives: ${\widehat {G}}(k_{x},k_{s})={\frac {\delta (k_{x}-k_{s})}{\prod _{i=1}^{N}(ik_{x}-z_{i})}}.$ The fraction can then be split into a sum using a partial fraction decomposition before Fourier transforming back to x and s space. This process yields identities that relate integrals of Green's functions and sums of the same. For example, if $L=\left(\partial _{x}+\gamma \right)\left(\partial _{x}+\alpha \right)^{2}$ then one form for its Green's function is: ${\begin{aligned}G(x,s)&={\frac {1}{\left(\gamma -\alpha \right)^{2}}}\Theta (x-s)e^{-\gamma (x-s)}-{\frac {1}{\left(\gamma -\alpha \right)^{2}}}\Theta (x-s)e^{-\alpha (x-s)}+{\frac {1}{\gamma -\alpha }}\Theta (x-s)\left(x-s\right)e^{-\alpha (x-s)}\\[1ex]&=\int \Theta (x-s_{1})\left(x-s_{1}\right)e^{-\alpha (x-s_{1})}\Theta (s_{1}-s)e^{-\gamma (s_{1}-s)}\,ds_{1}.\end{aligned}}$ While the example presented is tractable analytically, it illustrates a process that works when the integral is not trivial (for example, when $\nabla ^{2}$ is the operator in the polynomial).

### Table of Green's functions

The following table gives an overview of Green's functions of frequently appearing differential operators, where ${\textstyle r={\sqrt {x^{2}+y^{2}+z^{2}}}}$ , ${\textstyle \rho ={\sqrt {x^{2}+y^{2}}}}$ , ${\textstyle \Theta (t)}$ is the Heaviside step function, ${\textstyle J_{\nu }(z)}$ is a Bessel function, ${\textstyle I_{\nu }(z)}$ is a modified Bessel function of the first kind, and ${\textstyle K_{\nu }(z)}$ is a modified Bessel function of the second kind. Where time (t) appears in the first column, the retarded (causal) Green's function is listed.

| Differential operator *L* | Green's function G | Example of application |
|---|---|---|
| $\partial _{t}^{n+1}$ | ${\frac {t^{n}}{n!}}\Theta (t)$ |   |
| $\partial _{t}+\gamma$ | $\Theta (t)e^{-\gamma t}$ |   |
| $\left(\partial _{t}+\gamma \right)^{2}$ | $\Theta (t)te^{-\gamma t}$ |   |
| $\partial _{t}^{2}+2\gamma \partial _{t}+\omega _{0}^{2}$ where $\gamma <\omega _{0}$ | $\Theta (t)e^{-\gamma t}\,{\frac {\sin(\omega t)}{\omega }}$   with   $\omega ={\sqrt {\omega _{0}^{2}-\gamma ^{2}}}$ | 1D underdamped harmonic oscillator |
| $\partial _{t}^{2}+2\gamma \partial _{t}+\omega _{0}^{2}$ where $\gamma >\omega _{0}$ | $\Theta (t)e^{-\gamma t}\,{\frac {\sinh(\omega t)}{\omega }}$   with   $\omega ={\sqrt {\gamma ^{2}-\omega _{0}^{2}}}$ | 1D overdamped harmonic oscillator |
| $\partial _{t}^{2}+2\gamma \partial _{t}+\omega _{0}^{2}$ where $\gamma =\omega _{0}$ | $\Theta (t)e^{-\gamma t}t$ | 1D critically damped harmonic oscillator |
| 1D Laplace operator ${\frac {d^{2}}{dx^{2}}}$ | $\left(x-s\right)\Theta (x-s)+x\alpha (s)+\beta (s)$ | 1D Poisson equation |
| 2D Laplace operator $\nabla _{\text{2D}}^{2}=\partial _{x}^{2}+\partial _{y}^{2}$ | ${\frac {1}{2\pi }}\ln \rho$   with   $\rho ={\sqrt {x^{2}+y^{2}}}$ | 2D Poisson equation |
| 3D Laplace operator $\nabla _{\text{3D}}^{2}=\partial _{x}^{2}+\partial _{y}^{2}+\partial _{z}^{2}$ | $-{\frac {1}{4\pi r}}$   with   $r={\sqrt {x^{2}+y^{2}+z^{2}}}$ | Poisson equation |
| Helmholtz operator $\nabla _{\text{3D}}^{2}+k^{2}$ | ${\frac {-e^{-ikr}}{4\pi r}}=i{\sqrt {\frac {k}{32\pi r}}}H_{1/2}^{(2)}(kr)=i{\frac {k}{4\pi }}\,h_{0}^{(2)}(kr)$ where $H_{\alpha }^{(2)}$ is the Hankel function of the second kind, and $h_{0}^{(2)}$ is the spherical Hankel function of the second kind | stationary 3D Schrödinger equation for free particle |
| $\Delta ^{2}-k^{4}$ | ${\frac {1}{2k^{2}}}\left({\frac {i}{4}}H_{0}^{(1)}(kr)-{\frac {1}{2\pi }}K_{0}(kr)\right)$ where $H_{0}^{(1)}$ is the Hankel function of the first kind, and $K_{0}$ is the modified Bessel function | 2D time-harmonic flexural wave equation |
| Divergence operator $\nabla \cdot \mathbf {G}$ | $(-1)^{1+(d-1)!}{\frac {\Gamma \left({\frac {d}{2}}\right)}{2\pi ^{d/2}}}{\frac {(\,\|d-2\|+\delta _{d,2})\,(\mathbf {x} -\mathbf {x} _{0})}{\left\\|\mathbf {x} -\mathbf {x} _{0}\right\\|^{d}}}.$ | Let $\mathbf {G}$ be a vector field from $\mathbb {R} ^{d}$ to $\mathbb {R} ^{d}$ , and $\mathbf {x} ,\,\mathbf {x} _{0}\in \mathbb {R} ^{d}$ with $d\in \mathbb {N}$ , such that $\nabla \cdot \mathbf {G} =\delta$ . The function, $\Gamma (\cdot )$ , is the gamma function, and $\delta _{d,2}$ is Kronecker's delta, such that $\delta _{d,2}=0$ for $d\neq 2$ , and $\delta _{2,2}=1$ for $d=2$ . Lastly, ! is the factorial symbol and $\|\cdot \|$ is the absolute value. Examples include the time-independent transport or Continuity equation and source-free Maxwell's equations. |
| $\nabla ^{2}-k^{2}$ in n dimensions | $-\left(2\pi \right)^{-n/2}\left({\frac {k}{r}}\right)^{n/2-1}K_{n/2-1}(kr)$ | Yukawa potential, Feynman propagator, Screened Poisson equation |
| $\partial _{t}^{2}-c^{2}\partial _{x}^{2}$ | ${\frac {1}{2c}}\Theta (ct-x)$ | 1D wave equation |
| $\partial _{t}^{2}-c^{2}\,\nabla _{\text{2D}}^{2}$ | ${\frac {\Theta (ct-\rho )}{2\pi c{\sqrt {c^{2}t^{2}-\rho ^{2}}}}}$ | 2D wave equation |
| D'Alembert operator $\square ={\frac {1}{c^{2}}}\partial _{t}^{2}-\nabla _{\text{3D}}^{2}$ | ${\frac {1}{4\pi r}}\delta \left(t-{\frac {r}{c}}\right)$ | 3D wave equation |
| $\partial _{t}-k\partial _{x}^{2}$ | $\left({\frac {1}{4\pi kt}}\right)^{1/2}\Theta (t)e^{-x^{2}/4kt}$ | 1D diffusion |
| $\partial _{t}-k\,\nabla _{\text{2D}}^{2}$ | $\left({\frac {1}{4\pi kt}}\right)\Theta (t)e^{-\rho ^{2}/4kt}$ | 2D diffusion |
| $\partial _{t}-k\,\nabla _{\text{3D}}^{2}$ | $\left({\frac {1}{4\pi kt}}\right)^{3/2}\Theta (t)e^{-r^{2}/4kt}$ | 3D diffusion |
| ${\frac {1}{c^{2}}}\partial _{t}^{2}-\partial _{x}^{2}+\mu ^{2}$ | ${\begin{aligned}&{\tfrac {1}{2}}\left(1-\sin {\mu ct}\right)\left[\delta (ct-x)+\delta (ct+x)\right]\\[0.5ex]&+{\tfrac {1}{2}}\mu \Theta (ct-\|x\|)J_{0}(\mu u)\end{aligned}}$ with $u={\sqrt {c^{2}t^{2}-x^{2}}}$ | 1D Klein–Gordon equation |
| ${\frac {1}{c^{2}}}\partial _{t}^{2}-\nabla _{\text{2D}}^{2}+\mu ^{2}$ | ${\begin{aligned}&{\frac {\delta (ct-\rho )}{4\pi \rho }}\left(1+\cos(\mu ct)\right)\\[0.5ex]&+{\frac {\mu ^{2}\Theta (ct-\rho )}{4\pi }}\operatorname {sinc} (\mu u)\end{aligned}}$ with $u={\sqrt {c^{2}t^{2}-\rho ^{2}}}$ | 2D Klein–Gordon equation |
| $\square +\mu ^{2}$ | ${\frac {1}{4\pi r}}\delta {\left(t-{\frac {r}{c}}\right)}+{\frac {\mu c}{4\pi u}}\Theta (ct-r)J_{1}{\left(\mu u\right)}$   with   $u={\sqrt {c^{2}t^{2}-r^{2}}}$ | 3D Klein–Gordon equation |
| $\partial _{t}^{2}+2\gamma \partial _{t}-c^{2}\partial _{x}^{2}$ | ${\begin{aligned}&{\frac {e^{-\gamma t}}{2}}\left[\delta (ct-x)+\delta (ct+x)\right]\\[0.5ex]&+{\frac {e^{-\gamma t}}{2}}\Theta (ct-\|x\|)\left(kI_{0}(ku)+{\frac {\gamma t}{u}}I_{1}(ku)\right)\end{aligned}}$ with   $u={\sqrt {c^{2}t^{2}-x^{2}}}$ and $k=\gamma /c$ | telegrapher's equation |
| $\partial _{t}^{2}+2\gamma \partial _{t}-c^{2}\,\nabla _{\text{2D}}^{2}$ | ${\begin{aligned}&{\frac {e^{-\gamma t}}{4\pi \rho }}\delta (ct-\rho )\left(1+e^{-\gamma t}+3\gamma t\right)\\&+{\frac {e^{-\gamma t}}{4\pi u^{2}}}\Theta (ct-\rho )\left({\frac {ku^{2}-3ct}{cu}}\sinh \left(ku\right)+3\gamma t\cosh \left(ku\right)\right)\end{aligned}}$ with   $u={\sqrt {c^{2}t^{2}-\rho ^{2}}}$ and $k=\gamma /c$ | 2D relativistic heat conduction |
| $\partial _{t}^{2}+2\gamma \partial _{t}-c^{2}\,\nabla _{\text{3D}}^{2}$ | ${\begin{aligned}&{\frac {e^{-\gamma t}}{20\pi r^{2}}}\delta (ct-r)\left(8-3e^{-\gamma t}+2\gamma t+4\gamma ^{2}t^{2}\right)\\[0.5ex]&+{\frac {ke^{-\gamma t}}{20\pi u}}\Theta (ct-r)\left(kI_{1}(ku)+{\frac {4\gamma t}{u}}I_{2}(ku)\right)\end{aligned}}$ with   $u={\sqrt {c^{2}t^{2}-r^{2}}}$ and $k=\gamma /c$ | 3D relativistic heat conduction |

## Green's functions for the Laplacian

Green's functions for linear differential operators involving the Laplacian may be readily put to use using the second of Green's identities.

To derive Green's theorem, begin with the divergence theorem (otherwise known as Gauss's theorem), $\int _{V}\nabla \cdot \mathbf {A} \,dV=\int _{S}\mathbf {A} \cdot d{\hat {\boldsymbol {\sigma }}}\,.$

Let $\mathbf {A} =\varphi \,\nabla \psi -\psi \,\nabla \varphi$ and substitute into Gauss' law.

Compute $\nabla \cdot \mathbf {A}$ and apply the product rule for the ∇ operator, ${\begin{aligned}\nabla \cdot \mathbf {A} &=\nabla \cdot \left(\varphi \,\nabla \psi \;-\;\psi \,\nabla \varphi \right)\\&=(\nabla \varphi )\cdot (\nabla \psi )\;+\;\varphi \,\nabla ^{2}\psi \;-\;(\nabla \varphi )\cdot (\nabla \psi )\;-\;\psi \nabla ^{2}\varphi \\&=\varphi \,\nabla ^{2}\psi \;-\;\psi \,\nabla ^{2}\varphi .\end{aligned}}$

Plugging this into the divergence theorem produces Green's theorem, $\int _{V}\left(\varphi \,\nabla ^{2}\psi -\psi \,\nabla ^{2}\varphi \right)dV=\int _{S}\left(\varphi \,\nabla \psi -\psi \nabla \,\varphi \right)\cdot d{\hat {\boldsymbol {\sigma }}}.$

Suppose that the linear differential operator L is the Laplacian, ∇2, and that there is a Green's function G for the Laplacian. The defining property of the Green's function still holds, $LG(\mathbf {x} ,\mathbf {x} ')=\nabla ^{2}G(\mathbf {x} ,\mathbf {x} ')=\delta (\mathbf {x} -\mathbf {x} ').$

Let $\psi =G$ in Green's second identity, see Green's identities. Then, $\int _{V}\left[\varphi (\mathbf {x} ')\delta (\mathbf {x} -\mathbf {x} ')-G(\mathbf {x} ,\mathbf {x} ')\,{\nabla '}^{2}\,\varphi (\mathbf {x} ')\right]d^{3}\mathbf {x} '=\int _{S}\left[\varphi (\mathbf {x} ')\,{\nabla '}G(\mathbf {x} ,\mathbf {x} ')-G(\mathbf {x} ,\mathbf {x} ')\,{\nabla '}\varphi (\mathbf {x} ')\right]\cdot d{\hat {\boldsymbol {\sigma }}}'.$

Using this expression, it is possible to solve Laplace's equation ∇2*φ*(**x**) = 0 or Poisson's equation ∇2*φ*(**x**) = −*ρ*(**x**), subject to either Neumann or Dirichlet boundary conditions. In other words, we can solve for *φ*(**x**) everywhere inside a volume where either (1) the value of *φ*(**x**) is specified on the bounding surface of the volume (Dirichlet boundary conditions), or (2) the normal derivative of *φ*(**x**) is specified on the bounding surface (Neumann boundary conditions).

Suppose the problem is to solve for *φ*(**x**) inside the region. Then the integral $\int _{V}\varphi (\mathbf {x} ')\,\delta (\mathbf {x} -\mathbf {x} ')\,d^{3}\mathbf {x} '$ reduces to simply *φ*(**x**) due to the defining property of the Dirac delta function and we have $\varphi (\mathbf {x} )=-\int _{V}G(\mathbf {x} ,\mathbf {x} ')\,\rho (\mathbf {x} ')\,d^{3}\mathbf {x} '+\int _{S}\left[\varphi (\mathbf {x} ')\,\nabla 'G(\mathbf {x} ,\mathbf {x} ')-G(\mathbf {x} ,\mathbf {x} ')\,\nabla '\varphi (\mathbf {x} ')\right]\cdot d{\hat {\boldsymbol {\sigma }}}'.$

This form expresses the well-known property of harmonic functions, that *if the value or normal derivative is known on a bounding surface, then the value of the function inside the volume is known everywhere*.

In electrostatics, *φ*(**x**) is interpreted as the electric potential, *ρ*(**x**) as electric charge density, and the normal derivative $\nabla \varphi (\mathbf {x} ')\cdot d{\hat {\boldsymbol {\sigma }}}'$ as the normal component of the electric field.

If the problem is to solve a Dirichlet boundary value problem, the Green's function should be chosen such that *G*(*x*,*x*′) vanishes when either x or x′ is on the bounding surface. Thus only one of the two terms in the surface integral remains. If the problem is to solve a Neumann boundary value problem, it might seem logical to choose Green's function so that its normal derivative vanishes on the bounding surface. However, application of Gauss's theorem to the differential equation defining the Green's function yields $\int _{S}\nabla 'G(\mathbf {x} ,\mathbf {x} ')\cdot d{\hat {\boldsymbol {\sigma }}}'=\int _{V}\nabla '^{2}G(\mathbf {x} ,\mathbf {x} ')\,d^{3}\mathbf {x} '=\int _{V}\delta (\mathbf {x} -\mathbf {x} ')\,d^{3}\mathbf {x} '=1\,,$ meaning the normal derivative of *G*(**x**,**x**′) cannot vanish on the surface, because it must integrate to 1 on the surface.

The simplest form the normal derivative can take is that of a constant, namely 1/*S*, where *S* is the surface area of the surface. The surface term in the solution becomes $\int _{S}\varphi (\mathbf {x} ')\,\nabla 'G(\mathbf {x} ,\mathbf {x} ')\cdot d{\hat {\boldsymbol {\sigma }}}'=\langle \varphi \rangle _{S}$ where $\langle \varphi \rangle _{S}$ is the average value of the potential on the surface. This number is not known in general, but is often unimportant, as the goal is often to obtain the electric field given by the gradient of the potential, rather than the potential itself.

With no boundary conditions, the Green's function for the Laplacian (Green's function for the three-variable Laplace equation) is $G(\mathbf {x} ,\mathbf {x} ')=-{\frac {1}{4\pi \left|\mathbf {x} -\mathbf {x} '\right|}}.$

Supposing that the bounding surface goes out to infinity and plugging in this expression for the Green's function finally yields the standard expression for electric potential in terms of electric charge density as

$\varphi (\mathbf {x} )=\int _{V}{\dfrac {\rho (\mathbf {x} ')}{4\pi \varepsilon \left|\mathbf {x} -\mathbf {x} '\right|}}\,d^{3}\mathbf {x} '\,.$

## Example

Find the Green function for the following problem, whose Green's function number is X11: ${\begin{aligned}Lu&=u''+k^{2}u=f(x)\\u(0)&=0,\quad u{\left({\tfrac {\pi }{2k}}\right)}=0.\end{aligned}}$

**First step:** The Green's function for the linear operator at hand is defined as the solution to

| $G''(x,s)+k^{2}G(x,s)=\delta (x-s).$ |   | Eq. * |
|---|---|---|

If $x\neq s$ , then the delta function gives zero, and the general solution is $G(x,s)=c_{1}\cos kx+c_{2}\sin kx.$

For $x<s$ , the boundary condition at $x=0$ implies $G(0,s)=c_{1}\cdot 1+c_{2}\cdot 0=0,\quad c_{1}=0$ if $x<s$ and $s\neq {\tfrac {\pi }{2k}}$ .

For $x>s$ , the boundary condition at $x={\tfrac {\pi }{2k}}$ implies $G{\left({\tfrac {\pi }{2k}},s\right)}=c_{3}\cdot 0+c_{4}\cdot 1=0,\quad c_{4}=0$

The equation of $G(0,s)=0$ is skipped for similar reasons.

To summarize the results thus far: $G(x,s)={\begin{cases}c_{2}\sin kx,&{\text{for }}x<s,\\[0.4ex]c_{3}\cos kx,&{\text{for }}s<x.\end{cases}}$

**Second step:** The next task is to determine $c_{2}$ and $c_{3}$ .

Ensuring continuity in the Green's function at $x=s$ implies $c_{2}\sin ks=c_{3}\cos ks$

One can ensure proper discontinuity in the first derivative by integrating the defining differential equation (i.e., **Eq. ***) from $x=s-\varepsilon$ to $x=s+\varepsilon$ and taking the limit as $\varepsilon$ goes to zero. Note that we only integrate the second derivative as the remaining term will be continuous by construction. $c_{3}\cdot (-k\sin ks)-c_{2}\cdot (k\cos ks)=1$

The two (dis)continuity equations can be solved for $c_{2}$ and $c_{3}$ to obtain $c_{2}=-{\frac {\cos ks}{k}}\quad ;\quad c_{3}=-{\frac {\sin ks}{k}}$

So Green's function for this problem is: $G(x,s)={\begin{cases}-{\frac {\cos ks}{k}}\sin kx,&x<s,\\-{\frac {\sin ks}{k}}\cos kx,&s<x.\end{cases}}$

## Further examples

- Let *n* = 1 and let the subset be all of **R**. Let L be ${\textstyle {\frac {d}{dx}}}$ . Then, the Heaviside step function Θ(*x* − *x*0) is a Green's function of *L* at *x*0.
- Let *n* = 2 and let the subset be the quarter-plane {(*x*, *y*) : *x*, *y* ≥ 0} and L be the Laplacian. Also, assume a Dirichlet boundary condition is imposed at *x* = 0 and a Neumann boundary condition is imposed at *y* = 0. Then the X10Y20 Green's function is ${\begin{aligned}G(x,y,x_{0},y_{0})={\dfrac {1}{2\pi }}&\left[\ln {\sqrt {\left(x-x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}}-\ln {\sqrt {\left(x+x_{0}\right)^{2}+\left(y-y_{0}\right)^{2}}}\right.\\[5pt]&\left.{}+\ln {\sqrt {\left(x-x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}}}-\ln {\sqrt {\left(x+x_{0}\right)^{2}+\left(y+y_{0}\right)^{2}}}\,\right].\end{aligned}}$
- Let $a<x<b$ , and all three are elements of the real numbers. Then, for any function $f:\mathbb {R} \to \mathbb {R}$ with an n -th derivative that is integrable over the interval $[a,b]$ : $f(x)=\sum _{m=0}^{n-1}{\frac {(x-a)^{m}}{m!}}\left[{\frac {d^{m}f}{dx^{m}}}\right]_{x=a}+\int _{a}^{b}\left[{\frac {(x-s)^{n-1}}{(n-1)!}}\Theta (x-s)\right]\left[{\frac {d^{n}f}{dx^{n}}}\right]_{x=s}ds\,.$ The Green's function in the above equation, $G(x,s)={\frac {(x-s)^{n-1}}{(n-1)!}}\Theta (x-s)$ , is not unique. How is the equation modified if $g(x-s)$ is added to $G(x,s)$ , where $g(x)$ satisfies ${\textstyle {\frac {d^{n}g}{dx^{n}}}=0}$ for all $x\in [a,b]$ (for example, $g(x)=-x/2$ with $n=2$ )? Also, compare the above equation to the form of a Taylor series centered at $x=a$ .
