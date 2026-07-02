---
title: "Analytic function"
source: https://en.wikipedia.org/wiki/Analytic_function
domain: complex-analysis
license: CC-BY-SA-4.0
tags: complex analysis, holomorphic function, residue theorem, conformal map
fetched: 2026-07-02
---

# Analytic function

In mathematical analysis, an **analytic function** is a function that is locally represented by a convergent power series. More precisely, a real or complex function is analytic at a point if, in some neighborhood of that point, it is equal to a power series centered there. Analytic functions are therefore locally determined by their coefficients, or equivalently by their derivatives at the center of the expansion. In other words, an analytic function is a function that is locally represented by a convergent Taylor series.

Analytic functions occur in both real analysis and complex analysis, in slightly different ways. A real or complex analytic function is necessarily smooth, having derivatives of all orders. But a smooth real function need not be analytic. By contrast, a complex function on an open set is analytic if and only if it is holomorphic, that is, complex differentiable at every point of the set. For this reason, in complex analysis the terms *analytic function* and *holomorphic function* are often used interchangeably. The terms **complex analytic** and **real analytic** distinguish between these cases. In signal processing, a complex analytic function is sometimes called an analytic signal.

Analyticity is a strong regularity condition. Analytic functions have rigid local behavior: for example, on a connected domain, an analytic function whose zeros have an accumulation point must vanish identically. Standard examples include polynomials, the exponential function, and the trigonometric functions on their domains of analyticity.

## Definitions

Formally, a function f is *real analytic* on an open set D in the real line if for every $x_{0}\in D$ one can write $f(x)=\sum _{n=0}^{\infty }a_{n}\left(x-x_{0}\right)^{n}=a_{0}+a_{1}(x-x_{0})+a_{2}(x-x_{0})^{2}+\cdots$ in which the coefficients ⁠ $a_{0}$ ⁠, ⁠ $a_{1}$ ⁠, ...are real numbers and this series (the right-hand side of this equation) is convergent to $f(x)$ for x in a neighborhood of $x_{0}$ (that is a set containing an open set including ⁠ $x_{0}$ ⁠).

Alternatively, a real analytic function is an infinitely differentiable function such that the Taylor series at each point $x_{0}$ in its domain $T(x)=\sum _{n=0}^{\infty }{\frac {f^{(n)}(x_{0})}{n!}}(x-x_{0})^{n}$ converges to $f(x)$ for x in a neighborhood of $x_{0}$ pointwise. The set of all real analytic functions on a given set D is often denoted by ⁠ ${\mathcal {C}}^{\omega }(D)$ ⁠, or just by ${\mathcal {C}}^{\omega }$ if the domain is understood.

A function f defined on some subset of the real line is said to be real analytic at a point x if there is a neighborhood D of x on which f is real analytic.

The definition of a *complex analytic function* is obtained by replacing, in the definitions above, "real" with "complex" and "real line" with "complex plane". A function is complex analytic if and only if it is holomorphic i.e. it is complex differentiable. For this reason the terms "holomorphic" and "analytic" are often used interchangeably for such functions.

In complex analysis, a function is called analytic in an open set ⁠ U ⁠ if it is (complex) differentiable at each point in ⁠ U ⁠.

## Examples

Typical examples of analytic functions are

- The following elementary functions:
  - All polynomials: if a polynomial has degree ⁠ n ⁠, any terms of degree larger than ⁠ n ⁠ in its Taylor series expansion must immediately vanish to 0, and so this series will be trivially convergent. Furthermore, every polynomial is its own Maclaurin series.
  - The exponential function is analytic. Any Taylor series for this function converges not only for ⁠ x ⁠ close enough to ⁠ $x_{0}$ ⁠ (as in the definition) but for all values of ⁠ x ⁠ (real or complex).
  - The trigonometric functions are analytic on any open set of their domain.
  - The natural logarithm is analytic on any open set where its branch is single-valued, such as $(0,\infty )$ or the complement in the Riemann sphere of any simple arc connecting 0 to $\infty$ .
  - Power functions are analytic everywhere for non-negative integral powers, away from zero for negative integral powers, and for arbitrary complex powers on any open subset of the complex plane where the logarithm is analytic.
