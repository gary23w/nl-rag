---
title: "Curry–Howard correspondence"
source: https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence
domain: lambda-type-theory
license: CC-BY-SA-4.0
tags: lambda calculus, type theory, type system, type inference, hindley-milner, dependent type
fetched: 2026-07-02
---

# Curry–Howard correspondence

In programming language theory and proof theory, the **Curry–Howard correspondence** is a direct relationship between computer programs and mathematical proofs. It is also known as the **Curry–Howard isomorphism** or **equivalence**, or the **proofs-as-programs** and **propositions-** or **formulae-as-types interpretation**.

It is a generalization of a syntactic analogy between systems of formal logic and computational calculi that was first discovered by the American mathematician Haskell Curry and the logician William Alvin Howard. It is the link between logic and computation that is usually attributed to Curry and Howard, although the idea is related to the operational interpretation of intuitionistic logic given in various formulations by L. E. J. Brouwer, Arend Heyting and Andrey Kolmogorov (see Brouwer–Heyting–Kolmogorov interpretation) and Stephen Kleene (see Realizability). The relationship has been extended to include category theory as the three-way **Curry–Howard–Lambek correspondence**.

## Origin, scope, and consequences

The beginnings of the Curry–Howard correspondence lie in several observations:

1. In 1934, Curry observes that the types of the combinators could be seen as axiom-schemes for intuitionistic implicational logic.
2. In 1958, he observes that a certain kind of proof system, referred to as Hilbert-style deduction systems, coincides on some fragment with the typed fragment of a standard model of computation known as combinatory logic.
3. In 1969 Howard observes that another, more "high-level" proof system, referred to as natural deduction, can be directly interpreted in its intuitionistic version as a typed variant of the model of computation known as lambda calculus.

Actually, Howard's first formulation of the isomorphism was referred to (a variant of) Gentzen's sequent calculus. The observation that the isomorphism is best understood with natural deduction, as well as the current formulation of the isomorphism itself, are due to Per Martin-Löf. The Curry–Howard correspondence is the observation that there is an isomorphism between the proof systems, and the models of computation. It is the statement that these two families of formalisms can be considered as identical.

If one abstracts on the peculiarities of either formalism, the following generalization arises: *a proof is a program, and the formula it proves is the type for the program*. More informally, this can be seen as an analogy that states that the return type of a function (i.e., the type of values returned by a function) is analogous to a logical theorem, subject to hypotheses corresponding to the types of the argument values passed to the function; and that the program to compute that function is analogous to a proof of that theorem. This sets a form of logic programming on a rigorous foundation: *proofs can be represented as programs, and especially as lambda terms*, or *proofs can be **run***.

The correspondence has been the starting point of a large range of new research after its discovery, leading to a new class of formal systems designed to act both as a proof system and as a typed programming language based on functional programming. This includes Martin-Löf's intuitionistic type theory and Coquand's calculus of constructions (CoC), two calculi in which proofs are regular objects of the discourse and in which one can state properties of proofs the same way as of any program. This field of research is usually referred to as modern type theory.

Such typed lambda calculi derived from the Curry–Howard paradigm led to software like Rocq in which proofs seen as programs can be formalized, checked, and run.

A converse direction is to *use a program to extract a proof*, given its correctness, an area of research closely related to proof-carrying code. This is only feasible if the programming language the program is written for is very richly typed: the development of such type systems has been partly motivated by the wish to make the Curry–Howard correspondence practically relevant.

The Curry–Howard correspondence also raised new questions regarding the computational content of proof concepts that were not covered by the original works of Curry and Howard. In particular, classical logic has been shown to correspond to the ability to manipulate the continuation of programs and the symmetry of sequent calculus to express the duality between the two evaluation strategies known as call-by-name and call-by-value.

