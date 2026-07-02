---
title: "Error function"
source: https://en.wikipedia.org/wiki/Error_function
domain: special-functions
license: CC-BY-SA-4.0
tags: special functions, bessel functions, gamma function, error function
fetched: 2026-07-02
---

# Error function

In mathematics, the **error function** (also called the **Gauss error function**), often denoted by $\mathbf {erf}$ , is the function $\operatorname {erf} (z)={\frac {2}{\sqrt {\pi }}}\int _{0}^{z}e^{-t^{2}}\,dt.$

The integral here is a complex contour integral which is path-independent because $\exp(-t^{2})$ is holomorphic on the whole complex plane $\mathbb {C}$ . In many applications, the function argument is a real number, in which case the function value is also real.

In some older texts, the error function is defined without the factor of $2/{\sqrt {\pi }}$ . This nonelementary integral is a sigmoid function that occurs often in probability, statistics, and partial differential equations.

In statistics, for non-negative real values of X , the error function has the following interpretation: for a real random variable Y that is normally distributed with mean 0 and standard deviation $1/{\sqrt {2}}$ , $\operatorname {erf} (x)$ is the probability that Y falls in the range $[-x,x]$ .

Two closely related functions are the **complementary error function**

$\operatorname {erfc} (z)=1-\operatorname {erf} (z)$

and the **imaginary error function**

$\operatorname {erfi} (z)=-i\operatorname {erf} (iz),$

where i is the imaginary unit.

## Name

The name "error function" and its abbreviation $\operatorname {erf}$ were proposed by J. W. L. Glaisher in 1871 on account of its connection with "the theory of probability, and notably the theory of errors". The complementary error function was also discussed by Glaisher in a separate publication in the same year. For the "law of facility" of errors whose density is given by

$f(x)=\left({\frac {c}{\pi }}\right)^{1/2}e^{-cx^{2}}$

(the normal distribution), Glaisher calculates the probability of an error lying between p and q as

$\left({\frac {c}{\pi }}\right)^{\frac {1}{2}}\int _{p}^{q}e^{-cx^{2}}\,dx={\frac {1}{2}}{\big (}\operatorname {erf} (q{\sqrt {c}})-\operatorname {erf} (p{\sqrt {c}}){\big )}.$

## Applications

When the results of a series of measurements are described by a normal distribution with standard deviation $\sigma$ and expected value zero, then

$\operatorname {erf} {\bigg (}{\frac {a}{\sigma {\sqrt {2}}}}{\bigg )}$

is the probability that the error of a single measurement lies between $-a$ and a . This is useful, for example, in determining the bit error rate of a digital communication system.

The error and complementary error functions occur, for example, in solutions of the heat equation when boundary conditions are given by the Heaviside step function.

The error function and its approximations can be used to estimate results that hold with high probability or with low probability. Given a normally distributed random variable X with mean $\mu$ and standard deviation $\sigma$ and a constant $L>\mu$ , it can be shown (via integration by substitution) that

$\Pr[X\leq L]={\frac {1}{2}}+{\frac {1}{2}}\operatorname {erf} \left({\frac {L-\mu }{{\sqrt {2}}\sigma }}\right)\approx A\exp \left(\!-B\,\left({\frac {L-\mu }{\sigma }}\right)^{2}\right)$

where A and B are certain numeric constants. If L is sufficiently far from the mean, specifically, $\mu -L\geq \sigma {\sqrt {\log(k)}}$ , then

$\Pr[X\leq L]\leq A\exp(-B\log(k))={\frac {A}{k^{B}}}$

and so the probability goes to 0 as $k\to \infty$ .

The probability for X being in the interval $[L_{a},L_{b}]$ can be derived as ${\begin{aligned}\Pr[L_{a}\leq X\leq L_{b}]&=\int _{L_{a}}^{L_{b}}{\frac {1}{{\sqrt {2\pi }}\sigma }}\exp \left(-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}\right)\,dx\\[4pt]&={\frac {1}{2}}\left(\operatorname {erf} \left({\frac {L_{b}-\mu }{{\sqrt {2}}\sigma }}\right)-\operatorname {erf} \left({\frac {L_{a}-\mu }{{\sqrt {2}}\sigma }}\right)\right).\end{aligned}}$

## Properties

Plots in the complex plane

exp(−

z

2

)

in the complex plane, with

domain coloring

.

erf(

z

)

in the complex plane.

The error function is an odd function. This directly results from the fact that the integrand $e^{-t^{2}}$ is an even function (since the antiderivative of an even function which is zero at the origin is an odd function, and vice versa).

Since the error function is an entire function which maps real numbers to real numbers, for any complex number z ,

$\operatorname {erf} ({\bar {z}})={\overline {\operatorname {erf} (z)}}$

where ${\bar {z}}$ denotes the complex conjugate of z .

The error function at $\infty$ is exactly 1 (see Gaussian integral). At the real axis, $\operatorname {erf} (z)$ approaches 1 at $z\to \infty$ and $-1$ at $z\to -\infty$ . At the imaginary axis, it tends to $\pm i\infty$ .

### Taylor series

The error function is an entire function; it has no singularities (except at infinity) and its Taylor expansion always converges. For $x\gg 1$ , however, cancellation of leading terms makes the Taylor expansion impractical.

