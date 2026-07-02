---
title: "IEEE 754"
source: https://en.wikipedia.org/wiki/IEEE_754
domain: floating-point
license: CC-BY-SA-4.0 / CC-BY-3.0 (floating-point-gui.de)
tags: floating point, ieee 754, rounding error, double precision, machine epsilon
fetched: 2026-07-02
---

# IEEE 754

The **IEEE Standard for Floating-Point Arithmetic** (**IEEE 754**) is a technical standard for floating-point arithmetic originally established in 1985 by the Institute of Electrical and Electronics Engineers (IEEE). The standard addressed many problems found in the diverse floating-point implementations that made them difficult to use reliably and portably. Many hardware floating-point units use the IEEE 754 standard.

The standard defines:

- *arithmetic formats:* sets of binary and decimal floating-point data, which consist of finite numbers (including signed zeros and subnormal numbers), infinities, and special "not a number" values (NaNs)
- *interchange formats:* encodings (bit strings) that may be used to exchange floating-point data in an efficient and compact form
- *rounding rules:* properties to be satisfied when rounding numbers during arithmetic and conversions
- *operations:* arithmetic and other operations (such as trigonometric functions) on arithmetic formats
- *exception handling:* indications of exceptional conditions (such as division by zero, overflow, etc.)

IEEE 754-2008, published in August 2008, includes nearly all of the original IEEE 754-1985 standard, plus the IEEE 854-1987 (Radix-Independent Floating-Point Arithmetic) standard. The current version, IEEE 754-2019, was published in July 2019. It is a minor revision of the previous version, incorporating mainly clarifications, defect fixes and new recommended operations.

## History

| Year | Official Standard |
|---|---|
| 1982 | IEC 559:1982 |
| 1985 | IEEE 754-1985 |
| 1987 | IEEE 854-1987 |
| 1989 | IEC 559:1989 |
| 2008 | IEEE 754-2008 |
| 2011 | ISO/IEC/IEEE 60559:2011 |
| 2019 | IEEE 754-2019 |
| 2020 | ISO/IEC 60559:2020 |
| 2029 | TBA |

The need for a floating-point standard arose from chaos in the business and scientific computing industry in the 1960s and 1970s. IBM used a hexadecimal floating-point format with seven bits always used for the exponent regardless of precision. CDC and Cray computers used ones' complement representation, which admits a value of +0 and −0. CDC 60-bit computers did not have full 60-bit adders, so integer arithmetic was limited to 48 bits of precision from the floating-point unit. Exception processing from divide-by-zero was different on different computers. Moving data between systems and even repeating the same calculations on different systems was often difficult.

The first IEEE standard for floating-point arithmetic, IEEE 754-1985, was published in 1985. It covered only binary floating-point arithmetic.

A new version, IEEE 754-2008, was published in August 2008, following a seven-year revision process, chaired by Dan Zuras and edited by Mike Cowlishaw. It replaced both IEEE 754-1985 (Binary Floating-Point Arithmetic) and IEEE 854-1987 (Radix-Independent Floating-Point Arithmetic) standards. The binary formats in the original standard are included in this new standard along with three new basic formats, one binary and two decimal. To conform to the current standard, an implementation must implement at least one of the basic formats as both an arithmetic format and an interchange format.

The international standard **ISO/IEC/IEEE 60559:2011** (with content identical to IEEE 754-2008) has been approved for adoption through ISO/IEC JTC 1/SC 25 under the ISO/IEEE PSDO Agreement and published.

The current version, IEEE 754-2019 published in July 2019, is derived from and replaces IEEE 754-2008, following a revision process started in September 2015, chaired by David G. Hough and edited by Mike Cowlishaw. It incorporates mainly clarifications (e.g. *totalOrder*) and defect fixes (e.g. *minNum*), but also includes some new recommended operations (e.g. *augmentedAddition*).

The international standard **ISO/IEC 60559:2020** (with content identical to IEEE 754-2019) has been approved for adoption through ISO/IEC JTC 1/SC 25 and published.

The next projected revision of the standard is in 2029.

## Formats

IEEE 754 defines a *format* as "a set of representations of numerical values and symbols, perhaps accompanied by an encoding".

A floating-point format is specified by