Because of the possibility of writing non-terminating programs, Turing-complete models of computation (such as languages with arbitrary recursive functions) must be interpreted with care, as naive application of the correspondence leads to an inconsistent logic. The best way of dealing with arbitrary computation from a logical point of view is still an actively debated research question, but one popular approach is based on using monads to segregate provably terminating from potentially non-terminating code (an approach that also generalizes to much richer models of computation, and is itself related to modal logic by a natural extension of the Curry–Howard isomorphism). A more radical approach, advocated by total functional programming, is to eliminate unrestricted recursion (and forgo Turing completeness, although still retaining high computational complexity), using more controlled corecursion wherever non-terminating behavior is actually desired.

## General formulation

In its more general formulation, the Curry–Howard correspondence is a correspondence between formal proof calculi and type systems for models of computation. In particular, it splits into two correspondences. One at the level of formulas and types that is independent of which particular proof system or model of computation is considered, and one at the level of proofs and programs which, this time, is specific to the particular choice of proof system and model of computation considered.

At the level of formulas and types, the correspondence says that implication behaves the same as a function type, conjunction as a "product" type (this may be called a tuple, a struct, a list, or some other term depending on the language), disjunction as a sum type (this type may be called a union), the false formula as the empty type and the true formula as a unit type (whose sole member is the null object). Quantifiers correspond to dependent function space or products (as appropriate). This is summarized in the following table:

| Logic side | Programming side |
|---|---|
| formula | type |
| proof | term |
| formula is true | type has an element |
| formula is false | type does not have an element |
| logical constant ⊤ (truth) | unit type |
| logical constant ⊥ (falsehood) | empty type |
| implication | function type |
| conjunction | product type |
| disjunction | sum type |
| universal quantification | dependent product type |
| existential quantification | dependent sum type |

At the level of proof systems and models of computations, the correspondence mainly shows the identity of structure, first, between some particular formulations of systems known as Hilbert-style deduction system and combinatory logic, and, secondly, between some particular formulations of systems known as natural deduction and lambda calculus.

| Logic side | Programming side |
|---|---|
| Hilbert-style deduction system | type system for combinatory logic |
| natural deduction | type system for lambda calculus |

Between the natural deduction system and the lambda calculus there are the following correspondences:

| Logic side | Programming side |
|---|---|
| hypotheses | free variables |
| implication elimination (*modus ponens*) | application |
| implication introduction | abstraction |

## Corresponding systems

### Intuitionistic Hilbert-style deduction systems and typed combinatory logic

It was at the beginning a simple remark in Curry and Feys's 1958 book on combinatory logic: the simplest types for the basic combinators K and S of combinatory logic surprisingly corresponded to the respective axiom schemes *α* → (*β* → *α*) and (*α* → (*β* → *γ*)) → ((*α* → *β*) → (*α* → *γ*)) used in Hilbert-style deduction systems. For this reason, these schemes are now often called axioms K and S. Examples of programs seen as proofs in a Hilbert-style logic are given below.

If one restricts to the implicational intuitionistic fragment, a simple way to formalize logic in Hilbert's style is as follows. Let Γ be a finite collection of formulas, considered as hypotheses. Then δ is *derivable* from Γ, denoted Γ ⊢ δ, in the following cases:

- δ is an hypothesis, i.e. it is a formula of Γ,
- δ is an instance of an axiom scheme; i.e., under the most common axiom system:
  - δ has the form *α* → (*β* → *α*), or
  - δ has the form (*α* → (*β* → *γ*)) → ((*α* → *β*) → (*α* → *γ*)),
- δ follows by deduction, i.e., for some *α*, both *α* → *δ* and *α* are already derivable from Γ (this is the rule of modus ponens)

This can be formalized using inference rules, as in the left column of the following table.

Typed combinatory logic can be formulated using a similar syntax: let Γ be a finite collection of variables, annotated with their types. A term T (also annotated with its type) will depend on these variables [Γ ⊢ T:*δ*] when:

- T is one of the variables in Γ,
- T is a basic combinator; i.e., under the most common combinator basis:
  - T is K:*α* → (*β* → *α*) [where *α* and *β* denote the types of its arguments], or
  - T is S:(*α* → (*β* → *γ*)) → ((*α* → *β*) → (*α* → *γ*)),
