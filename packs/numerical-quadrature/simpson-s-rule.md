---
title: "Simpson's rule"
source: https://en.wikipedia.org/wiki/Simpson%27s_rule
domain: numerical-quadrature
license: CC-BY-SA-4.0
tags: numerical integration, simpson's rule, romberg method, adaptive quadrature
fetched: 2026-07-02
---

# Simpson's rule

In numerical integration, **Simpson's rules** are several approximations for definite integrals, named after Thomas Simpson (1710–1761).

The most basic of these rules, called **Simpson's 1/3 rule**, or just **Simpson's rule**, reads $\int _{a}^{b}f(x)\,dx\approx {\frac {b-a}{6}}\left[f(a)+4f\left({\frac {a+b}{2}}\right)+f(b)\right].$

In German and some other languages, it is named after Johannes Kepler, who derived it in 1615 after seeing it used for wine barrels (barrel rule, *Keplersche Fassregel*). The approximate equality in the rule becomes exact if *f* is a polynomial up to and including 3rd degree.

If the 1/3 rule is applied to *n* equal subdivisions of the integration range [*a*, *b*], one obtains the **composite Simpson's 1/3 rule**. Points inside the integration range are given alternating weights 4/3 and 2/3.

**Simpson's 3/8 rule**, also called **Simpson's second rule**, requires one more function evaluation inside the integration range and gives lower error bounds, but does not improve the order of the error.

If the 3/8 rule is applied to *n* equal subdivisions of the integration range [*a*, *b*], one obtains the **composite Simpson's 3/8 rule**.

Simpson's 1/3 and 3/8 rules are two special cases of closed Newton–Cotes formulas.

In naval architecture and ship stability estimation, there also exists *Simpson's third rule*, which has no special importance in general numerical analysis, see Simpson's rules (ship stability).

## Simpson's 1/3 rule

Simpson's 1/3 rule, also simply called Simpson's rule, is a method for numerical integration proposed by Thomas Simpson. It is based upon a quadratic interpolation and is the **composite Simpson's 1/3 rule** evaluated for $n=2$ . Simpson's 1/3 rule is as follows: ${\begin{aligned}\int _{a}^{b}f(x)\,dx&\approx {\frac {b-a}{6}}\left[f(a)+4f\left({\frac {a+b}{2}}\right)+f(b)\right]\\&={\frac {1}{3}}h\left[f(a)+4f\left(a+h\right)+f(b)\right],\end{aligned}}$ where $h=(b-a)/n$ is the step size for $n=2$ .

The error in approximating an integral by Simpson's rule for $n=2$ is $-{\frac {1}{90}}h^{5}f^{(4)}(\xi )=-{\frac {(b-a)^{5}}{2880}}f^{(4)}(\xi ),$ where $\xi$ (the Greek letter xi) is some number between a and b .

The error is asymptotically proportional to $(b-a)^{5}$ . However, the above derivations suggest an error proportional to $(b-a)^{4}$ . Simpson's rule gains an extra order because the points at which the integrand is evaluated are distributed symmetrically in the interval $[a,\ b]$ .

Since the error term is proportional to the fourth derivative of f at $\xi$ , this shows that Simpson's rule provides exact results for any polynomial f of degree three or less, since the fourth derivative of such a polynomial is zero at all points. Another way to see this result is to note that any interpolating cubic polynomial can be expressed as the sum of the unique interpolating quadratic polynomial plus an arbitrarily scaled cubic polynomial that vanishes at all three points in the interval, and the integral of this second term vanishes because it is odd within the interval.

If the second derivative $f''$ exists and is convex in the interval $(a,\ b)$ , then $(b-a)f\left({\frac {a+b}{2}}\right)+{\frac {1}{3}}\left({\frac {b-a}{2}}\right)^{3}f''\left({\frac {a+b}{2}}\right)\leq \int _{a}^{b}f(x)\,dx\leq {\frac {b-a}{6}}\left[f(a)+4f\left({\frac {a+b}{2}}\right)+f(b)\right].$

### Derivations

#### Quadratic interpolation

Consider finding the area under a general parabola $y=ax^{2}+bx+c$ between $x=-h$ and $x=h$ for some positive number h . The midpoint of this interval is therefore at $x=0$ .

