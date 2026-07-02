---
title: "Lanczos algorithm"
source: https://en.wikipedia.org/wiki/Lanczos_algorithm
domain: eigenvalue-solvers
license: CC-BY-SA-4.0
tags: eigenvalue algorithm, lanczos algorithm, arnoldi iteration, qr algorithm
fetched: 2026-07-02
---

# Lanczos algorithm

The **Lanczos algorithm** is an iterative method devised by Cornelius Lanczos that is an adaptation of power methods to find the m "most useful" (tending towards extreme highest/lowest) eigenvalues and eigenvectors of an $n\times n$ Hermitian matrix, where m is often but not necessarily much smaller than n . Although computationally efficient in principle, the method as initially formulated was not useful, due to its numerical instability.

In 1970, Ojalvo and Newman showed how to make the method numerically stable and applied it to the solution of very large engineering structures subjected to dynamic loading. This was achieved using a method for purifying the Lanczos vectors (i.e. by repeatedly reorthogonalizing each newly generated vector with **all** previously generated ones) to any degree of accuracy, which when not performed, produced a series of vectors that were highly contaminated by those associated with the lowest natural frequencies.

In their original work, these authors also suggested how to select a starting vector (i.e. use a random-number generator to select each element of the starting vector) and suggested an empirically determined method for determining m , the reduced number of vectors (i.e. it should be selected to be approximately 1.5 times the number of accurate eigenvalues desired). Soon thereafter their work was followed by Paige, who also provided an error analysis. In 1988, Ojalvo produced a more detailed history of this algorithm and an efficient eigenvalue error test.

## The algorithm

Input

a

Hermitian matrix

A

of size

$n\times n$

, and optionally a number of iterations

m

(as default, let

$m=n$

).

- Strictly speaking, the algorithm does not need access to the explicit matrix, but only a function $v\mapsto Av$ that computes the product of the matrix by an arbitrary vector. This function is called at most m times.

Output

an

$n\times m$

matrix

V

with

orthonormal

columns and a

tridiagonal

real symmetric matrix

$T=V^{*}AV$

of size

$m\times m$

. If

$m=n$

, then

V

is

unitary

, and

$A=VTV^{*}$

.

Warning

The Lanczos iteration is prone to numerical instability. When executed in non-exact arithmetic, additional measures (as outlined in later sections) should be taken to ensure validity of the results.

1. Let $v_{1}\in \mathbb {C} ^{n}$ be an arbitrary vector with Euclidean norm 1 .
2. Abbreviated initial iteration step:
  1. Let $w_{1}'=Av_{1}$ .
  2. Let $\alpha _{1}=w_{1}'^{*}v_{1}$ .
  3. Let $w_{1}=w_{1}'-\alpha _{1}v_{1}$ .
3. For $j=2,\dots ,m$ do:
  1. Let $\beta _{j}=\|w_{j-1}\|$ (also Euclidean norm).
  2. If $\beta _{j}\neq 0$ , then let $v_{j}=w_{j-1}/\beta _{j}$ , else pick as $v_{j}$ an arbitrary vector with Euclidean norm 1 that is orthogonal to all of $v_{1},\dots ,v_{j-1}$ .
  3. Let $w_{j}'=Av_{j}-\beta _{j}v_{j-1}$ .
  4. Let $\alpha _{j}=w_{j}'^{*}v_{j}$ .
  5. Let $w_{j}=w_{j}'-\alpha _{j}v_{j}$ .
4. Let V be the matrix with columns $v_{1},\dots ,v_{m}$ . Let $T={\begin{pmatrix}\alpha _{1}&\beta _{2}&&&&0\\\beta _{2}&\alpha _{2}&\beta _{3}&&&\\&\beta _{3}&\alpha _{3}&\ddots &&\\&&\ddots &\ddots &\beta _{m-1}&\\&&&\beta _{m-1}&\alpha _{m-1}&\beta _{m}\\0&&&&\beta _{m}&\alpha _{m}\\\end{pmatrix}}$ .

Note

$Av_{j}=\beta _{j+1}v_{j+1}+\alpha _{j}v_{j}+\beta _{j}v_{j-1}$

for

$2<j<m$

.

There are in principle four ways to write the iteration procedure. Paige and other works show that the above order of operations is the most numerically stable. In practice the initial vector $v_{1}$ may be taken as another argument of the procedure, with $\beta _{j}=0$ and indicators of numerical imprecision being included as additional loop termination conditions.

Not counting the matrix–vector multiplication, each iteration does $O(n)$ arithmetical operations. The matrix–vector multiplication can be done in $O(dn)$ arithmetical operations where d is the average number of nonzero elements in a row. The total complexity is thus $O(dmn)$ , or $O(dn^{2})$ if $m=n$ ; the Lanczos algorithm can be very fast for sparse matrices. Schemes for improving numerical stability are typically judged against this high performance.

