---
title: "Spectrum (functional analysis)"
source: https://en.wikipedia.org/wiki/Spectrum_(functional_analysis)
domain: spectral-theory
license: CC-BY-SA-4.0
tags: spectral theory, spectral theorem, self-adjoint operator, sturm-liouville theory
fetched: 2026-07-02
---

# Spectrum (functional analysis)

In mathematics, particularly in functional analysis, the **spectrum** of a bounded linear operator (or, more generally, an unbounded linear operator) is a generalisation of the set of eigenvalues of a matrix. Specifically, a complex number $\lambda$ is said to be in the spectrum of a bounded linear operator T if $T-\lambda I$

- either has *no* set-theoretic inverse;
- or the set-theoretic inverse is either unbounded or defined on a non-dense subset.

Here, I is the identity operator.

By the closed graph theorem, $\lambda$ is in the spectrum if and only if the bounded operator $T-\lambda I:V\to V$ is non-bijective on V .

The study of spectra and related properties is known as *spectral theory*, which has numerous applications, most notably the mathematical formulation of quantum mechanics.

The spectrum of an operator on a finite-dimensional vector space is precisely the set of eigenvalues. However an operator on an infinite-dimensional space may have additional elements in its spectrum, and may have no eigenvalues. For example, consider the right shift operator *R* on the Hilbert space ℓ2,

$(x_{1},x_{2},\dots )\mapsto (0,x_{1},x_{2},\dots ).$

This has no eigenvalues, since if *Rx*=*λx* then by expanding this expression we see that *x*1=0, *x*2=0, etc. On the other hand, 0 is in the spectrum because although the operator *R* − 0 (i.e. *R* itself) is invertible, the inverse is defined on a set which is not dense in ℓ2. In fact *every* bounded linear operator on a complex Banach space must have a non-empty spectrum.

The notion of spectrum extends to unbounded (i.e. not necessarily bounded) operators. A complex number *λ* is said to be in the spectrum of an unbounded operator $T:\,X\to X$ defined on domain $D(T)\subseteq X$ if there is no bounded inverse $(T-\lambda I)^{-1}:\,X\to D(T)$ defined on the whole of $X.$ If *T* is closed (which includes the case when *T* is bounded), boundedness of $(T-\lambda I)^{-1}$ follows automatically from its existence.

The space of bounded linear operators *B*(*X*) on a Banach space *X* is an example of a unital Banach algebra. Since the definition of the spectrum does not mention any properties of *B*(*X*) except those that any such algebra has, the notion of a spectrum may be generalised to this context by using the same definition verbatim.

## Spectrum of a bounded operator

### Definition

Let T be a bounded linear operator acting on a Banach space X over the complex scalar field $\mathbb {C}$ , and I be the identity operator on X . The **spectrum** of T is the set of all $\lambda \in \mathbb {C}$ for which the operator $T-\lambda I$ does not have an inverse that is a bounded linear operator.

Since $T-\lambda I$ is a linear operator, the inverse is linear if it exists; and, by the bounded inverse theorem, it is bounded. Therefore, the spectrum consists precisely of those scalars $\lambda$ for which $T-\lambda I$ is not bijective.

The spectrum of a given operator T is often denoted $\sigma (T)$ , and its complement, the resolvent set, is denoted $\rho (T)=\mathbb {C} \setminus \sigma (T)$ . ( $\rho (T)$ is sometimes used to denote the spectral radius of T )

### Relation to eigenvalues

If $\lambda$ is an eigenvalue of T , then the operator $T-\lambda I$ is not one-to-one, and therefore its inverse $(T-\lambda I)^{-1}$ is not defined. However, the converse statement is not true: the operator $T-\lambda I$ may not have an inverse, even if $\lambda$ is not an eigenvalue. Thus the spectrum of an operator always contains all its eigenvalues, but is not limited to them.

For example, consider the Hilbert space $\ell ^{2}(\mathbb {Z} )$ , that consists of all bi-infinite sequences of real numbers

$v=(\ldots ,v_{-2},v_{-1},v_{0},v_{1},v_{2},\ldots )$