The area under the parabola, A , is therefore

${\begin{aligned}A=\int _{-h}^{h}ax^{2}+bx+c\,dx&=\left[{\frac {ax^{3}}{3}}+{\frac {bx^{2}}{2}}+cx\right]_{x=-h}^{x=h}\\&=\left({\frac {ah^{3}}{3}}+{\frac {bh^{2}}{2}}+ch\right)-\left(-{\frac {ah^{3}}{3}}+{\frac {bh^{2}}{2}}-ch\right)\\&={\frac {2ah^{3}}{3}}+2ch\\&={\frac {h}{3}}\left(2ah^{2}+6c\right).\end{aligned}}$

Assuming the parabola has midpoint $(0,y_{1})$ and endpoints $(-h,y_{0})$ and $(h,y_{2})$ , substituting these three points into the parabola formula gives

$y_{0}=ah^{2}-bh+c$ $y_{1}=c$ $y_{2}=ah^{2}+bh+c.$

Solving these gives

$c=y_{1}$

from the second equation, and

$2ah^{2}=y_{0}-2y_{1}+y_{2}$

by adding the first and third equations. Substituting this into the expression for A gives

${\begin{aligned}A&={\frac {h}{3}}\left(2ah^{2}+6c\right)\\&={\frac {h}{3}}\left(y_{0}-2y_{1}+y_{2}+6y_{1}\right)\\&={\frac {h}{3}}\left(y_{0}+4y_{1}+y_{2}\right).\end{aligned}}$

Simpsons 1/3 rule approximates a definite integral over an interval [a, b] by replacing the integrand with a parabola which interpolates the function at $x=a$ , $x=b$ and the midpoint of the interval, which gives

$\int _{a}^{b}f(x)\,dx\approx A={\frac {1}{3}}h\left[f(a)+4f(a+h)+f(b)\right].$ Because of the $1/3$ factor, Simpson's rule is also referred to as "Simpson's 1/3 rule" (see below for generalization).

#### Averaging the midpoint and the trapezoidal rules

Another derivation constructs Simpson's rule from two simpler approximations. For functions that behave like polynomials over the interval $[a,b]$ , the midpoint rule says $M=(b-a)f\left({\frac {a+b}{2}}\right)=\int _{a}^{b}f(x)dx-{\frac {1}{24}}(b-a)^{3}f''(a)+O{\big (}(b-a)^{4}{\big )}$ and the trapezoidal rule says $T=(b-a)\left({\frac {f(a)+f(b)}{2}}\right)=\int _{a}^{b}f(x)dx+{\frac {1}{12}}(b-a)^{3}f''(a)+O{\big (}(b-a)^{4}{\big )},$ where $O{\big (}(b-a)^{4}{\big )}$ denotes a term asymptotically proportional to $(b-a)^{4}$ . The two $O{\big (}(b-a)^{4}{\big )}$ terms are not equal; see Big O notation for more details. It follows from the above formulas that the leading error term vanishes if we take the weighted average ${\frac {2M+T}{3}}=\int _{a}^{b}f(x)\,dx+O((b-a)^{4}).$ This weighted average is exactly Simpson's rule.

Using another approximation (for example, the trapezoidal rule with twice as many points), it is possible to take a suitable weighted average and eliminate another error term. This is Romberg's method.

#### Undetermined coefficients

The third derivation starts from the *ansatz* ${\frac {1}{b-a}}\int _{a}^{b}f(x)\,dx\approx \alpha f(a)+\beta f\left({\frac {a+b}{2}}\right)+\gamma f(b).$

The coefficients α, β and γ can be fixed by requiring that this approximation be exact for all quadratic polynomials. This yields Simpson's rule. (This derivation is essentially a less rigorous version of the quadratic interpolation derivation, where one saves significant calculation effort by guessing the correct functional form.)

### Composite Simpson's 1/3 rule

If the interval of integration $[a,b]$ is in some sense "small", then Simpson's rule with $n=2$ subintervals will provide an adequate approximation to the exact integral. By "small" we mean that the function being integrated is relatively smooth over the interval $[a,b]$ . For such a function, a smooth quadratic interpolant like the one used in Simpson's rule will give good results.

