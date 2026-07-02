---
title: "Newton polynomial"
source: https://en.wikipedia.org/wiki/Newton_polynomial
domain: interpolation-methods
license: CC-BY-SA-4.0
tags: polynomial interpolation, lagrange polynomial, newton polynomial, runge phenomenon
fetched: 2026-07-02
---

# Newton polynomial

In the mathematical field of numerical analysis, a **Newton polynomial**, named after its inventor Isaac Newton, is an interpolation polynomial for a given set of data points. The Newton polynomial is sometimes called **Newton's divided differences interpolation polynomial** because the coefficients of the polynomial are calculated using Newton's divided differences method.

## Definition

Given a set of ⁠ $k+1$ ⁠ data points

$(x_{0},y_{0}),\ldots ,(x_{j},y_{j}),\ldots ,(x_{k},y_{k})$

where no two *x**j* are the same, the Newton interpolation polynomial is a linear combination of **Newton basis polynomials**

$N(x):=\sum _{j=0}^{k}a_{j}n_{j}(x)$

with the Newton basis polynomials defined as

$n_{j}(x):=\prod _{i=0}^{j-1}(x-x_{i})$

for ⁠ $j>0$ ⁠ and ⁠ $n_{0}(x)\equiv 1$ ⁠.

The coefficients are defined as

$a_{j}:=[y_{0},\ldots ,y_{j}]$

where $[y_{0},\ldots ,y_{j}]$ are the divided differences defined as ${\begin{aligned}{\mathopen {[}}y_{k}]&:=y_{k},&&k\in \{0,\ldots ,n\}\\{\mathopen {[}}y_{k},\ldots ,y_{k+j}]&:={\frac {[y_{k+1},\ldots ,y_{k+j}]-[y_{k},\ldots ,y_{k+j-1}]}{x_{k+j}-x_{k}}},&&k\in \{0,\ldots ,n-j\},\ j\in \{1,\ldots ,n\}.\end{aligned}}$

Thus the Newton polynomial can be written as

$N(x)=[y_{0}]+[y_{0},y_{1}](x-x_{0})+\cdots +[y_{0},\ldots ,y_{k}](x-x_{0})(x-x_{1})\cdots (x-x_{k-1}).$

### Newton forward divided difference formula

The Newton polynomial can be expressed in a simplified form when $x_{0},x_{1},\dots ,x_{k}$ are arranged consecutively with equal spacing.

If $x_{0},x_{1},\dots ,x_{k}$ are consecutively arranged and equally spaced with ${x}_{i}={x}_{0}+ih$ for ⁠ $i=0,1,\dots ,k$ ⁠ and some variable ⁠ x ⁠ is expressed as ⁠ ${x}={x}_{0}+sh$ ⁠, then the difference $x-x_{i}$ can be written as ⁠ $(s-i)h$ ⁠. So the Newton polynomial becomes

${\begin{aligned}N(x)&=[y_{0}]+[y_{0},y_{1}]sh+\cdots +[y_{0},\ldots ,y_{k}]s(s-1)\cdots (s-k+1){h}^{k}\\&=\sum _{i=0}^{k}s(s-1)\cdots (s-i+1){h}^{i}[y_{0},\ldots ,y_{i}]\\&=\sum _{i=0}^{k}{s \choose i}i!{h}^{i}[y_{0},\ldots ,y_{i}].\end{aligned}}$

This is called the **Newton forward divided difference formula**.

### Newton backward divided difference formula

If the nodes are reordered as ⁠ ${x}_{k},{x}_{k-1},\dots ,{x}_{0}$ ⁠, the Newton polynomial becomes

$N(x)=[y_{k}]+[{y}_{k},{y}_{k-1}](x-{x}_{k})+\cdots +[{y}_{k},\ldots ,{y}_{0}](x-{x}_{k})(x-{x}_{k-1})\cdots (x-{x}_{1}).$

If ${x}_{k},\;{x}_{k-1},\;\dots ,\;{x}_{0}$ are equally spaced with ${x}_{i}={x}_{k}-(k-i)h$ for ⁠ $i=0,1,\dots ,k$ ⁠ and ⁠ ${x}={x}_{k}+sh$ ⁠, then,