- Many special functions are analytic on a suitable domain:
  - hypergeometric functions on suitable domains
  - Bessel functions on suitable domains
  - The gamma function away from its poles at zero and the negative integers
  - The Riemann zeta function except for a simple pole at 1
- Algebraic functions are analytic away from any poles and branch points they may have. Near a branch point, an algebraic function can be represented by a convergent Puiseux series; equivalently, after a change of variable $z-a=t^{e}$ , it becomes analytic as a function of t .

Typical examples of functions that are not analytic are

- The absolute value function $x\mapsto |x|$ on the real numbers is not analytic at 0 . The corresponding function $z\mapsto |z|$ on the complex numbers is not complex analytic on any nonempty open subset of $\mathbb {C}$ .
- Piecewise defined functions (functions given by different formulae in different regions) are typically not analytic where the pieces meet.
- The complex conjugate function ⁠ $z\to z^{*}$ ⁠ is not complex analytic, although its restriction to the real line is the identity function and therefore real analytic, and it is real analytic as a function from $\mathbb {R} ^{2}$ to ⁠ $\mathbb {R} ^{2}$ ⁠.
- Other non-analytic smooth functions, and in particular any smooth function f with compact support that is not identically zero, i.e. $f\in C_{0}^{\infty }(\mathbb {R} ^{n})\setminus \{0\}$ , cannot be analytic on all of $\mathbb {R} ^{n}$ .

## Alternative characterizations

The following conditions are equivalent:

1. f is real analytic on an open set ⁠ D ⁠.
2. There is a complex analytic extension of f to an open set $G\subset \mathbb {C}$ that contains ⁠ D ⁠.
3. f is smooth and for every compact set $K\subset D$ there exists a constant C such that for every $x\in K$ and every non-negative integer k the following bound holds; $\left|{\frac {d^{k}f}{dx^{k}}}(x)\right|\leq C^{k+1}k!$

Complex analytic functions are exactly equivalent to holomorphic functions, and are thus much more easily characterized.

For the case of an analytic function with several variables (see below), the real analyticity can be characterized using the Fourier–Bros–Iagolnitzer transform.

In the multivariable case, real analytic functions satisfy a direct generalization of the third characterization. Let $U\subset \mathbb {R} ^{n}$ be an open set, and let ⁠ $f:U\to \mathbb {R}$ ⁠. Then f is real analytic on U if and only if $f\in C^{\infty }(U)$ and for every compact $K\subseteq U$ there exists a constant C such that for every multi-index $\alpha \in \mathbb {Z} _{\geq 0}^{n}$ the following bound holds $\sup _{x\in K}\left|{\frac {\partial ^{\alpha }f}{\partial x^{\alpha }}}(x)\right|\leq C^{|\alpha |+1}\alpha !$

## Properties of analytic functions

- The sums, products, and compositions of analytic functions are analytic.
- The reciprocal of an analytic function that is nowhere zero is analytic.
- In one variable, the inverse of a one-to-one analytic function whose derivative is nowhere zero is analytic. In several variables, the corresponding condition is that the derivative be an invertible linear map, or equivalently that the Jacobian determinant be nonzero.
- Any analytic function is smooth, that is, infinitely differentiable. The converse is not true for real functions; in fact, in a certain sense, the real analytic functions are sparse compared to all real infinitely differentiable functions. For the complex numbers, the converse does hold: any function with a single complex derivative on an open set is analytic on that set (see *§ Analyticity and differentiability*).
- For any open set ⁠ $\Omega \subseteq \mathbb {C}$ ⁠, the set ⁠ $A(\Omega )$ ⁠ of all analytic functions $u:\Omega \to \mathbb {C}$ is a Fréchet space with respect to the uniform convergence on compact sets. The fact that uniform limits on compact sets of analytic functions are analytic is an easy consequence of Morera's theorem. The set $A_{\infty }(\Omega )$ of all bounded analytic functions with the supremum norm is a Banach space.
- In contrast, the real analytic functions on an open set are not complete under the topology of uniform convergence on compact subsets, since compact-open limits of real analytic functions need not be real analytic. Real analytic functions are dense in the space of continuous functions in the compact-open topology.

