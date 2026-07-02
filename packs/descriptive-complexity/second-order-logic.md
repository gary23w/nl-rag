---
title: "Second-order logic"
source: https://en.wikipedia.org/wiki/Second-order_logic
domain: descriptive-complexity
license: CC-BY-SA-4.0
tags: descriptive complexity, second order logic, fagin theorem, finite model theory
fetched: 2026-07-02
---

# Second-order logic

In logic and mathematics, **second-order logic** is an extension of first-order logic, which itself is an extension of propositional logic. Second-order logic is in turn extended by higher-order logic and type theory.

First-order logic quantifies only variables that range over individuals (elements of the domain of discourse); second-order logic, in addition, quantifies over relations. For example, the second-order sentence $\forall P\,\forall x(Px\lor \neg Px)$ says that for every formula *P*, and every individual *x*, either *Px* is true or not(*Px*) is true (this is the law of excluded middle). Second-order logic also includes quantification over sets, functions, and other variables (see section below). Both first-order and second-order logic use the idea of a domain of discourse (often called simply the "domain" or the "universe"). The domain is a set over which individual elements may be quantified.

## Examples

First-order logic can quantify over individuals, but not over properties. That is, we can take an atomic sentence like Cube(*b*) and obtain a quantified sentence by replacing the name with a variable and attaching a quantifier:

$\exists x\,\mathrm {Cube} (x)$

However, we cannot do the same with the predicate. That is, the following expression:

$\exists \mathrm {P} \,\mathrm {P} (b)$

is not a sentence of first-order logic, but this is a legitimate sentence of second-order logic. Here, *P* is a predicate variable and is semantically a set of individuals.

As a result, second-order logic has greater expressive power than first-order logic. For example, there is no way in first-order logic to identify the set of all cubes and tetrahedrons. But the existence of this set can be asserted in second-order logic as:

$\exists \mathrm {P} \,\forall x\,(\mathrm {P} x\leftrightarrow (\mathrm {Cube} (x)\vee \mathrm {Tet} (x))).$

We can then assert properties of this set. For instance, the following says that the set of all cubes and tetrahedrons does not contain any dodecahedrons:

$\forall \mathrm {P} \,(\forall x\,(\mathrm {P} x\leftrightarrow (\mathrm {Cube} (x)\vee \mathrm {Tet} (x)))\rightarrow \lnot \exists x\,(\mathrm {P} x\wedge \mathrm {Dodec} (x))).$

Second-order quantification is especially useful because it gives the ability to express reachability properties. For example, if Parent(*x*, *y*) denotes that *x* is a parent of *y*, then first-order logic cannot express the property that *x* is an ancestor of *y*. In second-order logic we can express this by saying that every set of people containing *y* and closed under the Parent relation contains *x*:

$\forall \mathrm {P} \,((\mathrm {P} y\wedge \forall a\,\forall b\,((\mathrm {P} b\wedge \mathrm {Parent} (a,b))\rightarrow \mathrm {P} a))\rightarrow \mathrm {P} x).$

It is notable that while we have variables for predicates in second-order logic, we don't have variables for properties of predicates. We cannot say, for example, that there is a property Shape(*P*) that is true for the predicates *P* Cube, Tet, and Dodec. This would require third-order logic.

### Definition of equality

Objects are defined to be equal when they share all properties. In second-order logic, this can be expressed regardless of the type of objects we study and without the need to add any special treatment for equality to the logic as follows:

$\forall a\,\forall b\,(a=b\leftrightarrow (\forall \mathrm {P} \,(\mathrm {P} (a)\leftrightarrow \mathrm {P} (b))))$

### Mathematical induction

In first-order logic, the induction axiom of Peano arithmetic is actually stated as a schema for generating an infinite collection of first-order axioms. But in second-order logic, it can be expressed concisely as a single axiom:

$\forall \mathrm {P} \,((\mathrm {P} (0)\land \forall n\,(\mathrm {P} (n)\rightarrow \mathrm {P} (n+1)))\rightarrow \forall n\,\mathrm {P} (n))$

## Syntax and fragments

The syntax of second-order logic prescribes which expressions are well formed formulas. In addition to the syntax of first-order logic, second-order logic includes many new *sorts* (sometimes called *types*) of variables. These are:

