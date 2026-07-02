---
title: "Low-rank approximation"
source: https://en.wikipedia.org/wiki/Low-rank_approximation
domain: singular-value-decomposition-deep
license: CC-BY-SA-4.0
tags: singular value decomposition, moore-penrose inverse, low-rank approximation, polar decomposition
fetched: 2026-07-02
---

# Low-rank approximation

In mathematics, **low-rank approximation** refers to the process of approximating a given matrix by a matrix of lower rank. More precisely, it is a minimization problem, in which the cost function measures the fit between a given matrix (the data) and an approximating matrix (the optimization variable), subject to a constraint that the approximating matrix has reduced rank. The problem is used for mathematical modeling and data compression. The rank constraint is related to a constraint on the complexity of a model that fits the data. In applications, often there are other constraints on the approximating matrix apart from the rank constraint, e.g., non-negativity and Hankel structure.

Low-rank approximation is closely related to numerous other techniques, including principal component analysis, factor analysis, total least squares, latent semantic analysis, orthogonal regression, and dynamic mode decomposition.

## Definition

Given

- structure specification ${\mathcal {S}}:\mathbb {R} ^{n_{p}}\to \mathbb {R} ^{m\times n}$ ,
- vector of structure parameters $p\in \mathbb {R} ^{n_{p}}$ ,
- norm $\|\cdot \|$ , and
- desired rank r ,

${\text{minimize}}\quad {\text{over }}{\widehat {p}}\quad \|p-{\widehat {p}}\|\quad {\text{subject to}}\quad \operatorname {rank} {\big (}{\mathcal {S}}({\widehat {p}}){\big )}\leq r.$

## Applications

- Linear system identification, in which case the approximating matrix is Hankel structured.
- Machine learning, in which case the approximating matrix is nonlinearly structured.
- Recommender systems, in which cases the data matrix has missing values and the approximation is categorical.
- Distance matrix completion, in which case there is a positive definiteness constraint.
- Natural language processing, in which case the approximation is nonnegative.
- Computer algebra, in which case the approximation is Sylvester structured.
- Matrix product states, in which case the approximation is usually rescaled to have fixed Frobenius norm.

## Basic low-rank approximation problem

The unstructured problem with fit measured by the Frobenius norm, i.e.,

${\text{minimize}}\quad {\text{over }}{\widehat {D}}\quad \|D-{\widehat {D}}\|_{\text{F}}\quad {\text{subject to}}\quad \operatorname {rank} {\big (}{\widehat {D}}{\big )}\leq r$

has an analytic solution in terms of the singular value decomposition of the data matrix. The result is referred to as the matrix approximation lemma or **Eckart–Young–Mirsky theorem**. This problem was originally solved by Erhard Schmidt in the infinite dimensional context of integral operators (although his methods easily generalize to arbitrary compact operators on Hilbert spaces) and later rediscovered by C. Eckart and G. Young. L. Mirsky generalized the result to arbitrary unitarily invariant norms. Let

$D=U\Sigma V^{\top }\in \mathbb {R} ^{m\times n},\quad m\geq n$

be the singular value decomposition of D , where $\Sigma =:\operatorname {diag} (\sigma _{1},\ldots ,\sigma _{r})$ , where $r\leq \min\{m,n\}=n$ , is the $m\times n$ rectangular diagonal matrix with r non-zero singular values $\sigma _{1}\geq \ldots \geq \sigma _{r}>\sigma _{r+1}=\ldots =\sigma _{n}=0$ . For a given $k\in \{1,\dots ,r\}$ , partition U , $\Sigma$ , and V as follows:

$U=:{\begin{bmatrix}U_{1}&U_{2}\end{bmatrix}},\quad \Sigma =:{\begin{bmatrix}\Sigma _{1}&0\\0&\Sigma _{2}\end{bmatrix}},\quad {\text{and}}\quad V=:{\begin{bmatrix}V_{1}&V_{2}\end{bmatrix}},$

where $U_{1}$ is $m\times k$ , $\Sigma _{1}$ is $k\times k$ , and $V_{1}$ is $n\times k$ . Then the rank k matrix

${\widehat {D}}^{*}:=U_{1}\Sigma _{1}V_{1}^{\top },$

obtained from the truncated singular value decomposition is such that

$\|D-{\widehat {D}}^{*}\|_{\text{F}}=\min _{\operatorname {rank} ({\widehat {D}})\leq k}\|D-{\widehat {D}}\|_{\text{F}}={\sqrt {\sigma _{k+1}^{2}+\cdots +\sigma _{r}^{2}}}.$