The vectors $v_{j}$ are called *Lanczos vectors*. The vector $w_{j}'$ is not used after $w_{j}$ is computed, and the vector $w_{j}$ is not used after $v_{j+1}$ is computed. Hence one may use the same storage for all three. Likewise, if only the tridiagonal matrix T is sought, then the raw iteration does not need $v_{j-1}$ after having computed $w_{j}$ , although some schemes for improving the numerical stability would need it later on. Sometimes the subsequent Lanczos vectors are recomputed from $v_{1}$ when needed.

### Application to the eigenproblem

The Lanczos algorithm is most often brought up in the context of finding the eigenvalues and eigenvectors of a matrix, but whereas an ordinary diagonalization of a matrix would make eigenvectors and eigenvalues apparent from inspection, the same is not true for the tridiagonalization performed by the Lanczos algorithm; nontrivial additional steps are needed to compute even a single eigenvalue or eigenvector. Nonetheless, applying the Lanczos algorithm is often a significant step forward in computing the eigendecomposition.

If $\lambda$ is an eigenvalue of T , and x its eigenvector ( $Tx=\lambda x$ ), then $y=Vx$ is a corresponding eigenvector of A with the same eigenvalue:

${\begin{aligned}Ay&=AVx\\&=VTV^{*}Vx\\&=VTIx\\&=VTx\\&=V(\lambda x)\\&=\lambda Vx\\&=\lambda y.\end{aligned}}$

Thus the Lanczos algorithm transforms the eigendecomposition problem for A into the eigendecomposition problem for T .

1. For tridiagonal matrices, there exist a number of specialised algorithms, often with better computational complexity than general-purpose algorithms. For example, if T is an $m\times m$ tridiagonal symmetric matrix then:
  - The continuant recursion allows computing the characteristic polynomial in $O(m^{2})$ operations, and evaluating it at a point in $O(m)$ operations.
  - The divide-and-conquer eigenvalue algorithm can be used to compute the entire eigendecomposition of T in $O(m^{2})$ operations.
  - The Fast Multipole Method can compute all eigenvalues in just $O(m\log m)$ operations.
2. Some general eigendecomposition algorithms, notably the QR algorithm, are known to converge faster for tridiagonal matrices than for general matrices. Asymptotic complexity of tridiagonal QR is $O(m^{2})$ just as for the divide-and-conquer algorithm (though the constant factor may be different); since the eigenvectors together have $m^{2}$ elements, this is asymptotically optimal.
3. Even algorithms whose convergence rates are unaffected by unitary transformations, such as the power method and inverse iteration, may enjoy low-level performance benefits from being applied to the tridiagonal matrix T rather than the original matrix A . Since T is very sparse with all nonzero elements in highly predictable positions, it permits compact storage with excellent performance vis-à-vis caching. Likewise, T is a real matrix with all eigenvectors and eigenvalues real, whereas A in general may have complex elements and eigenvectors, so real arithmetic is sufficient for finding the eigenvectors and eigenvalues of T .
4. If n is very large, then reducing m so that T is of a manageable size will still allow finding the more extreme eigenvalues and eigenvectors of A ; in the $m\ll n$ region, the Lanczos algorithm can be viewed as a lossy compression scheme for Hermitian matrices, that emphasises preserving the extreme eigenvalues.

The combination of good performance for sparse matrices and the ability to compute several (without computing all) eigenvalues are the main reasons for choosing to use the Lanczos algorithm.

### Application to tridiagonalization

Though the eigenproblem is often the motivation for applying the Lanczos algorithm, the operation the algorithm primarily performs is tridiagonalization of a matrix, for which numerically stable Householder transformations have been favoured since the 1950s. During the 1960s the Lanczos algorithm was disregarded. Interest in it was rejuvenated by the Kaniel–Paige convergence theory and the development of methods to prevent numerical instability, but the Lanczos algorithm remains the alternative algorithm that one tries only if Householder is not satisfactory.

Aspects in which the two algorithms differ include:

- Lanczos takes advantage of A being a sparse matrix, whereas Householder does not, and will generate fill-in.
- Lanczos works throughout with the original matrix A (and has no problem with it being known only implicitly), whereas raw Householder wants to modify the matrix during the computation (although that can be avoided).
- Each iteration of the Lanczos algorithm produces another column of the final transformation matrix V , whereas an iteration of Householder produces another factor in a unitary factorisation $Q_{1}Q_{2}\dots Q_{n}$ of V . Each factor is however determined by a single vector, so the storage requirements are the same for both algorithms, and $V=Q_{1}Q_{2}\dots Q_{n}$ can be computed in $O(n^{3})$ time.
- Householder is numerically stable, whereas raw Lanczos is not.
- Lanczos is highly parallel, with only $O(n)$ points of synchronisation (the computations of $\alpha _{j}$ and $\beta _{j}$ ). Householder is less parallel, having a sequence of $O(n^{2})$ scalar quantities computed that each depend on the previous quantity in the sequence.

