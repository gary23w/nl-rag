---
title: "Frobenius method"
source: https://en.wikipedia.org/wiki/Frobenius_method
domain: differential-equations-ode
license: CC-BY-SA-4.0
tags: ordinary differential equation, initial value problem, laplace transform, linear differential equation
fetched: 2026-07-02
---

# Frobenius method

In mathematics, the **method of Frobenius**, named after Ferdinand Georg Frobenius, is a way to find an infinite series solution for a linear second-order ordinary differential equation of the form $z^{2}u''+p(z)zu'+q(z)u=0$ with ${\textstyle u'\equiv {\frac {du}{dz}}}$ and ${\textstyle u''\equiv {\frac {d^{2}u}{dz^{2}}}}$ .

in the vicinity of the regular singular point $z=0$ .

One can divide by $z^{2}$ to obtain a differential equation of the form $u''+{\frac {p(z)}{z}}u'+{\frac {q(z)}{z^{2}}}u=0$ which will not be solvable with regular power series methods if either *p*(*z*)/*z* or *q*(*z*)/*z*2 is not analytic at *z* = 0. The Frobenius method enables one to create a power series solution to such a differential equation, provided that *p*(*z*) and *q*(*z*) are themselves analytic at 0 or, being analytic elsewhere, both their limits at 0 exist (and are finite).

## History

Frobenius' contribution was not so much in all the possible *forms* of the series solutions involved (see below). These forms had all been established earlier, by Lazarus Fuchs. The *indicial polynomial* (see below) and its role had also been established by Fuchs.

A first contribution by Frobenius to the theory was to show that - as regards a first, linearly independent solution, which then has the form of an analytical power series multiplied by an arbitrary power *r* of the independent variable (see below) - the coefficients of the generalized power series obey a *recurrence relation*, so that they can always be straightforwardly calculated.

A second contribution by Frobenius was to show that, in cases in which the roots of the indicial equation differ by an integer, the general *form* of the second linearly independent solution (see below) can be obtained by a procedure which is based on differentiation with respect to the parameter *r*, mentioned above.

A large part of Frobenius' 1873 publication was devoted to proofs of convergence of all the series involved in the solutions, as well as establishing the radii of convergence of these series.

## Explanation

The method of Frobenius is to seek a power series solution of the form $u(z)=z^{r}\sum _{k=0}^{\infty }A_{k}z^{k},\qquad (A_{0}\neq 0)$

Differentiating: $u'(z)=\sum _{k=0}^{\infty }(k+r)A_{k}z^{k+r-1}$ $u''(z)=\sum _{k=0}^{\infty }(k+r-1)(k+r)A_{k}z^{k+r-2}$

Substituting the above differentiation into our original ODE: ${\begin{aligned}&z^{2}\sum _{k=0}^{\infty }(k+r-1)(k+r)A_{k}z^{k+r-2}+zp(z)\sum _{k=0}^{\infty }(k+r)A_{k}z^{k+r-1}+q(z)\sum _{k=0}^{\infty }A_{k}z^{k+r}\\={}&\sum _{k=0}^{\infty }(k+r-1)(k+r)A_{k}z^{k+r}+p(z)\sum _{k=0}^{\infty }(k+r)A_{k}z^{k+r}+q(z)\sum _{k=0}^{\infty }A_{k}z^{k+r}\\={}&\sum _{k=0}^{\infty }[(k+r-1)(k+r)A_{k}z^{k+r}+p(z)(k+r)A_{k}z^{k+r}+q(z)A_{k}z^{k+r}]\\={}&\sum _{k=0}^{\infty }\left[(k+r-1)(k+r)+p(z)(k+r)+q(z)\right]A_{k}z^{k+r}\\={}&\left[r(r-1)+p(z)r+q(z)\right]A_{0}z^{r}+\sum _{k=1}^{\infty }\left[(k+r-1)(k+r)+p(z)(k+r)+q(z)\right]A_{k}z^{k+r}=0\end{aligned}}$

