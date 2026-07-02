---
title: "Compact operator"
source: https://en.wikipedia.org/wiki/Compact_operator
domain: spectral-theory
license: CC-BY-SA-4.0
tags: spectral theory, spectral theorem, self-adjoint operator, sturm-liouville theory
fetched: 2026-07-02
---

# Compact operator

In functional analysis, a branch of mathematics, a **compact operator** is a linear operator that behaves, in several important respects, like a finite-dimensional operator such as a matrix. In infinite-dimensional spaces, bounded sets are usually not compact, and bounded sequences need not have convergent subsequences. Compact operators partly restore this finite-dimensional behavior by sending bounded sets to sets whose closures are compact, or equivalently, in normed spaces, by sending bounded sequences to sequences with convergent subsequences.

Compact operators first arose in the theory of integral equations, where many integral operators have compactness properties. They play a central role in the Fredholm alternative, in the spectral theory of linear operators, and in applications to differential equations and Sobolev spaces. For example, compactness often implies that the nonzero spectrum of an operator consists of isolated eigenvalues of finite multiplicity, with possible accumulation only at zero.

## Motivation: integral equations

Compact operators were first studied in connection with integral equations. A typical example is an operator of the form

$(Kf)(x)=\int _{a}^{b}k(x,y)f(y)\,dy,$

where the function k is called the integral kernel. Under suitable regularity assumptions on k , the operator K sends bounded families of functions to families that are uniformly bounded and equicontinuous. By the Arzelà–Ascoli theorem, such families have compact closure in spaces such as $C([a,b])$ . Thus many integral operators are compact.

This compactness is useful because it makes some infinite-dimensional linear equations resemble finite-dimensional systems of linear equations. For example, the Fredholm equation

$u-\lambda Ku=f$

can often be studied by finite-dimensional approximation and by the Fredholm alternative. In this way, compact operators provide a bridge between concrete integral equations and the abstract spectral theory of operators on function spaces.

The same idea appears in other parts of analysis. Compact embeddings of function spaces, such as certain embeddings of Sobolev spaces into Lp spaces, allow differential and boundary value problems to be treated by methods similar to those used for compact integral operators.

## Definitions

### Normed spaces

Let X and Y be normed vector spaces, and let $T:X\to Y$ be a linear operator. The operator T is called *compact* if it maps bounded subsets of X to relatively compact subsets of Y ; that is, if for every bounded set $B\subseteq X$ , the closure of $T(B)$ in Y is compact.

Equivalently, T is compact if the image of the closed unit ball of X is relatively compact in Y . In metric terms, this means that every sequence $(x_{n})$ bounded in X has a subsequence $(x_{n_{k}})$ such that $(Tx_{n_{k}})$ converges in Y .

Every compact linear operator between normed spaces is bounded, and hence continuous.

Many standard results on compact operators are stated for Banach spaces. If Y is Banach, a subset of Y is relatively compact if and only if it is totally bounded. Thus, for operators into Banach spaces, compactness may also be expressed by saying that the image of every bounded subset of X is totally bounded in Y .

### TVS case

Let $X,Y$ be topological vector spaces and $T:X\to Y$ a linear operator.

The following statements are equivalent, and different authors may pick any one of these as the principal definition for "*T* is a compact operator":

- there exists a neighborhood U of the origin in *X* and $T(U)$ is a relatively compact subset of *Y*;
- there exists a neighborhood U of the origin in *X* and a compact subset $V\subseteq Y$ such that $T(U)\subseteq V$ ;
- there exists a nonempty open set U in *X* and $T(U)$ is a relatively compact subset of *Y*.

## Basic properties

Throughout this section, $X,Y,Z$ denote normed or Banach spaces, as specified, and $B(X,Y)$ denotes the space of bounded linear operators from X to Y . The compact operators from X to Y are denoted by $K(X,Y)$ .

### Relation with finite-dimensional operators

