---
title: "Floating-point arithmetic (part 2/2)"
source: https://en.wikipedia.org/wiki/Floating-point_arithmetic
domain: awq-quantization
license: CC-BY-SA-4.0
tags: activation aware quantization, weight quantization scaling, awq method, salient weight preservation, low bit llm
fetched: 2026-07-02
part: 2/2
---

## Dealing with exceptional cases

Floating-point computation in a computer can run into three kinds of problems:

- An operation can be mathematically undefined, such as ∞/∞, or division by zero.
- An operation can be legal in principle, but not supported by the specific format, for example, calculating the square root of −1 or the inverse sine of 2 (both of which result in complex numbers).
- An operation can be legal in principle, but the result can be impossible to represent in the specified format, because the exponent is too large or too small to encode in the exponent field. Such an event is called an overflow (exponent too large), underflow (exponent too small) or denormalization (precision loss).

Prior to the IEEE standard, such conditions usually caused the program to terminate, or triggered some kind of trap that the programmer might be able to catch. How this worked was system-dependent, meaning that floating-point programs were not portable.

The term "exception" as used in IEEE 754 is a general term meaning an exceptional condition, which is not necessarily an error, and is a different usage to that typically defined in programming languages such as a C++ or Java, in which an "exception" is an alternative flow of control, closer to what is termed a "trap" in IEEE 754 terminology. However, in such languages, a control-flow exception such as `ArithmeticException` may still be thrown.

Here, the required default method of handling exceptions according to IEEE 754 is discussed (the IEEE 754 optional trapping and other "alternate exception handling" modes are not discussed). Arithmetic exceptions are (by default) required to be recorded in "sticky" status flag bits. That they are "sticky" means that they are not reset by the next (arithmetic) operation, but stay set until explicitly reset. The use of "sticky" flags thus allows for testing of exceptional conditions to be delayed until after a full floating-point expression or subroutine: without them exceptional conditions that could not be otherwise ignored would require explicit testing immediately after every floating-point operation. By default, an operation always returns a result according to specification without interrupting computation. For instance, 1/0 returns +∞, while also setting the divide-by-zero flag bit (this default of ∞ is designed to often return a finite result when used in subsequent operations and so be safely ignored).

The original IEEE 754 standard, however, failed to recommend operations to handle such sets of arithmetic exception flag bits. So while these were implemented in hardware, initially programming language implementations typically did not provide a means to access them (apart from assembler). Over time some programming language standards (e.g., C99/C11 and Fortran) have been updated to specify methods to access and change status flag bits. The 2008 version of the IEEE 754 standard now specifies a few operations for accessing and handling the arithmetic flag bits. The programming model is based on a single thread of execution and use of them by multiple threads has to be handled by a means outside of the standard (e.g. C11 specifies that the flags have thread-local storage).

IEEE 754 specifies five arithmetic exceptions that are to be recorded in the status flags ("sticky bits"):

- **inexact**, set if the rounded (and returned) value is different from the mathematically exact result of the operation.
- **underflow**, set if the rounded value is tiny (as specified in IEEE 754) *and* inexact (or maybe limited to if it has denormalization loss, as per the 1985 version of IEEE 754), returning a subnormal value including the zeros.
- **overflow**, set if the absolute value of the rounded value is too large to be represented. An infinity or maximal finite value is returned, depending on which rounding is used.
- **divide-by-zero**, set if the result is infinite given finite operands, returning an infinity, either +∞ or −∞.
- **invalid**, set if a finite or infinite result cannot be returned e.g. sqrt(−1) or 0/0, returning a quiet NaN.

The default return value for each of the exceptions is designed to give the correct result in the majority of cases such that the exceptions can be ignored in the majority of codes. *inexact* returns a correctly rounded result, and *underflow* returns a value less than or equal to the smallest positive normal number in magnitude and can almost always be ignored. *divide-by-zero* returns infinity exactly, which will typically then divide a finite number and so give zero, or else will give an *invalid* exception subsequently if not, and so can also typically be ignored. For example, the effective resistance of n resistors in parallel (see fig. 1) is given by $R_{\text{tot}}=1/(1/R_{1}+1/R_{2}+\cdots +1/R_{n})$ . If a short-circuit develops with $R_{1}$ set to 0, $1/R_{1}$ will return +infinity which will give a final $R_{tot}$ of 0, as expected (see the continued fraction example of IEEE 754 design rationale for another example).

