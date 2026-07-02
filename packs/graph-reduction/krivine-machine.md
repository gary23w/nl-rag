---
title: "Krivine machine"
source: https://en.wikipedia.org/wiki/Krivine_machine
domain: graph-reduction
license: CC-BY-SA-4.0
tags: graph reduction, combinator graph reduction, spineless tagless G-machine, supercombinator compilation
fetched: 2026-07-02
---

# Krivine machine

In theoretical computer science, the **Krivine machine** is an *abstract machine*. As an abstract machine, it shares features with Turing machines and the SECD machine. The Krivine machine explains how to compute a recursive function. More specifically it aims to define rigorously head normal form reduction of a lambda term using call-by-name reduction. Thanks to its formalism, it tells in details how a kind of reduction works and sets the theoretical foundation of the operational semantics of functional programming languages. On the other hand, Krivine machine implements call-by-name because it evaluates the body of a β-redex before it applies the body to its parameter. In other words, in an expression (*λ* *x*. *t*) *u* it evaluates first *λ* *x*. *t* before applying it to *u*. In functional programming, this would mean that in order to evaluate a function applied to a parameter, it evaluates first the function before applying it to the parameter.

The Krivine machine was designed by the French logician Jean-Louis Krivine at the beginning of the 1980s.

## Call by name and head normal form reduction

The Krivine machine is based on two concepts related to lambda calculus, namely head reduction and call by name.

### Head normal form reduction

A redex (one says also β-redex) is a term of the lambda calculus of the form (*λ* *x*. *t*) *u*. If a term has the shape (*λ* *x*. *t*) *u*1 ... *u**n* it is said to be a *head redex*. A *head normal form* is a term of the lambda calculus which is not a head redex. A *head reduction* is a (non empty) sequence of contractions of a term which contracts head redexes. A head reduction of a term *t* (which is supposed not to be in head normal form) is a head reduction which starts from a term *t* and ends on a head normal form. From an abstract point of view, head reduction is the way a program computes when it evaluates a recursive sub-program. To understand how such a reduction can be implemented is important. One of the aims of the Krivine machine is to propose a process to reduct a term in head normal form and to describe formally this process. Like Turing used an abstract machine to describe formally the notion of algorithm, Krivine used an abstract machine to describe formally the notion of head normal form reduction.

#### An example

The term ((*λ* 0) (*λ* 0)) (*λ* 0) (which corresponds, if one uses explicit variables, to the term (*λx*.*x*) (*λy*.*y*) (*λz*.*z*)) is not in head normal form because (*λ* 0) (*λ* 0) contracts in (*λ* 0) yielding the head redex (*λ* 0) (*λ* 0) which contracts in (*λ* 0) and which is therefore the head normal form of ((*λ* 0) (*λ* 0)) (*λ* 0). Said otherwise the head normal form contraction is:

((

λ

0) (

λ

0)) (

λ

0) ➝ (

λ

0) (

λ

0) ➝

λ

0,

which corresponds to :

(

λx

.

x

) (

λy

.

y

) (

λz

.

z

) ➝ (

λy

.

y

) (

λz

.

z

) ➝

λz

.

z

.

We will see further how the Krivine machine reduces the term ((*λ* 0) (*λ* 0)) (*λ* 0).

### Call by name

To implement the head reduction of a term *u v* which is an application, but which is not a redex, one must reduce the body *u* to exhibit an abstraction and therefore create a redex with *v*. When a redex appears, one reduces it. To reduce always the body of an application first is called *call by name*. The Krivine machine implements *call by name*.

## Description

The presentation of the Krivine machine given here is based on notations of lambda terms that use de Bruijn indices and assumes that the terms of which it computes the head normal forms are closed. It modifies the current **state** until it cannot do it anymore, in which case it obtains a head normal form. This head normal form represents the result of the computation or yields an error, meaning that the term it started from is not correct. However, it can enter an infinite sequence of transitions, which means that the term it attempts reducing has no head normal form and corresponds to a non terminating computation.

It has been proved that the Krivine machine implements correctly the call by name head normal form reduction in the lambda-calculus. Moreover, the Krivine machine is deterministic, since each pattern of the state corresponds to at most one machine transition.

### The state

The state has three components

1. a **term**,
2. a **stack**,
3. an **environment**.

The term is a λ-term with de Bruijn indices. The stack and the environment belong to the same recursive data structure. More precisely, the environment and the stack are lists of pairs *<term, environment>*, that are called *closures*. In what follows, the insertion as the head of a list ℓ (stack or environment) of an element *a* is written *a:ℓ*, whereas the empty list is written □. The stack is the location where the machine stores the closures that must be evaluated furthermore, whereas the environment is the association between the indices and the closures at a given time during the evaluation. The first element of the environment is the closure associated with the index *0*, the second element corresponds to the closure associated with index *1* etc. If the machine has to evaluate an index, it fetches there the pair *<term, environment>* the closure that yields the term to be evaluated and the environment in which this term must be evaluated. This intuitive explanations allow understanding the operating rules of the machine. If one writes *t* for term, p for stack, and e for environment, the states associated with these three entities will be written *t*, p, e. The rules explain how the machine transforms a state into another state, after identifying the patterns among the states.

