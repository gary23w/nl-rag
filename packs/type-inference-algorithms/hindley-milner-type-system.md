---
title: "Hindley–Milner type system"
source: https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system
domain: type-inference-algorithms
license: CC-BY-SA-4.0
tags: type inference, algorithm W, constraint-based type inference, principal type
fetched: 2026-07-02
---

# Hindley–Milner type system

A **Hindley–Milner** (**HM**) **type system** is a classical type system for the lambda calculus with parametric polymorphism. It is also known as **Damas–Milner** or **Damas–Hindley–Milner**. It was first described by J. Roger Hindley and later rediscovered by Robin Milner. Luis Damas contributed a close formal analysis and proof of the method in his PhD thesis.

Among HM's more notable properties are its completeness and its ability to infer the most general type of a given program without programmer-supplied type annotations or other hints. Algorithm W is an efficient type inference method in practice and has been successfully applied on large code bases, although it has a high theoretical complexity. HM is preferably used for functional programming languages. It was first implemented as part of the type system of the programming language ML. Since then, HM has been extended in various ways, most notably with type class constraints like those in Haskell.

## Introduction

As a type inference method, Hindley–Milner is able to deduce the types of variables, expressions and functions from programs written in an entirely untyped style. Being scope sensitive, it is not limited to deriving the types only from a small portion of source code, but rather from complete programs or modules. Being able to cope with parametric types, too, it is core to the type systems of many functional programming languages. It was first applied in this manner in the ML programming language.

The origin is the type inference algorithm for the simply typed lambda calculus that was devised by Haskell Curry and Robert Feys in 1958. In 1969, J. Roger Hindley extended this work and proved that their algorithm always inferred the most general type. In 1978, Robin Milner, independently of Hindley's work, provided an equivalent algorithm, Algorithm W. In 1982, Luis Damas finally proved that Milner's algorithm is complete and extended it to support systems with polymorphic references.

### Monomorphism vs. polymorphism

In the simply typed lambda calculus, types T are either atomic type constants or function types of form $T\rightarrow T$ . Such types are *monomorphic*. Typical examples are the types used in arithmetic values:

${\begin{array}{ll}3&:{\mathtt {Number}}\\{\mathtt {add}}\ 3\ 4&:{\mathtt {Number}}\\{\mathtt {add}}&:{\mathtt {Number}}\rightarrow {\mathtt {Number}}\rightarrow {\mathtt {Number}}\end{array}}$

Contrary to this, the untyped lambda calculus is neutral to typing at all, and many of its functions can be meaningfully applied to all type of arguments. The trivial example is the identity function

${\mathtt {id}}\equiv \lambda x.x$

which simply returns whatever value it is applied to. Less trivial examples include parametric types like lists.

While polymorphism in general means that operations accept values of more than one type, the polymorphism used here is parametric. One finds the notation of *type schemes* in the literature, too, emphasizing the parametric nature of the polymorphism. Additionally, constants may be typed with (quantified) type variables. For example, the following type schemes quantify universally over $\alpha$ , meaning that they are true for all possible $\alpha$ :

${\begin{array}{ll}{\mathtt {cons}}&:\forall \alpha .\alpha \rightarrow {\mathtt {List}}\ \alpha \rightarrow {\mathtt {List}}\ \alpha \\{\mathtt {nil}}&:\forall \alpha .{\mathtt {List}}\ \alpha \\{\mathtt {id}}&:\forall \alpha .\alpha \rightarrow \alpha \end{array}}$

Polymorphic types can become monomorphic by consistent substitution of their variables. Examples of monomorphic *instances* are:

${\begin{array}{ll}{\mathtt {id}}'&:{\mathtt {String}}\rightarrow {\mathtt {String}}\\{\mathtt {nil}}'&:{\mathtt {List}}\ {\mathtt {Number}}\end{array}}$

More generally, types are polymorphic when they contain type variables, while types without them are monomorphic.

Contrary to the type systems used for example in Pascal (1970) or C (1972), which only support monomorphic types, HM is designed with emphasis on parametric polymorphism. The successors of the languages mentioned, like C++ (1985), focused on different types of polymorphism, namely subtyping in connection with object-oriented programming and overloading. While subtyping is incompatible with HM, a variant of systematic overloading is available in the HM-based type system of Haskell.

### Let-polymorphism

When extending the type inference for the simply-typed lambda calculus towards polymorphism, one has to decide whether assigning a polymorphic type not only as type of an expression, but also as the type of a λ-bound variable is admissible. This would allow the generic identity type to be assigned to the variable 'id' in:

```
 (λ id .  ... (id 3) ... (id "text") ... ) (λ x . x)
```

Allowing this gives rise to the polymorphic lambda calculus; however, type inference in this system is not decidable. Instead, HM distinguishes variables that are immediately bound to an expression from more general λ-bound variables, calling the former let-bound variables, and allows polymorphic types to be assigned only to these. This leads to *let-polymorphism* where the above example takes the form

