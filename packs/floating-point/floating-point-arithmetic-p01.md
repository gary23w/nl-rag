---
title: "Floating-point arithmetic (part 1/2)"
source: https://en.wikipedia.org/wiki/Floating-point_arithmetic
domain: floating-point
license: CC-BY-SA-4.0 / CC-BY-3.0 (floating-point-gui.de)
tags: floating point, ieee 754, rounding error, double precision, machine epsilon
fetched: 2026-07-02
part: 1/2
---

# Floating-point arithmetic

In computing, **floating-point arithmetic** (**FP**) is arithmetic on subsets of real numbers formed by a *significand* (a signed sequence of a fixed number of digits in some base) multiplied by an integer power of that base. Numbers of this form are called **floating-point numbers**.

For example, the number 2469/200 is a floating-point number in base ten with five digits: $2469/200=12.345=\!\underbrace {12345} _{\text{significand}}\!\times \!\underbrace {10} _{\text{base}}\!\!\!\!\!\!\!\overbrace {{}^{-3}} ^{\text{exponent}}$ However, 7716/625 = 12.3456 is not a floating-point number in base ten with five digits—it needs six digits. The nearest floating-point number with only five digits is 12.346. And 1/3 = 0.3333… is not a floating-point number in base ten with any finite number of digits. In practice, most floating-point systems use base two, though base ten (decimal floating point) is also common.

Floating-point arithmetic operations, such as addition and division, approximate the corresponding real number arithmetic operations by rounding any result that is not a floating-point number itself to a nearby floating-point number. For example, in a floating-point arithmetic with five base-ten digits, the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

The term *floating point* refers to the fact that the number's radix point can "float" anywhere to the left, right, or between the significant digits of the number. This position is indicated by the exponent, so floating point can be considered a form of scientific notation.

A floating-point system can be used to represent, with a fixed number of digits, numbers of very different orders of magnitude — such as the number of meters between galaxies or between protons in an atom. For this reason, floating-point arithmetic is often used to allow very small and very large real numbers that require fast processing times. The result of this dynamic range is that the numbers that can be represented are not uniformly spaced; the difference between two consecutive representable numbers varies with their exponent.

Over the years, a variety of floating-point representations have been used in computers. In 1985, the IEEE 754 Standard for Floating-Point Arithmetic was established, and since the 1990s, the most commonly encountered representations are those defined by the IEEE.

The speed of floating-point operations, commonly measured in terms of FLOPS, is an important characteristic of a computer system, especially for applications that involve intensive mathematical calculations.

Floating-point numbers can be computed using software implementations (softfloat) or hardware implementations (hardfloat). Floating-point units (FPUs, colloquially math coprocessors) are specially designed to carry out operations on floating-point numbers and are part of most computer systems. When FPUs are not available, software implementations can be used instead.


## Overview

### Floating-point numbers

A number representation specifies some way of encoding a number, usually as a string of digits.

There are several mechanisms by which strings of digits can represent numbers. In standard mathematical notation, the digit string can be of any length, and the location of the radix point is indicated by placing an explicit "point" character (dot or comma) there. If the radix point is not specified, then the string implicitly represents an integer and the unstated radix point would be off the right-hand end of the string, next to the least significant digit. In fixed-point systems, a position in the string is specified for the radix point. So a fixed-point scheme might use a string of 8 decimal digits with the decimal point in the middle, whereby "00012345" would represent 0001.2345.

In scientific notation, the given number is scaled by a power of 10, so that it lies within a specific range—typically between 1 and 10, with the radix point appearing immediately after the first digit. As a power of ten, the scaling factor is then indicated separately at the end of the number. For example, the orbital period of Jupiter's moon Io is 152,853.5047 seconds, a value that would be represented in standard-form scientific notation as 1.528535047×105 seconds.

Floating-point representation is similar in concept to scientific notation. Logically, a floating-point number consists of:

- A signed (meaning positive or negative) digit string of a given length in a given radix (or base). This digit string is referred to as the *significand*, *mantissa*, or *coefficient*. The length of the significand determines the *precision* to which numbers can be represented. The radix point position is assumed always to be somewhere within the significand—often just after or just before the most significant digit, or to the right of the rightmost (least significant) digit. This article generally follows the convention that the radix point is set just after the most significant (leftmost) digit.
- A signed integer exponent (also referred to as the *characteristic*, or *scale*), which modifies the magnitude of the number.

To derive the value of the floating-point number, the *significand* is multiplied by the *base* raised to the power of the *exponent*, equivalent to shifting the radix point from its implied position by a number of places equal to the value of the exponent—to the right if the exponent is positive or to the left if the exponent is negative.

