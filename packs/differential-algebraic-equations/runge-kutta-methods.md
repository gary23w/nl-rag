---
title: "Runge–Kutta methods"
source: https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods
domain: differential-algebraic-equations
license: CC-BY-SA-4.0
tags: differential-algebraic equations, backward differentiation formula, method of lines, runge-kutta methods
fetched: 2026-07-02
---

# Runge–Kutta methods

In numerical analysis, the **Runge–Kutta methods** (English: /ˈrʊŋəˈkʊtɑː/ ⓘ *RUUNG-ə-KUUT-tah*) are a family of implicit and explicit iterative methods, which include the Euler method, used in temporal discretization for the approximate solutions of simultaneous nonlinear equations. These methods were developed around 1900 by the German mathematicians Carl Runge and Wilhelm Kutta.

## The Runge–Kutta method

The most widely known member of the Runge–Kutta family is generally referred to as "RK4", the "classic Runge–Kutta method" or simply as "the Runge–Kutta method".

Let an initial value problem be specified as follows:

${\frac {dy}{dt}}=f(t,y),\quad y(t_{0})=y_{0}.$

Here y is an unknown function (scalar or vector) of time t , which we would like to approximate; we are told that ${\frac {dy}{dt}}$ , the rate at which y changes, is a function of t and of y itself. At the initial time $t_{0}$ the corresponding y value is $y_{0}$ . The function f and the initial conditions $t_{0}$ , $y_{0}$ are given.

Now we pick a step-size *h* > 0 and define:

${\begin{aligned}y_{n+1}&=y_{n}+{\frac {h}{6}}\left(k_{1}+2k_{2}+2k_{3}+k_{4}\right),\\t_{n+1}&=t_{n}+h\\\end{aligned}}$

for *n* = 0, 1, 2, 3, ..., using

${\begin{aligned}k_{1}&=\ f(t_{n},y_{n}),\\k_{2}&=\ f\!\left(t_{n}+{\frac {h}{2}},y_{n}+k_{1}{\frac {h}{2}}\right),\\k_{3}&=\ f\!\left(t_{n}+{\frac {h}{2}},y_{n}+k_{2}{\frac {h}{2}}\right),\\k_{4}&=\ f\!\left(t_{n}+h,y_{n}+hk_{3}\right).\end{aligned}}$

(*Note: the above equations have different but equivalent definitions in different texts.*)

Here $y_{n+1}$ is the RK4 approximation of $y(t_{n+1})$ , and the next value ( $y_{n+1}$ ) is determined by the present value ( $y_{n}$ ) plus the weighted average of four increments, where each increment is the product of the size of the interval, *h*, and an estimated slope specified by function *f* on the right-hand side of the differential equation.

