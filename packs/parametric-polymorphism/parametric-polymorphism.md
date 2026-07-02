---
title: "Parametric polymorphism"
source: https://en.wikipedia.org/wiki/Parametric_polymorphism
domain: parametric-polymorphism
license: CC-BY-SA-4.0
tags: parametric polymorphism, type parameter, generic programming, type constructor
fetched: 2026-07-02
---

# Parametric polymorphism

In programming languages and type theory, **parametric polymorphism** allows a single piece of code to be given a "generic" type, using variables in place of actual types, and then instantiated with particular types as needed. Parametrically polymorphic functions and data types are sometimes called **generic functions** and **generic datatypes**, respectively, and they form the basis of generic programming.

Parametric polymorphism may be contrasted with ad hoc polymorphism. Parametrically polymorphic definitions are *uniform*: they behave identically regardless of the type they are instantiated at. In contrast, ad hoc polymorphic definitions are given a distinct definition for each type. Thus, ad hoc polymorphism can generally only support a limited number of such distinct types, since a separate implementation has to be provided for each type.

The usual theoretical device for studying parametric polymorphism is system F, which extends simply typed lambda calculus with quantification over types.

## Basic definition

It is possible to write functions that do not depend on the types of their arguments. For example, the identity function ${\mathsf {id}}(x)=x$ simply returns its argument unmodified. This naturally gives rise to a family of potential types, such as ${\mathsf {Int}}\to {\mathsf {Int}}$ , ${\mathsf {Bool}}\to {\mathsf {Bool}}$ , ${\mathsf {String}}\to {\mathsf {String}}$ , and so on. Parametric polymorphism allows ${\mathsf {id}}$ to be given a single, most general type by introducing a universally quantified type variable:

${\mathsf {id}}:\forall \alpha .\alpha \to \alpha$

The polymorphic definition can then be *instantiated* by substituting any concrete type for $\alpha$ , yielding the full family of potential types.

The identity function is a particularly extreme example, but many other functions also benefit from parametric polymorphism. For example, an ${\mathsf {append}}$ function that concatenates two lists does not inspect the elements of the list, only the list structure itself. Therefore, ${\mathsf {append}}$ can be given a similar family of types, such as $[{\mathsf {Int}}]\times [{\mathsf {Int}}]\to [{\mathsf {Int}}]$ , $[{\mathsf {Bool}}]\times [{\mathsf {Bool}}]\to [{\mathsf {Bool}}]$ , and so on, where $[T]$ denotes a list of elements of type T . The most general type is therefore

${\mathsf {append}}:\forall \alpha .[\alpha ]\times [\alpha ]\to [\alpha ]$

which can be instantiated to any type in the family.

Parametrically polymorphic functions like ${\mathsf {id}}$ and ${\mathsf {append}}$ are said to be *parameterized over* an arbitrary type $\alpha$ . Both ${\mathsf {id}}$ and ${\mathsf {append}}$ are parameterized over a single type, but functions may be parameterized over arbitrarily many types. For example, the ${\mathsf {fst}}$ and ${\mathsf {snd}}$ functions that return the first and second elements of a pair, respectively, can be given the following types:

${\begin{aligned}{\mathsf {fst}}&:\forall \alpha .\forall \beta .\alpha \times \beta \to \alpha \\{\mathsf {snd}}&:\forall \alpha .\forall \beta .\alpha \times \beta \to \beta \end{aligned}}$

In the expression ${\mathsf {fst}}((3,{\mathsf {true}}))$ , $\alpha$ is instantiated to ${\mathsf {Int}}$ and $\beta$ is instantiated to ${\mathsf {Bool}}$ in the call to ${\mathsf {fst}}$ , so the type of the overall expression is ${\mathsf {Int}}$ .

The syntax used to introduce parametric polymorphism varies significantly between programming languages. For example, in some programming languages, such as Haskell, the $\forall \alpha$ quantifier is implicit and may be omitted. Other languages require types to be instantiated explicitly at some or all of a parametrically polymorphic function's call sites.

## History

Parametric polymorphism was first introduced to programming languages in ML in 1975. Today it exists in Standard ML, OCaml, F#, Ada, Haskell, Mercury, Visual Prolog, Scala, Julia, Python, TypeScript, C++ and others. Java, C#, Visual Basic .NET and Delphi have each introduced "generics" for parametric polymorphism. Some implementations of type polymorphism are superficially similar to parametric polymorphism while also introducing ad hoc aspects. One example is C++ template specialization.

In the 1980s, Leivant introduced a stratified (i.e. predicative) version of Girard and Reynold's system F. Leivant's approach is based on a notion of rank of the quantifiers, which measures their nesting depth inside function constructors. The ML approach is limited to rank-1 polymorphism in this perspective. Haskell has adopted higher-rank parametric polymorphism in the 1990s. For example, rank-2 parametric polymorphism is used in Haskell to define the `runST` monad, which effectively simulates a type and effect system, with "isolated regions of imperative programming". At type level, state isolation essentially stems from the deeper, rank-2 quantification over state in `runST`. (This is not enough to formally describe the runtime semantics of `runST`. For the latter, one needs some additional ingredients like separation logic.)