Using base-10 (the familiar decimal notation) as an example, the number 152,853.5047, which has ten decimal digits of precision, is represented as the significand 1528535047 together with 5 as the exponent. To determine the actual value, a decimal point is placed after the first digit of the significand and the result is multiplied by 105 to give 1.528535047×105, or 152,853.5047. In storing such a number, the base (10) need not be stored, since it will be the same for the entire range of supported numbers, and can thus be inferred.

Symbolically, this final value is: ${\frac {s}{b^{\,p-1}}}\times b^{e},$

where s is the significand (ignoring any implied decimal point), p is the precision (the number of digits in the significand), b is the base (in our example, this is the number *ten*), and e is the exponent.

Historically, several number bases have been used for representing floating-point numbers, with base two (binary) being the most common, followed by base ten (decimal floating point), and other less common varieties, such as base sixteen (hexadecimal floating point), base eight (octal floating point), base four (quaternary floating point), base three (balanced ternary floating point) and even base 256 and base 65,536.

A floating-point number is a rational number, because it can be represented as one integer divided by another; for example 1.45×103 is (145/100)×1000 or 145,000/100. The base determines the fractions that can be represented; for instance, 1/5 cannot be represented exactly as a floating-point number using a binary base, but 1/5 can be represented exactly using a decimal base (0.2, or 2×10−1). However, 1/3 cannot be represented exactly by either binary (0.010101...) or decimal (0.333...), but in base 3, it is trivial (0.1 or 1×3−1) . The occasions on which infinite expansions occur depend on the base and its prime factors.

The way in which the significand (including its sign) and exponent are stored in a computer is implementation-dependent. The common IEEE formats are described in detail later and elsewhere, but as an example, in the binary single-precision (32-bit) floating-point representation, $p=24$ , and so the significand is a string of 24 bits. For instance, the number π's first 33 bits are: $11001001\ 00001111\ 1101101{\underline {0}}\ 10100010\ 0.$

In this binary expansion, let us denote the positions from 0 (leftmost bit, or most significant bit) to 32 (rightmost bit). The 24-bit significand will stop at position 23, shown as the underlined bit 0 above. The next bit, at position 24, is called the *round bit* or *rounding bit*. It is used to round the 33-bit approximation to the nearest 24-bit number (there are specific rules for halfway values, which is not the case here). This bit, which is 1 in this example, is added to the integer formed by the leftmost 24 bits, yielding: $11001001\ 00001111\ 1101101{\underline {1}}.$

When this is stored in memory using the IEEE 754 encoding, this becomes the significand s. The significand is assumed to have a binary point to the right of the leftmost bit. So, the binary representation of π is calculated from left-to-right as follows: ${\begin{aligned}&{\biggl (}\sum _{n=0}^{p-1}{\text{bit}}_{n}\times 2^{-n}{\biggr )}\times 2^{e}\\&\qquad {}=\left(1\times 2^{-0}+1\times 2^{-1}+0\times 2^{-2}+0\times 2^{-3}+\cdots +1\times 2^{-23}\right)\times 2^{1}\\[2mu]&\qquad {}\approx 1.57079637\times 2\\[3mu]&\qquad {}\approx 3.1415927\end{aligned}}$

where p is the precision (24 in this example), n is the position of the bit of the significand from the left (starting at 0 and finishing at 23 here) and e is the exponent (1 in this example).

It can be required that the most significant digit of the significand of a non-zero number be non-zero (except when the corresponding exponent would be smaller than the minimum one). This process is called *normalization*. For binary formats (which uses only the digits 0 and 1), this non-zero digit is necessarily 1. Therefore, it does not need to be represented in memory, allowing the format to have one more bit of precision. This rule is variously called the *leading bit convention*, the *implicit bit convention*, the *hidden bit convention*, or the *assumed bit convention*.

### Alternatives to floating-point numbers

The floating-point representation is by far the most common way of representing in computers an approximation to real numbers. However, there are alternatives:

- Fixed-point representation uses integer hardware operations controlled by a software implementation of a specific convention about the location of the binary or decimal point, for example, 6 bits or digits from the right. The hardware to manipulate these representations is less costly than floating point, and it can be used to perform normal integer operations, too. Binary fixed point is usually used in special-purpose applications on embedded processors that can only do integer arithmetic, but decimal fixed point is common in commercial applications.
- Logarithmic number systems (LNSs) represent a real number by the logarithm of its absolute value and a sign bit. The value distribution is similar to floating point, but the value-to-representation curve (*i.e.*, the graph of the logarithm function) is smooth (except at 0). Conversely to floating-point arithmetic, in a logarithmic number system multiplication, division and exponentiation are simple to implement, but addition and subtraction are complex. The (symmetric) level-index arithmetic (LI and SLI) of Charles Clenshaw, Frank Olver and Peter Turner is a scheme based on a generalized logarithm representation.
- Tapered floating-point representation, used in Unum formats, including Posit.
- Some simple rational numbers (*e.g.*, 1/3 and 1/10) cannot be represented exactly in binary floating point, no matter what the precision is. Using a different radix allows one to represent some of them (*e.g.*, 1/10 in decimal floating point), but the possibilities remain limited. Software packages that perform rational arithmetic represent numbers as fractions with integral numerator and denominator, and can therefore represent any rational number exactly. Such packages generally need to use "bignum" arithmetic for the individual integers.
- Interval arithmetic allows one to represent numbers as intervals and obtain guaranteed bounds on results. It is generally based on other arithmetics, in particular floating point.
- Computer algebra systems such as Mathematica, Maxima, and Maple can often handle irrational numbers like $\pi$ or ${\sqrt {3}}$ in a completely "formal" way (symbolic computation), without dealing with a specific encoding of the significand. Such a program can evaluate expressions like " $\sin(3\pi )$ " exactly, because it is programmed to process the underlying mathematics directly, instead of using approximate values for each intermediate calculation.


## History

In 1914, the Spanish engineer Leonardo Torres Quevedo published *Essays on Automatics*, where he designed a special-purpose electromechanical calculator based on Charles Babbage's analytical engine and described a way to store floating-point numbers in a consistent manner. He stated that numbers will be stored in exponential format as $n\times 10^{m}$ , and offered three rules by which consistent manipulation of floating-point numbers by machines could be implemented. For Torres, "*n* will always be the same number of digits (e.g. six), the first digit of *n* will be of order of tenths, the second of hundredths, etc, and one will write each quantity in the form: *n*; *m*." The format he proposed shows the need for a fixed-sized significand as is presently used for floating-point data, fixing the location of the decimal point in the significand so that each representation was unique, and how to format such numbers by specifying a syntax to be used that could be entered through a typewriter, as was the case of his Electromechanical Arithmometer in 1920.

In 1938, Konrad Zuse of Berlin completed the Z1, the first binary, programmable mechanical computer; it uses a 24-bit binary floating-point number representation with a 7-bit signed exponent, a 17-bit significand (including one implicit bit), and a sign bit. The more reliable relay-based Z3, completed in 1941, has representations for both positive and negative infinities; in particular, it implements defined operations with infinity, such as division by infinity, where $1/\infty =0$ , and it stops on undefined operations, such as $0\times \infty$ .

Zuse also proposed, but did not complete, carefully rounded floating-point arithmetic that includes $\pm \infty$ and NaN representations, anticipating features of the IEEE Standard by four decades. In contrast, von Neumann recommended against floating-point numbers for the 1951 IAS machine, arguing that fixed-point arithmetic is preferable.

The first *commercial* computer with floating-point hardware was Zuse's Z4 computer, designed in 1942–1945. In 1946, Bell Laboratories introduced the Model V, which implemented decimal floating-point numbers.

The Pilot ACE has binary floating-point arithmetic, and it became operational in 1950 at National Physical Laboratory, UK. Thirty-three were later sold commercially as the English Electric DEUCE. The arithmetic is actually implemented in software, but with a one megahertz clock rate, the speed of floating-point and fixed-point operations in this machine were initially faster than those of many competing computers.

The mass-produced IBM 704 followed in 1954; it introduced the use of a biased exponent. For many decades after that, floating-point hardware was typically an optional feature, and computers that had it were said to be "scientific computers", or to have "scientific computation" (SC) capability (see also Extensions for Scientific Computation (XSC)). It was not until the launch of the Intel i486 in 1989 that *general-purpose* personal computers had floating-point capability in hardware as a standard feature.

The UNIVAC 1100/2200 series, introduced in 1962, supported two floating-point representations:

- *Single precision*: 36 bits, organized as a 1-bit sign, an 8-bit exponent, and a 27-bit significand.
- *Double precision*: 72 bits, organized as a 1-bit sign, an 11-bit exponent, and a 60-bit significand.

The IBM 7094, also introduced in 1962, supported single-precision and double-precision representations, but with no relation to the UNIVAC's representations. Indeed, in 1964, IBM introduced hexadecimal floating-point representations in its System/360 mainframes; these same representations are still available for use in modern z/Architecture systems. In 1998, IBM implemented IEEE-compatible binary floating-point arithmetic in its mainframes; in 2005, IBM also added IEEE-compatible decimal floating-point arithmetic.

