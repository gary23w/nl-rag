---
title: "Type theory (part 2/2)"
source: https://en.wikipedia.org/wiki/Type_theory
domain: lambda-type-theory
license: CC-BY-SA-4.0
tags: lambda calculus, type theory, type system, type inference, hindley-milner, dependent type
fetched: 2026-07-02
part: 2/2
---

## Differences from set theory

The most commonly accepted foundation for mathematics is first-order logic with the language and axioms of Zermelo–Fraenkel set theory with the axiom of choice, abbreviated ZFC. Type theories having sufficient expressibility may also act as a foundation of mathematics. There are a number of differences between these two approaches.

- Set theory has both rules and axioms, while type theories only have rules. Type theories, in general, do not have axioms and are defined by their rules of inference.
- Classical set theory and logic have the law of excluded middle. When a type theory encodes the concepts of "and" and "or" as types, it leads to intuitionistic logic, and does not necessarily have the law of excluded middle.
- In set theory, an element is not restricted to one set. The element can appear in subsets and unions with other sets. In type theory, terms (generally) belong to only one type. Where a subset would be used, type theory can use a predicate function or use a dependently-typed product type, where each element x {\displaystyle x} ({\displaystyle x}) is paired with a proof that the subset's property holds for ⁠ x {\displaystyle x} ({\displaystyle x})⁠. Where a union would be used, type theory uses the sum type, which contains new canonical terms.
- Type theory has a built-in notion of computation. Thus, "1+1" and "2" are different terms in type theory, but they compute to the same value. Moreover, functions are defined computationally as lambda terms. In set theory, "1+1=2" means that "1+1" is just another way to refer the value "2". Type theory's computation does require a complicated concept of equality.
- Set theory encodes numbers as sets. Type theory can encode numbers as functions using Church encoding, or more naturally as inductive types, and the construction closely resembles Peano's axioms.
- In type theory, proofs have types whereas in set theory, proofs are part of the underlying first-order logic.

Proponents of type theory will also point out its connection to constructive mathematics through the BHK interpretation, its connection to logic by the Curry–Howard isomorphism, and its connections to category theory.

### Properties of type theories

Terms usually belong to a single type. However, there are type theories that define "subtyping".

Computation takes place by repeated application of rules. Many types of theories are strongly normalizing, which means that any order of applying the rules will always end in the same result. However, some are not. In a normalizing type theory, the one-directional computation rules are called "reduction rules", and applying the rules "reduces" the term. If a rule is not one-directional, it is called a "conversion rule".

Some combinations of types are equivalent to other combinations of types. When functions are considered "exponentiation", the combinations of types can be written similarly to algebraic identities. Thus, ⁠ 0 + A ≅ A {\displaystyle {\mathbb {0} }+A\cong A} ({\displaystyle {\mathbb {0} }+A\cong A})⁠, ⁠ 1 × A ≅ A {\displaystyle {\mathbb {1} }\times A\cong A} ({\displaystyle {\mathbb {1} }\times A\cong A})⁠, ⁠ 1 + 1 ≅ 2 {\displaystyle {\mathbb {1} }+{\mathbb {1} }\cong {\mathbb {2} }} ({\displaystyle {\mathbb {1} }+{\mathbb {1} }\cong {\mathbb {2} }})⁠, ⁠ A B + C ≅ A B × A C {\displaystyle A^{B+C}\cong A^{B}\times A^{C}} ({\displaystyle A^{B+C}\cong A^{B}\times A^{C}})⁠, ⁠ A B × C ≅ ( A B ) C {\displaystyle A^{B\times C}\cong (A^{B})^{C}} ({\displaystyle A^{B\times C}\cong (A^{B})^{C}})⁠.

### Axioms

Most type theories do not have axioms. This is because a type theory is defined by its rules of inference. This is a source of confusion for people familiar with Set Theory, where a theory is defined by both the rules of inference for a logic (such as first-order logic) and axioms about sets.

Sometimes, a type theory will add a few axioms. An axiom is a judgment that is accepted without a derivation using the rules of inference. They are often added to ensure properties that cannot be added cleanly through the rules.

Axioms can cause problems if they introduce terms without a way to compute on those terms. That is, axioms can interfere with the normalizing property of the type theory.

Some commonly encountered axioms are:

- "Axiom K" ensures "uniqueness of identity proofs". That is, that every term of an identity type is equal to reflexivity.
- "Univalence axiom" holds that equivalence of types is equality of types. The research into this property led to cubical type theory, where the property holds without needing an axiom.
- "Law of excluded middle" is often added to satisfy users who want classical logic, instead of intuitionistic logic.

The axiom of choice does not need to be added to type theory, because in most type theories it can be derived from the rules of inference. This is because of the constructive nature of type theory, where proving that a value exists requires a method to compute the value. The axiom of choice is less powerful in type theory than most set theories, because type theory's functions must be computable and, being syntax-driven, the number of terms in a type must be countable. (See *Axiom of choice § In constructive mathematics*.)


## List of type theories

### Major

- Simply typed lambda calculus which is a higher-order logic
- Intuitionistic type theory
- System F
- LF is often used to define other type theories
- Calculus of constructions and its derivatives

### Minor

- Automath
- ST type theory
- UTT (Luo's unified theory of dependent types)
- some forms of combinatory logic
- others defined in the lambda cube (also known as pure type systems)
- others under the name typed lambda calculus

### Active research

- Homotopy type theory explores equality of types
- Cubical type theory is an implementation of homotopy type theory
