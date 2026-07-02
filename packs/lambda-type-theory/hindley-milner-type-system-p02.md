---
title: "Hindley–Milner type system (part 2/2)"
source: https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system
domain: lambda-type-theory
license: CC-BY-SA-4.0
tags: lambda calculus, type theory, type system, type inference, hindley-milner, dependent type
fetched: 2026-07-02
part: 2/2
---

## Proving the algorithm

In the previous section, while sketching the algorithm its proof was hinted at with metalogical argumentation. While this leads to an efficient algorithm J, it is not clear whether the algorithm properly reflects the deduction systems D or S which serve as a semantic base line.

The most critical point in the above argumentation is the refinement of monotype variables bound by the context. For instance, the algorithm boldly changes the context while inferring e.g. λ f . ( f   1 ) {\displaystyle \lambda f.(f\ 1)} ({\displaystyle \lambda f.(f\ 1)}), because the monotype variable added to the context for the parameter f {\displaystyle f} ({\displaystyle f}) later needs to be refined to i n t → β {\displaystyle int\rightarrow \beta } ({\displaystyle int\rightarrow \beta }) when handling application. The problem is that the deduction rules do not allow such a refinement. Arguing that the refined type could have been added earlier instead of the monotype variable is an expedient at best.

The key to reaching a formally satisfying argument is to properly include the context within the refinement. Formally, typing is compatible with substitution of free type variables.

Γ

⊢

S

e

:

τ

⟹

S

Γ

⊢

S

e

:

S

τ

{\displaystyle \Gamma \vdash _{S}e:\tau \quad \Longrightarrow \quad S\Gamma \vdash _{S}e:S\tau }

To refine the free variables thus means to refine the whole typing.

### Algorithm W

From there, a proof of algorithm J leads to algorithm W, which only makes the side effects imposed by the procedure union {\displaystyle {\textit {union}}} ({\displaystyle {\textit {union}}}) explicit by expressing its serial composition by means of the substitutions S i {\displaystyle S_{i}} ({\displaystyle S_{i}}). The presentation of algorithm W in the sidebar still makes use of side effects in the operations set in italic, but these are now limited to generating fresh symbols. The form of judgement is Γ ⊢ e : τ , S {\displaystyle \Gamma \vdash e:\tau ,S} ({\displaystyle \Gamma \vdash e:\tau ,S}), denoting a function with a context and expression as parameter producing a monotype together with a substitution. mgu {\displaystyle {\textsf {mgu}}} ({\displaystyle {\textsf {mgu}}}) is a side-effect free version of union {\displaystyle {\textit {union}}} ({\displaystyle {\textit {union}}}) producing a substitution which is the most general unifier.

While algorithm W is normally considered to be *the* HM algorithm and is often directly presented after the rule system in literature, its purpose is described by Milner on P. 369 as follows:

As it stands, W is hardly an efficient algorithm; substitutions are applied too often. It was formulated to aid the proof of soundness. We now present a simpler algorithm J which simulates W in a precise sense.

While he considered W more complicated and less efficient, he presented it in his publication before J. It has its merits when side effects are unavailable or unwanted. W is also needed to prove completeness, which is factored by him into the soundness proof.

### Proof obligations

Before formulating the proof obligations, a deviation between the rules systems D and S and the algorithms presented needs to be emphasized.

While the development above sort of misused the monotypes as "open" proof variables, the possibility that proper monotype variables might be harmed was sidestepped by introducing fresh variables and hoping for the best. But there's a catch: One of the promises made was that these fresh variables would be "kept in mind" as such. This promise is not fulfilled by the algorithm.

Having a context 1 : i n t ,   f : α {\displaystyle 1:int,\ f:\alpha } ({\displaystyle 1:int,\ f:\alpha }), the expression f   1 {\displaystyle f\ 1} ({\displaystyle f\ 1}) cannot be typed in either ⊢ D {\displaystyle \vdash _{D}} ({\displaystyle \vdash _{D}}) or ⊢ S {\displaystyle \vdash _{S}} ({\displaystyle \vdash _{S}}), but the algorithms come up with the type β {\displaystyle \beta } ({\displaystyle \beta }), where W additionally delivers the substitution { α ↦ i n t → β } {\displaystyle \left\{\alpha \mapsto int\rightarrow \beta \right\}} ({\displaystyle \left\{\alpha \mapsto int\rightarrow \beta \right\}}), meaning that the algorithm fails to detect all type errors. This omission can easily be fixed by more carefully distinguishing proof variables and monotype variables.

