---
title: "Clang"
source: https://en.wikipedia.org/wiki/Clang
domain: safe-stack
license: CC-BY-SA-4.0
tags: safe stack isolation, unsafe stack separation, control data protection, code pointer integrity
fetched: 2026-07-02
---

# Clang

**Clang** (/ˈklæŋ/) is a compiler front end for the programming languages C, C++, Objective-C, and Objective-C++ and the software frameworks OpenMP, OpenCL, RenderScript, CUDA, SYCL, and HIP. It acts as a drop-in replacement for the GNU Compiler Collection (GCC), supporting most of its compiling flags and unofficial language extensions. It includes a static analyzer and several code analysis tools.

Clang operates in tandem with the LLVM compiler back end and has been a subproject of LLVM 2.6 and later. As with LLVM, it is free and open-source software under the Apache 2.0 software license. Its contributors include Apple, IBM, Microsoft, Google, ARM, Sony, Intel and AMD.

Clang 22 has full support for all published C++ standards up to C++17, implements most features of C++20 and C++23, and has initial support for the C++26 standard. Since v16.0.0, Clang compiles C++ using the GNU++17 dialect by default, which includes features from the C++17 standard and conforming GNU extensions.

## Background

In 2005, Apple Inc. made extensive use of LLVM in several commercial products, including the iOS SDK and Xcode 3.1. An OpenGL code compiler for OS X that converts OpenGL calls into more fundamental calls for graphics processing units (GPU) that do not support certain features was one of the first uses of LLVM. This enabled Apple to support OpenGL on computers using Intel GMA chipsets, increasing performance on those machines.

The LLVM project originally intended to use GCC's front end. The GCC source code, however, is large and somewhat cumbersome; as one long-time GCC developer put it, referring to LLVM, "Trying to make the hippo dance is not really a lot of fun." Besides, Apple software uses Objective-C, which is a low priority for GCC developers. As such, GCC does not integrate smoothly into Apple's integrated development environment. Finally, GCC's license agreement, the GNU General Public License (GPL) version 3, requires developers who distribute extensions or modified versions of GCC to make their source code available, but LLVM's permissive software license doesn't require this.

For these reasons, Apple developed Clang, a new compiler front end which supports C, Objective-C and C++. In July 2007, the project received the approval for becoming open-source.

## Design

Clang works in tandem with LLVM. The combination of Clang and LLVM provides most of the toolchain for replacing the GCC stack. One of Clang's main goals is to provide a library-based architecture, so that the compiler could interoperate with other tools that interact with source code, such as integrated development environments (IDE). In contrast, GCC works in a compile-link-debug workflow; integrating it with other tools is not always easy. For instance, GCC uses a step called *fold* that is key to the overall compile process, which has the side effect of translating the code tree into a form that looks unlike the original source code. If an error is found during or after the fold step, it can be difficult to translate that back into one location in the original source. Besides, vendors using the GCC stack within IDEs must use separate tools to index the code, to provide features like syntax highlighting and intelligent code completion.

Clang retains more information during the compiling process than GCC, and preserves the overall form of the original code, making it easier to map errors back into the original source. Clang's error reports are more detailed, specific, and machine-readable, so IDEs can index the compiler's output. Modular design of the compiler can offer source code indexing, syntax checking, and other features normally associated with rapid application development systems. The parse tree is also more suitable for supporting automated code refactoring, as it directly represents the original source code.

Clang compiles only C-like languages, such as C, C++, Objective-C, and Objective-C++. In many cases, Clang can replace GCC as needed, with no other effects on the toolchain as a whole. It supports most of the commonly used GCC options. A Fortran project, Flang was in-progress in 2022. However, for other languages, such as Ada, LLVM remains dependent on GCC or another compiler front end.

### Flang

The *Flang* project, by Nvidia and The Portland Group, adds Fortran support. Flang is LLVM's Fortran frontend, often referred to as *LLVM Flang* to differentiate it from *Classic Flang*. These are two separate and independent Fortran compilers. LLVM Flang is under active development. As of October 2023, development versions of Flang were in progress and could be downloaded from the LLVM Project.

## Performance and GCC compatibility

Clang is compatible with GCC. Its command-line interface shares many of GCC's flags and options. Clang implements many GNU language extensions and compiler intrinsics, some of which are purely for compatibility. For example, even though Clang implements atomic intrinsics which correspond exactly with C11 atomics, it also implements GCC's `__sync_*` intrinsics for compatibility with GCC and the C++ Standard Library (libstdc++). Clang also maintains application binary interface (ABI) compatibility with GCC-generated object code. In practice, Clang is a drop-in replacement for GCC.

Clang's developers aim to reduce memory footprint and increase compiling speed compared to other compilers, such as GCC. In October 2007, they report that Clang compiled the Carbon libraries more than twice as fast as GCC, while using about one-sixth GCC's memory and disk space. By 2011, Clang seemed to retain this advantage in compiler performance. As of mid-2014, Clang still consistently compiles faster than GCC in a mixed compile time and program performance benchmark. However, by 2019, Clang is significantly slower at compiling the Linux Kernel than GCC while remaining slightly faster at compiling LLVM.

While Clang has historically been faster than GCC at compiling, the output quality has lagged behind. As of 2014, performance of Clang-compiled programs lagged behind performance of the GCC-compiled program, sometimes by large factors (up to 5.5x), replicating earlier reports of slower performance. Both compilers have evolved to increase their performance since then, with the gap narrowing:

- Comparisons in November 2016 between GCC 4.8.2 versus clang 3.4, on a large harness of test files shows that GCC outperforms clang by approximately 17% on well-optimized source code. Test results are code-specific, and unoptimized C source code can reverse such differences. The two compilers thus seem broadly comparable.
- Comparisons in 2019 on Intel Ice Lake has shown that programs generated by Clang 10 has achieved 96% of the performance of GCC 10 over 41 different benchmarks (while winning 22 and losing 19 out of them).
- Another comparison conducted in 2023 revealed that programs compiled using Clang now match the performance of those compiled with GCC. On average, Clang 16 surpasses GCC 13 by 6%.

## Interface

`libclang` provides a C interface, providing a relatively small API. Exposed functionality includes: parsing source code into an AST, loading ASTs, traversing the AST, associating source locations with elements within the AST.

## Status history

This table presents only significant steps and releases in Clang history.

| Date | Highlights |
|---|---|
| 11 July 2007 | Clang front-end released under open-source licence |
| 25 February 2009 | Clang/LLVM can compile a working FreeBSD kernel. |
| 16 March 2009 | Clang/LLVM can compile a working DragonFly BSD kernel. |
| 23 October 2009 | Clang 1.0 released, with LLVM 2.6 for the first time. |
| December 2009 | Code generation for C and Objective-C reach production quality. Support for C++ and Objective-C++ still incomplete. Clang C++ can parse GCC 4.2 libstdc++ and generate working code for non-trivial programs, and can compile itself. |
| 2 February 2010 | Clang self-hosting. |
| 20 May 2010 | Clang latest version built the Boost C++ libraries successfully, and passed nearly all tests. |
| 10 June 2010 | Clang/LLVM becomes integral part of FreeBSD, but default compiler is still GCC. |
| 25 October 2010 | Clang/LLVM can compile a working modified Linux kernel. |
| January 2011 | Preliminary work completed to support the draft C++0x standard, with a few of the draft's new features supported in Clang development version. |
| 10 February 2011 | Clang can compile a working HotSpot Java virtual machine. |
| 19 January 2012 | Clang becomes an optional component in NetBSD cross-platform build system, but GCC is still default. |
| 29 February 2012 | Clang 3.0 can rebuild 91.2% of the Debian archive. |
| 29 February 2012 | Clang becomes default compiler in MINIX 3 |
| 12 May 2012 | Clang/LLVM announced to replace GCC in FreeBSD. |
| 5 November 2012 | Clang becomes default compiler in FreeBSD 10.x on amd64/i386. |
| 18 February 2013 | Clang/LLVM can compile a working modified Android Linux Kernel for Nexus 7. |
| 19 April 2013 | Clang is C++11 feature complete. |
| 6 November 2013 | Clang is C++14 feature complete. |
| 11 September 2014 | Clang 3.5 can rebuild 94.3% of the Debian archive. The percentage of failures has dropped by 1.2% per release since January 2013, mainly due to increased compatibility with GCC flags. |
| 27 Feb 2015 | Clang 3.6.0 released. The default C version becomes `-std=gnu11`. |
| October 2016 | Clang becomes default compiler for Android (and later only compiler supported by Android NDK). |
| 13 March 2017 | Clang 4.0.0 released |
| 26 July 2017 | Clang becomes default compiler in OpenBSD 6.2 on amd64/i386. |
| 7 September 2017 | Clang 5.0.0 released |
| 19 January 2018 | Clang becomes default compiler in OpenBSD 6.3 on arm. |
| 5 March 2018 | Clang is now used to build Google Chrome for Windows. |
| 8 March 2018 | Clang 6.0.0 released. The default C++ version becomes `-std=gnu++14`. |
| 5 September 2018 | Clang is now used to build Firefox for Windows. |
| 19 September 2018 | Clang 7.0.0 released |
| 20 March 2019 | Clang 8.0.0 released |
| 1 July 2019 | Clang becomes default compiler in OpenBSD 6.6 on mips64. |
| 19 September 2019 | Clang 9.0.0 released with official RISC-V target support. |
| 29 February 2020 | Clang becomes the only C compiler in the FreeBSD base system, with the removal of GCC. |
| 24 March 2020 | Clang 10.0.0 released |
| 2 April 2020 | Clang becomes default compiler in OpenBSD 6.7 on powerpc. |
| 12 October 2020 | Clang 11.0.0 released. The default C version becomes `-std=gnu17`. |
| 21 December 2020 | Clang becomes default compiler in OpenBSD 6.9 on mips64el. |
| 14 April 2021 | Clang 12.0.0 released |
| 4 October 2021 | Clang 13.0.0 released |
| 25 March 2022 | Clang 14.0.0 released |
| 6 September 2022 | Clang 15.0.0 released |
| 17 March 2023 | Clang 16.0.0 released. The default C++ version becomes `-std=gnu++17`. |
| 9 September 2023 | Clang 17.0.1 released |
| 8 March 2024 | Clang 18.1.1 released |
| 17 September 2024 | Clang 19.1.0 released |
| 4 March 2025 | Clang 20.1.0 released |
| 26 August 2025 | Clang 21.1.0 released |
| 24 February 2026 | Clang 22.1.0 released |
