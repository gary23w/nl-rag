---
title: "Stirling's approximation"
source: https://en.wikipedia.org/wiki/Stirling%27s_approximation
domain: gamma-beta-functions
license: CC-BY-SA-4.0
tags: gamma function, beta function, digamma function, incomplete gamma function
fetched: 2026-07-02
---

# Stirling's approximation

In mathematics, **Stirling's approximation** (or **Stirling's formula**) is an asymptotic approximation for factorials. It is a good approximation, leading to accurate results even for small values of n . It is named after James Stirling, though a related but less precise result was first stated by Abraham de Moivre.

One way of stating the approximation involves the logarithm of the factorial: $\ln n!=n\ln n-n+O(\ln n),$ where the big *O* notation means that, for all sufficiently large values of n , the difference between $\ln n!$ and $n\ln n-n$ will be at most proportional to the logarithm of n . In computer science applications such as the worst-case lower bound for comparison sorting, it is convenient to instead use the binary logarithm, giving the equivalent form $\log _{2}n!=n\log _{2}n-n\log _{2}e+O(\log _{2}n).$ The error term in either base can be expressed more precisely as ${\tfrac {1}{2}}\log(2\pi n)+O({\tfrac {1}{n}})$ , corresponding to an approximate formula for the factorial itself, $n!\sim {\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}.$ Here the sign $\sim$ means that the two quantities are asymptotic, that is, their ratio tends to 1 as n tends to infinity.

## History

The formula was first discovered by Abraham de Moivre in 1721 in the form $n!\sim [{\rm {constant}}]\cdot n^{n+{\frac {1}{2}}}e^{-n}.$

De Moivre gave an approximate rational-number expression for the natural logarithm of the constant. Stirling's contribution in 1730 consisted of showing that the constant is precisely ${\sqrt {2\pi }}$ .

## Derivation

The simplest version of Stirling's formula is $n!={\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}\left(1+O\!\left({\frac {1}{n}}\right)\right).$ It can be quickly obtained by approximating the sum $\ln n!=\sum _{j=1}^{n}\ln j$ with an integral: $\sum _{j=1}^{n}\ln j\approx \int _{1}^{n}\ln x\,{\rm {d}}x=n\ln n-n+1.$

The full formula, together with precise estimates of its error, can be derived as follows. Instead of approximating $n!$ , one considers its natural logarithm, as this is a slowly varying function: $\ln n!=\ln 1+\ln 2+\cdots +\ln n.$

The right-hand side of this equation minus ${\tfrac {1}{2}}(\ln 1+\ln n)={\tfrac {1}{2}}\ln n$ is the approximation by the trapezoid rule of the integral $\ln n!-{\tfrac {1}{2}}\ln n\approx \int _{1}^{n}\ln x\,{\rm {d}}x=n\ln n-n+1,$

and the error in this approximation is given by the Euler–Maclaurin formula: ${\begin{aligned}\ln n!-{\tfrac {1}{2}}\ln n&=\ln 1+\ln 2+\ln 3+\cdots +\ln(n-1)+{\tfrac {1}{2}}\ln n\\&=n\ln n-n+1+\sum _{k=2}^{m}{\frac {(-1)^{k}B_{k}}{k(k-1)}}\left({\frac {1}{n^{k-1}}}-1\right)+R_{m,n},\end{aligned}}$

where $B_{k}$ is a Bernoulli number, and *R**m*,*n* is the remainder term in the Euler–Maclaurin formula. Take limits to find that $\lim _{n\to \infty }\left(\ln n!-n\ln n+n-{\tfrac {1}{2}}\ln n\right)=1-\sum _{k=2}^{m}{\frac {(-1)^{k}B_{k}}{k(k-1)}}+\lim _{n\to \infty }R_{m,n}.$

Denote this limit as y . Because the remainder *R**m*,*n* in the Euler–Maclaurin formula satisfies $R_{m,n}=\lim _{n\to \infty }R_{m,n}+O\!\left({\frac {1}{n^{m}}}\right),$