- a base (also called *radix*) *b*, which is either 2 (binary) or 10 (decimal) in IEEE 754;
- a precision *p*;
- an exponent range from *emin* to *emax*, with *emin* = 1 − *emax*, or equivalently *emin* = − (*emax* − 1), for all IEEE 754 formats.

A format comprises

- Finite numbers, which can be described by three integers: *s* = a *sign* (zero or one), *c* = a *significand* (also called a *coefficient* or *mantissa*) having no more than *p* digits when written in base *b* (i.e., an integer in the range through 0 to *b**p* − 1), and *q* = an *exponent* such that *emin* ≤ *q* + *p* − 1 ≤ *emax*. The numerical value of such a finite number is (−1)*s* × *c* × *b**q*. Moreover, there are two zero values, called signed zeros: the sign bit specifies whether a zero is +0 (positive zero) or −0 (negative zero).
- Two infinities: +∞ and −∞.
- Two kinds of NaN (not-a-number): a quiet NaN (qNaN) and a signaling NaN (sNaN).

For example, if *b* = 10, *p* = 7, and *emax* = 96, then *emin* = −95, the significand satisfies 0 ≤ *c* ≤ 9999999, and the exponent satisfies −101 ≤ *q* ≤ 90. Consequently, the smallest non-zero positive number that can be represented is 1×10−101, and the largest is 9999999×1090 (9.999999×1096), so the full range of numbers is −9.999999×1096 through 9.999999×1096. The numbers −*b*1−*emax* and *b*1−*emax* (here, −1×10−95 and 1×10−95) are the smallest (in magnitude) *normal numbers*; non-zero numbers between these smallest numbers are called subnormal numbers.

### Representation and encoding in memory

Some numbers may have several possible floating-point representations. For instance, if *b* = 10, and *p* = 7, then −12.345 can be represented by −12345×10−3, −123450×10−4, and −1234500×10−5. However, for most operations, such as arithmetic operations, the result (value) does not depend on the representation of the inputs.

For the decimal formats, any representation is valid, and the set of these representations is called a *cohort*. When a result can have several representations, the standard specifies which member of the cohort is chosen.

For the binary formats, the representation is made unique. Most floating point numbers, those with absolute value larger than 2*emin*, are called *normal*. They have a significand which is between 1 (included) and 2 (excluded), which thus always has a leading 1 bit; this bit is not explicitly stored in the representation, but is left implicit; this rule is called *leading bit convention*, *implicit bit convention*, or *hidden bit convention*, and it allows the format to have an extra bit of precision. A normal number's exponent has a "bias" added to it, and the resulting biased exponent is always a positive integer. Numbers smaller than 2*emin* are called *subnormal* numbers. These numbers are represented by the biased exponent 0, which stands for *emin*. For subnormal numbers, there is no longer an implicit leading 1 bit, and the significand lies between 0 and 1.

Due to the possibility of multiple encodings (at least in formats called *interchange formats*), a NaN may carry other information: a sign bit (which has no meaning, but may be used by some operations) and a *payload*, which is intended for diagnostic information indicating the source of the NaN (but the payload may have other uses, such as *NaN-boxing*).

### Basic and interchange formats

The standard defines five basic formats that are named for their numeric base and the number of bits used in their interchange encoding. There are three binary floating-point basic formats (encoded with 32, 64 or 128 bits) and two decimal floating-point basic formats (encoded with 64 or 128 bits). The binary32 and binary64 formats are the *single* and *double* formats of IEEE 754-1985 respectively. A conforming implementation must fully implement at least one of the basic formats.

The standard specifies interchange formats at a range of widths, including the basic formats, to support the exchange of floating-point data between implementations. The exponent and significand field sizes for each width are determined by defined rules based on width. The following table summarizes some of the possible interchange formats (including the basic formats).

Significand

Exponent

Properties

Name

Common name

Radix

Digits

Decimal

digits

Min

Max

MAXVAL

log

10

MAXVAL

MINVAL

>0

(normal)

MINVAL

>0

(subnormal)

Notes

binary16

Half precision

2

11

3.31

−14

15

65504

4.816

6.10

×

10

−5

5.96

×

10

−8

Interchange

binary32

Single precision

2

24

7.22

−126

127

3.40

×

10

38

38.532

1.18

×

10

−38

1.40

×

10

−45

Basic

binary64

Double precision

2

53

15.95

−1022

1023

1.80

×

