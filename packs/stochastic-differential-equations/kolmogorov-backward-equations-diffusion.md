---
title: "Kolmogorov backward equations (diffusion)"
source: https://en.wikipedia.org/wiki/Kolmogorov_backward_equations_(diffusion)
domain: stochastic-differential-equations
license: CC-BY-SA-4.0
tags: stochastic differential equation, euler-maruyama method, milstein method, langevin equation
fetched: 2026-07-02
---

# Kolmogorov backward equations (diffusion)

The **Kolmogorov backward equation (KBE)** and its adjoint, the Kolmogorov forward equation, are partial differential equations (PDE) that arise in the theory of continuous-time continuous-state Markov processes. Both were published by Andrey Kolmogorov in 1931. Later it was realized that the forward equation was already known to physicists under the name Fokker–Planck equation; the KBE on the other hand was new.

## Overview

The Kolmogorov forward equation is used to evolve the state of a system forward in time. Given an initial probability distribution $p_{t}(x)$ for a system being in state x at time $t,$ the forward PDE is integrated to obtain $p_{s}(x)$ at later times $s>t.$ A common case takes the initial value $p_{t}(x)$ to be a Dirac delta function centered on the known initial state $x.$

The Kolmogorov backward equation is used to estimate the probability of the current system evolving so that its future state at time $s>t$ is given by some fixed probability function $p_{s}(x).$ That is, the probability distribution in the future is given as a boundary condition, and the backwards PDE is integrated backwards in time.

A common boundary condition is to ask that the future state is contained in some subset of states $B,$ the **target set**. Writing the set membership function as $1_{B},$ so that $1_{B}(x)=1$ if $x\in B$ and zero otherwise, the backward equation expresses the **hit probability** $p_{t}(x)$ that in the future, the set membership will be sharp, given by $p_{s}(x)=1_{B}(x)/\Vert B\Vert .$ Here, $\Vert B\Vert$ is just the size of the set $B,$ a normalization so that the total probability at time s integrates to one.

## Kolmogorov backward equation

Let $\{X_{t}\}_{0\leq t\leq T}$ be the solution of the stochastic differential equation

$dX_{t}\;=\;\mu {\bigl (}t,X_{t}{\bigr )}\,dt\;+\;\sigma {\bigl (}t,X_{t}{\bigr )}\,dW_{t},\quad 0\;\leq \;t\;\leq \;T,$

where $W_{t}$ is a (possibly multi-dimensional) Wiener process (Brownian motion), $\mu$ is the drift coefficient, and $\sigma$ is related to the diffusion coefficient D as $D=\sigma ^{2}/2.$ Define the transition density (or fundamental solution) $p(t,x;\,T,y)$ by

$p(t,x;\,T,y)\;=\;{\frac {\mathbb {P} [\,X_{T}\in dy\,\mid \,X_{t}=x\,]}{dy}},\quad t<T.$

Then the usual Kolmogorov backward equation for p is

${\frac {\partial p}{\partial t}}(t,x;\,T,y)\;+\;A\,p(t,x;\,T,y)\;=\;0,\quad \lim _{t\to T}\,p(t,x;\,T,y)\;=\;\delta _{y}(x),$

where $\delta _{y}(x)$ is the Dirac delta in x centered at y , and A is the infinitesimal generator of the diffusion:

$A\,f(x)\;=\;\sum _{i}\,\mu _{i}(x)\,{\frac {\partial f}{\partial x_{i}}}(x)\;+\;{\frac {1}{2}}\,\sum _{i,j}\,{\bigl [}\sigma (x)\,\sigma (x)^{\mathsf {T}}{\bigr ]}_{ij}\,{\frac {\partial ^{2}f}{\partial x_{i}\,\partial x_{j}}}(x).$

## Feynman–Kac formula

The backward Kolmogorov equation can be used to derive the Feynman–Kac formula. Given a function F that satisfies the boundary value problem

