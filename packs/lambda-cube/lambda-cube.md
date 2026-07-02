---
title: "Lambda cube"
source: https://en.wikipedia.org/wiki/Lambda_cube
domain: lambda-cube
license: CC-BY-SA-4.0
tags: lambda cube, pure type system, calculus of constructions, higher-order logic
fetched: 2026-07-02
---

# Lambda cube

In mathematical logic and type theory, the **λ-cube** (also written **lambda cube**) is a framework introduced by Henk Barendregt to investigate the different dimensions in which the calculus of constructions is a generalization of the simply typed λ-calculus. Each dimension of the cube corresponds to a new kind of dependency between terms and types. Here, "dependency" refers to the capacity of a term or type to bind a term or type. The respective dimensions of the λ-cube correspond to:

- x-axis ( $\rightarrow$ ): types that can depend on terms, corresponding to dependent types.
- y-axis ( $\uparrow$ ): terms that can depend on types, corresponding to polymorphism.
- z-axis ( $\nearrow$ ): types that can depend on other types, corresponding to (binding) type operators.

The different ways to combine these three dimensions yield the 8 vertices of the cube, each corresponding to a different kind of typed system. The λ-cube can be generalized into the concept of a pure type system.

## Examples of systems

### (λ→) Simply typed lambda calculus

The simplest system found in the λ-cube is the simply typed lambda calculus, also called λ→. In this system, the only way to construct an abstraction is by making *a term depend on a term*, with the typing rule:

${\frac {\Gamma ,x:\sigma \;\vdash \;t:\tau }{\Gamma \;\vdash \;\lambda x.t:\sigma \to \tau }}$

### (λ2) System F

In System F (also named λ2 for the "second-order typed lambda calculus") there is another type of abstraction, written with a $\Lambda$ , that allows *terms to depend on types*, with the following rule:

${\frac {\Gamma \;\vdash \;t:\sigma }{\Gamma \;\vdash \;\Lambda \alpha .t:\Pi \alpha .\sigma }}\;{\text{ if }}\alpha {\text{ does not occur free in }}\Gamma$

The terms beginning with a $\Lambda$ are called polymorphic, as they can be applied to different types to get different functions, similarly to polymorphic functions in ML-like languages. For instance, the polymorphic identity

```mw
fun x -> x
```

of OCaml has type

```mw
'a -> 'a
```

meaning it can take an argument of any type `'a` and return an element of that type. This type corresponds in λ2 to the type $\Pi \alpha .\alpha \to \alpha$ .

### (λω) System Fω

In System F ${\underline {\omega }}$ a construction is introduced to supply *types that depend on other types*. This is called a type constructor and provides a way to build "a function with a type as a *value*". An example of such a type constructor is the type of binary trees with leaves labeled by data of a given type A : ${\mathsf {TREE}}:=\lambda A:*.\Pi B.(A\to B)\to (B\to B\to B)\to B$ , where " $A:*$ " informally means " A is a type". This is a function that takes a type parameter A as an argument and returns the type of ${\mathsf {TREE}}$ s of values of type A . In concrete programming, this feature corresponds to the ability to define type constructors inside the language, rather than considering them as primitives. The previous type constructor roughly corresponds to the following definition of a tree with labeled leaves in OCaml:

```mw
type 'a tree = | Leaf of 'a | Node of 'a tree * 'a tree
```

This type constructor can be applied to other types to obtain new types. E.g., to obtain type of trees of integers:

```mw
type int_tree = int tree
```

System F ${\underline {\omega }}$ is generally not used on its own, but is useful to isolate the independent feature of type constructors.

### (λP) Lambda-P

In the λP system, also named λΠ, which is closely related to the LF Logical Framework, one has so called dependent types. These are *types that are allowed to depend on terms*. The crucial introduction rule of the system is

${\frac {\Gamma ,x:A\;\vdash \;B:*}{\Gamma \;\vdash \;(\Pi x:A.B):*}}$

where * represents valid types. The new type constructor $\Pi$ corresponds via the Curry-Howard isomorphism to a universal quantifier, and the system λP as a whole corresponds to first-order logic with implication as only connective. An example of these dependent types in concrete programming is the type of vectors on a certain length: the length is a term, on which the type depends.

### (λω) System Fω

System Fω combines both the $\Lambda$ constructor of System F and the type constructors from System F ${\underline {\omega }}$ . Thus System Fω provides both *terms that depend on types* and *types that depend on types*.

### (λC) Calculus of constructions

In the calculus of constructions, denoted as λC in the cube or as λPω, these four features cohabit, so that both types and terms can depend on types and terms. The clear border that exists in λ→ between terms and types is somewhat abolished, as all types except the universal $\square$ are themselves terms with a type.

## Formal definition

As for all systems based upon the simply typed lambda calculus, all systems in the cube are given in two steps: first, raw terms, together with a notion of β-reduction, and then typing rules that allow to type those terms.

