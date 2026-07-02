---
title: "Equioscillation theorem"
source: https://en.wikipedia.org/wiki/Equioscillation_theorem
domain: chebyshev-approximation
license: CC-BY-SA-4.0
tags: chebyshev approximation, clenshaw algorithm, chebyshev nodes, equioscillation theorem
fetched: 2026-07-02
---

# Equioscillation theorem

In mathematics, the **equioscillation theorem** concerns the approximation of continuous functions using polynomials when the merit function is the maximum difference (uniform norm). Its discovery is attributed to Chebyshev.

## Statement

Let f be a continuous function from $[a,b]$ to $\mathbb {R}$ . Among all the polynomials of degree $\leq n$ , the polynomial g minimizes the uniform norm of the difference $\|f-g\|_{\infty }$ if and only if there are $n+2$ points $a\leq x_{0}<x_{1}<\cdots <x_{n+1}\leq b$ such that $f(x_{i})-g(x_{i})=\sigma (-1)^{i}\|f-g\|_{\infty }$ where $\sigma$ is either -1 or +1.

That is, the polynomial g oscillates above and below f at the interpolation points, and does so to the same degree.

## Proof

Let us define the *equioscillation* condition as the condition in the theorem statement, that is, the condition that there exists $n+2$ ordered points in the interval such that the difference $f(x_{i})-g(x_{i})$ alternates in sign and is equal in magnitude to the uniform-norm of $f(x)-g(x)$ .

We need to prove that this condition is 'sufficient' for the polynomial g being the best uniform approximation to f , and we need to prove that this condition is 'necessary' for a polynomial to be the best uniform approximation.

### Sufficiency

Assume by contradiction that a polynomial $p(x)$ of degree less than or equal to n existed that provides a uniformly better approximation to f , which means that $\|f-p\|_{\infty }<\|f-g\|_{\infty }$ . Then the polynomial

$h(x)=g(x)-p(x)=(g(x)-f(x))-(p(x)-f(x))$

is also of degree less than or equal to n . However, for every $x_{i}$ of the $n+2$ points $x_{0},x_{1},...x_{n}$ , we know that $|p(x_{i})-f(x_{i})|<|g(x)-f(x)|$ because $|p(x_{i})-f(x_{i})|\leq \|f-p\|_{\infty }$ and $\|f-p||_{\infty }<\|f-g\|_{\infty }$ (since p is a better approximation than g ).

Therefore, $h(x_{i})=(g(x_{i})-f(x_{i}))-(p(x_{i})-f(x_{i}))$ will have the same sign as $g(x_{i})-f(x_{i})$ (because the second term has a smaller magnitude than the first). Thus, $h(x_{i})$ will also alternate sign on these $n+2$ points, and thus have at least $n+1$ roots. However, since h is a 'polynomial' of at most degree n , it should only have at most n roots. This is a contradiction.

### Necessity

Given a polynomial g , let us define $M=\|f(x)-g(x)\|_{\infty }$ . We will call a point x an *upper point* if $f(x)-g(x)=M$ and a *lower point* if it equals $-M$ instead.

Define an *alternating set* (given polynomial g and function f ) to be a set of ordered points $x_{0},...x_{n}$ in $[a,b]$ such that for every point $x_{i}$ in the alternating set, we have $f(x_{i})-g(x_{i})=\sigma (-1^{i})M$ , where $\sigma$ equals 1 or $-1$ as before.

Define a *sectioned alternating set* to be an alternating set $x_{0},...x_{n}$ along with nonempty closed intervals $I_{0},...I_{n}$ called *sections* such that 1. the sections partition $[a,b]$ (meaning that the union of the sections is the whole interval, and the intersection of any two sections is either empty or a single common endpoint) 2. For every i , the i th alternating point $x_{i}$ is in the i th section $I_{i}$ 3. If $x_{i}$ is an upper point, then $I_{i}$ contains no lower points. Likewise, if $x_{i}$ is a lower point, then $I_{i}$ contains no upper points.

Given an approximating polynomial g that does not satisfy the equioscillation condition, it is possible to show that the polynomial will have a two point alternating set. This alternating set can then be expanded to a sectioned alternating set. We can then use this sectioned alternating set to improve the approximation, unless the sectioned alternating set has more than $n+2$ points in which case our improvement cannot be guaranteed to still be a polynomial of degree at most n

## Variants

The equioscillation theorem is also valid when polynomials are replaced by rational functions: among all rational functions whose numerator has degree $\leq n$ and denominator has degree $\leq m$ , the rational function $g=p/q$ , with p and q being relatively prime polynomials of degree $n-\nu$ and $m-\mu$ , minimizes the uniform norm of the difference $\|f-g\|_{\infty }$ if and only if there are $m+n+2-\min\{\mu ,\nu \}$ points $a\leq x_{0}<x_{1}<\cdots <x_{m+n+1-\min\{\mu ,\nu \}}\leq b$ such that $f(x_{i})-g(x_{i})=\sigma (-1)^{i}\|f-g\|_{\infty }$ where $\sigma$ is either -1 or +1.

## Algorithms

Several minimax approximation algorithms are available, the most common being the Remez algorithm.