```
 let id = λ x . x
  in ... (id 3) ... (id "text") ...
```

which can be typed with a polymorphic type for 'id'. As indicated, the expression syntax is extended to make the let-bound variables explicit, and by restricting the type system to allow only let-bound variable to have polymorphic types, while the parameters in lambda-abstractions must get a monomorphic type, type inference becomes decidable.

## Overview

The remainder of this article proceeds as follows:

- The HM type system is defined. This is done by describing a deduction system that makes precise what expressions have what type, if any.
- From there, it works towards an implementation of the type inference method. After introducing a syntax-driven variant of the above deductive system, it sketches an efficient implementation (algorithm J), appealing mostly to the reader's metalogical intuition.
- Because it remains open whether algorithm J indeed realises the initial deduction system, a less efficient implementation (algorithm W), is introduced and its use in a proof is hinted.
- Finally, further topics related to the algorithm are discussed.

The same description of the deduction system is used throughout, even for the two algorithms, to make the various forms in which the HM method is presented directly comparable.

## The Hindley–Milner type system

The type system can be formally described by syntax rules that fix a language for the expressions, types, etc. The presentation here of such a syntax is not too formal, in that it is written down not to study the surface grammar, but rather the depth grammar, and leaves some syntactical details open. This form of presentation is usual. Building on this, typing rules are used to define how expressions and types are related. As before, the form used is a bit liberal.

### Syntax

The expressions to be typed are exactly those of the lambda calculus extended with a let-expression as shown in the adjacent table. Parentheses can be used to disambiguate an expression. The application is left-binding and binds stronger than abstraction or the let-in construct.

Types are syntactically split into two groups, monotypes and polytypes.

#### Monotypes

Monotypes always designate a particular type. Monotypes $\tau$ are syntactically represented as terms.

Examples of monotypes include type constants like ${\mathtt {int}}$ or ${\mathtt {string}}$ , and parametric types like ${\mathtt {Map\ (Set\ string)\ int}}$ . The latter types are examples of *applications* of type functions, for example, from the set $\{{\mathtt {Map^{2},\ Set^{1},\ string^{0},\ int^{0}}},\ \rightarrow ^{2}\}$ , where the superscript indicates the number of type parameters. The complete set of type functions C is arbitrary in HM, except that it *must* contain at least $\rightarrow ^{2}$ , the type of functions. It is often written in infix notation for convenience. For example, a function mapping integers to strings has type ${\mathtt {int}}\rightarrow {\mathtt {string}}$ . Again, parentheses can be used to disambiguate a type expression. The application binds stronger than the infix arrow, which is right-binding.

Type variables are admitted as monotypes. Monotypes are not to be confused with monomorphic types, which exclude variables and allow only ground terms.

Two monotypes are equal if they have identical terms.

#### Polytypes

*Polytypes* (or *type schemes*) are types containing variables bound by zero or more for-all quantifiers, e.g. $\forall \alpha .\alpha \rightarrow \alpha$ .

A function with polytype $\forall \alpha .\alpha \rightarrow \alpha$ can map *any* value of the same type to itself, and the identity function is a value for this type.

As another example, $\forall \alpha .({\mathtt {Set}}\ \alpha )\rightarrow {\mathtt {int}}$ is the type of a function mapping all finite sets to integers. A function which returns the cardinality of a set would be a value of this type.

Quantifiers can only appear top level. For instance, a type $\forall \alpha .\alpha \rightarrow \forall \alpha .\alpha$ is excluded by the syntax of types. Also monotypes are included in the polytypes, thus a type has the general form $\forall \alpha _{1}\dots \forall \alpha _{n}.\tau$ , where $n\geq 0$ and $\tau$ is a monotype.

Equality of polytypes is up to reordering the quantification and renaming the quantified variables ( $\alpha$ -conversion). Further, quantified variables not occurring in the monotype can be dropped.

#### Context and typing

To meaningfully bring together the still disjoint parts (syntax expressions and types) a third part is needed: context. Syntactically, a context is a list of pairs $x:\sigma$ , called assignments, assumptions or bindings, each pair stating that value variable $x_{i}$ has type $\sigma _{i}.$ All three parts combined give a *typing judgment* of the form $\Gamma \ \vdash \ e:\sigma$ , stating that under assumptions $\Gamma$ , the expression e has type $\sigma$ .

#### Free type variables

In a type $\forall \alpha _{1}\dots \forall \alpha _{n}.\tau$ , the symbol $\forall$ is the quantifier binding the type variables $\alpha _{i}$ in the monotype $\tau$ . The variables $\alpha _{i}$ are called *quantified* and any occurrence of a quantified type variable in $\tau$ is called *bound* and all unbound type variables in $\tau$ are called *free*. Additionally to the quantification $\forall$ in polytypes, type variables can also be bound by occurring in the context, but with the inverse effect on the right hand side of the $\vdash$ . Such variables then behave like type constants there. Finally, a type variable may legally occur unbound in a typing, in which case they are implicitly all-quantified.

