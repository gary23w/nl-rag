---
title: "Hamilton–Jacobi equation"
source: https://en.wikipedia.org/wiki/Hamilton%E2%80%93Jacobi_equation
domain: hamiltonian-mechanics
license: CC-BY-SA-4.0
tags: hamiltonian mechanics, phase space, canonical transformation, poisson bracket
fetched: 2026-07-02
---

# Hamilton–Jacobi equation

In physics, the **Hamilton–Jacobi equation**, named after William Rowan Hamilton and Carl Gustav Jacob Jacobi, is an alternative formulation of classical mechanics, equivalent to other formulations such as Newton's laws of motion, Lagrangian mechanics and Hamiltonian mechanics.

The Hamilton–Jacobi equation is a formulation of mechanics in which the motion of a particle can be represented as a wave. In this sense, it fulfilled a long-held goal of theoretical physics (dating at least to Johann Bernoulli in the eighteenth century) of finding an analogy between the propagation of light and the motion of a particle. The wave equation followed by mechanical systems is similar to, but not identical with, the Schrödinger equation, as described below; for this reason, the Hamilton–Jacobi equation is considered the "closest approach" of classical mechanics to quantum mechanics. The qualitative form of this connection is called Hamilton's optico-mechanical analogy.

In mathematics, the Hamilton–Jacobi equation is a necessary condition describing extremal geometry in generalizations of problems from the calculus of variations. It can be understood as a special case of the Hamilton–Jacobi–Bellman equation from dynamic programming.

## Overview

The Hamilton–Jacobi equation is a first-order, non-linear partial differential equation

$-{\frac {\partial S}{\partial t}}=H{\left(\mathbf {q} ,{\frac {\partial S}{\partial \mathbf {q} }},t\right)}.$

for a system of particles at coordinates ⁠ $\mathbf {q}$ ⁠. The function H is the system's Hamiltonian giving the system's energy. The solution of this equation is the *action*, ⁠ S ⁠, called *Hamilton's principal function*. The solution can be related to the system Lagrangian $\ {\mathcal {L}}\$ by an indefinite integral of the form used in the principle of least action: $\ S=\int {\mathcal {L}}\ \mathrm {d} t+~{\mathsf {some\ constant}}~$ Geometrical surfaces of constant action are perpendicular to system trajectories, creating a wavefront-like view of the system dynamics. This property of the Hamilton–Jacobi equation connects classical mechanics to quantum mechanics.

## Mathematical formulation

### Notation

Boldface variables such as $\mathbf {q}$ represent a list of N generalized coordinates, $\mathbf {q} =(q_{1},q_{2},\ldots ,q_{N-1},q_{N})$

