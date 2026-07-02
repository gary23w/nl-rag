---
title: "Finite difference"
source: https://en.wikipedia.org/wiki/Finite_difference
domain: finite-difference-methods
license: CC-BY-SA-4.0
tags: finite difference method, crank-nicolson method, upwind scheme, von neumann stability analysis
fetched: 2026-07-02
---

# Finite difference

A **finite difference** is a mathematical expression of the form *f*(*x* + *b*) − *f*(*x* + *a*). Finite differences (or the associated difference quotients) are often used as approximations of derivatives, such as in numerical differentiation.

The difference operator, commonly denoted $\Delta$ (uppercase Delta), is the operator that maps a function f to the function $\Delta [f]$ defined by $\Delta [f](x)=f(x+1)-f(x).$ A difference equation is a functional equation that involves the finite difference operator in the same way as a differential equation involves derivatives. There are many similarities between difference equations and differential equations. Certain recurrence relations can be written as difference equations by replacing iteration notation with finite differences.

In numerical analysis, finite differences are widely used for approximating derivatives, and the term "finite difference" is often used as an abbreviation of "finite difference approximation of derivatives".

Finite differences were introduced by Brook Taylor in 1715 and have also been studied as abstract self-standing mathematical objects in works by George Boole (1860), L. M. Milne-Thomson (1933), and Károly Jordan (1939). Finite differences trace their origins back to one of Jost Bürgi's algorithms (c. 1592) and work by others including Isaac Newton. The formal calculus of finite differences can be viewed as an alternative to the calculus of infinitesimals.

## Basic types

Three basic types are commonly considered: *forward*, *backward*, and *central* finite differences.

A **forward difference**, denoted $\Delta _{h}[f]$ of a function f is a function defined as $\Delta _{h}[f](x)=f(x+h)-f(x).$

Depending on the application, the spacing h may be variable or constant. When not specified, the default value for h is 1; that is, $\Delta [f](x)=\Delta _{1}[f](x)=f(x+1)-f(x).$

A **backward difference** uses the function values at x and *x* − *h*, instead of the values at *x* + *h* and x: $\nabla _{h}[f](x)=f(x)-f(x-h)=\Delta _{h}[f](x-h).$

Finally, the **central difference** is given by $\delta _{h}[f](x)=f(x+{\tfrac {h}{2}})-f(x-{\tfrac {h}{2}})=\Delta _{\tfrac {h}{2}}[f](x)+\nabla _{\tfrac {h}{2}}[f](x).$

## Relation with derivatives

The approximation of derivatives by finite differences plays a central role in finite difference methods for the numerical solution of differential equations, especially boundary value problems.

The derivative of a function f at a point x is defined by the limit $f'(x)=\lim _{h\to 0}{\frac {f(x+h)-f(x)}{h}}.$

If h has a fixed (non-zero) value instead of approaching zero, then the right-hand side of the above equation would be written ${\frac {f(x+h)-f(x)}{h}}={\frac {\Delta _{h}[f](x)}{h}}.$

Hence, the forward difference divided by h approximates the derivative when h is small. The error in this approximation can be derived from Taylor's theorem. Assuming that f is twice differentiable, we have ${\frac {\Delta _{h}[f](x)}{h}}-f'(x)=o(h)\to 0\quad {\text{as }}h\to 0.$

The same formula holds for the backward difference: ${\frac {\nabla _{h}[f](x)}{h}}-f'(x)=o(h)\to 0\quad {\text{as }}h\to 0.$

However, the central (also called centered) difference yields a more accurate approximation. If f is three times differentiable, ${\frac {\delta _{h}[f](x)}{h}}-f'(x)=o\left(h^{2}\right).$

The main problem with the central difference method, however, is that oscillating functions can yield zero derivative. If *f*(*nh*) = 1 for n odd, and *f*(*nh*) = 2 for n even, then *f*′(*nh*) = 0 if it is calculated with the central difference scheme. This is particularly troublesome if the domain of f is discrete. See also Symmetric derivative.

Authors for whom finite differences mean finite difference approximations define the forward/backward/central differences as the quotients given in this section (instead of employing the definitions given in the previous section).

## Higher-order differences

In an analogous way, one can obtain finite difference approximations to higher order derivatives and differential operators. For example, by using the above central difference formula for *f* ′(*x* + ⁠*h*/2⁠) and *f* ′(*x* − ⁠*h*/2⁠) and applying a central difference formula for the derivative of *f* ′ at x, we obtain the central difference approximation of the second derivative of   f :