The presence of both bound and unbound type variables is a bit uncommon in programming languages. Often, all type variables are implicitly treated all-quantified. For instance, one does not have clauses with free variables in Prolog. Likewise in Haskell, where all type variables implicitly occur quantified, i.e. a Haskell type `a -> a` means $\forall \alpha .\alpha \rightarrow \alpha$ here. Related and also very uncommon is the binding effect of the right hand side $\sigma$ of the assignments.

Typically, the mixture of both bound and unbound type variables originate from the use of free variables in an expression. The constant function **K** = $\lambda x.\lambda y.x$ provides an example. It has the monotype $\alpha \rightarrow \beta \rightarrow \alpha$ . One can force polymorphism by $\mathbf {let} \ k=\lambda x.(\mathbf {let} \ f=\lambda y.x\ \mathbf {in} \ f)\ \mathbf {in} \ k$ . Herein, f has the type $\forall \gamma .\gamma \rightarrow \alpha$ . The free monotype variable $\alpha$ originates from the type of the variable x bound in the surrounding scope. k has the type $\forall \alpha \forall \beta .\alpha \rightarrow \beta \rightarrow \alpha$ . One could imagine the free type variable $\alpha$ in the type of f be bound by the $\forall \alpha$ in the type of k . But such a scoping cannot be expressed in HM. Rather, the binding is realized by the context.

### Type order

Polymorphism means that one and the same expression can have (perhaps infinitely) many types. But in this type system, these types are not completely unrelated, but rather orchestrated by the parametric polymorphism.

As an example, the identity $\lambda x.x$ can have $\forall \alpha .\alpha \rightarrow \alpha$ as its type as well as ${\texttt {string}}\rightarrow {\texttt {string}}$ or ${\texttt {int}}\rightarrow {\texttt {int}}$ and many others, but not ${\texttt {int}}\rightarrow {\texttt {string}}$ . The most general type for this function is $\forall \alpha .\alpha \rightarrow \alpha$ , while the others are more specific and can be derived from the general one by consistently replacing another type for the *type parameter*, i.e. the quantified variable $\alpha$ . The counter-example fails because the replacement is not consistent.

The consistent replacement can be made formal by applying a substitution $S=\left\{\ a_{i}\mapsto \tau _{i},\ \dots \ \right\}$ to the term of a type $\tau$ , written $S\tau$ . As the example suggests, substitution is not only strongly related to an order, that expresses that a type is more or less special, but also with the all-quantification which allows the substitution to be applied.

Formally, in HM, a type $\sigma '$ is more general than $\sigma$ , formally $\sigma '\sqsubseteq \sigma$ , if some quantified variable in $\sigma '$ is consistently substituted such that one gains $\sigma$ as shown in the side bar. This order is part of the type definition of the type system.

In our previous example, applying the substitution $S=\left\{\alpha \mapsto {\texttt {string}}\right\}$ would result in $\forall \alpha .\alpha \rightarrow \alpha \sqsubseteq {\texttt {string}}\rightarrow {\texttt {string}}$ .

While substituting a monomorphic (ground) type for a quantified variable is straight forward, substituting a polytype has some pitfalls caused by the presence of free variables. Most particularly, unbound variables must not be replaced. They are treated as constants here. Additionally, quantifications can only occur top-level. Substituting a parametric type, one has to lift its quantifiers. The table on the right makes the rule precise.

Alternatively, consider an equivalent notation for the polytypes without quantifiers in which quantified variables are represented by a different set of symbols. In such a notation, the specialization reduces to plain consistent replacement of such variables.

The relation $\sqsubseteq$ is a partial order and $\forall \alpha .\alpha$ is its smallest element.

#### Principal type

While specialization of a type scheme is one use of the order, it plays a crucial second role in the type system. Type inference with polymorphism faces the challenge of summarizing all possible types an expression may have. The order guarantees that such a summary exists as the most general type of the expression.

#### Substitution in typings

The type order defined above can be extended to typings because the implied all-quantification of typings enables consistent replacement:

$\Gamma \vdash e:\sigma \quad \Longrightarrow \quad S\Gamma \vdash e:S\sigma$

Contrary to the specialisation rule, this is not part of the definition, but like the implicit all-quantification rather a consequence of the type rules defined next. Free type variables in a typing serve as placeholders for possible refinement. The binding effect of the environment to free type variables on the right hand side of $\vdash$ that prohibits their substitution in the specialisation rule is again that a replacement has to be consistent and would need to include the whole typing.

This article will discuss four different rule sets:

1. $\vdash _{D}$ declarative system
2. $\vdash _{S}$ syntactical system
3. $\vdash _{J}$ algorithm J
4. $\vdash _{W}$ algorithm W

### Deductive system

The syntax of HM is carried forward to the syntax of the inference rules that form the body of the formal system, by using the typings as judgments. Each of the rules define what conclusion could be drawn from what premises. Additionally to the judgments, some extra conditions introduced above might be used as premises, too.

