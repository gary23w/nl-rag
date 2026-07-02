---
title: "Spectral theory"
source: https://en.wikipedia.org/wiki/Spectral_theory
domain: spectral-theory
license: CC-BY-SA-4.0
tags: spectral theory, spectral theorem, self-adjoint operator, sturm-liouville theory
fetched: 2026-07-02
---

# Spectral theory

In mathematics, **spectral theory** is an inclusive term for theories extending the eigenvector and eigenvalue theory of a single square matrix to a much broader theory of the structure of operators in a variety of mathematical spaces. It is a result of studies of linear algebra and the solutions of systems of linear equations and their generalizations. The theory is connected to that of analytic functions because the spectral properties of an operator are related to analytic functions of the spectral parameter.

## Mathematical background

The name *spectral theory* was introduced by David Hilbert in his original formulation of Hilbert space theory, which was cast in terms of quadratic forms in infinitely many variables. The original spectral theorem was therefore conceived as a version of the theorem on principal axes of an ellipsoid, in an infinite-dimensional setting. The later discovery in quantum mechanics that spectral theory could explain features of atomic spectra was therefore fortuitous. Hilbert himself was surprised by the unexpected application of this theory, noting that "I developed my theory of infinitely many variables from purely mathematical interests, and even called it 'spectral analysis' without any presentiment that it would later find application to the actual spectrum of physics."

There have been three main ways to formulate spectral theory, each of which find use in different domains. After Hilbert's initial formulation, the later development of abstract Hilbert spaces and the spectral theory of single normal operators on them were well suited to the requirements of physics, exemplified by the work of von Neumann. The further theory built on this to address Banach algebras in general. This development leads to the Gelfand representation, which covers the commutative case, and further into non-commutative harmonic analysis.

The difference can be seen in making the connection with Fourier analysis. The Fourier transform on the real line is in one sense the spectral theory of differentiation as a differential operator. But for that to cover the phenomena one has already to deal with generalized eigenfunctions (for example, by means of a rigged Hilbert space). On the other hand, it is simple to construct a group algebra, the spectrum of which captures the Fourier transform's basic properties, and this is carried out by means of Pontryagin duality.

One can also study the spectral properties of operators on Banach spaces. For example, compact operators on Banach spaces have many spectral properties similar to that of matrices.

## Physical background

The background in the physics of vibrations has been explained in this way:

> Spectral theory is connected with the investigation of localized vibrations of a variety of different objects, from atoms and molecules in chemistry to obstacles in acoustic waveguides. These vibrations have frequencies, and the issue is to decide when such localized vibrations occur, and how to go about computing the frequencies. This is a very complicated problem since every object has not only a fundamental tone but also a complicated series of overtones, which vary radically from one body to another.

