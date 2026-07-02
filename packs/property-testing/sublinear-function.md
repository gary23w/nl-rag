---
title: "Sublinear function"
source: https://en.wikipedia.org/wiki/Sublinear_function
domain: property-testing
license: CC-BY-SA-4.0
tags: property testing, sublinear verification, locally testable code, graph property tester
fetched: 2026-07-02
---

# Sublinear function

In linear algebra, a **sublinear** function (or functional as is more often used in functional analysis), also called a **quasi-seminorm**, on a vector space is a real-valued function with some of the properties of a seminorm. Unlike seminorms, a sublinear function does not have to be nonnegative-valued and also does not have to be absolutely homogeneous. Seminorms are themselves abstractions of the more well known notion of norms, where a seminorm has all the defining properties of a norm *except* that it is not required to map non-zero vectors to non-zero values.

In functional analysis the name **Banach functional** is sometimes used, reflecting that they are most commonly used when applying a general formulation of the Hahn–Banach theorem. The notion of a sublinear function was introduced by Stefan Banach when he proved the Hahn-Banach theorem.

There is also a different notion in computer science, described below, that also goes by the name "sublinear function."

## Definitions

Let X be a vector space over a field $\mathbb {K} ,$ where $\mathbb {K}$ is either the real numbers $\mathbb {R}$ or complex numbers $\mathbb {C} .$ A function $p\colon X\to \mathbb {R}$ is called a **sublinear** if it has these two properties:

1. Positive homogeneity, that is $p(rx)=rp(x)$ , for all $r\geq 0$ and $x\in X$ .
2. Subadditivity, that is $p(x+y)\leq p(x)+p(y)$ for $x,y\in X.$

A function $p:X\to \mathbb {R}$ is called *positive* or *nonnegative* if $p(x)\geq 0$ for all $x\in X,$ although some authors define *positive* to instead mean that $p(x)\neq 0$ whenever $x\neq 0;$ these definitions are not equivalent. It is a *symmetric function* if $p(-x)=p(x)$ for all $x\in X.$ Every subadditive symmetric function is necessarily nonnegative. A sublinear function on a real vector space is symmetric if and only if it is a seminorm. A sublinear function on a real or complex vector space is a seminorm if and only if it is a balanced function or equivalently, if and only if $p(ux)\leq p(x)$ for every unit length scalar u and $x\in X.$