- $k_{1}$ is the slope at the beginning of the interval, using y (Euler's method);
- $k_{2}$ is the slope at the midpoint of the interval, using y and $k_{1}$ ;
- $k_{3}$ is again the slope at the midpoint, but now using y and $k_{2}$ ;
- $k_{4}$ is the slope at the end of the interval, using y and $k_{3}$ .

In averaging the four slopes, greater weight is given to the slopes at the midpoint. If f is independent of y , so that the differential equation is equivalent to a simple integral, then RK4 is Simpson's rule.

The RK4 method is a fourth-order method, meaning that the local truncation error is on the order of $O(h^{5})$ , while the total accumulated error is on the order of $O(h^{4})$ .

In many practical applications the function f is independent of t (so called autonomous system, or time-invariant system, especially in physics), and their increments are not computed at all and not passed to function f , with only the final formula for $t_{n+1}$ used.

## Explicit Runge–Kutta methods

The family of explicit Runge–Kutta methods is a generalization of the RK4 method mentioned above. It is given by

$y_{n+1}=y_{n}+h\sum _{i=1}^{s}b_{i}k_{i},$

where

${\begin{aligned}k_{1}&=f(t_{n},y_{n}),\\k_{2}&=f(t_{n}+c_{2}h,y_{n}+(a_{21}k_{1})h),\\k_{3}&=f(t_{n}+c_{3}h,y_{n}+(a_{31}k_{1}+a_{32}k_{2})h),\\&\ \ \vdots \\k_{s}&=f(t_{n}+c_{s}h,y_{n}+(a_{s1}k_{1}+a_{s2}k_{2}+\cdots +a_{s,s-1}k_{s-1})h).\end{aligned}}$

(

Note: the above equations may have different but equivalent definitions in some texts.

)

To specify a particular method, one needs to provide the integer *s* (the number of stages), and the coefficients *aij* (for 1 ≤ *j* < *i* ≤ *s*), *bi* (for *i* = 1, 2, ..., *s*) and *ci* (for *i* = 2, 3, ..., *s*). The matrix [*aij*] is called the *Runge–Kutta matrix*, while the *bi* and *ci* are known as the *weights* and the *nodes*. These data are usually arranged in a mnemonic device, known as a *Butcher tableau* (after John C. Butcher):

| 0 |   |   |   |   |   |
|---|---|---|---|---|---|
| $c_{2}$ | $a_{21}$ |   |   |   |   |
| $c_{3}$ | $a_{31}$ | $a_{32}$ |   |   |   |
| $\vdots$ | $\vdots$ |   | $\ddots$ |   |   |
| $c_{s}$ | $a_{s1}$ | $a_{s2}$ | $\cdots$ | $a_{s,s-1}$ |   |
|   | $b_{1}$ | $b_{2}$ | $\cdots$ | $b_{s-1}$ | $b_{s}$ |

A Taylor series expansion shows that the Runge–Kutta method is consistent if and only if

$\sum _{i=1}^{s}b_{i}=1.$

There are also accompanying requirements if one requires the method to have a certain order *p*, meaning that the local truncation error is O(*hp*+1). These can be derived from the definition of the truncation error itself. For example, a two-stage method has order 2 if *b*1 + *b*2 = 1, *b*2*c*2 = 1/2, and *b*2*a*21 = 1/2. Note that a popular condition for determining coefficients is

$\sum _{j=1}^{i-1}a_{ij}=c_{i}{\text{ for }}i=2,\ldots ,s.$

This condition alone, however, is neither sufficient, nor necessary for consistency.

In general, if an explicit s -stage Runge–Kutta method has order p , then it can be proven that the number of stages must satisfy $s\geq p$ and if $p\geq 5$ , then $s\geq p+1$ . However, it is not known whether these bounds are *sharp* in all cases. In some cases, it is proven that the bound cannot be achieved. For instance, Butcher proved that for $p>6$ , there is no explicit method with $s=p+1$ stages. Butcher also proved that for $p>7$ , there is no explicit Runge-Kutta method with $p+2$ stages. In general, however, it remains an open problem what the precise minimum number of stages s is for an explicit Runge–Kutta method to have order p . Some values which are known are:

${\begin{array}{c|cccccccc}p&1&2&3&4&5&6&7&8\\\hline \min s&1&2&3&4&6&7&9&11\end{array}}$

The provable bound above then implies that we cannot find methods of orders $p=1,2,\ldots ,6$ that require fewer stages than the methods we already know for these orders. The work of Butcher also proves that 7th and 8th order methods have a minimum of 9 and 11 stages, respectively. An example of an explicit method of order 6 with 7 stages can be found in Ref. Explicit methods of order 7 with 9 stages and explicit methods of order 8 with 11 stages are also known. See Refs. for a summary.

### Examples

The RK4 method falls in this framework. Its tableau is

| 0 |   |   |   |   |
|---|---|---|---|---|
| 1/2 | 1/2 |   |   |   |
| 1/2 | 0 | 1/2 |   |   |
| 1 | 0 | 0 | 1 |   |
|   | 1/6 | 1/3 | 1/3 | 1/6 |

A slight variation of "the" Runge–Kutta method is also due to Kutta in 1901 and is called the 3/8-rule. The primary advantage this method has is that almost all of the error coefficients are smaller than in the popular method, but it requires slightly more floating-point operations per time step. Its Butcher tableau is

| 0 |   |   |   |   |
|---|---|---|---|---|
| 1/3 | 1/3 |   |   |   |
| 2/3 | −1/3 | 1 |   |   |
| 1 | 1 | −1 | 1 |   |
|   | 1/8 | 3/8 | 3/8 | 1/8 |

However, the simplest Runge–Kutta method is the (forward) Euler method, given by the formula $y_{n+1}=y_{n}+hf(t_{n},y_{n})$ . This is the only consistent explicit Runge–Kutta method with one stage. The corresponding tableau is

| 0 |   |
|---|---|
|   | 1 |

### Second-order methods with two stages

An example of a second-order method with two stages is provided by the explicit midpoint method:

$y_{n+1}=y_{n}+hf\left(t_{n}+{\frac {1}{2}}h,y_{n}+{\frac {1}{2}}hf(t_{n},\ y_{n})\right).$

The corresponding tableau is

| 0 |   |   |
|---|---|---|
| 1/2 | 1/2 |   |
|   | 0 | 1 |

The midpoint method is not the only second-order Runge–Kutta method with two stages; there is a family of such methods, parameterized by α and given by the formula

$y_{n+1}=y_{n}+h{\bigl (}(1-{\tfrac {1}{2\alpha }})f(t_{n},y_{n})+{\tfrac {1}{2\alpha }}f(t_{n}+\alpha h,y_{n}+\alpha hf(t_{n},y_{n})){\bigr )}.$

Its Butcher tableau is

| 0 |   |   |
|---|---|---|
| $\alpha$ | $\alpha$ |   |
|   | $(1-{\tfrac {1}{2\alpha }})$ | ${\tfrac {1}{2\alpha }}$ |

In this family, $\alpha ={\tfrac {1}{2}}$ gives the midpoint method, $\alpha =1$ is Heun's method, and $\alpha ={\tfrac {2}{3}}$ is Ralston's method.

## Use

As an example, consider the two-stage second-order Runge–Kutta method with α = 2/3, also known as Ralston method. It is given by the tableau

|   | 0 |   |   |
|---|---|---|---|
|   | 2/3 | 2/3 |   |
|   |   | 1/4 | 3/4 |

with the corresponding equations

${\begin{aligned}k_{1}&=f(t_{n},\ y_{n}),\\k_{2}&=f(t_{n}+{\tfrac {2}{3}}h,\ y_{n}+{\tfrac {2}{3}}hk_{1}),\\y_{n+1}&=y_{n}+h\left({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2}\right).\end{aligned}}$

This method is used to solve the initial-value problem

${\frac {dy}{dt}}=\tan(y)+1,\quad y_{0}=1,\ t\in [1,1.1]$

with step size *h* = 0.025, so the method needs to take four steps.

The method proceeds as follows:

| $t_{0}=1\colon$ |   |   |   |
|---|---|---|---|
|   | $y_{0}=1$ |   |   |
| $t_{1}=1.025\colon$ |   |   |   |
|   | $y_{0}=1$ | $k_{1}=2.557407725$ | $k_{2}=f(t_{0}+{\tfrac {2}{3}}h,\ y_{0}+{\tfrac {2}{3}}hk_{1})=2.7138981400$ |
|   | $y_{1}=y_{0}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.066869388}}$ |   |   |
| $t_{2}=1.05\colon$ |   |   |   |
|   | $y_{1}=1.066869388$ | $k_{1}=2.813524695$ | $k_{2}=f(t_{1}+{\tfrac {2}{3}}h,\ y_{1}+{\tfrac {2}{3}}hk_{1})$ |
|   | $y_{2}=y_{1}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.141332181}}$ |   |   |
| $t_{3}=1.075\colon$ |   |   |   |
|   | $y_{2}=1.141332181$ | $k_{1}=3.183536647$ | $k_{2}=f(t_{2}+{\tfrac {2}{3}}h,\ y_{2}+{\tfrac {2}{3}}hk_{1})$ |
|   | $y_{3}=y_{2}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.227417567}}$ |   |   |
| $t_{4}=1.1\colon$ |   |   |   |
|   | $y_{3}=1.227417567$ | $k_{1}=3.796866512$ | $k_{2}=f(t_{3}+{\tfrac {2}{3}}h,\ y_{3}+{\tfrac {2}{3}}hk_{1})$ |
|   | $y_{4}=y_{3}+h({\tfrac {1}{4}}k_{1}+{\tfrac {3}{4}}k_{2})={\underline {1.335079087}}.$ |   |   |

