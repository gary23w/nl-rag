---
title: "Hilbert space (part 1/2)"
source: https://en.wikipedia.org/wiki/Hilbert_space
domain: operator-algebras
license: CC-BY-SA-4.0
tags: operator algebra, von neumann algebra, banach algebra, gelfand representation
fetched: 2026-07-02
part: 1/2
---

# Hilbert space

The mathematical concept of a **Hilbert space** generalizes the notion of Euclidean space. It extends the methods of Euclidean geometry and calculus from the two-dimensional Euclidean plane and three-dimensional space to spaces of any finite or infinite dimension. A Hilbert space is an abstract vector space, and it has the additional structure of an inner product that allows length and angle to be measured. Finally, Hilbert spaces are required to be complete, a property that stipulates the existence of enough limits in the space to allow the techniques of calculus to be used.

Hilbert spaces were studied beginning in the first decade of the 20th century by David Hilbert (after whom they are named), Erhard Schmidt, and Frigyes Riesz. They are indispensable tools in the theories of partial differential equations, quantum mechanics, Fourier analysis (which includes applications to signal processing and heat transfer), and ergodic theory (which forms the mathematical underpinning of thermodynamics). John von Neumann coined the term *Hilbert space* for the abstract concept that underlies many of these diverse applications. The success of Hilbert space methods ushered in a very fruitful era for functional analysis. Apart from the classical Euclidean vector spaces, examples of Hilbert spaces include spaces of square-integrable functions, spaces of sequences, Sobolev spaces consisting of generalized functions, and Hardy spaces of holomorphic functions.

Geometric intuition plays an important role in many aspects of Hilbert space theory. Exact analogs of the Pythagorean theorem and parallelogram law hold in a Hilbert space. At a deeper level, perpendicular projection onto a linear subspace plays a significant role in optimization problems and other aspects of the theory. An element of a Hilbert space can be uniquely specified by its coordinates with respect to an orthonormal basis, in analogy with Cartesian coordinates in classical geometry. When this basis is countably infinite, it allows identifying the Hilbert space with the space of the infinite sequences that are square-summable. The latter space is often in the older literature referred to as *the* Hilbert space.


## Definition and illustration

### Motivating example: Euclidean vector space

One of the most familiar examples of a Hilbert space is the Euclidean vector space consisting of three-dimensional vectors, denoted by $\mathbf {R} ^{3}$ , and equipped with the dot product. The dot product takes two vectors **x** and **y**, and produces a real number **x** ⋅ **y**. If **x** and **y** are represented in Cartesian coordinates, then the dot product is defined by: ${\begin{pmatrix}x_{1}\\x_{2}\\x_{3}\end{pmatrix}}\cdot {\begin{pmatrix}y_{1}\\y_{2}\\y_{3}\end{pmatrix}}=x_{1}y_{1}+x_{2}y_{2}+x_{3}y_{3}\,.$

The dot product satisfies the properties:

1. It is symmetric in **x** and **y**: **x** ⋅ **y** = **y** ⋅ **x**.
2. It is linear in its first argument: (*a***x**1 + *b***x**2) ⋅ **y** = *a*(**x**1 ⋅ **y**) + *b*(**x**2 ⋅ **y**) for any scalars a, b, and vectors **x**1, **x**2, and **y**.
3. It is positive definite: for all vectors **x**, **x** ⋅ **x** ≥ 0 , with equality if and only if **x** = **0**.

An operation on pairs of vectors that, like the dot product, satisfies these three properties is known as a (real) inner product. A vector space equipped with such an inner product is known as a (real) inner product space. Every finite-dimensional inner product space is also a Hilbert space. The basic feature of the dot product that connects it with Euclidean geometry is that it is related to both the length (or norm) of a vector, denoted ‖**x**‖, and to the angle θ between two vectors **x** and **y** by means of the formula $\mathbf {x} \cdot \mathbf {y} =\left\|\mathbf {x} \right\|\left\|\mathbf {y} \right\|\,\cos \theta \,.$

Multivariable calculus in Euclidean space relies on the ability to compute limits, and to have useful criteria for concluding that limits exist. A mathematical series $\sum _{n=0}^{\infty }\mathbf {x} _{n}$ consisting of vectors in **R**3 is absolutely convergent provided that the sum of the lengths converges as an ordinary series of real numbers: $\sum _{k=0}^{\infty }\|\mathbf {x} _{k}\|<\infty \,.$ Just as with a series of scalars, a series of vectors that converges absolutely also converges to some limit vector **L** in the Euclidean space, in the sense that $\lim _{N\to \infty }{\Biggl \|}\mathbf {L} -\sum _{k=0}^{N}\mathbf {x} _{k}{\Biggr \|}=0.$ This property expresses the *completeness* of Euclidean space: that a series that converges absolutely also converges in the ordinary sense.

Hilbert spaces are often taken over the complex numbers. The complex plane denoted by **C** is equipped with a notion of magnitude, the complex modulus |*z*|, which is defined as the square root of the product of z with its complex conjugate: $|z|^{2}=z{\overline {z}}\,.$