A proof using the rules is a sequence of judgments such that all premises are listed before a conclusion. The examples below show a possible format of proofs. From left to right, each line shows the conclusion, the $[{\mathtt {Name}}]$ of the rule applied and the premises, either by referring to an earlier line (number) if the premise is a judgment or by making the predicate explicit.

#### Typing rules

See also

Typing rules

The side box shows the deduction rules of the HM type system. One can roughly divide the rules into two groups:

The first four rules $[{\mathtt {Var}}]$ (variable or function access), $[{\mathtt {App}}]$ (*application*, i.e. function call with one parameter), $[{\mathtt {Abs}}]$ (*abstraction*, i.e. function declaration) and $[{\mathtt {Let}}]$ (variable declaration) are centered around the syntax, presenting one rule for each of the expression forms. Their meaning is obvious at the first glance, as they decompose each expression, prove their sub-expressions and finally combine the individual types found in the premises to the type in the conclusion.

The second group is formed by the remaining two rules $[{\mathtt {Inst}}]$ and $[{\mathtt {Gen}}]$ . They handle specialization and generalization of types. While the rule $[{\mathtt {Inst}}]$ should be clear from the section on specialization above, $[{\mathtt {Gen}}]$ complements the former, working in the opposite direction. It allows generalization, i.e. to quantify monotype variables not bound in the context.

The following two examples exercise the rule system in action. Since both the expression and the type are given, they are a type-checking use of the rules.

**Example**: A proof for $\Gamma \vdash _{D}id(n):int$ where $\Gamma =id:\forall \alpha .\alpha \rightarrow \alpha ,\ n:int$ , could be written

${\begin{array}{llll}1:&\Gamma \vdash _{D}id:\forall \alpha .\alpha \rightarrow \alpha &[{\mathtt {Var}}]&(id:\forall \alpha .\alpha \rightarrow \alpha \in \Gamma )\\2:&\Gamma \vdash _{D}id:int\rightarrow int&[{\mathtt {Inst}}]&(1),\ (\forall \alpha .\alpha \rightarrow \alpha \sqsubseteq int\rightarrow int)\\3:&\Gamma \vdash _{D}n:int&[{\mathtt {Var}}]&(n:int\in \Gamma )\\4:&\Gamma \vdash _{D}id(n):int&[{\mathtt {App}}]&(2),\ (3)\\\end{array}}$

**Example**: To demonstrate generalization, $\vdash _{D}\ {\textbf {let}}\,id=\lambda x.x\ {\textbf {in}}\ id\,:\,\forall \alpha .\alpha \rightarrow \alpha$ is shown below:

${\begin{array}{llll}1:&x:\alpha \vdash _{D}x:\alpha &[{\mathtt {Var}}]&(x:\alpha \in \left\{x:\alpha \right\})\\2:&\vdash _{D}\lambda x.x:\alpha \rightarrow \alpha &[{\mathtt {Abs}}]&(1)\\3:&id:\alpha \rightarrow \alpha \vdash _{D}id:\alpha \rightarrow \alpha &[{\mathtt {Var}}]&(id:\alpha \rightarrow \alpha \in \left\{id:\alpha \rightarrow \alpha \right\})\\4:&\vdash _{D}{\textbf {let}}\,id=\lambda x.x\ {\textbf {in}}\ id\,:\,\alpha \rightarrow \alpha &[{\mathtt {Let}}]&(2),\ (3)\\5:&\vdash _{D}{\textbf {let}}\,id=\lambda x.x\ {\textbf {in}}\ id\,:\,\forall \alpha .\alpha \rightarrow \alpha &[{\mathtt {Gen}}]&(4),\ (\alpha \not \in free(\epsilon ))\\\end{array}}$

### Let-polymorphism

Not visible immediately, the rule set encodes a regulation under which circumstances a type might be generalized or not by a slightly varying use of mono- and polytypes in the rules $[{\mathtt {Abs}}]$ and $[{\mathtt {Let}}]$ . Remember that $\sigma$ and $\tau$ denote poly- and monotypes respectively.

In rule $[{\mathtt {Abs}}]$ , the value variable of the parameter of the function $\lambda x.e$ is added to the context with a monomorphic type through the premise $\Gamma ,\ x:\tau \vdash _{D}e:\tau '$ , while in the rule $[{\mathtt {Let}}]$ , the variable enters the environment in polymorphic form $\Gamma ,\ x:\sigma \vdash _{D}e_{1}:\tau$ . Though in both cases the presence of x in the context prevents the use of the generalisation rule for any free variable in the assignment, this regulation forces the type of parameter x in a $\lambda$ -expression to remain monomorphic, while in a let-expression, the variable could be introduced polymorphic, making specializations possible.

As a consequence of this regulation, $\lambda f.(f\,{\textrm {true}},f\,{\textrm {0}})$ cannot be typed, since the parameter f is in a monomorphic position, while ${\textbf {let}}\ f=\lambda x.x\,{\textbf {in}}\,(f\,{\textrm {true}},f\,{\textrm {0}})$ has type $(bool,int)$ , because f has been introduced in a let-expression and is treated polymorphic therefore.

