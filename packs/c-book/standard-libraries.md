---
title: "C Programming/Standard libraries"
source: https://en.wikibooks.org/wiki/C_Programming/Standard_libraries
domain: c-book
license: CC-BY-SA-4.0 (Wikibooks C Programming)
tags: c pointers, c arrays, c memory management, c strings
fetched: 2026-07-02
---

# C Programming/Standard libraries

<

C Programming

The **C standard library** is a standardized collection of header files and library routines used to implement common operations, such as input/output and character string handling. Unlike other languages (such as COBOL, Fortran, and PL/I) C does not include built in keywords for these tasks, so nearly all C programs rely on the standard library to operate.

## History

The C programming language previously did not provide any elementary functions, such as I/O operations. Over time, user communities of C shared ideas and implementations to provide those functions. These ideas became common, and were eventually incorporated into the definition of the standardized C programming language in 1989. These are now called the **C standard libraries**.

Both Unix and C were created at AT&T's Bell Laboratories in the late 1960s and early 1970s. During the 1970s the C programming language became increasingly popular, with many universities and organizations beginning to create their own variations of the language for their own projects. By the start of the 1980s compatibility problems between the various C implementations became apparent. In 1983 the American National Standards Institute (ANSI) formed a committee to establish a standard specification of C known as "ANSI C". This work culminated in the creation of the so-called **C89** standard in 1989. Part of the resulting standard was a set of software libraries called the **ANSI C standard library**.

Later revisions of the C standard have added several new required header files to the library. Support for these new extensions varies between implementations.

The headers **<iso646.h>**, **<wchar.h>**, and **<wctype.h>** were added with Normative Addendum 1 (hereafter abbreviated as **NA1**), an addition to the C Standard ratified in 1995.

The headers **<complex.h>**, **<fenv.h>**, **<inttypes.h>**, **<stdbool.h>**, **<stdint.h>**, and **<tgmath.h>** were added with **C99**, a revision to the C Standard published in 1999.

## Design

The declaration of each function is kept in a header file, while the actual implementation of functions are separated into a library file. The naming and scope of headers have become common but the organization of libraries still remains diverse. The standard library is usually shipped along with a compiler. Since C compilers often provide extra functions that are not specified in ANSI C, a standard library with a particular compiler is mostly incompatible with standard libraries of other compilers.

Much of the C standard library has been shown to have been well-designed. A few parts, with the benefit of hindsight, are regarded as mistakes. The string input functions `gets()` (and the use of `scanf()` to read string input) are the source of many buffer overflows, and most programming guides recommend avoiding this usage. Another oddity is `strtok()`, a function that is designed as a primitive lexical analyser but is highly "fragile" and difficult to use.

## ANSI standard

The ANSI C standard library consists of 24 C header files which can be included into a programmer's project with a single directive. Each header file contains one or more function declarations, data type definitions and macros. The contents of these header files follows.

In comparison to some other languages (for example Java) the standard library is minuscule. The library provides a basic set of mathematical functions, string manipulation, type conversions, and file and console-based I/O. It does not include a standard set of "container types" like the C++ Standard Template Library, let alone the complete graphical user interface (GUI) toolkits, networking tools, and profusion of other functions that Java provides as standard. The main advantage of the small standard library is that providing a working ANSI C environment is much easier than it is with other languages, and consequently porting C to a new platform is relatively easy.

Many other libraries have been developed to supply equivalent functions to that provided by other languages in their standard library. For instance, the GNOME desktop environment project has developed the GTK+ graphics toolkit and GLib, a library of container data structures, and there are many other well-known examples. The variety of libraries available has meant that some superior toolkits have proven themselves through history. The considerable downside is that they often do not work particularly well together, programmers are often familiar with different sets of libraries, and a different set of them may be available on any particular platform.

### ANSI C library header files

| **<assert.h>** | Contains the assert macro, used to assist with detecting logical errors and other types of bug in debugging versions of a program. |
|---|---|
| **<complex.h>** | A set of functions for manipulating complex numbers. (New with **C99**) |
| **<ctype.h>** | This header file contains functions used to classify characters by their types or to convert between upper and lower case in a way that is independent of the used character set (typically ASCII or one of its extensions, although implementations utilizing EBCDIC are also known). |
| **<errno.h>** | For testing error codes reported by library functions. |
| **<fenv.h>** | For controlling floating-point environment. (New with **C99**) |
| **<float.h>** | Contains defined constants specifying the implementation-specific properties of the floating-point library, such as the minimum difference between two different floating-point numbers (_EPSILON), the maximum number of digits of accuracy (_DIG) and the range of numbers which can be represented (_MIN, _MAX). |
| **<inttypes.h>** | For precise conversion between integer types. (New with **C99**) |
| **<iso646.h>** | For programming in ISO 646 variant character sets. (New with **NA1**) |
| **<limits.h>** | Contains defined constants specifying the implementation-specific properties of the integer types, such as the range of numbers which can be represented (_MIN, _MAX). |
| **<locale.h>** | For setlocale() and related constants. This is used to choose an appropriate locale. |
| **<math.h>** | For computing common mathematical functions -- see Further math or C++ Programming/Code/Standard C Library/Math for details. |
| **<setjmp.h>** | setjmp and longjmp, which are used for non-local exits |
| **<signal.h>** | For controlling various exceptional conditions |
| **<stdarg.h>** | For accessing a varying number of arguments passed to functions. |
| **<stdbool.h>** | For a boolean data type. (New with **C99**) |
| **<stdint.h>** | For defining various integer types. (New with **C99**) |
| **<stddef.h>** | For defining several useful types and macros. |
| **<stdio.h>** | Provides the core input and output capabilities of the C language. This file includes the venerable `printf` function. |
| **<stdlib.h>** | For performing a variety of operations, including conversion, pseudo-random numbers, memory allocation, process control, environment, signalling, searching, and sorting. |
| **<string.h>** | For manipulating several kinds of strings. |
| **<tgmath.h>** | For type-generic mathematical functions. (New with **C99**) |
| **<time.h>** | For converting between various time and date formats. |
| **<wchar.h>** | For manipulating wide streams and several kinds of strings using wide characters - key to supporting a range of languages. (New with **NA1**) |
| **<wctype.h>** | For classifying wide characters. (New with **NA1**) |

