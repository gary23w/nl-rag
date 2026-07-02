---
title: "Dependent type"
source: https://en.wikipedia.org/wiki/Dependent_type
domain: agda-lang
license: CC-BY-SA-4.0
tags: agda language, agda lang, agda proof
fetched: 2026-07-02
---

# Dependent type

In computer science and logic, a **dependent type** is a type whose definition depends on a value. It is an overlapping feature of type theory and type systems. In intuitionistic type theory, dependent types are used to encode logic's quantifiers like "for all" and "there exists". In functional programming languages like Agda, ATS, Rocq (previously known as *Coq*), F*, Epigram, Idris, and Lean, dependent types help reduce bugs by enabling the programmer to assign types that further restrain the set of possible implementations.

Two common examples of dependent types are *dependent functions* and *dependent pairs*. The return type of a dependent function may depend on the *value* (not just type) of one of its arguments. For instance, a function that takes a positive integer n may return an array of length n , where the array length is part of the type of the array. (Note that this is different from polymorphism and generic programming, both of which include the type as an argument.) A dependent pair may have a second value, the type of which depends on the first value. Sticking with the array example, a dependent pair may be used to pair an array with its length in a type-safe way.

Dependent types add complexity to a type system. Deciding the equality of dependent types in a program may require computations. If arbitrary values are allowed in dependent types, then deciding type equality may involve deciding whether two arbitrary programs produce the same result; hence the decidability of type checking may depend on the given type theory's semantics of equality, that is, whether the type theory is intensional or extensional.

## History

In 1934, Haskell Curry noticed that the types used in typed lambda calculus, and in its combinatory logic counterpart, followed the same pattern as axioms in propositional logic. Going further, for every proof in the logic, there was a matching function (term) in the programming language. One of Curry's examples was the correspondence between simply typed lambda calculus and intuitionistic logic.

Predicate logic is an extension of propositional logic, adding quantifiers. Howard and de Bruijn extended lambda calculus to match this more powerful logic by creating types for dependent functions, which correspond to "for all", and dependent pairs, which correspond to "there exists".

Because of this, and other work by Howard, propositions-as-types is known as the Curry–Howard correspondence.

## Formal definition

In dependent type theory, a dependent type is a type whose specification may vary with a value, and can be viewed as analogous to an indexed family of sets. Let ${\mathcal {U}}$ denote a universe of types, and write $A:{\mathcal {U}}$ to indicate that A is a type in ${\mathcal {U}}$ . For a term a of type A , write $a:A$ . A dependent **family of types** over A is written $B:A\to {\mathcal {U}}$ , meaning that to each term $a:A$ the family assigns a type $B(a):{\mathcal {U}}$ . Thus, given $A:{\mathcal {U}}$ and $B:A\to {\mathcal {U}}$ , the expression $B(a)$ denotes a type that depends on the particular value a . In standard terminology, this is described by saying that the type $B(a)$ varies with a .

### Π type

A function whose type of return value varies with its argument (i.e. there is no fixed codomain) is a **dependent function** and the type of this function is called **dependent product type**, **pi-type** (**Π type**) or **dependent function type**. From a family of types $B:A\to {\mathcal {U}}$ we may construct the type of dependent functions ${\textstyle \prod _{x:A}B(x)}$ , whose terms are functions that take a term $a:A$ and return a term in $B(a)$ . For this example, the dependent function type is typically written as ${\textstyle \prod _{x:A}B(x)}$ or ${\textstyle \prod {(x:A)}B(x)}$ .

If $B:A\to {\mathcal {U}}$ is a constant function, the corresponding dependent product type is equivalent to an ordinary function type. That is, ${\textstyle \prod _{x:A}B}$ is judgmentally equal to $A\to B$ when B does not depend on x .

The name 'Π-type' comes from the idea that these may be viewed as a Cartesian product of types. Π-types can also be understood as models of universal quantifiers.

For example, if we write $\operatorname {Vec} (\mathbb {R} ,n)$ for *n*-tuples of real numbers, then ${\textstyle \prod _{n:\mathbb {N} }\operatorname {Vec} (\mathbb {R} ,n)}$ would be the type of a function which, given a natural number n, returns a tuple of real numbers of size n. The usual function space arises as a special case when the range type does not actually depend on the input. E.g. ${\textstyle \prod _{n:\mathbb {N} }{\mathbb {R} }}$ is the type of functions from natural numbers to the real numbers, which is written as $\mathbb {N} \to \mathbb {R}$ in typed lambda calculus.

For a more concrete example, taking A to be the type of unsigned integers from 0 to 255 (the ones that fit into 8 bits or 1 byte) and $B(a)=X_{a}$ for $a:A$ , then ${\textstyle \prod _{x:A}B(x)}$ devolves into the product of $X_{0}\times X_{1}\times X_{2}\times \ldots \times X_{253}\times X_{254}\times X_{255}$ .

### Σ type

The dual of the dependent product type is the **dependent pair type**, **dependent sum type**, **sigma-type**, or (confusingly) **dependent product type**. Sigma-types can also be understood as existential quantifiers. Continuing the above example, if, in the universe of types ${\mathcal {U}}$ , there is a type $A:{\mathcal {U}}$ and a family of types $B:A\to {\mathcal {U}}$ , then there is a dependent pair type ${\textstyle \sum _{x:A}B(x)}$ . (The alternative notations are similar to that of Π types.)

The dependent pair type captures the idea of an ordered pair where the type of the second term is dependent on the value of the first. If ${\textstyle (a,b):\sum _{x:A}B(x),}$ then $a:A$ and $b:B(a)$ . If B is a constant function, then the dependent pair type becomes (is judgmentally equal to) the product type, that is, an ordinary Cartesian product $A\times B$ .

