---
title: "Machine epsilon"
source: https://en.wikipedia.org/wiki/Machine_epsilon
domain: floating-point
license: CC-BY-SA-4.0 / CC-BY-3.0 (floating-point-gui.de)
tags: floating point, ieee 754, rounding error, double precision, machine epsilon
fetched: 2026-07-02
---

# Machine epsilon

**Machine epsilon** or **machine precision** is an upper bound on the relative approximation error due to rounding in floating point number systems. This value characterizes computer arithmetic in the field of numerical analysis, and by extension in the subject of computational science. The quantity is also called **macheps** and it has the symbols Greek epsilon $\varepsilon$ .

There are two prevailing definitions, denoted here as *rounding machine epsilon* or the *formal definition* and *interval machine epsilon* or *mainstream definition*.

In the *mainstream definition*, machine epsilon is independent of rounding method, and is defined simply as *the difference between 1 and the next larger floating point number*.

In the *formal definition*, machine epsilon is dependent on the type of rounding used and is also called **unit roundoff**, which has the symbol bold Roman $\mathbf {u}$ .

The two terms can generally be considered to differ by simply a factor of two, with the *formal definition* yielding an epsilon half the size of the *mainstream definition*, as summarized in the tables in the next section.

## Values for standard hardware arithmetics

The following table lists machine epsilon values for standard floating-point formats.

| IEEE 754 - 2008 | Common name | C data type | Base b | Precision p | Rounding machine epsilon $b^{-(p-1)}/2$ | Interval machine epsilon $b^{-(p-1)}$ |
|---|---|---|---|---|---|---|
| binary16 | half precision | `int16_t` | 2 | 11 (one bit is implicit) | 2−11 ≈ 4.88e-04 | 2−10 ≈ 9.77e-04 |
| binary32 | single precision | `float32_t` | 2 | 24 (one bit is implicit) | 2−24 ≈ 5.96e-08 | 2−23 ≈ 1.19e-07 |
| binary64 | double precision | `float64_t` | 2 | 53 (one bit is implicit) | 2−53 ≈ 1.11e-16 | 2−52 ≈ 2.22e-16 |
|   | extended precision, long double | `_float80` | 2 | 64 | 2−64 ≈ 5.42e-20 | 2−63 ≈ 1.08e-19 |
| binary128 | quad(ruple) precision | `_float128` | 2 | 113 (one bit is implicit) | 2−113 ≈ 9.63e-35 | 2−112 ≈ 1.93e-34 |
| decimal32 | single precision decimal | `_Decimal32` | 10 | 7 | 5 × 10−7 | 10−6 |
| decimal64 | double precision decimal | `_Decimal64` | 10 | 16 | 5 × 10−16 | 10−15 |
| decimal128 | quad(ruple) precision decimal | `_Decimal128` | 10 | 34 | 5 × 10−34 | 10−33 |

1. According to formal definition — used by Prof. Demmel, LAPACK and Scilab. It represents the *largest relative rounding error* in round-to-nearest mode. The rationale is that the *rounding error* is half the interval upwards to the next representable number in finite-precision. Thus, the *relative* rounding error for number x is $[{\text{interval}}/2]/x$ . In this context, the *largest* relative error occurs when $x=1.0$ , and is equal to $[{\text{ULP}}(1.0)/2]/1.0$ , because real numbers in the lower half of the interval $1.0\sim 1.0+{\text{ULP}}(1)$ are rounded down to $1.0$ , and numbers in the upper half of the interval are rounded up to $1.0+{\text{ULP}}(1)$ . Here we use the definition of ${\text{ULP}}(1)$ (*Unit in Last Place*) as the positive difference between 1.0 (which can be represented exactly in finite-precision) and the next greater number representable in finite-precision.
2. According to the mainstream definition — used by Prof. Higham; applied in language constants in Ada, C, C++, Fortran, MATLAB, Mathematica, Octave, Pascal, Python and Rust etc., and defined in textbooks like «Numerical Recipes» by Press *et al*. It represents the *largest relative interval* between two nearest numbers in finite-precision, or the largest rounding error in round-by-chop mode. The rationale is that the *relative* interval for number x is $[{\text{interval}}]/x$ where ${\text{interval}}$ is the distance to upwards the next representable number in finite-precision. In this context, the *largest* relative interval occurs when $x=1.0$ , and is the interval between 1.0 (which can be represented exactly in finite-precision) and the next larger representable floating-point number. This interval is equal to ULP(1).

## Alternative definitions for epsilon

The IEEE standard does not define the terms *machine epsilon* and *unit roundoff*, so differing definitions of these terms are in use, which can cause some confusion.