The authors were well aware of the problem but decided not to fix it. One might assume a pragmatic reason behind this. While more properly implementing the type inference would have enabled the algorithm to deal with abstract monotypes, they were not needed for the intended application where none of the items in a preexisting context have free variables. In this light, the unneeded complication was dropped in favor of a simpler algorithm. The remaining downside is that the proof of the algorithm with respect to the rule system is less general and can only be made for contexts with f r e e ( Γ ) = ∅ {\displaystyle free(\Gamma )=\emptyset } ({\displaystyle free(\Gamma )=\emptyset }) as a side condition.

(Correctness) Γ ⊢ W e : τ , S ⟹ Γ ⊢ S e : τ (Completeness) Γ ⊢ S e : τ ⟹ Γ ⊢ W e : τ ′ , S forall   τ   where   ∅ ¯ ( τ ′ ) ⊑ τ {\displaystyle {\begin{array}{lll}{\text{(Correctness)}}&\Gamma \vdash _{W}e:\tau ,S&\quad \Longrightarrow \quad \Gamma \vdash _{S}e:\tau \\{\text{(Completeness)}}&\Gamma \vdash _{S}e:\tau &\quad \Longrightarrow \quad \Gamma \vdash _{W}e:\tau ',S\quad \quad {\text{forall}}\ \tau \ {\text{where}}\ {\overline {\emptyset }}(\tau ')\sqsubseteq \tau \end{array}}} ({\displaystyle {\begin{array}{lll}{\text{(Correctness)}}&\Gamma \vdash _{W}e:\tau ,S&\quad \Longrightarrow \quad \Gamma \vdash _{S}e:\tau \\{\text{(Completeness)}}&\Gamma \vdash _{S}e:\tau &\quad \Longrightarrow \quad \Gamma \vdash _{W}e:\tau ',S\quad \quad {\text{forall}}\ \tau \ {\text{where}}\ {\overline {\emptyset }}(\tau ')\sqsubseteq \tau \end{array}}})

The side condition in the completeness obligation addresses how the deduction may give many types, while the algorithm always produces one. At the same time, the side condition demands that the type inferred is actually the most general.

To properly prove the obligations one needs to strengthen them first to allow activating the substitution lemma threading the substitution S {\displaystyle S} ({\displaystyle S}) through ⊢ S {\displaystyle \vdash _{S}} ({\displaystyle \vdash _{S}}) and ⊢ W {\displaystyle \vdash _{W}} ({\displaystyle \vdash _{W}}). From there, the proofs are by induction over the expression.

Another proof obligation is the substitution lemma itself, i.e. the substitution of the typing, which finally establishes the all-quantification. The later cannot formally be proven, since no such syntax is at hand.


## Extensions

### Recursive definitions

To make programming practical recursive functions are needed. A central property of the lambda calculus is that recursive definitions are not directly available, but can instead be expressed with a fixed point combinator. However, the fixpoint combinator cannot be formulated in a typed version of the lambda calculus without having a disastrous effect on the system as outlined below.

#### Typing rule

The original paper shows recursion can be realized by a combinator f i x : ∀ α . ( α → α ) → α {\displaystyle {\mathit {fix}}:\forall \alpha .(\alpha \rightarrow \alpha )\rightarrow \alpha } ({\displaystyle {\mathit {fix}}:\forall \alpha .(\alpha \rightarrow \alpha )\rightarrow \alpha }). A possible recursive definition could thus be formulated as r e c   v = e 1   i n   e 2   ::= l e t   v = f i x ( λ v . e 1 )   i n   e 2 {\displaystyle {\mathtt {rec}}\ v=e_{1}\ {\mathtt {in}}\ e_{2}\ ::={\mathtt {let}}\ v={\mathit {fix}}(\lambda v.e_{1})\ {\mathtt {in}}\ e_{2}} ({\displaystyle {\mathtt {rec}}\ v=e_{1}\ {\mathtt {in}}\ e_{2}\ ::={\mathtt {let}}\ v={\mathit {fix}}(\lambda v.e_{1})\ {\mathtt {in}}\ e_{2}}).

Alternatively an extension of the expression syntax and an extra typing rule is possible:

Γ

,

Γ

′

⊢

e

1

:

τ

1

…

Γ

,

Γ

′

⊢

e

n

:

τ

n

Γ

,

Γ

″

⊢

e

:

τ

Γ

⊢

r

e

c

v

1

=

e

1

a

n

d

…

a

n

d

v

n

=

e

n

i

n

e

:

τ

[

R

e

c

]

{\displaystyle \displaystyle {\frac {\Gamma ,\Gamma '\vdash e_{1}:\tau _{1}\quad \dots \quad \Gamma ,\Gamma '\vdash e_{n}:\tau _{n}\quad \Gamma ,\Gamma ''\vdash e:\tau }{\Gamma \ \vdash \ {\mathtt {rec}}\ v_{1}=e_{1}\ {\mathtt {and}}\ \dots \ {\mathtt {and}}\ v_{n}=e_{n}\ {\mathtt {in}}\ e:\tau }}\quad [{\mathtt {Rec}}]}

