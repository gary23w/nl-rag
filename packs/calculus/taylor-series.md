---
title: "Taylor series"
source: https://en.wikipedia.org/wiki/Taylor_series
domain: calculus
license: CC-BY-SA-4.0
tags: calculus, differential calculus, integral calculus, differentiation, antiderivative
fetched: 2026-07-02
---

# Taylor series

In mathematical analysis, the **Taylor series** or **Taylor expansion** of a function is an infinite sum of terms that are expressed in terms of the function's derivatives at a single point. For most common functions, the function and the sum of its Taylor series are equal near this point. Taylor series are named after Brook Taylor, who introduced them in 1715. A Taylor series is also called a **Maclaurin series** when 0 is the point where the derivatives are considered, after Colin Maclaurin, who made extensive use of this special case of Taylor series in the 18th century.

The partial sum formed by the first *n* + 1 terms of a Taylor series is a polynomial of degree n that is called the nth **Taylor polynomial** of the function. Taylor polynomials are approximations of a function, which become generally more accurate as n increases. Taylor's theorem gives quantitative estimates on the error introduced by the use of such approximations. If the Taylor series of a function is convergent, its sum is the limit of the infinite sequence of the Taylor polynomials. A function may differ from the sum of its Taylor series, even if its Taylor series is convergent. A function is analytic at a point x if it is equal to the sum of its Taylor series in some open interval (or open disk in the complex plane) containing x. This implies that the function is analytic at every point of the interval (or disk).

## Definition

The Taylor series of a real or complex-valued function *f*(*x*), that is infinitely differentiable at a real or complex number *a*, is the power series $f(a)+{\frac {f'(a)}{1!}}(x-a)+{\frac {f''(a)}{2!}}(x-a)^{2}+\cdots =\sum _{n=0}^{\infty }{\frac {f^{(n)}(a)}{n!}}(x-a)^{n}.$ Here, *n*! denotes the factorial of n. The function *f*(*n*)(*a*) denotes the nth derivative of *f* evaluated at the point a. The derivative of order zero of *f* is defined to be *f* itself and (*x* − *a*)0 and 0! are both defined to be 1. This series can be written by using sigma notation, as in the right side formula. The corresponding Taylor polynomial of degree n is $T_{n}(x)=\sum _{k=0}^{n}{\frac {f^{(k)}(a)}{k!}}(x-a)^{k}.$ With *a* = 0, the Maclaurin series takes the form: $f(0)+{\frac {f'(0)}{1!}}x+{\frac {f''(0)}{2!}}x^{2}+\cdots =\sum _{n=0}^{\infty }{\frac {f^{(n)}(0)}{n!}}x^{n}.$

## Basic properties

Taylor series inherit the basic properties of power series. Taylor series can also be combined algebraically. Sums, differences, products, and scalar multiples of Taylor series are obtained by the corresponding operations on power series. In particular, the Taylor series of $f(x)g(x)$ around a point $x=a$ is the Cauchy product of the Taylor series of $f(x)$ and $g(x)$ about $x=a$ . Compositions of functions having Taylor series likewise have Taylor series, obtained by substituting one convergent power series into another when the substitution is valid.

A Taylor series may be differentiated and integrated term by term. Thus ${\frac {d}{dx}}\sum _{n=0}^{\infty }c_{n}(x-a)^{n}=\sum _{n=1}^{\infty }nc_{n}(x-a)^{n-1},$ and $\int \sum _{n=0}^{\infty }c_{n}(x-a)^{n}\,dx=C+\sum _{n=0}^{\infty }{\frac {c_{n}}{n+1}}(x-a)^{n+1}.$ The differentiated and integrated series have the same radius of convergence as the original power series, although the convergence behavior at the boundary may be different.

These properties sometimes allow the Taylor series of functions, such as the arctangent, to be computed in terms of simpler series, such as the geometric series.

## Calculation of Taylor series

Several methods can be used to calculate Taylor series. One may apply the definition directly, although this often requires first identifying a general formula for the derivatives or coefficients. In many cases, Taylor series can also be obtained from known expansions by algebraic manipulations of power series, such as substitution, multiplication, division, addition, or subtraction, as well as termwise differentiation and integration of known Taylor series. In some cases, they may also be derived by repeated integration by parts. In practice, Taylor series are often computed with the aid of computer algebra systems.

A number of standard Maclaurin series are frequently used as starting points for calculating other Taylor series. Some fundamental examples are listed below; a more comprehensive listing appears later in the article.

| Function | Maclaurin series | Convergence |
|---|---|---|
| $e^{x}$ | $\displaystyle \sum _{n=0}^{\infty }{\frac {x^{n}}{n!}}=1+x+{\frac {x^{2}}{2!}}+{\frac {x^{3}}{3!}}+\cdots$ | All x |
| $\sin x$ | $\displaystyle \sum _{n=0}^{\infty }(-1)^{n}{\frac {x^{2n+1}}{(2n+1)!}}=x-{\frac {x^{3}}{3!}}+{\frac {x^{5}}{5!}}-\cdots$ | All x |
| $\cos x$ | $\displaystyle \sum _{n=0}^{\infty }(-1)^{n}{\frac {x^{2n}}{(2n)!}}=1-{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}-\cdots$ | All x |
| ${\frac {1}{1-x}}$ | $\displaystyle \sum _{n=0}^{\infty }x^{n}=1+x+x^{2}+x^{3}+\cdots$ | $\|x\|<1$ |

