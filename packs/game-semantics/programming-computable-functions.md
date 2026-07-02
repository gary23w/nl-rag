---
title: "Programming Computable Functions"
source: https://en.wikipedia.org/wiki/Programming_Computable_Functions
domain: game-semantics
license: CC-BY-SA-4.0
tags: game semantics, dialogical logic, full abstraction, strategy (game theory)
fetched: 2026-07-02
---

# Programming Computable Functions

In computer science, **Programming Computable Functions** (**PCF**), or **Programming with Computable Functions**, or **Programming language for Computable Functions**, is a programming language which is typed and based on functional programming, introduced by Gordon Plotkin in 1977, based on prior unpublished material by Dana Scott. It can be considered as an extended version of the typed lambda calculus, or a simplified version of modern typed functional languages such as ML or Haskell.

A fully abstract model for PCF was first given by Robin Milner. However, since Milner's model was essentially based on the syntax of PCF it was considered less than satisfactory. The first two fully abstract models not employing syntax were formulated during the 1990s. These models are based on game semantics and Kripke logical relations. For a time it was felt that neither of these models was completely satisfactory, since they were not effectively presentable. However, Ralph Loader demonstrated that no effectively presentable fully abstract model could exist, since the question of program equivalence in the finitary fragment of PCF is not decidable.

## Syntax

The *data types* of PCF are inductively defined as

- **nat** is a type
- For types *σ* and *τ*, there is a function type *σ* → *τ*

A *context* is a list of pairs *x : σ*, where *x* is a variable name and *σ* is a type, such that no variable name is duplicated. One then defines typing judgments of terms-in-context in the usual way for the following syntactical constructs:

- Variables (if *x : σ* is part of a context *Γ*, then *Γ* ⊢ *x* : *σ*)
- Application (of a term of type *σ* → *τ* to a term of type *σ*)
- λ-abstraction
- The **Y** fixed point combinator (making terms of type *σ* out of terms of type *σ* → *σ*)
- The successor (**succ**) and predecessor (**pred**) operations on **nat** and the constant **0**
- The conditional **if** with the typing rule:

${\frac {\Gamma \;\vdash \;t\;:{\textbf {nat}},\quad \quad \Gamma \;\vdash \;s_{0}\;:\sigma ,\quad \quad \Gamma \;\vdash \;s_{1}\;:\sigma }{\Gamma \;\vdash \;{\textbf {if}}(t,s_{0},s_{1})\;:\sigma }}$

(

nat

s will be interpreted as booleans here with a convention like zero denoting truth, and any other number denoting falsity)

## Semantics

### Denotational semantics

A relatively straightforward semantics for the language is the **Scott model**. In this model,

- Types are interpreted as certain domains.
  - $[\![{\textbf {nat}}]\!]:=\mathbb {N} _{\bot }$ (the natural numbers with a bottom element adjoined, with the flat ordering)
  - $[\![\sigma \to \tau \,]\!]$ is interpreted as the domain of Scott-continuous functions from $[\![\sigma ]\!]\,$ to $[\![\tau ]\!]\,$ , with the pointwise ordering.
- A context $x_{1}:\sigma _{1},\;\dots ,\;x_{n}:\sigma _{n}$ is interpreted as the product $[\![\sigma _{1}]\!]\times \;\dots \;\times [\![\sigma _{n}]\!]$
- Terms in context $\Gamma \;\vdash \;x\;:\;\sigma$ are interpreted as continuous functions $[\![\Gamma ]\!]\;\to \;[\![\sigma ]\!]$
  - Variable terms are interpreted as projections
  - Lambda abstraction and application are interpreted by making use of the cartesian closed structure of the category of domains and continuous functions
  - **Y** is interpreted by taking the least fixed point of the argument

This model is not fully abstract for PCF; but it is fully abstract for the language obtained by adding a *parallel or* operator to PCF.
