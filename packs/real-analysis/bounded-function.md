---
title: "Bounded function"
source: https://en.wikipedia.org/wiki/Bounded_function
domain: real-analysis
license: CC-BY-SA-4.0
tags: real analysis, uniform convergence, riemann integral, metric space
fetched: 2026-07-02
---

# Bounded function

In mathematics, a function f defined on some set X with real or complex values is called **bounded** if the set of its values (its image) is bounded. In other words, there exists a real number M such that

$|f(x)|\leq M$

for all x in X . A function that is *not* bounded is said to be **unbounded**.

If f is real-valued and $f(x)\leq A$ for all x in X , then the function is said to be **bounded (from) above** by A . If $f(x)\geq B$ for all x in X , then the function is said to be **bounded (from) below** by B . A real-valued function is bounded if and only if it is bounded from above and below.

An important special case is a **bounded sequence**, where *X* is taken to be the set $\mathbb {N}$ of natural numbers. Thus a sequence $f=(a_{0},a_{1},a_{2},\ldots )$ is bounded if there exists a real number M such that

$|a_{n}|\leq M$

for every natural number n . The set of all bounded sequences forms the sequence space $l^{\infty }$ .

The definition of boundedness can be generalized to functions $f:X\rightarrow Y$ taking values in a more general space Y by requiring that the image $f(X)$ is a bounded set in Y .

Weaker than boundedness is local boundedness. A family of bounded functions may be uniformly bounded.

A bounded operator *$T:X\rightarrow Y$* is not a bounded function in the sense of this page's definition (unless $T=0$ ), but has the weaker property of **preserving boundedness**; bounded sets $M\subseteq X$ are mapped to bounded sets *$T(M)\subseteq Y$ .* This definition can be extended to any function $f:X\rightarrow Y$ if *X* and *Y* allow for the concept of a bounded set. Boundedness can also be determined by looking at a graph.

## Examples

- The sine function ${\displaystyle \sin$ is bounded since $|\sin(x)|\leq 1$ for all $x\in \mathbb {R}$ .
- The function $f(x)=(x^{2}-1)^{-1}$ , defined for all real x except for −1 and 1, is unbounded. As *x* approaches −1 or 1, the values of this function get larger in magnitude. This function can be made bounded if one restricts its domain to be, for example, $[2,\infty )$ or $(-\infty ,-2]$ .
- The function ${\textstyle f(x)=(x^{2}+1)^{-1}}$ , defined for all real *x*, *is* bounded, since ${\textstyle |f(x)|\leq 1}$ for all *x*.
- The inverse trigonometric function arctangent defined as: $y=\arctan(x)$ or $x=\tan(y)$ is increasing for all real numbers *x* and bounded with $-{\frac {\pi }{2}}<y<{\frac {\pi }{2}}$ radians
- By the boundedness theorem, every continuous function on a closed interval, such as $f:[0,1]\rightarrow \mathbb {R}$ , is bounded. More generally, any continuous function from a compact space into a metric space is bounded.
- All complex-valued functions $f:\mathbb {C} \rightarrow \mathbb {C}$ which are entire are either unbounded or constant as a consequence of Liouville's theorem. In particular, the complex ${\displaystyle \sin$ must be unbounded since it is entire.
- The function f which takes the value 0 for x rational number and 1 for *x* irrational number (cf. Dirichlet function) *is* bounded. Thus, a function does not need to be "nice" in order to be bounded. The set of all bounded functions defined on $[0,1]$ is much larger than the set of continuous functions on that interval. Moreover, continuous functions need not be bounded; for example, the functions $g:\mathbb {R} ^{2}\to \mathbb {R}$ and $h:(0,1)^{2}\to \mathbb {R}$ defined by $g(x,y):=x+y$ and $h(x,y):={\frac {1}{x+y}}$ are both continuous, but neither is bounded. (However, a continuous function must be bounded if its domain is both closed and bounded.)
