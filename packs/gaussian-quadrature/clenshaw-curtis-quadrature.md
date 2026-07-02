---
title: "Clenshaw–Curtis quadrature"
source: https://en.wikipedia.org/wiki/Clenshaw%E2%80%93Curtis_quadrature
domain: gaussian-quadrature
license: CC-BY-SA-4.0
tags: gaussian quadrature, gauss-legendre quadrature, gauss-kronrod quadrature, clenshaw-curtis quadrature
fetched: 2026-07-02
---

# Clenshaw–Curtis quadrature

**Clenshaw–Curtis quadrature** and **Fejér quadrature** are methods for numerical integration, or "quadrature", that are based on an expansion of the integrand in terms of Chebyshev polynomials. Equivalently, they employ a change of variables $x=\cos \theta$ and use a discrete cosine transform (DCT) approximation for the cosine series. Besides having fast-converging accuracy comparable to Gaussian quadrature rules, Clenshaw–Curtis quadrature naturally leads to nested quadrature rules (where different accuracy orders share points), which is important for both adaptive quadrature and multidimensional quadrature (cubature).

Briefly, the function $f(x)$ to be integrated is evaluated at the N extrema or roots of a Chebyshev polynomial and these values are used to construct a polynomial approximation for the function. This polynomial is then integrated exactly. In practice, the integration weights for the value of the function at each node are precomputed, and this computation can be performed in $O(N\log N)$ time by means of fast Fourier transform-related algorithms for the DCT.

## General method

A simple way of understanding the algorithm is to realize that Clenshaw–Curtis quadrature (proposed by those authors in 1960) amounts to integrating via a change of variable *x* = cos(*θ*). The algorithm is normally expressed for integration of a function *f*(*x*) over the interval [−1,1] (any other interval can be obtained by appropriate rescaling). For this integral, we can write:

$\int _{-1}^{1}f(x)\,dx=\int _{0}^{\pi }f(\cos \theta )\sin(\theta )\,d\theta .$

That is, we have transformed the problem from integrating $f(x)$ to one of integrating $f(\cos \theta )\sin \theta$ . This can be performed if we know the cosine series for $f(\cos \theta )$ :

$f(\cos \theta )={\frac {a_{0}}{2}}+\sum _{k=1}^{\infty }a_{k}\cos(k\theta )$

in which case the integral becomes:

$\int _{0}^{\pi }f(\cos \theta )\sin(\theta )\,d\theta =a_{0}+\sum _{k=1}^{\infty }{\frac {2a_{2k}}{1-(2k)^{2}}}.$

Of course, in order to calculate the cosine series coefficients

$a_{k}={\frac {2}{\pi }}\int _{0}^{\pi }f(\cos \theta )\cos(k\theta )\,d\theta ,\quad k=0,1,2,\dots ,$

one must again perform a numeric integration, so at first this may not seem to have simplified the problem. Unlike computation of arbitrary integrals, however, Fourier-series integrations for periodic functions (like $f(\cos \theta )$ , by construction), up to the Nyquist frequency $k=N$ , are accurately computed by the $N+1$ equally spaced and equally weighted points $\theta _{n}=n\pi /N$ for $n=0,\ldots ,N$ (except the endpoints are weighted by 1/2, to avoid double-counting, equivalent to the trapezoidal rule or the Euler–Maclaurin formula). That is, we approximate the cosine-series integral by the type-I discrete cosine transform (DCT):

$a_{k}\approx {\frac {2}{N}}\left[{\frac {f(1)}{2}}+{\frac {f(-1)}{2}}(-1)^{k}+\sum _{n=1}^{N-1}f(\cos[n\pi /N])\cos(nk\pi /N)\right]$

for $k=0,\ldots ,N$ and then use the formula above for the integral in terms of these $a_{k}$ . Because only $a_{2k}$ is needed, the formula simplifies further into a type-I DCT of order *N*/2, assuming *N* is an even number:

$a_{2k}\approx {\frac {2}{N}}\left[{\frac {f(1)+f(-1)}{2}}+f(0)(-1)^{k}+\sum _{n=1}^{N/2-1}\left\{f(\cos[n\pi /N])+f(-\cos[n\pi /N])\right\}\cos \left({\frac {nk\pi }{N/2}}\right)\right]$

From this formula, it is clear that the Clenshaw–Curtis quadrature rule is symmetric, in that it weights *f*(*x*) and *f*(−*x*) equally.

