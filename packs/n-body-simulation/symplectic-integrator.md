---
title: "Symplectic integrator"
source: https://en.wikipedia.org/wiki/Symplectic_integrator
domain: n-body-simulation
license: CC-BY-SA-4.0
tags: n-body simulation, barnes-hut simulation, fast multipole method, astrophysical plasma
fetched: 2026-07-02
---

# Symplectic integrator

In mathematics, a **symplectic integrator** (**SI**) is a numerical integration scheme for Hamiltonian systems. Symplectic integrators form the subclass of geometric integrators which, by definition, are canonical transformations. They are widely used in nonlinear dynamics, molecular dynamics, discrete element methods, accelerator physics, plasma physics, quantum physics, and celestial mechanics.

## Introduction

Symplectic integrators are designed for the numerical solution of Hamilton's equations, which read ${\dot {p}}=-{\frac {\partial H}{\partial q}}\quad {\mbox{and}}\quad {\dot {q}}={\frac {\partial H}{\partial p}},$ where q denotes the position coordinates, p the momentum coordinates, and H is the Hamiltonian. The set of position and momentum coordinates $(q,p)$ are called canonical coordinates. (See Hamiltonian mechanics for more background.)

The time evolution of Hamilton's equations is a symplectomorphism, meaning that it conserves the symplectic 2-form $dp\wedge dq$ . A numerical scheme is a symplectic integrator if it also conserves this 2-form.

Symplectic integrators possess, as a conserved quantity, a Hamiltonian which is slightly perturbed from the original one. By virtue of these advantages, the SI scheme has been widely applied to the calculations of long-term evolution of chaotic Hamiltonian systems ranging from the Kepler problem to the classical and semi-classical simulations in molecular dynamics.

Most of the usual numerical methods, such as the primitive Euler scheme and the classical Runge–Kutta scheme, are not symplectic integrators.

## Methods for constructing symplectic algorithms

### Splitting methods for separable Hamiltonians

A widely used class of symplectic integrators is formed by the splitting methods.

Assume that the Hamiltonian is separable, meaning that it can be written in the form

| $H(p,q)=T(p)+V(q).$ |   | 1 |
|---|---|---|

This happens frequently in Hamiltonian mechanics, with T being the kinetic energy and V the potential energy.

For the notational simplicity, let us introduce the symbol $z=(q,p)$ to denote the canonical coordinates including both the position and momentum coordinates. Then, the set of the Hamilton's equations given in the introduction can be expressed in a single expression as

| ${\dot {z}}=\{z,H(z)\},$ |   | 2 |
|---|---|---|

where $\{\cdot ,\cdot \}$ is a Poisson bracket. Furthermore, by introducing an operator $D_{H}\cdot =\{\cdot ,H\}$ , which returns a Poisson bracket of the operand with the Hamiltonian, the expression of the Hamilton's equation can be further simplified to

${\dot {z}}=D_{H}z.$

The formal solution of this set of equations at time t is given as a matrix exponential:

| $z(t)=\exp(tD_{H})\,z(0).$ |   | 3 |
|---|---|---|

Note the positivity of $tD_{H}$ in the matrix exponential.

When the Hamiltonian has the form of equation (**1**), the solution (**3**) is equivalent to

| $z(t)=\exp \left[t(D_{T}+D_{V})\right]\,z(0).$ |   | 4 |
|---|---|---|

The SI scheme approximates the time-evolution operator $\exp[t(D_{T}+D_{V})]$ in the formal solution (**4**) by a product of operators as

| ${\begin{aligned}\exp[t(D_{T}+D_{V})]&=\prod _{i=k,\dots ,1}\exp(td_{i}D_{T})\exp(tc_{i}D_{V})+O(t^{k+1})\\&=\exp(td_{k}D_{T})\exp(tc_{k}D_{V})\cdots \exp(td_{1}D_{T})\exp(tc_{1}D_{V})+O(t^{k+1}),\end{aligned}}$ |   | 5 |
|---|---|---|

where $c_{i}$ and $d_{i}$ are real numbers, k is an integer, which is called the order of the integrator, and where ${\textstyle \sum _{i=1}^{k}c_{i}=\sum _{i=1}^{k}d_{i}=1}$ . Note that each of the operators $\exp(tc_{i}D_{V})$ and $\exp(td_{i}D_{T})$ provides a symplectic map, so their product appearing in the right-hand side of (**5**) also constitutes a symplectic map.