that have a finite sum of squares ${\textstyle \sum _{i=-\infty }^{+\infty }v_{i}^{2}}$ . The bilateral shift operator T simply displaces every element of the sequence by one position; namely if $u=T(v)$ then $u_{i}=v_{i-1}$ for every integer i . The eigenvalue equation $T(v)=\lambda v$ has no nonzero solution in this space, since it implies that all the values $v_{i}$ have the same absolute value (if $\vert \lambda \vert =1$ ) or are a geometric progression (if $\vert \lambda \vert \neq 1$ ); either way, the sum of their squares would not be finite. However, the operator $T-\lambda I$ is not invertible if $|\lambda |=1$ . For example, the sequence u such that $u_{i}=1/(|i|+1)$ is in $\ell ^{2}(\mathbb {Z} )$ ; but there is no sequence v in $\ell ^{2}(\mathbb {Z} )$ such that $(T-I)v=u$ (that is, $v_{i-1}=u_{i}+v_{i}$ for all i ).

### Basic properties

The spectrum of a bounded operator T is always a closed, bounded subset of the complex plane.

If the spectrum were empty, then the *resolvent function*

$R(\lambda )=(T-\lambda I)^{-1},\qquad \lambda \in \mathbb {C} ,$

would be defined everywhere on the complex plane and bounded. But it can be shown that the resolvent function R is holomorphic on its domain. By the vector-valued version of Liouville's theorem, this function is constant, thus everywhere zero as it is zero at infinity. This would be a contradiction.

The boundedness of the spectrum follows from the Neumann series expansion in $\lambda$ ; the spectrum $\sigma (T)$ is bounded by $\left\|T\right\|$ . A similar result shows the closedness of the spectrum.

The bound $\left\|T\right\|$ on the spectrum can be refined somewhat. The *spectral radius*, $r(T)$ , of T is the radius of the smallest circle in the complex plane which is centered at the origin and contains the spectrum $\sigma (T)$ inside of it, i.e.

$r(T)=\sup\{|\lambda |:\lambda \in \sigma (T)\}.$

The **spectral radius formula** says that for any element T of a Banach algebra,

$r(T)=\lim _{n\to \infty }\left\|T^{n}\right\|^{1/n}.$

## Spectrum of an unbounded operator

One can extend the definition of spectrum to unbounded operators on a Banach space *X*. These operators are no longer elements in the Banach algebra *B*(*X*).

### Definition

Let *X* be a Banach space and $T:\,D(T)\to X$ be a linear operator defined on domain $D(T)\subseteq X$ . A complex number *λ* is said to be in the **resolvent set** (also called **regular set**) of T if the operator

$T-\lambda I:\,D(T)\to X$

has a bounded everywhere-defined inverse, i.e. if there exists a bounded operator

$S:\,X\rightarrow D(T)$

such that

$S(T-\lambda I)=I_{D(T)},\,(T-\lambda I)S=I_{X}.$

A complex number *λ* is then in the **spectrum** if *λ* is not in the resolvent set.

For *λ* to be in the resolvent (i.e. not in the spectrum), just like in the bounded case, $T-\lambda I$ must be bijective, since it must have a two-sided inverse. As before, if an inverse exists, then its linearity is immediate, but in general it may not be bounded, so this condition must be checked separately.

By the closed graph theorem, boundedness of $(T-\lambda I)^{-1}$ *does* follow directly from its existence when *T* is closed. Then, just as in the bounded case, a complex number *λ* lies in the spectrum of a closed operator *T* if and only if $T-\lambda I$ is not bijective. Note that the class of closed operators includes all bounded operators.

### Basic properties

The spectrum of an unbounded operator is in general a closed, possibly empty, subset of the complex plane. If the operator *T* is not closed, then $\sigma (T)=\mathbb {C}$ .

The following example indicates that non-closed operators may have empty spectra. Let T denote the differentiation operator on $L^{2}([0,1])$ , whose domain is defined to be the closure of $C_{c}^{\infty }((0,1])$ with respect to the $H^{1}$ -Sobolev space norm. This space can be characterized as all functions in $H^{1}([0,1])$ that are zero at $t=0$ . Then, $T-z$ has trivial kernel on this domain, as any $H^{1}([0,1])$ -function in its kernel is a constant multiple of $e^{zt}$ , which is zero at $t=0$ if and only if it is identically zero. Therefore, the complement of the spectrum is all of $\mathbb {C} .$