Every finite-rank operator is compact. Indeed, if the range of $T:X\to Y$ is finite-dimensional, then the image of a bounded subset of X is a bounded subset of a finite-dimensional normed space, and hence has compact closure.

Compactness is therefore automatic in finite-dimensional linear algebra. Conversely, the identity operator on an infinite-dimensional Banach space is not compact: the closed unit ball of an infinite-dimensional Banach space is not compact. Thus a Banach space X is finite-dimensional if and only if its identity operator $\operatorname {Id} _{X}$ is compact.

More generally, if a Banach space X admits an invertible compact operator $T:X\to X$ , then X is finite-dimensional.

### Continuity and boundedness

Every compact linear operator between normed spaces is bounded, and hence continuous.

### Algebraic properties

If X and Y are Banach spaces, then $K(X,Y)$ is a closed linear subspace of $B(X,Y)$ in the operator norm. Equivalently, if a sequence of compact operators $T_{n}:X\to Y$ converges in operator norm to an operator T , then T is compact.

Compact operators are stable under composition with bounded operators. If $T:X\to Y$ is compact and $A:W\to X$ , $B:Y\to Z$ are bounded linear operators, then

$BTA:W\to Z$

is compact. In particular, $K(X)=K(X,X)$ is a two-sided ideal in the Banach algebra $B(X)=B(X,X)$ .

In a Hilbert space X , the ring $B(X)$ of bounded operators modulo the two-sided ideal $K(X)$ is the Calkin algebra. This quotient is used to define one common form of the essential spectrum: for a bounded operator T on a Hilbert space, the essential spectrum is the spectrum of the coset $T+K(H)$ in the Calkin algebra, so compact perturbations do not change it.

### Approximation by finite-rank operators

Since every finite-rank operator is compact, every operator-norm limit of finite-rank operators is compact. On Hilbert spaces the converse also holds: every compact operator between Hilbert spaces is the operator-norm limit of finite-rank operators.

For general Banach spaces this converse need not hold. The question of whether compact operators can always be approximated by finite-rank operators is related to the approximation property, which fails for some Banach spaces. Whether this was true in general for Banach spaces (the approximation property) was an unsolved question for many years; in 1973 Per Enflo gave a counter-example, building on work by Alexander Grothendieck and Stefan Banach.

### Adjoints and ranges

A bounded linear operator between Banach spaces is compact if and only if its adjoint is compact; this result is known as Schauder's theorem.

If $T:X\to Y$ is compact, then the closure of the range of T is separable. If the range of T is closed, then the range is finite-dimensional.

### Relation to other operator classes

Every compact operator between Banach spaces is strictly singular, but the converse is false: there are strictly singular operators that are not compact.

## Fredholm theory

Compact operators are closely connected with Fredholm operators and the Fredholm alternative. This connection is one reason compact operators behave, in many respects, like finite-dimensional linear maps.

Let X be a Banach space and let $K:X\to X$ be compact. Then

$I-K$

is a Fredholm operator of index zero. Equivalently, the kernel of $I-K$ is finite-dimensional, the range of $I-K$ is closed, and

$\dim \ker(I-K)=\dim {\bigl (}X/\operatorname {Im} (I-K){\bigr )}.$

More generally, for every scalar $\lambda \neq 0$ , the operator

$\lambda I-K$

is Fredholm of index zero.

### Fredholm alternative

A standard consequence is the Fredholm alternative. For a compact operator $K:X\to X$ , the equation

$u-Ku=f$

has a unique solution $u\in X$ for every $f\in X$ if and only if the homogeneous equation

$u-Ku=0$

has only the zero solution. If the homogeneous equation has a nonzero solution, then its solution space is finite-dimensional, and the inhomogeneous equation is solvable only for those f satisfying finitely many compatibility conditions.

In terms of the adjoint operator $K^{*}:X^{*}\to X^{*}$ , these compatibility conditions can be written as