If *z* = *x* + *iy* is a decomposition of z into its real and imaginary parts, then the modulus is the usual Euclidean two-dimensional length: $|z|={\sqrt {x^{2}+y^{2}}}\,.$

The inner product of a pair of complex numbers z and w is the product of z with the complex conjugate of w: $\langle z,w\rangle =z{\overline {w}}\,.$

This is complex-valued. The real part of ⟨*z*, *w*⟩ gives the usual two-dimensional Euclidean dot product.

A second example is the space **C**2 whose elements are pairs of complex numbers *z* = (*z*1, *z*2). Then an inner product of z with another such vector *w* = (*w*1, *w*2) is given by $\langle z,w\rangle =z_{1}{\overline {w}}_{1}+z_{2}{\overline {w}}_{2}\,.$

The real part of ⟨*z*, *w*⟩ is then the four-dimensional Euclidean dot product. This inner product is *Hermitian* symmetric, which means that the result of interchanging z and w is the complex conjugate: $\langle w,z\rangle ={\overline {\langle z,w\rangle }}\,.$

### Definition

A *Hilbert space* is a real or complex inner product space that is also a complete metric space with respect to the distance function induced by the inner product.

To say that a complex vector space *H* is a *complex inner product space* means that there is an inner product $\langle x,y\rangle$ associating a complex number to each pair of elements $x,y$ of *H* that satisfies the following properties:

1. The inner product is conjugate symmetric; that is, the inner product of a pair of elements is equal to the complex conjugate of the inner product of the swapped elements: $\langle y,x\rangle ={\overline {\langle x,y\rangle }}\,.$ Importantly, this implies that $\langle x,x\rangle$ is a real number.
2. The inner product is linear in its first argument. For all complex numbers a and $b,$ $\langle ax_{1}+bx_{2},y\rangle =a\langle x_{1},y\rangle +b\langle x_{2},y\rangle \,.$
3. The inner product of an element with itself is positive definite: ${\begin{alignedat}{4}\langle x,x\rangle >0&\quad {\text{ if }}x\neq 0,\\\langle x,x\rangle =0&\quad {\text{ if }}x=0\,.\end{alignedat}}$

It follows from properties 1 and 2 that a complex inner product is *antilinear*, also called *conjugate linear*, in its second argument, meaning that $\langle x,ay_{1}+by_{2}\rangle ={\bar {a}}\langle x,y_{1}\rangle +{\bar {b}}\langle x,y_{2}\rangle \,.$

A *real inner product space* is defined in the same way, except that *H* is a real vector space and the inner product takes real values. Such an inner product will be a bilinear map and $(H,H,\langle \cdot ,\cdot \rangle )$ will form a dual system.

The norm is the real-valued function $\|x\|={\sqrt {\langle x,x\rangle }}\,,$ and the distance d between two points $x,y$ in *H* is defined in terms of the norm by $d(x,y)=\|x-y\|={\sqrt {\langle x-y,x-y\rangle }}\,.$ Here, $d(x,y)$ is a distance function meaning firstly that it is symmetric in x and $y,$ secondly that the distance between x and itself is zero, and otherwise the distance between x and y must be positive, and lastly that the triangle inequality holds, meaning that the length of one leg of a triangle *xyz* cannot exceed the sum of the lengths of the other two legs: $d(x,z)\leq d(x,y)+d(y,z)\,.$

This last property is ultimately a consequence of the more fundamental Cauchy–Schwarz inequality, which asserts $\left|\langle x,y\rangle \right|\leq \|x\|\|y\|$ with equality if and only if x and y are linearly dependent.

With a distance function defined in this way, any inner product space is a metric space. An inner product space is sometimes known as a *pre-Hilbert space*. Any pre-Hilbert space that is additionally also a complete space is a Hilbert space.

The *completeness* of *H* is expressed using a form of the Cauchy criterion for sequences in *H*: a pre-Hilbert space *H* is complete if every Cauchy sequence converges with respect to this norm to an element in the space. Completeness can be characterized by the following equivalent condition: if a series of vectors $\sum _{k=0}^{\infty }u_{k}$ converges absolutely in the sense that $\sum _{k=0}^{\infty }\|u_{k}\|<\infty \,,$ then the series converges in *H*, in the sense that the partial sums converge to an element of *H*.

As a complete normed space, Hilbert spaces are by definition also Banach spaces. As such they are topological vector spaces, in which topological notions like the openness and closedness of subsets are well defined. Of special importance is the notion of a closed linear subspace of a Hilbert space that, with the inner product induced by restriction, is also complete (being a closed set in a complete metric space) and therefore a Hilbert space in its own right.

### Second example: sequence spaces

The sequence space ${\textstyle \ell ^{2}}$ consists of all infinite sequences **z** = (*z*1, *z*2, ...) of complex numbers such that the series $\sum _{n=1}^{\infty }|z_{n}|^{2}$ of its squared norms converges. The inner product on ${\textstyle \ell ^{2}}$ is defined by $\langle \mathbf {z} ,\mathbf {w} \rangle =\sum _{n=1}^{\infty }z_{n}{\overline {w}}_{n}\,.$ The series for the inner product converges as a consequence of the Cauchy–Schwarz inequality and the assumed convergence of the two series of squared norms.

