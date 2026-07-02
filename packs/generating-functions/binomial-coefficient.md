---
title: "Binomial coefficient"
source: https://en.wikipedia.org/wiki/Binomial_coefficient
domain: generating-functions
license: CC-BY-SA-4.0
tags: generating function, formal power series, catalan number, binomial coefficient
fetched: 2026-07-02
---

# Binomial coefficient

In mathematics, the **binomial coefficients** are the positive integers that occur as coefficients in the binomial theorem. Commonly, a binomial coefficient is indexed by a pair of integers *n* ≥ *k* ≥ 0 and is written ${\tbinom {n}{k}}$ or ⁠ $C(n,k)$ ⁠. It is the coefficient of the *x**k* term in the polynomial expansion of the binomial power (1 + *x*)*n*; this coefficient can be computed by the multiplicative formula

${\binom {n}{k}}={\frac {n\times (n-1)\times \cdots \times (n-k+1)}{k\times (k-1)\times \cdots \times 1}},$

which using factorial notation can be compactly expressed as

${\binom {n}{k}}={\frac {n!}{k!(n-k)!}}.$

For example, the fourth power of 1 + *x* is ${\begin{aligned}(1+x)^{4}&={\tbinom {4}{0}}x^{0}+{\tbinom {4}{1}}x^{1}+{\tbinom {4}{2}}x^{2}+{\tbinom {4}{3}}x^{3}+{\tbinom {4}{4}}x^{4}\\&=1+4x+6x^{2}+4x^{3}+x^{4},\end{aligned}}$ and the binomial coefficient ${\tbinom {4}{2}}={\tfrac {4\times 3}{2\times 1}}={\tfrac {4!}{2!2!}}=6$ is the coefficient of the *x*2 term.

Arranging the numbers ${\tbinom {n}{0}},{\tbinom {n}{1}},\ldots ,{\tbinom {n}{n}}$ in successive rows for *n* = 0, 1, 2, ... gives a triangular array called Pascal's triangle, satisfying the recurrence relation ${\binom {n}{k}}={\binom {n-1}{k-1}}+{\binom {n-1}{k}}.$

The binomial coefficients occur in many areas of mathematics, and especially in combinatorics. In combinatorics the symbol ${\tbinom {n}{k}}$ is usually read as "n choose k" because there are ${\tbinom {n}{k}}$ ways to choose an (unordered) subset of k elements from a fixed set of n elements. For example, there are ${\tbinom {4}{2}}=6$ ways to choose 2 elements from {1, 2, 3, 4}, namely {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4} and {3, 4}.

The binomial coefficients can be extended to accept more general families of inputs. When n is a nonnegative integer and k is an integer such that *k* < 0 or *k* > *n*, it is common to define ⁠ ${\tbinom {n}{k}}=0$ ⁠. If k is a nonnegative integer and z is any complex number, the first multiplicative formula above can be used to define ⁠ ${\tbinom {z}{k}}$ ⁠. Many of the properties of binomial coefficients continue to hold in these more general contexts.

## History and notation

