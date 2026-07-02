---
title: "Sum-of-squares optimization"
source: https://en.wikipedia.org/wiki/Sum-of-squares_optimization
domain: semidefinite-programming
license: CC-BY-SA-4.0
tags: semidefinite programming, conic optimization, linear matrix inequality, sum-of-squares optimization
fetched: 2026-07-02
---

# Sum-of-squares optimization

A **sum-of-squares optimization** program is an optimization problem with a linear cost function and constraints that certain polynomials constructed from the decision variables should be sums of squares. When the maximum degree of the polynomials involved is fixed, sum-of-squares optimization is also known as the **Lasserre hierarchy** of semidefinite programming relaxations.

Sum-of-squares optimization techniques have been applied across a variety of areas, including control theory (in particular, for searching for polynomial Lyapunov functions for dynamical systems described by polynomial vector fields), statistics, finance and machine learning.

## Background

A polynomial p is a *sum of squares* (*SOS*) if there exist polynomials $\{f_{i}\}_{i=1}^{m}$ such that ${\textstyle p=\sum _{i=1}^{m}f_{i}^{2}}$ . For example, $p=x^{2}-4xy+7y^{2}$ is a sum of squares since $p=f_{1}^{2}+f_{2}^{2}$ where $f_{1}=(x-2y){\text{ and }}f_{2}={\sqrt {3}}y.$ Note that if p is a sum of squares then $p(x)\geq 0$ for all $x\in \mathbb {R} ^{n}$ . Detailed descriptions of polynomial SOS are available.

Quadratic forms can be expressed as $p(x)=x^{T}Qx$ where Q is a symmetric matrix. Similarly, polynomials of degree ≤ 2*d* can be expressed as $p(x)=z(x)^{\mathsf {T}}Qz(x),$ where the vector z contains all monomials of degree $\leq d$ . This is known as the Gram matrix form. An important fact is that p is SOS if and only if there exists a symmetric and positive-semidefinite matrix Q such that $p(x)=z(x)^{\mathsf {T}}Qz(x)$ . This provides a connection between SOS polynomials and positive-semidefinite matrices.

## Optimization problem

A sum-of-squares optimization problem is a conic optimization problem with respect to the cone of sum-of-squares polynomials. Concretely, given a vector $c\in \mathbb {R} ^{n}$ and polynomials $a_{k,j}$ for $k=1,\dots N_{s}$ , $j=0,1,\dots ,n$ , a sum-of-squares optimization problem is written as

${\begin{aligned}{\underset {u\in \mathbb {R} ^{n}}{\text{maximize}}}\quad &c^{T}u\\{\text{subject to}}\quad &a_{k,0}(x)+a_{k,1}(x)u_{1}+\cdots +a_{k,n}(x)u_{n}\in {\text{SOS}}\quad (k=1,\ldots ,N_{s}).\end{aligned}}$

Here "SOS" represents the class of sum-of-squares (SOS) polynomials. The quantities $u\in \mathbb {R} ^{n}$ are the decision variables. SOS programs can be converted to semidefinite programs (SDPs) using the duality of the SOS polynomial program and a relaxation for constrained polynomial optimization using positive-semidefinite matrices, see the following section.

## Dual problem: constrained polynomial optimization

Consider a nonlinear optimization problem of the form ${\begin{aligned}&{\underset {x\in \mathbb {R} ^{n}}{\operatorname {minimize} }}&&p(x)\\&\operatorname {subject\;to} &&a_{i}(x)=0,\quad i=1,\dots ,m\end{aligned}}$

where $p(x):\mathbb {R} ^{n}\to \mathbb {R}$ is an *n*-variate polynomial and each $a_{i}(x)$ is an *n*-variate polynomial of degree at most 2*d*. The same problem can be rewritten as

| ${\begin{aligned}&{\underset {x\in \mathbb {R} ^{n}}{\operatorname {minimize} }}&&\langle C,x^{\leq d}(x^{\leq d})^{\top }\rangle \\&\operatorname {subject\;to} &&\langle A_{i},x^{\leq d}(x^{\leq d})^{\top }\rangle =0,\quad i=1,\dots ,m\\&&&x_{\emptyset }=1\end{aligned}}$ |   | 1 |
|---|---|---|