The set of sorts is defined as $S:=\{*,\square \}$ , sorts are represented with the letter s . There is also a set V of variables, represented by the letters $x,y,\dots$ . The raw terms of the eight systems of the cube are given by the following syntax:

$A:=x\mid s\mid A~A\mid \lambda x:A.A\mid \Pi x:A.A$

and $A\to B$ denoting $\Pi x:A.B$ when x does not occur free in B .

The environments, as is usual in typed systems, are given by ${\displaystyle \Gamma$

The notion of β-reduction is common to all systems in the cube. It is written $\to _{\beta }$ and given by the rules ${\frac {}{(\lambda x:A.B)~C\to _{\beta }B[C/x]}}$ ${\frac {B\to _{\beta }B'}{\lambda x:A.B\to _{\beta }\lambda x:A.B'}}$ ${\frac {A\to _{\beta }A'}{\lambda x:A.B\to _{\beta }\lambda x:A'.B}}$ ${\frac {B\to _{\beta }B'}{\Pi x:A.B\to _{\beta }\Pi x:A.B'}}$ ${\frac {A\to _{\beta }A'}{\Pi x:A.B\to _{\beta }\Pi x:A'.B}}$ Its reflexive, transitive closure is written $=_{\beta }$ .

The following typing rules are also common to all systems in the cube: ${\frac {}{\vdash *:\square }}\quad {\text{(Axiom)}}$ ${\frac {\Gamma \vdash A:s}{\Gamma ,x:A\vdash x:A}}x\not \in \Gamma \quad {\text{(Start)}}$ ${\frac {\Gamma \vdash A:B\quad \Gamma \vdash C:s}{\Gamma ,x:C\vdash A:B}}x\not \in \Gamma \quad {\text{(Weakening)}}$ ${\frac {\Gamma \vdash C:\Pi x:A.B\quad \Gamma \vdash D:A}{\Gamma \vdash CD:B[D/x]}}\quad {\text{(Application)}}$ ${\frac {\Gamma \vdash A:B\quad B=_{\beta }B'\quad \Gamma \vdash B':s}{\Gamma \vdash A:B'}}\quad {\text{(Conversion)}}$

The difference between the systems is in the pairs of sorts ${\textstyle (s_{1},s_{2})}$ that are allowed in the following two typing rules: ${\frac {\Gamma \vdash A:s_{1}\quad \Gamma ,x:A\vdash B:s_{2}}{\Gamma \vdash \Pi x:A.B:s_{2}}}\quad {\text{(Product)}}$ ${\frac {\Gamma \vdash A:s_{1}\quad \Gamma ,x:A\vdash B:s_{2}\quad \Gamma ,x:A\vdash C:B}{\Gamma \vdash \lambda x:A.C:\Pi x:A.B}}\quad {\text{(Abstraction)}}$

The correspondence between the systems and the pairs ${\textstyle (s_{1},s_{2})}$ allowed in the rules is the following:

| $(s_{1},s_{2})$ | $(*,*)$ | $(*,\square )$ | $(\square ,*)$ | $(\square ,\square )$ |
|---|---|---|---|---|
| λ→ | (Yes) | (No) | (No) | (No) |
| λP | (Yes) | (Yes) | (No) | (No) |
| λ2 | (Yes) | (No) | (Yes) | (No) |
| λω | (Yes) | (No) | (No) | (Yes) |
| λP2 | (Yes) | (Yes) | (Yes) | (No) |
| λPω | (Yes) | (Yes) | (No) | (Yes) |
| λω | (Yes) | (No) | (Yes) | (Yes) |
| λC | (Yes) | (Yes) | (Yes) | (Yes) |

Each direction of the cube corresponds to one pair (excluding the pair ${\textstyle (*,*)}$ shared by all systems), and in turn each pair corresponds to one possibility of dependency between terms and types:

- ${\textstyle (*,*)}$ allows terms to depend on terms.
- ${\textstyle (*,\square )}$ allows types to depend on terms.
- ${\textstyle (\square ,*)}$ allows terms to depend on types.
- ${\textstyle (\square ,\square )}$ allows types to depend on types.

## Comparison between the systems

### λ→

A typical derivation that can be obtained is ${\displaystyle \alpha$ or with the arrow shortcut ${\displaystyle \alpha$ closely resembling the identity (of type ${\textstyle \alpha }$ ) of the usual λ→. Note that all types used must appear in the context, because the only derivation that can be done in an empty context is ${\textstyle \vdash *:\square }$ .

The computing power is quite weak, it corresponds to the extended polynomials (polynomials together with a conditional operator).

### λ2

In λ2, such terms can be obtained as ${\displaystyle \vdash (\lambda \beta$ with ${\textstyle \bot =\Pi \alpha$ . If one reads ${\textstyle \Pi }$ as a universal quantification, via the Curry-Howard isomorphism, this can be seen as a proof of the principle of explosion. In general, λ2 adds the possibility to have impredicative types such as ${\textstyle \bot }$ , that is terms quantifying over all types including themselves. The polymorphism also allows the construction of functions that were not constructible in λ→. More precisely, the functions definable in λ2 are those provably total in second-order Peano arithmetic. In particular, all primitive recursive functions are definable.

### λP

In λP, the ability to have types depending on terms means one can express logical predicates. For instance, the following is derivable: ${\displaystyle {\begin{array}{l}\alpha$ which corresponds, via the Curry-Howard isomorphism, to a proof of $(\forall x:A,Px\to Q)\to (\forall x:A,Px)\to Q$ . From the computational point of view, however, having dependent types does not enhance computational power, only the possibility to express more precise type properties.

The conversion rule is strongly needed when dealing with dependent types, because it allows to perform computation on the terms in the type. For instance, if one has $\Gamma \vdash A:P((\lambda x.x)y)$ and $\Gamma \vdash B:\Pi x:P(y).C$ , one needs to apply the conversion rule to obtain $\Gamma \vdash A:P(y)$ to be able to type $\Gamma \vdash BA:C$ .

### λω

In λω, the following operator ${\displaystyle AND:=\lambda \alpha$ is definable, that is $\vdash AND:*\to *\to *$ . The derivation ${\displaystyle \alpha$ can be obtained already in λ2, however the polymorphic ${\textstyle AND}$ can only be defined if the rule ${\textstyle (\square ,*)}$ is also present.

From a computing point of view, λω is extremely strong, and has been considered as a basis for programming languages.

### λC

The calculus of constructions has both the predicate expressiveness of λP and the computational power of λω, hence why λC is also called λPω, so it is very powerful, both on the logical side and on the computational side.

## Relation to other systems

The system Automath is similar to λ2 from a logical point of view. The ML-like languages, from a typing point of view, lie somewhere between λ→ and λ2, as they admit a restricted kind of polymorphic types, that is the types in prenex normal form. However, because they feature some recursion operators, their computing power is greater than that of λ2. The Coq system is based on an extension of λC with a linear hierarchy of universes, rather than only one untypable ${\textstyle \square }$ , and the ability to construct inductive types.

Pure type systems can be seen as a generalization of the cube, with an arbitrary set of sorts, axiom, product and abstraction rules. Conversely, the systems of the lambda cube can be expressed as pure type systems with two sorts $\{*,\square \}$ , the only axiom ${\textstyle \{*,\square \}}$ , and a set of rules ${\textstyle R}$ such that $\{(*,*,*)\}\subseteq R\subseteq \{(*,*,*),(*,\square ,\square ),(\square ,*,*),(\square ,\square ,\square )\}$ .

Via the Curry-Howard isomorphism, there is a one-to-one correspondence between the systems in the lambda cube and logical systems, namely:

| System of the cube | Logical System |
|---|---|
| λ→ | (Zeroth-order) Propositional Calculus |
| λ2 | Second-order Propositional Calculus |
| λω | Weakly Higher Order Propositional Calculus |
| λω | Higher Order Propositional Calculus |
| λP | (First order) Predicate Logic |
| λP2 | Second-order Predicate Calculus |
| λPω | Weak Higher Order Predicate Calculus |
| λC | Calculus of Constructions |

All the logics are implicative (i.e. the only connectives are ${\textstyle \to }$ and ${\textstyle \forall }$ ); however, one can define other connectives such as $\wedge$ or $\neg$ in an impredicative way in second and higher order logics. In the weak higher order logics, there are variables for higher order predicates, but no quantification on those can be done.

## Common properties

All systems in the cube enjoy

- the Church-Rosser property: if $M\to _{\beta }N$ and $M\to _{\beta }N'$ then there exists $N''$ such that $N\to _{\beta }^{*}N''$ and $N'\to _{\beta }^{*}N''$ ;
- the subject reduction property: if $\Gamma \vdash M:T$ and $M\to _{\beta }M'$ then $\Gamma \vdash M':T$ ;
- the uniqueness of types: if $\Gamma \vdash A:B$ and $\Gamma \vdash A:B'$ then $B=_{\beta }B'$ .

All of these can be proven on generic pure type systems.

Any term well-typed in a system of the cube is strongly normalizing, although this property is not common to all pure type systems. No system in the cube is Turing complete.

## Subtyping

Subtyping however is not represented in the cube, even though systems like $F_{<:}^{\omega }$ , known as higher-order bounded quantification, which combines subtyping and polymorphism are of practical interest, and can be further generalized to bounded type operators. Further extensions to $F_{<:}^{\omega }$ allow the definition of purely functional objects; these systems were generally developed after the lambda cube paper was published.

The idea of the cube is due to the mathematician Henk Barendregt (1991). The framework of pure type systems generalizes the lambda cube in the sense that all corners of the cube, as well as many other systems can be represented as instances of this general framework. This framework predates the lambda cube by a couple of years. In his 1991 paper, Barendregt also defines the corners of the cube in this framework.