The numerical solutions correspond to the underlined values.

## Implicit Runge–Kutta methods

Explicit Runge–Kutta methods are generally unsuitable for the solution of stiff equations because their region of absolute stability is small; in particular, it is bounded. This issue is especially important in the solution of partial differential equations.

The instability of explicit Runge–Kutta methods motivates the development of implicit methods. An implicit Runge–Kutta method has the form

$y_{n+1}=y_{n}+h\sum _{i=1}^{s}b_{i}k_{i},$

where

$k_{i}=f\left(t_{n}+c_{i}h,\ y_{n}+h\sum _{j=1}^{s}a_{ij}k_{j}\right),\quad i=1,\ldots ,s.$

The difference with an explicit method is that in an explicit method, the sum over *j* only goes up to *i* − 1. This also shows up in the Butcher tableau: the coefficient matrix $a_{ij}$ of an explicit method is lower triangular. In an implicit method, the sum over *j* goes up to *s* and the coefficient matrix is not strictly triangular, yielding a Butcher tableau of the form

${\begin{array}{c|cccc}c_{1}&a_{11}&a_{12}&\dots &a_{1s}\\c_{2}&a_{21}&a_{22}&\dots &a_{2s}\\\vdots &\vdots &\vdots &\ddots &\vdots \\c_{s}&a_{s1}&a_{s2}&\dots &a_{ss}\\\hline &b_{1}&b_{2}&\dots &b_{s}\\\end{array}}={\begin{array}{c|c}\mathbf {c} &A\\\hline &\mathbf {b^{T}} \\\end{array}}$

