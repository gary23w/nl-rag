---
title: "Riemann sum"
source: https://en.wikipedia.org/wiki/Rectangle_method
domain: communication-complexity
license: CC-BY-SA-4.0
tags: communication complexity, two party protocol, fooling set, discrepancy method
fetched: 2026-07-02
---

# Riemann sum

(Redirected from

Rectangle method

)

In mathematics, a **Riemann sum** is a certain kind of approximation of an integral by a finite sum. It is named after nineteenth century German mathematician Bernhard Riemann. One very common application is in numerical integration, i.e., approximating the area of functions or lines on a graph, where it is also known as the **rectangle rule**. It can also be applied for approximating the length of curves and other approximations.

The sum is calculated by partitioning the region into shapes (rectangles, trapezoids, parabolas, or cubics—sometimes infinitesimally small) that together form a region that is similar to the region being measured, then calculating the area for each of these shapes, and finally adding all of these small areas together. This approach can be used to find a numerical approximation for a definite integral even if the fundamental theorem of calculus does not make it easy to find a closed-form solution.

Because the region by the small shapes is usually not exactly the same shape as the region being measured, the Riemann sum will differ from the area being measured. This error can be reduced by dividing up the region more finely, using smaller and smaller shapes. As the shapes get smaller and smaller, the sum approaches the Riemann integral.

## Definition

Let $f:[a,b]\to \mathbb {R}$ be a function defined on a closed interval $[a,b]$ of the real numbers, $\mathbb {R}$ , and $P=(x_{0},x_{1},\ldots ,x_{n})$ as a partition of $[a,b]$ , that is $a=x_{0}<x_{1}<x_{2}<\dots <x_{n}=b.$ A **Riemann sum** S of f over $[a,b]$ with partition P is defined as $S=\sum _{i=1}^{n}f(x_{i}^{*})\,\Delta x_{i},$ where $\Delta x_{i}=x_{i}-x_{i-1}$ and $x_{i}^{*}\in [x_{i-1},x_{i}]$ . One might produce different Riemann sums depending on which $x_{i}^{*}$ s are chosen. In the end this will not matter, if the function is Riemann integrable, when the difference or width of the summands $\Delta x_{i}$ approaches zero.

## Types of Riemann sums

Specific choices of $x_{i}^{*}$ give different types of Riemann sums:

- If $x_{i}^{*}=x_{i-1}$ for all *i*, the method is the **left rule** and gives a **left Riemann sum**.
- If $x_{i}^{*}=x_{i}$ for all *i*, the method is the **right rule** and gives a **right Riemann sum**.
- If $x_{i}^{*}=(x_{i}+x_{i-1})/2$ for all *i*, the method is the **midpoint rule** and gives a **middle Riemann sum**.
- If $f(x_{i}^{*})=\sup f([x_{i-1},x_{i}])$ (that is, the supremum of ${\textstyle f}$ over $[x_{i-1},x_{i}]$ ), the method is the **upper rule** and gives an **upper Riemann sum** or **upper Darboux sum**.
- If $f(x_{i}^{*})=\inf f([x_{i-1},x_{i}])$ (that is, the infimum of *f* over $[x_{i-1},x_{i}]$ ), the method is the **lower rule** and gives a **lower Riemann sum** or **lower Darboux sum**.

All these Riemann summation methods are among the most basic ways to accomplish numerical integration. Loosely speaking, a function is Riemann integrable if all Riemann sums converge as the partition "gets finer and finer".

While not derived as a Riemann sum, taking the average of the left and right Riemann sums is the **trapezoidal rule** and gives a **trapezoidal sum**. It is one of the simplest of a very general way of approximating integrals using weighted averages. This is followed in complexity by Simpson's rule and Newton–Cotes formulas.

Any Riemann sum on a given partition (that is, for any choice of $x_{i}^{*}$ between $x_{i-1}$ and $x_{i}$ ) is contained between the lower and upper Darboux sums. This forms the basis of the Darboux integral, which is ultimately equivalent to the Riemann integral.

## Riemann summation methods

The four Riemann summation methods are usually best approached with subintervals of equal size. The interval [*a*, *b*] is therefore divided into n subintervals, each of length $\Delta x={\frac {b-a}{n}}.$

The points in the partition will then be $a,\;a+\Delta x,\;a+2\Delta x,\;\ldots ,\;a+(n-2)\Delta x,\;a+(n-1)\Delta x,\;b.$

### Left rule

For the left rule, the function is approximated by its values at the left endpoints of the subintervals. This gives multiple rectangles with base Δ*x* and height *f*(*a* + *i*Δ*x*). Doing this for *i* = 0, 1, ..., *n* − 1, and summing the resulting areas gives $S_{\mathrm {left} }=\Delta x\left[f(a)+f(a+\Delta x)+f(a+2\Delta x)+\dots +f(b-\Delta x)\right].$