- T is the composition of two subterms which depend on the variables in Γ.

The generation rules defined here are given in the right-column below. Curry's remark simply states that both columns are in one-to-one correspondence. The restriction of the correspondence to intuitionistic logic means that some classical tautologies, such as Peirce's law ((*α* → *β*) → *α*) → *α*, are excluded from the correspondence.

| Hilbert-style intuitionistic implicational logic | Typed combinatory logic |
|---|---|
| ${\frac {\alpha \in \Gamma }{\Gamma \vdash \alpha }}\qquad \qquad {\text{Assum}}$ | ${\frac {x:\alpha \in \Gamma }{\Gamma \vdash x:\alpha }}$ |
| ${\frac {}{\Gamma \vdash \alpha \rightarrow (\beta \rightarrow \alpha )}}\qquad {\text{Ax}}_{K}$ | ${\frac {}{\Gamma \vdash K:\alpha \rightarrow (\beta \rightarrow \alpha )}}$ |
| ${\frac {}{\Gamma \vdash (\alpha \!\rightarrow \!(\beta \!\rightarrow \!\gamma ))\!\rightarrow \!((\alpha \!\rightarrow \!\beta )\!\rightarrow \!(\alpha \!\rightarrow \!\gamma ))}}\;{\text{Ax}}_{S}$ | ${\frac {}{\Gamma \vdash S:(\alpha \!\rightarrow \!(\beta \!\rightarrow \!\gamma ))\!\rightarrow \!((\alpha \!\rightarrow \!\beta )\!\rightarrow \!(\alpha \!\rightarrow \!\gamma ))}}$ |
| ${\frac {\Gamma \vdash \alpha \rightarrow \beta \qquad \Gamma \vdash \alpha }{\Gamma \vdash \beta }}\quad {\text{Modus Ponens}}$ | ${\frac {\Gamma \vdash E_{1}:\alpha \rightarrow \beta \qquad \Gamma \vdash E_{2}:\alpha }{\Gamma \vdash E_{1}\;E_{2}:\beta }}$ |

Seen at a more abstract level, the correspondence can be restated as shown in the following table. Especially, the deduction theorem specific to Hilbert-style logic matches the process of abstraction elimination of combinatory logic.

| Logic side | Programming side |
|---|---|
| assumption | variable |
| axiom schemes | combinators |
| modus ponens | application |
| deduction theorem | abstraction elimination |

Thanks to the correspondence, results from combinatory logic can be transferred to Hilbert-style logic and vice versa. For instance, the notion of reduction of terms in combinatory logic can be transferred to Hilbert-style logic and it provides a way to canonically transform proofs into other proofs of the same statement. One can also transfer the notion of normal terms to a notion of normal proofs, expressing that the hypotheses of the axioms never need to be all detached (since otherwise a simplification can happen).

Conversely, the non provability in intuitionistic logic of Peirce's law can be transferred back to combinatory logic: there is no typed term of combinatory logic that is typable with type

((

α

→

β

) →

α

) →

α

.

Results on the completeness of some sets of combinators or axioms can also be transferred. For instance, the fact that the combinator **X** constitutes a one-point basis of (extensional) combinatory logic implies that the single axiom scheme

(((

α

→ (

β

→

γ

)) → ((

α

→

β

) → (

α

→

γ

))) → ((

δ

→ (

ε

→

δ

)) →

ζ

)) →

ζ

,

which is the principal type of **X**, is an adequate replacement to the combination of the axiom schemes

α

→ (

β

→

α

) and

(

α

→ (

β

→

γ

)) → ((

α

→

β

) → (

α

→

γ

)).

### Intuitionistic natural deduction and typed lambda calculus

