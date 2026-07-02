---
title: "Comparison of parser generators"
source: https://en.wikipedia.org/wiki/Comparison_of_parser_generators
domain: peg-parser
license: CC-BY-SA-4.0
tags: parsing expression grammar, peg parser, packrat parsing, top-down parsing
fetched: 2026-07-02
---

# Comparison of parser generators

This is a list of notable lexer generators and parser generators for various language classes.

## Regular languages

Regular languages are a category of languages (sometimes termed Chomsky Type 3) which can be matched by a state machine (more specifically, by a deterministic finite automaton or a nondeterministic finite automaton) constructed from a regular expression. In particular, a regular language can match constructs like "A follows B", "Either A or B", "A, followed by zero or more instances of B", but cannot match constructs which require consistency between non-adjacent elements, such as "some instances of A followed by the same number of instances of B", and also cannot express the concept of recursive "nesting" ("every A is eventually followed by a matching B"). A classic example of a problem which a regular grammar cannot handle is the question of whether a given string contains correctly nested parentheses. (This is typically handled by a Chomsky Type 2 grammar, also termed a context-free grammar.)

| Name | Lexer algorithm | Output languages | Grammar, code | Development platform | License |
|---|---|---|---|---|---|
| Alex | DFA | Haskell | Mixed | All | Free, BSD |
| AnnoFlex | DFA | Java | Mixed | Java virtual machine | Free, BSD |
| Astir | DFA table driven, with branching | C++ | Only grammar (actioned) | All | Free, MIT |
| AustenX | DFA | Java | Separate | All | Free, BSD |
| C# Flex | DFA | C# | Mixed | .NET CLR | Free, GNU GPL |
| C# Lex | DFA | C# | Mixed | .NET CLR | ? |
| CookCC | DFA | Java | Mixed | Java virtual machine | Free, Apache 2.0 |
| DFA | DFA compressed matrix | C, C++ | Separate | Windows, Visual Studio | BSD |
| Dolphin | DFA | C++ | Separate | All | Proprietary |
| Flex | DFA table driven | C, C++ | Mixed | All | Free, BSD |
| gelex | DFA | Eiffel | Mixed | Eiffel | Free, MIT |
| golex | DFA | Go | Mixed | Go | Free, BSD-style |
| gplex | DFA | C# | Mixed | .NET CLR | Free, BSD-like |
| JFlex | DFA | Java | Mixed | Java virtual machine | Free, BSD |
| JLex | DFA | Java | Mixed | Java virtual machine | Free, BSD-like |
| lex | DFA | C | Mixed | POSIX | Partial, proprietary, CDDL |
| lexertl | DFA | C++ | ? | All | Free, GNU LGPL |
| Quex | DFA direct code | C, C++ | Mixed | All | Free, GNU LGPL |
| Ragel | DFA | Go, C, C++, Java, assembly | Mixed | All | Free, GNU GPL, MIT |
| RE/flex | DFA direct code, DFA table driven, and NFA regex libraries | C++ | Mixed | All | Free, BSD |
| re2c | DFA direct code | C, C++, Go, Rust | Mixed | All | Free, public domain |

## Deterministic context-free languages

Context-free languages are a category of languages (sometimes termed Chomsky Type 2) which can be matched by a sequence of replacement rules, each of which essentially maps each non-terminal element to a sequence of terminal elements and/or other nonterminal elements. Grammars of this type can match anything that can be matched by a regular grammar, and furthermore, can handle the concept of recursive "nesting" ("every A is eventually followed by a matching B"), such as the question of whether a given string contains correctly nested parentheses. The rules of Context-free grammars are purely local, however, and therefore cannot handle questions that require non-local analysis such as "Does a declaration exist for every variable that is used in a function?". To do so technically would require a more sophisticated grammar, like a Chomsky Type 1 grammar, also termed a context-sensitive grammar. However, parser generators for context-free grammars often support the ability for user-written code to introduce limited amounts of context-sensitivity. (For example, upon encountering a variable declaration, user-written code could save the name and type of the variable into an external data structure, so that these could be checked against later variable references detected by the parser.)