- A sort of variables that range over sets of individuals. If *S* is a variable of this sort and *t* is a first-order term then the expression *t* ∈ *S* (also written *S*(*t*), or *St* to save parentheses) is an atomic formula. Sets of individuals can also be viewed as unary relations on the domain.
- For each natural number *k* there is a sort of variables that ranges over all *k*-ary relations on the individuals. If *R* is such a *k*-ary relation variable and *t*1,...,*t**k* are first-order terms then the expression *R*(*t*1,...,*t**k*) is an atomic formula.
- For each natural number *k* there is a sort of variables that ranges over all functions taking *k* elements of the domain and returning a single element of the domain. If *f* is such a *k*-ary function variable and *t*1,...,*t**k* are first-order terms then the expression *f*(*t*1,...,*t**k*) is a first-order term.

Each of the variables just defined may be universally and/or existentially quantified over, to build up formulas. Thus there are many kinds of quantifiers, two for each sort of variables. A *sentence* in second-order logic, as in first-order logic, is a well-formed formula with no free variables (of any sort).

It's possible to forgo the introduction of function variables in the definition given above (and some authors do this) because an *n*-ary function variable can be represented by a relation variable of arity *n*+1 and an appropriate formula for the uniqueness of the "result" in the *n*+1 argument of the relation. (Shapiro 2000, p. 63)

**Weak second-order logic** (WSO) is a restriction of second-order logic in which only quantification over finite sets is allowed. That is, it only allows quantification over unary relations with finitely many positive elements.

**Monadic second-order logic** (MSO) is a restriction of second-order logic in which only quantification over unary relations (i.e. sets) is allowed. It is stronger than WSO. Quantification over functions, owing to the equivalence to relations as described above, is thus also not allowed. The second-order logic without these restrictions is sometimes called *full second-order logic* to distinguish it from the monadic version. Monadic second-order logic is particularly used in the context of Courcelle's theorem, an algorithmic meta-theorem in graph theory. The MSO theory of the complete infinite binary tree (**S2S**) is decidable. By contrast, full second-order logic over any infinite set (or MSO logic over for example ( $\mathbb {N}$ ,+)) can interpret the true second-order arithmetic and is thus undecidable.

Just as in first-order logic, second-order logic may include non-logical symbols in a particular second-order language. These are restricted, however, in that all terms that they form must be either first-order terms (which can be substituted for a first-order variable) or second-order terms (which can be substituted for a second-order variable of an appropriate sort).

A formula in second-order logic is said to be of first-order (and sometimes denoted $\Sigma _{0}^{1}$ or $\Pi _{0}^{1}$ ) if its quantifiers (which may be universal or existential) range only over variables of first order, although it may have free variables of second order. A $\Sigma _{1}^{1}$ (existential second-order) formula is one additionally having some existential quantifiers over second-order variables, i.e. $\exists R_{0}\ldots \exists R_{m}\phi$ , where $\phi$ is a first-order formula. The fragment of second-order logic consisting only of existential second-order formulas is called **existential second-order logic** and abbreviated as ESO, as $\Sigma _{1}^{1}$ , or even as ∃SO. The fragment of $\Pi _{1}^{1}$ formulas is defined dually, it is called universal second-order logic. More expressive fragments are defined for any *k* > 0 by mutual recursion: $\Sigma _{k+1}^{1}$ has the form $\exists R_{0}\ldots \exists R_{m}\phi$ , where $\phi$ is a $\Pi _{k}^{1}$ formula, and similar, $\Pi _{k+1}^{1}$ has the form $\forall R_{0}\ldots \forall R_{m}\phi$ , where $\phi$ is a $\Sigma _{k}^{1}$ formula. (See analytical hierarchy for the analogous construction of second-order arithmetic.)

## Semantics

The semantics of second-order logic establish the meaning of each sentence. Unlike first-order logic, which has only one standard semantics, there are two different semantics that are commonly used for second-order logic: **standard semantics** and **Henkin semantics**. In each of these semantics, the interpretations of the first-order quantifiers and the logical connectives are the same as in first-order logic. Only the ranges of quantifiers over second-order variables differ in the two types of semantics.

In standard semantics, also called full semantics, the quantifiers range over *all* sets or functions of the appropriate sort. A model with this condition is called a full model, and these are the same as models in which the range of the second-order quantifiers is the powerset of the model's first-order part. Thus once the domain of the first-order variables is established, the meaning of the remaining quantifiers is fixed. It is these semantics that give second-order logic its expressive power, and they will be assumed for the remainder of this article.