Initially, computers used many different representations for floating-point numbers. The lack of standardization at the mainframe level was an ongoing problem by the early 1970s for those writing and maintaining higher-level source code; these manufacturer floating-point standards differed in the word sizes, the representations, and the rounding behavior and general accuracy of operations. Floating-point compatibility across multiple computing systems was in desperate need of standardization by the early 1980s, leading to the creation of the IEEE 754 standard once the 32-bit (or 64-bit) word had become commonplace. This standard was significantly based on a proposal from Intel, which was designing the i8087 numerical coprocessor; Motorola, which was designing the 68000 around the same time, gave significant input as well.

In 1989, mathematician and computer scientist William Kahan was honored with the Turing Award for being the primary architect behind this proposal; he was aided by his student Jerome Coonen and a visiting professor, Harold Stone.

Among the x86 (more specifically i8087) innovations are these:

- A precisely specified floating-point representation at the bit-string level, so that all compliant computers interpret bit patterns the same way. This makes it possible to accurately and efficiently transfer floating-point numbers from one computer to another (after accounting for endianness).
- A precisely specified behavior for the arithmetic operations: A result is required to be produced as if infinitely precise arithmetic were used to yield a value that is then rounded according to specific rules. This means that a compliant computer program would always produce the same result when given a particular input, thus mitigating the almost mystical reputation that floating-point computation had developed for its hitherto seemingly non-deterministic behavior.
- The ability of exceptional conditions (overflow, divide by zero, etc.) to propagate through a computation in a benign manner and then be handled by the software in a controlled fashion.

These features would be inherited into IEEE 754-1985 (with the exception of the encoding of special values and exceptions), though the extended internal precision of x87 means it requires explicit rounding of exact results directly to the destination precision in order to match standard IEEE 754 results. However, the behavior may not be the same as a rounding to the destination format due to a possible wider exponent range of the extended format.


## Range of floating-point numbers

A floating-point number consists of two fixed-point components, whose range depends exclusively on the number of bits or digits in their representation. Whereas components linearly depend on their range, the floating-point range linearly depends on the significand range and exponentially on the range of exponent component, which attaches outstandingly wider range to the number.

On a typical computer system, a *double-precision* (64-bit) binary floating-point number has a coefficient of 53 bits (including 1 implied bit), an exponent of 11 bits, and 1 sign bit. Since 210 = 1024, the complete range of the positive normal floating-point numbers in this format is from 2−1022 ≈ 2 × 10−308 to approximately 21024 ≈ 2 × 10308.

The number of normal floating-point numbers in a system (*B*, *P*, *L*, *U*) where

- *B* is the base of the system,
- *P* is the precision of the significand (in base *B*),
- *L* is the smallest exponent of the system,
- *U* is the largest exponent of the system,

is $2\left(B-1\right)\left(B^{P-1}\right)\left(U-L+1\right)$ , or $2\left(B-1\right)\left(B^{P-1}\right)\left(U-L+1\right)+1$ considering the value 0.

There is a smallest positive normal floating-point number,

Underflow level = UFL =

$B^{L}$

,

which has a 1 as the leading digit and 0 for the remaining digits of the significand, and the smallest possible value for the exponent.

There is a largest floating-point number,

Overflow level = OFL =

$\left(1-B^{-P}\right)\left(B^{U+1}\right)$

,

which has *B* − 1 as the value for each digit of the significand and the largest possible value for the exponent.

In addition, there are representable values strictly between −UFL and UFL. Namely, positive and negative zeros, as well as subnormal numbers.


## IEEE 754: floating point in modern computers

The IEEE standardized the computer representation for binary floating-point numbers in IEEE 754 (a.k.a. IEC 60559) in 1985. This first standard is followed by almost all modern machines. It was revised in 2008. IBM mainframes support IBM's own hexadecimal floating point format and IEEE 754-2008 decimal floating point in addition to the IEEE 754 binary format. The Cray T90 series had an IEEE version, but the SV1 still uses Cray floating-point format.

The standard provides for many closely related formats, differing in only a few details. Five of these formats are called *basic formats*, and others are termed *extended precision formats* and *extendable precision format*. Three formats are especially widely used in computer hardware and languages:

- Single precision (binary32), usually used to represent the "float" type in the C language family. This is a binary format that occupies 32 bits (4 bytes) and its significand has a precision of 24 bits (about 7 decimal digits).
- Double precision (binary64), usually used to represent the "double" type in the C language family. This is a binary format that occupies 64 bits (8 bytes) and its significand has a precision of 53 bits (about 16 decimal digits).
- Double extended, also ambiguously called "extended precision" format. This is a binary format that occupies at least 79 bits (80 if the hidden/implicit bit rule is not used) and its significand has a precision of at least 64 bits (about 19 decimal digits). The C99 and C11 standards of the C language family, in their annex F ("IEC 60559 floating-point arithmetic"), recommend such an extended format to be provided as "long double". A format satisfying the minimal requirements (64-bit significand precision, 15-bit exponent, thus fitting on 80 bits) is provided by the x86 architecture. Often on such processors, this format can be used with "long double", though extended precision is not available with MSVC. For alignment purposes, many tools store this 80-bit value in a 96-bit or 128-bit space. On other processors, "long double" may stand for a larger format, such as quadruple precision, or just double precision, if any form of extended precision is not available.

