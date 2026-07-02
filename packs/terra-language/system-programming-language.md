---
title: "System programming language"
source: https://en.wikipedia.org/wiki/System_programming_language
domain: terra-language
license: CC-BY-SA-4.0
tags: terra language, lua language, multi stage programming, llvm backend, ahead of time compilation
fetched: 2026-07-02
---

# System programming language

A **system programming language** is a programming language used for system programming; such languages are designed for writing system software, which usually requires different development approaches when compared with application software. Edsger Dijkstra referred to these languages as **machine oriented high order languages**, or **mohol**.

General-purpose programming languages tend to focus on generic features to allow programs written in the language to use the same code on different computing platforms. Examples of such languages include ALGOL and Pascal. This generic quality typically comes at the cost of denying direct access to the machine's internal workings, and this often has negative effects on performance.

System languages, in contrast, are designed not for compatibility, but for performance and ease of access to the underlying computer hardware while still providing high-level programming concepts like structured programming. Examples include Executive Systems Problem Oriented Language (ESPOL) and Systems Programming Language (SPL), both of which are ALGOL-like in syntax but tuned to their respective platforms. Others are cross-platform software, but designed to work close to the hardware, like BLISS, JOVIAL, and BCPL.

Some languages straddle the system and application domains, bridging the gap between these uses. The canonical example is C, which is used widely for both system and application programming. PL/I was an early example. Some modern languages also do this such as Rust and Swift.

## Features

In contrast with application languages, system programming languages typically offer more-direct access to the physical hardware of the machine: an archetypical system programming language in this sense was BCPL. System programming languages often lack built-in input/output (I/O) facilities because a system-software project usually develops its own I/O mechanisms or builds on basic monitor I/O or screen management facilities. The distinction between languages used for system programming and application programming became blurred over time with the widespread popularity of PL/I, C and Pascal.

## History

The earliest system software was written in assembly language mostly because no alternative existed, but also for reasons including efficiency of object code, compiling time, and ease of debugging. Application languages such as FORTRAN were used for system programming, although they usually still required some routines to be written in assembly language.

### Mid-level languages

Mid-level languages "have much of the syntax and facilities of a higher level language, but also provide direct access in the language (and often an assembly language) to machine features." The earliest of these was ESPOL on Burroughs mainframes in about 1960, followed by Niklaus Wirth's PL360 (first written on a Burroughs system as a cross compiler), which had the general syntax of ALGOL 60 but whose statements directly manipulated CPU registers and memory. Other languages in this category include MOL-360 and PL/S.

As an example, a typical PL360 statement is `R9 := R8 and R7 shll 8 or R6`, signifying that registers 8 and 7 should be and'ed together, the result shifted left 8 bits, the result of that or'ed with the contents of register 6, and the final result placed into register 9.

### Higher-level languages

While PL360 is at the semantic level of assembly language, another kind of system programming language operates at a higher semantic level, but has specific extensions designed to make the language suitable for system programming. An early example of this kind of language is LRLTRAN, which extended Fortran with features for character and bit manipulation, pointers, and directly addressed jump tables.

Subsequently, languages such as C were developed, where the combination of features was sufficient to write system software, and a compiler could be developed that generated efficient object programs on modest hardware. Such a language generally omits features that cannot be implemented efficiently, and adds a small number of machine-dependent features needed to access specific hardware abilities; inline assembly code, such as C's `asm` statement, is often used for this purpose. Although many such languages were developed, C and C++ are the ones which survived.

## Major languages

| Language | Originator | Birth date | Influenced by | Used for |
|---|---|---|---|---|
| JOVIAL | System Development Corporation | 1960 | ALGOL 58 | Many systems, mostly military |
| ESPOL | Burroughs Corporation | 1961 | ALGOL 60 | MCP |
| PL/I | IBM, SHARE | 1964 | ALGOL, FORTRAN, some COBOL | Multics, Stratus VOS. Dialects used in PRIMOS, IBM CPF, IBM OS/400. |
| PL/S | IBM | 1960s | PL/I | OS/360 and successors |
| Edinburgh IMP | University of Edinburgh | 1966 | ALGOL 60, Atlas Autocode | Edinburgh Multiple Access System |
| BCPL | Martin Richards | 1967 | CPL | Xerox Alto Executive, TRIPOS |
| PL360 | Niklaus Wirth | 1968 | ALGOL 60 | ALGOL W |
| Pascal | Niklaus Wirth | 1970 | ALGOL W | Apollo AEGIS, MacApp, UCSD p-System, VAXELN, Lisa OS, PERQ OS |
| BLISS | Carnegie Mellon University | 1970 | ALGOL, PL/I | OpenVMS (portions), Hydra |
| Language for Systems Development (LSD or LSyD) | R. Daniel Bergeron, et al. (Brown University) | 1971 | PL/I |   |
| C | Dennis Ritchie | 1972 | BCPL, B | Many operating system kernels, including most Unix-like systems; SQLite |
| System Programming Language (SPL) | Hewlett-Packard | 1972 | ALGOL 60, ESPOL | HP 3000 system software, including MPE |
| PL/M | Gary Kildall | 1973 | PL/I, XPL | CP/M, ISIS, iRMX |
| NEWP | Burroughs | 1970s | ESPOL, ALGOL | MCP |
| PL.8 | IBM | 1970s | PL/I | compiler development, AIX (versions 1 and 2 only), IBM mainframe firmware |
| PL-6 | Honeywell, Inc. | 1970s | PL/I | CP-6 |
| SYMPL | CDC | 1970s | JOVIAL | NOS subsystems, most compilers, FSE editor |
| Transaction Application Language (TAL) | Tandem Computers | 1970s | SPL, C, Pascal | NonStop OS |
| Mesa | Xerox PARC | 1976 | Pascal, ALGOL 68 | Pilot, GlobalView |
| Modula-2 | Niklaus Wirth | 1978 | Pascal, Mesa | Medos-2, portions of IBM OS/400 and PRIMOS. Modula-2+ variant used in ARX, Topaz. |
| C++ | Bjarne Stroustrup | 1979 | C, Simula | BeOS, Haiku, Serenity OS, Symbian. Portions of IBM i, macOS, Microsoft Windows. |
| S3 | ICL | 1980s | ALGOL 68 | ICL VME |
| Ada | Jean Ichbiah, S. Tucker Taft | 1983 | ALGOL 68, Pascal, C++, Eiffel | Military, aerospace mass transportation, high-integrity computation, operating system kernels, iMAX 432, BiiN/OS |
| Oberon | Niklaus Wirth | 1987 | Modula-2 | Oberon System |
| Modula-3 | DEC SRC, Olivetti | 1988 | Modula-2+ | SPIN |
| D | Digital Mars | 2001 | C++ |   |
| Nim | Andreas Rumpf | 2008 | Python, Ada, Lisp, Oberon, C++, Modula-3, Object Pascal |   |
| Go | Google | 2009 | Oberon, C, Pascal | Kubernetes, Docker |
| Rust | Mozilla Research | 2010 | C++, Haskell, Erlang, Ruby | Servo, RedoxOS. Portions of the Linux kernel and of Microsoft Windows. |
| Swift | Apple Inc. | 2014 | C, Objective-C, D, Rust | macOS, iOS, watchOS, and tvOS app development |
| Zig | Andrew Kelley | 2016 | C, C++, LLVM IR, Go, Rust | Bun, TigerBeetle, Mach engine, Ghostty |
| Mojo | Modular Inc. | 2023 | C, C++, Python, Rust, Swift, Zig |   |
