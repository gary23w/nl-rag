---
title: "Round-off error"
source: https://en.wikipedia.org/wiki/Round-off_error
domain: gptq-quantization
license: CC-BY-SA-4.0
tags: post training quantization, weight only quantization, layer wise quantization, gptq method, low bit inference
fetched: 2026-07-02
---

# Round-off error

In computing, a **roundoff error**, also called **rounding error**, is the difference between the result produced by a given algorithm using exact arithmetic and the result produced by the same algorithm using finite-precision, rounded arithmetic. Rounding errors are due to inexactness in the representation of real numbers and the arithmetic operations done with them. This is a form of quantization error. When using approximation equations or algorithms, especially when using finitely many digits to represent real numbers (which in theory have infinitely many digits), one of the goals of numerical analysis is to estimate computation errors. Computation errors, also called numerical errors, include both truncation errors and roundoff errors.

When a sequence of calculations with an input involving any roundoff error are made, errors may accumulate, sometimes dominating the calculation. In ill-conditioned problems, significant error may accumulate.

In short, there are two major facets of roundoff errors involved in numerical calculations:

1. The ability of computers to represent both magnitude and precision of numbers is inherently limited.
2. Certain numerical manipulations are highly sensitive to roundoff errors. This can result from both mathematical considerations as well as from the way in which computers perform arithmetic operations.

## Representation error

The error introduced by attempting to represent a number using a finite string of digits is a form of roundoff error called **representation error**. Here are some examples of representation error in decimal representations:

| Notation | Representation | Approximation | Error |
|---|---|---|---|
| 1⁄7 | 0.142 857 | 0.142 857 | 0.000 000 142 857 |
| ln 2 | 0.693 147 180 559 945 309 41... | 0.693 147 | 0.000 000 180 559 945 309 41... |
| log10 2 | 0.301 029 995 663 981 195 21... | 0.3010 | 0.000 029 995 663 981 195 21... |
| 3√2 | 1.259 921 049 894 873 164 76... | 1.25992 | 0.000 001 049 894 873 164 76... |
| √2 | 1.414 213 562 373 095 048 80... | 1.41421 | 0.000 003 562 373 095 048 80... |
| *e* | 2.718 281 828 459 045 235 36... | 2.718 281 828 459 045 | 0.000 000 000 000 000 235 36... |
| *π* | 3.141 592 653 589 793 238 46... | 3.141 592 653 589 793 | 0.000 000 000 000 000 238 46... |

Increasing the number of digits allowed in a representation reduces the magnitude of possible roundoff errors, but any representation limited to finitely many digits will still cause some degree of roundoff error for uncountably many real numbers. Additional digits used for intermediary steps of a calculation are known as guard digits.

Rounding multiple times can cause error to accumulate. For example, if 9.945309 is rounded to two decimal places (9.95), then rounded again to one decimal place (10.0), the total error is 0.054691. Rounding 9.945309 to one decimal place (9.9) in a single step introduces less error (0.045309). This can occur, for example, when software performs arithmetic in x86 80-bit floating-point and then rounds the result to IEEE 754 binary64 floating-point.

## Floating-point number system

Compared with the fixed-point number system, the floating-point number system is more efficient in representing real numbers so it is widely used in modern computers. While the real numbers $\mathbb {R}$ are infinite and continuous, a floating-point number system F is finite and discrete. Thus, representation error, which leads to roundoff error, occurs under the floating-point number system.

### Notation of floating-point number system

A floating-point number system F is characterized by 4 integers:

- $\beta$ : base or radix
- p : precision
- $[L,U]$ : exponent range, where L is the lower bound and U is the upper bound

Any $x\in F$ has the following form: $x=\pm (\underbrace {d_{0}.d_{1}d_{2}\ldots d_{p-1}} _{\text{significand}})_{\beta }\times \beta ^{\overbrace {E} ^{\text{exponent}}}=\pm d_{0}\times \beta ^{E}+d_{1}\times \beta ^{E-1}+\ldots +d_{p-1}\times \beta ^{E-(p-1)}$ where $d_{i}$ is an integer such that $0\leq d_{i}\leq \beta -1$ for $i=0,1,\ldots ,p-1$ , and E is an integer such that $L\leq E\leq U$ .

### Normalized floating-number system

