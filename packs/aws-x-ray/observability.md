---
title: "Observability"
source: https://en.wikipedia.org/wiki/Observability
domain: aws-x-ray
license: CC-BY-SA-4.0
tags: aws x-ray, distributed request tracing, application performance tracing, microservice observability
fetched: 2026-07-02
---

# Observability

**Observability** is a measure of how well internal states of a system can be inferred from knowledge of its external outputs. In control theory, the observability and controllability of a linear system are mathematical duals.

The concept of observability was introduced by the Hungarian-American engineer Rudolf E. Kálmán for linear dynamic systems. A dynamical system designed to estimate the state of a system from measurements of the outputs is called a *state observer* for that system, such as Kalman filters.

## Definition

Consider a physical system modeled in state-space representation. A system is said to be **observable** if, for every possible evolution of state and control vectors, the current state can be estimated using only the information from outputs (physically, this generally corresponds to information obtained by sensors). In other words, one can determine the behavior of the entire system from the system's outputs. On the other hand, if the system is not observable, there are state trajectories that are not distinguishable by only measuring the outputs.

## Linear time-invariant systems

For time-invariant linear systems in the state space representation, there are convenient tests to check whether a system is observable. Consider a SISO system with n state variables (see state space for details about MIMO systems) given by

${\dot {\mathbf {x} }}(t)=\mathbf {A} \mathbf {x} (t)+\mathbf {B} \mathbf {u} (t)$

$\mathbf {y} (t)=\mathbf {C} \mathbf {x} (t)+\mathbf {D} \mathbf {u} (t)$

### Observability matrix

If and only if the column rank of the *observability matrix*, defined as

${\mathcal {O}}={\begin{bmatrix}C\\CA\\CA^{2}\\\vdots \\CA^{n-1}\end{bmatrix}}$

is equal to n , then the system is observable. The rationale for this test is that if n columns are linearly independent, then each of the n state variables is viewable through linear combinations of the output variables y . Observability is a sufficient and necessary condition for the design of continuous-time state observers.

#### Observability index

The *observability index* v of a linear time-invariant discrete system is the smallest natural number for which the following is satisfied: ${\text{rank}}{({\mathcal {O}}_{v})}={\text{rank}}{({\mathcal {O}}_{v+1})}$ , where

${\mathcal {O}}_{v}={\begin{bmatrix}C\\CA\\CA^{2}\\\vdots \\CA^{v-1}\end{bmatrix}}.$

#### Unobservable subspace

The *unobservable subspace* N of the linear system is the kernel of the linear map G given by