Because of aliasing, one only computes the coefficients $a_{2k}$ up to *k* = *N*/2, since discrete sampling of the function makes the frequency of 2*k* indistinguishable from that of *N*–2*k*. Equivalently, the $a_{2k}$ are the amplitudes of the unique bandlimited trigonometric interpolation polynomial passing through the *N*+1 points where *f*(cos *θ*) is evaluated, and we approximate the integral by the integral of this interpolation polynomial. There is some subtlety in how one treats the $a_{N}$ coefficient in the integral, however—to avoid double-counting with its alias it is included with weight 1/2 in the final approximate integral (as can also be seen by examining the interpolating polynomial):

$\int _{0}^{\pi }f(\cos \theta )\sin(\theta )\,d\theta \approx a_{0}+\sum _{k=1}^{N/2-1}{\frac {2a_{2k}}{1-(2k)^{2}}}+{\frac {a_{N}}{1-N^{2}}}.$

## Connection to Chebyshev polynomials

The reason that this is connected to the Chebyshev polynomials $T_{k}(x)$ is that, by definition, $T_{k}(\cos \theta )=\cos(k\theta )$ , and so the cosine series above is really an approximation of $f(x)$ by Chebyshev polynomials:

$f(x)={\frac {a_{0}}{2}}T_{0}(x)+\sum _{k=1}^{\infty }a_{k}T_{k}(x),$

and thus we are "really" integrating $f(x)$ by integrating its approximate expansion in terms of Chebyshev polynomials. The evaluation points $x_{n}=\cos(n\pi /N)$ correspond to the extrema of the Chebyshev polynomial $T_{N}(x)$ .

The fact that such Chebyshev approximation is just a cosine series under a change of variables is responsible for the rapid convergence of the approximation as more terms $T_{k}(x)$ are included. A cosine series converges very rapidly for functions that are even, periodic, and sufficiently smooth. This is true here, since $f(\cos \theta )$ is even and periodic in $\theta$ by construction, and is *k*-times differentiable everywhere if $f(x)$ is *k*-times differentiable on $[-1,1]$ . (In contrast, directly applying a cosine-series expansion to $f(x)$ instead of $f(\cos \theta )$ will usually *not* converge rapidly because the slope of the even-periodic extension would generally be discontinuous.)

## Fejér quadrature

Fejér proposed two quadrature rules very similar to Clenshaw–Curtis quadrature, but much earlier (in 1933).

Of these two, Fejér's "second" quadrature rule is nearly identical to Clenshaw–Curtis. The only difference is that the endpoints $f(-1)$ and $f(1)$ are set to zero. That is, Fejér only used the *interior* extrema of the Chebyshev polynomials, i.e. the true stationary points.

Fejér's "first" quadrature rule evaluates the $a_{k}$ by evaluating $f(\cos \theta )$ at a different set of equally spaced points, halfway between the extrema: $\theta _{n}={\bigl (}n+{\tfrac {1}{2}}{\bigr )}\pi {\big /}N$ for $0\leq n<N$ . These are the *roots* of $T_{N}(\cos \theta )$ , and are known as the Chebyshev nodes. (These equally spaced midpoints are the only other choice of quadrature points that preserve both the even symmetry of the cosine transform and the translational symmetry of the periodic Fourier series.) This leads to a formula:

$a_{k}\approx {\frac {2}{N}}\sum _{n=0}^{N-1}f{\left(\cos {\frac {{\bigl (}n+{\tfrac {1}{2}}{\bigr )}\pi }{N}}\right)\cos {\frac {{\bigl (}n+{\tfrac {1}{2}}{\bigr )}k\pi }{N}}}$

which is precisely the type-II DCT. However, Fejér's first quadrature rule is not nested: the evaluation points for 2*N* do not coincide with any of the evaluation points for *N*, unlike Clenshaw–Curtis quadrature or Fejér's second rule.

Despite the fact that Fejér discovered these techniques before Clenshaw and Curtis, the name "Clenshaw–Curtis quadrature" has become standard.

## Comparison to Gaussian quadrature