The minimizer ${\widehat {D}}^{*}$ is unique if and only if $\sigma _{k}>\sigma _{k+1}$ .

## Proof of Eckart–Young–Mirsky theorem (for spectral norm)

Let $A\in \mathbb {R} ^{m\times n}$ be a real (possibly rectangular) matrix with $m\leq n$ . Suppose that

$A=U\Sigma V^{\top }$

is the singular value decomposition of A . Recall that U and V are orthogonal matrices, and $\Sigma$ is an $m\times n$ diagonal matrix with entries $(\sigma _{1},\sigma _{2},\cdots ,\sigma _{m})$ such that $\sigma _{1}\geq \sigma _{2}\geq \cdots \geq \sigma _{m}\geq 0$ .

We claim that the best rank- k approximation to A in the spectral norm, denoted by $\|\cdot \|_{2}$ , is given by

$A_{k}:=\sum _{i=1}^{k}\sigma _{i}u_{i}v_{i}^{\top }$

where $u_{i}$ and $v_{i}$ denote the i th column of U and V , respectively.

First, note that we have

$\|A-A_{k}\|_{2}=\left\|\sum _{i=1}^{\color {red}{n}}\sigma _{i}u_{i}v_{i}^{\top }-\sum _{i=1}^{\color {red}{k}}\sigma _{i}u_{i}v_{i}^{\top }\right\|_{2}=\left\|\sum _{i=\color {red}{k+1}}^{n}\sigma _{i}u_{i}v_{i}^{\top }\right\|_{2}=\sigma _{k+1}$

Therefore, we need to show that if $B_{k}=XY^{\top }$ where X and Y have k columns then $\|A-A_{k}\|_{2}=\sigma _{k+1}\leq \|A-B_{k}\|_{2}$ .

Since Y has k columns, then there must be a nontrivial linear combination of the first $k+1$ columns of V , i.e.,

$w=\gamma _{1}v_{1}+\cdots +\gamma _{k+1}v_{k+1},$

such that $Y^{\top }w=0$ . Without loss of generality, we can scale w so that $\|w\|_{2}=1$ or (equivalently) $\gamma _{1}^{2}+\cdots +\gamma _{k+1}^{2}=1$ . Therefore,

$\|A-B_{k}\|_{2}^{2}\geq \|(A-B_{k})w\|_{2}^{2}=\|Aw\|_{2}^{2}=\gamma _{1}^{2}\sigma _{1}^{2}+\cdots +\gamma _{k+1}^{2}\sigma _{k+1}^{2}\geq \sigma _{k+1}^{2}.$

The result follows by taking the square root of both sides of the above inequality.

## Proof of Eckart–Young–Mirsky theorem (for Frobenius norm)

Let $A\in \mathbb {R} ^{m\times n}$ be a real (possibly rectangular) matrix with $m\leq n$ . Suppose that

$A=U\Sigma V^{\top }$

is the singular value decomposition of A .

We claim that the best rank k approximation to A in the Frobenius norm, denoted by $\|\cdot \|_{F}$ , is given by

$A_{k}=\sum _{i=1}^{k}\sigma _{i}u_{i}v_{i}^{\top }$

where $u_{i}$ and $v_{i}$ denote the i th column of U and V , respectively.

First, note that we have

$\|A-A_{k}\|_{F}^{2}=\left\|\sum _{i=k+1}^{n}\sigma _{i}u_{i}v_{i}^{\top }\right\|_{F}^{2}=\sum _{i=k+1}^{n}\sigma _{i}^{2}$

Therefore, we need to show that if $B_{k}=XY^{\top }$ where X and Y have k columns then

$\|A-A_{k}\|_{F}^{2}=\sum _{i=k+1}^{n}\sigma _{i}^{2}\leq \|A-B_{k}\|_{F}^{2}.$

By the triangle inequality with the spectral norm, if $A=A'+A''$ then $\sigma _{1}(A)\leq \sigma _{1}(A')+\sigma _{1}(A'')$ . Suppose $A'_{k}$ and $A''_{k}$ respectively denote the rank k approximation to $A'$ and $A''$ by SVD method described above. Then, for any $i,j\geq 1$