The deterministic context-free languages are a proper subset of the context-free languages which can be efficiently parsed by deterministic pushdown automata.

Name

Parsing

algorithm

Input grammar notation

Output languages

Grammar, code

Lexer

Development platform

IDE

License

ANTLR

4

Adaptive LL(*)

EBNF

C#

,

Java

,

Python

,

JavaScript

,

C++

,

Swift

,

Go

,

PHP

Separate

generated

Java virtual machine

Yes

Free,

BSD

ANTLR

3

LL

(*)

EBNF

ActionScript

,

Ada95

,

C

,

C++

,

C#

,

Java

,

JavaScript

,

Objective-C

,

Perl

,

Python

,

Ruby

Mixed

generated

Java virtual machine

Yes

Free,

BSD

APG

Recursive descent

,

backtracking

ABNF

Python

,

JavaScript

,

C

,

Java

Separate

none

All

No

Free,

BSD

Beaver

LALR

(1)

EBNF

Java

Mixed

external

Java virtual machine

No

Free,

BSD

Bison

LALR

(1),

LR

(1),

IELR

(1),

GLR

Yacc

C

,

C++

,

D

,

Java

Mixed

external

All

No

Free,

GNU GPL

with exception

BtYacc

Backtracking

Bottom-up

?

C++

Mixed

external

All

No

Free,

public domain

byacc

LALR

(1)

Yacc

C

Mixed

external

All

No

Free,

public domain

CL-Yacc

LALR

(1)

Lisp

Common Lisp

Mixed

external

All

No

Free,

MIT

Coco/R

LL

(1) + semantic predicates

EBNF

C

,

C++

,

C#

,

F#

,

Java

,

Ada

,

Object Pascal

,

Delphi

,

Modula-2

,

Oberon

,

Ruby

,

Swift

,

Unicon

,

Visual Basic .NET

Mixed

generated

Java virtual machine

,

.NET

framework,

Windows

,

POSIX

(depends on output language)

No

Free,

GNU GPL

CppCC

LL

(k)

?

C++

Mixed

generated

POSIX

No

Free,

GNU GPL

CUP

LALR

(1)

?

Java

Mixed

external

Java virtual machine

No

Free,

BSD

-like

Eli

LALR

(1)

?

C

Mixed

generated

POSIX

No

Free,

GNU GPL

,

GNU LGPL

Essence

LR

(?)

?

Scheme 48

Mixed

external

All

No

Free,

BSD

eyapp

LALR

(1)

?

Perl

Mixed

external or generated

All

No

Free,

Artistic

GOLD

LALR

(1)

BNF

x86 assembly language

,

ANSI C

,

C#

,

D

,

Java

,

Pascal

,

Object Pascal

,

Python

,

Visual Basic

6,

Visual Basic .NET

,

Visual C++

Separate

generated

Windows

Yes

Free,

zlib

modified

Hime Parser Generator

LALR

(1),

GLR

BNF dialect

C#

,

Java

,

Rust

Separate

generated

.NET

framework,

Java virtual machine

No

Free,

GNU LGPL

Hyacc

LR(1), LALR(1), LR

(0)

Yacc

C

Mixed

external

All

No

Free,

GNU GPL

JavaCC

LL

(k)

EBNF

Java

,

C++

,

JavaScript

(via

GWT

compiler)

Mixed

generated

Java virtual machine

Yes

Free,

BSD

JFLAP

LL

(1),

LALR

(1)

?

Java

?

?

Java virtual machine

Yes

?

JetPAG

LL

(k)

?

C++

Mixed

generated

All

No

Free,

GNU GPL

JS/CC

LALR

(1)

EBNF

JavaScript

,

JScript

,

ECMAScript

Mixed

internal

All

Yes

Free,

BSD

KDevelop-PG-Qt

LL

(1),

backtracking

,

shunting-yard

?

C++

Mixed

generated or external

All,

KDE

No

Free,

GNU LGPL

Kelbt

Backtracking

LALR

(1)

?

C++

Mixed

generated

POSIX

No

Free,

GNU GPL

kmyacc

LALR

(1)

?

C

,

Java

,

Perl

,

JavaScript

Mixed

external

All

No

Free,

GNU GPL