${\begin{aligned}N(x)&=[{y}_{k}]+[{y}_{k},{y}_{k-1}]sh+\cdots +[{y}_{k},\ldots ,{y}_{0}]s(s+1)\cdots (s+k-1){h}^{k}\\&=\sum _{i=0}^{k}{(-1)}^{i}{-s \choose i}i!{h}^{i}[{y}_{k},\ldots ,{y}_{k-i}].\end{aligned}}$

This is called the **Newton backward divided difference formula**.

## Significance

Newton's formula is of interest because it is the straightforward and natural differences-version of Taylor's polynomial. Taylor's polynomial tells where a function will go, based on its ⁠ y ⁠ value, and its derivatives (its rate of change, and the rate of change of its rate of change, etc.) at one particular ⁠ x ⁠ value. Newton's formula is Taylor's polynomial based on finite differences instead of instantaneous rates of change.

### Polynomial interpolation

For a polynomial $p_{n}$ of degree less than or equal to ⁠ n ⁠, that interpolates f at the nodes $x_{i}$ where ⁠ $i=0,1,2,3,\dots ,n$ ⁠. Let $p_{n+1}$ be the polynomial of degree less than or equal to ⁠ $n+1$ ⁠ that interpolates f at the nodes $x_{i}$ where ⁠ $i=0,1,2,3,\dots ,n,n+1$ ⁠. Then $p_{n+1}$ is given by: $p_{n+1}(x)=p_{n}(x)+a_{n+1}w_{n}(x)$ where ${\textstyle w_{n}(x):=\prod _{i=0}^{n}(x-x_{i})}$ and ⁠ $\textstyle a_{n+1}:={f(x_{n+1})-p_{n}(x_{n+1}) \over w_{n}(x_{n+1})}$ ⁠.

**Proof:**

This can be shown for the case where $i=0,1,2,3,\cdots ,n$ : $p_{n+1}(x_{i})=p_{n}(x_{i})+a_{n+1}\prod _{j=0}^{n}(x_{i}-x_{j})=p_{n}(x_{i})$ and when ⁠ $i=n+1$ ⁠: $p_{n+1}(x_{n+1})=p_{n}(x_{n+1})+{f(x_{n+1})-p_{n}(x_{n+1}) \over w_{n}(x_{n+1})}w_{n}(x_{n+1})=f(x_{n+1})$

By the uniqueness of interpolated polynomials of degree less than ⁠ $n+1$ ⁠, ${\textstyle p_{n+1}(x)=p_{n}(x)+a_{n+1}w_{n}(x)}$ is the required polynomial interpolation. The function can thus be expressed as: ${\textstyle p_{n}(x)=a_{0}+a_{1}(x-x_{0})+a_{2}(x-x_{0})(x-x_{1})+\cdots +a_{n}(x-x_{0})\cdots (x-x_{n-1})}$ where the factors $a_{i}$ are divided differences. Thus, Newton polynomials are used to provide polynomial interpolation formula of n points.

Taking $y_{i}=f(x_{i})$ for some unknown function in Newton divided difference formulas, if the representation of ⁠ x ⁠ in the previous sections was instead taken to be ⁠ $x=x_{j}+sh$ ⁠, in terms of forward differences, the **Newton forward interpolation formula** is expressed as: $f(x)\approx N(x)=N(x_{j}+sh)=\sum _{i=0}^{k}{s \choose i}\Delta ^{(i)}f(x_{j})$ whereas for the same in terms of backward differences, the **Newton backward interpolation formula** is expressed as: $f(x)\approx N(x)=N(x_{j}+sh)=\sum _{i=0}^{k}{(-1)}^{i}{-s \choose i}\nabla ^{(i)}f(x_{j}).$ This follows since relationship between divided differences and forward differences is given as: $[y_{j},y_{j+1},\ldots ,y_{j+n}]={\frac {1}{n!h^{n}}}\Delta ^{(n)}y_{j},$ whereas for backward differences, it is given as: $[{y}_{j},y_{j-1},\ldots ,{y}_{j-n}]={\frac {1}{n!h^{n}}}\nabla ^{(n)}y_{j}.$