$\varphi (f)=0\quad {\text{for every }}\varphi \in \ker(I-K^{*}).$

Thus the obstruction to solving $u-Ku=f$ is finite-dimensional. This is analogous to the finite-dimensional situation in which a system of linear equations is solvable precisely when the right-hand side is orthogonal to the nullspace of the transpose.

For the parameter-dependent equation

$u-\lambda Ku=f,$

with $\lambda \neq 0$ , the same alternative applies to the operator $I-\lambda K$ . Failure of invertibility occurs precisely when $1/\lambda$ is a nonzero eigenvalue of K . Since the nonzero spectrum of a compact operator consists only of isolated eigenvalues of finite multiplicity, these exceptional parameters form a discrete set, with possible accumulation only at infinity.

## Spectral theory

The spectral theory of compact operators is closer to finite-dimensional linear algebra than the spectral theory of general bounded operators.

Let X be an infinite-dimensional complex Banach space, and let $T:X\to X$ be a compact operator. Then 0 belongs to the spectrum $\sigma (T)$ . Apart from 0 , every spectral value of T is an eigenvalue of finite multiplicity. More precisely, if $\lambda \neq 0$ and $\lambda \in \sigma (T)$ , then

$\ker(T-\lambda I)$

is finite-dimensional, the range of $T-\lambda I$ is closed, and $\lambda$ is an isolated point of the spectrum.

The nonzero spectrum is therefore either finite or countably infinite. If it is infinite, its only possible accumulation point is 0 . Equivalently, for every $r>0$ , the set

$\{\lambda \in \sigma (T):|\lambda |>r\}$

is finite. Thus compact operators cannot have a continuous band of nonzero spectral values.

The finite-dimensional character of the nonzero spectrum can also be expressed in Fredholm-theoretic terms. For $\lambda \neq 0$ , the operator

$T-\lambda I$

has finite-dimensional kernel and cokernel, and these dimensions are equal:

$\dim \ker(T-\lambda I)=\dim {\bigl (}X/\operatorname {Im} (T-\lambda I){\bigr )}.$

In particular, $T-\lambda I$ fails to be invertible precisely because $\lambda$ is an eigenvalue, not because of residual or continuous spectrum away from zero.

The adjoint has the same nonzero spectral values. If $\lambda \neq 0$ is in the spectrum of T , then $\lambda$ is also an eigenvalue of the adjoint operator $T^{*}:X^{*}\to X^{*}$ . More precisely,

$\dim \ker(T-\lambda I)=\dim \ker(T^{*}-\lambda I)$

when algebraic multiplicities are taken into account.

These results are often called the Riesz–Schauder theory of compact operators. They generalize the elementary fact that a finite-dimensional linear map has a spectrum consisting only of eigenvalues, while allowing for the infinite-dimensional phenomenon that eigenvalues may accumulate at 0 .

A notion related to the compactness of an operator is an operator with compact resolvent. An unbounded operator A , such as a differential operator, is said to have compact resolvent if $(A-\lambda I)^{-1}$ exists for some $\lambda$ and is a compact operator. This condition implies that the spectrum of A has discrete eigenvalues of finite multiplicity, with no finite accumulation point. Compact resolvents commonly arise for elliptic operators on bounded domains, where compact Sobolev embeddings provide the required compactness.

## Compact operators on Hilbert spaces

Compact operators on Hilbert spaces have a particularly close relationship with finite-dimensional linear algebra. In addition to the general Banach-space spectral properties of compact operators, Hilbert-space compact operators admit orthogonal decompositions, singular-value expansions, and, in the self-adjoint case, a spectral theorem resembling the spectral theorem for finite-dimensional Hermitian matrices.

### Compact self-adjoint operators

If H is a Hilbert space and $T:H\to H$ is compact and self-adjoint, then every nonzero element of the spectrum of T is an eigenvalue of finite multiplicity. The nonzero eigenvalues are real, have no possible accumulation point except 0 , and the eigenspaces corresponding to distinct eigenvalues are mutually orthogonal.