Lapg

LALR

(1)

?

C

,

C++

,

C#

,

Java

,

JavaScript

Mixed

generated

Java virtual machine

No

Free,

GNU GPL

Lark

LALR

(1),

Earley (SPPF)

EBNF

derivative

Python

,

JavaScript

Mixed

generated

All

Yes

Free,

MIT

Lemon

LALR

(1)

BNF dialect

C

Mixed

external

All

No

Free,

public domain

Lezer

LR

(1),

GLR

EBNF dialect

JavaScript

Separate

generated

Node.js

,

JavaScript

No

Free,

MIT

Lime

LALR

(1)

?

PHP

Mixed

external

All

No

Free,

GNU GPL

LISA

LR

(?),

LL

(?),

LALR

(?),

SLR

(?)

?

Java

Mixed

generated

Java virtual machine

Yes

Free,

public domain

LLgen

LL

(1)

?

C

Mixed

external

POSIX

No

Free,

BSD

LLnextgen

LL

(1)

?

C

Mixed

external

All

No

Free,

GNU GPL

LLLPG

LL

(k) +

syntactic

and semantic predicates

ANTLR-like

C#

Mixed

generated (?)

.NET

framework,

Mono

Visual Studio

Free,

GNU LGPL

LPG

Backtracking

LALR

(k)

?

Java

Mixed

generated

Java virtual machine

No

Free,

EPL

LRSTAR

LALR

(1),

LALR

(*)

YACC, ANTLR, EBNF

C++

Separate

generated

Windows

Visual Studio

Free,

BSD

Menhir

LR

(1)

?

OCaml

Mixed

generated

All

No

Free,

QPL

ML-Yacc

LALR

(1)

?

ML

Mixed

external

All

No

?

Monkey

LR

(1)

?

Java

Separate

generated

Java virtual machine

No

Free,

GNU GPL

Msta

LALR

(k),

LR

(k)

YACC

,

EBNF

C

,

C++

Mixed

external or generated

POSIX

,

Cygwin

No

Free,

GNU GPL

MTP (More Than Parsing)

LL

(1)

?

Java

Separate

generated

Java virtual machine

No

Free,

GNU GPL

MyParser

LL

(*)

Markdown

C++11

Separate

internal

Any with standard C++11 compiler

No

Free,

MIT

NLT

GLR

C#

/

BNF

-like

C#

Mixed

mixed

.NET

framework

No

Free,

MIT

ocamlyacc

LALR

(1)

?

OCaml

Mixed

external

All

No

Free,

QPL

olex

LL

(1)

?

C++

Mixed

generated

All

No

Free,

GNU GPL

Parsec

LL

,

backtracking

Haskell

Haskell

Mixed

none

All

No

Free,

BSD

yapp

LALR

(1)

?

Perl

Mixed

external

All

No

Free,

GNU GPL

Parser Objects

LL

(k)

?

Java

Mixed

?

Java virtual machine

No

Free,

zlib

PCCTS

LL

?

C

,

C++

?

?

All

No

?

PLY

LALR

(1)

BNF

Python

Mixed

generated

All

No

Free,

MIT

PlyPlus

LALR

(1)

EBNF

Python

Separate

generated

All

No

Free,

MIT

PRECC

LL

(k)

?

C

Separate

generated

MS-DOS

,

POSIX

No

Free,

GNU GPL

QLALR

LALR

(1)

?

C++

Mixed

external

All

No

Free,

GNU GPL

racc

LALR

(1)

BNF

-like, yacc-like

Ruby

Mixed

?

Windows, Linux, macOS, FreeBSD, NetBSD

No

LGPL

REX

LL

(1)

sLL

(k)

LR

(k)

LALR

(k)

GLR

PEG

DFA

Context-dependent lexing

EBNF

C++

,

C#

,

Java

,

JavaScript

,

Go

,

Haxe

,

Python

,

Scala

,

TypeScript

,

XQuery

,

XSLT

Separate

generated

All

No

Free,

Apache License 2.0

SableCC

LALR

(1)

?

C

,

C++

,

C#

,

Java

,

OCaml

,

Python

Separate

generated

Java virtual machine

No

