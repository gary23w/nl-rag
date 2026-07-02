---
title: "Type theory (part 1/2)"
source: https://en.wikipedia.org/wiki/Type_theory
domain: lambda-type-theory
license: CC-BY-SA-4.0
tags: lambda calculus, type theory, type system, type inference, hindley-milner, dependent type
fetched: 2026-07-02
part: 1/2
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

The most common construction takes the basic types e {\displaystyle e} ({\displaystyle e}) and t {\displaystyle t} ({\displaystyle t}) for individuals and truth-values, respectively, and defines the set of types recursively as follows:

- if a {\displaystyle a} ({\displaystyle a}) and b {\displaystyle b} ({\displaystyle b}) are types, then so is ⁠ ⟨ a , b ⟩ {\displaystyle \langle a,b\rangle } ({\displaystyle \langle a,b\rangle })⁠;
- nothing except the basic types, and what can be constructed from them by means of the previous clause are types.

A complex type ⟨ a , b ⟩ {\displaystyle \langle a,b\rangle } ({\displaystyle \langle a,b\rangle }) is the type of functions from entities of type a {\displaystyle a} ({\displaystyle a}) to entities of type ⁠ b {\displaystyle b} ({\displaystyle b})⁠. Thus one has types like ⟨ e , t ⟩ {\displaystyle \langle e,t\rangle } ({\displaystyle \langle e,t\rangle }) that are interpreted as elements of the set of functions from entities to truth-values, i.e. indicator functions of sets of entities. An expression of type ⟨ ⟨ e , t ⟩ , t ⟩ {\displaystyle \langle \langle e,t\rangle ,t\rangle } ({\displaystyle \langle \langle e,t\rangle ,t\rangle }) is a function from sets of entities to truth-values, i.e. a (indicator function of a) set of sets. This latter type is standardly taken to be the type of natural language quantifiers, like *everybody* or *nobody* (Montague 1973, Barwise and Cooper 1981).

Type theory with records is a formal semantics representation framework, using *records* to express *type theory types*. It has been used in natural language processing, principally computational semantics and dialogue systems.

Gregory Bateson introduced a theory of logical types into the social sciences; his notions of double bind and logical levels are based on Russell's theory of types.


## Logic

A type theory is a mathematical logic, which is to say it is a collection of rules of inference that result in judgments. Most logics have judgments asserting "The proposition φ {\displaystyle \varphi } ({\displaystyle \varphi }) is true", or "The formula φ {\displaystyle \varphi } ({\displaystyle \varphi }) is a well-formed formula". A type theory has judgments that define types and assign them to a collection of formal objects, known as terms. A term and its type are often written together as ⁠ t e r m : t y p e {\displaystyle \mathrm {term} :{\mathsf {type}}} ({\displaystyle \mathrm {term} :{\mathsf {type}}})⁠.

### Terms

A term in logic is recursively defined as a constant symbol, variable, or a function application, where a term is applied to another term. Constant symbols could include the natural number ⁠ 0 {\displaystyle 0} ({\displaystyle 0})⁠, the Boolean value ⁠ true {\displaystyle {\texttt {true}}} ({\displaystyle {\texttt {true}}})⁠, and functions such as the successor function S {\displaystyle \mathrm {S} } ({\displaystyle \mathrm {S} }) and conditional operator ⁠ i f {\displaystyle \mathrm {if} } ({\displaystyle \mathrm {if} })⁠. Thus some terms could be ⁠ 0 {\displaystyle 0} ({\displaystyle 0})⁠, ⁠ ( S 0 ) {\displaystyle (\mathrm {S} \,0)} ({\displaystyle (\mathrm {S} \,0)})⁠, ⁠ ( S ( S 0 ) ) {\displaystyle (\mathrm {S} \,(\mathrm {S} \,0))} ({\displaystyle (\mathrm {S} \,(\mathrm {S} \,0))})⁠, and ⁠ ( i f true 0 ( S 0 ) ) {\displaystyle (\mathrm {if} \,{\texttt {true}}\,0\,(\mathrm {S} \,0))} ({\displaystyle (\mathrm {if} \,{\texttt {true}}\,0\,(\mathrm {S} \,0))})⁠.

### Judgments

Most type theories have 4 judgments:

- " T {\displaystyle T} ({\displaystyle T}) is a type"
- " t {\displaystyle t} ({\displaystyle t}) is a term of type ⁠ T {\displaystyle T} ({\displaystyle T})⁠"
- "Type T 1 {\displaystyle T_{1}} ({\displaystyle T_{1}}) is equal to type ⁠ T 2 {\displaystyle T_{2}} ({\displaystyle T_{2}})⁠"
- "Terms t 1 {\displaystyle t_{1}} ({\displaystyle t_{1}}) and t 2 {\displaystyle t_{2}} ({\displaystyle t_{2}}) both of type T {\displaystyle T} ({\displaystyle T}) are equal"

Judgments may follow from assumptions. For example, one might say "assuming x {\displaystyle x} ({\displaystyle x}) is a term of type b o o l {\displaystyle {\mathsf {bool}}} ({\displaystyle {\mathsf {bool}}}) and y {\displaystyle y} ({\displaystyle y}) is a term of type ⁠ n a t {\displaystyle {\mathsf {nat}}} ({\displaystyle {\mathsf {nat}}})⁠, it follows that ( if x y y ) {\displaystyle ({\textrm {if}}\,x\,y\,y)} ({\displaystyle ({\textrm {if}}\,x\,y\,y)}) is a term of type ⁠ n a t {\displaystyle {\mathsf {nat}}} ({\displaystyle {\mathsf {nat}}})⁠". Such judgments are formally written with the turnstile symbol ⁠ ⊢ {\displaystyle \vdash } ({\displaystyle \vdash })⁠.