Increasing the precision of the floating-point representation generally reduces the amount of accumulated round-off error caused by intermediate calculations. Other IEEE formats include:

- Decimal64 and decimal128 floating-point formats. These formats (especially decimal128) are pervasive in financial transactions because, along with the decimal32 format, they allow correct decimal rounding.
- Quadruple precision (binary128). This is a binary format that occupies 128 bits (16 bytes) and its significand has a precision of 113 bits (about 34 decimal digits).
- Half precision, also called binary16, a 16-bit floating-point value. It is being used in the NVIDIA Cg graphics language, and in the openEXR standard (where it actually predates the introduction in the IEEE 754 standard).

Any integer with absolute value less than 224 can be exactly represented in the single-precision format, and any integer with absolute value less than 253 can be exactly represented in the double-precision format. Furthermore, a wide range of powers of 2 times such a number can be represented. These properties are sometimes used for purely integer data, to get 53-bit integers on platforms that have double-precision floats but only 32-bit integers.

The standard specifies some special values, and their representation: positive infinity (+∞), negative infinity (−∞), a negative zero (−0) distinct from ordinary ("positive") zero, and "not a number" values (NaNs).

Comparison of floating-point numbers, as defined by the IEEE standard, is a bit different from usual integer comparison. Negative and positive zero compare equal, and every NaN compares unequal to every value, including itself. All finite floating-point numbers are strictly smaller than +∞ and strictly greater than −∞, and they are ordered in the same way as their values (in the set of real numbers).

### Internal representation

Floating-point numbers are typically packed into a computer datum as the sign bit, the exponent field, and a field for the significand, from left to right. For the IEEE 754 binary formats (basic and extended) that have extant hardware implementations, they are apportioned as follows:

| Format | Bits for the encoding |   | Exponent bias | Bits precision | Number of decimal digits |   |   |
|---|---|---|---|---|---|---|---|
| Sign | Exponent | Significand | Total |   |   |   |   |
| Half (binary16) | 1 | 5 | 10 | 16 | 15 | 11 | ~3.3 |
| Single (binary32) | 1 | 8 | 23 | 32 | 127 | 24 | ~7.2 |
| Double (binary64) | 1 | 11 | 52 | 64 | 1023 | 53 | ~15.9 |
| x86 extended | 1 | 15 | 64 | 80 | 16383 | 64 | ~19.2 |
| Quadruple (binary128) | 1 | 15 | 112 | 128 | 16383 | 113 | ~34.0 |
| Octuple (binary256) | 1 | 19 | 236 | 256 | 262143 | 237 | ~71.3 |

While the exponent can be positive or negative, in binary formats it is stored as an unsigned number that has a fixed "bias" added to it. Values of all 0s in this field are reserved for the zeros and subnormal numbers; values of all 1s are reserved for the infinities and NaNs. The exponent range for normal numbers is [−126, 127] for single precision, [−1022, 1023] for double, or [−16382, 16383] for quad. Normal numbers exclude subnormal values, zeros, infinities, and NaNs.

In the IEEE binary interchange formats the leading bit of a normalized significand is not actually stored in the computer datum, since it is always 1. It is called the "hidden" or "implicit" bit. Because of this, the single-precision format actually has a significand with 24 bits of precision, the double-precision format has 53, quad has 113, and octuple has 237.

For example, it was shown above that π, rounded to 24 bits of precision, has:

- sign = 0 ; *e* = 1 ; *s* = 110010010000111111011011 (including the hidden bit)

The sum of the exponent bias (127) and the exponent (1) is 128, so this is represented in the single-precision format as

- 0 10000000 10010010000111111011011 (excluding the hidden bit) = 40490FDB as a hexadecimal number.

An example of a layout for 32-bit floating point is

and the 64-bit ("double") layout is similar.


## Other notable floating-point formats

In addition to the widely used IEEE 754 standard formats, other floating-point formats are used, or have been used, in certain domain-specific areas.