Free,

GNU LGPL

SLK

LL

(k)

LR

(k)

LALR

(k)

EBNF

C

,

C++

,

C#

,

Java

,

JavaScript

Separate

external

All

No

SLK

SLY

LALR

(1)

BNF

Python

Mixed

generated

All

No

Free,

BSD

SP (Simple Parser)

Recursive descent

Python

Python

Separate

generated

All

No

Free,

GNU LGPL

Spirit

Recursive descent

?

C++

Mixed

internal

All

No

Free,

Boost

Styx

LALR

(1)

?

C

,

C++

Separate

generated

All

No

Free,

GNU LGPL

Sweet Parser

LALR

(1)

?

C++

Separate

generated

Windows

No

Free,

zlib

Tap

LL

(1)

?

C++

Mixed

generated

All

No

Free,

GNU GPL

TextTransformer

LL

(k)

?

C++

Mixed

generated

Windows

Yes

Proprietary

TinyPG

LL

(1)

?

C#

,

Visual Basic

?

?

Windows

Yes

Partial,

CPOL

1.0

Toy Parser Generator

Recursive descent

?

Python

Mixed

generated

All

No

Free,

GNU LGPL

TP Yacc

LALR

(1)

?

Turbo Pascal

Mixed

external

All

Yes

Free,

GNU GPL

Tree-Sitter

LR

(1),

GLR

JavaScript

DSL

,

JSON

C

, bindings (

Rust

,

WebAssembly

,

JavaScript

,

Python

, many other)

Separate

generated + external

All

Neovim

,

Helix

,

GNU Emacs

,

Lapce

,

Zed

Free,

MIT

Tunnel Grammar Studio

Tunnel Parsing

ABNF

C++

Separate

generated

Windows

Yes

Proprietary

UltraGram

LALR

(1),

LR

(1),

GLR

BNF

C++, Java, C#, Visual Basic .NET

Separate

external

Windows

Yes

Free,

public domain

UniCC

LALR

(1)

EBNF

C

,

C++

,

Python

,

JavaScript

,

JSON

,

XML

Mixed

generated

POSIX

No

Free,

BSD

UrchinCC

LL

(1)

?

Java

?

generated

Java virtual machine

No

?

Yacc

AT&T

/

Sun

LALR

(1)

Yacc

C

Mixed

external

POSIX

No

Free,

CPL

&

CDDL

Yacc++

LR

(1),

LALR

(1)

Yacc

C++

,

C#

Mixed

generated or external

All

No

Proprietary

Yapps

LL

(1)

?

Python

Mixed

generated

All

No

Free,

MIT

yecc

LALR

(1)

?

Erlang

Separate

generated

All

No

Free,

Apache

2.0

Visual BNF

LR

(1),

LALR

(1)

?

C#

Separate

generated

.NET

framework

Yes

Proprietary

YooParse

LR

(1),

LALR

(1)

?

C++

Mixed

external

All

No

Free,

MIT

Parse

LR

(1)

BNF in

C++

types

?

?

none

C++11 standard compiler

No

Free,

MIT

GGLL

LL

(1)

Graph

Java

Mixed

generated

Windows

Yes

Free,

MIT

Product

Parsing

algorithm

Input grammar notation

Output languages

Grammar, code

Lexer

Development platform

IDE

License

## Parsing expression grammars, deterministic Boolean grammars

This table compares parser generators with parsing expression grammars, deterministic Boolean grammars.

