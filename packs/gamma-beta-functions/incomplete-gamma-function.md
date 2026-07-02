---
title: "Incomplete gamma function"
source: https://en.wikipedia.org/wiki/Incomplete_gamma_function
domain: gamma-beta-functions
license: CC-BY-SA-4.0
tags: gamma function, beta function, digamma function, incomplete gamma function
fetched: 2026-07-02
---

# Incomplete gamma function

In mathematics, the **upper** and **lower incomplete gamma functions** are types of special functions which arise as solutions to various mathematical problems such as certain integrals.

Their respective names stem from their integral definitions, which are defined similarly to the gamma function but with different or "incomplete" integral limits. The gamma function is defined as an integral from zero to infinity. This contrasts with the lower incomplete gamma function, which is defined as an integral from zero to a variable upper limit. Similarly, the upper incomplete gamma function is defined as an integral from a variable lower limit to infinity.

## Definition

The upper incomplete gamma function is defined as: $\Gamma (s,x)=\int _{x}^{\infty }t^{s-1}\,e^{-t}\,dt,$ whereas the lower incomplete gamma function is defined as: $\gamma (s,x)=\int _{0}^{x}t^{s-1}\,e^{-t}\,dt.$ In both cases s is a complex parameter, such that the real part of s is positive.

## Properties

By integration by parts we find the recurrence relations $\Gamma (s+1,x)=s\Gamma (s,x)+x^{s}e^{-x}$ and $\gamma (s+1,x)=s\gamma (s,x)-x^{s}e^{-x}.$ Since the ordinary gamma function is defined as $\Gamma (s)=\int _{0}^{\infty }t^{s-1}\,e^{-t}\,dt$ we have $\Gamma (s)=\Gamma (s,0)=\lim _{x\to \infty }\gamma (s,x)$ and $\gamma (s,x)+\Gamma (s,x)=\Gamma (s).$

### Continuation to complex values

The lower incomplete gamma and the upper incomplete gamma function, as defined above for real positive s and x, can be developed into holomorphic functions, with respect both to x and s, defined for almost all combinations of complex x and s. Complex analysis shows how properties of the real incomplete gamma functions extend to their holomorphic counterparts.

#### Lower incomplete gamma function

##### Holomorphic extension

Repeated application of the recurrence relation for the **lower incomplete gamma** function leads to the power series expansion: $\gamma (s,x)=\sum _{k=0}^{\infty }{\frac {x^{s}e^{-x}x^{k}}{s(s+1)\cdots (s+k)}}=x^{s}\,\Gamma (s)\,e^{-x}\sum _{k=0}^{\infty }{\frac {x^{k}}{\Gamma (s+k+1)}}.$ Given the rapid growth in absolute value of Γ(*z* + *k*) when *k* → ∞, and the fact that the reciprocal of Γ(*z*) is an entire function, the coefficients in the rightmost sum are well-defined, and locally the sum converges uniformly for all complex s and x. By a theorem of Weierstrass, the limiting function, sometimes denoted as $\gamma ^{*}$ , $\gamma ^{*}(s,z):=e^{-z}\sum _{k=0}^{\infty }{\frac {z^{k}}{\Gamma (s+k+1)}}$ is entire with respect to both z (for fixed s) and s (for fixed z), and, thus, holomorphic on **C** × **C** by Hartogs' theorem. Hence, the following *decomposition* $\gamma (s,z)=z^{s}\,\Gamma (s)\,\gamma ^{*}(s,z),$ extends the real lower incomplete gamma function as a holomorphic function, both jointly and separately in z and s. It follows from the properties of $z^{s}$ and the Γ-function, that the first two factors capture the singularities of $\gamma (s,z)$ (at *z* = 0 or s a non-positive integer), whereas the last factor contributes to its zeros.

##### Multi-valuedness

The complex logarithm log *z* = log |*z*| + *i* arg *z* is determined up to a multiple of 2*πi* only, which renders it multi-valued. Functions involving the complex logarithm typically inherit this property. Among these are the complex power, and, since *z**s* appears in its decomposition, the γ-function, too.

The indeterminacy of multi-valued functions introduces complications, since it must be stated how to select a value. Strategies to handle this are:

