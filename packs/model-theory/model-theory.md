---
title: "Model theory"
source: https://en.wikipedia.org/wiki/Model_theory
domain: model-theory
license: CC-BY-SA-4.0
tags: model theory, compactness theorem, elementary equivalence, quantifier elimination
fetched: 2026-07-02
---

# Model theory

In mathematical logic, **model theory** is the study of the relationship between formal theories (a collection of sentences in a formal language expressing statements about a mathematical structure) and their models (those structures in which the statements of the theory hold). The aspects investigated include the number and size of models of a theory, the relationship of different models to each other, and their interaction with the formal language itself. In particular, model theorists also investigate the sets that can be defined in a model of a theory, and the relationship of such definable sets to each other. As a separate discipline, model theory goes back to Alfred Tarski, who first used the term "Theory of Models" in publication in 1954. Since the 1970s, the subject has been shaped decisively by Saharon Shelah's stability theory.

Compared to other areas of mathematical logic such as proof theory, model theory is often less concerned with formal rigour and closer in spirit to classical mathematics. This has prompted the comment that *"if proof theory is about the sacred, then model theory is about the profane"*. The applications of model theory to algebraic and Diophantine geometry reflect this proximity to classical mathematics, as they often involve an integration of algebraic and model-theoretic results and techniques. Consequently, proof theory is syntactic in nature, in contrast to model theory, which is semantic in nature.

## Overview

This article focuses on finitary first order model theory.

The relative emphasis placed on the class of models of a theory as opposed to the class of definable sets within a model fluctuated in the history of the subject, and the two directions are summarised by the pithy characterisations from 1973 and 1997 respectively:

model theory

=

universal algebra

+

logic

where universal algebra stands for mathematical structures and logic for logical theories; and

model theory

=

algebraic geometry

−

fields

.

where logical formulas are to definable sets what equations are to varieties over a field.

Nonetheless, the interplay of classes of models and the sets definable in them has been crucial to the development of model theory throughout its history. For instance, while stability was originally introduced to classify theories by their numbers of models in a given cardinality, stability theory proved crucial to understanding the geometry of definable sets.

## Fundamental notions of first-order model theory

### First-order logic

A first-order *formula* is built out of atomic formulas such as $R(f(x,y),z)$ or $y=x+1$ by means of the Boolean connectives $\neg ,\land ,\lor ,\rightarrow$ and prefixing of quantifiers $\forall v$ or $\exists v$ . A sentence is a formula in which each occurrence of a variable is in the scope of a corresponding quantifier. Examples for formulas are $\varphi$ (or $\varphi (x)$ to indicate x is the unbound variable in $\varphi$ ) and $\psi$ (or $\psi (x)$ ), defined as follows:

${\begin{array}{lcl}\varphi &=&\forall u\forall v(\exists w(x\times w=u\times v)\rightarrow (\exists w(x\times w=u)\lor \exists w(x\times w=v)))\land x\neq 0\land x\neq 1,\\\psi &=&\forall u\forall v((u\times v=x)\rightarrow (u=x)\lor (v=x))\land x\neq 0\land x\neq 1.\end{array}}$

(Note that the equality symbol has a double meaning here.) It is intuitively clear how to translate such formulas into mathematical meaning. In the semiring of natural numbers ${\mathcal {N}}$ , viewed as a structure with binary functions for addition and multiplication and constants for 0 and 1 of the natural numbers, for example, an element n *satisfies* the formula $\varphi$ if and only if n is a prime number. The formula $\psi$ similarly defines irreducibility. Tarski gave a rigorous definition, sometimes called "Tarski's definition of truth", for the satisfaction relation $\models$ , so that one easily proves:

${\mathcal {N}}\models \varphi (n)\iff n$

is a prime number.

${\mathcal {N}}\models \psi (n)\iff n$

is irreducible.

A set T of sentences is called a (first-order) theory, which takes the sentences in the set as its axioms. A theory is *satisfiable* if it has a *model* ${\mathcal {M}}\models T$ , i.e. a structure (of the appropriate signature) which satisfies all the sentences in the set T . A complete theory is a theory that contains every sentence or its negation. The complete theory of all sentences satisfied by a structure is also called the *theory of that structure*.

It's a consequence of Gödel's completeness theorem (not to be confused with his incompleteness theorems) that a theory has a model if and only if it is consistent, i.e. no contradiction is proved by the theory. Therefore, model theorists often use "consistent" as a synonym for "satisfiable".

### Basic model-theoretic concepts

A signature or language is a set of non-logical symbols such that each symbol is either a constant symbol, or a function or relation symbol with a specified arity. Note that in some literature, constant symbols are considered as function symbols with zero arity, and hence are omitted. A structure is a set M together with interpretations of each of the symbols of the signature as relations and functions on M (not to be confused with the formal notion of an "interpretation" of one structure in another).