The expression $r\left(r-1\right)+p\left(0\right)r+q\left(0\right)=I(r)$ is known as the *indicial polynomial*, which is quadratic in *r*. The general definition of the *indicial polynomial* is the coefficient of the lowest power of *z* in the infinite series. In this case it happens to be that this is the *r*th coefficient but, it is possible for the lowest possible exponent to be *r* − 2, *r* − 1 or, something else depending on the given differential equation. This detail is important to keep in mind. In the process of synchronizing all the series of the differential equation to start at the same index value (which in the above expression is *k* = 1), one can end up with complicated expressions. However, in solving for the indicial roots attention is focused only on the coefficient of the lowest power of *z*.

Using this, the general expression of the coefficient of *z**k* + *r* is $I(k+r)A_{k}+\sum _{j=0}^{k-1}{(j+r)p^{(k-j)}(0)+q^{(k-j)}(0) \over (k-j)!}A_{j},$

These coefficients must be zero, since they should be solutions of the differential equation, so

${\begin{aligned}I(k+r)A_{k}+\sum _{j=0}^{k-1}{(j+r)p^{(k-j)}(0)+q^{(k-j)}(0) \over (k-j)!}A_{j}&=0\\[4pt]\sum _{j=0}^{k-1}{(j+r)p^{(k-j)}(0)+q^{(k-j)}(0) \over (k-j)!}A_{j}&=-I(k+r)A_{k}\\[4pt]{1 \over -I(k+r)}\sum _{j=0}^{k-1}{(j+r)p^{(k-j)}(0)+q^{(k-j)}(0) \over (k-j)!}A_{j}&=A_{k}\end{aligned}}$

The series solution with *A**k* above, $U_{r}(z)=\sum _{k=0}^{\infty }A_{k}z^{k+r}$ satisfies $z^{2}U_{r}(z)''+p(z)zU_{r}(z)'+q(z)U_{r}(z)=I(r)z^{r}$

If we choose one of the roots to the indicial polynomial for *r* in *U**r*(*z*), we gain a solution to the differential equation. If the difference between the roots is not an integer, we get another, linearly independent solution in the other root.

## Example

Let us solve $z^{2}f''-zf'+(1-z)f=0$

Divide throughout by *z*2 to give $f''-{1 \over z}f'+{1-z \over z^{2}}f=f''-{1 \over z}f'+\left({1 \over z^{2}}-{1 \over z}\right)f=0$ which has the requisite singularity at *z* = 0.