- (the most general way) replace the domain **C** of multi-valued functions by a suitable manifold in **C** × **C** called Riemann surface. While this removes multi-valuedness, one has to know the theory behind it;
- restrict the domain such that a multi-valued function decomposes into separate single-valued branches, which can be handled individually.

The following set of rules can be used to interpret formulas in this section correctly. If not mentioned otherwise, the following is assumed:

###### Sectors

Sectors in **C** having their vertex at *z* = 0 often prove to be appropriate domains for complex expressions. A sector D consists of all complex z fulfilling *z* ≠ 0 and *α* − *δ* < arg *z* < *α* + *δ* with some α and 0 < *δ* ≤ *π*. Often, α can be arbitrarily chosen and is not specified then. If δ is not given, it is assumed to be π, and the sector is in fact the whole plane **C**, with the exception of a half-line originating at *z* = 0 and pointing into the direction of −*α*, usually serving as a branch cut. Note: In many applications and texts, α is silently taken to be 0, which centers the sector around the positive real axis.

###### Branches

In particular, a single-valued and holomorphic logarithm exists on any such sector D having its imaginary part bound to the range (*α* − *δ*, *α* + *δ*). Based on such a restricted logarithm, *z**s* and the incomplete gamma functions in turn collapse to single-valued, holomorphic functions on D (or **C**×*D*), called branches of their multi-valued counterparts on D. Adding a multiple of 2*π* to α yields a different set of correlated branches on the same set D. However, in any given context here, α is assumed fixed and all branches involved are associated to it. If |*α*| < *δ*, the branches are called principal, because they equal their real analogues on the positive real axis. Note: In many applications and texts, formulas hold only for principal branches.

###### Relation between branches

The values of different branches of both the complex power function and the lower incomplete gamma function can be derived from each other by multiplication of $e^{2\pi iks}$ , for k a suitable integer.

##### Behavior near branch point

The decomposition above further shows, that γ behaves near *z* = 0 asymptotically like: $\gamma (s,z)\asymp z^{s}\,\Gamma (s)\,\gamma ^{*}(s,0)=z^{s}\,\Gamma (s)/\Gamma (s+1)=z^{s}/s.$

For positive real x, y and s, *x**y*/y → 0, when (*x*, *y*) → (0, *s*). This seems to justify setting *γ*(*s*, 0) = 0 for real *s* > 0. However, matters are somewhat different in the complex realm. Only if (a) the real part of s is positive, and (b) values *u**v* are taken from just a finite set of branches, they are guaranteed to converge to zero as (*u*, *v*) → (0, *s*), and so does *γ*(*u*, *v*). On a single branch of *γ*(*b*) is naturally fulfilled, so **there** *γ*(*s*, 0) = 0 for s with positive real part is a continuous limit. Also note that such a continuation is by no means an analytic one.

##### Algebraic relations