**Example:** A common signature for ordered rings is $\sigma _{or}=(0,1,+,\times ,-,<)$ , where 0 and 1 are 0-ary function symbols (also known as constant symbols), + and $\times$ are binary (= 2-ary) function symbols, - is a unary (= 1-ary) function symbol, and < is a binary relation symbol. Then, when these symbols are interpreted to correspond with their usual meaning on $\mathbb {Q}$ (so that e.g. + is a function from $\mathbb {Q} ^{2}$ to $\mathbb {Q}$ and < is a subset of $\mathbb {Q} ^{2}$ ), one obtains a structure $(\mathbb {Q} ,\sigma _{or})$ .

A structure ${\mathcal {N}}$ is said to model a set of first-order sentences T in the given language if each sentence in T is true in ${\mathcal {N}}$ with respect to the interpretation of the signature previously specified for ${\mathcal {N}}$ . (Again, not to be confused with the formal notion of an "interpretation" of one structure in another) A *model* of T is a structure that models T .

A substructure ${\mathcal {A}}$ of a σ-structure ${\mathcal {B}}$ is a subset of its domain, closed under all functions in its signature σ, which is regarded as a σ-structure by restricting all functions and relations in σ to the subset. This generalises the analogous concepts from algebra; for instance, a subgroup is a substructure in the signature with multiplication and inverse.

A substructure is said to be *elementary* if for any first-order formula $\varphi$ and any elements *a*1, ..., *a**n* of ${\mathcal {A}}$ ,

${\mathcal {A}}\models \varphi (a_{1},...,a_{n})$

if and only if

${\mathcal {B}}\models \varphi (a_{1},...,a_{n})$

.

In particular, if $\varphi$ is a sentence and ${\mathcal {A}}$ an elementary substructure of ${\mathcal {B}}$ , then ${\mathcal {A}}\models \varphi$ if and only if ${\mathcal {B}}\models \varphi$ . Thus, an elementary substructure is a model of a theory exactly when the superstructure is a model.

**Example:** While the field of algebraic numbers ${\overline {\mathbb {Q} }}$ is an elementary substructure of the field of complex numbers $\mathbb {C}$ , the rational field $\mathbb {Q}$ is not, as we can express "There is a square root of 2" as a first-order sentence satisfied by $\mathbb {C}$ but not by $\mathbb {Q}$ .

An embedding of a σ-structure ${\mathcal {A}}$ into another σ-structure ${\mathcal {B}}$ is a map *f*: *A* → *B* between the domains which can be written as an isomorphism of ${\mathcal {A}}$ with a substructure of ${\mathcal {B}}$ . If it can be written as an isomorphism with an elementary substructure, it is called an elementary embedding. Every embedding is an injective homomorphism, but the converse holds only if the signature contains no relation symbols, such as in groups or fields.

A field or a vector space can be regarded as a (commutative) group by simply ignoring some of its structure. The corresponding notion in model theory is that of a *reduct* of a structure to a subset of the original signature. The opposite relation is called an *expansion* - e.g. the (additive) group of the rational numbers, regarded as a structure in the signature {+,0} can be expanded to a field with the signature {×,+,1,0} or to an ordered group with the signature {+,0,<}.

Similarly, if σ' is a signature that extends another signature σ, then a complete σ'-theory can be restricted to σ by intersecting the set of its sentences with the set of σ-formulas. Conversely, a complete σ-theory can be regarded as a σ'-theory, and one can extend it (in more than one way) to a complete σ'-theory. The terms reduct and expansion are sometimes applied to this relation as well.

### Compactness and the Löwenheim–Skolem theorem

The compactness theorem states that a set of sentences S is satisfiable if every finite subset of S is satisfiable. The analogous statement with *consistent* instead of *satisfiable* is trivial, since every proof can have only a finite number of antecedents used in the proof. The completeness theorem allows us to transfer this to satisfiability. However, there are also several direct (semantic) proofs of the compactness theorem. As a corollary (i.e., its contrapositive), the compactness theorem says that every unsatisfiable first-order theory has a finite unsatisfiable subset. This theorem is of central importance in model theory, where the words "by compactness" are commonplace.

Another cornerstone of first-order model theory is the Löwenheim–Skolem theorem. According to the theorem, every infinite structure in a countable signature has a countable elementary substructure. Conversely, for any infinite cardinal κ every infinite structure in a countable signature that is of cardinality less than κ can be elementarily embedded in another structure of cardinality κ (There is a straightforward generalisation to uncountable signatures). In particular, the Löwenheim-Skolem theorem implies that any theory in a countable signature with infinite models has a countable model as well as arbitrarily large models.

