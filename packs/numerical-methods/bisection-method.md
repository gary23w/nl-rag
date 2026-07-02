---
title: "Bisection method"
source: https://en.wikipedia.org/wiki/Bisection_method
domain: numerical-methods
license: CC-BY-SA-4.0
tags: numerical analysis, numerical method, root finding, polynomial interpolation, numerical integration
fetched: 2026-07-02
---

# Bisection method

In mathematics, the **bisection method** is a root-finding method that applies to any continuous function for which one knows two values with opposite signs. The method consists of repeatedly bisecting the interval defined by these values, then selecting the subinterval in which the function changes sign, which therefore must contain a root. It is a very simple and robust method, but it is also relatively slow. Because of this, it is often used to obtain a rough approximation to a solution which is then used as a starting point for more rapidly converging methods. The method is also called the **interval halving** method, the **binary search method**, or the **dichotomy method**.

For polynomials, more elaborate methods exist for testing the existence of a root in an interval (Descartes' rule of signs, Sturm's theorem, Budan's theorem). They allow extending the bisection method into efficient algorithms for finding all real roots of a polynomial; see Real-root isolation.

## The method

The method is applicable for numerically solving the equation $f(x)=0$ for the real variable x , where f is a continuous function defined on an interval $[a,b]$ and where $f(a)$ and $f(b)$ have opposite signs. In this case a and b are said to bracket a root since, by the intermediate value theorem, the continuous function f must have at least one root in the interval $(a,b)$ .

At each step the method divides the interval in two parts/halves by computing the midpoint $c=(a+b)/2$ of the interval and the value of the function $f(c)$ at that point. If c itself is a root then the process has succeeded and stops. Otherwise, there are now only two possibilities: either $f(a)$ and $f(c)$ have opposite signs and bracket a root, or $f(c)$ and $f(b)$ have opposite signs and bracket a root. The method selects the subinterval that is guaranteed to be a bracket as the new interval to be used in the next step. In this way an interval that contains a zero of f is reduced in width by 50% at each step. The process is continued until the interval is sufficiently small.

Explicitly, if $f(c)=0$ then c may be taken as the solution and the process stops.

Otherwise, if $f(a)$ and $f(c)$ have the same signs,

- then the method sets $a=c$ ,
- else the method sets $b=c$ .

In both cases, the new $f(a)$ and $f(b)$ have opposite signs, so the method may be applied to this smaller interval.

Once the process starts, the signs at the left and right ends of the interval remain the same for all iterations.

### Stopping conditions

In order to determine when the iteration should stop, it is necessary to consider various possible stopping conditions with respect to a tolerance ( $\epsilon$ ). Burden and Faires (2016) identify the three stopping conditions:

- Absolute tolerance: $|p_{N}-p_{N-1}|<\epsilon$
- Relative tolerance: $\left|{\frac {p_{N}-p_{N-1}}{p_{N}}}\right|<\epsilon ,$ || $p_{N}\neq 0$
- $|f(p_{N})|<\epsilon .$

$|f(p_{N})|<\epsilon$ does not give an accurate result to within $\epsilon$ unless $|f'(p_{N})|\geq 1$ . The other two possibilities represent different concepts: the absolute difference $|c-a|\leq 5\times 10^{-t}$ says that c and a are the same to t decimal places, while the relative difference $\left|{\frac {c-a}{c}}\right|\leq 5\times 10^{-t}$ says that c and a are the same to t significant figures. If nothing is known about the value of the root, then relative tolerance is the best stopping condition.

### Iteration process

The input for the method is a continuous function f and an interval $[a,b]$ , such that the function values $f(a)$ and $f(b)$ are of opposite sign (there is at least one zero crossing within the interval). Each iteration performs these steps:

1. Calculate c , the midpoint of the interval, $c={\frac {a+b}{2}}$ ;
2. Calculate the function value at the midpoint, $f(c)$ ;
3. If $f(c)=0$ , return c;
4. If convergence is satisfactory (that is, $\left|c-a\right|\leq 5\times 10^{-t}|c|$ ), return c ;
5. Examine the sign of $f(c)$ and replace either a or b with c so that there is a zero crossing within the new interval.

### Example

Suppose that the bisection method is used to find a root of the polynomial

$f(x)=x^{3}-x-2\,.$

First, two numbers a and b have to be found such that $f(a)$ and $f(b)$ have opposite signs. For the above function, $a=1$ and $b=2$ satisfy this criterion, as

$f(1)=(1)^{3}-(1)-2=-2$

and

$f(2)=(2)^{3}-(2)-2=+4\,.$

Because the function is continuous, there must be a root within the interval [1, 2]. Iterating the bisection method on this interval gives increasingly accurate approximations:

| Iteration | $a_{n}$ | $b_{n}$ | $c_{n}$ | $f(c_{n})$ |
|---|---|---|---|---|
| 1 | 1 | 2 | 1.5 | −0.125 |
| 2 | 1.5 | 2 | 1.75 | 1.6093750 |
| 3 | 1.5 | 1.75 | 1.625 | 0.6660156 |
| 4 | 1.5 | 1.625 | 1.5625 | 0.2521973 |
| 5 | 1.5 | 1.5625 | 1.5312500 | 0.0591125 |
| 6 | 1.5 | 1.5312500 | 1.5156250 | −0.0340538 |
| 7 | 1.5156250 | 1.5312500 | 1.5234375 | 0.0122504 |
| 8 | 1.5156250 | 1.5234375 | 1.5195313 | −0.0109712 |
| 9 | 1.5195313 | 1.5234375 | 1.5214844 | 0.0006222 |
| 10 | 1.5195313 | 1.5214844 | 1.5205078 | −0.0051789 |
| 11 | 1.5205078 | 1.5214844 | 1.5209961 | −0.0022794 |
| 12 | 1.5209961 | 1.5214844 | 1.5212402 | −0.0008289 |
| 13 | 1.5212402 | 1.5214844 | 1.5213623 | −0.0001034 |
| 14 | 1.5213623 | 1.5214844 | 1.5214233 | 0.0002594 |
| 15 | 1.5213623 | 1.5214233 | 1.5213928 | 0.0000780 |

After 13 iterations, it becomes apparent that there is a convergence to about 1.521: a root for the polynomial.

## Generalization to higher dimensions

The bisection method has been generalized to multi-dimensional functions. Such methods are called **generalized bisection methods**.

### Methods based on degree computation

Some of these methods are based on computing the topological degree.

### Characteristic bisection method

The **characteristic bisection method** uses only the signs of a function in different points. Lef *f* be a function from R*d* to R*d*, for some integer *d* ≥ 2. A **characteristic polyhedron** (also called an **admissible polygon**) of *f* is a polyhedron in R*d*, having 2*d* vertices, such that in each vertex **v**, the combination of signs of *f*(**v**) is unique. For example, for *d*=2, a characteristic polyhedron of *f* is a quadrilateral with vertices (say) A,B,C,D, such that:

- Sign *f*(A) = (−,−), that is, *f*1(A)<0, *f*2(A)<0.
- Sign *f*(B) = (−,+), that is, *f*1(B)<0, *f*2(B)>0.
- Sign *f*(C) = (+,−), that is, *f*1(C)>0, *f*2(C)<0.
- Sign *f*(D) = (+,+), that is, *f*1(D)>0, *f*2(D)>0.

A **proper edge** of a characteristic polygon is a edge between a pair of vertices, such that the sign vector differs by only a single sign. In the above example, the proper edges of the characteristic quadrilateral are AB, AC, BD and CD. A **diagonal** is a pair of vertices, such that the sign vector differs by all *d* signs. In the above example, the diagonals are AD and BC.

At each iteration, the algorithm picks a proper edge of the polyhedron (say, A—B), and computes the signs of *f* in its mid-point (say, M). Then it proceeds as follows:

- If Sign *f*(M) = Sign(A), then A is replaced by M, and we get a smaller characteristic polyhedron.
- If Sign *f*(M) = Sign(B), then B is replaced by M, and we get a smaller characteristic polyhedron.
- Else, we pick a new proper edge and try again.

Suppose the diameter (= length of longest proper edge) of the original characteristic polyhedron is D. Then, at least $\log _{2}(D/\varepsilon )$ bisections of edges are required so that the diameter of the remaining polygon will be at most $\varepsilon$ .