## Derivation of the algorithm

There are several lines of reasoning which lead to the Lanczos algorithm.

### A more provident power method

The power method for finding the eigenvalue of largest magnitude and a corresponding eigenvector of a matrix A is roughly

1. Pick a random vector $u_{1}\neq 0$ .
2. For $j\geqslant 1$ (until the direction of $u_{j}$ has converged) do:
  1. Let $u_{j+1}'=Au_{j}.$
  2. Let $u_{j+1}=u_{j+1}'/\|u_{j+1}'\|.$

- In the large j limit, $u_{j}$ approaches the normed eigenvector corresponding to the largest magnitude eigenvalue.

A critique that can be raised against this method is that it is wasteful: it spends a lot of work (the matrix–vector products in step 2.1) extracting information from the matrix A , but pays attention only to the very last result; implementations typically use the same variable for all the vectors $u_{j}$ , having each new iteration overwrite the results from the previous one. It may be desirable to instead keep all the intermediate results and organise the data.

One piece of information that trivially is available from the vectors $u_{j}$ is a chain of Krylov subspaces. One way of stating that without introducing sets into the algorithm is to claim that it computes

a subset

$\{v_{j}\}_{j=1}^{m}$

of a basis of

$\mathbb {C} ^{n}$

such that

$Ax\in \operatorname {span} (v_{1},\dotsc ,v_{j+1})$

for every

$x\in \operatorname {span} (v_{1},\dotsc ,v_{j})$

and all

$1\leqslant j<m;$

this is trivially satisfied by $v_{j}=u_{j}$ as long as $u_{j}$ is linearly independent of $u_{1},\dotsc ,u_{j-1}$ (and in the case that there is such a dependence then one may continue the sequence by picking as $v_{j}$ an arbitrary vector linearly independent of $u_{1},\dotsc ,u_{j-1}$ ). A basis containing the $u_{j}$ vectors is however likely to be numerically ill-conditioned, since this sequence of vectors is by design meant to converge to an eigenvector of A . To avoid that, one can combine the power iteration with a Gram–Schmidt process, to instead produce an orthonormal basis of these Krylov subspaces.

1. Pick a random vector $u_{1}$ of Euclidean norm 1 . Let $v_{1}=u_{1}$ .
2. For $j=1,\dotsc ,m-1$ do:
  1. Let $u_{j+1}'=Au_{j}$ .
  2. For all $k=1,\dotsc ,j$ let $g_{k,j}=v_{k}^{*}u_{j+1}'$ . (These are the coordinates of $Au_{j}=u_{j+1}'$ with respect to the basis vectors $v_{1},\dotsc ,v_{j}$ .)
  3. Let $w_{j+1}=u_{j+1}'-\sum _{k=1}^{j}g_{k,j}v_{k}$ . (Cancel the component of $u_{j+1}'$ that is in $\operatorname {span} (v_{1},\dotsc ,v_{j})$ .)
  4. If $w_{j+1}\neq 0$ then let $u_{j+1}=u_{j+1}'/\|u_{j+1}'\|$ and $v_{j+1}=w_{j+1}/\|w_{j+1}\|$ , otherwise pick as $u_{j+1}=v_{j+1}$ an arbitrary vector of Euclidean norm 1 that is orthogonal to all of $v_{1},\dotsc ,v_{j}$ .

The relation between the power iteration vectors $u_{j}$ and the orthogonal vectors $v_{j}$ is that

$Au_{j}=\|u_{j+1}'\|u_{j+1}=u_{j+1}'=w_{j+1}+\sum _{k=1}^{j}g_{k,j}v_{k}=\|w_{j+1}\|v_{j+1}+\sum _{k=1}^{j}g_{k,j}v_{k}$

.

Here it may be observed that we do not actually need the $u_{j}$ vectors to compute these $v_{j}$ , because $u_{j}-v_{j}\in \operatorname {span} (v_{1},\dotsc ,v_{j-1})$ and therefore the difference between $u_{j+1}'=Au_{j}$ and $w_{j+1}'=Av_{j}$ is in $\operatorname {span} (v_{1},\dotsc ,v_{j})$ , which is cancelled out by the orthogonalisation process. Thus the same basis for the chain of Krylov subspaces is computed by

