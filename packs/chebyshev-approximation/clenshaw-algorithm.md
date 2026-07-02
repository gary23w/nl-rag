---
title: "Clenshaw algorithm"
source: https://en.wikipedia.org/wiki/Clenshaw_algorithm
domain: chebyshev-approximation
license: CC-BY-SA-4.0
tags: chebyshev approximation, clenshaw algorithm, chebyshev nodes, equioscillation theorem
fetched: 2026-07-02
---

# Clenshaw algorithm

In numerical analysis, the **Clenshaw algorithm**, also called **Clenshaw summation**, is a recursive method to evaluate a linear combination of Chebyshev polynomials. The method was published by Charles William Clenshaw in 1955. It is a generalization of Horner's method for evaluating a linear combination of monomials.

It generalizes to more than just Chebyshev polynomials; it applies to any class of functions that can be defined by a three-term recurrence relation.

## Clenshaw algorithm

In full generality, the Clenshaw algorithm computes the weighted sum of a finite series of functions $\phi _{k}(x)$ : $S(x)=\sum _{k=0}^{n}a_{k}\phi _{k}(x)$ where $\phi _{k},\;k=0,1,\ldots$ is a sequence of functions that satisfy the linear recurrence relation $\phi _{k+1}(x)=\alpha _{k}(x)\,\phi _{k}(x)+\beta _{k}(x)\,\phi _{k-1}(x),$ where the coefficients $\alpha _{k}(x)$ and $\beta _{k}(x)$ are known in advance.

The algorithm is most useful when $\phi _{k}(x)$ are functions that are complicated to compute directly, but $\alpha _{k}(x)$ and $\beta _{k}(x)$ are particularly simple. In the most common applications, $\alpha (x)$ does not depend on k , and $\beta$ is a constant that depends on neither x nor k .

To perform the summation for given series of coefficients $a_{0},\ldots ,a_{n}$ , compute the values $b_{k}(x)$ by the "reverse" recurrence formula: ${\begin{aligned}b_{n+1}(x)&=b_{n+2}(x)=0,\\b_{k}(x)&=a_{k}+\alpha _{k}(x)\,b_{k+1}(x)+\beta _{k+1}(x)\,b_{k+2}(x).\end{aligned}}$

Note that this computation makes no direct reference to the functions $\phi _{k}(x)$ . After computing $b_{2}(x)$ and $b_{1}(x)$ , the desired sum can be expressed in terms of them and the simplest functions $\phi _{0}(x)$ and $\phi _{1}(x)$ : $S(x)=\phi _{0}(x)\,a_{0}+\phi _{1}(x)\,b_{1}(x)+\beta _{1}(x)\,\phi _{0}(x)\,b_{2}(x).$

See Fox and Parker for more information and stability analyses.

## Examples

### Horner as a special case of Clenshaw

A particularly simple case occurs when evaluating a polynomial of the form $S(x)=\sum _{k=0}^{n}a_{k}x^{k}.$ The functions are simply ${\begin{aligned}\phi _{0}(x)&=1,\\\phi _{k}(x)&=x^{k}=x\phi _{k-1}(x)\end{aligned}}$ and are produced by the recurrence coefficients $\alpha (x)=x$ and $\beta =0$ .

In this case, the recurrence formula to compute the sum is $b_{k}(x)=a_{k}+xb_{k+1}(x)$ and, in this case, the sum is simply $S(x)=a_{0}+xb_{1}(x)=b_{0}(x),$ which is exactly the usual Horner's method.

### Special case for Chebyshev series

Consider a truncated Chebyshev series $p_{n}(x)=a_{0}+a_{1}T_{1}(x)+a_{2}T_{2}(x)+\cdots +a_{n}T_{n}(x).$

The coefficients in the recursion relation for the Chebyshev polynomials are $\alpha (x)=2x,\quad \beta =-1,$ with the initial conditions $T_{0}(x)=1,\quad T_{1}(x)=x.$

Thus, the recurrence is $b_{k}(x)=a_{k}+2xb_{k+1}(x)-b_{k+2}(x)$ and the final results are $b_{0}(x)=a_{0}+2xb_{1}(x)-b_{2}(x),$ $p_{n}(x)={\tfrac {1}{2}}\left[a_{0}+b_{0}(x)-b_{2}(x)\right].$

An equivalent expression for the sum is given by $p_{n}(x)=a_{0}+xb_{1}(x)-b_{2}(x).$

### Meridian arc length on the ellipsoid

Clenshaw summation is extensively used in geodetic applications. A simple application is summing the trigonometric series to compute the meridian arc distance on the surface of an ellipsoid. These have the form $m(\theta )=C_{0}\,\theta +C_{1}\sin \theta +C_{2}\sin 2\theta +\cdots +C_{n}\sin n\theta .$

Leaving off the initial $C_{0}\,\theta$ term, the remainder is a summation of the appropriate form. There is no leading term because $\phi _{0}(\theta )=\sin 0\theta =\sin 0=0$ .

