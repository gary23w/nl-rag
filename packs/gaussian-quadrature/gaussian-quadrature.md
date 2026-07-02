---
title: "Gaussian quadrature"
source: https://en.wikipedia.org/wiki/Gaussian_quadrature
domain: gaussian-quadrature
license: CC-BY-SA-4.0
tags: gaussian quadrature, gauss-legendre quadrature, gauss-kronrod quadrature, clenshaw-curtis quadrature
fetched: 2026-07-02
---

# Gaussian quadrature

In numerical analysis, an n-point **Gaussian quadrature rule**, named after Carl Friedrich Gauss, is a quadrature rule constructed to yield an exact result for polynomials of degree 2*n* − 1 or less by a suitable choice of the nodes xi and weights wi for *i* = 1, ..., *n*.

The modern formulation using orthogonal polynomials was developed by Carl Gustav Jacobi in 1826. The most common domain of integration for such a rule is taken as [−1, 1], so the rule is stated as $\int _{-1}^{1}f(x)\,dx\approx \sum _{i=1}^{n}w_{i}f(x_{i}),$

which is exact for polynomials of degree 2*n* − 1 or less. This exact rule is known as the Gauss–Legendre quadrature rule. The quadrature rule will only be an accurate approximation to the integral above if *f* (*x*) is well-approximated by a polynomial of degree 2*n* − 1 or less on [−1, 1].

The Gauss–Legendre quadrature rule is not typically used for integrable functions with endpoint singularities. Instead, if the integrand can be written as

$f(x)=\left(1-x\right)^{\alpha }\left(1+x\right)^{\beta }g(x),\quad \alpha ,\beta >-1,$

where *g*(*x*) is well-approximated by a low-degree polynomial, then alternative nodes xi' and weights wi' will usually give more accurate quadrature rules. These are known as Gauss–Jacobi quadrature rules, i.e.,

$\int _{-1}^{1}f(x)\,dx=\int _{-1}^{1}\left(1-x\right)^{\alpha }\left(1+x\right)^{\beta }g(x)\,dx\approx \sum _{i=1}^{n}w_{i}'g\left(x_{i}'\right).$

Common weights include ${\textstyle {\frac {1}{\sqrt {1-x^{2}}}}}$ (Chebyshev–Gauss) and ${\textstyle {\sqrt {1-x^{2}}}}$ . One may also want to integrate over semi-infinite (Gauss–Laguerre quadrature) and infinite intervals (Gauss–Hermite quadrature).

It can be shown (see Press et al., or Stoer and Bulirsch) that the quadrature nodes xi are the roots of a polynomial belonging to a class of orthogonal polynomials (the class orthogonal with respect to a weighted inner-product). This is a key observation for computing Gauss quadrature nodes and weights.

## Gauss–Legendre quadrature

