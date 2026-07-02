---
title: "Wolfram Language"
source: https://en.wikipedia.org/wiki/Wolfram_Language
domain: wolfram-language
license: CC-BY-SA-4.0
tags: wolfram language, mathematica language, wolfram lang, symbolic wolfram
fetched: 2026-07-02
---

# Wolfram Language

The **Wolfram Language** (/ˈwʊlfrəm/ *WUUL-frəm*) is a proprietary, high-level multi-paradigm programming language developed by Wolfram Research. It emphasizes symbolic computation, functional programming, and rule-based programming and can employ arbitrary structures and data. It is the programming language of the mathematical symbolic computation program Mathematica.

## History

The Wolfram Language was part of the initial version of Mathematica in 1988.

Symbolic aspects of the engine make it a computer algebra system. The language can perform integration, differentiation, matrix manipulations, and solve differential equations using a set of rules. Also, the initial version introduced the notebook model and the ability to embed sound and images, according to Theodore Gray's patent.

Wolfram also added features for more complex tasks, such as 3D modeling.

A name was finally adopted for the language in 2013, as Wolfram Research decided to make a version of the language engine free for Raspberry Pi users, and they needed to come up with a name for it. It was included in the recommended software bundle that the Raspberry Pi Foundation provides for beginners, which caused some controversy due to the Wolfram language's proprietary nature. Plans to port the Wolfram language to the Intel Edison were announced after the board's introduction at CES 2014 but were never released. In 2019, a link was added to make Wolfram libraries compatible with the Unity game engine, giving game developers access to the language's high-level functions.

## Syntax

The Wolfram Language syntax is overall similar to the M-expression of 1960s LISP, with support for infix operators and "function-notation" function calls.

### Basics

#### Hello, World

To print "Hello, World!" in Wolfram Language is the following:

```mw
Print["Hello, World!"]
```

#### Arithmetic

The Wolfram language writes basic arithmetic expressions using infix operators.

```mw
(* This is a comment. *)

4 + 3
(* = 7 *)

1 + 2 * (3 + 4)
(* = 15 *)
(* Note that Multiplication can be omitted: 1 + 2 (3 + 4) *)

(* Divisions return rational numbers: *)
6 / 4
(* = 3/2 *)
```

Function calls are denoted with square brackets:

```mw
Sin[Pi]
(* = 0 *)

(* This is the function to convert rationals to floating point: *)
N[3 / 2]
(* = 1.5 *)
```

Lists are enclosed in curly brackets:

```mw
Oddlist={1,3,5}
(* = {1,3,5} *)
```

### Syntactic sugar

The language may deviate from the M-expression paradigm when an alternative, more human-friendly way of showing an expression is available:

- A number of formatting rules are used in this language, including `TeXForm` for typeset expressions and `InputForm` for language input.
- Functions can also be applied using the prefix expression `@` and the postfix expression `//`.
- Derivatives can be denoted with the apostrophe `'`.
- The infix operators themselves are considered "sugar" for the function notation system.

A `FullForm` formatter desugars the input:

```mw
FullForm[1+2]
(* = Plus[1, 2] *)
```

### Functional programming

Currying is supported.

### Pattern matching

Functions in the Wolfram Language are effectively a case of simple patterns for replacement:

```mw
F[x_] := x ^ 0
```

The `:=` is a "SetDelayed operator", so that the x is not immediately looked for. `x_` is syntax sugar for `Pattern[x, Blank[]]`, i.e. a "blank" for any value to replace x in the rest of the evaluation.

An iteration of bubble sort is expressed as:

```mw
sortRule := {x___,y_,z_,k___} /; y>z -> {x,z,y,k}
(* Rule[Condition[List[PatternSequence[x, BlankNullSequence[]], Pattern[y, Blank[]], Pattern[z, Blank[]], PatternSequence[k, BlankNullSequence[]]], Greater[y, z]], List[x, z, y, k]] *)
```

The `/;` operator is "condition", so that the rule only applies when `y>z`. The three underscores are a syntax for a `BlankNullSequence[]`, for a sequence that can be null.

A ReplaceRepeated `//.` operator can be used to apply this rule repeatedly, until no more change happens:

```mw
{ 9, 5, 3, 1, 2, 4 } //. sortRule
(* = ReplaceRepeated[{ 9, 5, 3, 1, 2, 4 }, sortRule] *)
(* = {1, 2, 3, 4, 5, 9} *)
```

The pattern matching system also easily gives rise to rule-based integration and derivation. The following are excerpts from the Rubi package of rules:

```mw
(* Reciprocal rule *)
Int[1/x_,x_Symbol] :=
  Log[x];
(* Power rule *)
Int[x_^m_.,x_Symbol] :=
  x^(m+1)/(m+1) /;
FreeQ[m,x] && NeQ[m,-1]
```

## Implementations

The official and reference implementation of the Wolfram Language lies in Mathematica and associated online services. These are closed source. Wolfram Research has, however, released a parser of the language under the open source MIT License. The parser was originally developed in C++ but was rewritten in Rust in 2023. The reference book is open access.

In the over three-decade-long existence of the Wolfram language, a number of open-source third-party implementations have also been developed. Richard Fateman's MockMMA from 1991 is of historical note, both for being the earliest reimplementation and for having received a cease-and-desist from Wolfram. Modern ones still being maintained as of April 2020 include Symja in Java, expreduce in Golang, and SymPy-based Mathics. These implementations focus on the core language and the computer algebra system that it implies, not on the online "knowledgebase" features of Wolfram.

In 2019, Wolfram Research released the freeware Wolfram Engine, to be used as a programming library in non-commercial software. This developer-only engine provides a command-line shell of the Mathematica evaluator (with a limited number of kernels) and requires signup and license activation over the web. The freely available Jupyter Notebook/Lab project provides a protocol (ZMQ) to connect their notebooks to various languages, this is available as an alternative to the text-only CLI interface via the Wolfram Kernel for Jupyter.

## Naming

The language was officially named in June 2013 and has been used as the backend of Mathematica and other Wolfram technologies for over 30 years.