Use the series solution ${\begin{aligned}f&=\sum _{k=0}^{\infty }A_{k}z^{k+r}\\f'&=\sum _{k=0}^{\infty }(k+r)A_{k}z^{k+r-1}\\f''&=\sum _{k=0}^{\infty }(k+r)(k+r-1)A_{k}z^{k+r-2}\end{aligned}}$

Now, substituting ${\begin{aligned}\sum _{k=0}^{\infty }&(k+r)(k+r-1)A_{k}z^{k+r-2}-{\frac {1}{z}}\sum _{k=0}^{\infty }(k+r)A_{k}z^{k+r-1}+\left({\frac {1}{z^{2}}}-{\frac {1}{z}}\right)\sum _{k=0}^{\infty }A_{k}z^{k+r}\\&=\sum _{k=0}^{\infty }(k+r)(k+r-1)A_{k}z^{k+r-2}-{\frac {1}{z}}\sum _{k=0}^{\infty }(k+r)A_{k}z^{k+r-1}+{\frac {1}{z^{2}}}\sum _{k=0}^{\infty }A_{k}z^{k+r}-{\frac {1}{z}}\sum _{k=0}^{\infty }A_{k}z^{k+r}\\&=\sum _{k=0}^{\infty }(k+r)(k+r-1)A_{k}z^{k+r-2}-\sum _{k=0}^{\infty }(k+r)A_{k}z^{k+r-2}+\sum _{k=0}^{\infty }A_{k}z^{k+r-2}-\sum _{k=0}^{\infty }A_{k}z^{k+r-1}\\&=\sum _{k=0}^{\infty }(k+r)(k+r-1)A_{k}z^{k+r-2}-\sum _{k=0}^{\infty }(k+r)A_{k}z^{k+r-2}+\sum _{k=0}^{\infty }A_{k}z^{k+r-2}-\sum _{k-1=0}^{\infty }A_{k-1}z^{k-1+r-1}\\&=\sum _{k=0}^{\infty }(k+r)(k+r-1)A_{k}z^{k+r-2}-\sum _{k=0}^{\infty }(k+r)A_{k}z^{k+r-2}+\sum _{k=0}^{\infty }A_{k}z^{k+r-2}-\sum _{k=1}^{\infty }A_{k-1}z^{k+r-2}\\&=\left\{\sum _{k=0}^{\infty }\left((k+r)(k+r-1)-(k+r)+1\right)A_{k}z^{k+r-2}\right\}-\sum _{k=1}^{\infty }A_{k-1}z^{k+r-2}\\&=\left\{\left(r(r-1)-r+1\right)A_{0}z^{r-2}+\sum _{k=1}^{\infty }\left((k+r)(k+r-1)-(k+r)+1\right)A_{k}z^{k+r-2}\right\}-\sum _{k=1}^{\infty }A_{k-1}z^{k+r-2}\\&=(r-1)^{2}A_{0}z^{r-2}+\left\{\sum _{k=1}^{\infty }(k+r-1)^{2}A_{k}z^{k+r-2}-\sum _{k=1}^{\infty }A_{k-1}z^{k+r-2}\right\}\\&=(r-1)^{2}A_{0}z^{r-2}+\sum _{k=1}^{\infty }\left((k+r-1)^{2}A_{k}-A_{k-1}\right)z^{k+r-2}\end{aligned}}$

From (*r* − 1)2 = 0 we get a double root of 1. Using this root, we set the coefficient of *z**k* + *r* − 2 to be zero (for it to be a solution), which gives us: $(k+1-1)^{2}A_{k}-A_{k-1}=k^{2}A_{k}-A_{k-1}=0$ hence we have the recurrence relation: $A_{k}={\frac {A_{k-1}}{k^{2}}}$

Given some initial conditions, we can either solve the recurrence entirely or obtain a solution in power series form.

Since the ratio of coefficients $A_{k}/A_{k-1}$ is a rational function, the power series can be written as a generalized hypergeometric series.

## Exceptional cases: roots separated by an integer

The previous example involved an indicial polynomial with a repeated root, which gives only one solution to the given differential equation. In general, the Frobenius method gives two independent solutions provided that the indicial equation's roots are not separated by an integer (including zero).

If the root is repeated or the roots differ by an integer, then the second solution can be found using: $y_{2}=Cy_{1}\ln x+\sum _{k=0}^{\infty }B_{k}x^{k+r_{2}}$ where $y_{1}(x)$ is the first solution (based on the larger root in the case of unequal roots), $r_{2}$ is the smaller root, and the constant C and the coefficients $B_{k}$ are to be determined. Once $B_{0}$ is chosen (for example by setting it to 1) then C and the $B_{k}$ are determined up to but not including $B_{r_{1}-r_{2}}$ , which can be set arbitrarily. This then determines the rest of the $B_{k}.$ In some cases the constant C must be zero.

**Example**: consider the following differential equation (Kummer's equation with *a* = 1 and *b* = 2): $zu''+(2-z)u'-u=0$ The roots of the indicial equation are −1 and 0. Two independent solutions are $1/z$ and $e^{z}/z,$ so we see that the logarithm does not appear in any solution. The solution $(e^{z}-1)/z$ has a power series starting with the power zero. In a power series starting with $z^{-1}$ the recurrence relation places no restriction on the coefficient for the term $z^{0},$ which can be set arbitrarily. If it is set to zero then with this differential equation all the other coefficients will be zero and we obtain the solution 1/*z*.

### Tandem recurrence relations for series coefficients in the exceptional cases

In cases in which roots of the indicial polynomial differ by an integer (including zero), the coefficients of all series involved in second linearly independent solutions can be calculated straightforwardly from *tandem recurrence relations*. These tandem relations can be constructed by further developing Frobenius' original invention of differentiating with respect to the parameter *r*, and using this approach to actually calculate the series coefficients in all cases.