## Addition of new points

As with other difference formulas, the degree of a Newton interpolating polynomial can be increased by adding more terms and points without discarding existing ones. Newton's form has the simplicity that the new points are always added at one end: Newton's forward formula can add new points to the right, and Newton's backward formula can add new points to the left.

The accuracy of polynomial interpolation depends on how close the interpolated point is to the middle of the ⁠ x ⁠ values of the set of points used. Obviously, as new points are added at one end, that middle becomes farther and farther from the first data point. Therefore, if it isn't known how many points will be needed for the desired accuracy, the middle of the ⁠ x ⁠-values might be far from where the interpolation is done.

Gauss, Stirling, and Bessel all developed formulae to remedy that problem.

Gauss's formula alternately adds new points at the left and right ends, thereby keeping the set of points centered near the same place (near the evaluated point). When so doing, it uses terms from Newton's formula, with data points and ⁠ x ⁠ values renamed in keeping with one's choice of what data point is designated as the ⁠ $x_{0}$ ⁠ data point.

Stirling's formula remains centered about a particular data point, for use when the evaluated point is nearer to a data point than to a middle of two data points.

Bessel's formula remains centered about a particular middle between two data points, for use when the evaluated point is nearer to a middle than to a data point.

Bessel and Stirling achieve that by sometimes using the average of two differences, and sometimes using the average of two products of binomials in ⁠ x ⁠, where Newton's or Gauss's would use just one difference or product. Stirling's uses an average difference in odd-degree terms (whose difference uses an even number of data points); Bessel's uses an average difference in even-degree terms (whose difference uses an odd number of data points).

## Strengths and weaknesses of various formulae

For any given finite set of data points, there is only one polynomial of least possible degree that passes through all of them. Thus, it is appropriate to speak of the "Newton form", or Lagrange form, etc., of the interpolation polynomial. However, different methods of computing this polynomial can have differing computational efficiency. There are several similar methods, such as those of Gauss, Bessel and Stirling. They can be derived from Newton's by renaming the ⁠ x ⁠-values of the data points, but in practice they are important.

### Bessel vs. Stirling

The choice between Bessel and Stirling depends on whether the interpolated point is closer to a data point, or closer to a middle between two data points.

A polynomial interpolation's error approaches zero, as the interpolation point approaches a data-point. Therefore, Stirling's formula brings its accuracy improvement where it is least needed and Bessel brings its accuracy improvement where it is most needed.

So, Bessel's formula could be said to be the most consistently accurate difference formula, and, in general, the most consistently accurate of the familiar polynomial interpolation formulas.

### Divided-difference methods vs. Lagrange

Lagrange is sometimes said to require less work, and is sometimes recommended for problems in which it is known, in advance, from previous experience, how many terms are needed for sufficient accuracy.

The divided difference methods have the advantage that more data points can be added, for improved accuracy. The terms based on the previous data points can continue to be used. With the ordinary Lagrange formula, to do the problem with more data points would require re-doing the whole problem.

There is a "barycentric" version of Lagrange that avoids the need to re-do the entire calculation when adding a new data point. But it requires that the values of each term be recorded.

But the ability, of Gauss, Bessel and Stirling, to keep the data points centered close to the interpolated point gives them an advantage over Lagrange, when it is not known, in advance, how many data points will be needed.

Additionally, suppose that one wants to find out if, for some particular type of problem, linear interpolation is sufficiently accurate. That can be determined by evaluating the quadratic term of a divided difference formula. If the quadratic term is negligible—meaning that the linear term is sufficiently accurate without adding the quadratic term—then linear interpolation is sufficiently accurate. If the problem is sufficiently important, or if the quadratic term is nearly big enough to matter, then one might want to determine whether the sum of the quadratic and cubic terms is large enough to matter in the problem.

Of course, only a divided-difference method can be used for such a determination.

For that purpose, the divided-difference formula and/or its ⁠ $x_{0}$ ⁠ point should be chosen so that the formula will use, for its linear term, the two data points between which the linear interpolation of interest would be done.

