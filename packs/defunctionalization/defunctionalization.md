---
title: "Defunctionalization"
source: https://en.wikipedia.org/wiki/Defunctionalization
domain: defunctionalization
license: CC-BY-SA-4.0
tags: defunctionalization transform, closure conversion, higher-order function, apply function
fetched: 2026-07-02
---

# Defunctionalization

In programming languages, **defunctionalization** is a compile-time transformation which eliminates higher-order functions, replacing them by a single first-order *apply* function. The technique was first described by John C. Reynolds in his 1972 paper, "Definitional Interpreters for Higher-Order Programming Languages". Reynolds' observation was that a given program contains only finitely many function abstractions, so that each can be assigned and replaced by a unique identifier. Every function application within the program is then replaced by a call to the *apply* function with the function identifier as the first argument. The *apply* function's only job is to dispatch on this first argument, and then perform the instructions denoted by the function identifier on the remaining arguments.

One complication to this basic idea is that function abstractions may reference free variables. In such situations, defunctionalization must be preceded by lambda lifting, so that any free variables of a function abstraction are passed as extra arguments to *apply*. In addition, if closures are supported as first-class values, it becomes necessary to represent these captured bindings by creating data structures.

Instead of having a single *apply* function dispatch on all function abstractions in a program, various kinds of control flow analysis (including simple distinctions based on arity or type signature) can be employed to determine which function(s) may be called at each function application site, and a specialized *apply* function may be referenced instead. Alternatively, the target language may support indirect calls through function pointers, which may be more efficient and extensible than a dispatch-based approach.

Besides its use as a compilation technique for higher-order functional languages, defunctionalization has been studied (particularly by Olivier Danvy and collaborators) as a way of mechanically transforming interpreters into abstract machines. Defunctionalization is also related to the technique from object-oriented programming of representing functions by function objects (as an alternative to closures).

## Example

The following is a Haskell translation of an example due to Olivier Danvy. Consider the `Tree` datatype and the following program.

```mw
data Tree a = Leaf a
            | Node (Tree a) (Tree a)
```

```mw
cons :: a -> [a] -> [a]
cons x xs = x : xs

o :: (b -> c) -> (a -> b) -> a -> c
o f g x = f (g x)

flatten :: Tree t -> [t]
flatten t = walk t []

walk :: Tree t -> [t] -> [t]
walk (Leaf x)     = cons x
walk (Node t1 t2) = o (walk t1) (walk t2)
```

Defunctionalization replaces all higher-order functions (in this case, `o` is the only higher-order function) with a value of the `Lam` datatype. Instead of calling higher-order functions directly, it introduces an `apply` function that interprets the `Lam` datatype.

```mw
data Lam a = LamCons a
           | LamO (Lam a) (Lam a)

apply :: Lam a -> [a] -> [a]
apply (LamCons x)  xs = x : xs
apply (LamO f1 f2) xs = apply f1 (apply f2 xs)

cons_def :: a -> Lam a
cons_def x  = LamCons x

o_def :: Lam a -> Lam a -> Lam a
o_def f1 f2 = LamO f1 f2

flatten_def :: Tree t -> [t]
flatten_def t = apply (walk_def t) []

walk_def :: Tree t -> Lam t
walk_def (Leaf x)     = cons_def x
walk_def (Node t1 t2) = o_def (walk_def t1) (walk_def t2)
```