10

308

308.255

2.23

×

10

−308

4.94

×

10

−324

Basic

binary128

Quadruple precision

2

113

34.02

−16382

16383

1.19

×

10

4932

4932.075

3.36

×

10

−4932

6.48

×

10

−4966

Basic

binary256

Octuple precision

2

237

71.34

−262142

262143

1.61

×

10

78

913

78913.207

2.48

×

10

−78913

2.25

×

10

−78984

Interchange

decimal32

10

7

7

−95

96

1.0

×

10

97

97 − 4.34

×

10

−8

1

×

10

−95

1

×

10

−101

Interchange

decimal64

10

16

16

−383

384

1.0

×

10

385

385 − 4.34

×

10

−17

1

×

10

−383

1

×

10

−398

Basic

decimal128

10

34

34

−6143

6144

1.0

×

10

6145

6145 − 4.34

×

10

−35

1

×

10

−6143

1

×

10

−6176

Basic

In the table above, integer values are exact, whereas values in decimal notation (e.g. 1.0) are rounded values. The minimum exponents listed are for normal numbers; the special subnormal number representation allows even smaller (in magnitude) numbers to be represented with some loss of precision. For example, the smallest positive number that can be represented in binary64 is 2−1074; contributions to the −1074 figure include the *emin* value −1022 and all but one of the 53 significand bits (2−1022 − (53 − 1) = 2−1074).

Decimal digits is the precision of the format expressed in terms of an equivalent number of decimal digits. It is computed as *digits* × log10 *base*. E.g. binary128 has approximately the same precision as a 34 digit decimal number.

log10 *MAXVAL* is a measure of the range of the encoding. Its integer part is the largest exponent shown on the output of a value in scientific notation with one leading digit in the significand before the decimal point (e.g. 1.698×1038 is near the largest value in binary32, 9.999999×1096 is the largest value in decimal32).

The binary32 (single) and binary64 (double) formats are two of the most common formats used today. The figure below shows the absolute precision for both formats over a range of values. This figure can be used to select an appropriate format given the expected value of a number and the required precision.

An example of a layout for 32-bit floating point is

and the 64 bit layout is similar.

### Extended and extendable precision formats

The standard specifies optional extended and extendable precision formats, which provide greater precision than the basic formats. An extended precision format extends a basic format by using more precision and more exponent range. An extendable precision format allows the user to specify the precision and exponent range. An implementation may use whatever internal representation it chooses for such formats; all that needs to be defined are its parameters (*b*, *p*, and *emax*). These parameters uniquely describe the set of finite numbers (combinations of sign, significand, and exponent for the given radix) that it can represent.

The standard recommends that language standards provide a method of specifying *p* and *emax* for each supported base *b*. The standard recommends that language standards and implementations support an extended format which has a greater precision than the largest basic format supported for each radix *b*. For an extended format with a precision between two basic formats the exponent range must be as great as that of the next wider basic format. So for instance a 64-bit extended precision binary number must have an 'emax' of at least 16383. The x87 80-bit extended format meets this requirement.

The original IEEE 754-1985 standard also had the concept of *extended formats*, but without any mandatory relation between *emin* and *emax*. For example, the Motorola 68881 80-bit format, where *emin* = − *emax*, was a conforming extended format, but it became non-conforming in the 2008 revision.

### Interchange formats

Interchange formats are intended for the exchange of floating-point data using a bit string of fixed length for a given format.

#### Binary

For the exchange of binary floating-point numbers, interchange formats of length 16 bits, 32 bits, 64 bits, and any multiple of 32 bits ≥ 128 are defined. The 16-bit format is intended for the exchange or storage of small numbers (e.g., for graphics).

The encoding scheme for these binary interchange formats is the same as that of IEEE 754-1985: a sign bit, followed by *w* exponent bits that describe the exponent offset by a *bias*, and *p* − 1 bits that describe the significand. The width of the exponent field for a *k*-bit format is computed as *w* = round(4 log2(*k*)) − 13. The existing 64- and 128-bit formats follow this rule, but the 16- and 32-bit formats have more exponent bits (5 and 8 respectively) than this formula would provide (3 and 7 respectively).

