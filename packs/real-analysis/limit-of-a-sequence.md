---
title: "Limit of a sequence"
source: https://en.wikipedia.org/wiki/Limit_of_a_sequence
domain: real-analysis
license: CC-BY-SA-4.0
tags: real analysis, uniform convergence, riemann integral, metric space
fetched: 2026-07-02
---

# Limit of a sequence

| n | $n\times \sin \left({\tfrac {1}{n}}\right)$ |
|---|---|
| 1 | 0.841471 |
| 2 | 0.958851 |
| ... |   |
| 10 | 0.998334 |
| ... |   |
| 100 | 0.999983 |

As the positive integer ${\textstyle n}$ becomes larger and larger, the value ${\textstyle n\times \sin \left({\tfrac {1}{n}}\right)}$ becomes arbitrarily close to ${\textstyle 1}$ . We say that "the limit of the sequence ${\textstyle n\times \sin \left({\tfrac {1}{n}}\right)}$ equals ${\textstyle 1}$ ."

In mathematics, the **limit of a sequence** is the value that the terms of a sequence "tend to", and is often denoted using the $\lim$ symbol (e.g., $\lim _{n\to \infty }a_{n}$ ). If such a limit exists and is finite, the sequence is called **convergent**. A sequence that does not converge is said to be **divergent**. The limit of a sequence is said to be the fundamental notion on which the whole of mathematical analysis ultimately rests.

Limits can be defined in any metric or topological space, but are usually first encountered in the real numbers.

## History

The Greek philosopher Zeno of Elea is famous for formulating paradoxes that involve limiting processes.

Leucippus, Democritus, Antiphon, Eudoxus, and Archimedes developed the method of exhaustion, which uses an infinite sequence of approximations to determine an area or a volume. Archimedes succeeded in summing what is now called a geometric series in his *Quadrature of the Parabola*, computing the area enclosed by a parabola and a straight line.

Grégoire de Saint-Vincent gave the first definition of limit (terminus) of a geometric series in his work *Opus Geometricum* (1647): "The *terminus* of a progression is the end of the series, which none progression can reach, even not if she is continued in infinity, but which she can approach nearer than a given segment."

Pietro Mengoli anticipated the modern idea of limit of a sequence with his study of quasi-proportions in *Geometriae speciosae elementa* (1659). He used the term *quasi-infinite* for unbounded and *quasi-null* for vanishing.

Newton dealt with series in his works on *Analysis with infinite series* (written in 1669, circulated in manuscript, published in 1711), *Method of fluxions and infinite series* (written in 1671, published in English translation in 1736, Latin original published much later) and *Tractatus de Quadratura Curvarum* (written in 1693, published in 1704 as an Appendix to his *Optiks*). In the latter work, Newton considers the binomial expansion of ${\textstyle (x+o)^{n}}$ , which he then linearizes by *taking the limit* as ${\textstyle o}$ tends to ${\textstyle 0}$ .

In the 18th century, mathematicians such as Euler succeeded in summing some *divergent* series by stopping at the right moment; they did not much care whether a limit existed, as long as it could be calculated. At the end of the century, Lagrange in his *Théorie des fonctions analytiques* (1797) opined that the lack of rigour precluded further development in calculus. Gauss in his study of hypergeometric series (1813) for the first time rigorously investigated the conditions under which a series converged to a limit.

The modern definition of a limit (for any ${\textstyle \varepsilon }$ there exists an index ${\textstyle N}$ so that ...) was given by Bernard Bolzano (*Der binomische Lehrsatz*, Prague 1816, which was little noticed at the time), and by Karl Weierstrass in the 1870s.

## Real numbers

In the real numbers, a number L is the limit of the sequence $(x_{n})$ , if the numbers in the sequence become closer and closer to L , and not to any other number.

### Examples

Examples of limit of a sequence in real numbers are the following:

- If $x_{n}=c$ for constant ${\textstyle c}$ , then $x_{n}\to c$ .
- If $x_{n}={\frac {1}{n}}$ , then $x_{n}\to 0$ .
- If $x_{n}={\frac {1}{n}}$ when n is even, and $x_{n}={\frac {1}{n^{2}}}$ when n is odd, then $x_{n}\to 0$ . (The fact that $x_{n+1}>x_{n}$ whenever n is odd is irrelevant.)
- Given any real number, one may easily construct a sequence that converges to that number by taking decimal approximations. For example, the sequence ${\textstyle 0.3,0.33,0.333,0.3333,\dots }$ converges to ${\textstyle {\frac {1}{3}}}$ . The decimal representation ${\textstyle 0.3333\dots }$ is the *limit* of the previous sequence, defined by $0.3333...:=\lim _{n\to \infty }\sum _{k=1}^{n}{\frac {3}{10^{k}}}$
- Finding the limit of a sequence is not always obvious. Two examples are $\lim _{n\to \infty }\left(1+{\tfrac {1}{n}}\right)^{n}$ (the limit of which is the number *e*) and the arithmetic–geometric mean. The squeeze theorem is often useful in the establishment of such limits.

### Definition

We call x the **limit** of the sequence $(x_{n})$ , which is written

$x_{n}\to x$

, or

$\lim _{n\to \infty }x_{n}=x$

,

if the following condition holds:

For each

real number

$\varepsilon >0$

, there exists a

natural number

N

such that, for every natural number

$n\geq N$

, we have

$|x_{n}-x|<\varepsilon$

.

In other words, for every measure of closeness $\varepsilon$ , the sequence's terms are eventually that close to the limit. The sequence $(x_{n})$ is said to **converge to** or **tend to** the limit x .

Symbolically, this is:

$\forall \varepsilon >0\left(\exists N\in \mathbb {N} \left(\forall n\in \mathbb {N} \left(n\geq N\implies |x_{n}-x|<\varepsilon \right)\right)\right)$

.

If a sequence $(x_{n})$ converges to some limit x , then it is **convergent** and x is the only limit; otherwise $(x_{n})$ is **divergent**. A sequence that has zero as its limit is sometimes called a **null sequence**.

### Illustration

- (Example of a sequence which converges to the limit a {\displaystyle a} .) Example of a sequence which converges to the limit a
- (Regardless which '"`UNIQ--postMath-00000035-QINU`"' we have, there is an index '"`UNIQ--postMath-00000036-QINU`"', so that the sequence lies afterwards completely in the epsilon tube '"`UNIQ--postMath-00000037-QINU`"'.) Regardless which $\varepsilon >0$ we have, there is an index $N_{0}$ , so that the sequence lies afterwards completely in the epsilon tube $(a-\varepsilon ,a+\varepsilon )$ .
- (There is also for a smaller '"`UNIQ--postMath-00000038-QINU`"' an index '"`UNIQ--postMath-00000039-QINU`"', so that the sequence is afterwards inside the epsilon tube '"`UNIQ--postMath-0000003A-QINU`"'.) There is also for a smaller $\varepsilon _{1}>0$ an index $N_{1}$ , so that the sequence is afterwards inside the epsilon tube $(a-\varepsilon _{1},a+\varepsilon _{1})$ .
- (For each '"`UNIQ--postMath-0000003B-QINU`"' there are only finitely many sequence members outside the epsilon tube.) For each $\varepsilon >0$ there are only finitely many sequence members outside the epsilon tube.

### Properties

Some other important properties of limits of real sequences include the following:

- When it exists, the limit of a sequence is unique.
- Limits of sequences behave well with respect to the usual arithmetic operations. If $\lim _{n\to \infty }a_{n}$ and $\lim _{n\to \infty }b_{n}$ exists, then

$\lim _{n\to \infty }(a_{n}\pm b_{n})=\lim _{n\to \infty }a_{n}\pm \lim _{n\to \infty }b_{n}$

$\lim _{n\to \infty }ca_{n}=c\cdot \lim _{n\to \infty }a_{n}$

$\lim _{n\to \infty }(a_{n}\cdot b_{n})=\left(\lim _{n\to \infty }a_{n}\right)\cdot \left(\lim _{n\to \infty }b_{n}\right)$

$\lim _{n\to \infty }\left({\frac {a_{n}}{b_{n}}}\right)={\frac {\lim \limits _{n\to \infty }a_{n}}{\lim \limits _{n\to \infty }b_{n}}}$

provided

$\lim _{n\to \infty }b_{n}\neq 0$

$\lim _{n\to \infty }a_{n}^{p}=\left(\lim _{n\to \infty }a_{n}\right)^{p}$

- For any continuous function ${\textstyle f}$ , if $\lim _{n\to \infty }x_{n}$ exists, then $\lim _{n\to \infty }f\left(x_{n}\right)$ exists too. In fact, any real-valued function *${\textstyle f}$* is continuous if and only if it preserves the limits of sequences (though this is not necessarily true when using more general notions of continuity).