x

:

b

o

o

l

,

y

:

n

a

t

⊢

(

i

f

x

y

y

)

:

n

a

t

{\displaystyle x:{\mathsf {bool}},y:{\mathsf {nat}}\vdash (\mathrm {if} \,x\,y\,y):{\mathsf {nat}}}

If there are no assumptions, there will be nothing to the left of the turnstile.

⊢

S

:

n

a

t

→

n

a

t

{\displaystyle \vdash \mathrm {S}

:{\mathsf {nat}}\to {\mathsf {nat}}}

The list of assumptions on the left is the *context* of the judgment. Capital greek letters, such as Γ {\displaystyle \Gamma } ({\displaystyle \Gamma }) and Δ {\displaystyle \Delta } ({\displaystyle \Delta }), are common choices to represent some or all of the assumptions. The 4 different judgments are thus usually written as follows.

| Formal notation for judgments | Description |
|---|---|
| Γ ⊢ T {\displaystyle \Gamma \vdash T} ({\displaystyle \Gamma \vdash T}) Type | T {\displaystyle T} ({\displaystyle T}) is a type (under assumptions ⁠ Γ {\displaystyle \Gamma } ({\displaystyle \Gamma })⁠). |
| Γ ⊢ t : T {\displaystyle \Gamma \vdash t:T} ({\displaystyle \Gamma \vdash t:T}) | t {\displaystyle t} ({\displaystyle t}) is a term of type T {\displaystyle T} ({\displaystyle T}) (under assumptions ⁠ Γ {\displaystyle \Gamma } ({\displaystyle \Gamma })⁠). |
| Γ ⊢ T 1 = T 2 {\displaystyle \Gamma \vdash T_{1}=T_{2}} ({\displaystyle \Gamma \vdash T_{1}=T_{2}}) | Type T 1 {\displaystyle T_{1}} ({\displaystyle T_{1}}) is equal to type T 2 {\displaystyle T_{2}} ({\displaystyle T_{2}}) (under assumptions ⁠ Γ {\displaystyle \Gamma } ({\displaystyle \Gamma })⁠). |
| Γ ⊢ t 1 = t 2 : T {\displaystyle \Gamma \vdash t_{1}=t_{2}:T} ({\displaystyle \Gamma \vdash t_{1}=t_{2}:T}) | Terms t 1 {\displaystyle t_{1}} ({\displaystyle t_{1}}) and t 2 {\displaystyle t_{2}} ({\displaystyle t_{2}}) are both of type T {\displaystyle T} ({\displaystyle T}) and are equal (under assumptions ⁠ Γ {\displaystyle \Gamma } ({\displaystyle \Gamma })⁠). |

Some textbooks use a triple equal sign ≡ {\displaystyle \equiv } ({\displaystyle \equiv }) to stress that this is judgmental equality and thus an extrinsic notion of equality. The judgments enforce that every term has a type. The type will restrict which rules can be applied to a term.

### Rules of inference

A type theory's inference rules say what judgments can be made, based on the existence of other judgments. Rules are expressed as a Gentzen-style deduction using a horizontal line, with the required input judgments above the line and the resulting judgment below the line. For example, the following inference rule states a substitution rule for judgmental equality. Γ ⊢ t : T 1 Δ ⊢ T 1 = T 2 Γ , Δ ⊢ t : T 2 {\displaystyle {\begin{array}{c}\Gamma \vdash t:T_{1}\qquad \Delta \vdash T_{1}=T_{2}\\\hline \Gamma ,\Delta \vdash t:T_{2}\end{array}}} ({\displaystyle {\begin{array}{c}\Gamma \vdash t:T_{1}\qquad \Delta \vdash T_{1}=T_{2}\\\hline \Gamma ,\Delta \vdash t:T_{2}\end{array}}})The rules are syntactic and work by rewriting. The metavariables ⁠ Γ {\displaystyle \Gamma } ({\displaystyle \Gamma })⁠, ⁠ Δ {\displaystyle \Delta } ({\displaystyle \Delta })⁠, ⁠ t {\displaystyle t} ({\displaystyle t})⁠, ⁠ T 1 {\displaystyle T_{1}} ({\displaystyle T_{1}})⁠, and ⁠ T 2 {\displaystyle T_{2}} ({\displaystyle T_{2}})⁠ may actually consist of complex terms and types that contain many function applications, not just single symbols.

To generate a particular judgment in type theory, there must be a rule to generate it, as well as rules to generate all of that rule's required inputs, and so on. The applied rules form a proof tree, where the top-most rules need no assumptions. One example of a rule that does not require any inputs is one that states the type of a constant term. For example, to assert that there is a term 0 {\displaystyle 0} ({\displaystyle 0}) of type ⁠ n a t {\displaystyle {\mathsf {nat}}} ({\displaystyle {\mathsf {nat}}})⁠, one would write the following. ⊢ 0 : n a t {\displaystyle {\begin{array}{c}\hline \vdash 0:{\mathsf {nat}}\\\end{array}}} ({\displaystyle {\begin{array}{c}\hline \vdash 0:{\mathsf {nat}}\\\end{array}}})

#### Type inhabitation

Generally, the desired conclusion of a proof in type theory is one of type inhabitation. The decision problem of type inhabitation (abbreviated by ⁠ ∃ t . Γ ⊢ t : τ ? {\displaystyle \exists t.\Gamma \vdash t:\tau ?} ({\displaystyle \exists t.\Gamma \vdash t:\tau ?})⁠) is:

Given a context

⁠

Γ

{\displaystyle \Gamma }

⁠

and a type

⁠

τ

{\displaystyle \tau }

⁠

, decide whether there exists a term

⁠

t

{\displaystyle t}

⁠

that can be assigned the type

⁠

τ

{\displaystyle \tau }

⁠

in the type environment

⁠

Γ

{\displaystyle \Gamma }

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
| True | ⊤ {\displaystyle \top } ({\displaystyle \top }) | ⊤ {\displaystyle \top } ({\displaystyle \top }) | Unit Type |
| False | ⊥ {\displaystyle \bot } ({\displaystyle \bot }) | ⊥ {\displaystyle \bot } ({\displaystyle \bot }) | Empty Type |
| Implication | A → B {\displaystyle A\to B} ({\displaystyle A\to B}) | A → B {\displaystyle A\to B} ({\displaystyle A\to B}) | Function |
| Not | ¬ A {\displaystyle \neg A} ({\displaystyle \neg A}) | A → ⊥ {\displaystyle A\to \bot } ({\displaystyle A\to \bot }) | Function to Empty Type |
| And | A ∧ B {\displaystyle A\land B} ({\displaystyle A\land B}) | A × B {\displaystyle A\times B} ({\displaystyle A\times B}) | Product Type |
| Or | A ∨ B {\displaystyle A\lor B} ({\displaystyle A\lor B}) | A + B {\displaystyle A+B} ({\displaystyle A+B}) | Sum Type |
| For All | ∀ a ∈ A , P ( a ) {\displaystyle \forall a\in A,P(a)} ({\displaystyle \forall a\in A,P(a)}) | Π a : A . P ( a ) {\displaystyle \Pi a:A.P(a)} ({\displaystyle \Pi a:A.P(a)}) | Dependent Product |
| Exists | ∃ a ∈ A , P ( a ) {\displaystyle \exists a\in A,P(a)} ({\displaystyle \exists a\in A,P(a)}) | Σ a : A . P ( a ) {\displaystyle \Sigma a:A.P(a)} ({\displaystyle \Sigma a:A.P(a)}) | Dependent Sum |

Because the law of excluded middle does not hold, there is no term of type ⁠ Π A . A + ( A → ⊥ ) {\displaystyle \Pi A.A+(A\to \bot )} ({\displaystyle \Pi A.A+(A\to \bot )})⁠. Likewise, double negation does not hold, so there is no term of type ⁠ Π A . ( ( A → ⊥ ) → ⊥ ) → A {\displaystyle \Pi A.((A\to \bot )\to \bot )\to A} ({\displaystyle \Pi A.((A\to \bot )\to \bot )\to A})⁠.

It is possible to include the law of excluded middle and double negation into a type theory, by rule or assumption. However, terms may not compute down to canonical terms and it will interfere with the ability to determine if two terms are judgementally equal to each other.

#### Constructive mathematics

Per Martin-Löf proposed his intuitionistic type theory as a foundation for constructive mathematics. Constructive mathematics requires when proving "there exists an x {\displaystyle x} ({\displaystyle x}) with property ⁠ P ( x ) {\displaystyle P(x)} ({\displaystyle P(x)})⁠", one must construct a particular x {\displaystyle x} ({\displaystyle x}) and a proof that it has property P {\displaystyle P} ({\displaystyle P}). In type theory, existence is accomplished using the dependent product type, and its proof requires a term of that type.

An example of a non-constructive proof is proof by contradiction. The first step is assuming that x {\displaystyle x} ({\displaystyle x}) does not exist and refuting it by contradiction. The conclusion from that step is "it is not the case that x {\displaystyle x} ({\displaystyle x}) does not exist". The last step is, by double negation, concluding that x {\displaystyle x} ({\displaystyle x}) exists. Constructive mathematics does not allow the last step of removing the double negation to conclude that x {\displaystyle x} ({\displaystyle x}) exists.

Most of the type theories proposed as foundations are constructive, and this includes most of the ones used by proof assistants. It is possible to add non-constructive features to a type theory, by rule or assumption. These include operators on continuations such as call with current continuation. However, these operators tend to break desirable properties such as canonicity and parametricity.

### Curry–Howard correspondence

The Curry–Howard correspondence is the observed similarity between logics and programming languages. The implication in logic, "A → {\displaystyle \to } ({\displaystyle \to }) B" resembles a function from type "A" to type "B". For a variety of logics, the rules are similar to expressions in a programming language's types. The similarity goes farther, as applications of the rules resemble programs in the programming languages. Thus, the correspondence is often summarized as "proofs as programs".

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

The most basic types are called atoms, and a term whose type is an atom is known as an atomic term. Common atomic terms included in type theories are natural numbers, often notated with the type ⁠ n a t {\displaystyle {\mathsf {nat}}} ({\displaystyle {\mathsf {nat}}})⁠, Boolean logic values (⁠ true {\displaystyle {\texttt {true}}} ({\displaystyle {\texttt {true}}})⁠ and ⁠ false {\displaystyle {\texttt {false}}} ({\displaystyle {\texttt {false}}})⁠), notated with the type ⁠ b o o l {\displaystyle {\mathsf {bool}}} ({\displaystyle {\mathsf {bool}}})⁠, and formal variables, whose type may vary. For example, the following may be atomic terms.