However, it is often the case that the function we are trying to integrate is not smooth over the interval. Typically, this means that either the function is highly oscillatory or lacks derivatives at certain points. In these cases, Simpson's rule may give very poor results. One common way of handling this problem is by breaking up the interval $[a,b]$ into $n>2$ small subintervals. Simpson's rule is then applied to each subinterval, with the results being summed to produce an approximation for the integral over the entire interval. This sort of approach is termed the *composite Simpson's 1/3 rule*, or just *composite Simpson's rule*.

Suppose that the interval $[a,b]$ is split up into n subintervals, with n an even number. Then, the composite Simpson's rule is given by

Dividing the interval $[a,b]$ into n subintervals of length $h=(b-a)/n$ and introducing the points $x_{i}=a+ih$ for $0\leq i\leq n$ (in particular, $x_{0}=a$ and $x_{n}=b$ ), we have ${\begin{aligned}\int _{a}^{b}f(x)\,dx&\approx {\frac {1}{3}}h\sum _{i=1}^{n/2}{\big [}f(x_{2i-2})+4f(x_{2i-1})+f(x_{2i}){\big ]}\\&={\frac {1}{3}}h{\big [}f(x_{0})+4f(x_{1})+2f(x_{2})+4f(x_{3})+2f(x_{4})+\dots +2f(x_{n-2})+4f(x_{n-1})+f(x_{n}){\big ]}\\&={\frac {1}{3}}h\left[f(x_{0})+4\sum _{i=1}^{n/2}f(x_{2i-1})+2\sum _{i=1}^{n/2-1}f(x_{2i})+f(x_{n})\right].\end{aligned}}$ This composite rule with $n=2$ corresponds with the regular Simpson's rule of the preceding section.

The error committed by the composite Simpson's rule is $-{\frac {1}{180}}h^{4}(b-a)f^{(4)}(\xi ),$ where $\xi$ is some number between a and b , and $h=(b-a)/n$ is the "step length". The error is bounded (in absolute value) by ${\frac {1}{180}}h^{4}(b-a)\max _{\xi \in [a,b]}\left|f^{(4)}(\xi )\right|.$

This formulation splits the interval $[a,b]$ in subintervals of equal length. In practice, it is often advantageous to use subintervals of different lengths and concentrate the efforts on the places where the integrand is less well-behaved. This leads to the adaptive Simpson's method.

### Examples

#### Approximating the natural logarithm of 2

Since

$\int _{1}^{2}{\frac {1}{x}}\,dx=\ln(2)-\ln(1)=\ln(2),$

approximations of $\ln(2)$ can be generated by approximating this integral. Applying Composite Simpson's 1/3 rule with $n=6$ intervals gives ${\begin{aligned}\ln(2)=\int _{1}^{2}{\frac {1}{x}}\,dx&\approx {\frac {1}{18}}\left(\ 1+{\frac {24}{7}}+{\frac {3}{2}}+{\frac {8}{3}}+{\frac {6}{5}}+{\frac {24}{11}}+{\frac {1}{2}}\right)\\&\approx 0.69316,\end{aligned}}$

which has a relative error of about $0.003\%$ .

#### An application to statistics

In statistics, when data tends around a central value with no left or right bias, it's said to be normally distributed. In the case where the mean is zero and the standard deviation is 1, the curve is said to follow the **standard normal** (or **standard Gaussian**) distribution. The equation of this distribution is

$f(x)={\frac {1}{\sqrt {2\pi }}}\exp \left({\frac {-x^{2}}{2}}\right).$

By the 68–95–99.7 rule, approximately 68.27% of values are within a single standard deviation of the mean, so

$\int _{-1}^{1}{\frac {1}{\sqrt {2\pi }}}\exp \left({\frac {-x^{2}}{2}}\right)dx\approx 0.6827.$