### Generalization rule

The generalisation rule is also worth a closer look. Here, the all-quantification implicit in the premise $\Gamma \vdash _{D}e:\sigma$ is simply moved to the right hand side of $\vdash _{D}$ in the conclusion, bound by an explicit universal quantifier. This is possible, since $\alpha$ does not occur free in the context. Again, while this makes the generalization rule plausible, it is not really a consequence. On the contrary, the generalization rule is part of the definition of HM's type system and the implicit all-quantification a consequence.

## An inference algorithm

Now that the deduction system of HM is at hand, one could present an algorithm and validate it with respect to the rules. Alternatively, it might be possible to derive it by taking a closer look on how the rules interact and proof are formed. This is done in the remainder of this article focusing on the possible decisions one can make while proving a typing.

### Degrees of freedom choosing the rules

Isolating the points in a proof, where no decision is possible at all, the first group of rules centered around the syntax leaves no choice since to each syntactical rule corresponds a unique typing rule, which determines a part of the proof, while between the conclusion and the premises of these fixed parts chains of $[{\mathtt {Inst}}]$ and $[{\mathtt {Gen}}]$ could occur. Such a chain could also exist between the conclusion of the proof and the rule for topmost expression. All proofs must have the so sketched shape.

Because the only choice in a proof with respect of rule selection are the $[{\mathtt {Inst}}]$ and $[{\mathtt {Gen}}]$ chains, the form of the proof suggests the question whether it can be made more precise, where these chains might not be needed. This is in fact possible and leads to a variant of the rules system with no such rules.

### Syntax-directed rule system

A contemporary treatment of HM uses a purely syntax-directed rule system due to Clement as an intermediate step. In this system, the specialization is located directly after the original $[{\mathtt {Var}}]$ rule and merged into it, while the generalization becomes part of the $[{\mathtt {Let}}]$ rule. There the generalization is also determined to always produce the most general type by introducing the function ${\bar {\Gamma }}(\tau )$ , which quantifies all monotype variables not bound in $\Gamma$ .

Formally, to validate that this new rule system $\vdash _{S}$ is equivalent to the original $\vdash _{D}$ , one has to show that $\Gamma \vdash _{D}\ e:\sigma \Leftrightarrow \Gamma \vdash _{S}\ e:\sigma$ , which decomposes into two sub-proofs:

- $\Gamma \vdash _{D}\ e:\sigma \Leftarrow \Gamma \vdash _{S}\ e:\sigma$ (Consistency)
- $\Gamma \vdash _{D}\ e:\sigma \Rightarrow \Gamma \vdash _{S}\ e:\sigma$ (Completeness)

While consistency can be seen by decomposing the rules $[{\mathtt {Let}}]$ and $[{\mathtt {Var}}]$ of $\vdash _{S}$ into proofs in $\vdash _{D}$ , it is likely visible that $\vdash _{S}$ is incomplete, as one cannot show $\lambda \ x.x:\forall \alpha .\alpha \rightarrow \alpha$ in $\vdash _{S}$ , for instance, but only $\lambda \ x.x:\alpha \rightarrow \alpha$ . An only slightly weaker version of completeness is provable though, namely

- $\Gamma \vdash _{D}\ e:\sigma \Rightarrow \Gamma \vdash _{S}\ e:\tau \wedge {\bar {\Gamma }}(\tau )\sqsubseteq \sigma$

implying, one can derive the principal type for an expression in $\vdash _{S}$ allowing us to generalize the proof in the end.

Comparing $\vdash _{D}$ and $\vdash _{S}$ , now only monotypes appear in the judgments of all rules. Additionally, the shape of any possible proof with the deduction system is now identical to the shape of the expression (both seen as trees). Thus the expression fully determines the shape of the proof. In $\vdash _{D}$ the shape would likely be determined with respect to all rules except $[{\mathtt {Inst}}]$ and $[{\mathtt {Gen}}]$ , which allow building arbitrarily long branches (chains) between the other nodes.

### Degrees of freedom instantiating the rules

Now that the shape of the proof is known, one is already close to formulating a type inference algorithm. Because any proof for a given expression must have the same shape, one can assume the monotypes in the proof's judgements to be undetermined and consider how to determine them.

Here, the substitution (specialisation) order comes into play. Although at the first glance one cannot determine the types locally, the hope is that it is possible to refine them with the help of the order while traversing the proof tree, additionally assuming, because the resulting algorithm is to become an inference method, that the type in any premise will be determined as the best possible. And in fact, one can, as looking at the rules of $\vdash _{S}$ suggests:

- [*Abs*]: The critical choice is τ. At this point, nothing is known about τ, so one can only assume the most general type, which is $\forall \alpha .\alpha$ . The plan is to specialize the type if it should become necessary. A polytype is not permitted in this place, so some α has to do for the moment. To avoid unwanted captures, a type variable not yet in the proof is a safe choice. Additionally, one has to keep in mind that this monotype is not yet fixed, but might be further refined.
- [*Var*]: The choice is how to refine σ. Because any choice of a type τ here depends on the usage of the variable, which is not locally known, the safest bet is the most general one. Using the same method as above one can instantiate all quantified variables in σ with fresh monotype variables, again keeping them open to further refinement.
- [*Let*]: The rule does not leave any choice. Done.
- [*App*]: Only the application rule might force a refinement to the variables "opened" so far, as required by both premises.
  1. The first premise forces the outcome of the inference to be of the form $\tau \rightarrow \tau '$ .
    - If it is, then fine. One can later pick its τ' for the result.
    - If not, it might be an open variable. Then this can be refined to the required form with two new variables as before.
    - Otherwise, the type checking fails because the first premise inferred a type which is not and cannot be made into a function type.
  2. The second premise requires that the inferred type is equal to τ of the first premise. Now there are two possibly different types, perhaps with open type variables, at hand to compare and to make equal if it is possible. If it is, a refinement is found, and if not, a type error is detected again. An effective method is known to "make two terms equal" by substitution, Robinson's Unification in combination with the so-called Union-Find algorithm.

To briefly summarize the union-find algorithm, given the set of all types in a proof, it allows one to group them together into equivalence classes by means of a union procedure and to pick a representative for each such class using a find procedure. Emphasizing the word procedure in the sense of side effect, we're clearly leaving the realm of logic in order to prepare an effective algorithm. The representative of a ${\mathtt {union}}(a,b)$ is determined such that, if both a and b are type variables then the representative is arbitrarily one of them, but while uniting a variable and a term, the term becomes the representative. Assuming an implementation of union-find at hand, one can formulate the unification of two monotypes as follows:

```
unify(ta, tb):
    ta = find(ta)
    tb = find(tb)
    if both ta,tb are terms of the form D p1..pn with identical D,n then
        unify(ta[i], tb[i]) for each corresponding ith parameter
    else
    if at least one of ta,tb is a type variable then
        union(ta, tb)
    else
        error 'types do not match'
```

Now having a sketch of an inference algorithm at hand, a more formal presentation is given in the next section. It is described in Milner P. 370 ff. as algorithm J.

### Algorithm J

The presentation of Algorithm J is a misuse of the notation of logical rules, since it includes side effects but allows a direct comparison with $\vdash _{S}$ while expressing an efficient implementation at the same time. The rules now specify a procedure with parameters $\Gamma ,e$ yielding $\tau$ in the conclusion where the execution of the premises proceeds from left to right.

The procedure $inst(\sigma )$ specializes the polytype $\sigma$ by copying the term and replacing the bound type variables consistently by new monotype variables. ' $newvar$ ' produces a new monotype variable. Likely, ${\bar {\Gamma }}(\tau )$ has to copy the type introducing new variables for the quantification to avoid unwanted captures. Overall, the algorithm now proceeds by always making the most general choice leaving the specialization to the unification, which by itself produces the most general result. As noted above, the final result $\tau$ has to be generalized to ${\bar {\Gamma }}(\tau )$ in the end, to gain the most general type for a given expression.

Because the procedures used in the algorithm have nearly O(1) cost, the overall cost of the algorithm is close to linear in the size of the expression for which a type is to be inferred. This is in strong contrast to many other attempts to derive type inference algorithms, which often came out to be NP-hard, if not undecidable with respect to termination. Thus the HM performs as well as the best fully informed type-checking algorithms can. Type-checking here means that an algorithm does not have to find a proof, but only to validate a given one.

Efficiency is slightly reduced because the binding of type variables in the context has to be maintained to allow computation of ${\bar {\Gamma }}(\tau )$ and enable an occurs check to prevent the building of recursive types during ${\mathit {unify}}(\alpha ,\tau )$ . An example of such a case is $\lambda \ x.(x\ x)$ , for which no type can be derived using HM. Practically, types are only small terms and do not build up expanding structures. Thus, in complexity analysis, one can treat comparing them as a constant, retaining O(1) costs.

## Proving the algorithm

In the previous section, while sketching the algorithm its proof was hinted at with metalogical argumentation. While this leads to an efficient algorithm J, it is not clear whether the algorithm properly reflects the deduction systems D or S which serve as a semantic base line.

The most critical point in the above argumentation is the refinement of monotype variables bound by the context. For instance, the algorithm boldly changes the context while inferring e.g. $\lambda f.(f\ 1)$ , because the monotype variable added to the context for the parameter f later needs to be refined to $int\rightarrow \beta$ when handling application. The problem is that the deduction rules do not allow such a refinement. Arguing that the refined type could have been added earlier instead of the monotype variable is an expedient at best.

The key to reaching a formally satisfying argument is to properly include the context within the refinement. Formally, typing is compatible with substitution of free type variables.

$\Gamma \vdash _{S}e:\tau \quad \Longrightarrow \quad S\Gamma \vdash _{S}e:S\tau$

