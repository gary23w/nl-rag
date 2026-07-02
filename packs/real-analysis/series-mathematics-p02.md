---
title: "Series (mathematics) (part 2/2)"
source: https://en.wikipedia.org/wiki/Series_(mathematics)
domain: real-analysis
license: CC-BY-SA-4.0
tags: real analysis, uniform convergence, riemann integral, metric space
fetched: 2026-07-02
part: 2/2
---

## Summations over general index sets

Definitions may be given for infinitary sums over an arbitrary index set $I.$ This generalization introduces two main differences from the usual notion of series: first, there may be no specific order given on the set I ; second, the set I may be uncountable. The notions of convergence need to be reconsidered for these, then, because for instance the concept of conditional convergence depends on the ordering of the index set.

If $a:I\mapsto G$ is a function from an index set I to a set $G,$ then the "series" associated to a is the formal sum of the elements $a(x)\in G$ over the index elements $x\in I$ denoted by the

$\sum _{x\in I}a(x).$

When the index set is the natural numbers $I=\mathbb {N} ,$ the function $a:\mathbb {N} \mapsto G$ is a sequence denoted by $a(n)=a_{n}.$ A series indexed on the natural numbers is an ordered formal sum and so we rewrite ${\textstyle \sum _{n\in \mathbb {N} }}$ as ${\textstyle \sum _{n=0}^{\infty }}$ in order to emphasize the ordering induced by the natural numbers. Thus, we obtain the common notation for a series indexed by the natural numbers

$\sum _{n=0}^{\infty }a_{n}=a_{0}+a_{1}+a_{2}+\cdots .$

### Families of non-negative numbers

When summing a family $\left\{a_{i}:i\in I\right\}$ of non-negative real numbers over the index set I , define

$\sum _{i\in I}a_{i}=\sup {\biggl \{}\sum _{i\in A}a_{i}\,:A\subseteq I,A{\text{ finite}}{\biggr \}}\in [0,+\infty ].$

Any sum over non-negative reals can be understood as the integral of a non-negative function with respect to the counting measure, which accounts for the many similarities between the two constructions.

When the supremum is finite then the set of $i\in I$ such that $a_{i}>0$ is countable. Indeed, for every $n\geq 1,$ the cardinality $\left|A_{n}\right|$ of the set $A_{n}=\left\{i\in I:a_{i}>1/n\right\}$ is finite because

${\frac {1}{n}}\,\left|A_{n}\right|=\sum _{i\in A_{n}}{\frac {1}{n}}\leq \sum _{i\in A_{n}}a_{i}\leq \sum _{i\in I}a_{i}<\infty .$

Hence the set $A=\left\{i\in I:a_{i}>0\right\}=\bigcup _{n=1}^{\infty }A_{n}$ is countable.

If I is countably infinite and enumerated as $I=\left\{i_{0},i_{1},\ldots \right\}$ then the above defined sum satisfies

$\sum _{i\in I}a_{i}=\sum _{k=0}^{\infty }a_{i_{k}},$ provided the value $\infty$ is allowed for the sum of the series.

### Abelian topological groups

Let $a:I\to X$ be a map, also denoted by $\left(a_{i}\right)_{i\in I},$ from some non-empty set I into a Hausdorff abelian topological group $X.$ Let $\operatorname {Finite} (I)$ be the collection of all finite subsets of $I,$ with $\operatorname {Finite} (I)$ viewed as a directed set, ordered under inclusion $\,\subseteq \,$ with union as join. The family $\left(a_{i}\right)_{i\in I},$ is said to be *unconditionally summable* if the following limit, which is denoted by $\textstyle \sum _{i\in I}a_{i}$ and is called the *sum* of $\left(a_{i}\right)_{i\in I},$ exists in $X:$

$\sum _{i\in I}a_{i}:=\lim _{A\in \operatorname {Finite} (I)}\ \sum _{i\in A}a_{i}=\lim {\biggl \{}\sum _{i\in A}a_{i}\,:A\subseteq I,A{\text{ finite }}{\biggr \}}$ Saying that the sum $\textstyle S:=\sum _{i\in I}a_{i}$ is the limit of finite partial sums means that for every neighborhood V of the origin in $X,$ there exists a finite subset $A_{0}$ of I such that