## Common support libraries

While not standardized, C programs may depend on a runtime library of routines which contain code the compiler uses at runtime. The code that initializes the process for the operating system, for example, before calling `main()`, is implemented in the C Run-Time Library for a given vendor's compiler. The Run-Time Library code might help with other language feature implementations, like handling uncaught exceptions or implementing floating point code.

The C standard library only documents that the specific routines mentioned in this article are available, and how they behave. Because the compiler implementation might depend on these additional implementation-level functions to be available, it is likely the vendor-specific routines are packaged with the C Standard Library in the same module, because they're both likely to be needed by any program built with their toolset.

Though often confused with the C Standard Library because of this packaging, the C Runtime Library is not a standardized part of the language and is vendor-specific.

## Compiler built-in functions

Some compilers (for example, GCC) provide built-in versions of many of the functions in the C standard library; that is, the implementations of the functions are written into the compiled object file, and the program calls the built-in versions instead of the functions in the C library shared object file. This reduces function call overhead, especially if function calls are replaced with inline variants, and allows other forms of optimization (as the compiler knows the control-flow characteristics of the built-in variants), but may cause confusion when debugging (for example, the built-in versions cannot be replaced with instrumented variants).

## POSIX standard library

POSIX, (along with the Single Unix Specification), specifies a number of routines that should be available over and above those in the C standard library proper; these are often implemented alongside the C standard library functions, with varying degrees of closeness. For example, glibc implements functions such as fork within libc.so, but before NPTL was merged into glibc it constituted a separate library with its own linker flag. Often, this POSIX-specified function will be regarded as part of the library; the C library proper may be identified as the ANSI or ISO C library.

The following libraries are recognized by POSIX:

| **c** | This option shall make available all interfaces referenced in the System Interfaces volume of POSIX.1-2008, with the possible exception of those interfaces listed as residing in <aio.h>, <arpa/inet.h>, <complex.h>, <fenv.h>, <math.h>, <mqueue.h>, <netdb.h>, <net/if.h>, <netinet/in.h>, <pthread.h>, <sched.h>, <semaphore.h>, <spawn.h>, <sys/socket.h>, pthread_kill(), and pthread_sigmask() in <signal.h>, <trace.h>, interfaces marked as optional in <sys/mman.h>, interfaces marked as ADV (Advisory Information) in <fcntl.h>, and interfaces beginning with the prefix clock_ or time_ in <time.h>. This option shall not be required to be present to cause a search of this library. |
|---|---|
| **l** | This option shall make available all interfaces required by the C-language output of lex that are not made available through the -l c option. (The flex program, a clone of lex, uses fl instead of l.) |
| **pthread** | This option shall make available all interfaces referenced in <pthread.h> and pthread_kill() and pthread_sigmask() referenced in <signal.h>. An implementation may search this library in the absence of this option. |
| **m** | This option shall make available all interfaces referenced in <math.h>, <complex.h>, and <fenv.h>. An implementation may search this library in the absence of this option. |
| **rt** | This option shall make available all interfaces referenced in <aio.h>, <mqueue.h>, <sched.h>, <semaphore.h>, and <spawn.h>, interfaces marked as optional in <sys/mman.h>, interfaces marked as ADV (Advisory Information) in <fcntl.h>, and interfaces beginning with the prefix clock_ and time_ in <time.h>. An implementation may search this library in the absence of this option. |
| **trace** | This option shall make available all interfaces referenced in <trace.h>. An implementation may search this library in the absence of this option. |
| **xnet** | This option shall make available all interfaces referenced in <arpa/inet.h>, <netdb.h>, <net/if.h>, <netinet/in.h>, and <sys/socket.h>. An implementation may search this library in the absence of this option. |
| **y** | This option shall make available all interfaces required by the C-language output of yacc that are not made available through the -l c option. (Some clones of yacc, including bison and byacc, include the entire library in the generated file, so it is not necessary to use -l y.) |