- A floating-point number system is normalized if the leading digit $d_{0}$ is always nonzero unless the number is zero. Since the significand is $d_{0}.d_{1}d_{2}\ldots d_{p-1}$ , the significand of a nonzero number in a normalized system satisfies $1\leq {\text{significand}}<\beta ^{p}$ . Thus, the normalized form of a nonzero IEEE floating-point number is $\pm 1.bb\ldots b\times 2^{E}$ where $b\in {0,1}$ . In binary, the leading digit is always 1 so it is not written out and is called the implicit bit. This gives an extra bit of precision so that the roundoff error caused by representation error is reduced.
- Since floating-point number system F is finite and discrete, it cannot represent all real numbers which means infinite real numbers can only be approximated by some finite numbers through rounding rules. The floating-point approximation of a given real number x by $fl(x)$ can be denoted.
  - The total number of normalized floating-point numbers is $2(\beta -1)\beta ^{p-1}(U-L+1)+1,$ where
    - 2 counts choice of sign, being positive or negative
    - $(\beta -1)$ counts choice of the leading digit
    - $\beta ^{p-1}$ counts remaining significand digits
    - $U-L+1$ counts choice of exponents
    - 1 counts the case when the number is 0 .

### IEEE standard

In the IEEE standard the base is binary, i.e. $\beta =2$ , and normalization is used. The IEEE standard stores the sign, exponent, and significand in separate fields of a floating point word, each of which has a fixed width (number of bits). The two most commonly used levels of precision for floating-point numbers are single precision and double precision.

| Precision | Sign (bits) | Exponent (bits) | Trailing Significand field (bits) |
|---|---|---|---|
| Single | 1 | 8 | 23 |
| Double | 1 | 11 | 52 |

## Machine epsilon

Machine epsilon can be used to measure the level of roundoff error in the floating-point number system. Here are two different definitions.

- The machine epsilon, denoted $\epsilon _{\text{mach}}$ , is the maximum possible absolute relative error in representing a nonzero real number, x in a floating-point number system. $\epsilon _{\text{mach}}=\max _{x}{\frac {|x-\operatorname {fl} (x)|}{|x|}}$
- The machine epsilon, denoted $\epsilon _{\text{mach}}$ , is the smallest number $\epsilon$ such that $\operatorname {fl} (1+\epsilon )>1$ . Thus, $\operatorname {fl} (1+\delta )=\operatorname {fl} (1)=1$ , whenever $|\delta |<\epsilon _{\text{mach}}.$

## Roundoff error under different rounding rules

There are two common rounding rules, round-by-chop and round-to-nearest. The IEEE standard uses round-to-nearest.

- **Round-by-chop**: The base- $\beta$ expansion of x is truncated after the $(p-1)$ -th digit.
  - This rounding rule is biased because it always moves the result toward zero.
- **Round-to-nearest**: $\operatorname {fl} (x)$ is set to the nearest floating-point number to x . When there is a tie, the floating-point number whose last stored digit is even (also, the last digit, in binary form, is equal to 0) is used.
  - For IEEE standard where the base $\beta$ is 2 , this means when there is a tie it is rounded so that the last digit is equal to 0 .
  - This rounding rule is more accurate but more computationally expensive.
  - Rounding so that the last stored digit is even when there is a tie ensures that it is not rounded up or down systematically. This is to try to avoid the possibility of an unwanted slow drift in long calculations due simply to a biased rounding.

The following example illustrates the level of roundoff error under the two rounding rules. The rounding rule, round-to-nearest, leads to less roundoff error in general.

| x | Round-by-chop | Roundoff Error | Round-to-nearest | Roundoff Error |
|---|---|---|---|---|
| 1.649 | 1.6 | 0.049 | 1.6 | 0.049 |
| 1.650 | 1.6 | 0.050 | 1.6 | 0.050 |
| 1.651 | 1.6 | 0.051 | 1.7 | −0.049 |
| 1.699 | 1.6 | 0.099 | 1.7 | −0.001 |
| 1.749 | 1.7 | 0.049 | 1.7 | 0.049 |
| 1.750 | 1.7 | 0.050 | 1.8 | −0.050 |

### Calculating roundoff error in IEEE standard

Suppose the usage of round-to-nearest and IEEE double precision.

Example: the decimal number $(9.4)_{10}=(1001.{\overline {0110}})_{2}$ can be rearranged into $+1.\underbrace {0010110011001100110011001100110011001100110011001100} _{\text{52 bits}}110\ldots \times 2^{3}$ Since the 53rd bit to the right of the binary point is a 1 and is followed by other nonzero bits, the round-to-nearest rule requires rounding up, that is, add 1 bit to the 52nd bit. Thus, the normalized floating-point representation in IEEE standard of 9.4 is $\operatorname {fl} (9.4)=1.0010110011001100110011001100110011001100110011001101\times 2^{3}.$