The set of all sublinear functions on $X,$ denoted by $X^{\#},$ can be partially ordered by declaring $p\leq q$ if and only if $p(x)\leq q(x)$ for all $x\in X.$ A sublinear function is called **minimal** if it is a minimal element of $X^{\#}$ under this order. A sublinear function is minimal if and only if it is a real linear functional.

## Examples and sufficient conditions

Every norm, seminorm, and real linear functional is a sublinear function. The identity function on $\mathbb {R}$ is an example of a sublinear function (in fact, it is even a linear functional) that is neither positive nor a seminorm; the same is true of this map's negation $x\mapsto -x.$ More generally, for any real $a\leq b,$ the map

$S_{a,b}\colon \mathbb {R} \to \mathbb {R} ,\quad x\mapsto {\begin{cases}ax,&{\text{if }}x\leq 0,\\bx,&{\text{if }}x\geq 0\end{cases}}$

is a sublinear function on $\mathbb {R}$ and moreover, every sublinear function $p\colon \mathbb {R} \to \mathbb {R}$ is of this form; specifically, if $a=-p(-1)$ and $b=p(1)$ then $a\leq b$ and $p=S_{a,b}.$

If p and q are sublinear functions on a real vector space X then so is the map $x\mapsto \max\{p(x),q(x)\}.$ More generally, if ${\mathcal {P}}$ is any non-empty collection of sublinear functionals on a real vector space X and if for all $x\in X,$ $q(x)=\sup\{p(x)\,;\,p\in {\mathcal {P}}\},$ then q is a sublinear functional on $X.$

A function $p\colon X\to \mathbb {R}$ which is subadditive, convex, and satisfies $p(0)\leq 0$ is also positively homogeneous (the latter condition $p(0)\leq 0$ is necessary as the example of $p(x)={\sqrt {x^{2}+1}}$ on $X=\mathbb {R}$ shows). If p is positively homogeneous, it is convex if and only if it is subadditive. Therefore, assuming $p(0)\leq 0$ , any two properties among subadditivity, convexity, and positive homogeneity implies the third.

## Properties

Every sublinear function is a convex function: For $0\leq t\leq 1,$ ${\begin{alignedat}{3}p(tx+(1-t)y)&\leq p(tx)+p((1-t)y)&&\quad {\text{ subadditivity}}\\&=tp(x)+(1-t)p(y)&&\quad {\text{ nonnegative homogeneity}}\\\end{alignedat}}$

If $p:X\to \mathbb {R}$ is a sublinear function on a vector space X then $p(0)~=~0~\leq ~p(x)+p(-x),$ for every $x\in X,$ which implies that at least one of $p(x)$ and $p(-x)$ must be nonnegative; that is, for every $x\in X,$ $0~\leq ~\max\{p(x),p(-x)\}.$ Moreover, when $p:X\to \mathbb {R}$ is a sublinear function on a real vector space then the map $q:X\to \mathbb {R}$ defined by $q(x)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\max\{p(x),p(-x)\}$ is a seminorm.

Subadditivity of $p:X\to \mathbb {R}$ guarantees that for all vectors $x,y\in X,$ $p(x)-p(y)~\leq ~p(x-y),$ $-p(x)~\leq ~p(-x),$ so if p is also symmetric then the reverse triangle inequality will hold for all vectors $x,y\in X,$ $|p(x)-p(y)|~\leq ~p(x-y).$

Defining $\ker p~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~p^{-1}(0),$ then subadditivity also guarantees that for all $x\in X,$ the value of p on the set $x+(\ker p\cap -\ker p)=\{x+k:p(k)=0=p(-k)\}$ is constant and equal to $p(x).$ In particular, if $\ker p=p^{-1}(0)$ is a vector subspace of X then $-\ker p=\ker p$ and the assignment $x+\ker p\mapsto p(x),$ which will be denoted by ${\hat {p}},$ is a well-defined real-valued sublinear function on the quotient space $X\,/\,\ker p$ that satisfies ${\hat {p}}^{-1}(0)=\ker p.$ If p is a seminorm then ${\hat {p}}$ is just the usual canonical norm on the quotient space $X\,/\,\ker p.$

**Pryce's sublinearity lemma**—Suppose $p:X\to \mathbb {R}$ is a sublinear functional on a vector space X and that $K\subseteq X$ is a non-empty convex subset. If $x\in X$ is a vector and $a,c>0$ are positive real numbers such that $p(x)+ac~<~\inf _{k\in K}p(x+ak)$ then for every positive real $b>0$ there exists some $\mathbf {z} \in K$ such that $p(x+a\mathbf {z} )+bc~<~\inf _{k\in K}p(x+a\mathbf {z} +bk).$

Adding $bc$ to both sides of the hypothesis ${\textstyle p(x)+ac\,<\,\inf _{}p(x+aK)}$ (where $p(x+aK)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{p(x+ak):k\in K\}$ ) and combining that with the conclusion gives $p(x)+ac+bc~<~\inf _{}p(x+aK)+bc~\leq ~p(x+a\mathbf {z} )+bc~<~\inf _{}p(x+a\mathbf {z} +bK)$ which yields many more inequalities, including, for instance, $p(x)+ac+bc~<~p(x+a\mathbf {z} )+bc~<~p(x+a\mathbf {z} +b\mathbf {z} )$ in which an expression on one side of a strict inequality $\,<\,$ can be obtained from the other by replacing the symbol c with $\mathbf {z}$ (or vice versa) and moving the closing parenthesis to the right (or left) of an adjacent summand (all other symbols remain fixed and unchanged).

### Associated seminorm

If $p:X\to \mathbb {R}$ is a real-valued sublinear function on a real vector space X (or if X is complex, then when it is considered as a real vector space) then the map $q(x)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\max\{p(x),p(-x)\}$ defines a seminorm on the real vector space X called the **seminorm associated with $p.$** A sublinear function p on a real or complex vector space is a symmetric function if and only if $p=q$ where $q(x)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\max\{p(x),p(-x)\}$ as before.

More generally, if $p:X\to \mathbb {R}$ is a real-valued sublinear function on a (real or complex) vector space X then $q(x)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\sup _{|u|=1}p(ux)~=~\sup\{p(ux):u{\text{ is a unit scalar }}\}$ will define a seminorm on X if this supremum is always a real number (that is, never equal to $\infty$ ).

### Relation to linear functionals

If p is a sublinear function on a real vector space X then the following are equivalent:

1. p is a linear functional.
2. for every $x\in X,$ $p(x)+p(-x)\leq 0.$
3. for every $x\in X,$ $p(x)+p(-x)=0.$
4. p is a minimal sublinear function.

If p is a sublinear function on a real vector space X then there exists a linear functional f on X such that $f\leq p.$

If X is a real vector space, f is a linear functional on $X,$ and p is a positive sublinear function on $X,$ then $f\leq p$ on X if and only if $f^{-1}(1)\cap \{x\in X:p(x)<1\}=\varnothing .$

#### Dominating a linear functional

A real-valued function f defined on a subset of a real or complex vector space X is said to be *dominated by* a sublinear function p if $f(x)\leq p(x)$ for every x that belongs to the domain of $f.$ If $f:X\to \mathbb {R}$ is a real linear functional on X then f is dominated by p (that is, $f\leq p$ ) if and only if $-p(-x)\leq f(x)\leq p(x)\quad {\text{ for every }}x\in X.$ Moreover, if p is a seminorm or some other *symmetric map* (which by definition means that $p(-x)=p(x)$ holds for all x ) then $f\leq p$ if and only if $|f|\leq p.$

**Theorem**—If $p:X\to \mathbb {R}$ be a sublinear function on a real vector space X and if $z\in X$ then there exists a linear functional f on X that is dominated by p (that is, $f\leq p$ ) and satisfies $f(z)=p(z).$ Moreover, if X is a topological vector space and p is continuous at the origin then f is continuous.

### Continuity

**Theorem**—Suppose $f:X\to \mathbb {R}$ is a subadditive function (that is, $f(x+y)\leq f(x)+f(y)$ for all $x,y\in X$ ). Then f is continuous at the origin if and only if f is uniformly continuous on $X.$ If f satisfies $f(0)=0$ then f is continuous if and only if its absolute value $|f|:X\to [0,\infty )$ is continuous. If f is non-negative then f is continuous if and only if $\{x\in X:f(x)<1\}$ is open in $X.$

Suppose X is a topological vector space (TVS) over the real or complex numbers and p is a sublinear function on $X.$ Then the following are equivalent:

1. p is continuous;
2. p is continuous at 0;
3. p is uniformly continuous on X ;

and if p is positive then this list may be extended to include:

1. $\{x\in X:p(x)<1\}$ is open in $X.$

If X is a real TVS, f is a linear functional on $X,$ and p is a continuous sublinear function on $X,$ then $f\leq p$ on X implies that f is continuous.

### Relation to Minkowski functions and open convex sets

**Theorem**—If U is a convex open neighborhood of the origin in a topological vector space X then the Minkowski functional of $U,$ $p_{U}:X\to [0,\infty ),$ is a continuous non-negative sublinear function on X such that $U=\left\{x\in X:p_{U}(x)<1\right\};$ if in addition U is a balanced set then $p_{U}$ is a seminorm on $X.$

#### Relation to open convex sets

**Theorem**—Suppose that X is a topological vector space (not necessarily locally convex or Hausdorff) over the real or complex numbers. Then the open convex subsets of X are exactly those that are of the form $z+\{x\in X:p(x)<1\}=\{x\in X:p(x-z)<1\}$ for some $z\in X$ and some positive continuous sublinear function p on $X.$

Proof

Let V be an open convex subset of $X.$ If $0\in V$ then let $z:=0$ and otherwise let $z\in V$ be arbitrary. Let $p:X\to [0,\infty )$ be the Minkowski functional of $V-z,$ which is a continuous sublinear function on X since $V-z$ is convex, absorbing, and open ( p however is not necessarily a seminorm since V was not assumed to be balanced). From $X=X-z,$ it follows that $z+\{x\in X:p(x)<1\}=\{x\in X:p(x-z)<1\}.$ It will be shown that $V=z+\{x\in X:p(x)<1\},$ which will complete the proof. One of the known properties of Minkowski functionals guarantees ${\textstyle \{x\in X:p(x)<1\}=(0,1)(V-z),}$ where $(0,1)(V-z)\;{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\;\{tx:0<t<1,x\in V-z\}=V-z$ since $V-z$ is convex and contains the origin. Thus $V-z=\{x\in X:p(x)<1\},$ as desired. $\blacksquare$

## Operators

The concept can be extended to operators that are homogeneous and subadditive. This requires only that the codomain be, say, an ordered vector space to make sense of the conditions.

## Computer science definition

In computer science, a function $f:\mathbb {Z} ^{+}\to \mathbb {R}$ is called **sublinear** if $\lim _{n\to \infty }{\frac {f(n)}{n}}=0,$ or $f(n)\in o(n)$ in asymptotic notation (notice the small o ). Formally, $f(n)\in o(n)$ if and only if, for any given $c>0,$ there exists an N such that $f(n)<cn$ for $n\geq N.$ That is, f grows slower than any linear function. The two meanings should not be confused: while a Banach functional is convex, almost the opposite is true for functions of sublinear growth: every function $f(n)\in o(n)$ can be upper-bounded by a concave function of sublinear growth.
