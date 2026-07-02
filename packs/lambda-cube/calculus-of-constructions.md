---
title: "Calculus of constructions"
source: https://en.wikipedia.org/wiki/Calculus_of_constructions
domain: lambda-cube
license: CC-BY-SA-4.0
tags: lambda cube, pure type system, calculus of constructions, higher-order logic
fetched: 2026-07-02
---

# Calculus of constructions

In mathematical logic and computer science, the **calculus of constructions** (**CoC**) is a type theory created by Thierry Coquand. It can serve as both a typed programming language and as constructive foundation for mathematics. For this second reason, the CoC and its variants have been the basis for Rocq and other proof assistants.

Some of its variants include the calculus of inductive constructions (which adds inductive types), the calculus of (co)inductive constructions (which adds coinduction), and the predicative calculus of inductive constructions (which removes some impredicativity).

## General traits

The CoC is a higher-order typed lambda calculus, initially developed by Thierry Coquand. It is well known for being at the top of Barendregt's lambda cube. It is possible within CoC to define functions from terms to terms, terms to types, types to types, and from types to terms.

The CoC is strongly normalizing, and hence consistent.

## Usage

The CoC has been developed alongside the Rocq proof assistant. As features were added (or possible liabilities removed) to the theory, they became available in Rocq.

Variants of the CoC are used in other proof assistants, such as Matita and Lean.

## The basics of the calculus of constructions

The calculus of constructions can be considered an extension of the Curry–Howard isomorphism. The Curry–Howard isomorphism associates a term in the simply typed lambda calculus with each natural-deduction proof in intuitionistic propositional logic. The calculus of constructions extends this isomorphism to proofs in the full intuitionistic predicate calculus, which includes proofs of quantified statements (which we will also call "propositions").

### Terms

A *term* in the calculus of constructions is constructed using the following rules:

- $\mathbf {T}$ is a term (also called *type*);
- $\mathbf {P}$ is a term (also called *prop*, the type of all propositions);
- Variables ( $x,y,\ldots$ ) are terms;
- If A and B are terms, then so is $(AB)$ ;
- If A and B are terms and x is a variable, then the following are also terms:
  - $(\lambda x:A.B)$ ,
  - $(\forall x:A.B)$ .

In other words, the term syntax, in Backus–Naur form, is then:

$e::=\mathbf {T} \mid \mathbf {P} \mid x\mid e\,e\mid \lambda x{\mathbin {:}}e.e\mid \forall x{\mathbin {:}}e.e$

The calculus of constructions has five kinds of objects:

1. *proofs*, which are terms whose types are *propositions*;
2. *propositions*, which are also known as *small types*;
3. *predicates*, which are functions that return propositions;
4. *large types*, which are the types of predicates ( $\mathbf {P}$ is an example of a large type);
5. $\mathbf {T}$ itself, which is the type of large types.

### β-equivalence

As with the untyped lambda calculus, the calculus of constructions uses a basic notion of equivalence of terms, known as $\beta$ -equivalence. This captures the meaning of $\lambda$ -abstraction:

- $(\lambda x:A.B)N=_{\beta }B(x:=N)$

$\beta$ -equivalence is a congruence relation for the calculus of constructions, in the sense that

- If $A=_{\beta }B$ and $M=_{\beta }N$ , then $AM=_{\beta }BN$ .

### Judgments

The calculus of constructions allows proving **typing judgments**:

$x_{1}:A_{1},x_{2}:A_{2},\ldots \vdash t:B$

,

which can be read as the implication

If variables

$x_{1},x_{2},\ldots$

have, respectively, types

$A_{1},A_{2},\ldots$

, then term

t

has type

B

.

The valid judgments for the calculus of constructions are derivable from a set of inference rules. In the following, we use $\Gamma$ to mean a sequence of type assignments $x_{1}:A_{1},x_{2}:A_{2},\ldots$ ; $A,B,C,D$ to mean terms; and $K,L$ to mean either $\mathbf {P}$ or $\mathbf {T}$ . We shall write $B[x:=N]$ to mean the result of substituting the term N for the free variable x in the term B .

An inference rule is written in the form

${\frac {\Gamma \vdash A:B}{\Gamma '\vdash C:D}}$

,

which means

if

$\Gamma \vdash A:B$

is a valid judgment, then so is

$\Gamma '\vdash C:D$

.

### Inference rules for the calculus of constructions

**1**. ${{} \over \Gamma \vdash \mathbf {P} :\mathbf {T} }$

**2**. ${{\Gamma \vdash A:K} \over {\Gamma ,x:A,\Gamma '\vdash x:A}}$

**3**. ${\Gamma \vdash A:K\qquad \qquad \Gamma ,x:A\vdash B:L \over {\Gamma \vdash (\forall x:A.B):L}}$

**4**. ${\Gamma \vdash A:K\qquad \qquad \Gamma ,x:A\vdash N:B \over {\Gamma \vdash (\lambda x:A.N):(\forall x:A.B)}}$

**5**. ${\Gamma \vdash M:(\forall x:A.B)\qquad \qquad \Gamma \vdash N:A \over {\Gamma \vdash MN:B[x:=N]}}$

**6**. ${\Gamma \vdash M:A\qquad \qquad A=_{\beta }B\qquad \qquad \Gamma \vdash B:K \over {\Gamma \vdash M:B}}$

### Defining logical operators

The calculus of constructions has very few basic operators: the only logical operator for forming propositions is $\forall$ . However, this one operator is sufficient to define all the other logical operators:

${\begin{array}{ccll}A\Rightarrow B&\equiv &\forall x:A.B&(x\notin B)\\A\wedge B&\equiv &\forall C:\mathbf {P} .(A\Rightarrow B\Rightarrow C)\Rightarrow C&\\A\vee B&\equiv &\forall C:\mathbf {P} .(A\Rightarrow C)\Rightarrow (B\Rightarrow C)\Rightarrow C&\\\neg A&\equiv &\forall C:\mathbf {P} .(A\Rightarrow C)&\\\exists x:A.B&\equiv &\forall C:\mathbf {P} .(\forall x:A.(B\Rightarrow C))\Rightarrow C&\end{array}}$

### Defining data types

The basic data types used in computer science can be defined within the calculus of constructions:

**Booleans**

$\forall A:\mathbf {P} .A\Rightarrow A\Rightarrow A$

**Naturals**

$\forall A:\mathbf {P} .(A\Rightarrow A)\Rightarrow A\Rightarrow A$

**Product $A\times B$**

$A\wedge B$

**Disjoint union $A+B$**

$A\vee B$

Booleans and Naturals are defined in the same way as in Church encoding. However, added problems arise from propositional extensionality and proof irrelevance.
