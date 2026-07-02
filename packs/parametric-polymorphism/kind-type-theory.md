---
title: "Kind (type theory)"
source: https://en.wikipedia.org/wiki/Kind_(type_theory)
domain: parametric-polymorphism
license: CC-BY-SA-4.0
tags: parametric polymorphism, type parameter, generic programming, type constructor
fetched: 2026-07-02
---

# Kind (type theory)

In the area of mathematical logic and computer science known as type theory, a **kind** is the type of a type constructor or, less commonly, the type of a higher-order type operator (type constructor). A kind system is essentially a simply typed lambda calculus "one level up", endowed with a primitive type, usually denoted * and called "type", which is the kind of any data type that does not need any type parameters.

Syntactically, it is natural to consider polymorphic data types to be type constructors, thus non-polymorphic types to be nullary type constructors. But all nullary constructors, thus all monomorphic types, have the same, simplest kind; namely * . This is essentially a stratified type theory approach, in the style of Leivant's stratified system F, a predicative variant of Girard's impredicative system F.

Since higher-order type operators are uncommon in programming languages, in most programming practice, kinds are used to distinguish between data types and the types of constructors which are used to implement parametric polymorphism. Kinds appear, either explicitly or implicitly, in languages whose type systems account for parametric polymorphism in a programmatically accessible way, such as C++, Haskell, and Scala. ML-polymorphism coincides with rank-1 polymorphism in Leivant's stratification, thus kinds are not explicitly present in ML, although theoretical presentations of ML's type inference algorithm sometimes do use kinds. This is useful for instance when record types (and row polymorphism) are introduced, because the record type constructor is basically a partial function; it does not allow for instance labels to be repeated. This restriction can be expressed as the row kind being parametrized by a set of labels.

## Examples

- * , pronounced "type", is the kind of all data types seen as nullary type constructors, and also called proper types in this context. This normally includes function types in functional programming languages.
- $*\rightarrow *$ is the kind of a unary type constructor, e.g., of a list type constructor.
- $*\rightarrow *\rightarrow *$ is the kind of a binary type constructor (via currying), e.g., of a pair type constructor, and also that of a function type constructor (not to be confused with the result of its application, which itself is a function type, thus of kind * )
- $(*\rightarrow *)\rightarrow *$ is the kind of a higher-order type operator from unary type constructors to proper types.
- In Cyclone, boxed types have kind B, while unboxed types have kind A (for "any") and there is a subkinding relationship between B and A, B≤A.
- Cyclone also uses kinds to separate ordinary types from lock names; locks have kind L. Furthermore, there are shareable (S) and unshareable (U) kinds. This kinding separation ensures that all data shared between threads uses locking. (This results in a "necessarily conservative" data race prevention discipline, which does prevent some race-free programs from type checking.) More precisely, combined with the previous example, that results in the sub-kidding relationships: BS≤BU, AS≤AU, BS≤AS, BU≤AU, and BS≤AU in Cyclone. B and A are, in fact, short-hand for BU and AU.

## Kinds in Haskell