The two terms differ by simply a factor of two. The more-widely used term (referred to as the *mainstream definition* in this article), is used in most modern programming languages and is simply defined as *machine epsilon is the difference between 1 and the next larger floating point number*. The *formal definition* can generally be considered to yield an epsilon half the size of the *mainstream definition*, although its definition does vary depending on the form of rounding used.

The two terms are described at length in the next two subsections.

### Formal definition (*Rounding* machine epsilon)

The formal definition for *machine epsilon* is the one used by Prof. James Demmel in lecture scripts, the *LAPACK* linear algebra package, numerics research papers and some scientific computing software. Most numerical analysts use the words *machine epsilon* and *unit roundoff* interchangeably with this meaning, which is explored in depth throughout this subsection.

*Rounding* is a procedure for choosing the representation of a real number in a floating point number system. For a number system and a rounding procedure, machine epsilon is the maximum relative error of the chosen rounding procedure.

Some background is needed to determine a value from this definition. A floating point number system is characterized by a radix which is also called the base, b , and by the precision p , i.e. the number of radix b digits of the significand (including any leading implicit bit). All the numbers with the same exponent, e , have the spacing, $b^{e-(p-1)}$ . The spacing changes at the numbers that are perfect powers of b ; the spacing on the side of larger magnitude is b times larger than the spacing on the side of smaller magnitude.

Since machine epsilon is a bound for relative error, it suffices to consider numbers with exponent $e=0$ . It also suffices to consider positive numbers. For the usual round-to-nearest kind of rounding, the absolute rounding error is at most half the spacing, or $b^{-(p-1)}/2$ . This value is the biggest possible numerator for the relative error. The denominator in the relative error is the number being rounded, which should be as small as possible to make the relative error large. The worst relative error therefore happens when rounding is applied to numbers of the form $1+a$ where a is between 0 and $b^{-(p-1)}/2$ . All these numbers round to 1 with relative error $a/(1+a)$ . The maximum occurs when a is at the upper end of its range. The $1+a$ in the denominator is negligible compared to the numerator, so it is left off for expediency, and just $b^{-(p-1)}/2$ is taken as machine epsilon. As has been shown here, the relative error is worst for numbers that round to 1 , so machine epsilon also is called *unit roundoff* meaning roughly "the maximum error that can occur when rounding to the unit value".

Thus, the maximum spacing between a normalised floating point number, x , and an adjacent normalised number is $2\varepsilon |x|$ .

#### Arithmetic model

Numerical analysis uses machine epsilon to study the effects of rounding error. The actual errors of machine arithmetic are far too complicated to be studied directly, so instead, the following simple model is used. The IEEE arithmetic standard says all floating-point operations are done as if it were possible to perform the infinite-precision operation, and then, the result is rounded to a floating-point number. Suppose (1) x , y are floating-point numbers, (2) $\bullet$ is an arithmetic operation on floating-point numbers such as addition or multiplication, and (3) $\circ$ is the infinite precision operation. According to the standard, the computer calculates:

$x\bullet y={\mbox{round}}(x\circ y)$

By the meaning of machine epsilon, the relative error of the rounding is at most machine epsilon in magnitude, so:

$x\bullet y=(x\circ y)(1+z)$

where z in absolute magnitude is at most $\varepsilon$ or **u**. The books by Demmel and Higham in the references can be consulted to see how this model is used to analyze the errors of, say, Gaussian elimination.

### Mainstream definition (*Interval* machine epsilon)

This alternative definition is significantly more widespread: *machine epsilon is the difference between 1 and the next larger floating point number*. This definition is used in language constants in Ada, C, C++, Fortran, MATLAB, Mathematica, Octave, Pascal, Python and Rust etc., and defined in textbooks like «Numerical Recipes» by Press *et al*.

By this definition, $\varepsilon$ equals the value of the unit in the last place relative to 1, i.e. $b^{-(p-1)}$ (where b is the base of the floating point system and p is the precision) and the unit roundoff is $\mathbf {u} ={\frac {\varepsilon }{2}}$ , assuming round-to-nearest mode, and $\mathbf {u} =\varepsilon$ , assuming round-by-chop.

The prevalence of this definition is rooted in its use in the ISO C Standard for constants relating to floating-point types and corresponding constants in other programming languages. It is also widely used in scientific computing software and in the numerics and computing literature.

## How to determine machine epsilon

Where standard libraries do not provide precomputed values (for example `FLT_EPSILON`, `DBL_EPSILON` and `LDBL_EPSILON` in C, `std::numeric_limits<T>::epsilon()` in C++, or `java.lang.Float.EPSILON`/`java.lang.Double.EPSILON` in Java), the best way to determine machine epsilon is to refer to the table, above, and use the appropriate power formula. Computing machine epsilon is often given as a textbook exercise. The following examples compute *interval machine epsilon* in the sense of the spacing of the floating point numbers at 1 rather than in the sense of the unit roundoff.