A polynomial cannot be zero at too many points unless it is the zero polynomial (more precisely, the number of zeros is at most the degree of the polynomial). A similar but weaker statement holds for analytic functions. If the set of zeros of an analytic function ⁠ f ⁠ has an accumulation point inside its domain, then ⁠ f ⁠ is zero everywhere on the connected component containing the accumulation point. In other words, if ⁠ $(r_{n})$ ⁠ is a sequence of distinct numbers such that ⁠ $f(r_{n})=0$ ⁠ for all ⁠ n ⁠ and this sequence converges to a point ⁠ r ⁠ in the domain of ⁠ D ⁠, then ⁠ f ⁠ is identically zero on the connected component of ⁠ D ⁠ containing ⁠ r ⁠. This is known as the identity theorem.

Also, if all the derivatives of an analytic function at a point are zero, the function is constant on the corresponding connected component.

These statements imply that while analytic functions do have more degrees of freedom than polynomials, they are still quite rigid.

## Analyticity and differentiability

As noted above, any function (real or complex) is infinitely differentiable on a neighborhood where it is equal to a convergent power series. In a neighborhood of a point of analyticity, there is a convergent power series equal to the function in the neighborhood, so the function is infinitely differentiable there. There exist smooth real functions that are not analytic: see *Non-analytic smooth function*. In fact there are many such functions.

The situation is quite different when one considers complex analytic functions and complex derivatives. Any complex-differentiable function in an open disc centered at $z=z_{0}$ (holomorphic function) is analytic there, and conversely any function given by a convergent power series in the complex variable $z-z_{0}$ is complex differentiable (and infinitely differentiable) on the disk of convergence. Consequently, in complex analysis, the term *analytic function* is synonymous with *holomorphic function*.

## Real versus complex analytic functions

Real and complex analytic functions have important differences (one could notice that even from their different relationship with differentiability). Analyticity of complex functions is a more restrictive property, as it has more restrictive necessary conditions and complex analytic functions have more structure than their real-line counterparts.

According to Liouville's theorem, any bounded complex analytic function defined on the whole complex plane is constant. The corresponding statement for real analytic functions, with the complex plane replaced by the real line, is clearly false; this is illustrated by $f(x)={\frac {1}{x^{2}+1}}.$

Also, if a complex analytic function is defined in an open ball around a point ⁠ $x_{0}$ ⁠, its power series expansion at ⁠ $x_{0}$ ⁠ is convergent in the whole open ball (holomorphic functions are analytic). This statement for real analytic functions (with open ball meaning an open interval of the real line rather than an open disk of the complex plane) is not true in general; the function of the example above gives an example for ⁠ $x_{0}=0$ ⁠ and a ball of radius exceeding ⁠ 1 ⁠, since the power series ⁠ $1-x^{2}+x^{4}-x^{6}+\ldots$ ⁠ diverges for ⁠ $\vert x\vert \geq 1$ ⁠.

Any real analytic function on some open set on the real line can be extended to a complex analytic function on some open set of the complex plane. However, not every real analytic function defined on the whole real line can be extended to a complex function defined on the whole complex plane. The function ⁠ $f(x)$ ⁠ defined in the paragraph above is a counterexample, as it is not defined for ⁠ $x=\pm i$ ⁠. This explains why the Taylor series of ⁠ $f(x)$ ⁠ diverges for ⁠ $\vert x\vert >1$ ⁠, i.e., the radius of convergence is ⁠ 1 ⁠ because the complexified function has a pole at distance ⁠ 1 ⁠ from the evaluation point ⁠ 0 ⁠ and no further poles within the open disc of radius ⁠ 1 ⁠ around the evaluation point.