1. Pick a random vector $v_{1}$ of Euclidean norm 1 .
2. For $j=1,\dotsc ,m-1$ do:
  1. Let $w_{j+1}'=Av_{j}$ .
  2. For all $k=1,\dotsc ,j$ let $h_{k,j}=v_{k}^{*}w_{j+1}'$ .
  3. Let $w_{j+1}=w_{j+1}'-\sum _{k=1}^{j}h_{k,j}v_{k}$ .
  4. Let $h_{j+1,j}=\|w_{j+1}\|$ .
  5. If $h_{j+1,j}\neq 0$ then let $v_{j+1}=w_{j+1}/h_{j+1,j}$ , otherwise pick as $v_{j+1}$ an arbitrary vector of Euclidean norm 1 that is orthogonal to all of $v_{1},\dotsc ,v_{j}$ .

A priori the coefficients $h_{k,j}$ satisfy

$Av_{j}=\sum _{k=1}^{j+1}h_{k,j}v_{k}$

for all

$j<m$

;

the definition $h_{j+1,j}=\|w_{j+1}\|$ may seem a bit odd, but fits the general pattern $h_{k,j}=v_{k}^{*}w_{j+1}'$ since

$v_{j+1}^{*}w_{j+1}'=v_{j+1}^{*}w_{j+1}=\|w_{j+1}\|v_{j+1}^{*}v_{j+1}=\|w_{j+1}\|.$

Because the power iteration vectors $u_{j}$ that were eliminated from this recursion satisfy $u_{j}\in \operatorname {span} (v_{1},\ldots ,v_{j}),$ the vectors $\{v_{j}\}_{j=1}^{m}$ and coefficients $h_{k,j}$ contain enough information from A that all of $u_{1},\ldots ,u_{m}$ can be computed, so nothing was lost by switching vectors. (Indeed, it turns out that the data collected here give significantly better approximations of the largest eigenvalue than one gets from an equal number of iterations in the power method, although that is not necessarily obvious at this point.)

This last procedure is the Arnoldi iteration. The Lanczos algorithm then arises as the simplification one gets from eliminating calculation steps that turn out to be trivial when A is Hermitian—in particular most of the $h_{k,j}$ coefficients turn out to be zero.

Elementarily, if A is Hermitian then

$h_{k,j}=v_{k}^{*}w_{j+1}'=v_{k}^{*}Av_{j}=v_{k}^{*}A^{*}v_{j}=(Av_{k})^{*}v_{j}.$

For $k<j-1$ we know that $Av_{k}\in \operatorname {span} (v_{1},\ldots ,v_{j-1})$ , and since $v_{j}$ by construction is orthogonal to this subspace, this inner product must be zero. (This is essentially also the reason why sequences of orthogonal polynomials can always be given a three-term recurrence relation.) For $k=j-1$ one gets

$h_{j-1,j}=(Av_{j-1})^{*}v_{j}={\overline {v_{j}^{*}Av_{j-1}}}={\overline {h_{j,j-1}}}=h_{j,j-1}$

since the latter is real on account of being the norm of a vector. For $k=j$ one gets

$h_{j,j}=(Av_{j})^{*}v_{j}={\overline {v_{j}^{*}Av_{j}}}={\overline {h_{j,j}}},$

meaning this is real too.

More abstractly, if V is the matrix with columns $v_{1},\ldots ,v_{m}$ then the numbers $h_{k,j}$ can be identified as elements of the matrix $H=V^{*}AV$ , and $h_{k,j}=0$ for $k>j+1;$ the matrix H is upper Hessenberg. Since

$H^{*}=\left(V^{*}AV\right)^{*}=V^{*}A^{*}V=V^{*}AV=H$

the matrix H is Hermitian. This implies that H is also lower Hessenberg, so it must in fact be tridiagional. Being Hermitian, its main diagonal is real, and since its first subdiagonal is real by construction, the same is true for its first superdiagonal. Therefore, H is a real, symmetric matrix—the matrix T of the Lanczos algorithm specification.

### Simultaneous approximation of extreme eigenvalues

One way of characterising the eigenvectors of a Hermitian matrix A is as stationary points of the Rayleigh quotient

$r(x)={\frac {x^{*}Ax}{x^{*}x}},\qquad x\in \mathbb {C} ^{n}.$

In particular, the largest eigenvalue $\lambda _{\max }$ is the global maximum of r and the smallest eigenvalue $\lambda _{\min }$ is the global minimum of r .

Within a low-dimensional subspace ${\mathcal {L}}$ of $\mathbb {C} ^{n}$ it can be feasible to locate the maximum x and minimum y of r . Repeating that for an increasing chain ${\mathcal {L}}_{1}\subset {\mathcal {L}}_{2}\subset \cdots$ produces two sequences of vectors: $x_{1},x_{2},\ldots$ and $y_{1},y_{2},\dotsc$ such that $x_{j},y_{j}\in {\mathcal {L}}_{j}$ and