${\begin{aligned}\sigma _{i}(A')+\sigma _{j}(A'')&=\sigma _{1}(A'-A'_{i-1})+\sigma _{1}(A''-A''_{j-1})\\&\geq \sigma _{1}(A-A'_{i-1}-A''_{j-1})\\&\geq \sigma _{1}(A-A_{i+j-2})\qquad ({\text{since }}{\rm {rank}}(A'_{i-1}+A''_{j-1})\leq i+j-2))\\&=\sigma _{i+j-1}(A).\end{aligned}}$

Since $\sigma _{k+1}(B_{k})=0$ , when $A'=A-B_{k}$ and $A''=B_{k}$ we conclude that for $i\geq 1,j=k+1$

$\sigma _{i}(A-B_{k})\geq \sigma _{k+i}(A).$

Therefore,

$\|A-B_{k}\|_{F}^{2}=\sum _{i=1}^{n}\sigma _{i}(A-B_{k})^{2}\geq \sum _{i=k+1}^{n}\sigma _{i}(A)^{2}=\|A-A_{k}\|_{F}^{2},$

as required.

## Weighted low-rank approximation problems

The Frobenius norm weights uniformly all elements of the approximation error $D-{\widehat {D}}$ . Prior knowledge about distribution of the errors can be taken into account by considering the weighted low-rank approximation problem

${\text{minimize}}\quad {\text{over }}{\widehat {D}}\quad \operatorname {vec} (D-{\widehat {D}})^{\top }W\operatorname {vec} (D-{\widehat {D}})\quad {\text{subject to}}\quad \operatorname {rank} ({\widehat {D}})\leq r,$

where ${\text{vec}}(A)$ vectorizes the matrix A column wise and W is a given positive (semi)definite weight matrix.

The general weighted low-rank approximation problem does not admit an analytic solution in terms of the singular value decomposition and is solved by local optimization methods, which provide no guarantee that a globally optimal solution is found.

In case of uncorrelated weights, weighted low-rank approximation problem also can be formulated in this way: for a non-negative matrix W and a matrix A we want to minimize $\sum _{i,j}(W_{i,j}(A_{i,j}-B_{i,j}))^{2}$ over matrices, B , of rank at most r .

## Entry-wise *L**p* low-rank approximation problems

Let $\|A\|_{p}=\left(\sum _{i,j}|A_{i,j}^{p}|\right)^{1/p}$ . For $p=2$ , the fastest algorithm runs in $nnz(A)+n\cdot poly(k/\epsilon )$ time. One of the important ideas been used is called Oblivious Subspace Embedding (OSE), it is first proposed by Sarlos.

For $p=1$ , it is known that this entry-wise L1 norm is more robust than the Frobenius norm in the presence of outliers and is indicated in models where Gaussian assumptions on the noise may not apply. It is natural to seek to minimize $\|B-A\|_{1}$ . For $p=0$ and $p\geq 1$ , there are some algorithms with provable guarantees.

## Distance low-rank approximation problem

Let $P=\{p_{1},\ldots ,p_{m}\}$ and $Q=\{q_{1},\ldots ,q_{n}\}$ be two point sets in an arbitrary metric space. Let A represent the $m\times n$ matrix where $A_{i,j}=dist(p_{i},q_{i})$ . Such distances matrices are commonly computed in software packages and have applications to learning image manifolds, handwriting recognition, and multi-dimensional unfolding. In an attempt to reduce their description size, one can study low rank approximation of such matrices.

## Distributed/Streaming low-rank approximation problem

The low-rank approximation problems in the distributed and streaming setting has been considered in.

## Image and kernel representations of the rank constraints

Using the equivalences

$\operatorname {rank} ({\widehat {D}})\leq r\quad \iff \quad {\text{there are }}P\in \mathbb {R} ^{m\times r}{\text{ and }}L\in \mathbb {R} ^{r\times n}{\text{ such that }}{\widehat {D}}=PL$

and

$\operatorname {rank} ({\widehat {D}})\leq r\quad \iff \quad {\text{there is full row rank }}R\in \mathbb {R} ^{m-r\times m}{\text{ such that }}R{\widehat {D}}=0$

the weighted low-rank approximation problem becomes equivalent to the parameter optimization problems

${\text{minimize}}\quad {\text{over }}{\widehat {D}},P{\text{ and }}L\quad \operatorname {vec} ^{\top }(D-{\widehat {D}})W\operatorname {vec} (D-{\widehat {D}})\quad {\text{subject to}}\quad {\widehat {D}}=PL$

and

${\text{minimize}}\quad {\text{over }}{\widehat {D}}{\text{ and }}R\quad \operatorname {vec} ^{\top }(D-{\widehat {D}})W\operatorname {vec} (D-{\widehat {D}})\quad {\text{subject to}}\quad R{\widehat {D}}=0\quad {\text{and}}\quad RR^{\top }=I_{r},$

where $I_{r}$ is the identity matrix of size r .

## Alternating projections algorithm

The image representation of the rank constraint suggests a parameter optimization method in which the cost function is minimized alternatively over one of the variables ( P or L ) with the other one fixed. Although simultaneous minimization over both P and L is a difficult biconvex optimization problem, minimization over one of the variables alone is a linear least squares problem and can be solved globally and efficiently.

The resulting optimization algorithm (called alternating projections) is globally convergent with a linear convergence rate to a locally optimal solution of the weighted low-rank approximation problem. Starting value for the P (or L ) parameter should be given. The iteration is stopped when a user defined convergence condition is satisfied.

Matlab implementation of the alternating projections algorithm for weighted low-rank approximation:

```mw
function [dh, f] = wlra_ap(d, w, p, tol, maxiter)
[m, n] = size(d); r = size(p, 2); f = inf;
for i = 2:maxiter
    % minimization over L
    bp = kron(eye(n), p);
    vl = (bp' * w * bp) \ bp' * w * d(:);
    l  = reshape(vl, r, n);
    % minimization over P
    bl = kron(l', eye(m));
    vp = (bl' * w * bl) \ bl' * w * d(:);
    p  = reshape(vp, m, r);
    % check exit condition
    dh = p * l; dd = d - dh;
    f(i) = dd(:)' * w * dd(:);
    if abs(f(i - 1) - f(i)) < tol, break, end
endfor
```

## Variable projections algorithm

The alternating projections algorithm exploits the fact that the low rank approximation problem, parameterized in the image form, is bilinear in the variables P or L . The bilinear nature of the problem is effectively used in an alternative approach, called variable projections.

Consider again the weighted low rank approximation problem, parameterized in the image form. Minimization with respect to the L variable (a linear least squares problem) leads to the closed form expression of the approximation error as a function of P

$f(P)={\sqrt {\operatorname {vec} ^{\top }(D){\Big (}W-W(I_{n}\otimes P){\big (}(I_{n}\otimes P)^{\top }W(I_{n}\otimes P){\big )}^{-1}(I_{n}\otimes P)^{\top }W{\Big )}\operatorname {vec} (D)}}.$

The original problem is therefore equivalent to the nonlinear least squares problem of minimizing $f(P)$ with respect to P . For this purpose standard optimization methods, e.g. the Levenberg-Marquardt algorithm can be used.

Matlab implementation of the variable projections algorithm for weighted low-rank approximation:

```mw
function [dh, f] = wlra_varpro(d, w, p, tol, maxiter)
prob = optimset(); prob.solver = 'lsqnonlin';
prob.options = optimset('MaxIter', maxiter, 'TolFun', tol); 
prob.x0 = p; prob.objective = @(p) cost_fun(p, d, w);
[p, f ] = lsqnonlin(prob); 
[f, vl] = cost_fun(p, d, w); 
dh = p * reshape(vl, size(p, 2), size(d, 2));

function [f, vl] = cost_fun(p, d, w)
bp = kron(eye(size(d, 2)), p);
vl = (bp' * w * bp) \ bp' * w * d(:);
f = d(:)' * w * (d(:) - bp * vl);
```

The variable projections approach can be applied also to low rank approximation problems parameterized in the kernel form. The method is effective when the number of eliminated variables is much larger than the number of optimization variables left at the stage of the nonlinear least squares minimization. Such problems occur in system identification, parameterized in the kernel form, where the eliminated variables are the approximating trajectory and the remaining variables are the model parameters. In the context of linear time-invariant systems, the elimination step is equivalent to Kalman smoothing.

## A Variant: convex-restricted low rank approximation

Usually, we want our new solution not only to be of low rank, but also satisfy other convex constraints due to application requirements. Our interested problem would be as follows,

${\text{minimize}}\quad {\text{over }}{\widehat {p}}\quad \|p-{\widehat {p}}\|\quad {\text{subject to}}\quad \operatorname {rank} {\big (}{\mathcal {S}}({\widehat {p}}){\big )}\leq r{\text{ and }}g({\widehat {p}})\leq 0$

This problem has many real world applications, including to recover a good solution from an inexact (semidefinite programming) relaxation. If additional constraint $g({\widehat {p}})\leq 0$ is linear, like we require all elements to be nonnegative, the problem is called structured low rank approximation. The more general form is named convex-restricted low rank approximation.

This problem is helpful in solving many problems. However, it is challenging due to the combination of the convex and nonconvex (low-rank) constraints. Different techniques were developed based on different realizations of $g({\widehat {p}})\leq 0$ . However, the Alternating Direction Method of Multipliers (ADMM) can be applied to solve the nonconvex problem with convex objective function, rank constraints and other convex constraints, and is thus suitable to solve our above problem. Moreover, unlike the general nonconvex problems, ADMM will guarantee to converge a feasible solution as long as its dual variable converges in the iterations.