**Second-order central**

$f''(x)\approx {\frac {\delta _{h}^{2}[f](x)}{h^{2}}}={\frac {{\frac {f(x+h)-f(x)}{h}}-{\frac {f(x)-f(x-h)}{h}}}{h}}={\frac {f(x+h)-2f(x)+f(x-h)}{h^{2}}}~.$

Similarly we can apply other differencing formulas in a recursive manner.

**Second-order forward**

$f''(x)\approx {\frac {\Delta _{h}^{2}[f](x)}{h^{2}}}={\frac {{\frac {f(x+2h)-f(x+h)}{h}}-{\frac {f(x+h)-f(x)}{h}}}{h}}={\frac {f(x+2h)-2f(x+h)+f(x)}{h^{2}}}~.$

**Second-order backward**

$f''(x)\approx {\frac {\nabla _{h}^{2}[f](x)}{h^{2}}}={\frac {{\frac {f(x)-f(x-h)}{h}}-{\frac {f(x-h)-f(x-2h)}{h}}}{h}}={\frac {f(x)-2f(x-h)+f(x-2h)}{h^{2}}}~.$

More generally, the **n-th order forward, backward, and central** differences are given by, respectively,

**Forward**

$\Delta _{h}^{n}[f](x)=\sum _{j=0}^{n}(-1)^{n-j}{\binom {n}{j}}f{\bigl (}x+jh{\bigr )},$

**Backward**

$\nabla _{h}^{n}[f](x)=\sum _{j=0}^{n}(-1)^{j}{\binom {n}{j}}f(x-jh),$

**Central**

$\delta _{h}^{n}[f](x)=\sum _{j=0}^{n}(-1)^{j}{\binom {n}{j}}f\left(x+\left({\frac {n}{2}}-j\right)h\right)~.$

These equations use binomial coefficients after the summation sign shown as ${\textstyle \ {\binom {n}{j}}~.}$ Each row of Pascal's triangle provides the coefficient for each value of   j .

Note that the central difference will, for odd n, have h multiplied by non-integers. This is often a problem because it amounts to changing the interval of discretization. The problem may be remedied substituting the average of ${\textstyle \delta ^{n}[f](x-{\tfrac {h}{2}})}$ and ${\textstyle \delta ^{n}[f](x+{\tfrac {h}{2}}).}$

Forward differences applied to a sequence are sometimes called the binomial transform of the sequence, and have a number of interesting combinatorial properties. Forward differences may be evaluated using the Nörlund–Rice integral. The integral representation for these types of series is interesting, because the integral can often be evaluated using asymptotic expansion or saddle-point techniques; by contrast, the forward difference series can be extremely hard to evaluate numerically, because the binomial coefficients grow rapidly for large n.

The relationship of these higher-order differences with the respective derivatives is straightforward, ${\frac {\mathrm {d} ^{n}f}{(\mathrm {d} x)^{n}}}(x)={\frac {\Delta _{h}^{n}[f](x)}{h^{n}}}+{\mathcal {o}}(h)={\frac {\nabla _{h}^{n}[f](x)}{h^{n}}}+{\mathcal {o}}(h)={\frac {\delta _{h}^{n}[f](x)}{h^{n}}}+{\mathcal {o}}\!\left(h^{2}\right).$

Higher-order differences can also be used to construct better approximations. As mentioned above, the first-order difference approximates the first-order derivative up to a term of order h. However, the combination ${\frac {\Delta _{h}[f](x)-{\frac {1}{2}}\Delta _{h}^{2}[f](x)}{h}}=-{\frac {f(x+2h)-4f(x+h)+3f(x)}{2h}}$ approximates *f* ′(*x*) up to a term of order *h*2. This can be proven by expanding the above expression in Taylor series, or by using the calculus of finite differences, explained below.

If necessary, the finite difference can be centered about any point by mixing forward, backward, and central differences.

Sometimes, the low order derivatives of a function may be analytically known, but high order derivatives are not. In these cases, the high order derivatives can be approximated by finite difference of low order derivatives, which is often more accurate and numerically more stable than finite difference of the function *f* (*x*) itself. This is sometimes called seminumerical differentiation. For example, when the first order derivative *f* ′(*x*) is available but the second order derivative *f* ′′(*x*) is not, the latter can be approximated by second-order central difference of *f* ′(*x*): $f''(x)\approx {\frac {f'(x+h)-f'(x-h)}{2h}}~.$