- The Microsoft Binary Format (MBF) was developed for the Microsoft BASIC language products, including Microsoft's first ever product the Altair BASIC (1975), TRS-80 LEVEL II, CP/M's MBASIC, IBM PC 5150's BASICA, MS-DOS's GW-BASIC and QuickBASIC prior to version 4.00. QuickBASIC version 4.00 and 4.50 switched to the IEEE 754-1985 format but can revert to the MBF format using the /MBF command option. MBF was designed and developed on a simulated Intel 8080 by Monte Davidoff, a dormmate of Bill Gates, during spring of 1975 for the MITS Altair 8800. The initial release of July 1975 supported a single-precision (32 bits) format due to cost of the MITS Altair 8800 4-kilobytes memory. In December 1975, the 8-kilobytes version added a double-precision (64 bits) format. A single-precision (40 bits) variant format was adopted for other CPU's, notably the MOS 6502 (Apple II, Commodore PET, Atari), Motorola 6800 (MITS Altair 680) and Motorola 6809 (TRS-80 Color Computer). All Microsoft language products from 1975 through 1987 used the Microsoft Binary Format until Microsoft adopted the IEEE 754 standard format in all its products starting in 1988 to their current releases. MBF consists of the MBF single-precision format (32 bits, "6-digit BASIC"), the MBF extended-precision format (40 bits, "9-digit BASIC"), and the MBF double-precision format (64 bits); each of them is represented with an 8-bit exponent, followed by a sign bit, followed by a significand of respectively 23, 31, and 55 bits.
- The bfloat16 format requires the same amount of memory (16 bits) as the IEEE 754 half-precision format, but allocates 8 bits to the exponent instead of 5, thus providing the same range as a IEEE 754 single-precision number. The tradeoff is a reduced precision, as the trailing significand field is reduced from 10 to 7 bits. This format is mainly used in the training of machine learning models, where range is more valuable than precision. Many machine learning accelerators provide hardware support for this format.
- The TensorFloat-32 format combines the 8 bits of exponent of the bfloat16 with the 10 bits of trailing significand field of half-precision formats, resulting in a size of 19 bits. This format was introduced by Nvidia, which provides hardware support for it in the Tensor Cores of its GPUs based on the Nvidia Ampere architecture. The drawback of this format is its size, which is not a power of 2. However, according to Nvidia, this format should only be used internally by hardware to speed up computations, while inputs and outputs should be stored in the 32-bit single-precision IEEE 754 format.
- The Hopper and CDNA 3 architecture GPUs provide two FP8 formats: one with the same numerical range as half-precision (E5M2) and one with higher precision, but less range (E4M3).
- The Blackwell and CDNA 4 GPU architecture includes support for FP6 (E3M2 and E2M3) and FP4 (E2M1) formats. FP4 is the smallest floating-point format which allows for all IEEE 754 principles (see minifloat).

| Type | Sign | Exponent | Significand | Total bits |
|---|---|---|---|---|
| FP4 | 1 | 2 | 1 | 4 |
| FP6 (E2M3) | 1 | 2 | 3 | 6 |
| FP6 (E3M2) | 1 | 3 | 2 | 6 |
| FP8 (E4M3) | 1 | 4 | 3 | 8 |
| FP8 (E5M2) | 1 | 5 | 2 | 8 |
| Half-precision | 1 | 5 | 10 | 16 |
| bfloat16 | 1 | 8 | 7 | 16 |
| TensorFloat-32 | 1 | 8 | 10 | 19 |
| Single-precision | 1 | 8 | 23 | 32 |
| Double-precision | 1 | 11 | 52 | 64 |
| Quadruple-precision | 1 | 15 | 112 | 128 |
| Octuple-precision | 1 | 19 | 236 | 256 |


## Representable numbers, conversion and rounding

By their nature, all numbers expressed in floating-point format are rational numbers with a terminating expansion in the relevant base (for example, a terminating decimal expansion in base-10, or a terminating binary expansion in base-2). Irrational numbers, such as π or ${\textstyle {\sqrt {2}}}$ , or non-terminating rational numbers, must be approximated. The number of digits (or bits) of precision also limits the set of rational numbers that can be represented exactly. For example, the decimal number 123456789 cannot be exactly represented if only eight decimal digits of precision are available (it would be rounded to one of the two straddling representable values, 12345678 × 101 or 12345679 × 101), the same applies to non-terminating digits (.5 to be rounded to either .55555555 or .55555556).

When a number is represented in some format (such as a character string) which is not a native floating-point representation supported in a computer implementation, then it will require a conversion before it can be used in that implementation. If the number can be represented exactly in the floating-point format then the conversion is exact. If there is not an exact representation then the conversion requires a choice of which floating-point number to use to represent the original value. The representation chosen will have a different value from the original, and the value thus adjusted is called the *rounded value*.

