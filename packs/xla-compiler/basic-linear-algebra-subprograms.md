---
title: "Basic Linear Algebra Subprograms"
source: https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms
domain: xla-compiler
license: CC-BY-SA-4.0
tags: xla compiler, linear algebra compilation, just in time compilation, kernel fusion
fetched: 2026-07-02
---

# Basic Linear Algebra Subprograms

**Basic Linear Algebra Subprograms** (**BLAS**) is a specification that prescribes a set of low-level routines for performing common linear algebra operations such as vector addition, scalar multiplication, dot products, linear combinations, and matrix multiplication. They are the *de facto* standard low-level routines for linear algebra libraries; the routines have bindings for both C ("CBLAS interface") and Fortran ("BLAS interface"). Although the BLAS specification is general, BLAS implementations are often optimized for speed on a particular machine, so using them can bring substantial performance benefits. BLAS implementations will take advantage of special floating point hardware such as vector registers or SIMD instructions.

It originated as a Fortran library in 1979 and its interface was standardized by the BLAS Technical (BLAST) Forum, whose latest BLAS report can be found on the netlib website. This Fortran library is known as the *reference implementation* (sometimes confusingly referred to as *the* BLAS library) and is not optimized for speed but is in the public domain.

Most libraries that offer linear algebra routines conform to the BLAS interface, allowing library users to develop programs that are indifferent to the BLAS library being used.

Many BLAS libraries have been developed, targeting various different hardware platforms. Examples includes cuBLAS (NVIDIA GPU, GPGPU), rocBLAS (AMD GPU), and OpenBLAS. Examples of CPU-based BLAS library branches include: OpenBLAS, BLIS (BLAS-like Library Instantiation Software), Arm Performance Libraries, ATLAS, and Intel Math Kernel Library (iMKL). AMD maintains a fork of BLIS that is optimized for the AMD platform. ATLAS is a portable library that automatically optimizes itself for an arbitrary architecture. iMKL is a freeware and proprietary vendor library optimized for x86 and x86-64 with a performance emphasis on Intel processors. OpenBLAS is an open-source library that is hand-optimized for many of the popular architectures. The LINPACK benchmarks rely heavily on the BLAS routine `gemm` for its performance measurements.

Many numerical software applications use BLAS-compatible libraries to do linear algebra computations, including LAPACK, LINPACK, Armadillo, GNU Octave, Mathematica, MATLAB, NumPy, R, Julia and Lisp-Stat.

The C++ `std::linalg` library, introduced in C++26, is based on BLAS.

## Background

With the advent of numerical programming, sophisticated subroutine libraries became useful. These libraries would contain subroutines for common high-level mathematical operations such as root finding, matrix inversion, and solving systems of equations. The language of choice was FORTRAN. The most prominent numerical programming library was IBM's Scientific Subroutine Package (SSP). These subroutine libraries allowed programmers to concentrate on their specific problems and avoid re-implementing well-known algorithms. The library routines would also be better than average implementations; matrix algorithms, for example, might use full pivoting to get better numerical accuracy. The library routines would also have more efficient routines. For example, a library may include a program to solve a matrix that is upper triangular. The libraries would include single-precision and double-precision versions of some algorithms.

Initially, these subroutines used hard-coded loops for their low-level operations. For example, if a subroutine needed to perform a matrix multiplication, then the subroutine would have three nested loops. Linear algebra programs have many common low-level operations (the so-called "kernel" operations, not related to operating systems). Between 1973 and 1977, several of these kernel operations were identified. These kernel operations became defined subroutines that math libraries could call. The kernel calls had advantages over hard-coded loops: the library routine would be more readable, there were fewer chances for bugs, and the kernel implementation could be optimized for speed. A specification for these kernel operations using scalars and vectors, the level-1 Basic Linear Algebra Subroutines (BLAS), was published in 1979. BLAS was used to implement the linear algebra subroutine library LINPACK.

The BLAS abstraction allows customization for high performance. For example, LINPACK is a general purpose library that can be used on many different machines without modification. LINPACK could use a generic version of BLAS. To gain performance, different machines might use tailored versions of BLAS. As computer architectures became more sophisticated, vector machines appeared. BLAS for a vector machine could use the machine's fast vector operations. (While vector processors eventually fell out of favor, vector instructions in modern CPUs are essential for optimal performance in BLAS routines.)

Other machine features became available and could also be exploited. Consequently, BLAS was augmented from 1984 to 1986 with level-2 kernel operations that concerned vector-matrix operations. Memory hierarchy was also recognized as something to exploit. Many computers have cache memory that is much faster than main memory; keeping matrix manipulations localized allows better usage of the cache. In 1987 and 1988, the level 3 BLAS were identified to do matrix-matrix operations. The level 3 BLAS encouraged block-partitioned algorithms. The LAPACK library uses level 3 BLAS.

The original BLAS concerned only densely stored vectors and matrices. Further extensions to BLAS, such as for sparse matrices, have been addressed.

## Functionality

