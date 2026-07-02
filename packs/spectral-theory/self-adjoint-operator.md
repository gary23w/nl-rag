---
title: "Self-adjoint operator"
source: https://en.wikipedia.org/wiki/Self-adjoint_operator
domain: spectral-theory
license: CC-BY-SA-4.0
tags: spectral theory, spectral theorem, self-adjoint operator, sturm-liouville theory
fetched: 2026-07-02
---

# Self-adjoint operator

In mathematics, a **self-adjoint operator** on a complex vector space V with inner product $\langle \cdot ,\cdot \rangle$ is a linear map A (from V to itself) that is its own adjoint. That is, $\langle Ax,y\rangle =\langle x,Ay\rangle$ for all $x,y\in V$ . If V is finite-dimensional with a given orthonormal basis, this is equivalent to the condition that the matrix of A is a Hermitian matrix, i.e., equal to its conjugate transpose $A^{*}$ . By the finite-dimensional spectral theorem, V has an orthonormal basis such that the matrix of A relative to this basis is a diagonal matrix with entries in the real numbers. This article deals with applying generalizations of this concept to operators on Hilbert spaces of arbitrary dimension.

Self-adjoint operators are used in functional analysis and quantum mechanics. In quantum mechanics their importance lies in the Dirac–von Neumann formulation of quantum mechanics, in which physical observables such as position, momentum, angular momentum and spin are represented by self-adjoint operators on a Hilbert space. Of particular significance is the Hamiltonian operator ${\hat {H}}$ defined by

${\hat {H}}\psi =-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}\psi +V\psi ,$

which as an observable corresponds to the total energy of a particle of mass m in a real potential field V . Differential operators are an important class of unbounded operators.

The structure of self-adjoint operators on infinite-dimensional Hilbert spaces essentially resembles the finite-dimensional case. That is to say, operators are self-adjoint if and only if they are unitarily equivalent to real-valued multiplication operators. With suitable modifications, this result can be extended to possibly unbounded operators on infinite-dimensional spaces. Since an everywhere-defined self-adjoint operator is necessarily bounded, one needs to be more attentive to the domain issue in the unbounded case. This is explained below in more detail.

## Definitions

Let H be a Hilbert space and A an unbounded (i.e. not necessarily bounded) linear operator with a dense domain $\operatorname {Dom} A\subseteq H.$ This condition holds automatically when H is finite-dimensional since $\operatorname {Dom} A=H$ for every linear operator on a finite-dimensional space.

The **graph** of an (arbitrary) operator A is the set $G(A)=\{(x,Ax)\mid x\in \operatorname {Dom} A\}.$ An operator B is said to **extend** A if $G(A)\subseteq G(B).$ This is written as $A\subseteq B.$

Let the inner product $\langle \cdot ,\cdot \rangle$ be conjugate linear on the *second* argument. The **adjoint operator** $A^{*}$ acts on the subspace $\operatorname {Dom} A^{*}\subseteq H$ consisting of the elements y such that

$\langle Ax,y\rangle =\langle x,A^{*}y\rangle ,\quad \forall x\in \operatorname {Dom} A.$

The densely defined operator A is called **symmetric** (or **Hermitian**) if $A\subseteq A^{*}$ , i.e., if $\operatorname {Dom} A\subseteq \operatorname {Dom} A^{*}$ and $Ax=A^{*}x$ for all $x\in \operatorname {Dom} A$ . Equivalently, A is symmetric if and only if

$\langle Ax,y\rangle =\langle x,Ay\rangle ,\quad \forall x,y\in \operatorname {Dom} A.$

Since $\operatorname {Dom} A^{*}\supseteq \operatorname {Dom} A$ is dense in H , symmetric operators are always closable (i.e. the closure of $G(A)$ is the graph of an operator). If $A^{*}$ is a closed extension of A , the smallest closed extension $A^{**}$ of A must be contained in $A^{*}$ . Hence,

$A\subseteq A^{**}\subseteq A^{*}$

for symmetric operators and

$A=A^{**}\subseteq A^{*}$

for closed symmetric operators.

The densely defined operator A is called **self-adjoint** if $A=A^{*}$ , that is, if and only if A is symmetric and $\operatorname {Dom} A=\operatorname {Dom} A^{*}$ . Equivalently, a closed symmetric operator A is self-adjoint if and only if $A^{*}$ is symmetric. If A is self-adjoint, then $\left\langle x,Ax\right\rangle$ is real for all $x\in \operatorname {Dom} A$ , i.e.,

$\langle x,Ax\rangle ={\overline {\langle Ax,x\rangle }}={\overline {\langle x,Ax\rangle }}\in \mathbb {R} ,\quad \forall x\in \operatorname {Dom} A.$

A symmetric operator A is said to be **essentially self-adjoint** if the closure of A is self-adjoint. Equivalently, A is essentially self-adjoint if it has a *unique* self-adjoint extension. In practical terms, having an essentially self-adjoint operator is almost as good as having a self-adjoint operator, since we merely need to take the closure to obtain a self-adjoint operator.