### Examples

#### Term-by-term differentiation

Inside the region of convergence, a Taylor series can be differentiated term-by-term. For example, differentiating the geometric series ${\frac {1}{1-x}}=1+x+x^{2}+x^{3}+\cdots ,\quad |x|<1,$ one gets ${\frac {d}{dx}}{\frac {1}{1-x}}={\frac {1}{(1-x)^{2}}}=0+1+2x+3x^{2}+\cdots ,\quad |x|<1.$ Thus ${\frac {1}{(1-x)^{2}}}=\sum _{n=1}^{\infty }nx^{n-1},\quad |x|<1.$ This process can be iterated, giving ${\frac {1}{(1-x)^{3}}}=\sum _{n=2}^{\infty }n(n-1)x^{n-2},\quad |x|<1.$ ${\frac {1}{(1-x)^{4}}}=\sum _{n=3}^{\infty }n(n-1)(n-2)x^{n-3},\quad |x|<1.$ and so forth.

#### Term-by-term integration

Inside the region of convergence, a Taylor series can be integrated term-by-term. For example, integrating the geometric series ${\frac {1}{1-t}}=1+t+t^{2}+t^{3}+\cdots ,\quad |t|<1,$ one gets $-\log(1-x)=\int _{0}^{x}{\frac {dt}{1-t}}=x+{\frac {x^{2}}{2}}+{\frac {x^{3}}{3}}+{\frac {x^{4}}{4}}+\cdots ,\quad |x|<1.$ This gives the Maclaurin series $\log(1-x)=-\sum _{n=1}^{\infty }{\frac {x^{n}}{n}},$ valid for $|x|<1$ .

#### Substitution

Taylor series can be composed, for example if the Taylor series of $f(t)$ is known, then the Taylor series of $f(x^{n})$ is obtained by evaluating at $t=x^{n}$ term by term. For instance, the geometric series $1/(1-t)=1+t+t^{2}+\cdots$ evaluated at $t=-x^{2}$ gives ${\frac {1}{1+x^{2}}}=1-x^{2}+x^{4}-x^{6}+\cdots =\sum _{n=0}^{\infty }(-1)^{n}x^{2n}.$ This last series can be integrated term-by-term to give $\arctan x=\int _{0}^{x}{\frac {dt}{1+t^{2}}}=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{2n+1}}x^{2n+1},$ for $|x|<1$ .

#### Composition

In order to compute the 7th-degree Maclaurin polynomial for the function $f(x)=\ln(\cos x),\quad x\in {\bigl (}{-{\tfrac {\pi }{2}}},{\tfrac {\pi }{2}}{\bigr )},$ one may first rewrite the function as $f(x)={\ln }{\bigl (}1+(\cos x-1){\bigr )},$ the composition of two functions *x* ↦ ln(1 + *x*) and *x* ↦ cos *x* − 1. The Taylor series for the natural logarithm is (using big O notation) $\ln(1+x)=x-{\frac {x^{2}}{2}}+{\frac {x^{3}}{3}}+O{\left(x^{4}\right)}$ and for the cosine function $\cos x-1=-{\frac {x^{2}}{2}}+{\frac {x^{4}}{24}}-{\frac {x^{6}}{720}}+O{\left(x^{8}\right)}.$

The first several terms from the second series can be substituted into each term of the first series. Because the first term in the second series has degree 2, three terms of the first series suffice to give a polynomial of degree 7: ${\begin{aligned}f(x)&=\ln {\bigl (}1+(\cos x-1){\bigr )}\\&=(\cos x-1)-{\tfrac {1}{2}}(\cos x-1)^{2}+{\tfrac {1}{3}}(\cos x-1)^{3}+O{\left((\cos x-1)^{4}\right)}\\&=-{\frac {x^{2}}{2}}-{\frac {x^{4}}{12}}-{\frac {x^{6}}{45}}+O{\left(x^{8}\right)}.\end{aligned}}$

Since the cosine is an even function, the coefficients for all the odd powers are zero.

#### Division

Given that the Taylor series at 0 of the function *g*(*x*) = ⁠*e**x*/cos *x*⁠. The Taylor series for the exponential function is $e^{x}=1+x+{\frac {x^{2}}{2!}}+{\frac {x^{3}}{3!}}+{\frac {x^{4}}{4!}}+\cdots ,$ and the series for cosine is $\cos x=1-{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}-\cdots .$