${\frac {\partial F}{\partial t}}(t,x)\;+\;\mu (t,x)\,{\frac {\partial F}{\partial x}}(t,x)\;+\;{\frac {1}{2}}\,\sigma ^{2}(t,x)\,{\frac {\partial ^{2}F}{\partial x^{2}}}(t,x)\;=\;0,\quad 0\leq t\leq T,\quad F(T,x)\;=\;\Phi (x)$

and given $\{X_{t}\}_{0\leq t\leq T},$ that, just as before, is a solution of

$dX_{t}\;=\;\mu (t,X_{t})\,dt\;+\;\sigma (t,X_{t})\,dW_{t},\quad 0\leq t\leq T,$

then if the expectation value is finite

$\int _{0}^{T}\,\mathbb {E} \!{\Bigl [}{\bigl (}\sigma (t,X_{t})\,{\frac {\partial F}{\partial x}}(t,X_{t}){\bigr )}^{2}{\Bigr ]}\,dt\;<\;\infty ,$

then the Feynman–Kac formula is obtained:

$F(t,x)\;=\;\mathbb {E} \!{\bigl [}\;\Phi (X_{T})\,{\big |}\;X_{t}=x{\bigr ]}.$

**Proof.** Apply Itô's formula to $F(s,X_{s})$ for $t\leq s\leq T$ :

$F(T,X_{T})\;=\;F(t,X_{t})\;+\;\int _{t}^{T}\!{\Bigl \{}{\frac {\partial F}{\partial s}}(s,X_{s})\;+\;\mu (s,X_{s})\,{\frac {\partial F}{\partial x}}(s,X_{s})\;+\;{\tfrac {1}{2}}\,\sigma ^{2}(s,X_{s})\,{\frac {\partial ^{2}F}{\partial x^{2}}}(s,X_{s}){\Bigr \}}\,ds\;+\;\int _{t}^{T}\!\sigma (s,X_{s})\,{\frac {\partial F}{\partial x}}(s,X_{s})\,dW_{s}.$

Because F solves the PDE, the first integral is zero. Taking conditional expectation and using the martingale property of the Itô integral gives

$\mathbb {E} \!{\bigl [}F(T,X_{T})\,{\big |}\;X_{t}=x{\bigr ]}\;=\;F(t,x).$

Substitute $F(T,X_{T})=\Phi (X_{T})$ to conclude

$F(t,x)\;=\;\mathbb {E} \!{\bigl [}\;\Phi (X_{T})\,{\big |}\;X_{t}=x{\bigr ]}.$

## Derivation of the backward Kolmogorov equation

The Feynman–Kac representation can be used to find the PDE solved by the transition densities of solutions to SDEs. Suppose

$dX_{t}\;=\;\mu (t,X_{t})\,dt\;+\;\sigma (t,X_{t})\,dW_{t}.$

For any set B , define

$p_{B}(t,x;\,T)\;\triangleq \;\mathbb {P} \!{\bigl [}X_{T}\in B\,\mid \,X_{t}=x{\bigr ]}\;=\;\mathbb {E} \!{\bigl [}\mathbf {1} _{B}(X_{T})\,{\big |}\;X_{t}=x{\bigr ]}.$

By Feynman–Kac (under integrability conditions), taking $\Phi =\mathbf {1} _{B}$ , then

${\frac {\partial p_{B}}{\partial t}}(t,x;\,T)\;+\;A\,p_{B}(t,x;\,T)\;=\;0,\quad p_{B}(T,x;\,T)\;=\;\mathbf {1} _{B}(x),$

where

$A\,f(t,x)\;=\;\mu (t,x)\,{\frac {\partial f}{\partial x}}(t,x)\;+\;{\tfrac {1}{2}}\,\sigma ^{2}(t,x)\,{\frac {\partial ^{2}f}{\partial x^{2}}}(t,x).$

Assuming Lebesgue measure as the reference, write $|B|$ for its measure. The transition density $p(t,x;\,T,y)$ is

$p(t,x;\,T,y)\;\triangleq \;\lim _{B\to y}\,{\frac {1}{|B|}}\,\mathbb {P} \!{\bigl [}X_{T}\in B\,\mid \,X_{t}=x{\bigr ]}.$