In a certain sense made precise by Lindström's theorem, first-order logic is the most expressive logic for which both the Löwenheim–Skolem theorem and the compactness theorem hold.

## Definability

### Definable sets

In model theory, definable sets are important objects of study. For instance, in $\mathbb {N}$ the formula

$\forall u\forall v(\exists w(x\times w=u\times v)\rightarrow (\exists w(x\times w=u)\lor \exists w(x\times w=v)))\land x\neq 0\land x\neq 1$

defines the subset of prime numbers, while the formula

$\exists y(2\times y=x)$

defines the subset of even numbers. In a similar way, formulas with *n* free variables define subsets of ${\mathcal {M}}^{n}$ . For example, in a field, the formula

$y=x\times x$

defines the curve of all $(x,y)$ such that $y=x^{2}$ .

Both of the definitions mentioned here are *parameter-free*, that is, the defining formulas don't mention any fixed domain elements. However, one can also consider definitions *with parameters from the model*. For instance, in $\mathbb {R}$ , the formula

$y=x\times x+\pi$

uses the parameter $\pi$ from $\mathbb {R}$ to define a curve.

### Eliminating quantifiers

In general, definable sets without quantifiers are easy to describe, while definable sets involving possibly nested quantifiers can be much more complicated.

This makes quantifier elimination a crucial tool for analysing definable sets: A theory *T* has quantifier elimination if every first-order formula *φ*(*x*1, ..., *x**n*) over its signature is equivalent modulo *T* to a first-order formula *ψ*(*x*1, ..., *x**n*) without quantifiers, i.e. $\forall x_{1}\dots \forall x_{n}(\phi (x_{1},\dots ,x_{n})\leftrightarrow \psi (x_{1},\dots ,x_{n}))$ holds in all models of *T*. If the theory of a structure has quantifier elimination, every set definable in a structure is definable by a quantifier-free formula over the same parameters as the original definition. For example, the theory of algebraically closed fields in the signature *σ*ring = (×,+,−,0,1) has quantifier elimination. This means that in an algebraically closed field, every formula is equivalent to a Boolean combination of equations between polynomials.

If a theory does not have quantifier elimination, one can add additional symbols to its signature so that it does. Axiomatisability and quantifier elimination results for specific theories, especially in algebra, were among the early landmark results of model theory. But often instead of quantifier elimination a weaker property suffices:

A theory *T* is called model-complete if every substructure of a model of *T* which is itself a model of *T* is an elementary substructure. There is a useful criterion for testing whether a substructure is an elementary substructure, called the Tarski–Vaught test. It follows from this criterion that a theory *T* is model-complete if and only if every first-order formula *φ*(*x*1, ..., *x**n*) over its signature is equivalent modulo *T* to an existential first-order formula, i.e. a formula of the following form:

$\exists v_{1}\dots \exists v_{m}\psi (x_{1},\dots ,x_{n},v_{1},\dots ,v_{m})$

,

where ψ is quantifier free. A theory that is not model-complete may have a model completion, which is a related model-complete theory that is not, in general, an extension of the original theory. A more general notion is that of a model companion.

### Minimality

In every structure, every finite subset $\{a_{1},\dots ,a_{n}\}$ is definable with parameters: Simply use the formula

$x=a_{1}\vee \dots \vee x=a_{n}$

.

Since we can negate this formula, every cofinite subset (which includes all but finitely many elements of the domain) is also always definable.

This leads to the concept of a *minimal structure*. A structure ${\mathcal {M}}$ is called minimal if every subset $A\subseteq {\mathcal {M}}$ definable with parameters from ${\mathcal {M}}$ is either finite or cofinite. The corresponding concept at the level of theories is called *strong minimality*: A theory *T* is called strongly minimal if every model of *T* is minimal. A structure is called *strongly minimal* if the theory of that structure is strongly minimal. Equivalently, a structure is strongly minimal if every elementary extension is minimal. Since the theory of algebraically closed fields has quantifier elimination, every definable subset of an algebraically closed field is definable by a quantifier-free formula in one variable. Quantifier-free formulas in one variable express Boolean combinations of polynomial equations in one variable, and since a nontrivial polynomial equation in one variable has only a finite number of solutions, the theory of algebraically closed fields is strongly minimal.

On the other hand, the field $\mathbb {R}$ of real numbers is not minimal: Consider, for instance, the definable set

$\varphi (x)\;=\;\exists y(y\times y=x)$

.

This defines the subset of non-negative real numbers, which is neither finite nor cofinite. One can in fact use $\varphi$ to define arbitrary intervals on the real number line. It turns out that these suffice to represent every definable subset of $\mathbb {R}$ . This generalisation of minimality has been very useful in the model theory of ordered structures. A densely totally ordered structure ${\mathcal {M}}$ in a signature including a symbol for the order relation is called o-minimal if every subset $A\subseteq {\mathcal {M}}$ definable with parameters from ${\mathcal {M}}$ is a finite union of points and intervals.