This result can be verified with Composite Simpson's 1/3 rule - applying the rule with $n=6$ intervals gives ${\begin{aligned}\int _{-1}^{1}{\frac {1}{\sqrt {2\pi }}}\exp \left({\frac {-x^{2}}{2}}\right)\,dx&\approx {\frac {1}{\sqrt {2\pi }}}\times {\frac {1}{9}}\left(\ {\frac {1}{e^{\frac {1}{2}}}}+{\frac {4}{e^{\frac {2}{9}}}}+{\frac {2}{e^{\frac {1}{18}}}}+{\frac {4}{1}}+{\frac {2}{e^{\frac {1}{18}}}}+{\frac {4}{e^{\frac {2}{9}}}}+{\frac {1}{e^{\frac {1}{2}}}}\right)\\&\approx {\frac {1}{\sqrt {2\pi }}}\times 1.71142\\&\approx 0.6827,\end{aligned}}$

as expected.

Similarly, the 68–95–99.7 rule says approximately 95.45% of values are within two standard deviations of the mean, so

$\int _{-2}^{2}{\frac {1}{\sqrt {2\pi }}}\exp \left({\frac {-x^{2}}{2}}\right)dx\approx 0.9545.$

As before, this result can be verified with Composite Simpson's 1/3 rule - applying the rule with $n=6$ intervals gives ${\begin{aligned}\int _{-2}^{2}{\frac {1}{\sqrt {2\pi }}}\exp \left({\frac {-x^{2}}{2}}\right)\,dx&\approx {\frac {1}{\sqrt {2\pi }}}\times {\frac {2}{9}}\left(\ {\frac {1}{e^{2}}}+{\frac {4}{e^{\frac {8}{9}}}}+{\frac {2}{e^{\frac {2}{9}}}}+{\frac {4}{1}}+{\frac {2}{e^{\frac {2}{9}}}}+{\frac {4}{e^{\frac {8}{9}}}}+{\frac {1}{e^{2}}}\right)\\&\approx {\frac {1}{\sqrt {2\pi }}}\times 2.39167\\&\approx 0.9541,\end{aligned}}$

which has a relative error of about $0.0419\%$ . The interval of integration can be shortened (thereby reducing discretization error) by noting that the integrand is an even function, so

$\int _{-2}^{2}{\frac {1}{\sqrt {2\pi }}}\exp \left({\frac {-x^{2}}{2}}\right)\,dx=2\int _{0}^{2}{\frac {1}{\sqrt {2\pi }}}\exp \left({\frac {-x^{2}}{2}}\right)\,dx.$

Once again, applying Composite Simpson's 1/3 rule with $n=6$ intervals gives ${\begin{aligned}2\int _{0}^{2}{\frac {1}{\sqrt {2\pi }}}\exp \left({\frac {-x^{2}}{2}}\right)\,dx&\approx {\frac {2}{\sqrt {2\pi }}}\times {\frac {1}{9}}\left(\ 1+{\frac {4}{e^{\frac {1}{18}}}}+{\frac {2}{e^{\frac {2}{9}}}}+{\frac {4}{e^{\frac {1}{2}}}}+{\frac {2}{e^{\frac {8}{9}}}}+{\frac {4}{e^{\frac {25}{18}}}}+{\frac {1}{e^{2}}}\right)\\&\approx {\frac {2}{\sqrt {2\pi }}}\times 1.19626\\&\approx 0.9544,\end{aligned}}$

which has an improved relative error of about $0.0104\%$ but with the same number of intervals.

#### Approximating π

Since

$\int _{0}^{1}{\frac {1}{1+x^{2}}}\,dx=\arctan(1)-\arctan(0)={\frac {\pi }{4}},$

this can be rearranged to give

$\pi =4\int _{0}^{1}{\frac {1}{1+x^{2}}}\,dx.$

Therefore, approximations of $\pi$ can be generated by approximating this integral. Applying Composite Simpson's 1/3 rule with $n=6$ intervals gives ${\begin{aligned}\pi =4\int _{0}^{1}{\frac {1}{1+x^{2}}}\,dx&\approx {\frac {2}{9}}\left(\ 1+{\frac {144}{37}}+{\frac {9}{5}}+{\frac {16}{5}}+{\frac {18}{13}}+{\frac {144}{61}}+{\frac {1}{2}}\right)\\&\approx 3.141591,\end{aligned}}$

which remarkably only has a relative error of about $0.00002\%$ .

#### Determining the number of intervals for a desired accuracy