For the simplest integration problem stated above, i.e., *f*(*x*) is well-approximated by polynomials on $[-1,1]$ , the associated orthogonal polynomials are Legendre polynomials, denoted by *P**n*(*x*). With the n-th polynomial normalized to give *P**n*(1) = 1, the i-th Gauss node, xi, is the i-th root of Pn and the weights are given by the formula $w_{i}={\frac {2}{\left(1-x_{i}^{2}\right)\left[P'_{n}(x_{i})\right]^{2}}}.$

Some low-order quadrature rules are tabulated below (over interval [−1, 1], see the section below for other intervals).

| Number of points, n | Points/abscissa, xi | Weights, wi |   |   |
|---|---|---|---|---|
| 1 | 0 | 2 |   |   |
| 2 | $\pm {\frac {1}{\sqrt {3}}}$ | ±0.57735... | 1 |   |
| 3 | 0 | ${\frac {8}{9}}$ | 0.888889... |   |
| $\pm {\sqrt {\frac {3}{5}}}$ | ±0.774597... | ${\frac {5}{9}}$ | 0.555556... |   |
| 4 | $\pm {\sqrt {{\frac {3}{7}}-{\frac {2}{7}}{\sqrt {\frac {6}{5}}}}}$ | ±0.339981... | ${\frac {18+{\sqrt {30}}}{36}}$ | 0.652145... |
| $\pm {\sqrt {{\frac {3}{7}}+{\frac {2}{7}}{\sqrt {\frac {6}{5}}}}}$ | ±0.861136... | ${\frac {18-{\sqrt {30}}}{36}}$ | 0.347855... |   |
| 5 | 0 | ${\frac {128}{225}}$ | 0.568889... |   |
| $\pm {\frac {1}{3}}{\sqrt {5-2{\sqrt {\frac {10}{7}}}}}$ | ±0.538469... | ${\frac {322+13{\sqrt {70}}}{900}}$ | 0.478629... |   |
| $\pm {\frac {1}{3}}{\sqrt {5+2{\sqrt {\frac {10}{7}}}}}$ | ±0.90618... | ${\frac {322-13{\sqrt {70}}}{900}}$ | 0.236927... |   |

## Change of interval

An integral over [*a*, *b*] must be changed into an integral over [−1, 1] before applying the Gaussian quadrature rule. This change of interval can be done in the following way: $\int _{a}^{b}f(x)\,dx=\int _{-1}^{1}f\left({\frac {b-a}{2}}\xi +{\frac {a+b}{2}}\right)\,{\frac {dx}{d\xi }}d\xi$

with ${\frac {dx}{d\xi }}={\frac {b-a}{2}}$

Applying the n point Gaussian quadrature $(\xi ,w)$ rule then results in the following approximation: $\int _{a}^{b}f(x)\,dx\approx {\frac {b-a}{2}}\sum _{i=1}^{n}w_{i}f\left({\frac {b-a}{2}}\xi _{i}+{\frac {a+b}{2}}\right).$

## Example of two-point Gauss quadrature rule

Use the two-point Gauss quadrature rule to approximate the distance in meters covered by a rocket from $t=8\mathrm {s}$ to $t=30\mathrm {s} ,$ as given by $s=\int _{8}^{30}{\left(2000\ln \left[{\frac {140000}{140000-2100t}}\right]-9.8t\right){dt}}$

Change the limits so that one can use the weights and abscissae given in Table 1. Also, find the absolute relative true error. The true value is given as 11061.34 m.

Solution

First, changing the limits of integration from $\left[8,30\right]$ to $\left[-1,1\right]$ gives

${\begin{aligned}\int _{8}^{30}{f(t)dt}&={\frac {30-8}{2}}\int _{-1}^{1}{f\left({\frac {30-8}{2}}x+{\frac {30+8}{2}}\right){dx}}\\&=11\int _{-1}^{1}{f\left(11x+19\right){dx}}\end{aligned}}$

Next, get the weighting factors and function argument values from Table 1 for the two-point rule,

- $c_{1}=1.000000000$
- $x_{1}=-0.577350269$
- $c_{2}=1.000000000$
- $x_{2}=0.577350269$

Now we can use the Gauss quadrature formula ${\begin{aligned}11\int _{-1}^{1}{f\left(11x+19\right){dx}}&\approx 11\left[c_{1}f\left(11x_{1}+19\right)+c_{2}f\left(11x_{2}+19\right)\right]\\&=11\left[f\left(11(-0.5773503)+19\right)+f\left(11(0.5773503)+19\right)\right]\\&=11\left[f(12.64915)+f(25.35085)\right]\\&=11\left[(296.8317)+(708.4811)\right]\\&=11058.44\end{aligned}}$ since ${\begin{aligned}f(12.64915)&=2000\ln \left[{\frac {140000}{140000-2100(12.64915)}}\right]-9.8(12.64915)\\&=296.8317\end{aligned}}$ ${\begin{aligned}f(25.35085)&=2000\ln \left[{\frac {140000}{140000-2100(25.35085)}}\right]-9.8(25.35085)\\&=708.4811\end{aligned}}$

Given that the true value is 11061.34 m, the absolute relative true error, $\left|\varepsilon _{t}\right|$ is $\left|\varepsilon _{t}\right|=\left|{\frac {11061.34-11058.44}{11061.34}}\right|\times 100\%=0.0262\%$

## Other forms

The integration problem can be expressed in a slightly more general way by introducing a positive weight function ω into the integrand, and allowing an interval other than [−1, 1]. That is, the problem is to calculate $\int _{a}^{b}\omega (x)\,f(x)\,dx$ for some choices of a, b, and ω. For *a* = −1, *b* = 1, and *ω*(*x*) = 1, the problem is the same as that considered above. Other choices lead to other integration rules. Some of these are tabulated below. Equation numbers are given for Abramowitz and Stegun (A & S).

| Interval | *ω*(*x*) | Orthogonal polynomials | A & S | For more information, see ... |
|---|---|---|---|---|
| [−1, 1] | 1 | Legendre polynomials | 25.4.29 | § Gauss–Legendre quadrature |
| (−1, 1) | $\left(1-x\right)^{\alpha }\left(1+x\right)^{\beta },\quad \alpha ,\beta >-1$ | Jacobi polynomials | 25.4.33 (*β* = 0) | Gauss–Jacobi quadrature |
| (−1, 1) | ${\frac {1}{\sqrt {1-x^{2}}}}$ | Chebyshev polynomials (first kind) | 25.4.38 | Chebyshev–Gauss quadrature |
| [−1, 1] | ${\sqrt {1-x^{2}}}$ | Chebyshev polynomials (second kind) | 25.4.40 | Chebyshev–Gauss quadrature |
| [0, ∞) | $e^{-x}\,$ | Laguerre polynomials | 25.4.45 | Gauss–Laguerre quadrature |
| [0, ∞) | $x^{\alpha }e^{-x},\quad \alpha >-1$ | Generalized Laguerre polynomials |   | Gauss–Laguerre quadrature |
| (−∞, ∞) | $e^{-x^{2}}$ | Hermite polynomials | 25.4.46 | Gauss–Hermite quadrature |

### Fundamental theorem

Let pn be a nontrivial polynomial of degree n such that $\int _{a}^{b}\omega (x)\,x^{k}p_{n}(x)\,dx=0,\quad {\text{for all }}k=0,1,\ldots ,n-1.$

Note that this will be true for all the orthogonal polynomials above, because each pn is constructed to be orthogonal to the other polynomials pj for *j*<*n*, and *x**k* is in the span of that set.

If we pick the n nodes xi to be the zeros of pn, $p_{n}\propto \prod _{i=1}^{n}(x-x_{i})$ , then there exist n weights wi which make the Gaussian quadrature computed integral exact for all polynomials *h*(*x*) of degree 2*n* − 1 or less. Furthermore, all these nodes xi will lie in the open interval (*a*, *b*).

To prove the first part of this claim, let *h*(*x*) be any polynomial of degree 2*n* − 1 or less. Divide it by the orthogonal polynomial pn to get $h(x)=p_{n}(x)\,q(x)+r(x).$ where *q*(*x*) is the quotient, of degree *n* − 1 or less (because the sum of its degree and that of the divisor pn must equal that of the dividend), and *r*(*x*) is the remainder, also of degree *n* − 1 or less (because the degree of the remainder is always less than that of the divisor). Since pn is by assumption orthogonal to all monomials of degree less than n, it must be orthogonal to the quotient *q*(*x*). Therefore $\int _{a}^{b}\omega (x)\,h(x)\,dx=\int _{a}^{b}\omega (x)\,{\big (}\,p_{n}(x)q(x)+r(x)\,{\big )}\,dx=\int _{a}^{b}\omega (x)\,r(x)\,dx.$

Since the remainder *r*(*x*) is of degree *n* − 1 or less, we can interpolate it exactly using n interpolation points with Lagrange polynomials *l**i*(*x*), where $l_{i}(x)=\prod _{j\neq i}{\frac {x-x_{j}}{x_{i}-x_{j}}}.$

We have $r(x)=\sum _{i=1}^{n}l_{i}(x)\,r(x_{i}).$

Then its integral will equal $\int _{a}^{b}\omega (x)\,r(x)\,dx=\int _{a}^{b}\omega (x)\,\sum _{i=1}^{n}l_{i}(x)\,r(x_{i})\,dx=\sum _{i=1}^{n}\,r(x_{i})\,\int _{a}^{b}\omega (x)\,l_{i}(x)\,dx=\sum _{i=1}^{n}\,r(x_{i})\,w_{i},$

where *w**i*, the weight associated with the node *x**i*, is defined to equal the weighted integral of *l**i*(*x*) (see below for other formulas for the weights). But all the xi are roots of pn, so the division formula above tells us that $h(x_{i})=p_{n}(x_{i})\,q(x_{i})+r(x_{i})=r(x_{i}),$ for all i. Thus we finally have $\int _{a}^{b}\omega (x)\,h(x)\,dx=\int _{a}^{b}\omega (x)\,r(x)\,dx=\sum _{i=1}^{n}w_{i}\,r(x_{i})=\sum _{i=1}^{n}w_{i}\,h(x_{i}).$

This proves that for any polynomial *h*(*x*) of degree 2*n* − 1 or less, its integral is given exactly by the Gaussian quadrature sum.

To prove the second part of the claim, consider the factored form of the polynomial *p**n*. Any complex conjugate roots will yield a quadratic factor that is either strictly positive or strictly negative over the entire real line. Any factors for roots outside the interval from a to b will not change sign over that interval. Finally, for factors corresponding to roots xi inside the interval from a to b that are of odd multiplicity, multiply *p**n* by one more factor to make a new polynomial $p_{n}(x)\,\prod _{i}(x-x_{i}).$

This polynomial cannot change sign over the interval from a to b because all its roots there are now of even multiplicity. So the integral $\int _{a}^{b}p_{n}(x)\,\left(\prod _{i}(x-x_{i})\right)\,\omega (x)\,dx\neq 0,$ since the weight function *ω*(*x*) is always non-negative. But *p**n* is orthogonal to all polynomials of degree *n* − 1 or less, so the degree of the product $\prod _{i}(x-x_{i})$ must be at least n. Therefore *p**n* has n distinct roots, all real, in the interval from a to b.

#### General formula for the weights

The weights can be expressed as

| $w_{i}={\frac {a_{n}}{a_{n-1}}}{\frac {\int _{a}^{b}\omega (x)p_{n-1}(x)^{2}dx}{p'_{n}(x_{i})p_{n-1}(x_{i})}}$ |   | 1 |
|---|---|---|

where $a_{k}$ is the coefficient of $x^{k}$ in $p_{k}(x)$ . To prove this, note that using Lagrange interpolation one can express *r*(*x*) in terms of $r(x_{i})$ as $r(x)=\sum _{i=1}^{n}r(x_{i})\prod _{\begin{smallmatrix}1\leq j\leq n\\j\neq i\end{smallmatrix}}{\frac {x-x_{j}}{x_{i}-x_{j}}}$ because *r*(*x*) has degree less than n and is thus fixed by the values it attains at n different points. Multiplying both sides by *ω*(*x*) and integrating from a to b yields $\int _{a}^{b}\omega (x)r(x)dx=\sum _{i=1}^{n}r(x_{i})\int _{a}^{b}\omega (x)\prod _{\begin{smallmatrix}1\leq j\leq n\\j\neq i\end{smallmatrix}}{\frac {x-x_{j}}{x_{i}-x_{j}}}dx$

The weights wi are thus given by $w_{i}=\int _{a}^{b}\omega (x)\prod _{\begin{smallmatrix}1\leq j\leq n\\j\neq i\end{smallmatrix}}{\frac {x-x_{j}}{x_{i}-x_{j}}}dx$

This integral expression for $w_{i}$ can be expressed in terms of the orthogonal polynomials $p_{n}(x)$ and $p_{n-1}(x)$ as follows.

We can write $\prod _{\begin{smallmatrix}1\leq j\leq n\\j\neq i\end{smallmatrix}}\left(x-x_{j}\right)={\frac {\prod _{1\leq j\leq n}\left(x-x_{j}\right)}{x-x_{i}}}={\frac {p_{n}(x)}{a_{n}\left(x-x_{i}\right)}}$

where $a_{n}$ is the coefficient of $x^{n}$ in $p_{n}(x)$ . Taking the limit of x to $x_{i}$ yields using L'Hôpital's rule $\prod _{\begin{smallmatrix}1\leq j\leq n\\j\neq i\end{smallmatrix}}\left(x_{i}-x_{j}\right)={\frac {p'_{n}(x_{i})}{a_{n}}}$

We can thus write the integral expression for the weights as

| $w_{i}={\frac {1}{p'_{n}(x_{i})}}\int _{a}^{b}\omega (x){\frac {p_{n}(x)}{x-x_{i}}}dx$ |   | 2 |
|---|---|---|

In the integrand, writing ${\frac {1}{x-x_{i}}}={\frac {1-\left({\frac {x}{x_{i}}}\right)^{k}}{x-x_{i}}}+\left({\frac {x}{x_{i}}}\right)^{k}{\frac {1}{x-x_{i}}}$

yields $\int _{a}^{b}\omega (x){\frac {x^{k}p_{n}(x)}{x-x_{i}}}dx=x_{i}^{k}\int _{a}^{b}\omega (x){\frac {p_{n}(x)}{x-x_{i}}}dx$

provided $k\leq n$ , because ${\frac {1-\left({\frac {x}{x_{i}}}\right)^{k}}{x-x_{i}}}$ is a polynomial of degree *k* − 1 which is then orthogonal to $p_{n}(x)$ . So, if *q*(*x*) is a polynomial of at most nth degree we have $\int _{a}^{b}\omega (x){\frac {p_{n}(x)}{x-x_{i}}}dx={\frac {1}{q(x_{i})}}\int _{a}^{b}\omega (x){\frac {q(x)p_{n}(x)}{x-x_{i}}}dx$

We can evaluate the integral on the right hand side for $q(x)=p_{n-1}(x)$ as follows. Because ${\frac {p_{n}(x)}{x-x_{i}}}$ is a polynomial of degree *n* − 1, we have ${\frac {p_{n}(x)}{x-x_{i}}}=a_{n}x^{n-1}+s(x)$ where *s*(*x*) is a polynomial of degree $n-2$ . Since *s*(*x*) is orthogonal to $p_{n-1}(x)$ we have $\int _{a}^{b}\omega (x){\frac {p_{n}(x)}{x-x_{i}}}dx={\frac {a_{n}}{p_{n-1}(x_{i})}}\int _{a}^{b}\omega (x)p_{n-1}(x)x^{n-1}dx$

We can then write $x^{n-1}=\left(x^{n-1}-{\frac {p_{n-1}(x)}{a_{n-1}}}\right)+{\frac {p_{n-1}(x)}{a_{n-1}}}$

The term in the brackets is a polynomial of degree $n-2$ , which is therefore orthogonal to $p_{n-1}(x)$ . The integral can thus be written as $\int _{a}^{b}\omega (x){\frac {p_{n}(x)}{x-x_{i}}}dx={\frac {a_{n}}{a_{n-1}p_{n-1}(x_{i})}}\int _{a}^{b}\omega (x)p_{n-1}(x)^{2}dx$

According to equation (**2**), the weights are obtained by dividing this by $p'_{n}(x_{i})$ and that yields the expression in equation (**1**).

$w_{i}$ can also be expressed in terms of the orthogonal polynomials $p_{n}(x)$ and now $p_{n+1}(x)$ . In the 3-term recurrence relation $p_{n+1}(x_{i})=(a)p_{n}(x_{i})+(b)p_{n-1}(x_{i})$ the term with $p_{n}(x_{i})$ vanishes, so $p_{n-1}(x_{i})$ in Eq. (1) can be replaced by ${\textstyle {\frac {1}{b}}p_{n+1}\left(x_{i}\right)}$ .

#### Proof that the weights are positive

Consider the following polynomial of degree $2n-2$ $f(x)=\prod _{\begin{smallmatrix}1\leq j\leq n\\j\neq i\end{smallmatrix}}{\frac {\left(x-x_{j}\right)^{2}}{\left(x_{i}-x_{j}\right)^{2}}}$ where, as above, the xj are the roots of the polynomial $p_{n}(x)$ . Clearly $f(x_{j})=\delta _{ij}$ . Since the degree of $f(x)$ is less than $2n-1$ , the Gaussian quadrature formula involving the weights and nodes obtained from $p_{n}(x)$ applies. Since $f(x_{j})=0$ for j not equal to i, we have $\int _{a}^{b}\omega (x)f(x)dx=\sum _{j=1}^{n}w_{j}f(x_{j})=\sum _{j=1}^{n}\delta _{ij}w_{j}=w_{i}>0.$

Since both $\omega (x)$ and $f(x)$ are non-negative functions, it follows that $w_{i}>0$ .

### Computation of Gaussian quadrature rules

There are many algorithms for computing the nodes xi and weights wi of Gaussian quadrature rules. The most popular are the Golub-Welsch algorithm requiring *O*(*n*2) operations, Newton's method for solving $p_{n}(x)=0$ using the three-term recurrence for evaluation requiring *O*(*n*2) operations, and asymptotic formulas for large *n* requiring *O*(*n*) operations.

#### Recurrence relation

Orthogonal polynomials $p_{r}$ with $(p_{r},p_{s})=0$ for $r\neq s$ for a scalar product $(\cdot ,\cdot )$ , degree $(p_{r})=r$ and leading coefficient one (i.e. monic orthogonal polynomials) satisfy the recurrence relation $p_{r+1}(x)=(x-a_{r,r})p_{r}(x)-a_{r,r-1}p_{r-1}(x)\cdots -a_{r,0}p_{0}(x)$

and scalar product defined $(f(x),g(x))=\int _{a}^{b}\omega (x)f(x)g(x)dx$

for $r=0,1,\ldots ,n-1$ where n is the maximal degree which can be taken to be infinity, and where ${\textstyle a_{r,s}={\frac {\left(xp_{r},p_{s}\right)}{\left(p_{s},p_{s}\right)}}}$ . First of all, the polynomials defined by the recurrence relation starting with $p_{0}(x)=1$ have leading coefficient one and correct degree. Given the starting point by $p_{0}$ , the orthogonality of $p_{r}$ can be shown by induction. For $r=s=0$ one has $(p_{1},p_{0})=(x-a_{0,0})(p_{0},p_{0})=(xp_{0},p_{0})-a_{0,0}(p_{0},p_{0})=(xp_{0},p_{0})-(xp_{0},p_{0})=0.$

Now if $p_{0},p_{1},\ldots ,p_{r}$ are orthogonal, then also $p_{r+1}$ , because in $(p_{r+1},p_{s})=(xp_{r},p_{s})-a_{r,r}(p_{r},p_{s})-a_{r,r-1}(p_{r-1},p_{s})\cdots -a_{r,0}(p_{0},p_{s})$ all scalar products vanish except for the first one and the one where $p_{s}$ meets the same orthogonal polynomial. Therefore, $(p_{r+1},p_{s})=(xp_{r},p_{s})-a_{r,s}(p_{s},p_{s})=(xp_{r},p_{s})-(xp_{r},p_{s})=0.$

However, if the scalar product satisfies $(xf,g)=(f,xg)$ (which is the case for Gaussian quadrature), the recurrence relation reduces to a three-term recurrence relation: For $s<r-1,xp_{s}$ is a polynomial of degree less than or equal to *r* − 1. On the other hand, $p_{r}$ is orthogonal to every polynomial of degree less than or equal to *r* − 1. Therefore, one has $(xp_{r},p_{s})=(p_{r},xp_{s})=0$ and $a_{r,s}=0$ for *s* < *r* − 1. The recurrence relation then simplifies to $p_{r+1}(x)=(x-a_{r,r})p_{r}(x)-a_{r,r-1}p_{r-1}(x)$

or $p_{r+1}(x)=(x-a_{r})p_{r}(x)-b_{r}p_{r-1}(x)$

(with the convention $p_{-1}(x)\equiv 0$ ) where $a_{r}:={\frac {(xp_{r},p_{r})}{(p_{r},p_{r})}},\qquad b_{r}:={\frac {(xp_{r},p_{r-1})}{(p_{r-1},p_{r-1})}}={\frac {(p_{r},p_{r})}{(p_{r-1},p_{r-1})}}$

(the last because of $(xp_{r},p_{r-1})=(p_{r},xp_{r-1})=(p_{r},p_{r})$ , since $xp_{r-1}$ differs from $p_{r}$ by a degree less than r).

#### The Golub-Welsch algorithm

The three-term recurrence relation can be written in matrix form $J{\tilde {P}}=x{\tilde {P}}-p_{n}(x)\mathbf {e} _{n}$ where ${\tilde {P}}={\begin{bmatrix}p_{0}(x)&p_{1}(x)&\cdots &p_{n-1}(x)\end{bmatrix}}^{\mathsf {T}}$ , $\mathbf {e} _{n}$ is the n th standard basis vector, i.e., $\mathbf {e} _{n}={\begin{bmatrix}0&\cdots &0&1\end{bmatrix}}^{\mathsf {T}}$ , and J is the following tridiagonal matrix, called the Jacobi matrix: $\mathbf {J} ={\begin{bmatrix}a_{0}&1&0&\cdots &0\\b_{1}&a_{1}&1&\ddots &\vdots \\0&b_{2}&\ddots &\ddots &0\\\vdots &\ddots &\ddots &a_{n-2}&1\\0&\cdots &0&b_{n-1}&a_{n-1}\end{bmatrix}}.$

The zeros $x_{j}$ of the polynomials up to degree n, which are used as nodes for the Gaussian quadrature can be found by computing the eigenvalues of this matrix. This procedure is known as *Golub–Welsch algorithm*.

For computing the weights and nodes, it is preferable to consider the symmetric tridiagonal matrix ${\mathcal {J}}$ with elements ${\begin{aligned}{\mathcal {J}}_{k,i}=J_{k,i}&=a_{k-1}&k&=1,2,\ldots ,n\\[2.1ex]{\mathcal {J}}_{k-1,i}={\mathcal {J}}_{k,k-1}={\sqrt {J_{k,k-1}J_{k-1,k}}}&={\sqrt {b_{k-1}}}&k&={\hphantom {1,\,}}2,\ldots ,n.\end{aligned}}$

That is,

${\mathcal {J}}={\begin{bmatrix}a_{0}&{\sqrt {b_{1}}}&0&\cdots &0\\{\sqrt {b_{1}}}&a_{1}&{\sqrt {b_{2}}}&\ddots &\vdots \\0&{\sqrt {b_{2}}}&\ddots &\ddots &0\\\vdots &\ddots &\ddots &a_{n-2}&{\sqrt {b_{n-1}}}\\0&\cdots &0&{\sqrt {b_{n-1}}}&a_{n-1}\end{bmatrix}}.$

**J** and ${\mathcal {J}}$ are similar matrices and therefore have the same eigenvalues (the nodes). The weights can be computed from the corresponding eigenvectors: If $\phi ^{(j)}$ is a normalized eigenvector (i.e., an eigenvector with euclidean norm equal to one) associated with the eigenvalue xj, the corresponding weight can be computed from the first component of this eigenvector, namely: $w_{j}=\mu _{0}\left(\phi _{1}^{(j)}\right)^{2}$

where $\mu _{0}$ is the integral of the weight function $\mu _{0}=\int _{a}^{b}\omega (x)dx.$

See, for instance, (Gil, Segura & Temme 2007) for further details.

### Error estimates

The error of a Gaussian quadrature rule can be stated as follows. For an integrand which has 2*n* continuous derivatives, $\int _{a}^{b}\omega (x)\,f(x)\,dx-\sum _{i=1}^{n}w_{i}\,f(x_{i})={\frac {f^{(2n)}(\xi )}{(2n)!}}\,(p_{n},p_{n})$ for some ξ in (*a*, *b*), where pn is the monic (i.e. the leading coefficient is 1) orthogonal polynomial of degree n and where $(f,g)=\int _{a}^{b}\omega (x)f(x)g(x)\,dx.$

In the important special case of *ω*(*x*) = 1, we have the error estimate ${\frac {\left(b-a\right)^{2n+1}\left(n!\right)^{4}}{(2n+1)\left[\left(2n\right)!\right]^{3}}}f^{(2n)}(\xi ),\qquad a<\xi <b.$

Stoer and Bulirsch remark that this error estimate is inconvenient in practice, since it may be difficult to estimate the order 2*n* derivative, and furthermore the actual error may be much less than a bound established by the derivative. Another approach is to use two Gaussian quadrature rules of different orders, and to estimate the error as the difference between the two results. For this purpose, Gauss–Kronrod quadrature rules can be useful.

### Gauss–Kronrod rules

If the interval [*a*, *b*] is subdivided, the Gauss evaluation points of the new subintervals never coincide with the previous evaluation points (except at zero for odd numbers), and thus the integrand must be evaluated at every point. *Gauss–Kronrod rules* are extensions of Gauss quadrature rules generated by adding *n* + 1 points to an n-point rule in such a way that the resulting rule is of order 2*n* + 1. This allows for computing higher-order estimates while re-using the function values of a lower-order estimate. The difference between a Gauss quadrature rule and its Kronrod extension is often used as an estimate of the approximation error.

### Gauss–Lobatto rules

In some applications, it is desirable to have quadrature rules that have the high accuracy of Gauss formulas, but that also include the end points of the interval among the evaluation points. Such rules are known as **Gauss–Lobatto**, or simply **Lobatto quadrature**, named after Dutch mathematician Rehuel Lobatto. Because for an *n* point rule, one can no longer freely choose the locations of all quadrature points (2 of the points are fixed at the end points), one needs to expect that the rule is less accurate than regular Gaussian quadrature. Indeed, an *n* point Gauss-Lobatto rule is only accurate for polynomials up to degree 2*n* − 3.

Lobatto quadrature of function *f*(*x*) on interval [−1, 1]: $\int _{-1}^{1}{f(x)\,dx}={\frac {2}{n(n-1)}}[f(1)+f(-1)]+\sum _{i=2}^{n-1}{w_{i}f(x_{i})}+R_{n}.$

Abscissas: xi is the $(i-1)$ st zero of $P'_{n-1}(x)$ , here $P_{m}(x)$ denotes the standard Legendre polynomial of m-th degree and the dash denotes the derivative.

Weights: $w_{i}={\frac {2}{n(n-1)\left[P_{n-1}\left(x_{i}\right)\right]^{2}}},\qquad x_{i}\neq \pm 1.$

Remainder: $R_{n}={\frac {-n\left(n-1\right)^{3}2^{2n-1}\left[\left(n-2\right)!\right]^{4}}{(2n-1)\left[\left(2n-2\right)!\right]^{3}}}f^{(2n-2)}(\xi ),\qquad -1<\xi <1.$

Some of the weights are:

| Number of points, *n* | Points, xi | Weights, wi |
|---|---|---|
| 3 | 0 | ${\frac {4}{3}}$ |
| $\pm 1$ | ${\frac {1}{3}}$ |   |
| 4 | $\pm {\sqrt {\frac {1}{5}}}$ | ${\frac {5}{6}}$ |
| $\pm 1$ | ${\frac {1}{6}}$ |   |
| 5 | 0 | ${\frac {32}{45}}$ |
| $\pm {\sqrt {\frac {3}{7}}}$ | ${\frac {49}{90}}$ |   |
| $\pm 1$ | ${\frac {1}{10}}$ |   |
| 6 | $\pm {\sqrt {{\frac {1}{3}}-{\frac {2{\sqrt {7}}}{21}}}}$ | ${\frac {14+{\sqrt {7}}}{30}}$ |
| $\pm {\sqrt {{\frac {1}{3}}+{\frac {2{\sqrt {7}}}{21}}}}$ | ${\frac {14-{\sqrt {7}}}{30}}$ |   |
| $\pm 1$ | ${\frac {1}{15}}$ |   |
| 7 | 0 | ${\frac {256}{525}}$ |
| $\pm {\sqrt {{\frac {5}{11}}-{\frac {2}{11}}{\sqrt {\frac {5}{3}}}}}$ | ${\frac {124+7{\sqrt {15}}}{350}}$ |   |
| $\pm {\sqrt {{\frac {5}{11}}+{\frac {2}{11}}{\sqrt {\frac {5}{3}}}}}$ | ${\frac {124-7{\sqrt {15}}}{350}}$ |   |
| $\pm 1$ | ${\frac {1}{21}}$ |   |

An adaptive variant of this algorithm with 2 interior nodes is found in GNU Octave and MATLAB as `quadl` and `integrate`.