Haskell98 had mostly untyped kinds, thus kinds in Haskell98 are more of an arity specifier. For instance, taking the usual option generics as example, it could distinguish between the kind of the constructor `Maybe` of kind `* -> *` and `Maybe Int` (for instance) of kind `*`, but the arrow was essentially the only kind constructor. Around 2010, this was approach was deemed unsatisfactory, especially with the introduction of GADTs in the language, because the untyped stratification prevented the "promotion" (or equal treatment) of kind equations on par with type equations in a GADT context. Consequently Haskell (around GHC 7.4) added "promoted datatypes", in which a type is automatically mirrored to a kind. (There is a certain similarity between this concrete approach with how type schemes with no metavariables are identified with the underlying types, in certain theoretical presentation of ML's type inference algorithm, although in that context it is a mere mathematical artifice.) As this in turn introduced more ground kinds (called "datakinds") than the mere `*`, kind polymorphism was added to Haskell around that time as well. Its proponents deemed it a resonable compromise between Haskell98 and adding full-fledged dependent types.

Haskell documentation uses the same arrow for both function *types* and *kinds*.

The kind system of Haskell 98 includes exactly two kinds:

- * , pronounced "type" is the kind of all data types.
- $k_{1}\rightarrow k_{2}$ is the kind of a unary type constructor, which takes a type of kind $k_{1}$ and produces a type of kind $k_{2}$ .

An inhabited type (as proper types are called in Haskell) is a type which has values. For example, ignoring type classes which complicate the picture, `4` is a value of type `Int`, while `[1, 2, 3]` is a value of type `[Int]` (list of Ints). Therefore, `Int` and `[Int]` have kind * , but so does any function type, for example `Int -> Bool` or even `Int -> Int -> Bool`.

A type constructor takes one or more type arguments, and produces a data type when enough arguments are supplied, i.e. it supports partial application thanks to currying. This is how Haskell achieves parametric types. For example, the type `[]` (list) is a type constructor - it takes a single argument to specify the type of the elements of the list. Hence, `[Int]` (list of Ints), `[Float]` (list of Floats) and even `[[Int]]` (list of lists of Ints) are valid applications of the `[]` type constructor. Therefore, `[]` is a type of kind $*\rightarrow *$ . Because `Int` has kind * , applying `[]` to it results in `[Int]`, of kind * . The 2-tuple constructor `(,)` has kind $*\rightarrow *\rightarrow *$ , the 3-tuple constructor `(,,)` has kind $*\rightarrow *\rightarrow *\rightarrow *$ and so on.

### Kind inference

Standard Haskell does not allow polymorphic kinds, in contrast to parametric polymorphism on types, which Haskell supports. For example:

```mw
data Tree z = Leaf | Fork (Tree z) (Tree z)
```

the kind of `z` could be anything, including * , but also $*\rightarrow *$ etc. Haskell by default will always infer kinds to be * , unless the type explicitly indicates otherwise (see below). Therefore the type checker will reject this use of `Tree`:

```mw
type FunnyTree = Tree []     -- invalid
```

because the kind of `[]`, $*\rightarrow *$ does not match the expected kind for `z`, which is always * .

Higher-order type operators are allowed however. For example:

```mw
data App unt z = Z (unt z)
```

has kind $(*\rightarrow *)\rightarrow *\rightarrow *$ , i.e. `unt` is expected to be a unary data constructor, which gets applied to its argument, which must be a type, and returns another type.

Glasgow Haskell Compiler (GHC) has the extension `PolyKinds`, which, together with `KindSignatures`, allows polymorphic kinds. For example:

```mw
data Tree (z :: k) = Leaf | Fork (Tree z) (Tree z)
type FunnyTree = Tree []     -- OK
```

Since GHC 8.0.1, types and kinds are merged. Despite adding the typing rule `* : *`, which would usually cause Girard's paradox, typing in the post-2012 versions of Haskell remains decidable, because the GHC typing algorithms don't rely on that rule; instead "all type equalities are witnessed by finite equality proofs, not potentially infinite reductions", according to its authors.

At the introduction of unboxed types in GHC, these were abstracted to the `#` kind, different from the `*` kind of boxed types. And there was no subkinding relation between the two, meaning for instance that a partially applied polymorphic function, which was always inferred to be over boxed types, could not be applied to unboxed types. In GHC 8.2 this approach was changed to use kind polymorphism instead. There is a new `TYPE` constructor that is used to classify types, and the old `*` kind, now aliased to `Type` is defined as `TYPE LiftedRep`, while a boxed type like `Int#` is defined as `TYPE IntRep`. The argument to TYPE "is a perfectly ordinary algebraic data type, promoted to the kind level by GHC’s DataKinds extension. [...] Only TYPE is primitive in this design." Because all boxed types like `Int` and `Bool` have the same kind, they can share calling convention details in the compiler implementation, while the unboxed types are treated individually. The most general type of the polymorphic function constructor is henceforth `TYPE r1 → TYPE r2 → Type` in GHC 8. This approach is dubbed "levity polymorphism". Levity-polymorphic types cannot be inferred in GHC, only type checked. This is because the most general type for such functions is un-compilable (due to unknown calling convention details for the arguments), so the loss of principal types (for them) is inevitable.