The divided difference formulas are more versatile, useful in more kinds of problems.

The Lagrange formula is at its best when all the interpolation will be done at one ⁠ x ⁠ value, with only the data points' ⁠ y ⁠ values varying from one problem to another, and when it is known, from past experience, how many terms are needed for sufficient accuracy.

With the Newton form of the interpolating polynomial a compact and effective algorithm exists for combining the terms to find the coefficients of the polynomial.

### Accuracy

When, with Stirling's or Bessel's, the last term used includes the average of two differences, then one more point is being used than Newton's or other polynomial interpolations would use for the same polynomial degree. So, in that instance, Stirling's or Bessel's is not putting an ⁠ $N-1$ ⁠ degree polynomial through ⁠ N ⁠ points, but is, instead, trading equivalence with Newton's for better centering and accuracy, giving those methods sometimes potentially greater accuracy, for a given polynomial degree, than other polynomial interpolations.

## General case

For the special case of ⁠ $x_{i}=i$ ⁠, there is a closely related set of polynomials, also called the Newton polynomials, that are simply the binomial coefficients for general argument. That is, one also has the Newton polynomials $p_{n}(z)$ given by

$p_{n}(z)={z \choose n}={\frac {z(z-1)\cdots (z-n+1)}{n!}}$

In this form, the Newton polynomials generate the Newton series. These are in turn a special case of the general difference polynomials which allow the representation of analytic functions through generalized difference equations.

## Main idea

Solving an interpolation problem leads to a problem in linear algebra where we have to solve a system of linear equations. Using a standard monomial basis for our interpolation polynomial we get the very complicated Vandermonde matrix. By choosing another basis, the Newton basis, we get a system of linear equations with a much simpler lower triangular matrix which can be solved faster.

For ⁠ $k+1$ ⁠ data points we construct the Newton basis as

$n_{0}(x):=1,\qquad n_{j}(x):=\prod _{i=0}^{j-1}(x-x_{i})\qquad j=1,\ldots ,k.$

Using these polynomials as a basis for $\Pi _{k}$ we have to solve

${\begin{bmatrix}1&&\ldots &&0\\1&x_{1}-x_{0}&&&\\1&x_{2}-x_{0}&(x_{2}-x_{0})(x_{2}-x_{1})&&\vdots \\\vdots &\vdots &&\ddots &\\1&x_{k}-x_{0}&\ldots &\ldots &\prod _{j=0}^{k-1}(x_{k}-x_{j})\end{bmatrix}}{\begin{bmatrix}a_{0}\\\\\vdots \\\\a_{k}\end{bmatrix}}={\begin{bmatrix}y_{0}\\\\\vdots \\\\y_{k}\end{bmatrix}}$

to solve the polynomial interpolation problem.

This system of equations can be solved iteratively by solving

$\sum _{i=0}^{j}a_{i}n_{i}(x_{j})=y_{j}\qquad j=0,\dots ,k.$

## Derivation

While the interpolation formula can be found by solving a linear system of equations, there is a loss of intuition in what the formula is showing and why Newton's interpolation formula works is not readily apparent. To begin, we will need to establish two facts first:

**Fact 1.** Reversing the terms of a divided difference leaves it unchanged: ⁠ $[y_{0},\ldots ,y_{n}]=[y_{n},\ldots ,y_{0}]$ ⁠.

The proof of this is an easy induction: for $n=1$ we compute $[y_{0},y_{1}]={\frac {[y_{1}]-[y_{0}]}{x_{1}-x_{0}}}={\frac {[y_{0}]-[y_{1}]}{x_{0}-x_{1}}}=[y_{1},y_{0}].$

Induction step: Suppose the result holds for any divided difference involving at most $n+1$ terms. Then using the induction hypothesis in the following 2nd equality we see that for a divided difference involving $n+2$ terms we have $[y_{0},\ldots ,y_{n+1}]={\frac {[y_{1},\ldots ,y_{n+1}]-[y_{0},\ldots ,y_{n}]}{x_{n+1}-x_{0}}}={\frac {[y_{n},\ldots ,y_{0}]-[y_{n+1},\ldots ,y_{1}]}{x_{0}-x_{n+1}}}=[y_{n+1},\ldots ,y_{0}].$