As with IEEE 754-1985, the biased-exponent field is filled with all 1 bits to indicate either infinity (trailing significand field = 0) or a NaN (trailing significand field ≠ 0). For NaNs, quiet NaNs and signaling NaNs are distinguished by using the most significant bit of the trailing significand field exclusively, and the payload is carried in the remaining bits.

#### Decimal

For the exchange of decimal floating-point numbers, interchange formats of any multiple of 32 bits are defined. As with binary interchange, the encoding scheme for the decimal interchange formats encodes the sign, exponent, and significand. Two different bit-level encodings are defined, and interchange is complicated by the fact that some external indicator of the encoding in use may be required.

The two options allow the significand to be encoded as a compressed sequence of decimal digits using densely packed decimal or, alternatively, as a binary integer. The former is more convenient for direct hardware implementation of the standard, while the latter is more suited to software emulation on a binary computer. In either case, the set of numbers (combinations of sign, significand, and exponent) that may be encoded is identical, and special values (±zero with the minimum exponent, ±infinity, quiet NaNs, and signaling NaNs) have identical encodings.

## Rounding rules

The standard defines five rounding rules. The first two rules round to a nearest value; the others are called *directed roundings*:

### Roundings to nearest

- **Round to nearest, ties to even** – rounds to the nearest value; if the number falls midway, it is rounded to the nearest value with an even least significant digit.
- **Round to nearest, ties away from zero** (or **ties to away**)  – rounds to the nearest value; if the number falls midway, it is rounded to the nearest value above (for positive numbers) or below (for negative numbers).