All algebraic relations and differential equations observed by the real *γ*(*s*, *z*) hold for its holomorphic counterpart as well. This is a consequence of the identity theorem, stating that equations between holomorphic functions valid on a real interval, hold everywhere. In particular, the recurrence relation and *∂γ*(*s*, *z*)/*∂z* = *z**s*−1 *e*−*z* are preserved on corresponding branches.

##### Integral representation

The last relation tells us, that, for fixed s, γ is a primitive or antiderivative of the holomorphic function *z**s*−1 *e*−*z*. Consequently, for any complex *u*, *v* ≠ 0, $\int _{u}^{v}t^{s-1}\,e^{-t}\,dt=\gamma (s,v)-\gamma (s,u)$ holds, as long as the path of integration is entirely contained in the domain of a branch of the integrand. If, additionally, the real part of s is positive, then the limit *γ*(*s*, *u*) → 0 for *u* → 0 applies, finally arriving at the complex integral definition of *γ* $\gamma (s,z)=\int _{0}^{z}t^{s-1}\,e^{-t}\,dt,\,\Re (s)>0.$

Any path of integration containing 0 only at its beginning, otherwise restricted to the domain of a branch of the integrand, is valid here, for example, the straight line connecting 0 and z.

##### Limit for *z* → +∞

###### Real values

Given the integral representation of a principal branch of *γ*, the following equation holds for all positive real s, x: $\Gamma (s)=\int _{0}^{\infty }t^{s-1}\,e^{-t}\,dt=\lim _{x\to \infty }\gamma (s,x)$

###### *s* complex

This result extends to complex s. Assume first 1 ≤ Re(*s*) ≤ 2 and 1 < *a* < *b*. Then $\left|\gamma (s,b)-\gamma (s,a)\right|\leq \int _{a}^{b}\left|t^{s-1}\right|e^{-t}\,dt=\int _{a}^{b}t^{\Re s-1}e^{-t}\,dt\leq \int _{a}^{b}te^{-t}\,dt$ where $\left|z^{s}\right|=\left|z\right|^{\Re s}\,e^{-\Im s\arg z}$ has been used in the middle. Since the final integral becomes arbitrarily small if only a is large enough, *γ*(*s*, *x*) converges uniformly for *x* → ∞ on the strip 1 ≤ Re(s) ≤ 2 towards a holomorphic function, which must be Γ(s) because of the identity theorem. Taking the limit in the recurrence relation *γ*(*s*, *x*) = (*s* − 1) *γ*(*s* − 1, *x*) − *x**s* − 1 *e*−*x* and noting, that lim *x**n* *e*−*x* = 0 for *x* → ∞ and all n, shows, that *γ*(*s*, *x*) converges outside the strip, too, towards a function obeying the recurrence relation of the Γ-function. It follows $\Gamma (s)=\lim _{x\to \infty }\gamma (s,x)$ for all complex s not a non-positive integer, x real and *γ* principal.

###### Sectorwise convergence

Now let u be from the sector |arg *z*| < *δ* < *π*/2 with some fixed δ (*α* = 0), *γ* be the principal branch on this sector, and look at $\Gamma (s)-\gamma (s,u)=\Gamma (s)-\gamma (s,|u|)+\gamma (s,|u|)-\gamma (s,u).$

As shown above, the first difference can be made arbitrarily small, if |*u*| is sufficiently large. The second difference allows for following estimation: $\left|\gamma (s,|u|)-\gamma (s,u)\right|\leq \int _{u}^{|u|}\left|z^{s-1}e^{-z}\right|dz=\int _{u}^{|u|}\left|z\right|^{\Re s-1}\,e^{-\Im s\,\arg z}\,e^{-\Re z}\,dz,$ where we made use of the integral representation of *γ* and the formula about |*z**s*| above. If we integrate along the arc with radius *R* = |*u*| around 0 connecting u and |*u*|, then the last integral is $\leq R\left|\arg u\right|R^{\Re s-1}\,e^{\Im s\,|\arg u|}\,e^{-R\cos \arg u}\leq \delta \,R^{\Re s}\,e^{\Im s\,\delta }\,e^{-R\cos \delta }=M\,(R\,\cos \delta )^{\Re s}\,e^{-R\cos \delta }$ where *M* = *δ*(cos *δ*)−Re *s* *e*Im *sδ* is a constant independent of u or R. Again referring to the behavior of *x**n* *e*−*x* for large x, we see that the last expression approaches 0 as R increases towards ∞. In total we now have: $\Gamma (s)=\lim _{|z|\to \infty }\gamma (s,z),\quad \left|\arg z\right|<\pi /2-\epsilon ,$ if s is not a non-negative integer, 0 < *ε* < *π*/2 is arbitrarily small, but fixed, and *γ* denotes the principal branch on this domain.

##### Overview

$\gamma (s,z)$ is:

- entire in z for fixed, positive integer s;
- multi-valued holomorphic in z for fixed s not an integer, with a branch point at *z* = 0;
- on each branch meromorphic in s for fixed *z* ≠ 0, with simple poles at non-positive integers s.

#### Upper incomplete gamma function

As for the **upper incomplete gamma function**, a holomorphic extension, with respect to z or s, is given by $\Gamma (s,z)=\Gamma (s)-\gamma (s,z)$ at points (*s*, *z*), where the right hand side exists. Since $\gamma$ is multi-valued, the same holds for $\Gamma$ , but a restriction to principal values only yields the single-valued principal branch of $\Gamma$ .

When s is a non-positive integer in the above equation, neither part of the difference is defined, and a limiting process, here developed for *s* → 0, fills in the missing values. Complex analysis guarantees holomorphicity, because $\Gamma (s,z)$ proves to be bounded in a neighbourhood of that limit for a fixed z.