## Classification of points in the spectrum

A bounded operator *T* on a Banach space is invertible, i.e. has a bounded inverse, if and only if *T* is bounded below, i.e. $\|Tx\|\geq c\|x\|,$ for some $c>0,$ and has dense range. Accordingly, the spectrum of *T* can be divided into the following parts:

1. $\lambda \in \sigma (T)$ if $T-\lambda I$ is not bounded below. In particular, this is the case if $T-\lambda I$ is not injective, that is, *λ* is an eigenvalue. The set of eigenvalues is called the **point spectrum** of *T* and denoted by *σ*p(*T*). Alternatively, $T-\lambda I$ could be one-to-one but still not bounded below. Such *λ* is not an eigenvalue but still an *approximate eigenvalue* of *T* (eigenvalues themselves are also approximate eigenvalues). The set of approximate eigenvalues (which includes the point spectrum) is called the **approximate point spectrum** of *T*, denoted by *σ*ap(*T*).
2. $\lambda \in \sigma (T)$ if $T-\lambda I$ does not have dense range. The set of such *λ* is called the **compression spectrum** of *T*, denoted by $\sigma _{\mathrm {cp} }(T)$ . If $T-\lambda I$ does not have dense range but is injective, *λ* is said to be in the **residual spectrum** of *T*, denoted by $\sigma _{\mathrm {r} }(T)$ .

Note that the approximate point spectrum and residual spectrum are not necessarily disjoint (however, the point spectrum and the residual spectrum are).

The following subsections provide more details on the three parts of *σ*(*T*) sketched above.

### Point spectrum

If an operator is not injective (so there is some nonzero *x* with *T*(*x*) = 0), then it is clearly not invertible. So if *λ* is an eigenvalue of *T*, one necessarily has *λ* ∈ *σ*(*T*). The set of eigenvalues of *T* is also called the **point spectrum** of *T*, denoted by *σ*p(*T*). Some authors refer to the closure of the point spectrum as the **pure point spectrum** $\sigma _{pp}(T)={\overline {\sigma _{p}(T)}}$ while others simply consider $\sigma _{pp}(T):=\sigma _{p}(T).$

### Approximate point spectrum

More generally, by the bounded inverse theorem, *T* is not invertible if it is not bounded below; that is, if there is no *c* > 0 such that ||*Tx*|| ≥ *c*||*x*|| for all *x* ∈ *X*. So the spectrum includes the set of **approximate eigenvalues**, which are those *λ* such that *T* - *λI* is not bounded below; equivalently, it is the set of *λ* for which there is a sequence of unit vectors *x*1, *x*2, ... for which

$\lim _{n\to \infty }\|Tx_{n}-\lambda x_{n}\|=0$

.

The set of approximate eigenvalues is known as the **approximate point spectrum**, denoted by $\sigma _{\mathrm {ap} }(T)$ .

It is easy to see that the eigenvalues lie in the approximate point spectrum.

For example, consider the bilateral shift *W* on $l^{2}(\mathbb {Z} )$ defined by

$W:\,e_{j}\mapsto e_{j+1},\quad j\in \mathbb {Z} ,$

where ${\big (}e_{j}{\big )}_{j\in \mathbb {N} }$ is the standard orthonormal basis in $l^{2}(\mathbb {Z} )$ . Direct calculation shows *W* has no eigenvalues, but every *λ* with $|\lambda |=1$ is an approximate eigenvalue; letting *x**n* be the vector

${\frac {1}{\sqrt {n}}}(\dots ,0,1,\lambda ^{-1},\lambda ^{-2},\dots ,\lambda ^{1-n},0,\dots )$

one can see that ||*x**n*|| = 1 for all *n*, but

$\|Wx_{n}-\lambda x_{n}\|={\sqrt {\frac {2}{n}}}\to 0.$

Since *W* is a unitary operator, its spectrum lies on the unit circle. Therefore, the approximate point spectrum of *W* is its entire spectrum.

This conclusion is also true for a more general class of operators. A unitary operator is normal. By the spectral theorem, a bounded operator on a Hilbert space H is normal if and only if it is equivalent (after identification of *H* with an $L^{2}$ space) to a multiplication operator. It can be shown that the approximate point spectrum of a bounded multiplication operator equals its spectrum.