In physics, the term **Hermitian** refers to symmetric as well as self-adjoint operators alike. The subtle difference between the two is generally overlooked.

## Bounded self-adjoint operators

Let H be a Hilbert space and $A:\operatorname {Dom} (A)\to H$ a symmetric operator. According to Hellinger–Toeplitz theorem, if $\operatorname {Dom} (A)=H$ then A is necessarily bounded. A bounded operator $A:H\to H$ is self-adjoint if

$\langle Ax,y\rangle =\langle x,Ay\rangle ,\quad \forall x,y\in H.$

Every bounded operator $T:H\to H$ can be written in the complex form $T=A+iB$ where $A:H\to H$ and $B:H\to H$ are bounded self-adjoint operators.

Alternatively, every positive bounded linear operator $A:H\to H$ is self-adjoint if the Hilbert space H is *complex*.

### Properties

A bounded self-adjoint operator $A:H\to H$ defined on $\operatorname {Dom} \left(A\right)=H$ has the following properties:

- $A:H\to \operatorname {Im} A\subseteq H$ is invertible if the image of A is dense in $H.$
- The operator norm is given by $\left\|A\right\|=\sup \left\{|\langle x,Ax\rangle |:\|x\|=1\right\}$
- If $\lambda$ is an eigenvalue of A then $|\lambda |\leq \sup \left\{|\langle x,Ax\rangle |:\|x\|\leq 1\right\}$ ; the eigenvalues are real and the corresponding eigenvectors are orthogonal.

Bounded self-adjoint operators do not necessarily have an eigenvalue. If, however, A is a compact self-adjoint operator then it always has an eigenvalue $|\lambda |=\|A\|$ and corresponding normalized eigenvector.

## Spectrum of self-adjoint operators

Let $A:\operatorname {Dom} (A)\to H$ be an unbounded operator. The **resolvent set** (or **regular set**) of A is defined as

$\rho (A)=\left\{\lambda \in \mathbb {C} \,:\,\exists (A-\lambda I)^{-1}\;{\text{bounded and densely defined}}\right\}.$

If A is bounded, the definition reduces to $A-\lambda I$ being bijective on H . The **spectrum** of A is defined as the complement

$\sigma (A)=\mathbb {C} \setminus \rho (A).$

In finite dimensions, $\sigma (A)\subseteq \mathbb {C}$ consists exclusively of (complex) eigenvalues. The spectrum of a self-adjoint operator is always real (i.e. $\sigma (A)\subseteq \mathbb {R}$ ), though non-self-adjoint operators with real spectrum exist as well. For bounded (normal) operators, however, the spectrum is real *if and only if* the operator is self-adjoint. This implies, for example, that a non-self-adjoint operator with real spectrum is necessarily unbounded.

As a preliminary, define $S=\{x\in \operatorname {Dom} A\mid \Vert x\Vert =1\},$ $\textstyle m=\inf _{x\in S}\langle Ax,x\rangle$ and $\textstyle M=\sup _{x\in S}\langle Ax,x\rangle$ with $m,M\in \mathbb {R} \cup \{\pm \infty \}$ . Then, for every $\lambda \in \mathbb {C}$ and every $x\in \operatorname {Dom} A,$

$\Vert (A-\lambda )x\Vert \geq d(\lambda )\cdot \Vert x\Vert ,$

where $\textstyle d(\lambda )=\inf _{r\in [m,M]}|r-\lambda |.$

Indeed, let $x\in \operatorname {Dom} A\setminus \{0\}.$ By the Cauchy–Schwarz inequality,

$\Vert (A-\lambda )x\Vert \geq {\frac {|\langle (A-\lambda )x,x\rangle |}{\Vert x\Vert }}=\left|\left\langle A{\frac {x}{\Vert x\Vert }},{\frac {x}{\Vert x\Vert }}\right\rangle -\lambda \right|\cdot \Vert x\Vert \geq d(\lambda )\cdot \Vert x\Vert .$

If $\lambda \notin [m,M],$ then $d(\lambda )>0,$ and $A-\lambda I$ is called *bounded below*.

**Theorem**—Self-adjoint operator has real spectrum

Proof

Let A be self-adjoint and denote $R_{\lambda }=A-\lambda I$ with $\lambda \in \mathbb {C} .$ It suffices to prove that $\sigma (A)\subseteq [m,M].$

