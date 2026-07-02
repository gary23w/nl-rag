---
title: "Value restriction"
source: https://en.wikipedia.org/wiki/Value_restriction
domain: hindley-milner-deep
license: CC-BY-SA-4.0
tags: Hindley-Milner type system, let-polymorphism, type scheme, damas-milner algorithm
fetched: 2026-07-02
---

# Value restriction

In programming languages with Hindley–Milner type inference and imperative features, in particular the ML programming language family, the **value restriction** means that declarations are only polymorphically generalized if they are syntactic values (also called *non-expansive*). The value restriction prevents reference cells from holding values of different types and preserves type safety.

## A counter example to type safety

In the Hindley–Milner type system, expressions can be given multiple types through parametric polymorphism. But naively giving multiple types to references breaks type safety. The following are typing rules for references and related operators in ML-like languages.

${\begin{aligned}{\mathtt {ref}}&:\forall \alpha .\alpha \to (\alpha \ {\mathtt {ref}})\\{\mathtt {!}}&:\forall \alpha .(\alpha \ {\mathtt {ref}})\to \alpha \\{\mathtt {:=}}&:\forall \alpha .(\alpha \ {\mathtt {ref}})\to \alpha \to {\mathtt {unit}}\end{aligned}}$

The operators have the following semantics: ${\textstyle {\mathtt {ref}}}$ takes a value and creates a reference containing that value, ${\textstyle {\mathtt {!}}}$ (dereference) takes a reference and reads the value in that reference, and ${\textstyle {\mathtt {:=}}}$ (assignment) updates a reference to contain a new value and returns a value of the unit type. Given these, the following program unsoundly applies a function meant for integers to a Boolean value.

```mw
let val c = ref (fn x => x)
in  c := (fn x => x + 1);
     !c true
end
```

The above program type checks using Hindley-Milner because `c` is given the type ${\textstyle \forall \alpha .(\alpha \to \alpha )\ {\mathtt {ref}}}$ , which is then instantiated to be of the type ${\textstyle ({\mathtt {int}}\to {\mathtt {int}})\ {\mathtt {ref}}}$ when typing the assignment `c := (fn x => x + 1)`, and ${\textstyle ({\mathtt {bool}}\to {\mathtt {bool}})\ {\mathtt {ref}}}$ ref when typing the dereference `!c true`.

## The value restriction

Under the value restriction, the types of let bound expressions are only generalized if the expressions are *syntactic values*. In his paper, Wright considers the following to be syntactic values: constants, variables, ${\textstyle \lambda }$ -expressions and constructors applied to values. The function and operator applications are not considered values. In particular, applications of the ${\mathtt {ref}}$ operator are not generalized. It is safe to generalize type variables of syntactic values because their evaluation cannot cause any side-effects such as writing to a reference.

The above example is rejected by the type checker under the value restriction as follows.

- First `c` is given the type ${\textstyle (\alpha \to \alpha )\ {\mathtt {ref}}}$ . This type is not generalized and ${\textstyle \alpha }$ is a free variable in the typing context for the body of the let binding.
- When the assignment is typed, the type of `c` is modified in the typing context to be of type ${\textstyle ({\mathtt {int}}\to {\mathtt {int}})\ {\mathtt {ref}}}$ via unification.
- The dereference `!c` is typed as ${\mathtt {int}}\to {\mathtt {int}}$ , but is applied to a value of type ${\textstyle {\mathtt {bool}}}$ , and the type checker rejects the program.