To determine the limit, the power series of $\gamma ^{*}$ at *z* = 0 is useful. When replacing $e^{-x}$ by its power series in the integral definition of $\gamma$ , one obtains (assume x,s positive reals for now): ${\begin{aligned}\gamma (s,x)&=\int _{0}^{x}t^{s-1}e^{-t}\,dt=\int _{0}^{x}\sum _{k=0}^{\infty }\left(-1\right)^{k}\,{\frac {t^{s+k-1}}{k!}}\,dt\\[1ex]&=\sum _{k=0}^{\infty }\left(-1\right)^{k}\,{\frac {x^{s+k}}{k!(s+k)}}=x^{s}\,\sum _{k=0}^{\infty }{\frac {(-x)^{k}}{k!(s+k)}}\end{aligned}}$ or $\gamma ^{*}(s,x)=\sum _{k=0}^{\infty }{\frac {(-x)^{k}}{k!\,\Gamma (s)(s+k)}},$ which, as a series representation of the entire $\gamma ^{*}$ function, converges for all complex x (and all complex s not a non-positive integer).

With its restriction to real values lifted, the series allows the expansion: ${\begin{aligned}\gamma (s,z)-{\frac {1}{s}}&=-{\frac {1}{s}}+z^{s}\,\sum _{k=0}^{\infty }{\frac {(-z)^{k}}{k!(s+k)}}\\[1ex]&={\frac {z^{s}-1}{s}}+z^{s}\,\sum _{k=1}^{\infty }{\frac {\left(-z\right)^{k}}{k!(s+k)}},&\Re (s)>-1,\,s\neq 0.\end{aligned}}$

When *s* → 0: ${\frac {z^{s}-1}{s}}\to \ln(z),\quad \Gamma (s)-{\frac {1}{s}}={\frac {1}{s}}-\gamma +O(s)-{\frac {1}{s}}\to -\gamma ,$ ( $\gamma$ is the Euler–Mascheroni constant here), hence, ${\begin{aligned}\Gamma (0,z)&=\lim _{s\to 0}\left(\Gamma (s)-{\tfrac {1}{s}}-\left(\gamma (s,z)-{\tfrac {1}{s}}\right)\right)\\&=-\gamma -\ln(z)-\sum _{k=1}^{\infty }{\frac {\left(-z\right)^{k}}{k\,(k!)}}\end{aligned}}$ is the limiting function to the upper incomplete gamma function as *s* → 0, also known as the exponential integral $E_{1}(z)$ .

By way of the recurrence relation, values of $\Gamma (-n,z)$ for positive integers n can be derived from this result, $\Gamma (-n,z)={\frac {1}{n!}}\left({\frac {e^{-z}}{z^{n}}}\sum _{k=0}^{n-1}(-1)^{k}(n-k-1)!\,z^{k}+\left(-1\right)^{n}\Gamma (0,z)\right)$ so the upper incomplete gamma function proves to exist and be holomorphic, with respect both to z and s, for all s and *z* ≠ 0.

$\Gamma (s,z)$ is:

- entire in z for fixed, positive integral s;
- multi-valued holomorphic in z for fixed s non zero and not a positive integer, with a branch point at *z* = 0;
- equal to $\Gamma (s)$ for s with positive real part and *z* = 0 (the limit when $(s_{i},z_{i})\to (s,0)$ ), but this is a continuous extension, not an analytic one (**does not** hold for real *s* < 0!);
- on each branch entire in s for fixed *z* ≠ 0.

### Special values

- $\Gamma (s+1,1)={\frac {\lfloor es!\rfloor }{e}}$ if s is a positive integer,
- $\Gamma (s,x)=(s-1)!\,e^{-x}\sum _{k=0}^{s-1}{\frac {x^{k}}{k!}}$ if s is a positive integer,
- $\Gamma (s,0)=\Gamma (s),\Re (s)>0$ ,
- $\Gamma (1,x)=e^{-x}$ ,
- $\gamma (1,x)=1-e^{-x}$ ,
- $\Gamma (0,x)=-\operatorname {Ei} (-x)$ for $x>0$ ,
- $\Gamma (s,x)=x^{s}\operatorname {E} _{1-s}(x)$ ,
- $\Gamma \left({\tfrac {1}{2}},x\right)={\sqrt {\pi }}\operatorname {erfc} \left({\sqrt {x}}\right)$ ,
- $\gamma \left({\tfrac {1}{2}},x\right)={\sqrt {\pi }}\operatorname {erf} \left({\sqrt {x}}\right)$ .