Completeness of the space holds provided that whenever a series of elements from ${\textstyle \ell ^{2}}$ converges absolutely (in norm), then it converges to an element of ${\textstyle \ell ^{2}}$ . The proof is basic in mathematical analysis, and permits mathematical series of elements of the space to be manipulated with the same ease as series of complex numbers (or vectors in a finite-dimensional Euclidean space).


## History

Prior to the development of Hilbert spaces, other generalizations of Euclidean spaces were known to mathematicians and physicists. In particular, the idea of an abstract linear space (vector space) had gained some traction towards the end of the 19th century: this is a space whose elements can be added together and multiplied by scalars (such as real or complex numbers) without necessarily identifying these elements with "geometric" vectors, such as position and momentum vectors in physical systems. Other objects studied at the turn of the 20th century, in particular spaces of sequences (including series) and spaces of functions, can naturally be thought of as linear spaces. Functions, for instance, can be added together or multiplied by constant scalars, and these operations obey the algebraic laws satisfied by addition and scalar multiplication of spatial vectors.

In the first decade of the 20th century, parallel developments led to the introduction of Hilbert spaces. The first of these was the observation, which arose during David Hilbert and Erhard Schmidt's study of integral equations, that two square-integrable real-valued functions f and g on an interval [*a*, *b*] have an *inner product*

$\langle f,g\rangle =\int _{a}^{b}f(x)g(x)\,\mathrm {d} x$

that has many of the familiar properties of the Euclidean dot product. In particular, the idea of an orthogonal family of functions has meaning. Schmidt exploited the similarity of this inner product with the usual dot product to prove an analog of the spectral decomposition for an operator of the form

$f(x)\mapsto \int _{a}^{b}K(x,y)f(y)\,\mathrm {d} y$

where K is a continuous function symmetric in x and y. The resulting eigenfunction expansion expresses the function K as a series of the form

$K(x,y)=\sum _{n}\lambda _{n}\varphi _{n}(x)\varphi _{n}(y)$

where the functions φn are orthogonal in the sense that ⟨*φ**n*, *φ**m*⟩ = 0 for all *n* ≠ *m*. The individual terms in this series are sometimes referred to as elementary product solutions. However, there are eigenfunction expansions that fail to converge in a suitable sense to a square-integrable function: the missing ingredient, which ensures convergence, is completeness.

The second development was the Lebesgue integral, an alternative to the Riemann integral introduced by Henri Lebesgue in 1904. The Lebesgue integral made it possible to integrate a much broader class of functions. In 1907, Frigyes Riesz and Ernst Sigismund Fischer independently proved that the space *L*2 of square Lebesgue-integrable functions is a complete metric space. As a consequence of the interplay between geometry and completeness, the 19th century results of Joseph Fourier, Friedrich Bessel and Marc-Antoine Parseval on trigonometric series easily carried over to these more general spaces, resulting in a geometrical and analytical apparatus now usually known as the Riesz–Fischer theorem.

Further basic results were proved in the early 20th century. For example, the Riesz representation theorem was independently established by Maurice Fréchet and Frigyes Riesz in 1907. John von Neumann coined the term *abstract Hilbert space* in his work on unbounded Hermitian operators. Although other mathematicians such as Hermann Weyl and Norbert Wiener had already studied particular Hilbert spaces in great detail, often from a physically motivated point of view, von Neumann gave the first complete and axiomatic treatment of them. Von Neumann later used them in his seminal work on the foundations of quantum mechanics, and in his continued work with Eugene Wigner. The name "Hilbert space" was soon adopted by others, for example by Hermann Weyl in his book on quantum mechanics and the theory of groups.

The significance of the concept of a Hilbert space was underlined with the realization that it offers one of the best mathematical formulations of quantum mechanics. In short, the states of a quantum mechanical system are vectors in a certain Hilbert space, the observables are hermitian operators on that space, the symmetries of the system are unitary operators, and measurements are orthogonal projections. The relation between quantum mechanical symmetries and unitary operators provided an impetus for the development of the unitary representation theory of groups, initiated in the 1928 work of Hermann Weyl. On the other hand, in the early 1930s it became clear that classical mechanics can be described in terms of Hilbert space (Koopman–von Neumann classical mechanics) and that certain properties of classical dynamical systems can be analyzed using Hilbert space techniques in the framework of ergodic theory.

The algebra of observables in quantum mechanics is naturally an algebra of operators defined on a Hilbert space, according to Werner Heisenberg's matrix mechanics formulation of quantum theory. Von Neumann began investigating operator algebras in the 1930s, as rings of operators on a Hilbert space. Such algebras are now known as von Neumann algebras. In the 1940s, Israel Gelfand, Mark Naimark and Irving Segal gave a definition of a kind of operator algebras called C*-algebras that on the one hand made no reference to an underlying Hilbert space, and on the other extrapolated many of the useful features of the operator algebras that had previously been studied. The spectral theorem for self-adjoint operators in particular that underlies much of the existing Hilbert space theory was generalized to C*-algebras. These techniques are now basic in abstract harmonic analysis and representation theory.


