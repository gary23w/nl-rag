---
title: "Joy (programming language)"
source: https://en.wikipedia.org/wiki/Joy_(programming_language)
domain: joy-language
license: CC-BY-SA-4.0
tags: joy language, function level programming, manfred von thun, concatenative programming, higher order function
fetched: 2026-07-02
---

# Joy (programming language)

The **Joy programming language** in computer science is a purely functional programming language that was produced by Manfred von Thun of La Trobe University in Melbourne, Australia. Joy is based on composition of functions rather than lambda calculus. It was inspired by the function-level programming style of John Backus's FP. It has turned out to have many similarities to Forth, due not to design but to an independent evolution and convergence.

## Overview

Functions in Joy lack formal parameters. For example, a function that squares a numeric input can be expressed as follows:

```
DEFINE square == dup * .
```

In Joy, everything is a function that takes a stack as an argument and returns a stack as a result. For instance, the numeral '5' does not represent an integer constant, but instead a short program that pushes the number 5 onto the stack.

- The **dup** operator simply duplicates the top element of the stack by pushing a copy of it.
- The ***** operator pops two numbers off the stack and pushes their product.

So the square function makes a copy of the top element, and then multiplies the two top elements of the stack, leaving the square of the original top element at the top of the stack, with no need for a formal parameter. This makes Joy concise, as illustrated by this definition of quicksort:

```
DEFINE qsort ==
  [small]
  []
  [uncons [>] split]
  [swapd cons concat]
  binrec.
```

## Mathematical purity

Joy is a concatenative programming language: "The concatenation of two programs denotes the composition of the functions denoted by the two programs".