- 42 : n a t {\displaystyle 42:{\mathsf {nat}}} ({\displaystyle 42:{\mathsf {nat}}})
- true : b o o l {\displaystyle {\texttt {true}}:{\mathsf {bool}}} ({\displaystyle {\texttt {true}}:{\mathsf {bool}}})
- x : n a t {\displaystyle x:{\mathsf {nat}}} ({\displaystyle x:{\mathsf {nat}}})
- y : b o o l {\displaystyle y:{\mathsf {bool}}} ({\displaystyle y:{\mathsf {bool}}})

#### Function terms

In addition to atomic terms, most modern type theories also allow for functions. Function types introduce an arrow symbol, and are defined inductively: If σ {\displaystyle \sigma } ({\displaystyle \sigma }) and τ {\displaystyle \tau } ({\displaystyle \tau }) are types, then the notation σ → τ {\displaystyle \sigma \to \tau } ({\displaystyle \sigma \to \tau }) is the type of a function which takes a parameter of type σ {\displaystyle \sigma } ({\displaystyle \sigma }) and returns a term of type ⁠ τ {\displaystyle \tau } ({\displaystyle \tau })⁠. Types of this form are known as *simple* types.

Some terms may be declared directly as having a simple type, such as the following term, ⁠ a d d {\displaystyle \mathrm {add} } ({\displaystyle \mathrm {add} })⁠, which takes in two natural numbers in sequence and returns one natural number.

a

d

d

:

n

a

t

→

(

n

a

t

→

n

a

t

)

{\displaystyle \mathrm {add}

:{\mathsf {nat}}\to ({\mathsf {nat}}\to {\mathsf {nat}})}

Strictly speaking, a simple type only allows for one input and one output, so a more faithful reading of the above type is that a d d {\displaystyle \mathrm {add} } ({\displaystyle \mathrm {add} }) is a function which takes in a natural number and returns a function of the form ⁠ n a t → n a t {\displaystyle {\mathsf {nat}}\to {\mathsf {nat}}} ({\displaystyle {\mathsf {nat}}\to {\mathsf {nat}}})⁠. The parentheses clarify that a d d {\displaystyle \mathrm {add} } ({\displaystyle \mathrm {add} }) does not have the type ⁠ ( n a t → n a t ) → n a t {\displaystyle ({\mathsf {nat}}\to {\mathsf {nat}})\to {\mathsf {nat}}} ({\displaystyle ({\mathsf {nat}}\to {\mathsf {nat}})\to {\mathsf {nat}}})⁠, which would be a function which takes in a function of natural numbers and returns a natural number. The convention is that the arrow is right associative, so the parentheses may be dropped from ⁠ a d d {\displaystyle \mathrm {add} } ({\displaystyle \mathrm {add} })⁠'s type.

#### Lambda terms

New function terms may be constructed using lambda expressions, and are called lambda terms. These terms are also defined inductively: a lambda term has the form ⁠ ( λ v . t ) {\displaystyle (\lambda v.t)} ({\displaystyle (\lambda v.t)})⁠, where v {\displaystyle v} ({\displaystyle v}) is a formal variable and t {\displaystyle t} ({\displaystyle t}) is a term, and its type is notated ⁠ σ → τ {\displaystyle \sigma \to \tau } ({\displaystyle \sigma \to \tau })⁠, where σ {\displaystyle \sigma } ({\displaystyle \sigma }) is the type of ⁠ v {\displaystyle v} ({\displaystyle v})⁠, and τ {\displaystyle \tau } ({\displaystyle \tau }) is the type of ⁠ t {\displaystyle t} ({\displaystyle t})⁠. The following lambda term represents a function which doubles an input natural number.

(

λ

x

.

a

d

d

x

x

)

:

n

a

t

→

n

a

t

{\displaystyle (\lambda x.\mathrm {add} \,x\,x):{\mathsf {nat}}\to {\mathsf {nat}}}