## Further examples

### Lebesgue spaces

Lebesgue spaces are function spaces associated to measure spaces (*X*, *M*, *μ*), where *X* is a set, *M* is a σ-algebra of subsets of *X*, and *μ* is a countably additive measure on *M*. Let *L*2(*X*, *μ*) be the space of those complex-valued measurable functions on *X* for which the Lebesgue integral of the square of the absolute value of the function is finite, i.e., for a function *f* in *L*2(*X*, *μ*), $\int _{X}|f|^{2}\,\mathrm {d} \mu <\infty \,,$ and where functions are identified if and only if they differ only on a set of measure zero.

The inner product of functions *f* and *g* in *L*2(*X*, *μ*) is then defined as $\langle f,g\rangle =\int _{X}f(t){\overline {g(t)}}\,\mathrm {d} \mu (t)$ or $\langle f,g\rangle =\int _{X}{\overline {f(t)}}g(t)\,\mathrm {d} \mu (t)\,,$

where the second form (conjugation of the first element) is commonly found in the theoretical physics literature. For *f* and *g* in *L*2, the integral exists because of the Cauchy–Schwarz inequality, and defines an inner product on the space. Equipped with this inner product, *L*2 is in fact complete. The Lebesgue integral is essential to ensure completeness: on domains of real numbers, for instance, not enough functions are Riemann integrable.

The Lebesgue spaces appear in many natural settings. The spaces *L*2(**R**) and *L*2([0,1]) of square-integrable functions with respect to the Lebesgue measure on the real line and unit interval, respectively, are natural domains on which to define the Fourier transform and Fourier series. In other situations, the measure may be something other than the ordinary Lebesgue measure on the real line. For instance, if *w* is any positive measurable function, the space of all measurable functions *f* on the interval [0, 1] satisfying $\int _{0}^{1}{\bigl |}f(t){\bigr |}^{2}w(t)\,\mathrm {d} t<\infty$ is called the weighted *L*2 space *L*2 *w*([0, 1]), and *w* is called the weight function. The inner product is defined by $\langle f,g\rangle =\int _{0}^{1}f(t){\overline {g(t)}}w(t)\,\mathrm {d} t\,.$

The weighted space *L*2 *w*([0, 1]) is identical with the Hilbert space *L*2([0, 1], *μ*) where the measure *μ* of a Lebesgue-measurable set *A* is defined by $\mu (A)=\int _{A}w(t)\,\mathrm {d} t\,.$

Weighted *L*2 spaces like this are frequently used to study orthogonal polynomials, because different families of orthogonal polynomials are orthogonal with respect to different weighting functions.

### Sobolev spaces

Sobolev spaces, denoted by *H**s* or *W**s*,2, are Hilbert spaces. These are a special kind of function space in which differentiation may be performed, but that (unlike other Banach spaces such as the Hölder spaces) support the structure of an inner product. Because differentiation is permitted, Sobolev spaces are a convenient setting for the theory of partial differential equations. They also form the basis of the theory of direct methods in the calculus of variations.

For *s* a non-negative integer and Ω ⊂ **R***n*, the Sobolev space *H**s*(Ω) contains *L*2 functions whose weak derivatives of order up to *s* are also *L*2. The inner product in *H**s*(Ω) is $\langle f,g\rangle =\int _{\Omega }f(x){\bar {g}}(x)\,\mathrm {d} x+\int _{\Omega }Df(x)\cdot D{\bar {g}}(x)\,\mathrm {d} x+\cdots +\int _{\Omega }D^{s}f(x)\cdot D^{s}{\bar {g}}(x)\,\mathrm {d} x$ where the dot indicates the dot product in the Euclidean space of partial derivatives of each order. Sobolev spaces can also be defined when *s* is not an integer.

Sobolev spaces are also studied from the point of view of spectral theory, relying more specifically on the Hilbert space structure. If Ω is a suitable domain, then one can define the Sobolev space *H**s*(Ω) as the space of Bessel potentials; roughly, $H^{s}(\Omega )=\left\{(1-\Delta )^{-s/2}f\mathrel {\Big |} f\in L^{2}(\Omega )\right\}\,.$

Here Δ is the Laplacian and (1 − Δ)−*s* / 2 is understood in terms of the spectral mapping theorem. Apart from providing a workable definition of Sobolev spaces for non-integer *s*, this definition also has particularly desirable properties under the Fourier transform that make it ideal for the study of pseudodifferential operators. Using these methods on a compact Riemannian manifold, one can obtain for instance the Hodge decomposition, which is the basis of Hodge theory.

### Spaces of holomorphic functions

#### Hardy spaces