## Taylor series and radius of convergence

If a function is analytic at a , then its Taylor series converges *to the function* in some open neighborhood of a . More generally, for any power series $\sum _{n=0}^{\infty }c_{n}(x-a)^{n},$ there is a number R called the radius of convergence, which can be any non-negative number or $+\infty$ , such that the power series converges absolutely for $|x-a|<R$ and diverges for $|x-a|>R$ . Thus, when a Taylor series converges, it does so in an open interval centered at a in the real case, or a disc centered at a in the complex case. A Taylor series may converge absolutely or conditionally at some, all, or none of the boundary points of the open interval or disc.

In complex analysis, the radius of convergence of a holomorphic function at a point is the radius of the largest open disc centered at that point on which the function remains holomorphic. In many common cases, this is the distance to the nearest singularity of the function in the complex plane.

This explains the different radii of convergence for familiar Taylor series. The series for $e^{z}$ , $\sin z$ , and $\cos z$ have infinite radius of convergence because these are entire functions, having no singularities in the complex plane. By contrast, the Taylor series for $\log(1+z)$ around $z=0$ has radius of convergence 1 , because the nearest singularity is at $z=-1$ .

Complex singularities can determine the radius of convergence even for functions that are smooth on the real line. For example, although $f(x)={\frac {1}{1+x^{2}}}$ is smooth for all real x , the radius of convergence of its Taylor series around $x=0$ is 1 , because the corresponding complex function has singularities at $x=i$ and $x=-i$ , which are points of the complex unit circle. Thus, even for real-valued functions, the role of complex singularities is important: a function can be infinitely differentiable on the whole real line, and yet have a Taylor series with only a finite radius of convergence, because the limiting obstruction can come from singularities in the corresponding complex function rather than any failure of smoothness on the real axis.

A power series may converge at every point of the boundary of its disc of convergence and still fail to extend holomorphically beyond that disc. For example, if $\alpha >0$ is not an integer, then the binomial series $(1+z)^{\alpha }=\sum _{n=0}^{\infty }{\binom {\alpha }{n}}z^{n}$ has radius of convergence $R=1$ . The series converges everywhere on the closed unit disc, including every boundary point. However, for nonintegral $\alpha$ , the function $(1+z)^{\alpha }$ does not extend as a single-valued holomorphic function to any neighborhood of $z=-1$ . Thus the obstruction to analytic continuation at the boundary point $z=-1$ is not a failure of convergence of the power series, nor a pole or essential singularity, but the branching of the analytic continuation. In effect, $z=-1$ is a branch point of the function. This illustrates that convergence on the closed disc is weaker than holomorphic extendibility beyond the boundary.

## Analytic continuation

Because analytic functions are locally represented by power series, a value of the function on one small neighborhood can sometimes determine values on a larger region. This process is called analytic continuation. Starting with a power series representation in one neighborhood, one can then sometimes use this to define the function on overlapping neighborhoods, and continue this process along paths in the domain.

Analytic continuation is unique when it exists on a connected domain. More precisely, if two analytic functions on a connected open set agree on a nonempty open subset, or more generally on a set having an accumulation point in the domain, then they agree everywhere on that connected open set. This is a form of the identity theorem.

However, analytic continuation need not be possible everywhere, and it need not be single-valued. For example, the natural logarithm is locally analytic on $\mathbb {C} \setminus \{0\}$ , but continuation around a closed path encircling 0 changes its value by an integer multiple of $2\pi i$ . For this reason, a single-valued branch of the logarithm can be defined on domains such as $\mathbb {C} \setminus (-\infty ,0]$ , but not on all of $\mathbb {C} \setminus \{0\}$ . Taking a single analytic function in a disc and forming all possible analytic continuations of it leads in general to a Riemann surface that covers an open subset of the Riemann sphere. The global analytic function obtained in this way is naturally a sheaf rather than a function: each germ is a convergent power series in some disc, but multiple germs may be stacked on top of each other.