${\begin{aligned}r(x_{1})&\leqslant r(x_{2})\leqslant \cdots \leqslant \lambda _{\max }\\r(y_{1})&\geqslant r(y_{2})\geqslant \cdots \geqslant \lambda _{\min }\end{aligned}}$

The question then arises how to choose the subspaces so that these sequences converge at optimal rate.

From $x_{j}$ , the optimal direction in which to seek larger values of r is that of the gradient $\nabla r(x_{j})$ , and likewise from $y_{j}$ the optimal direction in which to seek smaller values of r is that of the negative gradient $-\nabla r(y_{j})$ . In general

$\nabla r(x)={\frac {2}{x^{*}x}}(Ax-r(x)x),$

so the directions of interest are easy enough to compute in matrix arithmetic, but if one wishes to improve on both $x_{j}$ and $y_{j}$ then there are two new directions to take into account: $Ax_{j}$ and $Ay_{j};$ since $x_{j}$ and $y_{j}$ can be linearly independent vectors (indeed, are close to orthogonal), one cannot in general expect $Ax_{j}$ and $Ay_{j}$ to be parallel. It is not necessary to increase the dimension of ${\mathcal {L}}_{j}$ by 2 on every step if $\{{\mathcal {L}}_{j}\}_{j=1}^{m}$ are taken to be Krylov subspaces, because then $Az\in {\mathcal {L}}_{j+1}$ for all $z\in {\mathcal {L}}_{j},$ thus in particular for both $z=x_{j}$ and $z=y_{j}$ .

In other words, we can start with some arbitrary initial vector $x_{1}=y_{1},$ construct the vector spaces

${\mathcal {L}}_{j}=\operatorname {span} (x_{1},Ax_{1},\ldots ,A^{j-1}x_{1})$

and then seek $x_{j},y_{j}\in {\mathcal {L}}_{j}$ such that

$r(x_{j})=\max _{z\in {\mathcal {L}}_{j}}r(z)\qquad {\text{and}}\qquad r(y_{j})=\min _{z\in {\mathcal {L}}_{j}}r(z).$

Since the j th power method iterate $u_{j}$ belongs to ${\mathcal {L}}_{j},$ it follows that an iteration to produce the $x_{j}$ and $y_{j}$ cannot converge slower than that of the power method, and will achieve more by approximating both eigenvalue extremes. For the subproblem of optimising r on some ${\mathcal {L}}_{j}$ , it is convenient to have an orthonormal basis $\{v_{1},\ldots ,v_{j}\}$ for this vector space. Thus we are again led to the problem of iteratively computing such a basis for the sequence of Krylov subspaces.

## Convergence and other dynamics

When analysing the dynamics of the algorithm, it is convenient to take the eigenvalues and eigenvectors of A as given, even though they are not explicitly known to the user. To fix notation, let $\lambda _{1}\geqslant \lambda _{2}\geqslant \dotsb \geqslant \lambda _{n}$ be the eigenvalues (these are known to all be real, and thus possible to order) and let $z_{1},\dotsc ,z_{n}$ be an orthonormal set of eigenvectors such that $Az_{k}=\lambda _{k}z_{k}$ for all $k=1,\dotsc ,n$ .

It is also convenient to fix a notation for the coefficients of the initial Lanczos vector $v_{1}$ with respect to this eigenbasis; let $d_{k}=z_{k}^{*}v_{1}$ for all $k=1,\dotsc ,n$ , so that $\textstyle v_{1}=\sum _{k=1}^{n}d_{k}z_{k}$ . A starting vector $v_{1}$ depleted of some eigencomponent will delay convergence to the corresponding eigenvalue, and even though this just comes out as a constant factor in the error bounds, depletion remains undesirable. One common technique for avoiding being consistently hit by it is to pick $v_{1}$ by first drawing the elements randomly according to the same normal distribution with mean 0 and then rescale the vector to norm 1 . Prior to the rescaling, this causes the coefficients $d_{k}$ to also be independent normally distributed stochastic variables from the same normal distribution (since the change of coordinates is unitary), and after rescaling the vector $(d_{1},\dotsc ,d_{n})$ will have a uniform distribution on the unit sphere in $\mathbb {C} ^{n}$ . This makes it possible to bound the probability that for example $|d_{1}|<\varepsilon$ .