## Predicativity, impredicativity, and higher-rank polymorphism

A type is said to be of rank *k* (for some fixed integer *k*) if no path from its root to a $\forall$ quantifier passes to the left of *k* or more arrows, when the type is drawn as a tree. A type system is said to support rank-*k* polymorphism if it admits types with rank less than or equal to *k*. For example, a type system that supports rank-2 polymorphism would allow $(\forall \alpha .\alpha \rightarrow \alpha )\rightarrow T$ but not $((\forall \alpha .\alpha \rightarrow \alpha )\rightarrow T)\rightarrow T$ . A type system that admits types of arbitrary rank is said to be "rank-*n* polymorphic".

(This notion of rank is a different from how quantifier rank is defined in classical logic because here it measures nesting depth relative to a non-quantifier connective, whereas in classical logic non-quantifier connectives do not increase the rank of quantifiers nested under them, but other quantifiers do.)

### Rank-1 (predicative) polymorphism

In a *predicative* type system (also known as a *prenex polymorphic* system), type variables may not be instantiated with polymorphic types. Predicative type theories include Martin-Löf type theory and Nuprl. This is very similar to what is called "ML-style" or "Let-polymorphism" (technically ML's Let-polymorphism has a few other syntactic restrictions). This restriction makes the distinction between polymorphic and non-polymorphic types very important; thus in predicative systems polymorphic types are sometimes referred to as *type schemas* to distinguish them from ordinary (monomorphic) types, which are sometimes called *monotypes*.

A consequence of predicativity is that all types can be written in a form that places all quantifiers at the outermost (prenex) position. For example, consider the ${\mathsf {append}}$ function described above, which has the following type:

${\mathsf {append}}:\forall \alpha .[\alpha ]\times [\alpha ]\to [\alpha ]$

In order to apply this function to a pair of lists, a concrete type T must be substituted for the variable $\alpha$ such that the resulting function type is consistent with the types of the arguments. In an *impredicative* system, T may be any type whatsoever, including a type that is itself polymorphic; thus ${\mathsf {append}}$ can be applied to pairs of lists with elements of any type—even to lists of polymorphic functions such as ${\mathsf {append}}$ itself. Polymorphism in the language ML is predicative. This is because predicativity, together with other restrictions, makes the type system simple enough that full type inference is always possible.

As a practical example, OCaml (a descendant or dialect of ML) performs type inference and supports impredicative polymorphism, but in some cases when impredicative polymorphism is used, the system's type inference is incomplete unless some explicit type annotations are provided by the programmer.

### Higher-rank polymorphism

Some type systems support an impredicative function type constructor even though other type constructors remain predicative. For example, the type $(\forall \alpha .\alpha \rightarrow \alpha )\rightarrow T$ is permitted in a system that supports higher-rank polymorphism, even though $[\forall \alpha .\alpha \rightarrow \alpha ]$ may not be.

Type inference for rank-2 polymorphism is decidable, but for rank-3 and above, it is not.

### Impredicative polymorphism

*Impredicative polymorphism* (also called *first-class polymorphism*) is the most powerful form of parametric polymorphism. In formal logic, a definition is said to be impredicative if it is self-referential; in type theory, it refers to the ability for a type to be in the domain of a quantifier it contains. This allows the instantiation of any type variable with any type, including polymorphic types. An example of a system supporting full impredicativity is System F, which allows instantiating $\forall \alpha .\alpha \to \alpha$ at any type, including itself.

In type theory, the most frequently studied impredicative typed λ-calculi are based on those of the lambda cube, especially System F.

### Generalizations of the notion of rank

Leivant's notion of rank can be generalized to symbols other than quantifiers with a simple, suitable substitution. For example, it can be applied to the (constructor of) intersection types. However, the rank-based type hierarchy that results can have different properties. For instance, type inference for rank-3 and above system F remains undecidable (as detailed above), however, for intersection types, type inference is decidable for all finite ranks.

## Bounded parametric polymorphism

In 1985, Luca Cardelli and Peter Wegner recognized the advantages of allowing *bounds* on the type parameters. Many operations require some knowledge of the data types, but can otherwise work parametrically. For example, to check whether an item is included in a list, we need to compare the items for equality. In Standard ML, type parameters of the form *’’a* are restricted so that the equality operation is available, thus the function would have the type *’’a* × *’’a* list → bool and *’’a* can only be a type with defined equality. In Haskell, bounding is achieved by requiring types to belong to a type class; thus the same function has the type ${\textstyle \mathrm {Eq} \,\alpha \,\Rightarrow \alpha \,\rightarrow \left[\alpha \right]\rightarrow \mathrm {Bool} }$ in Haskell. In most object-oriented programming languages that support parametric polymorphism, parameters can be constrained to be subtypes of a given type (see the articles Subtype polymorphism and Generic programming).
