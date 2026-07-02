---
title: "Bloch sphere"
source: https://en.wikipedia.org/wiki/Bloch_sphere
domain: quantum-computing
license: CC-BY-SA-4.0
tags: quantum computing, quantum logic gate, quantum entanglement, quantum circuit
fetched: 2026-07-02
---

# Bloch sphere

In quantum mechanics and computing, the **Bloch sphere** is a geometrical representation of the pure state space of a two-level quantum mechanical system (qubit), named after the physicist Felix Bloch.

Mathematically each quantum mechanical system is associated with a separable complex Hilbert space H . A pure state of a quantum system is represented by a non-zero vector $\psi$ in H . The vectors $\psi$ and $\lambda \psi$ (with $\lambda$ a non-zero complex number) represent the same state. A system with *n* mutually orthogonal quantum states can be described by a Hilbert space of dimension *n*. Pure states can be represented as equivalence classes, or, *rays* in a projective Hilbert space $\mathbf {P} (H_{n})=\mathbb {C} \mathbf {P} ^{n-1}$ . For a two-dimensional Hilbert space, the space of all such states is the complex projective line $\mathbb {C} \mathbf {P} ^{1}.$ This is the Bloch sphere, which can be mapped to the Riemann sphere.

The Bloch sphere is a unit 2-sphere, with antipodal points corresponding to a pair of mutually orthogonal state vectors. The north and south poles of the Bloch sphere are typically chosen to correspond to the standard basis vectors $|0\rangle$ and $|1\rangle$ , respectively, which in turn might correspond e.g. to the spin-up and spin-down states of an electron. This choice is arbitrary, however. The points on the surface of the sphere correspond to the pure states of the system, whereas the interior points correspond to the mixed states. The Bloch sphere may be generalized to an *n*-level quantum system, but then the visualization is less useful.

The natural metric on the Bloch sphere is the Fubini–Study metric. The mapping from the unit 3-sphere in the two-dimensional state space $\mathbb {C} ^{2}$ to the Bloch sphere is the Hopf fibration, with each ray of spinors mapping to one point on the Bloch sphere.

## Definition

Given an orthonormal basis, any pure state $|\psi \rangle$ of a two-level quantum system can be written as a superposition of the basis vectors $|0\rangle$ and $|1\rangle$ , where the coefficient of (or contribution from) each of the two basis vectors is a complex number. This means that the state is described by four real numbers. However, only the relative phase between the coefficients of the two basis vectors has any physical meaning (the phase of the quantum system is not directly measurable), so that there is redundancy in this description. We can take the coefficient of $|0\rangle$ to be real and non-negative. This allows the state to be described by only three real numbers, giving rise to the three dimensions of the Bloch sphere.

We also know from quantum mechanics that the total probability of the system has to be one:

$\langle \psi |\psi \rangle =1$

, or equivalently

${\left\||\psi \rangle \right\|\,}^{2}=1$

.

Given this constraint, we can write $|\psi \rangle$ using the following representation:

$|\psi \rangle =\cos \left(\theta /2\right)|0\rangle \,+\,e^{i\phi }\sin \left(\theta /2\right)|1\rangle =\cos \left(\theta /2\right)|0\rangle \,+\,(\cos \phi +i\sin \phi )\,\sin \left(\theta /2\right)|1\rangle$

, where

$0\leq \theta \leq \pi$

and

$0\leq \phi <2\pi$

.

The representation is always unique, because, even though the value of $\phi$ is not unique when $|\psi \rangle$ is one of the states (see Bra-ket notation) $|0\rangle$ or $|1\rangle$ , the point represented by $\theta$ and $\phi$ is unique.

The parameters $\theta \,$ and $\phi \,$ , re-interpreted in spherical coordinates as respectively the colatitude with respect to the *z*-axis and the longitude with respect to the *x*-axis, specify a point

${\vec {a}}=(\sin \theta \cos \phi ,\;\sin \theta \sin \phi ,\;\cos \theta )=(u,v,w)$

on the unit sphere in $\mathbb {R} ^{3}$ .

For mixed states, one considers the density operator. Any two-dimensional density operator ρ can be expanded using the identity I and the Hermitian, traceless Pauli matrices ${\vec {\sigma }}$ ,

