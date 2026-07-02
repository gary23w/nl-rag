---
title: "Spectral theory of ordinary differential equations"
source: https://en.wikipedia.org/wiki/Spectral_theory_of_ordinary_differential_equations
domain: sturm-liouville-theory
license: CC-BY-SA-4.0
tags: sturm-liouville theory, eigenfunction expansion, oscillation theory, rayleigh quotient
fetched: 2026-07-02
---

# Spectral theory of ordinary differential equations

In mathematics, the **spectral theory of ordinary differential equations** is the part of spectral theory concerned with the determination of the spectrum and eigenfunction expansion associated with a linear ordinary differential equation. In his dissertation, Hermann Weyl generalized the classical Sturm–Liouville theory on a finite closed interval to second order differential operators with singularities at the endpoints of the interval, possibly semi-infinite or infinite. Unlike the classical case, the spectrum may no longer consist of just a countable set of eigenvalues, but may also contain a continuous part. In this case the eigenfunction expansion involves an integral over the continuous part with respect to a spectral measure, given by the Titchmarsh–Kodaira formula. The theory was put in its final simplified form for singular differential equations of even degree by Kodaira and others, using von Neumann's spectral theorem. It has had important applications in quantum mechanics, operator theory and harmonic analysis on semisimple Lie groups.

## Introduction

Spectral theory for second order ordinary differential equations on a compact interval was developed by Jacques Charles François Sturm and Joseph Liouville in the nineteenth century and is now known as Sturm–Liouville theory. In modern language, it is an application of the spectral theorem for compact operators due to David Hilbert. In his dissertation, published in 1910, Hermann Weyl extended this theory to second order ordinary differential equations with singularities at the endpoints of the interval, now allowed to be infinite or semi-infinite. He simultaneously developed a spectral theory adapted to these special operators and introduced boundary conditions in terms of his celebrated dichotomy between *limit points* and *limit circles*.

In the 1920s, John von Neumann established a general spectral theorem for unbounded self-adjoint operators, which Kunihiko Kodaira used to streamline Weyl's method. Kodaira also generalised Weyl's method to singular ordinary differential equations of even order and obtained a simple formula for the spectral measure. The same formula had also been obtained independently by E. C. Titchmarsh in 1946 (scientific communication between Japan and the United Kingdom had been interrupted by World War II). Titchmarsh had followed the method of the German mathematician Emil Hilb, who derived the eigenfunction expansions using complex function theory instead of operator theory. Other methods avoiding the spectral theorem were later developed independently by Levitan, Levinson and Yoshida, who used the fact that the resolvent of the singular differential operator could be approximated by compact resolvents corresponding to Sturm–Liouville problems for proper subintervals. Another method was found by Mark Grigoryevich Krein; his use of *direction functionals* was subsequently generalised by Izrail Glazman to arbitrary ordinary differential equations of even order.

Weyl applied his theory to Carl Friedrich Gauss's hypergeometric differential equation, thus obtaining a far-reaching generalisation of the transform formula of Gustav Ferdinand Mehler (1881) for the Legendre differential equation, rediscovered by the Russian physicist Vladimir Fock in 1943, and usually called the Mehler–Fock transform. The corresponding ordinary differential operator is the radial part of the Laplacian operator on 2-dimensional hyperbolic space. More generally, the Plancherel theorem for SL(2,R) of Harish Chandra and Gelfand–Naimark can be deduced from Weyl's theory for the hypergeometric equation, as can the theory of spherical functions for the isometry groups of higher dimensional hyperbolic spaces. Harish Chandra's later development of the Plancherel theorem for general real semisimple Lie groups was strongly influenced by the methods Weyl developed for eigenfunction expansions associated with singular ordinary differential equations. Equally importantly the theory also laid the mathematical foundations for the analysis of the Schrödinger equation and scattering matrix in quantum mechanics.

## Solutions of ordinary differential equations

### Reduction to standard form

Let *D* be the second order differential operator on (*a*, *b*) given by $Df(x)=-p(x)f''(x)+r(x)f'(x)+q(x)f(x),$ where *p* is a strictly positive continuously differentiable function and *q* and *r* are continuous real-valued functions.

For *x*0 in (*a*, *b*), define the Liouville transformation *ψ* by $\psi (x)=\int _{x_{0}}^{x}p(t)^{-1/2}\,dt$

