---
title: "Toom–Cook multiplication"
source: https://en.wikipedia.org/wiki/Toom–Cook_multiplication
domain: karatsuba-multiplication
license: CC-BY-SA-4.0
tags: karatsuba algorithm, fast multiplication, toom cook multiplication, divide and conquer
fetched: 2026-07-02
---

# Toom–Cook multiplication

**Toom–Cook**, sometimes known as **Toom-3**, named after Andrei Toom, who introduced the new algorithm with its low complexity, and Stephen Cook, who cleaned the description of it, is a multiplication algorithm for large integers.

Given two large integers, *a* and *b*, Toom–Cook splits up *a* and *b* into *k* smaller parts each of length *l*, and performs operations on the parts. As *k* grows, one may combine many of the multiplication sub-operations, thus reducing the overall computational complexity of the algorithm. The multiplication sub-operations can then be computed recursively using Toom–Cook multiplication again, and so on. Although the terms "Toom-3" and "Toom–Cook" are sometimes incorrectly used interchangeably, Toom-3 is only a single instance of the Toom–Cook algorithm, where *k* = 3.

Toom-3 reduces nine multiplications to five, and runs in $\Theta (n^{\log(5)/\log(3)})\approx \Theta (n^{1.46})$ . In general, Toom- k runs in $\Theta (c(k)n^{e})$ , where $e=\log(2k-1)/\log(k)$ , $n^{e}$ is the time spent on sub-multiplications, and c is the time spent on additions and multiplication by small constants (Knuth, p. 296). The Karatsuba algorithm is equivalent to Toom-2, where the number is split into two smaller ones. It reduces four multiplications to three and so operates at $\Theta (n^{\log(3)/\log(2)})\approx \Theta (n^{1.58})$ .

Although the exponent e can be set arbitrarily close to 1 by increasing k , the constant term in the function grows very rapidly. The growth rate for mixed-level Toom–Cook schemes was still an open research problem in 2005. An implementation described by Donald Knuth achieves the time complexity $\Theta (n\,2^{\sqrt {2\log n}}\log n)$ .

Because of its overhead, Toom–Cook is slower than long multiplication with small numbers, and it is therefore typically used for intermediate-size multiplications, before the asymptotically faster Schönhage–Strassen algorithm (with complexity $\Theta (n\log n\log \log n)$ ) becomes practical.

Toom first described this algorithm in 1963, and Cook published an improved (asymptotically equivalent) algorithm in his PhD thesis in 1966.

## Details

This section discusses exactly how to perform Toom-*k* for any given value of *k*, and is a simplification of a description of Toom–Cook polynomial multiplication described by Marco Bodrato. The algorithm has five main steps:

1. Splitting
2. Evaluation
3. Pointwise multiplication
4. Interpolation
5. Recomposition

In a typical large integer implementation, each integer is represented as a sequence of digits in positional notation, with the base or radix set to some (typically large) value *b*; for this example we use *b* = 10000, so that each digit corresponds to a group of four decimal digits (in a computer implementation, *b* would typically be a power of 2 instead). Say the two integers being multiplied are:

| *m* | = | 12 | 3456 | 7890 | 1234 | 5678 | 9012 |
|---|---|---|---|---|---|---|---|
| *n* | = | 9 | 8765 | 4321 | 9876 | 5432 | 1098. |

These are much smaller than would normally be processed with Toom–Cook (grade-school multiplication would be faster) but they will serve to illustrate the algorithm.

### Splitting

In Toom-*k*, we want to split the factors into *k* parts.

The first step is to select the base *B* = *b**i*, such that the number of digits of both *m* and *n* in base *B* is at most *k* (e.g., 3 in Toom-3). A typical choice for *i* is given by:

$i=\max \left\{\left\lfloor {\frac {\left\lfloor \log _{b}m\right\rfloor }{k}}\right\rfloor ,\left\lfloor {\frac {\left\lfloor \log _{b}n\right\rfloor }{k}}\right\rfloor \right\}+1.$

In our example we'll be doing Toom-3, so we choose *B* = *b*2 = 108. We then separate *m* and *n* into their base *B* digits *m**i*, *n**i*:

${\begin{aligned}m_{2}&{}=123456\\m_{1}&{}=78901234\\m_{0}&{}=56789012\\n_{2}&{}=98765\\n_{1}&{}=43219876\\n_{0}&{}=54321098\end{aligned}}$

We then use these digits as coefficients in degree-(*k* − 1) polynomials *p* and *q*, with the property that *p*(*B*) = *m* and *q*(*B*) = *n*:

$p(x)=m_{2}x^{2}+m_{1}x+m_{0}=123456x^{2}+78901234x+56789012\,$

$q(x)=n_{2}x^{2}+n_{1}x+n_{0}=98765x^{2}+43219876x+54321098\,$

The purpose of defining these polynomials is that if we can compute their product *r*(*x*) = *p*(*x*)*q*(*x*), our answer will be *r*(*B*) = *m* × *n*.

In the case where the numbers being multiplied are of different sizes, it's useful to use different values of *k* for *m* and *n*, which we'll call *k**m* and *k**n*. For example, the algorithm "Toom-2.5" refers to Toom–Cook with *k**m* = 3 and *k**n* = 2. In this case the *i* in *B* = *b**i* is typically chosen by:

$i=\max \left\{\left\lfloor {\frac {\left\lceil \log _{b}m\right\rceil }{k_{m}}}\right\rfloor ,\left\lfloor {\frac {\left\lceil \log _{b}n\right\rceil }{k_{n}}}\right\rfloor \right\}.$

### Evaluation

The Toom–Cook approach to computing the polynomial product $p(x)q(x)$ is a commonly used one. Note that a polynomial of degree d is uniquely determined by $d+1$ points (for example, a line – polynomial of degree one is specified by two points). The idea is to evaluate $p(\cdot )$ and $q(\cdot )$ at various points. Then multiply their values at these points to get points on the product polynomial. Finally interpolate to find its coefficients.

Since $\deg(pq)=\deg(p)+\deg(q)$ , we will need $\deg(p)+\deg(q)+1=k_{m}+k_{n}-1$ points to determine the final result. Call this d . In the case of Toom-3, $d=5$ . The algorithm will work no matter what points are chosen (with a few small exceptions, see matrix invertibility requirement in Interpolation), but in the interest of simplifying the algorithm it's better to choose small integer values like 0, 1, −1, and −2.

One unusual point value that is frequently used is infinity, written $\infty$ or $1/0$ . To "evaluate" a polynomial p at infinity actually means to take the limit of $p(x)/x^{\deg p}$ as x goes to infinity. Consequently, $p(\infty )$ is always the value of its highest-degree coefficient (in the example above coefficient $m_{2}$ ).

In our Toom-3 example, we will use the points 0 , 1 , $-1$ , $-2$ , and $\infty$ . These choices simplify evaluation, producing the formulas:

${\begin{array}{lrlrlr}p(0)&=&m_{0}+m_{1}(0)+m_{2}(0)^{2}&=&m_{0}\\p(1)&=&m_{0}+m_{1}(1)+m_{2}(1)^{2}&=&m_{0}+m_{1}+m_{2}\\p(-1)&=&m_{0}+m_{1}(-1)+m_{2}(-1)^{2}&=&m_{0}-m_{1}+m_{2}\\p(-2)&=&m_{0}+m_{1}(-2)+m_{2}(-2)^{2}&=&m_{0}-2m_{1}+4m_{2}\\p(\infty )&=&m_{2}&&\end{array}}$

and analogously for q . In our example, the values we get are:

${\begin{array}{lrlrlr}p(0)&=&m_{0}&=&56789012&=&56789012\\p(1)&=&m_{0}+m_{1}+m_{2}&=&56789012+78901234+123456&=&135813702\\p(-1)&=&m_{0}-m_{1}+m_{2}&=&56789012-78901234+123456&=&-21988766\\p(-2)&=&m_{0}-2m_{1}+4m_{2}&=&56789012-2\times 78901234+4\times 123456&=&-100519632\\p(\infty )&=&m_{2}&=&123456&=&123456\\[4pt]q(0)&=&n_{0}&=&54321098&=&54321098\\q(1)&=&n_{0}+n_{1}+n_{2}&=&54321098+43219876+98765&=&97639739\\q(-1)&=&n_{0}-n_{1}+n_{2}&=&54321098-43219876+98765&=&11199987\\q(-2)&=&n_{0}-2n_{1}+4n_{2}&=&54321098-2\times 43219876+4\times 98765&=&-31723594\\q(\infty )&=&n_{2}&=&98765&=&98765\end{array}}$