The left Riemann sum amounts to an overestimation if *f* is monotonically decreasing on this interval, and an underestimation if it is monotonically increasing. The error of this formula will be $\left\vert \int _{a}^{b}f(x)\,dx-S_{\mathrm {left} }\right\vert \leq {\frac {M_{1}(b-a)^{2}}{2n}},$ where $M_{1}$ is the maximum value of the absolute value of $f^{\prime }(x)$ over the interval.

### Right rule

For the right rule, the function is approximated by its values at the right endpoints of the subintervals. This gives multiple rectangles with base Δ*x* and height *f*(*a* + *i*Δ*x*). Doing this for *i* = 1, ..., *n*, and summing the resulting areas gives $S_{\mathrm {right} }=\Delta x\left[f(a+\Delta x)+f(a+2\Delta x)+\dots +f(b)\right].$

The right Riemann sum amounts to an underestimation if *f* is monotonically decreasing, and an overestimation if it is monotonically increasing. The error of this formula will be $\left\vert \int _{a}^{b}f(x)\,dx-S_{\mathrm {right} }\right\vert \leq {\frac {M_{1}(b-a)^{2}}{2n}},$ where $M_{1}$ is the maximum value of the absolute value of $f^{\prime }(x)$ over the interval.

### Midpoint rule

For the midpoint rule, the function is approximated by its values at the midpoints of the subintervals. This gives *f*(*a* + Δ*x*/2) for the first subinterval, *f*(*a* + 3Δ*x*/2) for the next one, and so on until *f*(*b* − Δ*x*/2). Summing the resulting areas gives $S_{\mathrm {mid} }=\Delta x\left[f\left(a+{\tfrac {\Delta x}{2}}\right)+f\left(a+{\tfrac {3\Delta x}{2}}\right)+\dots +f\left(b-{\tfrac {\Delta x}{2}}\right)\right].$

The error of this formula will be $\left\vert \int _{a}^{b}f(x)\,dx-S_{\mathrm {mid} }\right\vert \leq {\frac {M_{2}(b-a)^{3}}{24n^{2}}},$ where $M_{2}$ is the maximum value of the absolute value of $f^{\prime \prime }(x)$ over the interval. This error is half of that of the trapezoidal sum; as such the middle Riemann sum is the most accurate approach to the Riemann sum.

### Trapezoidal rule

For the trapezoidal rule, the function is approximated by the average of its values at the left and right endpoints of the subintervals. Using the area formula ${\tfrac {1}{2}}h(b_{1}+b_{2})$ for a trapezium with parallel sides *b*1 and *b*2, and height h, and summing the resulting areas gives $S_{\mathrm {trap} }={\tfrac {1}{2}}\Delta x\left[f(a)+2f(a+\Delta x)+2f(a+2\Delta x)+\dots +f(b)\right].$

The error of this formula will be $\left\vert \int _{a}^{b}f(x)\,dx-S_{\mathrm {trap} }\right\vert \leq {\frac {M_{2}(b-a)^{3}}{12n^{2}}},$ where $M_{2}$ is the maximum value of the absolute value of $f''(x)$ .

The approximation obtained with the trapezoidal sum for a function is the same as the average of the left hand and right hand sums of that function.

## Connection with integration

For a one-dimensional Riemann sum over domain $[a,b]$ , as the maximum size of a subinterval shrinks to zero (that is the limit of the norm of the subintervals goes to zero), some functions will have all Riemann sums converge to the same value. This limiting value, if it exists, is defined as the definite Riemann integral of the function over the domain, $\int _{a}^{b}f(x)\,dx=\lim _{\|\Delta x\|\rightarrow 0}\sum _{i=1}^{n}f(x_{i}^{*})\,\Delta x_{i}.$

For a finite-sized domain, if the maximum size of a subinterval shrinks to zero, this implies the number of subinterval goes to infinity. For finite partitions, Riemann sums are always approximations to the limiting value and this approximation gets better as the partition gets finer. The following animations help demonstrate how increasing the number of subintervals (while lowering the maximum subinterval size) better approximates the "area" under the curve:

- (Left Riemann sum)Left Riemann sum
- (Right Riemann sum)Right Riemann sum
- (Middle Riemann sum)Middle Riemann sum

Since the red function here is assumed to be a smooth function, all three Riemann sums will converge to the same value as the number of subintervals goes to infinity.

## Example

Comparison of the right Riemann sum with the integral of

x

↦

x

2

over

${\textstyle [0,2]}$

.

A visual representation of the area under the curve

y

=

x

2

over [0, 2]. Using antiderivatives this area is exactly

${\textstyle {\dfrac {8}{3}}}$

.

Approximating the area under the curve

y

=

x

2

over [0, 2] using the right Riemann sum. Notice that because the function is monotonically increasing, the right Riemann sum will always overestimate the area contributed by each term in the sum (and do so maximally).

The value of the right Riemann sum of

x

↦

x

2

over

${\textstyle [0,2]}$

. As the number of rectangles increases, it approaches the exact area of

${\textstyle {\dfrac {8}{3}}}$

.

Taking an example, the area under the curve *y* = *x*2 over [0, 2] can be procedurally computed using Riemann's method.