*Overflow* and *invalid* exceptions can typically not be ignored, but do not necessarily represent errors: for example, a root-finding routine, as part of its normal operation, may evaluate a passed-in function at values outside of its domain, returning NaN and an *invalid* exception flag to be ignored until finding a useful start point.


## Accuracy problems

The fact that floating-point numbers cannot accurately represent all real numbers, and that floating-point operations cannot accurately represent true arithmetic operations, leads to many surprising situations. This is related to the finite precision with which computers generally represent numbers.

For example, the decimal numbers 0.1 and 0.01 cannot be represented exactly as binary floating-point numbers. In the IEEE 754 binary32 format with its 24-bit significand, the result of attempting to square the approximation to 0.1 is neither 0.01 nor the representable number closest to it. The decimal number 0.1 is represented in binary as *e* = −4; *s* = 110011001100110011001101, which is

0.100000001490116119384765625 exactly.

Squaring this number gives

0.010000000298023226097399174250313080847263336181640625 exactly.

Squaring it with rounding to the 24-bit precision gives

0.010000000707805156707763671875 exactly.

But the representable number closest to 0.01 is

0.009999999776482582092285156250 exactly.

Also, the non-representability of π (and π/2) means that an attempted computation of tan(π/2) will not yield a result of infinity, nor will it even overflow in the usual floating-point formats (assuming an accurate implementation of tan). It is simply not possible for standard floating-point hardware to attempt to compute tan(π/2), because π/2 cannot be represented exactly. This computation in C:

```mw
// Enough digits to be sure we get the correct approximation.
const double pi = 3.1415926535897932384626433832795;
double z = tan(pi / 2.0);
```

will give a result of 16331239353195370.0. In single precision (using the `tanf` function), the result will be −22877332.0.

By the same token, an attempted computation of sin(π) will not yield zero. The result will be (approximately) 0.1225×10−15 in double precision, or −0.8742×10−7 in single precision.

While floating-point addition and multiplication are both commutative (*a* + *b* = *b* + *a* and *a* × *b* = *b* × *a*), they are not necessarily associative. That is, (*a* + *b*) + *c* is not necessarily equal to *a* + (*b* + *c*). Using 7-digit significand decimal arithmetic:

```
 a = 1234.567, b = 45.67834, c = 0.0004
```

```
 (a + b) + c:
     1234.567   (a)
   +   45.67834 (b)
   ____________
     1280.24534   rounds to   1280.245
```

```
    1280.245  (a + b)
   +   0.0004 (c)
   ____________
    1280.2454   rounds to   1280.245  ← (a + b) + c
```

```
 a + (b + c):
   45.67834 (b)
 +  0.0004  (c)
 ____________
   45.67874
```

```
   1234.567   (a)
 +   45.67874   (b + c)
 ____________
   1280.24574   rounds to   1280.246 ← a + (b + c)
```

They are also not necessarily distributive. That is, (*a* + *b*) × *c* may not be the same as *a* × *c* + *b* × *c*:

```
 1234.567 × 3.333333 = 4115.223
 1.234567 × 3.333333 = 4.115223
                       4115.223 + 4.115223 = 4119.338
 but
 1234.567 + 1.234567 = 1235.802
                       1235.802 × 3.333333 = 4119.340
```

In addition to loss of significance, inability to represent numbers such as π and 0.1 exactly, and other slight inaccuracies, the following phenomena may occur:

- Cancellation: subtraction of nearly equal operands may cause extreme loss of accuracy. When we subtract two almost equal numbers we set the most significant digits to zero, leaving ourselves with just the insignificant, and most erroneous, digits. For example, when determining a derivative of a function the following formula is used: $Q(h)={\frac {f(a+h)-f(a)}{h}}.$ Intuitively one would want an *h* very close to zero; however, when using floating-point operations, the smallest number will not give the best approximation of a derivative. As *h* grows smaller, the difference between *f*(*a* + *h*) and *f*(*a*) grows smaller, cancelling out the most significant and least erroneous digits and making the most erroneous digits more important. As a result the smallest number of *h* possible will give a more erroneous approximation of a derivative than a somewhat larger number. This is perhaps the most common and serious accuracy problem.
- Conversions to integer are not intuitive: converting (63.0/9.0) to integer yields 7, but converting (0.63/0.09) may yield 6. This is because conversions generally truncate rather than round. Floor and ceiling functions may produce answers which are off by one from the intuitively expected value.
- Limited exponent range: results might overflow yielding infinity, or underflow yielding a subnormal number or zero. In these cases precision will be lost.
- Testing for safe division is problematic: Checking that the divisor is not zero does not guarantee that a division will not overflow.
- Testing for equality is problematic. Two computational sequences that are mathematically equal may well produce different floating-point values.

### Incidents

- On 25 February 1991, a loss of significance in a MIM-104 Patriot missile battery prevented it from intercepting an incoming Scud missile in Dhahran, Saudi Arabia, contributing to the death of 28 soldiers from the U.S. Army's 14th Quartermaster Detachment. The weapons control computer counted time in an integer number of tenths of a second since boot. For conversion to a floating-point number of seconds in velocity and position calculations, the software originally multiplied this number by a 24-bit fixed-point binary approximation to 0.1, specifically $0.00011001100110011001100_{2}=0.1\times (1-2^{-20}).$ Some parts of the software were later adapted to use a more accurate conversion to floating-point, but some parts were not updated and still used the 24-bit approximation. These parts of the software drifted from one another by about 3.43 milliseconds per hour. After 20 hours, the discrepancy of about 68.7 ms was enough for the radar tracking system to lose track of Scuds; the control system in the Dhahran missile battery had been running for about 100 hours when it failed to track and intercept an incoming Scud. The failure to intercept arose not from using floating point specifically, but from subtracting two different approximations to unit conversion with different errors when representing time, so the unit conversion error in the difference did not cancel out but rather grew indefinitely with uptime.
- Salami slicing is the practice of removing the "invisible" part of a transaction into a separate account.

### Machine precision and backward error analysis

*Machine precision* is a quantity that characterizes the accuracy of a floating-point system, and is used in backward error analysis of floating-point algorithms. It is also known as unit roundoff or *machine epsilon*. Usually denoted *Ε*mach, its value depends on the particular rounding being used.

With rounding to zero, $\mathrm {E} _{\text{mach}}=B^{1-P},\,$ whereas rounding to nearest, $\mathrm {E} _{\text{mach}}={\tfrac {1}{2}}B^{1-P},$ where *B* is the base of the system and *P* is the precision of the significand (in base *B*).

This is important since it bounds the *relative error* in representing any non-zero real number *x* within the normalized range of a floating-point system: $\left|{\frac {\operatorname {fl} (x)-x}{x}}\right|\leq \mathrm {E} _{\text{mach}}.$

Backward error analysis, the theory of which was developed and popularized by James H. Wilkinson, can be used to establish that an algorithm implementing a numerical function is numerically stable. The basic approach is to show that although the calculated result, due to roundoff errors, will not be exactly correct, it is the exact solution to a nearby problem with slightly perturbed input data. If the perturbation required is small, on the order of the uncertainty in the input data, then the results are in some sense as accurate as the data "deserves". The algorithm is then defined as *backward stable*. Stability is a measure of the sensitivity to rounding errors of a given numerical procedure; by contrast, the condition number of a function for a given problem indicates the inherent sensitivity of the function to small perturbations in its input and is independent of the implementation used to solve the problem.