After Curry emphasized the syntactic correspondence between intuitionistic Hilbert-style deduction and typed combinatory logic, Howard made explicit in 1969 a syntactic analogy between the programs of simply typed lambda calculus and the proofs of natural deduction. Below, the left-hand side formalizes intuitionistic implicational natural deduction as a calculus of sequents (the use of sequents is standard in discussions of the Curry–Howard isomorphism as it allows the deduction rules to be stated more cleanly) with implicit weakening and the right-hand side shows the typing rules of lambda calculus. In the left-hand side, Γ, Γ1 and Γ2 denote ordered sequences of formulas while in the right-hand side, they denote sequences of named (i.e., typed) formulas with all names different.

| Intuitionistic implicational natural deduction | Lambda calculus type assignment rules |
|---|---|
| ${\frac {}{\Gamma _{1},\alpha ,\Gamma _{2}\vdash \alpha }}{\text{Ax}}$ | ${\frac {}{\Gamma _{1},x:\alpha ,\Gamma _{2}\vdash x:\alpha }}$ |
| ${\frac {\Gamma ,\alpha \vdash \beta }{\Gamma \vdash \alpha \rightarrow \beta }}\rightarrow I$ | ${\frac {\Gamma ,x:\alpha \vdash t:\beta }{\Gamma \vdash (\lambda x\!:\!\alpha .~t):\alpha \rightarrow \beta }}$ |
| ${\frac {\Gamma \vdash \alpha \rightarrow \beta \qquad \Gamma \vdash \alpha }{\Gamma \vdash \beta }}\rightarrow E$ | ${\frac {\Gamma \vdash t:\alpha \rightarrow \beta \qquad \Gamma \vdash u:\alpha }{\Gamma \vdash t\;u:\beta }}$ |

To paraphrase the correspondence, proving Γ ⊢ *α* means having a program that, given values with the types listed in Γ, manufactures an object of type *α*. An axiom/hypothesis corresponds to the introduction of a new variable with a new, unconstrained type, the → *I* rule corresponds to function abstraction and the → *E* rule corresponds to function application. Observe that the correspondence is not exact if the context Γ is taken to be a set of formulas as, e.g., the λ-terms λ*x*.λ*y*.*x* and λ*x*.λ*y*.*y* of type *α* → *α* → *α* would not be distinguished in the correspondence. Examples are given below.

Howard showed that the correspondence extends to other connectives of the logic and other constructions of simply typed lambda calculus. Seen at an abstract level, the correspondence can then be summarized as shown in the following table. Especially, it also shows that the notion of normal forms in lambda calculus matches Prawitz's notion of normal deduction in natural deduction, from which it follows that the algorithms for the type inhabitation problem can be turned into algorithms for deciding intuitionistic provability.

| Logic side | Programming side |
|---|---|
| axiom/hypothesis | variable |
| introduction rule | constructor |
| elimination rule | destructor |
| normal deduction | normal form |
| normalisation of deductions | weak normalisation |
| provability | type inhabitation problem |
| intuitionistic tautology | universally inhabited type |

Howard's correspondence naturally extends to other extensions of natural deduction and simply typed lambda calculus. Here is a non-exhaustive list:

- Girard-Reynolds System F as a common language for both second-order propositional logic and polymorphic lambda calculus,
- higher-order logic and Girard's System Fω
- inductive types as algebraic data type
- necessity $\Box$ in modal logic and staged computation
- possibility $\Diamond$ in modal logic and monadic types for effects
- The λI calculus (where abstraction is restricted to *λx*.*E* where *x* has at least one free occurrence in *E)* and **CL**I calculus correspond to relevant logic.
- The local truth (∇) modality in Grothendieck topology or the equivalent "lax" modality (◯) of Benton, Bierman, and de Paiva (1998) correspond to CL-logic describing "computation types".

### Classical logic and control operators

At the time of Curry, and also at the time of Howard, the proofs-as-programs correspondence concerned only intuitionistic logic, i.e. a logic in which, in particular, Peirce's law was *not* deducible. The extension of the correspondence to Peirce's law and hence to classical logic became clear from the work of Griffin on typing operators that capture the evaluation context of a given program execution so that this evaluation context can be later on reinstalled. The basic Curry–Howard-style correspondence for classical logic is given below. Note the correspondence between the double-negation translation used to map classical proofs to intuitionistic logic and the continuation-passing-style translation used to map lambda terms involving control to pure lambda terms. More particularly, call-by-name continuation-passing-style translations relates to Kolmogorov's double negation translation and call-by-value continuation-passing-style translations relates to a kind of double-negation translation due to Kuroda.