The classic method of Gaussian quadrature evaluates the integrand at $N+1$ points and is constructed to *exactly* integrate polynomials up to degree $2N+1$ . In contrast, Clenshaw–Curtis quadrature, above, evaluates the integrand at $N+1$ points and exactly integrates polynomials only up to degree $N+1$ (assuming N is an even number). It may seem, therefore, that Clenshaw–Curtis is intrinsically worse than Gaussian quadrature, but in reality this does not seem to be the case.

In practice, several authors have observed that Clenshaw–Curtis can have accuracy comparable to that of Gaussian quadrature for the same number of points. This is possible because most numeric integrands are not polynomials (especially since polynomials can be integrated analytically), and approximation of many functions in terms of Chebyshev polynomials converges rapidly (see Chebyshev approximation). In fact, recent theoretical results argue that both Gaussian and Clenshaw–Curtis quadrature have error bounded by $O([2N]^{-k}/k)$ for a *k*-times differentiable integrand.

One often cited advantage of Clenshaw–Curtis quadrature is that the quadrature weights can be evaluated in $O(N\log N)$ time by fast Fourier transform algorithms (or their analogues for the DCT), whereas most algorithms for Gaussian quadrature weights required $O(N^{2})$ time to compute. However, recent algorithms have attained $O(N)$ complexity for Gauss–Legendre quadrature. As a practical matter, high-order numeric integration is rarely performed by simply evaluating a quadrature formula for very large N . Instead, one usually employs an adaptive quadrature scheme that first evaluates the integral to low order, and then successively refines the accuracy by increasing the number of sample points, possibly only in regions where the integral is inaccurate. To evaluate the accuracy of the quadrature, one compares the answer with that of a quadrature rule of even lower order. Ideally, this lower-order quadrature rule evaluates the integrand at a *subset* of the original *N* points, to minimize the integrand evaluations. This is called a nested quadrature rule, and here Clenshaw–Curtis has the advantage that the rule for order *N* uses a subset of the points from order 2*N*. In contrast, Gaussian quadrature rules are not naturally nested, and so one must employ Gauss–Kronrod quadrature formulas or similar methods. Nested rules are also important for sparse grids in multidimensional quadrature, and Clenshaw–Curtis quadrature is a popular method in this context.

## Integration with weight functions

More generally, one can pose the problem of integrating an arbitrary $f(x)$ against a fixed *weight function* $w(x)$ that is known ahead of time:

$\int _{-1}^{1}f(x)w(x)\,dx=\int _{0}^{\pi }f(\cos \theta )w(\cos \theta )\sin(\theta )\,d\theta .$

The most common case is $w(x)=1$ , as above, but in certain applications a different weight function is desirable. The basic reason is that, since $w(x)$ can be taken into account *a priori*, the integration error can be made to depend only on the accuracy in approximating $f(x)$ , regardless of how badly behaved the weight function might be.

Clenshaw–Curtis quadrature can be generalized to this case as follows. As before, it works by finding the cosine-series expansion of $f(\cos \theta )$ via a DCT, and then integrating each term in the cosine series. Now, however, these integrals are of the form

$W_{k}=\int _{0}^{\pi }w(\cos \theta )\cos(k\theta )\sin(\theta )\,d\theta .$

For most $w(x)$ , this integral cannot be computed analytically, unlike before. Since the same weight function is generally used for many integrands $f(x)$ , however, one can afford to compute these $W_{k}$ numerically to high accuracy beforehand. Moreover, since $w(x)$ is generally specified analytically, one can sometimes employ specialized methods to compute $W_{k}$ .

For example, special methods have been developed to apply Clenshaw–Curtis quadrature to integrands of the form $f(x)w(x)$ with a weight function $w(x)$ that is highly oscillatory, e.g. a sinusoid or Bessel function (see, e.g., Evans & Webster, 1999). This is useful for high-accuracy Fourier series and Fourier–Bessel series computation, where simple $w(x)=1$ quadrature methods are problematic because of the high accuracy required to resolve the contribution of rapid oscillations. Here, the rapid-oscillation part of the integrand is taken into account via specialized methods for $W_{k}$ , whereas the unknown function $f(x)$ is usually better behaved.

Another case where weight functions are especially useful is if the integrand is unknown but has a known singularity of some form, e.g. a known discontinuity or integrable divergence (such as 1/√*x*) at some point. In this case the singularity can be pulled into the weight function $w(x)$ and its analytical properties can be used to compute $W_{k}$ accurately beforehand.