## Polynomials

For a given polynomial of degree *n* ≥ 1, expressed in the function *P*(*x*), with real numbers *a* ≠ 0 and *b* and *lower order terms* (if any) marked as l.o.t.: $P(x)=ax^{n}+\;bx^{n-1}+~l.o.t.$

After *n* pairwise differences, the following result can be achieved, where *h* ≠ 0 is a real number marking the arithmetic difference: $\Delta _{h}^{n}[P](x)=ah^{n}n!$

Only the coefficient of the highest-order term remains. As this result is constant with respect to *x*, any further pairwise differences will have the value 0.

### Inductive proof

#### Base case

Let *Q*(*x*) be a polynomial of degree 1: $\Delta _{h}[Q](x)=Q(x+h)-Q(x)=[a(x+h)+b]-[ax+b]=ah=ah^{1}1!$

This proves it for the base case.

#### Inductive step

Let *R*(*x*) be a polynomial of degree *m* − 1 where *m* ≥ 2 and the coefficient of the highest-order term be *a* ≠ 0. Assuming the following holds true for all polynomials of degree *m* − 1: $\Delta _{h}^{m-1}[R](x)=ah^{m-1}(m-1)!$

Let *S*(*x*) be a polynomial of degree *m*. With one pairwise difference: $\Delta _{h}[S](x)=[a(x+h)^{m}+b(x+h)^{m-1}+{\text{l.o.t.}}]-[ax^{m}+bx^{m-1}+{\text{l.o.t.}}]=ahmx^{m-1}+{\text{l.o.t.}}=T(x)$

As *ahm* ≠ 0, this results in a polynomial *T*(*x*) of degree *m* − 1, with *ahm* as the coefficient of the highest-order term. Given the assumption above and *m* − 1 pairwise differences (resulting in a total of *m* pairwise differences for *S*(*x*)), it can be found that: $\Delta _{h}^{m-1}[T](x)=ahm\cdot h^{m-1}(m-1)!=ah^{m}m!$

This completes the proof.

### Application

This identity can be used to find the lowest-degree polynomial that intercepts a number of points (*x*, *y*) where the difference on the *x*-axis from one point to the next is a constant *h* ≠ 0. For example, given the following points:

| *x* | *y* |
|---|---|
| 1 | 4 |
| 4 | 109 |
| 7 | 772 |
| 10 | 2641 |
| 13 | 6364 |

We can use a differences table, where for all cells to the right of the first *y*, the following relation to the cells in the column immediately to the left exists for a cell (*a* + 1, *b* + 1), with the top-leftmost cell being at coordinate (0, 0): $(a+1,b+1)=(a,b+1)-(a,b)$

To find the first term, the following table can be used:

| *x* | *y* | Δ*y* | Δ2*y* | Δ3*y* |
|---|---|---|---|---|
| 1 | 4 |   |   |   |
| 4 | 109 | 105 |   |   |
| 7 | 772 | 663 | 558 |   |
| 10 | 2641 | 1869 | 1206 | 648 |
| 13 | 6364 | 3723 | 1854 | 648 |

This arrives at a constant 648. The arithmetic difference is *h* = 3, as established above. Given the number of pairwise differences needed to reach the constant, it can be surmised this is a polynomial of degree 3. Thus, using the identity above: $648=a\cdot 3^{3}\cdot 3!=a\cdot 27\cdot 6=a\cdot 162$

Solving for *a*, it can be found to have the value 4. Thus, the first term of the polynomial is 4*x*3.

Then, subtracting out the first term, which lowers the polynomial's degree, and finding the finite difference again:

| x | y | Δ*y* | Δ2*y* |
|---|---|---|---|
| 1 | 4 − 4(1)3 = 4 − 4 = 0 |   |   |
| 4 | 109 − 4(4)3 = 109 − 256 = −147 | −147 |   |
| 7 | 772 − 4(7)3 = 772 − 1372 = −600 | −453 | −306 |
| 10 | 2641 − 4(10)3 = 2641 − 4000 = −1359 | −759 | −306 |
| 13 | 6364 − 4(13)3 = 6364 − 8788 = −2424 | −1065 | −306 |

Here, the constant is achieved after only two pairwise differences, thus the following result: $-306=a\cdot 3^{2}\cdot 2!=a\cdot 18$