As shown, these values may be negative.

For the purpose of later explanation, it will be useful to view this evaluation process as a matrix-vector multiplication, where each row of the matrix contains powers of one of the evaluation points, and the vector contains the coefficients of the polynomial:

$\left({\begin{matrix}p(0)\\p(1)\\p(-1)\\p(-2)\\p(\infty )\end{matrix}}\right)=\left({\begin{matrix}0^{0}&0^{1}&0^{2}\\1^{0}&1^{1}&1^{2}\\(-1)^{0}&(-1)^{1}&(-1)^{2}\\(-2)^{0}&(-2)^{1}&(-2)^{2}\\0&0&1\end{matrix}}\right)\left({\begin{matrix}m_{0}\\m_{1}\\m_{2}\end{matrix}}\right)=\left({\begin{matrix}1&0&0\\1&1&1\\1&-1&1\\1&-2&4\\0&0&1\end{matrix}}\right)\left({\begin{matrix}m_{0}\\m_{1}\\m_{2}\end{matrix}}\right).$

The dimensions of the matrix are *d* by *k**m* for *p* and *d* by *k**n* for *q*. The row for infinity is always all zero except for a 1 in the last column.

#### Faster evaluation

Multipoint evaluation can be obtained faster than with the above formulas. The number of elementary operations (addition/subtraction) can be reduced. The sequence given by Bodrato for Toom-3, executed here over the first operand (polynomial *p*) of the running example is the following:

${\begin{array}{l c l c l c r}p_{0}&\leftarrow &m_{0}+m_{2}&=&56789012+123456&=&56912468\\p(0)&=&m_{0}&=&56789012&=&56789012\\p(1)&=&p_{0}+m_{1}&=&56912468+78901234&=&135813702\\p(-1)&=&p_{0}-m_{1}&=&56912468-78901234&=&-21988766\\p(-2)&=&(p(-1)+m_{2})\times 2-m_{0}&=&(-21988766+123456)\times 2-56789012&=&-100519632\\p(\infty )&=&m_{2}&=&123456&=&123456.\end{array}}$

This sequence requires five addition/subtraction operations, one less than the straightforward evaluation. Moreover the multiplication by 4 in the calculation of $p(-2)$ was saved.

### Pointwise multiplication

Unlike multiplying the polynomials $p(\cdot )$ and $q(\cdot )$ , multiplying the evaluated values $p(a)$ and $q(a)$ just involves multiplying integers — a smaller instance of the original problem. We recursively invoke our multiplication procedure to multiply each pair of evaluated points. In practical implementations, as the operands become smaller, the algorithm will switch to schoolbook long multiplication. Letting *r* be the product polynomial, in our example we have:

${\begin{array}{l c l c l c r}r(0)&=&p(0)\,q(0)&=&56789012\times 54321098&=&3084841486175176\\r(1)&=&p(1)\,q(1)&=&135813702\times 97639739&=&13260814415903778\\r(-1)&=&p(-1)\,q(-1)&=&-21988766\times 11199987&=&-246273893346042\\r(-2)&=&p(-2)\,q(-2)&=&-100519632\times -31723594&=&3188843994597408\\r(\infty )&=&p(\infty )\,q(\infty )&=&123456\times 98765&=&12193131840.\end{array}}$

As shown, these can also be negative. For large enough numbers, this is the most expensive step, the only step that is not linear in the sizes of m and n .

### Interpolation

This is the most complex step, the reverse of the evaluation step: given our d points on the product polynomial $r(\cdot )$ , we need to determine its coefficients. In other words, we want to solve this matrix equation for the vector on the right-hand side:

${\begin{aligned}\left({\begin{matrix}r(0)\\r(1)\\r(-1)\\r(-2)\\r(\infty )\end{matrix}}\right)&{}=\left({\begin{matrix}0^{0}&0^{1}&0^{2}&0^{3}&0^{4}\\1^{0}&1^{1}&1^{2}&1^{3}&1^{4}\\(-1)^{0}&(-1)^{1}&(-1)^{2}&(-1)^{3}&(-1)^{4}\\(-2)^{0}&(-2)^{1}&(-2)^{2}&(-2)^{3}&(-2)^{4}\\0&0&0&0&1\end{matrix}}\right)\left({\begin{matrix}r_{0}\\r_{1}\\r_{2}\\r_{3}\\r_{4}\end{matrix}}\right)\\&{}=\left({\begin{matrix}1&0&0&0&0\\1&1&1&1&1\\1&-1&1&-1&1\\1&-2&4&-8&16\\0&0&0&0&1\end{matrix}}\right)\left({\begin{matrix}r_{0}\\r_{1}\\r_{2}\\r_{3}\\r_{4}\end{matrix}}\right).\end{aligned}}$

This matrix is constructed the same way as the one in the evaluation step, except that it's $d\times d$ . We could solve this equation with a technique like Gaussian elimination, but this is too expensive. Instead, we use the fact that, provided the evaluation points were chosen suitably, this matrix is invertible (see also Vandermonde matrix), and so:

${\begin{aligned}\left({\begin{matrix}r_{0}\\r_{1}\\r_{2}\\r_{3}\\r_{4}\end{matrix}}\right)&{}=\left({\begin{matrix}1&0&0&0&0\\1&1&1&1&1\\1&-1&1&-1&1\\1&-2&4&-8&16\\0&0&0&0&1\end{matrix}}\right)^{-1}\left({\begin{matrix}r(0)\\r(1)\\r(-1)\\r(-2)\\r(\infty )\end{matrix}}\right)\\&{}=\left({\begin{matrix}1&0&0&0&0\\{\tfrac {1}{2}}&{\tfrac {1}{3}}&-1&{\tfrac {1}{6}}&-2\\-1&{\tfrac {1}{2}}&{\tfrac {1}{2}}&0&-1\\-{\tfrac {1}{2}}&{\tfrac {1}{6}}&{\tfrac {1}{2}}&-{\tfrac {1}{6}}&2\\0&0&0&0&1\end{matrix}}\right)\left({\begin{matrix}r(0)\\r(1)\\r(-1)\\r(-2)\\r(\infty )\end{matrix}}\right).\end{aligned}}$

All that remains is to compute this matrix-vector product. Although the matrix contains fractions, the resulting coefficients will be integers — so this can all be done with integer arithmetic, just additions, subtractions, and multiplication/division by small constants. A difficult design challenge in Toom–Cook is to find an efficient sequence of operations to compute this product; one sequence given by Bodrato for Toom-3 is the following, executed here over the running example:

${\begin{array}{l c l c r}r_{0}&\leftarrow &r(0)&=&3084841486175176\\r_{4}&\leftarrow &r(\infty )&=&12193131840\\r_{3}&\leftarrow &(r(-2)-r(1))/3&=&(3188843994597408-13260814415903778)/3\\&&&=&-3357323473768790\\r_{1}&\leftarrow &(r(1)-r(-1))/2&=&(13260814415903778-(-246273893346042))/2\\&&&=&6753544154624910\\r_{2}&\leftarrow &r(-1)-r(0)&=&-246273893346042-3084841486175176\\&&&=&-3331115379521218\\r_{3}&\leftarrow &(r_{2}-r_{3})/2+2r(\infty )&=&(-3331115379521218-(-3357323473768790))/2+2\times 12193131840\\&&&=&13128433387466\\r_{2}&\leftarrow &r_{2}+r_{1}-r_{4}&=&-3331115379521218+6753544154624910-12193131840\\&&&=&3422416581971852\\r_{1}&\leftarrow &r_{1}-r_{3}&=&6753544154624910-13128433387466\\&&&=&6740415721237444\end{array}}$

We now know our product polynomial r :

${\begin{array}{rrrl}r(x)=&&3084841486175176&\\&+&6740415721237444&\!\!\!\!x\\&+&3422416581971852&\!\!\!\!x^{2}\\&+&13128433387466&\!\!\!\!x^{3}\\&+&12193131840&\!\!\!\!x^{4}\end{array}}$

