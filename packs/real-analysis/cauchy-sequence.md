---
title: "Cauchy sequence"
source: https://en.wikipedia.org/wiki/Cauchy_sequence
domain: real-analysis
license: CC-BY-SA-4.0
tags: real analysis, uniform convergence, riemann integral, metric space
fetched: 2026-07-02
---

# Cauchy sequence

(a) The plot of a Cauchy

sequence

$(x_{n}),$

shown in blue, as

$x_{n}$

versus

$n.$

If the

space

containing the sequence is

complete

, then the sequence has a

limit

.

(b) A sequence that is not Cauchy. The

elements

of the sequence do not get arbitrarily close to each other as the sequence progresses.

In mathematics, a **Cauchy sequence** is a sequence whose elements become arbitrarily close to each other as the sequence progresses. More precisely, given any small positive distance, all excluding a finite number of elements of the sequence are less than that given distance from each other. Cauchy sequences are named after Augustin-Louis Cauchy; they may occasionally be known as **fundamental sequences**.

It is not sufficient for each term to become arbitrarily close to the *preceding* term. For instance, in the sequence of square roots of natural numbers: $a_{n}={\sqrt {n}},$ the consecutive terms become arbitrarily close to each other – their differences $a_{n+1}-a_{n}={\sqrt {n+1}}-{\sqrt {n}}={\frac {1}{{\sqrt {n+1}}+{\sqrt {n}}}}<{\frac {1}{2{\sqrt {n}}}}$ tend to zero as the index n grows. However, with growing values of n, the terms $a_{n}$ become arbitrarily large. So, for any index n and distance d, there exists an index m big enough such that $a_{m}-a_{n}>d.$ As a result, no matter how far one goes, the remaining terms of the sequence never get close to *each other*; hence the sequence is not Cauchy.

The utility of Cauchy sequences lies in the fact that in a complete metric space (one where all such sequences are known to converge to a limit), the criterion for convergence depends only on the terms of the sequence itself, as opposed to the definition of convergence, which uses the limit value as well as the terms. This is often exploited in algorithms, both theoretical and applied, where an iterative process can be shown relatively easily to produce a Cauchy sequence, consisting of the iterates, thus fulfilling a logical condition, such as termination.

Generalizations of Cauchy sequences in more abstract uniform spaces exist in the form of Cauchy filters and Cauchy nets.

## In real numbers

A sequence $x_{1},x_{2},x_{3},\ldots$ of real numbers is called a Cauchy sequence if for every positive real number $\varepsilon ,$ there is a positive integer *N* such that for all natural numbers $m,n>N,$ $|x_{m}-x_{n}|<\varepsilon ,$ where the vertical bars denote the absolute value. In a similar way one can define Cauchy sequences of rational or complex numbers. Cauchy formulated such a condition by requiring $x_{m}-x_{n}$ to be infinitesimal for every pair of infinite *m*, *n*.

For any real number *r*, the sequence of truncated decimal expansions of *r* forms a Cauchy sequence. For example, when $r=\pi ,$ this sequence is (3, 3.1, 3.14, 3.141, ...). The *m*th and *n*th terms differ by at most $10^{1-m}$ when *m* < *n*, and as *m* grows this becomes smaller than any fixed positive number $\varepsilon .$

### Modulus of Cauchy convergence

If $(x_{1},x_{2},x_{3},...)$ is a sequence in the set $X,$ then a *modulus of Cauchy convergence* for the sequence is a function $\alpha$ from the set of natural numbers to itself, such that for all natural numbers k and natural numbers $m,n>\alpha (k),$ $|x_{m}-x_{n}|<1/k.$

Any sequence with a modulus of Cauchy convergence is a Cauchy sequence. The existence of a modulus for a Cauchy sequence follows from the well-ordering property of the natural numbers (let $\alpha (k)$ be the smallest possible N in the definition of Cauchy sequence, taking $\varepsilon$ to be $1/k$ ). The existence of a modulus also follows from the principle of countable choice. *Regular Cauchy sequences* are sequences with a given modulus of Cauchy convergence (usually $\alpha (k)=k$ or $\alpha (k)=2^{k}$ ). Any Cauchy sequence with a modulus of Cauchy convergence is equivalent to a regular Cauchy sequence; this can be proven without using any form of the axiom of choice.

Moduli of Cauchy convergence are used by constructive mathematicians who do not wish to use any form of choice. Using a modulus of Cauchy convergence can simplify both definitions and theorems in constructive analysis. Regular Cauchy sequences were used by Bishop (2012) and by Bridges (1997) in constructive mathematics textbooks.

## In a metric space

Since the definition of a Cauchy sequence only involves metric concepts, it is straightforward to generalize it to any metric space *X*. To do so, the absolute difference $\left|x_{m}-x_{n}\right|$ is replaced by the distance $d\left(x_{m},x_{n}\right)$ (where *d* denotes a metric) between $x_{m}$ and $x_{n}.$

