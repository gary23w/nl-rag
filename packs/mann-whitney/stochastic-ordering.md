---
title: "Stochastic ordering"
source: https://en.wikipedia.org/wiki/Stochastic_ordering
domain: mann-whitney
license: CC-BY-SA-4.0
tags: Mann Whitney U test, Wilcoxon rank-sum, stochastic ordering, order statistic
fetched: 2026-07-02
---

# Stochastic ordering

In probability theory and statistics, a **stochastic order** quantifies the concept of one random variable being "bigger" than another. These are usually partial orders, so that one random variable A may be neither stochastically greater than, less than, nor equal to another random variable B . Many different orders exist, which have different applications.

## Usual stochastic order

A real random variable A is less than a random variable B in the "usual stochastic order" if

$\Pr(A>x)\leq \Pr(B>x){\text{ for all }}x\in (-\infty ,\infty ),$

where $\Pr(\cdot )$ denotes the probability of an event. This is sometimes denoted $A\preceq B$ or $A\leq _{\mathrm {st} }B$ .

If additionally $\Pr(A>x)<\Pr(B>x)$ for some x , then A is stochastically strictly less than B , sometimes denoted $A\prec B$ . In decision theory, under this circumstance, B is said to be first-order stochastically dominant over *A*.

### Characterizations

The following rules describe situations when one random variable is stochastically less than or equal to another. Strict version of some of these rules also exist.

1. $A\preceq B$ if and only if for all non-decreasing functions u , $\operatorname {E} [u(A)]\leq \operatorname {E} [u(B)]$ .
2. If u is non-decreasing and $A\preceq B$ then $u(A)\preceq u(B)$
3. If $u:\mathbb {R} ^{n}\to \mathbb {R}$ is increasing in each variable and $A_{i}$ and $B_{i}$ are independent sets of random variables with $A_{i}\preceq B_{i}$ for each i , then $u(A_{1},\dots ,A_{n})\preceq u(B_{1},\dots ,B_{n})$ and in particular $\sum _{i=1}^{n}A_{i}\preceq \sum _{i=1}^{n}B_{i}$ Moreover, the i th order statistics satisfy $A_{(i)}\preceq B_{(i)}$ .
4. If two sequences of random variables $A_{i}$ and $B_{i}$ , with $A_{i}\preceq B_{i}$ for all i each converge in distribution, then their limits satisfy $A\preceq B$ .
5. If A , B and C are random variables such that $\sum _{c}\Pr(C=c)=1$ and $\Pr(A>u\mid C=c)\leq \Pr(B>u\mid C=c)$ for all u and c such that $\Pr(C=c)>0$ , then $A\preceq B$ .

### Other properties

If $A\preceq B$ and $\operatorname {E} [A]=\operatorname {E} [B]$ then $A\mathrel {\overset {d}{=}} B$ (the random variables are equal in distribution).

## Stochastic dominance

Stochastic dominance relations are a family of stochastic orderings used in decision theory:

- Zeroth-order stochastic dominance: $A\prec _{(0)}B$ if and only if $A\leq B$ for all realizations of these random variables and $A<B$ for at least one realization.
- First-order stochastic dominance: $A\prec _{(1)}B$ if and only if $\Pr(A>x)\leq \Pr(B>x)$ for all x and there exists x such that $\Pr(A>x)<\Pr(B>x)$ .
- Second-order stochastic dominance: $A\prec _{(2)}B$ if and only if $\int _{-\infty }^{x}[\Pr(B>t)-\Pr(A>t)]\,dt\geq 0$ for all x , with strict inequality at some x .

There also exist higher-order notions of stochastic dominance. With the definitions above, we have $A\prec _{(i)}B\implies A\prec _{(i+1)}B$ .

## Multivariate stochastic order

An $\mathbb {R} ^{d}$ -valued random variable A is less than an $\mathbb {R} ^{d}$ -valued random variable B in the "usual stochastic order" if

$\operatorname {E} [f(A)]\leq \operatorname {E} [f(B)]{\text{ for all bounded, increasing functions }}f\colon \mathbb {R} ^{d}\longrightarrow \mathbb {R}$

Other types of multivariate stochastic orders exist. For instance the upper and lower orthant order which are similar to the usual one-dimensional stochastic order. A is said to be smaller than B in upper orthant order if

$\Pr(A>\mathbf {x} )\leq \Pr(B>\mathbf {x} ){\text{ for all }}\mathbf {x} \in \mathbb {R} ^{d}$

and A is smaller than B in lower orthant order if

$\Pr(A\leq \mathbf {x} )\leq \Pr(B\leq \mathbf {x} ){\text{ for all }}\mathbf {x} \in \mathbb {R} ^{d}$

All three order types also have integral representations, that is for a particular order A is smaller than B if and only if $\operatorname {E} [f(A)]\leq \operatorname {E} [f(B)]$ for all $f\colon \mathbb {R} ^{d}\longrightarrow \mathbb {R}$ in a class of functions ${\mathcal {G}}$ . ${\mathcal {G}}$ is then called generator of the respective order.

