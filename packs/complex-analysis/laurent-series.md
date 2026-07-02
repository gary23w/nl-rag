---
title: "Laurent series"
source: https://en.wikipedia.org/wiki/Laurent_series
domain: complex-analysis
license: CC-BY-SA-4.0
tags: complex analysis, holomorphic function, residue theorem, conformal map
fetched: 2026-07-02
---

# Laurent series

In mathematics, the **Laurent series** of a complex function $f(z)$ is a representation of that function as a power series which includes terms of negative degree. It may be used to express complex functions in cases where a Taylor series expansion cannot be applied. The Laurent series was named after and first published by Pierre Alphonse Laurent in 1843. Karl Weierstrass had previously described it in a paper written in 1841 but not published until 1894.

## Definition

The Laurent series for a complex function $f(z)$ about an arbitrary point c is given by $f(z)=\sum _{n=-\infty }^{\infty }a_{n}(z-c)^{n},$ where the coefficients $a_{n}$ are defined by a contour integral that generalizes Cauchy's integral formula: $a_{n}={\frac {1}{2\pi i}}\oint _{\gamma }{\frac {f(z)}{(z-c)^{n+1}}}\,dz.$

The path of integration $\gamma$ is counterclockwise around a Jordan curve enclosing c and lying in an annulus A in which $f(z)$ is holomorphic (analytic). The expansion for $f(z)$ will then be valid anywhere inside the annulus. The annulus is shown in red in the figure on the right, along with an example of a suitable path of integration labeled $\gamma$ . When $\gamma$ is defined as the circle $|z-c|=\varrho$ , where $r<\varrho <R$ , this amounts to computing the complex Fourier coefficients of the restriction of f to $\gamma$ . The fact that these integrals are unchanged by a deformation of the contour $\gamma$ is an immediate consequence of Cauchy's integral theorem.

One may also obtain the Laurent series for a complex function $f(z)$ at $z=\infty$ . However, this is the same as when $R\rightarrow \infty$ .

The above integral formula may not offer the most practical method for computing the coefficients $a_{n}$ for a given function $f(z)$ ; instead, one often pieces together the Laurent series by combining known Taylor expansions. Because the Laurent expansion of a function is unique whenever it exists, any expression of this form that equals the given function $f(z)$ in some annulus must actually be the Laurent expansion of $f(z)$ .

## Convergence

Laurent series with complex coefficients are an important tool in complex analysis, especially to investigate the behavior of functions near singularities.

Consider for instance the function $f(x)=e^{-1/x^{2}}$ with $f(0)=0$ . As a real function, it is infinitely differentiable everywhere; as a complex function however it is not differentiable at $x=0$ . The Laurent series of $f(x)$ is obtained via the power series representation, $e^{-1/x^{2}}=\sum _{n=0}^{\infty }(-1)^{n}\,{x^{-2n} \over n!},$ which converges to $f(x)$ for all $x\in \mathbb {C}$ except at the singularity $x=0$ . The graph on the right shows $f(x)$ in black and its Laurent approximations $\sum _{n=0}^{N}(-1)^{n}\,{x^{-2n} \over n!},\quad \forall N\in \mathbb {N} ^{+}.$ As $N\to \infty$ , the approximation becomes exact for all (complex) numbers x except at the singularity $x=0$ .

More generally, Laurent series can be used to express holomorphic functions defined on an annulus, much as power series are used to express holomorphic functions defined on a disc.

Suppose $\sum _{n=-\infty }^{\infty }a_{n}(z-c)^{n}$ is a given Laurent series with complex coefficients $a_{n}$ and a complex center c . Then there exists a unique inner radius r and outer radius R such that:

- The Laurent series converges on the open annulus $A=\{z:r<|z-c|<R\}$ . That is, both the positive- and negative degree power series converge. Furthermore, this convergence will be uniform on compact sets. Finally, the convergent series defines a holomorphic function $f(z)$ on A .
- Outside the annulus, the Laurent series diverges. That is, at each point in the exterior of A , either the positive- or negative degree power series diverges.
- On the boundary of the annulus, one cannot make a general statement, except that there is at least one point on the inner boundary and one point on the outer boundary such that $f(z)$ cannot be holomorphically extended to those points; giving rise to a Riemann-Hilbert problem.

It is possible that r may be zero or R may be infinite; at the other extreme, it's not necessarily true that r is less than R . These radii can be computed by taking the limit superior of the coefficients $a_{n}$ such that: ${\begin{aligned}r&=\limsup _{n\to \infty }|a_{-n}|^{\frac {1}{n}},\\{\frac {1}{R}}&=\limsup _{n\to \infty }|a_{n}|^{\frac {1}{n}}.\end{aligned}}$

When $r=0$ , the coefficient $a_{-1}$ of the Laurent expansion is called the **residue** of $f(z)$ at the singularity c . For example, the function $f(z)={e^{z} \over z}+e^{{1}/{z}},$ is holomorphic everywhere except at $z=0$ . The Laurent expansion about $c=0$ can then be obtained from the power series representation: $f(z)=\cdots +\left({1 \over 3!}\right)z^{-3}+\left({1 \over 2!}\right)z^{-2}+2z^{-1}+2+\left({1 \over 2!}\right)z+\left({1 \over 3!}\right)z^{2}+\left({1 \over 4!}\right)z^{3}+\cdots ,$ hence, the residue is given by $a_{-1}=2$ .

Conversely, for a holomorphic function $f(z)$ defined on the annulus $A=\{z:r<|z-c|<R\}$ , there always exists a unique Laurent series with center c which converges (at least on A ) to $f(z)$ .

