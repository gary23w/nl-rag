---
title: "PureScript"
source: https://en.wikipedia.org/wiki/PureScript
domain: purescript
license: CC-BY-SA-4.0
tags: purescript, pure script language, purescript lang
fetched: 2026-07-02
---

# PureScript

**PureScript** is a strongly typed, purely functional programming language that transpiles to JavaScript and, with alternate backends, to C++11, Erlang, and Go. It can be used to develop web applications, server side apps, and also desktop applications with use of Electron or via C++11 and Go compilers with suitable libraries. Its syntax is mostly comparable to that of Haskell. Also, it introduces row polymorphism and extensible records. Also, contrary to Haskell, the PureScript language is defined as having a strict evaluation strategy, although there are non-conforming back-ends which implement a lazy evaluation strategy. It is free and open-source software released under a BSD 3-clause license.

## History

PureScript was initially designed by Phil Freeman in 2013. He began work on it because he was unsatisfied by other attempts to transpile Haskell to JavaScript (e.g., using Fay, Haste, or GHCJS).

Since then it has been adopted by the community and is developed on GitHub. Further community-developed core tools include the dedicated build tool *Pulp*, the documentation directory *Pursuit*, and the package manager *Spago*.

## Features

PureScript features strict evaluation, persistent data structures, and type inference. Its data type system shares many features with those of similar functional languages like Haskell: algebraic data types and pattern matching, higher kinded types, type classes, functional dependencies, and higher-rank polymorphism. Its type system adds support for row polymorphism and extensible records, but does not support some of the more advanced features of Haskell such as the generalized algebraic data type (GADT) and the type family.

The PureScript transpilers attempt to produce readable code, where possible. Through a simple foreign function interface (FFI), it also allows code reuse of extant source code in JavaScript, C++11, and Go, usually as an intermediate representation.

PureScript supports incremental compilation, and the transpiler to JavaScript distribution supports building source-code editor plug-ins for iterative development. Editor plug-ins exist for many popular text editors, including Vim, Emacs, Sublime Text, Atom and Visual Studio Code.

PureScript supports type-driven development via its typed holes feature, in which a program can be constructed with missing subexpressions. The JavaScript transpiler will subsequently attempt to infer the types of the missing subexpressions, and report those types to the user. This feature inspired similar work in the Glasgow Haskell Compiler (GHC).

## Examples

Here is a minimal "Hello, World!" program in PureScript:

```mw
module Main where

import Effect.Console (log)

main = log "Hello World!"
```

Here, the type of the program is inferred and checked by the PureScript transpiler. A more verbose version of the same program might include explicit type annotations:

```mw
module Main where

import Prelude

import Effect (Effect)
import Effect.Console (log)

main :: Effect Unit
main = log "Hello World!"
```