The Hardy spaces are function spaces, arising in complex analysis and harmonic analysis, whose elements are certain holomorphic functions in a complex domain. Let *U* denote the unit disc in the complex plane. Then the Hardy space *H*2(*U*) is defined as the space of holomorphic functions *f* on *U* such that the means $M_{r}(f)={\frac {1}{2\pi }}\int _{0}^{2\pi }\left|f{\bigl (}re^{i\theta }{\bigr )}\right|^{2}\,\mathrm {d} \theta$ remain bounded for *r* < 1. The norm on this Hardy space is defined by $\left\|f\right\|_{2}=\lim _{r\to 1}{\sqrt {M_{r}(f)}}\,.$

Hardy spaces in the disc are related to Fourier series. A function *f* is in *H*2(*U*) if and only if $f(z)=\sum _{n=0}^{\infty }a_{n}z^{n}$ where $\sum _{n=0}^{\infty }|a_{n}|^{2}<\infty \,.$

Thus *H*2(*U*) consists of those functions that are *L*2 on the circle, and whose negative frequency Fourier coefficients vanish.

#### Bergman spaces

The Bergman spaces are another family of Hilbert spaces of holomorphic functions. Let *D* be a bounded open set in the complex plane (or a higher-dimensional complex space) and let *L*2, *h*(*D*) be the space of holomorphic functions *f* in *D* that are also in *L*2(*D*) in the sense that $\|f\|^{2}=\int _{D}|f(z)|^{2}\,\mathrm {d} \mu (z)<\infty \,,$ where the integral is taken with respect to the Lebesgue measure in *D*. Clearly *L*2, *h*(*D*) is a subspace of *L*2(*D*); in fact, it is a closed subspace, and so a Hilbert space in its own right. This is a consequence of the estimate, valid on compact subsets *K* of *D*, that $\sup _{z\in K}\left|f(z)\right|\leq C_{K}\left\|f\right\|_{2}\,,$ which in turn follows from Cauchy's integral formula. Thus convergence of a sequence of holomorphic functions in *L*2(*D*) implies also compact convergence, and so the limit function is also holomorphic. Another consequence of this inequality is that the linear functional that evaluates a function *f* at a point of *D* is actually continuous on *L*2,*h*(*D*). The Riesz representation theorem implies that the evaluation functional can be represented as an element of *L*2,*h*(*D*). Thus, for every *z* ∈ *D*, there is a function *η**z* ∈ *L*2,*h*(*D*) such that $f(z)=\int _{D}f(\zeta ){\overline {\eta _{z}(\zeta )}}\,\mathrm {d} \mu (\zeta )$ for all *f* ∈ *L*2,*h*(*D*). The integrand $K(\zeta ,z)={\overline {\eta _{z}(\zeta )}}$ is known as the Bergman kernel of *D*. This integral kernel satisfies a reproducing property $f(z)=\int _{D}f(\zeta )K(\zeta ,z)\,\mathrm {d} \mu (\zeta )\,.$

A Bergman space is an example of a reproducing kernel Hilbert space, which is a Hilbert space of functions along with a kernel *K*(*ζ*, *z*) that verifies a reproducing property analogous to this one. The Hardy space *H*2(*D*) also admits a reproducing kernel, known as the Szegő kernel. Reproducing kernels are common in other areas of mathematics as well. For instance, in harmonic analysis the Poisson kernel is a reproducing kernel for the Hilbert space of square-integrable harmonic functions in the unit ball. The latter is a Hilbert space because the mean theorem for harmonic functions implies $L^{2}$ -bounded point evaluations, from which it follows that it is a closed subspace of $L^{2}$ .


## Applications

Many of the applications of Hilbert spaces exploit the fact that Hilbert spaces support generalizations of simple geometric concepts like projection and change of basis from their usual finite dimensional setting. In particular, the spectral theory of continuous self-adjoint linear operators on a Hilbert space generalizes the usual spectral decomposition of a matrix, and this often plays a major role in applications of the theory to other areas of mathematics and physics.

### Sturm–Liouville theory

In the theory of ordinary differential equations, spectral methods on a suitable Hilbert space are used to study the behavior of eigenvalues and eigenfunctions of differential equations. For example, the Sturm–Liouville problem arises in the study of the harmonics of waves in a violin string or a drum, and is a central problem in ordinary differential equations. The problem is a differential equation of the form $-{\frac {\mathrm {d} }{\mathrm {d} x}}\left[p(x){\frac {\mathrm {d} y}{\mathrm {d} x}}\right]+q(x)y=\lambda w(x)y$ for an unknown function *y* on an interval [*a*, *b*], satisfying general homogeneous Robin boundary conditions ${\begin{cases}\alpha y(a)+\alpha 'y'(a)&=0\\\beta y(b)+\beta 'y'(b)&=0\,.\end{cases}}$ The functions *p*, *q*, and *w* are given in advance, and the problem is to find the function *y* and constants *λ* for which the equation has a solution. The problem only has solutions for certain values of *λ*, called eigenvalues of the system, and this is a consequence of the spectral theorem for compact operators applied to the integral operator defined by the Green's function for the system. Furthermore, another consequence of this general result is that the eigenvalues *λ* of the system can be arranged in an increasing sequence tending to infinity.

### Partial differential equations