For example, consider the following rational function, along with its partial fraction expansion: $f(z)={\frac {1}{(z-1)(z-2i)}}={\frac {1+2i}{5}}\left({\frac {1}{z-1}}-{\frac {1}{z-2i}}\right).$

This function has singularities at $z=1$ and $z=2i$ , where the denominator is zero and the expression is therefore undefined. A Taylor series about $z=0$ (which yields a power series) will only converge in a disc of radius 1, since it "hits" the singularity at $z=1$ .

However, there are three possible Laurent expansions about 0, depending on the radius of z :

- One series is defined on the inner disc where |*z*| < 1; it is the same as the Taylor series, $f(z)={\frac {1+2i}{5}}\sum _{n=0}^{\infty }\left({\frac {1}{(2i)^{n+1}}}-1\right)z^{n}.$ This follows from the partial fraction form of the function, along with the formula for the sum of a geometric series, ${\frac {1}{z-a}}=-{\frac {1}{a}}\sum _{n=0}^{\infty }\left({\tfrac {z}{a}}\right)^{n}$ for $|z|<|a|$ .
- The second series is defined on the middle annulus where $1<z<2$ is caught between the two singularities: $f(z)={\frac {1+2i}{5}}\left(\sum _{n=1}^{\infty }z^{-n}+\sum _{n=0}^{\infty }{\frac {1}{(2i)^{n+1}}}z^{n}\right).$ Here, we use the alternative form of the geometric series summation, ${\frac {1}{z-a}}={\frac {1}{z}}\sum _{n=0}^{\infty }\left({\frac {a}{z}}\right)^{n}$ for $|z|>|a|$ .
- The third series is defined on the infinite outer annulus where $2<z<\infty$ , (which is also the Laurent expansion at $z=\infty$ ) $f(z)={\frac {1+2i}{5}}\sum _{n=1}^{\infty }\left(1-(2i)^{n-1}\right)z^{-n}.$ This series can be derived using geometric series as before, or by performing polynomial long division of 1 by $(x-1)(x-2i)$ , not stopping with a remainder but continuing into $x^{-n}$ terms; indeed, the "outer" Laurent series of a rational function is analogous to the decimal form of a fraction. (The "inner" Taylor series expansion can be obtained similarly, just by reversing the term order in the division algorithm.)

## Uniqueness

Suppose a function $f(z)$ holomorphic on the annulus $r<|z-c|<R$ has two Laurent series: $f(z)=\sum _{n=-\infty }^{\infty }a_{n}(z-c)^{n}=\sum _{n=-\infty }^{\infty }b_{n}(z-c)^{n}.$

Multiply both sides by $(z-c)^{-k-1}$ , where k is an arbitrary integer, and integrate on a path γ inside the annulus, $\oint _{\gamma }\,\sum _{n=-\infty }^{\infty }a_{n}(z-c)^{n-k-1}\,dz=\oint _{\gamma }\,\sum _{n=-\infty }^{\infty }b_{n}(z-c)^{n-k-1}\,dz.$

The series converges uniformly on $r+\varepsilon \leq |z-c|\leq R-\varepsilon$ , where *ε* is a positive number small enough for *γ* to be contained in the constricted closed annulus, so the integration and summation can be interchanged. Substituting the identity $\oint _{\gamma }\,(z-c)^{n-k-1}\,dz=2\pi i\delta _{nk}$ into the summation yields $a_{k}=b_{k}.$

Hence the Laurent series is unique.

## Laurent polynomials

A **Laurent polynomial** is a Laurent series in which only finitely many coefficients are non-zero. Laurent polynomials differ from ordinary polynomials in that they may have terms of negative degree.

## Principal part

The **principal part** of a Laurent series is the series of terms with negative degree, that is $\sum _{k=-\infty }^{-1}a_{k}(z-c)^{k}.$

If the principal part of f is a finite sum, then f has a pole at c of order equal to (negative) the degree of the highest term; on the other hand, if f has an essential singularity at c , the principal part is an infinite sum (meaning it has infinitely many non-zero terms).

If the inner radius of convergence of the Laurent series for f is 0, then f has an essential singularity at c if and only if the principal part is an infinite sum, and has a pole otherwise.

If the inner radius of convergence is positive, f may have infinitely many negative terms but still be regular at c , as in the example above, in which case it is represented by a *different* Laurent series in a disk about  c .

Laurent series with only finitely many negative terms are well-behaved—they are a power series divided by $z^{k}$ , and can be analyzed similarly—while Laurent series with infinitely many negative terms have complicated behavior on the inner circle of convergence.

## Multiplication and sum

Laurent series cannot in general be multiplied. Algebraically, the expression for the terms of the product may involve infinite sums which need not converge (one cannot take the convolution of integer sequences). Geometrically, the two Laurent series may have non-overlapping annuli of convergence.

Two Laurent series with only *finitely* many negative terms can be multiplied: algebraically, the sums are all finite; geometrically, these have poles at c , and inner radius of convergence 0, so they both converge on an overlapping annulus.

Thus when defining formal Laurent series, one requires Laurent series with only finitely many negative terms.

Similarly, the sum of two convergent Laurent series need not converge, though it is always defined formally, but the sum of two bounded below Laurent series (or any Laurent series on a punctured disk) has a non-empty annulus of convergence.

Also, for a field F , by the sum and multiplication defined above, formal Laurent series would form a field $F((x))$ which is also the field of fractions of the ring $F[[x]]$ of formal power series.