Suppose we wish to determine the number of intervals required to approximate $\int _{0}^{\pi }\sin(x)\,dx$ with an absolute error of less than $0.00001$ . The error term in Composite Simpson's 1/3 rule is

$-{\frac {\pi h^{4}}{180}}\sin(\xi )$

for some $\xi$ between 0 and $\pi$ . Since the absolute error is to be less than $0.00001$ , we can calculate

$\left|{\frac {\pi h^{4}}{180}}\sin(\xi )\right|\leq {\frac {\pi h^{4}}{180}}={\frac {\pi ^{5}}{180n^{4}}}<0.00001$

which gives

$n>{\sqrt[{4}]{\frac {\pi ^{5}}{0.0018}}}\approx 20.3,$

so $n=22$ will generate the required accuracy.

For comparison purposes, suppose we wish to be assured of this degree of accuracy using the Composite Trapezoidal Rule. In this case, the error term is

$-{\frac {\pi h^{2}}{12}}\sin(\xi )$

for some $\xi$ between 0 and $\pi$ . Since the absolute error is to be less than $0.00001$ , we can calculate

$\left|{\frac {\pi h^{2}}{12}}\sin(\xi )\right|\leq {\frac {\pi h^{2}}{12}}={\frac {\pi ^{3}}{12n^{2}}}<0.00001$

which gives

$n>{\sqrt {\frac {\pi ^{3}}{0.00012}}}\approx 508.3,$

so $n=509$ will guarantee the required accuracy. This is significantly more calculations compared to Composite Simpson's 1/3 rule.

## Simpson's 3/8 rule

Simpson's 3/8 rule, also called Simpson's second rule, is another method for numerical integration proposed by Thomas Simpson. It is based upon a cubic interpolation rather than a quadratic interpolation.

Consider finding the area, A , under a general cubic $y=ax^{3}+bx^{2}+cx+d$ between $x=-h$ and $x=2h$ for some positive number h . This is given by

${\begin{aligned}A&=\int _{-h}^{2h}\left(ax^{3}+bx^{2}+cx+d\right)\,dx\\[1ex]&=\left[{\frac {1}{4}}ax^{4}+{\frac {1}{3}}bx^{3}+{\frac {1}{2}}cx^{2}+dx\right]_{x=-h}^{x=2h}\\[1ex]&=\left(4ah^{4}+{\frac {8}{3}}bh^{3}+2ch^{2}+2dh\right)-\left({\frac {1}{4}}ah^{4}-{\frac {1}{3}}bh^{3}+{\frac {1}{2}}ch^{2}-dh\right)\\[1ex]&={\frac {15}{4}}ah^{4}+3bh^{3}+{\frac {3}{2}}ch^{2}+3dh\\[1ex]&={\frac {3h}{8}}\left[10ah^{3}+8bh^{2}+4ch+8d\right].\end{aligned}}$

Assuming four equally spaced points over the interval of integration are $(-h,y_{0})$ , $(0,y_{1})$ , $(h,y_{2})$ and $(2h,y_{3})$ , substituting these four points into the cubic formula gives

$y_{0}=-ah^{3}+bh^{2}-ch+d$ $y_{1}=d$ $y_{2}=ah^{3}+bh^{2}+ch+d$ $y_{3}=8ah^{3}+4bh^{2}+2ch+d.$

Adding the first and third equation gives

$y_{0}+y_{2}=2bh^{2}+2d$

and adding the fourth equation to two times the third equation gives

$y_{3}+2y_{2}=10ah^{3}+6bh^{2}+4ch+3d.$

We now have

${\begin{aligned}A&={\frac {3h}{8}}\left[10ah^{3}+8bh^{2}+4ch+8d\right]\\&={\frac {3h}{8}}\left[\underbrace {10ah^{3}+6bh^{2}+4ch+3d} _{y_{3}+2y_{2}}+\underbrace {2bh^{2}+2d} _{y_{0}+y_{2}}+3\underbrace {d} _{y_{1}}\right]\\&={\frac {3h}{8}}\left[y_{0}+3y_{1}+3y_{2}+y_{3}\right].\end{aligned}}$

