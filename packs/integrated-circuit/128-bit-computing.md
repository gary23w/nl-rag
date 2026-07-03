---
title: "128-bit computing"
source: https://en.wikipedia.org/wiki/128-bit_computing
domain: integrated-circuit
license: CC-BY-SA-4.0
tags: integrated circuit
fetched: 2026-07-03
---

# 128-bit computing

In computer architecture, **128-bit** integers, memory addresses, or other data units are those that are 128 bits (16 octets) wide. Also, 128-bit central processing unit (CPU) and arithmetic logic unit (ALU) architectures are those that are based on registers, address buses, or data buses of that size.

As of June 2026, there are no mainstream general-purpose processors built to operate on 128-bit *integers* or addresses, although a number of processors do have specialized ways to operate on 128-bit chunks of data as summarized in § Hardware.

## Representation

A processor with 128-bit byte addressing could directly address up to 2128 (over 3.40×1038) bytes, which would greatly exceed the total data captured, created, or replicated on Earth as of 2024, which has been estimated to be around 149 zettabytes (over 276 bytes).

A 128-bit register can store 2128 (over 3.40 × 1038) different values. The range of integer values that can be stored in 128 bits depends on the integer representation used. With the two most common representations, the range is 0 through 340,282,366,920,938,463,463,374,607,431,768,211,455 (2128 − 1) for representation as an (unsigned) binary number, and −170,141,183,460,469,231,731,687,303,715,884,105,728 (−2127) through 170,141,183,460,469,231,731,687,303,715,884,105,727 (2127 − 1) for representation as two's complement.

Quadruple precision (128 bits) floating-point numbers can store 113-bit fixed-point numbers or integers accurately without losing precision (thus 64-bit integers in particular). Quadruple precision floats can also represent any position in the observable universe with at least micrometer precision.

Decimal128 floating-point numbers can represent numbers with up to 34 significant digits.

## Hardware

A 128-bit multicomparator was described by researchers in 1976.

The IBM System/360 Model 85, and IBM System/370 and its successors, support 128-bit floating-point arithmetic.

The Siemens 7.700 and 7.500 series mainframes and their successors support 128-bit floating-point arithmetic.

Most modern CPUs feature single instruction, multiple data (SIMD) instruction sets (Streaming SIMD Extensions, AltiVec etc.) where 128-bit vector registers are used to store several smaller numbers, such as four 32-bit floating-point numbers. A single instruction can then operate on all these values in parallel. However, these processors do not operate on individual numbers that are 128 binary digits in length; only their vector registers have the size of 128 bits.

The DEC VAX supported operations on 128-bit integer ('O' or octaword) and 128-bit floating-point ('H-float' or HFLOAT) datatypes. Support for such operations was an upgrade option rather than being a standard feature. Since the VAX's registers were 32 bits wide, a 128-bit operation used four consecutive registers or four longwords in memory.

The ICL 2900 Series provided a 128-bit accumulator, and its instruction set included 128-bit floating-point and packed decimal arithmetic.

A CPU with 128-bit multimedia extensions was designed by researchers in 1999.

Among the sixth generation of video game consoles, the Dreamcast and the PlayStation 2 used the term *128-bit* in their marketing to describe their capability. The PlayStation 2's CPU had 128-bit SIMD capabilities. Neither console supported 128-bit addressing or 128-bit integer arithmetic.

The RISC-V ISA specification from 2016 includes a reservation for a 128-bit version of the architecture, but the details remain undefined intentionally, because there is yet so little practical experience with such large word size.

## Software

In the same way that compilers emulate, e.g., 64-bit integer arithmetic on architectures with register sizes less than 64 bits, some compilers also support 128-bit integer arithmetic. For example, the GCC C compiler 4.6 and later has a 128-bit integer type `__int128` for some architectures. GCC and compatible compilers signal the presence of 128-bit arithmetic when the macro `__SIZEOF_INT128__` is defined. For the C programming language, 128-bit support is optional, e.g. via the `int128_t` type, or it can be implemented by a compiler-specific extension. The Rust programming language has built-in support for 128-bit integers (originally via LLVM), which is implemented on all platforms. A 128-bit type provided by a C compiler can be available in Perl via the `Math::Int128` module. The C3 programming language provides an implementation of a 128-bit integer data type.

### Other uses

- Universally unique identifiers (UUID) consist of a 128-bit value.
- IPv6 routes computer network traffic amongst a 128-bit range of addresses.
- ZFS is a 128-bit file system.
- 128 bits is a common key size for symmetric ciphers and a common block size for block ciphers in cryptography.
- The IBM i Machine Interface defines all pointers as 128-bit. The Machine Interface instructions are translated to the hardware's real instruction set as required, allowing the underlying hardware to change without needing to recompile the software. Past hardware had a CISC instruction set with 48-bit addressing, while current hardware is 64-bit PowerPC/Power ISA. In the PowerPC/Power ISA implementation, the first four bytes contain information used to identify the type of the object being referenced, and the final eight bytes are used as a virtual memory address. The remaining four bytes are unused, and would allow IBM i applications to be extended to 96-bit addressing in future without requiring code changes.
- Increasing the word size can speed up multiple precision mathematical libraries, with applications to cryptography, and potentially speed up algorithms used in complex mathematical processing (numerical analysis, signal processing, complex photo editing and audio and video processing).
- MD5 is a hash function producing a 128-bit hash value.
- Apache Avro uses a 128-bit random number as synchronization marker for efficient splitting of data files.
