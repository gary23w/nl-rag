---
title: "Concatenative programming language"
source: https://en.wikipedia.org/wiki/Concatenative_programming
domain: joy-language
license: CC-BY-SA-4.0
tags: joy language, function level programming, manfred von thun, concatenative programming, higher order function
fetched: 2026-07-02
---

# Concatenative programming language

(Redirected from

Concatenative programming

)

A **concatenative programming language** is a point-free computer programming language in which all expressions denote functions, and the juxtaposition of expressions denotes function composition. Concatenative programming replaces function application, which is common in other programming paradigms, with function composition as the default way to build subroutines.

## Example

For example, a nesting of operations in an applicative language like the following:

```mw
baz(bar(foo(x)))
```

...is written in a concatenative language as a sequence of functions:

```
x foo bar baz
```

Functions and procedures written in concatenative style are not value level, i.e., they typically do not represent the data structures they operate on with explicit names or identifiers. Instead they are function level – a function is defined as a pipeline, or a sequence of operations that take parameters from an implicit data structure on which all functions operate, and return the function results to that shared structure so that it will be used by the next operator.

The combination of compositional semantics with a syntax that mirrors such a semantic makes concatenative languages highly amenable to algebraic manipulation of programs; although it may be difficult to write mathematical expressions directly in them. Concatenative languages can be implemented efficiently with a stack machine, and are commonly present implicitly in virtual machines in the form of their instruction sets.

## Properties

The properties of concatenative languages are the result of their compositional syntax and semantics:

- The reduction of any expression is the simplification of one function to another function; it is never necessary to deal with the application of functions to objects.
- Any subexpression can be replaced with a name that represents the same subexpression. In concatenative programming practice, this is called factoring, and is used extensively to simplify programs into smaller parts.
- The syntax and semantics of concatenative languages form the algebraic structure of a monoid.
- Concatenative languages can be made well-suited to an implementation inspired by linear logic where no garbage is ever generated.

## Implementations

The first concatenative programming language was Forth, although Joy was the first language which was termed concatenative. Other concatenative languages are dc, Factor, Onyx, PostScript, RPL, Staapl, and experimental and discontinued ones including: Enchilada, Om, XY.

Most existing concatenative languages are stack-based. This is not required, and other models have been proposed. Concatenative languages are currently used for embedded, desktop, and web programming, as target languages, and for research purposes.

Most concatenative languages are dynamically typed. Exceptions include the statically typed Cat language and its successor, Kitten.