Leon Henkin (1950) defined an alternative kind of semantics for second-order and higher-order theories, in which the meaning of the higher-order domains is partly determined by an explicit axiomatisation, drawing on type theory, of the properties of the sets or functions ranged over. Henkin semantics is a kind of many-sorted first-order semantics, where there are a class of models of the axioms, instead of the semantics being fixed to just the standard model as in the standard semantics. A model in Henkin semantics will provide a set of sets or set of functions as the interpretation of higher-order domains, which may be a proper subset of all sets or functions of that sort. For his axiomatisation, Henkin proved that Gödel's completeness theorem and compactness theorem, which hold for first-order logic, carry over to second-order logic with Henkin semantics. Since also the Löwenheim–Skolem theorems hold for Henkin semantics, Lindström's theorem imports that Henkin models are just *disguised first-order models*.

For theories such as second-order arithmetic, the existence of non-standard interpretations of higher-order domains isn't just a deficiency of the particular axiomatisation derived from type theory that Henkin used, but a necessary consequence of Gödel's incompleteness theorem: Henkin's axioms can't be supplemented further to ensure the standard interpretation is the only possible model. Henkin semantics are commonly used in the study of second-order arithmetic.

Jouko Väänänen argued that the distinction between Henkin semantics and full semantics for second-order logic is analogous to the distinction between provability in ZFC and truth in *V*, in that the former obeys model-theoretic properties like the Löwenheim–Skolem theorem and compactness, and the latter has categoricity phenomena. For example, "we cannot meaningfully ask whether the V as defined in $\mathrm {ZFC}$ is the real V . But if we reformalize $\mathrm {ZFC}$ inside $\mathrm {ZFC}$ , then we can note that the reformalized $\mathrm {ZFC}$ ... has countable models and hence cannot be categorical."

## Expressive power

Second-order logic is more expressive than first-order logic. For example, if the domain is the set of all real numbers, one can assert in first-order logic the existence of an additive inverse of each real number by writing $\forall x\exists y(x+y=0)$ but one needs second-order logic to assert the least-upper-bound property for sets of real numbers, which states that every bounded, nonempty set of real numbers has a supremum. If the domain is the set of all real numbers, the following second-order sentence (split over two lines) expresses the least upper bound property: ${\begin{aligned}\forall A{\biggl (}&{\bigl (}\exists w(w\in A)\wedge \exists z\forall u(u\in A\rightarrow u\leq z){\bigr )}\rightarrow \\&\exists x{\Bigl (}\forall u(u\in A\rightarrow u\leq x)\wedge \forall y\forall u{\bigl (}(u\in A\rightarrow u\leq y)\rightarrow x\leq y{\bigr )}{\Bigr )}{\biggr )}\\\end{aligned}}$ Here, the part of the first line involving w represents the assumption that A is nonempty (it has an element, w ). The rest of the first line represents the assumption that A is bounded from above (there exists a number z that is greater than or equal to all elements u of A ). The second line expresses the existence of a least upper bound x . It asserts that x is an upper bound (it is greater than or equal to any element u in A ) and that, if any number y is also an upper bound, then $x\leq y$ . Any ordered field that satisfies this property is isomorphic to the real number field. On the other hand, the set of first-order sentences valid in the reals has arbitrarily large models due to the compactness theorem. Thus the least-upper-bound property cannot be expressed by any set of sentences in first-order logic. (In fact, every real-closed field satisfies the same first-order sentences in the signature $\langle +,\cdot ,\leq \rangle$ as the real numbers.)

In second-order logic, it is possible to write formal sentences that say “the domain is finite” or “the domain is of countable cardinality.” To say that the domain is finite, use the sentence that says that every surjective function from the domain to itself is injective. To say that the domain has countable cardinality, use the sentence that says that there is a bijection between every two infinite subsets of the domain. It follows from the compactness theorem and the upward Löwenheim–Skolem theorem that it is not possible to characterize finiteness or countability, respectively, in first-order logic.

Certain fragments of second-order logic like ESO are also more expressive than first-order logic even though they are strictly less expressive than the full second-order logic. ESO also enjoys translation equivalence with some extensions of first-order logic that allow non-linear ordering of quantifier dependencies, like first-order logic extended with Henkin quantifiers, Hintikka and Sandu's independence-friendly logic, and Väänänen's dependence logic.