where big-O notation is used, combining the equations above yields the approximation formula in its logarithmic form: $\ln n!=n\ln \left({\frac {n}{e}}\right)+{\tfrac {1}{2}}\ln n+y+\sum _{k=2}^{m}{\frac {(-1)^{k}B_{k}}{k(k-1)n^{k-1}}}+O\!\left({\frac {1}{n^{m}}}\right).$

Taking the exponential of both sides and choosing any positive integer m , one obtains a formula involving an unknown quantity $e^{y}$ . For *m* = 1, the formula is $n!=e^{y}{\sqrt {n}}\left({\frac {n}{e}}\right)^{n}\left(1+O\!\left({\frac {1}{n}}\right)\right).$

The quantity $e^{y}$ can be found by taking the limit on both sides as n tends to infinity and using Wallis' product, which shows that $e^{y}={\sqrt {2\pi }}$ . Therefore, one obtains Stirling's formula.

## Alternative derivations

An alternative formula for $n!$ using the gamma function is $n!=\int _{0}^{\infty }x^{n}e^{-x}\,{\rm {d}}x.$ (as can be seen by repeated integration by parts). Rewriting and changing variables *x* = *ny*, one obtains $n!=\int _{0}^{\infty }e^{n\ln x-x}\,{\rm {d}}x=e^{n\ln n}n\int _{0}^{\infty }e^{n(\ln y-y)}\,{\rm {d}}y.$ Applying Laplace's method one has $\int _{0}^{\infty }e^{n(\ln y-y)}\,{\rm {d}}y\sim {\sqrt {\frac {2\pi }{n}}}e^{-n},$ which recovers Stirling's formula: $n!\sim e^{n\ln n}n{\sqrt {\frac {2\pi }{n}}}e^{-n}={\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}.$

### Higher orders

Further corrections can also be obtained using Laplace's method. Stirling's formula to two orders is $n!={\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}\left(1+{\frac {1}{12n}}+O\!\left({\frac {1}{n^{2}}}\right)\right).$

From previous result, we know that $\Gamma (x)\sim x^{x}e^{-x}$ , so we "peel off" this dominant term, then perform two changes of variables, to obtain: $x^{-x}e^{x}\Gamma (x)=\int _{\mathbb {R} }e^{x\left(1+t-e^{t}\right)}\,dt$ To verify this: $\int _{\mathbb {R} }e^{x\left(1+t-e^{t}\right)}\,dt\ {\overset {t\mapsto \ln t}{=}}\ e^{x}\int _{0}^{\infty }t^{x-1}e^{-xt}\,dt\ {\overset {t\mapsto {\frac {t}{x}}}{=}}\ x^{-x}e^{x}\int _{0}^{\infty }e^{-t}t^{x-1}\,dt=x^{-x}e^{x}\Gamma (x).$

Now the function $t\mapsto 1+t-e^{t}$ is unimodal, with maximum value zero. Locally around zero, it looks like ${\textstyle -{\frac {t^{2}}{2}}}$ , which is why we are able to perform Laplace's method. In order to extend Laplace's method to higher orders, we perform another change of variables by ${\textstyle 1+t-e^{t}=-{\frac {\tau ^{2}}{2}}}$ . This equation cannot be solved in closed form, but it can be solved by serial expansion, which gives us $t=\tau -{\frac {\tau ^{2}}{6}}+{\frac {\tau ^{3}}{36}}+a_{4}\tau ^{4}+O\left(\tau ^{5}\right).$

Now plug back to the equation to obtain ${\begin{aligned}x^{-x}e^{x}\Gamma (x)&=\int _{\mathbb {R} }e^{-{\frac {x\tau ^{2}}{2}}}\left(1-{\frac {\tau }{3}}+{\frac {\tau ^{2}}{12}}+4a_{4}\tau ^{3}+O\left(\tau ^{4}\right)\right)\,d\tau \\&={\sqrt {2\pi }}\left(x^{-{\frac {1}{2}}}+{\frac {x^{-{\frac {3}{2}}}}{12}}\right)+O\left(x^{-{\frac {5}{2}}}\right).\end{aligned}}$