### Discrete spectrum

The discrete spectrum is defined as the set of normal eigenvalues or, equivalently, as the set of isolated points of the spectrum such that the corresponding Riesz projector is of finite rank. As such, the discrete spectrum is a strict subset of the point spectrum, i.e., $\sigma _{d}(T)\subset \sigma _{p}(T).$

### Continuous spectrum

The set of all *λ* for which $T-\lambda I$ is injective and has dense range, but is not surjective, is called the **continuous spectrum** of *T*, denoted by $\sigma _{\mathbb {c} }(T)$ . The continuous spectrum therefore consists of those approximate eigenvalues which are not eigenvalues and do not lie in the residual spectrum. That is,

$\sigma _{\mathrm {c} }(T)=\sigma _{\mathrm {ap} }(T)\setminus (\sigma _{\mathrm {r} }(T)\cup \sigma _{\mathrm {p} }(T))$

.

For example, $A:\,l^{2}(\mathbb {N} )\to l^{2}(\mathbb {N} )$ , $e_{j}\mapsto e_{j}/j$ , $j\in \mathbb {N}$ , is injective and has a dense range, yet $\mathrm {Ran} (A)\subsetneq l^{2}(\mathbb {N} )$ . Indeed, if ${\textstyle x=\sum _{j\in \mathbb {N} }c_{j}e_{j}\in l^{2}(\mathbb {N} )}$ with $c_{j}\in \mathbb {C}$ such that ${\textstyle \sum _{j\in \mathbb {N} }|c_{j}|^{2}<\infty }$ , one does not necessarily have ${\textstyle \sum _{j\in \mathbb {N} }\left|jc_{j}\right|^{2}<\infty }$ , and then ${\textstyle \sum _{j\in \mathbb {N} }jc_{j}e_{j}\notin l^{2}(\mathbb {N} )}$ .

### Compression spectrum

The set of $\lambda \in \mathbb {C}$ for which $T-\lambda I$ does not have dense range is known as the **compression spectrum** of *T* and is denoted by $\sigma _{\mathrm {cp} }(T)$ .

### Residual spectrum

The set of $\lambda \in \mathbb {C}$ for which $T-\lambda I$ is injective but does not have dense range is known as the **residual spectrum** of *T* and is denoted by $\sigma _{\mathrm {r} }(T)$ :

$\sigma _{\mathrm {r} }(T)=\sigma _{\mathrm {cp} }(T)\setminus \sigma _{\mathrm {p} }(T).$

An operator may be injective, even bounded below, but still not invertible. The right shift on $l^{2}(\mathbb {N} )$ , $R:\,l^{2}(\mathbb {N} )\to l^{2}(\mathbb {N} )$ , $R:\,e_{j}\mapsto e_{j+1},\,j\in \mathbb {N}$ , is such an example. This shift operator is an isometry, therefore bounded below by 1. But it is not invertible as it is not surjective ( $e_{1}\not \in \mathrm {Ran} (R)$ ), and moreover $\mathrm {Ran} (R)$ is not dense in $l^{2}(\mathbb {N} )$ ( $e_{1}\notin {\overline {\mathrm {Ran} (R)}}$ ).

### Peripheral spectrum

The peripheral spectrum of an operator is defined as the set of points in its spectrum which have modulus equal to its spectral radius.

### Essential spectrum

There are five similar definitions of the essential spectrum of closed densely defined linear operator $A:\,X\to X$ which satisfy

$\sigma _{\mathrm {ess} ,1}(A)\subset \sigma _{\mathrm {ess} ,2}(A)\subset \sigma _{\mathrm {ess} ,3}(A)\subset \sigma _{\mathrm {ess} ,4}(A)\subset \sigma _{\mathrm {ess} ,5}(A)\subset \sigma (A).$

All these spectra $\sigma _{\mathrm {ess} ,k}(A),\ 1\leq k\leq 5$ , coincide in the case of self-adjoint operators.