BLAS functionality is categorized into three sets of routines called "levels", which correspond to both the chronological order of definition and publication, as well as the degree of the polynomial in the complexities of algorithms; Level 1 BLAS operations typically take linear time, *O*(*n*), Level 2 operations quadratic time and Level 3 operations cubic time. Modern BLAS implementations typically provide all three levels.

### Level 1

This level consists of all the routines described in the original presentation of BLAS (1979), which defined only *vector operations* on strided arrays: dot products, vector norms, a generalized vector addition of the form

${\boldsymbol {y}}\leftarrow \alpha {\boldsymbol {x}}+{\boldsymbol {y}}$

(called "`axpy`", "a x plus y") and several other operations.

### Level 2

This level contains *matrix-vector operations* including, among other things, a *ge*neralized *m*atrix-*v*ector multiplication (`gemv`):

${\boldsymbol {y}}\leftarrow \alpha {\boldsymbol {A}}{\boldsymbol {x}}+\beta {\boldsymbol {y}}$

as well as a solver for ***x*** in the linear equation

${\boldsymbol {T}}{\boldsymbol {x}}={\boldsymbol {y}}$

with ***T*** being triangular. Design of the Level 2 BLAS started in 1984, with results published in 1988. The Level 2 subroutines are especially intended to improve performance of programs using BLAS on vector processors, where Level 1 BLAS are suboptimal "because they hide the matrix-vector nature of the operations from the compiler."

### Level 3

This level, formally published in 1990, contains *matrix-matrix operations*, including a "general matrix multiplication" (`gemm`), of the form

${\boldsymbol {C}}\leftarrow \alpha {\boldsymbol {A}}{\boldsymbol {B}}+\beta {\boldsymbol {C}},$

where ***A*** and ***B*** can optionally be transposed or hermitian-conjugated inside the routine, and all three matrices may be strided. The ordinary matrix multiplication ***A B*** can be performed by setting *α* to one and ***C*** to an all-zeros matrix of the appropriate size.

Also included in Level 3 are routines for computing

${\boldsymbol {B}}\leftarrow \alpha {\boldsymbol {T}}^{-1}{\boldsymbol {B}},$

where ***T*** is a triangular matrix, among other functionality.

Due to the ubiquity of matrix multiplications in many scientific applications, including for the implementation of the rest of Level 3 BLAS, and because faster algorithms exist beyond the obvious repetition of matrix-vector multiplication, `gemm` is a prime target of optimization for BLAS implementers. E.g., by decomposing one or both of ***A***, ***B*** into block matrices, `gemm` can be implemented recursively. This is one of the motivations for including the *β* parameter, so the results of previous blocks can be accumulated. Note that this decomposition requires the special case *β* = 1 which many implementations optimize for, thereby eliminating one multiplication for each value of ***C***. This decomposition allows for better locality of reference both in space and time of the data used in the product. This, in turn, takes advantage of the cache on the system. For systems with more than one level of cache, the blocking can be applied a second time to the order in which the blocks are used in the computation. Both of these levels of optimization are used in implementations such as ATLAS. More recently, implementations by Kazushige Goto have shown that blocking only for the L2 cache, combined with careful amortizing of copying to contiguous memory to reduce TLB misses, is superior to ATLAS. A highly tuned implementation based on these ideas is part of the GotoBLAS, OpenBLAS and BLIS.

A common variation of `gemm` is the `gemm3m`, which calculates a complex product using "three real matrix multiplications and five real matrix additions instead of the conventional four real matrix multiplications and two real matrix additions", an algorithm similar to Strassen algorithm first described by Peter Ungar.

## Implementations

**Accelerate**

Apple

's framework for

macOS

and

iOS

, which includes tuned versions of

BLAS

and

LAPACK

.

**Arm Performance Libraries**

Arm Performance Libraries

, supporting Arm 64-bit

AArch64

-based processors, available from

Arm

.

**ATLAS**

Automatically Tuned Linear Algebra Software

, an

open source

implementation of BLAS

APIs

for

C

and

Fortran 77

.

**BLIS**

BLAS-like Library Instantiation Software framework for rapid instantiation. Optimized for most modern CPUs. BLIS is a complete refactoring of the GotoBLAS that reduces the amount of code that must be written for a given platform.

**C++ AMP BLAS**

The

C++ AMP

BLAS Library is an

open source

implementation of BLAS for Microsoft's AMP language extension for Visual C++.

**cuBLAS**

Optimized BLAS for Nvidia-based GPU cards, requiring few additional library calls.

**NVBLAS**

Optimized BLAS for Nvidia-based GPU cards, providing only Level 3 functions, but as direct drop-in replacement for other BLAS libraries.

**clBLAS**

An

OpenCL

implementation of BLAS by AMD. Part of the AMD Compute Libraries.

**clBLAST**

A tuned

OpenCL

implementation of most of the BLAS api.

**Eigen BLAS**

A

Fortran 77

and

C

BLAS library implemented on top of the

MPL

-licensed

Eigen library

, supporting

x86

,

x86-64

,

ARM (NEON)