We formulate next Fact 2 which for purposes of induction and clarity we also call Statement n (⁠ ${\text{Stm}}_{n}$ ⁠):

**Fact 2.** ( ${\text{Stm}}_{n}$ ) : If $(x_{0},y_{0}),\ldots ,(x_{n-1},y_{n-1})$ are any n points with distinct x -coordinates and $P=P(x)$ is the unique polynomial of degree (at most) $n-1$ whose graph passes through these n points then there holds the relation $[y_{0},\ldots ,y_{n}](x_{n}-x_{0})\cdot \ldots \cdot (x_{n}-x_{n-1})=y_{n}-P(x_{n})$

Proof. (It will be helpful for fluent reading of the proof to have the precise statement and its subtlety in mind: P is defined by passing through $(x_{0},y_{0}),\dots ,(x_{n-1},y_{n-1})$ but the formula also speaks at both sides of an additional arbitrary point $(x_{n},y_{n})$ with x -coordinate distinct from the other ⁠ $x_{i}$ ⁠.)

We again prove these statements by induction. To show ⁠ ${\text{Stm}}_{1}$ ⁠, let $(x_{0},y_{0})$ be any one point and let $P(x)$ be the unique polynomial of degree 0 passing through ⁠ $(x_{0},y_{0})$ ⁠. Then evidently $P(x)=y_{0}$ and we can write $[y_{0},y_{1}](x_{1}-x_{0})={\frac {y_{1}-y_{0}}{x_{1}-x_{0}}}(x_{1}-x_{0})=y_{1}-y_{0}=y_{1}-P(x_{1})$ as wanted.

Proof of ⁠ ${\text{Stm}}_{n+1}$ ⁠, assuming ${\text{Stm}}_{n}$ already established: Let $P(x)$ be the polynomial of degree (at most) n passing through ⁠ $(x_{0},y_{0}),\ldots ,(x_{n},y_{n})$ ⁠.

With $Q(x)$ being the unique polynomial of degree (at most) $n-1$ passing through the points ⁠ $(x_{1},y_{1}),\ldots ,(x_{n},y_{n})$ ⁠, we can write the following chain of equalities, where we use in the penultimate equality that ⁠ ${\text{Stm}}_{n+1}$ ⁠ applies to ⁠ Q ⁠: ${\begin{aligned}&[y_{0},\ldots ,y_{n+1}](x_{n+1}-x_{0})\cdot \ldots \cdot (x_{n+1}-x_{n})\\&={\frac {[y_{1},\ldots ,y_{n+1}]-[y_{0},\ldots ,y_{n}]}{x_{n+1}-x_{0}}}(x_{n+1}-x_{0})\cdot \ldots \cdot (x_{n+1}-x_{n})\\&=\left([y_{1},\ldots ,y_{n+1}]-[y_{0},\ldots ,y_{n}]\right)(x_{n+1}-x_{1})\cdot \ldots \cdot (x_{n+1}-x_{n})\\&=[y_{1},\ldots ,y_{n+1}](x_{n+1}-x_{1})\cdot \ldots \cdot (x_{n+1}-x_{n})-[y_{0},\ldots ,y_{n}](x_{n+1}-x_{1})\cdot \ldots \cdot (x_{n+1}-x_{n})\\&=(y_{n+1}-Q(x_{n+1}))-[y_{0},\ldots ,y_{n}](x_{n+1}-x_{1})\cdot \ldots \cdot (x_{n+1}-x_{n})\\&=y_{n+1}-(Q(x_{n+1})+[y_{0},\ldots ,y_{n}](x_{n+1}-x_{1})\cdot \ldots \cdot (x_{n+1}-x_{n})).\end{aligned}}$