Solving for *a*, which is −17, the polynomial's second term is −17*x*2.

Moving on to the next term, by subtracting out the second term:

| *x* | *y* | Δ*y* |
|---|---|---|
| 1 | 0 − (−17(1)2) = 0 + 17 = 17 |   |
| 4 | −147 − (−17(4)2) = −147 + 272 = 125 | 108 |
| 7 | −600 − (−17(7)2) = −600 + 833 = 233 | 108 |
| 10 | −1359 − (−17(10)2) = −1359 + 1700 = 341 | 108 |
| 13 | −2424 − (−17(13)2) = −2424 + 2873 = 449 | 108 |

Thus the constant is achieved after only one pairwise difference: $108=a\cdot 3^{1}\cdot 1!=a\cdot 3$

It can be found that *a* = 36 and thus the third term of the polynomial is **36*x***. Subtracting out the third term:

| *x* | *y* |
|---|---|
| 1 | 17 − 36(1) = 17 − 36 = −19 |
| 4 | 125 − 36(4) = 125 − 144 = −19 |
| 7 | 233 − 36(7) = 233 − 252 = −19 |
| 10 | 341 − 36(10) = 341 − 360 = −19 |
| 13 | 449 − 36(13) = 449 − 468 = −19 |

Without any pairwise differences, it is found that the 4th and final term of the polynomial is the constant −19. Thus, the lowest-degree polynomial intercepting all the points in the first table is found: $4x^{3}-17x^{2}+36x-19$

## Arbitrarily sized kernels

Using linear algebra one can construct finite difference approximations which utilize an arbitrary number of points to the left and a (possibly different) number of points to the right of the evaluation point, for any order derivative. This involves solving a linear system such that the Taylor expansion of the sum of those points around the evaluation point best approximates the Taylor expansion of the desired derivative. Such formulas can be represented graphically on a hexagonal or diamond-shaped grid. This is useful for differentiating a function on a grid, where, as one approaches the edge of the grid, one must sample fewer and fewer points on one side. Finite difference approximations for non-standard (and even non-integer) stencils given an arbitrary stencil and a desired derivative order may be constructed.

### Properties

- For all positive k and n $\Delta _{kh}^{n}\left(f,x\right)=\sum \limits _{j_{1}=0}^{k-1}\sum \limits _{j_{2}=0}^{k-1}\cdots \sum \limits _{j_{n}=0}^{k-1}\Delta _{h}^{n}\left(f,x+j_{1}h+j_{2}h+\cdots +j_{n}h\right).$
- Leibniz rule: $\Delta _{h}^{n}\left(fg,x\right)=\sum \limits _{k=0}^{n}{\binom {n}{k}}\Delta _{h}^{k}\left(f,x\right)\cdot \Delta _{h}^{n-k}\left(g,x+kh\right).$

## In differential equations

An important application of finite differences is in numerical analysis, especially in numerical differential equations, which aim at the numerical solution of ordinary and partial differential equations. The idea is to replace the derivatives appearing in the differential equation by finite differences that approximate them. The resulting methods are called finite difference methods.

Common applications of the finite difference method are in computational science and engineering disciplines, such as thermal engineering, fluid mechanics, etc.

## Newton's series

The **Newton series** consists of the terms of the **Newton forward difference equation**, named after Isaac Newton; in essence, it is the **Gregory–Newton interpolation formula** (named after Isaac Newton and James Gregory), first published in his *Principia Mathematica* in 1687, namely the discrete analog of the continuous Taylor expansion,

$f(x)=\sum _{k=0}^{\infty }{\frac {\Delta ^{k}[f](a)}{k!}}\,(x-a)_{k}=\sum _{k=0}^{\infty }{\binom {x-a}{k}}\,\Delta ^{k}[f](a),$

which holds for any polynomial function f and for many (but not all) analytic functions. (It does not hold when f is exponential type $\pi$ . This is easily seen, as the sine function vanishes at integer multiples of $\pi$ ; the corresponding Newton series is identically zero, as all finite differences are zero in this case. Yet clearly, the sine function is not zero.) Here, the expression ${\binom {x}{k}}={\frac {(x)_{k}}{k!}}$ is the binomial coefficient, and $(x)_{k}=x(x-1)(x-2)\cdots (x-k+1)$ is the "falling factorial" or "lower factorial", while the empty product (*x*)0 is defined to be 1. In this particular case, there is an assumption of unit steps for the changes in the values of *x*, *h* = 1 of the generalization below.

