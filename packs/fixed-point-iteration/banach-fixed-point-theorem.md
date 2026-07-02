---
title: "Banach fixed-point theorem"
source: https://en.wikipedia.org/wiki/Banach_fixed-point_theorem
domain: fixed-point-iteration
license: CC-BY-SA-4.0
tags: fixed-point iteration, banach fixed-point theorem, contraction mapping, anderson acceleration
fetched: 2026-07-02
---

# Banach fixed-point theorem

In mathematics, the **Banach fixed-point theorem** (also known as the **contraction mapping theorem** or **contractive mapping theorem** or **Banach–Caccioppoli theorem**) is an important tool in the theory of metric spaces; it guarantees the existence and uniqueness of fixed points of certain self-maps of metric spaces and provides a constructive method to find those fixed points. It can be understood as an abstract formulation of Picard's method of successive approximations. The theorem is named after Stefan Banach (1892–1945) who first stated it in 1922.

## Statement

*Definition.* Let $(X,d)$ be a metric space with metric $d(x,y)$ . Then a map $T:X\to X$ is called a contraction mapping on X if there exists a nonnegative constant $q<1$ such that

$d(T(x),T(y))\leq q\,d(x,y)$

for all $x,y\in X.$

> **Banach fixed-point theorem.** Let $(X,d)$ be a non-empty complete metric space with a contraction mapping $T:X\to X.$ Then T admits a unique fixed point $x^{*}\in X$ , meaning $T(x^{*})=x^{*}$ . Furthermore, $x^{*}$ can be found as follows: start with an arbitrary element $x_{0}\in X$ and define $x_{n}=T(x_{n-1})$ for $n\geq 1.$ Then $\lim _{n\to \infty }x_{n}=x^{*}$ .

*Remark 1.* The following inequalities are equivalent and describe the speed of convergence:

${\begin{aligned}d(x^{*},x_{n})&\leq q^{n}d(x^{*},x_{0}),\\[5pt]d(x^{*},x_{n})&\leq {\frac {q^{n}}{1-q}}d(x_{1},x_{0}),\\[5pt]d(x^{*},x_{n+1})&\leq {\frac {q}{1-q}}d(x_{n+1},x_{n}),\\[5pt]d(x^{*},x_{n+1})&\leq q\,d(x^{*},x_{n}).\end{aligned}}$

The value q is called a *Lipschitz constant* for T , and a minimal such q is sometimes called "the best Lipschitz constant" of T .

*Remark 2.* The condition $d(T(x),T(y))<d(x,y)$ for all $x\neq y$ is in general not enough to ensure the existence of a fixed point, as is shown by the map $T:[1,\infty )\to [1,\infty ),\,\,T(x)=x+{\tfrac {1}{x}}\,,$ which lacks a fixed point. However, if X is compact, then this weaker condition does imply the existence and uniqueness of a fixed point which can be easily found as a minimizer of $d(x,T(x))$ : indeed, a minimizer exists by compactness, and must be a fixed point. It then easily follows that the fixed point is the limit of any sequence of iterations of T .

*Remark 3.* When using the theorem in practice, the most difficult part is typically to define X properly so that $T(X)\subseteq X$ .

## Proof

Let $x_{0}\in X$ be arbitrary and define a sequence $(x_{n})_{n\in \mathbb {N} }$ by setting $x_{n}=T(x_{n-1})$ . We first note that for all $n\in \mathbb {N} ,$ we have the inequality

$d(x_{n+1},x_{n})\leq q^{n}d(x_{1},x_{0}).$

This follows by induction on n , using the fact that T is a contraction mapping. Then we can show that $(x_{n})_{n\in \mathbb {N} }$ is a Cauchy sequence. In particular, let $m,n\in \mathbb {N}$ such that $m>n$ :

${\begin{aligned}d(x_{m},x_{n})&\leq d(x_{m},x_{m-1})+d(x_{m-1},x_{m-2})+\cdots +d(x_{n+1},x_{n})\\[5pt]&\leq q^{m-1}d(x_{1},x_{0})+q^{m-2}d(x_{1},x_{0})+\cdots +q^{n}d(x_{1},x_{0})\\[5pt]&=q^{n}d(x_{1},x_{0})\sum _{k=0}^{m-n-1}q^{k}\\[5pt]&\leq q^{n}d(x_{1},x_{0})\sum _{k=0}^{\infty }q^{k}\\[5pt]&=q^{n}d(x_{1},x_{0})\left({\frac {1}{1-q}}\right).\end{aligned}}$