Here, $\operatorname {Ei}$ is the exponential integral, $\operatorname {E} _{n}$ is the generalized exponential integral, $\operatorname {erf}$ is the error function, and $\operatorname {erfc}$ is the complementary error function, $\operatorname {erfc} (x)=1-\operatorname {erf} (x)$ .

### Asymptotic behavior

- ${\frac {\gamma (s,x)}{x^{s}}}\to {\frac {1}{s}}$ as $x\to 0$ ,
- ${\frac {\Gamma (s,x)}{x^{s}}}\to -{\frac {1}{s}}$ as $x\to 0$ and $\Re (s)<0$ (for real *s*, the error of Γ(*s*, *x*) ~ −*x**s* / *s* is on the order of *O*(*x*min{*s* + 1, 0}) if *s* ≠ −1 and *O*(ln(*x*)) if *s* = −1),
- $\Gamma (s,x)\sim \Gamma (s)-\sum _{n=0}^{\infty }(-1)^{n}{\frac {x^{s+n}}{n!(s+n)}}$ as an asymptotic series where $x\to 0^{+}$ and $s\neq 0,-1,-2,\dots$ .
- $\Gamma (-N,x)\sim C_{N}+{\frac {(-1)^{N+1}}{N!}}\ln x-\sum _{n=0,n\neq N}^{\infty }(-1)^{n}{\frac {x^{n-N}}{n!(n-N)}}$ as an asymptotic series where $x\to 0^{+}$ and $N=1,2,\dots$ , where ${\textstyle C_{N}={\frac {(-1)^{N+1}}{N!}}\left(\gamma -\displaystyle \sum _{n=1}^{N}{\frac {1}{n}}\right)}$ , where $\gamma$ is the Euler-Mascheroni constant.
- $\gamma (s,x)\to \Gamma (s)$ as $x\to \infty$ .
- ${\frac {\Gamma (s,x)}{x^{s-1}e^{-x}}}\to 1$ as $x\to \infty$ ,
- if s ≥ 0 is real-valued, $\Gamma (s,z)\sim z^{s-1}e^{-z}\sum _{k=0}{\frac {\Gamma (s)}{\Gamma (s-k)}}z^{-k}$ as an asymptotic series where $|z|\to \infty$ and $\left|\arg z\right|<{\tfrac {3}{2}}\pi$ .

## Evaluation formulae

The lower gamma function can be evaluated using the power series expansion: $\gamma (s,z)=\sum _{k=0}^{\infty }{\frac {z^{s}e^{-z}z^{k}}{s(s+1)\dots (s+k)}}=z^{s}e^{-z}\sum _{k=0}^{\infty }{\dfrac {z^{k}}{s^{\overline {k+1}}}}$ where $s^{\overline {k+1}}$ is the Pochhammer symbol.

An alternative expansion is $\gamma (s,z)=\sum _{k=0}^{\infty }{\frac {(-1)^{k}}{k!}}{\frac {z^{s+k}}{s+k}}={\frac {z^{s}}{s}}M(s,s+1,-z),$ where *M* is Kummer's confluent hypergeometric function.

### Connection with Kummer's confluent hypergeometric function

When the real part of z is positive, $\gamma (s,z)=s^{-1}z^{s}e^{-z}M(1,s+1,z)$ where $M(1,s+1,z)=1+{\frac {z}{(s+1)}}+{\frac {z^{2}}{(s+1)(s+2)}}+{\frac {z^{3}}{(s+1)(s+2)(s+3)}}+\cdots$ has an infinite radius of convergence.

Again with confluent hypergeometric functions and employing Kummer's identity, ${\begin{aligned}\Gamma (s,z)&=e^{-z}U(1{-}s,1{-}s,z)={\frac {z^{s}e^{-z}}{\Gamma (1-s)}}\int _{0}^{\infty }{\frac {e^{-u}}{u^{s}(z+u)}}du\\&=e^{-z}z^{s}U(1,1{+}s,z)=e^{-z}\int _{0}^{\infty }e^{-u}(z+u)^{s-1}du\\&=e^{-z}z^{s}\int _{0}^{\infty }e^{-zu}(1+u)^{s-1}du.\end{aligned}}$