Note that Gaussian quadrature can also be adapted for various weight functions, but the technique is somewhat different. In Clenshaw–Curtis quadrature, the integrand is always evaluated at the same set of points regardless of $w(x)$ , corresponding to the extrema or roots of a Chebyshev polynomial. In Gaussian quadrature, different weight functions lead to different orthogonal polynomials, and thus different roots where the integrand is evaluated.

## Integration on infinite and semi-infinite intervals

It is also possible to use Clenshaw–Curtis quadrature to compute integrals of the form ${\textstyle \int _{0}^{\infty }f(x)\,dx}$ and ${\textstyle \int _{-\infty }^{\infty }f(x)\,dx}$ , using a coordinate-remapping technique. High accuracy, even exponential convergence for smooth integrands, can be retained as long as $f(x)$ decays sufficiently quickly as |*x*| approaches infinity.

One possibility is to use a generic coordinate transformation such as *x* = *t*/(1−*t*2)

$\int _{-\infty }^{\infty }f(x)\,dx=\int _{-1}^{1}f{\left({\frac {t}{1-t^{2}}}\right)}{\frac {1+t^{2}}{(1-t^{2})^{2}}}\,dt,$

to transform an infinite or semi-infinite interval into a finite one, as described in Numerical integration. There are also additional techniques that have been developed specifically for Clenshaw–Curtis quadrature.

For example, one can use the coordinate remapping $x=L\cot ^{2}(\theta /2)$ , where *L* is a user-specified constant (one could simply use *L*=1; an optimal choice of *L* can speed convergence, but is problem-dependent), to transform the semi-infinite integral into:

$\int _{0}^{\infty }f(x)\,dx=2L\int _{0}^{\pi }{\frac {f[L\cot ^{2}(\theta /2)]}{[1-\cos(\theta )]^{2}}}\sin(\theta )\,d\theta .$