At the extremes, a value with a magnitude strictly less than $k=b^{\text{emax}}\left(b-{\tfrac {1}{2}}b^{1-p}\right)$ will be rounded to the minimum or maximum finite number (depending on the value's sign). Any numbers with exactly this magnitude are considered ties; this choice of tie may be conceptualized as the midpoint between $\pm b^{\text{emax}}(b-b^{1-p})$ and $\pm b^{{\text{emax}}+1}$ , which, were the exponent not limited, would be the next representable floating-point numbers larger in magnitude. Numbers with a magnitude strictly larger than k are rounded to the corresponding infinity.

"Round to nearest, ties to even" is the default for binary floating point and the recommended default for decimal. "Round to nearest, ties to away" is only required for decimal implementations.

### Directed roundings

- **Round toward 0** – directed rounding towards zero (also known as *truncation*).
- **Round toward +∞** – directed rounding towards positive infinity (also known as *rounding up* or *ceiling*).
- **Round toward −∞** – directed rounding towards negative infinity (also known as *rounding down* or *floor*).

| Mode | Example value |   |   |   |
|---|---|---|---|---|
| +11.5 | +12.5 | −11.5 | −12.5 |   |
| to nearest, ties to even | +12.0 | +12.0 | −12.0 | −12.0 |
| to nearest, ties away from zero | +12.0 | +13.0 | −12.0 | −13.0 |
| toward 0 | +11.0 | +12.0 | −11.0 | −12.0 |
| toward +∞ | +12.0 | +13.0 | −11.0 | −12.0 |
| toward −∞ | +11.0 | +12.0 | −12.0 | −13.0 |

Unless specified otherwise, the floating-point result of an operation is determined by applying the rounding function on the infinitely precise (mathematical) result. Such an operation is said to be *correctly rounded*. This requirement is called *correct rounding*.

## Required operations

Required operations for a supported arithmetic format (including the basic formats) include:

- Conversions to and from integer
- Previous and next consecutive values
- Arithmetic operations (add, subtract, multiply, divide, square root, fused multiply–add, remainder, minimum, maximum)
- Conversions (between formats, to and from strings, etc.)
- Scaling and (for decimal) quantizing
- Copying and manipulating the sign (abs, negate, etc.)
- Comparisons and total ordering
- Classification of numbers (subnormal, finite, etc.) and testing for NaNs
- Testing and setting status flags

### Comparison predicates

The standard provides comparison predicates to compare one floating-point datum to another in the supported arithmetic format. Any comparison with a NaN is treated as unordered. −0 and +0 compare as equal.

### Total-ordering predicate

The standard provides a predicate *totalOrder*, which defines a total ordering on canonical members of the supported arithmetic format. The predicate agrees with the comparison predicates (see section § Comparison predicates) when one floating-point number is less than the other. The main differences are:

- NaN is sortable.
  - NaN is treated as if it had a larger absolute value than Infinity (or any other floating-point numbers). (−NaN < −Infinity; +Infinity < +NaN.)
  - qNaN and sNaN are treated as if qNaN had a larger absolute value than sNaN. (−qNaN < −sNaN; +sNaN < +qNaN.)
  - NaN is then sorted according to the payload. In IEEE 754-2008, a NaN with a lesser payload is treated as having a lesser absolute value. In IEEE 754-2019, any implementation-defined ordering is acceptable.
- Negative zero is treated as smaller than positive zero.
- If both sides of the comparison refer to the same floating-point datum, the one with the lesser exponent is treated as having a lesser absolute value.

The *totalOrder* predicate does not impose a total ordering on all encodings in a format. In particular, it does not distinguish among different encodings of the same floating-point representation, as when one or both encodings are non-canonical. IEEE 754-2019 incorporates clarifications of *totalOrder*.

For the binary interchange formats whose encoding follows the IEEE 754-2008 recommendation on placement of the NaN signaling bit, the comparison is identical to one that type puns the floating-point numbers to a sign–magnitude integer (assuming a payload ordering consistent with this comparison), an old trick for FP comparison without an FPU.

## Exception handling

The standard defines five exceptions, each of which returns a default value and has a corresponding status flag that is raised when the exception occurs. No other exception handling is required, but additional non-default alternatives are recommended (see § Alternate exception handling).

The five possible exceptions are

**Invalid operation**

mathematically undefined, e.g., the square root of a negative number. By default, returns qNaN.

**Division by zero**

an operation on finite operands gives an exact infinite result, e.g., 1/0 or log(0). By default, returns ±infinity.

**Overflow**

a finite result is too large to be represented accurately (i.e., its exponent with an unbounded exponent range would be larger than

emax

). By default, returns ±infinity for the round-to-nearest modes (and follows the rounding rules for the directed rounding modes).

**Underflow**

a result is very small (outside the normal range). By default, returns a number less than or equal to the minimum positive normal number in magnitude (following the rounding rules); a

subnormal number

always implies an underflow exception, but by default, if it is exact, no flag is raised.

**Inexact**

the exact (i.e., unrounded) result is not representable exactly. By default, returns the correctly rounded result.

These are the same five exceptions as were defined in IEEE 754-1985, but the *division by zero* exception has been extended to operations other than the division.

Some decimal floating-point implementations define additional exceptions, which are not part of IEEE 754:

**Clamped**

a result's exponent is too large for the destination format. By default, trailing zeros will be added to the coefficient to reduce the exponent to the largest usable value. If this is not possible (because this would cause the number of digits needed to be more than the destination format) then an overflow exception occurs.

**Rounded**

a result's coefficient requires more digits than the destination format provides. An inexact exception is signaled if any non-zero digits are discarded.

## Special values

### Signed zero

In the IEEE 754 standard, zero is signed, meaning that there exist both a "positive zero" (+0) and a "negative zero" (−0). In most run-time environments, positive zero is usually printed as "`0`" and the negative zero as "`-0`". The two values behave as equal in numerical comparisons, but some operations return different results for +0 and −0. For instance, 1/(−0) returns negative infinity, while 1/(+0) returns positive infinity (so that the identity 1/(1/±∞) = ±∞ is maintained). Other common functions with a discontinuity at *x* = 0 which might treat +0 and −0 differently include Γ(*x*) and the principal square root of *y* + *xi* for any negative number *y*. As with any approximation scheme, operations involving "negative zero" can occasionally cause confusion. For example, in IEEE 754, *x* = *y* does not always imply 1/*x* = 1/*y*, as 0 = −0 but 1/0 ≠ 1/(−0). Moreover, the reciprocal square root of ±0 is ±∞ while the mathematical function $1/{\sqrt {x}}$ over the real numbers does not have any negative value.

### Subnormal numbers

Subnormal values fill the underflow gap with values where the absolute distance between them is the same as for adjacent values just outside the underflow gap. This is an improvement over the older practice to just have zero in the underflow gap, and where underflowing results were replaced by zero (flush to zero).

Modern floating-point hardware usually handles subnormal values (as well as normal values), and does not require software emulation for subnormals.

### Infinities

The infinities of the extended real number line can be represented in IEEE floating-point datatypes, just like ordinary floating-point values like 1, 1.5, etc. They are not error values in any way, though they are often (depends on the rounding) used as replacement values when there is an overflow. Upon a divide-by-zero exception, a positive or negative infinity is returned as an exact result. An infinity can also be introduced as a numeral (like C's "INFINITY" macro, or "∞" if the programming language allows that syntax).

IEEE 754 requires infinities to be handled in a reasonable way, such as

- (+∞) + (+7) = (+∞)
- (+∞) × (−2) = (−∞)
- (+∞) × 0 = NaN – there is no meaningful thing to do

### NaNs

IEEE 754 specifies a special value called "Not a Number" (NaN) to be returned as the result of certain "invalid" operations, such as 0/0, ∞×0, or sqrt(−1). In general, NaNs will be propagated, i.e. most operations involving a NaN will result in a NaN, although functions that would give some defined result for any given floating-point value will do so for NaNs as well, e.g. NaN ^ 0 = 1. There are two kinds of NaNs: the default *quiet* NaNs and, optionally, *signaling* NaNs. A signaling NaN in any arithmetic operation (including numerical comparisons) will cause an "invalid operation" exception to be signaled.

The representation of NaNs specified by the standard has some unspecified bits that could be used to encode the type or source of error; but there is no standard for that encoding. In theory, signaling NaNs could be used by a runtime system to flag uninitialized variables, or extend the floating-point numbers with other special values without slowing down the computations with ordinary values, although such extensions are not common. A variant of this approach (sometimes called "NaN-boxing") is used by some JavaScript runtimes and LuaJIT to store 64-bit pointer values and IEEE 754 double-precision floating-point values in the same data type, allowing runtimes to eliminate the overhead of extra memory allocations and indirections for floating-point values.

## Design rationale

It is a common misconception that the more esoteric features of the IEEE 754 standard discussed here, such as extended formats, NaN, infinities, subnormals etc., are only of interest to numerical analysts, or for advanced numerical applications. In fact the opposite is true: these features are designed to give safe robust defaults for numerically unsophisticated programmers, in addition to supporting sophisticated numerical libraries by experts. The key designer of IEEE 754, William Kahan, notes that it is incorrect to "... [deem] features of IEEE Standard 754 for Binary Floating-Point Arithmetic that ...[are] not appreciated to be features usable by none but numerical experts. The facts are quite the opposite. In 1977 those features were designed into the Intel 8087 to serve the widest possible market... Error-analysis tells us how to design floating-point arithmetic, like IEEE Standard 754, moderately tolerant of well-meaning ignorance among programmers".

- The special values such as infinity and NaN ensure that the floating-point arithmetic is algebraically complete: every floating-point operation produces a well-defined result and will not—by default—throw a machine interrupt or trap. Moreover, the choices of special values returned in exceptional cases were designed to give the correct answer in many cases. For instance, under IEEE 754 arithmetic, a continued fraction such as $R(z):=7-{\cfrac {3}{z-2+{\cfrac {4}{z-3}}}}$ can be implemented straightforwardly and will give the correct answer even when there is a division by zero, because any positive number divided by zero results in +∞, e.g. when *z* = 3, *R*(*z*) = 7. As noted by Kahan, the unhandled trap consecutive to a floating-point to 16-bit integer conversion overflow that caused the loss of an Ariane 5 rocket would not have happened under the default IEEE 754 floating-point policy.
- Subnormal numbers ensure that for *finite* floating-point numbers x and y, *x* − *y* = 0 if and only if *x* = *y*, as expected, but which did not hold under earlier floating-point representations.
- On the design rationale of the x87 80-bit format, Kahan notes: "This Extended format is designed to be used, with negligible loss of speed, for all but the simplest arithmetic with float and double operands. For example, it should be used for scratch variables in loops that implement recurrences like polynomial evaluation, scalar products, partial and continued fractions. It often averts premature Over/Underflow or severe local cancellation that can spoil simple algorithms". Computing intermediate results in an extended format with high precision and extended exponent has precedents in the historical practice of scientific calculation and in the design of scientific calculators e.g. Hewlett-Packard's financial calculators performed arithmetic and financial functions to three more significant decimals than they stored or displayed. The implementation of extended precision enabled standard elementary function libraries to be readily developed that normally gave double precision results within one unit in the last place (ULP) at high speed.
- Correct rounding of values to the nearest representable value avoids systematic biases in calculations and slows the growth of errors. Rounding ties to even removes the statistical bias that can occur in adding similar figures.
- Directed rounding was intended as an aid with checking error bounds, for instance in interval arithmetic. It is also used in the implementation of some functions.
- The mathematical basis of the operations, in particular correct rounding, allows one to prove mathematical properties and design floating-point algorithms such as 2Sum, Fast2Sum and Kahan summation algorithm, e.g. to improve accuracy or implement multiple-precision arithmetic subroutines relatively easily.

A property of the single- and double-precision formats is that their encoding allows one to easily sort them without using floating-point hardware, as if the bits represented sign-magnitude integers, although it is unclear whether this was a design consideration (it seems noteworthy that the earlier IBM hexadecimal floating-point representation also had this property for normalized numbers). With the prevalent two's-complement representation, interpreting the bits as signed integers sorts the positives correctly, but with the negatives reversed; as one possible correction for that, with an xor to flip the sign bit for positive values and all bits for negative values, all the values become sortable as unsigned integers (with −0 < +0).

## Recommendations

### Alternate exception handling

The standard recommends optional exception handling in various forms, including presubstitution of user-defined default values, and traps (exceptions that change the flow of control in some way) and other exception handling models that interrupt the flow, such as try/catch. The traps and other exception mechanisms remain optional, as they were in IEEE 754-1985.

### Recommended operations

Clause 9 in the standard recommends additional mathematical operations that language standards should define. None are required in order to conform to the standard.

The following are recommended arithmetic operations, which must round correctly:

- $e^{x}$ , $2^{x}$ , $10^{x}$
- $e^{x}-1$ , $2^{x}-1$ , $10^{x}-1$
- $\ln x$ , $\log _{2}x$ , $\log _{10}x$
- $\ln(1+x)$ , $\log _{2}(1+x)$ , $\log _{10}(1+x)$
- ${\textstyle {\sqrt {x^{2}+y^{2}}}}$
- $1{\big /}{\sqrt {x{\vphantom {t}}}}$
- $(1+x)^{n}$ for $x\geq -1$ (named *compound* and used to compute an exponential growth, whose rate cannot be less than −1)
- $x^{\frac {1}{n}}$
- $x^{n}$ , $x^{y}$
- $\sin x$ , $\cos x$ , $\tan x$
- $\arcsin x$ , $\arccos x$ , $\arctan x$ , $\operatorname {atan2} (y,x)$
- $\operatorname {sinPi} x=\sin \pi x$ , $\operatorname {cosPi} x=\cos \pi x$ , $\operatorname {tanPi} x=\tan \pi x$ (see also: Multiples of π)
- $\operatorname {asinPi} x={\tfrac {1}{\pi }}\arcsin x$ , $\operatorname {acosPi} x={\tfrac {1}{\pi }}\arccos x$ , $\operatorname {atanPi} x={\tfrac {1}{\pi }}\arctan x$ , $\operatorname {atan2Pi} (y,x)={\tfrac {1}{\pi }}\operatorname {atan2} (y,x)$ (see also: Multiples of π)
- $\sinh x$ , $\cosh x$ , $\tanh x$
- $\operatorname {arsinh} x$ , $\operatorname {arcosh} x$ , $\operatorname {artanh} x$

The $\operatorname {asinPi}$ , $\operatorname {acosPi}$ and $\operatorname {tanPi}$ functions were not part of the IEEE 754-2008 standard because they were deemed less necessary. $\operatorname {asinPi}$ and $\operatorname {acosPi}$ were mentioned, but this was regarded as an error. All three were added in the 2019 revision.

The recommended operations also include setting and accessing dynamic mode rounding direction, and implementation-defined vector reduction operations such as sum, scaled product, and dot product (correct rounding is not required). The standard admits that numerical results for these reduction operations may differ across implementations due to intermediate result width and order of operations.

As of 2019, *augmented arithmetic operations* for the binary formats are also recommended. These operations, specified for addition, subtraction and multiplication, produce a pair of values consisting of a result correctly rounded to nearest in the format and the error term, which is representable exactly in the format. At the time of publication of the standard, no hardware implementations are known, but very similar operations were already implemented in software using well-known algorithms. The history and motivation for their standardization are explained in a background document.

The formerly required *minNum*, *maxNum*, *minNumMag*, and *maxNumMag* from IEEE 754-2008 have been removed in the 2019 revision due to their non-associativity. Instead, two sets of new minimum and maximum operations are recommended. The first set contains *minimum*, *minimumNumber*, *maximum* and *maximumNumber*. The second set contains *minimumMagnitude*, *minimumMagnitudeNumber*, *maximumMagnitude* and *maximumMagnitudeNumber*. The history and motivation for this change are explained in a background document.

### Expression evaluation

The standard recommends how language standards should specify the semantics of sequences of operations, and points out the subtleties of literal meanings and optimizations that change the value of a result. By contrast, the previous 1985 version of the standard left aspects of the language interface unspecified, which led to inconsistent behavior between compilers, or different optimization levels in an optimizing compiler.

Programming languages should allow a user to specify a minimum precision for intermediate calculations of expressions for each radix. This is referred to as *preferredWidth* in the standard, and it should be possible to set this on a per-block basis. Intermediate calculations within expressions should be calculated, and any temporaries saved, using the maximum of the width of the operands and the preferred width if set. Thus, for instance, a compiler targeting x87 floating-point hardware should have a means of specifying that intermediate calculations must use the double-extended format. The stored value of a variable must always be used when evaluating subsequent expressions, rather than any precursor from before rounding and assigning to the variable.

### Reproducibility

The IEEE 754-1985 version of the standard allowed many variations in implementations (such as the encoding of some values and the detection of certain exceptions). IEEE 754-2008 has reduced these allowances, but a few variations still remain (especially for binary formats). The reproducibility clause recommends that language standards should provide a means to write reproducible programs (i.e., programs that will produce the same result in all implementations of a language) and describes what needs to be done to achieve reproducible results.

Concrete examples of potentially non-reproducible behavior can be found in C and C++, which allow the use of higher precision for results of floating-point operations and contraction of floating-point expressions, such as regular multiply-and-add into FMA and `1.0/sqrt(x)` into a reciprocal square root as a single instruction. C/C++ Compilers such as GCC and cl.exe generally default to allowing both unless specifically asked not to, as these changes can generate faster code without obvious loss of accuracy. Compilers also offer more overtly non-compliant "fast" optimizations. C mathematical functions are usually not implemented to be "correctly rounded" and add to the problem. The floating-point environment may also be unexpectedly changed by third-party code.

## Character representation

The standard requires operations to convert between supported formats and *external character sequences*. Conversions to and from a decimal character format are required for all formats. Conversion to an external character sequence must be such that round-trip conversion, from internal binary representation to external decimal text and back to internal binary representation, will recover the original number when using roundTiesToEven. There is no requirement to preserve the payload of a quiet NaN or signaling NaN, and conversion from the external character sequence may turn a signaling NaN into a quiet NaN.

The original binary value will be preserved by converting to decimal and back again using:

- 5 decimal digits for binary16,
- 9 decimal digits for binary32,
- 17 decimal digits for binary64,
- 36 decimal digits for binary128.

For other binary formats, the required number of decimal digits is

$1+\lceil p\log _{10}(2)\rceil ,$

where *p* is the number of significant bits in the binary format, e.g. 237 bits for binary256.

Algorithms, with code, for correctly rounded conversion from binary to decimal and decimal to binary are discussed by Gay, and for testing – by Paxson and Kahan.

With decimal floating-point formats conversion to decimal character sequences are exact and round-trip behavior is guaranteed so long as the text representation preserves the quantum by retaining trailing zeros to the right of the decimal point in the significand. The decimal representation will be preserved using:

- 7 decimal digits for decimal32,
- 16 decimal digits for decimal64,
- 34 decimal digits for decimal128.

### Hexadecimal literals

For binary formats, the standard recommends providing conversions to and from *external hexadecimal-significand character sequences*, based on C99's hexadecimal floating-point literals. Such a literal consists of an optional sign (`+` or `-`), the indicator "0x", a hexadecimal number with or without a period, an exponent indicator "p", and a decimal exponent with optional sign. The syntax is not case-sensitive. The decimal exponent scales by powers of 2. For example, `0x0.1p0` is 1/16 and `0x0.1p-4` is 1/256.

The standard does not mention hexadecimal literals for decimal formats since decimal character sequences can accurately represent all decimal floating-point values.