The fact that the Lanczos algorithm is coordinate-agnostic – operations only look at inner products of vectors, never at individual elements of vectors – makes it easy to construct examples with known eigenstructure to run the algorithm on: make A a diagonal matrix with the desired eigenvalues on the diagonal; as long as the starting vector $v_{1}$ has enough nonzero elements, the algorithm will output a general tridiagonal symmetric matrix as T .

### Kaniel–Paige convergence theory

After m iteration steps of the Lanczos algorithm, T is an $m\times m$ real symmetric matrix, that similarly to the above has m eigenvalues $\theta _{1}\geqslant \theta _{2}\geqslant \dots \geqslant \theta _{m}.$ Convergence is primarily understood as convergence of $\theta _{1}$ to $\lambda _{1}$ (and the symmetrical convergence of $\theta _{m}$ to $\lambda _{n}$ ) as m grows, and secondarily the convergence of some range $\theta _{1},\ldots ,\theta _{k}$ of eigenvalues of T to their counterparts $\lambda _{1},\ldots ,\lambda _{k}$ of A . The convergence for the Lanczos algorithm is often orders of magnitude faster than that for the power iteration algorithm.

The bounds for $\theta _{1}$ come from the above interpretation of eigenvalues as extreme values of the Rayleigh quotient $r(x)$ . Since $\lambda _{1}$ is a priori the maximum of r on the whole of $\mathbb {C} ^{n},$ whereas $\theta _{1}$ is merely the maximum on an m -dimensional Krylov subspace, we trivially get $\lambda _{1}\geqslant \theta _{1}$ . Conversely, any point x in that Krylov subspace provides a lower bound $r(x)$ for $\theta _{1}$ , so if a point can be exhibited for which $\lambda _{1}-r(x)$ is small then this provides a tight bound on $\theta _{1}$ .

The dimension m Krylov subspace is

$\operatorname {span} \left\{v_{1},Av_{1},A^{2}v_{1},\ldots ,A^{m-1}v_{1}\right\},$

so any element of it can be expressed as $p(A)v_{1}$ for some polynomial p of degree at most $m-1$ ; the coefficients of that polynomial are simply the coefficients in the linear combination of the vectors $v_{1},Av_{1},A^{2}v_{1},\ldots ,A^{m-1}v_{1}$ . The polynomial we want will turn out to have real coefficients, but for the moment we should allow also for complex coefficients, and we will write $p^{*}$ for the polynomial obtained by complex conjugating all coefficients of p . In this parametrisation of the Krylov subspace, we have

$r(p(A)v_{1})={\frac {(p(A)v_{1})^{*}Ap(A)v_{1}}{(p(A)v_{1})^{*}p(A)v_{1}}}={\frac {v_{1}^{*}p(A)^{*}Ap(A)v_{1}}{v_{1}^{*}p(A)^{*}p(A)v_{1}}}={\frac {v_{1}^{*}p^{*}(A^{*})Ap(A)v_{1}}{v_{1}^{*}p^{*}(A^{*})p(A)v_{1}}}={\frac {v_{1}^{*}p^{*}(A)Ap(A)v_{1}}{v_{1}^{*}p^{*}(A)p(A)v_{1}}}$

Using now the expression for $v_{1}$ as a linear combination of eigenvectors, we get

$Av_{1}=A\sum _{k=1}^{n}d_{k}z_{k}=\sum _{k=1}^{n}d_{k}\lambda _{k}z_{k}$

and more generally

$q(A)v_{1}=\sum _{k=1}^{n}d_{k}q(\lambda _{k})z_{k}$

for any polynomial q .

Thus

$\lambda _{1}-r(p(A)v_{1})=\lambda _{1}-{\frac {v_{1}^{*}\sum _{k=1}^{n}d_{k}p^{*}(\lambda _{k})\lambda _{k}p(\lambda _{k})z_{k}}{v_{1}^{*}\sum _{k=1}^{n}d_{k}p^{*}(\lambda _{k})p(\lambda _{k})z_{k}}}=\lambda _{1}-{\frac {\sum _{k=1}^{n}|d_{k}|^{2}\lambda _{k}p(\lambda _{k})^{*}p(\lambda _{k})}{\sum _{k=1}^{n}|d_{k}|^{2}p(\lambda _{k})^{*}p(\lambda _{k})}}={\frac {\sum _{k=1}^{n}|d_{k}|^{2}(\lambda _{1}-\lambda _{k})\left|p(\lambda _{k})\right|^{2}}{\sum _{k=1}^{n}|d_{k}|^{2}\left|p(\lambda _{k})\right|^{2}}}.$

A key difference between numerator and denominator here is that the $k=1$ term vanishes in the numerator, but not in the denominator. Thus if one can pick p to be large at $\lambda _{1}$ but small at all other eigenvalues, one will get a tight bound on the error $\lambda _{1}-\theta _{1}$ .