Let $\varepsilon >0$ be arbitrary. Since $q\in [0,1)$ , we can find a large $N\in \mathbb {N}$ so that

$q^{N}<{\frac {\varepsilon (1-q)}{d(x_{1},x_{0})}}.$

Therefore, by choosing m and n greater than N we may write:

$d(x_{m},x_{n})\leq q^{n}d(x_{1},x_{0})\left({\frac {1}{1-q}}\right)<\left({\frac {\varepsilon (1-q)}{d(x_{1},x_{0})}}\right)d(x_{1},x_{0})\left({\frac {1}{1-q}}\right)=\varepsilon .$

This proves that the sequence $(x_{n})_{n\in \mathbb {N} }$ is Cauchy. By completeness of $(X,d)$ , the sequence has a limit $x^{*}\in X.$ Furthermore, $x^{*}$ must be a fixed point of T :

$x^{*}=\lim _{n\to \infty }x_{n}=\lim _{n\to \infty }T(x_{n-1})=T\left(\lim _{n\to \infty }x_{n-1}\right)=T(x^{*}).$

As a contraction mapping, T is continuous, so bringing the limit inside T was justified. Lastly, T cannot have more than one fixed point in $(X,d)$ , since any pair of distinct fixed points $p_{1}$ and $p_{2}$ would contradict the contraction of T :

$d(p_{1},p_{2})=d(T(p_{1}),T(p_{2}))\leq qd(p_{1},p_{2})<d(p_{1},p_{2}),$

where the equality is due to $p_{1},p_{2}$ being fixed points of T , the first inequality is due to T being a contraction mapping, and the last inequality is due to $q<1$ and $d(p_{1},p_{2})>0$ as $p_{1}\neq p_{2}$ .

## Applications

- A standard application is the proof of the Picard–Lindelöf theorem about the existence and uniqueness of solutions to certain ordinary differential equations. The sought solution of the differential equation is expressed as a fixed point of a suitable integral operator on the space of continuous functions under the uniform norm. The Banach fixed-point theorem is then used to show that this integral operator has a unique fixed point.
- One consequence of the Banach fixed-point theorem is that small Lipschitz perturbations of the identity are bi-lipschitz homeomorphisms. Let $\Omega$ be an open set of a Banach space E ; let $I:\Omega \rightarrow E$ denote the identity (inclusion) map and let $g:\Omega \rightarrow E$ be a Lipschitz map of constant $k<1$ . Then

1. $\Omega ':=(I+g)\Omega$ is an open subset of E : precisely, for any x in $\Omega$ such that $B(x,r)\subset \Omega$ one has $B((I+g)(x),r(1-k))\subset \Omega '$ ;
2. $I+g:\Omega \rightarrow \Omega '$ is a bi-Lipschitz homeomorphism;

precisely,

$(I+g)^{-1}$

is still of the form

$I+h:\Omega \rightarrow \Omega '$

with

h

a Lipschitz map of constant

$k/(1-k)$

. A direct consequence of this result yields the proof of the

inverse function theorem

.

- It can be used to give sufficient conditions under which Newton's method of successive approximations is guaranteed to work, and similarly for Chebyshev's third-order method.
- It can be used to prove existence and uniqueness of solutions to integral equations.
- It can be used to give a proof to the Nash embedding theorem.
- It can be used to prove existence and uniqueness of solutions to value iteration, policy iteration, and policy evaluation of reinforcement learning.
- It can be used to prove existence and uniqueness of an equilibrium in Cournot competition, and other dynamic economic models.
- If *X* is a vector space, an alternative method for iteratively approximating the fixed point is to apply Newton's method to solve $f(x)-x=0$ .
- One real world illustration of the theorem is the following demonstration that can often be understood with little formal mathematics background. Suppose a person holds a sheet of paper on which is printed a map of the city they are in (or a map of their country, or a blueprint of the building they are in, etc.). The person then places the map on the floor. This can be considered to represent a continuous function from the city to itself and is clearly a contraction. Therefore, there is exactly one point in the map that lies directly above the point that it represents. The accuracy of the map and projection method do not matter as long as the map is complete and all points represented are moved closer together in the projection. What's more, should the person scrunch the map up into a ball and flatten it on the floor, as long as the paper does not tear, this will still be a contraction and the same conclusion can be reached.