Since $D_{T}^{2}z=\{\{z,T\},T\}=\{({\dot {q}},0),T\}=(0,0)$ for all z , we can conclude that

| $D_{T}^{2}=0.$ |   | 6 |
|---|---|---|

By using a Taylor series, $\exp(aD_{T})$ can be expressed as

| $\exp(aD_{T})=\sum _{n=0}^{\infty }{\frac {{\left(aD_{T}\right)}^{n}}{n!}},$ |   | 7 |
|---|---|---|

where a is an arbitrary real number. Combining (**6**) and (**7**), and by using the same reasoning for $D_{V}$ as we have used for $D_{T}$ , we get

| ${\begin{cases}\exp(aD_{V})=1+aD_{V},\\[2pt]\exp(aD_{T})=1+aD_{T}.\end{cases}}$ |   | 8 |
|---|---|---|

In concrete terms, $\exp(tc_{i}D_{V})$ gives the mapping

${\begin{pmatrix}q\\p\end{pmatrix}}\mapsto {\begin{pmatrix}q\\p-tc_{i}{\frac {\partial V}{\partial q}}(q)\end{pmatrix}},$

and $\exp(td_{i}D_{T})$ gives

${\begin{pmatrix}q\\p\end{pmatrix}}\mapsto {\begin{pmatrix}q+td_{i}{\frac {\partial T}{\partial p}}(p)\\p\end{pmatrix}}.$

Note that both of these maps are practically computable.

#### Algorithm

In each time step, the general algorithm for this class of symplectic integrators maps some initial state $(q_{0},p_{0})$ to the state $(q_{k},p_{k})$ one timestep t later. This is done through the sequence of substeps $(q_{0},p_{0})\mapsto (q_{1},p_{1})\mapsto \dots \mapsto (q_{k-1},p_{k-1})\mapsto (q_{k},p_{k})$ . For every $i=1,\dots ,k$ , the following equations are used to compute the substep $(q_{i-1},p_{i-1})\mapsto (q_{i},p_{i})$ :

${\begin{aligned}p_{i}&=p_{i-1}+tc_{i}F(q_{i-1})\\[1ex]q_{i}&=q_{i-1}+td_{i}{\frac {p_{i}}{m}}\end{aligned}}$

where q is the position, p is the momentum, $F(q)=-{\tfrac {\partial V}{\partial q}}(q)$ is the force vector at q , and m is the scalar quantity of mass.

Equivalently, after converting into Lagrangian coordinates, each substep becomes

${\begin{aligned}v_{i}&=v_{i-1}+tc_{i}a(x_{i-1})\\[1ex]x_{i}&=x_{i-1}+td_{i}v_{i}\end{aligned}}$

where x is the position, v is the velocity, and $a(x)$ is the acceleration vector at x .

Several symplectic integrators are given below.

#### A first-order example

The symplectic Euler method is the first-order integrator with $k=1$ and coefficients $c_{1}=d_{1}=1.$

Note that the algorithm above does not work if time-reversibility is needed. The algorithm has to be implemented in two parts, one for positive time steps, one for negative time steps.

#### A second-order example

The Verlet method is the second-order symplectic integrator with $k=2$ and coefficients

$c_{1}={\tfrac {1}{2}},\qquad d_{1}=1,\qquad c_{2}={\tfrac {1}{2}},\qquad d_{2}=0.$

Note that the coefficients

$c_{1}=0,\qquad d_{1}={\tfrac {1}{2}},\qquad c_{2}=1,\qquad d_{2}={\tfrac {1}{2}}$

also form a second-order symplectic integrator, which is the Verlet method but shifted by half a time step t .

Since $d_{2}=0$ in the first set of coefficients and $c_{1}=0$ in the second set of coefficients, in both algorithms above one update can be ignored. There are thus only 3 steps to the algorithm, and step 1 and 3 are exactly the same, leading to the algorithm being symmetric in time, so the positive time version can also be used for negative time.

#### A third-order example

A third-order symplectic integrator (with $k=3$ ) was discovered by Ronald Ruth in 1983. One of the many solutions is given by ${\begin{aligned}c_{1}&={\tfrac {7}{24}},&c_{2}&={\tfrac {3}{4}},&c_{3}&=-{\tfrac {1}{24}},\\[1ex]d_{1}&={\tfrac {2}{3}},&d_{2}&=-{\tfrac {2}{3}},&d_{3}&=1.\end{aligned}}$

#### A fourth-order example