Note that results depend on the particular floating-point format used, such as `float`, `double`, `long double`, or similar as supported by the programming language, the compiler, and the runtime library for the actual platform.

Some formats supported by the processor might not be supported by the chosen compiler and operating system. Other formats might be emulated by the runtime library, including arbitrary-precision arithmetic available in some languages and libraries.

In a strict sense the term *machine epsilon* means the $1+\varepsilon$ accuracy directly supported by the processor (or coprocessor), not some $1+\varepsilon$ accuracy supported by a specific compiler for a specific operating system, unless it's known to use the best format.

IEEE 754 floating-point formats have the property that, when reinterpreted as a two's complement integer of the same width, they monotonically increase over positive values and monotonically decrease over negative values (see the binary representation of 32 bit floats). They also have the property that $0<|f(x)|<\infty$ , and $|f(x+1)-f(x)|\geq |f(x)-f(x-1)|$ (where $f(x)$ is the aforementioned integer reinterpretation of x ). In languages that allow type punning and always use IEEE 754–1985, we can exploit this to compute a machine epsilon in constant time. For example, in C:

```mw
union DoubleBits {
    int64_t i;
    double d;
};

double epsilon(double value) {
    union DoubleBits s;
    s.d = value;
    s.i++;
    return s.d - value;
}
```

This will give a result of the same sign as value. If a positive result is always desired, the return statement of `epsilon()` can be replaced with:

```mw
return s.i < 0 ? value - s.d : s.d - value;
```

Example in Python:

```mw
from typing import Callable

def epsilon(func: Callable[[float], float] = float) -> float:
    eps: float = func(1)
    while func(1) + eps != func(1):
        eps_last: float = eps
        eps = func(eps) / func(2)
    return eps_last
```

64-bit doubles give 2.220446e-16, which is 2−52 as expected.

### Approximation

The following simple algorithm can be used to approximate the machine epsilon, to within a factor of two of its true value, using a linear search.

```
epsilon = 1.0;

while (1.0 + 0.5 * epsilon) ≠ 1.0:
    epsilon = 0.5 * epsilon
```

The machine epsilon, ${\textstyle \varepsilon _{\text{mach}}}$ can also simply be calculated as two to the negative power of the number of bits used for the mantissa.

$\varepsilon _{\text{mach}}\ =\ 2^{-{\text{bits used for magnitude of mantissa}}}$

## Relationship to absolute relative error

If ${\textstyle y}$ is the machine representation of a number ${\textstyle x}$ then the absolute relative error in the representation is ${\textstyle \left|{\dfrac {x-y}{x}}\right|\leq \varepsilon _{\text{mach}}.}$

### Proof

The following proof is limited to positive numbers and machine representations using round-by-chop.

If ${\textstyle x}$ is a positive number we want to represent, it will be between a machine number ${\textstyle x_{b}}$ below ${\textstyle x}$ and a machine number ${\textstyle x_{u}}$ above ${\textstyle x}$ .

If ${\textstyle x_{b}=\left(1.b_{1}b_{2}\ldots b_{m}\right)_{2}\times 2^{k}}$ , where ${\textstyle m}$ is the number of bits used for the magnitude of the significand, then:

${\begin{aligned}x_{u}&=\left[(1.b_{1}b_{2}\ldots b_{m})_{2}+(0.00\ldots 1)_{2}\right]\times 2^{k}\\&=\left[(1.b_{1}b_{2}\ldots b_{m})_{2}+2^{-m}\right]\times 2^{k}\\&=(1.b_{1}b_{2}\ldots b_{m})_{2}\times 2^{k}+2^{-m}\times 2^{k}\\&=(1.b_{1}b_{2}\ldots b_{m})_{2}\times 2^{k}+2^{-m+k}.\end{aligned}}$

Since the representation of ${\textstyle x}$ will be either ${\textstyle x_{b}}$ or ${\textstyle x_{u}}$ ,

${\begin{aligned}\left|x-y\right|&\leq \left|x_{b}-x_{u}\right|\\&=2^{-m+k}\end{aligned}}$ ${\begin{aligned}\left|{\frac {x-y}{x}}\right|&\leq {\frac {2^{-m+k}}{x}}\\&\leq {\frac {2^{-m+k}}{x_{b}}}\\&={\frac {2^{-m+k}}{(1\cdot b_{1}b_{2}\ldots b_{m})_{2}2^{k}}}\\&={\frac {2^{-m}}{(1\cdot b_{1}b_{2}\ldots b_{m})_{2}}}\\&\leq 2^{-m}=\varepsilon _{\text{mach}}.\end{aligned}}$

Although this proof is limited to positive numbers and round-by-chop, the same method can be used to prove the inequality in relation to negative numbers and round-to-nearest machine representations.