## Deductive systems

A deductive system for a logic is a set of inference rules and logical axioms that determine which sequences of formulas constitute valid proofs. Several deductive systems can be used for second-order logic, although none can be complete for the standard semantics (see below). Each of these systems is sound, which means any sentence they can be used to prove is logically valid in the appropriate semantics.

The weakest deductive system that can be used consists of a standard deductive system for first-order logic (such as natural deduction) augmented with substitution rules for second-order terms. This deductive system is commonly used in the study of second-order arithmetic.

The deductive systems considered by Shapiro (2000) and Henkin (1950) add to the augmented first-order deductive scheme both comprehension axioms and choice axioms. These axioms are sound for standard second-order semantics. They are sound for Henkin semantics restricted to Henkin models satisfying the comprehension and choice axioms.

## Non-reducibility to first-order logic

One might attempt to reduce the second-order theory of the real numbers, with full second-order semantics, to the first-order theory in the following way. First expand the domain from the set of all real numbers to a two-sorted domain, with the second sort containing all *sets of* real numbers. Add a new binary predicate to the language: the membership relation. Then sentences that were second-order become first-order, with the formerly second-order quantifiers ranging over the second sort instead. This reduction can be attempted in a one-sorted theory by adding unary predicates that tell one whether an element is a number or a set, and taking the domain to be the union of the set of real numbers and the power set of the real numbers.

But notice that the domain was asserted to include *all* sets of real numbers. That requirement cannot be reduced to a first-order sentence, or even a first-order theory, as the Löwenheim–Skolem theorem shows. That theorem implies that there is some countably infinite subset of the real numbers, whose members we will call *internal numbers*, and some countably infinite collection of sets of internal numbers, whose members we will call "internal sets", such that the domain consisting of internal numbers and internal sets satisfies exactly the same first-order sentences as are satisfied by the domain of real numbers and sets of real numbers. In particular, it satisfies a sort of least-upper-bound axiom that says, in effect:

Every nonempty

internal

set that has an

internal

upper bound has a least

internal

upper bound.

