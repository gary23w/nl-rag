---
title: "Trapezoidal rule"
source: https://en.wikipedia.org/wiki/Trapezoidal_rule
domain: numerical-quadrature
license: CC-BY-SA-4.0
tags: numerical integration, simpson's rule, romberg method, adaptive quadrature
fetched: 2026-07-02
---

# Trapezoidal rule

In calculus, the **trapezoidal rule** (informally **trapezoid rule**; or in British English **trapezium rule**) is a technique for numerical integration, i.e. approximating the definite integral: $\int _{a}^{b}f(x)\,dx.$

The trapezoidal rule works by approximating the region under the graph of the function $f(x)$ as a trapezoid and calculating its area. This is easily calculated by noting that the area of the region is made up of a rectangle with width $(b-a)$ and height $f(a)$ , and a triangle of width $(b-a)$ and height $f(b)-f(a)$ .

Therefore, ${\begin{aligned}\int _{a}^{b}f(x)\,dx&\approx \underbrace {(b-a)\cdot f(a)} _{\text{Area of rectangle}}+\underbrace {{\tfrac {1}{2}}(b-a)\cdot [f(b)-f(a)]} _{\text{Area of triangle}}\\&=(b-a)\cdot \left(f(a)+{\tfrac {1}{2}}f(b)-{\tfrac {1}{2}}f(a)\right)\\&=(b-a)\cdot \left({\tfrac {1}{2}}f(a)+{\tfrac {1}{2}}f(b)\right)\\&={\frac {1}{2}}(b-a)[f(a)+f(b)].\end{aligned}}$

The rule can also be derived by replacing the integrand with the equation of the line joining points ${\big (}a,f(a){\big )}$ and ${\big (}b,f(b){\big )}$ , which using the two point form of the equation of a line, is $y=(x-a)\,{\frac {f(b)-f(a)}{b-a}}+f(a).$

Therefore, ${\begin{aligned}\int _{a}^{b}f(x)\,dx&\approx \int _{a}^{b}(x-a)\,{\frac {f(b)-f(a)}{b-a}}+f(a)\,dx\\&=\left[{\frac {1}{2}}(x-a)^{2}\,{\frac {f(b)-f(a)}{b-a}}+xf(a)\right]_{x=a}^{x=b}\\&=\left[{\frac {1}{2}}(b-a)^{2}\,{\frac {f(b)-f(a)}{b-a}}+bf(a)\right]-af(a)\\&={\frac {1}{2}}(b-a)[f(b)-f(a)]+(b-a)f(a)\\&={\frac {1}{2}}(b-a)[f(a)+f(b)],\end{aligned}}$ as before.

The integral can be even better approximated by partitioning the integration interval, applying the trapezoidal rule to each subinterval and summing the results. In practice, this "chained" (or "composite") trapezoidal rule is usually what is meant by "integrating with the trapezoidal rule". Let $\{x_{k}\}$ be a partition of $[a,b]$ such that $a=x_{0}<x_{1}<\cdots <x_{N-1}<x_{N}=b,$ and $\Delta x_{k}$ be the length of the k -th subinterval (that is, $\Delta x_{k}=x_{k}-x_{k-1}$ ), then $\int _{a}^{b}f(x)\,dx\approx \sum _{k=1}^{N}{\frac {f(x_{k-1})+f(x_{k})}{2}}\Delta x_{k}.$ The trapezoidal rule may be viewed as the result obtained by averaging the left and right Riemann sums and is sometimes defined this way.

The approximation becomes more accurate as the resolution of the partition increases (that is, for larger N , all $\Delta x_{k}$ decrease).

When the partition has a regular spacing, as is often the case, that is, when all the $\Delta x_{k}$ have the same value $\Delta x,$ the formula can be simplified for calculation efficiency by factoring $\Delta x$ out: $\int _{a}^{b}f(x)\,dx\approx \Delta x\left({\frac {f(x_{0})+f(x_{N})}{2}}+\sum _{k=1}^{N-1}f(x_{k})\right).$

As discussed below, it is also possible to place error bounds on the accuracy of the value of a definite integral estimated using a trapezoidal rule.

## History

Evidence discovered in Babylonian cuniform tablets circa 200 BCE predicting the motion of Jupiter along the ecliptic suggests that the trapezoid rule was in use for numerical approximation long before calculus itself was invented.

## Numerical implementation

### Non-uniform grid