Simpsons 3/8 rule approximates a definite integral over an interval [a, b] by replacing the integrand with a cubic which interpolates the function at four equally spaced points, $x=a$ , $x=a+h$ , $x=a+2h$ and $x=a+3h=b$ , where $h={\frac {b-a}{3}}$ is the step size. This gives

${\begin{aligned}\int _{a}^{b}f(x)\,dx\approx A&={\frac {3}{8}}h\left[f(a)+3f\left(a+h\right)+3f\left(a+2h\right)+f(b)\right].\end{aligned}}$

The error of this method is $-{\frac {3}{80}}h^{5}f^{(4)}(\xi )=-{\frac {(b-a)^{5}}{6480}}f^{(4)}(\xi ),$ where $\xi$ is some number between a and b . Thus, the 3/8 rule is about twice as accurate as the standard method, but it uses one more function value. A composite 3/8 rule also exists, similarly as above.

A further generalization of this concept for interpolation with arbitrary-degree polynomials are the Newton–Cotes formulas.

### Composite Simpson's 3/8 rule

Dividing the interval $[a,b]$ into n subintervals of length $h=(b-a)/n$ and introducing the points $x_{i}=a+ih$ for $0\leq i\leq n$ (in particular, $x_{0}=a$ and $x_{n}=b$ ), we have ${\begin{aligned}\int _{a}^{b}f(x)\,dx&\approx {\frac {3}{8}}h\sum _{i=1}^{n/3}{\big [}f(x_{3i-3})+3f(x_{3i-2})+3f(x_{3i-1})+f(x_{3i}){\big ]}\\&={\frac {3}{8}}h{\big [}f(x_{0})+3f(x_{1})+3f(x_{2})+2f(x_{3})+3f(x_{4})+3f(x_{5})+2f(x_{6})+\dots \\&\qquad +2f(x_{n-3})+3f(x_{n-2})+3f(x_{n-1})+f(x_{n}){\big ]}\\&={\frac {3}{8}}h\left[f(x_{0})+3\sum _{i=1,\ 3\nmid i}^{n-1}f(x_{i})+2\sum _{i=1}^{n/3-1}f(x_{3i})+f(x_{n})\right].\end{aligned}}$

While the remainder for the rule is shown as $-{\frac {1}{80}}h^{4}(b-a)f^{(4)}(\xi ),$ we can only use this if n is a multiple of three. The 1/3 rule can be used for the remaining subintervals without changing the order of the error term (conversely, the 3/8 rule can be used with a composite 1/3 rule for odd-numbered subintervals).

### Numerical example

Suppose we wish to calculate the arc length, L , of the sine curve $y=\sin(x)$ over a half period. Using the arc length formula, this can be expressed as

