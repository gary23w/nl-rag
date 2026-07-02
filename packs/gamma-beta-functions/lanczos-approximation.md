---
title: "Lanczos approximation"
source: https://en.wikipedia.org/wiki/Lanczos_approximation
domain: gamma-beta-functions
license: CC-BY-SA-4.0
tags: gamma function, beta function, digamma function, incomplete gamma function
fetched: 2026-07-02
---

# Lanczos approximation

In mathematics, the **Lanczos approximation** is a method for computing the gamma function numerically, published by Cornelius Lanczos in 1964. It is a practical alternative to the more popular Stirling's approximation for calculating the gamma function with fixed precision.

## Introduction

The Lanczos approximation consists of the formula

$\Gamma (z+1)={\sqrt {2\pi }}{\left(z+g+{\tfrac {1}{2}}\right)}^{z+{\frac {1}{2}}}e^{-\left(z+g+{\frac {1}{2}}\right)}A_{g}(z)$

for the gamma function, with

$A_{g}(z)={\tfrac {1}{2}}p_{0}(g)+p_{1}(g){\frac {z}{z+1}}+p_{2}(g){\frac {z(z-1)}{(z+1)(z+2)}}+\cdots .$

Here g is a real constant that may be chosen arbitrarily subject to the restriction that Re(*z* + *g* + ⁠1/2⁠) > 0. The coefficients p, which depend on g, are slightly more difficult to calculate (see below). Although the formula as stated here is only valid for arguments in the right complex half-plane, it can be extended to the entire complex plane by the reflection formula,

$\Gamma (1-z)\;\Gamma (z)={\frac {\pi }{\sin \pi z}}.$

The series A is convergent, and may be truncated to obtain an approximation with the desired precision. By choosing an appropriate g (typically a small integer), only some 5–10 terms of the series are needed to compute the gamma function with typical single or double floating-point precision. If a fixed g is chosen, the coefficients can be calculated in advance and, thanks to partial fraction decomposition, the sum is recast into the following form:

$A_{g}(z)=c_{0}+\sum _{k=1}^{N}{\frac {c_{k}}{z+k}}$

Thus computing the gamma function becomes a matter of evaluating only a small number of elementary functions and multiplying by stored constants. The Lanczos approximation was popularized by *Numerical Recipes*, according to which computing the gamma function becomes "not much more difficult than other built-in functions that we take for granted, such as sin *x* or *e**x*." The method is also implemented in the GNU Scientific Library, Boost, CPython and musl.

## Coefficients

The coefficients are given by

$p_{k}(g)={\frac {\sqrt {2}}{\pi }}\sum _{l=0}^{k}C_{2k+1,\,2l+1}\left(l-{\tfrac {1}{2}}\right)!{\left(l+g+{\tfrac {1}{2}}\right)}^{-\left(l+{\frac {1}{2}}\right)}e^{l+g+{\frac {1}{2}}}$

where *C**n*,*m* represents the (*n*, *m*)th element of the matrix of coefficients for the Chebyshev polynomials, which can be calculated recursively from these identities:

${\begin{aligned}C_{1,\,1}&=1\\[5px]C_{2,\,2}&=1\\[5px]C_{n+1,\,1}&=-\,C_{n-1,\,1}&{\text{ for }}n&=2,3,4\,\dots \\[5px]C_{n+1,\,n+1}&=2\,C_{n,\,n}&{\text{ for }}n&=2,3,4\,\dots \\[5px]C_{n+1,\,m+1}&=2\,C_{n,\,m}-C_{n-1,\,m+1}&{\text{ for }}n&>m=1,2,3\,\dots \end{aligned}}$

Godfrey (2001) describes how to obtain the coefficients and also the value of the truncated series A as a matrix product.

## Derivation

Lanczos derived the formula from Leonhard Euler's integral

$\Gamma (z+1)=\int _{0}^{\infty }t^{z}\,e^{-t}\,dt,$

performing a sequence of basic manipulations to obtain

$\Gamma (z+1)=\left(z+g+1\right)^{z+1}e^{-(z+g+1)}\int _{0}^{e}{\bigl (}v(1-\log v){\bigr )}^{z}v^{g}\,dv,$

and deriving a series for the integral.

## Simple implementation

The following implementation in the Python programming language works for complex arguments and typically gives 13 correct decimal places. Note that omitting the smallest coefficients (in pursuit of speed, for example) gives totally inaccurate results; the coefficients must be recomputed from scratch for an expansion with fewer terms.

```mw
from cmath import sin, sqrt, pi, exp

"""
The coefficients used in the code are for when g = 7 and n = 9
Here are some other samples

g = 5
n = 5
p = [
    1.0000018972739440364,
    76.180082222642137322,
    -86.505092037054859197,
    24.012898581922685900,
    -1.2296028490285820771
]

g = 5
n = 7
p = [
    1.0000000001900148240,
    76.180091729471463483,
    -86.505320329416767652,
    24.014098240830910490,
    -1.2317395724501553875,
    0.0012086509738661785061,
    -5.3952393849531283785e-6
]

g = 8
n = 12
p = [
    0.9999999999999999298,
    1975.3739023578852322,
    -4397.3823927922428918,
    3462.6328459862717019,
    -1156.9851431631167820,
    154.53815050252775060,
    -6.2536716123689161798,
    0.034642762454736807441,
    -7.4776171974442977377e-7,
    6.3041253821852264261e-8,
    -2.7405717035683877489e-8,
    4.0486948817567609101e-9
]
"""

g = 7
n = 9
p = [
    0.99999999999980993,
    676.5203681218851,
    -1259.1392167224028,
    771.32342877765313,
    -176.61502916214059,
    12.507343278686905,
    -0.13857109526572012,
    9.9843695780195716e-6,
    1.5056327351493116e-7
]

EPSILON = 1e-07
def drop_imag(z):
    if abs(z.imag) <= EPSILON:
        z = z.real
    return z

def gamma(z):
    z = complex(z)
    if z.real < 0.5:
        y = pi / (sin(pi * z) * gamma(1 - z))  # Reflection formula
    else:
        z -= 1
        x = p[0]
        for i in range(1, len(p)):
            x += p[i] / (z + i)
        t = z + g + 0.5
        y = sqrt(2 * pi) * t ** (z + 0.5) * exp(-t) * x
    return drop_imag(y)
"""
The above use of the reflection (thus the if-else structure) is necessary, even though 
it may look strange, as it allows to extend the approximation to values of z where 
Re(z) < 0.5, where the Lanczos method is not valid.
"""

print(gamma(1))
print(gamma(5))   
print(gamma(0.5))
```
