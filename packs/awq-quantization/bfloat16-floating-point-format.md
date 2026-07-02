---
title: "bfloat16 floating-point format"
source: https://en.wikipedia.org/wiki/Bfloat16_floating-point_format
domain: awq-quantization
license: CC-BY-SA-4.0
tags: activation aware quantization, weight quantization scaling, awq method, salient weight preservation, low bit llm
fetched: 2026-07-02
---

# bfloat16 floating-point format

The **bfloat16** (**brain floating point**) floating-point format is a computer number format occupying 16 bits in computer memory; it represents a wide dynamic range of numeric values by using a floating radix point. This format is a shortened (16-bit) version of the 32-bit IEEE 754 single-precision floating-point format (binary32) with the intent of accelerating machine learning and near-sensor computing. It preserves the approximate dynamic range of 32-bit floating-point numbers by retaining 8 exponent bits, but supports only an 8-bit precision rather than the 24-bit significand of the binary32 format. More so than single-precision 32-bit floating-point numbers, bfloat16 numbers are unsuitable for integer calculations, but this is not their intended use. Bfloat16 is used to reduce the storage requirements and increase the calculation speed of machine learning algorithms.

The bfloat16 format was developed by Google Brain, an artificial intelligence research group at Google, for use in its TPU v2, released in 2017. It is utilized in many CPUs, GPUs, and AI processors, such as Intel Xeon processors (AVX-512 BF16 extensions), Intel Data Center GPU, Intel Nervana NNP-L1000, Intel FPGAs, AMD Zen, AMD Instinct, NVIDIA GPUs, Google Cloud TPUs, AWS Inferentia, AWS Trainium, ARMv8.6-A, and Apple's M2 and therefore A15 chips and later. Many libraries support bfloat16, such as CUDA, Intel oneAPI Math Kernel Library, AMD ROCm, AMD Optimizing CPU Libraries, PyTorch, and TensorFlow. On these platforms, bfloat16 may also be used in mixed-precision arithmetic, where bfloat16 numbers may be operated on and expanded to wider data types.

## bfloat16 floating-point format

**bfloat16** has the following format:

- Sign bit: 1 bit
- Exponent width: 8 bits
- Significand precision: 8 bits (7 explicitly stored, with an implicit leading bit), as opposed to 24 bits in a classical single-precision floating-point format

The bfloat16 format, being a shortened IEEE 754 single-precision 32-bit float, allows for fast conversion to and from an IEEE 754 single-precision 32-bit float; in conversion to the bfloat16 format, the exponent bits are preserved while the significand field can be reduced by truncation (thus corresponding to round toward 0) or other rounding mechanisms, ignoring the NaN special case. Preserving the exponent bits maintains the 32-bit float's range of ≈ 10−38 to ≈ 3 × 1038.

The bits are laid out as follows:

IEEE half-precision

16-bit float

sign

exponent (5 bit)

fraction (10 bit)

┃

|   |
|---|

|   |
|---|

0

0

1

1

0

0

0

1

0

0

0

0

0

0

0

0

15

14

10

9

0

bfloat16

sign

exponent (8 bit)

fraction (7 bit)

┃

|   |
|---|

|   |
|---|

0

0

1

1

1

1

1

0

0

0

1

0

0

0

0

0

15

14

7

6

0

Nvidia's TensorFloat-32

(19 bits)

sign

exponent (8 bit)

fraction (10 bit)

┃

|   |
|---|

|   |
|---|

0

0

1

1

1

1

1

0

0

0

1

0

0

0

0

0

0

0

0

18

17

10

9

0

ATI's fp24 format

sign

exponent (7 bit)

fraction (16 bit)

┃

|   |
|---|

|   |
|---|

0

0

1

1

1

1

0

0

0

1

0

0

0

0

0

0

0

0

0

0

0

0

0

0

23

22

16

15

0

Pixar's PXR24 format

sign

exponent (8 bit)

fraction (15 bit)

┃

|   |
|---|

|   |
|---|

0

0

1

1

1

1

0

0

0

1

0

0

0

0

0

0

0

0

0

0

0

0

0

0

23

22

15

14

0

IEEE 754 single-precision

32-bit float

sign

exponent (8 bit)

fraction (23 bit)

┃

|   |
|---|

|   |
|---|

0

0

1

1

1

1

1

0

0

0

1

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

31

30

23

22

0

### Exponent encoding