Equivalently, H decomposes as an orthogonal direct sum of the eigenspaces of T , together with the kernel of T . After choosing an orthonormal basis in each eigenspace and in the kernel, the operator is represented diagonally:

$Tx=\sum _{n}\lambda _{n}\langle x,e_{n}\rangle e_{n},$

where $(e_{n})$ is an orthonormal family of eigenvectors, $\lambda _{n}$ are the corresponding nonzero eigenvalues, and $\lambda _{n}\to 0$ if there are infinitely many nonzero eigenvalues. Thus compact self-adjoint operators behave much like finite-dimensional self-adjoint matrices, except that the eigenvalues may form a sequence tending to zero.

The same description applies, with complex eigenvalues, to compact normal operators on a complex Hilbert space.

### Singular-value expansion

A general compact operator on a Hilbert space need not be self-adjoint or normal. Nevertheless, it has a singular-value decomposition. If $T:H_{1}\to H_{2}$ is compact, then the positive eigenvalues of $|T|=(T^{*}T)^{1/2}$ are called the singular values of T . They form a finite sequence or a sequence tending to zero.

There are orthonormal families $(e_{n})$ in $H_{1}$ and $(f_{n})$ in $H_{2}$ , and nonnegative singular values $s_{n}$ with $s_{n}\to 0$ , such that

$Tx=\sum _{n}s_{n}\langle x,e_{n}\rangle f_{n}.$

The series converges in norm for each $x\in H_{1}$ , and the corresponding finite-rank partial sums converge to T in operator norm. If only finitely many singular values are nonzero, then T has finite rank. Conversely, every compact operator between Hilbert spaces is the operator-norm limit of finite-rank operators.

This singular-value expansion is often the most useful description of a compact Hilbert-space operator that is not self-adjoint. It generalizes the singular-value decomposition of finite-dimensional matrices.

### Hilbert–Schmidt and trace-class operators

Important subclasses of compact Hilbert-space operators are the Hilbert–Schmidt operators and trace-class operators. If T has singular values $(s_{n})$ , then T is Hilbert–Schmidt when

$\sum _{n}s_{n}^{2}<\infty ,$

and trace class when

$\sum _{n}s_{n}<\infty .$

Every trace-class operator is Hilbert–Schmidt, and every Hilbert–Schmidt operator is compact. The converses are false in general. For example, an operator with singular values $s_{n}=1/n$ is compact and Hilbert–Schmidt but not trace class, while an operator with singular values $s_{n}=1/{\sqrt {n}}$ is compact but not Hilbert–Schmidt.

## Completely continuous operators

Let $X,Y$ be Banach spaces. A bounded linear operator $T:X\to Y$ is called **completely continuous** if, for every weakly convergent sequence $(x_{n})$ from X , the sequence $(Tx_{n})$ is norm-convergent in Y .

Compact operators between Banach spaces are always completely continuous, but the converse is false, because there exists a completely continuous operator that is not compact. However, the converse is true if X is a reflexive Banach space: then every completely continuous operator $T:X\to Y$ is compact.

Somewhat confusingly, compact operators are sometimes referred to as "completely continuous" in older literature, even though the latter is a weaker condition in modern terminology.

## Examples and non-examples

Finite-rank operators are the simplest examples of compact operators. If $T:X\to Y$ has finite-dimensional range, then the image under T of any bounded subset of X is a bounded subset of a finite-dimensional normed space, and hence has compact closure. Thus finite-rank operators are compact. In finite-dimensional spaces this accounts for all bounded linear operators, but in infinite-dimensional spaces compactness is a genuine restriction.

One class of examples is given by diagonal or multiplication operators on sequence spaces. For example, on $\ell ^{p}$ , with $1\leq p\leq \infty$ , an operator of the form