The defining integral cannot be evaluated in closed form in terms of elementary functions (see Liouville's theorem), but by expanding the integrand $e^{-z^{2}}$ into its Maclaurin series, integrating term by term, and using the fact that $\operatorname {erf} (0)=0$ , one obtains the error function's Maclaurin series as: ${\begin{aligned}\operatorname {erf} (z)&={\frac {2}{\sqrt {\pi }}}\sum _{n=0}^{\infty }{\frac {(-1)^{n}z^{2n+1}}{n!(2n+1)}}\\[6pt]&={\frac {2}{\sqrt {\pi }}}\left(z-{\frac {z^{3}}{3}}+{\frac {z^{5}}{10}}-{\frac {z^{7}}{42}}+{\frac {z^{9}}{216}}-\cdots \right)\end{aligned}}$ which holds for every complex number z . The denominator terms form sequence A007680 in the OEIS. This is a special case of Kummer's function:

$\operatorname {erf} (z)={\frac {2z}{\sqrt {\pi }}}\,{}_{1}F_{1}{\bigg (}{\frac {1}{2}},{\frac {3}{2}},-z^{2}{\bigg )}.$

For iterative calculation of the above series, the following alternative formulation may be useful: ${\begin{aligned}\operatorname {erf} (z)&={\frac {2}{\sqrt {\pi }}}\sum _{n=0}^{\infty }\left(z\prod _{k=1}^{n}{\frac {-(2k-1)z^{2}}{k(2k+1)}}\right)\\[6pt]&={\frac {2}{\sqrt {\pi }}}\sum _{n=0}^{\infty }{\frac {z}{2n+1}}\prod _{k=1}^{n}{\frac {-z^{2}}{k}},\end{aligned}}$ because

${\frac {-(2k-1)z^{2}}{k(2k+1)}}$

expresses the multiplier to turn the k -th term into the $(k+1)$ -th term (considering z as the first term).

The imaginary error function has a similar Maclaurin series: ${\begin{aligned}\operatorname {erfi} (z)&={\frac {2}{\sqrt {\pi }}}\sum _{n=0}^{\infty }{\frac {z^{2n+1}}{n!(2n+1)}}\\[6pt]&={\frac {2}{\sqrt {\pi }}}\left(z+{\frac {z^{3}}{3}}+{\frac {z^{5}}{10}}+{\frac {z^{7}}{42}}+{\frac {z^{9}}{216}}+\cdots \right)\end{aligned}}$ which holds for every complex number z .

### Derivative and integral

The derivative of the error function follows immediately from its definition: ${\frac {d}{dz}}\operatorname {erf} (z)={\frac {2}{\sqrt {\pi }}}e^{-z^{2}}.$ From this, the derivative of the imaginary error function is also immediate: ${\frac {d}{dz}}\operatorname {erfi} (z)={\frac {2}{\sqrt {\pi }}}e^{z^{2}}.$ Higher order derivatives are given by $\operatorname {erf} ^{(k)}(z)={\frac {2(-1)^{k-1}}{\sqrt {\pi }}}{\mathit {H}}_{k-1}(z)e^{-z^{2}}={\frac {2}{\sqrt {\pi }}}{\frac {d^{k-1}}{dz^{k-1}}}{\big (}e^{-z^{2}}{\big )},$ where the $H_{k}$ are the physicists' Hermite polynomials.

An antiderivative of the error function, obtainable by integration by parts, is $\int \operatorname {erf} (z)dz=z\operatorname {erf} (z)+{\frac {e^{-z^{2}}}{\sqrt {\pi }}}+C.$ An antiderivative of the imaginary error function, also obtainable by integration by parts, is $\int \operatorname {erfi} (z)dz=z\operatorname {erfi} (z)-{\frac {e^{z^{2}}}{\sqrt {\pi }}}+C.$

### Bürmann series

An expansion which converges more rapidly for all real values of x than a Taylor expansion is obtained by using Bürmann's theorem: ${\begin{aligned}\operatorname {erf} (x)&={\frac {2}{\sqrt {\pi }}}\operatorname {sgn}(x)\cdot {\sqrt {1-e^{-x^{2}}}}\left(1-{\frac {1}{12}}\left(1-e^{-x^{2}}\right)-{\frac {7}{480}}\left(1-e^{-x^{2}}\right)^{2}-{\frac {5}{896}}\left(1-e^{-x^{2}}\right)^{3}-\cdots \right)\\[10pt]&={\frac {2}{\sqrt {\pi }}}\operatorname {sgn}(x)\cdot {\sqrt {1-e^{-x^{2}}}}\left({\frac {\sqrt {\pi }}{2}}+\sum _{k=1}^{\infty }c_{k}e^{-kx^{2}}\right)\end{aligned}}$ where $\operatorname {sgn}$ is the sign function. By keeping only the first two coefficients and choosing $c_{1}=31/200$ and $c_{2}=-341/8000$ , the resulting approximation shows its largest relative error at $x=\pm 1.40587$ , where it is less than $0.0034361$ : $\operatorname {erf} (x)\approx {\frac {2}{\sqrt {\pi }}}\operatorname {sgn}(x)\cdot {\sqrt {1-e^{-x^{2}}}}\left({\frac {\sqrt {\pi }}{2}}+{\frac {31}{200}}e^{-x^{2}}-{\frac {341}{8000}}e^{-2x^{2}}\right).$

### Inverse functions

Given a complex number z , there is not a *unique* complex number w satisfying $\operatorname {erf} (w)=z$ , so a true inverse function would be multivalued. However, for $-1<x<1$ , there is a unique *real* number denoted $\operatorname {erf} ^{-1}(x)$ satisfying

$\operatorname {erf} \left(\operatorname {erf} ^{-1}(x)\right)=x.$

The **inverse error function** is usually defined with domain $(-1,1)$ , and it is restricted to this domain in many computer algebra systems. However, it can be extended to the disk $|z|<1$ of the complex plane, using the Maclaurin series $\operatorname {erf} ^{-1}(z)=\sum _{k=0}^{\infty }{\frac {c_{k}}{2k+1}}\left({\frac {\sqrt {\pi }}{2}}z\right)^{2k+1},$ where $c_{0}=1$ and ${\begin{aligned}c_{k}&=\sum _{m=0}^{k-1}{\frac {c_{m}c_{k-1-m}}{(m+1)(2m+1)}}\\[1ex]&=\left\{1,1,{\frac {7}{6}},{\frac {127}{90}},{\frac {4369}{2520}},{\frac {34807}{16200}},\ldots \right\}.\end{aligned}}$

So we have the series expansion (common factors have been canceled from numerators and denominators):

$\operatorname {erf} ^{-1}(z)={\frac {\sqrt {\pi }}{2}}\left(z+{\frac {\pi }{12}}z^{3}+{\frac {7\pi ^{2}}{480}}z^{5}+{\frac {127\pi ^{3}}{40320}}z^{7}+{\frac {4369\pi ^{4}}{5806080}}z^{9}+{\frac {34807\pi ^{5}}{182476800}}z^{11}+\cdots \right).$

(After cancellation the numerator and denominator values in (sequence A092676 in the OEIS) and (sequence A092677 in the OEIS) respectively; without cancellation the numerator terms are values in (sequence A002067 in the OEIS).) The error function's value at $\pm \infty$ is equal to $\pm 1$ .

For $|z|<1$ , we have $\operatorname {erf} (\operatorname {erf} ^{-1}(z))=z$ .

The **inverse complementary error function** is defined as $\operatorname {erfc} ^{-1}(1-z)=\operatorname {erf} ^{-1}(z).$ For real x , there is a unique *real* number $\operatorname {erfi} ^{-1}(x)$ satisfying $\operatorname {erfi} (\operatorname {erfi} ^{-1}(x))=x$ . The **inverse imaginary error function** is defined as $\operatorname {erfi} ^{-1}(x)$ .

For any real x , Newton's method can be used to compute $\operatorname {erfi} ^{-1}(x)$ , and for $-1\leq x\leq 1$ , the following Maclaurin series converges:

$\operatorname {erfi} ^{-1}(z)=\sum _{k=0}^{\infty }{\frac {(-1)^{k}c_{k}}{2k+1}}\left({\frac {\sqrt {\pi }}{2}}z\right)^{2k+1},$

where $c_{k}$ is defined as above.

### Asymptotic expansion

A useful asymptotic expansion of the complementary error function (and therefore also of the error function) for large real x is ${\begin{aligned}\operatorname {erfc} (x)&={\frac {e^{-x^{2}}}{x{\sqrt {\pi }}}}\left(1+\sum _{n=1}^{\infty }(-1)^{n}{\frac {1\cdot 3\cdot 5\cdots (2n-1)}{\left(2x^{2}\right)^{n}}}\right)\\[6pt]&={\frac {e^{-x^{2}}}{x{\sqrt {\pi }}}}\sum _{n=0}^{\infty }(-1)^{n}{\frac {(2n-1)!!}{\left(2x^{2}\right)^{n}}},\end{aligned}}$ where $(2n-1)!!$ is the double factorial of $2n-1$ , i.e. the product of all odd numbers up to $2n-1$ . This series diverges for every finite x , and its meaning as asymptotic expansion is that for any integer $N\geq 1$ one has

$\operatorname {erfc} (x)={\frac {e^{-x^{2}}}{x{\sqrt {\pi }}}}\sum _{n=0}^{N-1}(-1)^{n}{\frac {(2n-1)!!}{\left(2x^{2}\right)^{n}}}+R_{N}(x),$

where the remainder is

$R_{N}(x):={\frac {(-1)^{N}\,(2N-1)!!}{{\sqrt {\pi }}\cdot 2^{N-1}}}\int _{x}^{\infty }t^{-2N}e^{-t^{2}}\,dt,$

which follows easily by induction, writing

$e^{-t^{2}}=-{\frac {1}{2t}}\,{\frac {d}{dt}}e^{-t^{2}}$

and integrating by parts. The asymptotic behavior of the remainder term is

$R_{N}(x)=O{\Big (}x^{-(1+2N)}e^{-x^{2}}{\Big )}$

as $x\to \infty$ . This can be found by

$R_{N}(x)\propto \int _{x}^{\infty }t^{-2N}e^{-t^{2}}\,dt=e^{-x^{2}}\int _{0}^{\infty }(t+x)^{-2N}e^{-t^{2}-2tx}\,dt\leq e^{-x^{2}}\int _{0}^{\infty }x^{-2N}e^{-2tx}\,dt\propto x^{-(1+2N)}e^{-x^{2}}.$

For large enough values of x , only the first few terms of this asymptotic expansion are needed to obtain a good approximation of $\operatorname {erfc} (x)$ (while for not too large values of x , the above Taylor expansion at 0 provides a very fast convergence).

### Continued fraction expansion

A continued fraction expansion of the complementary error function was found by Laplace: $\operatorname {erfc} (z)={\frac {z}{\sqrt {\pi }}}e^{-z^{2}}{\cfrac {1}{z^{2}+{\cfrac {a_{1}}{1+{\cfrac {a_{2}}{z^{2}+{\cfrac {a_{3}}{1+\dotsb }}}}}}}}$ where $a_{m}={\frac {m}{2}}$ .

### Factorial series

The inverse factorial series

${\begin{aligned}\operatorname {erfc} (z)&={\frac {e^{-z^{2}}}{{\sqrt {\pi }}\,z}}\sum _{n=0}^{\infty }{\frac {\left(-1\right)^{n}Q_{n}}{{\left(z^{2}+1\right)}^{(n)}}}\\[1ex]&={\frac {e^{-z^{2}}}{{\sqrt {\pi }}\,z}}\left[1-{\frac {1}{2}}{\frac {1}{(z^{2}+1)}}+{\frac {1}{4}}{\frac {1}{\left(z^{2}+1\right)\left(z^{2}+2\right)}}-\cdots \right]\end{aligned}}$

converges for $\operatorname {Re} (z^{2})>0$ . Here

${\begin{aligned}Q_{n}&={\frac {1}{\sqrt {\pi }}}\int _{0}^{\infty }\tau (\tau -1)\cdots (\tau -n+1)\tau ^{-{\frac {1}{2}}}e^{-\tau }\,d\tau \\[1ex]&=\sum _{k=0}^{n}s(n,k)\left({\frac {1}{2}}\right)^{(k)}=\sum _{k=0}^{n}s(n,k){\frac {(2k-1)!!}{2^{k}}}\end{aligned}}$

where $z^{(n)}$ denotes the rising factorial, and $s(n,k)$ denotes a signed Stirling number of the first kind. The Taylor series can be written in terms of the double factorial:

$\operatorname {erf} (z)={\frac {2}{\sqrt {\pi }}}\sum _{n=0}^{\infty }{\frac {(-2)^{n}(2n-1)!!}{(2n+1)!}}z^{2n+1}.$

## Bounds and numerical approximations

### Approximation with elementary functions

Abramowitz and Stegun give several approximations of varying accuracy (equations 7.1.25–28). This allows one to choose the fastest approximation suitable for a given application. In order of increasing accuracy, they are: $\operatorname {erf} (x)\approx 1-{\frac {1}{\left(1+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+a_{4}x^{4}\right)^{4}}},\qquad x\geq 0$ (maximum error: 5×10−4)

where *a*1 = 0.278393, *a*2 = 0.230389, *a*3 = 0.000972, *a*4 = 0.078108

$\operatorname {erf} (x)\approx 1-\left(a_{1}t+a_{2}t^{2}+a_{3}t^{3}\right)e^{-x^{2}},\quad t={\frac {1}{1+px}},\qquad x\geq 0$ (maximum error: 2.5×10−5)

where *p* = 0.47047, *a*1 = 0.3480242, *a*2 = −0.0958798, *a*3 = 0.7478556

$\operatorname {erf} (x)\approx 1-{\frac {1}{\left(1+a_{1}x+a_{2}x^{2}+\cdots +a_{6}x^{6}\right)^{16}}},\qquad x\geq 0$ (maximum error: 3×10−7)

where *a*1 = 0.0705230784, *a*2 = 0.0422820123, *a*3 = 0.0092705272, *a*4 = 0.0001520143, *a*5 = 0.0002765672, *a*6 = 0.0000430638

$\operatorname {erf} (x)\approx 1-\left(a_{1}t+a_{2}t^{2}+\cdots +a_{5}t^{5}\right)e^{-x^{2}},\quad t={\frac {1}{1+px}}$ (maximum error: 1.5×10−7)

where *p* = 0.3275911, *a*1 = 0.254829592, *a*2 = −0.284496736, *a*3 = 1.421413741, *a*4 = −1.453152027, *a*5 = 1.061405429

One can improve the accuracy of the A&S approximation by extending it with three extra parameters, $\operatorname {erf} (x)\approx 1-\left(a_{1}t+a_{2}t^{2}+\cdots +a_{5}t^{5}+a_{6}t^{6}+a_{7}t^{7}\right)e^{-x^{2}},\quad t={\frac {1}{1+p_{1}x+p_{2}x^{2}}}$ where p1 = 0.406742016006509, p2 = 0.0072279182302319, a1 = 0.316879890481381, a2 = -0.138329314150635, a3 = 1.08680830347054, a4 = -1.11694155120396, a5 = 1.20644903073232, a6 = -0.393127715207728, a7 = 0.0382613542530727. The maximum error of this approximation is about 2×10−9. The parameters are obtained by fitting the extended approximation to the accurate values of the error function using the following Python code.

| Python code to fit extended A&S approximation |
|---|
| import numpy as np from math import erf, exp, sqrt from scipy.optimize import least_squares # # Extended A&S approximation: # erf(x) ≈ 1 − t * exp(−x^2) * (a1 + a2*t + a3*t^2 + ... + a7*t^6) # where now # t = 1 / (1 + p1*x + p2*x^2) # We fit parameters p1, p2, a1..a7 over x in [0, 10]. # def approx_erf(params, x): p1 = params[0] p2 = params[1] a = params[2:] t = 1.0 / (1.0 + p1 * x + p2 * x * x) poly = np.zeros_like(x) tt = np.ones_like(x) # t^0 # polynomial: a1*t^0 + a2*t^1 + ... + a7*t^6 for ak in a: poly += ak * tt tt *= t return 1.0 - t * np.exp(-x * x) * poly def residuals(params, xs, ys): return approx_erf(params, xs) - ys # # Prepare data for fitting # N = 300 xmin = 0 xmax = 10 xs = np.linspace(xmin, xmax, N) ys = np.array([erf(x) for x in xs], dtype=float) # # Initial guess for parameters # Start from original A&S values and extend them conservatively # p1_0 = 0.3275911 # original A&S p p2_0 = 0.0 # new denominator parameter # original A&S 5 coefficients, add two => 7 in total a0 = [ 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429, 0.0, # new term 0.0, # another new term ] params0 = np.array([p1_0, p2_0] + a0, dtype=float) # # Fit using nonlinear least squares (Levenberg–Marquardt) # result = least_squares( residuals, params0, args=(xs, ys), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=5000 ) params = result.x p1_fit = params[0] p2_fit = params[1] a_fit = params[2:] # # Print fitted parameters # print("\nFitted parameters:") print(f"p1 = {p1_fit:.15g},") print(f"p2 = {p2_fit:.15g},") for i, ai in enumerate(a_fit, 1): print(f"a{i} = {ai:.15g},") # # Evaluate approximation error # approx_vals = approx_erf(params, xs) abs_err = np.abs(approx_vals - ys) print(f"\nMaximum absolute error on [{xmin},{xmax}]:", np.max(abs_err)) print("RMS error:", np.sqrt(np.mean(abs_err**2))) print("Done.") |

All of these approximations are valid for *x* ≥ 0. To use these approximations for negative x, use the fact that erf(*x*) is an odd function, so erf(*x*) = −erf(−*x*).

Exponential bounds and a pure exponential approximation for the complementary error function are given by ${\begin{aligned}\operatorname {erfc} (x)&\leq {\frac {1}{2}}e^{-2x^{2}}+{\frac {1}{2}}e^{-x^{2}}\leq e^{-x^{2}},&&x>0\\[1.5ex]\operatorname {erfc} (x)&\approx {\frac {1}{6}}e^{-x^{2}}+{\frac {1}{2}}e^{-{\frac {4}{3}}x^{2}},&&x>0.\end{aligned}}$

The above have been generalized to sums of N exponentials with increasing accuracy in terms of N so that erfc(*x*) can be accurately approximated or bounded by 2*Q̃*(√2*x*), where ${\tilde {Q}}(x)=\sum _{n=1}^{N}a_{n}e^{-b_{n}x^{2}}.$ In particular, there is a systematic methodology to solve the numerical coefficients {(*an*,*bn*)}*N* *n* = 1 that yield a minimax approximation or bound for the closely related Q-function: *Q*(*x*) ≈ *Q̃*(*x*), *Q*(*x*) ≤ *Q̃*(*x*), or *Q*(*x*) ≥ *Q̃*(*x*) for *x* ≥ 0. The coefficients {(*an*,*bn*)}*N* *n* = 1 for many variations of the exponential approximations and bounds up to *N* = 25 have been released to open access as a comprehensive dataset.

A tight approximation of the complementary error function for *x* ∈ [0,∞) is given by Karagiannidis & Lioumpas (2007), who showed for the appropriate choice of parameters {*A*,*B*} that $\operatorname {erfc} (x)\approx {\frac {\left(1-e^{-Ax}\right)e^{-x^{2}}}{B{\sqrt {\pi }}x}}.$ They determined {*A*,*B*} = {1.98,1.135}, which gave a good approximation for all *x* ≥ 0. Alternative coefficients are also available for tailoring accuracy for a specific application or transforming the expression into a tight bound.

A single-term lower bound is $\operatorname {erfc} (x)\geq {\sqrt {\frac {2e}{\pi }}}{\frac {\sqrt {\beta -1}}{\beta }}e^{-\beta x^{2}},\qquad x\geq 0,\quad \beta >1,$ where the parameter β can be picked to minimize error on the desired interval of approximation.

Another approximation is given by Sergei Winitzki using his "global Padé approximations": $\operatorname {erf} (x)\approx \operatorname {sgn} x\cdot {\sqrt {1-\exp \left(-x^{2}{\frac {{\frac {4}{\pi }}+ax^{2}}{1+ax^{2}}}\right)}}$ where $a={\frac {8(\pi -3)}{3\pi (4-\pi )}}\approx 0.140012.$ This is designed to be very accurate in the neighborhoods of 0 and infinity, and the *relative* error is less than 0.00035 for all real x. Using the alternate value *a* ≈ 0.147 reduces the maximum relative error to about 0.00013.

The extended "global Pade" approximation, $\operatorname {erf} (x)\approx \operatorname {sgn} x\cdot {\sqrt {1-\exp \left(-x^{2}{\frac {4+0.880877880079853x^{2}+0.144026670907584x^{4}+0.0077581300270021x^{6}}{\pi +0.786235558186528x^{2}+0.128368576906837x^{4}+0.00773380006014367x^{6}}}\right)}}\,,$ provides a maximum error of about 2×10−9, as demonstrated by the following Python script.

| Python script to fit extended "global Pade" approximation |
|---|
| import numpy,math from scipy.optimize import least_squares # approximation to erf(x) def approx_erf(p,x): frac=(4+p[0]*x**2+p[1]*x**4+p[2]*x**6)/( math.pi+p[3]*x**2+p[4]*x**4+p[5]*x**6) return numpy.sign(x)*numpy.sqrt( 1-numpy.exp(-x*x*frac)) def residuals(params, xs, ys): return approx_erf(params, xs) - ys # data for fitting N = 200 xmin = 0 xmax = 9 xs = numpy.linspace(xmin, xmax, N) ys = numpy.array([math.erf(x) for x in xs], dtype=float) params0 = numpy.array([0.9,0.1,0.008,0.8,0.1,0.008], dtype=float) # fitting result = least_squares( residuals, params0, args=(xs, ys), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=5000 ) params = result.x # print out fitted parameters print("\nFitted parameters:") for i, pi in enumerate(params, 0): print(f"p{i} = {pi:.15g},") # evaluate approximation error approx_vals = approx_erf(params, xs) abs_err = numpy.abs(approx_vals - ys) print(f"\nMaximum absolute error on [{xmin},{xmax}]:", numpy.max(abs_err)) print("RMS error:", numpy.sqrt(numpy.mean(abs_err**2))) print("Done.") |

Winitzki's approximation can be inverted to obtain an approximation for the inverse error function: $\operatorname {erf} ^{-1}(x)\approx \operatorname {sgn} x\cdot {\sqrt {{\sqrt {\left({\frac {2}{\pi a}}+{\frac {\ln \left(1-x^{2}\right)}{2}}\right)^{2}-{\frac {\ln \left(1-x^{2}\right)}{a}}}}-\left({\frac {2}{\pi a}}+{\frac {\ln \left(1-x^{2}\right)}{2}}\right)}}.$

An approximation with a maximal error of 1.2×10−7 for any real argument is: ${\begin{aligned}\operatorname {erf} (x)&={\begin{cases}1-\tau ,&x\geq 0\\\tau -1,&x<0\end{cases}}\\\tau &=t\cdot \exp \left(-x^{2}-1.26551223+1.00002368t+0.37409196t^{2}+0.09678418t^{3}-0.18628806t^{4}\right.\\&\left.\qquad \qquad \qquad +0.27886807t^{5}-1.13520398t^{6}+1.48851587t^{7}-0.82215223t^{8}+0.17087277t^{9}\right)\\t&={\frac {1}{1+{\frac {1}{2}}|x|}}\end{aligned}}$

An approximation of $\operatorname {erfc}$ with a maximum relative error less than $2^{-53}$ $\left(\approx 1.1\times 10^{-16}\right)$ in absolute value is: for $x\geq 0$ , ${\begin{aligned}\operatorname {erfc} \left(x\right)&=\left({\frac {0.56418958354775629}{x+2.06955023132914151}}\right)\left({\frac {x^{2}+2.71078540045147805x+5.80755613130301624}{x^{2}+3.47954057099518960x+12.06166887286239555}}\right)\\&\left({\frac {x^{2}+3.47469513777439592x+12.07402036406381411}{x^{2}+3.72068443960225092x+8.44319781003968454}}\right)\left({\frac {x^{2}+4.00561509202259545x+9.30596659485887898}{x^{2}+3.90225704029924078x+6.36161630953880464}}\right)\\&\left({\frac {x^{2}+5.16722705817812584x+9.12661617673673262}{x^{2}+4.03296893109262491x+5.13578530585681539}}\right)\left({\frac {x^{2}+5.95908795446633271x+9.19435612886969243}{x^{2}+4.11240942957450885x+4.48640329523408675}}\right)e^{-x^{2}}\\\end{aligned}}$ and for $x<0$ $\operatorname {erfc} \left(x\right)=2-\operatorname {erfc} \left(-x\right)$

A simple approximation for real-valued arguments can be done through hyperbolic functions: $\operatorname {erf} \left(x\right)\approx z(x)=\tanh \left({\frac {2}{\sqrt {\pi }}}\left(x+{\frac {11}{123}}x^{3}\right)\right)$ which keeps the absolute difference $\left|\operatorname {erf} \left(x\right)-z(x)\right|<0.000358,\,\forall x$ .

Since the error function and the Gaussian Q-function are closely related through the identity $\operatorname {erfc} (x)=2Q({\sqrt {2}}x)$ or equivalently $Q(x)={\frac {1}{2}}\operatorname {erfc} \left({\frac {x}{\sqrt {2}}}\right)$ , bounds developed for the Q-function can be adapted to approximate the complementary error function. A pair of tight lower and upper bounds on the Gaussian Q-function for positive arguments $x\in [0,\infty )$ was introduced by Abreu (2012) based on a simple algebraic expression with only two exponential terms: ${\begin{aligned}x&\geq 0\\{\frac {1}{2}}\operatorname {erfc} \left({\frac {x}{\sqrt {2}}}\right)&\geq {\frac {1}{12}}e^{-x^{2}}+{\frac {1}{{\sqrt {2\pi }}(x+1)}}e^{-x^{2}/2}\\&\leq {\frac {1}{50}}e^{-x^{2}}+{\frac {1}{2(x+1)}}e^{-x^{2}/2}\\{\frac {1}{25}}e^{-2x^{2}}+{\frac {1}{x+1}}e^{-x^{2}}\geq \operatorname {erfc} (x)&\geq {\frac {1}{6}}e^{-2x^{2}}+{\frac {1}{2{\sqrt {2\pi }}(x+1)}}e^{-x^{2}}\end{aligned}}$

These bounds stem from a unified form $Q_{\mathrm {B} }(x;a,b)={\frac {\exp(-x^{2})}{a}}+{\frac {\exp(-x^{2}/2)}{b(x+1)}},$ where the parameters a and b are selected to ensure the bounding properties: for the lower bound, $a_{\mathrm {L} }=12$ and $b_{\mathrm {L} }={\sqrt {2\pi }}$ , and for the upper bound, $a_{\mathrm {U} }=50$ and $b_{\mathrm {U} }=2$ . These expressions maintain simplicity and tightness, providing a practical trade-off between accuracy and ease of computation. They are particularly valuable in theoretical contexts, such as communication theory over fading channels, where both functions frequently appear. Additionally, the original Q-function bounds can be extended to $Q^{n}(x)$ for positive integers n via the binomial theorem, suggesting potential adaptability for powers of $\operatorname {erfc} (x)$ , though this is less commonly required in error function applications.

### Table of values

| *x* | erf(*x*) | 1 − erf(*x*) |
|---|---|---|
| 0 | 0 | 1 |
| 0.02 | 0.022564575 | 0.977435425 |
| 0.04 | 0.045111106 | 0.954888894 |
| 0.06 | 0.067621594 | 0.932378406 |
| 0.08 | 0.090078126 | 0.909921874 |
| 0.1 | 0.112462916 | 0.887537084 |
| 0.2 | 0.222702589 | 0.777297411 |
| 0.3 | 0.328626759 | 0.671373241 |
| 0.4 | 0.428392355 | 0.571607645 |
| 0.5 | 0.520499878 | 0.479500122 |
| 0.6 | 0.603856091 | 0.396143909 |
| 0.7 | 0.677801194 | 0.322198806 |
| 0.8 | 0.742100965 | 0.257899035 |
| 0.9 | 0.796908212 | 0.203091788 |
| 1 | 0.842700793 | 0.157299207 |
| 1.1 | 0.880205070 | 0.119794930 |
| 1.2 | 0.910313978 | 0.089686022 |
| 1.3 | 0.934007945 | 0.065992055 |
| 1.4 | 0.952285120 | 0.047714880 |
| 1.5 | 0.966105146 | 0.033894854 |
| 1.6 | 0.976348383 | 0.023651617 |
| 1.7 | 0.983790459 | 0.016209541 |
| 1.8 | 0.989090502 | 0.010909498 |
| 1.9 | 0.992790429 | 0.007209571 |
| 2 | 0.995322265 | 0.004677735 |
| 2.1 | 0.997020533 | 0.002979467 |
| 2.2 | 0.998137154 | 0.001862846 |
| 2.3 | 0.998856823 | 0.001143177 |
| 2.4 | 0.999311486 | 0.000688514 |
| 2.5 | 0.999593048 | 0.000406952 |
| 3 | 0.999977910 | 0.000022090 |
| 3.5 | 0.999999257 | 0.000000743 |

### Complementary error function

The **complementary error function**, denoted erfc, is defined as ${\begin{aligned}\operatorname {erfc} (x)&=1-\operatorname {erf} (x)\\&={\frac {2}{\sqrt {\pi }}}\int _{x}^{\infty }e^{-t^{2}}\,dt\\&=e^{-x^{2}}\operatorname {erfcx} (x),\end{aligned}}$ which also defines erfcx, the **scaled complementary error function** (which can be used instead of erfc to avoid arithmetic underflow). Another form of erfc *x* for *x* ≥ 0 is known as Craig's formula, after its discoverer: $\operatorname {erfc} (x\mid x\geq 0)={\frac {2}{\pi }}\int _{0}^{\frac {\pi }{2}}\exp \left(-{\frac {x^{2}}{\sin ^{2}\theta }}\right)\,d\theta .$ This expression is valid only for positive values of x, but can be used in conjunction with erfc(*x*) = 2 − erfc(−*x*) to obtain erfc(*x*) for negative values. This form is advantageous in that the range of integration is fixed and finite. An extension of this expression for the erfc of the sum of two non-negative variables is $\operatorname {erfc} (x+y\mid x,y\geq 0)={\frac {2}{\pi }}\int _{0}^{\frac {\pi }{2}}\exp \left(-{\frac {x^{2}}{\sin ^{2}\theta }}-{\frac {y^{2}}{\cos ^{2}\theta }}\right)\,d\theta .$

### Imaginary error function

The **imaginary error function**, denoted erfi, is defined as ${\begin{aligned}\operatorname {erfi} (x)&=-i\operatorname {erf} (ix)\\&={\frac {2}{\sqrt {\pi }}}\int _{0}^{x}e^{t^{2}}\,dt\\&={\frac {2}{\sqrt {\pi }}}e^{x^{2}}D(x),\end{aligned}}$ where *D*(*x*) is the Dawson function (which can be used instead of erfi to avoid arithmetic overflow).

Despite the name "imaginary error function", erfi(*x*) is real when x is real.

When the error function is evaluated for arbitrary complex arguments z, the resulting **complex error function** is usually discussed in scaled form as the Faddeeva function: $w(z)=e^{-z^{2}}\operatorname {erfc} (-iz)=\operatorname {erfcx} (-iz).$

### Cumulative distribution function

The error function is essentially identical to the standard normal cumulative distribution function, denoted Φ, also named norm(*x*) by some software languages, as they differ only by scaling and translation. Indeed, ${\begin{aligned}\Phi (x)&={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{x}e^{\tfrac {-t^{2}}{2}}\,dt\\[6pt]&={\frac {1}{2}}\left(1+\operatorname {erf} \left({\frac {x}{\sqrt {2}}}\right)\right)\\[6pt]&={\frac {1}{2}}\operatorname {erfc} \left(-{\frac {x}{\sqrt {2}}}\right)\end{aligned}}$ or rearranged for erf and erfc: ${\begin{aligned}\operatorname {erf} (x)&=2\Phi {\left(x{\sqrt {2}}\right)}-1\\[6pt]\operatorname {erfc} (x)&=2\Phi {\left(-x{\sqrt {2}}\right)}\\&=2\left(1-\Phi {\left(x{\sqrt {2}}\right)}\right).\end{aligned}}$

Consequently, the error function is also closely related to the Q-function, which is the tail probability of the standard normal distribution. The Q-function can be expressed in terms of the error function as ${\begin{aligned}Q(x)&={\frac {1}{2}}-{\frac {1}{2}}\operatorname {erf} \left({\frac {x}{\sqrt {2}}}\right)\\&={\frac {1}{2}}\operatorname {erfc} \left({\frac {x}{\sqrt {2}}}\right).\end{aligned}}$

The inverse of Φ is known as the normal quantile function, or probit function and may be expressed in terms of the inverse error function as $\operatorname {probit} (p)=\Phi ^{-1}(p)={\sqrt {2}}\operatorname {erf} ^{-1}(2p-1)=-{\sqrt {2}}\operatorname {erfc} ^{-1}(2p).$

The standard normal cdf is used more often in probability and statistics, and the error function is used more often in other branches of mathematics.

The error function is a special case of the Mittag-Leffler function, and can also be expressed as a confluent hypergeometric function (Kummer's function): $\operatorname {erf} (x)={\frac {2x}{\sqrt {\pi }}}M\left({\tfrac {1}{2}},{\tfrac {3}{2}},-x^{2}\right).$

It has a simple expression in terms of the Fresnel integral.

In terms of the regularized gamma function P and the incomplete gamma function, $\operatorname {erf} (x)=\operatorname {sgn}(x)\cdot P\left({\tfrac {1}{2}},x^{2}\right)={\frac {\operatorname {sgn}(x)}{\sqrt {\pi }}}\gamma {\left({\tfrac {1}{2}},x^{2}\right)}.$ sgn(*x*) is the sign function.

### Iterated integrals of the complementary error function

The iterated integrals of the complementary error function are defined by ${\begin{aligned}i^{n}\!\operatorname {erfc} (z)&=\int _{z}^{\infty }i^{n-1}\!\operatorname {erfc} (\zeta )\,d\zeta \\[6pt]i^{0}\!\operatorname {erfc} (z)&=\operatorname {erfc} (z)\\i^{1}\!\operatorname {erfc} (z)&=\operatorname {ierfc} (z)={\frac {1}{\sqrt {\pi }}}e^{-z^{2}}-z\operatorname {erfc} (z)\\i^{2}\!\operatorname {erfc} (z)&={\tfrac {1}{4}}\left(\operatorname {erfc} (z)-2z\operatorname {ierfc} (z)\right)\\\end{aligned}}$

The general recurrence formula is $2n\cdot i^{n}\!\operatorname {erfc} (z)=i^{n-2}\!\operatorname {erfc} (z)-2z\cdot i^{n-1}\!\operatorname {erfc} (z)$

They have the power series $i^{n}\!\operatorname {erfc} (z)=\sum _{j=0}^{\infty }{\frac {(-z)^{j}}{2^{n-j}j!\,\Gamma \left(1+{\frac {n-j}{2}}\right)}},$ from which follow the symmetry properties $i^{2m}\!\operatorname {erfc} (-z)=-i^{2m}\!\operatorname {erfc} (z)+\sum _{q=0}^{m}{\frac {z^{2q}}{2^{2(m-q)-1}(2q)!(m-q)!}}$ and $i^{2m+1}\!\operatorname {erfc} (-z)=i^{2m+1}\!\operatorname {erfc} (z)+\sum _{q=0}^{m}{\frac {z^{2q+1}}{2^{2(m-q)-1}(2q+1)!(m-q)!}}.$

## Implementations

### As real function of a real argument

- In POSIX-compliant operating systems, the header `math.h` shall declare and the mathematical library `libm` shall provide the functions `erf` and `erfc` (double precision) as well as their single precision and extended precision counterparts `erff`, `erfl` and `erfcf`, `erfcl`.
- The GNU Scientific Library provides `erf`, `erfc`, `log(erf)`, and scaled error functions.

### As complex function of a complex argument

- `libcerf`, numeric C library for complex error functions, provides the complex functions `cerf`, `cerfc`, `cerfcx` and the real functions `erfi`, `erfcx` with approximately 13–14 digits precision, based on the Faddeeva function as implemented in the MIT Faddeeva Package