The factor multiplying sin(*θ*), *f*(...)/(...)2, can then be expanded in a cosine series (approximately, using the discrete cosine transform) and integrated term-by-term, exactly as was done for *f*(cos *θ*) above. To eliminate the singularity at *θ*=0 in this integrand, one merely requires that *f*(*x*) go to zero sufficiently fast as *x* approaches infinity, and in particular *f*(*x*) must decay at least as fast as 1/*x*3/2.

For a doubly infinite interval of integration, one can use the coordinate remapping $x=L\cot(\theta )$ (where *L* is a user-specified constant as above) to transform the integral into:

$\int _{-\infty }^{\infty }f(x)\,dx=L\int _{0}^{\pi }{\frac {f[L\cot(\theta )]}{\sin ^{2}(\theta )}}\,d\theta \approx {\frac {L\pi }{N}}\sum _{n=1}^{N-1}{\frac {f[L\cot(n\pi /N)]}{\sin ^{2}(n\pi /N)}}.$

In this case, we have used the fact that the remapped integrand *f*(*L* cot *θ*)/sin2(*θ*) is already periodic and so can be directly integrated with high (even exponential) accuracy using the trapezoidal rule (assuming *f* is sufficiently smooth and rapidly decaying); there is no need to compute the cosine series as an intermediate step. Note that the quadrature rule does not include the endpoints, where we have assumed that the integrand goes to zero. The formula above requires that *f*(*x*) decay faster than 1/*x*2 as *x* goes to ±∞. (If *f* decays exactly as 1/*x*2, then the integrand goes to a finite value at the endpoints and these limits must be included as endpoint terms in the trapezoidal rule.). However, if *f* decays only polynomially quickly, then it may be necessary to use a further step of Clenshaw–Curtis quadrature to obtain exponential accuracy of the remapped integral instead of the trapezoidal rule, depending on more details of the limiting properties of *f*: the problem is that, although *f*(*L* cot*θ*)/sin2(*θ*) is indeed periodic with period π, it is not necessarily smooth at the endpoints if all the derivatives do not vanish there [e.g. the function *f*(*x*) = tanh(*x*3)/*x*3 decays as 1/*x*3 but has a jump discontinuity in the slope of the remapped function at θ=0 and π].

Another coordinate-remapping approach was suggested for integrals of the form ${\textstyle \int _{0}^{\infty }e^{-x}g(x)\,dx}$ , in which case one can use the transformation $x=-\ln[(1+\cos \theta )/2]$ to transform the integral into the form ${\textstyle \int _{0}^{\pi }f(\cos \theta )\sin \theta \,d\theta }$ where $f(u)=g(-\ln[(1+u)/2])/2$ , at which point one can proceed identically to Clenshaw–Curtis quadrature for *f* as above. Because of the endpoint singularities in this coordinate remapping, however, one uses Fejér's first quadrature rule [which does not evaluate *f*(−1)] unless *g*(∞) is finite.

## Precomputing the quadrature weights

In practice, it is inconvenient to perform a DCT of the sampled function values ⁠ $f(\cos \theta )$ ⁠ for each new integrand. Instead, one normally precomputes quadrature weights $w_{n}$ (for ⁠ n ⁠ from ⁠ 0 ⁠ to ⁠ ${\tfrac {1}{2}}N$ ⁠, assuming that ⁠ N ⁠ is even) so that

$\int _{-1}^{1}f(x)\,dx\approx \sum _{n=0}^{N/2}w_{n}{{\biggl (}f{\left(\cos {\frac {n\pi }{N}}\right)}+f{\left(-\cos {\frac {n\pi }{N}}\right)}{\biggr )}}.$

These weights $w_{n}$ are also computed by a DCT, as is easily seen by expressing the computation in terms of matrix algebra. In particular, we computed the cosine series coefficients $a_{2k}$ via an expression of the form:

$c={\begin{pmatrix}a_{0}\\a_{2}\\a_{4}\\\vdots \\a_{N}\end{pmatrix}}=D{\begin{pmatrix}y_{0}\\y_{1}\\y_{2}\\\vdots \\y_{N/2}\end{pmatrix}}=Dy,$ where *D* is the matrix form of the ⁠ ${\bigl (}{\tfrac {1}{2}}N+1{\bigr )}$ ⁠-point type-I DCT from above, with entries (for zero-based indices):

$D_{kn}={\frac {2}{N}}\cos \left({\frac {nk\pi }{{\tfrac {1}{2}}N}}\right)\times {\begin{cases}{\tfrac {1}{2}}&n=0,\,{\tfrac {1}{2}}N\\[5mu]1&\mathrm {otherwise} ,\end{cases}}$

and $y_{n}$ is

$y_{n}=f{\left(\cos {\frac {n\pi }{N}}\right)}+f{\left(-\cos {\frac {n\pi }{N}}\right)}.$

As discussed above, because of aliasing, there is no point in computing coefficients beyond $a_{N}$ , so *D* is an ${\bigl (}{\tfrac {1}{2}}N+1{\bigr )}\times {\bigl (}{\tfrac {1}{2}}N+1{\bigr )}$ matrix. In terms of these coefficients ⁠ c ⁠, the integral is approximately:

$\int _{-1}^{1}f(x)\,dx\approx a_{0}+\sum _{k=1}^{N/2-1}{\frac {2a_{2k}}{1-(2k)^{2}}}+{\frac {a_{N}}{1-N^{2}}}=d^{T}c,$

from above, where ⁠ c ⁠ is the vector of coefficients $a_{2k}$ above and ⁠ d ⁠ is the vector of integrals for each Fourier coefficient:

$d={\begin{pmatrix}1\\2/(1-4)\\2/(1-16)\\\vdots \\2/(1-[N-2]^{2})\\1/(1-N^{2})\end{pmatrix}}.$

(These weight factors are altered if one changes the DCT matrix ⁠ D ⁠ to use a different normalization convention. For example, it is common to define the type-I DCT with additional factors of ⁠ 2 ⁠ or ⁠ ${\sqrt {2}}$ ⁠ factors in the first and last rows or columns, which leads to corresponding alterations in the ⁠ d ⁠ entries.) The $d^{T}c$ summation can be re-arranged to:

$\int _{-1}^{1}f(x)\,dx\approx d^{T}c=d^{T}Dy=(D^{T}d)^{T}y=w^{T}y$

where *w* is the vector of the desired weights $w_{n}$ above, with: $w=D^{T}d.$

Since the transposed matrix $\textstyle D^{T}$ is also a DCT (e.g., the transpose of a type-I DCT is a type-I DCT, possibly with a slightly different normalization depending on the conventions that are employed), the quadrature weights *w* can be precomputed in ⁠ $O(N\log N)$ ⁠ time for a given ⁠ N ⁠ using fast DCT algorithms.

The weights $w_{n}$ are positive and their sum is equal to one.