Formally, given a metric space $(X,d),$ a sequence of elements of X $x_{1},x_{2},x_{3},\ldots$ is Cauchy, if for every positive real number $\varepsilon >0$ there is a positive integer N such that for all positive integers $m,n>N,$ the distance $d\left(x_{m},x_{n}\right)<\varepsilon .$

Roughly speaking, the terms of the sequence are getting closer and closer together in a way that suggests that the sequence ought to have a limit in *X*. Nonetheless, such a limit does not always exist within *X*: the property of a space that every Cauchy sequence converges in the space is called *completeness*, and is detailed below.

## Completeness

A metric space (*X*, *d*) in which every Cauchy sequence converges to an element of *X* is called complete. For any metric space *M*, it is possible to construct a complete metric space *M′* that contains *M* as a dense subspace; see Complete metric space § Completion.

### Examples of complete metric spaces

The real numbers $\mathbb {R}$ are complete under the metric induced by the usual absolute value, and one of the standard constructions of the real numbers involves Cauchy sequences of rational numbers. In this construction, each equivalence class of Cauchy sequences of rational numbers with a certain tail behavior—that is, each class of sequences that get arbitrarily close to one another— is a real number.

A rather different type of example is afforded by a metric space *X* which has the discrete metric (where any two distinct points are at distance 1 from each other). Any Cauchy sequence of elements of *X* must be constant beyond some fixed point, and converges to the eventually repeating term.

### Non-example: rational numbers

The rational numbers $\mathbb {Q}$ are not complete (for the usual distance): There are sequences of rationals that converge (in $\mathbb {R}$ ) to irrational numbers; these are Cauchy sequences having no limit in $\mathbb {Q} .$ In fact, if a real number *x* is irrational, then the sequence (*x**n*), whose *n*-th term is the truncation to *n* decimal places of the decimal expansion of *x*, gives a Cauchy sequence of rational numbers with irrational limit *x*. Irrational numbers certainly exist in $\mathbb {R} ,$ for example:

- The sequence defined by $x_{0}=1,x_{n+1}={\frac {x_{n}+2/x_{n}}{2}}$ consists of rational numbers (1, 3/2, 17/12,...), which is clear from the definition; however it converges to the irrational square root of 2, see Babylonian method of computing square root.
- The sequence $x_{n}=F_{n}/F_{n-1}$ of ratios of consecutive Fibonacci numbers which, if it converges at all, converges to a limit $\phi$ satisfying $\phi ^{2}=\phi +1,$ and no rational number has this property. If one considers this as a sequence of real numbers, however, it converges to the real number $\varphi =(1+{\sqrt {5}})/2,$ the Golden ratio, which is irrational.
- The values of the exponential, sine and cosine functions, exp(*x*), sin(*x*), cos(*x*), are known to be irrational for any rational value of $x\neq 0,$ but each can be defined as the limit of a rational Cauchy sequence, using, for instance, the Maclaurin series.

Completion turns $\mathbb {Q}$ into $\mathbb {R} .$

### Non-example: open interval

The open interval $(0,2)$ in the set of real numbers with an ordinary distance in $\mathbb {R}$ is not a complete space: there is a sequence $x_{n}=1/n$ in it, which is Cauchy (for arbitrarily small distance bound $d>0$ all terms $x_{n}$ of $n>1/d$ fit in the $(0,d)$ interval), however does not converge in X —its 'limit', number 0, does not belong to the space $X.$

Completion turns the open interval $(0,2)$ into the closed interval $[0,2].$

### Other properties

- Every convergent sequence (with limit *s*, say) is a Cauchy sequence, since, given any real number $\varepsilon >0,$ beyond some fixed point, every term of the sequence is within distance $\varepsilon /2$ of *s*, so any two terms of the sequence are within distance $\varepsilon$ of each other.
- In any metric space, a Cauchy sequence $x_{n}$ is bounded (since for some *N*, all terms of the sequence from the *N*-th onwards are within distance 1 of each other, and if *M* is the largest distance between $x_{N}$ and any terms up to the *N*-th, then no term of the sequence has distance greater than $M+1$ from $x_{N}$ ).
- In any metric space, a Cauchy sequence which has a convergent subsequence with limit *s* is itself convergent (with the same limit), since, given any real number *r* > 0, beyond some fixed point in the original sequence, every term of the subsequence is within distance *r*/2 of *s*, and any two terms of the original sequence are within distance *r*/2 of each other, so every term of the original sequence is within distance *r* of *s*.

These last two properties, together with the Bolzano–Weierstrass theorem, yield one standard proof of the completeness of the real numbers, closely related to both the Bolzano–Weierstrass theorem and the Heine–Borel theorem. Every Cauchy sequence of real numbers is bounded, hence by Bolzano–Weierstrass has a convergent subsequence, hence is itself convergent. This proof of the completeness of the real numbers implicitly makes use of the least upper bound axiom. The alternative approach, mentioned above, of *constructing* the real numbers as the completion of the rational numbers, makes the completeness of the real numbers tautological.