$L=\int _{0}^{\pi }{\sqrt {1+(y')^{2}}}\,dx=\int _{0}^{\pi }{\sqrt {1+[\cos(x)]^{2}}}\,dx$

which is a nonelementary integral, but can be shown to be ${\frac {\pi }{\varpi }}+\varpi \approx 3.820197789$ , where $\varpi$ is the lemniscate constant.

Applying Simpsons 3/8 rule with $n=6$ intervals gives

${\begin{aligned}L=\int _{0}^{\pi }{\sqrt {1+[\cos(x)]^{2}}}\,dx&\approx {\frac {\pi }{16}}{\dot {\left(\ {\sqrt {2}}+{\frac {3{\sqrt {7}}}{2}}+{\frac {3{\sqrt {5}}}{2}}+2+{\frac {3{\sqrt {5}}}{2}}+{\frac {3{\sqrt {7}}}{2}}+{\sqrt {2}}\right)}}\\&={\frac {\pi }{16}}\left(2{\sqrt {2}}+3{\sqrt {7}}+3{\sqrt {5}}+2\right)\\&\approx 3.823688376,\end{aligned}}$

which has a respectable relative error of only $0.0913\%$ .

## Alternative extended Simpson's rule

This is another formulation of a composite Simpson's rule: instead of applying Simpson's rule to disjoint segments of the integral to be approximated, Simpson's rule is applied to overlapping segments, yielding

${\begin{aligned}\int _{a}^{b}f(x)\,dx\approx {\frac {1}{48}}h{\bigg [}&17f(x_{0})+59f(x_{1})+43f(x_{2})+49f(x_{3})\\+&48\sum _{i=4}^{n-4}f(x_{i})\\+&49f(x_{n-3})+43f(x_{n-2})+59f(x_{n-1})+17f(x_{n}){\bigg ]}\end{aligned}}$ The formula above is obtained by combining the composite Simpson's 1/3 rule with the one consisting of using Simpson's 3/8 rule in the extreme subintervals and Simpson's 1/3 rule in the remaining subintervals. The result is then obtained by taking the mean of the two formulas.

### Simpson's rules in the case of narrow peaks

In the task of estimation of full area of narrow peak-like functions, Simpson's rules are much less efficient than trapezoidal rule. Namely, composite Simpson's 1/3 rule requires 1.8 times more points to achieve the same accuracy as trapezoidal rule. Composite Simpson's 3/8 rule is even less accurate. Integration by Simpson's 1/3 rule can be represented as a weighted average with 2/3 of the value coming from integration by the trapezoidal rule with step *h* and 1/3 of the value coming from integration by the rectangle rule with step 2*h*. The accuracy is governed by the second (2*h* step) term. Averaging of Simpson's 1/3 rule composite sums with properly shifted frames produces the following rules: $\int _{a}^{b}f(x)\,dx\approx {\frac {1}{24}}h\left[-f(x_{-1})+12f(x_{0})+25f(x_{1})+24\sum _{i=2}^{n-2}f(x_{i})+25f(x_{n-1})+12f(x_{n})-f(x_{n+1})\right],$ where two points outside of the integrated region are exploited, and $\int _{a}^{b}f(x)\,dx\approx {\frac {1}{24}}h\left[9f(x_{0})+28f(x_{1})+23f(x_{2})+24\sum _{i=3}^{n-3}f(x_{i})+23f(x_{n-2})+28f(x_{n-1})+9f(x_{n})\right],$ where only points within integration region are used. Application of the second rule to the region of 3 points generates 1/3 Simpson's rule, 4 points - 3/8 rule.

These rules are very much similar to the alternative extended Simpson's rule. The coefficients within the major part of the region being integrated are one with non-unit coefficients only at the edges. These two rules can be associated with Euler–MacLaurin formula with the first derivative term and named **First order** **Euler–MacLaurin integration rules**. The two rules presented above differ only in the way how the first derivative at the region end is calculated. The first derivative term in the Euler–MacLaurin integration rules accounts for integral of the second derivative, which equals the difference of the first derivatives at the edges of the integration region. It is possible to generate higher order Euler–Maclaurin rules by adding a difference of 3rd, 5th, and so on derivatives with coefficients, as defined by Euler–MacLaurin formula.

## Composite Simpson's rule for irregularly spaced data

For some applications, the integration interval $I=[a,b]$ needs to be divided into uneven intervals – perhaps due to uneven sampling of data, or missing or corrupted data points. Suppose we divide the interval I into an **even number N of subintervals** of widths $h_{k}$ . Then the composite Simpson's rule is given by $\int _{a}^{b}f(x)\,dx\approx \sum _{i=0}^{N/2-1}{\frac {h_{2i}+h_{2i+1}}{6}}\left[\left(2-{\frac {h_{2i+1}}{h_{2i}}}\right)f_{2i}+{\frac {(h_{2i}+h_{2i+1})^{2}}{h_{2i}h_{2i+1}}}f_{2i+1}+\left(2-{\frac {h_{2i}}{h_{2i+1}}}\right)f_{2i+2}\right],$ where $f_{k}=f\left(a+\sum _{i=0}^{k-1}h_{i}\right)$ are the function values at the k th sampling point on the interval I .

In case of an **odd number N of subintervals**, the above formula is used up to the second to last interval, and the last interval is handled separately by adding the following to the result: $\alpha f_{N}+\beta f_{N-1}-\eta f_{N-2},$ where ${\begin{aligned}\alpha &={\frac {2h_{N-1}^{2}+3h_{N-1}h_{N-2}}{6(h_{N-2}+h_{N-1})}},\\[1ex]\beta &={\frac {h_{N-1}^{2}+3h_{N-1}h_{N-2}}{6h_{N-2}}},\\[1ex]\eta &={\frac {h_{N-1}^{3}}{6h_{N-2}(h_{N-2}+h_{N-1})}}.\end{aligned}}$

| **Example implementation in Python** |
|---|
| from collections.abc import Sequence def simpson_nonuniform(x: Sequence[float], f: Sequence[float]) -> float: """ Simpson rule for irregularly spaced data. :param x: Sampling points for the function values :param f: Function values at the sampling points :return: approximation for the integral See ``scipy.integrate.simpson`` and the underlying ``_basic_simpson`` for a more performant implementation utilizing numpy's broadcast. """ N = len(x) - 1 h = [x[i + 1] - x[i] for i in range(0, N)] assert N > 0 result = 0.0 for i in range(1, N, 2): h0, h1 = h[i - 1], h[i] hph, hdh, hmh = h1 + h0, h1 / h0, h1 * h0 result += (hph / 6) * ( (2 - hdh) * f[i - 1] + (hph**2 / hmh) * f[i] + (2 - 1 / hdh) * f[i + 1] ) if N % 2 == 1: h0, h1 = h[N - 2], h[N - 1] result += f[N] * (2 * h1 ** 2 + 3 * h0 * h1) / (6 * (h0 + h1)) result += f[N - 1] * (h1 ** 2 + 3 * h1 * h0) / (6 * h0) result -= f[N - 2] * h1 ** 3 / (6 * h0 * (h0 + h1)) return result |

| **Example implementation in R** |
|---|
| SimpsonInt <- function(fx, dx) { n <- length(dx) h <- diff(dx) stopifnot(exprs = { length(fx) == n all(h >= 0) }) res <- 0 for (i in seq(1L, n - 2L, 2L)) { hph <- h[i] + h[i + 1L] hdh <- h[i + 1L] / h[i] res <- res + hph / 6 * ((2 - hdh) * fx[i] + hph ^ 2 / (h[i] * h[i + 1L]) * fx[i + 1L] + (2 - 1 / hdh) * fx[i + 2L]) } if (n %% 2 == 0) { hph <- h[n - 1L] + h[n - 2L] threehth <- 3 * h[n - 1L] * h[n - 2L] sixh2 <- 6 * h[n - 2L] h1sq <- h[n - 1L] ^ 2 res <- res + (2 * h1sq + threehth) / (6 * hph) * fx[n] + (h1sq + threehth) / sixh2 * fx[n - 1L] - (h1sq * h[n - 1L]) / (sixh2 * hph) * fx[n - 2L] } res } |

## Numerical stability

An important property of Simpson's Rule, which is shared across all Newton–Cotes formulas, is its stability with respect to round-off error. To illustrate, suppose we apply Composite Simpson's rule with n subintervals to some function $f(x)$ on an interval [a, b]. Let $e_{i}$ denote the round-off error when $f(x_{i})$ is calculated, and $E(h)$ denote the total accumulated error in Composite Simpson's rule, where $h={\frac {b-a}{n}}$ .

By definition, ${\begin{aligned}E(h)&=\left|{\frac {h}{3}}\left[e_{0}+2\sum _{j=1}^{(n/2)-1}e_{2j}+4\sum _{j=1}^{n/2}e_{2j-1}+e_{n}\right]\right|\\&\leq {\frac {h}{3}}\left[\left|e_{0}\right|+2\sum _{j=1}^{(n/2)-1}\left|e_{2j}\right|+4\sum _{j=1}^{n/2}\left|e_{2j-1}\right|+\left|e_{n}\right|\right].\end{aligned}}$

Assuming the round-off errors are bounded by some number $\varepsilon >0$ , we get

${\begin{aligned}E(h)&\leq {\frac {h}{3}}\left[\varepsilon +2\left({\frac {n}{2}}-1\right)\varepsilon +4\left({\frac {n}{2}}\right)\varepsilon +\varepsilon \right]\\&={\frac {h}{3}}3n\varepsilon \\[1ex]&=nh\varepsilon \\[1ex]&=n\left({\frac {b-a}{n}}\right)\varepsilon \\&=(b-a)\varepsilon ,\end{aligned}}$

which is a bound independent of h , so the procedure is stable as h approaches zero. This in contrast to numerical differentiation techniques, which are ill-conditioned.
