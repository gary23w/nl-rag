---
title: "Type theory"
source: https://en.wikipedia.org/wiki/Type_theory
domain: lambda-type-theory
license: CC-BY-SA-4.0
tags: lambda calculus, type theory, type system, type inference, hindley-milner, dependent type
fetched: 2026-07-02
---

# Type theory

In mathematical logic, and theoretical computer science, **type theory** is the study of formal systems that classify expressions or mathematical objects by their *types*. Roughly speaking, a type plays a similar role to that played by a data type in programming: it specifies what kind of thing an expression is and how it may be used. Type theories are used in the study of programming languages (type systems), formal logic, and the formalization of mathematics.

Some type theories have been proposed as alternatives to set theory as a foundation of mathematics. Examples include Alonzo Church's simple theory of types and Per Martin-Löf's intuitionistic type theory.

Many proof assistants are based on type theory. For example, the underlying formal language of Rocq (formerly Coq) is the calculus of inductive constructions, while Lean is based on dependent type theory.

## History

Type theory was created to avoid paradoxes in naive set theory and formal logic, such as Russell's paradox which demonstrates that, without proper axioms, it is possible to define the set of all sets that are not members of themselves; this set both contains itself and does not contain itself. Between 1902 and 1908, Bertrand Russell proposed various solutions to this problem.

By 1908, Russell arrived at a ramified theory of types together with an axiom of reducibility, both of which appeared in Whitehead and Russell's *Principia Mathematica* published in 1910, 1912, and 1913. This system avoided contradictions suggested in Russell's paradox by creating a hierarchy of types and then assigning each concrete mathematical entity to a specific type. Entities of a given type were built exclusively of subtypes of that type, thus preventing an entity from being defined using itself. This resolution of Russell's paradox is similar to approaches taken in other formal systems, such as Zermelo-Fraenkel set theory.

Type theory is particularly popular in conjunction with Alonzo Church's lambda calculus. One notable early example of type theory is Church's simply typed lambda calculus. Church's theory of types helped the formal system avoid the Kleene–Rosser paradox that afflicted the original untyped lambda calculus. Church demonstrated that it could serve as a foundation of mathematics and it was referred to as a higher-order logic.

In the modern literature, "type theory" refers to a typed system based around lambda calculus. One influential system is Per Martin-Löf's intuitionistic type theory, which was proposed as a foundation for constructive mathematics. Another is Thierry Coquand's calculus of constructions, which is used as the foundation by Rocq (previously known as *Coq*), Lean, and other computer proof assistants. Type theory is an active area of research, one direction being the development of homotopy type theory.

## Applications

### Mathematical foundations

The first computer proof assistant, called Automath, used type theory to encode mathematics on a computer. Martin-Löf specifically developed intuitionistic type theory to encode *all* mathematics to serve as a new foundation for mathematics. There is ongoing research into mathematical foundations using homotopy type theory.

Mathematicians working in category theory already had difficulty working with the widely accepted foundation of Zermelo–Fraenkel set theory. This led to proposals such as Lawvere's Elementary Theory of the Category of Sets (ETCS). Homotopy type theory continues in this line using type theory. Researchers are exploring connections between dependent types (especially the identity type) and algebraic topology (specifically homotopy).

### Proof assistants

Much of the current research into type theory is driven by proof checkers, interactive proof assistants, and automated theorem provers. Most of these systems use a type theory as the mathematical foundation for encoding proofs, which is not surprising, given the close connection between type theory and programming languages:

- LF is used by Twelf, often to define other type theories;
- many type theories which fall under higher-order logic are used by the HOL family of provers and PVS;
- computational type theory is used by NuPRL;
- calculus of constructions and its derivatives are used by Rocq (previously known as *Coq*), Matita, and Lean;
- UTT (Luo's Unified Theory of dependent Types) is used by Agda which is both a programming language and proof assistant

Many type theories are supported by LEGO and Isabelle. Isabelle also supports foundations besides type theories, such as ZFC. Mizar is an example of a proof system that only supports set theory.

### Programming languages

Any static program analysis, such as the type checking algorithms in the semantic analysis phase of compiler, has a connection to type theory. A prime example is Agda, a programming language which uses UTT (Luo's Unified Theory of dependent Types) for its type system.

The programming language ML was developed for manipulating type theories (see *Logic for Computable Functions*) and its own type system was heavily influenced by them.

### Linguistics

Type theory is also widely used in formal theories of semantics of natural languages, especially Montague grammar and its descendants. In particular, categorial grammars and pregroup grammars extensively use type constructors to define the types (*noun*, *verb*, etc.) of words.

The most common construction takes the basic types e and t for individuals and truth-values, respectively, and defines the set of types recursively as follows:

- if a and b are types, then so is ⁠ $\langle a,b\rangle$ ⁠;
- nothing except the basic types, and what can be constructed from them by means of the previous clause are types.

A complex type $\langle a,b\rangle$ is the type of functions from entities of type a to entities of type ⁠ b ⁠. Thus one has types like $\langle e,t\rangle$ that are interpreted as elements of the set of functions from entities to truth-values, i.e. indicator functions of sets of entities. An expression of type $\langle \langle e,t\rangle ,t\rangle$ is a function from sets of entities to truth-values, i.e. a (indicator function of a) set of sets. This latter type is standardly taken to be the type of natural language quantifiers, like *everybody* or *nobody* (Montague 1973, Barwise and Cooper 1981).

Type theory with records is a formal semantics representation framework, using *records* to express *type theory types*. It has been used in natural language processing, principally computational semantics and dialogue systems.

Gregory Bateson introduced a theory of logical types into the social sciences; his notions of double bind and logical levels are based on Russell's theory of types.

## Logic

A type theory is a mathematical logic, which is to say it is a collection of rules of inference that result in judgments. Most logics have judgments asserting "The proposition $\varphi$ is true", or "The formula $\varphi$ is a well-formed formula". A type theory has judgments that define types and assign them to a collection of formal objects, known as terms. A term and its type are often written together as ⁠ $\mathrm {term$ ⁠.

### Terms

A term in logic is recursively defined as a constant symbol, variable, or a function application, where a term is applied to another term. Constant symbols could include the natural number ⁠ 0 ⁠, the Boolean value ⁠ ${\texttt {true}}$ ⁠, and functions such as the successor function $\mathrm {S}$ and conditional operator ⁠ $\mathrm {if}$ ⁠. Thus some terms could be ⁠ 0 ⁠, ⁠ $(\mathrm {S} \,0)$ ⁠, ⁠ $(\mathrm {S} \,(\mathrm {S} \,0))$ ⁠, and ⁠ $(\mathrm {if} \,{\texttt {true}}\,0\,(\mathrm {S} \,0))$ ⁠.

### Judgments

Most type theories have 4 judgments:

- " T is a type"
- " t is a term of type ⁠ T ⁠"
- "Type $T_{1}$ is equal to type ⁠ $T_{2}$ ⁠"
- "Terms $t_{1}$ and $t_{2}$ both of type T are equal"

Judgments may follow from assumptions. For example, one might say "assuming x is a term of type ${\mathsf {bool}}$ and y is a term of type ⁠ ${\mathsf {nat}}$ ⁠, it follows that $({\textrm {if}}\,x\,y\,y)$ is a term of type ⁠ ${\mathsf {nat}}$ ⁠". Such judgments are formally written with the turnstile symbol ⁠ $\vdash$ ⁠.

$x:{\mathsf {bool}},y:{\mathsf {nat}}\vdash (\mathrm {if} \,x\,y\,y):{\mathsf {nat}}$

If there are no assumptions, there will be nothing to the left of the turnstile.

$\vdash \mathrm {S$

The list of assumptions on the left is the *context* of the judgment. Capital greek letters, such as $\Gamma$ and $\Delta$ , are common choices to represent some or all of the assumptions. The 4 different judgments are thus usually written as follows.

| Formal notation for judgments | Description |
|---|---|
| $\Gamma \vdash T$ Type | T is a type (under assumptions ⁠ $\Gamma$ ⁠). |
| $\Gamma \vdash t:T$ | t is a term of type T (under assumptions ⁠ $\Gamma$ ⁠). |
| $\Gamma \vdash T_{1}=T_{2}$ | Type $T_{1}$ is equal to type $T_{2}$ (under assumptions ⁠ $\Gamma$ ⁠). |
| $\Gamma \vdash t_{1}=t_{2}:T$ | Terms $t_{1}$ and $t_{2}$ are both of type T and are equal (under assumptions ⁠ $\Gamma$ ⁠). |

Some textbooks use a triple equal sign $\equiv$ to stress that this is judgmental equality and thus an extrinsic notion of equality. The judgments enforce that every term has a type. The type will restrict which rules can be applied to a term.

### Rules of inference

A type theory's inference rules say what judgments can be made, based on the existence of other judgments. Rules are expressed as a Gentzen-style deduction using a horizontal line, with the required input judgments above the line and the resulting judgment below the line. For example, the following inference rule states a substitution rule for judgmental equality. ${\begin{array}{c}\Gamma \vdash t:T_{1}\qquad \Delta \vdash T_{1}=T_{2}\\\hline \Gamma ,\Delta \vdash t:T_{2}\end{array}}$ The rules are syntactic and work by rewriting. The metavariables ⁠ $\Gamma$ ⁠, ⁠ $\Delta$ ⁠, ⁠ t ⁠, ⁠ $T_{1}$ ⁠, and ⁠ $T_{2}$ ⁠ may actually consist of complex terms and types that contain many function applications, not just single symbols.

To generate a particular judgment in type theory, there must be a rule to generate it, as well as rules to generate all of that rule's required inputs, and so on. The applied rules form a proof tree, where the top-most rules need no assumptions. One example of a rule that does not require any inputs is one that states the type of a constant term. For example, to assert that there is a term 0 of type ⁠ ${\mathsf {nat}}$ ⁠, one would write the following. ${\begin{array}{c}\hline \vdash 0:{\mathsf {nat}}\\\end{array}}$

#### Type inhabitation

Generally, the desired conclusion of a proof in type theory is one of type inhabitation. The decision problem of type inhabitation (abbreviated by ⁠ ${\displaystyle \exists t.\Gamma \vdash t:\tau$ ⁠) is:

Given a context

⁠

$\Gamma$

⁠

and a type

⁠

$\tau$

⁠

, decide whether there exists a term

⁠

t

⁠

that can be assigned the type

⁠

$\tau$

⁠

in the type environment

⁠

$\Gamma$

⁠

.

Girard's paradox shows that type inhabitation is strongly related to the consistency of a type system with Curry–Howard correspondence. To be sound, such a system must have uninhabited types.

A type theory usually has several rules, including ones to:

- create a judgment (known as a *context* in this case)
- add an assumption to the context (context *weakening*)
- rearrange the assumptions
- use an assumption to create a variable
- define reflexivity, symmetry and transitivity for judgmental equality
- define substitution for application of lambda terms
- list all the interactions of equality, such as substitution
- define a hierarchy of type universes
- assert the existence of new types

Also, for each "by rule" type, there are 4 different kinds of rules:

- "type formation" rules say how to create the type
- "term introduction" rules define the canonical terms and constructor functions, like "pair" and "S".
- "term elimination" rules define the other functions like "first", "second", and "R".
- "computation" rules specify how computation is performed with the type-specific functions.

For examples of rules, an interested reader may follow Appendix A.2 of the *Homotopy Type Theory* book, or read Martin-Löf's Intuitionistic Type Theory.

## Connections to foundations

The logical framework of a type theory bears a resemblance to intuitionistic, or constructive, logic. Formally, type theory is often cited as an implementation of the Brouwer–Heyting–Kolmogorov interpretation of intuitionistic logic. Additionally, connections can be made to category theory and computer programs.

### Intuitionistic logic

When used as a foundation, certain types are interpreted to be propositions (statements that can be proven), and terms inhabiting the type are interpreted to be proofs of that proposition. When some types are interpreted as propositions, there is a set of common types that can be used to connect them to make a Boolean algebra out of types. However, the logic is not classical logic but intuitionistic logic, which is to say it does not have the law of excluded middle nor double negation.

Under this intuitionistic interpretation, there are common types that act as the logical operators:

| Logic Name | Logic Notation | Type Notation | Type Name |
|---|---|---|---|
| True | $\top$ | $\top$ | Unit Type |
| False | $\bot$ | $\bot$ | Empty Type |
| Implication | $A\to B$ | $A\to B$ | Function |
| Not | $\neg A$ | $A\to \bot$ | Function to Empty Type |
| And | $A\land B$ | $A\times B$ | Product Type |
| Or | $A\lor B$ | $A+B$ | Sum Type |
| For All | $\forall a\in A,P(a)$ | $\Pi a:A.P(a)$ | Dependent Product |
| Exists | $\exists a\in A,P(a)$ | $\Sigma a:A.P(a)$ | Dependent Sum |

Because the law of excluded middle does not hold, there is no term of type ⁠ $\Pi A.A+(A\to \bot )$ ⁠. Likewise, double negation does not hold, so there is no term of type ⁠ $\Pi A.((A\to \bot )\to \bot )\to A$ ⁠.

It is possible to include the law of excluded middle and double negation into a type theory, by rule or assumption. However, terms may not compute down to canonical terms and it will interfere with the ability to determine if two terms are judgementally equal to each other.

#### Constructive mathematics

Per Martin-Löf proposed his intuitionistic type theory as a foundation for constructive mathematics. Constructive mathematics requires when proving "there exists an x with property ⁠ $P(x)$ ⁠", one must construct a particular x and a proof that it has property P . In type theory, existence is accomplished using the dependent product type, and its proof requires a term of that type.

An example of a non-constructive proof is proof by contradiction. The first step is assuming that x does not exist and refuting it by contradiction. The conclusion from that step is "it is not the case that x does not exist". The last step is, by double negation, concluding that x exists. Constructive mathematics does not allow the last step of removing the double negation to conclude that x exists.

Most of the type theories proposed as foundations are constructive, and this includes most of the ones used by proof assistants. It is possible to add non-constructive features to a type theory, by rule or assumption. These include operators on continuations such as call with current continuation. However, these operators tend to break desirable properties such as canonicity and parametricity.

### Curry–Howard correspondence

The Curry–Howard correspondence is the observed similarity between logics and programming languages. The implication in logic, "A $\to$ B" resembles a function from type "A" to type "B". For a variety of logics, the rules are similar to expressions in a programming language's types. The similarity goes farther, as applications of the rules resemble programs in the programming languages. Thus, the correspondence is often summarized as "proofs as programs".

The opposition of terms and types can also be viewed as one of *implementation* and *specification*. By program synthesis, (the computational counterpart of) type inhabitation can be used to construct (all or parts of) programs from the specification given in the form of type information.

#### Type inference

Many programs that work with type theory (e.g., interactive theorem provers) also do type inferencing. It lets them select the rules that the user intends, with fewer actions by the user.

### Research areas

#### Category theory

Although the initial motivation for category theory was far removed from foundationalism, the two fields turned out to have deep connections. As John Lane Bell writes: "In fact categories can *themselves* be viewed as type theories of a certain kind; this fact alone indicates that type theory is much more closely related to category theory than it is to set theory." In brief, a category can be viewed as a type theory by regarding its objects as types (or *sorts* ), i.e. "Roughly speaking, a category may be thought of as a type theory shorn of its syntax." A number of significant results follow in this way:

- cartesian closed categories correspond to the typed λ-calculus (Lambek, 1970);
- C-monoids (categories with products and exponentials and one non-terminal object) correspond to the untyped λ-calculus (observed independently by Lambek and Dana Scott around 1980);
- locally cartesian closed categories correspond to Martin-Löf type theories (Seely, 1984).

The interplay, known as categorical logic, has been a subject of active research since then; see the monograph of Jacobs (1999) for instance.

#### Homotopy type theory

Homotopy type theory attempts to combine type theory and category theory. It focuses on equalities, especially equalities between types. Homotopy type theory differs from intuitionistic type theory mostly by its handling of the equality type. In 2016, cubical type theory was proposed, which is a homotopy type theory with normalization.

## Definitions

### Terms and types

#### Atomic terms

The most basic types are called atoms, and a term whose type is an atom is known as an atomic term. Common atomic terms included in type theories are natural numbers, often notated with the type ⁠ ${\mathsf {nat}}$ ⁠, Boolean logic values (⁠ ${\texttt {true}}$ ⁠ and ⁠ ${\texttt {false}}$ ⁠), notated with the type ⁠ ${\mathsf {bool}}$ ⁠, and formal variables, whose type may vary. For example, the following may be atomic terms.

- $42:{\mathsf {nat}}$
- ${\texttt {true}}:{\mathsf {bool}}$
- $x:{\mathsf {nat}}$
- $y:{\mathsf {bool}}$

#### Function terms

In addition to atomic terms, most modern type theories also allow for functions. Function types introduce an arrow symbol, and are defined inductively: If $\sigma$ and $\tau$ are types, then the notation $\sigma \to \tau$ is the type of a function which takes a parameter of type $\sigma$ and returns a term of type ⁠ $\tau$ ⁠. Types of this form are known as *simple* types.

Some terms may be declared directly as having a simple type, such as the following term, ⁠ $\mathrm {add}$ ⁠, which takes in two natural numbers in sequence and returns one natural number.

$\mathrm {add$

Strictly speaking, a simple type only allows for one input and one output, so a more faithful reading of the above type is that $\mathrm {add}$ is a function which takes in a natural number and returns a function of the form ⁠ ${\mathsf {nat}}\to {\mathsf {nat}}$ ⁠. The parentheses clarify that $\mathrm {add}$ does not have the type ⁠ $({\mathsf {nat}}\to {\mathsf {nat}})\to {\mathsf {nat}}$ ⁠, which would be a function which takes in a function of natural numbers and returns a natural number. The convention is that the arrow is right associative, so the parentheses may be dropped from ⁠ $\mathrm {add}$ ⁠'s type.

#### Lambda terms

New function terms may be constructed using lambda expressions, and are called lambda terms. These terms are also defined inductively: a lambda term has the form ⁠ $(\lambda v.t)$ ⁠, where v is a formal variable and t is a term, and its type is notated ⁠ $\sigma \to \tau$ ⁠, where $\sigma$ is the type of ⁠ v ⁠, and $\tau$ is the type of ⁠ t ⁠. The following lambda term represents a function which doubles an input natural number.

$(\lambda x.\mathrm {add} \,x\,x):{\mathsf {nat}}\to {\mathsf {nat}}$

The variable is x and (implicit from the lambda term's type) must have type ⁠ ${\mathsf {nat}}$ ⁠. The term $\mathrm {add} \,x\,x$ has type ⁠ ${\mathsf {nat}}$ ⁠, which is seen by applying the function application inference rule twice. Thus, the lambda term has type ${\mathsf {nat}}\to {\mathsf {nat}}$ , which means it is a function taking a natural number as an argument and returning a natural number.

A lambda term is an anonymous function because it lacks a name. The concept of anonymous functions appears in many programming languages.

### Inference Rules

#### Function application

The power of type theories is in specifying how terms may be combined by way of inference rules. Type theories which have functions also have the inference rule of function application: if t is a term of type ⁠ $\sigma \to \tau$ ⁠, and s is a term of type ⁠ $\sigma$ ⁠, then the application of t to ⁠ s ⁠, often written ⁠ $(t\,s)$ ⁠, has type ⁠ $\tau$ ⁠. For example, if one knows the type notations ⁠ $0:{\textsf {nat}}$ ⁠, ⁠ $1:{\textsf {nat}}$ ⁠, and ⁠ $2:{\textsf {nat}}$ ⁠, then the following type notations can be deduced from function application.

- $(\mathrm {add} \,1):{\textsf {nat}}\to {\textsf {nat}}$
- $((\mathrm {add} \,2)\,0):{\textsf {nat}}$
- $((\mathrm {add} \,1)((\mathrm {add} \,2)\,0)):{\textsf {nat}}$

Parentheses indicate the order of operations; however, by convention, function application is left associative, so parentheses can be dropped where appropriate. In the case of the three examples above, all parentheses could be omitted from the first two, and the third may simplified to ⁠ $\mathrm {add} \,1\,(\mathrm {add} \,2\,0):{\textsf {nat}}$ ⁠.

#### Reductions

Type theories that allow for lambda terms also include inference rules known as $\beta$ -reduction and $\eta$ -reduction. They generalize the notion of function application to lambda terms. Symbolically, they are written

- $(\lambda v.t)\,s\rightarrow t[v\colon =s]$ (⁠ $\beta$ ⁠-reduction).
- $(\lambda v.t\,v)\rightarrow t$ , if v is not a free variable in t (⁠ $\eta$ ⁠-reduction).

The first reduction describes how to evaluate a lambda term: if a lambda expression $(\lambda v.t)$ is applied to a term ⁠ s ⁠, one replaces every occurrence of v in t with ⁠ s ⁠. The second reduction makes explicit the relationship between lambda expressions and function types: if $(\lambda v.t\,v)$ is a lambda term, then it must be that t is a function term because it is being applied to ⁠ v ⁠. Therefore, the lambda expression is equivalent to just ⁠ t ⁠, as both take in one argument and apply t to it.

For example, the following term may be $\beta$ -reduced.

$(\lambda x.\mathrm {add} \,x\,x)\,2\rightarrow \mathrm {add} \,2\,2$

In type theories that also establish notions of equality for types and terms, there are corresponding inference rules of $\beta$ -equality and $\eta$ -equality.

### Common terms and types

#### Empty type

The empty type has no terms. The type is usually written $\bot$ or ⁠ $\mathbb {0}$ ⁠. One use for the empty type is proofs of type inhabitation. If for a type ⁠ a ⁠, it is consistent to derive a function of type ⁠ $a\to \bot$ ⁠, then a is *uninhabited*, which is to say it has no terms.

#### Unit type

The unit type has exactly 1 canonical term. The type is written $\top$ or $\mathbb {1}$ and the single canonical term is written ⁠ $\ast$ ⁠. The unit type is also used in proofs of type inhabitation. If for a type ⁠ a ⁠, it is consistent to derive a function of type ⁠ $\top \to a$ ⁠, then a is *inhabited*, which is to say it must have one or more terms.

#### Boolean type

The Boolean type has exactly 2 canonical terms. The type is usually written ${\textsf {bool}}$ or $\mathbb {B}$ or ⁠ $\mathbb {2}$ ⁠. The canonical terms are usually $\mathrm {true}$ and ⁠ $\mathrm {false}$ ⁠.

#### Natural numbers

Natural numbers are usually implemented in the style of Peano Arithmetic. There is a canonical term $0:{\mathsf {nat}}$ for zero. Canonical values larger than zero use iterated applications of a successor function ⁠ $\mathrm {S$ ⁠.

### Type constructors

Some type theories allow for types of complex terms, such as functions or lists, to depend on the types of its arguments; these are called type constructors. For example, a type theory could have the dependent type ⁠ ${\mathsf {list}}\,a$ ⁠, which should correspond to lists of terms, where each term must have type ⁠ a ⁠. In this case, ${\mathsf {list}}$ has the kind ⁠ $U\to U$ ⁠, where U denotes the universe of all types in the theory.

#### Product type

The product type, ⁠ $\times$ ⁠, depends on two types, and its terms are commonly written as ordered pairs ⁠ $(s,t)$ ⁠. The pair $(s,t)$ has the product type ⁠ $\sigma \times \tau$ ⁠, where $\sigma$ is the type of s and $\tau$ is the type of ⁠ t ⁠. Each product type is then usually defined with eliminator functions $\mathrm {first$ and ⁠ $\mathrm {second$ ⁠.

- $\mathrm {first} \,(s,t)$ returns ⁠ s ⁠, and
- $\mathrm {second} \,(s,t)$ returns ⁠ t ⁠.

Besides ordered pairs, this type is used for the concepts of logical conjunction and intersection.

#### Sum type

The sum type is written as either + or ⁠ $\sqcup$ ⁠. In programming languages, sum types may be referred to as tagged unions. Each type $\sigma \sqcup \tau$ is usually defined with constructors $\mathrm {left$ and ⁠ $\mathrm {right$ ⁠, which are injective, and an eliminator function $\mathrm {match$ such that

- $\mathrm {match} \,f\,g\,(\mathrm {left} \,x)$ returns ⁠ $f\,x$ ⁠, and
- $\mathrm {match} \,f\,g\,(\mathrm {right} \,y)$ returns ⁠ $g\,y$ ⁠.

The sum type is used for the concepts of logical disjunction and union.

### Polymorphic types

Some theories also allow terms to have their definitions depend on types. For instance, an identity function of any type could be written as ⁠ $\lambda x.x:\forall \alpha .\alpha \to \alpha$ ⁠. The function is said to be polymorphic in ⁠ $\alpha$ ⁠, or generic in ⁠ x ⁠.

As another example, consider a function ⁠ $\mathrm {append}$ ⁠, which takes in a ${\mathsf {list}}\,a$ and a term of type ⁠ a ⁠, and returns the list with the element at the end. The type annotation of such a function would be ⁠ $\mathrm {append$ ⁠, which can be read as "for any type ⁠ a ⁠, pass in a ${\mathsf {list}}\,a$ and an ⁠ a ⁠, and return a ⁠ ${\mathsf {list}}\,a$ ⁠". Here $\mathrm {append}$ is polymorphic in ⁠ a ⁠.

#### Products and sums

With polymorphism, the eliminator functions can be defined generically for *all* product types as $\mathrm {first$ and ⁠ $\mathrm {second$ ⁠.

- $\mathrm {first} \,(s,t)$ returns ⁠ s ⁠, and
- $\mathrm {second} \,(s,t)$ returns ⁠ t ⁠.

Likewise, the sum type constructors can be defined for all valid types of sum members as $\mathrm {left$ and ⁠ $\mathrm {right$ ⁠, which are injective, and the eliminator function can be given as $\mathrm {match$ such that

- $\mathrm {match} \,f\,g\,(\mathrm {left} \,x)$ returns ⁠ $f\,x$ ⁠, and
- $\mathrm {match} \,f\,g\,(\mathrm {right} \,y)$ returns ⁠ $g\,y$ ⁠.

### Dependent typing

Some theories also permit types to be dependent on terms instead of types. For example, a theory could have the type ⁠ ${\mathsf {vector}}\,n$ ⁠, where n is a term of type ${\mathsf {nat}}$ encoding the length of the vector. This allows for greater specificity and type safety: functions with vector length restrictions or length matching requirements, such as the dot product, can encode this requirement as part of the type.

There are foundational issues that can arise from dependent types if a theory is not careful about what dependences are allowed, such as Girard's Paradox. The logician Henk Barendegt introduced the lambda cube as a framework for studying various restrictions and levels of dependent typing.

#### Dependent products and sums

Two common type dependences, dependent product and dependent sum types, allow for the theory to encode BHK intuitionistic logic by acting as equivalents to universal and existential quantification; this is formalized by Curry–Howard correspondence. As they also connect to products and sums in set theory, they are often written with the symbols $\Pi$ and ⁠ $\Sigma$ ⁠, respectively.

Sum types are seen in dependent pairs, where the second type depends on the value of the first term. This arises naturally in computer science where functions may return different types of outputs based on the input. For example, the Boolean type is usually defined with an eliminator function ⁠ $\mathrm {if}$ ⁠, which takes three arguments and behaves as follows.

- $\mathrm {if} \,{\texttt {true}}\,x\,y$ returns ⁠ x ⁠, and
- $\mathrm {if} \,{\texttt {false}}\,x\,y$ returns ⁠ y ⁠.

Ordinary definitions of $\mathrm {if}$ require x and y to have the same type. If the type theory allows for dependent types, then it is possible to define a dependent type $x:{\mathsf {bool}}\,\vdash \,\mathrm {TF} \,x:U\to U\to U$ such that

- $\mathrm {TF} \,{\texttt {true}}\,\sigma \,\tau$ returns ⁠ $\sigma$ ⁠, and
- $\mathrm {TF} \,{\texttt {false}}\,\sigma \,\tau$ returns ⁠ $\tau$ ⁠.

The type of $\mathrm {if}$ may then be written as ⁠ $\forall \,\sigma \,\tau .\Pi _{x:{\mathsf {bool}}}.\sigma \to \tau \to \mathrm {TF} \,x\,\sigma \,\tau$ ⁠.

#### Identity type

Following the notion of Curry–Howard Correspondence, the identity type is a type introduced to mirror propositional equivalence, as opposed to the judgmental (syntactic) equivalence that type theory already provides.

An identity type requires two terms of the same type and is written with the symbol ⁠ = ⁠. For example, if $x+1$ and $1+x$ are terms, then $x+1=1+x$ is a possible type. Canonical terms are created with a reflexivity function, ⁠ $\mathrm {refl}$ ⁠. For a term ⁠ t ⁠, the call $\mathrm {refl} \,t$ returns the canonical term inhabiting the type ⁠ $t=t$ ⁠.

The complexities of equality in type theory make it an active research topic; homotopy type theory is a notable area of research that mainly deals with equality in type theory.

#### Inductive types

Inductive types are a general template for creating a large variety of types. In fact, all the types described above and more can be defined using the rules of inductive types. Two methods of generating inductive types are induction-recursion and induction-induction. A method that only uses lambda terms is Scott encoding.

Some proof assistants, such as Rocq (previously known as *Coq*) and Lean, are based on the calculus for inductive constructions, which is a calculus of constructions with inductive types.

## Differences from set theory

The most commonly accepted foundation for mathematics is first-order logic with the language and axioms of Zermelo–Fraenkel set theory with the axiom of choice, abbreviated ZFC. Type theories having sufficient expressibility may also act as a foundation of mathematics. There are a number of differences between these two approaches.

- Set theory has both rules and axioms, while type theories only have rules. Type theories, in general, do not have axioms and are defined by their rules of inference.
- Classical set theory and logic have the law of excluded middle. When a type theory encodes the concepts of "and" and "or" as types, it leads to intuitionistic logic, and does not necessarily have the law of excluded middle.
- In set theory, an element is not restricted to one set. The element can appear in subsets and unions with other sets. In type theory, terms (generally) belong to only one type. Where a subset would be used, type theory can use a predicate function or use a dependently-typed product type, where each element x is paired with a proof that the subset's property holds for ⁠ x ⁠. Where a union would be used, type theory uses the sum type, which contains new canonical terms.
- Type theory has a built-in notion of computation. Thus, "1+1" and "2" are different terms in type theory, but they compute to the same value. Moreover, functions are defined computationally as lambda terms. In set theory, "1+1=2" means that "1+1" is just another way to refer the value "2". Type theory's computation does require a complicated concept of equality.
- Set theory encodes numbers as sets. Type theory can encode numbers as functions using Church encoding, or more naturally as inductive types, and the construction closely resembles Peano's axioms.
- In type theory, proofs have types whereas in set theory, proofs are part of the underlying first-order logic.

Proponents of type theory will also point out its connection to constructive mathematics through the BHK interpretation, its connection to logic by the Curry–Howard isomorphism, and its connections to category theory.

### Properties of type theories

Terms usually belong to a single type. However, there are type theories that define "subtyping".

Computation takes place by repeated application of rules. Many types of theories are strongly normalizing, which means that any order of applying the rules will always end in the same result. However, some are not. In a normalizing type theory, the one-directional computation rules are called "reduction rules", and applying the rules "reduces" the term. If a rule is not one-directional, it is called a "conversion rule".

Some combinations of types are equivalent to other combinations of types. When functions are considered "exponentiation", the combinations of types can be written similarly to algebraic identities. Thus, ⁠ ${\mathbb {0} }+A\cong A$ ⁠, ⁠ ${\mathbb {1} }\times A\cong A$ ⁠, ⁠ ${\mathbb {1} }+{\mathbb {1} }\cong {\mathbb {2} }$ ⁠, ⁠ $A^{B+C}\cong A^{B}\times A^{C}$ ⁠, ⁠ $A^{B\times C}\cong (A^{B})^{C}$ ⁠.

### Axioms

Most type theories do not have axioms. This is because a type theory is defined by its rules of inference. This is a source of confusion for people familiar with Set Theory, where a theory is defined by both the rules of inference for a logic (such as first-order logic) and axioms about sets.

Sometimes, a type theory will add a few axioms. An axiom is a judgment that is accepted without a derivation using the rules of inference. They are often added to ensure properties that cannot be added cleanly through the rules.

Axioms can cause problems if they introduce terms without a way to compute on those terms. That is, axioms can interfere with the normalizing property of the type theory.

Some commonly encountered axioms are:

- "Axiom K" ensures "uniqueness of identity proofs". That is, that every term of an identity type is equal to reflexivity.
- "Univalence axiom" holds that equivalence of types is equality of types. The research into this property led to cubical type theory, where the property holds without needing an axiom.
- "Law of excluded middle" is often added to satisfy users who want classical logic, instead of intuitionistic logic.

The axiom of choice does not need to be added to type theory, because in most type theories it can be derived from the rules of inference. This is because of the constructive nature of type theory, where proving that a value exists requires a method to compute the value. The axiom of choice is less powerful in type theory than most set theories, because type theory's functions must be computable and, being syntax-driven, the number of terms in a type must be countable. (See *Axiom of choice § In constructive mathematics*.)

## List of type theories

### Major

- Simply typed lambda calculus which is a higher-order logic
- Intuitionistic type theory
- System F
- LF is often used to define other type theories
- Calculus of constructions and its derivatives

### Minor

- Automath
- ST type theory
- UTT (Luo's unified theory of dependent types)
- some forms of combinatory logic
- others defined in the lambda cube (also known as pure type systems)
- others under the name typed lambda calculus

### Active research

- Homotopy type theory explores equality of types
- Cubical type theory is an implementation of homotopy type theory