One of the standard illustrations of the advantage of being able to work with Cauchy sequences and make use of completeness is provided by consideration of the summation of an infinite series of real numbers (or, more generally, of elements of any complete normed linear space, or Banach space). Such a series ${\textstyle \sum _{n=1}^{\infty }x_{n}}$ is considered to be convergent if and only if the sequence of partial sums $(s_{m})$ is convergent, where ${\textstyle s_{m}=\sum _{n=1}^{m}x_{n}.}$ It is a routine matter to determine whether the sequence of partial sums is Cauchy or not, since for positive integers $p>q,$ $s_{p}-s_{q}=\sum _{n=q+1}^{p}x_{n}.$

If $f:M\to N$ is a uniformly continuous map between the metric spaces *M* and *N* and (*x**n*) is a Cauchy sequence in *M*, then $(f(x_{n}))$ is a Cauchy sequence in *N*. If $(x_{n})$ and $(y_{n})$ are two Cauchy sequences in the rational, real or complex numbers, then the sum $(x_{n}+y_{n})$ and the product $(x_{n}y_{n})$ are also Cauchy sequences.

## Generalizations

### In topological vector spaces

There is also a concept of Cauchy sequence for a topological vector space X : Pick a local base B for X about 0; then ( $x_{k}$ ) is a Cauchy sequence if for each member $V\in B,$ there is some number N such that whenever $n,m>N,x_{n}-x_{m}$ is an element of $V.$ If the topology of X is compatible with a translation-invariant metric $d,$ the two definitions agree.

### In topological groups

Since the topological vector space definition of Cauchy sequence requires only that there be a continuous "subtraction" operation, it can just as well be stated in the context of a topological group: A sequence $(x_{k})$ in a topological group G is a Cauchy sequence if for every open neighbourhood U of the identity in G there exists some number N such that whenever $m,n>N$ it follows that $x_{n}x_{m}^{-1}\in U.$ As above, it is sufficient to check this for the neighbourhoods in any local base of the identity in $G.$

As in the construction of the completion of a metric space, one can furthermore define the binary relation on Cauchy sequences in G that $(x_{k})$ and $(y_{k})$ are equivalent if for every open neighbourhood U of the identity in G there exists some number N such that whenever $m,n>N$ it follows that $x_{n}y_{m}^{-1}\in U.$ This relation is an equivalence relation: It is reflexive since the sequences are Cauchy sequences. It is symmetric since $y_{n}x_{m}^{-1}=(x_{m}y_{n}^{-1})^{-1}\in U^{-1}$ which by continuity of the inverse is another open neighbourhood of the identity. It is transitive since $x_{n}z_{l}^{-1}=x_{n}y_{m}^{-1}y_{m}z_{l}^{-1}\in U'U''$ where $U'$ and $U''$ are open neighbourhoods of the identity such that $U'U''\subseteq U$ ; such pairs exist by the continuity of the group operation.

### In groups

There is also a concept of Cauchy sequence in a group G : Let $H=(H_{r})$ be a decreasing sequence of normal subgroups of G of finite index. Then a sequence $(x_{n})$ in G is said to be Cauchy (with respect to H ) if and only if for any r there is N such that for all $m,n>N,x_{n}x_{m}^{-1}\in H_{r}.$

Technically, this is the same thing as a topological group Cauchy sequence for a particular choice of topology on $G,$ namely that for which H is a local base.

The set C of such Cauchy sequences forms a group (for the componentwise product), and the set $C_{0}$ of null sequences (sequences such that $\forall r,\exists N,\forall n>N,x_{n}\in H_{r}$ ) is a normal subgroup of $C.$ The factor group $C/C_{0}$ is called the completion of G with respect to $H.$

One can then show that this completion is isomorphic to the inverse limit of the sequence $(G/H_{r}).$

An example of this construction familiar in number theory and algebraic geometry is the construction of the p -adic completion of the integers with respect to a prime $p.$ In this case, G is the integers under addition, and $H_{r}$ is the additive subgroup consisting of integer multiples of $p_{r}.$

If H is a cofinal sequence (that is, any normal subgroup of finite index contains some $H_{r}$ ), then this completion is canonical in the sense that it is isomorphic to the inverse limit of $(G/H)_{H},$ where H varies over *all* normal subgroups of finite index. For further details, see Ch. I.10 in Lang's "Algebra".

### In a hyperreal continuum

A real sequence $\langle u_{n}:n\in \mathbb {N} \rangle$ has a natural hyperreal extension, defined for hypernatural values *H* of the index *n* in addition to the usual natural *n*. The sequence is Cauchy if and only if for every infinite *H* and *K*, the values $u_{H}$ and $u_{K}$ are infinitely close, or adequal, that is,

$\mathrm {st} (u_{H}-u_{K})=0$

where "st" is the standard part function.

### Cauchy completion of categories

Krause (2020) introduced a notion of Cauchy completion of a category. Applied to $\mathbb {Q}$ (the category whose objects are rational numbers, and there is a morphism from *x* to *y* if and only if $x\leq y$ ), this Cauchy completion yields $\mathbb {R} \cup \left\{\infty \right\}$ (again interpreted as a category using its natural ordering).