Assume the series for their quotient is ${\frac {e^{x}}{\cos x}}=c_{0}+c_{1}x+c_{2}x^{2}+c_{3}x^{3}+c_{4}x^{4}+\cdots$ Multiplying both sides by the denominator cos *x* and then expanding it as a series yields ${\begin{aligned}e^{x}&=\left(c_{0}+c_{1}x+c_{2}x^{2}+c_{3}x^{3}+c_{4}x^{4}+\cdots \right)\left(1-{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}-\cdots \right)\\[5mu]&=c_{0}+c_{1}x+\left(c_{2}-{\frac {c_{0}}{2!}}\right)x^{2}+\left(c_{3}-{\frac {c_{1}}{2!}}\right)x^{3}+\left(c_{4}-{\frac {c_{2}}{2!}}+{\frac {c_{0}}{4!}}\right)x^{4}+\cdots \end{aligned}}$

Comparing the coefficients of *g*(*x*) cos *x* with the coefficients of *e**x*, $c_{0}=1,\ \ c_{1}=1,\ \ c_{2}-{\tfrac {1}{2}}c_{0}={\tfrac {1}{2}},\ \ c_{3}-{\tfrac {1}{2}}c_{1}={\tfrac {1}{6}},\ \ c_{4}-{\tfrac {1}{2}}c_{2}+{\tfrac {1}{24}}c_{0}={\tfrac {1}{24}},\ \ldots .$

The coefficients *c**i* of the series for *g*(*x*) can thus be computed one at a time, amounting to long division of the series for *e**x* and cos *x*: ${\frac {e^{x}}{\cos x}}=1+x+x^{2}+{\tfrac {2}{3}}x^{3}+{\tfrac {1}{2}}x^{4}+\cdots .$

#### Non-elementary integrals

Term-by-term integration of Taylor series can be used to find the Taylor series of non-elementary integrals. For example, the Fresnel integral is $S(x)=\int _{0}^{x}\sin(t^{2})\,dt$ and $S(x)$ cannot be expressed in terms of elementary functions. Its Maclaurin series can be determined by termwise integration of the series $\sin(t^{2})=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n+1)!}}t^{4n+2},$ giving $S(x)=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(4n+3)(2n+1)!}}x^{4n+3}.$

#### Differential equations

Taylor series can also be used to solve some ordinary differential equations. The method is to assume that the solution has a power series expansion, differentiate the series term by term, substitute the resulting series into the differential equation, and then determine the coefficients by equating like powers of the variable.

For example, to solve $y''-y=0,$ suppose that $y=\sum _{n=0}^{\infty }a_{n}x^{n}.$ Then $y''=\sum _{n=2}^{\infty }n(n-1)a_{n}x^{n-2}=\sum _{n=0}^{\infty }(n+2)(n+1)a_{n+2}x^{n}.$ Substitution into the differential equation gives $\sum _{n=0}^{\infty }{\bigl (}(n+2)(n+1)a_{n+2}-a_{n}{\bigr )}x^{n}=0.$ Since power series expansions are unique, each coefficient must vanish, so $a_{n+2}={\frac {a_{n}}{(n+2)(n+1)}}.$ The even and odd coefficients are therefore determined separately by the arbitrary constants $a_{0}$ and $a_{1}$ : $y=a_{0}\left(1+{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}+\cdots \right)+a_{1}\left(x+{\frac {x^{3}}{3!}}+{\frac {x^{5}}{5!}}+\cdots \right).$ Thus $y=a_{0}\cosh x+a_{1}\sinh x,$ or equivalently $y=C_{1}e^{x}+C_{2}e^{-x}$ .

## Approximation error and Taylor's theorem

Pictured is an accurate approximation of

sin

x

around the point

x

= 0

. The pink curve is a polynomial of degree seven

$\sin {x}\approx x-{\frac {x^{3}}{3!}}+{\frac {x^{5}}{5!}}-{\frac {x^{7}}{7!}}.$

The error in this approximation is no more than |*x*|9 / 9!. For a full cycle centered at the origin (−π < *x* < π), the error is less than 0.08215. In particular, for −1 < *x* < 1, the error is less than 0.000003.

In contrast, also shown is a picture of the natural logarithm function

ln(1 +

x

)

and some of its Taylor polynomials around

a

= 0

. These approximations converge to the function only in the region

−1 <

x

≤ 1

. Outside of this region, the higher-degree Taylor polynomials are

worse

approximations for the function.

The *error* incurred in approximating a function by its degree n Taylor polynomial is called the remainder and is denoted by the function *R**n*(*x*). Taylor's theorem can be used to obtain a bound on the size of the remainder.

In particular, Taylor's theorem writes a function, where the hypotheses of the theorem are satisfied, in the form $f(x)=\sum _{k=0}^{n}{\frac {f^{(k)}(a)}{k!}}(x-a)^{k}+R_{n}(x).$ The behavior of the remainder as n tends to infinity determines whether the Taylor series represents the original function, which are questions of convergence and analyticity.

## Generalization in finite differences