The consequence of this difference is that at every step, a system of algebraic equations has to be solved. This increases the computational cost considerably. If a method with *s* stages is used to solve a differential equation with *m* components, then the system of algebraic equations has *ms* components. This can be contrasted with implicit linear multistep methods (the other big family of methods for ODEs): an implicit *s*-step linear multistep method needs to solve a system of algebraic equations with only *m* components, so the size of the system does not increase as the number of steps increases.

### Examples

The simplest example of an implicit Runge–Kutta method is the backward Euler method:

$y_{n+1}=y_{n}+hf(t_{n}+h,\ y_{n+1}).\,$

The Butcher tableau for this is simply:

${\begin{array}{c|c}1&1\\\hline &1\\\end{array}}$

This Butcher tableau corresponds to the formulae

$k_{1}=f(t_{n}+h,\ y_{n}+hk_{1})\quad {\text{and}}\quad y_{n+1}=y_{n}+hk_{1},$

which can be re-arranged to get the formula for the backward Euler method listed above.

Another example for an implicit Runge–Kutta method is the trapezoidal rule. Its Butcher tableau is:

${\begin{array}{c|cc}0&0&0\\1&{\frac {1}{2}}&{\frac {1}{2}}\\\hline &{\frac {1}{2}}&{\frac {1}{2}}\\&1&0\\\end{array}}$

The trapezoidal rule is a collocation method (as discussed in that article). All collocation methods are implicit Runge–Kutta methods, but not all implicit Runge–Kutta methods are collocation methods.

The Gauss–Legendre methods form a family of collocation methods based on Gauss quadrature. A Gauss–Legendre method with *s* stages has order 2*s* (thus, methods with arbitrarily high order can be constructed). The method with two stages (and thus order four) has Butcher tableau:

${\begin{array}{c|cc}{\frac {1}{2}}-{\frac {1}{6}}{\sqrt {3}}&{\frac {1}{4}}&{\frac {1}{4}}-{\frac {1}{6}}{\sqrt {3}}\\{\frac {1}{2}}+{\frac {1}{6}}{\sqrt {3}}&{\frac {1}{4}}+{\frac {1}{6}}{\sqrt {3}}&{\frac {1}{4}}\\\hline &{\frac {1}{2}}&{\frac {1}{2}}\\&{\frac {1}{2}}+{\frac {1}{2}}{\sqrt {3}}&{\frac {1}{2}}-{\frac {1}{2}}{\sqrt {3}}\end{array}}$

### Stability

The advantage of implicit Runge–Kutta methods over explicit ones is their greater stability, especially when applied to stiff equations. Consider the linear test equation $y'=\lambda y$ . A Runge–Kutta method applied to this equation reduces to the iteration $y_{n+1}=r(h\lambda )\,y_{n}$ , with *r* given by

$r(z)=1+zb^{T}(I-zA)^{-1}e={\frac {\det(I-zA+zeb^{T})}{\det(I-zA)}},$

where *e* stands for the vector of ones. The function *r* is called the *stability function*. It follows from the formula that *r* is the quotient of two polynomials of degree *s* if the method has *s* stages. Explicit methods have a strictly lower triangular matrix *A*, which implies that det(*I* − *zA*) = 1 and that the stability function is a polynomial.

The numerical solution to the linear test equation decays to zero if | *r*(*z*) | < 1 with *z* = *h*λ. The set of such *z* is called the *domain of absolute stability*. In particular, the method is said to be absolute stable if all *z* with Re(*z*) < 0 are in the domain of absolute stability. The stability function of an explicit Runge–Kutta method is a polynomial, so explicit Runge–Kutta methods can never be A-stable.

If the method has order *p*, then the stability function satisfies $r(z)={\textrm {e}}^{z}+O(z^{p+1})$ as $z\to 0$ . Thus, it is of interest to study quotients of polynomials of given degrees that approximate the exponential function the best. These are known as Padé approximants. A Padé approximant with numerator of degree *m* and denominator of degree *n* is A-stable if and only if *m* ≤ *n* ≤ *m* + 2.

The Gauss–Legendre method with *s* stages has order 2*s*, so its stability function is the Padé approximant with *m* = *n* = *s*. It follows that the method is A-stable. This shows that A-stable Runge–Kutta can have arbitrarily high order. In contrast, the order of A-stable linear multistep methods cannot exceed two.

## Adaptive Runge–Kutta methods