${\begin{aligned}\rho &={\frac {1}{2}}\left(I+{\vec {a}}\cdot {\vec {\sigma }}\right)\\&={\frac {1}{2}}{\begin{pmatrix}1&0\\0&1\end{pmatrix}}+{\frac {a_{x}}{2}}{\begin{pmatrix}0&1\\1&0\end{pmatrix}}+{\frac {a_{y}}{2}}{\begin{pmatrix}0&-i\\i&0\end{pmatrix}}+{\frac {a_{z}}{2}}{\begin{pmatrix}1&0\\0&-1\end{pmatrix}}\\&={\frac {1}{2}}{\begin{pmatrix}1+a_{z}&a_{x}-ia_{y}\\a_{x}+ia_{y}&1-a_{z}\end{pmatrix}}\end{aligned}}$

,

where ${\vec {a}}\in \mathbb {R} ^{3}$ is called the **Bloch vector**.

It is this vector that indicates the point within the sphere that corresponds to a given mixed state. Specifically, as a basic feature of the Pauli vector, the eigenvalues of ρ are ${\frac {1}{2}}\left(1\pm |{\vec {a}}|\right)$ . Density operators must be positive-semidefinite, so it follows that $\left|{\vec {a}}\right|\leq 1$ .

For pure states, one then has

$\operatorname {tr} \left(\rho ^{2}\right)={\frac {1}{2}}\left(1+\left|{\vec {a}}\right|^{2}\right)=1\quad \Leftrightarrow \quad \left|{\vec {a}}\right|=1~,$

in comportance with the above.

As a consequence, the surface of the Bloch sphere represents all the pure states of a two-dimensional quantum system, whereas the interior corresponds to all the mixed states.

## *u*, *v*, *w* representation

The Bloch vector ${\vec {a}}=(u,v,w)$ can be represented in the following basis, with reference to the density operator $\rho$ :

$u=\rho _{10}+\rho _{01}=2\operatorname {Re} (\rho _{01})$

$v=i(\rho _{01}-\rho _{10})=2\operatorname {Im} (\rho _{10})$

$w=\rho _{00}-\rho _{11}$

where

$\rho ={\begin{pmatrix}\rho _{00}&\rho _{01}\\\rho _{10}&\rho _{11}\end{pmatrix}}={\frac {1}{2}}{\begin{pmatrix}1+w&u-iv\\u+iv&1-w\end{pmatrix}}.$

This basis is often used in laser theory, where w is known as the population inversion. In this basis, the values $u,v,w$ are the expectations of the three Pauli matrices $X,Y,Z$ , allowing one to identify the three coordinates with x y and z axes.

## Pure states

Consider an *n*-level quantum mechanical system. This system is described by an *n*-dimensional Hilbert space *H**n*. The pure state space is by definition the set of rays of *H**n*.

**Theorem**. Let U(*n*) be the Lie group of unitary matrices of size *n*. Then the pure state space of *H**n* can be identified with the compact coset space

$\operatorname {U} (n)/(\operatorname {U} (n-1)\times \operatorname {U} (1)).$

To prove this fact, note that there is a natural group action of U(*n*) on the set of states of *H**n*. This action is continuous and transitive on the pure states. For any state $|\psi \rangle$ , the isotropy group of $|\psi \rangle$ , (defined as the set of elements g of U(*n*) such that $g|\psi \rangle =|\psi \rangle$ ) is isomorphic to the product group

$\operatorname {U} (n-1)\times \operatorname {U} (1).$

In linear algebra terms, this can be justified as follows. Any g of U(*n*) that leaves $|\psi \rangle$ invariant must have $|\psi \rangle$ as an eigenvector. Since the corresponding eigenvalue must be a complex number of modulus 1, this gives the U(1) factor of the isotropy group. The other part of the isotropy group is parametrized by the unitary matrices on the orthogonal complement of $|\psi \rangle$ , which is isomorphic to U(*n* − 1). From this the assertion of the theorem follows from basic facts about transitive group actions of compact groups.

The important fact to note above is that the *unitary group acts transitively* on pure states.

Now the (real) dimension of U(*n*) is *n*2. This is easy to see since the exponential map

$A\mapsto e^{iA}$

is a local homeomorphism from the space of self-adjoint complex matrices to U(*n*). The space of self-adjoint complex matrices has real dimension *n*2.

**Corollary**. The real dimension of the pure state space of *H**n* is 2*n* − 2.

In fact,

$n^{2}-\left((n-1)^{2}+1\right)=2n-2.\quad$

Let us apply this to consider the real dimension of an *m* qubit quantum register. The corresponding Hilbert space has dimension 2*m*.