The recurrence relation for $\sin k\theta$ is $\sin(k+1)\theta =2\cos \theta \sin k\theta -\sin(k-1)\theta ,$ making the coefficients in the recursion relation $\alpha _{k}(\theta )=2\cos \theta ,\quad \beta _{k}=-1.$ and the evaluation of the series is given by ${\begin{aligned}b_{n+1}(\theta )&=b_{n+2}(\theta )=0,\\b_{k}(\theta )&=C_{k}+2\cos \theta \,b_{k+1}(\theta )-b_{k+2}(\theta ),\quad \mathrm {for\ } n\geq k\geq 1.\end{aligned}}$ The final step is made particularly simple because $\phi _{0}(\theta )=\sin 0=0$ , so the end of the recurrence is simply $b_{1}(\theta )\sin(\theta )$ ; the $C_{0}\,\theta$ term is added separately: $m(\theta )=C_{0}\,\theta +b_{1}(\theta )\sin \theta .$

Note that the algorithm requires only the evaluation of two trigonometric quantities $\cos \theta$ and $\sin \theta$ .

### Difference in meridian arc lengths

Sometimes it necessary to compute the difference of two meridian arcs in a way that maintains high relative accuracy. This is accomplished by using trigonometric identities to write $m(\theta _{1})-m(\theta _{2})=C_{0}(\theta _{1}-\theta _{2})+\sum _{k=1}^{n}2C_{k}\sin {\bigl (}{\textstyle {\frac {1}{2}}}k(\theta _{1}-\theta _{2}){\bigr )}\cos {\bigl (}{\textstyle {\frac {1}{2}}}k(\theta _{1}+\theta _{2}){\bigr )}.$ Clenshaw summation can be applied in this case provided we simultaneously compute $m(\theta _{1})+m(\theta _{2})$ and perform a matrix summation, ${\mathsf {M}}(\theta _{1},\theta _{2})={\begin{bmatrix}(m(\theta _{1})+m(\theta _{2}))/2\\(m(\theta _{1})-m(\theta _{2}))/(\theta _{1}-\theta _{2})\end{bmatrix}}=C_{0}{\begin{bmatrix}\mu \\1\end{bmatrix}}+\sum _{k=1}^{n}C_{k}{\mathsf {F}}_{k}(\theta _{1},\theta _{2}),$ where ${\begin{aligned}\delta &={\tfrac {1}{2}}(\theta _{1}-\theta _{2}),\\[1ex]\mu &={\tfrac {1}{2}}(\theta _{1}+\theta _{2}),\\[1ex]{\mathsf {F}}_{k}(\theta _{1},\theta _{2})&={\begin{bmatrix}\cos k\delta \sin k\mu \\{\dfrac {\sin k\delta }{\delta }}\cos k\mu \end{bmatrix}}.\end{aligned}}$ The first element of ${\mathsf {M}}(\theta _{1},\theta _{2})$ is the average value of m and the second element is the average slope. ${\mathsf {F}}_{k}(\theta _{1},\theta _{2})$ satisfies the recurrence relation ${\mathsf {F}}_{k+1}(\theta _{1},\theta _{2})={\mathsf {A}}(\theta _{1},\theta _{2}){\mathsf {F}}_{k}(\theta _{1},\theta _{2})-{\mathsf {F}}_{k-1}(\theta _{1},\theta _{2}),$ where ${\mathsf {A}}(\theta _{1},\theta _{2})=2{\begin{bmatrix}\cos \delta \cos \mu &-\delta \sin \delta \sin \mu \\-\displaystyle {\frac {\sin \delta }{\delta }}\sin \mu &\cos \delta \cos \mu \end{bmatrix}}$ takes the place of $\alpha$ in the recurrence relation, and $\beta =-1$ . The standard Clenshaw algorithm can now be applied to yield ${\begin{aligned}{\mathsf {B}}_{n+1}&={\mathsf {B}}_{n+2}={\mathsf {0}},\\[1ex]{\mathsf {B}}_{k}&=C_{k}{\mathsf {I}}+{\mathsf {A}}{\mathsf {B}}_{k+1}-{\mathsf {B}}_{k+2},\qquad \mathrm {for\ } n\geq k\geq 1,\\[1ex]{\mathsf {M}}(\theta _{1},\theta _{2})&=C_{0}{\begin{bmatrix}\mu \\1\end{bmatrix}}+{\mathsf {B}}_{1}{\mathsf {F}}_{1}(\theta _{1},\theta _{2}),\end{aligned}}$ where ${\mathsf {B}}_{k}$ are 2×2 matrices. Finally we have ${\frac {m(\theta _{1})-m(\theta _{2})}{\theta _{1}-\theta _{2}}}={\mathsf {M}}_{2}(\theta _{1},\theta _{2}).$ This technique can be used in the limit $\theta _{2}=\theta _{1}=\mu$ and $\delta =0$ to simultaneously compute $m(\mu )$ and the derivative $dm(\mu )/d\mu$ , provided that, in evaluating ${\mathsf {F}}_{1}$ and ${\mathsf {A}}$ , we take $\lim _{\delta \to 0}(\sin k\delta )/\delta =k$ .