Adaptive methods are designed to produce an estimate of the local truncation error of a single Runge–Kutta step. This is done by having two methods, one with order p and one with order $p-1$ . These methods are interwoven, i.e., they have common intermediate steps. Thanks to this, estimating the error has little or negligible computational cost compared to a step with the higher-order method.

During the integration, the step size is adapted such that the estimated error stays below a user-defined threshold: If the error is too high, a step is repeated with a lower step size; if the error is much smaller, the step size is increased to save time. This results in an (almost), optimal step size, which saves computation time. Moreover, the user does not have to spend time on finding an appropriate step size.

The lower-order step is given by

$y_{n+1}^{*}=y_{n}+h\sum _{i=1}^{s}b_{i}^{*}k_{i},$

where $k_{i}$ are the same as for the higher-order method. Then the error is

$e_{n+1}=y_{n+1}-y_{n+1}^{*}=h\sum _{i=1}^{s}(b_{i}-b_{i}^{*})k_{i},$

which is $O(h^{p})$ . The Butcher tableau for this kind of method is extended to give the values of $b_{i}^{*}$ :

${\begin{array}{c|cccc}c_{1}&a_{11}&a_{12}&\dots &a_{1s}\\c_{2}&a_{21}&a_{22}&\dots &a_{2s}\\\vdots &\vdots &\vdots &\ddots &\vdots \\c_{s}&a_{s1}&a_{s2}&\dots &a_{ss}\\\hline &b_{1}&b_{2}&\dots &b_{s}\\&b_{1}^{*}&b_{2}^{*}&\dots &b_{s}^{*}\\\end{array}}$

The Runge–Kutta–Fehlberg method has two methods of orders 5 and 4. Its extended Butcher tableau is:

|   | 0 |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   | 1/4 | 1/4 |   |   |   |   |   |
|   | 3/8 | 3/32 | 9/32 |   |   |   |   |
|   | 12/13 | 1932/2197 | −7200/2197 | 7296/2197 |   |   |   |
|   | 1 | 439/216 | −8 | 3680/513 | -845/4104 |   |   |
|   | 1/2 | −8/27 | 2 | −3544/2565 | 1859/4104 | −11/40 |   |
|   |   | 16/135 | 0 | 6656/12825 | 28561/56430 | −9/50 | 2/55 |
|   |   | 25/216 | 0 | 1408/2565 | 2197/4104 | −1/5 | 0 |

However, the simplest adaptive Runge–Kutta method involves combining Heun's method, which is order 2, with the Euler method, which is order 1. Its extended Butcher tableau is:

|   | 0 |   |   |
|---|---|---|---|
|   | 1 | 1 |   |
|   |   | 1/2 | 1/2 |
|   |   | 1 | 0 |

Other adaptive Runge–Kutta methods are the Bogacki–Shampine method (orders 3 and 2), the Cash–Karp method and the Dormand–Prince method (both with orders 5 and 4).

## Nonconfluent Runge–Kutta methods

A Runge–Kutta method is said to be *nonconfluent* if all the $c_{i},\,i=1,2,\ldots ,s$ are distinct.

## Runge–Kutta–Nyström methods

Runge–Kutta–Nyström (RKN) methods are a family of methods based on the same principles as Runge–Kutta methods but for second-order initial value problems, hence problems of the form :

${\frac {d^{2}y}{dt^{2}}}=f(t,{\frac {dy}{dt}},y),\quad y(t_{0})=y_{0},\quad {\frac {dy}{dt}}(t_{0})=y'_{0}.$

There are two derivatives two approximates, a Runge-Kutta-Nyström methods hence uses two Runge-Kutta matrices $a_{ij},a'_{ij}$ , and two sets of weights $b_{i},b'_{i}$ , but still only needs one set of nodes $c_{i}$ . This yields a Butcher table with the form :

${\begin{array}{c|cccc}c_{1}&a_{11}&a_{12}&\dots &a_{1s}\\c_{2}&a_{21}&a_{22}&\dots &a_{2s}\\\vdots &\vdots &\vdots &\ddots &\vdots \\c_{s}&a_{s1}&a_{s2}&\dots &a_{ss}\\\hline &a'_{11}&a'_{12}&\dots &a'_{1s}\\&a'_{21}&a'_{22}&\dots &a'_{2s}\\&\vdots &\vdots &\ddots &\vdots \\&a'_{s1}&a'_{s2}&\dots &a'_{ss}\\\hline &b_{1}&b_{2}&\dots &b_{s}\\&b'_{1}&b'_{2}&\dots &b'_{s}\\\end{array}}={\begin{array}{c|c}\mathbf {c} &\mathbf {A} \\\hline &\mathbf {A'} \\\hline &\mathbf {b} ^{\top }\\&\mathbf {b'} ^{\top }\end{array}}$