Since A has many more eigenvalues than p has coefficients, this may seem a tall order, but one way to meet it is to use Chebyshev polynomials. Writing $c_{k}$ for the degree k Chebyshev polynomial of the first kind (that which satisfies $c_{k}(\cos x)=\cos(kx)$ for all x ), we have a polynomial which stays in the range $[-1,1]$ on the known interval $[-1,1]$ but grows rapidly outside it. With some scaling of the argument, we can have it map all eigenvalues except $\lambda _{1}$ into $[-1,1]$ . Let

$p(x)=c_{m-1}\left({\frac {2x-\lambda _{2}-\lambda _{n}}{\lambda _{2}-\lambda _{n}}}\right)$

(in case $\lambda _{2}=\lambda _{1}$ , use instead the largest eigenvalue strictly less than $\lambda _{1}$ ), then the maximal value of $|p(\lambda _{k})|^{2}$ for $k\geqslant 2$ is 1 and the minimal value is 0 , so

$\lambda _{1}-\theta _{1}\leqslant \lambda _{1}-r(p(A)v_{1})={\frac {\sum _{k=2}^{n}|d_{k}|^{2}(\lambda _{1}-\lambda _{k})|p(\lambda _{k})|^{2}}{\sum _{k=1}^{n}|d_{k}|^{2}|p(\lambda _{k})|^{2}}}\leqslant {\frac {\sum _{k=2}^{n}|d_{k}|^{2}(\lambda _{1}-\lambda _{k})}{|d_{1}|^{2}|p(\lambda _{1})|^{2}}}\leqslant {\frac {(\lambda _{1}-\lambda _{n})\sum _{k=2}^{n}|d_{k}|^{2}}{|p(\lambda _{1})|^{2}|d_{1}|^{2}}}.$

Furthermore

$p(\lambda _{1})=c_{m-1}\left({\frac {2\lambda _{1}-\lambda _{2}-\lambda _{n}}{\lambda _{2}-\lambda _{n}}}\right)=c_{m-1}\left(2{\frac {\lambda _{1}-\lambda _{2}}{\lambda _{2}-\lambda _{n}}}+1\right);$

the quantity

$\rho ={\frac {\lambda _{1}-\lambda _{2}}{\lambda _{2}-\lambda _{n}}}$

(i.e., the ratio of the first eigengap to the diameter of the rest of the spectrum) is thus of key importance for the convergence rate here. Also writing

$R=e^{\operatorname {arcosh} (1+2\rho )}=1+2\rho +2{\sqrt {\rho ^{2}+\rho }},$

we may conclude that

${\begin{aligned}\lambda _{1}-\theta _{1}&\leqslant {\frac {(\lambda _{1}-\lambda _{n})\left(1-|d_{1}|^{2}\right)}{c_{m-1}(2\rho +1)^{2}|d_{1}|^{2}}}\\[6pt]&={\frac {1-|d_{1}|^{2}}{|d_{1}|^{2}}}(\lambda _{1}-\lambda _{n}){\frac {1}{\cosh ^{2}((m-1)\operatorname {arcosh} (1+2\rho ))}}\\[6pt]&={\frac {1-|d_{1}|^{2}}{|d_{1}|^{2}}}(\lambda _{1}-\lambda _{n}){\frac {4}{\left(R^{m-1}+R^{-(m-1)}\right)^{2}}}\\[6pt]&\leqslant 4{\frac {1-|d_{1}|^{2}}{|d_{1}|^{2}}}(\lambda _{1}-\lambda _{n})R^{-2(m-1)}\end{aligned}}$

The convergence rate is thus controlled chiefly by R , since this bound shrinks by a factor $R^{-2}$ for each extra iteration.

For comparison, one may consider how the convergence rate of the power method depends on $\rho$ , but since the power method primarily is sensitive to the quotient between absolute values of the eigenvalues, we need $|\lambda _{n}|\leqslant |\lambda _{2}|$ for the eigengap between $\lambda _{1}$ and $\lambda _{2}$ to be the dominant one. Under that constraint, the case that most favours the power method is that $\lambda _{n}=-\lambda _{2}$ , so consider that. Late in the power method, the iteration vector:

$u=(1-t^{2})^{1/2}z_{1}+tz_{2}\approx z_{1}+tz_{2},$

where each new iteration effectively multiplies the $z_{2}$ -amplitude t by

${\frac {\lambda _{2}}{\lambda _{1}}}={\frac {\lambda _{2}}{\lambda _{2}+(\lambda _{1}-\lambda _{2})}}={\frac {1}{1+{\frac {\lambda _{1}-\lambda _{2}}{\lambda _{2}}}}}={\frac {1}{1+2\rho }}.$