### Definable and interpretable structures

Particularly important are those definable sets that are also substructures, i. e. contain all constants and are closed under function application. For instance, one can study the definable subgroups of a certain group. However, there is no need to limit oneself to substructures in the same signature. Since formulas with *n* free variables define subsets of ${\mathcal {M}}^{n}$ , *n*-ary relations can also be definable. Functions are definable if the function graph is a definable relation, and constants $a\in {\mathcal {M}}$ are definable if there is a formula $\varphi (x)$ such that *a* is the only element of ${\mathcal {M}}$ such that $\varphi (a)$ is true. In this way, one can study definable groups and fields in general structures, for instance, which has been important in geometric stability theory.

One can even go one step further, and move beyond immediate substructures. Given a mathematical structure, there are very often associated structures which can be constructed as a quotient of part of the original structure via an equivalence relation. An important example is a quotient group of a group. One might say that to understand the full structure one must understand these quotients. When the equivalence relation is definable, we can give the previous sentence a precise meaning. We say that these structures are *interpretable*. A key fact is that one can translate sentences from the language of the interpreted structures to the language of the original structure. Thus one can show that if a structure ${\mathcal {M}}$ interprets another whose theory is undecidable, then ${\mathcal {M}}$ itself is undecidable.

## Types

### Basic notions

For a sequence of elements $a_{1},\dots ,a_{n}$ of a structure ${\mathcal {M}}$ and a subset *A* of ${\mathcal {M}}$ , one can consider the set of all first-order formulas $\varphi (x_{1},\dots ,x_{n})$ with parameters in *A* that are satisfied by $a_{1},\dots ,a_{n}$ . This is called the *complete (n-)type realised by* $a_{1},\dots ,a_{n}$ *over A*. If there is an automorphism of ${\mathcal {M}}$ that is constant on *A* and sends $a_{1},\dots ,a_{n}$ to $b_{1},\dots ,b_{n}$ respectively, then $a_{1},\dots ,a_{n}$ and $b_{1},\dots ,b_{n}$ realise the same complete type over *A*.

The real number line $\mathbb {R}$ , viewed as a structure with only the order relation {<}, will serve as a running example in this section. Every element $a\in \mathbb {R}$ satisfies the same 1-type over the empty set. This is clear since any two real numbers *a* and *b* are connected by the order automorphism that shifts all numbers by *b-a*. The complete 2-type over the empty set realised by a pair of numbers $a_{1},a_{2}$ depends on their order: either $a_{1}<a_{2}$ , $a_{1}=a_{2}$ or $a_{2}<a_{1}$ . Over the subset $\mathbb {Z} \subseteq \mathbb {R}$ of integers, the 1-type of a non-integer real number *a* depends on its value rounded down to the nearest integer.

More generally, whenever ${\mathcal {M}}$ is a structure and *A* a subset of ${\mathcal {M}}$ , a (partial) *n-type over A* is a set of formulas *p* with at most *n* free variables that are realised in an elementary extension ${\mathcal {N}}$ of ${\mathcal {M}}$ . If *p* contains every such formula or its negation, then *p* is *complete*. The set of complete *n*-types over *A* is often written as $S_{n}^{\mathcal {M}}(A)$ . If *A* is the empty set, then the type space only depends on the theory T of ${\mathcal {M}}$ . The notation $S_{n}(T)$ is commonly used for the set of types over the empty set consistent with T . If there is a single formula $\varphi$ such that the theory of ${\mathcal {M}}$ implies $\varphi \rightarrow \psi$ for every formula $\psi$ in *p*, then *p* is called *isolated*.

Since the real numbers $\mathbb {R}$ are Archimedean, there is no real number larger than every integer. However, a compactness argument shows that there is an elementary extension of the real number line in which there is an element larger than any integer. Therefore, the set of formulas $\{n<x|n\in \mathbb {Z} \}$ is a 1-type over $\mathbb {Z} \subseteq \mathbb {R}$ that is not realised in the real number line $\mathbb {R}$ .

A subset of ${\mathcal {M}}^{n}$ that can be expressed as exactly those elements of ${\mathcal {M}}^{n}$ realising a certain type over *A* is called *type-definable* over *A*. For an algebraic example, suppose M is an algebraically closed field. The theory has quantifier elimination . This allows us to show that a type is determined exactly by the polynomial equations it contains. Thus the set of complete n -types over a subfield A corresponds to the set of prime ideals of the polynomial ring $A[x_{1},\ldots ,x_{n}]$ , and the type-definable sets are exactly the affine varieties.

### Structures and types

While not every type is realised in every structure, every structure realises its isolated types. If the only types over the empty set that are realised in a structure are the isolated types, then the structure is called *atomic*.