Such physical ideas have nothing to do with the mathematical theory on a technical level, but there are examples of indirect involvement (see for example Mark Kac's question *Can you hear the shape of a drum?*). Hilbert's adoption of the term "spectrum" has been attributed to an 1897 paper of Wilhelm Wirtinger on Hill differential equation (by Jean Dieudonné), and it was taken up by his students during the first decade of the twentieth century, among them Erhard Schmidt and Hermann Weyl. The conceptual basis for Hilbert space was developed from Hilbert's ideas by Erhard Schmidt and Frigyes Riesz. It was almost twenty years later, when quantum mechanics was formulated in terms of the Schrödinger equation, that the connection was made to atomic spectra; a connection with the mathematical physics of vibration had been suspected before, as remarked by Henri Poincaré, but rejected for simple quantitative reasons, absent an explanation of the Balmer series. The later discovery in quantum mechanics that spectral theory could explain features of atomic spectra was therefore fortuitous, rather than being an object of Hilbert's spectral theory.

## A definition of spectrum

Consider a bounded linear transformation *T* defined everywhere over a general Banach space. We form the transformation: $R_{\zeta }=\left(\zeta I-T\right)^{-1}.$

Here *I* is the identity operator and ζ is a complex number. The *inverse* of an operator *T*, that is *T*−1, is defined by: $TT^{-1}=T^{-1}T=I.$

If the inverse exists, *T* is called *regular*. If it does not exist, *T* is called *singular*.

With these definitions, the *resolvent set* of *T* is the set of all complex numbers ζ such that *Rζ* exists and is bounded. This set often is denoted as *ρ*(*T*). The *spectrum* of *T* is the set of all complex numbers ζ such that *Rζ* fails to exist or is unbounded. Often the spectrum of *T* is denoted by *σ*(*T*). The function *Rζ* for all ζ in *ρ*(*T*) (that is, wherever *Rζ* exists as a bounded operator) is called the resolvent of *T*. The *spectrum* of *T* is therefore the complement of the *resolvent set* of *T* in the complex plane. Every eigenvalue of *T* belongs to *σ*(*T*), but *σ*(*T*) may contain non-eigenvalues.

This definition applies to a Banach space, but of course other types of space exist as well; for example, topological vector spaces include Banach spaces, but can be more general. On the other hand, Banach spaces include Hilbert spaces, and it is these spaces that find the greatest application and the richest theoretical results. With suitable restrictions, much can be said about the structure of the spectra of transformations in a Hilbert space. In particular, for self-adjoint operators, the spectrum lies on the real line and (in general) is a spectral combination of a point spectrum of discrete eigenvalues and a continuous spectrum.

## Spectral theory briefly

In functional analysis and linear algebra the spectral theorem establishes conditions under which an operator can be expressed in simple form as a sum of simpler operators. As a full rigorous presentation is not appropriate for this article, we take an approach that avoids much of the rigor and satisfaction of a formal treatment with the aim of being more comprehensible to a non-specialist.

This topic is easiest to describe by introducing the bra–ket notation of Dirac for operators. As an example, a very particular linear operator *L* might be written as a dyadic product:

$L=|k_{1}\rangle \langle b_{1}|,$

in terms of the "bra" ⟨b1| and the "ket" |k1⟩. A function f is described by a *ket* as |f ⟩. The function *f*(*x*) defined on the coordinates $(x_{1},x_{2},x_{3},\dots )$ is denoted as

$f(x)=\langle x|f\rangle$

and the magnitude of *f* by

$\|f\|^{2}=\langle f|f\rangle =\int \langle f|x\rangle \langle x|f\rangle \,dx=\int f^{*}(x)f(x)\,dx$

where the notation (*) denotes a complex conjugate. This inner product choice defines a very specific inner product space, restricting the generality of the arguments that follow.

The effect of *L* upon a function *f* is then described as:

$L|f\rangle =|k_{1}\rangle \langle b_{1}|f\rangle$

expressing the result that the effect of *L* on *f* is to produce a new function $|k_{1}\rangle$ multiplied by the inner product represented by $\langle b_{1}|f\rangle$ .

A more general linear operator *L* might be expressed as:

$L=\lambda _{1}|e_{1}\rangle \langle f_{1}|+\lambda _{2}|e_{2}\rangle \langle f_{2}|+\lambda _{3}|e_{3}\rangle \langle f_{3}|+\dots ,$

where the $\{\,\lambda _{i}\,\}$ are scalars and the $\{\,|e_{i}\rangle \,\}$ are a basis and the $\{\,\langle f_{i}|\,\}$ a reciprocal basis for the space. The relation between the basis and the reciprocal basis is described, in part, by:

$\langle f_{i}|e_{j}\rangle =\delta _{ij}$

If such a formalism applies, the $\{\,\lambda _{i}\,\}$ are eigenvalues of *L* and the functions $\{\,|e_{i}\rangle \,\}$ are eigenfunctions of *L*. The eigenvalues are in the *spectrum* of *L*.

Some natural questions are: under what circumstances does this formalism work, and for what operators *L* are expansions in series of other operators like this possible? Can any function *f* be expressed in terms of the eigenfunctions (are they a Schauder basis) and under what circumstances does a point spectrum or a continuous spectrum arise? How do the formalisms for infinite-dimensional spaces and finite-dimensional spaces differ, or do they differ? Can these ideas be extended to a broader class of spaces? Answering such questions is the realm of spectral theory and requires considerable background in functional analysis and matrix algebra.

## Resolution of the identity

This section continues in the rough and ready manner of the above section using the bra–ket notation, and glossing over the many important details of a rigorous treatment. A rigorous mathematical treatment may be found in various references. In particular, the dimension *n* of the space will be finite.

Using the bra–ket notation of the above section, the identity operator may be written as:

$I=\sum _{i=1}^{n}|e_{i}\rangle \langle f_{i}|$

where it is supposed as above that $\{|e_{i}\rangle \}$ are a basis and the $\{\langle f_{i}|\}$ a reciprocal basis for the space satisfying the relation:

$\langle f_{i}|e_{j}\rangle =\delta _{ij}.$

This expression of the identity operation is called a *representation* or a *resolution* of the identity. This formal representation satisfies the basic property of the identity:

$I^{k}=I$

valid for every positive integer *k*.

Applying the resolution of the identity to any function in the space $|\psi \rangle$ , one obtains:

$I|\psi \rangle =|\psi \rangle =\sum _{i=1}^{n}|e_{i}\rangle \langle f_{i}|\psi \rangle =\sum _{i=1}^{n}c_{i}|e_{i}\rangle$

which is the generalized Fourier expansion of ψ in terms of the basis functions { ei }. Here $c_{i}=\langle f_{i}|\psi \rangle$ .

Given some operator equation of the form:

$O|\psi \rangle =|h\rangle$

with *h* in the space, this equation can be solved in the above basis through the formal manipulations:

$O|\psi \rangle =\sum _{i=1}^{n}c_{i}\left(O|e_{i}\rangle \right)=\sum _{i=1}^{n}|e_{i}\rangle \langle f_{i}|h\rangle ,$

$\langle f_{j}|O|\psi \rangle =\sum _{i=1}^{n}c_{i}\langle f_{j}|O|e_{i}\rangle =\sum _{i=1}^{n}\langle f_{j}|e_{i}\rangle \langle f_{i}|h\rangle =\langle f_{j}|h\rangle ,\quad \forall j$

which converts the operator equation to a matrix equation determining the unknown coefficients *cj* in terms of the generalized Fourier coefficients $\langle f_{j}|h\rangle$ of *h* and the matrix elements $O_{ji}=\langle f_{j}|O|e_{i}\rangle$ of the operator *O*.

The role of spectral theory arises in establishing the nature and existence of the basis and the reciprocal basis. In particular, the basis might consist of the eigenfunctions of some linear operator *L*:

$L|e_{i}\rangle =\lambda _{i}|e_{i}\rangle \,;$

with the { *λi* } the eigenvalues of *L* from the spectrum of *L*. Then the resolution of the identity above provides the dyad expansion of *L*:

$LI=L=\sum _{i=1}^{n}L|e_{i}\rangle \langle f_{i}|=\sum _{i=1}^{n}\lambda _{i}|e_{i}\rangle \langle f_{i}|.$

## Resolvent operator

Using spectral theory, the resolvent operator *R*:

$R=(\lambda I-L)^{-1},\,$

can be evaluated in terms of the eigenfunctions and eigenvalues of *L*, and the Green's function corresponding to *L* can be found.

Applying *R* to some arbitrary function in the space, say $\varphi$ ,

$R|\varphi \rangle =(\lambda I-L)^{-1}|\varphi \rangle =\sum _{i=1}^{n}{\frac {1}{\lambda -\lambda _{i}}}|e_{i}\rangle \langle f_{i}|\varphi \rangle .$

This function has poles in the complex *λ*-plane at each eigenvalue of *L*. Thus, using the calculus of residues:

${\frac {1}{2\pi i}}\oint _{C}R|\varphi \rangle d\lambda =-\sum _{i=1}^{n}|e_{i}\rangle \langle f_{i}|\varphi \rangle =-|\varphi \rangle ,$

where the line integral is over a contour *C* that includes all the eigenvalues of *L*.

Suppose our functions are defined over some coordinates {*xj*}, that is:

$\langle x|\varphi \rangle =\varphi (x_{1},x_{2},...).$

Introducing the notation

$\langle x,y\rangle =\delta (x-y),$

where *δ(x − y)* = *δ(x1 − y1, x2 − y2, x3 − y3, ...)* is the Dirac delta function, we can write

$\langle x,\varphi \rangle =\int \langle x,y\rangle \langle y,\varphi \rangle dy.$

Then:

${\begin{aligned}\left\langle x,{\frac {1}{2\pi i}}\oint _{C}{\frac {\varphi }{\lambda I-L}}d\lambda \right\rangle &={\frac {1}{2\pi i}}\oint _{C}d\lambda \left\langle x,{\frac {\varphi }{\lambda I-L}}\right\rangle \\&={\frac {1}{2\pi i}}\oint _{C}d\lambda \int dy\left\langle x,{\frac {y}{\lambda I-L}}\right\rangle \langle y,\varphi \rangle \end{aligned}}$

The function *G(x, y; λ)* defined by:

${\begin{aligned}G(x,y;\lambda )&=\left\langle x,{\frac {y}{\lambda I-L}}\right\rangle \\&=\sum _{i=1}^{n}\sum _{j=1}^{n}\langle x,e_{i}\rangle \left\langle f_{i},{\frac {e_{j}}{\lambda I-L}}\right\rangle \langle f_{j},y\rangle \\&=\sum _{i=1}^{n}{\frac {\langle x,e_{i}\rangle \langle f_{i},y\rangle }{\lambda -\lambda _{i}}}\\&=\sum _{i=1}^{n}{\frac {e_{i}(x)f_{i}^{*}(y)}{\lambda -\lambda _{i}}},\end{aligned}}$

is called the *Green's function* for operator *L*, and satisfies:

${\frac {1}{2\pi i}}\oint _{C}G(x,y;\lambda )\,d\lambda =-\sum _{i=1}^{n}\langle x,e_{i}\rangle \langle f_{i},y\rangle =-\langle x,y\rangle =-\delta (x-y).$

## Operator equations

Consider the operator equation:

$(O-\lambda I)|\psi \rangle =|h\rangle ;$

in terms of coordinates:

$\int \langle x,(O-\lambda I)y\rangle \langle y,\psi \rangle \,dy=h(x).$

A particular case is *λ* = 0.

The Green's function of the previous section is:

$\langle y,G(\lambda )z\rangle =\left\langle y,(O-\lambda I)^{-1}z\right\rangle =G(y,z;\lambda ),$

and satisfies:

$\int \langle x,(O-\lambda I)y\rangle \langle y,G(\lambda )z\rangle \,dy=\int \langle x,(O-\lambda I)y\rangle \left\langle y,(O-\lambda I)^{-1}z\right\rangle \,dy=\langle x,z\rangle =\delta (x-z).$

Using this Green's function property:

$\int \langle x,(O-\lambda I)y\rangle G(y,z;\lambda )\,dy=\delta (x-z).$

Then, multiplying both sides of this equation by *h*(*z*) and integrating:

$\int dz\,h(z)\int dy\,\langle x,(O-\lambda I)y\rangle G(y,z;\lambda )=\int dy\,\langle x,(O-\lambda I)y\rangle \int dz\,h(z)G(y,z;\lambda )=h(x),$

which suggests the solution is:

$\psi (x)=\int h(z)G(x,z;\lambda )\,dz.$

That is, the function *ψ*(*x*) satisfying the operator equation is found if we can find the spectrum of *O*, and construct *G*, for example by using:

$G(x,z;\lambda )=\sum _{i=1}^{n}{\frac {e_{i}(x)f_{i}^{*}(z)}{\lambda -\lambda _{i}}}.$

There are many other ways to find *G*, of course. See the articles on Green's functions and on Fredholm integral equations. It must be kept in mind that the above mathematics is purely formal, and a rigorous treatment involves some pretty sophisticated mathematics, including a good background knowledge of functional analysis, Hilbert spaces, distributions and so forth. Consult these articles and the references for more detail.

## Spectral theorem and Rayleigh quotient

Optimization problems may be the most useful examples about the combinatorial significance of the eigenvalues and eigenvectors in symmetric matrices, especially for the Rayleigh quotient with respect to a matrix **M**.

**Theorem** *Let **M** be a symmetric matrix and let **x** be the non-zero vector that maximizes the Rayleigh quotient with respect to **M**. Then, **x** is an eigenvector of **M** with eigenvalue equal to the Rayleigh quotient. Moreover, this eigenvalue is the largest eigenvalue of **M**.*

**Proof** Assume the spectral theorem. Let the eigenvalues of **M** be $\lambda _{1}\leq \lambda _{2}\leq \cdots \leq \lambda _{n}$ . Since the $\{v_{i}\}$ form an orthonormal basis, any vector x can be expressed in this basis as

$x=\sum _{i}v_{i}^{T}xv_{i}$

The way to prove this formula is pretty easy. Namely,

${\begin{aligned}v_{j}^{T}\sum _{i}v_{i}^{T}xv_{i}={}&\sum _{i}v_{i}^{T}xv_{j}^{T}v_{i}\\[4pt]={}&(v_{j}^{T}x)v_{j}^{T}v_{j}\\[4pt]={}&v_{j}^{T}x\end{aligned}}$

evaluate the Rayleigh quotient with respect to *x*:

${\begin{aligned}x^{T}Mx={}&\left(\sum _{i}(v_{i}^{T}x)v_{i}\right)^{T}M\left(\sum _{j}(v_{j}^{T}x)v_{j}\right)\\[4pt]={}&\left(\sum _{i}(v_{i}^{T}x)v_{i}^{T}\right)\left(\sum _{j}(v_{j}^{T}x)v_{j}\lambda _{j}\right)\\[4pt]={}&\sum _{i,j}(v_{i}^{T}x)v_{i}^{T}(v_{j}^{T}x)v_{j}\lambda _{j}\\[4pt]={}&\sum _{j}(v_{j}^{T}x)(v_{j}^{T}x)\lambda _{j}\\[4pt]={}&\sum _{j}(v_{j}^{T}x)^{2}\lambda _{j}\leq \lambda _{n}\sum _{j}(v_{j}^{T}x)^{2}\\[4pt]={}&\lambda _{n}x^{T}x,\end{aligned}}$

where we used Parseval's identity in the last line. Finally we obtain that

${\frac {x^{T}Mx}{x^{T}x}}\leq \lambda _{n}$

so the Rayleigh quotient is always less than $\lambda _{n}$ .