$S-\sum _{i\in A}a_{i}\in V\qquad {\text{ for every finite superset}}\;A\supseteq A_{0}.$

Because $\operatorname {Finite} (I)$ is not totally ordered, this is not a limit of a sequence of partial sums, but rather of a net.

For every neighborhood W of the origin in $X,$ there is a smaller neighborhood V such that $V-V\subseteq W.$ It follows that the finite partial sums of an unconditionally summable family $\left(a_{i}\right)_{i\in I},$ form a *Cauchy net*, that is, for every neighborhood W of the origin in $X,$ there exists a finite subset $A_{0}$ of I such that

$\sum _{i\in A_{1}}a_{i}-\sum _{i\in A_{2}}a_{i}\in W\qquad {\text{ for all finite supersets }}\;A_{1},A_{2}\supseteq A_{0},$ which implies that $a_{i}\in W$ for every $i\in I\setminus A_{0}$ (by taking $A_{1}:=A_{0}\cup \{i\}$ and $A_{2}:=A_{0}$ ).

When X is complete, a family $\left(a_{i}\right)_{i\in I}$ is unconditionally summable in X if and only if the finite sums satisfy the latter Cauchy net condition. When X is complete and $\left(a_{i}\right)_{i\in I},$ is unconditionally summable in $X,$ then for every subset $J\subseteq I,$ the corresponding subfamily $\left(a_{j}\right)_{j\in J},$ is also unconditionally summable in $X.$

When the sum of a family of non-negative numbers, in the extended sense defined before, is finite, then it coincides with the sum in the topological group $X=\mathbb {R} .$

If a family $\left(a_{i}\right)_{i\in I}$ in X is unconditionally summable then for every neighborhood W of the origin in $X,$ there is a finite subset $A_{0}\subseteq I$ such that $a_{i}\in W$ for every index i not in $A_{0}.$ If X is a first-countable space then it follows that the set of $i\in I$ such that $a_{i}\neq 0$ is countable. This need not be true in a general abelian topological group (see examples below).

### Unconditionally convergent series

Suppose that $I=\mathbb {N} .$ If a family $a_{n},n\in \mathbb {N} ,$ is unconditionally summable in a Hausdorff abelian topological group $X,$ then the series in the usual sense converges and has the same sum,

$\sum _{n=0}^{\infty }a_{n}=\sum _{n\in \mathbb {N} }a_{n}.$

By nature, the definition of unconditional summability is insensitive to the order of the summation. When $\textstyle \sum a_{n}$ is unconditionally summable, then the series remains convergent after any permutation $\sigma :\mathbb {N} \to \mathbb {N}$ of the set $\mathbb {N}$ of indices, with the same sum,

$\sum _{n=0}^{\infty }a_{\sigma (n)}=\sum _{n=0}^{\infty }a_{n}.$

Conversely, if every permutation of a series $\textstyle \sum a_{n}$ converges, then the series is unconditionally convergent. When X is complete then unconditional convergence is also equivalent to the fact that all subseries are convergent; if X is a Banach space, this is equivalent to say that for every sequence of signs $\varepsilon _{n}=\pm 1$ , the series

$\sum _{n=0}^{\infty }\varepsilon _{n}a_{n}$

converges in $X.$

### Series in topological vector spaces

If X is a topological vector space (TVS) and $\left(x_{i}\right)_{i\in I}$ is a (possibly uncountable) family in X then this family is **summable** if the limit $\textstyle \lim _{A\in \operatorname {Finite} (I)}x_{A}$ of the net $\left(x_{A}\right)_{A\in \operatorname {Finite} (I)}$ exists in $X,$ where $\operatorname {Finite} (I)$ is the directed set of all finite subsets of I directed by inclusion $\,\subseteq \,$ and ${\textstyle x_{A}:=\sum _{i\in A}x_{i}.}$