On the other hand, no structure realises every type over every parameter set; if one takes all of ${\mathcal {M}}$ as the parameter set, then every 1-type over ${\mathcal {M}}$ realised in ${\mathcal {M}}$ is isolated by a formula of the form *a = x* for an $a\in {\mathcal {M}}$ . However, any proper elementary extension of ${\mathcal {M}}$ contains an element that is *not* in ${\mathcal {M}}$ . Therefore, a weaker notion has been introduced that captures the idea of a structure realising all types it could be expected to realise. A structure is called *saturated* if it realises every type over a parameter set $A\subset {\mathcal {M}}$ that is of smaller cardinality than ${\mathcal {M}}$ itself.

While an automorphism that is constant on *A* will always preserve types over *A*, it is generally not true that any two sequences $a_{1},\dots ,a_{n}$ and $b_{1},\dots ,b_{n}$ that satisfy the same type over *A* can be mapped to each other by such an automorphism. A structure ${\mathcal {M}}$ in which this converse does hold for all *A* of smaller cardinality than ${\mathcal {M}}$ is called (strongly) **homogeneous**.

The real number line is atomic in the language that contains only the order < , since all *n*-types over the empty set realised by $a_{1},\dots ,a_{n}$ in $\mathbb {R}$ are isolated by the order relations between the $a_{1},\dots ,a_{n}$ . It is not saturated, however, since it does not realise any 1-type over the countable set $\mathbb {Z}$ that implies *x* to be larger than any integer. The rational number line $\mathbb {Q}$ is saturated, in contrast, since $\mathbb {Q}$ is itself countable and therefore only has to realise types over finite subsets to be saturated.

### Stone spaces

The set of definable subsets of ${\mathcal {M}}^{n}$ over some parameters A is a Boolean algebra. By Stone's representation theorem for Boolean algebras there is a natural dual topological space, which consists exactly of the complete n -types over A . The topology generated by sets of the form $\{p|\varphi \in p\}$ for single formulas $\varphi$ . This is called the *Stone space of n-types over A*. This topology explains some of the terminology used in model theory: The compactness theorem says that the Stone space is a compact topological space, and a type *p* is isolated if and only if *p* is an isolated point in the Stone topology.

While types in algebraically closed fields correspond to the spectrum of the polynomial ring, the topology on the type space is the constructible topology: a set of types is basic open iff it is of the form $\{p:f(x)=0\in p\}$ or of the form $\{p:f(x)\neq 0\in p\}$ . This is finer than the Zariski topology.

## Constructing models

### Realising and omitting types

Constructing models that realise certain types and do not realise others is an important task in model theory. Not realising a type is referred to as *omitting* it, and is generally possible by the *(Countable) Omitting types theorem*:

Let

${\mathcal {T}}$

be a theory in a countable signature and let

$\Phi$

be a countable set of non-isolated types over the empty set.

Then there is a model

${\mathcal {M}}$

of

${\mathcal {T}}$

which omits every type in

$\Phi$

.

This implies that if a theory in a countable signature has only countably many types over the empty set, then this theory has an atomic model.

On the other hand, there is always an elementary extension in which any set of types over a fixed parameter set is realised:

Let

${\mathcal {M}}$

be a structure and let

$\Phi$

be a set of complete types over a given parameter set

$A\subset {\mathcal {M}}.$

Then there is an elementary extension

${\mathcal {N}}$

of

${\mathcal {M}}$

which realises every type in

$\Phi$

.

However, since the parameter set is fixed and there is no mention here of the cardinality of ${\mathcal {N}}$ , this does not imply that every theory has a saturated model. In fact, whether every theory has a saturated model is independent of the axioms of Zermelo–Fraenkel set theory, and is true if the generalised continuum hypothesis holds.

### Ultraproducts

Ultraproducts are used as a general technique for constructing models that realise certain types. An *ultraproduct* is obtained from the direct product of a set of structures over an index set I by identifying those tuples that agree on almost all entries, where *almost all* is made precise by an ultrafilter U on I. An ultraproduct of copies of the same structure is known as an *ultrapower*. The key to using ultraproducts in model theory is *Łoś's theorem*:

Let

${\mathcal {M}}_{i}$

be a set of

σ

-structures indexed by an index set

I

and

U

an ultrafilter on

I

. Then any

σ

-formula

$\varphi ([(a_{i})_{i\in :I}])$

is true in the ultraproduct of the

${\mathcal {M}}_{i}$

by

U

if the set of all

$i\in I$

for which

${\mathcal {M}}_{i}\models \varphi (a_{i})$

lies in

U

.

In particular, any ultraproduct of models of a theory is itself a model of that theory, and thus if two models have isomorphic ultrapowers, they are elementarily equivalent. The *Keisler-Shelah theorem* provides a converse:

If

M

and

N

are elementarily equivalent, then there is a set

I

and an ultrafilter

U

on

I

such that the ultrapowers by

U

of

M

and

:

N

are isomorphic.

Therefore, ultraproducts provide a way to talk about elementary equivalence that avoids mentioning first-order theories at all. Basic theorems of model theory such as the compactness theorem have alternative proofs using ultraproducts, and they can be used to construct saturated elementary extensions if they exist.

## Categoricity

A theory was originally called *categorical* if it determines a structure up to isomorphism. It turns out that this definition is not useful, due to serious restrictions in the expressivity of first-order logic. The Löwenheim–Skolem theorem implies that if a theory *T* has an infinite model for some infinite cardinal number, then it has a model of size κ for any sufficiently large cardinal number κ. Since two models of different sizes cannot possibly be isomorphic, only finite structures can be described by a categorical theory.

However, the weaker notion of κ-categoricity for a cardinal κ has become a key concept in model theory. A theory *T* is called *κ-categorical* if any two models of *T* that are of cardinality κ are isomorphic. It turns out that the question of κ-categoricity depends critically on whether κ is bigger than the cardinality of the language (i.e. $\aleph _{0}+|\sigma |$ , where |*σ*| is the cardinality of the signature). For finite or countable signatures this means that there is a fundamental difference between ω-cardinality and κ-cardinality for uncountable κ.

### ω-categoricity

ω-categorical theories can be characterised by properties of their type space:

For a complete first-order theory

T

in a finite or countable signature the following conditions are equivalent:

1. *T* is ω-categorical.
2. Every type in *Sn*(*T*) is isolated.
3. For every natural number *n*, *Sn*(*T*) is finite.
4. For every natural number *n*, the number of formulas *φ*(*x*1, ..., *x*n) in *n* free variables, up to equivalence modulo *T*, is finite.

The theory of $(\mathbb {Q} ,<)$ , which is also the theory of $(\mathbb {R} ,<)$ , is ω-categorical, as every *n*-type $p(x_{1},\dots ,x_{n})$ over the empty set is isolated by the pairwise order relation between the $x_{i}$ . This means that every countable dense linear order is order-isomorphic to the rational number line. On the other hand, the theories of ℚ, ℝ and ℂ as fields are not $\omega$ -categorical. This follows from the fact that in all those fields, any of the infinitely many natural numbers can be defined by a formula of the form $x=1+\dots +1$ .

$\aleph _{0}$ -categorical theories and their countable models also have strong ties with oligomorphic groups:

A complete first-order theory

T

in a finite or countable signature is

ω

-categorical if and only if its automorphism group is oligomorphic.

The equivalent characterisations of this subsection, due independently to Engeler, Ryll-Nardzewski and Svenonius, are sometimes referred to as the Ryll-Nardzewski theorem.

In combinatorial signatures, a common source of ω-categorical theories are Fraïssé limits, which are obtained as the limit of amalgamating all possible configurations of a class of finite relational structures.

### Uncountable categoricity

Michael Morley showed in 1963 that there is only one notion of *uncountable categoricity* for theories in countable languages.

Morley's categoricity theorem

If a first-order theory

T

in a finite or countable signature is

κ

-categorical for some uncountable cardinal

κ

, then

T

is

κ

-categorical for all uncountable cardinals

κ

.

Morley's proof revealed deep connections between uncountable categoricity and the internal structure of the models, which became the starting point of classification theory and stability theory. Uncountably categorical theories are from many points of view the most well-behaved theories. In particular, complete strongly minimal theories are uncountably categorical. This shows that the theory of algebraically closed fields of a given characteristic is uncountably categorical, with the transcendence degree of the field determining its isomorphism type.

A theory that is both ω-categorical and uncountably categorical is called *totally categorical*.

## Stability theory

A key factor in the structure of the class of models of a first-order theory is its place in the *stability hierarchy*.

A complete theory

T

is called

$\lambda$

-stable

for a cardinal

$\lambda$

if for any model

${\mathcal {M}}$

of

T

and any parameter set

$A\subset {\mathcal {M}}$

of cardinality not exceeding

$\lambda$

, there are at most

$\lambda$

complete

T

-types over

A

.

A theory is called *stable* if it is $\lambda$ -stable for some infinite cardinal $\lambda$ . Traditionally, theories that are $\aleph _{0}$ -stable are called *$\omega$ -stable*.

### The stability hierarchy

A fundamental result in stability theory is the *stability spectrum theorem*, which implies that every complete theory *T* in a countable signature falls in one of the following classes:

1. There are no cardinals $\lambda$ such that *T* is $\lambda$ -stable.
2. *T* is $\lambda$ -stable if and only if $\lambda ^{\aleph _{0}}=\lambda$ (see Cardinal exponentiation for an explanation of $\lambda ^{\aleph _{0}}$ ).
3. *T* is $\lambda$ -stable for any $\lambda \geq 2^{\aleph _{0}}$ (where $2^{\aleph _{0}}$ is the cardinality of the continuum).

A theory of the first type is called *unstable*, a theory of the second type is called *strictly stable* and a theory of the third type is called *superstable*. Furthermore, if a theory is $\omega$ -stable, it is stable in every infinite cardinal, so $\omega$ -stability is stronger than superstability.

Many constructions in model theory are easier when restricted to stable theories; for instance, every model of a stable theory has a saturated elementary extension, regardless of whether the generalised continuum hypothesis is true.

Shelah's original motivation for studying stable theories was to decide how many models a countable theory has of any uncountable cardinality. If a theory is uncountably categorical, then it is $\omega$ -stable. More generally, the *Main gap theorem* implies that if there is an uncountable cardinal $\lambda$ such that a theory *T* has less than $2^{\lambda }$ models of cardinality $\lambda$ , then *T* is superstable.

### Geometric stability theory

The stability hierarchy is also crucial for analysing the geometry of definable sets within a model of a theory. In $\omega$ -stable theories, *Morley rank* is an important dimension notion for definable sets *S* within a model. It is defined by transfinite induction:

- The Morley rank is at least 0 if *S* is non-empty.
- For *α* a successor ordinal, the Morley rank is at least *α* if in some elementary extension *N* of *M*, the set *S* has infinitely many disjoint definable subsets, each of rank at least *α* − 1.
- For *α* a non-zero limit ordinal, the Morley rank is at least *α* if it is at least *β* for all *β* less than *α*.