Hilbert spaces form a basic tool in the study of partial differential equations. For many classes of partial differential equations, such as linear elliptic equations, it is possible to consider a generalized solution (known as a weak solution) by enlarging the class of functions. Many weak formulations involve the class of Sobolev functions, which is a Hilbert space. A suitable weak formulation reduces to a geometrical problem, the analytic problem of finding a solution or, often what is more important, showing that a solution exists and is unique for given boundary data. For linear elliptic equations, one geometrical result that ensures unique solvability for a large class of problems is the Lax–Milgram theorem. This strategy forms the rudiment of the Galerkin method (a finite element method) for numerical solution of partial differential equations.

An example is the Poisson equation −Δ*u* = *g* with Dirichlet boundary conditions in a bounded domain Ω in **R**2. The weak formulation consists of finding a function *u* such that, for all continuously differentiable functions *v* in Ω vanishing on the boundary: $\int _{\Omega }\nabla u\cdot \nabla v=\int _{\Omega }gv\,.$

This can be recast in terms of the Hilbert space *H*1 0(Ω) consisting of functions *u* such that *u*, along with its weak partial derivatives, are square integrable on Ω, and vanish on the boundary. The question then reduces to finding *u* in this space such that for all *v* in this space $a(u,v)=b(v)$

where *a* is a continuous bilinear form, and *b* is a continuous linear functional, given respectively by $a(u,v)=\int _{\Omega }\nabla u\cdot \nabla v,\quad b(v)=\int _{\Omega }gv\,.$

Since the Poisson equation is elliptic, it follows from Poincaré's inequality that the bilinear form *a* is coercive. The Lax–Milgram theorem then ensures the existence and uniqueness of solutions of this equation.

Hilbert spaces allow for many elliptic partial differential equations to be formulated in a similar way, and the Lax–Milgram theorem is then a basic tool in their analysis. With suitable modifications, similar techniques can be applied to parabolic partial differential equations and certain hyperbolic partial differential equations.

### Ergodic theory

The field of ergodic theory is the study of the long-term behavior of chaotic dynamical systems. The protypical case of a field that ergodic theory applies to is thermodynamics, in which—though the microscopic state of a system is extremely complicated (it is impossible to understand the ensemble of individual collisions between particles of matter)—the average behavior over sufficiently long time intervals is tractable. The laws of thermodynamics are assertions about such average behavior. In particular, one formulation of the zeroth law of thermodynamics asserts that over sufficiently long timescales, the only functionally independent measurement that one can make of a thermodynamic system in equilibrium is its total energy, in the form of temperature.

An ergodic dynamical system is one for which, apart from the energy—measured by the Hamiltonian—there are no other functionally independent conserved quantities on the phase space. More explicitly, suppose that the energy *E* is fixed, and let Ω*E* be the subset of the phase space consisting of all states of energy *E* (an energy surface), and let *T**t* denote the evolution operator on the phase space. The dynamical system is ergodic if every invariant measurable function on Ω*E* is constant almost everywhere. An invariant function *f* is one for which $f(T_{t}w)=f(w)$ for all *w* on Ω*E* and all time *t*. Liouville's theorem implies that there exists a measure *μ* on the energy surface that is invariant under the time translation. As a result, time translation is a unitary transformation of the Hilbert space *L*2(Ω*E*, *μ*) consisting of square-integrable functions on the energy surface Ω*E* with respect to the inner product $\left\langle f,g\right\rangle _{L^{2}\left(\Omega _{E},\mu \right)}=\int _{\Omega _{E}}f{\bar {g}}\,\mathrm {d} \mu \,.$

The von Neumann mean ergodic theorem states the following:

- If *U**t* is a (strongly continuous) one-parameter semigroup of unitary operators on a Hilbert space *H*, and *P* is the orthogonal projection onto the space of common fixed points of *U**t*, {*x* ∈*H* | *U**t**x* = *x*, ∀*t* > 0}, then $Px=\lim _{T\to \infty }{\frac {1}{T}}\int _{0}^{T}U_{t}x\,\mathrm {d} t\,.$

For an ergodic system, the fixed set of the time evolution consists only of the constant functions, so the ergodic theorem implies the following: for any function *f* ∈ *L*2(Ω*E*, *μ*), ${\underset {T\to \infty }{L^{2}-\lim }}{\frac {1}{T}}\int _{0}^{T}f(T_{t}w)\,\mathrm {d} t=\int _{\Omega _{E}}f(y)\,\mathrm {d} \mu (y)\,.$

That is, the long time average of an observable *f* is equal to its expectation value over an energy surface.

### Fourier analysis

One of the basic goals of Fourier analysis is to decompose a function into a (possibly infinite) linear combination of given basis functions: the associated Fourier series. The classical Fourier series associated to a function *f* defined on the interval [0, 1] is a series of the form $\sum _{n=-\infty }^{\infty }a_{n}e^{2\pi in\theta }$ where $a_{n}=\int _{0}^{1}f(\theta )\;\!e^{-2\pi in\theta }\,\mathrm {d} \theta \,.$