Countability of the set of all internal numbers (in conjunction with the fact that those form a densely ordered set) implies that that set does not satisfy the full least-upper-bound axiom. Countability of the set of all *internal* sets implies that it is not the set of *all* subsets of the set of all *internal* numbers (since Cantor's theorem implies that the set of all subsets of a countably infinite set is an uncountably infinite set). This construction is closely related to Skolem's paradox.

Thus the first-order theory of real numbers and sets of real numbers has many models, some of which are countable. The second-order theory of the real numbers has only one model, however. This follows from the classical theorem that there is only one Archimedean complete ordered field, along with the fact that all the axioms of an Archimedean complete ordered field are expressible in second-order logic. This shows that the second-order theory of the real numbers cannot be reduced to a first-order theory, in the sense that the second-order theory of the real numbers has only one model but the corresponding first-order theory has many models.

There are more extreme examples showing that second-order logic with standard semantics is more expressive than first-order logic. There is a finite second-order theory whose only model is the real numbers if the continuum hypothesis holds and that has no model if the continuum hypothesis does not hold. This theory consists of a finite theory characterizing the real numbers as a complete Archimedean ordered field plus an axiom saying that the domain is of the first uncountable cardinality. This example illustrates that the question of whether a sentence in second-order logic is consistent is extremely subtle.

Additional limitations of second-order logic are described in the next section.

## Metalogical results

It is a corollary of Gödel's incompleteness theorem that there is no deductive system (that is, no notion of *provability*) for second-order formulas that simultaneously satisfies these three desired attributes:

- (Soundness) Every provable second-order sentence is universally valid, i.e., true in all domains under standard semantics.
- (Completeness) Every universally valid second-order formula, under standard semantics, is provable.
- (Effectiveness) There is a proof-checking algorithm that can correctly decide whether a given sequence of symbols is a proof or not.

This corollary is sometimes expressed by saying that second-order logic does not admit a complete proof theory. In this respect second-order logic with standard semantics differs from first-order logic; Quine pointed to the lack of a complete proof system as a reason for thinking of second-order logic as not *logic*, properly speaking.

As mentioned above, Henkin proved that the standard deductive system for first-order logic is sound, complete, and effective for second-order logic with Henkin semantics, and the deductive system with comprehension and choice principles is sound, complete, and effective for Henkin semantics using only models that satisfy these principles.

The compactness theorem and the Löwenheim–Skolem theorem do not hold for full models of second-order logic. They do hold however for Henkin models.

## History and disputed value

Predicate logic was introduced to the mathematical community by C. S. Peirce, who coined the term *second-order logic* and whose notation is most similar to the modern form (Putnam 1982). However, today most students of logic are more familiar with the works of Frege, who published his work several years prior to Peirce but whose works remained less known until Bertrand Russell and Alfred North Whitehead made them famous. Frege used different variables to distinguish quantification over objects from quantification over properties and sets; but he did not see himself as doing two different kinds of logic. After the discovery of Russell's paradox it was realized that something was wrong with his system. Eventually logicians found that restricting Frege's logic in various ways—to what is now called first-order logic—eliminated this problem: sets and properties cannot be quantified over in first-order logic alone. The now-standard hierarchy of orders of logics dates from this time.

It was found that set theory could be formulated as an axiomatized system within the apparatus of first-order logic (at the cost of several kinds of completeness, but nothing so bad as Russell's paradox), and this was done (see Zermelo–Fraenkel set theory), as sets are vital for mathematics. Arithmetic, mereology, and a variety of other powerful logical theories could be formulated axiomatically without appeal to any more logical apparatus than first-order quantification, and this, along with Gödel and Skolem's adherence to first-order logic, led to a general decline in work in second (or any higher) order logic.

This rejection was actively advanced by some logicians, most notably W. V. Quine. Quine advanced the view that in predicate-language sentences like *Fx* the “*x*” is to be thought of as a variable or name denoting an object and hence can be quantified over, as in “For all things, it is the case that …” but the “*F*” is to be thought of as an *abbreviation* for an incomplete sentence, not the name of an object (not even of an abstract object like a property). For example, it might mean “… is a dog.” But it makes no sense to think we can quantify over something like this. (Such a position is quite consistent with Frege's own arguments on the concept-object distinction.) So to use a predicate as a variable is to have it occupy the place of a name, which only individual variables should occupy. This reasoning has been rejected by George Boolos.

In recent years second-order logic has made something of a recovery, buoyed by Boolos’ interpretation of second-order quantification as plural quantification over the same domain of objects as first-order quantification (Boolos 1984). Boolos furthermore points to the claimed nonfirstorderizability of sentences such as “Some critics admire only each other” and “Some of Fianchetto’s men went into the warehouse unaccompanied by anyone else”, which he argues can only be expressed by the full force of second-order quantification. However, generalized quantification and partially ordered (or branching) quantification may suffice to express a certain class of purportedly nonfirstorderizable sentences as well and these do not appeal to second-order quantification.

## Relation to computational complexity

The expressive power of various forms of second-order logic on finite structures is intimately tied to computational complexity theory. The field of descriptive complexity studies which computational complexity classes can be characterized by the power of the logic needed to express languages (sets of finite strings) in them. A string *w* = *w*1···*wn* in a finite alphabet *A* can be represented by a finite structure with domain *D* = {1,...,*n*}, unary predicates *Pa* for each *a* ∈ *A*, satisfied by those indices *i* such that *wi* = *a*, and additional predicates that serve to uniquely identify which index is which (typically, one takes the graph of the successor function on *D* or the order relation <, possibly with other arithmetic predicates). Conversely, the Cayley tables of any finite structure (over a finite signature) can be encoded by a finite string.

This identification leads to the following characterizations of variants of second-order logic over finite structures:

- REG (the regular languages) is the set of languages definable by monadic, second-order formulas (Büchi-Elgot-Trakhtenbrot theorem, 1960).
- NP is the set of languages definable by existential, second-order formulas (Fagin's theorem, 1974).
- co-NP is the set of languages definable by universal, second-order formulas.
- PH is the set of languages definable by second-order formulas.
- PSPACE is the set of languages definable by second-order formulas with an added transitive closure operator.
- EXPTIME is the set of languages definable by second-order formulas with an added least fixed point operator.

Relationships among these classes directly impact the relative expressiveness of the logics over finite structures; for example, if **PH** = **PSPACE**, then adding a transitive closure operator to second-order logic would not make it any more expressive over finite structures.