When the grid spacing is non-uniform, one can use the formula $\int _{a}^{b}f(x)\,dx\approx \sum _{k=1}^{N}{\frac {f(x_{k-1})+f(x_{k})}{2}}\Delta x_{k},$ where $\Delta x_{k}=x_{k}-x_{k-1},$ or more a computationally efficient formula $\int _{a}^{b}f(x)\,dx\approx {\frac {1}{2}}{\biggl (}f(x_{0})\Delta _{+1}x_{0}+f(x_{N})\Delta _{-1}x_{N}+\sum _{k=1}^{N-1}f(x_{k})\Delta _{\pm 1}x_{k}{\biggr )},$ where $\Delta _{+1}x_{0}=x_{1}-x_{0},$ $\Delta _{-1}x_{N}=x_{N}-x_{N-1},$ $\Delta _{\pm 1}x_{k}=x_{k+1}-x_{k-1}$ are the corresponding forward, backward, and central differences.

### Uniform grid

For a domain partitioned by N equally spaced points, considerable simplification may occur.

Let $\Delta x={\frac {b-a}{N}}$ and $x_{k}=a+k\Delta x$ for $k=0,1,\ldots ,N.$ The approximation to the integral becomes ${\begin{aligned}\int _{a}^{b}f(x)\,dx&\approx {\frac {\Delta x}{2}}\sum _{k=1}^{N}[f(x_{k-1})+f(x_{k})]\\&=\Delta x{\biggl (}{\tfrac {1}{2}}f(x_{0})+{\tfrac {1}{2}}f(x_{N})+\sum _{k=1}^{N-1}f(x_{k}){\biggr )}.\end{aligned}}$

Sometimes this expression is written as $\Delta x\!\!\mathop {\ \sum {\vphantom {\big )}}'} _{k=0}^{N}f(x_{k}),$

where the symbol ⁠ $\textstyle \sum ~\!\!'$ ⁠ indicates that the first and last terms are halved.

## Error analysis

The error of the composite trapezoidal rule is the difference between the value of the integral and the numerical result: ${\text{E}}=\int _{a}^{b}f(x)\,dx-{\frac {b-a}{N}}\left[{f(a)+f(b) \over 2}+\sum _{k=1}^{N-1}f\left(a+k{\frac {b-a}{N}}\right)\right]$

There exists a number *ξ* between *a* and *b*, such that ${\text{E}}=-{\frac {(b-a)^{3}}{12N^{2}}}f''(\xi )$

It follows that if the integrand is concave up (and thus has a positive second derivative), then the error is negative and the trapezoidal rule overestimates the true value. This can also be seen from the geometric picture: the trapezoids include all of the area under the curve and extend over it. Similarly, a concave-down function yields an underestimate because area is unaccounted for under the curve, but none is counted above. If the interval of the integral being approximated includes an inflection point, the sign of the error is harder to identify.

An asymptotic error estimate for *N* → ∞ is given by ${\text{E}}=-{\frac {(b-a)^{2}}{12N^{2}}}{\big [}f'(b)-f'(a){\big ]}+O(N^{-3}).$ Further terms in this error estimate are given by the Euler–Maclaurin summation formula.

Several techniques can be used to analyze the error, including:

1. Fourier series
2. Residue calculus
3. Euler–Maclaurin summation formula
4. Polynomial interpolation

It is argued that the speed of convergence of the trapezoidal rule reflects and can be used as a definition of classes of smoothness of the functions.

### Proof

First suppose that $h={\frac {b-a}{N}}$ and $a_{k}=a+(k-1)h$ . Let $g_{k}(t)={\frac {1}{2}}t[f(a_{k})+f(a_{k}+t)]-\int _{a_{k}}^{a_{k}+t}f(x)\,dx$ be the function such that $|g_{k}(h)|$ is the error of the trapezoidal rule on one of the intervals, $[a_{k},a_{k}+h]$ . Then ${dg_{k} \over dt}={1 \over 2}[f(a_{k})+f(a_{k}+t)]+{1 \over 2}t\cdot f'(a_{k}+t)-f(a_{k}+t),$ and ${d^{2}g_{k} \over dt^{2}}={1 \over 2}t\cdot f''(a_{k}+t).$