The induction hypothesis for Q also applies to the second equality in the following computation, where $(x_{0},y_{0})$ is added to the points defining ⁠ Q ⁠: ${\begin{aligned}&Q(x_{0})+[y_{0},\ldots ,y_{n}](x_{0}-x_{1})\cdot \ldots \cdot (x_{0}-x_{n})\\&=Q(x_{0})+[y_{n},\ldots ,y_{0}](x_{0}-x_{n})\cdot \ldots \cdot (x_{0}-x_{1})\\&=Q(x_{0})+y_{0}-Q(x_{0})\\&=y_{0}\\&=P(x_{0}).\\\end{aligned}}$

Now look at ⁠ $Q(x)+[y_{0},\ldots ,y_{n}](x-x_{1})\cdot \ldots \cdot (x-x_{n})$ ⁠. By the definition of Q this polynomial passes through $(x_{1},y_{1}),...,(x_{n},y_{n})$ and, as we have just shown, it also passes through ⁠ $(x_{0},y_{0})$ ⁠. Thus it is the unique polynomial of degree $\leq n$ which passes through these points. Therefore this polynomial is ⁠ $P(x)$ ⁠; i.e.: ⁠ $P(x)=Q(x)+[y_{0},\ldots ,y_{n}](x-x_{1})\cdot \ldots \cdot (x-x_{n})$ ⁠.

Thus we can write the last line in the first chain of equalities as '⁠ $y_{n+1}-P(x_{n+1})$ ⁠' and have thus established that $[y_{0},\ldots ,y_{n+1}](x_{n+1}-x_{0})\cdot \ldots \cdot (x_{n+1}-x_{n})=y_{n+1}-P(x_{n+1}).$ So we established ⁠ ${\text{Stm}}_{n+1}$ ⁠, and hence completed the proof of Fact 2.

Now look at Fact 2: It can be formulated this way: If P is the unique polynomial of degree at most $n-1$ whose graph passes through the points ⁠ $(x_{0},y_{0}),\dots ,(x_{n-1},y_{n-1})$ ⁠, then $P(x)+[y_{0},\ldots ,y_{n}](x-x_{0})\cdot \ldots \cdot (x-x_{n-1})$ is the unique polynomial of degree at most n passing through points ⁠ $(x_{0},y_{0}),\dots ,(x_{n-1},y_{n-1}),(x_{n},y_{n})$ ⁠. So we see Newton interpolation permits indeed to add new interpolation points without destroying what has already been computed.

## Taylor polynomial