, and

PowerPC

architectures.

**ESSL**

IBM

's Engineering and Scientific Subroutine Library, supporting the

PowerPC

architecture under

AIX

and

Linux

.

**GotoBLAS**

Kazushige Goto

's BSD-licensed implementation of BLAS, tuned in particular for

Intel

Nehalem

/

Atom

,

VIA

Nanoprocessor

,

AMD

Opteron

.

**GNU Scientific Library**

Multi-platform implementation of many numerical routines. Contains a CBLAS interface.

**HP MLIB**

HP

's Math library supporting

IA-64

,

PA-RISC

,

x86

and

Opteron

architecture under

HP-UX

and

Linux

.

**Intel MKL**

The

Intel

Math Kernel Library

, supporting x86 32-bits and 64-bits, available free from

Intel

.

Includes optimizations for Intel

Pentium

,

Core

and Intel

Xeon

CPUs and Intel

Xeon Phi

; support for

Linux

,

Windows

and

macOS

.

**MathKeisan**

NEC

's math library, supporting

NEC SX architecture

under

SUPER-UX

, and

Itanium

under

Linux

**Netlib BLAS**

The official reference implementation on

Netlib

, written in

Fortran 77

.

**Netlib CBLAS**

Reference

C

interface to the BLAS. It is also possible (and popular) to call the Fortran BLAS from C.

**OpenBLAS**

Optimized BLAS based on GotoBLAS, supporting

x86

,

x86-64

,

MIPS

,

ARM

and

RISC-V

processors.

**PDLIB/SX**

NEC

's Public Domain Mathematical Library for the NEC

SX-4

system.

**rocBLAS**

Implementation that runs on

AMD

GPUs via

ROCm

.

**SCSL**

SGI

's Scientific Computing Software Library contains BLAS and LAPACK implementations for SGI's

Irix

workstations.

**Sun Performance Library**

Optimized BLAS and LAPACK for

SPARC

,

Core

and

AMD64

architectures under

Solaris

8, 9, and 10 as well as Linux.

**uBLAS**

A generic

C++

template class library providing BLAS functionality. Part of the

Boost library

. It provides bindings to many hardware-accelerated libraries in a unifying notation. Moreover, uBLAS focuses on correctness of the algorithms using advanced C++ features.

### Libraries using BLAS

**Armadillo**

Armadillo

is a C++ linear algebra library aiming towards a good balance between speed and ease of use. It employs template classes, and has optional links to BLAS/ATLAS and LAPACK. It is sponsored by

NICTA

(in Australia) and is licensed under a free license.

**LAPACK**

LAPACK is a higher level Linear Algebra library built upon BLAS. Like BLAS, a reference implementation exists, but many alternatives like libFlame and MKL exist.

**Mir**

An

LLVM

-accelerated generic numerical library for science and machine learning written in

D

. It provides generic linear algebra subprograms (GLAS). It can be built on a CBLAS implementation.

## Similar libraries (not compatible with BLAS)

**Elemental**

Elemental is an open source software for

distributed-memory

dense and sparse-direct linear algebra and optimization.

**HASEM**

is a C++ template library, being able to solve linear equations and to compute eigenvalues. It is licensed under BSD License.

**LAMA**

The Library for Accelerated Math Applications (

LAMA

) is a C++ template library for writing numerical solvers targeting various kinds of hardware (e.g.

GPUs

through

CUDA

or

OpenCL

) on

distributed memory

systems, hiding the hardware specific programming from the program developer

**MTL4**

The

Matrix Template Library

version 4 is a generic

C++

template library providing sparse and dense BLAS functionality. MTL4 establishes an intuitive interface (similar to

MATLAB

) and broad applicability thanks to

generic programming

.

## Sparse BLAS

Several extensions to BLAS for handling sparse matrices have been suggested over the course of the library's history; a small set of sparse matrix kernel routines was finally standardized in 2002.

## Batched BLAS

The traditional BLAS functions have been also ported to architectures that support large amounts of parallelism such as GPUs. Here, the traditional BLAS functions provide typically good performance for large matrices. However, when computing e.g., matrix-matrix-products of many small matrices by using the GEMM routine, those architectures show significant performance losses. To address this issue, in 2017 a batched version of the BLAS function has been specified.

Taking the GEMM routine from above as an example, the batched version performs the following computation simultaneously for many matrices:

${\boldsymbol {C}}[k]\leftarrow \alpha {\boldsymbol {A}}[k]{\boldsymbol {B}}[k]+\beta {\boldsymbol {C}}[k]\quad \forall k$

The index k in square brackets indicates that the operation is performed for all matrices k in a stack. Often, this operation is implemented for a strided batched memory layout where all matrices follow concatenated in the arrays A , B and C .

Batched BLAS functions can be a versatile tool and allow e.g. a fast implementation of exponential integrators and Magnus integrators that handle long integration periods with many time steps. Here, the matrix exponentiation, the computationally expensive part of the integration, can be implemented in parallel for all time-steps by using Batched BLAS functions.