Notice how it is not actually necessary to find $a_{4}$ , since it is cancelled out by the integral. Higher orders can be achieved by computing more terms in $t=\tau +\cdots$ , which can be obtained programmatically.

### Complex-analytic version

A complex-analysis version of this method is to consider ${\textstyle {\frac {1}{n!}}}$ as a Taylor coefficient of the exponential function $e^{z}=\sum _{n=0}^{\infty }{\frac {z^{n}}{n!}},$ computed by Cauchy's integral formula as ${\frac {1}{n!}}={\frac {1}{2\pi i}}\oint \limits _{|z|=r}{\frac {e^{z}}{z^{n+1}}}\,dz.$

This line integral can then be approximated using the saddle-point method with an appropriate choice of contour radius $r=r_{n}$ . The dominant portion of the integral near the saddle point is then approximated by a real integral and Laplace's method, while the remaining portion of the integral can be bounded above to give an error term.

### Using the Central Limit Theorem and the Poisson distribution

An alternative version uses the fact that the Poisson distribution converges to a normal distribution by the Central Limit Theorem.

Since the Poisson distribution with parameter $\mu$ converges to a normal distribution with mean $\mu$ and variance $\mu$ , their density functions will be approximately the same:

${\frac {\exp(-\mu )\mu ^{x}}{x!}}\approx {\frac {1}{\sqrt {2\pi \mu }}}\exp \left(-{\frac {1}{2}}\left({\frac {x-\mu }{\sqrt {\mu }}}\right)^{2}\right)$

Evaluating this expression at the mean, at which the approximation is particularly accurate, simplifies this expression to:

${\frac {\exp(-\mu )\mu ^{\mu }}{\mu !}}\approx {\frac {1}{\sqrt {2\pi \mu }}}$

Taking logs then results in

$-\mu +\mu \ln \mu -\ln \mu !\approx -{\frac {1}{2}}\ln(2\pi \mu )$

which can easily be rearranged to give:

$\ln \mu !\approx \mu \ln \mu -\mu +{\frac {1}{2}}\ln(2\pi \mu )$

Evaluating at $\mu =n$ gives the usual, more precise form of Stirling's approximation.

## Speed of convergence and error estimates

Stirling's formula is in fact the first approximation to the following series (now called the **Stirling series**): $n!\sim {\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}\left(1+{\frac {1}{12n}}+{\frac {1}{288n^{2}}}-{\frac {139}{51840n^{3}}}-{\frac {571}{2488320n^{4}}}+{\frac {163879}{209018880n^{5}}}-\cdots \right).$

An explicit formula for the coefficients in this series was given by G. Nemes. Further terms are listed in the On-Line Encyclopedia of Integer Sequences as A001163 and A001164. The first graph in this section shows the relative error vs. n , for 1 through all 5 terms listed above. The coefficients have the following asymptotic formula: $A_{2j+1}\sim {\frac {(-1)^{j}2(2j)!}{(2\pi )^{2(j+1)}}}$ which shows that it grows superexponentially, and that by the ratio test the radius of convergence is zero.

However, the representation obtained directly from the Euler–Maclaurin approximation, in which the correction term itself is the argument of the exponential function, converges much faster (needs half the number of correction terms for the same accuracy): $n!\sim {\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}\exp {\bigg (}{\frac {1}{12n}}-{\frac {1}{360n^{3}}}+{\frac {1}{1260n^{5}}}-{\frac {1}{1680n^{7}}}+{\frac {1}{1188n^{9}}}-\cdots {\bigg )}.$ The k th coefficient (for the reciprocal of the $\left(2k-1\right)$ th power of n ) is directly calculated using Bernoulli numbers and $c_{k}={\tfrac {B_{2k}}{2k(2k-1)}}.$

