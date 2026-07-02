---
title: "Generalized algebraic data type"
source: https://en.wikipedia.org/wiki/Generalized_algebraic_data_type
domain: system-f
license: CC-BY-SA-4.0
tags: System F, polymorphic lambda calculus, second-order lambda calculus, impredicative polymorphism
fetched: 2026-07-02
---

# Generalized algebraic data type

In functional programming, a **generalized algebraic data type** (**GADT**, also **first-class phantom type**, **guarded recursive datatype**, or **equality-qualified type**) is a generalization of a parametric algebraic data type (ADT).

## Overview

In a GADT, the product constructors (called data constructors in Haskell) can provide an explicit instantiation of the ADT as the type instantiation of their return value. This allows defining functions with a more advanced type behaviour. For a data constructor of Haskell 2010, the return value has the type instantiation implied by the instantiation of the ADT parameters at the constructor's application.

```mw
-- A parametric ADT that is not a GADT
data List a = Nil | Cons a (List a)

integers :: List Int
integers = Cons 12 (Cons 107 Nil)

strings :: List String
strings = Cons "boat" (Cons "dock" Nil)

-- A GADT
data Expr a where
    EBool  :: Bool     -> Expr Bool
    EInt   :: Int      -> Expr Int
    EEqual :: Expr Int -> Expr Int  -> Expr Bool

eval :: Expr a -> a
eval e = case e of
    EBool a    -> a
    EInt a     -> a
    EEqual a b -> (eval a) == (eval b)

expr1 :: Expr Bool
expr1 = EEqual (EInt 2) (EInt 3)

ret = eval expr1 -- False
```

They are currently implemented in the Glasgow Haskell Compiler (GHC) as a non-standard extension, used by, among others, Pugs and Darcs. OCaml supports GADT natively since version 4.00.

The GHC implementation provides support for existentially quantified type parameters and for local constraints.

## History

An early version of generalized algebraic data types were described by Augustsson & Petersson (1994) and based on pattern matching in ALF.

Generalized algebraic data types were introduced independently by Cheney & Hinze (2003) and prior by Xi, Chen & Chen (2003) as extensions to the algebraic data types of ML and Haskell. Both are essentially equivalent to each other. They are similar to the *inductive families of data types* (or *inductive datatypes*) found in Rocq's Calculus of Inductive Constructions and other dependently typed languages, modulo the dependent types and except that the latter have an additional positivity restriction which is not enforced in GADTs.

Sulzmann, Wazny & Stuckey (2006) introduced *extended algebraic data types* which combine GADTs together with the existential data types and type class constraints.

Type inference in the absence of any programmer supplied type annotation, is undecidable and functions defined over GADTs do not admit principal types in general. Type reconstruction requires several design trade-offs and is an area of active research (Peyton Jones, Washburn & Weirich 2004; Peyton Jones et al. 2006).

In spring 2021, Scala 3.0 was released. This major update of Scala introduced the possibility to write GADTs with the same syntax as algebraic data types, which is not the case in other programming languages according to Martin Odersky.

## Applications

Applications of GADTs include generic programming, modelling programming languages (higher-order abstract syntax), maintaining invariants in data structures, expressing constraints in embedded domain-specific languages, and modelling objects.

### Higher-order abstract syntax

An important application of GADTs is to embed higher-order abstract syntax in a type safe fashion. Here is an embedding of the simply typed lambda calculus with an arbitrary collection of base types, product types (tuples) and a fixed point combinator:

```mw
data Lam :: * -> * where
  Lift :: a                     -> Lam a        -- ^ lifted value
  Pair :: Lam a -> Lam b        -> Lam (a, b)   -- ^ product
  Lam  :: (Lam a -> Lam b)      -> Lam (a -> b) -- ^ lambda abstraction
  App  :: Lam (a -> b) -> Lam a -> Lam b        -- ^ function application
  Fix  :: Lam (a -> a)          -> Lam a        -- ^ fixed point
```

And a type safe evaluation function:

```mw
eval :: Lam t -> t
eval (Lift v)   = v
eval (Pair l r) = (eval l, eval r)
eval (Lam f)    = \x -> eval (f (Lift x))
eval (App f x)  = (eval f) (eval x)
eval (Fix f)    = (eval f) (eval (Fix f))
```

The factorial function can now be written as:

```mw
fact = Fix (Lam (\f -> Lam (\y -> Lift (if eval y == 0 then 1 else eval y * (eval f) (eval y - 1)))))
eval(fact)(10)
```

Problems would have occurred using regular algebraic data types. Dropping the type parameter would have made the lifted base types existentially quantified, making it impossible to write the evaluator. With a type parameter, it is still restricted to one base type. Further, ill-formed expressions such as `App (Lam (\x -> Lam (\y -> App x y))) (Lift True)` would have been possible to construct, while they are type incorrect using the GADT. A well-formed analogue is `App (Lam (\x -> Lam (\y -> App x y))) (Lift (\z -> True))`. This is because the type of `x` is `Lam (a -> b)`, inferred from the type of the `Lam` data constructor.
