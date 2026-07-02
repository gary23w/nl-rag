---
title: "System F"
source: https://en.wikipedia.org/wiki/System_F-omega
domain: lambda-cube
license: CC-BY-SA-4.0
tags: lambda cube, pure type system, calculus of constructions, higher-order logic
fetched: 2026-07-02
---

# System F

(Redirected from

System F-omega

)

**System F** (also **polymorphic lambda calculus** or **second-order lambda calculus**) is a typed lambda calculus that introduces, to simply typed lambda calculus, a mechanism of universal quantification over types. System F formalizes parametric polymorphism in programming languages, thus forming a theoretical basis for languages such as Haskell and ML. It was discovered independently by logician Jean-Yves Girard (1972) and computer scientist John C. Reynolds.

Whereas simply typed lambda calculus has variables ranging over terms, and binders for them, System F additionally has variables ranging over *types*, and binders for them. As an example, the fact that the identity function can have any type of the form *A* → *A* would be formalized in System F as the statement

$\vdash \Lambda \alpha .\lambda x^{\alpha }.x:\forall \alpha .\alpha \to \alpha$

where $\alpha$ is a type variable. The upper-case $\Lambda$ is traditionally used to denote type-level functions, as opposed to the lower-case $\lambda$ which is used for value-level functions. (The superscripted $\alpha$ means that the bound variable *x* is of type $\alpha$ ; the expression after the colon is the type of the lambda expression preceding it.)

As a term rewriting system, System F is strongly normalizing. However, type inference in System F (without explicit type annotations) is undecidable. Under the Curry–Howard isomorphism, System F corresponds to second-order propositional intuitionistic logic. System F can be seen as part of the lambda cube, together with even more expressive typed lambda calculi, including those with dependent types.

According to Girard, the "F" in *System F* was picked by chance.

## Typing rules

The typing rules of System F are those of simply typed lambda calculus with the addition of the following:

| ${\displaystyle {\frac {\Gamma \vdash M:\forall \alpha .\sigma }{\Gamma \vdash M\tau$ (1) | ${\frac {\Gamma ,\alpha ~{\text{type}}\vdash M:\sigma }{\Gamma \vdash \Lambda \alpha .M:\forall \alpha .\sigma }}$ (2) |
|---|---|

where $\sigma ,\tau$ are types, $\alpha$ is a type variable, and $\alpha ~{\text{type}}$ in the context indicates that $\alpha$ is bound. The first rule is that of application, and the second is that of abstraction.

## Logic and predicates

The ${\mathsf {Boolean}}$ type is defined as: $\forall \alpha .\alpha \to \alpha \to \alpha$ , where $\alpha$ is a type variable. This means: ${\mathsf {Boolean}}$ is the type of all functions which take as input a type α and two expressions of type α, and produce as output an expression of type α (note that we consider $\to$ to be right-associative.)

The following two definitions for the Boolean values $\mathbf {T}$ and $\mathbf {F}$ are used, extending the definition of Church Booleans:

$\mathbf {T} =\Lambda \alpha {.}\lambda x^{\alpha }\lambda y^{\alpha }{.}x$

$\mathbf {F} =\Lambda \alpha {.}\lambda x^{\alpha }\lambda y^{\alpha }{.}y$

(Note that the above two functions require *three* — not two — arguments. The latter two should be lambda expressions, but the first one should be a type. This fact is reflected in the fact that the type of these expressions is $\forall \alpha .\alpha \to \alpha \to \alpha$ ; the universal quantifier binding the α corresponds to the Λ binding the alpha in the lambda expression itself. Also, note that ${\mathsf {Boolean}}$ is a convenient shorthand for $\forall \alpha .\alpha \to \alpha \to \alpha$ , but it is not a symbol of System F itself, but rather a "meta-symbol". Likewise, $\mathbf {T}$ and $\mathbf {F}$ are also "meta-symbols", convenient shorthands, of System F "assemblies" (in the Bourbaki sense); otherwise, if such functions could be named (within System F), then there would be no need for the lambda-expressive apparatus capable of defining functions anonymously and for the fixed-point combinator, which works around that restriction.)

Then, with these two $\lambda$ -terms, we can define some logic operators (which are of type ${\mathsf {Boolean}}\rightarrow {\mathsf {Boolean}}\rightarrow {\mathsf {Boolean}}$ ):

${\begin{aligned}\mathrm {AND} &=\lambda x^{\mathsf {Boolean}}\lambda y^{\mathsf {Boolean}}{.}x\,{\mathsf {Boolean}}\,y\,\mathbf {F} \\\mathrm {OR} &=\lambda x^{\mathsf {Boolean}}\lambda y^{\mathsf {Boolean}}{.}x\,{\mathsf {Boolean}}\,\mathbf {T} \,y\\\mathrm {NOT} &=\lambda x^{\mathsf {Boolean}}{.}x\,{\mathsf {Boolean}}\,\mathbf {F} \,\mathbf {T} \end{aligned}}$

Note that in the definitions above, ${\mathsf {Boolean}}$ is a type argument to x , specifying that the other two parameters that are given to x are of type ${\mathsf {Boolean}}$ . As in Church encodings, there is no need for an IFTHENELSE function as one can just use raw ${\mathsf {Boolean}}$ -typed terms as decision functions. However, if one is requested:

$\mathrm {IFTHENELSE} =\Lambda \alpha .\lambda x^{\mathsf {Boolean}}\lambda y^{\alpha }\lambda z^{\alpha }.x\alpha yz$

will do. A *predicate* is a function which returns a ${\mathsf {Boolean}}$ -typed value. The most fundamental predicate is ISZERO which returns $\mathbf {T}$ if and only if its argument is the Church numeral 0:

$\mathrm {ISZERO} =\lambda n^{\forall \alpha .(\alpha \rightarrow \alpha )\rightarrow \alpha \rightarrow \alpha }{.}n\,{\mathsf {Boolean}}\,(\lambda x^{\mathsf {Boolean}}{.}\mathbf {F} )\,\mathbf {T}$

Furthermore, the existential quantifier (and therefore existential types) can be implemented in system F by the following:

$\exists X.A=\forall Y.(\forall X.A\rightarrow Y)\rightarrow Y$

## System F structures

System F allows recursive constructions to be embedded in a natural manner, related to that in Martin-Löf's type theory. Abstract structures (S) are created using *constructors*. These are functions typed as:

$K_{1}\rightarrow K_{2}\rightarrow \dots \rightarrow S$

.

Recursivity is manifested when S itself appears within one of the types $K_{i}$ . If you have m of these constructors, you can define the type of S as:

$\forall \alpha .(K_{1}^{1}[\alpha /S]\rightarrow \dots \rightarrow \alpha )\dots \rightarrow (K_{1}^{m}[\alpha /S]\rightarrow \dots \rightarrow \alpha )\rightarrow \alpha$

For instance, the natural numbers can be defined as an inductive datatype N with constructors

${\begin{aligned}{\mathit {zero}}&:\mathrm {N} \\{\mathit {succ}}&:\mathrm {N} \rightarrow \mathrm {N} \end{aligned}}$

The System F type corresponding to this structure is $\forall \alpha .\alpha \to (\alpha \to \alpha )\to \alpha$ . The terms of this type comprise a typed version of the Church numerals, the first few of which are:

${\begin{aligned}0&:=\Lambda \alpha .\lambda x^{\alpha }.\lambda f^{\alpha \to \alpha }.x\\1&:=\Lambda \alpha .\lambda x^{\alpha }.\lambda f^{\alpha \to \alpha }.fx\\2&:=\Lambda \alpha .\lambda x^{\alpha }.\lambda f^{\alpha \to \alpha }.f(fx)\\3&:=\Lambda \alpha .\lambda x^{\alpha }.\lambda f^{\alpha \to \alpha }.f(f(fx))\end{aligned}}$

If we reverse the order of the curried arguments (*i.e.,* $\forall \alpha .(\alpha \rightarrow \alpha )\rightarrow \alpha \rightarrow \alpha$ ), then the Church numeral for n is a function that takes a function f as argument and returns the nth power of f. That is to say, a Church numeral is a higher-order function – it takes a single-argument function f, and returns another single-argument function.

## Use in programming languages

The version of System F used in this article is as an explicitly typed, or Church-style, calculus. The typing information contained in λ-terms makes type-checking straightforward. Joe Wells (1994) settled an "embarrassing open problem" by proving that type checking is undecidable for a Curry-style variant of System F, that is, one that lacks explicit typing annotations.

Wells's result implies that type inference for System F is impossible. A restriction of System F known as "Hindley–Milner", or simply "HM", does have an easy type inference algorithm and is used for many statically typed functional programming languages such as Haskell 98 and the ML family. Over time, as the restrictions of HM-style type systems have become apparent, languages have steadily moved to more expressive logics for their type systems. GHC, a Haskell compiler, goes beyond HM (as of 2008) and uses System F extended with non-syntactic type equality; non-HM features in OCaml's type system include GADT.

## The Girard–Reynolds isomorphism

In second-order intuitionistic logic, the second-order polymorphic lambda calculus (F2) was discovered by Girard (1972) and independently by Reynolds (1974). Girard proved the *representation theorem*: that in second-order intuitionistic predicate logic (P2), functions from the natural numbers to the natural numbers that can be proved total, form a projection from P2 into F2. Reynolds proved the *abstraction theorem*: that every term in F2 satisfies a logical relation, which can be embedded into the logical relations P2. Reynolds proved that a Girard projection followed by a Reynolds embedding form the identity, i.e., the **Girard–Reynolds isomorphism**.

## System Fω

While System F corresponds to the first axis of Barendregt's lambda cube, **System Fω** or the **higher-order polymorphic lambda calculus** combines the first axis (polymorphism) with the second axis (type operators); it is a different, more complex system.

System Fω can be defined inductively on a family of systems, where induction is based on the kinds permitted in each system:

- $F_{n}$ permits kinds:
  - $\star$ (the kind of types) and
  - $J\Rightarrow K$ where $J\in F_{n-1}$ and $K\in F_{n}$ (the kind of functions from types to types, where the argument type is of a lower order)

In the limit, we can define system $F_{\omega }$ to be

- $F_{\omega }={\underset {1\leq i}{\bigcup }}F_{i}$

That is, Fω is the system which allows functions from types to types where the argument (and result) may be of any order.

Note that although Fω places no restrictions on the *order* of the arguments in these mappings, it does restrict the *universe* of the arguments for these mappings: they must be types rather than values. System Fω does not permit mappings from values to types (dependent types), though it does permit mappings from values to values ( $\lambda$ abstraction), mappings from types to values ( $\Lambda$ abstraction), and mappings from types to types ( $\lambda$ abstraction at the level of types).

## System F<:

**System F<:**, pronounced "F-sub", is an extension of system F with subtyping. System F<: has been of central importance to programming language theory since the 1980s because the core of functional programming languages, like those in the ML family, support both parametric polymorphism and record subtyping, which can be expressed in **System F<:**.