The estimate of the largest eigenvalue is then

$u^{*}Au=(1-t^{2})\lambda _{1}+t^{2}\lambda _{2},$

so the above bound for the Lanczos algorithm convergence rate should be compared to

$\lambda _{1}-u^{*}Au=(\lambda _{1}-\lambda _{2})t^{2},$

which shrinks by a factor of $(1+2\rho )^{-2}$ for each iteration. The difference thus boils down to that between $1+2\rho$ and $R=1+2\rho +2{\sqrt {\rho ^{2}+\rho }}$ . In the $\rho \gg 1$ region, the latter is more like $1+4\rho$ , and performs like the power method would with an eigengap twice as large; a notable improvement. The more challenging case is however that of $\rho \ll 1,$ in which $R\approx 1+2{\sqrt {\rho }}$ is an even larger improvement on the eigengap; the $\rho \gg 1$ region is where the Lanczos algorithm convergence-wise makes the *smallest* improvement on the power method.

## Numerical stability

Stability means how much the algorithm will be affected (i.e. will it produce the approximate result close to the original one) if there are small numerical errors introduced and accumulated. Numerical stability is the central criterion for judging the usefulness of implementing an algorithm on a computer with roundoff.

For the Lanczos algorithm, it can be proved that with *exact arithmetic*, the set of vectors $v_{1},v_{2},\cdots ,v_{m+1}$ constructs an *orthonormal* basis, and the eigenvalues/vectors solved are good approximations to those of the original matrix. However, in practice (as the calculations are performed in floating point arithmetic where inaccuracy is inevitable), the orthogonality is quickly lost and in some cases the new vector could even be linearly dependent on the set that is already constructed. As a result, some of the eigenvalues of the resultant tridiagonal matrix may not be approximations to the original matrix. Therefore, the Lanczos algorithm is not very stable.

Users of this algorithm must be able to find and remove those "spurious" eigenvalues. Practical implementations of the Lanczos algorithm go in three directions to fight this stability issue:

1. Prevent the loss of orthogonality,
2. Recover the orthogonality after the basis is generated.
3. After the good and "spurious" eigenvalues are all identified, remove the spurious ones.

## Variations

Variations on the Lanczos algorithm exist where the vectors involved are tall, narrow matrices instead of vectors and the normalizing constants are small square matrices. These are called "block" Lanczos algorithms and can be much faster on computers with large numbers of registers and long memory-fetch times.

Many implementations of the Lanczos algorithm restart after a certain number of iterations. One of the most influential restarted variations is the implicitly restarted Lanczos method, which is implemented in ARPACK. This has led into a number of other restarted variations such as restarted Lanczos bidiagonalization. Another successful restarted variation is the Thick-Restart Lanczos method, which has been implemented in a software package called TRLan.

### Nullspace over a finite field

In 1995, Peter Montgomery published an algorithm, based on the Lanczos algorithm, for finding elements of the nullspace of a large sparse matrix over GF(2); since the set of people interested in large sparse matrices over finite fields and the set of people interested in large eigenvalue problems scarcely overlap, this is often also called the *block Lanczos algorithm* without causing unreasonable confusion.

## Applications

Lanczos algorithms are very attractive because the multiplication by $A\,$ is the only large-scale linear operation. Since weighted-term text retrieval engines implement just this operation, the Lanczos algorithm can be applied efficiently to text documents (see latent semantic indexing). Eigenvectors are also important for large-scale ranking methods such as the HITS algorithm developed by Jon Kleinberg, or the PageRank algorithm used by Google.

Lanczos algorithms are also used in condensed matter physics as a method for solving Hamiltonians of strongly correlated electron systems, as well as in shell model codes in nuclear physics.

## Implementations

The NAG Library contains several routines for the solution of large scale linear systems and eigenproblems which use the Lanczos algorithm.

ARPACK (FORTRAN 77, also available in MATLAB[1], GNU Octave(eigs), Julia[2], and Python via the SciPy[3] package) focuses on eigenvalue problems, and supports both stored and implicit matrices.

A Matlab implementation of the Lanczos algorithm (note precision issues) is available as a part of the Gaussian Belief Propagation Matlab Package. The GraphLab collaborative filtering library incorporates a large scale parallel implementation of the Lanczos algorithm (in C++) for multicore.

Julia implementations of Lanczos and related Krylov methods can be found in Krylov.jl, KrylovKit.jl, IterativeSolvers.jl, and ArnoldiMethod.jl.

The PRIMME library also implements a Lanczos-like algorithm.

An open source Python package Leymosun implements Lanczos algorithm in the context of Krylov Complexity in pure Python: Its function called *lanczos* will generate Krylov bases and the coefficients.
