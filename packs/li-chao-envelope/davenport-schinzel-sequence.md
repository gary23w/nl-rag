---
title: "Davenport–Schinzel sequence"
source: https://en.wikipedia.org/wiki/Davenport–Schinzel_sequence
domain: li-chao-envelope
license: CC-BY-SA-4.0
tags: li chao tree, line container query, lower envelope, kinetic segment tree
fetched: 2026-07-02
---

# Davenport–Schinzel sequence

In combinatorics, a **Davenport–Schinzel sequence** is a sequence of symbols in which the number of times any two symbols may appear in alternation is limited. The maximum possible length of a Davenport–Schinzel sequence is bounded by the number of its distinct symbols multiplied by a small but nonconstant factor that depends on the number of alternations that are allowed. Davenport–Schinzel sequences were first defined in 1965 by Harold Davenport and Andrzej Schinzel to analyze linear differential equations. Following Atallah (1985) these sequences and their length bounds have also become a standard tool in discrete geometry and in the analysis of geometric algorithms.

## Definition

A finite sequence *U* = *u*1, *u*2, *u*3, is said to be a Davenport–Schinzel sequence of order *s* if it satisfies the following two properties:

1. No two consecutive values in the sequence are equal to each other.
2. If *x* and *y* are two distinct values occurring in the sequence, then the sequence does not contain a subsequence ... *x*, ... *y*, ..., *x*, ..., *y*, ... consisting of *s* + 2 values alternating between *x* and *y*.

For instance, the sequence

1, 2, 1, 3, 1, 3, 2, 4, 5, 4, 5, 2, 3

is a Davenport–Schinzel sequence of order 3: it contains alternating subsequences of length four, such as ...1, ... 2, ... 1, ... 2, ... (which appears in four different ways as a subsequence of the whole sequence) but it does not contain any alternating subsequences of length five.

If a Davenport–Schinzel sequence of order *s* includes *n* distinct values, it is called an (*n*,*s*) Davenport–Schinzel sequence, or a *DS*(*n*,*s*)-sequence.

## Length bounds

The complexity of *DS*(*n*,*s*)-sequence has been analyzed asymptotically in the limit as *n* goes to infinity, with the assumption that *s* is a fixed constant, and nearly tight bounds are known for all *s*. Let *λ**s*(*n*) denote the length of the longest *DS*(*n*,*s*)-sequence. The best bounds known on *λ**s* involve the inverse Ackermann function

α(

n

) = min {

m

|

A

(

m

,

m

) ≥

n

},

where *A* is the Ackermann function. Due to the very rapid growth of the Ackermann function, its inverse α grows very slowly, and is at most four for problems of any practical size.

Using big O and big Θ notation, the following bounds are known:

- $\lambda _{0}(n)=1$ .
- $\lambda _{1}(n)=n$ .
- $\lambda _{2}(n)=2n-1$ .
- $\lambda _{3}(n)=2n\alpha (n)+O(n)$ . This complexity bound can be realized to within a factor of 2 by line segments: there exist arrangements of *n* line segments in the plane whose lower envelopes have complexity Ω(*n* α(*n*)).
- $\lambda _{4}(n)=\Theta (n2^{\alpha (n)})$ .
- $\lambda _{5}(n)=\Theta (n\alpha (n)2^{\alpha (n)})$ .
- For both even and odd values of *s* ≥ 6,

$\lambda _{s}(n)=n\cdot 2^{{\frac {1}{t!}}\alpha (n)^{t}+O(\alpha (n)^{t-1})}$

, where

$t=\left\lfloor {\frac {s-2}{2}}\right\rfloor$

.

The value of *λ**s*(*n*) is also known when *s* is variable but *n* is a small constant:

$\lambda _{s}(1)=1\,$

$\lambda _{s}(2)=s+1\,$

$\lambda _{s}(3)=3s-2+(s{\bmod {2}})$

$\lambda _{s}(4)=6s-2+(s{\bmod {2}}).$

When *s* is a function of *n* the upper and lower bounds on Davenport-Schinzel sequences are not tight.

- When $s>n^{1/t}(t-1)!$ , $\lambda _{s}(n)=\Omega (n^{2}s/(t-1)!)$ and $\lambda _{s}(n)=O(n^{2}s)$ .
- When $\log \log n<s=n^{o(1)}$ , $\lambda _{s}(n)=\Omega \left(n\left({\frac {s}{2\log \log _{s}n}}\right)^{\log \log _{s}n}\right)$ .
- When $s\leq \log \log n$ , $\lambda _{s}(n)=\Omega (n2^{s})$ .

## Application to lower envelopes

The lower envelope of a set of functions ƒ*i*(*x*) of a real variable *x* is the function given by their pointwise minimum:

ƒ(

x

)

=

min

i

ƒ

i

(

x

).

Suppose that these functions are particularly well behaved: they are all continuous, and any two of them are equal on at most *s* values. With these assumptions, the real line can be partitioned into finitely many intervals within which one function has values smaller than all of the other functions. The sequence of these intervals, labeled by the minimizing function within each interval, forms a Davenport–Schinzel sequence of order *s*. Thus, any upper bound on the complexity of a Davenport–Schinzel sequence of this order also bounds the number of intervals in this representation of the lower envelope.

In the original application of Davenport and Schinzel, the functions under consideration were a set of different solutions to the same homogeneous linear differential equation of order *s*. Any two distinct solutions can have at most *s* values in common, so the lower envelope of a set of *n* distinct solutions forms a *DS*(*n*,*s*)-sequence.

The same concept of a lower envelope can also be applied to functions that are only piecewise continuous or that are defined only over intervals of the real line; however, in this case, the points of discontinuity of the functions and the endpoints of the interval within which each function is defined add to the order of the sequence. For instance, a non-vertical line segment in the plane can be interpreted as the graph of a function mapping an interval of *x* values to their corresponding *y* values, and the lower envelope of a collection of line segments forms a Davenport–Schinzel sequence of order three because any two line segments can form an alternating subsequence with length at most four.
