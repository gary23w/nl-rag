---
title: "Positive operator"
source: https://en.wikipedia.org/wiki/Positive_operator
domain: operator-algebras
license: CC-BY-SA-4.0
tags: operator algebra, von neumann algebra, banach algebra, gelfand representation
fetched: 2026-07-02
---

# Positive operator

In mathematics (specifically linear algebra, operator theory, and functional analysis) as well as physics, a linear operator A acting on an inner product space is called **positive-semidefinite** (or *non-negative*) if, for every $x\in \operatorname {Dom} (A)$ , $\langle Ax,x\rangle \in \mathbb {R}$ and $\langle Ax,x\rangle \geq 0$ , where $\operatorname {Dom} (A)$ is the domain of A . Positive-semidefinite operators are denoted as $A\geq 0$ . The operator is said to be **positive-definite**, and written $A>0$ , if $\langle Ax,x\rangle >0$ for all $x\in \mathop {\mathrm {Dom} } (A)\setminus \{0\}$ .

Many authors define a **positive operator** A to be a self-adjoint (or at least symmetric) non-negative operator. We show below that for a complex Hilbert space the self adjointness follows automatically from non-negativity. For a real Hilbert space non-negativity does not imply self adjointness.

In physics (specifically quantum mechanics), such operators represent quantum states, via the density matrix formalism.

## Cauchy–Schwarz inequality

Take the inner product $\langle \cdot ,\cdot \rangle$ to be anti-linear on the *first* argument and linear on the second and suppose that A is positive and symmetric, the latter meaning that $\langle Ax,y\rangle =\langle x,Ay\rangle$ . Then the non negativity of

${\begin{aligned}\langle A(\lambda x+\mu y),\lambda x+\mu y\rangle =|\lambda |^{2}\langle Ax,x\rangle +\lambda ^{*}\mu \langle Ax,y\rangle +\lambda \mu ^{*}\langle Ay,x\rangle +|\mu |^{2}\langle Ay,y\rangle \\[1mm]=|\lambda |^{2}\langle Ax,x\rangle +\lambda ^{*}\mu \langle Ax,y\rangle +\lambda \mu ^{*}(\langle Ax,y\rangle )^{*}+|\mu |^{2}\langle Ay,y\rangle \end{aligned}}$

for all complex $\lambda$ and $\mu$ shows that

$\left|\langle Ax,y\rangle \right|^{2}\leq \langle Ax,x\rangle \langle Ay,y\rangle .$

It follows that $\mathop {\text{Im}} A\perp \mathop {\text{Ker}} A.$ If A is defined everywhere, and $\langle Ax,x\rangle =0,$ then $Ax=0.$

## On a complex Hilbert space, if an operator is non-negative then it is symmetric

For $x,y\in \operatorname {Dom} A,$ the polarization identity

${\begin{aligned}\langle Ax,y\rangle ={\frac {1}{4}}({}&\langle A(x+y),x+y\rangle -\langle A(x-y),x-y\rangle \\[1mm]&{}-i\langle A(x+iy),x+iy\rangle +i\langle A(x-iy),x-iy\rangle )\end{aligned}}$

and the fact that $\langle Ax,x\rangle =\langle x,Ax\rangle ,$ for positive operators, show that $\langle Ax,y\rangle =\langle x,Ay\rangle ,$ so A is symmetric.

In contrast with the complex case, a positive-semidefinite operator on a real Hilbert space $H_{\mathbb {R} }$ may not be symmetric. As a counterexample, define $A:\mathbb {R} ^{2}\to \mathbb {R} ^{2}$ to be an operator of rotation by an acute angle $\varphi \in (-\pi /2,\pi /2).$ Then $\langle Ax,x\rangle =\|Ax\|\|x\|\cos \varphi >0,$ but $A^{*}=A^{-1}\neq A,$ so A is not symmetric.

## If an operator is non-negative and defined on the whole complex Hilbert space, then it is self-adjoint and bounded

The symmetry of A implies that $\operatorname {Dom} A\subseteq \operatorname {Dom} A^{*}$ and $A=A^{*}|_{\operatorname {Dom} (A)}.$ For A to be self-adjoint, it is necessary that $\operatorname {Dom} A=\operatorname {Dom} A^{*}.$ In our case, the equality of domains holds because $H_{\mathbb {C} }=\operatorname {Dom} A\subseteq \operatorname {Dom} A^{*},$ so A is indeed self-adjoint. The fact that A is bounded now follows from the Hellinger–Toeplitz theorem.

This property does not hold on $H_{\mathbb {R} }.$

## Partial order of self-adjoint operators

A natural partial ordering of self-adjoint operators arises from the definition of positive operators. Define $B\geq A$ if the following hold:

1. A and B are self-adjoint
2. $B-A\geq 0$

It can be seen that a similar result as the Monotone convergence theorem holds for monotone increasing, bounded, self-adjoint operators on Hilbert spaces.

## Application to physics: quantum states

The definition of a quantum system includes a complex separable Hilbert space $H_{\mathbb {C} }$ and a set ${\cal {S}}$ of positive trace-class operators $\rho$ on $H_{\mathbb {C} }$ for which $\mathop {\text{Trace}} \rho =1.$ The set ${\cal {S}}$ is *the set of states*. Every $\rho \in {\cal {S}}$ is called a *state* or a *density operator*. For $\psi \in H_{\mathbb {C} },$ where $\|\psi \|=1,$ the operator $P_{\psi }$ of projection onto the span of $\psi$ is called a *pure state*. (Since each pure state is identifiable with a unit vector $\psi \in H_{\mathbb {C} },$ some sources define pure states to be unit elements from $H_{\mathbb {C} }).$ States that are not pure are called *mixed*.
