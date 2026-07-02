---
title: "Clean (programming language)"
source: https://en.wikipedia.org/wiki/Clean_(programming_language)
domain: clean-language
license: CC-BY-SA-4.0
tags: clean language, uniqueness type, graph reduction, purely functional programming, lazy evaluation
fetched: 2026-07-02
---

# Clean (programming language)

**Clean** is a general-purpose purely functional programming language. Originally called the **Concurrent Clean System** or the **Clean System**, it has been developed by a group of researchers from the Radboud University in Nijmegen since 1987. Although development of the language has slowed, some researchers are still working in the language. In 2018, a spin-off company was founded that uses Clean.

## Features

Clean shares many properties and syntax with a younger sibling language, Haskell: referential transparency, list comprehension, guards, garbage collection, higher order functions, currying, and lazy evaluation. However, Clean deals with mutable state and input/output (I/O) through a uniqueness type system, in contrast to Haskell's use of monads. The compiler takes advantage of the uniqueness type system to generate more efficient code, because it knows that at any point during the execution of the program, only one reference can exist to a value with a unique type. Therefore, a unique value can be changed in place.

An integrated development environment (IDE) for Microsoft Windows is included in the Clean distribution.

## Examples

Hello world:

```mw
Start = "Hello, world!"
```

Factorial:

| fac :: Int -> Int fac 0 = 1 fac n = n * fac (n-1) Start = fac 10 | fac :: Int -> Int fac n = prod [1..n] // The product of the numbers 1 to n Start = fac 10 |
|---|---|

Fibonacci sequence:

| fib :: Int -> Int fib 0 = 1 fib 1 = 1 fib n = fib (n - 2) + fib (n - 1) Start = fib 7 | fibs :: Int Int -> [Int] fibs x_2 x_1 = [x_2:fibs x_1 (x_2 + x_1)] fib :: Int -> Int fib n = (fibs 1 1) !! n Start = fib 7 |
|---|---|

Infix operator:

```mw
(^) infixr 8 :: Int Int -> Int
(^) x 0 = 1
(^) x n = x * x ^ (n-1)
```

The type declaration states that the function is a right associative infix operator with priority 8: this states that `x*x^(n-1)` is equivalent to `x*(x^(n-1))` as opposed to `(x*x)^(n-1)`. This operator is pre-defined in StdEnv, the Clean standard library.

## How Clean works

Computing is based on graph rewriting and reduction. Constants such as numbers are graphs and functions are graph rewriting formulas. This, combined with compiling to native code, makes Clean programs which use high abstraction run relatively fast according to The Computer Language Benchmarks Game. A 2008 benchmark showed that Clean native code performs similarly to the Glasgow Haskell Compiler (GHC), depending on the benchmark.

## Compiling

Compilation of Clean to machine code is performed as follows:

1. Source files (.icl) and definition files (.dcl) are translated into Core Clean, a basic variant of Clean, by the compiler frontend written in Clean.
2. Core clean is converted into Clean's platform-independent intermediate language (.abc), by the compiler backend written in Clean and C.
3. Intermediate ABC code is converted to object code (.o) by the code generator written in C.
4. Object code is linked with other files in the module and the runtime system and converted into a normal executable using the system linker (when available) or a dedicated linker written in Clean on Windows.

Earlier versions of the Clean compiler were written completely in C, thus avoiding bootstrapping issues.

### The ABC machine

The ABC code mentioned above is an intermediate representation for an abstract machine. Because machine code generation for ABC code is relatively straightforward, it is easy to support new architectures. The ABC machine is an imperative abstract graph rewriting machine. It consists of a graph store to hold the Clean graph that is being rewritten and three stacks:

- The A(rgument)-stack holds arguments that refer to nodes in the graph store.
- The B(asic value)-stack holds basic values (integers, characters, reals, etc.). Although these values could be nodes in the graph store, a separate stack is used for efficiency.
- The C(ontrol)-stack holds return addresses for flow control.

The runtime system, which is linked into every executable, builds a `Start` node in the graph store and pushes it on the A-stack. It then begins printing it, evaluating it as needed.

### Running Clean in the browser

Although Clean is typically used to generate native executables, several projects have enabled applications in web browsers. The now abandoned SAPL project compiled Core Clean to JavaScript and did not use ABC code. Since 2019, an interpreter for ABC code, written in WebAssembly, is used instead.