As a trivial example, consider a simple expression giving the inner product of (length two) vectors x and y , then ${\begin{aligned}\operatorname {fl} (x\cdot y)&=\operatorname {fl} {\big (}\operatorname {fl} (x_{1}\cdot y_{1})+\operatorname {fl} (x_{2}\cdot y_{2}){\big )},&&{\text{ where }}\operatorname {fl} (){\text{ indicates correctly rounded floating-point arithmetic}}\\&=\operatorname {fl} {\big (}(x_{1}\cdot y_{1})(1+\delta _{1})+(x_{2}\cdot y_{2})(1+\delta _{2}){\big )},&&{\text{ where }}\delta _{n}\leq \mathrm {E} _{\text{mach}},{\text{ from above}}\\&={\big (}(x_{1}\cdot y_{1})(1+\delta _{1})+(x_{2}\cdot y_{2})(1+\delta _{2}){\big )}(1+\delta _{3})\\&=(x_{1}\cdot y_{1})(1+\delta _{1})(1+\delta _{3})+(x_{2}\cdot y_{2})(1+\delta _{2})(1+\delta _{3}),\end{aligned}}$ and so $\operatorname {fl} (x\cdot y)={\hat {x}}\cdot {\hat {y}},$

where

${\begin{aligned}{\hat {x}}_{1}&=x_{1}(1+\delta _{1});&{\hat {x}}_{2}&=x_{2}(1+\delta _{2});\\{\hat {y}}_{1}&=y_{1}(1+\delta _{3});&{\hat {y}}_{2}&=y_{2}(1+\delta _{3}),\\\end{aligned}}$

where

$\delta _{n}\leq \mathrm {E} _{\text{mach}}$

by definition, which is the sum of two slightly perturbed (on the order of Εmach) input data, and so is backward stable. For more realistic examples in numerical linear algebra, see Higham 2002 and other references below.

### Minimizing the effect of accuracy problems

Although individual arithmetic operations of IEEE 754 are guaranteed accurate to within half a ULP, more complicated formulae can suffer from larger errors for a variety of reasons. The loss of accuracy can be substantial if a problem or its data are ill-conditioned, meaning that the correct result is hypersensitive to tiny perturbations in its data. However, even functions that are well-conditioned can suffer from large loss of accuracy if an algorithm numerically unstable for that data is used: apparently equivalent formulations of expressions in a programming language can differ markedly in their numerical stability. One approach to remove the risk of such loss of accuracy is the design and analysis of numerically stable algorithms, which is an aim of the branch of mathematics known as numerical analysis. Another approach that can protect against the risk of numerical instabilities is the computation of intermediate (scratch) values in an algorithm at a higher precision than the final result requires, which can remove, or reduce by orders of magnitude, such risk: IEEE 754 quadruple precision and extended precision are designed for this purpose when computing at double precision.

For example, the following algorithm is a direct implementation to compute the function $f(x)={\frac {x-1}{\exp(x-1)-1}}$ , which is well-conditioned at $x=1$ . However, it can be shown to be numerically unstable and lose up to half the significant digits carried by the arithmetic when computed near 1.0.

```mw
#include <math.h>

double f(double x)
{
    double y = x - 1.0;
    double z = exp(y);
    if (z != 1.0) {
        z = y / (z - 1.0);
    }
    return z;
}
```

A numerical analysis of the algorithm reveals that if the following non-obvious change to the line `z = y / (z - 1.0);` is made:

```mw
z = log(z) / (z - 1.0);
```

then the algorithm becomes numerically stable and can compute to full double precision.

To maintain the properties of such carefully constructed numerically stable programs, careful handling by the compiler is required. Certain "optimizations" that compilers might make (for example, reordering operations) can work against the goals of well-behaved software. There is some controversy about the failings of compilers and language designs in this area: C99 is an example of a language where such optimizations are carefully specified to maintain numerical precision. See the external references at the bottom of this article.