Algebraic functions give another source of multi-valued analytic continuation. For example, the function $f(z)={\sqrt {1-z}}$ is analytic, where the branch is such that $f(0)=1$ , has a convergent power series in the disc $|z|<1$ . It can be continued around a loop enclosing $z=1$ , but transforms to its negative after a single loop. The Riemann surface associated with an algebraic function is a finite ramified cover of the Riemann sphere.

Many special functions are first defined by a power series or an integral formula on a restricted domain and then extended by analytic continuation. For example, the Riemann zeta function is initially defined by the Dirichlet series $\zeta (s)=\sum _{n=1}^{\infty }{\frac {1}{n^{s}}}$ for $\operatorname {Re} (s)>1$ , but it has a meromorphic continuation to the complex plane, with a single simple pole at $s=1$ .

## Analytic functions of several variables

One can define analytic functions in several variables by means of power series in those variables (see *Power series*). Analytic functions of several variables have some of the same properties as analytic functions of one variable. However, especially for complex analytic functions, new and interesting phenomena show up in two or more complex dimensions:

- Zero sets of complex analytic functions in more than one variable are never discrete if they are non-empty. This can be proved by Hartogs's extension theorem.
- Domains of holomorphy for single-valued functions consist of arbitrary (connected) open sets. In several complex variables, however, only some connected open sets are domains of holomorphy. The characterization of domains of holomorphy leads to the notion of pseudoconvexity.

## Analytic functions over other valued fields

Analogous notions of analyticity can be formulated over other complete valued fields, the real and complex numbers being the two most prominent ones where the absolute value is archimedean. Analytic functions can also be defined over non-Archimedean local fields, such as the p-adic numbers $\mathbb {Q} _{p}$ and its finite extension fields, and fields of formal Laurent series $\mathbb {F} _{q}((t))$ over a finite field.

If K is a complete valued field, a function on a neighborhood of a point $a\in K$ is called analytic if it is locally represented by a convergent power series $\sum _{n=0}^{\infty }c_{n}(x-a)^{n}$ with coefficients in K . In the non-Archimedean case, convergence is governed by an ultrametric absolute value, and the resulting theory differs significantly from both real and complex analysis.

For example, a power series over $\mathbb {Q} _{p}$ $\sum _{n=0}^{\infty }a_{n}x^{n}$ converges to an analytic function on the *p*-adic integers $\mathbb {Z} _{p}=\{x\in \mathbb {Q} _{p}\mid |x|_{p}\leq 1\}$ if and only if $|a_{n}|_{p}\to 0.$ Likewise, the series on a finite extension field K of a *p*-adic field converges on the ring of integers if and only if $|a_{n}|_{K}\to 0$ . The reason is the ultrametric criterion: if $|x|_{K}\leq 1$ , then $|a_{n}x^{n}|\leq |a_{n}|$ , and ultrametricity implies that any middle segment of the series satisfies $\left|\sum _{n=N}^{M}a_{n}x^{n}\right|_{K}\leq \max _{N\leq n\leq M}|a_{n}|.$

More generally, on the closed disc $a+\pi ^{m}{\mathcal {O}}_{K}=\{x:|x-a|\leq |\pi |^{m}\},$ a series $\sum _{n=0}^{\infty }b_{n}(x-a)^{n}$ converges on that disc if and only if $|b_{n}|\,|\pi |^{mn}\to 0.$ Here $\pi$ denotes the uniformizer of $K|\mathbb {Q} _{p}$ .

Over a non-Archimedean field the ring of analytic functions on a closed disc is thus related to the Tate algebra, the algebra of power series whose coefficients tend to zero sufficiently fast. This point of view is fundamental in rigid analytic geometry and other forms of non-Archimedean analytic geometry.