A fourth-order integrator (with $k=4$ ) was also discovered by Ruth in 1983 and distributed privately to the particle-accelerator community at that time. This was described in a lively review article by Forest. This fourth-order integrator was published in 1990 by Forest and Ruth and also independently discovered by two other groups around that same time: ${\begin{aligned}c_{1}&=c_{4}={\frac {1}{2\left(2-2^{1/3}\right)}},&c_{2}&=c_{3}={\frac {1-2^{1/3}}{2\left(2-2^{1/3}\right)}},\\[1ex]d_{1}&=d_{3}={\frac {1}{2-2^{1/3}}},&d_{2}&=-{\frac {2^{1/3}}{2-2^{1/3}}},\qquad d_{4}=0,\end{aligned}}$ or alternatively, ${\begin{aligned}c_{1}&=0,\qquad c_{3}=-{\frac {2^{1/3}}{2-2^{1/3}}},&c_{2}&=c_{4}={\frac {1}{2-2^{1/3}}},\\[1ex]d_{1}&=d_{4}={\frac {1}{2\left(2-2^{1/3}\right)}},&d_{2}&=d_{3}={\frac {1-2^{1/3}}{2\left(2-2^{1/3}\right)}}.\end{aligned}}$

To determine these coefficients, the Baker–Campbell–Hausdorff formula can be used. Yoshida, in particular, gives an elegant derivation of coefficients for higher-order integrators. Later on, Blanes and Moan further developed partitioned Runge–Kutta methods for the integration of systems with separable Hamiltonians with very small error constants. Numerov's method, developed by the Russian astronomer Boris Vasil'evich Numerov in 1924, is also a fourth-order symplectic integrator.

### Splitting methods for general nonseparable Hamiltonians

General nonseparable Hamiltonians can also be explicitly and symplectically integrated.

To do so, Tao introduced a restraint that binds two copies of phase space together to enable an explicit splitting of such systems. The idea is, instead of $H(Q,P)$ , one simulates ${\bar {H}}(q,p,x,y)=H(q,y)+H(x,p)+\omega \left({\tfrac {1}{2}}{\left\|q-x\right\|}_{2}^{2}+{\tfrac {1}{2}}{\left\|p-y\right\|}_{2}^{2}\right),$ whose solution agrees with that of $H(Q,P)$ in the sense that $q(t)=x(t)=Q(t)$ , $p(t)=y(t)=P(t)$ .

The new Hamiltonian is advantageous for explicit symplectic integration, because it can be split into the sum of three sub-Hamiltonians, $H_{A}=H(q,y)$ , $H_{B}=H(x,p)$ , and ${\textstyle H_{C}=\omega \left({\frac {1}{2}}\left\|q-x\right\|_{2}^{2}+{\frac {1}{2}}\left\|p-y\right\|_{2}^{2}\right)}$ . Exact solutions of all three sub-Hamiltonians can be explicitly obtained: both $H_{A},H_{B}$ solutions correspond to shifts of mismatched position and momentum, and $H_{C}$ corresponds to a linear transformation. To symplectically simulate the system, one simply composes these solution maps.

## Applications

### In plasma physics

In recent decades symplectic integrator in plasma physics has become an active research topic, because straightforward applications of the standard symplectic methods do not suit the need of large-scale plasma simulations enabled by the peta- to exa-scale computing hardware. Special symplectic algorithms need to be customarily designed, tapping into the special structures of the physics problem under investigation. One such example is the charged particle dynamics in an electromagnetic field. With the canonical symplectic structure, the Hamiltonian of the dynamics is $H({\boldsymbol {p}},{\boldsymbol {x}})={\tfrac {1}{2}}\left({\boldsymbol {p}}-{\boldsymbol {A}}\right)^{2}+\phi ,$ whose ${\textstyle {\boldsymbol {p}}}$ -dependence and ${\textstyle {\boldsymbol {x}}}$ -dependence are not separable, and standard explicit symplectic methods do not apply. For large-scale simulations on massively parallel clusters, however, explicit methods are preferred. To overcome this difficulty, we can explore the specific way that the ${\textstyle {\boldsymbol {p}}}$ -dependence and ${\textstyle {\boldsymbol {x}}}$ -dependence are entangled in this Hamiltonian, and try to design a symplectic algorithm just for this or this type of problem. First, we note that the ${\textstyle {\boldsymbol {p}}}$ -dependence is quadratic, therefore the first order symplectic Euler method implicit in ${\textstyle {\boldsymbol {p}}}$ is actually explicit. This is what is used in the canonical symplectic particle-in-cell (PIC) algorithm. To build high order explicit methods, we further note that the ${\textstyle {\boldsymbol {p}}}$ -dependence and ${\textstyle {\boldsymbol {x}}}$ -dependence in this ${\textstyle H({\boldsymbol {p}},{\boldsymbol {x}})}$ are product-separable, 2nd and 3rd order explicit symplectic algorithms can be constructed using generating functions, and arbitrarily high-order explicit symplectic integrators for time-dependent electromagnetic fields can also be constructed using Runge-Kutta techniques.