To refine the free variables thus means to refine the whole typing.

### Algorithm W

From there, a proof of algorithm J leads to algorithm W, which only makes the side effects imposed by the procedure ${\textit {union}}$ explicit by expressing its serial composition by means of the substitutions $S_{i}$ . The presentation of algorithm W in the sidebar still makes use of side effects in the operations set in italic, but these are now limited to generating fresh symbols. The form of judgement is $\Gamma \vdash e:\tau ,S$ , denoting a function with a context and expression as parameter producing a monotype together with a substitution. ${\textsf {mgu}}$ is a side-effect free version of ${\textit {union}}$ producing a substitution which is the most general unifier.

While algorithm W is normally considered to be *the* HM algorithm and is often directly presented after the rule system in literature, its purpose is described by Milner on P. 369 as follows:

As it stands, W is hardly an efficient algorithm; substitutions are applied too often. It was formulated to aid the proof of soundness. We now present a simpler algorithm J which simulates W in a precise sense.

While he considered W more complicated and less efficient, he presented it in his publication before J. It has its merits when side effects are unavailable or unwanted. W is also needed to prove completeness, which is factored by him into the soundness proof.

### Proof obligations

Before formulating the proof obligations, a deviation between the rules systems D and S and the algorithms presented needs to be emphasized.

While the development above sort of misused the monotypes as "open" proof variables, the possibility that proper monotype variables might be harmed was sidestepped by introducing fresh variables and hoping for the best. But there's a catch: One of the promises made was that these fresh variables would be "kept in mind" as such. This promise is not fulfilled by the algorithm.

Having a context $1:int,\ f:\alpha$ , the expression $f\ 1$ cannot be typed in either $\vdash _{D}$ or $\vdash _{S}$ , but the algorithms come up with the type $\beta$ , where W additionally delivers the substitution $\left\{\alpha \mapsto int\rightarrow \beta \right\}$ , meaning that the algorithm fails to detect all type errors. This omission can easily be fixed by more carefully distinguishing proof variables and monotype variables.

The authors were well aware of the problem but decided not to fix it. One might assume a pragmatic reason behind this. While more properly implementing the type inference would have enabled the algorithm to deal with abstract monotypes, they were not needed for the intended application where none of the items in a preexisting context have free variables. In this light, the unneeded complication was dropped in favor of a simpler algorithm. The remaining downside is that the proof of the algorithm with respect to the rule system is less general and can only be made for contexts with $free(\Gamma )=\emptyset$ as a side condition.

${\begin{array}{lll}{\text{(Correctness)}}&\Gamma \vdash _{W}e:\tau ,S&\quad \Longrightarrow \quad \Gamma \vdash _{S}e:\tau \\{\text{(Completeness)}}&\Gamma \vdash _{S}e:\tau &\quad \Longrightarrow \quad \Gamma \vdash _{W}e:\tau ',S\quad \quad {\text{forall}}\ \tau \ {\text{where}}\ {\overline {\emptyset }}(\tau ')\sqsubseteq \tau \end{array}}$

The side condition in the completeness obligation addresses how the deduction may give many types, while the algorithm always produces one. At the same time, the side condition demands that the type inferred is actually the most general.

To properly prove the obligations one needs to strengthen them first to allow activating the substitution lemma threading the substitution S through $\vdash _{S}$ and $\vdash _{W}$ . From there, the proofs are by induction over the expression.

Another proof obligation is the substitution lemma itself, i.e. the substitution of the typing, which finally establishes the all-quantification. The later cannot formally be proven, since no such syntax is at hand.

## Extensions

### Recursive definitions

To make programming practical recursive functions are needed. A central property of the lambda calculus is that recursive definitions are not directly available, but can instead be expressed with a fixed point combinator. However, the fixpoint combinator cannot be formulated in a typed version of the lambda calculus without having a disastrous effect on the system as outlined below.

#### Typing rule

The original paper shows recursion can be realized by a combinator ${\mathit {fix}}:\forall \alpha .(\alpha \rightarrow \alpha )\rightarrow \alpha$ . A possible recursive definition could thus be formulated as ${\mathtt {rec}}\ v=e_{1}\ {\mathtt {in}}\ e_{2}\ ::={\mathtt {let}}\ v={\mathit {fix}}(\lambda v.e_{1})\ {\mathtt {in}}\ e_{2}$ .

Alternatively an extension of the expression syntax and an extra typing rule is possible:

$\displaystyle {\frac {\Gamma ,\Gamma '\vdash e_{1}:\tau _{1}\quad \dots \quad \Gamma ,\Gamma '\vdash e_{n}:\tau _{n}\quad \Gamma ,\Gamma ''\vdash e:\tau }{\Gamma \ \vdash \ {\mathtt {rec}}\ v_{1}=e_{1}\ {\mathtt {and}}\ \dots \ {\mathtt {and}}\ v_{n}=e_{n}\ {\mathtt {in}}\ e:\tau }}\quad [{\mathtt {Rec}}]$

