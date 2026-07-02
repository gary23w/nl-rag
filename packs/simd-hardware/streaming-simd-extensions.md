---
title: "Streaming SIMD Extensions"
source: https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions
domain: simd-hardware
license: CC-BY-SA-4.0
tags: simd hardware, streaming simd extensions, advanced vector extensions, data parallelism
fetched: 2026-07-02
---

# Streaming SIMD Extensions

In computing, **Streaming SIMD Extensions** (**SSE**) is a single instruction, multiple data (SIMD) instruction set extension to the x86 architecture, designed by Intel and introduced in 1999 in its Pentium III series of central processing units (CPUs) shortly after the appearance of Advanced Micro Devices (AMD's) 3DNow!. SSE contains 70 new instructions (65 unique mnemonics using 70 encodings), most of which work on single precision floating-point data. SIMD instructions can greatly increase performance when exactly the same operations are to be performed on multiple data objects. Typical applications are digital signal processing and graphics processing.

Intel's first IA-32 SIMD effort was the MMX instruction set. MMX had two main problems: it re-used existing x87 floating-point registers making the CPUs unable to work on both floating-point and SIMD data at the same time, and it only worked on integers. SSE floating-point instructions operate on a new independent register set, the XMM registers, and adds a few integer instructions that work on MMX registers.

SSE was subsequently expanded by Intel to SSE2, SSE3, SSSE3 and SSE4. Because it supports floating-point math, it had wider applications than MMX and became more popular. The addition of integer support in SSE2 made MMX largely redundant, though further performance increases can be attained in some situations by using MMX in parallel with SSE operations.

SSE was originally called **Katmai New Instructions** (**KNI**), Katmai being the code name for the first Pentium III core revision. During the Katmai project Intel sought to distinguish it from its earlier product line, particularly its flagship Pentium II. It was later renamed **Internet Streaming SIMD Extensions** (**ISSE**), then SSE.

AMD added a subset of SSE, 19 of them, called *new MMX instructions*, and known as several variants and combinations of SSE and MMX, or otherwise as **Integer SSE** (**ISSE**, not to be confused with *Internet Streaming SIMD Extensions*, an early name for SSE) shortly after with the release of the original Athlon in August 1999 (see 3DNow! extensions). AMD eventually added full support for SSE instructions (sometimes referred to as 3DNow! Professional) starting with its Athlon XP (Corvette and Palomino cores) and Duron (Morgan core) processors.

## Registers

SSE originally added eight new 128-bit registers known as `XMM0` through `XMM7`. The AMD64 extensions from AMD added a further eight registers `XMM8` through `XMM15`, and this extension is duplicated in the Intel 64 architecture. There is also a new 32-bit control/status register, `MXCSR`. The registers `XMM8` through `XMM15` are accessible only in 64-bit operating mode.

SSE used only a single data type for XMM registers:

- four 32-bit single-precision floating-point numbers

SSE2 would later expand the usage of the XMM registers to include:

- two 64-bit double-precision floating-point numbers or
- two 64-bit integers or
- four 32-bit integers or
- eight 16-bit short integers or
- sixteen 8-bit bytes or characters.

Because these 128-bit registers are additional machine states that the operating system must preserve across task switches, they are disabled by default until the operating system explicitly enables them. This means that the OS must know how to use the `FXSAVE` and `FXRSTOR` instructions, which is the extended pair of instructions that can save all x86 and SSE register states at once. This support was quickly added to all major IA-32 operating systems.

The first CPU to support SSE, the Pentium III, shared execution resources between SSE and the floating-point unit (FPU). While a compiled application can interleave FPU and SSE instructions side-by-side, the Pentium III will not issue an FPU and an SSE instruction in the same clock cycle. This limitation reduces the effectiveness of pipelining, but the separate XMM registers do allow SIMD and scalar floating-point operations to be mixed without the performance hit from explicit MMX/floating-point mode switching.

## SSE instructions

SSE introduced both scalar and packed floating-point instructions.

### Floating-point instructions

Floating operations are IEEE 754-1985 compliant, with the exception of `RSQRTSS`, which is not specified in the standard.

- Memory-to-register/register-to-memory/register-to-register data movement
  - Scalar – `MOVSS`
  - Packed – `MOVAPS, MOVUPS, MOVLPS, MOVHPS, MOVLHPS, MOVHLPS, MOVMSKPS`
- Arithmetic
  - Scalar – `ADDSS, SUBSS, MULSS, DIVSS, RCPSS, SQRTSS, MAXSS, MINSS, RSQRTSS`
  - Packed – `ADDPS, SUBPS, MULPS, DIVPS, RCPPS, SQRTPS, MAXPS, MINPS, RSQRTPS`
- Compare
  - Scalar – `CMPSS, COMISS, UCOMISS`
  - Packed – `CMPPS`
- Data shuffle and unpacking
  - Packed – `SHUFPS, UNPCKHPS, UNPCKLPS`
- Data-type conversion
  - Scalar – `CVTSI2SS, CVTSS2SI, CVTTSS2SI`
  - Packed – `CVTPI2PS, CVTPS2PI, CVTTPS2PI`
- Bitwise logical operations
  - Packed – `ANDPS, ORPS, XORPS, ANDNPS`

### Integer instructions

- Arithmetic
  - `PMULHUW, PSADBW, PAVGB, PAVGW, PMAXUB, PMINUB, PMAXSW, PMINSW`
- Data movement
  - `PEXTRW, PINSRW`
- Other
  - `PMOVMSKB, PSHUFW`

### Other instructions

- `MXCSR` management
  - `LDMXCSR, STMXCSR`
- Cache and Memory management
  - `MOVNTQ, MOVNTPS, MASKMOVQ, PREFETCH0, PREFETCH1, PREFETCH2, PREFETCHNTA, SFENCE`

## Example

The following simple example demonstrates the advantage of using SSE. Consider an operation like vector addition, which is used very often in computer graphics applications. To add two single precision, four-component vectors together using x86 requires four floating-point addition instructions.

```mw
vec_res.x = v1.x + v2.x;
vec_res.y = v1.y + v2.y;
vec_res.z = v1.z + v2.z;
vec_res.w = v1.w + v2.w;
```

This corresponds to four x86 FADD instructions in the object code. On the other hand, as the following pseudo-code shows, a single 128-bit 'packed-add' instruction can replace the four scalar addition instructions.

```mw
movaps xmm0, [v1] ;xmm0 = v1.w | v1.z | v1.y | v1.x 
addps xmm0, [v2]  ;xmm0 = v1.w+v2.w | v1.z+v2.z | v1.y+v2.y | v1.x+v2.x
movaps [vec_res], xmm0  ;xmm0
```

## Later versions

- SSE2, Willamette New Instructions (WNI), introduced with the Pentium 4, is a major enhancement to SSE. SSE2 adds two major features: double-precision (64-bit) floating-point for all SSE operations, and MMX integer operations on 128-bit XMM registers. In the original SSE instruction set, conversion to and from integers placed the integer data in the 64-bit MMX registers. SSE2 enables the programmer to perform SIMD math on any data type (from 8-bit integer to 64-bit float) entirely with the XMM vector-register file, without the need to use the legacy MMX or FPU registers. It offers an orthogonal set of instructions for dealing with common data types.
- SSE3, also called Prescott New Instructions (PNI), is an incremental upgrade to SSE2, adding a handful of DSP-oriented mathematics instructions and some process (thread) management instructions. It also allowed addition or multiplication of two numbers that are stored in the same register, which wasn't possible in SSE2 and earlier. This capability, known as horizontal in Intel terminology, was the major addition to the SSE3 instruction set. AMD's 3DNow! extension could do the latter too.
- SSSE3, Merom New Instructions (MNI), is an upgrade to SSE3, adding 16 new instructions which include permuting the bytes in a word, multiplying 16-bit fixed-point numbers with correct rounding, and within-word accumulate instructions. SSSE3 is often mistaken for SSE4 as this term was used during the development of the Core microarchitecture.
- SSE4, Penryn New Instructions (PNI), is another major enhancement, adding a dot product instruction, additional integer instructions, a `popcnt` instruction (Population count: count number of bits set to 1, used extensively e.g. in cryptography), and more.
- XOP, FMA4 and CVT16 are new iterations announced by AMD in August 2007 and revised in May 2009.
- Advanced Vector Extensions (AVX), Gesher New Instructions (GNI), is an advanced version of SSE announced by Intel featuring a widened data path from 128 bits to 256 bits and 3-operand instructions (up from 2). Intel released processors in early 2011 with AVX support.
- AVX2 is an expansion of the AVX instruction set.
- AVX-512 (3.1 and 3.2) are 512-bit extensions to the 256-bit Advanced Vector Extensions SIMD instructions for x86 instruction set architecture.

## Identifying

The following programs can be used to determine which, if any, versions of SSE are supported on a system

- Intel Processor Identification Utility
- CPU-Z – CPU, motherboard, and memory identification utility.
- lscpu - provided by the util-linux package in most Linux distributions.