| Logic side | Programming side |
|---|---|
| Peirce's law: ((*α* → *β*) → *α*) → *α* | call-with-current-continuation |
| double-negation translation | continuation-passing-style translation |

A finer Curry–Howard correspondence exists for classical logic if one defines classical logic not by adding an axiom such as Peirce's law, but by allowing several conclusions in sequents. In the case of classical natural deduction, there exists a proofs-as-programs correspondence with the typed programs of Parigot's λμ-calculus.

### Sequent calculus

A proofs-as-programs correspondence can be settled for the formalism known as Gentzen's sequent calculus but it is not a correspondence with a well-defined pre-existing model of computation as it was for Hilbert-style and natural deductions.

Sequent calculus is characterized by the presence of left introduction rules, right introduction rule and a cut rule that can be eliminated. The structure of sequent calculus relates to a calculus whose structure is close to the one of some abstract machines. The informal correspondence is as follows:

| Logic side | Programming side |
|---|---|
| cut elimination | reduction in a form of abstract machine |
| right introduction rules | constructors of code |
| left introduction rules | constructors of evaluation stacks |
| priority to right-hand side in cut-elimination | call-by-name reduction |
| priority to left-hand side in cut-elimination | call-by-value reduction |

### Prawitz's 1968 homomorphism

In a paper published in 1970, but drawn from a talk given at the First Scandinavian Logic Symposium, held in Åbo/Turku in 1968, Dag Prawitz defined a homomorphism between natural deduction derivations for minimal and intuitionistic first-order logic and construction terms from a language very similar to typed lambda calculus (the correspondence stems from a proof of soundness of those logics over the language of constructions terms). Although Prawitz's homomorphism is less powerful than the Curry-Howard isomorphism, with a stronger type-language it becomes an isomorphism too, though still missing dependent types. Prawitz was presumably unaware of Howard's work, especially since the talk from which his 1970 paper is drawn was delivered one year before Howard's manuscript started circulating.

### The role of de Bruijn

N. G. de Bruijn used the lambda notation for representing proofs of the theorem checker Automath, and represented propositions as "categories" of their proofs. It was in the late 1960s at the same period of time Howard wrote his manuscript; de Bruijn was likely unaware of Howard's work, and stated the correspondence independently. Some researchers tend to use the term Curry–Howard–de Bruijn correspondence in place of Curry–Howard correspondence.

### BHK interpretation

The BHK interpretation interprets intuitionistic proofs as functions but it does not specify the class of functions relevant for the interpretation. If one takes lambda calculus for this class of function, then the BHK interpretation tells the same as Howard's correspondence between natural deduction and lambda calculus.

### Realizability

Kleene's recursive realizability splits proofs of intuitionistic arithmetic into the pair of a recursive function and of a proof of a formula expressing that the recursive function "realizes", i.e. correctly instantiates the disjunctions and existential quantifiers of the initial formula so that the formula gets true.

Kreisel's modified realizability applies to intuitionistic higher-order predicate logic and shows that the simply typed lambda term inductively extracted from the proof realizes the initial formula. In the case of propositional logic, it coincides with Howard's statement: the extracted lambda term is the proof itself (seen as an untyped lambda term) and the realizability statement is a paraphrase of the fact that the extracted lambda term has the type that the formula means (seen as a type).

Gödel's dialectica interpretation realizes (an extension of) intuitionistic arithmetic with computable functions. The connection with lambda calculus is unclear, even in the case of natural deduction.

### Curry–Howard–Lambek correspondence