If we were using different $k_{m},k_{n}$ , or evaluation points, the matrix and so our interpolation strategy would change; but it does not depend on the inputs and so can be hard-coded for any given set of parameters.

### Recomposition

Finally, we evaluate r(B) to obtain our final answer. This is straightforward since B is a power of *b* and so the multiplications by powers of B are all shifts by a whole number of digits in base *b*. In the running example b = 104 and B = b2 = 108.

3084

8414

8617

5176

6740

4157

2123

7444

3422

4165

8197

1852

13

1284

3338

7466

+

121

9313

1840

121

9326

3124

6761

1632

4937

6009

5208

5858

8617

5176

And this is in fact the product of 1234567890123456789012 and 987654321987654321098.

## Asymmetric splitting

The interpolation step depends on the degree of the product polynomial, which is the sum of the degrees of the factor polynomials, but not on the individual degrees. While basic Toom-3 divides each factor into 3 parts (quadratic polynomials), if the factors differ in size, it can be beneficial to split one into 2 parts (a linear polynomial) and the other into 4 parts (a cubic) with coefficients of more balanced size. Then the same interpolation step can produce a quartic product polynomial

For Toom-3, this is the only interesting alternative split (the degenerate case of splitting either factor into only 1 part offers no time saving), but higher-degree Toom-Cook allows additional possibilities.

In addition to the equal-split cases, it's possible to have half-integer cases which are always asymmetric; the total number of pieces is odd, and the degree of the product polynomial is even. For example, Toom-2.5 splits one factor into 2 parts and the other into 3, while Toom-3.5 can split the factors as 2+5 or 3+4.

## Interpolation matrices for various *k*

Here we give common interpolation matrices for a few different common small values of *k**m* and *k**n*.

### Toom-1

Applying formally the definition, we may consider Toom-1 (*k**m* = *k**n* = 1). This does not yield a multiplication algorithm, but a recursive algorithm that never halts, as it trivially reduces each input instance to a recursive call with the same instance. The algorithm requires 1 evaluation point, whose value is irrelevant, as it is used only to "evaluate" constant polynomials. Thus, the interpolation matrix is the identity matrix:

$\left({\begin{matrix}1\end{matrix}}\right)^{-1}=\left({\begin{matrix}1\end{matrix}}\right).$

### Toom-1.5

Toom-1.5 (*k**m* = 2, *k**n* = 1) is still degenerate: it recursively reduces one input by halving its size, but leaves the other input unchanged, hence we can make it into a multiplication algorithm only if we supply a 1 × *n* multiplication algorithm as a base case (whereas the true Toom–Cook algorithm reduces to constant-size base cases). It requires 2 evaluation points, here chosen to be 0 and ∞. Its interpolation matrix is then the identity matrix:

$\left({\begin{matrix}1&0\\0&1\end{matrix}}\right)^{-1}=\left({\begin{matrix}1&0\\0&1\end{matrix}}\right).$

The algorithm is essentially equivalent to a form of long multiplication: both coefficients of one factor are multiplied by the sole coefficient of the other factor.

### Toom-2

Toom-2 (*k**m* = 2, *k**n* = 2) requires 3 evaluation points, here chosen to be 0, 1, and ∞. It is the same as Karatsuba multiplication, with an interpolation matrix of:

$\left({\begin{matrix}1&0&0\\1&1&1\\0&0&1\end{matrix}}\right)^{-1}=\left({\begin{matrix}1&0&0\\-1&1&-1\\0&0&1\end{matrix}}\right).$

### Toom-2.5

Toom-2.5 (*k**m* = 3, *k**n* = 2) requires 4 evaluation points, here chosen to be 0, 1, −1, and ∞. It then has an interpolation matrix of:

$\left({\begin{matrix}1&0&0&0\\1&1&1&1\\1&-1&1&-1\\0&0&0&1\end{matrix}}\right)^{-1}=\left({\begin{matrix}1&0&0&0\\0&{\tfrac {1}{2}}&-{\tfrac {1}{2}}&-1\\-1&{\tfrac {1}{2}}&{\tfrac {1}{2}}&0\\0&0&0&1\end{matrix}}\right).$