One form of the Gregory–Newton interpolation formula can be written as $f(x)=\sum _{k=0}^{\infty }{\frac {\Delta ^{k}[f](a)}{k!}}\,(x-a)_{k}$ which interpolates a polynomial f in terms of its finite differences evaluated at a single point a , and where $(x-a)_{k}$ is the falling factorial. For a polynomial, this series terminates and gives the polynomial exactly; more generally, a function admits a Gregory–Newton development under suitable analytic hypotheses, classically formulated by Niels Erik Nørlund in terms of holomorphy in a half-plane together with an exponential type growth condition.

One generalization of the Taylor series that does converge to the value of the function itself for any bounded continuous function on (0, ∞), and this can be done by using the calculus of finite differences. Specifically, the following theorem, due to Einar Hille, that for any *t* > 0, $\lim _{h\to 0^{+}}\sum _{n=0}^{\infty }{\frac {t^{n}}{n!}}{\frac {\Delta _{h}^{n}f(a)}{h^{n}}}=f(a+t).$ Here Δ*n* *h* is the nth finite difference operator with step size h. The series is precisely the Taylor series, except that divided differences appear in place of differentiation. When the function *f* is analytic at a, the terms in the series converge to the terms of the Taylor series, and in this sense generalizes the usual Taylor series.

In general, for any infinite sequence *a**i*, the following power series identity holds: $\sum _{n=0}^{\infty }{\frac {u^{n}}{n!}}\Delta ^{n}a_{i}=e^{-u}\sum _{j=0}^{\infty }{\frac {u^{j}}{j!}}a_{i+j}.$ So in particular, $f(a+t)=\lim _{h\to 0^{+}}e^{-t/h}\sum _{j=0}^{\infty }f(a+jh){\frac {(t/h)^{j}}{j!}}.$