Joachim Lambek showed in the early 1970s that the proofs of intuitionistic propositional logic and the combinators of typed combinatory logic share a common equational theory, the theory of cartesian closed categories. The expression Curry–Howard–Lambek correspondence is now used by some people to refer to the relationships between intuitionistic logic, typed lambda calculus and cartesian closed categories. Under this correspondence, objects of a cartesian-closed category can be interpreted as propositions (types), and morphisms as deductions mapping a set of assumptions (typing context) to a valid consequent (well-typed term).

Lambek's correspondence is a correspondence of equational theories, abstracting away from dynamics of computation such as beta reduction and term normalization, and is not the expression of a syntactic identity of structures as it is the case for each of Curry's and Howard's correspondences: i.e. the structure of a well-defined morphism in a cartesian-closed category is not comparable to the structure of a proof of the corresponding judgment in either Hilbert-style logic or natural deduction. For example, it is not possible to state or prove that a morphism is normalizing, establish a Church-Rosser type theorem, or speak of a "strongly normalizing" cartesian closed category. To clarify this distinction, the underlying syntactic structure of cartesian closed categories is rephrased below.

Objects (propositions/types) include

- $\top$ as an object
- given $\alpha$ and $\beta$ as objects, then $\alpha \times \beta$ and $\alpha \rightarrow \beta$ as objects.

Morphisms (deductions/terms) include

- identities: ${\text{id}}_{\alpha }:\alpha \to \alpha$
- composition: if $t:\alpha \to \beta$ and $u:\beta \to \gamma$ are morphisms $u\circ t:\alpha \to \gamma$ is a morphism
- terminal morphisms: $\star _{\alpha }:\alpha \to \top$
- products: if $t:\alpha \to \beta$ and $u:\alpha \to \gamma$ are morphisms, $(t,u):\alpha \to \beta \times \gamma$ is a morphism
- projections: $\pi _{\alpha ,\beta ,1}:\alpha \times \beta \to \alpha$ and $\pi _{\alpha ,\beta ,2}:\alpha \times \beta \to \beta$
- evaluation: ${\text{eval}}_{\alpha ,\beta }:(\alpha \to \beta )\times \alpha \to \beta$
- currying: if $t:\alpha \times \beta \to \gamma$ is a morphism, $\lambda t:\alpha \to \beta \to \gamma$ is a morphism.

Equivalently to the annotations above, well-defined morphisms (typed terms) in any cartesian-closed category can be constructed according to the following typing rules. The usual categorical morphism notation $f:\alpha \to \beta$ is replaced with typing context notation $\alpha \vdash f:\beta$ .

Identity:

${\frac {}{\alpha \vdash {\text{id}}:\alpha }}$

Composition:

${\frac {\alpha \vdash t:\beta \qquad \beta \vdash u:\gamma }{\alpha \vdash u\circ t:\gamma }}$

Unit type (terminal object):

${\frac {}{\alpha \vdash \star :\top }}$

Cartesian product:

${\frac {\alpha \vdash t:\beta \qquad \alpha \vdash u:\gamma }{\alpha \vdash (t,u):\beta \times \gamma }}$

Left and right projection:

${\frac {}{\alpha \times \beta ~\vdash ~\pi _{1}:\alpha }}\qquad {\frac {}{\alpha \times \beta ~\vdash ~\pi _{2}:\beta }}$

Currying:

${\frac {\alpha \times \beta ~\vdash ~t:\gamma }{\alpha \vdash \lambda t:\beta \to \gamma }}$

Application:

${\frac {}{(\alpha \rightarrow \beta )\times \alpha \vdash {\text{eval}}:\beta }}$

Finally, the equations of the category are

- ${\text{id}}\circ t=t$
- $t\circ {\text{id}}=t$
- $(v\circ u)\circ t=v\circ (u\circ t)$
- $\star ={\text{id}}$ (if well-typed)
- $\star \circ u=\star$
- $\pi _{1}\circ (t,u)=t$
- $\pi _{2}\circ (t,u)=u$
- $(\pi _{1},\pi _{2})=id$
- $(t_{1},t_{2})\circ u=(t_{1}\circ u,t_{2}\circ u)$
- ${\text{eval}}\circ (\lambda t\circ \pi _{1},\pi _{2})=t$
- $\lambda {\text{eval}}={\text{id}}$
- $\lambda t\circ u=\lambda (t\circ (u\circ \pi _{1},\pi _{2}))$