## Converses

Several converses of the Banach contraction principle exist. The following is due to Czesław Bessaga, from 1959:

Let $f:X\rightarrow X$ be a map of an abstract set such that each iterate $f^{n}$ has a unique fixed point. Let $q\in (0,1)$ , then there exists a complete metric on X such that f is contractive, and q is the contraction constant.

Indeed, very weak assumptions suffice to obtain such a kind of converse. For example if $f:X\to X$ is a map on a *T*1 topological space with a unique fixed point a , such that for each $x\in X$ we have $f^{n}(x)\rightarrow a$ , then there already exists a metric on X with respect to which f satisfies the conditions of the Banach contraction principle with contraction constant $1/2$ . In this case the metric is in fact an ultrametric.

## Generalizations

There are a number of generalizations (some of which are immediate corollaries).

Let $T:X\rightarrow X$ be a map on a complete non-empty metric space. Then, for example, some generalizations of the Banach fixed-point theorem are:

- Assume that some iterate $T^{n}$ of T is a contraction. Then T has a unique fixed point.
- Assume that for each n , there exist $c_{n}$ such that $d(T^{n}(x),T^{n}(y))\leq c_{n}d(x,y)$ for all x and y , and that

$\sum \nolimits _{n}c_{n}<\infty .$

Then

T

has a unique fixed point.

In applications, the existence and uniqueness of a fixed point often can be shown directly with the standard Banach fixed point theorem, by a suitable choice of the metric that makes the map T a contraction. Indeed, the above result by Bessaga strongly suggests to look for such a metric. See also the article on fixed point theorems in infinite-dimensional spaces for generalizations.

In a non-empty compact metric space, any function T satisfying $d(T(x),T(y))<d(x,y)$ for all distinct $x,y$ , has a unique fixed point. The proof is simpler than the Banach theorem, because the function $d(T(x),x)$ is continuous, and therefore assumes a minimum, which is easily shown to be zero.

A different class of generalizations arise from suitable generalizations of the notion of metric space, e.g. by weakening the defining axioms for the notion of metric. Some of these have applications, e.g., in the theory of programming semantics in theoretical computer science.

## Example

An application of the Banach fixed-point theorem and fixed-point iteration can be used to quickly obtain an approximation of $\pi$ with high accuracy. Consider the function $f(x)=x+\sin(x)$ . It can be verified that $\pi$ is a fixed point of f , and that f maps the interval $\left[{\frac {3\pi }{4}},{\frac {5\pi }{4}}\right]$ to itself. Moreover, $f^{\prime }(x)=1+\cos(x)$ , and it can be verified that

$0\leqslant 1+\cos(x)\leqslant 1-{\frac {1}{{\sqrt {2\,}}\,}}\approx 0.292893<1$

on this interval. Therefore, by an application of the mean value theorem, f has a Lipschitz constant less than 1 (namely $1-1/{\sqrt {2}}$ ). Applying the Banach fixed-point theorem shows that the fixed point $\pi$ is the unique fixed point on the interval, allowing for fixed-point iteration to be used.

For example, the value 3 may be chosen to start the fixed-point iteration, as ${\frac {3\pi }{4}}\leqslant 3\leqslant {\frac {5\pi }{4}}$ . The Banach fixed-point theorem may be used to conclude that

$\pi =f\!{\bigg (}f\!{\Big (}f\!{\big (}\cdots f(3)\cdots {\big )}{\Big )}{\bigg )}={\big (}f\circ \cdots \circ f{\big )}(3).$

Applying f to 3 only thrice already yields an expansion of $\pi$ accurate up to $33$ digits:

${\begin{matrix}\operatorname {id} (3)&=&f^{[0]}\!(3)&=&{\boldsymbol {3.}}0000000000000000000000000000000000\cdots \\f(3)&=&f^{[1]}\!(3)&=&{\boldsymbol {3.141}}1200080598672221007448028081103\cdots \\f{\big (}f(3){\big )}&=&f^{[2]}\!(3)&=&{\boldsymbol {3.1415926535}}721955587348885681408797\cdots \\f{\Big (}f{\big (}f(3){\big )}{\Big )}&=&f^{[3]}\!(3)&=&{\boldsymbol {3.14159265358979323846264338327950}}20\cdots \end{matrix}}$