$(Tx)_{n}=t_{n}x_{n}$

is compact when the scalar sequence $(t_{n})$ tends to zero. Such an operator can be approximated in operator norm by finite-rank diagonal operators obtained by truncating the sequence $(t_{n})$ . Conversely, if $(t_{n})$ does not tend to zero, the images of suitable coordinate vectors cannot have a convergent subsequence, so the corresponding multiplication operator is not compact.

Integral operators also provide compact operators in many important cases. If

$(Kf)(x)=\int _{a}^{b}k(x,y)f(y)\,dy$

has a sufficiently regular kernel k , then K often maps bounded families of functions to uniformly bounded and equicontinuous families. By the Arzelà–Ascoli theorem, such families have compact closure in spaces such as $C([a,b])$ . For instance, the operator

$(Tf)(x)=\int _{0}^{x}f(t)g(t)\,dt,$

where $g\in C([0,1])$ , defines a compact operator on $C([0,1])$ . On Hilbert spaces, Hilbert–Schmidt integral operators are compact; in particular, if $k\in L^{2}(\Omega \times \Omega )$ , then the integral operator

$(Tf)(x)=\int _{\Omega }k(x,y)f(y)\,dy$

is compact on $L^{2}(\Omega )$ .

The identity operator on an infinite-dimensional Banach space is a basic non-example. It is bounded, but not compact, because the closed unit ball of an infinite-dimensional Banach space is not compact. Equivalently, the identity operator would be compact only if every bounded sequence had a convergent subsequence, which fails in infinite-dimensional Banach spaces. The same argument shows that any nonzero scalar multiple of the identity is not compact on an infinite-dimensional Banach space.

The unilateral shift operators on sequence spaces are also not compact. For example, on $\ell ^{2}$ , the forward shift sends the standard basis vector $e_{n}$ to $e_{n+1}$ . The sequence $(e_{n+1})$ has no norm-convergent subsequence, so the image of the bounded sequence $(e_{n})$ is not relatively compact. The backward shift is non-compact for the same reason.

Every bounded linear operator from a normed space into a complete nuclear space is compact, because bounded sets in complete nuclear spaces are precompact. A complex-analytic example is given by the Cauchy integral operator. For the unit disk $\mathbb {D}$ , define

$(Tf)(z)={\frac {1}{2\pi i}}\int _{\partial \mathbb {D} }{\frac {f(\zeta )}{\zeta -z}}\,d\zeta ,\qquad z\in \mathbb {D} .$

As an operator from $L^{2}(\partial \mathbb {D} )$ into the Fréchet space ${\mathcal {O}}(\mathbb {D} )$ of holomorphic functions on $\mathbb {D}$ , with the topology of uniform convergence on compact subsets, this operator is compact. The image of a bounded set in $L^{2}(\partial \mathbb {D} )$ is locally uniformly bounded in $\mathbb {D}$ , and is therefore relatively compact by Montel's theorem. The compactness comes from viewing holomorphic functions only on compact subsets strictly inside the domain. Boundary oscillations may remain large in $L^{2}(\partial \mathbb {D} )$ , but they become invisible in the compact-open topology of ${\mathcal {O}}(\mathbb {D} )$ .

## Compact embeddings

Compact operators often arise as inclusion maps between function spaces. If X and Y are normed spaces with $X\subseteq Y$ , the inclusion

$I:X\to Y,\qquad Iu=u,$

is called an embedding when it is continuous. The embedding is called **compact** if this inclusion map is a compact operator; that is, if every bounded sequence in X has a subsequence that converges in the norm of Y . Compact embeddings are often denoted

$X{\overset {c}{\hookrightarrow }}Y.$

Compactness of an embedding is stronger than continuity. A continuous embedding gives an estimate of the form

$\|u\|_{Y}\leq C\|u\|_{X},$