1. Let $\lambda \in \mathbb {C} \setminus [m,M].$ The goal is to prove the existence and boundedness of $R_{\lambda }^{-1},$ and show that $\operatorname {Dom} R_{\lambda }^{-1}=H.$ We begin by showing that $\ker R_{\lambda }=\{0\}$ and $\operatorname {Im} R_{\lambda }=H.$ As shown above, $R_{\lambda }$ is bounded below, i.e. $\Vert R_{\lambda }x\Vert \geq d(\lambda )\cdot \Vert x\Vert ,$ with $d(\lambda )>0.$ The triviality of $\ker R_{\lambda }$ follows.It remains to show that $\operatorname {Im} R_{\lambda }=H.$ Indeed, $\operatorname {Im} R_{\lambda }$ is closed. To prove this, pick a sequence $y_{n}=R_{\lambda }x_{n}\in \operatorname {Im} R_{\lambda }$ converging to some $y\in H.$ Since $\|x_{n}-x_{m}\|\leq {\frac {1}{d(\lambda )}}\|y_{n}-y_{m}\|,$ $x_{n}$ is fundamental. Hence, it converges to some $x\in H.$ Furthermore, $y_{n}+\lambda x_{n}=Ax_{n}$ and $y_{n}+\lambda x_{n}\to y+\lambda x.$ The arguments made thus far hold for any symmetric operator. It now follows from self-adjointness that A is closed, so $x\in \operatorname {Dom} A=\operatorname {Dom} R_{\lambda },$ $Ax=y+\lambda x\in \operatorname {Im} A,$ and consequently $y=R_{\lambda }x\in \operatorname {Im} R_{\lambda }.$ $\operatorname {Im} R_{\lambda }$ is dense in $H.$ The self-adjointness of A (i.e. $A^{*}=A$ ) implies $R_{\lambda }^{*}=R_{\bar {\lambda }}$ and thus $\left(\operatorname {Im} R_{\lambda }\right)^{\perp }=\ker R_{\bar {\lambda }}$ . The subsequent inclusion ${\bar {\lambda }}\in \mathbb {C} \setminus [m,M]$ implies $d({\bar {\lambda }})>0$ and, consequently, $\ker R_{\bar {\lambda }}=\{0\}.$
2. The operator $R_{\lambda }\colon \operatorname {Dom} A\to H$ has now been proven to be bijective, so $R_{\lambda }^{-1}$ exists and is everywhere defined. The graph of $R_{\lambda }^{-1}$ is the set $\{(R_{\lambda }x,x)\mid x\in \operatorname {Dom} A\}.$ Since $R_{\lambda }$ is closed (because A is), so is $R_{\lambda }^{-1}.$ By closed graph theorem, $R_{\lambda }^{-1}$ is bounded, so $\lambda \notin \sigma (A).$

**Theorem**—Symmetric operator with real spectrum is self-adjoint

Proof

1. A is symmetric; therefore $A\subseteq A^{*}$ and $A-\lambda I\subseteq A^{*}-\lambda I$ for every $\lambda \in \mathbb {C}$ . Let $\sigma (A)\subseteq [m,M].$ If $\lambda \notin [m,M]$ then ${\bar {\lambda }}\notin [m,M]$ and the operators $\{A-\lambda I,A-{\bar {\lambda }}I\}:\operatorname {Dom} A\to H$ are both bijective.
2. $A-\lambda I=A^{*}-\lambda I.$ Indeed, $H=\operatorname {Im} (A-\lambda I)\subseteq \operatorname {Im} (A^{*}-\lambda I)$ . That is, if $\operatorname {Dom} (A-\lambda I)\subsetneq \operatorname {Dom} (A^{*}-\lambda I)$ then $A^{*}-\lambda I$ would not be injective (i.e. $\ker(A^{*}-\lambda I)\neq \{0\}$ ). But $\operatorname {Im} (A-{\bar {\lambda }}I)^{\perp }=\ker(A^{*}-\lambda I)$ and, hence, $\operatorname {Im} (A-{\bar {\lambda }}I)\neq H.$ This contradicts the bijectiveness.
3. The equality $A-\lambda I=A^{*}-\lambda I$ shows that $A=A^{*},$ i.e. A is self-adjoint. Indeed, it suffices to prove that $A^{*}\subseteq A.$ For every $x\in \operatorname {Dom} A^{*}$ and $y=A^{*}x,$ $A^{*}x=y\Leftrightarrow (A^{*}-\lambda I)x=y-\lambda x\Leftrightarrow (A-\lambda I)x=y-\lambda x\Leftrightarrow Ax=y.$

## Spectral theorem