The *initial state* aims to evaluate a term *t*, it is the state *t*,□,□, in which the term is *t* and the stack and the environment are empty. The *final state* (in absence of error) is of the form *λ t*, □, e, in other words, the resulting terms is an abstraction together with its environment and an empty stack.

### The transitions

The Krivine machine has four transitions : ***App***, ***Abs***, ***Zero***, ***Succ***.

| Name | Before | After |
|---|---|---|
| ***App*** | *t u*, p, e | *t*, <*u*,e>:p, e |
| ***Abs*** | *λ t*, <*u*,e'>:p, e | *t*, p, <*u*,e'>:e |
| ***Zero*** | *0*, p, <*t*, e'>:e | *t*, p, e' |
| ***Succ*** | *n+1*, p, <*t*,e'>:e | n, p, e |

The transition ***App*** removes the parameter of an application and put it on the stack for further evaluation. The transition ***Abs*** removes the λ of the term and pop up the closure from the top of the stack and put it on the top of the environment. This closure corresponds to the de Bruijn index *0* in the new environment. The transition ***Zero*** takes the first closure of the environment. The term of this closure becomes the current term and the environment of this closure becomes the current environment. The transition ***Succ*** removes the first closure of the environment list and decreases the value of the index.

### Two examples

Let us evaluate the term (*λ* 0 0) (*λ* 0) which corresponds to the term (*λ* *x*. *x* *x*) (*λ* *x*. *x*). Let us start with the state (*λ* 0 0) (*λ* 0), □, □.

| **Term** | **Stack** | **Environment** | **Transition** |
|---|---|---|---|
| (*λ* 0 0) (*λ* 0) | □ | □ | *App* |
| *λ* 0 0 | <*λ* 0,□>:□ | □ | *Abs* |
| 0 0 | □ | <*λ* 0, □>:□ | *App* |
| 0 | <0,<*λ* 0,□>:□>:□ | <*λ* 0,□>:□ | *Zero* |
| *λ* 0 | <0,<*λ* 0,□>:□>:□ | □ | *Abs* |
| 0 | □ | <0,<*λ* 0,□>:□>:□ | *Zero* |
| 0 | □ | <*λ* 0, □>:□ | *Zero* |
| *λ* 0 | □ | □ | *Stop* |

The conclusion is that the head normal form of the term (*λ* 0 0) (*λ* 0) is *λ* 0 Putting variables back in: the head normal form of the term (*λ* *x*. *x* *x*) (*λ* *x*. *x*) is *λ* *x*. *x*

Let us evaluate the term ((*λ* 0) (*λ* 0)) (*λ* 0) as shown below:

| **Term** | **Stack** | **Environment** | **Transition** |
|---|---|---|---|
| ((*λ* 0) (*λ* 0)) (*λ* 0) | □ | □ | *App* |
| (*λ* 0) (*λ* 0) | <(*λ* 0),□>:□ | □ | *App* |
| *λ* 0, | <(*λ* 0),□>:<(*λ* 0),□>:□ | □ | *Abs* |
| 0 | <(*λ* 0),□>:□ | <(*λ* 0),□>:□ | *Zero* |
| *λ* 0 | <(*λ* 0),□>:□ | □ | *Abs* |
| 0 | □ | <(*λ* 0),□>:□ | *Zero* |
| (*λ* 0) | □ | □ | *Stop* |

This confirms the above fact that the normal form of the term ((*λ* 0) (*λ* 0)) (*λ* 0) is (*λ* 0) Or with variables: ((*λ* *x*. *x*) (*λ* *x*. *x*)) (*λ* *x*. *x*) is (*λ* *x*. *x*)

## Inter-derivations

The Krivine machine, like the CEK machine, not only corresponds functionally to a meta-circular evaluator, it also corresponds syntactically to the $\lambda {\widehat {\rho }}$ calculus -- a version of Pierre-Louis Curien's $\lambda {\widehat {\rho }}$ calculus of explicit substitutions that is closed under reduction -- with a normal-order reduction strategy.

If the $\lambda {\widehat {\rho }}$ calculus includes generalized $\beta$ reduction (i.e., the nested $\beta$ redex $(\lambda x_{1}.\lambda x_{2}.e_{0})\;e_{1}\;e_{2}$ is contracted in one step instead of two), then the syntactically corresponding machine coincides with Jean-Louis Krivine's original machine. (Also, if the reduction strategy is right-to-left call by value and includes generalized $\beta$ reduction, then the syntactically corresponding machine is Xavier Leroy's ZINC abstract machine, which underlies OCaml.)