As *n* → ∞, the error in the truncated series is asymptotically equal to the first omitted term. This is an example of an asymptotic expansion. It is not a convergent series; for any *particular* value of n there are only so many terms of the series that improve accuracy, after which accuracy worsens. This is shown in the next graph, which shows the relative error versus the number of terms in the series, for larger numbers of terms. More precisely, let *St*(*n*) be the Stirling series to t terms evaluated at  n . The graphs show $\left|\ln {\frac {S_{t}(n)}{n!}}\right|,$ which, when small, is essentially the relative error.

Writing Stirling's series in the form $\ln n!\sim n\ln n-n+{\tfrac {1}{2}}\ln(2\pi n)+{\frac {1}{12n}}-{\frac {1}{360n^{3}}}+{\frac {1}{1260n^{5}}}-{\frac {1}{1680n^{7}}}+\cdots ,$ it is known that the error in truncating the series is always of the opposite sign and at most the same magnitude as the first omitted term.

Other bounds, due to Robbins, valid for all positive integers n are ${\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}e^{\frac {1}{12n+1}}<n!<{\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}e^{\frac {1}{12n}}.$ This upper bound corresponds to stopping the above series for $\ln n!$ after the ${\tfrac {1}{n}}$ term. The lower bound is weaker than that obtained by stopping the series after the ${\tfrac {1}{n^{3}}}$ term. A looser version of this bound is that ${\frac {n!e^{n}}{n^{n+{\tfrac {1}{2}}}}}\in \left({\sqrt {2\pi }},e\right]\quad {\text{for all }}n\geq 1.$

## Stirling's formula for the gamma function

For all positive integers, $n!=\Gamma (n+1),$ where Γ denotes the gamma function.

However, the gamma function, unlike the factorial, is more broadly defined for all complex numbers other than non-positive integers; nevertheless, Stirling's formula may still be applied. If Re(*z*) > 0, then $\ln \Gamma (z)=z\ln z-z+{\tfrac {1}{2}}\ln {\frac {2\pi }{z}}+\int _{0}^{\infty }{\frac {2\arctan \left({\frac {t}{z}}\right)}{e^{2\pi t}-1}}\,dt.$

Repeated integration by parts gives ${\begin{aligned}ln\Gamma (z)&\sim z\ln z-z+{\tfrac {1}{2}}\ln {\frac {2\pi }{z}}+\sum _{n=1}^{N-1}{\frac {B_{2n}}{2n(2n-1)z^{2n-1}}}\\&=z\ln z-z+{\tfrac {1}{2}}\ln {\frac {2\pi }{z}}+{\frac {1}{12z}}-{\frac {1}{360z^{3}}}+{\frac {1}{1260z^{5}}}+\dots ,\end{aligned}}$

where $B_{n}$ is the nth Bernoulli number (note that the limit of the sum as $N\to \infty$ is not convergent, so this formula is just an asymptotic expansion). The formula is valid for z large enough in absolute value, when |arg(*z*)| < *π* − *ε*, where ε is positive, with an error term of *O*(*z*−2*N*+ 1). The corresponding approximation may now be written: $\Gamma (z)={\sqrt {\frac {2\pi }{z}}}{\left({\frac {z}{e}}\right)}^{z}\left(1+O\left({\frac {1}{z}}\right)\right).$

where the expansion is identical to that of Stirling's series above for $n!$ , except that n is replaced with *z* − 1.

A further application of this asymptotic expansion is for complex argument z with constant Re(*z*). See for example the Stirling formula applied in Im(*z*) = *t* of the Riemann–Siegel theta function on the straight line ⁠1/4⁠ + *it*.

## A convergent version of Stirling's formula

Thomas Bayes showed, in a letter to John Canton published by the Royal Society in 1763, that Stirling's formula did not give a convergent series. Obtaining a convergent version of Stirling's formula entails evaluating Binet's formula: $\int _{0}^{\infty }{\frac {2\arctan \left({\frac {t}{x}}\right)}{e^{2\pi t}-1}}\,{\rm {d}}t=\ln \Gamma (x)-x\ln x+x-{\tfrac {1}{2}}\ln {\frac {2\pi }{x}}.$