A dot over a variable or list signifies the time derivative (see Newton's notation). For example, ${\dot {\mathbf {q} }}={\frac {d\mathbf {q} }{dt}}.$

The dot product notation between two lists of the same number of coordinates is a shorthand for the sum of the products of corresponding components, such as $\mathbf {p} \cdot \mathbf {q} =\sum _{k=1}^{N}p_{k}q_{k}.$

### The action functional (a.k.a. Hamilton's principal function)

#### Definition

Let the Hessian matrix ${\textstyle H_{\mathcal {L}}(\mathbf {q} ,\mathbf {\dot {q}} ,t)=\left\{\partial ^{2}{\mathcal {L}}/\partial {\dot {q}}^{i}\partial {\dot {q}}^{j}\right\}_{ij}}$ be invertible. The relation ${\frac {d}{dt}}{\frac {\partial {\mathcal {L}}}{\partial {\dot {q}}^{i}}}=\sum _{j=1}^{n}\left({\frac {\partial ^{2}{\mathcal {L}}}{\partial {\dot {q}}^{i}\partial {\dot {q}}^{j}}}{\ddot {q}}^{j}+{\frac {\partial ^{2}{\mathcal {L}}}{\partial {\dot {q}}^{i}\partial {q}^{j}}}{\dot {q}}^{j}\right)+{\frac {\partial ^{2}{\mathcal {L}}}{\partial {\dot {q}}^{i}\partial t}},\qquad i=1,\ldots ,n,$ shows that the Euler–Lagrange equations form a $n\times n$ system of second-order ordinary differential equations. Inverting the matrix $H_{\mathcal {L}}$ transforms this system into ${\ddot {q}}^{i}=F_{i}(\mathbf {q} ,\mathbf {\dot {q}} ,t),\ i=1,\ldots ,n.$

Let a time instant $t_{0}$ and a point $\mathbf {q} _{0}\in M$ in the configuration space be fixed. The existence and uniqueness theorems guarantee that, for every $\mathbf {v} _{0},$ the initial value problem with the conditions $\gamma |_{\tau =t_{0}}=\mathbf {q} _{0}$ and ${\dot {\gamma }}|_{\tau =t_{0}}=\mathbf {v} _{0}$ has a locally unique solution $\gamma =\gamma (\tau ;t_{0},\mathbf {q} _{0},\mathbf {v} _{0}).$ Additionally, let there be a sufficiently small time interval $(t_{0},t_{1})$ such that extremals with different initial velocities $\mathbf {v} _{0}$ would not intersect in $M\times (t_{0},t_{1}).$ The latter means that, for any $\mathbf {q} \in M$ and any $t\in (t_{0},t_{1}),$ there can be at most one extremal $\gamma =\gamma (\tau ;t,t_{0},\mathbf {q} ,\mathbf {q} _{0})$ for which $\gamma |_{\tau =t_{0}}=\mathbf {q} _{0}$ and $\gamma |_{\tau =t}=\mathbf {q} .$ Substituting $\gamma =\gamma (\tau ;t,t_{0},\mathbf {q} ,\mathbf {q} _{0})$ into the action functional results in the Hamilton's principal function (HPF)

$S(\mathbf {q} ,t;\mathbf {q} _{0},t_{0})\ {\stackrel {\text{def}}{=}}\int _{t_{0}}^{t}{\mathcal {L}}(\gamma (\tau ;\cdot ),{\dot {\gamma }}(\tau ;\cdot ),\tau )\,d\tau ,$

where

- $\gamma =\gamma (\tau ;t,t_{0},\mathbf {q} ,\mathbf {q} _{0}),$
- $\gamma |_{\tau =t_{0}}=\mathbf {q} _{0},$
- $\gamma |_{\tau =t}=\mathbf {q} .$

### Formula for the momenta

The momenta are defined as the quantities ${\textstyle p_{i}(\mathbf {q} ,\mathbf {\dot {q}} ,t)=\partial {\mathcal {L}}/\partial {\dot {q}}^{i}.}$ This section shows that the dependency of $p_{i}$ on $\mathbf {\dot {q}}$ disappears, once the HPF is known.

Indeed, let a time instant $t_{0}$ and a point $\mathbf {q} _{0}$ in the configuration space be fixed. For every time instant t and a point $\mathbf {q} ,$ let $\gamma =\gamma (\tau ;t,t_{0},\mathbf {q} ,\mathbf {q} _{0})$ be the (unique) extremal from the definition of the Hamilton's principal function ⁠ S ⁠. Call $\mathbf {v} \,{\stackrel {\text{def}}{=}}\,{\dot {\gamma }}(\tau ;t,t_{0},\mathbf {q} ,\mathbf {q} _{0})|_{\tau =t}$ the velocity at ⁠ $\tau =t$ ⁠. Then

${\frac {\partial S}{\partial q^{i}}}=\left.{\frac {\partial {\mathcal {L}}}{\partial {\dot {q}}^{i}}}\right|_{\mathbf {\dot {q}} =\mathbf {v} }\!\!\!\!\!\!\!,\quad i=1,\ldots ,n.$

Proof

While the proof below assumes the configuration space to be an open subset of $\mathbb {R} ^{n},$ the underlying technique applies equally to arbitrary spaces. In the context of this proof, the calligraphic letter ${\mathcal {S}}$ denotes the action functional, and the italic S the Hamilton's principal function.

**Step 1.** Let $\xi =\xi (t)$ be a path in the configuration space, and $\delta \xi =\delta \xi (t)$ a vector field along $\xi$ . (For each $t,$ the vector $\delta \xi (t)$ is called *perturbation*, *infinitesimal variation* or *virtual displacement* of the mechanical system at the point $\xi (t)$ ). Recall that the variation $\delta {\mathcal {S}}_{\delta \xi }[\gamma ,t_{1},t_{0}]$ of the action ${\mathcal {S}}$ at the point $\xi$ in the direction $\delta \xi$ is given by the formula $\delta {\mathcal {S}}_{\delta \xi }[\xi ,t_{1},t_{0}]=\int _{t_{0}}^{t_{1}}\left({\frac {\partial {\mathcal {L}}}{\partial \mathbf {q} }}-{\frac {d}{dt}}{\frac {\partial {\mathcal {L}}}{\partial \mathbf {\dot {q}} }}\right)\delta \xi \,dt+{\frac {\partial {\mathcal {L}}}{\partial \mathbf {\dot {q}} }}\,\delta \xi {\Biggl |}_{t_{0}}^{t_{1}},$ where one should substitute $q^{i}=\xi ^{i}(t)$ and ${\dot {q}}^{i}={\dot {\xi }}^{i}(t)$ after calculating the partial derivatives on the right-hand side. (This formula follows from the definition of Gateaux derivative via integration by parts).

Assume that $\xi$ is an extremal. Since $\xi$ now satisfies the Euler–Lagrange equations, the integral term vanishes. If $\xi$ 's starting point $\mathbf {q} _{0}$ is fixed, then, by the same logic that was used to derive the Euler–Lagrange equations, $\delta \xi (t_{0})=0.$ Thus, $\delta {\mathcal {S}}_{\delta \xi }[\xi ,t;t_{0}]=\left.{\frac {\partial {\mathcal {L}}}{\partial \mathbf {\dot {q}} }}\right|_{\mathbf {\dot {q}} ={\dot {\xi }}(t)}^{\mathbf {q} =\xi (t)}\,\delta \xi (t).$

**Step 2.** Let $\gamma =\gamma (\tau ;\mathbf {q} ,\mathbf {q} _{0},t,t_{0})$ be the (unique) extremal from the definition of HPF, $\delta \gamma =\delta \gamma (\tau )$ a vector field along $\gamma ,$ and $\gamma _{\varepsilon }=\gamma _{\varepsilon }(\tau ;\mathbf {q} _{\varepsilon },\mathbf {q} _{0},t,t_{0})$ a variation of $\gamma$ "compatible" with $\delta \gamma .$ In precise terms, $\gamma _{\varepsilon }|_{\varepsilon =0}=\gamma ,$ ${\dot {\gamma }}_{\varepsilon }|_{\varepsilon =0}=\delta \gamma ,$ $\gamma _{\varepsilon }|_{\tau =t_{0}}=\gamma |_{\tau =t_{0}}=\mathbf {q} _{0}.$

By definition of HPF and Gateaux derivative, $\delta {\mathcal {S}}_{\delta \gamma }[\gamma ,t]{\overset {\text{def}}{{}={}}}\left.{\frac {d{\mathcal {S}}[\gamma _{\varepsilon },t]}{d\varepsilon }}\right|_{\varepsilon =0}=\left.{\frac {dS(\gamma _{\varepsilon }(t),t)}{d\varepsilon }}\right|_{\varepsilon =0}={\frac {\partial S}{\mathbf {\partial q} }}\,\delta \gamma (t).$

Here, we took into account that $\mathbf {q} =\gamma (t;\mathbf {q} ,\mathbf {q} _{0},t,t_{0})$ and dropped $t_{0}$ for compactness.

**Step 3.** We now substitute $\xi =\gamma$ and $\delta \xi =\delta \gamma$ into the expression for $\delta {\mathcal {S}}_{\delta \xi }[\xi ,t;t_{0}]$ from Step 1 and compare the result with the formula derived in Step 2. The fact that, for $t>t_{0},$ the vector field $\delta \gamma$ was chosen arbitrarily completes the proof.

### Formula

Given the Hamiltonian $H(\mathbf {q} ,\mathbf {p} ,t)$ of a mechanical system, the Hamilton–Jacobi equation is a first-order, non-linear partial differential equation for the Hamilton's principal function S ,

$-{\frac {\partial S}{\partial t}}=H{\left(\mathbf {q} ,{\frac {\partial S}{\partial \mathbf {q} }},t\right)}.$

Derivation

For an extremal $\xi =\xi (t;t_{0},\mathbf {q} _{0},\mathbf {v} _{0}),$ where $\mathbf {v} _{0}={\dot {\xi }}|_{t=t_{0}}$ is the initial speed (see discussion preceding the definition of HPF), ${\mathcal {L}}(\xi (t),{\dot {\xi }}(t),t)={\frac {dS(\xi (t),t)}{dt}}=\left[{\frac {\partial S}{\partial \mathbf {q} }}\mathbf {\dot {q}} +{\frac {\partial S}{\partial t}}\right]_{\mathbf {\dot {q}} ={\dot {\xi }}(t)}^{\mathbf {q} =\xi (t)}.$

From the formula for $p_{i}=p_{i}(\mathbf {q} ,t)$ and the coordinate-based definition of the Hamiltonian $H(\mathbf {q} ,\mathbf {p} ,t)=\mathbf {p} \mathbf {\dot {q}} -{\mathcal {L}}(\mathbf {q} ,\mathbf {\dot {q}} ,t),$ with $\mathbf {\dot {q}} (\mathbf {p} ,\mathbf {q} ,t)$ satisfying the (uniquely solvable for $\mathbf {\dot {q}} )$ equation ${\textstyle \mathbf {p} ={\frac {\partial {\mathcal {L}}(\mathbf {q} ,\mathbf {\dot {q}} ,t)}{\partial \mathbf {\dot {q}} }},}$ obtain ${\frac {\partial S}{\partial t}}={\mathcal {L}}(\mathbf {q} ,\mathbf {\dot {q}} ,t)-{\frac {\partial S}{\mathbf {\partial q} }}\mathbf {\dot {q}} =-H{\left(\mathbf {q} ,{\frac {\partial S}{\partial \mathbf {q} }},t\right)},$ where $\mathbf {q} =\xi (t)$ and $\mathbf {\dot {q}} ={\dot {\xi }}(t).$

Alternatively, as described below, the Hamilton–Jacobi equation may be derived from Hamiltonian mechanics by treating S as the generating function for a canonical transformation of the classical Hamiltonian $H=H(q_{1},q_{2},\ldots ,q_{N};p_{1},p_{2},\ldots ,p_{N};t).$

The conjugate momenta correspond to the first derivatives of S with respect to the generalized coordinates $p_{k}={\frac {\partial S}{\partial q_{k}}}.$

As a solution to the Hamilton–Jacobi equation, the principal function contains $N+1$ undetermined constants, the first N of them denoted as $\alpha _{1},\,\alpha _{2},\dots ,\alpha _{N}$ , and the last one coming from the integration of ${\frac {\partial S}{\partial t}}$ .

The relationship between $\mathbf {p}$ and $\mathbf {q}$ then describes the orbit in phase space in terms of these constants of motion. Furthermore, the quantities $\beta _{k}={\frac {\partial S}{\partial \alpha _{k}}},\quad k=1,2,\ldots ,N$ are also constants of motion, and these equations can be inverted to find $\mathbf {q}$ as a function of all the $\alpha$ and $\beta$ constants and time.

## Comparison with other formulations of mechanics

The Hamilton–Jacobi equation is a *single*, first-order partial differential equation for the function of the N generalized coordinates $q_{1},\,q_{2},\dots ,q_{N}$ and the time t . The generalized momenta do not appear, except as derivatives of S , the classical action.

For comparison, in the equivalent Euler–Lagrange equations of motion of Lagrangian mechanics, the conjugate momenta also do not appear; however, those equations are a *system* of N , generally second-order equations for the time evolution of the generalized coordinates. Similarly, Hamilton's equations of motion are another *system* of 2*N* first-order equations for the time evolution of the generalized coordinates and their conjugate momenta $p_{1},\,p_{2},\dots ,p_{N}$ .

Since the HJE is an equivalent expression of an integral minimization problem such as Hamilton's principle, the HJE can be useful in other problems of the calculus of variations and, more generally, in other branches of mathematics and physics, such as dynamical systems, symplectic geometry and quantum chaos. For example, the Hamilton–Jacobi equations can be used to determine the geodesics on a Riemannian manifold, an important variational problem in Riemannian geometry. However as a computational tool, the partial differential equations are notoriously complicated to solve except when is it possible to separate the independent variables; in this case the HJE become computationally useful.

## Derivation using a canonical transformation

Any canonical transformation involving a type-2 generating function $G_{2}(\mathbf {q} ,\mathbf {P} ,t)$ leads to the relations ${\begin{aligned}&\mathbf {p} ={\frac {\partial G_{2}}{\partial \mathbf {q} }},\quad \mathbf {Q} ={\frac {\partial G_{2}}{\partial \mathbf {P} }},\quad \\&K(\mathbf {Q} ,\mathbf {P} ,t)=H(\mathbf {q} ,\mathbf {p} ,t)+{\frac {\partial G_{2}}{\partial t}}\end{aligned}}$ and Hamilton's equations in terms of the new variables $\mathbf {P} ,\,\mathbf {Q}$ and new Hamiltonian K have the same form: ${\dot {\mathbf {P} }}=-{\partial K \over \partial \mathbf {Q} },\quad {\dot {\mathbf {Q} }}=+{\partial K \over \partial \mathbf {P} }.$

To derive the HJE, a generating function $G_{2}(\mathbf {q} ,\mathbf {P} ,t)$ is chosen in such a way that, it will make the new Hamiltonian $K=0$ . Hence, all its derivatives are also zero, and the transformed Hamilton's equations become trivial ${\dot {\mathbf {P} }}={\dot {\mathbf {Q} }}=0$ so the new generalized coordinates and momenta are *constants* of motion. As they are constants, in this context the new generalized momenta $\mathbf {P}$ are usually denoted $\alpha _{1},\,\alpha _{2},\dots ,\alpha _{N}$ , i.e. $P_{m}=\alpha _{m}$ and the new generalized coordinates $\mathbf {Q}$ are typically denoted as $\beta _{1},\,\beta _{2},\dots ,\beta _{N}$ , so $Q_{m}=\beta _{m}$ .

Setting the generating function equal to Hamilton's principal function, plus an arbitrary constant A : $G_{2}(\mathbf {q} ,{\boldsymbol {\alpha }},t)=S(\mathbf {q} ,t)+A,$ the HJE automatically arises ${\begin{aligned}&\mathbf {p} ={\frac {\partial G_{2}}{\partial \mathbf {q} }}={\frac {\partial S}{\partial \mathbf {q} }}\\[1ex]\rightarrow {}&H(\mathbf {q} ,\mathbf {p} ,t)+{\partial G_{2} \over \partial t}=0\\[1ex]\rightarrow {}&H{\left(\mathbf {q} ,{\frac {\partial S}{\partial \mathbf {q} }},t\right)}+{\partial S \over \partial t}=0.\end{aligned}}$

When solved for $S(\mathbf {q} ,{\boldsymbol {\alpha }},t)$ , these also give us the useful equations $\mathbf {Q} ={\boldsymbol {\beta }}={\partial S \over \partial {\boldsymbol {\alpha }}},$ or written in components for clarity $Q_{m}=\beta _{m}={\frac {\partial S(\mathbf {q} ,{\boldsymbol {\alpha }},t)}{\partial \alpha _{m}}}.$

Ideally, these N equations can be inverted to find the original generalized coordinates $\mathbf {q}$ as a function of the constants ${\boldsymbol {\alpha }},\,{\boldsymbol {\beta }},$ and t , thus solving the original problem.

## Separation of variables

When the problem allows additive separation of variables, the HJE leads directly to constants of motion. For example, the time *t* can be separated if the Hamiltonian does not depend on time explicitly. In that case, the time derivative ${\frac {\partial S}{\partial t}}$ in the HJE must be a constant, usually denoted ( $-E$ ), giving the separated solution $S=W(q_{1},q_{2},\ldots ,q_{N})-Et$ where the time-independent function $W(\mathbf {q} )$ is sometimes called the **abbreviated action** or **Hamilton's characteristic function** and sometimes written $S_{0}$ (see action principle names). The reduced Hamilton–Jacobi equation can then be written $H{\left(\mathbf {q} ,{\frac {\partial S}{\partial \mathbf {q} }}\right)}=E.$

To illustrate separability for other variables, a certain generalized coordinate $q_{k}$ and its derivative ${\frac {\partial S}{\partial q_{k}}}$ are assumed to appear together as a single function $\psi {\left(q_{k},{\frac {\partial S}{\partial q_{k}}}\right)}$ in the Hamiltonian $H=H(q_{1},q_{2},\ldots ,q_{k-1},q_{k+1},\ldots ,q_{N};p_{1},p_{2},\ldots ,p_{k-1},p_{k+1},\ldots ,p_{N};\psi ;t).$

In that case, the function *S* can be partitioned into two functions, one that depends only on *qk* and another that depends only on the remaining generalized coordinates $S=S_{k}(q_{k})+S_{\text{rem}}(q_{1},\ldots ,q_{k-1},q_{k+1},\ldots ,q_{N},t).$

Substitution of these formulae into the Hamilton–Jacobi equation shows that the function *ψ* must be a constant (denoted here as $\Gamma _{k}$ ), yielding a first-order ordinary differential equation for $S_{k}(q_{k}),$

$\psi {\left(q_{k},{\frac {dS_{k}}{dq_{k}}}\right)}=\Gamma _{k}.$

In fortunate cases, the function S can be separated completely into N functions $S_{m}(q_{m}),$ $S=S_{1}(q_{1})+S_{2}(q_{2})+\cdots +S_{N}(q_{N})-Et.$

In such a case, the problem devolves to N ordinary differential equations.

The separability of *S* depends both on the Hamiltonian and on the choice of generalized coordinates. For orthogonal coordinates and Hamiltonians that have no time dependence and are quadratic in the generalized momenta, S will be completely separable if the potential energy is additively separable in each coordinate, where the potential energy term for each coordinate is multiplied by the coordinate-dependent factor in the corresponding momentum term of the Hamiltonian (the **Staeckel conditions**). For illustration, several examples in orthogonal coordinates are worked in the next sections.

### Separation in spherical coordinates

In spherical coordinates the Hamiltonian of a free particle moving in a conservative potential *U* can be written $H={\frac {1}{2m}}\left[p_{r}^{2}+{\frac {p_{\theta }^{2}}{r^{2}}}+{\frac {p_{\phi }^{2}}{r^{2}\sin ^{2}\theta }}\right]+U(r,\theta ,\phi ).$

The Hamilton–Jacobi equation is separable in these coordinates provided that there exist functions $U_{r}(r),U_{\theta }(\theta ),U_{\phi }(\phi )$ such that U can be written in the analogous form $U(r,\theta ,\phi )=U_{r}(r)+{\frac {U_{\theta }(\theta )}{r^{2}}}+{\frac {U_{\phi }(\phi )}{r^{2}\sin ^{2}\theta }}.$

The last term has few physical applications. Dropping that term, the HJE becomes ${\frac {1}{2m}}\left({\frac {dS_{r}}{dr}}\right)^{2}+U_{r}(r)+{\frac {1}{2mr^{2}}}\left[\left({\frac {dS_{\theta }}{d\theta }}\right)^{2}+2mU_{\theta }(\theta )\right]+{\frac {1}{2mr^{2}\sin ^{2}\theta }}\left({\frac {dS_{\phi }}{d\phi }}\right)^{2}=E.$ The $\phi$ coordinate is *cyclic* and the solution can be written in the form $S_{0}=p_{\phi }+S_{r}(r)+S_{\theta }(\theta ),$ resulting in two ordinary differential equations for the remaining coordinates: $\left({\frac {dS_{\theta }}{d\theta }}\right)^{2}+2mU_{\theta }(\theta )+{\frac {p_{\phi }}{\sin ^{2}\theta }}=\Gamma _{\theta }$ ${\frac {1}{2m}}\left({\frac {dS_{r}}{dr}}\right)^{2}+U_{r}(r)+{\frac {\Gamma _{\theta }}{2mr^{2}}}=E$ where $p_{\phi }$ , $\Gamma _{\theta }$ , and E are constants of the motion. This reduces the HJE to the ordinary differential equations whose integration completes the solution for S .

## Waves and particles

### Optical wave fronts and trajectories

The HJE establishes a duality between trajectories and wavefronts. For example, in geometrical optics, light can be considered either as "rays" or waves. The wave front can be defined as the surface ${\textstyle {\mathcal {C}}_{t}}$ that the light emitted at time ${\textstyle t=0}$ has reached at time ${\textstyle t}$ . Light rays and wave fronts are dual: if one is known, the other can be deduced.

More precisely, geometrical optics is a variational problem where the "action" is the travel time ${\textstyle T}$ along a path, $T={\frac {1}{c}}\int _{A}^{B}n\,ds$ where ${\textstyle n}$ is the medium's index of refraction and ${\textstyle ds}$ is an infinitesimal arc length. From the above formulation, one can compute the ray paths using the Euler–Lagrange formulation; alternatively, one can compute the wave fronts by solving the Hamilton–Jacobi equation. Knowing one leads to knowing the other.

The above duality is very general and applies to *all* systems that derive from a variational principle: either compute the trajectories using Euler–Lagrange equations or the wave fronts by using Hamilton–Jacobi equation.

The wave front at time ${\textstyle t}$ , for a system initially at ${\textstyle \mathbf {q} _{0}}$ at time ${\textstyle t_{0}}$ , is defined as the collection of points ${\textstyle \mathbf {q} }$ such that ${\textstyle S(\mathbf {q} ,t)={\text{const}}}$ . If ${\textstyle S(\mathbf {q} ,t)}$ is known, the momentum is immediately deduced. $\mathbf {p} ={\frac {\partial S}{\partial \mathbf {q} }}.$

Once ${\textstyle \mathbf {p} }$ is known, tangents to the trajectories ${\textstyle {\dot {\mathbf {q} }}}$ are computed by solving the equation ${\frac {\partial {\mathcal {L}}}{\partial {\dot {\mathbf {q} }}}}={\boldsymbol {p}}$ for ${\textstyle {\dot {\mathbf {q} }}}$ , where ${\textstyle {\mathcal {L}}}$ is the Lagrangian. The trajectories are then recovered from the knowledge of ${\textstyle {\dot {\mathbf {q} }}}$ .

### Relationship to the Schrödinger equation

The isosurfaces of the function $S(\mathbf {q} ,t)$ can be determined at any time *t*. The motion of an S -isosurface as a function of time is defined by the motions of the particles beginning at the points $\mathbf {q}$ on the isosurface. The motion of such an isosurface can be thought of as a *wave* moving through $\mathbf {q}$ -space, although it does not obey the wave equation exactly. To show this, let *S* represent the phase of a wave $\psi =\psi _{0}e^{iS/\hbar }$ where $\hbar$ is a constant (the Planck constant) introduced to make the exponential argument dimensionless, and $\psi _{0}$ is a scalar normalization constant; changes in the amplitude of the wave can be represented by having S be a complex number.

The Schrödinger equation is : ${\frac {\hbar ^{2}}{2m}}\nabla ^{2}\psi -U\psi ={\frac {\hbar }{i}}{\frac {\partial \psi }{\partial t}}$

Starting with the Schrödinger equation and our ansatz for $\psi$ , it can be deduced that ${\frac {1}{2m}}\left(\nabla S\right)^{2}+U+{\frac {\partial S}{\partial t}}={\frac {i\hbar }{2m}}\nabla ^{2}S.$ This is the Schrödinger equation in nonlinear Riccati form.

The classical limit ( $\hbar \rightarrow 0$ ) of the Schrödinger equation above becomes identical to the following variant of the Hamilton–Jacobi equation, ${\frac {1}{2m}}\left(\nabla S\right)^{2}+U+{\frac {\partial S}{\partial t}}=0.$

The following table summarizes the similarities between optics and quantum mechancis. The Hamilton-Jacobi equation is to quantum mechanics what the eikonal equation is to the wave equation of optics. Both the eikonal equation and the Hamilton-Jacobi equation are slowly varying approximations (WKB approximations) of the corresponding more fundamental wave equations.

**Optics** $\nabla ^{2}\psi -{\frac {1}{c^{2}(x)}}{\frac {\partial ^{2}\psi }{\partial t^{2}}}=0$ EM Wave equation  ↓ $-{\frac {n(\partial _{t}S)^{2}}{c^{2}}}+{\frac {(\nabla S)^{2}}{n}}+(mc)^{2}=0$ Time dependant eikonal equation  ↓ $|\nabla S(x)|^{2}=n^{2}(x)$ Eikonal equation

**Quantum mechanics** $i\hbar {\frac {\partial \psi }{\partial t}}={\hat {H}}\psi$ Schrödinger equation  ↓ $\partial _{t}S+H(x,\nabla S,t)=0$ Hamilton–Jacobi equation

## Applications

### HJE in a gravitational field

Using the energy–momentum relation in the form $g^{\alpha \beta }P_{\alpha }P_{\beta }-(mc)^{2}=0$ for a particle of rest mass m travelling in curved space, where $g^{\alpha \beta }$ are the contravariant coordinates of the metric tensor (i.e., the inverse metric) solved from the Einstein field equations, and c is the speed of light. Setting the four-momentum $P_{\alpha }$ equal to the four-gradient of the action S , $P_{\alpha }=-{\frac {\partial S}{\partial x^{\alpha }}}$ gives the Hamilton–Jacobi equation in the geometry determined by the metric g : $g^{\alpha \beta }{\frac {\partial S}{\partial x^{\alpha }}}{\frac {\partial S}{\partial x^{\beta }}}-(mc)^{2}=0,$ in other words, in a gravitational field.

### HJE in electromagnetic fields

For a particle of rest mass m and electric charge e moving in electromagnetic field with four-potential $A_{i}=(\phi ,\mathrm {A} )$ in vacuum, the Hamilton–Jacobi equation in geometry determined by the metric tensor $g^{ik}=g_{ik}$ has a form $g^{ik}\left({\frac {\partial S}{\partial x^{i}}}+{\frac {e}{c}}A_{i}\right)\left({\frac {\partial S}{\partial x^{k}}}+{\frac {e}{c}}A_{k}\right)=m^{2}c^{2}$ and can be solved for the Hamilton principal action function S to obtain further solution for the particle trajectory and momentum: ${\begin{aligned}x&=-{\frac {e}{c\gamma }}\int A_{z}\,d\xi ,&y&=-{\frac {e}{c\gamma }}\int A_{y}\,d\xi ,\\[1ex]z&=-{\frac {e^{2}}{2c^{2}\gamma ^{2}}}\int \left(\mathrm {A} ^{2}-{\overline {\mathrm {A} ^{2}}}\right)\,d\xi ,&\xi &=ct-{\frac {e^{2}}{2\gamma ^{2}c^{2}}}\int \left(\mathrm {A} ^{2}-{\overline {\mathrm {A} ^{2}}}\right)\,d\xi ,\\[1ex]p_{x}&=-{\frac {e}{c}}A_{x},&p_{y}&=-{\frac {e}{c}}A_{y},\\[1ex]p_{z}&={\frac {e^{2}}{2\gamma c}}\left(\mathrm {A} ^{2}-{\overline {\mathrm {A} ^{2}}}\right),&{\mathcal {E}}&=c\gamma +{\frac {e^{2}}{2\gamma c}}\left(\mathrm {A} ^{2}-{\overline {\mathrm {A} ^{2}}}\right),\end{aligned}}$ where $\xi =ct-z$ and $\gamma ^{2}=m^{2}c^{2}+{\frac {e^{2}}{c^{2}}}{\overline {A}}^{2}$ with ${\overline {\mathbf {A} }}$ the cycle average of the vector potential.

#### A circularly polarized wave

In the case of circular polarization, ${\begin{aligned}E_{x}&=E_{0}\sin \omega \xi _{1},&E_{y}&=E_{0}\cos \omega \xi _{1},\\[1ex]A_{x}&={\frac {cE_{0}}{\omega }}\cos \omega \xi _{1},&A_{y}&=-{\frac {cE_{0}}{\omega }}\sin \omega \xi _{1}.\end{aligned}}$

Hence ${\begin{aligned}x&=-{\frac {ecE_{0}}{\omega }}\sin \omega \xi _{1},&y&=-{\frac {ecE_{0}}{\omega }}\cos \omega \xi _{1},\\[1ex]p_{x}&=-{\frac {eE_{0}}{\omega }}\cos \omega \xi _{1},&p_{y}&={\frac {eE_{0}}{\omega }}\sin \omega \xi _{1},\end{aligned}}$

where $\xi _{1}=\xi /c$ , implying the particle moving along a circular trajectory with a permanent radius $ecE_{0}/\gamma \omega ^{2}$ and an invariable value of momentum $eE_{0}/\omega ^{2}$ directed along a magnetic field vector.

#### A monochromatic linearly polarized plane wave

For the flat, monochromatic, linearly polarized wave with a field E directed along the axis y ${\begin{aligned}E_{y}&=E_{0}\cos \omega \xi _{1},&A_{y}&=-{\frac {cE_{0}}{\omega }}\sin \omega \xi _{1},\end{aligned}}$ hence ${\begin{aligned}x&={\text{const}},\\[1ex]y&=y_{0}\cos \omega \xi _{1},&y_{0}&=-{\frac {ecE_{0}}{\gamma \omega ^{2}}},\\[1ex]z&=C_{z}y_{0}\sin 2\omega \xi _{1},&C_{z}&={\frac {eE_{0}}{8\gamma \omega }},\\[1ex]\gamma ^{2}&=m^{2}c^{2}+{\frac {e^{2}E_{0}^{2}}{2\omega ^{2}}},\end{aligned}}$ ${\begin{aligned}p_{x}&=0,\\[1ex]p_{y}&=p_{y,0}\sin \omega \xi _{1},&p_{y,0}&={\frac {eE_{0}}{\omega }},\\[1ex]p_{z}&=-2C_{z}p_{y,0}\cos 2\omega \xi _{1}\end{aligned}}$

implying the particle figure-8 trajectory with its axis oriented along the electric field E vector.

#### An electromagnetic wave with a solenoidal magnetic field

For the electromagnetic wave with axial (solenoidal) magnetic field: $E=E_{\phi }={\frac {\omega \rho _{0}}{c}}B_{0}\cos \omega \xi _{1},$ $A_{\phi }=-\rho _{0}B_{0}\sin \omega \xi _{1}=-{\frac {L_{s}}{\pi \rho _{0}N_{s}}}I_{0}\sin \omega \xi _{1},$ hence ${\begin{aligned}x&={\text{constant}},\\y&=y_{0}\cos \omega \xi _{1},&y_{0}&=-{\frac {e\rho _{0}B_{0}}{\gamma \omega }},\\z&=C_{z}y_{0}\sin 2\omega \xi _{1},&C_{z}&={\frac {e\rho _{0}B_{0}}{8c\gamma }},\\\gamma ^{2}&=m^{2}c^{2}+{\frac {e^{2}\rho _{0}^{2}B_{0}^{2}}{2c^{2}}},\end{aligned}}$ ${\begin{aligned}p_{x}&=0,\\p_{y}&=p_{y,0}\sin \omega \xi _{1},&p_{y,0}&={\frac {e\rho _{0}B_{0}}{c}},\\p_{z}&=-2C_{z}p_{y,0}\cos 2\omega \xi _{1},\end{aligned}}$ where $B_{0}$ is the magnetic field magnitude in a solenoid with the effective radius $\rho _{0}$ , inductivity $L_{s}$ , number of windings $N_{s}$ , and an electric current magnitude $I_{0}$ through the solenoid windings. The particle motion occurs along the figure-8 trajectory in $yz$ plane set perpendicular to the solenoid axis with arbitrary azimuth angle $\varphi$ due to axial symmetry of the solenoidal magnetic field.