The series on the right is the expected value of *f*(*a* + *X*), where X is a Poisson-distributed random variable that takes the value *jh* with probability *e*−*t*/*h*·⁠(*t*/*h*)*j*/*j*!⁠. Hence, $f(a+t)=\lim _{h\to 0^{+}}\int _{-\infty }^{\infty }f(a+x)dP_{t/h,h}(x).$

The law of large numbers implies that the identity holds.

## Convergence and analyticity

A Taylor series is formed from the values of all derivatives of a function at a single point, but this does not by itself imply that the series converges to the function. In general, a Taylor series may fail to converge, or it may converge to a function different from the original one.

For example, the function $f(x)={\begin{cases}e^{-1/x^{2}}&{\text{if }}x\neq 0,\\[3mu]0&{\text{if }}x=0\end{cases}}$ is infinitely differentiable at $x=0$ , and all of its derivatives at 0 are equal to zero. Its Taylor series at 0 is therefore the zero series, even though the function itself is not identically zero. This gives a standard example of a non-analytic smooth function.

More generally, the Taylor series of a function represents the function at a point x precisely when the remainder terms in Taylor's theorem tend to zero at that point. If $f(x)=\sum _{k=0}^{n}{\frac {f^{(k)}(a)}{k!}}(x-a)^{k}+R_{n}(x),$ then the Taylor series converges to $f(x)$ exactly when $\lim _{n\to \infty }R_{n}(x)=0.$

A function is called analytic at a point if it is equal to the sum of its Taylor series in some open interval around that point, or, in the complex case, in some open disk. Equivalently, a function is analytic in a region if it is locally given by a convergent power series. Thus, if $f(x)=\sum _{n=0}^{\infty }a_{n}(x-b)^{n}$ near b , then differentiating the series term by term and setting $x=b$ gives $a_{n}={\frac {f^{(n)}(b)}{n!}}.$ Thus the power series expansion of an analytic function is its Taylor series.

In real analysis, infinite differentiability does not imply analyticity, as the example above shows. Borel's lemma implies that *every* power series is the Taylor series of some smooth function. In complex analysis, however, every holomorphic function is analytic. A function whose Taylor series converges to the function throughout the whole complex plane is called an entire function. Polynomials, the exponential function, and the sine and cosine functions are entire functions.

### Radius of convergence

For any power series $\sum _{n=0}^{\infty }c_{n}(x-a)^{n},$ there is a number R , called the radius of convergence, such that the series converges absolutely for $|x-a|<R$ and diverges for $|x-a|>R$ . The radius may be zero, finite and positive, or infinite. It is given by the Cauchy–Hadamard formula ${\frac {1}{R}}=\limsup _{n\to \infty }|c_{n}|^{1/n},$ with the usual conventions for $R=0$ and $R=\infty$ . When the limit exists, the ratio test often gives $R=\lim _{n\to \infty }\left|{\frac {c_{n}}{c_{n+1}}}\right|.$

Thus, when a Taylor series converges, it does so in an open interval centered at a in the real case, or in an open disk centered at a in the complex case. The behavior at the boundary points may vary: the series may converge at some, all, or none of them.

For a complex analytic function, the radius of convergence of the Taylor series at a is the distance from a to the nearest point where the function cannot be continued holomorphically. In many common examples this is the distance to the nearest singularity in the complex plane.

This explains the different radii of convergence for familiar Taylor series. The series for $e^{x}$ , $\sin x$ , and $\cos x$ have infinite radius of convergence because these functions are entire. By contrast, the Taylor series for $\log(1+x)$ at $x=0$ has radius of convergence 1 , because the nearest singularity is at $x=-1$ .

Complex singularities can determine the radius of convergence even for functions that are smooth on the real line. For example, ${\frac {1}{1+x^{2}}}$ is smooth for every real x , but its Taylor series at 0 has radius of convergence 1 , because the corresponding complex function has singularities at $x=i$ and $x=-i$ .

The radius of convergence should not be confused with the quality of approximation by a low-degree Taylor polynomial. A Taylor polynomial may approximate a function accurately near the center even if the full Taylor series has a small radius of convergence. Conversely, near the boundary of the interval or disk of convergence, the Taylor series may converge slowly. Outside the radius of convergence, the Taylor series does not represent the function.

### Generalizations near singularities

A Taylor series cannot be centered at a point where the function is not analytic. Some singularities, namely poles, can be accounted for by a Laurent series. If f has a pole of order k at $z=a$ , then near a it has a Laurent series of the form $\sum _{n=-k}^{\infty }a_{n}(z-a)^{n}.$ A meromorphic function is a function which is analytic except at isolated poles; near each pole it has a Laurent series with only finitely many negative-power terms.

More generally, a function analytic in an annulus $r<|z-a|<R$ has a convergent Laurent series of the form $\sum _{n=-\infty }^{\infty }a_{n}(z-a)^{n}$ in that annulus.

Other types of singularities, namely branch points, can occur for algebraic functions. If $f(z)$ is an algebraic function of a complex variable z and $z=a$ is a branch point, then $f(z)$ need not have a Taylor series based at $z=a$ . However, after a change of variables $z-a=t^{e},$ where e is a positive integer called the ramification index, a branch of the function becomes analytic as a function of t . The resulting expansion in fractional powers of $z-a$ is known as a Puiseux series.

## Taylor series in multiple variables

The Taylor series may also be generalized to functions of more than one variable with ${\begin{aligned}T(x_{1},\ldots ,x_{d})&=\sum _{n_{1}=0}^{\infty }\cdots \sum _{n_{d}=0}^{\infty }{\frac {(x_{1}-a_{1})^{n_{1}}\cdots (x_{d}-a_{d})^{n_{d}}}{n_{1}!\cdots n_{d}!}}\,\left({\frac {\partial ^{n_{1}+\cdots +n_{d}}f}{\partial x_{1}^{n_{1}}\cdots \partial x_{d}^{n_{d}}}}\right)(a_{1},\ldots ,a_{d})\\&=f(a_{1},\ldots ,a_{d})+\sum _{j=1}^{d}{\frac {\partial f(a_{1},\ldots ,a_{d})}{\partial x_{j}}}(x_{j}-a_{j})+{\frac {1}{2!}}\sum _{j=1}^{d}\sum _{k=1}^{d}{\frac {\partial ^{2}f(a_{1},\ldots ,a_{d})}{\partial x_{j}\partial x_{k}}}(x_{j}-a_{j})(x_{k}-a_{k})\\&\qquad \qquad +{\frac {1}{3!}}\sum _{j=1}^{d}\sum _{k=1}^{d}\sum _{l=1}^{d}{\frac {\partial ^{3}f(a_{1},\ldots ,a_{d})}{\partial x_{j}\partial x_{k}\partial x_{l}}}(x_{j}-a_{j})(x_{k}-a_{k})(x_{l}-a_{l})+\cdots ,\\&=\sum _{|\alpha |\geq 0}{\frac {(\mathbf {x} -\mathbf {a} )^{\alpha }}{\alpha !}}\left({\mathrm {\partial } ^{\alpha }}f\right)(\mathbf {a} ).\end{aligned}}$ The last expression is the multivariate Taylor series in terms of multi-index notation with a full analogy to the single variable case.

For example, for a function *f*(*x*, *y*) that depends on two variables, x and y, the Taylor series to second order about the point (*a*, *b*) is $f(a,b)+(x-a)f_{x}(a,b)+(y-b)f_{y}(a,b)+{\frac {1}{2!}}{\Big (}(x-a)^{2}f_{xx}(a,b)+2(x-a)(y-b)f_{xy}(a,b)+(y-b)^{2}f_{yy}(a,b){\Big )}$ where the subscripts denote the respective partial derivatives.

### Second-order Taylor series in several variables

A second-order Taylor series expansion of a scalar-valued function of more than one variable can be written compactly as $T(\mathbf {x} )=f(\mathbf {a} )+(\mathbf {x} -\mathbf {a} )^{\mathsf {T}}Df(\mathbf {a} )+{\frac {1}{2!}}(\mathbf {x} -\mathbf {a} )^{\mathsf {T}}\left\{D^{2}f(\mathbf {a} )\right\}(\mathbf {x} -\mathbf {a} )+\cdots ,$ where *D* *f*(**a**) is the gradient of *f* evaluated at **x** = **a** and *D*2 *f*(**a**) is the Hessian matrix.

### Example

In order to compute a second-order Taylor series expansion around the point (*a*, *b*) = (0, 0) of the function $f(x,y)=e^{x}\ln(1+y),$ one first computes all the necessary partial derivatives: ${\begin{aligned}f_{x}&=e^{x}\ln(1+y),&f_{y}&={\frac {e^{x}}{1+y}},\\f_{xx}&=e^{x}\ln(1+y),&f_{yy}&=-{\frac {e^{x}}{(1+y)^{2}}},\\f_{xy}&=f_{yx}={\frac {e^{x}}{1+y}}.\end{aligned}}$

Evaluating these derivatives at the origin gives the Taylor coefficients ${\begin{aligned}f_{x}(0,0)&=0,&f_{y}(0,0)&=1,\\f_{xx}(0,0)&=0,&f_{yy}(0,0)&=-1,\\f_{xy}(0,0)&=1.\end{aligned}}$

Substituting these values in to the general formula ${\begin{aligned}T(x,y)&=f(a,b)+(x-a)f_{x}(a,b)+(y-b)f_{y}(a,b)\\&\qquad {}+{\frac {1}{2!}}\left((x-a)^{2}f_{xx}(a,b)+2(x-a)(y-b)f_{xy}(a,b)+(y-b)^{2}f_{yy}(a,b)\right)+\cdots \end{aligned}}$ produces ${\begin{aligned}T(x,y)&=0+0(x-0)+1(y-0)+{\frac {1}{2}}{\big (}0(x-0)^{2}+2(x-0)(y-0)+(-1)(y-0)^{2}{\big )}+\cdots \\&=y+xy-{\tfrac {1}{2}}y^{2}+\cdots \end{aligned}}$

Since ln(1 + *y*) is analytic in |*y*| < 1, we have $e^{x}\ln(1+y)=y+xy-{\tfrac {1}{2}}y^{2}+\cdots ,\qquad |y|<1.$

## Applications

Taylor polynomials are used to approximate functions near a point. Keeping only the first nonzero terms often gives a simpler model of a more complicated expression. For example, the small-angle approximation $\sin x\approx x$ comes from the first term of the Taylor series for sine, and higher-order approximations are obtained by retaining more terms. This approximation is widely used: for example, in Gaussian optics where the behavior of light rays making small angles with an axis is studied by replacing the sine function with its linear approximation.

Such approximations are used throughout mathematics, physics, and engineering. In perturbation theory, a complicated quantity is often expanded in powers of a small parameter, and the first few terms are used as an approximate solution. Taylor expansions also occur in the analysis of the simple pendulum and in numerical methods for approximating functions.

## History

The ancient Greek philosopher Zeno of Elea considered the problem of summing an infinite series to achieve a finite result, but rejected it as an impossibility; the result was Zeno's paradox. Later, Aristotle proposed a philosophical resolution of the paradox, but the mathematical content was apparently unresolved until taken up by Archimedes, as it had been prior to Aristotle by the Presocratic Atomist Democritus. It was through Archimedes's method of exhaustion that an infinite number of progressive subdivisions could be performed to achieve a finite result. Liu Hui independently employed a similar method a few centuries later.

In the 14th century, the earliest examples of specific Taylor series (but not the general method) were given by the Indian mathematician Madhava of Sangamagrama. Though no record of his work survives, writings of his followers in the Kerala school of astronomy and mathematics suggest that he found the Taylor series for the trigonometric functions of sine, cosine, and arctangent; see Madhava series. During the following two centuries, his followers developed further series expansions and rational approximations.

In late 1670, James Gregory was shown in a letter from John Collins several Maclaurin series (sin *x*, cos *x*, arcsin *x*, and *x* cot *x*) derived by Isaac Newton, and told that Newton had developed a general method for expanding functions in series. Newton had in fact used a cumbersome method involving long division of series and term-by-term integration, but Gregory did not know it and set out to discover a general method for himself. In early 1671 Gregory discovered something like the general Maclaurin series and sent a letter to Collins including series for arctan *x*, tan *x*, sec *x*, ln sec *x* (the integral of tan), ln tan ⁠1/2⁠(⁠1/2⁠*π* + *x*) (the integral of sec, the inverse Gudermannian function), arcsec(√2 *e**x*), and 2 arctan *e**x* − ⁠1/2⁠*π* (the Gudermannian function). However, thinking that he had merely redeveloped a method by Newton, Gregory never described how he obtained these series, and it can only be inferred that he understood the general method by examining scratch work he had scribbled on the back of another letter from 1671.

In 1691–1692, Newton wrote down an explicit statement of the Taylor and Maclaurin series in an unpublished version of his work *De Quadratura Curvarum*. It was the earliest explicit formulation of the general Taylor series. However, this work by Newton was never completed and the relevant sections were omitted from the portions published in 1704 under the title *Tractatus de Quadratura Curvarum*.

It was not until 1715 that a general method for constructing these series for all functions for which they exist was finally published by Brook Taylor, after whom the series are now named.

The Maclaurin series was named after Colin Maclaurin, a Scottish mathematician, who published a special case of the Taylor result in the mid-18th century.

## List of Maclaurin series of some common functions

Several important Maclaurin series expansions follow. All these expansions are valid for complex arguments x. For multivalued complex functions, such as logarithms, fractional powers, and inverse trigonometric functions, a principal branch is understood.

### Exponential function

The exponential function *e**x* (with base e) has Maclaurin series $e^{x}=\sum _{n=0}^{\infty }{\frac {x^{n}}{n!}}=1+x+{\frac {x^{2}}{2!}}+{\frac {x^{3}}{3!}}+\cdots .$ It converges for all x.

The exponential generating function of the Bell numbers is the exponential function of the predecessor of the exponential function: $\exp(\exp {x}-1)=\sum _{n=0}^{\infty }{\frac {B_{n}}{n!}}x^{n}$

### Natural logarithm

The natural logarithm (with base e) has Maclaurin series ${\begin{aligned}\ln(1-x)&=-\sum _{n=1}^{\infty }{\frac {x^{n}}{n}}=-x-{\frac {x^{2}}{2}}-{\frac {x^{3}}{3}}-\cdots ,\\\ln(1+x)&=\sum _{n=1}^{\infty }(-1)^{n+1}{\frac {x^{n}}{n}}=x-{\frac {x^{2}}{2}}+{\frac {x^{3}}{3}}-\cdots .\end{aligned}}$

The last series is known as Mercator series, named after Nicholas Mercator since it was published in his 1668 treatise *Logarithmotechnia*. Both of these series converge for |*x*| < 1. In addition, the series for ln(1 − *x*) converges for *x* = −1, and the series for ln(1 + *x*) converges for *x* = 1.

### Geometric series

The geometric series and its derivatives have Maclaurin series ${\begin{aligned}{\frac {1}{1-x}}&=\sum _{n=0}^{\infty }x^{n}\\{\frac {1}{(1-x)^{2}}}&=\sum _{n=1}^{\infty }nx^{n-1}\\{\frac {1}{(1-x)^{3}}}&=\sum _{n=2}^{\infty }{\frac {(n-1)n}{2}}x^{n-2}.\end{aligned}}$

All are convergent for |*x*| < 1. These are special cases of the binomial series given in the next section.

### Binomial series

The binomial series is the power series

$(1+x)^{\alpha }=\sum _{n=0}^{\infty }{\binom {\alpha }{n}}x^{n}$

whose coefficients are the generalized binomial coefficients

${\binom {\alpha }{n}}=\prod _{k=1}^{n}{\frac {\alpha -k+1}{k}}={\frac {\alpha (\alpha -1)\cdots (\alpha -n+1)}{n!}}.$

(If *n* = 0, this product is an empty product and has value 1.) It converges for |*x*| < 1 for any real or complex number α.

When *α* = −1, this is essentially the infinite geometric series mentioned in the previous section. The special cases *α* = ⁠1/2⁠ and *α* = −⁠1/2⁠ give the square root function and its inverse: ${\begin{aligned}(1+x)^{\frac {1}{2}}&=1+{\frac {1}{2}}x-{\frac {1}{8}}x^{2}+{\frac {1}{16}}x^{3}-{\frac {5}{128}}x^{4}+{\frac {7}{256}}x^{5}-\cdots &=\sum _{n=0}^{\infty }{\frac {(-1)^{n-1}(2n)!}{4^{n}(n!)^{2}(2n-1)}}x^{n},\\(1+x)^{-{\frac {1}{2}}}&=1-{\frac {1}{2}}x+{\frac {3}{8}}x^{2}-{\frac {5}{16}}x^{3}+{\frac {35}{128}}x^{4}-{\frac {63}{256}}x^{5}+\cdots &=\sum _{n=0}^{\infty }{\frac {(-1)^{n}(2n)!}{4^{n}(n!)^{2}}}x^{n}.\end{aligned}}$

When only the linear term is retained, this simplifies to the binomial approximation.

### Trigonometric functions

The usual trigonometric functions and their inverses have the following Maclaurin series: ${\begin{aligned}\sin x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n+1)!}}x^{2n+1}&&=x-{\frac {x^{3}}{3!}}+{\frac {x^{5}}{5!}}-\cdots &&{\text{for all }}x\\[6pt]\cos x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n)!}}x^{2n}&&=1-{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}-\cdots &&{\text{for all }}x\\[6pt]\tan x&=\sum _{n=1}^{\infty }{\frac {B_{2n}(-4)^{n}\left(1-4^{n}\right)}{(2n)!}}x^{2n-1}&&=x+{\frac {x^{3}}{3}}+{\frac {2x^{5}}{15}}+\cdots &&{\text{for }}|x|<{\frac {\pi }{2}}\\[6pt]\sec x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}E_{2n}}{(2n)!}}x^{2n}&&=1+{\frac {x^{2}}{2}}+{\frac {5x^{4}}{24}}+\cdots &&{\text{for }}|x|<{\frac {\pi }{2}}\\[6pt]\arcsin x&=\sum _{n=0}^{\infty }{\frac {(2n)!}{4^{n}(n!)^{2}(2n+1)}}x^{2n+1}&&=x+{\frac {x^{3}}{6}}+{\frac {3x^{5}}{40}}+\cdots &&{\text{for }}|x|\leq 1\\[6pt]\arccos x&={\frac {\pi }{2}}-\arcsin x&&={\frac {\pi }{2}}-x-{\frac {x^{3}}{6}}-{\frac {3x^{5}}{40}}-\cdots &&{\text{for }}|x|\leq 1\\[6pt]\arctan x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{2n+1}}x^{2n+1}&&=x-{\frac {x^{3}}{3}}+{\frac {x^{5}}{5}}-\cdots &&{\text{for }}|x|\leq 1,\ x\neq \pm i\end{aligned}}$

All angles are expressed in radians. The numbers *Bk* appearing in the expansions of tan *x* are the Bernoulli numbers. The *E**k* in the expansion of sec *x* are Euler numbers.

### Hyperbolic functions

The hyperbolic functions have Maclaurin series closely related to the series for the corresponding trigonometric functions: ${\begin{aligned}\sinh x&=\sum _{n=0}^{\infty }{\frac {x^{2n+1}}{(2n+1)!}}&&=x+{\frac {x^{3}}{3!}}+{\frac {x^{5}}{5!}}+\cdots &&{\text{for all }}x\\[6pt]\cosh x&=\sum _{n=0}^{\infty }{\frac {x^{2n}}{(2n)!}}&&=1+{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}+\cdots &&{\text{for all }}x\\[6pt]\tanh x&=\sum _{n=1}^{\infty }{\frac {B_{2n}4^{n}\left(4^{n}-1\right)}{(2n)!}}x^{2n-1}&&=x-{\frac {x^{3}}{3}}+{\frac {2x^{5}}{15}}-{\frac {17x^{7}}{315}}+\cdots &&{\text{for }}|x|<{\frac {\pi }{2}}\\[6pt]\operatorname {arsinh} x&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}(2n)!}{4^{n}(n!)^{2}(2n+1)}}x^{2n+1}&&=x-{\frac {x^{3}}{6}}+{\frac {3x^{5}}{40}}-\cdots &&{\text{for }}|x|\leq 1\\[6pt]\operatorname {artanh} x&=\sum _{n=0}^{\infty }{\frac {x^{2n+1}}{2n+1}}&&=x+{\frac {x^{3}}{3}}+{\frac {x^{5}}{5}}+\cdots &&{\text{for }}|x|\leq 1,\ x\neq \pm 1\end{aligned}}$

The numbers *Bk* appearing in the series for tanh *x* are the Bernoulli numbers.

### Polylogarithmic functions

The polylogarithms have these defining identities: ${\begin{aligned}{\text{Li}}_{2}(x)&=\sum _{n=1}^{\infty }{\frac {1}{n^{2}}}x^{n}\\{\text{Li}}_{3}(x)&=\sum _{n=1}^{\infty }{\frac {1}{n^{3}}}x^{n}\end{aligned}}$

The Legendre chi functions are defined as follows: ${\begin{aligned}\chi _{2}(x)&=\sum _{n=0}^{\infty }{\frac {1}{(2n+1)^{2}}}x^{2n+1}\\\chi _{3}(x)&=\sum _{n=0}^{\infty }{\frac {1}{(2n+1)^{3}}}x^{2n+1}\end{aligned}}$

And the formulas presented below are called *inverse tangent integrals*: ${\begin{aligned}{\text{Ti}}_{2}(x)&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n+1)^{2}}}x^{2n+1}\\{\text{Ti}}_{3}(x)&=\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{(2n+1)^{3}}}x^{2n+1}\end{aligned}}$

These formulas occur in statistical mechanics. Integrals encountered in Bose–Einstein and Fermi–Dirac statistics can be expressed in terms of polylogarithms. The inverse tangent integral value ${\text{Ti}}_{2}(1/{\sqrt {3}})$ appears in the per-site entropy of spanning trees on a large triangular lattice.

### Elliptic functions

The complete elliptic integrals of first kind K and of second kind E can be defined as follows: ${\begin{aligned}{\frac {2}{\pi }}K(x)&=\sum _{n=0}^{\infty }{\frac {[(2n)!]^{2}}{16^{n}(n!)^{4}}}x^{2n}\\{\frac {2}{\pi }}E(x)&=\sum _{n=0}^{\infty }{\frac {[(2n)!]^{2}}{(1-2n)16^{n}(n!)^{4}}}x^{2n}\end{aligned}}$

The Jacobi theta functions describe the world of the elliptic modular functions and they have these Taylor series: ${\begin{aligned}\vartheta _{00}(x)&=1+2\sum _{n=1}^{\infty }x^{n^{2}}\\\vartheta _{01}(x)&=1+2\sum _{n=1}^{\infty }(-1)^{n}x^{n^{2}}\end{aligned}}$