One way to do this is by means of a convergent series of inverted rising factorials. If $z^{\bar {n}}=z(z+1)\cdots (z+n-1),$ then $\int _{0}^{\infty }{\frac {2\arctan \left({\frac {t}{x}}\right)}{e^{2\pi t}-1}}\,{\rm {d}}t=\sum _{n=1}^{\infty }{\frac {c_{n}}{(x+1)^{\bar {n}}}},$ where $c_{n}={\frac {1}{n}}\int _{0}^{1}x^{\bar {n}}\left(x-{\tfrac {1}{2}}\right)\,{\rm {d}}x={\frac {1}{2n}}\sum _{k=1}^{n}{\frac {k|s(n,k)|}{(k+1)(k+2)}},$ where *s*(*n*, *k*) denotes the Stirling numbers of the first kind. From this one obtains a version of Stirling's series ${\begin{aligned}\ln \Gamma (x)&=x\ln x-x+{\tfrac {1}{2}}\ln {\frac {2\pi }{x}}+{\frac {1}{12(x+1)}}+{\frac {1}{12(x+1)(x+2)}}\\&\quad +{\frac {59}{360(x+1)(x+2)(x+3)}}+{\frac {29}{60(x+1)(x+2)(x+3)(x+4)}}+\cdots ,\end{aligned}}$ which converges when Re(*x*) > 0. Stirling's formula may also be given in convergent form as $\Gamma (x)={\sqrt {2\pi }}x^{x-{\frac {1}{2}}}e^{-x+\mu (x)}$ where $\mu \left(x\right)=\sum _{n=0}^{\infty }\left(\left(x+n+{\frac {1}{2}}\right)\ln \left(1+{\frac {1}{x+n}}\right)-1\right).$

## Versions suitable for calculators

The approximation $\Gamma (z)\approx {\sqrt {\frac {2\pi }{z}}}\left({\frac {z}{e}}{\sqrt {z\sinh {\frac {1}{z}}+{\frac {1}{810z^{6}}}}}\right)^{z}$ and its equivalent form $2\ln \Gamma (z)\approx \ln(2\pi )-\ln z+z\left(2\ln z+\ln \left(z\sinh {\frac {1}{z}}+{\frac {1}{810z^{6}}}\right)-2\right)$ can be obtained by rearranging Stirling's extended formula and observing a coincidence between the resultant power series and the Taylor series expansion of the hyperbolic sine function. This approximation is good to more than 8 decimal digits for z with a real part greater than 8. Robert H. Windschitl suggested it in 2002 for computing the gamma function with fair accuracy on calculators with limited program or register memory.

Gergő Nemes proposed in 2007 an approximation which gives the same number of exact digits as the Windschitl approximation but is much simpler: $\Gamma (z)\approx {\sqrt {\frac {2\pi }{z}}}\left({\frac {1}{e}}\left(z+{\frac {1}{12z-{\frac {1}{10z}}}}\right)\right)^{z},$ or equivalently, $\ln \Gamma (z)\approx {\tfrac {1}{2}}\left(\ln(2\pi )-\ln z\right)+z\left(\ln \left(z+{\frac {1}{12z-{\frac {1}{10z}}}}\right)-1\right).$

An alternative approximation for the gamma function stated by Srinivasa Ramanujan in Ramanujan's lost notebook is $\Gamma (1+x)\approx {\sqrt {\pi }}\left({\frac {x}{e}}\right)^{x}\left(8x^{3}+4x^{2}+x+{\tfrac {1}{30}}\right)^{\frac {1}{6}}$ for *x* ≥ 0. The equivalent approximation for ln *n*! has an asymptotic error of ⁠1/1400*n*3⁠ and is given by $\ln n!\approx n\ln n-n+{\tfrac {1}{6}}\ln \left(8n^{3}+4n^{2}+n+{\tfrac {1}{30}}\right)+{\tfrac {1}{2}}\ln \pi .$