The bfloat16 binary floating-point exponent is encoded using an offset-binary representation, with the zero offset being 127; also known as exponent bias in the IEEE 754 standard.

- Emin = 01H−7FH = −126
- Emax = FEH−7FH = 127
- Exponent bias = 7FH = 127

Thus, in order to get the true exponent as defined by the offset-binary representation, the offset of 127 has to be subtracted from the value of the exponent field.

The minimum and maximum values of the exponent field (00H and FFH) are interpreted specially, like in the IEEE 754 standard formats.

| Exponent | Significand zero | Significand non-zero | Equation |
|---|---|---|---|
| 00H | zero, −0 | subnormal numbers | (−1)signbit×2−126× 0.significandbits |
| 01H, ..., FEH | normalized value | (−1)signbit×2exponentbits−127× 1.significandbits |   |
| FFH | ±infinity | NaN (quiet, signaling) |   |

The minimum positive normal value is 2−126 ≈ 1.18 × 10−38 and the minimum positive (subnormal) value is 2−126−7 = 2−133 ≈ 9.2 × 10−41.

### Rounding and conversion

The most common use case is the conversion between IEEE 754 binary32 and bfloat16. The following section describes the conversion process and its rounding scheme in the conversion. Note that there are other possible scenarios of format conversions to or from bfloat16. For example, int16 and bfloat16.

- From binary32 to bfloat16. When bfloat16 was first introduced as a storage format, the conversion from IEEE 754 binary32 (32-bit floating point) to bfloat16 is truncation (round toward 0). Later on, when it becomes the input of matrix multiplication units, the conversion can have various rounding mechanisms depending on the hardware platforms. For example, for Google TPU, the rounding scheme in the conversion is round-to-nearest-even; ARM uses the non-IEEE Round-to-Odd mode; for NVIDIA, it supports converting float number to bfloat16 precision in round-to-nearest-even mode.
- From bfloat16 to binary32. Since binary32 can represent all exact values in bfloat16, the conversion simply pads 16 zeros in the significand bits.

## Encoding of special values

### Positive and negative infinity

Just as in IEEE 754, positive and negative infinity are represented with their corresponding sign bits, all 8 exponent bits set (FFhex) and all significand bits zero. Explicitly,

```mw
val    s_exponent_signcnd
+inf = 0_11111111_0000000
-inf = 1_11111111_0000000
```

### Not a Number

Just as in IEEE 754, NaN values are represented with either sign bit, all 8 exponent bits set (FFhex) and not all significand bits zero. Explicitly,

```mw
val    s_exponent_signcnd
+NaN = 0_11111111_klmnopq
-NaN = 1_11111111_klmnopq
```

where at least one of *k, l, m, n, o, p,* or *q* is 1. As with IEEE 754, NaN values can be quiet or signaling, although there are no known uses of signaling bfloat16 NaNs.

## Range and precision

Bfloat16 is designed to maintain the number range from the 32-bit IEEE 754 single-precision floating-point format (binary32), while reducing the precision from 24 bits to 8 bits. This means that the precision is between two and three decimal digits, and bfloat16 can represent finite values up to about 3.4 × 1038.

## Examples

These examples are given in bit *representation*, in hexadecimal and binary, of the floating-point value. This includes the sign, (biased) exponent, and significand.

```
3f80 = 0 01111111 0000000 = 1
c000 = 1 10000000 0000000 = −2
```

```
7f7f = 0 11111110 1111111 = (28 − 1) × 2−7 × 2127 ≈ 3.38953139 × 1038 (max finite positive value in bfloat16 precision)
0080 = 0 00000001 0000000 = 2−126 ≈ 1.175494351 × 10−38 (min normalized positive value in bfloat16 precision and single-precision floating point)
```

The maximum positive finite value of a normal bfloat16 number is 3.38953139 × 1038, slightly below (224 − 1) × 2−23 × 2127 = 3.402823466 × 1038, the max finite positive value representable in single precision.

### Zeros and infinities

```
0000 = 0 00000000 0000000 = 0
8000 = 1 00000000 0000000 = −0
```

```
7f80 = 0 11111111 0000000 = infinity
ff80 = 1 11111111 0000000 = −infinity
```

### Special values

```
4049 = 0 10000000 1001001 = 3.140625 ≈ π ( pi )
3eab = 0 01111101 0101011 = 0.333984375 ≈ 1/3
```

### NaNs

```
ffc1 = x 11111111 1000001 => qNaN
ff81 = x 11111111 0000001 => sNaN
```