A detailed treatment of the techniques for writing high-quality floating-point software is beyond the scope of this article, and the reader is referred to, and the other references at the bottom of this article. Kahan suggests several rules of thumb that can substantially decrease by orders of magnitude the risk of numerical anomalies, in addition to, or in lieu of, a more careful numerical analysis. These include: as noted above, computing all expressions and intermediate results in the highest precision supported in hardware (a common rule of thumb is to carry twice the precision of the desired result, i.e. compute in double precision for a final single-precision result, or in double extended or quad precision for up to double-precision results); and rounding input data and results to only the precision required and supported by the input data (carrying excess precision in the final result beyond that required and supported by the input data can be misleading, increases storage cost and decreases speed, and the excess bits can affect convergence of numerical procedures: notably, the first form of the iterative example given below converges correctly when using this rule of thumb). Brief descriptions of several additional issues and techniques follow.

As decimal fractions can often not be exactly represented in binary floating-point, such arithmetic is at its best when it is simply being used to measure real-world quantities over a wide range of scales (such as the orbital period of a moon around Saturn or the mass of a proton), and at its worst when it is expected to model the interactions of quantities expressed as decimal strings that are expected to be exact. An example of the latter case is financial calculations. For this reason, financial software tends not to use a binary floating-point number representation. The "decimal" data type of the C# and Python programming languages, and the decimal formats of the IEEE 754-2008 standard, are designed to avoid the problems of binary floating-point representations when applied to human-entered exact decimal values, and make the arithmetic always behave as expected when numbers are printed in decimal.

Expectations from mathematics may not be realized in the field of floating-point computation. For example, it is known that $(x+y)(x-y)=x^{2}-y^{2}\,$ , and that $\sin ^{2}{\theta }+\cos ^{2}{\theta }=1\,$ . However, these facts cannot be relied on when the quantities involved are the result of floating-point computation.

The use of the equality test (`if (x==y) ...`) requires care when dealing with floating-point numbers. Even simple expressions like `0.6 / 0.2 - 3 == 0` will, on most computers, fail to be true (in IEEE 754 double precision, for example, `0.6 / 0.2 - 3` is approximately equal to −4.44089209850063×10−16). Consequently, such tests are sometimes replaced with "fuzzy" comparisons (`if (abs(x-y) < epsilon) ...`, where epsilon is sufficiently small and tailored to the application, such as 1.0E−13). The wisdom of doing this varies greatly, and can require numerical analysis to bound epsilon. Values derived from the primary data representation and their comparisons should be performed in a wider, extended, precision to minimize the risk of such inconsistencies due to round-off errors. It is often better to organize the code in such a way that such tests are unnecessary. For example, in computational geometry, exact tests of whether a point lies off or on a line or plane defined by other points can be performed using adaptive precision or exact arithmetic methods.

Small errors in floating-point arithmetic can grow when mathematical algorithms perform operations an enormous number of times. A few examples are matrix inversion, eigenvector computation, and differential equation solving. These algorithms must be very carefully designed, using numerical approaches such as iterative refinement, if they are to work well.

Summation of a vector of floating-point values is a basic algorithm in scientific computing, and so an awareness of when loss of significance can occur is essential. For example, if one is adding a very large number of numbers, the individual addends are very small compared with the sum. This can lead to loss of significance. A typical addition would then be something like

```
3253.671
+  3.141276
-----------
3256.812
```

The low 3 digits of the addends are effectively lost. Suppose, for example, that one needs to add many numbers, all approximately equal to 3. After 1000 of them have been added, the running sum is about 3000; the lost digits are not regained. The Kahan summation algorithm may be used to reduce the errors.

Round-off error can affect the convergence and accuracy of iterative numerical procedures. As an example, Archimedes approximated π by calculating the perimeters of polygons inscribing and circumscribing a circle, starting with hexagons, and successively doubling the number of sides. As noted above, computations may be rearranged in a way that is mathematically equivalent but less prone to error (numerical analysis). Two forms of the recurrence formula for the circumscribed polygon are:

- ${\textstyle t_{0}={\frac {1}{\sqrt {3}}}}$
- First form: ${\textstyle t_{i+1}={\frac {{\sqrt {t_{i}^{2}+1}}-1}{t_{i}}}}$
- Second form: ${\textstyle t_{i+1}={\frac {t_{i}}{{\sqrt {t_{i}^{2}+1}}+1}}}$
- $\pi \sim 6\times 2^{i}\times t_{i}$ , converging as $i\rightarrow \infty$

Here is a computation using IEEE "double" (a significand with 53 bits of precision) arithmetic:

```
 i   6 × 2i × ti, first form    6 × 2i × ti, second form
---------------------------------------------------------
 0   3.4641016151377543863      3.4641016151377543863
 1   3.2153903091734710173      3.2153903091734723496
 2   3.1596599420974940120      3.1596599420975006733
 3   3.1460862151314012979      3.1460862151314352708
 4   3.1427145996453136334      3.1427145996453689225
 5   3.1418730499801259536      3.1418730499798241950
 6   3.1416627470548084133      3.1416627470568494473
 7   3.1416101765997805905      3.1416101766046906629
 8   3.1415970343230776862      3.1415970343215275928
 9   3.1415937488171150615      3.1415937487713536668
10   3.1415929278733740748      3.1415929273850979885
11   3.1415927256228504127      3.1415927220386148377
12   3.1415926717412858693      3.1415926707019992125
13   3.1415926189011456060      3.1415926578678454728
14   3.1415926717412858693      3.1415926546593073709
15   3.1415919358822321783      3.1415926538571730119
16   3.1415926717412858693      3.1415926536566394222
17   3.1415810075796233302      3.1415926536065061913
18   3.1415926717412858693      3.1415926535939728836
19   3.1414061547378810956      3.1415926535908393901
20   3.1405434924008406305      3.1415926535900560168
21   3.1400068646912273617      3.1415926535898608396
22   3.1349453756585929919      3.1415926535898122118
23   3.1400068646912273617      3.1415926535897995552
24   3.2245152435345525443      3.1415926535897968907
25                              3.1415926535897962246
26                              3.1415926535897962246
27                              3.1415926535897962246
28                              3.1415926535897962246
              The true value is 3.14159265358979323846264338327...
```

While the two forms of the recurrence formula are clearly mathematically equivalent, the first subtracts 1 from a number extremely close to 1, leading to an increasingly problematic loss of significant digits. As the recurrence is applied repeatedly, the accuracy improves at first, but then it deteriorates. It never gets better than about 8 digits, even though 53-bit arithmetic should be capable of about 16 digits of precision. When the second form of the recurrence is used, the value converges to 15 digits of precision.

### "Fast math" optimization

The aforementioned lack of associativity of floating-point operations in general means that compilers cannot as effectively reorder arithmetic expressions as they could with integer and fixed-point arithmetic, presenting a roadblock in optimizations such as common subexpression elimination and auto-vectorization. The "fast math" option on many compilers (ICC, GCC, Clang, MSVC...) turns on reassociation along with unsafe assumptions such as a lack of NaN and infinite numbers in IEEE 754. Some compilers also offer more granular options to only turn on reassociation or to mark specific regions of code for more aggressive optimization. In either case, the programmer is exposed to many of the precision pitfalls mentioned above for the portion of the program using "fast" math.

In some compilers (GCC and Clang [when a GCC installation is present]), turning on "fast" math may cause the program to disable subnormal floats at startup, affecting the floating-point behavior of not only the generated code, but also any program using such code as a library. This was fixed in GCC 13.

In most Fortran compilers, as allowed by the ISO/IEC 1539-1:2004 Fortran standard, reassociation is the default, with breakage largely prevented by the "protect parens" setting (also on by default). This setting stops the compiler from reassociating beyond the boundaries of parentheses. Intel Fortran Compiler is a notable outlier.

A common problem in "fast" math is that subexpressions may not be optimized identically from place to place, leading to unexpected differences. One interpretation of the issue is that "fast" math as implemented currently has a poorly defined semantics. One attempt at formalizing "fast" math optimizations is seen in *Icing*, a verified compiler.