Assume the approximations have been carried out up to $t_{n}$ , with $y_{n}$ the approximation of $y(t_{n})$ and $y'_{n}$ the approximation of ${\frac {dy}{dt}}(t_{n})$ . The approximations $y_{n+1},y'_{n+1}$ at $t_{n+1}=t_{n}+h$ are the solutions of the following system :

${\begin{cases}g_{i}=y_{n}+c_{i}hy'_{n}+h^{2}\sum _{j=1}^{s}a_{ij}f(t_{n}+c_{j}h,g'_{j},g_{j}),&i=1,2,\ldots ,s\\g'_{i}=y'_{n}+h\sum _{j=1}^{s}a'_{ij}f(t_{n}+c_{j}h,g'_{j},g_{j}),&i=1,2,\ldots ,s\\\\y_{n+1}=y_{n}+hy'_{n}+h^{2}\sum _{j=1}^{s}b_{j}f(t_{n}+c_{j}h,g'_{j},g_{j})\\y'_{n+1}=y'_{n}+h\sum _{j=1}^{s}b'_{j}f(t_{n}+c_{j}h,g'_{j},g_{j})\end{cases}}$

Where $g_{i},g'_{i}$ are the intermediate approximations of y and ${\frac {dy}{dt}}$ . It is strictly equivalent to work with the values $k_{j}=f(t_{n}+c_{j}h,g'_{j},g_{j})$ where the $g_{j},g'_{j}$ have been replaced with their formula, instead of working with $g_{i},g'_{i}$ , similarly to what we previously did with Runge-Kutta methods, but the system is easier to write this way.

A Runge-Kutta-Nyström method is said to be explicit if both $A,A'$ are strictly lower triangular, and in this case, the sums ${\textstyle \sum _{j=1}^{s}}$ in the expressions of $g_{i},g'_{i}$ , may be replaced with ${\textstyle \sum _{j=1}^{i-1}}$ . Additionally, a Runge-Kutta-Nyström method is said to be of order p if the local truncation error of both $y_{n+1},y'_{n+1}$ is $O(h^{p+1})$ .

If the function f of the considered initial value problem is independent of ${\frac {dy}{dt}}$ , one does not need to approximate the intermediate values $g'_{i}$ to compute the approximations, the weights $a'_{ij}$ are hence useless and instead we write a method made only for this special case using a tableau of the form :

${\begin{array}{c|cccc}c_{1}&a_{11}&a_{12}&\dots &a_{1s}\\c_{2}&a_{21}&a_{22}&\dots &a_{2s}\\\vdots &\vdots &\vdots &\ddots &\vdots \\c_{s}&a_{s1}&a_{s2}&\dots &a_{ss}\\\hline &b_{1}&b_{2}&\dots &b_{s}\\&b'_{1}&b'_{2}&\dots &b'_{s}\\\end{array}}={\begin{array}{c|c}\mathbf {c} &\mathbf {A} \\\hline &\mathbf {b} ^{\top }\\&\mathbf {b'} ^{\top }\end{array}}$

This special case is particularly interesting since it allows for greater order than what a Runge-Kutta-Nyström can achieve in general. For example, two fourth-order explicit RKN methods are given by the following Butcher tableau:

${\begin{array}{c|ccc}c_{i}&&a_{ij}&\\{\frac {3+{\sqrt {3}}}{6}}&0&0&0\\{\frac {3-{\sqrt {3}}}{6}}&{\frac {2-{\sqrt {3}}}{12}}&0&0\\{\frac {3+{\sqrt {3}}}{6}}&0&{\frac {\sqrt {3}}{6}}&0\\\hline b_{i}&{\frac {3-2{\sqrt {3}}}{12}}&{\frac {1}{2}}&{\frac {3+2{\sqrt {3}}}{12}}\\\hline b'_{i}&{\frac {5-3{\sqrt {3}}}{24}}&{\frac {3+{\sqrt {3}}}{12}}&{\frac {1+{\sqrt {3}}}{24}}\\\end{array}}$ ${\begin{array}{c|ccc}c_{i}&&a_{ij}&\\{\frac {3-{\sqrt {3}}}{6}}&0&0&0\\{\frac {3+{\sqrt {3}}}{6}}&{\frac {2+{\sqrt {3}}}{12}}&0&0\\{\frac {3-{\sqrt {3}}}{6}}&0&-{\frac {\sqrt {3}}{6}}&0\\\hline b_{i}&{\frac {3+2{\sqrt {3}}}{12}}&{\frac {1}{2}}&{\frac {3-2{\sqrt {3}}}{12}}\\\hline b'_{i}&{\frac {5+3{\sqrt {3}}}{24}}&{\frac {3-{\sqrt {3}}}{12}}&{\frac {1-{\sqrt {3}}}{24}}\\\end{array}}$

