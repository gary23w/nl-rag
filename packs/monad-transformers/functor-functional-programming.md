---
title: "Functor (functional programming)"
source: https://en.wikipedia.org/wiki/Functor_(functional_programming)
domain: monad-transformers
license: CC-BY-SA-4.0
tags: monad transformer, monad stack, kleisli category, free monad
fetched: 2026-07-02
---

# Functor (functional programming)

In functional programming, a **functor** is a design pattern inspired by the definition from category theory that allows one to apply a function to values inside a generic type without changing the structure of the generic type. In Haskell this idea can be captured in a type class:

```mw
class Functor f where
  fmap :: (a -> b) -> f a -> f b
```

This declaration says that any instance of `Functor` must support a method `fmap`, which maps a function over the elements of the instance.

Functors in Haskell should also obey the so-called *functor laws*, which state that the mapping operation preserves the identity function and composition of functions:

```mw
fmap id = id
fmap (g . h) = (fmap g) . (fmap h)
```

where `.` stands for function composition.

In Scala a trait can instead be used:

```mw
trait Functor[F[_]] {
  def map[A,B](a: F[A])(f: A => B): F[B]
}
```

Functors form a base for more complex abstractions like applicative functors, monads, and comonads, all of which build atop a canonical functor structure. Functors are useful in modeling functional effects by values of parameterized data types. Modifiable computations are modeled by allowing a pure function to be applied to values of the "inner" type, thus creating the new overall value which represents the modified computation (which may have yet to run).

## Examples

In Haskell, lists are a simple example of a functor. We may implement `fmap` as

```mw
fmap f []     = []
fmap f (x:xs) = (f x) : fmap f xs
```

A binary tree may similarly be described as a functor:

```mw
data Tree a = Leaf | Node a (Tree a) (Tree a)
instance Functor Tree where
   fmap f Leaf         = Leaf
   fmap f (Node x l r) = Node (f x) (fmap f l) (fmap f r)
```

If we have a binary tree `tr :: Tree a` and a function `f :: a -> b`, the function `fmap f tr` will apply `f` to every element of `tr`. For example, if `a` is `Int`, adding 1 to each element of `tr` can be expressed as `fmap (+ 1) tr`.