- If $a_{n}\leq b_{n}$ for all n greater than some N , then $\lim _{n\to \infty }a_{n}\leq \lim _{n\to \infty }b_{n}$ .
- (Squeeze theorem) If $a_{n}\leq c_{n}\leq b_{n}$ for all n greater than some N , and $\lim _{n\to \infty }a_{n}=\lim _{n\to \infty }b_{n}=L$ , then $\lim _{n\to \infty }c_{n}=L$ .
- (Monotone convergence theorem) If $a_{n}$ is bounded and monotonic for all n greater than some N , then it is convergent.
- A sequence is convergent if and only if every subsequence is convergent.
- If every subsequence of a sequence has its own subsequence which converges to the same point, then the original sequence converges to that point.

These properties are extensively used to prove limits, without the need to directly use the cumbersome formal definition. For example, once it is proven that $1/n\to 0$ , it becomes easy to show—using the properties above—that ${\frac {a}{b+{\frac {c}{n}}}}\to {\frac {a}{b}}$ (assuming that $b\neq 0$ ).

### Infinite limits

A sequence $(x_{n})$ is said to **tend to infinity**, written

$x_{n}\to \infty$

, or

$\lim _{n\to \infty }x_{n}=\infty$

,

if the following holds:

For every real number

K

, there is a natural number

N

such that for every natural number

$n\geq N$

, we have

$x_{n}>K$

; that is, the sequence terms are eventually larger than any fixed

K

.

Symbolically, this is:

$\forall K\in \mathbb {R} \left(\exists N\in \mathbb {N} \left(\forall n\in \mathbb {N} \left(n\geq N\implies x_{n}>K\right)\right)\right)$

.

Similarly, we say a sequence **tends to minus infinity**, written

$x_{n}\to -\infty$

, or

$\lim _{n\to \infty }x_{n}=-\infty$

,

if the following holds:

For every real number

K

, there is a natural number

N

such that for every natural number

$n\geq N$

, we have

$x_{n}<K$

; that is, the sequence terms are eventually smaller than any fixed

K

.

Symbolically, this is:

$\forall K\in \mathbb {R} \left(\exists N\in \mathbb {N} \left(\forall n\in \mathbb {N} \left(n\geq N\implies x_{n}<K\right)\right)\right)$

.

If a sequence tends to infinity or minus infinity, then it is divergent. However, a divergent sequence need not tend to plus or minus infinity, and the sequence $x_{n}=(-1)^{n}$ provides one such example.

## Metric spaces

### Definition

A point x of the metric space $(X,d)$ is the **limit** of the sequence $(x_{n})$ if:

For each

real number

$\varepsilon >0$

, there is a

natural number

N

such that, for every natural number

$n\geq N$

, we have

$d(x_{n},x)<\varepsilon$

.

Symbolically, this is:

$\forall \varepsilon >0\left(\exists N\in \mathbb {N} \left(\forall n\in \mathbb {N} \left(n\geq N\implies d(x_{n},x)<\varepsilon \right)\right)\right)$

.

This coincides with the definition given for real numbers when $X=\mathbb {R}$ and $d(x,y)=|x-y|$ .

### Properties

- When it exists, the limit of a sequence is unique, as distinct points are separated by some positive distance, so for $\varepsilon$ less than half this distance, sequence terms cannot be within a distance $\varepsilon$ of both points.

- For any continuous function *f*, if $\lim _{n\to \infty }x_{n}$ exists, then $\lim _{n\to \infty }f(x_{n})=f\left(\lim _{n\to \infty }x_{n}\right)$ . In fact, a function *f* is continuous if and only if it preserves the limits of sequences.

### Cauchy sequences

A Cauchy sequence is a sequence whose terms ultimately become arbitrarily close together, after sufficiently many initial terms have been discarded. The notion of a Cauchy sequence is important in the study of sequences in metric spaces, and, in particular, in real analysis. One particularly important result in real analysis is the *Cauchy criterion for convergence of sequences*: a sequence of real numbers is convergent if and only if it is a Cauchy sequence. This remains true in other complete metric spaces.

## Topological spaces

### Definition

A point $x\in X$ of the topological space $(X,\tau )$ is a **limit** or **limit point** of the sequence $\left(x_{n}\right)_{n\in \mathbb {N} }$ if:

For every

neighbourhood

U

of

x

, there exists some

$N\in \mathbb {N}$

such that for every

$n\geq N$

, we have

$x_{n}\in U$

.

This coincides with the definition given for metric spaces, if $(X,d)$ is a metric space and $\tau$ is the topology generated by d .

A limit of a sequence of points $\left(x_{n}\right)_{n\in \mathbb {N} }$ in a topological space T is a special case of a limit of a function: the domain is $\mathbb {N}$ in the space $\mathbb {N} \cup \lbrace +\infty \rbrace$ , with the induced topology of the affinely extended real number system, the range is T , and the function argument n tends to $+\infty$ , which in this space is a limit point of $\mathbb {N}$ .

### Properties

In a Hausdorff space, limits of sequences are unique whenever they exist. This need not be the case in non-Hausdorff spaces; in particular, if two points x and y are topologically indistinguishable, then any sequence that converges to x must converge to y and vice versa.

## Hyperreal numbers

The definition of the limit using the hyperreal numbers formalizes the intuition that for a "very large" value of the index, the corresponding term is "very close" to the limit. More precisely, a real sequence $(x_{n})$ tends to *L* if for every infinite hypernatural ${\textstyle H}$ , the term $x_{H}$ is infinitely close to ${\textstyle L}$ (i.e., the difference $x_{H}-L$ is infinitesimal). Equivalently, *L* is the standard part of $x_{H}$ :

$L={\rm {st}}(x_{H})$

.

Thus, the limit can be defined by the formula

$\lim _{n\to \infty }x_{n}={\rm {st}}(x_{H})$

.

where the limit exists if and only if the righthand side is independent of the choice of an infinite *${\textstyle H}$*.

## Sequence of more than one index

Sometimes one may also consider a sequence with more than one index, for example, a double sequence $(x_{n,m})$ . This sequence has a limit L if it becomes closer and closer to L when both *n* and *m* becomes very large.

### Example

- If $x_{n,m}=c$ for constant ${\textstyle c}$ , then $x_{n,m}\to c$ .
- If $x_{n,m}={\frac {1}{n+m}}$ , then $x_{n,m}\to 0$ .
- If $x_{n,m}={\frac {n}{n+m}}$ , then the limit does not exist. Depending on the relative "growing speed" of ${\textstyle n}$ and ${\textstyle m}$ , this sequence can get closer to any value between ${\textstyle 0}$ and ${\textstyle 1}$ .

### Definition

We call x the **double limit** of the sequence $(x_{n,m})$ , written

$x_{n,m}\to x$

, or

$\lim _{\begin{smallmatrix}n\to \infty \\m\to \infty \end{smallmatrix}}x_{n,m}=x$

,

if the following condition holds:

For each

real number

$\varepsilon >0$

, there exists a

natural number

N

such that, for every pair of natural numbers

$n,m\geq N$

, we have

$|x_{n,m}-x|<\varepsilon$

.

In other words, for every measure of closeness $\varepsilon$ , the sequence's terms are eventually that close to the limit. The sequence $(x_{n,m})$ is said to **converge to** or **tend to** the limit x .

Symbolically, this is:

$\forall \varepsilon >0\left(\exists N\in \mathbb {N} \left(\forall n,m\in \mathbb {N} \left(n,m\geq N\implies |x_{n,m}-x|<\varepsilon \right)\right)\right)$

.

The double limit is different from taking limit in *n* first, and then in *m*. The latter is known as iterated limit. Given that both the double limit and the iterated limit exists, they have the same value. However, it is possible that one of them exist but the other does not.

### Infinite limits

A sequence $(x_{n,m})$ is said to **tend to infinity**, written

$x_{n,m}\to \infty$

, or

$\lim _{\begin{smallmatrix}n\to \infty \\m\to \infty \end{smallmatrix}}x_{n,m}=\infty$

,

if the following holds:

For every real number

K

, there is a natural number

N

such that for every pair of natural numbers

$n,m\geq N$

, we have

$x_{n,m}>K$

; that is, the sequence terms are eventually larger than any fixed

K

.

Symbolically, this is:

$\forall K\in \mathbb {R} \left(\exists N\in \mathbb {N} \left(\forall n,m\in \mathbb {N} \left(n,m\geq N\implies x_{n,m}>K\right)\right)\right)$

.

Similarly, a sequence $(x_{n,m})$ **tends to minus infinity**, written