The interval [0, 2] is firstly divided into n subintervals, each of which is given a width of ${\tfrac {2}{n}}$ ; these are the widths of the Riemann rectangles (hereafter "boxes"). Because the right Riemann sum is to be used, the sequence of x coordinates for the boxes will be $x_{1},x_{2},\ldots ,x_{n}$ . Therefore, the sequence of the heights of the boxes will be $x_{1}^{2},x_{2}^{2},\ldots ,x_{n}^{2}$ . It is an important fact that $x_{i}={\tfrac {2i}{n}}$ , and $x_{n}=2$ .

The area of each box will be ${\tfrac {2}{n}}\times x_{i}^{2}$ and therefore the *n*th right Riemann sum will be: ${\begin{aligned}S&={\frac {2}{n}}\left({\frac {2}{n}}\right)^{2}+\dots +{\frac {2}{n}}\left({\frac {2i}{n}}\right)^{2}+\dots +{\frac {2}{n}}\left({\frac {2n}{n}}\right)^{2}\\[1ex]&={\frac {8}{n^{3}}}\left(1+\dots +i^{2}+\dots +n^{2}\right)\\[1ex]&={\frac {8}{n^{3}}}\left({\frac {n(n+1)(2n+1)}{6}}\right)\\[1ex]&={\frac {8}{n^{3}}}\left({\frac {2n^{3}+3n^{2}+n}{6}}\right)\\[1ex]&={\frac {8}{3}}+{\frac {4}{n}}+{\frac {4}{3n^{2}}}.\end{aligned}}$

If the limit is viewed as *n* → ∞, it can be concluded that the approximation approaches the actual value of the area under the curve as the number of boxes increases. Hence: $\lim _{n\to \infty }S=\lim _{n\to \infty }\left({\frac {8}{3}}+{\frac {4}{n}}+{\frac {4}{3n^{2}}}\right)={\frac {8}{3}}.$

This method agrees with the definite integral as calculated in more mechanical ways: $\int _{0}^{2}x^{2}\,dx={\frac {8}{3}}.$

Because the function is continuous and monotonically increasing over the interval, a right Riemann sum overestimates the integral by the largest amount (while a left Riemann sum would underestimate the integral by the largest amount). This fact, which is intuitively clear from the diagrams, shows how the nature of the function determines how accurate the integral is estimated. While simple, right and left Riemann sums are often less accurate than more advanced techniques of estimating an integral such as the Trapezoidal rule or Simpson's rule.

The example function has an easy-to-find anti-derivative so estimating the integral by Riemann sums is mostly an academic exercise; however it must be remembered that not all functions have anti-derivatives so estimating their integrals by summation is practically important.

## Higher dimensions

The basic idea behind a Riemann sum is to "break-up" the domain via a partition into pieces, multiply the "size" of each piece by some value the function takes on that piece, and sum all these products. This can be generalized to allow Riemann sums for functions over domains of more than one dimension.

While intuitively, the process of partitioning the domain is easy to grasp, the technical details of how the domain may be partitioned get much more complicated than the one dimensional case and involves aspects of the geometrical shape of the domain.

### Two dimensions

In two dimensions, the domain A may be divided into a number of two-dimensional cells $A_{i}$ such that ${\textstyle A=\bigcup _{i}A_{i}}$ . Each cell then can be interpreted as having an "area" denoted by $\Delta A_{i}$ . The two-dimensional Riemann sum is $S=\sum _{i=1}^{n}f(x_{i}^{*},y_{i}^{*})\,\Delta A_{i},$ where $(x_{i}^{*},y_{i}^{*})\in A_{i}$ .

### Three dimensions

In three dimensions, the domain V is partitioned into a number of three-dimensional cells $V_{i}$ such that ${\textstyle V=\bigcup _{i}V_{i}}$ . Each cell then can be interpreted as having a "volume" denoted by $\Delta V_{i}$ . The three-dimensional Riemann sum is $S=\sum _{i=1}^{n}f(x_{i}^{*},y_{i}^{*},z_{i}^{*})\,\Delta V_{i},$ where $(x_{i}^{*},y_{i}^{*},z_{i}^{*})\in V_{i}$ .

### Arbitrary number of dimensions

Higher dimensional Riemann sums follow a similar pattern. An *n*-dimensional Riemann sum is $S=\sum _{i}f(P_{i}^{*})\,\Delta V_{i},$ where $P_{i}^{*}\in V_{i}$ , that is, it is a point in the *n*-dimensional cell $V_{i}$ with *n*-dimensional volume $\Delta V_{i}$ .

### Generalization

In high generality, Riemann sums can be written $S=\sum _{i}f(P_{i}^{*})\mu (V_{i}),$ where $P_{i}^{*}$ stands for any arbitrary point contained in the set $V_{i}$ and $\mu$ is a measure on the underlying set. Roughly speaking, a measure is a function that gives a "size" of a set, in this case the size of the set $V_{i}$ ; in one dimension this can often be interpreted as a length, in two dimensions as an area, in three dimensions as a volume, and so on.