where ${\textstyle x^{\leq d}}$ is the $n^{O(d)}$ -dimensional vector with one entry for every monomial in *x* of degree at most *d*, so that for each multiset $S\subset [n],|S|\leq d,$ ${\textstyle x_{S}=\prod _{i\in S}x_{i}}$ , ${\textstyle C}$ is a Gram matrix *p*, and ${\textstyle A_{i}}$ is a Gram matrix of $a_{i}$ . We adopt the convention that $x_{\emptyset }=1$ , so that the constant coefficient can be included in the Gram matrix of a polynomial.

This problem is non-convex in general. One can try to relax the problem to a convex one using semidefinite programming to replace the rank-one matrix of variables $x^{\leq d}(x^{\leq d})^{\top }$ with a positive semidefinite matrix X : we index each monomial of size at most $2d$ by a multiset S of at most $2d$ indices, $S\subset [n],|S|\leq 2d$ . For each such monomial, we create a variable $X_{S}$ in the program, and we arrange the variables $X_{S}$ to form the matrix ${\textstyle X\in \mathbb {R} ^{[n]^{\leq d}\times [n]^{\leq d}}}$ , where $\mathbb {R} ^{[n]^{\leq d}\times [n]^{\leq d}}$ is the set of real matrices whose rows and columns are identified with multisets of elements from n of size at most d . We then write the following semidefinite program in the variables $X_{S}$ :

${\begin{aligned}&{\underset {X\in \mathbb {R} ^{[n]^{\leq d}\times [n]^{\leq d}}}{\operatorname {minimize} }}&&\langle C,X\rangle \\&\operatorname {subject\;to} &&X_{U,V}=X_{S,T},\quad \forall \ U,V,S,T\in [n]^{\leq d},U\cup V=S\cup T\\&&&\langle A_{i},X\rangle =0,\quad i=1,\dots ,m\\&&&X_{\emptyset }=1\\&&&X\succeq 0\end{aligned}}$

where again *C* is a Gram matrix of *p* and ${\textstyle A_{i}}$ is a Gram matrix of ${\textstyle a_{i}}$ . The first constraint ensures that the value of a monomial that appears several times within the matrix is equal throughout the matrix, and is added to make the matrix X respect the same symmetries present in the matrix $x^{\leq d}(x^{\leq d})^{\top }$ .

### Duality

One can take the dual of the above semidefinite program and obtain the following program:

${\begin{aligned}&{\underset {y\in \mathbb {R} ^{m'}}{\operatorname {minimize} }}&&y_{0}\\&\operatorname {subject\;to} &&C-y_{0}e_{\emptyset }-\sum _{i\in [m]}y_{i}A_{i}-\sum _{S\cup T=U\cup V}y_{S,T,U,V}(e_{S,T}-e_{U,V})\succeq 0\end{aligned}}$

We have a variable $y_{0}$ corresponding to the constraint $\langle e_{\emptyset },X\rangle =1$ (where $e_{\emptyset }$ is the matrix with all entries zero save for the entry indexed by $(\varnothing ,\varnothing )$ ), a real variable $y_{i}$ for each polynomial constraint $\langle X,A_{i}\rangle =0\quad s.t.i\in [m],$ and for each group of multisets $S,T,U,V\subset [n],|S|,|T|,|U|,|V|\leq d,S\cup T=U\cup V$ , we have a dual variable $y_{S,T,U,V}$ for the symmetry constraint $\langle X,e_{S,T}-e_{U,V}\rangle =0$ . The positive-semidefiniteness constraint ensures that $p(x)-y_{0}$ is a sum-of-squares of polynomials over $A\subset \mathbb {R} ^{n}$ : by a characterization of positive-semidefinite matrices, for any positive-semidefinite matrix ${\textstyle Q\in \mathbb {R} ^{m\times m}}$ , we can write ${\textstyle Q=\sum _{i\in [m]}f_{i}f_{i}^{\top }}$ for vectors ${\textstyle f_{i}\in \mathbb {R} ^{m}}$ . Thus for any ${\textstyle x\in A\subset \mathbb {R} ^{n}}$ , ${\begin{aligned}p(x)-y_{0}&=p(x)-y_{0}-\sum _{i\in [m']}y_{i}a_{i}(x)\qquad {\text{since }}x\in A\\&=(x^{\leq d})^{\top }\left(C-y_{0}e_{\emptyset }-\sum _{i\in [m']}y_{i}A_{i}-\sum _{S\cup T=U\cup V}y_{S,T,U,V}(e_{S,T}-e_{U,V})\right)x^{\leq d}\qquad {\text{by symmetry}}\\&=(x^{\leq d})^{\top }\left(\sum _{i}f_{i}f_{i}^{\top }\right)x^{\leq d}\\&=\sum _{i}\langle x^{\leq d},f_{i}\rangle ^{2}\\&=\sum _{i}f_{i}(x)^{2},\end{aligned}}$

where we have identified the vectors ${\textstyle f_{i}}$ with the coefficients of a polynomial of degree at most d . This gives a sum-of-squares proof that the value ${\textstyle p(x)\geq y_{0}}$ over $A\subset \mathbb {R} ^{n}$ .

The above can also be extended to regions $A\subset \mathbb {R} ^{n}$ defined by polynomial inequalities.

## Sum-of-squares hierarchy

The sum-of-squares hierarchy (SOS hierarchy), also known as the Lasserre hierarchy, is a hierarchy of convex relaxations of increasing power and increasing computational cost. For each natural number ${\textstyle d\in \mathbb {N} }$ the corresponding convex relaxation is known as the *${\textstyle d}$ th level* or *${\textstyle d}$ -th round of the SOS hierarchy.* The ${\textstyle 1}$ st round, when ${\textstyle d=1}$ , corresponds to a basic semidefinite program, or to sum-of-squares optimization over polynomials of degree at most 2 . To augment the basic convex program at the ${\textstyle 1}$ st level of the hierarchy to ${\textstyle d}$ -th level, additional variables and constraints are added to the program to have the program consider polynomials of degree at most $2d$ .

The SOS hierarchy derives its name from the fact that the value of the objective function at the ${\textstyle d}$ -th level is bounded with a sum-of-squares proof using polynomials of degree at most ${\textstyle 2d}$ via the dual (see "Duality" above). Consequently, any sum-of-squares proof that uses polynomials of degree at most ${\textstyle 2d}$ can be used to bound the objective value, allowing one to prove guarantees on the tightness of the relaxation.

In conjunction with a theorem of Berg, this further implies that given sufficiently many rounds, the relaxation becomes arbitrarily tight on any fixed interval. Berg's result states that every non-negative real polynomial within a bounded interval can be approximated within accuracy ${\textstyle \varepsilon }$ on that interval with a sum-of-squares of real polynomials of sufficiently high degree, and thus if ${\textstyle OBJ(x)}$ is the polynomial objective value as a function of the point ${\textstyle x}$ , if the inequality ${\textstyle c+\varepsilon -OBJ(x)\geq 0}$ holds for all ${\textstyle x}$ in the region of interest, then there must be a sum-of-squares proof of this fact. Choosing ${\textstyle c}$ to be the minimum of the objective function over the feasible region, we have the result.

### Computational cost

When optimizing over a function in ${\textstyle n}$ variables, the ${\textstyle d}$ -th level of the hierarchy can be written as a semidefinite program over ${\textstyle n^{O(d)}}$ variables, and can be solved in time ${\textstyle n^{O(d)}}$ using the ellipsoid method.

## Hermitian sum-of-squares optimization

A Hermitian polynomial is a function of n complex variables $z_{1},\dots ,z_{n}$ and their conjugates $z_{1}^{*},\dots ,z_{n}^{*}$ which takes on only real values for all complex z . One can also consider semidefinite programming relaxations based on Hermitian sums of squares (HSOS) $g_{1}^{*}g_{1}+\dots +g_{k}^{*}g_{k}$ where each $g_{i}$ is a polynomial in only the variables $z_{1},\dots ,z_{n}$ and not their conjugates. The resulting semidefinite programs converge to the true optimum asymptotically in all well-behaved cases and reduce to calculating the largest eigenvalues of explicitly given matrices, as first observed by Putinar.

## Software tools

- SOSTOOLS, licensed under the GNU GPL. The reference guide is available at arXiv:1310.4716 [math.OC], and a presentation about its internals is available here.
- CDCS-sos, a package from CDCS, an augmented Lagrangian method solver, to deal with large scale SOS programs.
- The SumOfSquares extension of JuMP for Julia.
- TSSOS for Julia, a polynomial optimization tool based on the sparsity adapted moment-SOS hierarchies.
- For the dual problem of constrained polynomial optimization, GloptiPoly for MATLAB/Octave, Ncpol2sdpa for Python and MomentOpt for Julia.
