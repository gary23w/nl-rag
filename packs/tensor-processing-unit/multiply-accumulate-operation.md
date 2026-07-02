---
title: "Multiply–accumulate operation"
source: https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation
domain: tensor-processing-unit
license: CC-BY-SA-4.0
tags: tensor processing unit, ai accelerator hardware, matrix multiplication engine, hardware acceleration
fetched: 2026-07-02
---

# Multiply–accumulate operation

In computing, especially digital signal processing, the **multiply–accumulate** (**MAC**) or **multiply–add** (**MAD**) operation is a common step that computes the product of two numbers and adds that product to an accumulator. The hardware unit that performs the operation is known as a **multiplier–accumulator** (**MAC unit**); the operation itself is also often called a MAC or a MAD operation. The MAC operation modifies an accumulator *a*: $a\gets a+(b\times c)$

When done with floating-point numbers, it might be performed with two roundings (typical in many DSPs), or with a single rounding. When performed with a single rounding, it is called a **fused multiply–add** (**FMA**) or **fused multiply–accumulate** (**FMAC**).

Modern computers may contain a dedicated MAC, consisting of a multiplier implemented in combinational logic followed by an adder and an accumulator register that stores the result. The output of the register is fed back to one input of the adder, so that on each clock cycle, the output of the multiplier is added to the register. Combinational multipliers require a large amount of logic, but can compute a product much more quickly than the method of shifting and adding typical of earlier computers. Percy Ludgate was the first to conceive a MAC in his Analytical Machine of 1909, and the first to exploit a MAC for division (using multiplication seeded by reciprocal, via the convergent series (1+*x*)−1). The first modern processors to be equipped with MAC units were digital signal processors, but the technique is now also common in general-purpose processors.

## In floating-point arithmetic

When done with integers, the operation is typically exact (computed modulo some power of two). However, floating-point numbers have only a certain amount of mathematical precision. That is, digital floating-point arithmetic is generally not associative or distributive. (See Floating-point arithmetic § Accuracy problems.) Therefore, it makes a difference to the result whether the multiply–add is performed with two roundings, or in one operation with a single rounding (a fused multiply–add). IEEE 754-2008 specifies that it must be performed with one rounding, yielding a more accurate result.

## Fused multiply–add

A **fused multiply–add** (**FMA** or **fmadd**) is a floating-point multiply–add operation performed in one step (fused operation), with a single rounding. That is, where an unfused multiply–add would compute the product *b* × *c*, round it to *N* significant bits, add the result to *a*, and round back to *N* significant bits, a fused multiply–add would compute the entire expression *a* + (*b* × *c*) to its full precision before rounding the final result down to *N* significant bits.

A fast FMA can speed up and improve the accuracy of many computations that involve the accumulation of products:

- Dot product
- Matrix multiplication
- Polynomial evaluation (e.g., with Horner's rule)
- Newton's method for evaluating functions (from the inverse function)
- Convolution
- Neural network
- Multiplication in double-double arithmetic

Fused multiply–add can usually be relied on to give more accurate results. However, William Kahan has pointed out that it can give problems if used unthinkingly. If *x*2 − *y*2 is evaluated as ((*x* × *x*) − *y* × *y*) (following Kahan's suggested notation in which redundant parentheses direct the compiler to round the (*x* × *x*) term first) using fused multiply–add, then the result may be negative even when *x* = *y* due to the first multiplication discarding low significance bits. This could then lead to an error if, for instance, the square root of the result is then evaluated.

When implemented inside a microprocessor, an FMA can be faster than a multiply operation followed by an add. However, standard industrial implementations based on the original IBM RS/6000 design require a 2*N*-bit adder to compute the sum properly.

Another benefit of including this instruction is that it allows an efficient software implementation of division (see division algorithm) and square root (see methods of computing square roots) operations, thus eliminating the need for dedicated hardware for those operations.

### Dot-product instruction

Some machines combine multiple fused multiply add operations into a single step, e.g. performing a four-element dot-product on two 128-bit SIMD registers `a0×b0 + a1×b1 + a2×b2 + a3×b3` with single cycle throughput.

### Support

The FMA operation is included in IEEE 754-2008.

The 1999 standard of the C programming language supports the FMA operation through the `fma()` standard math library function and the automatic transformation of a multiplication followed by an addition (contraction of floating-point expressions), which can be explicitly enabled or disabled with standard pragmas (`#pragma STDC FP_CONTRACT`). The GCC and Clang C compilers do such transformations by default for processor architectures that support FMA instructions. With GCC, which does not support the aforementioned pragma, this can be globally controlled by the `-ffp-contract` command line option.

The fused multiply–add operation was introduced as "multiply–add fused" in the IBM POWER1 (1990) processor, but has been added to numerous processors:

- IBM POWER1 (1990)
- HP PA-8000 (1996) and above
- Hitachi SuperH SH-4 (1998)
- IBM z/Architecture (since 1998)
- SCE-Toshiba Emotion Engine (1999)
- Intel Itanium (2001)
- STI Cell (2006)
- Fujitsu SPARC64 VI (2007) and above
- (MIPS-compatible) Loongson-2F (2008)
- RISC-V instruction set (2010)
- ARM processors with VFPv4 and/or NEONv2:
  - ARM Cortex-M4F (2010)
  - STM32 Cortex-M33 (VFMA operation)
  - ARM Cortex-A5 (2012)
  - ARM Cortex-A7 (2013)
  - ARM Cortex-A15 (2012)
  - Qualcomm Krait (2012)
  - Apple A6 (2012)
  - All ARMv8 processors
    - Fujitsu A64FX has "Four-operand FMA with Prefix Instruction".
- x86 processors with FMA3 and/or FMA4 instruction set
  - AMD Bulldozer (2011, FMA4 only)
  - AMD Piledriver (2012, FMA3 and FMA4)
  - Intel Haswell (2013, FMA3 only)
  - AMD Steamroller (2014, FMA3 and FMA4)
  - AMD Excavator (2015, FMA3 and FMA4)
  - Intel Skylake (2015, FMA3 only)
  - AMD Zen (2017, FMA3 only)
- Elbrus-8SV (2018)

GPUs and GPGPU boards:

- AMD GPUs (2009) and newer
  - TeraScale 2 "Evergreen"-series based
  - Graphics Core Next-based
- Nvidia GPUs (2010) and newer
  - Fermi-based (2010)
  - Kepler-based (2012)
  - Maxwell-based (2014)
  - Pascal-based (2016)
  - Volta-based (2017)
- Intel GPUs:
  - Integrated GPUs since Sandy Bridge:
  - Intel MIC (2012)
- ARM Mali T600 Series (2012) and above
- Vector Processors:
  - NEC SX-Aurora TSUBASA

## Variants with two or more roundings

### Truncating MAD

A simpler implementation of MADD involves truncating the result of the multiplication before adding. This provides no accuracy benefit (and in fact is less accurate), but was, before 2010, more commonly supported on GPUs than the precise FMA. An example is seen in the "FMAD" instruction of Nvidia PTX.

The OpenCL optimization option `-cl-mad-enable` enables replacing `a * b + c` with `mad(a, b, c)`, the function computing the equivalent expression "with reduced accuracy" in OpenCL 1.0. The accuracy of this option as well as `mad()` has become more nuanced in newer versions of OpenCL, only allowing reduced accuracy in the "embedded profile" as of version 3.0.

### Rounding with extra intermediate precision

The Digital Equipment Corporation (DEC) VAX's `POLY` instruction is used for evaluating polynomials with Horner's rule using a succession of multiply and add steps. Instruction descriptions do not specify whether the multiply and add are performed using a single FMA step. This instruction has been a part of the VAX instruction set since its original 11/780 implementation in 1977. According to Bob Supnik, the machine internally performs the multiplication and addition in extended precision, then converts to the target format. There is therefore a rounding step after multiplication. As a result, although this operation is more precise than a naive `a * b + c` in target format, it does not meet the IEEE definition of FMA.

This behavior is also comparable to using `FLT_EVAL_METHOD == 2` on x87.