Now suppose that $\left|f''(x)\right|\leq \left|f''(\xi )\right|,$ which holds if f is sufficiently smooth. It then follows that $\left|f''(a_{k}+t)\right|\leq f''(\xi )$ which is equivalent to $-f''(\xi )\leq f''(a_{k}+t)\leq f''(\xi )$ , or $-{\frac {f''(\xi )t}{2}}\leq g_{k}''(t)\leq {\frac {f''(\xi )t}{2}}.$

Since $g_{k}'(0)=0$ and $g_{k}(0)=0$ , $\int _{0}^{t}g_{k}''(x)dx=g_{k}'(t)$ and $\int _{0}^{t}g_{k}'(x)dx=g_{k}(t).$

Using these results, we find $-{\frac {f''(\xi )t^{2}}{4}}\leq g_{k}'(t)\leq {\frac {f''(\xi )t^{2}}{4}}$ and $-{\frac {f''(\xi )t^{3}}{12}}\leq g_{k}(t)\leq {\frac {f''(\xi )t^{3}}{12}}$

Letting $t=h$ we find $-{\frac {f''(\xi )h^{3}}{12}}\leq g_{k}(h)\leq {\frac {f''(\xi )h^{3}}{12}}.$

Summing all of the local error terms we find $\sum _{k=1}^{N}g_{k}(h)={\frac {b-a}{N}}\left[{f(a)+f(b) \over 2}+\sum _{k=1}^{N-1}f\left(a+k{\frac {b-a}{N}}\right)\right]-\int _{a}^{b}f(x)dx.$

But we also have $-\sum _{k=1}^{N}{\frac {f''(\xi )h^{3}}{12}}\leq \sum _{k=1}^{N}g_{k}(h)\leq \sum _{k=1}^{N}{\frac {f''(\xi )h^{3}}{12}}$ and $\sum _{k=1}^{N}{\frac {f''(\xi )h^{3}}{12}}={\frac {f''(\xi )h^{3}N}{12}},$

so that

$-{\frac {f''(\xi )h^{3}N}{12}}\leq {\frac {b-a}{N}}\left[{f(a)+f(b) \over 2}+\sum _{k=1}^{N-1}f\left(a+k{\frac {b-a}{N}}\right)\right]-\int _{a}^{b}f(x)dx\leq {\frac {f''(\xi )h^{3}N}{12}}.$

Therefore the total error is bounded by

${\text{error}}=\left|\int _{a}^{b}f(x)\,dx-{\frac {b-a}{N}}\left[{f(a)+f(b) \over 2}+\sum _{k=1}^{N-1}f\left(a+k{\frac {b-a}{N}}\right)\right]\right|\leq {\frac {f''(\xi )h^{3}N}{12}}={\frac {f''(\xi )(b-a)^{3}}{12N^{2}}}.$

### Periodic and peak functions

The trapezoidal rule converges rapidly for periodic functions. This is an easy consequence of the Euler–Maclaurin summation formula, which says that if f is p times continuously differentiable with period $T,$ then $\sum _{k=0}^{N-1}f(kh)h=\int _{0}^{T}f(x)\,dx+\sum _{k=1}^{\lfloor p/2\rfloor }{\frac {B_{2k}}{(2k)!}}\left(f^{(2k-1)}(T)-f^{(2k-1)}(0)\right)-(-1)^{p}h^{p}\int _{0}^{T}{\tilde {B}}_{p}(x/T)f^{(p)}(x)\,dx,$ where $h:=T/N,$ and ${\tilde {B}}_{p}$ is the periodic extension of the p -th Bernoulli polynomial. Due to the periodicity, the derivatives at the endpoint cancel, and we see that the error is $O(h^{p})$ .

A similar effect is available for peak-like functions, such as Gaussian, Exponentially modified Gaussian and other functions with derivatives at integration limits that can be neglected. The evaluation of the full integral of a Gaussian function by trapezoidal rule with 1% accuracy can be made using just 4 points. Simpson's rule requires 1.8 times more points to achieve the same accuracy.

### "Rough" functions

For functions that are not in *C*2, the error bound given above is not applicable. Still, error bounds for such rough functions can be derived, which typically show a slower convergence with the number of function evaluations N than the $O(N^{-2})$ behaviour given above. Interestingly, in this case the trapezoidal rule often has sharper bounds than Simpson's rule for the same number of function evaluations.

## Applicability and alternatives

The trapezoidal rule is one of a family of formulas for numerical integration called Newton–Cotes formulas, of which the midpoint rule is similar to the trapezoid rule. Simpson's rule is another member of the same family, and in general has faster convergence than the trapezoidal rule for functions which are twice continuously differentiable, though not in all specific cases. However, for various classes of rougher functions (ones with weaker smoothness conditions), the trapezoidal rule has faster convergence in general than Simpson's rule.

