---
title: "PicoLisp"
source: https://en.wikipedia.org/wiki/PicoLisp
domain: picolisp
license: CC-BY-SA-4.0
tags: picolisp language, lisp language, minimalism computing, interpreter computing, s expression
fetched: 2026-07-02
---

# PicoLisp

**PicoLisp** is a programming language, a dialect of the language Lisp. It runs on operating systems including Linux and others that are Portable Operating System Interface (POSIX) compliant. Its most prominent features are simplicity and minimalism. It is built on one internal data type: a cell. On the language level, a programmer can use three different data types (numbers, symbols, and lists) being represented by cells and differentiated by bits at the end of the cell. It is free and open-source software released under an MIT License (X11).

## Features

Functions can accept arbitrary types and numbers of arguments. Macros are needed only in rare cases and are implemented using the quote function. PicoLisp does not include Lisp's lambda function. This is because the quote function is changed to return all its arguments unevaluated, not only the `car` of the first.

A special feature is the intrinsic *create, read, update, and delete* (CRUD) functioning. Persistent symbols are first-class citizens (objects), they are loaded from database files automatically when accessed, and written back when modified. Applications are written using a class hierarchy of entities and relations.

Other features include: Prolog engine, database engine and database queries, distributed databases, inlining of C language functions and native C function calls, child process management, interprocess communication, browser graphical user interface (GUI), and internationalization and localization.

## History

The design of PicoLisp is most similar to the first version of MacLisp, Interlisp and mainly Portable Standard Lisp. It was ported to DOS and SCO Unix. Since 1993, it was used mainly on Linux. In the mid-1990s, database functions were added.

The first versions were written in a mix of C and assembly language. In 1999, a first rewrite from scratch was done, fully in C. In 2002, that version was released under a GNU General Public License (GNU GPL). In 2010, it changed to an MIT/X11 license.

In 2009, the 64-bit version was released, another rewrite, this time written in generic assembly, which in turn is implemented in PicoLisp. This version adds support for coroutines.

In December 2010, a Java version named *Ersatz PicoLisp* was released.

In September 2014, Burger announced the PilMCU project on the PicoLisp development listserv, an effort with George Orais to implement PicoLisp in hardware directly.

In July 2015, Burger announced PilOS - The PicoLisp Operating System, a minimal prototype based on the modification of PilMCU targeting embedded applications. It runs on standard x86-64 PC hardware, directly off the BIOS and includes all the features of 64-bit PicoLisp (minus native function calls, due to the fact there is no other native environment such as the C standard library); in principle, it works as its own operating system.

In the summer of 2016, development of *PilBox* ("PicoLisp Box") – a generic Android app allowing to write apps in pure PicoLisp – was started. It is still being developed and maintained.

In 2021, PicoLisp was re-implemented in LLVM and released as *pil21*. The source language which is compiled to LLVM-IR is also in PicoLisp syntax.

1958

1960

1965

1970

1975

1980

1985

1990

1995

2000

2005

2010

2015

2020

LISP 1, 1.5,

LISP 2

(abandoned)

Maclisp

Interlisp

MDL

Lisp Machine Lisp

Scheme

R5RS

R6RS

R7RS small

NIL

ZIL (Zork Implementation Language)

Franz Lisp

muLisp

Common Lisp

ANSI standard

Le Lisp

MIT Scheme

XLISP

T

Chez Scheme

Emacs Lisp

AutoLISP

PicoLisp

Gambit

EuLisp

ISLISP

OpenLisp

PLT Scheme

Racket

newLISP

GNU Guile

Visual LISP

Clojure

Arc

LFE

Hy