| Name | Parsing algorithm | Output languages | Grammar, code | Development platform | License |
|---|---|---|---|---|---|
| AustenX | Packrat (modified) | Java | Separate | All | Free, BSD |
| Aurochs | Packrat | C, OCaml, Java | Mixed | All | Free, GNU GPL |
| BNFlite | Recursive descent | C++ | Mixed | All | Free, MIT |
| Canopy | Packrat | Java, JavaScript, Python, Ruby | Separate | All | Free, GNU GPL |
| CL-peg | Packrat | Common Lisp | Mixed | All | Free, MIT |
| Drat! | Packrat | D | Mixed | All | Free, GNU GPL |
| Frisby | Packrat | Haskell | Mixed | All | Free, BSD |
| grammar::peg | Packrat | Tcl | Mixed | All | Free, BSD |
| Grako | Packrat + Cut + Left Recursion | Python, C++ (beta) | Separate | All | Free, BSD |
| IronMeta | Packrat | C# | Mixed | Windows | Free, BSD |
| Laja | 2-phase scannerless top-down backtracking + runtime support | Java | Separate | All | Free, GNU GPL |
| lars::Parser | Packrat (supporting left-recursion and grammar ambiguity) | C++ | Identical | All | Free, BSD |
| LPeg | Parsing machine | Lua | Mixed | All | Free, MIT |
| lug | Parsing machine | C++17 | Mixed | All | Free, MIT |
| Mouse | Recursive descent (modified, limited memoization and left-recursion) | Java | Separate | Java virtual machine | Free, Apache 2.0 |
| Narwhal | Packrat | C | Mixed | POSIX, Windows | Free, BSD |
| Nearley | Earley | JavaScript | Mixed | All | Free, MIT |
| Nemerle.Peg | Recursive descent + Pratt | Nemerle | Separate | All | Free, BSD |
| neotoma | Packrat | Erlang | Separate | All | Free, MIT |
| nez | Parsing machine | Java, C | Separate | Java virtual machine | Free, BSD |
| NPEG | Recursive descent | C# | Mixed | All | Free, MIT |
| OMeta | Packrat (modified, partial memoization) | JavaScript, Squeak, Python | Mixed | All | Free, MIT |
| PackCC | Packrat (modified, left-recursion support) | C | Mixed | All | Free, MIT |
| Packrat | Packrat | Scheme | Mixed | All | Free, MIT |
| Pappy | Packrat | Haskell | Mixed | All | Free, BSD |
| parboiled | Recursive descent | Java, Scala | Mixed | Java virtual machine | Free, Apache 2.0 |
| Lambda PEG | Recursive descent | Java | Mixed | Java virtual machine | Free, Apache 2.0 |
| parsepp | Recursive descent | C++ | Mixed | All | Free, public domain |
| Parsnip | Packrat | C++ | Mixed | Windows | Free, GNU GPL |
| Patterns | Parsing machine | Swift | Identical | All | Free, MIT |
| peg | Recursive descent | C | Mixed | All | Free, MIT |
| PEG.js | Packrat (partial memoization) | JavaScript | Mixed | All | Free, MIT |
| Peggy | Packrat (partial memoization) | JavaScript | Mixed | All | Free, MIT |
| Pegasus | Recursive descent, Packrat (selectively) | C# | Mixed | Windows | Free, MIT |
| pegc | Recursive descent | C | Mixed | All | Free, public domain |
| pest | Recursive descent | Rust | Separate | All | Free, MIT, Apache 2.0 |
| PetitParser | Packrat | Smalltalk, Java, Dart | Mixed | All | Free, MIT |
| PEGTL | Recursive descent | C++11, C++17 | Mixed | All | Free, Boost |
| Parser Grammar Engine (PGE) | Hybrid recursive descent / operator precedence | Parrot bytecode | Mixed | Parrot virtual machine | Free, Artistic 2.0 |
| PyPy rlib | Packrat | Python | Mixed | All | Free, MIT |
| Rats! | Packrat | Java | Mixed | Java virtual machine | Free, GNU LGPL |
| Spirit2 | Recursive descent | C++ | Mixed | All | Free, Boost |
| Treetop | Recursive descent | Ruby | Mixed | All | Free, MIT |
| Yard | Recursive descent | C++ | Mixed | All | Free, MIT or public domain |
| Waxeye | Parsing machine | C, Java, JavaScript, Python, Racket, Ruby | Separate | All | Free, MIT |
| PHP PEG | PEG Parser? | PHP | Mixed | All | Free, BSD |

## General context-free, conjunctive, or Boolean languages

This table compares parser generator languages with a general context-free grammar, a conjunctive grammar, or a Boolean grammar.

Name

Parsing

algorithm

Input grammar notation

Output languages

Grammar, code

Lexer

Development platform

IDE

License

ACCENT

Earley

Yacc

variant

C

Mixed

external

All