Moreover, the trapezoidal rule tends to become extremely accurate when periodic functions are integrated over their periods, which can be analyzed in various ways. Convergence usually is exponential or faster. A similar effect is available for peak functions.

For infinitely smooth non-periodic functions, however, methods with unequally spaced points such as Gaussian quadrature and Clenshaw–Curtis quadrature generally give more precise answers for the same number of function evaluations; Clenshaw–Curtis quadrature can be viewed as a change of variables to express arbitrary integrals in terms of periodic integrals, at which point the trapezoidal rule can be applied accurately.

## Numerical examples

### Approximating the natural logarithm of 3

Since $\int _{1}^{3}{\frac {1}{x}}\,dx=\ln 3-\ln 1=\ln 3,$ we can use the trapezoidal rule to approximate the integral, thereby generating an approximation of $\ln 3$ .

Applying the rule with $n=3$ segments gives $\ln 3=\int _{1}^{3}{\frac {1}{x}}\,dx\approx {\frac {1}{3}}\left(1+{\frac {6}{5}}+{\frac {6}{7}}+{\frac {1}{3}}\right)={\frac {356}{315}}\approx 1.13015873,$ which has absolute error of $0.031546$ and a relative error of $2.87148\%$ .

Applying the rule with $n=6$ segments gives $\ln 3=\int _{1}^{3}{\frac {1}{x}}\,dx\approx {\frac {1}{6}}\left(1+{\frac {3}{2}}+{\frac {6}{5}}+1+{\frac {6}{7}}+{\frac {3}{4}}+{\frac {1}{3}}\right)={\frac {2789}{2520}}\approx 1.10674603,$ which has absolute error of $8.13\times 10^{-3}$ and a relative error of $0.74036\%$ .

### Approximating the integral of a product

The following integral is given: $\int _{0.1}^{1.3}5xe^{-2x}\,dx.$

1. Use the composite trapezoidal rule to estimate the value of this integral. Use three segments.
2. Find the true error $E_{t}$ for part (a).
3. Find the absolute relative true error $|\varepsilon _{t}|$ for part (a).

**Solution**

1. The solution using the composite trapezoidal rule with 3 segments is applied as follows. $\int _{a}^{b}f(x)\,dx\approx {\frac {b-a}{2n}}\left[f(a)+2\sum _{i=1}^{n-1}f(a+ih)+f(b)\right].$ ${\begin{aligned}n&=3,\\a&=0.1,\\b&=1.3,\\h&={\frac {b-a}{n}}={\frac {1.3-0.1}{3}}=0.4.\end{aligned}}$ Using the composite trapezoidal rule formula, $\int _{a}^{b}f(x)\,dx\approx {\frac {b-a}{2n}}\left[f(a)+2\left\{\sum _{i=1}^{n-1}f(a+ih)\right\}+f(b)\right].$ ${\begin{aligned}I&\approx {\frac {1.3-0.1}{6}}\left[f(0.1)+2\sum _{i=1}^{3-1}f(0.1+0.4i)+f(1.3)\right]\\I&\approx {\frac {1.3-0.1}{6}}\left[f(0.1)+2\sum _{i=1}^{2}f(0.1+0.4i)+f(1.3)\right]\\&=0.2[f(0.1)+2f(0.5)+2f(0.9)+f(1.3)]\\&=0.2\left[5\times 0.1\times e^{-2(0.1)}+2(5\times 0.5\times e^{-2(0.5)})+2(5\times 0.9\times e^{-2(0.9)})+5\times 1.3\times e^{-2(1.3)}\right]\\&=0.84385.\end{aligned}}$
2. The exact value of the above integral can be found by integration by parts and is $\int _{0.1}^{1.3}5xe^{-2x}\,dx=0.89387,$ so the true error is ${\begin{aligned}E_{t}&=({\text{true value}})-({\text{approximate value}})\\&=0.89387-0.84385\\&=0.05002.\end{aligned}}$
3. The absolute relative true error is ${\begin{aligned}|\varepsilon _{t}|&=\left|{\frac {\text{true error}}{\text{true value}}}\right|\times 100\%\\&=\left|{\frac {0.05002}{0.89387}}\right|\times 100\%\\&=5.5959\%.\end{aligned}}$