In the physics literature, the spectral theorem is often stated by saying that a self-adjoint operator has an orthonormal basis of eigenvectors. Physicists are well aware, however, of the phenomenon of "continuous spectrum"; thus, when they speak of an "orthonormal basis" they mean either an orthonormal basis in the classic sense *or* some continuous analog thereof. In the case of the momentum operator ${\textstyle P=-i{\frac {d}{dx}}}$ , for example, physicists would say that the eigenvectors are the functions $f_{p}(x):=e^{ipx}$ , which are clearly not in the Hilbert space $L^{2}(\mathbb {R} )$ . (Physicists would say that the eigenvectors are "non-normalizable.") Physicists would then go on to say that these "generalized eigenvectors" form an "orthonormal basis in the continuous sense" for $L^{2}(\mathbb {R} )$ , after replacing the usual Kronecker delta $\delta _{i,j}$ by a Dirac delta function $\delta \left(p-p'\right)$ .

Although these statements may seem disconcerting to mathematicians, they can be made rigorous by use of the Fourier transform, which allows a general $L^{2}$ function to be expressed as a "superposition" (i.e., integral) of the functions $e^{ipx}$ , even though these functions are not in $L^{2}$ . The Fourier transform "diagonalizes" the momentum operator; that is, it converts it into the operator of multiplication by p , where p is the variable of the Fourier transform.

The spectral theorem in general can be expressed similarly as the possibility of "diagonalizing" an operator by showing it is unitarily equivalent to a multiplication operator. Other versions of the spectral theorem are similarly intended to capture the idea that a self-adjoint operator can have "eigenvectors" that are not actually in the Hilbert space in question.

### Multiplication operator form of the spectral theorem

Firstly, let $(X,\Sigma ,\mu )$ be a σ-finite measure space and $h:X\to \mathbb {R}$ a measurable function on X . Then the operator $T_{h}:\operatorname {Dom} T_{h}\to L^{2}(X,\mu )$ , defined by

$T_{h}\psi (x)=h(x)\psi (x),\quad \forall \psi \in \operatorname {Dom} T_{h},$

where

$\operatorname {Dom} T_{h}:=\left\{\psi \in L^{2}(X,\mu )\;|\;h\psi \in L^{2}(X,\mu )\right\},$

is called a **multiplication operator**. Any multiplication operator is a self-adjoint operator.

Secondly, two operators A and B with dense domains $\operatorname {Dom} A\subseteq H_{1}$ and $\operatorname {Dom} B\subseteq H_{2}$ in Hilbert spaces $H_{1}$ and $H_{2}$ , respectively, are **unitarily equivalent** if and only if there is a unitary transformation $U:H_{1}\to H_{2}$ such that:

- $U\operatorname {Dom} A=\operatorname {Dom} B,$
- $UAU^{-1}\xi =B\xi ,\quad \forall \xi \in \operatorname {Dom} B.$

If unitarily equivalent A and B are bounded, then $\|A\|_{H_{1}}=\|B\|_{H_{2}}$ ; if A is self-adjoint, then so is B .

**Theorem**—Any self-adjoint operator A on a separable Hilbert space is unitarily equivalent to a multiplication operator, i.e.,

$UAU^{-1}\psi (x)=h(x)\psi (x),\quad \forall \psi \in U\operatorname {Dom} (A)$

The spectral theorem holds for both bounded and unbounded self-adjoint operators. Proof of the latter follows by reduction to the spectral theorem for unitary operators. We might note that if T is multiplication by h , then the spectrum of T is just the essential range of h .

More complete versions of the spectral theorem exist as well that involve direct integrals and carry with it the notion of "generalized eigenvectors".

### Functional calculus

One application of the spectral theorem is to define a functional calculus. That is, if f is a function on the real line and T is a self-adjoint operator, we wish to define the operator $f(T)$ . The spectral theorem shows that if T is represented as the operator of multiplication by h , then $f(T)$ is the operator of multiplication by the composition $f\circ h$ .

One example from quantum mechanics is the case where T is the Hamiltonian operator ${\hat {H}}$ . If ${\hat {H}}$ has a true orthonormal basis of eigenvectors $e_{j}$ with eigenvalues $\lambda _{j}$ , then $f({\hat {H}}):=e^{-it{\hat {H}}/\hbar }$ can be defined as the unique bounded operator with eigenvalues $f(\lambda _{j}):=e^{-it\lambda _{j}/\hbar }$ such that:

$f({\hat {H}})e_{j}=f(\lambda _{j})e_{j}.$

The goal of functional calculus is to extend this idea to the case where T has continuous spectrum (i.e. where T has no normalizable eigenvectors).

It has been customary to introduce the following notation

$\operatorname {E} (\lambda )=\mathbf {1} _{(-\infty ,\lambda ]}(T)$

where $\mathbf {1} _{(-\infty ,\lambda ]}$ is the indicator function of the interval $(-\infty ,\lambda ]$ . The family of projection operators E(λ) is called **resolution of the identity** for *T*. Moreover, the following Stieltjes integral representation for *T* can be proved:

$T=\int _{-\infty }^{+\infty }\lambda d\operatorname {E} (\lambda ).$

### Formulation in the physics literature

In quantum mechanics, Dirac notation is used as combined expression for both the spectral theorem and the Borel functional calculus. That is, if *H* is self-adjoint and *f* is a Borel function,

$f(H)=\int dE\left|\Psi _{E}\rangle f(E)\langle \Psi _{E}\right|$

with

$H\left|\Psi _{E}\right\rangle =E\left|\Psi _{E}\right\rangle$

where the integral runs over the whole spectrum of *H*. The notation suggests that *H* is diagonalized by the eigenvectors Ψ*E*. Such a notation is purely formal. The resolution of the identity (sometimes called projection-valued measures) formally resembles the rank-1 projections $\left|\Psi _{E}\right\rangle \left\langle \Psi _{E}\right|$ . In the Dirac notation, (projective) measurements are described via eigenvalues and eigenstates, both purely formal objects. As one would expect, this does not survive passage to the resolution of the identity. In the latter formulation, measurements are described using the spectral measure of $|\Psi \rangle$ , if the system is prepared in $|\Psi \rangle$ prior to the measurement. Alternatively, if one would like to preserve the notion of eigenstates and make it rigorous, rather than merely formal, one can replace the state space by a suitable rigged Hilbert space.

If *f* = 1, the theorem is referred to as resolution of unity:

$I=\int dE\left|\Psi _{E}\right\rangle \left\langle \Psi _{E}\right|$

In the case $H_{\text{eff}}=H-i\Gamma$ is the sum of an Hermitian *H* and a skew-Hermitian (see skew-Hermitian matrix) operator $-i\Gamma$ , one defines the biorthogonal basis set

$H_{\text{eff}}^{*}\left|\Psi _{E}^{*}\right\rangle =E^{*}\left|\Psi _{E}^{*}\right\rangle$

and write the spectral theorem as:

$f\left(H_{\text{eff}}\right)=\int dE\left|\Psi _{E}\right\rangle f(E)\left\langle \Psi _{E}^{*}\right|$

(See *Feshbach–Fano partitioning* for the context where such operators appear in scattering theory).

### Formulation for symmetric operators

The spectral theorem applies only to self-adjoint operators, and not in general to symmetric operators. Nevertheless, we can at this point give a simple example of a symmetric (specifically, an essentially self-adjoint) operator that has an orthonormal basis of eigenvectors. Consider the complex Hilbert space *L*2[0,1] and the differential operator

$A=-{\frac {d^{2}}{dx^{2}}}$

with $\mathrm {Dom} (A)$ consisting of all complex-valued infinitely differentiable functions *f* on [0, 1] satisfying the boundary conditions

$f(0)=f(1)=0.$

Then integration by parts of the inner product shows that *A* is symmetric. The eigenfunctions of *A* are the sinusoids

$f_{n}(x)=\sin(n\pi x)\qquad n=1,2,\ldots$

with the real eigenvalues *n*2π2; the well-known orthogonality of the sine functions follows as a consequence of *A* being symmetric.

The operator *A* can be seen to have a compact inverse, meaning that the corresponding differential equation *Af* = *g* is solved by some integral (and therefore compact) operator *G*. The compact symmetric operator *G* then has a countable family of eigenvectors which are complete in *L*2. The same can then be said for *A*.

### Pure point spectrum

A self-adjoint operator *A* on *H* has pure point spectrum if and only if *H* has an orthonormal basis {*ei*}*i* ∈ I consisting of eigenvectors for *A*.

**Example**. The Hamiltonian for the harmonic oscillator has a quadratic potential *V*, that is

$-\Delta +|x|^{2}.$

This Hamiltonian has pure point spectrum; this is typical for bound state Hamiltonians in quantum mechanics. As was pointed out in a previous example, a sufficient condition that an unbounded symmetric operator has eigenvectors which form a Hilbert space basis is that it has a compact inverse.

## Symmetric vs self-adjoint operators

Although the distinction between a symmetric operator and a (essentially) self-adjoint operator is subtle, it is important since self-adjointness is the hypothesis in the spectral theorem. Here we discuss some concrete examples of the distinction.

### Boundary conditions

In the case where the Hilbert space is a space of functions on a bounded domain, these distinctions have to do with a familiar issue in quantum physics: One cannot define an operator—such as the momentum or Hamiltonian operator—on a bounded domain without specifying *boundary conditions*. In mathematical terms, choosing the boundary conditions amounts to choosing an appropriate domain for the operator. Consider, for example, the Hilbert space $L^{2}([0,1])$ (the space of square-integrable functions on the interval [0,1]). Let us define a momentum operator *A* on this space by the usual formula, setting the Planck constant to 1:

$Af=-i{\frac {df}{dx}}.$

We must now specify a domain for *A*, which amounts to choosing boundary conditions. If we choose

$\operatorname {Dom} (A)=\left\{{\text{smooth functions}}\right\},$

then *A* is not symmetric (because the boundary terms in the integration by parts do not vanish).

If we choose

$\operatorname {Dom} (A)=\left\{{\text{smooth functions}}\,f\mid f(0)=f(1)=0\right\},$

then using integration by parts, one can easily verify that *A* is symmetric. This operator is not essentially self-adjoint, however, basically because we have specified too many boundary conditions on the domain of *A*, which makes the domain of the adjoint too big (see also the example below).

Specifically, with the above choice of domain for *A*, the domain of the closure $A^{\mathrm {cl} }$ of *A* is

$\operatorname {Dom} \left(A^{\mathrm {cl} }\right)=\left\{{\text{functions }}f{\text{ with two derivatives in }}L^{2}\mid f(0)=f(1)=0\right\},$

whereas the domain of the adjoint $A^{*}$ of *A* is

$\operatorname {Dom} \left(A^{*}\right)=\left\{{\text{functions }}f{\text{ with two derivatives in }}L^{2}\right\}.$

That is to say, the domain of the closure has the same boundary conditions as the domain of *A* itself, just a less stringent smoothness assumption. Meanwhile, since there are "too many" boundary conditions on *A*, there are "too few" (actually, none at all in this case) for $A^{*}$ . If we compute $\langle g,Af\rangle$ for $f\in \operatorname {Dom} (A)$ using integration by parts, then since f vanishes at both ends of the interval, no boundary conditions on g are needed to cancel out the boundary terms in the integration by parts. Thus, any sufficiently smooth function g is in the domain of $A^{*}$ , with $A^{*}g=-i\,dg/dx$ .

Since the domain of the closure and the domain of the adjoint do not agree, *A* is not essentially self-adjoint. After all, a general result says that the domain of the adjoint of $A^{\mathrm {cl} }$ is the same as the domain of the adjoint of *A*. Thus, in this case, the domain of the adjoint of $A^{\mathrm {cl} }$ is bigger than the domain of $A^{\mathrm {cl} }$ itself, showing that $A^{\mathrm {cl} }$ is not self-adjoint, which by definition means that *A* is not essentially self-adjoint.

The problem with the preceding example is that we imposed too many boundary conditions on the domain of *A*. A better choice of domain would be to use periodic boundary conditions:

$\operatorname {Dom} (A)=\{{\text{smooth functions}}\,f\mid f(0)=f(1)\}.$

With this domain, *A* is essentially self-adjoint.

In this case, we can understand the implications of the domain issues for the spectral theorem. If we use the first choice of domain (with no boundary conditions), all functions $f_{\beta }(x)=e^{\beta x}$ for $\beta \in \mathbb {C}$ are eigenvectors, with eigenvalues $-i\beta$ , and so the spectrum is the whole complex plane. If we use the second choice of domain (with Dirichlet boundary conditions), *A* has no eigenvectors at all. If we use the third choice of domain (with periodic boundary conditions), we can find an orthonormal basis of eigenvectors for *A*, the functions $f_{n}(x):=e^{2\pi inx}$ . Thus, in this case finding a domain such that *A* is self-adjoint is a compromise: the domain has to be small enough so that *A* is symmetric, but large enough so that $D(A^{*})=D(A)$ .

### Schrödinger operators with singular potentials

A more subtle example of the distinction between symmetric and (essentially) self-adjoint operators comes from Schrödinger operators in quantum mechanics. If the potential energy is singular—particularly if the potential is unbounded below—the associated Schrödinger operator may fail to be essentially self-adjoint. In one dimension, for example, the operator

${\hat {H}}:={\frac {P^{2}}{2m}}-X^{4}$

is not essentially self-adjoint on the space of smooth, rapidly decaying functions. In this case, the failure of essential self-adjointness reflects a pathology in the underlying classical system: A classical particle with a $-x^{4}$ potential escapes to infinity in finite time. This operator does not have a *unique* self-adjoint, but it does admit self-adjoint extensions obtained by specifying "boundary conditions at infinity". (Since ${\hat {H}}$ is a real operator, it commutes with complex conjugation. Thus, the deficiency indices are automatically equal, which is the condition for having a self-adjoint extension.)

In this case, if we initially define ${\hat {H}}$ on the space of smooth, rapidly decaying functions, the adjoint will be "the same" operator (i.e., given by the same formula) but on the largest possible domain, namely

$\operatorname {Dom} \left({\hat {H}}^{*}\right)=\left\{{\text{twice differentiable functions }}f\in L^{2}(\mathbb {R} )\left|\left(-{\frac {\hbar ^{2}}{2m}}{\frac {d^{2}f}{dx^{2}}}-x^{4}f(x)\right)\in L^{2}(\mathbb {R} )\right.\right\}.$

It is then possible to show that ${\hat {H}}^{*}$ is not a symmetric operator, which certainly implies that ${\hat {H}}$ is not essentially self-adjoint. Indeed, ${\hat {H}}^{*}$ has eigenvectors with pure imaginary eigenvalues, which is impossible for a symmetric operator. This strange occurrence is possible because of a cancellation between the two terms in ${\hat {H}}^{*}$ : There are functions f in the domain of ${\hat {H}}^{*}$ for which neither $d^{2}f/dx^{2}$ nor $x^{4}f(x)$ is separately in $L^{2}(\mathbb {R} )$ , but the combination of them occurring in ${\hat {H}}^{*}$ is in $L^{2}(\mathbb {R} )$ . This allows for ${\hat {H}}^{*}$ to be nonsymmetric, even though both $d^{2}/dx^{2}$ and $X^{4}$ are symmetric operators. This sort of cancellation does not occur if we replace the repelling potential $-x^{4}$ with the confining potential $x^{4}$ .

### Non-self-adjoint operators in quantum mechanics

In quantum mechanics, observables correspond to self-adjoint operators. By Stone's theorem on one-parameter unitary groups, self-adjoint operators are precisely the infinitesimal generators of unitary groups of time evolution operators. However, many physical problems are formulated as a time-evolution equation involving differential operators for which the Hamiltonian is only symmetric. In such cases, either the Hamiltonian is essentially self-adjoint, in which case the physical problem has unique solutions or one attempts to find self-adjoint extensions of the Hamiltonian corresponding to different types of boundary conditions or conditions at infinity.

**Example.** The one-dimensional Schrödinger operator with the potential $V(x)=-(1+|x|)^{\alpha }$ , defined initially on smooth compactly supported functions, is essentially self-adjoint for 0 < *α* ≤ 2 but not for *α* > 2.

The failure of essential self-adjointness for $\alpha >2$ has a counterpart in the classical dynamics of a particle with potential $V(x)$ : The classical particle escapes to infinity in finite time.

**Example.** There is no self-adjoint momentum operator p for a particle moving on a half-line. Nevertheless, the Hamiltonian $p^{2}$ of a "free" particle on a half-line has several self-adjoint extensions corresponding to different types of boundary conditions. Physically, these boundary conditions are related to reflections of the particle at the origin.

## Examples

### A symmetric operator that is not essentially self-adjoint

We first consider the Hilbert space $L^{2}[0,1]$ and the differential operator

$D:\phi \mapsto {\frac {1}{i}}\phi '$

defined on the space of continuously differentiable complex-valued functions on [0,1], satisfying the boundary conditions

$\phi (0)=\phi (1)=0.$

Then *D* is a symmetric operator as can be shown by integration by parts. The spaces *N*+, *N*− (defined below) are given respectively by the distributional solutions to the equation

${\begin{aligned}-iu'&=iu\\-iu'&=-iu\end{aligned}}$

which are in *L*2[0, 1]. One can show that each one of these solution spaces is 1-dimensional, generated by the functions *x* → *e**−x* and *x* → *e**x* respectively. This shows that *D* is not essentially self-adjoint, but does have self-adjoint extensions. These self-adjoint extensions are parametrized by the space of unitary mappings *N*+ → *N*−, which in this case happens to be the unit circle **T**.

In this case, the failure of essential self-adjointenss is due to an "incorrect" choice of boundary conditions in the definition of the domain of D . Since D is a first-order operator, only one boundary condition is needed to ensure that D is symmetric. If we replaced the boundary conditions given above by the single boundary condition

$\phi (0)=\phi (1)$

,

then *D* would still be symmetric and would now, in fact, be essentially self-adjoint. This change of boundary conditions gives one particular essentially self-adjoint extension of *D*. Other essentially self-adjoint extensions come from imposing boundary conditions of the form $\phi (1)=e^{i\theta }\phi (0)$ .

This simple example illustrates a general fact about self-adjoint extensions of symmetric differential operators *P* on an open set *M*. They are determined by the unitary maps between the eigenvalue spaces

$N_{\pm }=\left\{u\in L^{2}(M):P_{\operatorname {dist} }u=\pm iu\right\}$

where *P*dist is the distributional extension of *P*.

### Constant-coefficient operators

We next give the example of differential operators with constant coefficients. Let

$P\left({\vec {x}}\right)=\sum _{\alpha }c_{\alpha }x^{\alpha }$

be a polynomial on **R***n* with *real* coefficients, where α ranges over a (finite) set of multi-indices. Thus

$\alpha =(\alpha _{1},\alpha _{2},\ldots ,\alpha _{n})$

and

$x^{\alpha }=x_{1}^{\alpha _{1}}x_{2}^{\alpha _{2}}\cdots x_{n}^{\alpha _{n}}.$

We also use the notation

$D^{\alpha }={\frac {1}{i^{|\alpha |}}}\partial _{x_{1}}^{\alpha _{1}}\partial _{x_{2}}^{\alpha _{2}}\cdots \partial _{x_{n}}^{\alpha _{n}}.$

Then the operator *P*(D) defined on the space of infinitely differentiable functions of compact support on **R***n* by

$P(\operatorname {D} )\phi =\sum _{\alpha }c_{\alpha }\operatorname {D} ^{\alpha }\phi$

is essentially self-adjoint on *L*2(**R***n*).

**Theorem**—Let *P* a polynomial function on **R***n* with real coefficients, **F** the Fourier transform considered as a unitary map *L*2(**R***n*) → *L*2(**R***n*). Then **F****P*(D)**F** is essentially self-adjoint and its unique self-adjoint extension is the operator of multiplication by the function *P*.

More generally, consider linear differential operators acting on infinitely differentiable complex-valued functions of compact support. If *M* is an open subset of **R***n*

$P\phi (x)=\sum _{\alpha }a_{\alpha }(x)\left[D^{\alpha }\phi \right](x)$

where *a*α are (not necessarily constant) infinitely differentiable functions. *P* is a linear operator

$C_{0}^{\infty }(M)\to C_{0}^{\infty }(M).$

Corresponding to *P* there is another differential operator, the **formal adjoint** of *P*

$P^{\mathrm {*form} }\phi =\sum _{\alpha }D^{\alpha }\left({\overline {a_{\alpha }}}\phi \right)$

**Theorem**—The adjoint *P** of *P* is a restriction of the distributional extension of the formal adjoint to an appropriate subspace of $L^{2}$ . Specifically: $\operatorname {dom} P^{*}=\left\{u\in L^{2}(M):P^{\mathrm {*form} }u\in L^{2}(M)\right\}.$

## Spectral multiplicity theory

The multiplication representation of a self-adjoint operator, though extremely useful, is not a canonical representation. This suggests that it is not easy to extract from this representation a criterion to determine when self-adjoint operators *A* and *B* are unitarily equivalent. The finest grained representation which we now discuss involves spectral multiplicity. This circle of results is called the *Hahn–Hellinger theory of spectral multiplicity*.

### Uniform multiplicity

We first define *uniform multiplicity*:

**Definition**. A self-adjoint operator *A* has uniform multiplicity *n* where *n* is such that 1 ≤ *n* ≤ *ω* if and only if *A* is unitarily equivalent to the operator M*f* of multiplication by the function *f*(*λ*) = *λ* on

$L_{\mu }^{2}\left(\mathbf {R} ,\mathbf {H} _{n}\right)=\left\{\psi :\mathbf {R} \to \mathbf {H} _{n}:\psi {\text{ measurable and }}\int _{\mathbf {R} }\|\psi (t)\|^{2}d\mu (t)<\infty \right\}$

where **H***n* is a Hilbert space of dimension *n*. The domain of M*f* consists of vector-valued functions *ψ* on **R** such that

$\int _{\mathbf {R} }|\lambda |^{2}\ \|\psi (\lambda )\|^{2}\,d\mu (\lambda )<\infty .$

Non-negative countably additive measures *μ*, *ν* are **mutually singular** if and only if they are supported on disjoint Borel sets.

**Theorem**—Let *A* be a self-adjoint operator on a *separable* Hilbert space *H*. Then there is an *ω* sequence of countably additive finite measures on **R** (some of which may be identically 0) $\left\{\mu _{\ell }\right\}_{1\leq \ell \leq \omega }$ such that the measures are pairwise singular and *A* is unitarily equivalent to the operator of multiplication by the function *f*(*λ*) = *λ* on $\bigoplus _{1\leq \ell \leq \omega }L_{\mu _{\ell }}^{2}\left(\mathbf {R} ,\mathbf {H} _{\ell }\right).$

This representation is unique in the following sense: For any two such representations of the same *A*, the corresponding measures are equivalent in the sense that they have the same sets of measure 0.

### Direct integrals

The spectral multiplicity theorem can be reformulated using the language of direct integrals of Hilbert spaces:

**Theorem**— Any self-adjoint operator on a separable Hilbert space is unitarily equivalent to multiplication by the function λ ↦ λ on $\int _{\mathbf {R} }^{\oplus }H_{\lambda }\,d\mu (\lambda ).$

Unlike the multiplication-operator version of the spectral theorem, the direct-integral version is unique in the sense that the measure equivalence class of *μ* (or equivalently its sets of measure 0) is uniquely determined and the measurable function $\lambda \mapsto \mathrm {dim} (H_{\lambda })$ is determined almost everywhere with respect to *μ*. The function $\lambda \mapsto \operatorname {dim} \left(H_{\lambda }\right)$ is the **spectral multiplicity function** of the operator.

We may now state the classification result for self-adjoint operators: Two self-adjoint operators are unitarily equivalent if and only if (1) their spectra agree as sets, (2) the measures appearing in their direct-integral representations have the same sets of measure zero, and (3) their spectral multiplicity functions agree almost everywhere with respect to the measure in the direct integral.

### Example: structure of the Laplacian

The Laplacian on **R***n* is the operator

$\Delta =\sum _{i=1}^{n}\partial _{x_{i}}^{2}.$

As remarked above, the Laplacian is diagonalized by the Fourier transform. Actually it is more natural to consider the *negative* of the Laplacian −Δ since as an operator it is non-negative; (see elliptic operator).

**Theorem**—If *n* = 1, then −Δ has uniform multiplicity ${\text{mult}}=2$ , otherwise −Δ has uniform multiplicity ${\text{mult}}=\omega$ . Moreover, the measure *μ***mult** may be taken to be Lebesgue measure on [0, ∞).