These equations imply the following $\eta$ -laws:

- $(\pi _{1}\circ t,\pi _{2}\circ t)=t$
- $\lambda ({\text{eval}}\circ (t\circ \pi _{1},\pi _{2}))=t$

Now, there exists t such that $\alpha _{1}\times \ldots \times \alpha _{n}\vdash t:\beta$ iff $\alpha _{1},\ldots ,\alpha _{n}\vdash \beta$ is provable in implicational intuitionistic logic.

## Examples

Thanks to the Curry–Howard correspondence, a typed expression whose type corresponds to a logical formula is analogous to a proof of that formula. Here are examples.

### The identity combinator seen as a proof of *α* → *α* in Hilbert-style logic

As an example, consider a proof of the theorem *α* → *α*. In lambda calculus, this is the type of the identity function **I** = *λx*.*x* and in combinatory logic, the identity function is obtained by applying **S** = *λfgx*.*fx*(*gx*) twice to **K** = *λxy*.*x*. That is, **I** = ((**S** **K**) **K**). As a description of a proof, this says that the following steps can be used to prove *α* → *α*:

- instantiate the second axiom scheme with the formulas α, *β* → *α* and α to obtain a proof of (*α* → ((*β* → *α*) → *α*)) → ((*α* → (*β* → *α*)) → (*α* → *α*)),
- instantiate the first axiom scheme once with α and *β* → *α* to obtain a proof of *α* → ((*β* → *α*) → *α*),
- instantiate the first axiom scheme a second time with α and β to obtain a proof of *α* → (*β* → *α*),
- apply modus ponens twice to obtain a proof of *α* → *α*

In general, the procedure is that whenever the program contains an application of the form (*P* *Q*), these steps should be followed:

1. First prove theorems corresponding to the types of *P* and *Q*.
2. Since *P* is being applied to *Q*, the type of *P* must have the form *α* → *β* and the type of *Q* must have the form α for some α and β. Therefore, it is possible to detach the conclusion, β, via the modus ponens rule.

### The composition combinator seen as a proof of (*β* → *α*) → (*γ* → *β*) → *γ* → *α* in Hilbert-style logic

As a more complicated example, let's look at the theorem that corresponds to the **B** function. The type of **B** is (*β* → *α*) → (*γ* → *β*) → *γ* → *α*. **B** is equivalent to (**S** (**K** **S**) **K**). This is our roadmap for the proof of the theorem (*β* → *α*) → (*γ* → *β*) → *γ* → *α*.

The first step is to construct (**K** **S**). To make the antecedent of the **K** axiom look like the **S** axiom, set α equal to (*α* → *β* → *γ*) → (*α* → *β*) → *α* → *γ*, and β equal to δ (to avoid variable collisions):

K

:

α

→

β

→

α

K

[

α

= (

α

→

β

→

γ

) → (

α

→

β

) →

α

→

γ

,

β

= δ] : ((

α

→

β

→

γ

) → (

α

→

β

) →

α

→

γ

) →

δ

→ (

α

→

β

→

γ

) → (

α

→

β

) →

α

→

γ

Since the antecedent here is just **S**, the consequent can be detached using Modus Ponens:

K S

:

δ

→ (

α

→

β

→

γ

) → (

α

→

β

) →

α

→

γ

This is the theorem that corresponds to the type of (**K** **S**). Now apply **S** to this expression. Taking **S** as follows

S

: (

α

→

β

→

γ

) → (

α

→

β

) →

α

→

γ

,

put *α* = *δ*, *β* = *α* → *β* → *γ*, and *γ* = (*α* → *β*) → *α* → *γ*, yielding

S