Andreas von Ettingshausen introduced the notation ${\tbinom {n}{k}}$ in 1826, although the numbers were known centuries earlier (see Pascal's triangle). Around 1150, the Indian mathematician Bhaskaracharya gave an exposition of binomial coefficients in his book *Līlāvatī*.

Alternative notations include *C*(*n*, *k*), *n**C**k*, *n**C**k*, *C**k* *n*, *C**n* *k*, and *C**n*,*k*, in all of which the C stands for *combinations* or *choices*; the C notation means the number of ways to choose *k* out of *n* objects. Many calculators use variants of the C notation because they can represent it on a single-line display. In this form the binomial coefficients are easily compared to the numbers of k-permutations of n, written as *P*(*n*, *k*), etc.

## Definition and interpretations

| *k**n* | 0 | 1 | 2 | 3 | 4 | ⋯ |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | ⋯ |
| 1 | 1 | 1 | 0 | 0 | 0 | ⋯ |
| 2 | 1 | 2 | 1 | 0 | 0 | ⋯ |
| 3 | 1 | 3 | 3 | 1 | 0 | ⋯ |
| 4 | 1 | 4 | 6 | 4 | 1 | ⋯ |
| ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋱ |
| The first few binomial coefficients on a left-aligned Pascal's triangle |   |   |   |   |   |   |

For natural numbers (taken to include 0) n and k, the binomial coefficient ${\tbinom {n}{k}}$ can be defined as the coefficient of the monomial *X**k* in the expansion of (1 + *X*)*n*. The same coefficient also occurs (if *k* ≤ *n*) in the binomial formula

| $(x+y)^{n}=\sum _{k=0}^{n}{\binom {n}{k}}x^{k}y^{n-k}$ |   | ∗ |
|---|---|---|

(valid for any elements x, y of a commutative ring), which explains the name "binomial coefficient".

Another occurrence of this number is in combinatorics, where it gives the number of ways, disregarding order, that k objects can be chosen from among n objects; more formally, the number of k-element subsets (or k-combinations) of an n-element set. This number can be seen as equal to that of the first definition, independently of any of the formulas below to compute it: if in each of the n factors of the power (1 + *X*)*n* one temporarily labels the term X with an index i (running from 1 to n), then each subset of k indices gives after expansion a contribution *X**k*, and the coefficient of that monomial in the result will be the number of such subsets. This shows in particular that ${\tbinom {n}{k}}$ is a natural number for any natural numbers n and k. There are many other combinatorial interpretations of binomial coefficients (counting problems for which the answer is given by a binomial coefficient expression), for instance the number of words formed of n bits (digits 0 or 1) whose sum is k is given by ⁠ ${\tbinom {n}{k}}$ ⁠, while the number of ways to write $k=a_{1}+a_{2}+\cdots +a_{n}$ where every *a**i* is a nonnegative integer is given by ⁠ ${\tbinom {n+k-1}{n-1}}$ ⁠. Most of these interpretations can be shown to be equivalent to counting k-combinations.

## Computing the value of binomial coefficients

Several methods exist to compute the value of ${\tbinom {n}{k}}$ without actually expanding a binomial power or counting k-combinations.

### Recursive formula

One method uses the recursive, purely additive formula ${\binom {n}{k}}={\binom {n-1}{k-1}}+{\binom {n-1}{k}}$ for all integers $n,k$ such that ⁠ $1\leq k<n$ ⁠, with boundary values ${\binom {n}{0}}={\binom {n}{n}}=1$ for all integers *n* ≥ 0.

The formula follows from considering the set {1, 2, 3, ..., *n*} and counting separately (a) the k-element groupings that include a particular set element, say "i", in every group (since "i" is already chosen to fill one spot in every group, we need only choose *k* − 1 from the remaining *n* − 1) and (b) all the *k*-groupings that don't include "i"; this enumerates all the possible k-combinations of n elements. It also follows from tracing the contributions to *X**k* in (1 + *X*)*n*−1(1 + *X*). As there is zero *X**n*+1 or *X*−1 in (1 + *X*)*n*, one might extend the definition beyond the above boundaries to include ${\tbinom {n}{k}}=0$ when either *k* > *n* or *k* < 0. This recursive formula then allows the construction of Pascal's triangle, surrounded by white spaces where the zeros, or the trivial coefficients, would be.

### Multiplicative formula

A more efficient method to compute individual binomial coefficients is given by the formula ${\binom {n}{k}}={\frac {n^{\underline {k}}}{k!}}={\frac {n(n-1)(n-2)\cdots (n-(k-1))}{k(k-1)(k-2)\cdots 1}}=\prod _{i=1}^{k}{\frac {n+1-i}{i}},$ where the numerator of the first fraction, ⁠ $n^{\underline {k}}$ ⁠, is a falling factorial. This formula is easiest to understand for the combinatorial interpretation of binomial coefficients. The numerator gives the number of ways to select a sequence of k distinct objects, retaining the order of selection, from a set of n objects. The denominator counts the number of distinct sequences that define the same k-combination when order is disregarded. This formula can also be stated in a recursive form. Using the "C" notation from above, ⁠ $C_{n,k}=C_{n,k-1}\cdot (n-k+1)/k$ ⁠, where ⁠ $C_{n,0}=1$ ⁠. It is readily derived by evaluating $C_{n,k}/C_{n,k-1}$ and can intuitively be understood as starting at the leftmost coefficient of the ⁠ n ⁠-th row of Pascal's triangle, whose value is always ⁠ 1 ⁠, and recursively computing the next coefficient to its right until the ⁠ k ⁠-th one is reached.

Due to the symmetry of the binomial coefficients with regard to k and *n* − *k*, calculation of the above product, as well as the recursive relation, may be optimised by setting its upper limit to the smaller of k and *n* − *k*.

### Factorial formula

Finally, there is the compact form, often used in proofs and derivations, which makes repeated use of the familiar factorial function: ${\binom {n}{k}}={\frac {n!}{k!\,(n-k)!}}\quad {\text{for }}\ 0\leq k\leq n,$ where *n*! denotes the factorial of n. This formula follows from the multiplicative formula above by multiplying numerator and denominator by (*n* − *k*)!; as a consequence it involves many factors common to numerator and denominator. It is less practical for explicit computation (in the case that k is small and n is large) unless common factors are first cancelled (in particular since factorial values grow very rapidly). The formula does exhibit a symmetry that is less evident from the multiplicative formula (though it is from the definitions)

| ${\binom {n}{k}}={\binom {n}{n-k}}\quad {\text{for }}\ 0\leq k\leq n,$ |   | 1 |
|---|---|---|

which leads to a more efficient multiplicative computational routine. Using the falling factorial notation, ${\binom {n}{k}}={\begin{cases}n^{\underline {k}}/k!&{\text{if }}\ k\leq {\frac {n}{2}}\\n^{\underline {n-k}}/(n-k)!&{\text{if }}\ k>{\frac {n}{2}}\end{cases}}.$

### Generalization and connection to the binomial series

The multiplicative formula allows the definition of binomial coefficients to be extended by replacing *n* by an arbitrary number *α* (negative, real, complex) or even an element of any commutative ring in which all positive integers are invertible: ${\binom {\alpha }{k}}={\frac {\alpha ^{\underline {k}}}{k!}}={\frac {\alpha (\alpha -1)(\alpha -2)\cdots (\alpha -k+1)}{k(k-1)(k-2)\cdots 1}}\quad {\text{for }}k\in \mathbb {N} {\text{ and arbitrary }}\alpha .$

With this definition one has a generalization of the binomial formula (with one of the variables set to 1), which justifies still calling the ${\tbinom {\alpha }{k}}$ binomial coefficients:

| $(1+X)^{\alpha }=\sum _{k=0}^{\infty }{\binom {\alpha }{k}}X^{k}.$ |   | 2 |
|---|---|---|

This formula is valid for all complex numbers *α* and *X* with |*X*| < 1. It can also be interpreted as an identity of formal power series in *X*, where it actually can serve as definition of arbitrary powers of power series with constant coefficient equal to 1; the point is that with this definition all identities hold that one expects for exponentiation, notably $(1+X)^{\alpha }(1+X)^{\beta }=(1+X)^{\alpha +\beta }\quad {\text{and}}\quad ((1+X)^{\alpha })^{\beta }=(1+X)^{\alpha \beta }.$

If *α* is a nonnegative integer *n*, then all terms with *k* > *n* are zero, and the infinite series becomes a finite sum, thereby recovering the binomial formula. However, for other values of *α*, including negative integers and rational numbers, the series is really infinite.

## Pascal's triangle

Pascal's rule is the important recurrence relation

| ${\binom {n}{k}}+{\binom {n}{k+1}}={\binom {n+1}{k+1}},$ |   | 3 |
|---|---|---|

which can be used to prove by mathematical induction that ${\tbinom {n}{k}}$ is a natural number for all integer *n* ≥ 0 and all integer *k*, a fact that is not immediately obvious from formula (1). To the left and right of Pascal's triangle, the entries (shown as blanks) are all zero.

Pascal's rule also gives rise to Pascal's triangle:

0:

1

1:

1

1

2:

1

2

1

3:

1

3

3

1

4:

1

4

6

4

1

5:

1

5

10

10

5

1

6:

1

6

15

20

15

6

1

7:

1

7

21

35

35

21

7

1

8:

1

8

28

56

70

56

28

8

1

Row number n contains the numbers ${\tbinom {n}{k}}$ for *k* = 0, …, *n*. It is constructed by first placing 1s in the outermost positions, and then filling each inner position with the sum of the two numbers directly above. This method allows the quick calculation of binomial coefficients without the need for fractions or multiplications. For instance, by looking at row number 5 of the triangle, one can quickly read off that $(x+y)^{5}={\underline {1}}x^{5}+{\underline {5}}x^{4}y+{\underline {10}}x^{3}y^{2}+{\underline {10}}x^{2}y^{3}+{\underline {5}}xy^{4}+{\underline {1}}y^{5}.$

## Combinatorics and statistics

Binomial coefficients are of importance in combinatorics because they provide ready formulas for certain frequent counting problems:

- There are ${\tbinom {n}{k}}$ ways to choose *k* elements from a set of *n* elements. See Combination.
- There are ${\tbinom {n+k-1}{k}}$ ways to choose *k* elements from a set of *n* elements if repetitions are allowed. See Multiset.
- There are ${\tbinom {n+k}{k}}$ strings containing *k* ones and *n* zeros.
- There are ${\tbinom {n+1}{k}}$ strings consisting of *k* ones and *n* zeros such that no two ones are adjacent.
- The Catalan numbers are ⁠ ${\tfrac {1}{n+1}}{\tbinom {2n}{n}}$ ⁠.
- The binomial distribution in statistics is ⁠ ${\tbinom {n}{k}}p^{k}(1-p)^{n-k}$ ⁠.

## Binomial coefficients as polynomials

For any nonnegative integer *k*, the expression ${\textstyle {\binom {t}{k}}}$ can be written as a polynomial with denominator *k*!: ${\binom {t}{k}}={\frac {t^{\underline {k}}}{k!}}={\frac {t(t-1)(t-2)\cdots (t-k+1)}{k(k-1)(k-2)\cdots 2\cdot 1}};$ this presents a polynomial in *t* with rational coefficients.

As such, it can be evaluated at any real or complex number *t* to define binomial coefficients with such first arguments. These "generalized binomial coefficients" appear in Newton's generalized binomial theorem.

For each *k*, the polynomial ${\tbinom {t}{k}}$ can be characterized as the unique degree *k* polynomial *p*(*t*) satisfying *p*(0) = *p*(1) = ⋯ = *p*(*k* − 1) = 0 and *p*(*k*) = 1.

Its coefficients are expressible in terms of Stirling numbers of the first kind: ${\binom {t}{k}}=\sum _{i=0}^{k}s(k,i){\frac {t^{i}}{k!}}.$ The derivative of ${\tbinom {t}{k}}$ can be calculated by logarithmic differentiation: ${\frac {\mathrm {d} }{\mathrm {d} t}}{\binom {t}{k}}={\binom {t}{k}}\sum _{i=0}^{k-1}{\frac {1}{t-i}}.$ This can cause a problem when evaluated at integers from 0 to ⁠ $t-1$ ⁠, but using identities below we can compute the derivative as: ${\frac {\mathrm {d} }{\mathrm {d} t}}{\binom {t}{k}}=\sum _{i=0}^{k-1}{\frac {(-1)^{k-i-1}}{k-i}}{\binom {t}{i}}.$

### Binomial coefficients as a basis for the space of polynomials

Over any field of characteristic 0 (that is, any field that contains the rational numbers), each polynomial *p*(*t*) of degree at most *d* is uniquely expressible as a linear combination ${\textstyle \sum _{k=0}^{d}a_{k}{\binom {t}{k}}}$ of binomial coefficients, because the binomial coefficients consist of one polynomial of each degree. The coefficient *a**k* is the *k*th difference of the sequence *p*(0), *p*(1), ..., *p*(*k*). Explicitly,

| $a_{k}=\sum _{i=0}^{k}(-1)^{k-i}{\binom {k}{i}}p(i).$ |   | 4 |
|---|---|---|

### Integer-valued polynomials

Each polynomial ${\tbinom {t}{k}}$ is integer-valued: it has an integer value at all integer inputs ⁠ t ⁠. (One way to prove this is by induction on *k* using Pascal's identity.) Therefore, any integer linear combination of binomial coefficient polynomials is integer-valued too. Conversely, (**4**) shows that any integer-valued polynomial is an integer linear combination of these binomial coefficient polynomials. More generally, for any subring *R* of a characteristic 0 field *K*, a polynomial in *K*[*t*] takes values in *R* at all integers if and only if it is an *R*-linear combination of binomial coefficient polynomials.

### Example

The integer-valued polynomial 3*t*(3*t* + 1) / 2 can be rewritten as $9{\binom {t}{2}}+6{\binom {t}{1}}+0{\binom {t}{0}}.$

## Identities involving binomial coefficients

The factorial formula facilitates relating nearby binomial coefficients. For instance, if *k* is a positive integer and *n* is arbitrary, then

| ${\binom {n}{k}}={\frac {n}{k}}{\binom {n-1}{k-1}}$ |   | 5 |
|---|---|---|

and, with a little more work, ${\binom {n-1}{k}}-{\binom {n-1}{k-1}}={\frac {n-2k}{n}}{\binom {n}{k}}.$

We can also get ${\binom {n-1}{k}}={\frac {n-k}{n}}{\binom {n}{k}}.$

Moreover, the following may be useful: ${\binom {n}{k}}{\binom {k}{j}}={\binom {n}{j}}{\binom {n-j}{k-j}}={\binom {n}{k-j}}{\binom {n-k+j}{j}}.$

For constant *n*, we have the following recurrence: ${\binom {n}{k}}={\frac {n-k+1}{k}}{\binom {n}{k-1}}.$

To sum up, we have ${\binom {n}{k}}={\binom {n}{n-k}}={\frac {n-k+1}{k}}{\binom {n}{k-1}}={\frac {n}{n-k}}{\binom {n-1}{k}}$ $={\frac {n}{k}}{\binom {n-1}{k-1}}={\frac {n}{n-2k}}{\Bigg (}{\binom {n-1}{k}}-{\binom {n-1}{k-1}}{\Bigg )}={\binom {n-1}{k}}+{\binom {n-1}{k-1}}.$

### Sums of the binomial coefficients

The formula

| $\sum _{k=0}^{n}{\binom {n}{k}}=2^{n}$ |   | ∗∗ |
|---|---|---|

says that the elements in the nth row of Pascal's triangle always add up to 2 raised to the nth power. This is obtained from the binomial theorem (**∗**) by setting *x* = 1 and *y* = 1. The formula also has a natural combinatorial interpretation: the left side sums the number of subsets of {1, ..., *n*} of sizes *k* = 0, 1, ..., *n*, giving the total number of subsets. (That is, the left side counts the power set of {1, ..., *n*}.) However, these subsets can also be generated by successively choosing or excluding each element 1, ..., *n*; the *n* independent binary choices (bit-strings) allow a total of $2^{n}$ choices. The left and right sides are two ways to count the same collection of subsets, so they are equal.

The formulas

| $\sum _{k=0}^{n}k{\binom {n}{k}}=n2^{n-1}$ |   | 6 |
|---|---|---|

and $\sum _{k=0}^{n}k^{2}{\binom {n}{k}}=(n+n^{2})2^{n-2}$ follow from the binomial theorem after differentiating with respect to x (twice for the latter) and then substituting *x* = *y* = 1.

The Chu–Vandermonde identity, which holds for any complex values *m* and *n* and any non-negative integer *k*, is

| $\sum _{j=0}^{k}{\binom {m}{j}}{\binom {n-m}{k-j}}={\binom {n}{k}}$ |   | 7 |
|---|---|---|

and can be found by examination of the coefficient of $x^{k}$ in the expansion of (1 + *x*)*m*(1 + *x*)*n*−*m* = (1 + *x*)*n* using equation (**2**). When *m* = 1, equation (**7**) reduces to equation (**3**). In the special case *n* = 2*m*, *k* = *m*, using (**1**), the expansion (**7**) becomes (as seen in Pascal's triangle at right)

${\begin{array}{c}1\\1\qquad 1\\1\qquad 2\qquad 1\\{\color {blue}1\qquad 3\qquad 3\qquad 1}\\1\qquad 4\qquad 6\qquad 4\qquad 1\\1\qquad 5\qquad 10\qquad 10\qquad 5\qquad 1\\1\qquad 6\qquad 15\qquad {\color {red}20}\qquad 15\qquad 6\qquad 1\\1\qquad 7\qquad 21\qquad 35\qquad 35\qquad 21\qquad 7\qquad 1\end{array}}$

Pascal's triangle, rows 0 through 7. Equation

8

for

m

= 3

is illustrated in rows 3 and 6 as

⁠

$1^{2}+3^{2}+3^{2}+1^{2}=20$

⁠

.

| $\sum _{j=0}^{m}{\binom {m}{j}}^{2}={\binom {2m}{m}},$ |   | 8 |
|---|---|---|

where the term on the right side is a central binomial coefficient.

Another form of the Chu–Vandermonde identity, which applies for any integers *j*, *k*, and *n* satisfying 0 ≤ *j* ≤ *k* ≤ *n*, is

| $\sum _{m=0}^{n}{\binom {m}{j}}{\binom {n-m}{k-j}}={\binom {n+1}{k+1}}.$ |   | 9 |
|---|---|---|

The proof is similar, but uses the binomial series expansion (**2**) with negative integer exponents. When *j* = *k*, equation (**9**) gives the hockey-stick identity $\sum _{m=k}^{n}{\binom {m}{k}}={\binom {n+1}{k+1}}$ and its relative $\sum _{r=0}^{m}{\binom {n+r}{r}}={\binom {n+m+1}{m}}.$

Let *F*(*n*) denote the *n*-th Fibonacci number. Then $\sum _{k=0}^{\lfloor n/2\rfloor }{\binom {n-k}{k}}=F(n+1).$ This can be proved by induction using (**3**) or by Zeckendorf's representation. A combinatorial proof is given below.

#### Multisections of sums

For integers *s* and *t* such that ⁠ $0\leq t<s$ ⁠, series multisection gives the following identity for the sum of binomial coefficients: ${\binom {n}{t}}+{\binom {n}{t+s}}+{\binom {n}{t+2s}}+\ldots ={\frac {1}{s}}\sum _{j=0}^{s-1}\left(2\cos {\frac {\pi j}{s}}\right)^{n}\cos {\frac {\pi (n-2t)j}{s}}.$

For small s, these series have particularly nice forms; for example, ${\binom {n}{0}}+{\binom {n}{3}}+{\binom {n}{6}}+\cdots ={\frac {1}{3}}\left(2^{n}+2\cos {\frac {n\pi }{3}}\right)$ ${\binom {n}{1}}+{\binom {n}{4}}+{\binom {n}{7}}+\cdots ={\frac {1}{3}}\left(2^{n}+2\cos {\frac {(n-2)\pi }{3}}\right)$ ${\binom {n}{2}}+{\binom {n}{5}}+{\binom {n}{8}}+\cdots ={\frac {1}{3}}\left(2^{n}+2\cos {\frac {(n-4)\pi }{3}}\right)$ ${\binom {n}{0}}+{\binom {n}{4}}+{\binom {n}{8}}+\cdots ={\frac {1}{2}}\left(2^{n-1}+2^{\frac {n}{2}}\cos {\frac {n\pi }{4}}\right)$ ${\binom {n}{1}}+{\binom {n}{5}}+{\binom {n}{9}}+\cdots ={\frac {1}{2}}\left(2^{n-1}+2^{\frac {n}{2}}\sin {\frac {n\pi }{4}}\right)$ ${\binom {n}{2}}+{\binom {n}{6}}+{\binom {n}{10}}+\cdots ={\frac {1}{2}}\left(2^{n-1}-2^{\frac {n}{2}}\cos {\frac {n\pi }{4}}\right)$ ${\binom {n}{3}}+{\binom {n}{7}}+{\binom {n}{11}}+\cdots ={\frac {1}{2}}\left(2^{n-1}-2^{\frac {n}{2}}\sin {\frac {n\pi }{4}}\right)$

#### Partial sums

Although there is no closed formula for partial sums $\sum _{j=0}^{k}{\binom {n}{j}}$ of binomial coefficients, one can again use (**3**) and induction to show that for *k* = 0, …, *n* − 1, $\sum _{j=0}^{k}(-1)^{j}{\binom {n}{j}}=(-1)^{k}{\binom {n-1}{k}},$ with special case

$\sum _{j=0}^{n}(-1)^{j}{\binom {n}{j}}=0$ for *n* > 0. This latter result is also a special case of the result from the theory of finite differences that for any polynomial *P*(*x*) of degree less than *n*, $\sum _{j=0}^{n}(-1)^{j}{\binom {n}{j}}P(j)=0.$ Differentiating (**2**) *k* times and setting *x* = −1 yields this for ⁠ $P(x)=x(x-1)\cdots (x-k+1)$ ⁠, when 0 ≤ *k* < *n*, and the general case follows by taking linear combinations of these.

When *P*(*x*) is of degree less than or equal to *n*,

| $\sum _{j=0}^{n}(-1)^{j}{\binom {n}{j}}P(n-j)=n!a_{n}$ |   | 10 |
|---|---|---|

where $a_{n}$ is the coefficient of degree *n* in *P*(*x*).

More generally for (**10**), $\sum _{j=0}^{n}(-1)^{j}{\binom {n}{j}}P(m+(n-j)d)=d^{n}n!a_{n}$ where *m* and *d* are complex numbers. This follows immediately applying (**10**) to the polynomial ⁠ $Q(x):=P(m+dx)$ ⁠ instead of ⁠ $P(x)$ ⁠, and observing that ⁠ $Q(x)$ ⁠ still has degree less than or equal to *n*, and that its coefficient of degree *n* is *dnan*.

The series ${\textstyle {\frac {k-1}{k}}\sum _{j=0}^{\infty }{\frac {1}{\binom {j+x}{k}}}={\frac {1}{\binom {x-1}{k-1}}}}$ is convergent for *k* ≥ 2. This formula is used in the analysis of the German tank problem. It follows from ${\textstyle {\frac {k-1}{k}}\sum _{j=0}^{M}{\frac {1}{\binom {j+x}{k}}}={\frac {1}{\binom {x-1}{k-1}}}-{\frac {1}{\binom {M+x}{k-1}}}}$ which is proved by induction on *M*.

### Identities with combinatorial proofs

Many identities involving binomial coefficients can be proved by combinatorial means. For example, for nonnegative integers ⁠ ${n}\geq {q}$ ⁠, the identity $\sum _{k=q}^{n}{\binom {n}{k}}{\binom {k}{q}}=2^{n-q}{\binom {n}{q}}$ (which reduces to (**6**) when *q* = 1) can be given a double counting proof, as follows. The left side counts the number of ways of selecting a subset of [*n*] = {1, 2, ..., *n*} with at least *q* elements, and marking *q* elements among those selected. The right side counts the same thing, because there are ${\tbinom {n}{q}}$ ways of choosing a set of *q* elements to mark, and $2^{n-q}$ to choose which of the remaining elements of [*n*] also belong to the subset.

In Pascal's identity ${\binom {n}{k}}={\binom {n-1}{k-1}}+{\binom {n-1}{k}},$ both sides count the number of *k*-element subsets of [*n*]: the two terms on the right side group them into those that contain element *n* and those that do not.

The identity (**8**) also has a combinatorial proof. The identity reads $\sum _{k=0}^{n}{\binom {n}{k}}^{2}={\binom {2n}{n}}.$

Suppose you have $2n$ empty squares arranged in a row and you want to mark (select) *n* of them. There are ${\tbinom {2n}{n}}$ ways to do this. On the other hand, you may select your *n* squares by selecting *k* squares from among the first *n* and $n-k$ squares from the remaining *n* squares; any *k* from 0 to *n* will work. This gives $\sum _{k=0}^{n}{\binom {n}{k}}{\binom {n}{n-k}}={\binom {2n}{n}}.$ Now apply (**1**) to get the result.

If one denotes by *F*(*i*) the sequence of Fibonacci numbers, indexed so that *F*(0) = *F*(1) = 1, then the identity $\sum _{k=0}^{\left\lfloor {\frac {n}{2}}\right\rfloor }{\binom {n-k}{k}}=F(n)$ has the following combinatorial proof. One may show by induction that *F*(*n*) counts the number of ways that a *n* × 1 strip of squares may be covered by 2 × 1 and 1 × 1 tiles. On the other hand, if such a tiling uses exactly k of the 2 × 1 tiles, then it uses *n* − 2*k* of the 1 × 1 tiles, and so uses *n* − *k* tiles total. There are ${\tbinom {n-k}{k}}$ ways to order these tiles, and so summing this coefficient over all possible values of k gives the identity.

#### Sum of coefficients row

The number of *k*-combinations for all *k*, ⁠ $\sum _{0\leq {k}\leq {n}}{\binom {n}{k}}=2^{n}$ ⁠, is the sum of the *n*th row (counting from 0) of the binomial coefficients. These combinations are enumerated by the 1 digits of the set of base 2 numbers counting from 0 to ⁠ $2^{n}-1$ ⁠, where each digit position is an item from the set of *n*.

### Dixon's identity

Dixon's identity is $\sum _{k=-a}^{a}(-1)^{k}{\binom {2a}{k+a}}^{3}={\frac {(3a)!}{(a!)^{3}}}$ or, more generally, $\sum _{k=-a}^{a}(-1)^{k}{\binom {a+b}{a+k}}{\binom {b+c}{b+k}}{\binom {c+a}{c+k}}={\frac {(a+b+c)!}{a!\,b!\,c!}}\,,$ where *a*, *b*, and *c* are non-negative integers.

### Continuous identities

Certain trigonometric integrals have values expressible in terms of binomial coefficients: For any ⁠ $m,n\in \mathbb {N}$ ⁠, $\int _{-\pi }^{\pi }\cos((2m-n)x)\cos ^{n}(x)\ dx={\frac {\pi }{2^{n-1}}}{\binom {n}{m}}$ $\int _{-\pi }^{\pi }\sin((2m-n)x)\sin ^{n}(x)\ dx={\begin{cases}(-1)^{m+(n+1)/2}{\frac {\pi }{2^{n-1}}}{\binom {n}{m}},&n{\text{ odd}}\\0,&{\text{otherwise}}\end{cases}}$ $\int _{-\pi }^{\pi }\cos((2m-n)x)\sin ^{n}(x)\ dx={\begin{cases}(-1)^{m+(n/2)}{\frac {\pi }{2^{n-1}}}{\binom {n}{m}},&n{\text{ even}}\\0,&{\text{otherwise}}\end{cases}}$

These can be proved by using Euler's formula to convert trigonometric functions to complex exponentials, expanding using the binomial theorem, and integrating term by term.

### Congruences

If *n* is prime, then ${\binom {n-1}{k}}\equiv (-1)^{k}\mod n$ for every *k* with ⁠ $0\leq k\leq n-1$ ⁠. More generally, this remains true if *n* is any number and *k* is such that all the numbers between 1 and *k* are coprime to *n*.

Indeed, we have ${\binom {n-1}{k}}={(n-1)(n-2)\cdots (n-k) \over 1\cdot 2\cdots k}=\prod _{i=1}^{k}{n-i \over i}\equiv \prod _{i=1}^{k}{-i \over i}=(-1)^{k}\mod n.$

## Generating functions

### Ordinary generating functions

For a fixed n, the ordinary generating function of the sequence ${\tbinom {n}{0}},{\tbinom {n}{1}},{\tbinom {n}{2}},\ldots$ is $\sum _{k=0}^{\infty }{\binom {n}{k}}x^{k}=(1+x)^{n}.$

For a fixed k, the ordinary generating function of the sequence ⁠ ${\tbinom {0}{k}},{\tbinom {1}{k}},{\tbinom {2}{k}},\ldots$ ⁠, is $\sum _{n=0}^{\infty }{\binom {n}{k}}y^{n}={\frac {y^{k}}{(1-y)^{k+1}}}.$

The bivariate generating function of the binomial coefficients is $\sum _{n=0}^{\infty }\sum _{k=0}^{n}{\binom {n}{k}}x^{k}y^{n}={\frac {1}{1-y-xy}}.$

A symmetric bivariate generating function of the binomial coefficients is $\sum _{n=0}^{\infty }\sum _{k=0}^{\infty }{\binom {n+k}{k}}x^{k}y^{n}={\frac {1}{1-x-y}}.$ which is the same as the previous generating function after the substitution ⁠ $x\to xy$ ⁠.

### Exponential generating function

A symmetric exponential bivariate generating function of the binomial coefficients is: $\sum _{n=0}^{\infty }\sum _{k=0}^{\infty }{\binom {n+k}{k}}{\frac {x^{k}y^{n}}{(n+k)!}}=e^{x+y}.$

## Divisibility properties

In 1852, Kummer proved that if *m* and *n* are nonnegative integers and *p* is a prime number, then the largest power of *p* dividing ${\tbinom {m+n}{m}}$ equals *p**c*, where *c* is the number of carries when *m* and *n* are added in base *p*. Equivalently, the exponent of a prime *p* in ${\tbinom {n}{k}}$ equals the number of nonnegative integers *j* such that the fractional part of *k*/*p**j* is greater than the fractional part of *n*/*p**j*. (For example, ${\tbinom {n}{k}}$ is not divisible by *p* if every digit in the base-*p* representation of *k* is less than or equal to the corresponding digit in the base-*p* representation of *n*.) It can be deduced from this that ${\tbinom {n}{k}}$ is divisible by *n*/gcd(*n*,*k*). In particular therefore it follows that *p* divides ${\tbinom {p^{r}}{s}}$ for all positive integers *r* and *s* such that *s* < *p**r*. However this is not true of higher powers of *p*: for example 9 does not divide ⁠ ${\tbinom {9}{6}}$ ⁠.

Any integer divides almost all binomial coefficients. More precisely, fix an integer *d* and let *f*(*N*) denote the number of binomial coefficients ${\tbinom {n}{k}}$ with $n<N$ such that *d* divides ⁠ ${\tbinom {n}{k}}$ ⁠. Then $\lim _{N\to \infty }{\frac {f(N)}{N(N+1)/2}}=1.$ Since the number of binomial coefficients ${\tbinom {n}{k}}$ with *n* < *N* is *N*(*N* + 1) / 2, this implies that the density of binomial coefficients divisible by *d* goes to 1.

Binomial coefficients have divisibility properties related to least common multiples of consecutive integers. For example: ${\binom {n+k}{k}}$ divides ⁠ ${\frac {\operatorname {lcm} (n,n+1,\ldots ,n+k)}{n}}$ ⁠. ${\binom {n+k}{k}}$ is a multiple of ⁠ ${\frac {\operatorname {lcm} (n,n+1,\ldots ,n+k)}{n\cdot \operatorname {lcm} ({\binom {k}{0}},{\binom {k}{1}},\ldots ,{\binom {k}{k}})}}$ ⁠.

Another fact: An integer *n* ≥ 2 is prime if and only if all the intermediate binomial coefficients ${\binom {n}{1}},{\binom {n}{2}},\ldots ,{\binom {n}{n-1}}$ are divisible by *n*.

Proof: When *p* is prime, *p* divides ${\binom {p}{k}}={\frac {p\cdot (p-1)\cdots (p-k+1)}{k\cdot (k-1)\cdots 1}}$ for all 0 < *k* < *p* because ${\tbinom {p}{k}}$ is a natural number and *p* divides the numerator but not the denominator. When *n* is composite, let *p* be the smallest prime factor of *n* and let *k* = *n*/*p*. Then 0 < *p* < *n* and ${\binom {n}{p}}={\frac {n(n-1)(n-2)\cdots (n-p+1)}{p!}}={\frac {k(n-1)(n-2)\cdots (n-p+1)}{(p-1)!}}\not \equiv 0{\pmod {n}}$ otherwise the numerator *k*(*n* − 1)(*n* − 2)⋯(*n* − *p* + 1) has to be divisible by *n* = *k*×*p*, this can only be the case when (*n* − 1)(*n* − 2)⋯(*n* − *p* + 1) is divisible by *p*. But *n* is divisible by *p*, so *p* does not divide *n* − 1, *n* − 2, …, *n* − *p* + 1 and because *p* is prime, we know that *p* does not divide (*n* − 1)(*n* − 2)⋯(*n* − *p* + 1) and so the numerator cannot be divisible by *n*.

## Bounds and asymptotic formulas

The following bounds for ${\tbinom {n}{k}}$ hold for all values of *n* and *k* such that 1 ≤ *k* ≤ *n*: ${\frac {n^{k}}{k^{k}}}\leq {\binom {n}{k}}\leq {\frac {n^{k}}{k!}}<\left({\frac {n\cdot e}{k}}\right)^{k}.$ The first inequality follows from the fact that ${\binom {n}{k}}={\frac {n}{k}}\cdot {\frac {n-1}{k-1}}\cdots {\frac {n-(k-1)}{1}}$ and each of these k terms in this product is ⁠ $\geq {\frac {n}{k}}$ ⁠. A similar argument can be made to show the second inequality. The final strict inequality is equivalent to ⁠ $e^{k}>k^{k}/k!$ ⁠, that is clear since the RHS is a term of the exponential series ⁠ $e^{k}=\sum _{j=0}^{\infty }k^{j}/j!$ ⁠.

From the divisibility properties we can infer that ${\frac {\operatorname {lcm} (n-k,\ldots ,n)}{(n-k)\cdot \operatorname {lcm} \left({\binom {k}{0}},\ldots ,{\binom {k}{k}}\right)}}\leq {\binom {n}{k}}\leq {\frac {\operatorname {lcm} (n-k,\ldots ,n)}{n-k}},$ where both equalities can be achieved.

The following bounds are useful in information theory: ${\frac {1}{n+1}}2^{nH(k/n)}\leq {\binom {n}{k}}\leq 2^{nH(k/n)}$ where $H(p)=-p\log _{2}(p)-(1-p)\log _{2}(1-p)$ is the binary entropy function. It can be further tightened to ${\sqrt {\frac {n}{8k(n-k)}}}2^{nH(k/n)}\leq {\binom {n}{k}}\leq {\sqrt {\frac {n}{2\pi k(n-k)}}}2^{nH(k/n)}$ for all ⁠ $1\leq k\leq n-1$ ⁠.

### Both *n* and *k* large

Stirling's approximation yields the following approximation, valid when $n-k,k$ both tend to infinity: ${\binom {n}{k}}\sim {\sqrt {n \over 2\pi k(n-k)}}\cdot {n^{n} \over k^{k}(n-k)^{n-k}}$ Because the inequality forms of Stirling's formula also bound the factorials, slight variants on the above asymptotic approximation give exact bounds. In particular, when n is sufficiently large, one has ${\binom {2n}{n}}\sim {\frac {2^{2n}}{\sqrt {n\pi }}}$ and ⁠ ${\sqrt {n}}{\binom {2n}{n}}\geq 2^{2n-1}$ ⁠. More generally, for *m* ≥ 2 and *n* ≥ 1 (again, by applying Stirling's formula to the factorials in the binomial coefficient), ${\sqrt {n}}{\binom {mn}{n}}\geq {\frac {m^{m(n-1)+1}}{(m-1)^{(m-1)(n-1)}}}.$

If *n* is large and *k* is linear in *n*, various precise asymptotic estimates exist for the binomial coefficient ⁠ ${\binom {n}{k}}$ ⁠. For example, if $|n/2-k|=o(n^{2/3})$ then ${\binom {n}{k}}\sim {\binom {n}{\frac {n}{2}}}e^{-d^{2}/(2n)}\sim {\frac {2^{n}}{\sqrt {{\frac {1}{2}}n\pi }}}e^{-d^{2}/(2n)}$ where *d* = *n* − 2*k*.

### n much larger than k

If n is large and k is *o*(*n*) (that is, if *k*/*n* → 0), then ${\binom {n}{k}}\sim \left({\frac {ne}{k}}\right)^{k}\cdot (2\pi k)^{-1/2}\cdot \exp \left(-{\frac {k^{2}}{2n}}(1+o(1))\right)$ where again o is the little o notation.

### Sums of binomial coefficients

A simple upper bound for the sum of binomial coefficients can be obtained using a rough estimate for the multiplicative formula for ${\binom {m}{i}}$ and then the binomial theorem: $\sum _{i=0}^{k}{\binom {n}{i}}\leq \sum _{i=0}^{k}n^{i}\leq \sum _{i=0}^{k}{\binom {k}{i}}\,n^{i}\cdot 1^{k-i}=(n+1)^{k}.$ More precise bounds are given by ${\frac {1}{\sqrt {8n\varepsilon (1-\varepsilon )}}}\cdot 2^{H(\varepsilon )\cdot n}\leq \sum _{i=0}^{k}{\binom {n}{i}}\leq 2^{H(\varepsilon )\cdot n},$ valid for all integers $n>k\geq 1$ with ⁠ $\varepsilon \doteq k/n\leq 1/2$ ⁠.

### Generalized binomial coefficients

The infinite product formula for the gamma function also gives an expression for binomial coefficients $(-1)^{k}{\binom {z}{k}}={\binom {-z+k-1}{k}}={\frac {1}{\Gamma (-z)}}{\frac {1}{(k+1)^{z+1}}}\prod _{j=k+1}{\frac {\left(1+{\frac {1}{j}}\right)^{-z-1}}{1-{\frac {z+1}{j}}}}$ which yields the asymptotic formulas ${\binom {z}{k}}\approx {\frac {(-1)^{k}}{\Gamma (-z)k^{z+1}}}\qquad {\text{and}}\qquad {\binom {z+k}{k}}={\frac {k^{z}}{\Gamma (z+1)}}\left(1+{\frac {z(z+1)}{2k}}+{\mathcal {O}}\left(k^{-2}\right)\right)$ as ⁠ $k\to \infty$ ⁠.

This asymptotic behaviour is contained in the approximation ${\binom {z+k}{k}}\approx {\frac {e^{z(H_{k}-\gamma )}}{\Gamma (z+1)}}$ as well. (Here $H_{k}$ is the *k*-th harmonic number and $\gamma$ is the Euler–Mascheroni constant.)

Further, the asymptotic formula ${\frac {\binom {z+k}{j}}{\binom {k}{j}}}\to \left(1-{\frac {j}{k}}\right)^{-z}\quad {\text{and}}\quad {\frac {\binom {j}{j-k}}{\binom {j-z}{j-k}}}\to \left({\frac {j}{k}}\right)^{z}$ hold true, whenever $k\to \infty$ and $j/k\to x$ for some complex number ⁠ x ⁠.

## Generalizations

### Generalization to multinomials

Binomial coefficients can be generalized to **multinomial coefficients** defined to be the number: ${\binom {n}{k_{1},k_{2},\ldots ,k_{r}}}={\frac {n!}{k_{1}!k_{2}!\cdots k_{r}!}}$ where $\sum _{i=1}^{r}k_{i}=n.$

While the binomial coefficients represent the coefficients of (*x* + *y*)*n*, the multinomial coefficients represent the coefficients of the polynomial $(x_{1}+x_{2}+\cdots +x_{r})^{n}.$ The case *r* = 2 gives binomial coefficients: ${\binom {n}{k_{1},k_{2}}}={\binom {n}{k_{1},n-k_{1}}}={\binom {n}{k_{1}}}={\binom {n}{k_{2}}}.$

The combinatorial interpretation of multinomial coefficients is distribution of *n* distinguishable elements over *r* (distinguishable) containers, each containing exactly *ki* elements, where *i* is the index of the container.

Multinomial coefficients have many properties similar to those of binomial coefficients, for example the recurrence relation: ${\binom {n}{k_{1},k_{2},\ldots ,k_{r}}}={\binom {n-1}{k_{1}-1,k_{2},\ldots ,k_{r}}}+{\binom {n-1}{k_{1},k_{2}-1,\ldots ,k_{r}}}+\ldots +{\binom {n-1}{k_{1},k_{2},\ldots ,k_{r}-1}}$ and symmetry: ${\binom {n}{k_{1},k_{2},\ldots ,k_{r}}}={\binom {n}{k_{\sigma _{1}},k_{\sigma _{2}},\ldots ,k_{\sigma _{r}}}}$ where $(\sigma _{i})$ is a permutation of (1, 2, ..., *r*).

### Taylor series

Using Stirling numbers of the first kind the series expansion around any arbitrarily chosen point $z_{0}$ is ${\begin{aligned}{\binom {z}{k}}={\frac {1}{k!}}\sum _{i=0}^{k}z^{i}s_{k,i}&=\sum _{i=0}^{k}(z-z_{0})^{i}\sum _{j=i}^{k}{\binom {z_{0}}{j-i}}{\frac {s_{k+i-j,i}}{(k+i-j)!}}\\&=\sum _{i=0}^{k}(z-z_{0})^{i}\sum _{j=i}^{k}z_{0}^{j-i}{\binom {j}{i}}{\frac {s_{k,j}}{k!}}.\end{aligned}}$

### Binomial coefficient with *n* = 1/2

The definition of the binomial coefficients can be extended to the case where n is real and k is integer.

In particular, the following identity holds for any non-negative integer ⁠ k ⁠: ${\binom {1/2}{k}}={\binom {2k}{k}}{\frac {(-1)^{k+1}}{2^{2k}(2k-1)}}.$

This shows up when expanding ${\sqrt {1+x}}$ into a power series using the Newton binomial series : ${\sqrt {1+x}}=\sum _{k\geq 0}{\binom {1/2}{k}}x^{k}.$

### Products of binomial coefficients

One can express the product of two binomial coefficients as a linear combination of binomial coefficients: ${\binom {z}{m}}{\binom {z}{n}}=\sum _{k=0}^{\min(m,n)}{\binom {m+n-k}{k,m-k,n-k}}{\binom {z}{m+n-k}},$

where the connection coefficients are multinomial coefficients. In terms of labelled combinatorial objects, the connection coefficients represent the number of ways to assign *m* + *n* − *k* labels to a pair of labelled combinatorial objects—of weight *m* and *n* respectively—that have had their first *k* labels identified, or glued together to get a new labelled combinatorial object of weight *m* + *n* − *k*. (That is, to separate the labels into three portions to apply to the glued part, the unglued part of the first object, and the unglued part of the second object.) In this regard, binomial coefficients are to exponential generating series what falling factorials are to ordinary generating series.

The product of all binomial coefficients in the *n*th row of the Pascal triangle is given by the formula: $\prod _{k=0}^{n}{\binom {n}{k}}=\prod _{k=1}^{n}k^{2k-n-1}.$

### Partial fraction decomposition

The partial fraction decomposition of the reciprocal is given by ${\frac {1}{\binom {z}{n}}}=\sum _{i=0}^{n-1}(-1)^{n-1-i}{\binom {n}{i}}{\frac {n-i}{z-i}},\qquad {\frac {1}{\binom {z+n}{n}}}=\sum _{i=1}^{n}(-1)^{i-1}{\binom {n}{i}}{\frac {i}{z+i}}.$

### Newton's binomial series

Newton's binomial series, named after Sir Isaac Newton, is a generalization of the binomial theorem to infinite series: $(1+z)^{\alpha }=\sum _{n=0}^{\infty }{\binom {\alpha }{n}}z^{n}=1+{\binom {\alpha }{1}}z+{\binom {\alpha }{2}}z^{2}+\cdots .$

The identity can be obtained by showing that both sides satisfy the differential equation (1 + *z*) *f'*(*z*) = *α* *f*(*z*).

The radius of convergence of this series is 1. An alternative expression is ${\frac {1}{(1-z)^{\alpha +1}}}=\sum _{n=0}^{\infty }{\binom {n+\alpha }{n}}z^{n}$ where the identity ${\binom {n}{k}}=(-1)^{k}{\binom {k-n-1}{k}}$ is applied.

### Multiset (rising) binomial coefficient

Binomial coefficients count subsets of prescribed size from a given set. A related combinatorial problem is to count multisets of prescribed size with elements drawn from a given set, that is, to count the number of ways to select a certain number of elements from a given set with the possibility of selecting the same element repeatedly. The resulting numbers are called *multiset coefficients*; the number of ways to "multichoose" (i.e., choose with replacement) *k* items from an *n* element set is denoted ⁠ $\left(\!\!{\binom {n}{k}}\!\!\right)$ ⁠.

To avoid ambiguity and confusion with *n'*s main denotation in this article, let *f* = *n* = *r* + (*k* − 1) and *r* = *f* − (*k* − 1).

Multiset coefficients may be expressed in terms of binomial coefficients by the rule ${\binom {f}{k}}=\left(\!\!{\binom {r}{k}}\!\!\right)={\binom {r+k-1}{k}}.$ One possible alternative characterization of this identity is as follows: We may define the falling factorial as $(f)_{k}=f^{\underline {k}}=(f-k+1)\cdots (f-3)\cdot (f-2)\cdot (f-1)\cdot f,$ and the corresponding rising factorial as $r^{(k)}=\,r^{\overline {k}}=\,r\cdot (r+1)\cdot (r+2)\cdot (r+3)\cdots (r+k-1);$ so, for example, $17\cdot 18\cdot 19\cdot 20\cdot 21=(21)_{5}=21^{\underline {5}}=17^{\overline {5}}=17^{(5)}.$ Then the binomial coefficients may be written as ${\binom {f}{k}}={\frac {(f)_{k}}{k!}}={\frac {(f-k+1)\cdots (f-2)\cdot (f-1)\cdot f}{1\cdot 2\cdot 3\cdot 4\cdot 5\cdots k}},$ while the corresponding multiset coefficient is defined by replacing the falling with the rising factorial: $\left(\!\!{\binom {r}{k}}\!\!\right)={\frac {r^{(k)}}{k!}}={\frac {r\cdot (r+1)\cdot (r+2)\cdots (r+k-1)}{1\cdot 2\cdot 3\cdot 4\cdot 5\cdots k}}.$

#### Generalization to negative integers *n*

For any *n*, ${\begin{aligned}{\binom {-n}{k}}&={\frac {-n\cdot -(n+1)\dots -(n+k-2)\cdot -(n+k-1)}{k!}}\\&=(-1)^{k}\;{\frac {n\cdot (n+1)\cdot (n+2)\cdots (n+k-1)}{k!}}\\&=(-1)^{k}{\binom {n+k-1}{k}}\\&=(-1)^{k}\left(\!\!{\binom {n}{k}}\!\!\right)\;.\end{aligned}}$ In particular, binomial coefficients evaluated at negative integers *n* are given by signed multiset coefficients. In the special case ⁠ $n=-1$ ⁠, this reduces to ⁠ $(-1)^{k}={\binom {-1}{k}}=\left(\!\!{\binom {-k}{k}}\!\!\right)$ ⁠.

For example, if *n* = −4 and *k* = 7, then *r* = 4 and *f* = 10: ${\begin{aligned}{\binom {-4}{7}}&={\frac {-10\cdot -9\cdot -8\cdot -7\cdot -6\cdot -5\cdot -4}{1\cdot 2\cdot 3\cdot 4\cdot 5\cdot 6\cdot 7}}\\&=(-1)^{7}\;{\frac {4\cdot 5\cdot 6\cdot 7\cdot 8\cdot 9\cdot 10}{1\cdot 2\cdot 3\cdot 4\cdot 5\cdot 6\cdot 7}}\\&=\left(\!\!{\binom {-7}{7}}\!\!\right)\left(\!\!{\binom {4}{7}}\!\!\right)={\binom {-1}{7}}{\binom {10}{7}}.\end{aligned}}$

### Two real or complex valued arguments

The binomial coefficient is generalized to two real or complex valued arguments using the gamma function or beta function via ${\binom {x}{y}}={\frac {\Gamma (x+1)}{\Gamma (y+1)\Gamma (x-y+1)}}={\frac {1}{(x+1)\mathrm {B} (y+1,x-y+1)}}.$ This definition inherits these following additional properties from ⁠ $\Gamma$ ⁠: ${\binom {x}{y}}={\frac {\sin(y\pi )}{\sin(x\pi )}}{\binom {-y-1}{-x-1}}={\frac {\sin((x-y)\pi )}{\sin(x\pi )}}{\binom {y-x-1}{y}};$ moreover, ${\binom {x}{y}}\cdot {\binom {y}{x}}={\frac {\sin((x-y)\pi )}{(x-y)\pi }}.$

The resulting function has been little-studied, apparently first being graphed in (Fowler 1996). Notably, many binomial identities fail: ${\textstyle {\binom {n}{m}}={\binom {n}{n-m}}}$ but ${\textstyle {\binom {-n}{m}}\neq {\binom {-n}{-n-m}}}$ for *n* positive (so $-n$ negative). The behavior is quite complex, and markedly different in various octants (that is, with respect to the *x* and *y* axes and the line ⁠ $y=x$ ⁠), with the behavior for negative *x* having singularities at negative integer values and a checkerboard of positive and negative regions:

- in the octant $0\leq y\leq x$ it is a smoothly interpolated form of the usual binomial, with a ridge ("Pascal's ridge").
- in the octant $0\leq x\leq y$ and in the quadrant $x\geq 0,y\leq 0$ the function is close to zero.
- in the quadrant $x\leq 0,y\geq 0$ the function is alternatingly very large positive and negative on the parallelograms with vertices $(-n,m+1),(-n,m),(-n-1,m-1),(-n-1,m)$
- in the octant $0>x>y$ the behavior is again alternatingly very large positive and negative, but on a square grid.
- in the octant $-1>y>x+1$ it is close to zero, except for near the singularities.

### Generalization to *q*-series

The binomial coefficient has a *q*-analog generalization known as the Gaussian binomial coefficient. These coefficients are polynomials in an indeterminate (traditionally denoted *q*) and have applications to many enumerative problems in combinatorics, such as counting the number of linear subspaces of a vector space over a finite field and counting the number of subsets of {1, 2, ..., *n*} with certain symmetries (an instance of the cyclic sieving phenomenon).

### Generalization to infinite cardinals

The definition of the binomial coefficient can be generalized to infinite cardinals by defining: ${\binom {\alpha }{\beta }}=\left|\left\{B\subseteq A:\left|B\right|=\beta \right\}\right|$ where A is some set with cardinality ⁠ $\alpha$ ⁠. One can show that the generalized binomial coefficient is well-defined, in the sense that no matter what set we choose to represent the cardinal number ⁠ $\alpha$ ⁠, ${\textstyle {\alpha \choose \beta }}$ will remain the same. For finite cardinals, this definition coincides with the standard definition of the binomial coefficient.

Assuming the Axiom of Choice, one can show that ${\textstyle {\binom {\alpha }{\alpha }}=2^{\alpha }}$ for any infinite cardinal ⁠ $\alpha$ ⁠.