The variable is x {\displaystyle x} ({\displaystyle x}) and (implicit from the lambda term's type) must have type ⁠ n a t {\displaystyle {\mathsf {nat}}} ({\displaystyle {\mathsf {nat}}})⁠. The term a d d x x {\displaystyle \mathrm {add} \,x\,x} ({\displaystyle \mathrm {add} \,x\,x}) has type ⁠ n a t {\displaystyle {\mathsf {nat}}} ({\displaystyle {\mathsf {nat}}})⁠, which is seen by applying the function application inference rule twice. Thus, the lambda term has type n a t → n a t {\displaystyle {\mathsf {nat}}\to {\mathsf {nat}}} ({\displaystyle {\mathsf {nat}}\to {\mathsf {nat}}}), which means it is a function taking a natural number as an argument and returning a natural number.

A lambda term is an anonymous function because it lacks a name. The concept of anonymous functions appears in many programming languages.

### Inference Rules

#### Function application

The power of type theories is in specifying how terms may be combined by way of inference rules. Type theories which have functions also have the inference rule of function application: if t {\displaystyle t} ({\displaystyle t}) is a term of type ⁠ σ → τ {\displaystyle \sigma \to \tau } ({\displaystyle \sigma \to \tau })⁠, and s {\displaystyle s} ({\displaystyle s}) is a term of type ⁠ σ {\displaystyle \sigma } ({\displaystyle \sigma })⁠, then the application of t {\displaystyle t} ({\displaystyle t}) to ⁠ s {\displaystyle s} ({\displaystyle s})⁠, often written ⁠ ( t s ) {\displaystyle (t\,s)} ({\displaystyle (t\,s)})⁠, has type ⁠ τ {\displaystyle \tau } ({\displaystyle \tau })⁠. For example, if one knows the type notations ⁠ 0 : nat {\displaystyle 0:{\textsf {nat}}} ({\displaystyle 0:{\textsf {nat}}})⁠, ⁠ 1 : nat {\displaystyle 1:{\textsf {nat}}} ({\displaystyle 1:{\textsf {nat}}})⁠, and ⁠ 2 : nat {\displaystyle 2:{\textsf {nat}}} ({\displaystyle 2:{\textsf {nat}}})⁠, then the following type notations can be deduced from function application.

- ( a d d 1 ) : nat → nat {\displaystyle (\mathrm {add} \,1):{\textsf {nat}}\to {\textsf {nat}}} ({\displaystyle (\mathrm {add} \,1):{\textsf {nat}}\to {\textsf {nat}}})
- ( ( a d d 2 ) 0 ) : nat {\displaystyle ((\mathrm {add} \,2)\,0):{\textsf {nat}}} ({\displaystyle ((\mathrm {add} \,2)\,0):{\textsf {nat}}})
- ( ( a d d 1 ) ( ( a d d 2 ) 0 ) ) : nat {\displaystyle ((\mathrm {add} \,1)((\mathrm {add} \,2)\,0)):{\textsf {nat}}} ({\displaystyle ((\mathrm {add} \,1)((\mathrm {add} \,2)\,0)):{\textsf {nat}}})

Parentheses indicate the order of operations; however, by convention, function application is left associative, so parentheses can be dropped where appropriate. In the case of the three examples above, all parentheses could be omitted from the first two, and the third may simplified to ⁠ a d d 1 ( a d d 2 0 ) : nat {\displaystyle \mathrm {add} \,1\,(\mathrm {add} \,2\,0):{\textsf {nat}}} ({\displaystyle \mathrm {add} \,1\,(\mathrm {add} \,2\,0):{\textsf {nat}}})⁠.

#### Reductions

Type theories that allow for lambda terms also include inference rules known as β {\displaystyle \beta } ({\displaystyle \beta })-reduction and η {\displaystyle \eta } ({\displaystyle \eta })-reduction. They generalize the notion of function application to lambda terms. Symbolically, they are written

- ( λ v . t ) s → t [ v : = s ] {\displaystyle (\lambda v.t)\,s\rightarrow t[v\colon =s]} ({\displaystyle (\lambda v.t)\,s\rightarrow t[v\colon =s]}) (⁠ β {\displaystyle \beta } ({\displaystyle \beta })⁠-reduction).
- ( λ v . t v ) → t {\displaystyle (\lambda v.t\,v)\rightarrow t} ({\displaystyle (\lambda v.t\,v)\rightarrow t}), if v {\displaystyle v} ({\displaystyle v}) is not a free variable in t {\displaystyle t} ({\displaystyle t}) (⁠ η {\displaystyle \eta } ({\displaystyle \eta })⁠-reduction).

The first reduction describes how to evaluate a lambda term: if a lambda expression ( λ v . t ) {\displaystyle (\lambda v.t)} ({\displaystyle (\lambda v.t)}) is applied to a term ⁠ s {\displaystyle s} ({\displaystyle s})⁠, one replaces every occurrence of v {\displaystyle v} ({\displaystyle v}) in t {\displaystyle t} ({\displaystyle t}) with ⁠ s {\displaystyle s} ({\displaystyle s})⁠. The second reduction makes explicit the relationship between lambda expressions and function types: if ( λ v . t v ) {\displaystyle (\lambda v.t\,v)} ({\displaystyle (\lambda v.t\,v)}) is a lambda term, then it must be that t {\displaystyle t} ({\displaystyle t}) is a function term because it is being applied to ⁠ v {\displaystyle v} ({\displaystyle v})⁠. Therefore, the lambda expression is equivalent to just ⁠ t {\displaystyle t} ({\displaystyle t})⁠, as both take in one argument and apply t {\displaystyle t} ({\displaystyle t}) to it.

For example, the following term may be β {\displaystyle \beta } ({\displaystyle \beta })-reduced.

(

λ

x

.

a

d

d

x

x

)

2

→

a

d

d

2

2

{\displaystyle (\lambda x.\mathrm {add} \,x\,x)\,2\rightarrow \mathrm {add} \,2\,2}

In type theories that also establish notions of equality for types and terms, there are corresponding inference rules of β {\displaystyle \beta } ({\displaystyle \beta })-equality and η {\displaystyle \eta } ({\displaystyle \eta })-equality.

### Common terms and types

#### Empty type

The empty type has no terms. The type is usually written ⊥ {\displaystyle \bot } ({\displaystyle \bot }) or ⁠ 0 {\displaystyle \mathbb {0} } ({\displaystyle \mathbb {0} })⁠. One use for the empty type is proofs of type inhabitation. If for a type ⁠ a {\displaystyle a} ({\displaystyle a})⁠, it is consistent to derive a function of type ⁠ a → ⊥ {\displaystyle a\to \bot } ({\displaystyle a\to \bot })⁠, then a {\displaystyle a} ({\displaystyle a}) is *uninhabited*, which is to say it has no terms.

#### Unit type

The unit type has exactly 1 canonical term. The type is written ⊤ {\displaystyle \top } ({\displaystyle \top }) or 1 {\displaystyle \mathbb {1} } ({\displaystyle \mathbb {1} }) and the single canonical term is written ⁠ ∗ {\displaystyle \ast } ({\displaystyle \ast })⁠. The unit type is also used in proofs of type inhabitation. If for a type ⁠ a {\displaystyle a} ({\displaystyle a})⁠, it is consistent to derive a function of type ⁠ ⊤ → a {\displaystyle \top \to a} ({\displaystyle \top \to a})⁠, then a {\displaystyle a} ({\displaystyle a}) is *inhabited*, which is to say it must have one or more terms.

#### Boolean type

The Boolean type has exactly 2 canonical terms. The type is usually written bool {\displaystyle {\textsf {bool}}} ({\displaystyle {\textsf {bool}}}) or B {\displaystyle \mathbb {B} } ({\displaystyle \mathbb {B} }) or ⁠ 2 {\displaystyle \mathbb {2} } ({\displaystyle \mathbb {2} })⁠. The canonical terms are usually t r u e {\displaystyle \mathrm {true} } ({\displaystyle \mathrm {true} }) and ⁠ f a l s e {\displaystyle \mathrm {false} } ({\displaystyle \mathrm {false} })⁠.

#### Natural numbers

Natural numbers are usually implemented in the style of Peano Arithmetic. There is a canonical term 0 : n a t {\displaystyle 0:{\mathsf {nat}}} ({\displaystyle 0:{\mathsf {nat}}}) for zero. Canonical values larger than zero use iterated applications of a successor function ⁠ S : n a t → n a t {\displaystyle \mathrm {S} :{\mathsf {nat}}\to {\mathsf {nat}}} ({\displaystyle \mathrm {S} :{\mathsf {nat}}\to {\mathsf {nat}}})⁠.

### Type constructors

Some type theories allow for types of complex terms, such as functions or lists, to depend on the types of its arguments; these are called type constructors. For example, a type theory could have the dependent type ⁠ l i s t a {\displaystyle {\mathsf {list}}\,a} ({\displaystyle {\mathsf {list}}\,a})⁠, which should correspond to lists of terms, where each term must have type ⁠ a {\displaystyle a} ({\displaystyle a})⁠. In this case, l i s t {\displaystyle {\mathsf {list}}} ({\displaystyle {\mathsf {list}}}) has the kind ⁠ U → U {\displaystyle U\to U} ({\displaystyle U\to U})⁠, where U {\displaystyle U} ({\displaystyle U}) denotes the universe of all types in the theory.

#### Product type

The product type, ⁠ × {\displaystyle \times } ({\displaystyle \times })⁠, depends on two types, and its terms are commonly written as ordered pairs ⁠ ( s , t ) {\displaystyle (s,t)} ({\displaystyle (s,t)})⁠. The pair ( s , t ) {\displaystyle (s,t)} ({\displaystyle (s,t)}) has the product type ⁠ σ × τ {\displaystyle \sigma \times \tau } ({\displaystyle \sigma \times \tau })⁠, where σ {\displaystyle \sigma } ({\displaystyle \sigma }) is the type of s {\displaystyle s} ({\displaystyle s}) and τ {\displaystyle \tau } ({\displaystyle \tau }) is the type of ⁠ t {\displaystyle t} ({\displaystyle t})⁠. Each product type is then usually defined with eliminator functions f i r s t : σ × τ → σ {\displaystyle \mathrm {first} :\sigma \times \tau \to \sigma } ({\displaystyle \mathrm {first} :\sigma \times \tau \to \sigma }) and ⁠ s e c o n d : σ × τ → τ {\displaystyle \mathrm {second} :\sigma \times \tau \to \tau } ({\displaystyle \mathrm {second} :\sigma \times \tau \to \tau })⁠.

- f i r s t ( s , t ) {\displaystyle \mathrm {first} \,(s,t)} ({\displaystyle \mathrm {first} \,(s,t)}) returns ⁠ s {\displaystyle s} ({\displaystyle s})⁠, and
- s e c o n d ( s , t ) {\displaystyle \mathrm {second} \,(s,t)} ({\displaystyle \mathrm {second} \,(s,t)}) returns ⁠ t {\displaystyle t} ({\displaystyle t})⁠.

Besides ordered pairs, this type is used for the concepts of logical conjunction and intersection.

#### Sum type

The sum type is written as either + {\displaystyle +} ({\displaystyle +}) or ⁠ ⊔ {\displaystyle \sqcup } ({\displaystyle \sqcup })⁠. In programming languages, sum types may be referred to as tagged unions. Each type σ ⊔ τ {\displaystyle \sigma \sqcup \tau } ({\displaystyle \sigma \sqcup \tau }) is usually defined with constructors l e f t : σ → ( σ ⊔ τ ) {\displaystyle \mathrm {left} :\sigma \to (\sigma \sqcup \tau )} ({\displaystyle \mathrm {left} :\sigma \to (\sigma \sqcup \tau )}) and ⁠ r i g h t : τ → ( σ ⊔ τ ) {\displaystyle \mathrm {right} :\tau \to (\sigma \sqcup \tau )} ({\displaystyle \mathrm {right} :\tau \to (\sigma \sqcup \tau )})⁠, which are injective, and an eliminator function m a t c h : ( σ → ρ ) → ( τ → ρ ) → ( σ ⊔ τ ) → ρ {\displaystyle \mathrm {match} :(\sigma \to \rho )\to (\tau \to \rho )\to (\sigma \sqcup \tau )\to \rho } ({\displaystyle \mathrm {match} :(\sigma \to \rho )\to (\tau \to \rho )\to (\sigma \sqcup \tau )\to \rho }) such that

- m a t c h f g ( l e f t x ) {\displaystyle \mathrm {match} \,f\,g\,(\mathrm {left} \,x)} ({\displaystyle \mathrm {match} \,f\,g\,(\mathrm {left} \,x)}) returns ⁠ f x {\displaystyle f\,x} ({\displaystyle f\,x})⁠, and
- m a t c h f g ( r i g h t y ) {\displaystyle \mathrm {match} \,f\,g\,(\mathrm {right} \,y)} ({\displaystyle \mathrm {match} \,f\,g\,(\mathrm {right} \,y)}) returns ⁠ g y {\displaystyle g\,y} ({\displaystyle g\,y})⁠.

The sum type is used for the concepts of logical disjunction and union.

### Polymorphic types

Some theories also allow terms to have their definitions depend on types. For instance, an identity function of any type could be written as ⁠ λ x . x : ∀ α . α → α {\displaystyle \lambda x.x:\forall \alpha .\alpha \to \alpha } ({\displaystyle \lambda x.x:\forall \alpha .\alpha \to \alpha })⁠. The function is said to be polymorphic in ⁠ α {\displaystyle \alpha } ({\displaystyle \alpha })⁠, or generic in ⁠ x {\displaystyle x} ({\displaystyle x})⁠.

As another example, consider a function ⁠ a p p e n d {\displaystyle \mathrm {append} } ({\displaystyle \mathrm {append} })⁠, which takes in a l i s t a {\displaystyle {\mathsf {list}}\,a} ({\displaystyle {\mathsf {list}}\,a}) and a term of type ⁠ a {\displaystyle a} ({\displaystyle a})⁠, and returns the list with the element at the end. The type annotation of such a function would be ⁠ a p p e n d : ∀ a . l i s t a → a → l i s t a {\displaystyle \mathrm {append} :\forall \,a.{\mathsf {list}}\,a\to a\to {\mathsf {list}}\,a} ({\displaystyle \mathrm {append} :\forall \,a.{\mathsf {list}}\,a\to a\to {\mathsf {list}}\,a})⁠, which can be read as "for any type ⁠ a {\displaystyle a} ({\displaystyle a})⁠, pass in a l i s t a {\displaystyle {\mathsf {list}}\,a} ({\displaystyle {\mathsf {list}}\,a}) and an ⁠ a {\displaystyle a} ({\displaystyle a})⁠, and return a ⁠ l i s t a {\displaystyle {\mathsf {list}}\,a} ({\displaystyle {\mathsf {list}}\,a})⁠". Here a p p e n d {\displaystyle \mathrm {append} } ({\displaystyle \mathrm {append} }) is polymorphic in ⁠ a {\displaystyle a} ({\displaystyle a})⁠.

#### Products and sums

With polymorphism, the eliminator functions can be defined generically for *all* product types as f i r s t : ∀ σ τ . σ × τ → σ {\displaystyle \mathrm {first} :\forall \,\sigma \,\tau .\sigma \times \tau \to \sigma } ({\displaystyle \mathrm {first} :\forall \,\sigma \,\tau .\sigma \times \tau \to \sigma }) and ⁠ s e c o n d : ∀ σ τ . σ × τ → τ {\displaystyle \mathrm {second} :\forall \,\sigma \,\tau .\sigma \times \tau \to \tau } ({\displaystyle \mathrm {second} :\forall \,\sigma \,\tau .\sigma \times \tau \to \tau })⁠.

- f i r s t ( s , t ) {\displaystyle \mathrm {first} \,(s,t)} ({\displaystyle \mathrm {first} \,(s,t)}) returns ⁠ s {\displaystyle s} ({\displaystyle s})⁠, and
- s e c o n d ( s , t ) {\displaystyle \mathrm {second} \,(s,t)} ({\displaystyle \mathrm {second} \,(s,t)}) returns ⁠ t {\displaystyle t} ({\displaystyle t})⁠.

Likewise, the sum type constructors can be defined for all valid types of sum members as l e f t : ∀ σ τ . σ → ( σ ⊔ τ ) {\displaystyle \mathrm {left} :\forall \,\sigma \,\tau .\sigma \to (\sigma \sqcup \tau )} ({\displaystyle \mathrm {left} :\forall \,\sigma \,\tau .\sigma \to (\sigma \sqcup \tau )}) and ⁠ r i g h t : ∀ σ τ . τ → ( σ ⊔ τ ) {\displaystyle \mathrm {right} :\forall \,\sigma \,\tau .\tau \to (\sigma \sqcup \tau )} ({\displaystyle \mathrm {right} :\forall \,\sigma \,\tau .\tau \to (\sigma \sqcup \tau )})⁠, which are injective, and the eliminator function can be given as m a t c h : ∀ σ τ ρ . ( σ → ρ ) → ( τ → ρ ) → ( σ ⊔ τ ) → ρ {\displaystyle \mathrm {match} :\forall \,\sigma \,\tau \,\rho .(\sigma \to \rho )\to (\tau \to \rho )\to (\sigma \sqcup \tau )\to \rho } ({\displaystyle \mathrm {match} :\forall \,\sigma \,\tau \,\rho .(\sigma \to \rho )\to (\tau \to \rho )\to (\sigma \sqcup \tau )\to \rho }) such that

- m a t c h f g ( l e f t x ) {\displaystyle \mathrm {match} \,f\,g\,(\mathrm {left} \,x)} ({\displaystyle \mathrm {match} \,f\,g\,(\mathrm {left} \,x)}) returns ⁠ f x {\displaystyle f\,x} ({\displaystyle f\,x})⁠, and
- m a t c h f g ( r i g h t y ) {\displaystyle \mathrm {match} \,f\,g\,(\mathrm {right} \,y)} ({\displaystyle \mathrm {match} \,f\,g\,(\mathrm {right} \,y)}) returns ⁠ g y {\displaystyle g\,y} ({\displaystyle g\,y})⁠.

### Dependent typing

Some theories also permit types to be dependent on terms instead of types. For example, a theory could have the type ⁠ v e c t o r n {\displaystyle {\mathsf {vector}}\,n} ({\displaystyle {\mathsf {vector}}\,n})⁠, where n {\displaystyle n} ({\displaystyle n}) is a term of type n a t {\displaystyle {\mathsf {nat}}} ({\displaystyle {\mathsf {nat}}}) encoding the length of the vector. This allows for greater specificity and type safety: functions with vector length restrictions or length matching requirements, such as the dot product, can encode this requirement as part of the type.

There are foundational issues that can arise from dependent types if a theory is not careful about what dependences are allowed, such as Girard's Paradox. The logician Henk Barendegt introduced the lambda cube as a framework for studying various restrictions and levels of dependent typing.

#### Dependent products and sums

Two common type dependences, dependent product and dependent sum types, allow for the theory to encode BHK intuitionistic logic by acting as equivalents to universal and existential quantification; this is formalized by Curry–Howard correspondence. As they also connect to products and sums in set theory, they are often written with the symbols Π {\displaystyle \Pi } ({\displaystyle \Pi }) and ⁠ Σ {\displaystyle \Sigma } ({\displaystyle \Sigma })⁠, respectively.

Sum types are seen in dependent pairs, where the second type depends on the value of the first term. This arises naturally in computer science where functions may return different types of outputs based on the input. For example, the Boolean type is usually defined with an eliminator function ⁠ i f {\displaystyle \mathrm {if} } ({\displaystyle \mathrm {if} })⁠, which takes three arguments and behaves as follows.

- i f true x y {\displaystyle \mathrm {if} \,{\texttt {true}}\,x\,y} ({\displaystyle \mathrm {if} \,{\texttt {true}}\,x\,y}) returns ⁠ x {\displaystyle x} ({\displaystyle x})⁠, and
- i f false x y {\displaystyle \mathrm {if} \,{\texttt {false}}\,x\,y} ({\displaystyle \mathrm {if} \,{\texttt {false}}\,x\,y}) returns ⁠ y {\displaystyle y} ({\displaystyle y})⁠.

Ordinary definitions of i f {\displaystyle \mathrm {if} } ({\displaystyle \mathrm {if} }) require x {\displaystyle x} ({\displaystyle x}) and y {\displaystyle y} ({\displaystyle y}) to have the same type. If the type theory allows for dependent types, then it is possible to define a dependent type x : b o o l ⊢ T F x : U → U → U {\displaystyle x:{\mathsf {bool}}\,\vdash \,\mathrm {TF} \,x:U\to U\to U} ({\displaystyle x:{\mathsf {bool}}\,\vdash \,\mathrm {TF} \,x:U\to U\to U}) such that

- T F true σ τ {\displaystyle \mathrm {TF} \,{\texttt {true}}\,\sigma \,\tau } ({\displaystyle \mathrm {TF} \,{\texttt {true}}\,\sigma \,\tau }) returns ⁠ σ {\displaystyle \sigma } ({\displaystyle \sigma })⁠, and
- T F false σ τ {\displaystyle \mathrm {TF} \,{\texttt {false}}\,\sigma \,\tau } ({\displaystyle \mathrm {TF} \,{\texttt {false}}\,\sigma \,\tau }) returns ⁠ τ {\displaystyle \tau } ({\displaystyle \tau })⁠.

The type of i f {\displaystyle \mathrm {if} } ({\displaystyle \mathrm {if} }) may then be written as ⁠ ∀ σ τ . Π x : b o o l . σ → τ → T F x σ τ {\displaystyle \forall \,\sigma \,\tau .\Pi _{x:{\mathsf {bool}}}.\sigma \to \tau \to \mathrm {TF} \,x\,\sigma \,\tau } ({\displaystyle \forall \,\sigma \,\tau .\Pi _{x:{\mathsf {bool}}}.\sigma \to \tau \to \mathrm {TF} \,x\,\sigma \,\tau })⁠.

#### Identity type

Following the notion of Curry–Howard Correspondence, the identity type is a type introduced to mirror propositional equivalence, as opposed to the judgmental (syntactic) equivalence that type theory already provides.

An identity type requires two terms of the same type and is written with the symbol ⁠ = {\displaystyle =} ({\displaystyle =})⁠. For example, if x + 1 {\displaystyle x+1} ({\displaystyle x+1}) and 1 + x {\displaystyle 1+x} ({\displaystyle 1+x}) are terms, then x + 1 = 1 + x {\displaystyle x+1=1+x} ({\displaystyle x+1=1+x}) is a possible type. Canonical terms are created with a reflexivity function, ⁠ r e f l {\displaystyle \mathrm {refl} } ({\displaystyle \mathrm {refl} })⁠. For a term ⁠ t {\displaystyle t} ({\displaystyle t})⁠, the call r e f l t {\displaystyle \mathrm {refl} \,t} ({\displaystyle \mathrm {refl} \,t}) returns the canonical term inhabiting the type ⁠ t = t {\displaystyle t=t} ({\displaystyle t=t})⁠.

The complexities of equality in type theory make it an active research topic; homotopy type theory is a notable area of research that mainly deals with equality in type theory.

#### Inductive types

Inductive types are a general template for creating a large variety of types. In fact, all the types described above and more can be defined using the rules of inductive types. Two methods of generating inductive types are induction-recursion and induction-induction. A method that only uses lambda terms is Scott encoding.

Some proof assistants, such as Rocq (previously known as *Coq*) and Lean, are based on the calculus for inductive constructions, which is a calculus of constructions with inductive types.