The approximation may be made precise by giving paired upper and lower bounds; one such inequality is ${\sqrt {\pi }}\left({\frac {x}{e}}\right)^{x}\left(8x^{3}+4x^{2}+x+{\tfrac {1}{100}}\right)^{\frac {1}{6}}<\Gamma (1+x)<{\sqrt {\pi }}\left({\frac {x}{e}}\right)^{x}\left(8x^{3}+4x^{2}+x+{\tfrac {1}{30}}\right)^{\frac {1}{6}}.$

## Equation for discrete cases

For discrete cases, rather than the asymptotic formula described above, a more accurate equation, and much easier to prove result has been derived by T. S. Nanjundiah:

$n!={\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}e^{\frac {\theta _{n}}{12n}},\theta _{n}\in [0,1]$

or further, we can deduce that:

$n!={\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}\cdot \exp \left({{\frac {1}{12n}}-{\frac {\theta _{n}'}{360n^{3}}}}\right)\quad (\theta _{n}'\in (0,1))$

To prove this, we first assume that:

$a_{n}=n!\cdot n^{-\left(n+{\frac {1}{2}}\right)}\cdot e^{n}\qquad l_{n}=\ln a_{n}$

It is easy to calculate that:

${\frac {a_{n}}{a_{n+1}}}={\frac {n!\cdot n^{-\left(n+{\frac {1}{2}}\right)}\cdot e^{n}}{(n+1)!\cdot (n+1)^{-\left(n+{\frac {3}{2}}\right)}\cdot e^{n+1}}}={\frac {1}{e}}\left({\frac {n+1}{n}}\right)^{n+{\frac {1}{2}}}$

$\implies l_{n}-l_{n+1}=\left(n+{\frac {1}{2}}\right)\ln \left(1+{\frac {1}{n}}\right)-1$

and, by combining the Taylor's series of logarithms:

$\ln(1+x)=x-{\frac {x^{2}}{2}}+{\frac {x^{3}}{3}}-{\frac {x^{4}}{4}}+{\frac {x^{5}}{5}}-\dots \qquad \ln(1-x)=-x-{\frac {x^{2}}{2}}-{\frac {x^{3}}{3}}-{\frac {x^{4}}{4}}-{\frac {x^{5}}{5}}-\dots$

subtracting them,

$\ln \left({\frac {1+x}{1-x}}\right)=2\left(x+{\frac {x^{3}}{3}}+{\frac {x^{5}}{5}}+\dots \right)$

let the two variables be equal,

${\frac {1+x}{1-x}}={\frac {n+1}{n}}\implies x={\frac {1}{2n+1}}$

replacing x with n, we get:

$\ln \left(1+{\frac {1}{n}}\right)=2\cdot {\frac {1}{2n+1}}\left[1+{\frac {1}{3}}\left({\frac {1}{2n+1}}\right)^{2}+{\frac {1}{5}}\left({\frac {1}{2n+1}}\right)^{4}+\dots \right]$

thus, for $l_{n}$ we have that:

$l_{n}-l_{n+1}={\frac {1}{3(2n+1)^{2}}}+{\frac {1}{5(2n+1)^{4}}}+\dots$

To calculate the sum, we force them to be a geometric series:

$l_{n}-l_{n+1}<{\frac {1}{3(2n+1)^{2}}}\sum _{k=0}^{\infty }\left[{\frac {1}{(2n+1)^{2}}}\right]^{k}={\frac {1}{3(2n+1)^{2}}}\cdot {\frac {1}{1-{\frac {1}{(2n+1)^{2}}}}}={\frac {1}{12n(n+1)}}$

and, it is also evident that ${\textstyle l_{n}-l_{n+1}>0}$ ,

$\implies l_{n}-{\frac {1}{12n}}<l_{n+1}-{\frac {1}{12(n+1)}}$

we can let ${\textstyle x_{n}=l_{n}-{\frac {1}{12n}}}$ , thus we have that

$x_{n}<x_{n+1},l_{n}<l_{n+1},\quad \forall n,x_{n}<l_{n},$

according to monotone convergence theorem, we know that $l_{n}$ is convergent, we assume that $\lim _{n\rightarrow +\infty }l_{n}=\lambda$

then $\lim _{n\rightarrow +\infty }a_{n}=e^{\lambda }=\alpha ,$

${\begin{aligned}\alpha &=\lim _{n\to +\infty }{\frac {a_{n}^{2}}{a_{2n}}}\\&=\lim _{n\to +\infty }{\frac {(n!)^{2}\cdot n^{-2n-1}\cdot e^{2n}}{(2n)!\cdot (2n)^{-2n-{\frac {1}{2}}}\cdot e^{2n}}}\\&=\lim _{n\to +\infty }{\frac {(n!)^{2}\cdot 2^{2n+{\frac {1}{2}}}\cdot n^{2n+{\frac {1}{2}}}}{(2n)!\cdot n^{2n+1}}}\\&=\lim _{n\to +\infty }{\frac {2^{2n}(n!)^{2}}{(2n)!}}{\sqrt {\frac {2}{n}}}\\&=\lim _{n\to +\infty }{\sqrt {\frac {2}{n}}}{\frac {(2n)!!}{(2n-1)!!}}\end{aligned}}$

combined with Wallis Formula, we can finally derive that the limit is ${\sqrt {2\pi }}$ , which finalize our proof of the asymptotic case.

And notice that for every n, we have that ${\textstyle l_{n}-{\frac {1}{12n}}<\lambda <l_{n}}$ , rewrite the formula by substituting λ with ${\textstyle l_{n}\implies l_{n}=\lambda +{\frac {\theta _{n}}{12n}}}$ , we get:

$n!={\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}e^{\frac {\theta _{n}}{12n}}$

and, if we further elaborate on the inequality we used, by keeping the first term as original and using another geometric series with ration ${\textstyle {\frac {1}{3(2n+1)^{2}}}}$ , we have:

${\begin{aligned}l_{n}-l_{n+1}&>{\frac {1}{3(2n+1)^{2}}}\left(1-{\frac {1}{3(2n+1)^{2}}}\right)^{-1}+\left({\frac {1}{5}}-{\frac {1}{3^{2}}}\right){\frac {1}{(2n+1)^{4}}}\\&={\frac {1}{12n(n+1)}}\left(1+{\frac {1}{6n(n+1)}}\right)^{-1}+{\frac {1}{180n^{2}(n+1)^{2}}}\left(1+{\frac {1}{4n(n+1)}}\right)^{-2}\\&>{\frac {1}{12n(n+1)}}\left(1-{\frac {1}{6n(n+1)}}\right)+{\frac {1}{180n^{2}(n+1)^{2}}}\left(1-{\frac {1}{2n(n+1)}}\right)={\frac {1}{12n(n+1)}}-{\frac {3n(n+1)+1}{360n^{3}(n+1)^{3}}}\end{aligned}}$ Here, we can derive that:

$l_{n}-{\frac {1}{12n}}+{\frac {1}{360n^{3}}}>l_{n+1}-{\frac {1}{12(n+1)}}+{\frac {1}{360(n+1)^{3}}}$

since it is trivial that $l_{n}-{\frac {1}{12n}}<l_{n}-{\frac {1}{12n}}+{\frac {1}{360n^{3}}}<l_{n},$ and $\lim _{n\rightarrow +\infty }{\frac {1}{12n}}=\lim _{n\rightarrow +\infty }{\frac {1}{360n^{3}}}=0$

we know that: $l_{n}-{\frac {1}{12n}}<\lambda <l_{n}-{\frac {1}{12n}}+{\frac {1}{360n^{3}}},$ and rewrite the equation above using ${\textstyle l_{n}=\lambda +{\frac {1}{12n}}-{\frac {\theta _{n}}{360n^{3}}}}$ , finally we prove that:

$n!={\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}\exp \left({\frac {1}{12n}}-{\frac {\theta _{n}}{360n^{3}}}\right)$
