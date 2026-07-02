---
title: "Simply typed lambda calculus"
source: https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus
domain: simply-typed-lambda
license: CC-BY-SA-4.0
tags: simply typed lambda calculus, typing rule, type judgment, strong normalization
fetched: 2026-07-02
---

# Simply typed lambda calculus

The **simply typed lambda calculus** (⁠ $\lambda ^{\to }$ ⁠), a form of type theory, is a typed interpretation of the lambda calculus with only one type constructor (⁠ $\to$ ⁠) that builds function types. It is the canonical and simplest example of a typed lambda calculus. The simply typed lambda calculus was originally introduced by Alonzo Church in 1940 as an attempt to avoid paradoxical use of the untyped lambda calculus.

The term *simple type* is also used to refer to extensions of the simply typed lambda calculus with constructs such as products, coproducts or natural numbers (System T) or even full recursion (like PCF). In contrast, systems that introduce polymorphic types (like System F) or dependent types (like the Logical Framework) are not considered *simply typed*. The simple types, except for full recursion, are still considered *simple* because the Church encodings of such structures can be done using only $\to$ and suitable type variables, while polymorphism and dependency cannot.

## Syntax

In the 1930s Alonzo Church sought to use *the logistic method*: his lambda calculus, as a formal language based on symbolic expressions, consisted of a denumerably infinite series of axioms and variables, but also a finite set of primitive symbols, denoting abstraction and scope, as well as four constants: negation, disjunction, universal quantification, and selection respectively; and also, a finite set of rules I to VI. This finite set of rules included rule V *modus ponens* as well as IV and VI for substitution and generalization respectively. Rules I to III are known as alpha, beta, and eta conversion in the lambda calculus. Church sought to use English only as a syntax language (that is, a metamathematical language) for describing symbolic expressions with no interpretations.

In 1940 Church settled on a subscript notation for denoting the type in a symbolic expression. In his presentation, Church used only two base types: o for "the type of propositions" and $\iota$ for "the type of individuals". The type o has no term constants, whereas $\iota$ has one term constant. Frequently the calculus with only one base type, usually ⁠ o ⁠, is considered. The Greek letter subscripts ⁠ $\alpha$ ⁠, ⁠ $\beta$ ⁠, etc. denote type variables; the parenthesized subscripted $(\alpha \beta )$ denotes the function type ⁠ $\beta \to \alpha$ ⁠. Church 1940 p.58 used 'arrow or ⁠ $\to$ ⁠' to denote *stands for*, or *is an abbreviation for*. By the 1970s stand-alone arrow notation was in use; for example in this article non-subscripted symbols $\sigma$ and $\tau$ can range over types. The infinite number of axioms were then seen to be a consequence of applying rules I to VI to the types (see Peano axioms). Informally, the *function type* $\sigma \to \tau$ refers to the type of functions that, given an input of type ⁠ $\sigma$ ⁠, produce an output of type ⁠ $\tau$ ⁠. By convention, $\to$ associates to the right: $\sigma \to \tau \to \rho$ is read as ⁠ $\sigma \to (\tau \to \rho )$ ⁠.

To define the types, a set of *base types*, ⁠ B ⁠, must first be defined. These are sometimes called *atomic types* or *type constants*. With this fixed, the syntax of types is:

$\tau \;{{:}{:=}}\;\tau \to \tau \mid T\quad \mathrm {where} \quad T\in B.$

For example, ⁠ $B=\{a,b\}$ ⁠, generates an infinite set of types starting with ⁠ a ⁠, ⁠ b ⁠, ⁠ $a\to a$ ⁠, ⁠ $a\to b$ ⁠, ⁠ $b\to b$ ⁠, ⁠ $b\to a$ ⁠, ⁠ $a\to (a\to a)$ ⁠, ..., ⁠ $(b\to a)\to (a\to b)$ ⁠, ...

A set of *term constants* is also fixed for the base types. For example, it might be assumed that one of the base types is nat, and its term constants could be the natural numbers.

The syntax of the simply typed lambda calculus is essentially that of the lambda calculus itself. The term $x{\mathbin {:}}\tau$ denotes that the variable x is of type ⁠ $\tau$ ⁠. The term syntax, in Backus–Naur form, is *variable reference*, *abstractions*, *application*, or *constant*:

$e\;{{:}{:=}}\;x\mid \lambda x\mathbin {:} \tau .e\mid e\,e\mid c$