$x_{n,m}\to -\infty$

, or

$\lim _{\begin{smallmatrix}n\to \infty \\m\to \infty \end{smallmatrix}}x_{n,m}=-\infty$

,

if the following holds:

For every real number

K

, there is a natural number

N

such that for every pair of natural numbers

$n,m\geq N$

, we have

$x_{n,m}<K$

; that is, the sequence terms are eventually smaller than any fixed

K

.

Symbolically, this is:

$\forall K\in \mathbb {R} \left(\exists N\in \mathbb {N} \left(\forall n,m\in \mathbb {N} \left(n,m\geq N\implies x_{n,m}<K\right)\right)\right)$

.

If a sequence tends to infinity or minus infinity, then it is divergent. However, a divergent sequence need not tend to plus or minus infinity, and the sequence $x_{n,m}=(-1)^{n+m}$ provides one such example.

### Pointwise limits and uniform limits

For a double sequence $(x_{n,m})$ , we may take limit in one of the indices, say, $n\to \infty$ , to obtain a single sequence $(y_{m})$ . In fact, there are two possible meanings when taking this limit. The first one is called **pointwise limit**, denoted

$x_{n,m}\to y_{m}\quad {\text{pointwise}}$

, or

$\lim _{n\to \infty }x_{n,m}=y_{m}\quad {\text{pointwise}}$

,

which means:

For each

real number

$\varepsilon >0$

and each fixed

natural number

m

, there exists a natural number

$N(\varepsilon ,m)>0$

such that, for every natural number

$n\geq N$

, we have

$|x_{n,m}-y_{m}|<\varepsilon$

.

Symbolically, this is:

$\forall \varepsilon >0\left(\forall m\in \mathbb {N} \left(\exists N\in \mathbb {N} \left(\forall n\in \mathbb {N} \left(n\geq N\implies |x_{n,m}-y_{m}|<\varepsilon \right)\right)\right)\right)$

.

When such a limit exists, we say the sequence $(x_{n,m})$ converges pointwise to $(y_{m})$ .

The second one is called **uniform limit**, denoted

$x_{n,m}\to y_{m}\quad {\text{uniformly}}$

,

$\lim _{n\to \infty }x_{n,m}=y_{m}\quad {\text{uniformly}}$

,

$x_{n,m}\rightrightarrows y_{m}$

, or

${\underset {n\to \infty }{\mathrm {unif} \lim }}\;x_{n,m}=y_{m}$

,

which means:

For each

real number

$\varepsilon >0$

, there exists a natural number

$N(\varepsilon )>0$

such that, for every

natural number

m

and for every natural number

$n\geq N$

, we have

$|x_{n,m}-y_{m}|<\varepsilon$

.

Symbolically, this is:

$\forall \varepsilon >0\left(\exists N\in \mathbb {N} \left(\forall m\in \mathbb {N} \left(\forall n\in \mathbb {N} \left(n\geq N\implies |x_{n,m}-y_{m}|<\varepsilon \right)\right)\right)\right)$

.

In this definition, the choice of N is independent of m . In other words, the choice of N is *uniformly applicable* to all natural numbers m . Hence, one can easily see that uniform convergence is a stronger property than pointwise convergence: the existence of uniform limit implies the existence and equality of pointwise limit:

If

$x_{n,m}\to y_{m}$

uniformly, then

$x_{n,m}\to y_{m}$

pointwise.

When such a limit exists, we say the sequence $(x_{n,m})$ converges uniformly to $(y_{m})$ .

### Iterated limit

For a double sequence $(x_{n,m})$ , we may take limit in one of the indices, say, $n\to \infty$ , to obtain a single sequence $(y_{m})$ , and then take limit in the other index, namely $m\to \infty$ , to get a number y . Symbolically,

$\lim _{m\to \infty }\lim _{n\to \infty }x_{n,m}=\lim _{m\to \infty }y_{m}=y$

.

This limit is known as **iterated limit** of the double sequence. The order of taking limits may affect the result, i.e.,

$\lim _{m\to \infty }\lim _{n\to \infty }x_{n,m}\neq \lim _{n\to \infty }\lim _{m\to \infty }x_{n,m}$

in general.

A sufficient condition of equality is given by the Moore-Osgood theorem, which requires the limit $\lim _{n\to \infty }x_{n,m}=y_{m}$ to be uniform in ${\textstyle m}$ .