For the actual computation of numerical values, Gauss's continued fraction provides a useful expansion: $\gamma (s,z)={\cfrac {z^{s}e^{-z}}{s-{\cfrac {sz}{s+1+{\cfrac {z}{s+2-{\cfrac {(s+1)z}{s+3+{\cfrac {2z}{s+4-{\cfrac {(s+2)z}{s+5+{\cfrac {3z}{s+6-\ddots }}}}}}}}}}}}}}.$

This continued fraction converges for all complex z, provided only that s is not a negative integer.

The upper gamma function has the continued fraction $\Gamma (s,z)={\cfrac {z^{s}e^{-z}}{z+{\cfrac {1-s}{1+{\cfrac {1}{z+{\cfrac {2-s}{1+{\cfrac {2}{z+{\cfrac {3-s}{1+\ddots }}}}}}}}}}}}$ and $\Gamma (s,z)={\cfrac {z^{s}e^{-z}}{1+z-s+{\cfrac {s-1}{3+z-s+{\cfrac {2(s-2)}{5+z-s+{\cfrac {3(s-3)}{7+z-s+{\cfrac {4(s-4)}{9+z-s+\ddots }}}}}}}}}}$

### Multiplication theorem

The following multiplication theorem holds true: ${\begin{aligned}\Gamma (s,z)&={\frac {1}{t^{s}}}\sum _{i=0}^{\infty }{\frac {\left(1-{\frac {1}{t}}\right)^{i}}{i!}}\Gamma (s+i,tz)\\&=\Gamma (s,tz)-(tz)^{s}e^{-tz}\sum _{i=1}^{\infty }{\frac {\left({\frac {1}{t}}-1\right)^{i}}{i}}L_{i-1}^{(s-i)}(tz).\end{aligned}}$

### Software implementation

The incomplete gamma functions are available in various of the computer algebra systems.

Even if unavailable directly, however, incomplete function values can be calculated using functions commonly included in spreadsheets (and computer algebra packages). In Excel, for example, these can be calculated using the gamma function combined with the gamma distribution function.

- The lower incomplete function: $\gamma (s,x)$ `= EXP(GAMMALN(s))*GAMMA.DIST(x,s,1,TRUE)`.
- The upper incomplete function: $\Gamma (s,x)$ `= EXP(GAMMALN(s))*(1-GAMMA.DIST(x,s,1,TRUE))`.

These follow from the definition of the gamma distribution's cumulative distribution function.

In Python, the Scipy library provides implementations of incomplete gamma functions under `scipy.special`, however, it does not support negative values for the first argument. The function `gammainc` from the mpmath library supports all complex arguments.

## Regularized gamma functions and Poisson random variables

Two related functions are the regularized gamma functions: ${\begin{aligned}P(s,x)&={\frac {\gamma (s,x)}{\Gamma (s)}},\\[1ex]Q(s,x)&={\frac {\Gamma (s,x)}{\Gamma (s)}}=1-P(s,x).\end{aligned}}$ $P(s,x)$ is the cumulative distribution function for gamma random variables with shape parameter s and scale parameter 1.

When s is an integer, $Q(s+1,\lambda )$ is the cumulative distribution function for Poisson random variables: If X is a $\mathrm {Poi} (\lambda )$ random variable then $\Pr(X\leq s)=\sum _{i\leq s}e^{-\lambda }{\frac {\lambda ^{i}}{i!}}={\frac {\Gamma (s+1,\lambda )}{\Gamma (s+1)}}=Q(s+1,\lambda ).$

This formula can be derived by repeated integration by parts.

$P(s,x)$ and $Q(s,x)$ are implemented as `gammainc` and `gammaincc` in scipy.

## Partial derivatives