It is called **absolutely summable** if in addition, for every continuous seminorm p on $X,$ the family $\left(p\left(x_{i}\right)\right)_{i\in I}$ is summable. If X is a normable space and if $\left(x_{i}\right)_{i\in I}$ is an absolutely summable family in $X,$ then necessarily all but a countable collection of $x_{i}$ ’s are zero. Hence, in normed spaces, it is usually only ever necessary to consider series with countably many terms.

Summable families play an important role in the theory of nuclear spaces.

### Series in Banach and seminormed spaces

The notion of series can be easily extended to the case of a seminormed space. If $x_{n}$ is a sequence of elements of a normed space X and if $x\in X$ then the series $\textstyle \sum x_{n}$ converges to x in X if the sequence of partial sums of the series ${\textstyle {\bigl (}\!\!~\sum _{n=0}^{N}x_{n}{\bigr )}_{N=1}^{\infty }}$ converges to x in X ; to wit,

${\Biggl \|}x-\sum _{n=0}^{N}x_{n}{\Biggr \|}\to 0\quad {\text{ as }}N\to \infty .$

More generally, convergence of series can be defined in any abelian Hausdorff topological group. Specifically, in this case, $\textstyle \sum x_{n}$ converges to x if the sequence of partial sums converges to $x.$

If $(X,|\cdot |)$ is a seminormed space, then the notion of absolute convergence becomes: A series ${\textstyle \sum _{i\in I}x_{i}}$ of vectors in X **converges absolutely** if

$\sum _{i\in I}\left|x_{i}\right|<+\infty$

in which case all but at most countably many of the values $\left|x_{i}\right|$ are necessarily zero.

If a countable series of vectors in a Banach space converges absolutely then it converges unconditionally, but the converse only holds in finite-dimensional Banach spaces (theorem of Dvoretzky & Rogers (1950)).

### Well-ordered sums

Conditionally convergent series can be considered if I is a well-ordered set, for example, an ordinal number $\alpha _{0}.$ In this case, define by transfinite recursion:

$\sum _{\beta <\alpha +1}\!a_{\beta }=a_{\alpha }+\sum _{\beta <\alpha }a_{\beta }$

and for a limit ordinal $\alpha ,$

$\sum _{\beta <\alpha }a_{\beta }=\lim _{\gamma \to \alpha }\,\sum _{\beta <\gamma }a_{\beta }$

if this limit exists. If all limits exist up to $\alpha _{0},$ then the series converges.

### Examples

- Given a function $f:X\to Y$ into an abelian topological group $Y,$ define for every $a\in X,$ $f_{a}(x)={\begin{cases}0&x\neq a,\\f(a)&x=a,\\\end{cases}}$ a function whose support is a singleton $\{a\}.$ Then $f=\sum _{a\in X}f_{a}$ in the topology of pointwise convergence (that is, the sum is taken in the infinite product group $\textstyle Y^{X}$ ).
- In the definition of partitions of unity, one constructs sums of functions over arbitrary index set $I,$ $\sum _{i\in I}\varphi _{i}(x)=1.$ While, formally, this requires a notion of sums of uncountable series, by construction there are, for every given $x,$ only finitely many nonzero terms in the sum, so issues regarding convergence of such sums do not arise. Actually, one usually assumes more: the family of functions is *locally finite*, that is, for every x there is a neighborhood of x in which all but a finite number of functions vanish. Any regularity property of the $\varphi _{i},$ such as continuity, differentiability, that is preserved under finite sums will be preserved for the sum of any subcollection of this family of functions.
- On the first uncountable ordinal $\omega _{1}$ viewed as a topological space in the order topology, the constant function $f:\left[0,\omega _{1}\right)\to \left[0,\omega _{1}\right]$ given by $f(\alpha )=1$ satisfies $\sum _{\alpha \in [0,\omega _{1})}\!\!\!f(\alpha )=\omega _{1}$ (in other words, $\omega _{1}$ copies of 1 is $\omega _{1}$ ) only if one takes a limit over all *countable* partial sums, rather than finite partial sums. This space is not separable.