If $U:L^{2}(a,b)\mapsto L^{2}(\psi (a),\psi (b))$ is the unitary operator defined by $(Uf)(\psi (x))=f(x)\times \left(\psi '(x)\right)^{-1/2},\ \ \forall x\in (a,b)$ then $U{\frac {\mathrm {d} }{\mathrm {d} x}}U^{-1}g=g'\psi '+{\frac {1}{2}}g{\frac {\psi ''}{\psi '}}$ and ${\begin{aligned}U{\frac {\mathrm {d} ^{2}}{\mathrm {d} x^{2}}}U^{-1}g&=\left(U{\frac {\mathrm {d} }{\mathrm {d} x}}U^{-1}\right)\times \left(U{\frac {\mathrm {d} }{\mathrm {d} x}}U^{-1}\right)g\\[1ex]&={\frac {\mathrm {d} }{\mathrm {d} \psi }}\left[g'\psi '+{\frac {1}{2}}g{\frac {\psi ''}{\psi '}}\right]\cdot \psi '+{\frac {1}{2}}\left[g'\psi '+{\frac {1}{2}}g{\frac {\psi ''}{\psi '}}\right]\cdot {\frac {\psi ''}{\psi '}}\\[1ex]&=g''\psi '^{2}+2g'\psi ''+{\frac {1}{2}}g\cdot \left[{\frac {\psi '''}{\psi '}}-{\frac {1}{2}}{\frac {\psi ''^{2}}{\psi '^{2}}}\right]\end{aligned}}$

Hence, $UDU^{-1}g=-g''+Rg'+Qg,$ where $R={\frac {p'+r}{p^{1/2}}}$ and $Q=q-{\frac {rp'}{4p}}+{\frac {p''}{4}}-{\frac {5p'^{2}}{16p}}$

The term in *g′* can be removed using an Euler integrating factor. If *S′*/*S* = *R*/2, then *h* = *Sg* satisfies $(SUDU^{-1}S^{-1})h=-h''+Vh,$ where the potential *V* is given by $V=Q+{\frac {S''}{S}}$

The differential operator can thus always be reduced to one of the form $Df=-f''+qf.$

### Existence theorem

The following is a version of the classical Picard existence theorem for second order differential equations with values in a Banach space **E**.

Let *α*, *β* be arbitrary elements of **E**, *A* a bounded operator on *E* and *q* a continuous function on [*a*, *b*].

Then, for *c* = *a* or *c* = *b*, the differential equation $Df=Af$ has a unique solution *f* in *C*2([*a*,*b*], **E**) satisfying the initial conditions $f(c)=\beta \,,\;f'(c)=\alpha .$

In fact a solution of the differential equation with these initial conditions is equivalent to a solution of the integral equation $f=h+Tf$ with *T* the bounded linear map on *C*([*a*,*b*], **E**) defined by $Tf(x)=\int _{c}^{x}K(x,y)f(y)\,dy,$ where *K* is the Volterra kernel $K(x,t)=(x-t)(q(t)-A)$ and $h(x)=\alpha (x-c)+\beta .$

Since ‖*T*k‖ tends to 0, this integral equation has a unique solution given by the Neumann series $f=(I-T)^{-1}h=h+Th+T^{2}h+T^{3}h+\cdots$

This iterative scheme is often called *Picard iteration* after the French mathematician Charles Émile Picard.

### Fundamental eigenfunctions

If *f* is twice continuously differentiable (i.e. *C*2) on (*a*, *b*) satisfying *Df* = *λf*, then *f* is called an eigenfunction of *D* with eigenvalue λ.

- In the case of a compact interval [*a*, *b*] and *q* continuous on [*a*, *b*], the existence theorem implies that for *c* = *a* or *c* = *b* and every complex number λ there a unique *C*2 eigenfunction *f**λ* on [*a*, *b*] with *f**λ*(*c*) and *f*′*λ*(*c*) prescribed. Moreover, for each x in [*a*, *b*], *f**λ*(*x*) and *f*′*λ*(*x*) are holomorphic functions of λ.
- For an arbitrary interval (*a*, *b*) and *q* continuous on (*a*, *b*), the existence theorem implies that for *c* in (*a*, *b*) and every complex number λ there a unique *C*2 eigenfunction *f**λ* on (*a*, *b*) with *f**λ*(*c*) and *f*′*λ*(*c*) prescribed. Moreover, for each x in (*a*, *b*), *f**λ*(*x*) and *f*′*λ*(*x*) are holomorphic functions of λ.

### Green's formula

If *f* and *g* are *C*2 functions on (*a*, *b*), the Wronskian *W*(*f*, *g*) is defined by $W(f,g)(x)=f(x)g'(x)-f'(x)g(x).$

Green's formula - which in this one-dimensional case is a simple integration by parts - states that for x, y in (*a*, *b*) $\int _{x}^{y}(Df)g-f(Dg)\,dt=W(f,g)(y)-W(f,g)(x).$

When *q* is continuous and *f*, *g* are *C*2 on the compact interval [*a*, *b*], this formula also holds for *x* = *a* or *y* = *b*.

When *f* and *g* are eigenfunctions for the same eigenvalue, then ${\frac {d}{dx}}W(f,g)=0,$ so that *W*(*f*, *g*) is independent of x.

## Classical Sturm–Liouville theory

Let [*a*, *b*] be a finite closed interval, *q* a real-valued continuous function on [*a*, *b*] and let *H*0 be the space of *C*2 functions *f* on [*a*, *b*] satisfying the Robin boundary conditions ${\begin{cases}\cos \alpha \,f(a)-\sin \alpha \,f'(a)=0,\\[0.5ex]\cos \beta \,f(b)-\sin \beta \,f'(b)=0,\end{cases}}$ with inner product $(f,g)=\int _{a}^{b}f(x){\overline {g(x)}}\,dx.$

In practice usually one of the two standard boundary conditions:

- Dirichlet boundary condition *f*(*c*) = 0
- Neumann boundary condition *f*′(*c*) = 0

is imposed at each endpoint *c* = *a*, *b*.

The differential operator *D* given by $Df=-f''+qf$ acts on *H*0. A function *f* in *H*0 is called an eigenfunction of *D* (for the above choice of boundary values) if *Df* = *λ* *f* for some complex number λ, the corresponding eigenvalue. By Green's formula, *D* is formally self-adjoint on *H*0, since the Wronskian *W*(*f*, *g*) vanishes if both *f*, *g* satisfy the boundary conditions: $(Df,g)=(f,Dg),\quad {\text{ for }}f,g\in H_{0}.$

As a consequence, exactly as for a self-adjoint matrix in finite dimensions,

- the eigenvalues of *D* are real;
- the eigenspaces for distinct eigenvalues are orthogonal.

It turns out that the eigenvalues can be described by the maximum-minimum principle of Rayleigh–Ritz (see below). In fact it is easy to see *a priori* that the eigenvalues are bounded below because the operator *D* is itself *bounded below* on *H*0:

$(Df,f)\geq M(f,f)$

for some finite (possibly negative) constant

M

.

In fact, integrating by parts, $(Df,f)=\left[-f'{\overline {f}}\right]_{a}^{b}+\int |f'|^{2}+\int q|f|^{2}.$

For Dirichlet or Neumann boundary conditions, the first term vanishes and the inequality holds with *M* = inf *q*.

For general Robin boundary conditions the first term can be estimated using an elementary *Peter-Paul* version of Sobolev's inequality:

> "Given *ε* > 0, there is constant *R* > 0 such that |*f*(*x*)|2 ≤ *ε* (*f*′, f′) + *R* (*f*, *f*) for all *f* in *C*1[*a*, *b*]."

In fact, since $|f(b)-f(x)|\leq (b-a)^{1/2}\cdot \|f'\|_{2},$ only an estimate for *f*(*b*) is needed and this follows by replacing *f*(*x*) in the above inequality by (*x* − *a*)*n*·(*b* − *a*)−*n*·*f*(*x*) for n sufficiently large.

### Green's function (regular case)

From the theory of ordinary differential equations, there are unique fundamental eigenfunctions *φ**λ*(*x*), *χ**λ*(*x*) such that

- *D* *φ**λ* = *λ* *φ**λ*, *φ**λ*(*a*) = sin *α*, *φ**λ*'(*a*) = cos *α*
- *D* *χ**λ* = *λ* *χ**λ*, *χ**λ*(*b*) = sin *β*, *χ**λ*'(*b*) = cos *β*

which at each point, together with their first derivatives, depend holomorphically on λ. Let $\omega (\lambda )=W(\phi _{\lambda },\chi _{\lambda }),$ be an entire holomorphic function.

This function *ω*(*λ*) plays the role of the characteristic polynomial of *D*. Indeed, the uniqueness of the fundamental eigenfunctions implies that its zeros are precisely the eigenvalues of *D* and that each non-zero eigenspace is one-dimensional. In particular there are at most countably many eigenvalues of *D* and, if there are infinitely many, they must tend to infinity. It turns out that the zeros of *ω*(*λ*) also have mutilplicity one (see below).

If λ is not an eigenvalue of *D* on *H*0, define the Green's function by $G_{\lambda }(x,y)={\begin{cases}\phi _{\lambda }(x)\chi _{\lambda }(y)/\omega (\lambda )&{\text{ for }}x\geq y\\[1ex]\chi _{\lambda }(x)\phi _{\lambda }(y)/\omega (\lambda )&{\text{ for }}y\geq x.\end{cases}}$

This kernel defines an operator on the inner product space *C*[*a*,*b*] via $(G_{\lambda }f)(x)=\int _{a}^{b}G_{\lambda }(x,y)f(y)\,dy.$

Since *G**λ*(*x*,*y*) is continuous on [*a*, *b*] × [*a*, *b*], it defines a Hilbert–Schmidt operator on the Hilbert space completion *H* of *C*[*a*, *b*] = *H*1 (or equivalently of the dense subspace *H*0), taking values in *H*1. This operator carries *H*1 into *H*0. When λ is real, *G**λ*(*x*,*y*) = *G**λ*(*y*,*x*) is also real, so defines a self-adjoint operator on *H*. Moreover,

- *G**λ* (*D* − *λ*) = *I* on *H*0
- *G**λ* carries *H*1 into *H*0, and (*D* − *λ*) *G**λ* = *I* on *H*1.

Thus the operator *G**λ* can be identified with the resolvent (*D* − *λ*)−1.

### Spectral theorem

**Theorem**—The eigenvalues of D are real of multiplicity one and form an increasing sequence *λ*1 < *λ*2 < ⋯ tending to infinity.

The corresponding normalised eigenfunctions form an orthonormal basis of *H*0.

The k-th eigenvalue of *D* is given by the minimax principle $\lambda _{k}=\max _{\dim G=k-1}\,\min _{f\perp G}{(Df,f) \over (f,f)}.$

In particular if *q*1 ≤ *q*2, then $\lambda _{k}(D_{1})\leq \lambda _{k}(D_{2}).$

In fact let *T* = *G**λ* for λ large and negative. Then *T* defines a compact self-adjoint operator on the Hilbert space *H*. By the spectral theorem for compact self-adjoint operators, *H* has an orthonormal basis consisting of eigenvectors *ψ**n* of *T* with *Tψ**n* = *μ**n* *ψ**n*, where *μ**n* tends to zero. The range of *T* contains *H*0 so is dense. Hence 0 is not an eigenvalue of *T*. The resolvent properties of *T* imply that *ψ**n* lies in *H*0 and that $D\psi _{n}=\left(\lambda +{\frac {1}{\mu _{n}}}\right)\psi _{n}$

The minimax principle follows because if $\lambda (G)=\min _{f\perp G}{\frac {(Df,f)}{(f,f)}},$ then *λ*(*G*) = *λ**k* for the linear span of the first *k* − 1 eigenfunctions. For any other (*k* − 1)-dimensional subspace *G*, some *f* in the linear span of the first k eigenvectors must be orthogonal to *G*. Hence *λ*(*G*) ≤ (*Df*,*f*)/(*f*,*f*) ≤ *λ**k*.

### Wronskian as a Fredholm determinant

For simplicity, suppose that *m* ≤ *q*(*x*) ≤ *M* on [0, *π*] with Dirichlet boundary conditions. The minimax principle shows that $n^{2}+m\leq \lambda _{n}(D)\leq n^{2}+M.$

It follows that the resolvent (*D* − *λ*)−1 is a trace-class operator whenever λ is not an eigenvalue of *D* and hence that the Fredholm determinant det I − *μ*(*D* − *λ*)−1 is defined.

The Dirichlet boundary conditions imply that $\omega (\lambda )=\phi _{\lambda }(b).$

Using Picard iteration, Titchmarsh showed that *φ**λ*(*b*), and hence *ω*(*λ*), is an entire function of finite order 1/2: $\omega (\lambda )={\mathcal {O}}\left(e^{\sqrt {|\lambda |}}\right)$

At a zero *μ* of *ω*(*λ*), *φ**μ*(*b*) = 0. Moreover, $\psi (x)=\partial _{\lambda }\varphi _{\lambda }(x)|_{\lambda =\mu }$ satisfies (*D* − *μ*)*ψ* = *φ**μ*. Thus $\omega (\lambda )=(\lambda -\mu )\psi (b)+{\mathcal {O}}((\lambda -\mu )^{2})$

This implies that

μ

is a simple zero of

ω

(

λ

)

.

For otherwise *ψ*(*b*) = 0, so that *ψ* would have to lie in *H*0. But then $(\phi _{\mu },\phi _{\mu })=((D-\mu )\psi ,\phi _{\mu })=(\psi ,(D-\mu )\phi _{\mu })=0,$ a contradiction.

On the other hand, the distribution of the zeros of the entire function ω(λ) is already known from the minimax principle.

By the Hadamard factorization theorem, it follows that $\omega (\lambda )=C\prod (1-\lambda /\lambda _{n}),$ for some non-zero constant *C*.

Hence $\det(I-\mu (D-\lambda )^{-1})=\prod \left(1-{\mu \over \lambda _{n}-\lambda }\right)=\prod {1-(\lambda +\mu )/\lambda _{n} \over 1-\lambda /\lambda _{n}}={\omega (\lambda +\mu ) \over \omega (\lambda )}.$

In particular if 0 is not an eigenvalue of *D* $\omega (\mu )=\omega (0)\cdot \det(I-\mu D^{-1}).$

## Tools from abstract spectral theory

### Functions of bounded variation

A function *ρ*(*x*) of bounded variation on a closed interval [*a*, *b*] is a complex-valued function such that its total variation *V*(*ρ*), the supremum of the variations $\sum _{r=0}^{k-1}|\rho (x_{r+1})-\rho (x_{r})|$ over all dissections $a=x_{0}<x_{1}<\dots <x_{k}=b$ is finite. The real and imaginary parts of *ρ* are real-valued functions of bounded variation. If *ρ* is real-valued and normalised so that *ρ*(*a*) = 0, it has a canonical decomposition as the difference of two bounded non-decreasing functions: $\rho (x)=\rho _{+}(x)-\rho _{-}(x),$ where *ρ*+(*x*) and *ρ*–(*x*) are the total positive and negative variation of *ρ* over [*a*, *x*].

If *f* is a continuous function on [*a*, *b*] its Riemann–Stieltjes integral with respect to *ρ* $\int _{a}^{b}f(x)\,d\rho (x)$ is defined to be the limit of approximating sums $\sum _{r=0}^{k-1}f(x_{r})(\rho (x_{r+1})-\rho (x_{r}))$ as the mesh of the dissection, given by sup |*x**r*+1 − *x**r*|, tends to zero.

This integral satisfies $\left|\int _{a}^{b}f(x)\,d\rho (x)\right|\leq V(\rho )\cdot \|f\|_{\infty }$

and thus defines a bounded linear functional *dρ* on *C*[*a*, *b*] with norm ‖*dρ*‖ = *V*(*ρ*).

Every bounded linear functional *μ* on *C*[*a*, *b*] has an absolute value |μ| defined for non-negative *f* by $|\mu |(f)=\sup _{0\leq |g|\leq f}|\mu (g)|.$

The form |*μ*| extends linearly to a bounded linear form on *C*[*a*, *b*] with norm ‖*μ*‖ and satisfies the characterizing inequality $|\mu (f)|\leq |\mu |(|f|)$ for *f* in *C*[*a*, *b*]. If *μ* is *real*, i.e. is real-valued on real-valued functions, then $\mu =|\mu |-(|\mu |-\mu )\equiv \mu _{+}-\mu _{-}$ gives a canonical decomposition as a difference of *positive* forms, i.e. forms that are non-negative on non-negative functions.

Every positive form *μ* extends uniquely to the linear span of non-negative bounded lower semicontinuous functions *g* by the formula $\mu (g)=\lim \mu (f_{n}),$ where the non-negative continuous functions *f**n* increase pointwise to *g*.

The same therefore applies to an arbitrary bounded linear form *μ*, so that a function *ρ* of bounded variation may be defined by $\rho (x)=\mu (\chi _{[a,x]}),$ where *χ**A* denotes the characteristic function of a subset *A* of [*a*, *b*]. Thus *μ* = *dρ* and ‖*μ*‖ = ‖*dρ*‖. Moreover *μ*+ = *dρ*+ and *μ*– = *dρ*–.

This correspondence between functions of bounded variation and bounded linear forms is a special case of the **Riesz representation theorem**.

The support of *μ* = *dρ* is the complement of all points x in [*a*, *b*] where *ρ* is constant on some neighborhood of x; by definition it is a closed subset *A* of [*a*, *b*]. Moreover, *μ*((1 − *χ**A*)*f*) = 0, so that *μ*(*f*) = 0 if *f* vanishes on *A*.

### Spectral measure

Let *H* be a Hilbert space and T a self-adjoint bounded operator on *H* with $0\leq T\leq I$ , so that the spectrum $\sigma (T)$ of T is contained in $[0,1]$ . If $p(t)$ is a complex polynomial, then by the spectral mapping theorem $\sigma (p(T))=p(\sigma (T))$ and hence $\|p(T)\|\leq \|p\|_{\infty }$ where $\|\cdot \|_{\infty }$ denotes the uniform norm on *C*[0, 1]. By the Weierstrass approximation theorem, polynomials are uniformly dense in *C*[0, 1]. It follows that $f(T)$ can be defined $\forall f\in C[0,1]$ , with $\sigma (f(T))=f(\sigma (T))$ and $\|f(T)\|\leq \|f\|_{\infty }.$

If $0\leq g\leq 1$ is a lower semicontinuous function on [0, 1], for example the characteristic function $\chi _{[0,\alpha ]}$ of a subinterval of [0, 1], then g is a pointwise increasing limit of non-negative $f_{n}\in C[0,1]$ .

If $\xi$ is a vector in *H*, then the vectors $\eta _{n}=f_{n}(T)\xi$ form a Cauchy sequence in *H*, since, for $n\geq m$ , $\|\eta _{n}-\eta _{m}\|^{2}\leq (\eta _{n},\xi )-(\eta _{m},\xi ),$ and $(\eta _{n},\xi )=(f_{n}(T)\xi ,\xi )$ is bounded and increasing, so has a limit.

It follows that $g(T)$ can be defined by $g(T)\xi =\lim f_{n}(T)\xi .$

If $\xi$ and *η* are vectors in *H*, then $\mu _{\xi ,\eta }(f)=(f(T)\xi ,\eta )$ defines a bounded linear form $\mu _{\xi ,\eta }$ on *H*. By the Riesz representation theorem $\mu _{\xi ,\eta }=d\rho _{\xi ,\eta }$ for a unique normalised function $\rho _{\xi ,\eta }$ of bounded variation on [0, 1].

$d\rho _{\xi ,\eta }$ (or sometimes slightly incorrectly $\rho _{\xi ,\eta }$ itself) is called the **spectral measure** determined by $\xi$ and *η*.

The operator $g(T)$ is accordingly uniquely characterised by the equation $(g(T)\xi ,\eta )=\mu _{\xi ,\eta }(g)=\int _{0}^{1}g(\lambda )\,d\rho _{\xi ,\eta }(\lambda ).$

The spectral projection $E(\lambda )$ is defined by $E(\lambda )=\chi _{[0,\lambda ]}(T),$ so that $\rho _{\xi ,\eta }(\lambda )=(E(\lambda )\xi ,\eta ).$

It follows that $g(T)=\int _{0}^{1}g(\lambda )\,dE(\lambda ),$ which is understood in the sense that for any vectors $\xi$ and $\eta$ , $(g(T)\xi ,\eta )=\int _{0}^{1}g(\lambda )\,d(E(\lambda )\xi ,\eta )=\int _{0}^{1}g(\lambda )\,d\rho _{\xi ,\eta }(\lambda ).$

For a single vector $\xi ,\,\mu _{\xi }=\mu _{\xi ,\xi }$ is a positive form on [0, 1] (in other words proportional to a probability measure on [0, 1]) and $\rho _{\xi }=\rho _{\xi ,\xi }$ is non-negative and non-decreasing. Polarisation shows that all the forms $\mu _{\xi ,\eta }$ can naturally be expressed in terms of such positive forms, since $\mu _{\xi ,\eta }={\frac {1}{4}}\left(\mu _{\xi +\eta }+i\mu _{\xi +i\eta }-\mu _{\xi -\eta }-i\mu _{\xi -i\eta }\right)$

If the vector $\xi$ is such that the linear span of the vectors $(T^{n}\xi )$ is dense in *H*, i.e. $\xi$ is a *cyclic vector* for T , then the map U defined by $U(f)=f(T)\xi ,\,C[0,1]\rightarrow H$ satisfies $(Uf_{1},Uf_{2})=\int _{0}^{1}f_{1}(\lambda ){\overline {f_{2}(\lambda )}}\,d\rho _{\xi }(\lambda ).$

Let $L_{2}([0,1],d\rho _{\xi })$ denote the Hilbert space completion of $C[0,1]$ associated with the possibly degenerate inner product on the right hand side. Thus U extends to a unitary transformation of $L_{2}([0,1],\rho _{\xi })$ onto *H*. $UTU^{\ast }$ is then just multiplication by $\lambda$ on $L_{2}([0,1],d\rho _{\xi })$ ; and more generally $Uf(T)U^{\ast }$ is multiplication by $f(\lambda )$ . In this case, the support of $d\rho _{\xi }$ is exactly $\sigma (T)$ , so that

the self-adjoint operator becomes a multiplication operator on the space of functions on its spectrum with inner product given by the spectral measure

.

## Weyl–Titchmarsh–Kodaira theory

The eigenfunction expansion associated with singular differential operators of the form $Df=-(pf')'+qf$ on an open interval (*a*, *b*) requires an initial analysis of the behaviour of the fundamental eigenfunctions near the endpoints *a* and *b* to determine possible boundary conditions there. Unlike the regular Sturm–Liouville case, in some circumstances spectral values of *D* can have multiplicity 2. In the development outlined below standard assumptions will be imposed on *p* and *q* that guarantee that the spectrum of *D* has multiplicity one everywhere and is bounded below. This includes almost all important applications; modifications required for the more general case will be discussed later.

Having chosen the boundary conditions, as in the classical theory the resolvent of *D*, (*D* + *R*)−1 for *R* large and positive, is given by an operator *T* corresponding to a Green's function constructed from two fundamental eigenfunctions. In the classical case *T* was a compact self-adjoint operator; in this case *T* is just a self-adjoint bounded operator with 0 ≤ *T* ≤ *I*. The abstract theory of spectral measure can therefore be applied to *T* to give the eigenfunction expansion for *D*.

The central idea in the proof of Weyl and Kodaira can be explained informally as follows. Assume that the spectrum of *D* lies in [1, ∞) and that *T* = *D*−1 and let $E(\lambda )=\chi _{[\lambda ^{-1},1]}(T)$ be the spectral projection of *D* corresponding to the interval [1, *λ*]. For an arbitrary function *f* define $f(x,\lambda )=(E(\lambda )f)(x).$ *f*(*x*, *λ*) may be regarded as a differentiable map into the space of functions of bounded variation ρ; or equivalently as a differentiable map $x\mapsto (d_{\lambda }f)(x)$ into the Banach space **E** of bounded linear functionals *dρ* on *C*[*α*,*β*] whenever [*α*, *β*] is a compact subinterval of [1, ∞).

Weyl's fundamental observation was that *d**λ* *f* satisfies a second order ordinary differential equation taking values in **E**: $D(d_{\lambda }f)=\lambda \cdot d_{\lambda }f.$

After imposing initial conditions on the first two derivatives at a fixed point *c*, this equation can be solved explicitly in terms of the two fundamental eigenfunctions and the "initial value" functionals $(d_{\lambda }f)(c)=d_{\lambda }f(c,\cdot ),\quad (d_{\lambda }f)^{\prime }(c)=d_{\lambda }f_{x}(c,\cdot ).$

This point of view may now be turned on its head: *f*(*c*, *λ*) and *f**x*(*c*, *λ*) may be written as $f(c,\lambda )=(f,\xi _{1}(\lambda )),\quad f_{x}(c,\lambda )=(f,\xi _{2}(\lambda )),$ where *ξ*1(*λ*) and *ξ*2(*λ*) are given purely in terms of the fundamental eigenfunctions. The functions of bounded variation $\sigma _{ij}(\lambda )=(\xi _{i}(\lambda ),\xi _{j}(\lambda ))$ determine a spectral measure on the spectrum of *D* and can be computed explicitly from the behaviour of the fundamental eigenfunctions (the Titchmarsh–Kodaira formula).

### Limit circle and limit point for singular equations

Let *q*(*x*) be a continuous real-valued function on (0, ∞) and let *D* be the second order differential operator $Df=-f''+qf$ on (0, ∞). Fix a point *c* in (0, ∞) and, for complex λ, let $\varphi _{\lambda },\theta _{\lambda }$ be the unique **fundamental eigenfunctions** of *D* on (0, ∞) satisfying $(D-\lambda )\varphi _{\lambda }=0,\quad (D-\lambda )\theta _{\lambda }=0$ together with the initial conditions at *c* $\varphi _{\lambda }(c)=1,\,\varphi _{\lambda }'(c)=0,\,\theta _{\lambda }(c)=0,\,\theta _{\lambda }'(c)=1.$

Then their Wronskian satisfies $W(\varphi _{\lambda },\theta _{\lambda })=\varphi _{\lambda }\theta _{\lambda }'-\theta _{\lambda }\varphi _{\lambda }'\equiv 1,$

since it is constant and equal to 1 at *c*.

Let λ be non-real and 0 < *x* < ∞. If the complex number $\mu$ is such that $f=\varphi +\mu \theta$ satisfies the boundary condition $\cos \beta \,f(x)-\sin \beta \,f'(x)=0$ for some $\beta$ (or, equivalently, $f'(x)/f(x)$ is real) then, using integration by parts, one obtains $\operatorname {Im} (\lambda )\int _{c}^{x}|\varphi +\mu \theta |^{2}=\operatorname {Im} (\mu ).$

Therefore, the set of *μ* satisfying this equation is not empty. This set is a circle in the complex *μ*-plane. Points *μ* in its interior are characterized by $\int _{c}^{x}|\varphi +\mu \theta |^{2}<{\operatorname {Im} (\mu ) \over \operatorname {Im} (\lambda )}$ if *x* > *c* and by $\int _{x}^{c}|\varphi +\mu \theta |^{2}<{\operatorname {Im} (\mu ) \over \operatorname {Im} (\lambda )}$ if *x* < *c*.

Let *D**x* be the closed disc enclosed by the circle. By definition these closed discs are nested and decrease as *x* approaches 0 or ∞. So in the limit, the circles tend either to a **limit circle** or a **limit point** at each end. If $\mu$ is a limit point or a point on the limit circle at 0 or ∞, then $f=\varphi +\mu \theta$ is square integrable (*L*2) near 0 or ∞, since $\mu$ lies in *D**x* for all *x* > *c* (in the ∞ case) and so $\int _{c}^{x}|\varphi +\mu \theta |^{2}<{\operatorname {Im} (\mu ) \over \operatorname {Im} (\lambda )}$ is bounded independent of x. In particular:

- there are always non-zero solutions of *Df* = *λf* which are square integrable near 0 resp. ∞;
- in the limit circle case all solutions of *Df* = *λf* are square integrable near 0 resp. ∞.

The radius of the disc *D**x* can be calculated to be $\left|{1 \over {2\operatorname {Im} (\lambda )\int _{c}^{x}|\theta |^{2}}}\right|$ and this implies that in the limit point case $\theta$ cannot be square integrable near 0 resp. ∞. Therefore, we have a converse to the second statement above:

- in the limit point case there is exactly one non-zero solution (up to scalar multiples) of Df = λf which is square integrable near 0 resp. ∞.

On the other hand, if *Dg* = *λ*′ *g* for another value *λ*′, then $h(x)=g(x)-(\lambda ^{\prime }-\lambda )\int _{c}^{x}(\varphi _{\lambda }(x)\theta _{\lambda }(y)-\theta _{\lambda }(x)\varphi _{\lambda }(y))g(y)\,dy$ satisfies *Dh* = *λh*, so that $g(x)=c_{1}\varphi _{\lambda }+c_{2}\theta _{\lambda }+(\lambda ^{\prime }-\lambda )\int _{c}^{x}(\varphi _{\lambda }(x)\theta _{\lambda }(y)-\theta _{\lambda }(x)\varphi _{\lambda }(y))g(y)\,dy.$

This formula may also be obtained directly by the variation of constant method from (*D* − *λ*)*g* = (*λ*′ − *λ*)*g*. Using this to estimate *g*, it follows that

- the limit point/limit circle behaviour at 0 or ∞ is independent of the choice of *λ*.

More generally if *Dg* = (*λ* – *r*) *g* for some function *r*(*x*), then $g(x)=c_{1}\varphi _{\lambda }+c_{2}\theta _{\lambda }-\int _{c}^{x}(\varphi _{\lambda }(x)\theta _{\lambda }(y)-\theta _{\lambda }(x)\varphi _{\lambda }(y))r(y)g(y)\,dy.$

From this it follows that

- if *r* is continuous at 0, then *D* + *r* is limit point or limit circle at 0 precisely when *D* is,

so that in particular

- if *q*(*x*) − *a*/*x*2 is continuous at 0, then *D* is limit point at 0 if and only if *a* ≥ ⁠3/4⁠.

Similarly

- if *r* has a finite limit at ∞, then *D* + *r* is limit point or limit circle at ∞ precisely when D is,

so that in particular

- if *q* has a finite limit at ∞, then D is limit point at ∞.

Many more elaborate criteria to be limit point or limit circle can be found in the mathematical literature.

### Green's function (singular case)

Consider the differential operator $D_{0}f=-(p_{0}f')'+q_{0}f$ on (0, ∞) with *q*0 positive and continuous on (0, ∞) and *p*0 continuously differentiable in [0, ∞), positive in (0, ∞) and *p*0(0) = 0.

Moreover, assume that after reduction to standard form *D*0 becomes the equivalent operator $Df=-f''+qf$ on (0, ∞) where *q* has a finite limit at ∞. Thus

- *D* is limit point at ∞.

At 0, *D* may be either limit circle or limit point. In either case there is an eigenfunction Φ0 with *D*Φ0 = 0 and Φ0 square integrable near 0. In the limit circle case, Φ0 determines a **boundary condition** at 0: $W(f,\Phi _{0})(0)=0.$

For complex λ, let Φ*λ* and Χ*λ* satisfy

- (*D* – *λ*)Φ*λ* = 0, (*D* – *λ*)Χ*λ* = 0
- Χ*λ* square integrable near infinity
- Φ*λ* square integrable at 0 if 0 is *limit point*
- Φ*λ* satisfies the boundary condition above if 0 is *limit circle*.

Let $\omega (\lambda )=W(\Phi _{\lambda },\mathrm {X} _{\lambda }),$ a constant which vanishes precisely when Φ*λ* and Χ*λ* are proportional, i.e. λ is an eigenvalue of *D* for these boundary conditions.

On the other hand, this cannot occur if Im *λ* ≠ 0 or if λ is negative.

Indeed, if *D f* = *λf* with *q*0 – *λ* ≥ *δ* > 0, then by Green's formula (*Df*,*f*) = (*f*,*Df*), since *W*(*f*,*f**) is constant. So λ must be real. If *f* is taken to be real-valued in the *D*0 realization, then for 0 < *x* < *y* $[p_{0}ff']_{x}^{y}=\int _{x}^{y}(q_{0}-\lambda )|f|^{2}+p_{0}(f')^{2}.$

Since *p*0(0) = 0 and *f* is integrable near 0, *p*0*f* *f*′ must vanish at 0. Setting *x* = 0, it follows that *f*(*y*) *f*′(*y*) > 0, so that *f*2 is increasing, contradicting the square integrability of *f* near ∞.

Thus, adding a positive scalar to *q*, it may be assumed that $\omega (\lambda )\neq 0~~{\text{ if }}\lambda \notin [1,\infty ).$

If *ω*(*λ*) ≠ 0, the **Green's function** *G**λ*(*x*,*y*) at λ is defined by $G_{\lambda }(x,y)={\begin{cases}\Phi _{\lambda }(x)\mathrm {X} _{\lambda }(y)/\omega (\lambda )&(x\leq y),\\[1ex]\mathrm {X} _{\lambda }(x)\Phi _{\lambda }(y)/\omega (\lambda )&(x\geq y).\end{cases}}$ and is independent of the choice of Φ*λ* and Χ*λ*.

In the examples there will be a third "bad" eigenfunction Ψ*λ* defined and holomorphic for λ not in [1, ∞) such that Ψ*λ* satisfies the boundary conditions at neither 0 nor ∞. This means that for λ not in [1, ∞)

- *W*(Φ*λ*,Ψ*λ*) is nowhere vanishing;
- *W*(Χ*λ*,Ψ*λ*) is nowhere vanishing.

In this case Χ*λ* is proportional to Φ*λ* + *m*(*λ*) Ψ*λ*, where $m(\lambda )=-W(\Phi _{\lambda },\mathrm {X} _{\lambda })/W(\Psi _{\lambda },\mathrm {X} _{\lambda }).$

Let *H*1 be the space of square integrable continuous functions on (0, ∞) and let *H*0 be

- the space of *C*2 functions *f* on (0, ∞) of compact support if *D* is limit point at 0
- the space of *C*2 functions *f* on (0, ∞) with *W*(*f*, Φ0) = 0 at 0 and with *f* = 0 near ∞ if *D* is limit circle at 0.

Define *T* = *G*0 by $(Tf)(x)=\int _{0}^{\infty }G_{0}(x,y)f(y)\,dy.$

Then *T* *D* = *I* on *H*0, *D* *T* = *I* on *H*1 and the operator *D* is bounded below on *H*0: $(Df,f)\geq (f,f).$

Thus *T* is a self-adjoint bounded operator with 0 ≤ *T* ≤ *I*.

Formally *T* = *D*−1. The corresponding operators *G**λ* defined for λ not in [1, ∞) can be formally identified with $(D-\lambda )^{-1}=T(I-\lambda T)^{-1}$ and satisfy *G**λ* (*D* – *λ*) = *I* on *H*0, (*D* – *λ*)*G**λ* = *I* on *H*1.

### Spectral theorem and Titchmarsh–Kodaira formula

**Theorem.**—For every real number λ let *ρ*(*λ*) be defined by the **Titchmarsh–Kodaira formula**: $\rho (\lambda )=\lim _{\delta \downarrow 0}\lim _{\varepsilon \downarrow 0}{\frac {1}{\pi }}\int _{\delta }^{\lambda +\delta }\operatorname {Im} m(t+i\varepsilon )\,dt.$

Then *ρ*(*λ*) is a lower semicontinuous non-decreasing function of λ and if $(Uf)(\lambda )=\int _{0}^{\infty }f(x)\Phi (x,\lambda )\,dx,$ then *U* defines a unitary transformation of *L*2(0, ∞) onto *L*2([1,∞), *dρ*) such that *UDU*−1 corresponds to multiplication by λ.

The inverse transformation *U*−1 is given by $(U^{-1}g)(x)=\int _{1}^{\infty }g(\lambda )\Phi (x,\lambda )\,d\rho (\lambda ).$

The spectrum of *D* equals the support of *dρ*.

Kodaira gave a streamlined version of Weyl's original proof. (M.H. Stone had previously shown how part of Weyl's work could be simplified using von Neumann's spectral theorem.)

In fact for *T* =*D*−1 with 0 ≤ *T* ≤ *I*, the spectral projection *E*(*λ*) of *T* is defined by $E(\lambda )=\chi _{[\lambda ^{-1},1]}(T)$

It is also the spectral projection of *D* corresponding to the interval [1, *λ*].

For *f* in *H*1 define $f(x,\lambda )=(E(\lambda )f)(x).$

*f*(*x*, *λ*) may be regarded as a differentiable map into the space of functions *ρ* of bounded variation; or equivalently as a differentiable map $x\mapsto (d_{\lambda }f)(x)$ into the Banach space **E** of bounded linear functionals *dρ* on [*C*[*α*, *β*]] for any compact subinterval [*α*, *β*] of [1, ∞).

The functionals (or measures) *d**λ* *f*(*x*) satisfies the following **E**-valued second order ordinary differential equation: $D(d_{\lambda }f)=\lambda \cdot d_{\lambda }f,$ with initial conditions at *c* in (0, ∞) $(d_{\lambda }f)(c)=d_{\lambda }f(c,\cdot )=\mu ^{(0)},\quad (d_{\lambda }f)^{\prime }(c)=d_{\lambda }f_{x}(c,\cdot )=\mu ^{(1)}.$

If *φ**λ* and *χ**λ* are the special eigenfunctions adapted to *c*, then $d_{\lambda }f(x)=\varphi _{\lambda }(x)\mu ^{(0)}+\chi _{\lambda }(x)\mu ^{(1)}.$

Moreover, $\mu ^{(k)}=d_{\lambda }(f,\xi _{\lambda }^{(k)}),$ where $\xi _{\lambda }^{(k)}=DE(\lambda )\eta ^{(k)},$ with $\eta _{z}^{(0)}(y)=G_{z}(c,y),\,\,\,\,\eta _{z}^{(1)}(x)=\partial _{x}G_{z}(c,y),\,\,\,\,(z\notin [1,\infty )).$ (As the notation suggests, *ξ**λ*(0) and *ξ**λ*(1) do not depend on the choice of z.)

Setting $\sigma _{ij}(\lambda )=(\xi _{\lambda }^{(i)},\xi _{\lambda }^{(j)}),$ it follows that $d_{\lambda }(E(\lambda )\eta _{z}^{(i)},\eta _{z}^{(j)})=|\lambda -z|^{-2}\cdot d_{\lambda }\sigma _{ij}(\lambda ).$

On the other hand, there are holomorphic functions *a*(*λ*), *b*(*λ*) such that

- *φ**λ* + *a*(*λ*) *χ**λ* is proportional to Φ*λ*;
- *φ**λ* + *b*(*λ*) *χ**λ* is proportional to Χ*λ*.

Since *W*(*φ**λ*, *χ**λ*) = 1, the Green's function is given by $G_{\lambda }(x,y)={\begin{cases}{\dfrac {(\varphi _{\lambda }(x)+a(\lambda )\chi _{\lambda }(x))(\varphi _{\lambda }(y)+b(\lambda )\chi _{\lambda }(y))}{b(\lambda )-a(\lambda )}}&(x\leq y),\\[1ex]{\dfrac {(\varphi _{\lambda }(x)+b(\lambda )\chi _{\lambda }(x))(\varphi _{\lambda }(y)+a(\lambda )\chi _{\lambda }(y))}{b(\lambda )-a(\lambda )}}&(y\leq x).\end{cases}}$

Direct calculation shows that $(\eta _{z}^{(i)},\eta _{z}^{(j)})=\operatorname {Im} M_{ij}(z)/\operatorname {Im} z,$ where the so-called ***characteristic matrix*** *M**ij*(*z*) is given by $M_{00}(z)={\frac {a(z)b(z)}{a(z)-b(z)}},\,\,M_{01}(z)=M_{10}(z)={\frac {a(z)+b(z)}{2(a(z)-b(z))}},\,\,M_{11}(z)={\frac {1}{a(z)-b(z)}}.$

Hence $\int _{-\infty }^{\infty }(\operatorname {Im} z)\cdot |\lambda -z|^{-2}\,d\sigma _{ij}(\lambda )=\operatorname {Im} M_{ij}(z),$ which immediately implies $\sigma _{ij}(\lambda )=\lim _{\delta \downarrow 0}\lim _{\varepsilon \downarrow 0}\int _{\delta }^{\lambda +\delta }\operatorname {Im} M_{ij}(t+i\varepsilon )\,dt.$ (This is a special case of the "Stieltjes inversion formula".)

Setting *ψ**λ*(0) = *φ**λ* and *ψ**λ*(1) = *χ**λ*, it follows that $(E(\mu )f)(x)=\sum _{i.j}\int _{0}^{\mu }\int _{0}^{\infty }\psi _{\lambda }^{(i)}(x)\psi _{\lambda }^{(j)}(y)f(y)\,dy\,d\sigma _{ij}(\lambda )=\int _{0}^{\mu }\int _{0}^{\infty }\Phi _{\lambda }(x)\Phi _{\lambda }(y)f(y)\,dy\,d\rho (\lambda ).$

This identity is equivalent to the spectral theorem and Titchmarsh–Kodaira formula.

## Application to the hypergeometric equation

The **Mehler–Fock transform** concerns the eigenfunction expansion associated with the Legendre differential operator *D* $Df=-((x^{2}-1)f')'=-(x^{2}-1)f''-2xf'$ on (1, ∞). The eigenfunctions are the Legendre functions $P_{-1/2+i{\sqrt {\lambda }}}(\cosh r)={1 \over 2\pi }\int _{0}^{2\pi }\left({\sin \theta +ie^{-r}\cos \theta \over \cos \theta -ie^{-r}\sin \theta }\right)^{{1 \over 2}+i{\sqrt {\lambda }}}\,d\theta$ with eigenvalue *λ* ≥ 0. The two Mehler–Fock transformations are $Uf(\lambda )=\int _{1}^{\infty }f(x)\,P_{-1/2+i{\sqrt {\lambda }}}(x)\,dx$ and $U^{-1}g(x)=\int _{0}^{\infty }g(\lambda )\,{1 \over 2}\tanh \pi {\sqrt {\lambda }}\,d\lambda .$

(Often this is written in terms of the variable τ = √λ.)

Mehler and Fock studied this differential operator because it arose as the radial component of the Laplacian on 2-dimensional hyperbolic space. More generally, consider the group *G* = SU(1,1) consisting of complex matrices of the form ${\begin{bmatrix}\alpha &\beta \\{\overline {\beta }}&{\overline {\alpha }}\end{bmatrix}}$

with determinant |*α*|2 − |*β*|2 = 1.

## Application to the hydrogen atom

## Generalisations and alternative approaches

A Weyl function can be defined at a singular endpoint *a* giving rise to a singular version of Weyl–Titchmarsh–Kodaira theory. this applies for example to the case of radial Schrödinger operators $Df=-f''+{\frac {\ell (\ell +1)}{x^{2}}}f+V(x)f,\qquad x\in (0,\infty )$

The whole theory can also be extended to the case where the coefficients are allowed to be measures.

## Gelfand–Levitan theory