where

- $\Gamma '=v_{1}:\tau _{1},\ \dots ,\ v_{n}:\tau _{n}$
- $\Gamma ''=v_{1}:{\bar {\Gamma }}(\ \tau _{1}\ ),\ \dots ,\ v_{n}:{\bar {\Gamma }}(\ \tau _{n}\ )$

basically merging $[{\mathtt {Abs}}]$ and $[{\mathtt {Let}}]$ while including the recursively defined variables in monotype positions where they occur to the left of the ${\mathtt {in}}$ but as polytypes to the right of it.

#### Consequences

While the above is straightforward it does come at a price.

Type theory connects lambda calculus with computation and logic. The easy modification above has effects on both:

- The strong normalisation property is invalidated, because non-terminating terms can be formulated.
- The logic collapses because the type $\forall a.a$ becomes inhabited.

### Overloading

Overloading means that different functions can be defined and used with the same name. Most programming languages at least provide overloading with the built-in arithmetic operations (+, <, etc.), to allow the programmer to write arithmetic expressions in the same form, even for different numerical types like `int` or `real`. Because a mixture of these different types within the same expression also demands for implicit conversion, overloading especially for these operations is often built into the programming language itself. In some languages, this feature is generalized and made available to the user, e.g. in C++.

While ad hoc overloading has been avoided in functional programming for the computation costs both in type checking and inference, a means to systematise overloading has been introduced that resembles both in form and naming to object oriented programming, but works one level upwards. "Instances" in this systematic are not objects (i.e. on value level), but rather types. The quicksort example mentioned in the introduction uses the overloading in the orders, having the following type annotation in Haskell:

```mw
quickSort :: Ord a => [a] -> [a]
```

Herein, the type `a` is not only polymorphic, but also restricted to be an instance of some type class `Ord`, that provides the order predicates `<` and `>=` used in the functions body. The proper implementations of these predicates are then passed to quicksorts as additional parameters, as soon as quicksort is used on more concrete types providing a single implementation of the overloaded function quickSort.

Because the "classes" only allow a single type as their argument, the resulting type system can still provide inference. Additionally, the type classes can then be equipped with some kind of overloading order allowing one to arrange the classes as a lattice.

### Higher-order types

Parametric polymorphism implies that types themselves are passed as parameters as if they were proper values. Passed as arguments to a proper functions, but also into "type functions" as in the "parametric" type constants, leads to the question how to more properly type types themselves. Higher-order types are used to create an even more expressive type system.

Unification is no longer decidable in the presence of meta types, rendering type inference impossible in this extend of generality. Additionally, assuming a type of all types that includes itself as type leads into a paradox, as in the set of all sets, so one must proceed in steps of levels of abstraction. Research in second order lambda calculus, one step upwards, showed that type inference is undecidable in this generality.

Haskell introduces one higher level named kind. In standard Haskell, kinds are inferred and used for little more than to describe the arity of type constructors. e.g. a list type constructor is thought of as mapping a type (the type of its elements) to another type (the type of the list containing said elements); notationally this is expressed as $*\to *$ . Language extensions are available which extend kinds to emulate features of a dependent type system.

### Subtyping

Attempts to combine subtyping and type inference have caused quite some frustration. It is straightforward to accumulate and propagate subtyping constraints (as opposed to type equality constraints), making the resulting constraints part of the inferred typing schemes, for example $\forall \alpha .\ (\alpha \leq T)\Rightarrow \alpha \rightarrow \alpha$ , where $\alpha \leq T$ is a constraint on the type variable $\alpha$ . However, because type variables are no longer unified eagerly in this approach, it tends to generate large and unwieldy typing schemes containing many useless type variables and constraints, making them hard to read and understand. Therefore, considerable effort was put into simplifying such typing schemes and their constraints, using techniques similar to those of nondeterministic finite automaton (NFA) simplification (useful in the presence of inferred recursive types). More recently, Dolan and Mycroft formalized the relationship between typing scheme simplification and NFA simplification and showed that an algebraic take on the formalization of subtyping allowed generating compact principal typing schemes for an ML-like language (called MLsub). Notably, their proposed typing scheme used a restricted form of union and intersection types instead of explicit constraints. Parreaux later claimed that this algebraic formulation was equivalent to a relatively simple algorithm resembling Algorithm W, and that the use of union and intersection types was not essential.

On the other hand, type inference has proven more difficult in the context of object-oriented programming languages, because object methods tend to require first-class polymorphism in the style of System F (where type inference is undecidable) and because of features like F-bounded polymorphism. Consequently, type systems with subtyping enabling object-oriented programming, such as Cardelli's system $F_{<:}$ , do not support HM-style type inference.

Row polymorphism can be used as an alternative to subtyping for supporting language features like structural records. While this style of polymorphism is less flexible than subtyping in some ways, notably requiring more polymorphism than strictly necessary to cope with the lack of directionality in type constraints, it has the advantage that it can be integrated with the standard HM algorithms quite easily.