No

Free,

GNU GPL

APaGeD

GLR

,

LALR

(1),

LL

(k)

?

D

Mixed

generated

All

No

Free,

Artistic

Bison

LALR

(1),

LR

(1),

IELR

(1),

GLR

Yacc

C

,

C++

,

D

,

Java

,

XML

Mixed, except XML

external

All

No

Free,

GNU GPL

DMS Software Reengineering Toolkit

GLR

?

Parlanse

Mixed

generated

Windows

No

Proprietary

DParser

Scannerless GLR

?

C

Mixed

scannerless

POSIX

No

Free,

BSD

Dypgen

Runtime-extensible

GLR

?

OCaml

Mixed

generated

All

No

Free,

CeCILL

-B

E3

Earley

?

OCaml

Mixed

external, or scannerless

All

No

?

Elkhound

GLR

?

C++

,

OCaml

Mixed

external

All

No

Free,

BSD

GDK

LALR

(1),

GLR

?

C

,

Lex

,

Haskell

,

HTML

,

Java

,

Object Pascal

,

Yacc

Mixed

generated

POSIX

No

Free,

MIT

Happy

LALR

,

GLR

?

Haskell

Mixed

external

All

No

Free,

BSD

Hime Parser Generator

GLR

?

C#

,

Java

,

Rust

Separate

generated

.NET

framework,

Java virtual machine

No

Free,

GNU LGPL

IronText Library

LALR

(1),

GLR

C#

C#

Mixed

generated or external

.NET

framework

No

Free,

Apache

2.0

Jison

LALR

(1),

LR

(0),

SLR

(1)

Yacc

JavaScript

,

C#

,

PHP

Mixed

generated

All

No

Free,

MIT

Syntax

LALR

(1),

LR

(0),

SLR

(1)

CLR

(1)

LL

(1)

JSON

/

Yacc

JavaScript

,

Python

,

PHP

,

Ruby

,

C++

,

C#

,

Rust

,

Java

Mixed

generated

All

No

Free,

MIT

Laja

Scannerless, two phase

Laja

Java

Separate

scannerless

All

No

Free,

GNU GPL

ModelCC

Earley

Annotated class model

Java

Generated

generated

All

No

Free,

BSD

P3

Earley–combinators

BNF-like

OCaml

Mixed

external, or scannerless

All

No

?

P4

Earley–combinators, infinitary CFGs

BNF-like

OCaml

Mixed

external, or scannerless

All

No

?

Scannerless Boolean Parser

Scannerless GLR

(

Boolean grammars

)

?

Haskell

,

Java

Separate

scannerless

Java virtual machine

No

Free,

BSD

SDF

/SGLR

Scannerless GLR

SDF

C

,

Java

Separate

scannerless

All

Yes

Free,

BSD

SmaCC

GLR

(1),

LALR

(1),

LR

(1)

?

Smalltalk

Mixed

internal

All

Yes

Free,

MIT

SPARK

Earley

?

Python

Mixed

external

All

No

Free,

MIT

Tom

GLR

?

C

Generated

none

All

No

Free, "No licensing or copyright restrictions"

UltraGram

LALR

,

LR

,

GLR

?

C++

,

C#

,

Java

,

Visual Basic .NET

Separate

generated

Windows

Yes

Proprietary

Wormhole

Pruning

,

LR

,

GLR

,

Scannerless GLR

?

C

,

Python

Mixed

scannerless

Windows

No

Free,

MIT

Whale Calf

General tabular,

SLL

(k), Linear normal form (

conjunctive grammars

),

LR

, Binary normal form (

Boolean grammars

)

?

C++

Separate

external

All

No

Proprietary

yaep

Earley

Yacc

-like

C

Mixed

external

All

No

Free,

GNU LGPL

## Context-sensitive grammars

This table compares parser generators with context-sensitive grammars.

| Name | Parsing algorithm | Input grammar notation | Boolean grammar abilities | Development platform | License |
|---|---|---|---|---|---|
| bnf2xml | Recursive descent (is a text filter output is xml) | simple BNF grammar (input matching), output is xml | ? | Beta, and not a full EBNF parser | Free, GNU GPL |