Whether or not a rational number has a terminating expansion depends on the base. For example, in base-10 the number 1/2 has a terminating expansion (0.5) while the number 1/3 does not (0.333...). In base-2 only rationals with denominators that are powers of 2 (such as 1/2 or 3/16) are terminating. Any rational with a denominator that has a prime factor other than 2 will have an infinite binary expansion. This means that numbers that appear to be short and exact when written in decimal format may need to be approximated when converted to binary floating-point. For example, the decimal number 0.1 is not representable in binary floating-point of any finite precision; the exact binary representation would have a "1100" sequence continuing endlessly:

e

= −4;

s

= 1100110011001100110011001100110011...,

where, as previously, *s* is the significand and *e* is the exponent.

When rounded to 24 bits this becomes

e

= −4;

s

= 110011001100110011001101,

which is actually 0.100000001490116119384765625 in decimal.

As a further example, the real number π, represented in binary as an infinite sequence of bits is

11.0010010000111111011010101000100010000101101000110000100011010011...

but is

11.0010010000111111011011

when approximated by rounding to a precision of 24 bits.

In binary single-precision floating-point, this is represented as *s* = 1.10010010000111111011011 with *e* = 1. This has a decimal value of

3.141592

7410125732421875,

whereas a more accurate approximation of the true value of π is

3.14159265358979323846264338327950

...

The result of rounding differs from the true value by about 0.03 parts per million, and matches the decimal representation of π in the first 7 digits. The difference is the discretization error and is limited by the machine epsilon.

The arithmetical difference between two consecutive representable floating-point numbers which have the same exponent is called a unit in the last place (ULP). For example, if there is no representable number lying between the representable numbers 1.45A70C2216 and 1.45A70C2416, the ULP is 2×16−8, or 2−31. For numbers with a base-2 exponent part of 0, i.e. numbers with an absolute value higher than or equal to 1 but lower than 2, an ULP is exactly 2−23 or about 10−7 in single precision, and exactly 2−53 or about 10−16 in double precision. The mandated behavior of IEEE-compliant hardware is that the result be within one-half of a ULP.

### Rounding modes