For a more concrete example, taking A to again be type of unsigned integers from 0 to 255, and $B(a)$ to again be equal to $X_{a}$ for 256 more arbitrary $X_{a}$ , then ${\textstyle \sum _{x:A}B(x)}$ devolves into the sum $X_{0}+X_{1}+X_{2}+\ldots +X_{253}+X_{254}+X_{255}$ .

#### Example as existential quantification

Let $A:{\mathcal {U}}$ be some type, and let $B:A\to {\mathcal {U}}$ . By the Curry–Howard correspondence, B can be interpreted as a logical predicate on terms of A . For a given $a:A$ , whether the type $B(a)$ is inhabited indicates whether a satisfies this predicate. The correspondence can be extended to existential quantification and dependent pairs: the proposition $\exists {a}{\in }A\,B(a)$ is true if and only if the type ${\textstyle \sum _{a:A}B(a)}$ is inhabited.

For example, $m:\mathbb {N}$ is less than or equal to $n:\mathbb {N}$ if and only if there exists another natural number $k:\mathbb {N}$ such that $m+k=n$ . In logic, this statement is codified by existential quantification:

$m\leq n\iff \exists {k}{\in }\mathbb {N} \,m+k=n.$

This proposition corresponds to the dependent pair type:

$\sum _{k:\mathbb {N} }m+k=n.$

That is, a proof of the statement that m is less than or equal to n is a pair that contains both a non-negative number k , which is the difference between m and n , and a proof of the equality $m+k=n$ .

## Systems of the lambda cube

Henk Barendregt developed the lambda cube as a means of classifying type systems along three axes. The eight corners of the resulting cube-shaped diagram each correspond to a type system, with simply typed lambda calculus in the least expressive corner, and calculus of constructions in the most expressive. The three axes of the cube correspond to three different augmentations of the simply typed lambda calculus: the addition of dependent types, the addition of polymorphism, and the addition of higher kinded type constructors (functions from types to types, for example). The lambda cube is generalized further by pure type systems.

### First order dependent type theory

The system $\lambda \Pi$ of pure first order dependent types, corresponding to the logical framework LF, is obtained by generalising the function space type of the simply typed lambda calculus to the dependent product type.

### Second order dependent type theory

The system $\lambda \Pi 2$ of second order dependent types is obtained from $\lambda \Pi$ by allowing quantification over type constructors. In this theory the dependent product operator subsumes both the $\to$ operator of simply typed lambda calculus and the $\forall$ binder of System F.

### Higher order dependently typed polymorphic lambda calculus

The higher order system $\lambda \Pi \omega$ extends $\lambda \Pi 2$ to all four forms of abstraction from the lambda cube: functions from terms to terms, types to types, terms to types and types to terms. The system corresponds to the calculus of constructions whose derivative, the calculus of inductive constructions is the underlying system of Rocq.

## Simultaneous programming language and logic

The Curry–Howard correspondence implies that types can be constructed that express arbitrarily complex mathematical properties. If the user can supply a constructive proof that a type is *inhabited* (i.e., that a value of that type exists) then a compiler can check the proof and convert it into executable computer code that computes the value by carrying out the construction. The proof checking feature makes dependently typed languages closely related to proof assistants. The code-generation aspect provides a powerful approach to formal program verification and proof-carrying code, since the code is derived directly from a mechanically verified mathematical proof.

## Comparison of languages with dependent types

Language

Actively developed

Paradigm

Tactics

Proof terms

Termination checking

Types can depend on

Universes

Proof irrelevance

Program extraction

Extraction erases irrelevant terms

Agda

Yes

Purely functional

Few/limited

Yes

Yes (optional)

Any term

Yes (optional)

Proof-irrelevant arguments

Proof-irrelevant propositions

Haskell

,

JavaScript

Yes

ATS

Yes

Functional / imperative

No

Yes

Yes

Static terms

?

Yes

Yes

Yes

Cayenne

No

Purely functional

No

Yes

No

Any term

No

No

?

?

Gallina

(

Rocq

(previously known as

Coq

))

Yes

Purely functional

Yes

Yes

Yes

Any term

Yes

Yes

Haskell

,

Scheme

,

OCaml

Yes

Dependent ML

No

?

?

Yes

?

Natural numbers

?

?

?

?

F*

Yes

Functional and imperative

Yes

Yes

Yes (optional)

Any pure term

Yes

Yes

OCaml

,

F#

, and

C

Yes

Guru

No

Purely functional

hypjoin

Yes

Yes

Any term

No

Yes

Carraway

Yes

Idris

Yes

Purely functional

Yes

Yes

Yes (optional)

Any term

Yes

No

Yes

Yes

Lean

Yes

Purely functional

Yes

Yes

Yes

Any term

Yes

Yes

Yes

Yes

Matita

Yes

Purely functional

Yes

Yes

Yes

Any term

Yes

Yes

OCaml

Yes

NuPRL

Yes

Purely functional

Yes

Yes

Yes

Any term

Yes

?

Yes

?

PVS

Yes

?

Yes

?

?

?

?

?

?

?

Sage

Archived

2020-11-09 at the

Wayback Machine

No

Purely functional

No

No

No

?

No

?

?

?

Twelf

Yes

Logic programming

?

Yes

Yes (optional)

Any (LF) term

No

No

?

?

1. This refers to the *core* language, not to any tactic (theorem proving procedure) or code generation sublanguage.
2. Subject to semantic constraints, such as universe constraints
3. Ring solver
4. Optional universes, optional universe polymorphism, and optional explicitly specified universes
5. Universes, automatically inferred universe constraints (not the same as Agda's universe polymorphism) and optional explicit printing of universe constraints
6. Has been superseded by ATS
7. Last Sage paper and last code snapshot are both dated 2006