1. The essential spectrum $\sigma _{\mathrm {ess} ,1}(A)$ is defined as the set of points $\lambda$ of the spectrum such that $A-\lambda I$ is not semi-Fredholm. (The operator is *semi-Fredholm* if its range is closed and either its kernel or cokernel (or both) is finite-dimensional.) **Example 1:** $\lambda =0\in \sigma _{\mathrm {ess} ,1}(A)$ for the operator $A:\,l^{2}(\mathbb {N} )\to l^{2}(\mathbb {N} )$ , $A:\,e_{j}\mapsto e_{j}/j,~j\in \mathbb {N}$ (because the range of this operator is not closed: the range does not include all of $l^{2}(\mathbb {N} )$ although its closure does). **Example 2:** $\lambda =0\in \sigma _{\mathrm {ess} ,1}(N)$ for $N:\,l^{2}(\mathbb {N} )\to l^{2}(\mathbb {N} )$ , $N:\,v\mapsto 0$ for any $v\in l^{2}(\mathbb {N} )$ (because both kernel and cokernel of this operator are infinite-dimensional).
2. The essential spectrum $\sigma _{\mathrm {ess} ,2}(A)$ is defined as the set of points $\lambda$ of the spectrum such that the operator either $A-\lambda I$ has infinite-dimensional kernel or has a range which is not closed. It can also be characterized in terms of *Weyl's criterion*: there exists a sequence $(x_{j})_{j\in \mathbb {N} }$ in the space *X* such that $\Vert x_{j}\Vert =1$ , ${\textstyle \lim _{j\to \infty }\left\|(A-\lambda I)x_{j}\right\|=0,}$ and such that $(x_{j})_{j\in \mathbb {N} }$ contains no convergent subsequence. Such a sequence is called a *singular sequence* (or a *singular Weyl sequence*). **Example:** $\lambda =0\in \sigma _{\mathrm {ess} ,2}(B)$ for the operator $B:\,l^{2}(\mathbb {N} )\to l^{2}(\mathbb {N} )$ , $B:\,e_{j}\mapsto e_{j/2}$ if *j* is even and $e_{j}\mapsto 0$ when *j* is odd (kernel is infinite-dimensional; cokernel is zero-dimensional). Note that $\lambda =0\not \in \sigma _{\mathrm {ess} ,1}(B)$ .
3. The essential spectrum $\sigma _{\mathrm {ess} ,3}(A)$ is defined as the set of points $\lambda$ of the spectrum such that $A-\lambda I$ is not Fredholm. (The operator is *Fredholm* if its range is closed and both its kernel and cokernel are finite-dimensional.) **Example:** $\lambda =0\in \sigma _{\mathrm {ess} ,3}(J)$ for the operator $J:\,l^{2}(\mathbb {N} )\to l^{2}(\mathbb {N} )$ , $J:\,e_{j}\mapsto e_{2j}$ (kernel is zero-dimensional, cokernel is infinite-dimensional). Note that $\lambda =0\not \in \sigma _{\mathrm {ess} ,2}(J)$ .
4. The essential spectrum $\sigma _{\mathrm {ess} ,4}(A)$ is defined as the set of points $\lambda$ of the spectrum such that $A-\lambda I$ is not Fredholm of index zero. It could also be characterized as the largest part of the spectrum of *A* which is preserved by compact perturbations. In other words, ${\textstyle \sigma _{\mathrm {ess} ,4}(A)=\bigcap _{K\in B_{0}(X)}\sigma (A+K)}$ ; here $B_{0}(X)$ denotes the set of all compact operators on *X*. **Example:** $\lambda =0\in \sigma _{\mathrm {ess} ,4}(R)$ where $R:\,l^{2}(\mathbb {N} )\to l^{2}(\mathbb {N} )$ is the right shift operator, $R:\,l^{2}(\mathbb {N} )\to l^{2}(\mathbb {N} )$ , $R:\,e_{j}\mapsto e_{j+1}$ for $j\in \mathbb {N}$ (its kernel is zero, its cokernel is one-dimensional). Note that $\lambda =0\not \in \sigma _{\mathrm {ess} ,3}(R)$ .
5. The essential spectrum $\sigma _{\mathrm {ess} ,5}(A)$ is the union of $\sigma _{\mathrm {ess} ,1}(A)$ with all components of $\mathbb {C} \setminus \sigma _{\mathrm {ess} ,1}(A)$ that do not intersect with the resolvent set $\mathbb {C} \setminus \sigma (A)$ . It can also be characterized as $\sigma (A)\setminus \sigma _{\mathrm {d} }(A)$ . **Example:** consider the operator $T:\,l^{2}(\mathbb {Z} )\to l^{2}(\mathbb {Z} )$ , $T:\,e_{j}\mapsto e_{j-1}$ for $j\neq 0$ , $T:\,e_{0}\mapsto 0$ . Since $\Vert T\Vert =1$ , one has $\sigma (T)\subset {\overline {\mathbb {D} _{1}}}$ . For any $z\in \mathbb {C}$ with $|z|=1$ , the range of $T-zI$ is dense but not closed, hence the boundary of the unit disc is in the first type of the essential spectrum: $\partial \mathbb {D} _{1}\subset \sigma _{\mathrm {ess} ,1}(T)$ . For any $z\in \mathbb {C}$ with $|z|<1$ , $T-zI$ has a closed range, one-dimensional kernel, and one-dimensional cokernel, so $z\in \sigma (T)$ although $z\not \in \sigma _{\mathrm {ess} ,k}(T)$ for $1\leq k\leq 4$ ; thus, $\sigma _{\mathrm {ess} ,k}(T)=\partial \mathbb {D} _{1}$ for $1\leq k\leq 4$ . There are two components of $\mathbb {C} \setminus \sigma _{\mathrm {ess} ,1}(T)$ : $\{z\in \mathbb {C$ and $\{z\in \mathbb {C$ . The component $\{|z|<1\}$ has no intersection with the resolvent set; by definition, $\sigma _{\mathrm {ess} ,5}(T)=\sigma _{\mathrm {ess} ,1}(T)\cup \{z\in \mathbb {C$ .

## Example: Hydrogen atom

The hydrogen atom provides an example of different types of the spectra. The hydrogen atom Hamiltonian operator $H=-\Delta -{\frac {Z}{|x|}}$ , $Z>0$ , with domain $D(H)=H^{1}(\mathbb {R} ^{3})$ has a discrete set of eigenvalues (the discrete spectrum $\sigma _{\mathrm {d} }(H)$ , which in this case coincides with the point spectrum $\sigma _{\mathrm {p} }(H)$ since there are no eigenvalues embedded into the continuous spectrum) that can be computed by the Rydberg formula. Their corresponding eigenfunctions are called **eigenstates**, or the bound states. The result of the ionization process is described by the continuous part of the spectrum (the energy of the collision/ionization is not "quantized"), represented by $\sigma _{\mathrm {cont} }(H)=[0,+\infty )$ (it also coincides with the essential spectrum, $\sigma _{\mathrm {ess} }(H)=[0,+\infty )$ ).

## Spectrum of the adjoint operator

Let *X* be a Banach space and $T:\,X\to X$ a closed linear operator with dense domain $D(T)\subset X$ . If *X** is the dual space of *X*, and $T^{*}:\,X^{*}\to X^{*}$ is the hermitian adjoint of *T*, then

$\sigma (T^{*})={\overline {\sigma (T)}}:=\{z\in \mathbb {C$

**Theorem**—For a bounded (or, more generally, closed and densely defined) operator *T*,

$\sigma _{\mathrm {cp} }(T)={\overline {\sigma _{\mathrm {p} }(T^{*})}}$

.

In particular, $\sigma _{\mathrm {r} }(T)\subset {\overline {\sigma _{\mathrm {p} }(T^{*})}}\subset \sigma _{\mathrm {r} }(T)\cup \sigma _{\mathrm {p} }(T)$ .

Proof

Suppose that $\mathrm {Ran} (T-\lambda I)$ is not dense in *X*. By the Hahn–Banach theorem, there exists a non-zero $\varphi \in X^{*}$ that vanishes on $\mathrm {Ran} (T-\lambda I)$ . For all *x* ∈ *X*,

$\langle \varphi ,(T-\lambda I)x\rangle =\langle (T^{*}-{\bar {\lambda }}I)\varphi ,x\rangle =0.$

Therefore, $(T^{*}-{\bar {\lambda }}I)\varphi =0\in X^{*}$ and ${\bar {\lambda }}$ is an eigenvalue of *T**.

Conversely, suppose that ${\bar {\lambda }}$ is an eigenvalue of *T**. Then there exists a non-zero $\varphi \in X^{*}$ such that $(T^{*}-{\bar {\lambda }}I)\varphi =0$ , i.e.

$\forall x\in X,\;\langle (T^{*}-{\bar {\lambda }}I)\varphi ,x\rangle =\langle \varphi ,(T-\lambda I)x\rangle =0.$

If $\mathrm {Ran} (T-\lambda I)$ is dense in *X*, then *φ* must be the zero functional, a contradiction. The claim is proved.

We also get $\sigma _{\mathrm {p} }(T)\subset {\overline {\sigma _{\mathrm {r} }(T^{*})\cup \sigma _{\mathrm {p} }(T^{*})}}$ by the following argument: *X* embeds isometrically into *X***. Therefore, for every non-zero element in the kernel of $T-\lambda I$ there exists a non-zero element in *X*** which vanishes on $\mathrm {Ran} (T^{*}-{\bar {\lambda }}I)$ . Thus $\mathrm {Ran} (T^{*}-{\bar {\lambda }}I)$ can not be dense.

Furthermore, if *X* is reflexive, we have ${\overline {\sigma _{\mathrm {r} }(T^{*})}}\subset \sigma _{\mathrm {p} }(T)$ .

## Spectra of particular classes of operators

### Compact operators

If *T* is a compact operator, or, more generally, an inessential operator, then it can be shown that the spectrum is countable, that zero is the only possible accumulation point, and that any nonzero *λ* in the spectrum is an eigenvalue.

### Quasinilpotent operators

A bounded operator $A:\,X\to X$ is **quasinilpotent** if $\lVert A^{n}\rVert ^{1/n}\to 0$ as $n\to \infty$ (in other words, if the spectral radius of *A* equals zero). Such operators could equivalently be characterized by the condition

$\sigma (A)=\{0\}.$

An example of such an operator is $A:\,l^{2}(\mathbb {N} )\to l^{2}(\mathbb {N} )$ , $e_{j}\mapsto e_{j+1}/2^{j}$ for $j\in \mathbb {N}$ .

### Self-adjoint operators

If *X* is a Hilbert space and *T* is a self-adjoint operator (or, more generally, a normal operator), then a remarkable result known as the spectral theorem gives an analogue of the diagonalisation theorem for normal finite-dimensional operators (Hermitian matrices, for example).

For self-adjoint operators, one can use spectral measures to define a decomposition of the spectrum into absolutely continuous, pure point, and singular parts.

## Spectrum of a real operator

The definitions of the resolvent and spectrum can be extended to any continuous linear operator T acting on a Banach space X over the real field $\mathbb {R}$ (instead of the complex field $\mathbb {C}$ ) via its complexification $T_{\mathbb {C} }$ . In this case we define the resolvent set $\rho (T)$ as the set of all $\lambda \in \mathbb {C}$ such that $T_{\mathbb {C} }-\lambda I$ is invertible as an operator acting on the complexified space $X_{\mathbb {C} }$ ; then we define $\sigma (T)=\mathbb {C} \setminus \rho (T)$ .

### Real spectrum

The *real spectrum* of a continuous linear operator T acting on a real Banach space X , denoted $\sigma _{\mathbb {R} }(T)$ , is defined as the set of all $\lambda \in \mathbb {R}$ for which $T-\lambda I$ fails to be invertible in the real algebra of bounded linear operators acting on X . In this case we have $\sigma (T)\cap \mathbb {R} =\sigma _{\mathbb {R} }(T)$ . Note that the real spectrum may or may not coincide with the complex spectrum. In particular, the real spectrum could be empty.

## Spectrum of a unital Banach algebra

Let *B* be a complex Banach algebra containing a unit *e*. Then we define the spectrum *σ*(*x*) (or more explicitly *σ**B*(*x*)) of an element *x* of *B* to be the set of those complex numbers *λ* for which *λe* − *x* is not invertible in *B*. This extends the definition for bounded linear operators *B*(*X*) on a Banach space *X*, since *B*(*X*) is a unital Banach algebra.