Note the formal correspondence of this result to Taylor's theorem. Historically, this, as well as the Chu–Vandermonde identity, $(x+y)_{n}=\sum _{k=0}^{n}{\binom {n}{k}}(x)_{n-k}\,(y)_{k},$ (following from it, and corresponding to the binomial theorem), are included in the observations that matured to the system of umbral calculus.

Newton series expansions can be superior to Taylor series expansions when applied to discrete quantities like quantum spins (see Holstein–Primakoff transformation), bosonic operator functions or discrete counting statistics.

To illustrate how one may use Newton's formula in actual practice, consider the first few terms of doubling the Fibonacci sequence *f* = 2, 2, 4, ... One can find a polynomial that reproduces these values, by first computing a difference table, and then substituting the differences that correspond to *x*0 (underlined) into the formula as follows, ${\begin{matrix}{\begin{array}{|c||c|c|c|}\hline x&f=\Delta ^{0}&\Delta ^{1}&\Delta ^{2}\\\hline 1&{\underline {2}}&&\\&&{\underline {0}}&\\2&2&&{\underline {2}}\\&&2&\\3&4&&\\\hline \end{array}}&\quad {\begin{aligned}f(x)&=\Delta ^{0}\cdot 1+\Delta ^{1}\cdot {\dfrac {(x-x_{0})_{1}}{1!}}+\Delta ^{2}\cdot {\dfrac {(x-x_{0})_{2}}{2!}}\quad (x_{0}=1)\\\\&=2\cdot 1+0\cdot {\dfrac {x-1}{1}}+2\cdot {\dfrac {(x-1)(x-2)}{2}}\\\\&=2+(x-1)(x-2)\\\end{aligned}}\end{matrix}}$

For the case of nonuniform steps in the values of x, Newton computes the divided differences, $\Delta _{j,0}=y_{j},\qquad \Delta _{j,k}={\frac {\Delta _{j+1,k-1}-\Delta _{j,k-1}}{x_{j+k}-x_{j}}}\quad \ni \quad \left\{k>0,\;j\leq \max \left(j\right)-k\right\},\qquad \Delta 0_{k}=\Delta _{0,k}$ the series of products, ${P_{0}}=1,\quad \quad P_{k+1}=P_{k}\cdot \left(\xi -x_{k}\right),$ and the resulting polynomial is the scalar product, $f(\xi )=\Delta 0\cdot P\left(\xi \right).$

In analysis with p-adic numbers, Mahler's theorem states that the assumption that f is a polynomial function can be weakened all the way to the assumption that f is merely continuous.

Carlson's theorem provides necessary and sufficient conditions for a Newton series to be unique, if it exists. However, a Newton series does not, in general, exist.

The Newton series, together with the Stirling series and the Selberg series, is a special case of the general difference series, all of which are defined in terms of suitably scaled forward differences.

In a compressed and slightly more general form and equidistant nodes the formula reads $f(x)=\sum _{k=0}{\binom {\frac {x-a}{h}}{k}}\sum _{j=0}^{k}(-1)^{k-j}{\binom {k}{j}}f(a+jh).$

## Calculus of finite differences

The forward difference can be considered as an operator, called the difference operator, which maps the function f to Δ*h*[*f*]. This operator amounts to $\Delta _{h}=\operatorname {T} _{h}-\operatorname {I} ,$ where T*h* is the shift operator with step h, defined by T*h*[*f*](*x*) = *f*(*x* + *h*), and I is the identity operator.

The finite difference of higher orders can be defined in recursive manner as Δ*n* *h* ≡ Δ*h*(Δ*n* − 1 *h*). Another equivalent definition is Δ*n* *h* ≡ [T*h* − I]*n*.

The difference operator Δ*h* is a linear operator, as such it satisfies Δ*h*[*α f* + *β g*](*x*) = *α* Δ*h*[*f*](*x*) + *β* Δ*h*[*g*](*x*).

It also satisfies a special Leibniz rule:

$\operatorname {\Delta } _{h}{\bigl (}fg{\bigr )}(x)={\bigl (}\operatorname {\Delta } _{h}f(x){\bigr )}g(x+h)+f(x){\bigl (}\operatorname {\Delta } _{h}g(x){\bigr )}~.$