The example of adding up the first few terms in a Fourier series for a sawtooth function is shown in the figure. The basis functions are sine waves with wavelengths ⁠*λ*/*n*⁠ (for integer *n*) shorter than the wavelength *λ* of the sawtooth itself (except for *n* = 1, the *fundamental* wave).

A significant problem in classical Fourier series asks in what sense the Fourier series converges, if at all, to the function *f*. Hilbert space methods provide one possible answer to this question. The functions *en*(*θ*) = *e*2π*inθ* form an orthogonal basis of the Hilbert space *L*2([0, 1]). Consequently, any square-integrable function can be expressed as a series $f(\theta )=\sum _{n}a_{n}e_{n}(\theta )\,,\quad a_{n}=\langle f,e_{n}\rangle$ and, moreover, this series converges in the Hilbert space sense (that is, in the *L*2 mean).

The problem can also be studied from the abstract point of view: every Hilbert space has an orthonormal basis, and every element of the Hilbert space can be written in a unique way as a sum of multiples of these basis elements. The coefficients appearing on these basis elements are sometimes known abstractly as the Fourier coefficients of the element of the space. The abstraction is especially useful when it is more natural to use different basis functions for a space such as *L*2([0, 1]). In many circumstances, it is desirable not to decompose a function into trigonometric functions, but rather into orthogonal polynomials or wavelets for instance, and in higher dimensions into spherical harmonics.

For instance, if *e**n* are any orthonormal basis functions of *L*2[0, 1], then a given function in *L*2[0, 1] can be approximated as a finite linear combination $f(x)\approx f_{n}(x)=a_{1}e_{1}(x)+a_{2}e_{2}(x)+\cdots +a_{n}e_{n}(x)\,.$

The coefficients {*a**j*} are selected to make the magnitude of the difference ‖*f* − *f**n*‖2 as small as possible. Geometrically, the best approximation is the orthogonal projection of *f* onto the subspace consisting of all linear combinations of the {*e**j*}, and can be calculated by $a_{j}=\int _{0}^{1}{\overline {e_{j}(x)}}f(x)\,\mathrm {d} x\,.$

That this formula minimizes the difference ‖*f* − *f**n*‖2 is a consequence of Bessel's inequality and Parseval's formula.

In various applications to physical problems, a function can be decomposed into physically meaningful eigenfunctions of a differential operator (typically the Laplace operator): this forms the foundation for the spectral study of functions, in reference to the spectrum of the differential operator. A concrete physical application involves the problem of hearing the shape of a drum: given the fundamental modes of vibration that a drumhead is capable of producing, can one infer the shape of the drum itself? The mathematical formulation of this question involves the Dirichlet eigenvalues of the Laplace equation in the plane, that represent the fundamental modes of vibration in direct analogy with the integers that represent the fundamental modes of vibration of the violin string.

Spectral theory also underlies certain aspects of the Fourier transform of a function. Whereas Fourier analysis decomposes a function defined on a compact set into the discrete spectrum of the Laplacian (which corresponds to the vibrations of a violin string or drum), the Fourier transform of a function is the decomposition of a function defined on all of Euclidean space into its components in the continuous spectrum of the Laplacian. The Fourier transformation is also geometrical, in a sense made precise by the Plancherel theorem, that asserts that it is an isometry of one Hilbert space (the "time domain") with another (the "frequency domain"). This isometry property of the Fourier transformation is a recurring theme in abstract harmonic analysis (since it reflects the conservation of energy for the continuous Fourier Transform), as evidenced for instance by the Plancherel theorem for spherical functions occurring in noncommutative harmonic analysis.

### Quantum mechanics

In the mathematically rigorous formulation of quantum mechanics, developed by John von Neumann, the possible states (more precisely, the pure states) of a quantum mechanical system are represented by unit vectors (called *state vectors*) residing in a complex separable Hilbert space, known as the state space, well defined up to a complex number of norm 1 (the phase factor). In other words, the possible states are points in the projectivization of a Hilbert space, usually called the complex projective space. The exact nature of this Hilbert space is dependent on the system; for example, the position and momentum states for a single non-relativistic spin zero particle is the space of all square-integrable functions, while the states for the spin of a single proton are unit elements of the two-dimensional complex Hilbert space of spinors. Each observable is represented by a self-adjoint linear operator acting on the state space. Each eigenstate of an observable corresponds to an eigenvector of the operator, and the associated eigenvalue corresponds to the value of the observable in that eigenstate.

The inner product between two state vectors is a complex number known as a probability amplitude. During an ideal measurement of a quantum mechanical system, the probability that a system collapses from a given initial state to a particular eigenstate is given by the square of the absolute value of the probability amplitudes between the initial and final states. The possible results of a measurement are the eigenvalues of the operator—which explains the choice of self-adjoint operators, for all the eigenvalues must be real. The probability distribution of an observable in a given state can be found by computing the spectral decomposition of the corresponding operator.

For a general system, states are typically not pure, but instead are represented as statistical mixtures of pure states, or mixed states, given by density matrices: self-adjoint operators of trace one on a Hilbert space. Moreover, for general quantum mechanical systems, the effects of a single measurement can influence other parts of a system in a manner that is described instead by a positive operator valued measure. Thus the structure both of the states and observables in the general theory is considerably more complicated than the idealization for pure states.

### Probability theory

In probability theory, Hilbert spaces also have diverse applications. Here a fundamental Hilbert space is the space of random variables on a given probability space, having class $L^{2}$ (finite first and second moments). A common operation in statistics is that of centering a random variable by subtracting its expectation. Thus if X is a random variable, then $X-E(X)$ is its centering. In the Hilbert space view, this is the orthogonal projection of X onto the kernel of the expectation operator, which a continuous linear functional on the Hilbert space (in fact, the inner product with the constant random variable 1), and so this kernel is a closed subspace.

The conditional expectation has a natural interpretation in the Hilbert space. Suppose that a probability space $(\Omega ,P,{\mathcal {B}})$ is given, where ${\mathcal {B}}$ is a sigma algebra on the set $\Omega$ , and P is a probability measure on the measure space $(\Omega ,{\mathcal {B}})$ . If ${\mathcal {F}}\leq {\mathcal {B}}$ is a sigma subalgebra of ${\mathcal {B}}$ , then the conditional expectation $E[X\mid {\mathcal {F}}]$ is the orthogonal projection of X onto the subspace of $L^{2}(\Omega ,P)$ consisting of the ${\mathcal {F}}$ -measurable functions. If the random variable X in $L^{2}(\Omega ,P)$ is independent of the sigma algebra ${\mathcal {F}}$ then conditional expectation $E(X\mid {\mathcal {F}})=E(X)$ , i.e., its projection onto the ${\mathcal {F}}$ -measurable functions is constant. Equivalently, the projection of its centering is zero.

In particular, if two random variables X and Y (in $L^{2}(\Omega ,P)$ ) are independent, then the centered random variables $X-E(X)$ and $Y-E(Y)$ are orthogonal. (This means that the two variables have zero covariance: they are uncorrelated.) In that case, the Pythagorean theorem in the kernel of the expectation operator implies that the variances of X and Y satisfy the identity: $\operatorname {Var} (X+Y)=\operatorname {Var} (X)+\operatorname {Var} (Y),$ sometimes called the Pythagorean theorem of statistics, and is of importance in linear regression. The analysis of variance could use the Pythagorean Theorem so that the variance is viewed as the decomposition of the squared length of a vector into the sum of the squared lengths of several vectors.

The theory of martingales can be formulated in Hilbert spaces. A martingale in a Hilbert space is a sequence $x_{1},x_{2},\dots$ of elements of a Hilbert space such that, for each *n*, $x_{n}$ is the orthogonal projection of $x_{n+1}$ onto the linear hull of $x_{1},\dots ,x_{n}$ . If the $x_{k}$ are random variables, this reproduces the usual definition of a (discrete) martingale: the expectation of $x_{n+1}$ , conditioned on $x_{1},\dots ,x_{n}$ , is equal to $x_{n}$ .

Hilbert spaces are also used throughout the foundations of the Itô calculus. To any square-integrable martingale, it is possible to associate a Hilbert norm on the space of equivalence classes of progressively measurable processes with respect to the martingale (using the quadratic variation of the martingale as the measure). The Itô integral can be constructed by first defining it for simple processes, and then exploiting their density in the Hilbert space. A noteworthy result is then the Itô isometry, which attests that for any martingale *M* having quadratic variation measure $d\langle M\rangle _{t}$ , and any progressively measurable process *H*: $E{\biggl [}{\left(\int _{0}^{t}H_{s}\,dM_{s}\right){\vphantom {{\Bigr )}^{2}}}^{\!\!2\,}}{\biggr ]}=E\left[\int _{0}^{t}H_{s}^{2}\,d\langle M\rangle _{s}\right]$ whenever the expectation on the right-hand side is finite.

A deeper application of Hilbert spaces that is especially important in the theory of Gaussian processes is an attempt, due to Leonard Gross and others, to make sense of certain formal integrals over infinite dimensional spaces like the Feynman path integral from quantum field theory. The problem with integrals like this is that there is no infinite dimensional Lebesgue measure. The notion of an abstract Wiener space allows one to construct a measure on a Banach space *B* that contains a Hilbert space *H*, called the Cameron–Martin space, as a dense subset, out of a finitely additive cylinder set measure on *H*. The resulting measure on *B* is countably additive and invariant under translation by elements of *H*, and this provides a mathematically rigorous way of thinking of the Wiener measure as a Gaussian measure adapted to the Sobolev space $H^{1}([0,\infty ))$ .

### Color perception

Any true physical color can be represented by a combination of pure spectral colors. As physical colors can be composed of any number of spectral colors, the space of physical colors may aptly be represented by a Hilbert space over spectral colors. Humans have three types of cone cells for color perception, so the perceivable colors can be represented by 3-dimensional Euclidean space. The many-to-one linear mapping from the Hilbert space of physical colors to the Euclidean space of human perceivable colors explains why many distinct physical colors may be perceived by humans to be identical (e.g., pure yellow light versus a mix of red and green light, see *Metamerism*).