The limit of the Newton polynomial if all nodes coincide is a Taylor polynomial, because the divided differences become derivatives. ${\begin{aligned}&\lim _{(x_{0},\dots ,x_{n})\to (z,\dots ,z)}f[x_{0}]+f[x_{0},x_{1}]\cdot (\xi -x_{0})+\dots +f[x_{0},\dots ,x_{n}]\cdot (\xi -x_{0})\cdot \dots \cdot (\xi -x_{n-1})\\&=f(z)+f'(z)\cdot (\xi -z)+\dots +{\frac {f^{(n)}(z)}{n!}}\cdot (\xi -z)^{n}\end{aligned}}$

## Application

As can be seen from the definition of the divided differences new data points can be added to the data set to create a new interpolation polynomial without recalculating the old coefficients. And when a data point changes we usually do not have to recalculate all coefficients. Furthermore, if the *x**i* are distributed equidistantly the calculation of the divided differences becomes significantly easier. Therefore, the divided-difference formulas are usually preferred over the Lagrange form for practical purposes.

### Examples

The divided differences can be written in the form of a table. For example, for a function ⁠ f ⁠ is to be interpolated on points ⁠ $x_{0},\ldots ,x_{n}$ ⁠. Write

${\begin{matrix}x_{0}&f(x_{0})&&\\&&{f(x_{1})-f(x_{0}) \over x_{1}-x_{0}}&\\x_{1}&f(x_{1})&&{{f(x_{2})-f(x_{1}) \over x_{2}-x_{1}}-{f(x_{1})-f(x_{0}) \over x_{1}-x_{0}} \over x_{2}-x_{0}}\\&&{f(x_{2})-f(x_{1}) \over x_{2}-x_{1}}&\\x_{2}&f(x_{2})&&\vdots \\&&\vdots &\\\vdots &&&\vdots \\&&\vdots &\\x_{n}&f(x_{n})&&\\\end{matrix}}$

Then the interpolating polynomial is formed as above using the topmost entries in each column as coefficients.

For example, suppose we are to construct the interpolating polynomial to ⁠ $f(x)=\tan(x)$ ⁠ using divided differences, at the points

| n | $x_{n}$ | $f(x_{n})$ |
|---|---|---|
| 0 | $-{\tfrac {3}{2}}$ | $-14.1014$ |
| 1 | $-{\tfrac {3}{4}}$ | $-0.931596$ |
| 2 | 0 | 0 |
| 3 | ${\tfrac {3}{4}}$ | $0.931596$ |
| 4 | ${\tfrac {3}{2}}$ | $14.1014$ |

Using six digits of accuracy, we construct the table

${\begin{matrix}-{\tfrac {3}{2}}&-14.1014&&&&\\&&17.5597&&&\\-{\tfrac {3}{4}}&-0.931596&&-10.8784&&\\&&1.24213&&4.83484&\\0&0&&0&&0\\&&1.24213&&4.83484&\\{\tfrac {3}{4}}&0.931596&&10.8784&&\\&&17.5597&&&\\{\tfrac {3}{2}}&14.1014&&&&\\\end{matrix}}$

Thus, the interpolating polynomial is

${\begin{aligned}&-14.1014+17.5597(x+{\tfrac {3}{2}})-10.8784(x+{\tfrac {3}{2}})(x+{\tfrac {3}{4}})+4.83484(x+{\tfrac {3}{2}})(x+{\tfrac {3}{4}})(x)+0(x+{\tfrac {3}{2}})(x+{\tfrac {3}{4}})(x)(x-{\tfrac {3}{4}})\\={}&-0.00005-1.4775x-0.00001x^{2}+4.83484x^{3}\end{aligned}}$

Given more digits of accuracy in the table, the first and third coefficients will be found to be zero.

Another example:

The sequence $f_{0}$ such that $f_{0}(1)=6,f_{0}(2)=9,f_{0}(3)=2$ and ⁠ $f_{0}(4)=5$ ⁠, i.e., they are $6,9,2,5$ from $x_{0}=1$ to ⁠ $x_{3}=4$ ⁠.

You obtain the slope of order 1 in the following way:

- $f_{1}(x_{0},x_{1})={\frac {f_{0}(x_{1})-f_{0}(x_{0})}{x_{1}-x_{0}}}={\frac {9-6}{2-1}}=3$
- $f_{1}(x_{1},x_{2})={\frac {f_{0}(x_{2})-f_{0}(x_{1})}{x_{2}-x_{1}}}={\frac {2-9}{3-2}}=-7$
- $f_{1}(x_{2},x_{3})={\frac {f_{0}(x_{3})-f_{0}(x_{2})}{x_{3}-x_{2}}}={\frac {5-2}{4-3}}=3$

As we have the slopes of order 1 , it is possible to obtain the next order:

- $f_{2}(x_{0},x_{1},x_{2})={\frac {f_{1}(x_{1},x_{2})-f_{1}(x_{0},x_{1})}{x_{2}-x_{0}}}={\frac {-7-3}{3-1}}=-5$
- $f_{2}(x_{1},x_{2},x_{3})={\frac {f_{1}(x_{2},x_{3})-f_{1}(x_{1},x_{2})}{x_{3}-x_{1}}}={\frac {3-(-7)}{4-2}}=5$

Finally, we define the slope of order ⁠ 3 ⁠:

- $f_{3}(x_{0},x_{1},x_{2},x_{3})={\frac {f_{2}(x_{1},x_{2},x_{3})-f_{2}(x_{0},x_{1},x_{2})}{x_{3}-x_{0}}}={\frac {5-(-5)}{4-1}}={\frac {10}{3}}$

Once we have the slope, we can define the consequent polynomials:

- $p_{0}(x)=6$
- $p_{1}(x)=6+3(x-1)$
- $p_{2}(x)=6+3(x-1)-5(x-1)(x-2)$
- $p_{3}(x)=6+3(x-1)-5(x-1)(x-2)+{\frac {10}{3}}(x-1)(x-2)(x-3)$