**Corollary**. The real dimension of the pure state space of an *m*-qubit quantum register is 2*m*+1 − 2.

### Plotting pure two-spinor states through stereographic projection

Mathematically the Bloch sphere for a two-spinor state can be mapped to a Riemann sphere $\mathbb {C} \mathbf {P} ^{1}$ , i.e., the projective Hilbert space $\mathbf {P} (H_{2})$ with the 2-dimensional complex Hilbert space $H_{2}$ a representation space of SO(3). Given a pure state

$\alpha \left|\uparrow \right\rangle +\beta \left|\downarrow \right\rangle =\left|\nearrow \right\rangle$

where $\alpha$ and $\beta$ are complex numbers which are normalized so that

$|\alpha |^{2}+|\beta |^{2}=\alpha ^{*}\alpha +\beta ^{*}\beta =1$

and such that $\langle \downarrow |\uparrow \rangle =0$ and $\langle \downarrow |\downarrow \rangle =\langle \uparrow |\uparrow \rangle =1$ , i.e., such that $\left|\uparrow \right\rangle$ and $\left|\downarrow \right\rangle$ form a basis and have diametrically opposite representations on the Bloch sphere, then let

$u={\beta \over \alpha }={\alpha ^{*}\beta \over \alpha ^{*}\alpha }={\alpha ^{*}\beta \over |\alpha |^{2}}=u_{x}+iu_{y}$

be their ratio.