whereas a compact embedding also asserts a precompactness property: bounded sets in the stronger space X become relatively compact when viewed in the weaker space Y .

The Arzelà–Ascoli theorem provides one example. The inclusion of a uniformly bounded and equicontinuous family of functions into $C([a,b])$ has compact closure. This is one reason many integral operators are compact: they send bounded sets of functions into equicontinuous families.

The Rellich–Kondrachov theorem yields other compact embeddings. If $\Omega \subset \mathbb {R} ^{n}$ is a bounded domain with suitable regularity, then certain Sobolev space embeddings are compact. For example, if $1\leq p<n$ and

$1\leq q<p^{*}={\frac {np}{n-p}},$

then the natural inclusion

$W^{1,p}(\Omega )\hookrightarrow L^{q}(\Omega )$

is compact. Thus every bounded sequence in $W^{1,p}(\Omega )$ has a subsequence converging in $L^{q}(\Omega )$ .

A non-example is the inclusion of Lebesgue spaces. If $(X,\mu )$ is a finite measure space, then by Hölder's inequality $L^{q}(X,\mu )\subset L^{p}(X,\mu )$ whenever $1\leq p<q\leq \infty$ . However, this inclusion is not compact in general. For example, on $[0,1]$ with Lebesgue measure, the Rademacher functions form a bounded sequence in every $L^{q}$ , but no subsequence converges in $L^{p}$ . Thus compactness of embeddings such as those in the Rellich–Kondrachov theorem depends on additional regularity, not merely on the inclusion of a stronger normed space into a weaker one.

Compact embeddings are central in the study of partial differential equations and calculus of variations. They allow weak or bounded sequences of approximate solutions to be replaced, after passing to subsequences, by strongly convergent sequences in a weaker norm. This compactness is used in existence proofs, in the study of elliptic boundary value problems, and in showing that many differential operators have discrete spectral behavior analogous to that of compact operators.

Holomorphic function spaces provide another class of compact embeddings. Let $\Omega \subset \mathbb {C} ^{n}$ be a domain, and let ${\mathcal {O}}(\Omega )$ denote the space of holomorphic functions on $\Omega$ , with the topology of uniform convergence on compact subsets. Many Banach spaces of holomorphic functions embed compactly into ${\mathcal {O}}(\Omega )$ . For example, on the unit disk, the inclusion

$H^{p}(\mathbb {D} )\hookrightarrow {\mathcal {O}}(\mathbb {D} )$

from the Hardy space $H^{p}(\mathbb {D} )$ into the space of holomorphic functions is compact for $1\leq p\leq \infty$ . A bounded set in $H^{p}(\mathbb {D} )$ is locally uniformly bounded in $\mathbb {D}$ , and hence is relatively compact in the compact-open topology by Montel's theorem.

The same principle applies to Bergman spaces. If $A^{p}(\Omega )$ is a Bergman space of holomorphic functions on a domain $\Omega$ , then estimates on compact subsets give, for each compact $K\subset \Omega$ ,

$\sup _{z\in K}|f(z)|\leq C_{K}\|f\|_{A^{p}(\Omega )}.$

Thus bounded sets in $A^{p}(\Omega )$ are normal families, and the natural inclusion

$A^{p}(\Omega )\hookrightarrow {\mathcal {O}}(\Omega )$

is compact. Similar compactness statements hold for restrictions to smaller subdomains $\Omega '\Subset \Omega$ , where bounded sets in Hardy or Bergman spaces become relatively compact in spaces of holomorphic functions on $\Omega '$ .

In several complex variables, analogous compact embeddings occur for Hardy and Bergman spaces on bounded domains, and for Hardy spaces on tube domains. For example, Hardy spaces on tube domains over cones consist of holomorphic functions satisfying uniform $L^{p}$ -type bounds on translated real slices. Interior estimates again imply local boundedness on compact subsets of the tube, so bounded sets form normal families and are compact in the compact-open topology.