where

- Γ ′ = v 1 : τ 1 ,   … ,   v n : τ n {\displaystyle \Gamma '=v_{1}:\tau _{1},\ \dots ,\ v_{n}:\tau _{n}} ({\displaystyle \Gamma '=v_{1}:\tau _{1},\ \dots ,\ v_{n}:\tau _{n}})
- Γ ″ = v 1 : Γ ¯ (   τ 1   ) ,   … ,   v n : Γ ¯ (   τ n   ) {\displaystyle \Gamma ''=v_{1}:{\bar {\Gamma }}(\ \tau _{1}\ ),\ \dots ,\ v_{n}:{\bar {\Gamma }}(\ \tau _{n}\ )} ({\displaystyle \Gamma ''=v_{1}:{\bar {\Gamma }}(\ \tau _{1}\ ),\ \dots ,\ v_{n}:{\bar {\Gamma }}(\ \tau _{n}\ )})

basically merging [ A b s ] {\displaystyle [{\mathtt {Abs}}]} ({\displaystyle [{\mathtt {Abs}}]}) and [ L e t ] {\displaystyle [{\mathtt {Let}}]} ({\displaystyle [{\mathtt {Let}}]}) while including the recursively defined variables in monotype positions where they occur to the left of the i n {\displaystyle {\mathtt {in}}} ({\displaystyle {\mathtt {in}}}) but as polytypes to the right of it.

#### Consequences

While the above is straightforward it does come at a price.

Type theory connects lambda calculus with computation and logic. The easy modification above has effects on both:

- The strong normalisation property is invalidated, because non-terminating terms can be formulated.
- The logic collapses because the type ∀ a . a {\displaystyle \forall a.a} ({\displaystyle \forall a.a}) becomes inhabited.

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

Haskell introduces one higher level named kind. In standard Haskell, kinds are inferred and used for little more than to describe the arity of type constructors. e.g. a list type constructor is thought of as mapping a type (the type of its elements) to another type (the type of the list containing said elements); notationally this is expressed as ∗ → ∗ {\displaystyle *\to *} ({\displaystyle *\to *}). Language extensions are available which extend kinds to emulate features of a dependent type system.

### Subtyping

Attempts to combine subtyping and type inference have caused quite some frustration. It is straightforward to accumulate and propagate subtyping constraints (as opposed to type equality constraints), making the resulting constraints part of the inferred typing schemes, for example ∀ α .   ( α ≤ T ) ⇒ α → α {\displaystyle \forall \alpha .\ (\alpha \leq T)\Rightarrow \alpha \rightarrow \alpha } ({\displaystyle \forall \alpha .\ (\alpha \leq T)\Rightarrow \alpha \rightarrow \alpha }), where α ≤ T {\displaystyle \alpha \leq T} ({\displaystyle \alpha \leq T}) is a constraint on the type variable α {\displaystyle \alpha } ({\displaystyle \alpha }). However, because type variables are no longer unified eagerly in this approach, it tends to generate large and unwieldy typing schemes containing many useless type variables and constraints, making them hard to read and understand. Therefore, considerable effort was put into simplifying such typing schemes and their constraints, using techniques similar to those of nondeterministic finite automaton (NFA) simplification (useful in the presence of inferred recursive types). More recently, Dolan and Mycroft formalized the relationship between typing scheme simplification and NFA simplification and showed that an algebraic take on the formalization of subtyping allowed generating compact principal typing schemes for an ML-like language (called MLsub). Notably, their proposed typing scheme used a restricted form of union and intersection types instead of explicit constraints. Parreaux later claimed that this algebraic formulation was equivalent to a relatively simple algorithm resembling Algorithm W, and that the use of union and intersection types was not essential.

On the other hand, type inference has proven more difficult in the context of object-oriented programming languages, because object methods tend to require first-class polymorphism in the style of System F (where type inference is undecidable) and because of features like F-bounded polymorphism. Consequently, type systems with subtyping enabling object-oriented programming, such as Cardelli's system F <: {\displaystyle F_{<:}} ({\displaystyle F_{<:}}), do not support HM-style type inference.

Row polymorphism can be used as an alternative to subtyping for supporting language features like structural records. While this style of polymorphism is less flexible than subtyping in some ways, notably requiring more polymorphism than strictly necessary to cope with the lack of directionality in type constraints, it has the advantage that it can be integrated with the standard HM algorithms quite easily.
