---
title: "Idris (programming language)"
source: https://en.wikipedia.org/wiki/Idris_(programming_language)
domain: dependent-types-pl
license: CC-BY-SA-4.0
tags: dependent type, pi type, dependent product, type family
fetched: 2026-07-02
---

# Idris (programming language)

**Idris** is a purely-functional programming language with dependent types, quantity annotations, optional lazy evaluation, and features such as a totality checker. Idris is designed to be a general-purpose programming language similar to Haskell, but may also be used as a proof assistant.

The Idris type system is similar to Agda's. Compared to Agda, Idris prioritizes management of side effects and support for embedded domain-specific languages. Idris is compiled by modular backends, which provide code generation and a runtime system. The Idris compiler includes backends for Chez Scheme, Racket, JavaScript (both browser- and Node.js-based), and C. Additional third-party backends are available for other platforms.

Idris is named after a singing dragon from the 1970s UK children's television programme *Ivor the Engine*.

## Features

Idris combines a number of features from relatively mainstream functional programming languages with features borrowed from proof assistants.

### Functional programming

The syntax of Idris shows many similarities with that of Haskell. A hello world program in Idris might look like this:

```mw
module Main

main : IO ()
main = putStrLn "Hello, World!"
```

The only differences between this program and its Haskell equivalent are the single (instead of double) colon in the type signature of the main function, and the omission of the word "`where`" in the module declaration.

### Inductive and parametric data types

Idris supports inductively-defined data types and parametric polymorphism. Such types can be defined both in traditional *Haskell 98*-like syntax:

```mw
data Tree a = Node (Tree a) (Tree a) | Leaf a
```

or in the more general generalized algebraic data type (GADT)-like syntax:

```mw
data Tree : Type -> Type where
    Node : Tree a -> Tree a -> Tree a
    Leaf : a -> Tree a
```

### Dependent types

With dependent types, it is possible for values to appear in the types; in effect, any value-level computation can be performed during type checking. The following defines a type of lists whose lengths are known before the program runs, traditionally called vectors:

```mw
data Vect : Nat -> Type -> Type where
  Nil  : Vect 0 a
  (::) : (x : a) -> (xs : Vect n a) -> Vect (n + 1) a
```

This type can be used as follows:

```mw
total
append : Vect n a -> Vect m a -> Vect (n + m) a
append Nil       ys = ys
append (x :: xs) ys = x :: append xs ys
```

The function `append` appends a vector of `m` elements of type `a` to a vector of `n` elements of type `a`. Since the precise types of the input vectors depend on a value, it is possible to be certain at compile time that the resulting vector will have exactly (`n` + `m`) elements of type `a`. The word "`total`" invokes the totality checker which will report an error if the function doesn't cover all possible cases or cannot be (automatically) proven not to enter an infinite loop.

Another common example is pairwise addition of two vectors that are parameterized over their length:

```mw
total
pairAdd : Num a => Vect n a -> Vect n a -> Vect n a
pairAdd Nil       Nil       = Nil
pairAdd (x :: xs) (y :: ys) = x + y :: pairAdd xs ys
```

`Num` a signifies that the type a belongs to the type class `Num`. Note that this function still typechecks successfully as total, even though there is no case matching `Nil` in one vector and a number in the other. Because the type system can prove that the vectors have the same length, we can be sure at compile time that case will not occur and there is no need to include that case in the function’s definition.

### Proof assistant features

Dependent types are powerful enough to encode most properties of programs, and an Idris program can prove invariants at compile time. This makes Idris into a proof assistant.

There are two standard ways of interacting with proof assistants: by writing a series of tactic invocations (Rocq style), or by interactively elaborating a proof term (Epigram–Agda style). Idris supports both modes of interaction, although the set of available tactics is not yet as useful as that of Rocq.

### Code generation

Because Idris contains a proof assistant, Idris programs can be written to pass proofs around. If treated naïvely, such proofs remain around at runtime. Idris aims to avoid this pitfall by aggressively erasing unused terms.

By default, Idris generates native code through C. The other officially supported backend generates JavaScript.

## Idris 2

Idris 2 is a new self-hosted version of the language which deeply integrates a linear type system, based on quantitative type theory. It currently compiles to Scheme and C.