## Platforms

Clean is available for Microsoft Windows (IA-32 and X86-64), macOS (X86-64), and Linux (IA-32, X86-64, and AArch64).

Some libraries are not available on all platforms, like ObjectIO which is only available on Windows. Also the feature to write dynamics to files is only available on Windows.

The availability of Clean per platform varies with each version:

Version

Date

Linux

macOS

Oracle Solaris

Windows

Miscellaneous

IA-32

x86-64

AArch64

Motorola 68040

PowerPC

x86-64

SPARC

IA-32

x86-64

3.1

5 January 2022

Yes

Yes

Yes

No

No

Yes

No

Yes

Yes

3.0

2 October 2018

Yes

Yes

No

No

No

Yes

No

Yes

Yes

2.4

23 December 2011

Yes

Yes

No

No

No

Yes

No

Yes

Yes

2.3

22 December 2010

Yes

Yes

No

No

No

No

No

Yes

Yes

2.2

19 December 2006

Yes

Yes

No

No

Yes

No

Yes

Yes

Yes

2.1.1

31 May 2005

Yes

No

No

No

Yes

No

Yes

Yes

No

2.1.0

31 October 2003

Yes

No

No

No

Yes

No

Yes

Yes

No

2.0.2

12 December 2002

Yes

No

No

No

Yes

No

Yes

Yes

No

2.0.1

4 July 2002

Yes

No

No

No

Yes

No

Yes

Yes

No

2.0

21 December 2001

No

No

No

No

No

No

No

Yes

No

1.3.3

13 September 2000

Yes

No

No

No

Yes

No

Yes

Yes

No

1.3.2

1 July 1999

No

No

No

Yes

Yes

No

Yes

Yes

No

1.3.1

January 1999

Yes

No

No

No

Yes

No

Yes

Yes

No

1.3

22 May 1998

Yes

No

No

No

Yes

No

Yes

Yes

No

1.2.4

June 1997

No

No

No

Yes

Yes

No

No

Yes

No

1.2.3

May 1997

No

No

No

Yes

Yes

No

No

Yes

No

1.2

13 January 1997

No

No

No

Yes

Yes

No

No

No

No

1.1.3

October 1996

No

No

No

No

No

No

Yes

No

No

OS/2

(

i80386

)

1.1.2

September 1996

Yes

No

No

No

No

No

Yes

No

No

SunOS

4 (

SPARC

)

1.1

March 1996

Yes

No

No

Yes

No

No

No

No

No

1.0.2

September 1995

Yes

No

No

Yes

No

No

Yes

No

No

OS/2

(

i80386

);

SunOS

4 (

SPARC

)

1.0

May 1995

No

No

No

Yes

No

No

No

No

No

OS/2

(

i80386

)

0.8.4

11 May 1993

Yes

No

No

Yes

No

No

No

No

No

Experimental

T800 transputer

release

0.8.3

26 February 1993

No

No

No

Yes

No

No

No

No

No

0.8.1

19 October 1992

No

No

No

Yes

No

No

No

No

No

0.8

13 July 1992

No

No

No

Yes

No

No

No

No

No

OS/2

(

i80386

);

SunOS

3–4 (

SPARC

)

0.7

May 1991

No

No

No

Yes

No

No

No

No

No

SunOS

3–4 (

SPARC

)

## Comparison to Haskell

The syntax of Clean is very similar to that of Haskell, with some notable differences. In general, Haskell has introduced more syntactic sugar than Clean:

| Haskell | Clean | Remarks |
|---|---|---|
| [ x \| x <- [1..10] , isOdd x] | [ x \\ x <- [1..10] \| isOdd x] | list comprehension |
| x:xs | [x:xs] | cons operator |
| data Tree a = Empty \| Node (Tree a) a (Tree a) | :: Tree a = Empty \| Node (Tree a) a (Tree a) | algebraic data type |
| (Eq a, Eq b) => ... | ... \| Eq a & Eq b | class assertions and contexts |
| fun t@(Node l x r) = ... | fun t=:(Node l x r) = ... | as-patterns |
| if x > 10 then 10 else x | if (x > 10) 10 x | if |
