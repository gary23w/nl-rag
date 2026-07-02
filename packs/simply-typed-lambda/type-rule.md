---
title: "Typing rule"
source: https://en.wikipedia.org/wiki/Type_rule
domain: simply-typed-lambda
license: CC-BY-SA-4.0
tags: simply typed lambda calculus, typing rule, type judgment, strong normalization
fetched: 2026-07-02
---

# Typing rule

(Redirected from

Type rule

)

In type theory, a **typing rule** is an inference rule that describes how a type system assigns a type to a syntactic construction. These rules may be applied by the type system to determine if a program is well-typed and what type expressions have. A prototypical example of the use of typing rules is in defining type inference in the simply typed lambda calculus, which is the internal language of Cartesian closed categories.

## Notation

Typing rules specify the structure of a *typing relation* that relates syntactic terms to their types. Syntactically, the typing relation is usually denoted by a colon, so for example $e:\tau$ denotes that an expression e has type $\tau$ . The rules themselves are usually specified using the notation of natural deduction. For example, the following typing rules specify the typing relation for a simple language of booleans:

${\frac {}{{\mathsf {true}}:{\mathsf {Bool}}}}\qquad {\frac {}{{\mathsf {false}}:{\mathsf {Bool}}}}\qquad {\frac {e_{1}:{\mathsf {Bool}}\quad \;e_{2}:\tau \quad \;e_{3}:\tau }{\mathbf {if} \ e_{1}\ \mathbf {then} \ e_{2}\ \mathbf {else} \ e_{3}:\tau }}$

Each rule states that the conclusion below the line may be derived from the premises above the line. The first two rules have no premises above the line, so they are axioms. The third rule has premises above the line (specifically, three premises), so it is an inference rule.

In programming languages, the type of a variable depends on where it is bound, which necessitates context-sensitive typing rules. These rules are given by a *typing judgment*, usually written $\Gamma \vdash e:\tau$ , which states that an expression e has type $\tau$ under a typing context $\Gamma$ that relates variables to their types. Typing contexts are occasionally supplemented by the types of individual variables; for example, $\Gamma ,x{:}\tau _{1}\vdash e:\tau _{2}$ can be read as "the context $\Gamma$ supplemented by the information that the expression x has type $\tau _{1}$ yields the judgement that expression e has type $\tau _{2}$ ". This notation can be used to give typing rules for variable references and lambda abstraction in the simply typed lambda calculus:

${\frac {x{:}\tau \in \Gamma }{\Gamma \vdash x:\tau }}\qquad {\frac {\Gamma ,x{:}\tau _{1}\vdash e:\tau _{2}}{\Gamma \vdash (\lambda x{:}\tau _{1}.\,e):\tau _{1}\rightarrow \tau _{2}}}$

Similarly, the following typing rule describes the $\mathbf {let}$ construct of Standard ML:

${\frac {\Gamma \vdash e_{1}:\tau _{1}\qquad \Gamma ,x{:}\tau _{1}\vdash e_{2}:\tau _{2}}{\Gamma \vdash \mathbf {let} \ x=e_{1}\ \mathbf {in} \ e_{2}\ \mathbf {end$

Not all systems of typing rules directly specify a type checking algorithm. For example, the typing rule for applying a parametrically polymorphic function in the Hindley–Milner type system requires "guessing" the appropriate type at which the function should be instantiated. Adapting a declarative rule system to a decidable algorithm requires the production of a separate, algorithmic system that can be proven to specify the same typing relation.
