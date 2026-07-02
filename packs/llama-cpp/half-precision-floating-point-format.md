---
title: "Half-precision floating-point format"
source: https://en.wikipedia.org/wiki/Half-precision_floating-point_format
domain: llama-cpp
license: CC-BY-SA-4.0
tags: llama cpp, gguf quantization, cpu inference, local llm, ggml tensor
fetched: 2026-07-02
---

# Half-precision floating-point format

**Half precision** (sometimes called **FP16** or **float16**) is a binary floating-point computer number format that occupies 16 bits (two bytes in modern computers) in computer memory. It is intended for storage of floating-point values in applications where higher precision is not essential, in particular image processing and neural networks.

Almost all modern uses follow the IEEE 754-2008 standard, where the 16-bit base-2 format is referred to as **binary16**, and the exponent uses 5 bits. This can express values in the range ±65,504, with the minimum value above 1 being 1 + 1/1024.

## History

Several earlier 16-bit floating point formats have existed including that of Hitachi's HD61810 DSP of 1982 (a 4-bit exponent and a 12-bit mantissa), the top 16 bits of a 32-bit float (8 exponent and 7 mantissa bits) called a bfloat16, and Thomas J. Scott's WIF of 1991 (5 exponent bits, 10 mantissa bits) and the 3dfx Voodoo Graphics processor of 1995 (same as Hitachi).

ILM was searching for an image format that could handle a wide dynamic range, but without the hard drive and memory cost of single or double precision floating point. The hardware-accelerated programmable shading group led by John Airey at SGI (Silicon Graphics) used the s10e5 data type in 1997 as part of the "bali" design effort. This is described in a SIGGRAPH 2000 paper (see section 4.3) and further documented in US patent 7518615. It was popularized by its use in the open-source OpenEXR image format.

Nvidia and Microsoft defined the **half** datatype in the Cg language, released in early 2002, and implemented it in silicon in the GeForce FX, released in late 2002. However, hardware support for accelerated 16-bit floating point was later dropped by Nvidia before being reintroduced in the Tegra X1 mobile GPU in 2015.

The F16C extension in 2012 allows x86 processors to convert half-precision floats to and from single-precision floats with a machine instruction.

## IEEE 754 half-precision binary floating-point format: binary16

The IEEE 754 standard specifies a **binary16** as having the following format:

- Sign bit: 1 bit
- Exponent width: 5 bits
- Significand precision: 11 bits (10 explicitly stored)

The format is laid out as follows:

The format is assumed to have an implicit lead bit with value 1 unless the exponent field is stored with all zeros. Thus, only 10 bits of the significand appear in the memory format but the total precision is 11 bits. In IEEE 754 parlance, there are 10 bits of significand, but there are 11 bits of significand precision (log10(211) ≈ 3.311 decimal digits, or 4 digits ± slightly less than 5 units in the last place).

### Exponent encoding

The half-precision binary floating-point exponent is encoded using an offset-binary representation, with the zero offset being 15; also known as exponent bias in the IEEE 754 standard.

- Emin = 000012 − 011112 = −14
- Emax = 111102 − 011112 = 15
- Exponent bias = 011112 = 15

Thus, as defined by the offset binary representation, in order to get the true exponent the offset of 15 has to be subtracted from the stored exponent.

The stored exponents 000002 and 111112 are interpreted specially.

| Exponent | Significand = zero | Significand ≠ zero | Equation |
|---|---|---|---|
| 000002 | zero, −0 | subnormal numbers | (−1)signbit × 2−14 × 0.significantbits2 |
| 000012, ..., 111102 | normalized value | (−1)signbit × 2exponent−15 × 1.significantbits2 |   |
| 111112 | ±infinity | NaN (quiet, signaling) |   |

The minimum strictly positive (subnormal) value is 2−24 ≈ 5.96 × 10−8. The minimum positive normal value is 2−14 ≈ 6.10 × 10−5. The maximum representable value is (2−2−10) × 215 = 65504.

### Half precision examples

These examples are given in bit representation of the floating-point value. This includes the sign bit, (biased) exponent, and significand.

