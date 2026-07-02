---
title: "Applicative functor"
source: https://en.wikipedia.org/wiki/Applicative_functor
domain: monad-transformers
license: CC-BY-SA-4.0
tags: monad transformer, monad stack, kleisli category, free monad
fetched: 2026-07-02
---

# Applicative functor

In functional programming, an **applicative functor**, or an applicative for short, is an intermediate structure between functors and monads. Applicative functors allow for functorial computations to be sequenced (unlike plain functors), but don't allow using results from prior computations in the definition of subsequent ones (unlike monads).

In terms of category theory, applicative functors may be defined as lax monoidal functors with tensorial strength. This may not be the most obvious categorification of the standard definition of applicative functor given below, but they are equivalent in the category of Haskell types. Note that the observation that all monads are applicative functors is specific to the category of Haskell types, and is not true in general with this categorical definition of applicative functor; monads in an arbitrary category need not preserve any monoidal product.

Applicative functors were introduced in 2008 by Conor McBride and Ross Paterson in their paper *Applicative programming with effects*.

Applicative functors first appeared as a library feature in Haskell, but have since spread to other languages such as Idris, Agda, OCaml, Scala, and F#. Glasgow Haskell, Idris, and F# offer language features designed to ease programming with applicative functors. In Haskell, applicative functors are implemented in the `Applicative` type class.

While in languages like Haskell monads are applicative functors, this is not always the case in general settings of category theory—examples of monads which are *not* strong can be found on Math Overflow.

## Definition

In Haskell, an applicative is a parameterized type that can be thought of as being a container for data of the parameter type with two additional methods: `pure` and `<*>`. The `pure` method for an applicative of parameterized type `f` has type

```mw
pure :: a -> f a
```

and can be thought of as bringing values into the applicative. The `<*>` method for an applicative of type `f` has type

```mw
(<*>) :: f (a -> b) -> f a -> f b
```

and can be thought of as the equivalent of function application inside the applicative.

Alternatively, instead of providing `<*>`, one may provide a function called `liftA2`. These two functions may be defined in terms of each other; therefore only one is needed for a minimally complete definition.

Applicatives are also required to satisfy four equational laws:

- Identity: `pure id <*> v = v`
- Composition: `pure (.) <*> u <*> v <*> w = u <*> (v <*> w)`
- Homomorphism: `pure f <*> pure x = pure (f x)`
- Interchange: `u <*> pure y = pure ($ y) <*> u`

Every applicative is a functor. To be explicit, given the methods `pure` and `<*>`, `fmap` can be implemented as

```mw
fmap g x = pure g <*> x
```

The commonly used notation `g <$> x` is equivalent to `pure g <*> x`.

## Examples

In Haskell, the Maybe type can be made an instance of the type class `Applicative` using the following definition:

```mw
instance Applicative Maybe where
    -- pure :: a -> Maybe a
    pure a = Just a

    -- (<*>) :: Maybe (a -> b) -> Maybe a -> Maybe b
    Nothing  <*> _        = Nothing
    _        <*> Nothing  = Nothing
    (Just g) <*> (Just x) = Just (g x)
```

As stated in the Definition section, `pure` turns an `a` into a `Maybe a`, and `<*>` applies a Maybe function to a Maybe value. Using the Maybe applicative for type `a` allows one to operate on values of type `a` with the error being handled automatically by the applicative machinery. For example, to add `m :: Maybe Int` and `n :: Maybe Int`, one needs only write

```mw
(+) <$> m <*> n
```

For the non-error case, adding `m=Just i` and `n=Just j` gives `Just(i+j)`. If either of `m` or `n` is `Nothing`, then the result will be `Nothing` also. This example also demonstrates how applicatives allow a sort of generalized function application.