These two schemes also have the symplectic-preserving properties when the original equation is derived from a conservative classical mechanical system, i.e. when

$f_{i}(x_{1},\ldots ,x_{n})={\frac {\partial V}{\partial x_{i}}}(x_{1},\ldots ,x_{n})$

for some scalar function V .

## B-stability

The *A-stability* concept for the solution of differential equations is related to the linear autonomous equation $y'=\lambda y$ . Dahlquist (1963) proposed the investigation of stability of numerical schemes when applied to nonlinear systems that satisfy a monotonicity condition. The corresponding concepts were defined as *G-stability* for multistep methods (and the related one-leg methods) and *B-stability* (Butcher, 1975) for Runge–Kutta methods. A Runge–Kutta method applied to the non-linear system $y'=f(y)$ , which verifies $\langle f(y)-f(z),\ y-z\rangle \leq 0$ , is called *B-stable*, if this condition implies $\|y_{n+1}-z_{n+1}\|\leq \|y_{n}-z_{n}\|$ for two numerical solutions.

Let B , M and Q be three $s\times s$ matrices defined by ${\begin{aligned}B&=\operatorname {diag} (b_{1},b_{2},\ldots ,b_{s}),\\[4pt]M&=BA+A^{T}B-bb^{T},\\[4pt]Q&=BA^{-1}+A^{-T}B-A^{-T}bb^{T}A^{-1}.\end{aligned}}$ A Runge–Kutta method is said to be *algebraically stable* if the matrices B and M are both non-negative definite. A sufficient condition for *B-stability* is: B and Q are non-negative definite.

## Derivation of the Runge–Kutta fourth-order method

In general a Runge–Kutta method of order s can be written as:

$y_{t+h}=y_{t}+h\cdot \sum _{i=1}^{s}a_{i}k_{i}+{\mathcal {O}}(h^{s+1}),$

where:

$k_{i}=\sum _{j=1}^{s}\beta _{ij}f(k_{j},\ t_{n}+\alpha _{i}h)$

are increments obtained evaluating the derivatives of $y_{t}$ at the i -th order.

We develop the derivation for the Runge–Kutta fourth-order method using the general formula with $s=4$ evaluated, as explained above, at the starting point, the midpoint and the end point of any interval $(t,\ t+h)$ ; thus, we choose:

${\begin{aligned}&\alpha _{i}&&\beta _{ij}\\\alpha _{1}&=0&\beta _{21}&={\frac {1}{2}}\\\alpha _{2}&={\frac {1}{2}}&\beta _{32}&={\frac {1}{2}}\\\alpha _{3}&={\frac {1}{2}}&\beta _{43}&=1\\\alpha _{4}&=1&&\\\end{aligned}}$

and $\beta _{ij}=0$ otherwise. We begin by defining the following quantities:

${\begin{aligned}y_{t+h}^{1}&=y_{t}+hf\left(y_{t},\ t\right)\\y_{t+h}^{2}&=y_{t}+hf\left(y_{t+h/2}^{1},\ t+{\frac {h}{2}}\right)\\y_{t+h}^{3}&=y_{t}+hf\left(y_{t+h/2}^{2},\ t+{\frac {h}{2}}\right)\end{aligned}}$

where $y_{t+h/2}^{1}={\dfrac {y_{t}+y_{t+h}^{1}}{2}}$ and $y_{t+h/2}^{2}={\dfrac {y_{t}+y_{t+h}^{2}}{2}}.$ If we define:

${\begin{aligned}k_{1}&=f(y_{t},\ t)\\k_{2}&=f\left(y_{t+h/2}^{1},\ t+{\frac {h}{2}}\right)=f\left(y_{t}+{\frac {h}{2}}k_{1},\ t+{\frac {h}{2}}\right)\\k_{3}&=f\left(y_{t+h/2}^{2},\ t+{\frac {h}{2}}\right)=f\left(y_{t}+{\frac {h}{2}}k_{2},\ t+{\frac {h}{2}}\right)\\k_{4}&=f\left(y_{t+h}^{3},\ t+h\right)=f\left(y_{t}+hk_{3},\ t+h\right)\end{aligned}}$