Now, the roundoff error can be calculated when representing $9.4$ with $\operatorname {fl} (9.4)$ . This representation is derived by discarding the infinite tail $0.{\overline {1100}}\times 2^{-52}\times 2^{3}=0.{\overline {0110}}\times 2^{-51}\times 2^{3}=0.4\times 2^{-48}$ from the right tail and then added $1\times 2^{-52}\times 2^{3}=2^{-49}$ in the rounding step. Then $\operatorname {fl} (9.4)=9.4-0.4\times 2^{-48}+2^{-49}=9.4+(0.2)_{10}\times 2^{-49}.$ Thus, the roundoff error is $(0.2\times 2^{-49})_{10}$ .

### Measuring roundoff error by using machine epsilon

The machine epsilon $\epsilon _{\text{mach}}$ can be used to measure the level of roundoff error when using the two rounding rules above. Below are the formulas and corresponding proof. The first definition of machine epsilon is used here.

#### Theorem

1. Round-by-chop: $\epsilon _{\text{mach}}=\beta ^{1-p}$
2. Round-to-nearest: $\epsilon _{\text{mach}}={\frac {1}{2}}\beta ^{1-p}$

#### Proof

Let $x=d_{0}.d_{1}d_{2}\ldots d_{p-1}d_{p}\ldots \times \beta ^{n}\in \mathbb {R}$ where $n\in [L,U]$ , and let $\operatorname {fl} (x)$ be the floating-point representation of x . Since round-by-chop is being used, it is ${\begin{aligned}{\frac {|x-\operatorname {fl} (x)|}{|x|}}&={\frac {|d_{0}.d_{1}d_{2}\ldots d_{p-1}d_{p}d_{p+1}\ldots \times \beta ^{n}-d_{0}.d_{1}d_{2}\ldots d_{p-1}\times \beta ^{n}|}{|d_{0}.d_{1}d_{2}\ldots \times \beta ^{n}|}}\\&={\frac {|d_{p}.d_{p+1}\ldots \times \beta ^{n-p}|}{|d_{0}.d_{1}d_{2}\ldots \times \beta ^{n}|}}\\&={\frac {|d_{p}.d_{p+1}d_{p+2}\ldots |}{|d_{0}.d_{1}d_{2}\ldots |}}\times \beta ^{-p}\end{aligned}}$ In order to determine the maximum of this quantity, there is a need to find the maximum of the numerator and the minimum of the denominator. Since $d_{0}\neq 0$ (normalized system), the minimum value of the denominator is 1 . The numerator is bounded above by $(\beta -1).(\beta -1){\overline {(\beta -1)}}=\beta$ . Thus, ${\frac {|x-fl(x)|}{|x|}}\leq {\frac {\beta }{1}}\times \beta ^{-p}=\beta ^{1-p}.$ Therefore, $\epsilon =\beta ^{1-p}$ for round-by-chop. The proof for round-to-nearest is similar.

- Note that the first definition of machine epsilon is not quite equivalent to the second definition when using the round-to-nearest rule but it is equivalent for round-by-chop.

## Roundoff error caused by floating-point arithmetic

Even if some numbers can be represented exactly by floating-point numbers and such numbers are called **machine numbers**, performing floating-point arithmetic may lead to roundoff error in the final result.

### Addition

Machine addition consists of lining up the decimal points of the two numbers to be added, adding them, and then storing the result again as a floating-point number. The addition itself can be done in higher precision but the result must be rounded back to the specified precision, which may lead to roundoff error.

- For example, adding 1 to $2^{-53}$ in IEEE double precision as follows, ${\begin{aligned}1.00\ldots 0\times 2^{0}+1.00\ldots 0\times 2^{-53}&=1.\underbrace {00\ldots 0} _{\text{52 bits}}\times 2^{0}+0.\underbrace {00\ldots 0} _{\text{52 bits}}1\times 2^{0}\\&=1.\underbrace {00\ldots 0} _{\text{52 bits}}1\times 2^{0}.\end{aligned}}$ This is saved as $1.\underbrace {00\ldots 0} _{\text{52 bits}}\times 2^{0}$ since round-to-nearest is used in IEEE standard. Therefore, $1+2^{-53}$ is equal to 1 in IEEE double precision and the roundoff error is $2^{-53}$ .

This example shows that roundoff error can be introduced when adding a large number and a small number. The shifting of the decimal points in the significands to make the exponents match causes the loss of some of the less significant digits. The loss of precision may be described as **absorption**.

Note that the addition of two floating-point numbers can produce roundoff error when their sum is an order of magnitude greater than that of the larger of the two.

- For example, consider a normalized floating-point number system with base $10$ and precision 2 . Then $fl(62)=6.2\times 10^{1}$ and $fl(41)=4.1\times 10^{1}$ . Note that $62+41=103$ but $fl(103)=1.0\times 10^{2}$ . There is a roundoff error of $103-fl(103)=3$ .