## Other dominance orders

The following stochastic orders are useful in the theory of random social choice. They are used to compare the outcomes of random social choice functions, in order to check them for efficiency or other desirable criteria. The dominance orders below are ordered from the most conservative to the least conservative. They are exemplified on random variables over the finite support {30,20,10}.

**Deterministic dominance**, denoted $A\succeq _{\mathrm {dd} }B$ , means that every possible outcome of A is at least as good as every possible outcome of B : for all *x* < *y*, $\Pr[A=x]\cdot \Pr[B=y]=0$ . In other words: $\Pr[A\geq B]=1$ . For example, $0.6\times 30+0.4\times 20\succeq _{\mathrm {dd} }0.5\times 20+0.5\times 10$ .

**Bilinear dominance**, denoted $A\succeq _{\mathrm {bd} }B$ , means that, for every possible outcome, the probability that A yields the better one and B yields the worse one is at least as large as the probability the other way around: for all x<y, $\Pr[A=x]\cdot \Pr[B=y]\leq \Pr[A=y]\cdot \Pr[B=x]$ For example, $0.5\times 30+0.5\times 20\succeq _{\mathrm {bd} }0.33\times 30+0.33\times 20+0.34\times 10$ .

**Stochastic dominance** (already mentioned above), denoted $A\succeq _{\mathrm {sd} }B$ , means that, for every possible outcome *x*, the probability that A yields at least *x* is at least as large as the probability that B yields at least *x*: for all x, $\Pr[A\geq x]\geq \Pr[B\geq x]$ . For example, $0.5\times 30+0.5\times 10\succeq _{\mathrm {sd} }0.5\times 20+0.5\times 10$ .

**Pairwise-comparison dominance**, denoted $A\succeq _{\mathrm {pc} }B$ , means that the probability that that A yields a better outcome than B is larger than the other way around: $\Pr[A\geq B]\geq \Pr[B\geq A]$ . For example, $0.67\times 30+0.33\times 10\succeq _{\mathrm {pc} }1.0\times 20$ .

**Downward-lexicographic dominance,** denoted $A\succeq _{\mathrm {dl} }B$ , means that A has a larger probability than B of returning the best outcome, or both A and B have the same probability to return the best outcome but A has a larger probability than B of returning the second-best best outcome, etc. **Upward-lexicographic dominance** is defined analogously based on the probability to return the *worst* outcomes. See lexicographic dominance.

## Other stochastic orders

### Hazard rate order

The *hazard rate* of a non-negative random variable X with absolutely continuous distribution function F and density function f is defined as

$r(t)={\frac {d}{dt}}(-\log(1-F(t)))={\frac {f(t)}{1-F(t)}}.$

Given two non-negative variables X and Y with absolutely continuous distribution F and G , and with hazard rate functions r and q , respectively, X is said to be smaller than Y in the hazard rate order (denoted as $X\preceq _{\mathrm {hr} }Y$ ) if

$r(t)\geq q(t)$

for all

$t\geq 0$

,

or equivalently if

${\frac {1-F(t)}{1-G(t)}}$

is decreasing in

t

.

### Likelihood ratio order

Let X and Y two continuous (or discrete) random variables with densities (or discrete densities) $f(t)$ and $g(t)$ , respectively, so that ${\frac {g(t)}{f(t)}}$ increases in t over the union of the supports of X and Y ; in this case, X is smaller than Y in the *likelihood ratio order* ( $X\preceq _{\mathrm {lr} }Y$ ).

### Variability orders

If two variables have the same mean, they can still be compared by how "spread out" their distributions are. This is captured to a limited extent by the variance, but more fully by a range of stochastic orders.

#### Convex order

Convex order is a special kind of variability order. Under the convex ordering, A is less than B if and only if for all convex u , $\operatorname {E} [u(A)]\leq \operatorname {E} [u(B)]$ .

### Laplace transform order

Laplace transform order compares both size and variability of two random variables. Similar to convex order, Laplace transform order is established by comparing the expectation of a function of the random variable where the function is from a special class: $u(x)=-\exp(-\alpha x)$ . This makes the Laplace transform order an integral stochastic order with the generator set given by the function set defined above with $\alpha$ a positive real number.

### Realizable monotonicity

Considering a family of probability distributions $({P}_{\alpha })_{\alpha \in F}$ on partially ordered space $(E,\preceq )$ indexed with $\alpha \in F$ (where $(F,\preceq )$ is another partially ordered space, the concept of complete or realizable monotonicity may be defined. It means, there exists a family of random variables $(X_{\alpha })_{\alpha }$ on the same probability space, such that the distribution of $X_{\alpha }$ is ${P}_{\alpha }$ and $X_{\alpha }\preceq X_{\beta }$ almost surely whenever $\alpha \preceq \beta$ . It means the existence of a monotone coupling.