> ${\begin{aligned}G\colon \mathbb {R} ^{n}&\rightarrow {\mathcal {C}}(\mathbb {R$

where ${\mathcal {C}}(\mathbb {R$ is the set of continuous functions from $\mathbb {R}$ to $\mathbb {R} ^{n}$ . N can also be written as

$N=\bigcap _{k=0}^{n-1}\ker(CA^{k})=\ker {\mathcal {O}}$

Since the system is observable if and only if $\operatorname {rank} ({\mathcal {O}})=n$ , the system is observable if and only if N is the zero subspace.

The following properties for the unobservable subspace are valid:

- $N\subset Ke(C)$
- $A(N)\subset N$
- $N=\bigcup \{S\subset R^{n}\mid S\subset Ke(C),A(S)\subset N\}$

#### Detectability

A slightly weaker notion than observability is *detectability*. A system is detectable if all the unobservable states are stable.

Detectability conditions are important in the context of sensor networks.

#### Functional observability

*Functional observability* is a property that extends the classical notion of observability for cases in which full-state observability is not possible or required (due to lack of measurement signals and sensor placement). Rather than requiring full-state reconstruction, functional observability establishes the condition under which a *linear functional* $\mathbf {z} (t)=\mathbf {F} \mathbf {x} (t)$ can still be estimated using solely information from the output signals. Formally, given a (typically low-dimensional) $r\times n$ matrix $\mathbf {F}$ , where $r\leq n$ , a system is functionally observable if and only if

$\operatorname {rank} {\begin{bmatrix}{\mathcal {O}}\\\mathbf {F} \end{bmatrix}}=\operatorname {rank} {\mathcal {O}}.$

Functional observability is an important concept because it determines the sufficient and necessary condition under which a *functional observer* (also known as a Darouach observer ) can be designed to asymptotically estimate $\mathbf {z} (t)$ . Under certain conditions, functional observability and output controllability are mathematical duals, implying that the problems of estimating and controlling a linear functional $\mathbf {z} (t)$ (rather than the full state $\mathbf {x} (t)$ ) are equivalent under a system transformation.

## Linear time-varying systems

Consider the continuous linear time-variant system

${\dot {\mathbf {x} }}(t)=A(t)\mathbf {x} (t)+B(t)\mathbf {u} (t)\,$

$\mathbf {y} (t)=C(t)\mathbf {x} (t).\,$

Suppose that the matrices A , B and C are given as well as inputs and outputs u and y for all $t\in [t_{0},t_{1}];$ then it is possible to determine $x(t_{0})$ to within an additive constant vector which lies in the null space of $M(t_{0},t_{1})$ defined by

$M(t_{0},t_{1})=\int _{t_{0}}^{t_{1}}\varphi (t,t_{0})^{T}C(t)^{T}C(t)\varphi (t,t_{0})\,dt$

where $\varphi$ is the state-transition matrix.

It is possible to determine a unique $x(t_{0})$ if $M(t_{0},t_{1})$ is nonsingular. In fact, it is not possible to distinguish the initial state for $x_{1}$ from that of $x_{2}$ if $x_{1}-x_{2}$ is in the null space of $M(t_{0},t_{1})$ .

Note that the matrix M defined as above has the following properties:

- $M(t_{0},t_{1})$ is symmetric
- $M(t_{0},t_{1})$ is positive semidefinite for $t_{1}\geq t_{0}$
- $M(t_{0},t_{1})$ satisfies the linear matrix differential equation

${\frac {d}{dt}}M(t,t_{1})=-A(t)^{T}M(t,t_{1})-M(t,t_{1})A(t)-C(t)^{T}C(t),\;M(t_{1},t_{1})=0$

- $M(t_{0},t_{1})$ satisfies the equation

$M(t_{0},t_{1})=M(t_{0},t)+\varphi (t,t_{0})^{T}M(t,t_{1})\varphi (t,t_{0})$

### Observability matrix generalization

The system is observable in $[t_{0},t_{1}]$ if and only if there exists an interval $[t_{0},t_{1}]$ in $\mathbb {R}$ such that the matrix $M(t_{0},t_{1})$ is nonsingular.

If $A(t),C(t)$ are analytic, then the system is observable in the interval [ $t_{0}$ , $t_{1}$ ] if there exists ${\bar {t}}\in [t_{0},t_{1}]$ and a positive integer *k* such that

$\operatorname {rank} {\begin{bmatrix}&N_{0}({\bar {t}})&\\&N_{1}({\bar {t}})&\\&\vdots &\\&N_{k}({\bar {t}})&\end{bmatrix}}=n,$

where $N_{0}(t):=C(t)$ and $N_{i}(t)$ is defined recursively as

$N_{i+1}(t):=N_{i}(t)A(t)+{\frac {\mathrm {d} }{\mathrm {d} t}}N_{i}(t),\ i=0,\ldots ,k-1$

#### Example

Consider a system varying analytically in $(-\infty ,\infty )$ and matrices

> $A(t)={\begin{bmatrix}t&1&0\\0&t^{3}&0\\0&0&t^{2}\end{bmatrix}},\,C(t)={\begin{bmatrix}1&0&1\end{bmatrix}}.$

Then ${\begin{bmatrix}N_{0}(0)\\N_{1}(0)\\N_{2}(0)\end{bmatrix}}={\begin{bmatrix}1&0&1\\0&1&0\\1&0&0\end{bmatrix}}$ , and since this matrix has rank = 3, the system is observable on every nontrivial interval of $\mathbb {R}$ .

## Nonlinear systems

Given the system ${\dot {x}}=f(x)+\sum _{j=1}^{m}g_{j}(x)u_{j}$ , $y_{i}=h_{i}(x),i\in p$ . Where $x\in \mathbb {R} ^{n}$ the state vector, $u\in \mathbb {R} ^{m}$ the input vector and $y\in \mathbb {R} ^{p}$ the output vector. $f,g,h$ are to be smooth vector fields.

Define the observation space ${\mathcal {O}}_{s}$ to be the space containing all repeated Lie derivatives, then the system is observable in $x_{0}$ if and only if $\dim(d{\mathcal {O}}_{s}(x_{0}))=n$ , where

$d{\mathcal {O}}_{s}(x_{0})=\operatorname {span} (dh_{1}(x_{0}),\ldots ,dh_{p}(x_{0}),dL_{v_{i}}L_{v_{i-1}},\ldots ,L_{v_{1}}h_{j}(x_{0})),\ j\in p,k=1,2,\ldots .$

Early criteria for observability in nonlinear dynamic systems were discovered by Griffith and Kumar, Kou, Elliot and Tarn, and Singh.

There also exist an observability criteria for nonlinear time-varying systems.

## Static systems and general topological spaces

Observability may also be characterized for steady state systems (systems typically defined in terms of algebraic equations and inequalities), or more generally, for sets in $\mathbb {R} ^{n}$ . Just as observability criteria are used to predict the behavior of Kalman filters or other observers in the dynamic system case, observability criteria for sets in $\mathbb {R} ^{n}$ are used to predict the behavior of data reconciliation and other static estimators. In the nonlinear case, observability can be characterized for individual variables, and also for local estimator behavior rather than just global behavior.