Then

${\frac {\partial p}{\partial t}}(t,x;\,T,y)\;+\;A\,p(t,x;\,T,y)\;=\;0,\quad p(t,x;\,T,y)\;\to \;\delta _{y}(x)\quad {\text{as }}t\;\to \;T.$

## Derivation of the forward Kolmogorov equation

The Kolmogorov forward equation is

${\frac {\partial }{\partial T}}\,p{\bigl (}t,x;\,T,y{\bigr )}\;=\;A^{*}\!{\bigl [}p{\bigl (}t,x;\,T,y{\bigr )}{\bigr ]},\quad \lim _{T\to t}\,p(t,x;\,T,y)\;=\;\delta _{y}(x).$

For $T>r>t$ , the Markov property implies

$p(t,x;\,T,y)\;=\;\int _{-\infty }^{\infty }p{\bigl (}t,x;\,r,z{\bigr )}\,p{\bigl (}r,z;\,T,y{\bigr )}\,dz.$

Differentiate both sides w.r.t. r :

$0\;=\;\int _{-\infty }^{\infty }{\Bigl [}{\frac {\partial }{\partial r}}\,p{\bigl (}t,x;\,r,z{\bigr )}\,\cdot \,p{\bigl (}r,z;\,T,y{\bigr )}\;+\;p{\bigl (}t,x;\,r,z{\bigr )}\,\cdot \,{\frac {\partial }{\partial r}}\,p{\bigl (}r,z;\,T,y{\bigr )}{\Bigr ]}\,dz.$

From the backward Kolmogorov equation:

${\frac {\partial }{\partial r}}\,p{\bigl (}r,z;\,T,y{\bigr )}\;=\;-\,A\,p{\bigl (}r,z;\,T,y{\bigr )}.$

Substitute into the integral:

$0\;=\;\int _{-\infty }^{\infty }{\Bigl [}{\frac {\partial }{\partial r}}\,p{\bigl (}t,x;\,r,z{\bigr )}\,\cdot \,p{\bigl (}r,z;\,T,y{\bigr )}\;-\;p{\bigl (}t,x;\,r,z{\bigr )}\,\cdot \,A\,p{\bigl (}r,z;\,T,y{\bigr )}{\Bigr ]}\,dz.$

By definition of the adjoint operator $A^{*}$ :

$\int _{-\infty }^{\infty }{\bigl [}{\frac {\partial }{\partial r}}\,p{\bigl (}t,x;\,r,z{\bigr )}\;-\;A^{*}\,p{\bigl (}t,x;\,r,z{\bigr )}{\bigr ]}\,p{\bigl (}r,z;\,T,y{\bigr )}\,dz\;=\;0.$

Since $p(r,z;\,T,y)$ can be arbitrary, the bracket must vanish:

${\frac {\partial }{\partial r}}\,p{\bigl (}t,x;\,r,z{\bigr )}\;=\;A^{*}{\bigl [}p{\bigl (}t,x;\,r,z{\bigr )}{\bigr ]}.$

Relabel $r\to T$ and $z\to y$ , yielding the forward Kolmogorov equation:

${\frac {\partial }{\partial T}}\,p{\bigl (}t,x;\,T,y{\bigr )}\;=\;A^{*}\!{\bigl [}p{\bigl (}t,x;\,T,y{\bigr )}{\bigr ]},\quad \lim _{T\to t}\,p(t,x;\,T,y)\;=\;\delta _{y}(x).$

Finally,

$A^{*}\,g(x)\;=\;-\sum _{i}\,{\frac {\partial }{\partial x_{i}}}{\bigl [}\mu _{i}(x)\,g(x){\bigr ]}\;+\;{\frac {1}{2}}\,\sum _{i,j}\,{\frac {\partial ^{2}}{\partial x_{i}\,\partial x_{j}}}{\Bigl [}{\bigl (}\sigma (x)\,\sigma (x)^{\mathsf {T}}{\bigr )}_{ij}\,g(x){\Bigr ]}.$