| Binary | Hex | Value | Notes |
|---|---|---|---|
| 0 00000 0000000000 | 0000 | 0 |   |
| 0 00000 0000000001 | 0001 | 2−14 × (0 + ⁠1/1024⁠ ) ≈ 0.000000059604645 | smallest positive subnormal number |
| 0 00000 1111111111 | 03ff | 2−14 × (0 + ⁠1023/1024⁠ ) ≈ 0.000060975552 | largest subnormal number |
| 0 00001 0000000000 | 0400 | 2−14 × (1 + ⁠0/1024⁠ ) ≈ 0.00006103515625 | smallest positive normal number |
| 0 01101 0101010101 | 3555 | 2−2 × (1 + ⁠341/1024⁠ ) ≈ 0.33325195 | nearest value to 1/3 |
| 0 01110 1111111111 | 3bff | 2−1 × (1 + ⁠1023/1024⁠ ) ≈ 0.99951172 | largest number less than one |
| 0 01111 0000000000 | 3c00 | 20 × (1 + ⁠0/1024⁠ ) = 1 | one |
| 0 01111 0000000001 | 3c01 | 20 × (1 + ⁠1/1024⁠ ) ≈ 1.00097656 | smallest number larger than one |
| 0 10000 1001001000 | 4248 | 21 × (1 + ⁠584/1024⁠ ) = 3.140625 | closest value to π |
| 0 11001 1111111111 | 67ff | 210 × (1 + ⁠1023/1024⁠ ) = 2047 | largest odd number |
| 0 11110 1111111111 | 7bff | 215 × (1 + ⁠1023/1024⁠ ) = 65504 | largest finite number |
| 0 11111 0000000000 | 7c00 | ∞ | infinity |
| 1 00000 0000000000 | 8000 | −0 |   |
| 1 10000 0000000000 | c000 | (−1)1 × 21 × (1 + ⁠0/1024⁠ ) = −2 |   |
| 1 11111 0000000000 | fc00 | −∞ | negative infinity |

By default, 1/3 rounds down like for double precision, because of the odd number of bits in the significand. The bits beyond the rounding point are 0101... which is less than 1/2 of a unit in the last place.

## ARM alternative half-precision

ARM processors support (via a floating-point control register bit) an "alternative half-precision" format, which does away with the special case for an exponent value of 31 (111112). It is almost identical to the IEEE format, but there is no encoding for infinity or NaNs; instead, an exponent of 31 encodes normalized numbers in the range 65536 to 131008.

## Uses of half precision

Half precision is used in several computer graphics environments to store pixels, including MATLAB, OpenEXR, JPEG XR, GIMP, OpenGL, Vulkan, Cg, Direct3D, and D3DX. The advantage over 8-bit or 16-bit integers is that the increased dynamic range allows for more detail to be preserved in highlights and shadows for images, and avoids gamma correction. The advantage over 32-bit single-precision floating point is that it requires half the storage and bandwidth (at the expense of precision and range).

Half precision can be useful for mesh quantization. Mesh data is usually stored using 32-bit single-precision floats for the vertices, however in some situations it is acceptable to reduce the precision to only 16-bit half-precision, requiring only half the storage at the expense of some precision. Mesh quantization can also be done with 8-bit or 16-bit fixed precision depending on the requirements.

Hardware and software for machine learning and neural networks often use half-precision arithmetic to accelerate computations. In these applications, the distinct bfloat16 format is sometimes preferred for its wider dynamic range than half-precision, and specialized floating point formats with only 8 bits or less are increasingly used to further accelerate certain computations.

If the hardware has instructions to compute half-precision math, it is often faster than single or double precision, sometimes up to 4 times faster. In addition if the system has SIMD instructions, often one instruction can simultaneously operate on twice as many half values than float values.

## Support by programming languages

Zig, Odin, and other languages provide support for half precisions with their `f16` type.

.NET 5 introduced half precision floating point numbers with the `System.Half` standard library type. As of 16 July 2025, no .NET language (C#, F#, Visual Basic, and C++/CLI and C++/CX) has literals (e.g. in C#, `1.0f` has type `System.Single` or `1.0m` has type `System.Decimal`) or a keyword for the type.

Swift introduced half-precision floating point numbers in Swift 5.3 with the `Float16` type.

OpenCL also supports half-precision floating point numbers with the half datatype on IEEE 754-2008 half-precision storage format.

As of 31 May 2026, Rust is currently working on adding a new `f16` type for IEEE half-precision 16-bit floats.

Julia provides support for half-precision floating point numbers with the `Float16` type.

C++ introduced half-precision since C++23 with the `std::float16_t` type. GCC already implements support for it.

## Hardware support

Several versions of the ARM architecture have support for half precision.

Support for conversions with half-precision floats in the x86 instruction set is specified in the F16C instruction set extension, first introduced in 2009 by AMD and fairly broadly adopted by AMD and Intel CPUs by 2012. This was further extended up the AVX-512_FP16 instruction set extension implemented in the Intel Sapphire Rapids processor.

On RISC-V, the `Zfh` and `Zfhmin` extensions provide hardware support for 16-bit half precision floats. The `Zfhmin` extension is a minimal alternative to `Zfh`.

On Power ISA, VSX and the not-yet-approved SVP64 extension provide hardware support for 16-bit half-precision floats as of PowerISA v3.1B and later.

Support for half precision on IBM Z is part of the Neural-network-processing-assist facility that IBM introduced with Telum. IBM refers to half precision floating point data as NNP-Data-Type 1 (16-bit).