Using the integral representation above, the derivative of the upper incomplete gamma function $\Gamma (s,x)$ with respect to x is ${\frac {\partial \Gamma (s,x)}{\partial x}}=-x^{s-1}e^{-x}$ The derivative with respect to its first argument s is given by ${\frac {\partial \Gamma (s,x)}{\partial s}}=\ln x\Gamma (s,x)+x\,T(3,s,x)$ and the second derivative by ${\frac {\partial ^{2}\Gamma (s,x)}{\partial s^{2}}}=\ln ^{2}x\Gamma (s,x)+2x\left[\ln x\,T(3,s,x)+T(4,s,x)\right]$ where the function $T(m,s,x)$ is a special case of the Meijer G-function $T(m,s,x)=G_{m-1,\,m}^{\,m,\,0}\!\left(\left.{\begin{matrix}0,0,\dots ,0\\s-1,-1,\dots ,-1\end{matrix}}\;\right|\,x\right).$ This particular special case has internal *closure* properties of its own because it can be used to express *all* successive derivatives. In general, ${\frac {\partial ^{m}\Gamma (s,x)}{\partial s^{m}}}=\ln ^{m}x\Gamma (s,x)+mx\,\sum _{n=0}^{m-1}P_{n}^{m-1}\ln ^{m-n-1}x\,T(3+n,s,x)$ where $P_{j}^{n}$ is the permutation defined by the Pochhammer symbol: $P_{j}^{n}={\binom {n}{j}}j!={\frac {n!}{(n-j)!}}.$ All such derivatives can be generated in succession from: ${\frac {\partial T(m,s,x)}{\partial s}}=\ln x~T(m,s,x)+(m-1)T(m+1,s,x)$ and ${\frac {\partial T(m,s,x)}{\partial x}}=-{\frac {T(m-1,s,x)+T(m,s,x)}{x}}$ This function $T(m,s,x)$ can be computed from its series representation valid for $|z|<1$ , $T(m,s,z)=-{\frac {\left(-1\right)^{m-1}}{(m-2)!}}\left.{\frac {d^{m-2}}{dt^{m-2}}}\left[\Gamma (s-t)z^{t-1}\right]\right|_{t=0}+\sum _{n=0}^{\infty }{\frac {\left(-1\right)^{n}z^{s-1+n}}{n!\left(-s-n\right)^{m-1}}}$ with the understanding that s is not a negative integer or zero. In such a case, one must use a limit. Results for $|z|\geq 1$ can be obtained by analytic continuation. Some special cases of this function can be simplified. For example, $T(2,s,x)=\Gamma (s,x)/x$ , $x\,T(3,1,x)=\mathrm {E} _{1}(x)$ , where $\mathrm {E} _{1}(x)$ is the exponential integral. These derivatives and the function $T(m,s,x)$ provide exact solutions to a number of integrals by repeated differentiation of the integral definition of the upper incomplete gamma function. For example, $\int _{x}^{\infty }{\frac {t^{s-1}\ln ^{m}t}{e^{t}}}dt={\frac {\partial ^{m}}{\partial s^{m}}}\int _{x}^{\infty }{\frac {t^{s-1}}{e^{t}}}dt={\frac {\partial ^{m}}{\partial s^{m}}}\Gamma (s,x)$ This formula can be further *inflated* or generalized to a huge class of Laplace transforms and Mellin transforms. When combined with a computer algebra system, the exploitation of special functions provides a powerful method for solving definite integrals, in particular those encountered by practical engineering applications (see Symbolic integration for more details).

## Indefinite and definite integrals

The following indefinite integrals are readily obtained using integration by parts (with the constant of integration omitted in both cases): ${\begin{aligned}\int x^{b-1}\gamma (s,x)\,dx&={\frac {1}{b}}\left(x^{b}\gamma (s,x)-\gamma (s+b,x)\right),\\[1ex]\int x^{b-1}\Gamma (s,x)\,dx&={\frac {1}{b}}\left(x^{b}\Gamma (s,x)-\Gamma (s+b,x)\right).\end{aligned}}$ The lower and the upper incomplete gamma function are connected via the Fourier transform: $\int _{-\infty }^{\infty }{\frac {\gamma \left({\frac {s}{2}},z^{2}\pi \right)}{(z^{2}\pi )^{\frac {s}{2}}}}e^{-2\pi ikz}dz={\frac {\Gamma \left({\frac {1-s}{2}},k^{2}\pi \right)}{(k^{2}\pi )^{\frac {1-s}{2}}}}.$ This follows, for example, by suitable specialization of (Gradshteyn et al. 2015, §7.642).
