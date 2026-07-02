---
title: "Inductive type"
source: https://en.wikipedia.org/wiki/Inductive_type
domain: dependent-types-pl
license: CC-BY-SA-4.0
tags: dependent type, pi type, dependent product, type family
fetched: 2026-07-02
---

# Inductive type

In type theory, a system has **inductive types** if it has facilities for creating a new type from constants and functions that create terms of that type. The feature serves a role similar to data structures in a programming language and allows a type theory to add concepts like numbers, relations, and trees. As the name suggests, inductive types can be self-referential, but usually only in a way that permits structural recursion.

The standard example is encoding the natural numbers using Peano's encoding. It can be defined in Rocq (formerly named *Coq*) as follows:

```mw
Inductive nat : Type :=
  | O : nat
  | S : nat -> nat.
```

Here, a natural number is created either from the constant "O" (representing zero) or by applying the function "S" to another natural number. "S" is the successor function which represents adding one to a number. Thus, "S O" is one, "S (S O)" is two, "S (S (S O))" is three, and so on.

Since their introduction, inductive types have been extended to encode more and more structures, while still being predicative and supporting structural recursion.

## Induction principle

Inductive types usually come with a function to prove properties about them. Thus, "nat" may come with (in Rocq syntax):

```mw
nat_ind : (forall P : nat -> Prop, (P O) -> (forall n, P n -> P (S n)) -> (forall n, P n)).
```

In words: for any predicate "P" over natural numbers, given a proof of "P O" and a proof of "P n -> P (n+1)", we get back a proof of "forall n, P n". This is the familiar induction principle for natural numbers.

## Implementations

### W- and M-types

W-types are well-founded types in intuitionistic type theory (ITT). They generalize natural numbers, lists, binary trees, and other "tree-shaped" data types. Let *U* be a universe of types. Given a type *A* : *U* and a dependent family *B* : *A* → *U*, one can form a W-type ${\mathsf {W}}_{a:A}B(a)$ . The type *A* may be thought of as "labels" for the (potentially infinitely many) constructors of the inductive type being defined, whereas *B* indicates the (potentially infinite) arity of each constructor. W-types (resp. M-types) may also be understood as well-founded (resp. non-well-founded) trees with nodes labeled by elements *a* : *A* and where the node labeled by *a* has *B*(*a*)-many subtrees. Each W-type is isomorphic to the initial algebra of a so-called polynomial functor.

Let **0**, **1**, **2**, etc. be finite types with inhabitants 1**1** : **1**, 1**2**, 2**2**:**2**, etc. One may define the natural numbers as the W-type $\mathbb {N$ with *f* : **2** → *U* is defined by *f*(1**2**) = **0** (representing the constructor for zero, which takes no arguments), and *f*(2**2**) = **1** (representing the successor function, which takes one argument).

One may define lists over a type *A* : *U* as $\operatorname {List} (A):={\mathsf {W}}_{(x:\mathbf {1} +A)}f(x)$ where ${\begin{aligned}f(\operatorname {inl} (1_{\mathbf {1} }))&=\mathbf {0} \\f(\operatorname {inr} (a))&=\mathbf {1} \end{aligned}}$ and 1**1** is the sole inhabitant of **1**. The value of $f(\operatorname {inl} (1_{\mathbf {1} }))$ corresponds to the constructor for the empty list, whereas the value of $f(\operatorname {inr} (a))$ corresponds to the constructor that appends *a* to the beginning of another list.

The constructor for elements of a generic W-type ${\mathsf {W}}_{x:A}B(x)$ has type ${\mathsf {sup}}:\prod _{a:A}{\Big (}B(a)\to {\mathsf {W}}_{x:A}B(x){\Big )}\to {\mathsf {W}}_{x:A}B(x).$ We can also write this rule in the style of a natural deduction proof, ${\frac {a:A\qquad f:B(a)\to {\mathsf {W}}_{x:A}B(x)}{{\mathsf {sup}}(a,f):{\mathsf {W}}_{x:A}B(x)}}.$

The elimination rule for W-types works similarly to structural induction on trees. If, whenever a property (under the propositions-as-types interpretation) $C:{\mathsf {W}}_{x:A}B(x)\to U$ holds for all subtrees of a given tree it also holds for that tree, then it holds for all trees.

${\frac {w:{\mathsf {W}}_{a:A}B(a)\qquad a:A,\;f:B(a)\to {\mathsf {W}}_{x:A}B(x),\;c:\prod _{b:B(a)}C(f(b))\;\vdash \;h(a,f,c):C({\mathsf {sup}}(a,f))}{{\mathsf {elim}}(w,h):C(w)}}$

In extensional type theories, W-types (resp. M-types) can be defined up to isomorphism as initial algebras (resp. final coalgebras) for polynomial functors. In this case, the property of initiality (res. finality) corresponds directly to the appropriate induction principle. In intensional type theories with the univalence axiom, this correspondence holds up to homotopy (propositional equality).

M-types are dual to W-types, and represent coinductive (potentially infinite) data such as streams. M-types can be derived from W-types.

### Mutually inductive definitions

This technique allows *some* definitions of multiple types that depend on each other. For example, defining two parity predicates on natural numbers using two mutually inductive types in Rocq:

```mw
Inductive even : nat -> Prop :=
  | zero_is_even : even O
  | S_of_odd_is_even : (forall n:nat, odd n -> even (S n))
with odd : nat -> Prop :=
  | S_of_even_is_odd : (forall n:nat, even n -> odd (S n)).
```

### Induction-recursion

Induction-recursion started as a study into the limits of ITT. Once found, the limits were turned into rules that allowed defining new inductive types. These types could depend upon a function and the function on the type, as long as both were defined simultaneously.

Universe types can be defined using induction-recursion.

### Induction-induction

Induction-induction allows definition of a type and a family of types at the same time. So, a type A and a family of types $B:A\to Type$ .

### Higher inductive types

This is a current research area in Homotopy type theory (HoTT). This differs from ITT by its identity type (equality). Higher inductive types define a new type with constants and functions that create elements of the type, and new instances of the identity type that relate them.

A simple example is the circle type, which is defined with two constructors, a basepoint;

base

:

circle

and a loop;

loop

:

base

=

base

.

The existence of a new constructor for the identity type makes circle a higher inductive type.
