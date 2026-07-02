---
title: "Futhark (programming language)"
source: https://en.wikipedia.org/wiki/Futhark_(programming_language)
domain: futhark-deep
license: CC-BY-SA-4.0
tags: futhark language, data parallelism, parallel programming model, purely functional programming, gpu computing
fetched: 2026-07-02
---

# Futhark (programming language)

**Futhark** is a multi-paradigm, high-level, functional, data parallel, array programming language. It is a dialect of the language ML, originally developed at UCPH Department of Computer Science (DIKU) as part of the HIPERFIT project. It focuses on enabling data parallel programs written in a functional style to be executed with high performance on massively parallel hardware, especially graphics processing units (GPUs). Futhark is strongly inspired by NESL, and its implementation uses a variant of the flattening transformation, but imposes constraints on how parallelism can be expressed in order to enable more aggressive compiler optimisations. In particular, irregular nested data parallelism is not supported. It is free and open-source software released under an ISC license.

## Overview

Futhark is a language in the ML family, with an indentation-insensitive syntax derived from OCaml, Standard ML, and Haskell. The type system is based on a Hindley–Milner type system with a variety of extensions, such as uniqueness types and size-dependent types. Futhark is not intended as a general-purpose programming language for writing full applications, but is instead focused on writing *compute kernels* (not always the same as a *GPU kernel*) which are then invoked from applications written in conventional languages.

Futhark is named after the first six letters of the Runic alphabet.

## Examples

### Dot product

The following program computes the dot product of two vectors containing double-precision numbers.

```mw
def dotprod xs ys = f64.sum (map2 (*) xs ys))
```

It can also be equivalently written with explicit type annotations as follows.

```mw
def dotprod [n] (xs: [n]f64) (ys: [n]f64) : f64 = f64.sum (map2 (*) xs ys))
```

This makes the size-dependent types explicit: this function can only be invoked with two arrays of the same size, and the type checker will reject any program where this cannot be statically determined.

### Matrix multiplication

The following program performs matrix multiplication, using the definition of dot product above.

```mw
def matmul [n][m][p] (A: [n][m]f64) (B: [m][p]f64) : [n][p]f64 =
  map (\A_row ->
         map (\B_col -> dotprod A_row B_col)
             (transpose B))
      A
```

This shows how the types enforce that the function is only invoked with matrices of compatible size. Also, it is an example of nested data parallelism.