Similar Leibniz rules hold for the backward and central differences.

Formally applying the Taylor series with respect to h, yields the operator equation $\operatorname {\Delta } _{h}=h\operatorname {D} +{\frac {1}{2!}}h^{2}\operatorname {D} ^{2}+{\frac {1}{3!}}h^{3}\operatorname {D} ^{3}+\cdots =e^{h\operatorname {D} }-\operatorname {I} ,$ where D denotes the conventional, continuous derivative operator, mapping f to its derivative *f*′. The expansion is valid when both sides act on analytic functions, for sufficiently small h; in the special case that the series of derivatives terminates (when the function operated on is a finite polynomial) the expression is exact, for *all* finite stepsizes, h . Thus T*h* = *e**h* D, and formally inverting the exponential yields $h\operatorname {D} =\ln(1+\Delta _{h})=\Delta _{h}-{\tfrac {1}{2}}\,\Delta _{h}^{2}+{\tfrac {1}{3}}\,\Delta _{h}^{3}-\cdots ~.$ This formula holds in the sense that both operators give the same result when applied to a polynomial.

Even for analytic functions, the series on the right is not guaranteed to converge; it may be an asymptotic series. However, it can be used to obtain more accurate approximations for the derivative. For instance, retaining the first two terms of the series yields the second-order approximation to *f* ′(*x*) mentioned at the end of the section *§ Higher-order differences*.

The analogous formulas for the backward and central difference operators are $h\operatorname {D} =-\ln(1-\nabla _{h})\quad {\text{ and }}\quad h\operatorname {D} =2\operatorname {arsinh} \left({\tfrac {1}{2}}\,\delta _{h}\right)~.$

The calculus of finite differences is related to the umbral calculus of combinatorics. This remarkably systematic correspondence is due to the identity of the commutators of the umbral quantities to their continuum analogs (*h* → 0 limits),

$\left[{\frac {\Delta _{h}}{h}},x\,\operatorname {T} _{h}^{-1}\right]=[\operatorname {D} ,x]=I.$

A large number of formal differential relations of standard calculus involving functions *f*(*x*) thus *systematically map to umbral finite-difference analogs* involving *f*( *x* T−1 *h* ).

For instance, the umbral analog of a monomial xn is a generalization of the above falling factorial (Pochhammer k-symbol), $(x)_{n}=\left(x\operatorname {T} _{h}^{-1}\right)^{n}=x\left(x-h\right)\left(x-2h\right)\cdots {\bigl (}x-\left(n-1\right)h{\bigr )},$ so that ${\frac {\Delta _{h}}{h}}(x)_{n}=n(x)_{n-1},$ hence the above Newton interpolation formula (by matching coefficients in the expansion of an arbitrary function *f*(*x*) in such symbols), and so on.

For example, the umbral sine is $\sin \left(x\operatorname {T} _{h}^{-1}\right)=x-{\frac {(x)_{3}}{3!}}+{\frac {(x)_{5}}{5!}}-{\frac {(x)_{7}}{7!}}+\cdots$

