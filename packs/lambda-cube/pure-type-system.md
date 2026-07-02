---
title: "Pure type system"
source: https://en.wikipedia.org/wiki/Pure_type_system
domain: lambda-cube
license: CC-BY-SA-4.0
tags: lambda cube, pure type system, calculus of constructions, higher-order logic
fetched: 2026-07-02
---

# Pure type system

Unsolved problem in computer science

Is every weakly normalizing pure type system also strongly normalizing?

More unsolved problems in computer science

In the branches of mathematical logic known as proof theory and type theory, a **pure type system** (**PTS**), previously known as a **generalized type system** (**GTS**), is a form of typed lambda calculus that allows an arbitrary number of sorts and dependencies between any of these. The framework can be seen as a generalisation of Barendregt's lambda cube, in the sense that all corners of the cube can be represented as instances of a PTS with just two sorts. In fact, Barendregt (1991) framed his cube in this setting. Pure type systems may obscure the distinction between *types* and *terms* and collapse the type hierarchy, as is the case with the calculus of constructions, but this is not generally the case, e.g. the simply typed lambda calculus allows only terms to depend on terms.

Pure type systems were independently introduced by Stefano Berardi (1988) and Jan Terlouw (1989). Barendregt discussed them at length in his subsequent papers. In his PhD thesis, Berardi defined a cube of constructive logics akin to the lambda cube (these specifications are non-dependent). A modification of this cube was later called the L-cube by Herman Geuvers, who in his PhD thesis extended the Curry–Howard correspondence to this setting. Based on these ideas, G. Barthe and others defined *classical pure type systems* (CPTS) by adding a double negation operator. Similarly, in 1998, Tijn Borghuis introduced *modal pure type systems* (MPTS). Roorda has discussed the application of pure type systems to functional programming; and Roorda and Jeuring have proposed a programming language based on pure type systems.

The systems from the lambda cube are all known to be strongly normalizing. Pure type systems in general need not be, for example System U from **Girard's paradox** is not. (Roughly speaking, Girard found pure systems in which one can express the sentence "the types form a type".) Furthermore, all known examples of pure type systems that are not strongly normalizing are not even (weakly) normalizing: they contain expressions that do not have normal forms, just like the untyped lambda calculus. It is a major open problem in the field whether this is always the case, i.e. whether a (weakly) normalizing PTS always has the strong normalization property. This is known as the Barendregt–Geuvers–Klop conjecture (named after Henk Barendregt, Herman Geuvers, and Jan Willem Klop).

## Definition

A pure type system is defined by a triple ${\textstyle ({\mathcal {S}},{\mathcal {A}},{\mathcal {R}})}$ where ${\textstyle {\mathcal {S}}}$ is the set of sorts, ${\textstyle {\mathcal {A}}\subseteq {\mathcal {S}}^{2}}$ is the set of axioms, and ${\textstyle {\mathcal {R}}\subseteq {\mathcal {S}}^{3}}$ is the set of rules. Typing in pure type systems is determined by the following rules, where ${\textstyle s}$ is any sort:

${\frac {(s_{1},s_{2})\in {\mathcal {A}}}{\vdash s_{1}:s_{2}}}\quad {\text{(axiom)}}$

${\frac {\Gamma \vdash A:s\quad x\notin {\text{dom}}(\Gamma )}{\Gamma ,x:A\vdash x:A}}\quad {\text{(start)}}$

${\frac {\Gamma \vdash A:B\quad \Gamma \vdash C:s\quad x\notin {\text{dom}}(\Gamma )}{\Gamma ,x:C\vdash A:B}}\quad {\text{(weakening)}}$

${\frac {\Gamma \vdash A:s_{1}\quad \Gamma ,x:A\vdash B:s_{2}\quad (s_{1},s_{2},s_{3})\in {\mathcal {R}}}{\Gamma \vdash \Pi x:A.B:s_{3}}}\quad {\text{(product)}}$

${\frac {\Gamma \vdash C:\Pi x:A.B\quad \Gamma \vdash a:A}{\Gamma \vdash Ca:B[x:=a]}}\quad {\text{(application)}}$

${\frac {\Gamma ,x:A\vdash b:B\quad \Gamma \vdash \Pi x:A.B:s}{\Gamma \vdash \lambda x:A.b:\Pi x:A.B}}\quad {\text{(abstraction)}}$

${\frac {\Gamma \vdash A:B\quad B=_{\beta }B'\quad \Gamma \vdash B':s}{\Gamma \vdash A:B'}}\quad {\text{(conversion)}}$

## Implementations

The following programming languages have pure type systems:

- SAGE
- Yarrow
- Henk 2000
- Haskell since GHC version 8.