If the Bloch sphere is thought of as being embedded in $\mathbb {R} ^{3}$ with its center at the origin and with radius one, then the plane *z* = 0 (which intersects the Bloch sphere at a great circle; the sphere's equator, as it were) can be thought of as an Argand diagram. Plot point *u* in this plane — so that in $\mathbb {R} ^{3}$ it has coordinates $(u_{x},u_{y},0)$ .

Draw a straight line through *u* and through the point on the sphere that represents $\left|\downarrow \right\rangle$ . (Let (0,0,1) represent $\left|\uparrow \right\rangle$ and (0,0,−1) represent $\left|\downarrow \right\rangle$ .) This line intersects the sphere at another point besides $\left|\downarrow \right\rangle$ . (The only exception is when $u=\infty$ , i.e., when $\alpha =0$ and $\beta \neq 0$ .) Call this point *P*. Point *u* on the plane *z* = 0 is the stereographic projection of point *P* on the Bloch sphere. The vector with tail at the origin and tip at *P* is the direction in 3-D space corresponding to the spinor $\left|\nearrow \right\rangle$ . The coordinates of *P* are

$P_{x}={2u_{x} \over 1+u_{x}^{2}+u_{y}^{2}},$

$P_{y}={2u_{y} \over 1+u_{x}^{2}+u_{y}^{2}},$

$P_{z}={1-u_{x}^{2}-u_{y}^{2} \over 1+u_{x}^{2}+u_{y}^{2}}.$

## Density operators

Formulations of quantum mechanics in terms of pure states are adequate for isolated systems; in general quantum mechanical systems need to be described in terms of density operators. The Bloch sphere parametrizes not only pure states but mixed states for 2-level systems. The density operator describing the mixed-state of a 2-level quantum system (qubit) corresponds to a point *inside* the Bloch sphere with the following coordinates:

$\left(\sum p_{i}x_{i},\sum p_{i}y_{i},\sum p_{i}z_{i}\right),$

where $p_{i}$ is the probability of the individual states within the ensemble and $x_{i},y_{i},z_{i}$ are the coordinates of the individual states (on the *surface* of Bloch sphere). The set of all points on and inside the Bloch sphere is known as the *Bloch ball.*

For states of higher dimensions there is difficulty in extending this to mixed states. The topological description is complicated by the fact that the unitary group does not act transitively on density operators. The orbits moreover are extremely diverse as follows from the following observation:

**Theorem**. Suppose *A* is a density operator on an *n* level quantum mechanical system whose distinct eigenvalues are μ1, ..., μ*k* with multiplicities *n*1, ..., *n**k*. Then the group of unitary operators *V* such that *V A V** = *A* is isomorphic (as a Lie group) to

$\operatorname {U} (n_{1})\times \cdots \times \operatorname {U} (n_{k}).$

In particular the orbit of *A* is isomorphic to

$\operatorname {U} (n)/\left(\operatorname {U} (n_{1})\times \cdots \times \operatorname {U} (n_{k})\right).$

It is possible to generalize the construction of the Bloch ball to dimensions larger than 2, but the geometry of such a "Bloch body" is more complicated than that of a ball.

## Rotations

A useful advantage of the Bloch sphere representation is that the evolution of the qubit state is describable by rotations of the Bloch sphere. The most concise explanation for why this is the case is that the Lie algebra for the group of unitary and hermitian matrices $SU(2)$ is isomorphic to the Lie algebra of the group of three dimensional rotations $SO(3)$ .

### Rotation operators about the Bloch basis

The rotations of the Bloch sphere about the Cartesian axes in the Bloch basis are given by

${\begin{aligned}R_{x}(\theta )&=e^{(-i\theta X/2)}=\cos(\theta /2)I-i\sin(\theta /2)X={\begin{bmatrix}\cos \theta /2&-i\sin \theta /2\\-i\sin \theta /2&\cos \theta /2\end{bmatrix}}\\R_{y}(\theta )&=e^{(-i\theta Y/2)}=\cos(\theta /2)I-i\sin(\theta /2)Y={\begin{bmatrix}\cos \theta /2&-\sin \theta /2\\\sin \theta /2&\cos \theta /2\end{bmatrix}}\\R_{z}(\theta )&=e^{(-i\theta Z/2)}=\cos(\theta /2)I-i\sin(\theta /2)Z={\begin{bmatrix}e^{-i\theta /2}&0\\0&e^{i\theta /2}\end{bmatrix}}\end{aligned}}$

### Rotations about a general axis

If ${\hat {n}}=(n_{x},n_{y},n_{z})$ is a real unit vector in three dimensions, the rotation of the Bloch sphere about this axis is given by:

$R_{\hat {n}}(\theta )=\exp \left(-i\theta {\hat {n}}\cdot {\frac {1}{2}}{\vec {\sigma }}\right)$

An interesting thing to note is that this expression is identical under relabelling to the extended Euler formula for pure imaginary quaternions.

$\mathbf {q} =e^{{\frac {1}{2}}\theta (u_{x}\mathbf {i} +u_{y}\mathbf {j} +u_{z}\mathbf {k} )}=\cos {\frac {\theta }{2}}+(u_{x}\mathbf {i} +u_{y}\mathbf {j} +u_{z}\mathbf {k} )\sin {\frac {\theta }{2}}$

### Derivation of the Bloch rotation generator

Ballentine presents an intuitive derivation for the infinitesimal unitary transformation. This is important for understanding why the rotations of Bloch spheres are exponentials of linear combinations of Pauli matrices. Hence a brief treatment on this is given here. A more complete description in a quantum mechanical context can be found here.

Consider a family of unitary operators U representing a rotation about some axis. Since the rotation has one degree of freedom, the operator acts on a field of scalars S such that:

$U(0)=I$

$U(s_{1}+s_{2})=U(s_{1})U(s_{2})$

where $0,s_{1},s_{2},\in S$

We define the infinitesimal unitary as the Taylor expansion truncated at second order.

$U(s)=I+{\frac {dU}{ds}}{\Bigg |}_{s=0}s+O\left(s^{2}\right)$

By the unitary condition:

$U^{\dagger }U=I$

Hence

$U^{\dagger }U=I+s\left({\frac {dU}{ds}}{\Bigg |}_{s=0}+{\frac {dU^{\dagger }}{ds}}{\Bigg |}_{s=0}\right)+O\left(s^{2}\right)=I$

For this equality to hold true (assuming $O\left(s^{2}\right)$ is negligible) we require

${\frac {dU}{ds}}{\Bigg |}_{s=0}+{\frac {dU^{\dagger }}{ds}}{\Bigg |}_{s=0}=0$

.

This results in a solution of the form:

${\frac {dU}{ds}}{\Bigg |}_{s=0}=iK$

where K is any Hermitian transformation, and is called the generator of the unitary family. Hence

$U(s)=e^{iKs}$

Since the Pauli matrices $(\sigma _{x},\sigma _{y},\sigma _{z})$ are unitary Hermitian matrices and have eigenvectors corresponding to the Bloch basis, $({\hat {x}},{\hat {y}},{\hat {z}})$ , we can naturally see how a rotation of the Bloch sphere about an arbitrary axis ${\hat {n}}$ is described by

$R_{\hat {n}}(\theta )=\exp(-i\theta {\hat {n}}\cdot {\vec {\sigma }}/2)$

with the rotation generator given by $K={\hat {n}}\cdot {\vec {\sigma }}/2.$