As in the continuum limit, the eigenfunction of ⁠Δ*h*/*h*⁠ also happens to be an exponential,

${\frac {\Delta _{h}}{h}}(1+\lambda h)^{\frac {x}{h}}={\frac {\Delta _{h}}{h}}e^{\ln(1+\lambda h){\frac {x}{h}}}=\lambda e^{\ln(1+\lambda h){\frac {x}{h}}},$

and hence *Fourier sums of continuum functions are readily, faithfully mapped to umbral Fourier sums*, i.e., involving the same Fourier coefficients multiplying these umbral basis exponentials. This umbral exponential thus amounts to the exponential generating function of the Pochhammer symbols.

Thus, for instance, the Dirac delta function maps to its umbral correspondent, the cardinal sine function $\delta (x)\mapsto {\frac {\sin \left[{\frac {\pi }{2}}\left(1+{\frac {x}{h}}\right)\right]}{\pi (x+h)}},$ and so forth. Difference equations can often be solved with techniques very similar to those for solving differential equations.

The inverse operator of the forward difference operator, so then the umbral integral, is the indefinite sum or antidifference operator.

### Rules for calculus of finite difference operators

Analogous to rules for finding the derivative, we have:

- **Constant rule**: If c is a constant, then $\Delta c=0$
- **Linearity**: If a and b are constants, $\Delta (af+bg)=a\Delta f+b\Delta g$

All of the above rules apply equally well to any difference operator as to Δ, including δ and ∇.

- **Product rule**: ${\begin{aligned}\Delta (fg)&=f\,\Delta g+g\,\Delta f+\Delta f\Delta g\\[4pt]\nabla (fg)&=f\,\nabla g+g\,\nabla f-\nabla f\nabla g\end{aligned}}$
- **Quotient rule**: $\nabla \left({\frac {f}{g}}\right)=\left.\left(\det {\begin{bmatrix}\nabla f&\nabla g\\f&g\end{bmatrix}}\right)\right/\left(g\cdot \det {\begin{bmatrix}g&\nabla g\\1&1\end{bmatrix}}\right)$ or $\nabla \left({\frac {f}{g}}\right)={\frac {g\,\nabla f-f\,\nabla g}{g\cdot (g-\nabla g)}}$
- **Summation rules**: ${\begin{aligned}\sum _{n=a}^{b}\Delta f(n)&=f(b+1)-f(a)\\\sum _{n=a}^{b}\nabla f(n)&=f(b)-f(a-1)\end{aligned}}$

See references.

## Generalizations

- A **generalized finite difference** is usually defined as $\Delta _{h}^{\mu }[f](x)=\sum _{k=0}^{N}\mu _{k}f(x+kh),$ where *μ* = (*μ*0, …, *μN*) is its coefficient vector. An **infinite difference** is a further generalization, where the finite sum above is replaced by an infinite series. Another way of generalization is making coefficients *μk* depend on point x: *μk* = *μk*(*x*), thus considering **weighted finite difference**. Also one may make the step h depend on point x: *h* = *h*(*x*). Such generalizations are useful for constructing different modulus of continuity.
- The generalized difference can be seen as the polynomial rings *R*[*Th*]. It leads to difference algebras.
- Difference operator generalizes to Möbius inversion over a partially ordered set.
- As a convolution operator: Via the formalism of incidence algebras, difference operators and other Möbius inversion can be represented by convolution with a function on the poset, called the Möbius function μ; for the difference operator, μ is the sequence (1, −1, 0, 0, 0, …).

## Multivariate finite differences

Finite differences can be considered in more than one variable. They are analogous to partial derivatives in several variables.

Some partial derivative approximations are: ${\begin{aligned}f_{x}(x,y)&\approx {\frac {f(x+h,y)-f(x-h,y)}{2h}}\\f_{y}(x,y)&\approx {\frac {f(x,y+k)-f(x,y-k)}{2k}}\\f_{xx}(x,y)&\approx {\frac {f(x+h,y)-2f(x,y)+f(x-h,y)}{h^{2}}}\\f_{yy}(x,y)&\approx {\frac {f(x,y+k)-2f(x,y)+f(x,y-k)}{k^{2}}}\\f_{xy}(x,y)&\approx {\frac {f(x+h,y+k)-f(x+h,y-k)-f(x-h,y+k)+f(x-h,y-k)}{4hk}}.\end{aligned}}$

Alternatively, for applications in which the computation of f is the most costly step, and both first and second derivatives must be computed, a more efficient formula for the last case is $f_{xy}(x,y)\approx {\frac {f(x+h,y+k)-f(x+h,y)-f(x,y+k)+2f(x,y)-f(x-h,y)-f(x,y-k)+f(x-h,y-k)}{2hk}},$ since the only values to compute that are not already needed for the previous four equations are *f*(*x* + *h*, *y* + *k*) and *f*(*x* − *h*, *y* − *k*).

For functions with N variables $f(x_{1},x_{2},\ldots ,x_{N})$ , evaluating the full m -th order derivative tensor via finite difference requires $O(N^{m})$ calls of the function f (where we have used the Big O notation to denote the asymptotic scaling behavior), or $O(N^{m-m'})$ calls of the $m'$ -th order derivative of the function f (where $m'<m$ ). However, for many classes of functions, the m -th order derivative tensor is sparse, or its off-diagonal blocks may have low rank. In these cases, algorithms may exist that can numerically estimate the m -th order derivative tensor using less than $O(N^{m-m'})$ calls of the $m'$ -th order derivative, for example when $m=2$ and $m'=1$ ; in the latter case it is possible to estimate the Hessian matrix using only $O(1)$ gradients, instead of $O(N)$ gradients as would be required by the conventional finite difference algorithm.