[

α

=

δ

,

β

=

α

→

β

→

γ

,

γ

= (

α

→

β

) →

α

→

γ

] : (

δ

→ (

α

→

β

→

γ

) → (

α

→

β

) →

α

→

γ

) → (

δ

→ (

α

→

β

→

γ

)) → δ → (

α

→

β

) →

α

→

γ

and then detach the consequent:

S (K S)

: (

δ

→

α

→

β

→

γ

) → δ → (

α

→

β

) →

α

→

γ

This is the formula for the type of (**S** (**K** **S**)). A special case of this theorem has *δ* = (*β* → *γ*):

S (K S)

[

δ

=

β

→

γ

] : ((

β

→

γ

) →

α

→

β

→

γ

) → (

β

→

γ

) → (

α

→

β

) →

α

→

γ

This last formula must be applied to **K**. Specialize **K** again, this time by replacing α with (*β* → *γ*) and β with α:

K

:

α

→

β

→

α

K

[

α

=

β

→

γ

,

β

=

α

] : (

β

→

γ

) →

α

→ (

β

→

γ

)

This is the same as the antecedent of the prior formula so, detaching the consequent:

S (K S) K

: (

β

→

γ

) → (

α

→

β

) →

α

→

γ

Switching the names of the variables α and γ gives us

(

β

→

α

) → (

γ

→

β

) →

γ

→

α

which was what remained to prove.

### The normal proof of (*β* → *α*) → (*γ* → *β*) → *γ* → *α* in natural deduction seen as a *λ*-term

The diagram below gives proof of (*β* → *α*) → (*γ* → *β*) → *γ* → *α* in natural deduction and shows how it can be interpreted as the λ-expression λ*a*.λ*b*.λ*g*.(*a* (*b* *g*)) of type (*β* → *α*) → (*γ* → *β*) → *γ* → *α*.

```
                                     a:β → α, b:γ → β, g:γ ⊢ b : γ → β    a:β → α, b:γ → β, g:γ ⊢ g : γ
———————————————————————————————————  ————————————————————————————————————————————————————————————————————
a:β → α, b:γ → β, g:γ ⊢ a : β → α      a:β → α, b:γ → β, g:γ ⊢ b g : β
————————————————————————————————————————————————————————————————————————
               a:β → α, b:γ → β, g:γ ⊢ a (b g) : α
               ————————————————————————————————————
               a:β → α, b:γ → β ⊢ λ g. a (b g) : γ → α
               ————————————————————————————————————————
                        a:β → α ⊢ λ b. λ g. a (b g) : (γ → β) → γ → α
                        ————————————————————————————————————
                                ⊢ λ a. λ b. λ g. a (b g) : (β → α) → (γ → β) → γ → α
```

## Other applications

Recently, the isomorphism has been proposed as a way to define search space partition in genetic programming. The method indexes sets of genotypes (the program trees evolved by the GP system) by their Curry–Howard isomorphic proof (referred to as a species).

As noted by INRIA research director Bernard Lang, the Curry-Howard correspondence constitutes an argument against the patentability of software: since algorithms are mathematical proofs, patentability of the former would imply patentability of the latter. A theorem could be private property; a mathematician would have to pay for using it, and to trust the company that sells it but keeps its proof secret and rejects responsibility for any errors.

## Generalizations

The correspondences listed here go much farther and deeper. For example, cartesian closed categories are generalized by closed monoidal categories. The internal language of these categories is the linear type system (corresponding to linear logic), which generalizes simply-typed lambda calculus as the internal language of cartesian closed categories. Moreover, these can be shown to correspond to cobordisms, which play a vital role in string theory.

An extended set of equivalences is also explored in homotopy type theory. Here, type theory is extended by the univalence axiom ("equivalence is equivalent to equality") which permits homotopy type theory to be used as a foundation for all of mathematics (including set theory and classical logic, providing new ways to discuss the axiom of choice and many other things). That is, the Curry–Howard correspondence that proofs are elements of inhabited types is generalized to the notion of homotopic equivalence of proofs (as paths in space, the identity type or equality type of type theory being interpreted as a path).