where c is a term constant. A variable reference x is *bound* if it is inside of an abstraction binding ⁠ x ⁠. A term is *closed* if there are no unbound variables.

In comparison, the syntax of untyped lambda calculus has no such typing or term constants:

$e\;{{:}{:=}}\;x\mid \lambda x.e\mid e\,e$

Whereas in typed lambda calculus every *abstraction* (i.e. function) must specify the type of its argument.

## Typing rules

To define the set of well-typed lambda terms of a given type, one defines a typing relation between terms and types. First, one introduces *typing contexts*, or *typing environments* $\Gamma ,\Delta ,\dots$ , which are sets of typing assumptions. A *typing assumption* has the form ⁠ $x{\mathbin {:}}\sigma$ ⁠, meaning variable x has type ⁠ $\sigma$ ⁠.

The *typing relation* $\Gamma \vdash e{\mathbin {:}}\sigma$ indicates that e is a term of type $\sigma$ in context ⁠ $\Gamma$ ⁠. In this case e is said to be *well-typed* (having type ⁠ $\sigma$ ⁠). Instances of the typing relation are called *typing judgments*. The validity of a typing judgment is shown by providing a *typing derivation*, constructed using typing rules (wherein the premises above the line allow us to derive the conclusion below the line). Simply typed lambda calculus uses these rules:

| ${\frac {x{\mathbin {:}}\sigma \in \Gamma }{\Gamma \vdash x{\mathbin {:}}\sigma }}$ (1) | ${\frac {c{\text{ is a constant of type }}T}{\Gamma \vdash c{\mathbin {:}}T}}$ (2) |
|---|---|
| ${\frac {\Gamma ,x{\mathbin {:}}\sigma \vdash e{\mathbin {:}}\tau }{\Gamma \vdash (\lambda x{\mathbin {:}}\sigma .~e){\mathbin {:}}(\sigma \to \tau )}}$ (3) | ${\frac {\Gamma \vdash e_{1}{\mathbin {:}}\sigma \to \tau \quad \Gamma \vdash e_{2}{\mathbin {:}}\sigma }{\Gamma \vdash e_{1}~e_{2}{\mathbin {:}}\tau }}$ (4) |

In words,

1. If x has type $\sigma$ in the context, then x has type ⁠ $\sigma$ ⁠.
2. Term constants have the appropriate base types.
3. If, in a certain context with x having type ⁠ $\sigma$ ⁠, e has type ⁠ $\tau$ ⁠, then, in the same context without ⁠ x ⁠, ⁠ $\lambda x{\mathbin {:}}\sigma .~e$ ⁠ has type ⁠ $\sigma \to \tau$ ⁠.
4. If, in a certain context, $e_{1}$ has type ⁠ $\sigma \to \tau$ ⁠, and $e_{2}$ has type ⁠ $\sigma$ ⁠, then $e_{1}~e_{2}$ has type ⁠ $\tau$ ⁠.

Examples of closed terms, i.e. terms typable in the empty context, are:

- For every type ⁠ $\tau$ ⁠, a term $\lambda x{\mathbin {:}}\tau .x{\mathbin {:}}\tau \to \tau$ (identity function/I-combinator),
- For types ⁠ $\sigma ,\tau$ ⁠, a term $\lambda x{\mathbin {:}}\sigma .\lambda y{\mathbin {:}}\tau .x{\mathbin {:}}\sigma \to \tau \to \sigma$ (the K-combinator), and
- For types ⁠ $\tau ,\tau ',\tau ''$ ⁠, a term $\lambda x{\mathbin {:}}\tau \to \tau '\to \tau ''.\lambda y{\mathbin {:}}\tau \to \tau '.\lambda z{\mathbin {:}}\tau .xz(yz):(\tau \to \tau '\to \tau '')\to (\tau \to \tau ')\to \tau \to \tau ''$ (the S-combinator).

These are the typed lambda calculus representations of the basic combinators of combinatory logic.

Each type $\tau$ is assigned an order, a number ⁠ $o(\tau )$ ⁠. For base types, ⁠ $o(T)=0$ ⁠; for function types, ⁠ $o(\sigma \to \tau )={\mbox{max}}(o(\sigma )+1,o(\tau ))$ ⁠. That is, the order of a type measures the depth of the most left-nested arrow. Hence:

$o(\iota \to \iota \to \iota )=1$

$o((\iota \to \iota )\to \iota )=2$

## Semantics

### Intrinsic vs. extrinsic interpretations

Broadly speaking, there are two different ways of assigning meaning to the simply typed lambda calculus, as to typed languages more generally, variously called intrinsic vs. extrinsic, ontological vs. semantical, or Church-style vs. Curry-style. An intrinsic semantics only assigns meaning to well-typed terms, or more precisely, assigns meaning directly to typing derivations. This has the effect that terms differing only by type annotations can nonetheless be assigned different meanings. For example, the identity term $\lambda x{\mathbin {:}}{\mathtt {int}}.~x$ on integers and the identity term $\lambda x{\mathbin {:}}{\mathtt {bool}}.~x$ on Booleans may mean different things. (The classic intended interpretations are the identity function on integers and the identity function on Boolean values.) In contrast, an extrinsic semantics assigns meaning to terms regardless of typing, as they would be interpreted in an untyped language. In this view, $\lambda x{\mathbin {:}}{\mathtt {int}}.~x$ and $\lambda x{\mathbin {:}}{\mathtt {bool}}.~x$ mean the same thing (i.e., the same thing as ⁠ $\lambda x.~x$ ⁠).

The distinction between intrinsic and extrinsic semantics is sometimes associated with the presence or absence of annotations on lambda abstractions, but strictly speaking this usage is imprecise. It is possible to define an extrinsic semantics on annotated terms simply by ignoring the types (i.e., through type erasure), as it is possible to give an intrinsic semantics on unannotated terms when the types can be deduced from context (i.e., through type inference). The essential difference between intrinsic and extrinsic approaches is just whether the typing rules are viewed as defining the language, or as a formalism for verifying properties of a more primitive underlying language. Most of the different semantic interpretations discussed below can be seen through either an intrinsic or extrinsic perspective.

### Equational theory

The simply typed lambda calculus (STLC) has the same equational theory of βη-equivalence as untyped lambda calculus, but subject to type restrictions. The equation for beta reduction

$(\lambda x{\mathbin {:}}\sigma .~t)\,u=_{\beta }t[x:=u]$

holds in context $\Gamma$ whenever $\Gamma ,x{\mathbin {:}}\sigma \vdash t{\mathbin {:}}\tau$ and ⁠ $\Gamma \vdash u{\mathbin {:}}\sigma$ ⁠, while the equation for eta reduction

$\lambda x{\mathbin {:}}\sigma .~t\,x=_{\eta }t$

holds whenever $\Gamma \vdash t{:}\sigma \to \tau$ and x does not appear free in ⁠ t ⁠. The advantage of typed lambda calculus is that STLC allows potentially nonterminating computations to be cut short (that is, *reduced*).

### Operational semantics

Likewise, the operational semantics of simply typed lambda calculus can be fixed as for the untyped lambda calculus, using call by name, call by value, or other evaluation strategies. As for any typed language, type safety is a fundamental property of all of these evaluation strategies. Additionally, the strong normalization property described below implies that any evaluation strategy will terminate on all simply typed terms.

### Categorical semantics

The simply typed lambda calculus enriched with product types, pairing and projection operators (with $\beta \eta$ -equivalence) is the internal language of Cartesian closed categories (CCCs), as was first observed by Joachim Lambek. Given any CCC, the basic types of the corresponding lambda calculus are the objects, and the terms are the morphisms. Conversely, the simply typed lambda calculus with product types and pairing operators over a collection of base types and given terms forms a CCC whose objects are the types, and morphisms are equivalence classes of terms.

There are typing rules for *pairing*, *projection*, and a *unit term*. Given two terms $s{\mathbin {:}}\sigma$ and ⁠ $t{\mathbin {:}}\tau$ ⁠, the term $(s,t)$ has type ⁠ $\sigma \times \tau$ ⁠. Likewise, if one has a term ⁠ $u{\mathbin {:}}\tau _{1}\times \tau _{2}$ ⁠, then there are terms $\pi _{1}(u){\mathbin {:}}\tau _{1}$ and $\pi _{2}(u){\mathbin {:}}\tau _{2}$ where the $\pi _{i}$ correspond to the projections of the Cartesian product. The *unit term*, of type 1, written as $()$ and vocalized as 'nil', is the final object. The equational theory is extended likewise, so that one has

$\pi _{1}(s{\mathbin {:}}\sigma ,t{\mathbin {:}}\tau )=s{\mathbin {:}}\sigma$

$\pi _{2}(s{\mathbin {:}}\sigma ,t{\mathbin {:}}\tau )=t{\mathbin {:}}\tau$

$(\pi _{1}(u{\mathbin {:}}\sigma \times \tau ),\pi _{2}(u{\mathbin {:}}\sigma \times \tau ))=u{\mathbin {:}}\sigma \times \tau$

$t{\mathbin {:}}1=()$

This last is read as "*if t has type 1, then it reduces to nil*".

The above can then be turned into a category by taking the types as the objects. The morphisms $\sigma \to \tau$ are equivalence classes of pairs $(x{\mathbin {:}}\sigma ,t{\mathbin {:}}\tau )$ where *x* is a variable (of type ⁠ $\sigma$ ⁠) and *t* is a term (of type ⁠ $\tau$ ⁠), having no free variables in it, except for (optionally) *x*. The set of terms in the language is the closure of this set of terms under the operations of abstraction and application.

This correspondence can be extended to include "language homomorphisms" and functors between the category of Cartesian closed categories, and the category of simply typed lambda theories.

Part of this correspondence can be extended to closed symmetric monoidal categories by using a linear type system.

### Proof-theoretic semantics

The simply typed lambda calculus is closely related to the implicational fragment of propositional intuitionistic logic, i.e., the implicational propositional calculus, via the Curry–Howard isomorphism: terms correspond precisely to proofs in natural deduction, and inhabited types are exactly the tautologies of this logic.

From his logistic method Church 1940 p.58 laid out an axiom schema, p. 60, which Henkin 1949 filled in with type domains (e.g. the natural numbers, the real numbers, etc.). Henkin 1996 p. 146 described how Church's logistic method could seek to provide a foundation for mathematics (Peano arithmetic and real analysis), via model theory.

## Alternative syntaxes

The presentation given above is not the only way of defining the syntax of the simply typed lambda calculus.

### Type Erasure

One alternative is to remove type annotations entirely (so that the syntax is identical to the untyped lambda calculus), while ensuring that terms are well-typed via Hindley–Milner type inference. The inference algorithm is terminating, sound, and complete: whenever a term is typable, the algorithm computes its type. More precisely, it computes the term's principal type, since often an unannotated term (such as ⁠ $\lambda x.~x$ ⁠) may have more than one type (⁠ ${\mathtt {int}}\to {\mathtt {int}}$ ⁠, ⁠ ${\mathtt {bool}}\to {\mathtt {bool}}$ ⁠, etc., which are all instances of the principal type ⁠ $\alpha \to \alpha$ ⁠).

### Bidirectional Type Checking

Another alternative presentation of simply typed lambda calculus is based on **bidirectional type checking**, which requires more type annotations than Hindley–Milner inference but is easier to describe. The type system is divided into two judgments, representing both *checking* and *synthesis*, written $\Gamma \vdash e\Leftarrow \tau$ and $\Gamma \vdash e\Rightarrow \tau$ respectively. Operationally, the three components ⁠ $\Gamma$ ⁠, ⁠ e ⁠, and $\tau$ are all *inputs* to the checking judgment ⁠ $\Gamma \vdash e\Leftarrow \tau$ ⁠, whereas the synthesis judgment $\Gamma \vdash e\Rightarrow \tau$ only takes $\Gamma$ and e as inputs, producing the type $\tau$ as output. These judgments are derived via the following rules:

| ${\frac {x{\mathbin {:}}\sigma \in \Gamma }{\Gamma \vdash x\Rightarrow \sigma }}$ [1] | ${\frac {c{\text{ is a constant of type }}T}{\Gamma \vdash c\Rightarrow T}}$ [2] |
|---|---|
| ${\frac {\Gamma ,x{\mathbin {:}}\sigma \vdash e\Leftarrow \tau }{\Gamma \vdash \lambda x.~e\Leftarrow \sigma \to \tau }}$ [3] | ${\frac {\Gamma \vdash e_{1}\Rightarrow \sigma \to \tau \quad \Gamma \vdash e_{2}\Leftarrow \sigma }{\Gamma \vdash e_{1}~e_{2}\Rightarrow \tau }}$ [4] |
| ${\frac {\Gamma \vdash e\Rightarrow \tau }{\Gamma \vdash e\Leftarrow \tau }}$ [5] | ${\frac {\Gamma \vdash e\Leftarrow \tau }{\Gamma \vdash (e{\mathbin {:}}\tau )\Rightarrow \tau }}$ [6] |

Observe that rules [1]–[4] are nearly identical to rules (1)–(4) above, except for the careful choice of checking or synthesis judgments. These choices can be explained like so:

1. If $x{\mathbin {:}}\sigma$ is in the context, we can synthesize type $\sigma$ for ⁠ x ⁠.
2. The types of term constants are fixed and can be synthesized.
3. To check that $\lambda x.~e$ has type $\sigma \to \tau$ in some context, we extend the context with $x{\mathbin {:}}\sigma$ and check that e has type ⁠ $\tau$ ⁠.
4. If $e_{1}$ synthesizes type $\sigma \to \tau$ (in some context), and $e_{2}$ checks against type $\sigma$ (in the same context), then $e_{1}~e_{2}$ synthesizes type ⁠ $\tau$ ⁠.

Observe that the rules for synthesis are read top-to-bottom, whereas the rules for checking are read bottom-to-top. Note in particular that we do **not** need any annotation on the lambda abstraction in rule [3], because the type of the bound variable can be deduced from the type at which we check the function. Finally, we explain rules [5] and [6] as follows:

1. To check that e has type ⁠ $\tau$ ⁠, it suffices to synthesize type ⁠ $\tau$ ⁠.
2. If e checks against type ⁠ $\tau$ ⁠, then the explicitly annotated term $(e{\mathbin {:}}\tau )$ synthesizes ⁠ $\tau$ ⁠.

Because of these last two rules coercing between synthesis and checking, it is easy to see that any well-typed but unannotated term can be checked in the bidirectional system, so long as we insert "enough" type annotations. And in fact, annotations are needed only at β-redexes.

## General observations

Given the standard semantics, the simply typed lambda calculus is strongly normalizing: every sequence of reductions eventually terminates. This is because recursion is not allowed by the typing rules: it is impossible to find types for fixed-point combinators and the looping term ⁠ $\Omega =(\lambda x.~x~x)(\lambda x.~x~x)$ ⁠. Recursion can be added to the language by either having a special operator ${\mathtt {fix}}_{\alpha }$ of type $(\alpha \to \alpha )\to \alpha$ or adding general recursive types, though both eliminate strong normalization.

Unlike the untyped lambda calculus, the simply typed lambda calculus is not Turing complete. All programs in the simply typed lambda calculus halt. For the untyped lambda calculus, there are programs that do not halt, and moreover there is no general decision procedure that can determine whether a program halts.

## Important results

- Tait showed in 1967 that $\beta$ -reduction is strongly normalizing. As a corollary $\beta \eta$ -equivalence is decidable. Statman showed in 1979 that the normalisation problem is non-elementary, a proof that was later simplified by Mairson. The problem is known to be in the set ${\mathcal {E}}^{4}$ of the Grzegorczyk hierarchy, and more precisely, it is complete in the complexity class called **TOWER**. A purely semantic normalisation proof (see normalisation by evaluation) was given by Berger and Schwichtenberg in 1991.
- The unification problem for $\beta \eta$ -equivalence is undecidable. Huet showed in 1973 that 3rd order unification is undecidable and this was improved upon by Baxter in 1978 then by Goldfarb in 1981 by showing that 2nd order unification is already undecidable. A proof that higher order matching (unification where only one term contains existential variables) is decidable was announced by Colin Stirling in 2006, and a full proof was published in 2009.
- We can encode natural numbers by terms of the type $(o\to o)\to (o\to o)$ (Church numerals). Schwichtenberg showed in 1975 that in $\lambda ^{\to }$ exactly the extended polynomials are representable as functions over Church numerals; these are roughly the polynomials closed up under a conditional operator.
- A *full model* of $\lambda ^{\to }$ is given by interpreting base types as sets and function types by the set-theoretic function space. Friedman showed in 1975 that this interpretation is complete for $\beta \eta$ -equivalence, if the base types are interpreted by infinite sets. Statman showed in 1983 that $\beta \eta$ -equivalence is the maximal equivalence that is *typically ambiguous*, i.e. closed under type substitutions (*Statman's Typical Ambiguity Theorem*). A corollary of this is that the *finite model property* holds, i.e. finite sets are sufficient to distinguish terms that are not identified by $\beta \eta$ -equivalence.
- Plotkin introduced logical relations in 1973 to characterize the elements of a model that are definable by lambda terms. In 1993 Jung and Tiuryn showed that a general form of logical relation (Kripke logical relations with varying arity) exactly characterizes lambda definability. Plotkin and Statman conjectured that it is decidable whether a given element of a model generated from finite sets is definable by a lambda term (*Plotkin–Statman conjecture*). The conjecture was shown to be false by Loader in 2001.