Rounding is used when the exact result of a floating-point operation (or a conversion to floating-point format) would need more digits than there are digits in the significand. IEEE 754 requires *correct rounding*: that is, the rounded result is as if infinitely precise arithmetic was used to compute the value and then rounded (although in implementation only three extra bits are needed to ensure this). There are several different rounding schemes (or *rounding modes*). Historically, truncation was the typical approach. Since the introduction of IEEE 754, the default method (*round to nearest, ties to even*, sometimes called Banker's Rounding) is more commonly used. This method rounds the ideal (infinitely precise) result of an arithmetic operation to the nearest representable value, and gives that representation as the result. In the case of a tie, the value that would make the significand end in an even digit is chosen. The IEEE 754 standard requires the same rounding to be applied to all fundamental algebraic operations, including square root and conversions, when there is a numeric (non-NaN) result. It means that the results of IEEE 754 operations are completely determined in all bits of the result, except for the representation of NaNs. ("Library" functions such as cosine and log are not mandated.)

Alternative rounding options are also available. IEEE 754 specifies the following rounding modes:

- round to nearest, where ties round to the nearest even digit in the required position (the default and by far the most common mode)
- round to nearest, where ties round away from zero (optional for binary floating-point and commonly used in decimal)
- round up (toward +∞; negative results thus round toward zero)
- round down (toward −∞; negative results thus round away from zero)
- round toward zero (truncation; it is similar to the common behavior of float-to-integer conversions, which convert −3.9 to −3 and 3.9 to 3)

Alternative modes are useful when the amount of error being introduced must be bounded. Applications that require a bounded error are multi-precision floating-point, and interval arithmetic. The alternative rounding modes are also useful in diagnosing numerical instability: if the results of a subroutine vary substantially between rounding to + and − infinity then it is likely numerically unstable and affected by round-off error.

### Binary-to-decimal conversion with minimal number of digits

Converting a double-precision binary floating-point number to a decimal string is a common operation, but an algorithm producing results that are both accurate and minimal did not appear in print until 1990, with Steele and White's Dragon4. Some of the improvements since then include:

- David M. Gay's *dtoa.c*, a practical open-source implementation of many ideas in Dragon4.
- Grisu3, with a 4× speedup as it removes the use of bignums. Must be used with a fallback, as it fails for ~0.5% of cases.
- Errol3, an always-succeeding algorithm similar to, but slower than, Grisu3. Apparently not as good as an early-terminating Grisu with fallback.
- Ryū, an always-succeeding algorithm that is faster and simpler than Grisu3.
- Schubfach, an always-succeeding algorithm that is based on a similar idea to Ryū, developed almost simultaneously and independently. Performs better than Ryū and Grisu3 in certain benchmarks.

Many modern language runtimes use Grisu3 with a Dragon4 fallback.

### Decimal-to-binary conversion

The problem of parsing a decimal string into a binary FP representation is complex, with an accurate parser not appearing until Clinger's 1990 work (implemented in dtoa.c). Further work has likewise progressed in the direction of faster parsing.


## Floating-point operations

For ease of presentation and understanding, decimal radix with 7 digit precision will be used in the examples, as in the IEEE 754 *decimal32* format. The fundamental principles are the same in any radix or precision, except that normalization is optional (it does not affect the numerical value of the result). Here, *s* denotes the significand and *e* denotes the exponent.

### Addition and subtraction

A simple method to add floating-point numbers is to first represent them with the same exponent. In the example below, the second number (with the smaller exponent) is shifted right by three digits, and one then proceeds with the usual addition method:

```
  123456.7 = 1.234567 × 10^5
  101.7654 = 1.017654 × 10^2 = 0.001017654 × 10^5
```

```
  Hence:
  123456.7 + 101.7654 = (1.234567 × 10^5) + (1.017654 × 10^2)
                      = (1.234567 × 10^5) + (0.001017654 × 10^5)
                      = (1.234567 + 0.001017654) × 10^5
                      =  1.235584654 × 10^5
```

In detail:

```
  e=5;  s=1.234567     (123456.7)
+ e=2;  s=1.017654     (101.7654)
```

```
  e=5;  s=1.234567
+ e=5;  s=0.001017654  (after shifting)
--------------------
  e=5;  s=1.235584654  (true sum: 123558.4654)
```

This is the true result, the exact sum of the operands. It will be rounded to seven digits and then normalized if necessary. The final result is

```
  e=5;  s=1.235585    (final sum: 123558.5)
```

The lowest three digits of the second operand (654) are essentially lost. This is round-off error. In extreme cases, the sum of two non-zero numbers may be equal to one of them:

```
  e=5;  s=1.234567
+ e=−3; s=9.876543
```

```
  e=5;  s=1.234567
+ e=5;  s=0.00000009876543 (after shifting)
----------------------
  e=5;  s=1.23456709876543 (true sum)
  e=5;  s=1.234567         (after rounding and normalization)
```

In the above conceptual examples it would appear that a large number of extra digits would need to be provided by the adder to ensure correct rounding; however, for binary addition or subtraction using careful implementation techniques only a *guard* bit, a *rounding* bit and one extra *sticky* bit need to be carried beyond the precision of the operands.

Another problem of loss of significance occurs when *approximations* to two nearly equal numbers are subtracted. In the following example *e* = 5; *s* = 1.234571 and *e* = 5; *s* = 1.234567 are approximations to the rationals 123457.1467 and 123456.659.

```
  e=5;  s=1.234571
− e=5;  s=1.234567
----------------
  e=5;  s=0.000004
  e=−1; s=4.000000 (after rounding and normalization)
```

The floating-point difference is computed exactly because the numbers are close—the Sterbenz lemma guarantees this, even in case of underflow when gradual underflow is supported. Despite this, the difference of the original numbers is *e* = −1; *s* = 4.877000, which differs more than 20% from the difference *e* = −1; *s* = 4.000000 of the approximations. In extreme cases, all significant digits of precision can be lost. This *cancellation* illustrates the danger in assuming that all of the digits of a computed result are meaningful. Dealing with the consequences of these errors is a topic in numerical analysis; see also Accuracy problems.

### Multiplication and division

To multiply, the significands are multiplied while the exponents are added, and the result is rounded and normalized.

```
  e=3;  s=4.734612
× e=5;  s=5.417242
-----------------------
  e=8;  s=25.648538980104 (true product)
  e=8;  s=25.64854        (after rounding)
  e=9;  s=2.564854        (after normalization)
```

Similarly, division is accomplished by subtracting the divisor's exponent from the dividend's exponent, and dividing the dividend's significand by the divisor's significand.

There are no cancellation or absorption problems with multiplication or division, though small errors may accumulate as operations are performed in succession. In practice, the way these operations are carried out in digital logic can be quite complex (see Booth's multiplication algorithm and Division algorithm).

### Literal syntax

Literals for floating-point numbers depend on languages. They typically use `e` or `E` to denote scientific notation. The C programming language and the IEEE 754 standard also define a hexadecimal literal syntax with a base-2 exponent instead of 10. In languages like C, when the decimal exponent is omitted, a decimal point is needed to differentiate them from integers. Other languages do not have an integer type (such as JavaScript), or allow overloading of numeric types (such as Haskell). In these cases, digit strings such as `123` may also be floating-point literals.

Examples of floating-point literals are:

- `99.9`
- `-5000.12`
- `6.02e23`
- `-3e-45`
- `0x1.fffffep+127` in C and IEEE 754