A theory *T* in which every definable set has well-defined Morley rank is called *totally transcendental*; if *T* is countable, then *T* is totally transcendental if and only if *T* is $\omega$ -stable. Morley Rank can be extended to types by setting the Morley rank of a type to be the minimum of the Morley ranks of the formulas in the type. Thus, one can also speak of the Morley rank of an element *a* over a parameter set *A*, defined as the Morley rank of the type of *a* over *A*. There are also analogues of Morley rank which are well-defined if and only if a theory is superstable (U-rank) or merely stable (Shelah's $\infty$ -rank). Those dimension notions can be used to define notions of independence and of generic extensions.

More recently, stability has been decomposed into simplicity and "not the independence property" (NIP). Simple theories are those theories in which a well-behaved notion of independence can be defined, while NIP theories generalise o-minimal structures. They are related to stability since a theory is stable if and only if it is NIP and simple, and various aspects of stability theory have been generalised to theories in one of these classes.

## Non-elementary model theory

Model-theoretic results have been generalised beyond elementary classes, that is, classes axiomatisable by a first-order theory.

Model theory in higher-order logics or infinitary logics is hampered by the fact that completeness and compactness do not in general hold for these logics. This is made concrete by Lindström's theorem, stating roughly that first-order logic is essentially the strongest logic in which both the Löwenheim-Skolem theorems and compactness hold. However, model theoretic techniques have been developed extensively for these logics too. It turns out, however, that much of the model theory of more expressive logical languages is independent of Zermelo–Fraenkel set theory.

More recently, alongside the shift in focus to complete stable and categorical theories, there has been work on classes of models defined semantically rather than axiomatised by a logical theory. One example is *homogeneous model theory*, which studies the class of substructures of arbitrarily large homogeneous models. Fundamental results of stability theory and geometric stability theory generalise to this setting. As a generalisation of strongly minimal theories, quasiminimally excellent classes are those in which every definable set is either countable or co-countable. They are key to the model theory of the complex exponential function. The most general semantic framework in which stability is studied are abstract elementary classes, which are defined by a *strong substructure* relation generalising that of an elementary substructure. Even though its definition is purely semantic, every abstract elementary class can be presented as the models of a first-order theory which omit certain types. Generalising stability-theoretic notions to abstract elementary classes is an ongoing research program.

## Selected applications

Among the early successes of model theory are Tarski's proofs of quantifier elimination for various algebraically interesting classes, such as the real closed fields, Boolean algebras and algebraically closed fields of a given characteristic. Quantifier elimination allowed Tarski to show that the first-order theories of real-closed and algebraically closed fields as well as the first-order theory of Boolean algebras are decidable, classify the Boolean algebras up to elementary equivalence and show that the theories of real-closed fields and algebraically closed fields of a given characteristic are unique. Furthermore, quantifier elimination provided a precise description of definable relations on algebraically closed fields as algebraic varieties and of the definable relations on real-closed fields as semialgebraic sets

In the 1960s, the introduction of the ultraproduct construction led to new applications in algebra. This includes Ax's work on pseudofinite fields, proving that the theory of finite fields is decidable, and Ax and Kochen's proof of as special case of Artin's conjecture on diophantine equations, the Ax–Kochen theorem. The ultraproduct construction also led to Abraham Robinson's development of nonstandard analysis, which aims to provide a rigorous calculus of infinitesimals.

More recently, the connection between stability and the geometry of definable sets led to several applications from algebraic and diophantine geometry, including Ehud Hrushovski's 1996 proof of the geometric Mordell–Lang conjecture in all characteristics In 2001, similar methods were used to prove a generalisation of the Manin-Mumford conjecture. In 2011, Jonathan Pila applied techniques around o-minimality to prove the André–Oort conjecture for products of Modular curves.

In a separate strand of inquiries that also grew around stable theories, Laskowski showed in 1992 that NIP theories describe exactly those definable classes that are PAC-learnable in machine learning theory. This has led to several interactions between these separate areas. In 2018, the correspondence was extended as Hunter and Chase showed that stable theories correspond to online learnable classes.

## History

Model theory as a subject has existed since approximately the middle of the 20th century, and the term "theory of models" was coined by Alfred Tarski, a member of the Lwów–Warsaw school, in 1954. However some earlier research, especially in mathematical logic, is often regarded as being of a model-theoretical nature in retrospect. The first significant result in what is now model theory was a special case of the downward Löwenheim–Skolem theorem, published by Leopold Löwenheim in 1915. The compactness theorem was implicit in work by Thoralf Skolem, but it was first published in 1930, as a lemma in Kurt Gödel's proof of his completeness theorem. The Löwenheim–Skolem theorem and the compactness theorem received their respective general forms in 1936 and 1941 from Anatoly Maltsev. The development of model theory as an independent discipline was brought on by Alfred Tarski during the interbellum. Tarski's work included logical consequence, deductive systems, the algebra of logic, the theory of definability, and the semantic definition of truth, among other topics. His semantic methods culminated in the model theory he and a number of his Berkeley students developed in the 1950s and '60s.

In the further history of the discipline, different strands began to emerge, and the focus of the subject shifted. In the 1960s, techniques around ultraproducts became a popular tool in model theory. At the same time, researchers such as James Ax were investigating the first-order model theory of various algebraic classes, and others such as H. Jerome Keisler were extending the concepts and results of first-order model theory to other logical systems. Then, inspired by Morley's problem, Shelah developed stability theory. His work around stability changed the complexion of model theory, giving rise to a whole new class of concepts. This is known as the paradigm shift. Over the next decades, it became clear that the resulting stability hierarchy is closely connected to the geometry of sets that are definable in those models; this gave rise to the subdiscipline now known as geometric stability theory. An example of an influential proof from geometric model theory is Hrushovski's proof of the Mordell–Lang conjecture for function fields.

### Finite model theory

Finite model theory, which concentrates on finite structures, diverges significantly from the study of infinite structures in both the problems studied and the techniques used. In particular, many central results of classical model theory fail when restricted to finite structures. This includes the compactness theorem, Gödel's completeness theorem, and the method of ultraproducts for first-order logic. At the interface of finite and infinite model theory are algorithmic or computable model theory and the study of 0-1 laws, where the infinite models of a generic theory of a class of structures provide information on the distribution of finite models. Prominent application areas of FMT are descriptive complexity theory, database theory and formal language theory.

### Set theory

Any set theory (which is expressed in a countable language), if it is consistent, has a countable model; this is known as Skolem's paradox, since there are sentences in set theory which postulate the existence of uncountable sets and yet these sentences are true in our countable model. Particularly the proof of the independence of the continuum hypothesis requires considering sets in models which appear to be uncountable when viewed from *within* the model, but are countable to someone *outside* the model.

The model-theoretic viewpoint has been useful in set theory; for example in Kurt Gödel's work on the constructible universe, which, along with the method of forcing developed by Paul Cohen can be shown to prove the (again philosophically interesting) independence of the axiom of choice and the continuum hypothesis from the other axioms of set theory.

In the other direction, model theory is itself formalised within Zermelo–Fraenkel set theory. For instance, the development of the fundamentals of model theory (such as the compactness theorem) rely on the axiom of choice, and is in fact equivalent over Zermelo–Fraenkel set theory without choice to the Boolean prime ideal theorem. Other results in model theory depend on set-theoretic axioms beyond the standard ZFC framework. For example, if the Continuum Hypothesis holds then every countable model has an ultrapower which is saturated (in its own cardinality). Similarly, if the Generalized Continuum Hypothesis holds then every model has a saturated elementary extension. Neither of these results are provable in ZFC alone. Finally, some questions arising from model theory (such as compactness for infinitary logics) have been shown to be equivalent to large cardinal axioms.