and for the previous relations we can show that the following equalities hold up to ${\mathcal {O}}(h^{2})$ : ${\begin{aligned}k_{2}&=f\left(y_{t+h/2}^{1},\ t+{\frac {h}{2}}\right)=f\left(y_{t}+{\frac {h}{2}}k_{1},\ t+{\frac {h}{2}}\right)\\&=f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f\left(y_{t},\ t\right)\\k_{3}&=f\left(y_{t+h/2}^{2},\ t+{\frac {h}{2}}\right)=f\left(y_{t}+{\frac {h}{2}}f\left(y_{t}+{\frac {h}{2}}k_{1},\ t+{\frac {h}{2}}\right),\ t+{\frac {h}{2}}\right)\\&=f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f\left(y_{t},\ t\right)\right]\\k_{4}&=f\left(y_{t+h}^{3},\ t+h\right)=f\left(y_{t}+hf\left(y_{t}+{\frac {h}{2}}k_{2},\ t+{\frac {h}{2}}\right),\ t+h\right)\\&=f\left(y_{t}+hf\left(y_{t}+{\frac {h}{2}}f\left(y_{t}+{\frac {h}{2}}f\left(y_{t},\ t\right),\ t+{\frac {h}{2}}\right),\ t+{\frac {h}{2}}\right),\ t+h\right)\\&=f\left(y_{t},\ t\right)+h{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f\left(y_{t},\ t\right)\right]\right]\end{aligned}}$ where: ${\frac {d}{dt}}f(y_{t},\ t)={\frac {\partial }{\partial y}}f(y_{t},\ t){\dot {y}}_{t}+{\frac {\partial }{\partial t}}f(y_{t},\ t)=f_{y}(y_{t},\ t){\dot {y}}_{t}+f_{t}(y_{t},\ t):={\ddot {y}}_{t}$ is the total derivative of f with respect to time.

If we now express the general formula using what we just derived we obtain: ${\begin{aligned}y_{t+h}={}&y_{t}+h\left\lbrace a\cdot f(y_{t},\ t)+b\cdot \left[f(y_{t},\ t)+{\frac {h}{2}}{\frac {d}{dt}}f(y_{t},\ t)\right]\right.+\\&{}+c\cdot \left[f(y_{t},\ t)+{\frac {h}{2}}{\frac {d}{dt}}\left[f\left(y_{t},\ t\right)+{\frac {h}{2}}{\frac {d}{dt}}f(y_{t},\ t)\right]\right]+\\&{}+d\cdot \left[f(y_{t},\ t)+h{\frac {d}{dt}}\left[f(y_{t},\ t)+{\frac {h}{2}}{\frac {d}{dt}}\left[f(y_{t},\ t)+\left.{\frac {h}{2}}{\frac {d}{dt}}f(y_{t},\ t)\right]\right]\right]\right\rbrace +{\mathcal {O}}(h^{5})\\={}&y_{t}+a\cdot hf_{t}+b\cdot hf_{t}+b\cdot {\frac {h^{2}}{2}}{\frac {df_{t}}{dt}}+c\cdot hf_{t}+c\cdot {\frac {h^{2}}{2}}{\frac {df_{t}}{dt}}+\\&{}+c\cdot {\frac {h^{3}}{4}}{\frac {d^{2}f_{t}}{dt^{2}}}+d\cdot hf_{t}+d\cdot h^{2}{\frac {df_{t}}{dt}}+d\cdot {\frac {h^{3}}{2}}{\frac {d^{2}f_{t}}{dt^{2}}}+d\cdot {\frac {h^{4}}{4}}{\frac {d^{3}f_{t}}{dt^{3}}}+{\mathcal {O}}(h^{5})\end{aligned}}$

and comparing this with the Taylor series of $y_{t+h}$ around t : ${\begin{aligned}y_{t+h}&=y_{t}+h{\dot {y}}_{t}+{\frac {h^{2}}{2}}{\ddot {y}}_{t}+{\frac {h^{3}}{6}}y_{t}^{(3)}+{\frac {h^{4}}{24}}y_{t}^{(4)}+{\mathcal {O}}(h^{5})=\\&=y_{t}+hf(y_{t},\ t)+{\frac {h^{2}}{2}}{\frac {d}{dt}}f(y_{t},\ t)+{\frac {h^{3}}{6}}{\frac {d^{2}}{dt^{2}}}f(y_{t},\ t)+{\frac {h^{4}}{24}}{\frac {d^{3}}{dt^{3}}}f(y_{t},\ t)\end{aligned}}$

we obtain a system of constraints on the coefficients:

${\begin{cases}&a+b+c+d=1\\[6pt]&{\frac {1}{2}}b+{\frac {1}{2}}c+d={\frac {1}{2}}\\[6pt]&{\frac {1}{4}}c+{\frac {1}{2}}d={\frac {1}{6}}\\[6pt]&{\frac {1}{4}}d={\frac {1}{24}}\end{cases}}$

which when solved gives $a={\frac {1}{6}},b={\frac {1}{3}},c={\frac {1}{3}},d={\frac {1}{6}}$ as stated above.