A more elegant and versatile alternative is to look at the following non-canonical symplectic structure of the problem, ${\begin{aligned}i_{({\dot {\boldsymbol {x}}},{\dot {\boldsymbol {v}}})}\Omega &=-dH,\\\Omega &=d({\boldsymbol {v}}+{\boldsymbol {A}})\wedge d{\boldsymbol {x}},\\[1ex]H&={\tfrac {1}{2}}{\boldsymbol {v}}^{2}+\phi .\end{aligned}}$ Here ${\textstyle \Omega }$ is a non-constant non-canonical symplectic form. General symplectic integrator for non-constant non-canonical symplectic structure, explicit or implicit, is not known to exist. However, for this specific problem, a family of high-order explicit non-canonical symplectic integrators can be constructed using the He splitting method. Splitting ${\textstyle H}$ into 4 parts, $H=H_{x}+H_{y}+H_{z}+H_{\phi },$ ${\begin{aligned}H_{x}&={\tfrac {1}{2}}v_{x}^{2},&H_{y}&={\tfrac {1}{2}}v_{y}^{2},\\[2pt]H_{z}&={\tfrac {1}{2}}v_{z}^{2},&H_{\phi }&=\phi ,\end{aligned}}$ we find serendipitously that for each subsystem, e.g., $i_{({\dot {\boldsymbol {x}}},{\dot {\boldsymbol {v}}})}\Omega =-dH_{x}$ and $i_{({\dot {\boldsymbol {x}}},{\dot {\boldsymbol {v}}})}\Omega =-dH_{\phi },$ the solution map can be written down explicitly and calculated exactly. Then explicit high-order non-canonical symplectic algorithms can be constructed using different compositions. Let ${\textstyle \Theta _{x},\Theta _{y},\Theta _{z}}$ and ${\textstyle \Theta _{\phi }}$ denote the exact solution maps for the 4 subsystems. A 1st-order symplectic scheme is ${\begin{aligned}\Theta _{1}{\left(\Delta \tau \right)}=\Theta _{x}{\left(\Delta \tau \right)}\,\Theta _{y}{\left(\Delta \tau \right)}\,\Theta _{z}{\left(\Delta \tau \right)}\,\Theta _{\phi }{\left(\Delta \tau \right)}\,.\end{aligned}}$ A symmetric 2nd-order symplectic scheme is, ${\begin{aligned}\Theta _{2}{\left(\Delta \tau \right)}={}&\Theta _{x}{\left({\tfrac {\Delta \tau }{2}}\right)}\,\Theta _{y}{\left({\tfrac {\Delta \tau }{2}}\right)}\,\Theta _{z}{\left({\tfrac {\Delta \tau }{2}}\right)}\,\Theta _{\phi }{\left(\Delta \tau \right)}\\&\Theta _{z}{\left({\tfrac {\Delta t}{2}}\right)}\,\Theta _{y}{\left({\tfrac {\Delta t}{2}}\right)}\,\Theta _{x}{\left({\tfrac {\Delta t}{2}}\right)},\end{aligned}}$ which is a customarily modified Strang splitting. A ${\textstyle 2(\ell +1)}$ -th order scheme can be constructed from a ${\textstyle 2\ell }$ -th order scheme using the method of triple jump, $\Theta _{2(\ell +1)}(\Delta \tau )=\Theta _{2\ell }(\alpha _{\ell }\Delta \tau )\,\Theta _{2\ell }(\beta _{\ell }\Delta \tau )\,\Theta _{2\ell }(\alpha _{\ell }\Delta \tau )\,,$ ${\begin{aligned}\alpha _{\ell }&={\frac {1}{2-2^{1/(2\ell +1)}}},&\beta _{\ell }&=1-2\alpha _{\ell }\,.\end{aligned}}$ The He splitting method is one of key techniques used in the structure-preserving geometric particle-in-cell (PIC) algorithms.