This kind of error can occur alongside an absorption error in a single operation.

### Multiplication

In general, the product of two p-digit significands contains up to 2p digits, so the result might not fit in the significand. Thus roundoff error will be involved in the result.

- For example, consider a normalized floating-point number system with the base $\beta =10$ and the significand digits are at most 2 . Then $fl(77)=7.7\times 10^{1}$ and $fl(88)=8.8\times 10^{1}$ . Note that $77\times 88=6776$ but $fl(6776)=6.7\times 10^{3}$ since there at most 2 significand digits. The roundoff error would be $6776-fl(6776)=6776-6.7\times 10^{3}=76$ .

### Division

In general, the quotient of 2p-digit significands may contain more than p-digits.Thus roundoff error will be involved in the result.

- For example, if the normalized floating-point number system above is still being used, then $1/3=0.333\ldots$ but $fl(1/3)=fl(0.333\ldots )=3.3\times 10^{-1}$ . So, the tail $0.333\ldots -3.3\times 10^{-1}=0.00333\ldots$ is cut off.

### Subtraction

Absorption also applies to subtraction.

- For example, subtracting $2^{-60}$ from 1 in IEEE double precision as follows, ${\begin{aligned}1.00\ldots 0\times 2^{0}-1.00\ldots 0\times 2^{-60}&=\underbrace {1.00\ldots 0} _{\text{60 bits}}\times 2^{0}-\underbrace {0.00\ldots 01} _{\text{60 bits}}\times 2^{0}\\&=\underbrace {0.11\ldots 1} _{\text{60 bits}}\times 2^{0}.\end{aligned}}$ This is saved as $\underbrace {1.00\ldots 0} _{\text{53 bits}}\times 2^{0}$ since round-to-nearest is used in IEEE standard. Therefore, $1-2^{-60}$ is equal to 1 in IEEE double precision and the roundoff error is $-2^{-60}$ .

The subtracting of two nearly equal numbers is called **subtractive cancellation**. When the leading digits are cancelled, the result may be too small to be represented exactly and it will just be represented as 0 .

- For example, let $|\epsilon |<\epsilon _{\text{mach}}$ and the second definition of machine epsilon is used here. What is the solution to $(1+\epsilon )-(1-\epsilon )$ ? It is known that $1+\epsilon$ and $1-\epsilon$ are nearly equal numbers, and $(1+\epsilon )-(1-\epsilon )=1+\epsilon -1+\epsilon =2\epsilon$ . However, in the floating-point number system, $fl((1+\epsilon )-(1-\epsilon ))=fl(1+\epsilon )-fl(1-\epsilon )=1-1=0$ . Although $2\epsilon$ is easily big enough to be represented, both instances of $\epsilon$ have been rounded away giving 0 .

Even with a somewhat larger $\epsilon$ , the result is still significantly unreliable in typical cases. There is not much faith in the accuracy of the value because the most uncertainty in any floating-point number is the digits on the far right.

- For example, $1.99999\times 10^{2}-1.99998\times 10^{2}=0.00001\times 10^{2}=1\times 10^{-5}\times 10^{2}=1\times 10^{-3}$ . The result $1\times 10^{-3}$ is clearly representable, but there is not much faith in it.

This is closely related to the phenomenon of catastrophic cancellation, in which the two numbers are *known* to be approximations.

## Accumulation of roundoff error

Errors can be magnified or accumulated when a sequence of calculations is applied on an initial input with roundoff error due to inexact representation.

### Unstable algorithms

An algorithm or numerical process is called **stable** if small changes in the input only produce small changes in the output, and **unstable** if large changes in the output are produced. For example, the computation of $f(x)={\sqrt {1+x}}-1$ using the "obvious" method is unstable near $x=0$ due to the large error introduced in subtracting two similar quantities, whereas the equivalent expression $\textstyle {f(x)={\frac {x}{{\sqrt {1+x}}+1}}}$ is stable.

### Ill-conditioned problems

Even if a stable algorithm is used, the solution to a problem may still be inaccurate due to the accumulation of roundoff error when the problem itself is **ill-conditioned**.

The condition number of a problem is the ratio of the relative change in the solution to the relative change in the input. A problem is **well-conditioned** if small relative changes in input result in small relative changes in the solution. Otherwise, the problem is **ill-conditioned**. In other words, a problem is **ill-conditioned** if its conditions number is "much larger" than 1.

The condition number is introduced as a measure of the roundoff errors that can result when solving ill-conditioned problems.
