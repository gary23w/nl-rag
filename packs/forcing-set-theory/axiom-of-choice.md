---
title: "Axiom of choice"
source: https://en.wikipedia.org/wiki/Axiom_of_choice
domain: forcing-set-theory
license: CC-BY-SA-4.0
tags: forcing method, continuum hypothesis, constructible universe, large cardinal
fetched: 2026-07-02
---

# Axiom of choice

In mathematics, the **axiom of choice**, abbreviated **AC** or **AoC**, is an axiom of set theory. Informally put, the axiom of choice says that given any collection of non-empty sets, one can identify another set containing one element chosen from each set, even if the collection is infinite. Formally, the axiom establishes existence rather than a construction; it states that for every set I and every I -indexed family $(S_{i})_{i\in I}$ of nonempty sets, there exists an I -indexed set $(x_{i})_{i\in I}$ of elements of $\cup _{i\in I}S_{i}$ such that $x_{i}\in S_{i}$ for every $i\in I$ . The axiom of choice was formulated in 1904 by Ernst Zermelo in order to formalize his proof of the well-ordering theorem.

In many cases, a set created by choosing elements can be made without invoking the axiom of choice, particularly if the number of sets from which to choose the elements is finite (in which induction can be applied), or if a *canonical* rule on how to choose the elements is available – some distinguishing property that happens to hold for exactly one element in each set. An illustrative example is sets picked from the natural numbers. From such sets, one may always select the smallest number, e.g. given the sets {{4, 5, 6}, {10, 12}, {1, 400, 617, 8000}}, the set containing each smallest element is {4, 10, 1}. In this case, "select the smallest number" is a choice function. Even if infinitely many sets are collected from the natural numbers, it will always be possible to form a choice function from choosing the smallest element from each set to produce a set; the axiom of choice is not needed here. On the other hand, for the collection of all non-empty subsets of the real numbers, there is *no* known *canonical* rule by which one can choose one element from each of these subsets. In that case, the axiom of choice must be invoked to construct the desired choice function.

Bertrand Russell coined an analogy: for any (even infinite) collection of unordered pairs of shoes, one can pick out the left shoe from each pair to obtain an appropriate collection (i.e. set) of shoes; this makes it possible to define a choice function without using the axiom of choice. However, for an infinite collection of unordered pairs of *socks* (assumed to have no distinguishing features such as being a left sock rather than a right sock), there is no *natural* (i.e., canonical) way of choosing one sock from each pair, so one must appeal to the axiom of choice to construct the desired choice function.

Although originally controversial, the axiom of choice is now used without reservation by most mathematicians, and is included in the standard form of axiomatic set theory, Zermelo–Fraenkel set theory with the axiom of choice (ZFC). One motivation for this is that a number of generally accepted mathematical results, such as Tychonoff's theorem, require the axiom of choice for their proofs. Contemporary set theorists also study axioms that are not compatible with the axiom of choice, such as the axiom of determinacy. While some varieties of constructive mathematics avoid the axiom of choice, others embrace it.

## Statement

A choice function (also called selector or selection) is a function f , defined on a collection X of nonempty sets, such that for every set A in X , $f(A)$ is an element of A . With this concept, the axiom can be stated:

**Axiom**—For any set X of nonempty sets, there exists a choice function f that is defined on X and maps each set of X to an element of that set.

Formally, this may be expressed as follows:

$\forall X\left[\varnothing \in X\lor \exists f\left[\mathrm {dom} \ f=X\land \forall A\in X\left[f\left(A\right)\in A\right]\right]\right].$

Each choice function on a family X of nonempty sets is an element of the Cartesian product of the sets in X , and vice versa. Therefore an equivalent form of the axiom of choice is:

The Cartesian product of any collection of nonempty sets is nonempty.

This form implies a more general form where the Cartesian product is of a general indexed family of sets (which may contain duplicates), since one can always select the same element from duplicate factors.

### Nomenclature

In this article and other discussions of the axiom of choice the following abbreviations are common:

- AC – the axiom of choice. More rarely, AoC is used.
- ZF – Zermelo–Fraenkel set theory omitting the axiom of choice.
- ZFC – Zermelo–Fraenkel set theory, extended to include the axiom of choice.

### Variants

There are many other equivalent statements of the axiom of choice. These are equivalent in the sense that, in the presence of other basic axioms of set theory, they imply the axiom of choice and are implied by it.

One variation avoids the use of choice functions by, in effect, replacing each choice function with its range:

Given any set

X

, if the empty set is not an element of

X

and the elements of

X

are

pairwise disjoint

, then there exists a set

C

such that its intersection with any of the elements of

X

contains exactly one element.

This can be formalized in first-order logic as:

${\begin{aligned}\forall x(&\\&\exists e(e\in x\land \lnot \exists y(y\in e))\lor \\&\exists a\,\exists b\,\exists c\,(a\in x\land b\in x\land c\in a\land c\in b\land \lnot (a=b))\lor \\&\exists c\,\forall e\,(e\in x\implies \exists a\,(a\in e\land a\in c\land \forall b\,((b\in e\land b\in c)\implies a=b))))\end{aligned}}$

Note that $P\lor Q\lor R$ is logically equivalent to $(\lnot P\land \lnot Q)\implies R$ . In English, this first-order sentence reads:

Given any set

X

,

X

contains the empty set as an element or

the elements of

X

are not pairwise disjoint or

there exists a set

C

such that its intersection with any of the elements of

X

contains exactly one element.

This guarantees for any partition of a set X the existence of a subset C of X containing exactly one element from each part of the partition.

Another equivalent axiom only considers collections X that are essentially powersets of other sets:

For any set

A

, the

power set

of

A

(with the empty set removed) has a choice function.

Authors who use this formulation often speak of the *choice function on A*, but this is a slightly different notion of choice function. Its domain is the power set of A (with the empty set removed), and so makes sense for any set A , whereas with the definition used elsewhere in this article, the domain of a choice function on a *collection of sets* is that collection, and so only makes sense for sets of sets. With this alternate notion of choice function, the axiom of choice can be compactly stated as

Every set has a choice function.

which is equivalent to

For any set

A

there is a function

$f:{\mathcal {P}}(A)\setminus \{\emptyset \}\to A$

such that for any non-empty subset

B

of

A

,

$f(B)$

lies in

B

.

The negation of the axiom can thus be expressed as:

There is a set

A

such that for all functions

f

(on the set of non-empty subsets of

A

), there is a subset

B

such that

$f(B)$

does not lie in

B

.

## Usage

Until the late 19th century, the axiom of choice was often used implicitly, although it had not yet been formally stated. For example, after having established that the set *X* contains only non-empty sets, a mathematician might have said "let *F*(*s*) be one of the members of *s* for all *s* in *X*" to define a function *F*. In general, it is impossible to prove that *F* exists without the axiom of choice, but this seems to have gone unnoticed until Zermelo.

## Examples

### Cases where the axiom of choice is not needed

The existence of a choice function for a finite collection of nonempty sets can be proved by the principle of finite induction, without appealing to the axiom of choice. The proof uses the fact that, given a *single* nonempty set ⁠ A ⁠, first-order logic allows choosing some concrete ⁠ $a\in A$ ⁠. However, since a proof in first-order logic must be finite, one cannot make an infinite number of choices with first-order logic alone.

Another case where the axiom of choice is not needed is when there exists an explicit rule that gives a *canonical* choice function. For example, if each member of the collection ⁠ X ⁠ is a nonempty subset of the natural numbers, then one such explicit rule is to choose the *smallest element* of each ⁠ $A\in X$ ⁠. The canonical choice function that maps each ⁠ $A\in X$ ⁠ to its smallest element can again be constructed in ZF without the axiom of choice.

In general, if the union of all sets in ⁠ X ⁠ can be well-ordered, then a choice function for ⁠ X ⁠ can be constructed without using the axiom of choice. Note that it does not suffice that each ⁠ $A\in X$ ⁠ can be well-ordered, since the axiom of choice may be needed to choose a *canonical well-ordering* for each ⁠ A ⁠ anyway.

### Real numbers

As an example where the axiom of choice is required, let ⁠ X ⁠ be set of all non-empty subsets of the real numbers. Choosing the least element from each set no longer works, because some subsets of the real numbers do not have least elements. For example, the open interval ⁠ $(0,1)$ ⁠ does not have a least element: if ⁠ x ⁠ is in ⁠ $(0,1)$ ⁠, then so is ⁠ $x/2$ ⁠, and ⁠ $x/2$ ⁠ is always strictly smaller than ⁠ x ⁠. This strategy fails here because the natural order of real numbers is not a well-order.

If there exists a different ordering of the real numbers which is a well-ordering, then applying the least-element strategy with respect to that ordering would give a choice function for ⁠ X ⁠. Conversely, if there exists a choice function for ⁠ X ⁠, then the proof of the well-ordering theorem would show that a well-ordering of the real numbers does exist.

### Constructing a non-measurable set

Let ⁠ S ⁠ be the unit circle, and ⁠ G ⁠ be the group consisting of all rational rotations (i.e., rotations by angles which are rational multiples of ⁠ $\pi$ ⁠). Since ⁠ G ⁠ is countable while ⁠ S ⁠ is uncountable, ⁠ S ⁠ must break up into uncountably many orbits under the action of ⁠ G ⁠.

Using the axiom of choice, we could pick a single point from each orbit, obtaining an uncountable subset ⁠ X ⁠ of ⁠ S ⁠ with the property that all of its translates by ⁠ G ⁠ are disjoint from ⁠ X ⁠. The set of those translates partitions the circle into a countable collection of pairwise disjoint sets, which are all pairwise congruent. The set ⁠ X ⁠ will be non-measurable for any rotation-invariant countably additive measure on ⁠ S ⁠: if ⁠ X ⁠ has zero measure, countable additivity would imply that the whole circle has zero measure. If ⁠ X ⁠ has positive measure, countable additivity would show that the circle has infinite measure.

Applying a similar construction to the three-dimensional ball can result in a set that is non-measurable even for any rotation-invariant *finitely* additive measure, as shown by the Banach–Tarski paradox.

## Criticism and acceptance

A proof requiring the axiom of choice may establish the existence of an object without *canonically* defining the object in the language of set theory. For example, while the axiom of choice implies that there is a well-ordering of the real numbers, there are models of set theory with the axiom of choice in which no individual well-ordering of the reals is definable. Similarly, although a subset of the real numbers that is not Lebesgue measurable can be proved to exist using the axiom of choice, it is consistent that no such set is definable.

The axiom of choice asserts the existence of these intangibles (objects that are proved to exist, but which cannot be constructed in any *canonical* way), which may conflict with some philosophical principles. Because there is no canonical well-ordering of all sets, a construction that relies on a well-ordering may not produce a canonical result, even if a canonical result is desired (as is often the case in category theory). This has been used as an argument against the use of the axiom of choice.

Another argument against the axiom of choice is that it implies the existence of objects that may seem counterintuitive. One example is the Banach–Tarski paradox, which says that it is possible to decompose the 3-dimensional solid unit ball into finitely many pieces and, using only rotations and translations, reassemble the pieces into two solid balls each with the same volume as the original. The pieces in this decomposition, constructed using the axiom of choice, are non-measurable sets.

Despite these seemingly paradoxical results, most mathematicians accept the axiom of choice as a valid principle for proving new results in mathematics. But the debate is interesting enough that it is considered notable when a theorem in ZFC (ZF plus AC) is logically equivalent (with just the ZF axioms) to the axiom of choice, and mathematicians look for results that require the axiom of choice to be false, though this type of deduction is less common than the type that requires the axiom of choice to be true.

Theorems of ZF hold true in any model of that theory, regardless of the truth or falsity of the axiom of choice in that particular model. The implications of choice below, including weaker versions of the axiom itself, are listed because they are not theorems of ZF. The Banach–Tarski paradox, for example, is neither provable nor disprovable from ZF alone: it is impossible to construct the required decomposition of the unit ball in ZF, but also impossible to prove there is no such decomposition. Such statements can be rephrased as conditional statements—for example, "If AC holds, then the decomposition in the Banach–Tarski paradox exists." Such conditional statements are provable in ZF when the original statements are provable from ZF and the axiom of choice.

## In constructive mathematics

As discussed above, in the classical theory of ZFC, the axiom of choice enables nonconstructive proofs in which the existence of a type of object is proved without an explicit canonical construction of an instance of this type. In fact, in set theory and topos theory, Diaconescu's theorem shows that the axiom of choice implies the law of excluded middle. The principle is thus not available in constructive set theory, where non-classical logic is employed.

The situation is different when the principle is formulated in Martin-Löf type theory. There and higher-order Heyting arithmetic, the appropriate statement of the axiom of choice is (depending on approach) included as an axiom or provable as a theorem. A cause for this difference is that the axiom of choice in type theory does not have the extensionality properties that the axiom of choice in constructive set theory does. The type theoretical context is discussed further below.

Different choice principles have been thoroughly studied in the constructive contexts and the principles' status varies between different school and varieties of the constructive mathematics. Some results in constructive set theory use the axiom of countable choice or the axiom of dependent choice, which do not imply the law of the excluded middle. Errett Bishop, who is notable for developing a framework for constructive analysis, argued that an axiom of choice was constructively acceptable, saying

> A choice function exists in constructive mathematics, because a choice is implied by the very meaning of existence.

Although the axiom of countable choice in particular is commonly used in constructive mathematics, its use has also been questioned.

## Independence

It has been known since as early as 1922 that the axiom of choice may fail in a variant of ZF with urelements, through the technique of permutation models introduced by Abraham Fraenkel and developed further by Andrzej Mostowski. The basic technique can be illustrated as follows: Let *x**n* and *y**n* be distinct urelements for *n*=1, 2, 3..., and build a model where each set is symmetric under the interchange *x**n* ↔ *y**n* for all but a finite number of *n*. Then the set *X* = {{*x*1, *y*1}, {*x*2, *y*2}, {*x*3, *y*3}, ...} can be in the model but sets such as {*x*1, *x*2, *x*3, ...} cannot, and thus *X* cannot have a choice function.

In 1938, Kurt Gödel showed that the *negation* of the axiom of choice is not a theorem of ZF by constructing an inner model (the constructible universe) that satisfies ZFC, thus showing that ZFC is consistent if ZF itself is consistent. In 1963, Paul Cohen employed the technique of forcing, developed for this purpose, to show that, assuming ZF is consistent, the axiom of choice itself is not a theorem of ZF. He did this by constructing a much more complex model that satisfies ZF¬C (ZF with the negation of AC added as axiom) and thus showing that ZF¬C is consistent. Cohen's model is a symmetric model, which is similar to permutation models, but uses "generic" subsets of the natural numbers (justified by forcing) in place of urelements.

Together these results establish that the axiom of choice is logically independent of ZF. The assumption that ZF is consistent is harmless because adding another axiom to an already inconsistent system cannot make the situation worse. Because of independence, the decision whether to use the axiom of choice (or its negation) in a proof cannot be made by appeal to other axioms of set theory. It must be made on other grounds.

One argument in favor of using the axiom of choice is that it is convenient because it allows one to prove some simplifying propositions that otherwise could not be proved. Many theorems provable using choice are of an elegant general character: the cardinalities of any two sets are comparable, every nontrivial unital ring has a maximal ideal, every vector space has a basis, every connected graph has a spanning tree, and every product of compact spaces is compact, among many others. Frequently, the axiom of choice allows generalizing a theorem to "larger" objects. For example, it is provable without the axiom of choice that every vector space of finite dimension has a basis, but the generalization to all vector spaces requires the axiom of choice. Likewise, a finite product of compact spaces can be proven to be compact without the axiom of choice, but the generalization to infinite products (Tychonoff's theorem) requires the axiom of choice.

The proof of the independence result also shows that a wide class of mathematical statements, including all statements that can be phrased in the language of Peano arithmetic, are provable in ZF if and only if they are provable in ZFC. Statements in this class include the statement that P = NP, the Riemann hypothesis, and many other unsolved mathematical problems. When attempting to solve problems in this class, it makes no difference whether ZF or ZFC is employed if the only question is the existence of a proof. It is possible, however, that there is a shorter proof of a theorem from ZFC than from ZF.

The axiom of choice is not the only significant statement that is independent of ZF. For example, the generalized continuum hypothesis (GCH) is not only independent of ZF, but also independent of ZFC. However, ZF plus GCH implies AC, making GCH a strictly stronger claim than AC, even though they are both independent of ZF.

## Stronger axioms

The axiom of constructibility and the generalized continuum hypothesis each imply the axiom of choice and are strictly stronger than it. In class theories such as Von Neumann–Bernays–Gödel set theory and Morse–Kelley set theory, there is an axiom called the axiom of global choice that is stronger than the axiom of choice for sets because it also applies to proper classes. The axiom of global choice follows from the axiom of limitation of size. Tarski's axiom, which is used in Tarski–Grothendieck set theory and states (in the vernacular) that every set belongs to *some* Grothendieck universe, is stronger than the axiom of choice.

## Equivalents

There are important statements that, assuming the axioms of ZF but neither AC nor ¬AC, are equivalent to the axiom of choice (that is, their truth values in ZF, while undecidable, are the same as that of AC). The most important among them are Zorn's lemma and the well-ordering theorem. In fact, Zermelo initially introduced the axiom of choice in order to formalize his proof of the well-ordering theorem.

- Set theory
  - Trichotomy: The cardinalities of any two sets are comparable with each other. That is, given any two sets, an injection exists from (at least) one of the sets to the other.
  - Tarski's theorem about choice: For every infinite set A , the sets A and $A\times A$ have the same cardinality; i.e., there exists a bijection between them.
  - Every surjection $f:S\to T$ has a right inverse; i.e., there exists a function $g:T\to S$ such that $f\circ g=\mathrm {id} _{T}$ .
  - For every disjoint collection ${\mathcal {C}}$ of nonempty sets, there exists a set $C\subseteq \cup _{S\in {\mathcal {C}}}(S)$ that intersects each member of ${\mathcal {C}}$ in exactly one element. That is, every partition of a set has a transversal.
  - If a relation R from a set X to a set Y has the property that for every $x\in X$ , there is a $y\in Y$ with $xRy$ , then there exists a function $f:X\to Y$ such that $xRf(x)$ for all $x\in X$ .
  - The Cartesian product of any indexed family of nonempty sets is nonempty. That is, for any set I , and any I -indexed family $(S_{i})_{i\in I}$ of nonempty sets, there exists an I -indexed set $(s_{i})_{i\in I}$ of elements in $\cup _{i\in I}(S_{i})$ such that $s_{i}\in S_{i}$ for all $i\in I$ .
  - In any collection ${\mathcal {A}}$ of nonempty sets, there exists a disjoint subcollection ${\mathcal {C}}$ of sets whose union $\cup _{S\in {\mathcal {C}}}(S)$ intersects all the members of ${\mathcal {A}}$ . (Note that such a disjoint subcollection is precisely one that is *maximal* with respect to set inclusion.)
  - For any set X , there exists a *maximal* (under set inclusion) collection ${\mathcal {A}}$ of subsets of X for which every *finite* subcollection ${\mathcal {C}}$ of ${\mathcal {A}}$ has a nonempty intersection $\cap _{S\in {\mathcal {C}}}(S)$ . (This statement is key to a standard proof of Tychonoff's theorem.)
  - Well-ordering theorem: Every set A has a well-ordering (i.e., a total ordering in which every nonempty subset of A has a minimum element). Consequently, every cardinal has an initial ordinal.
  - For every ordinal $\alpha$ , the powerset (i.e., the set of all subsets) of $\alpha$ has a well-ordering.
  - Hausdorff maximal principle: Every partially ordered set has a maximal chain (with respect to inclusion). Equivalently, in a partially ordered set, every chain can be extended to a maximal chain.
  - Antichain principle: Every partially ordered set has a maximal antichain (with respect to inclusion). Equivalently, in any partially ordered set, every antichain can be extended to a maximal antichain.
  - Zorn's lemma: If $(A,<)$ is any partially ordered set in which every chain has an upper bound in A , then $(A,<)$ has at least one maximal element.
  - Kuratowski's lemma: If ${\mathcal {A}}$ is any family of sets with the property that for any subfamily ${\mathcal {C}}$ of ${\mathcal {A}}$ totally ordered by set inclusion, the union $\cup _{A\in {\mathcal {C}}}(A)$ is an element of ${\mathcal {A}}$ , then ${\mathcal {A}}$ has at least one element *maximal* with respect to inclusion.
  - Tukey's lemma: If ${\mathcal {A}}$ is any family of subsets of a set X with the property that a set $B\subseteq X$ is an element of ${\mathcal {A}}$ iff every *finite* subset of B is an element of ${\mathcal {A}}$ , then ${\mathcal {A}}$ has at least one element *maximal* with respect to inclusion.
  - König's theorem: Informally, the sum of a sequence of cardinals is strictly less than the product of a sequence of larger cardinals. (The reason for the term "informally" is that the sum or product of a "sequence" of cardinals cannot itself be defined without some aspect of the axiom of choice.)
- Abstract algebra
  - Every vector space has a basis; equivalently, every linearly independent subset of a vector space can be extended to a basis, while every spanning subset contains a basis. In the language of module theory, all vector spaces are free modules.
  - Krull's theorem: Every nontrivial unital ring contains a maximal ideal; equivalently, every proper ideal of a unital ring can be extended to a maximal ideal.
  - For every non-empty set S there is a binary operation defined on S that gives it a group structure. (A cancellative binary operation is enough; see Group structure and the axiom of choice.)
  - Every free abelian group is projective.
  - Baer's criterion: Every divisible abelian group is injective.
  - Every set is a projective object in the category of sets.
- Functional analysis
  - The closed unit ball of the dual of a normed vector space over the reals has an extreme point.
- Point-set topology
  - Tychonoff's theorem: The product of any indexed family of compact topological spaces is compact.
  - The closure of the product of any indexed family of subsets of a topological space is equal to the product of the closures of those subsets.
- Mathematical logic
  - If S is a set of sentences of first-order logic and B is a consistent subset of S , then B is included in a set that is maximal among consistent subsets of S . The special case where S is the set of **all** first-order sentences in a given signature is weaker, equivalent to the Boolean prime ideal theorem; see the section "Weaker forms" below.
  - Löwenheim–Skolem theorem: If a first-order theory has an infinite model, then it has an infinite model of every possible cardinality greater than or equal to the cardinality of the language of this theory.
- Graph theory
  - Every connected graph has a spanning tree; equivalently, every tree in a connected graph can be extended to a spanning tree, while every spanning subgraph contains a spanning tree.

### Category theory

Several results in category theory invoke the axiom of choice for their proof. These results might be weaker than, equivalent to, or stronger than the axiom of choice, depending on the strength of the technical foundations. For example, if one defines categories in terms of sets, that is, as sets of objects and morphisms (usually called a small category), then there is no category of all sets, and so it is difficult for a category-theoretic formulation to apply to all sets. On the other hand, other foundational descriptions of category theory are considerably stronger, and an identical category-theoretic statement of choice may be stronger than the standard formulation, à la class theory, mentioned above.

Examples of category-theoretic statements which require choice include:

- Every small category has a skeleton.
- If two small categories are weakly equivalent, then they are equivalent.
- Every continuous functor on a small-complete category which satisfies the appropriate solution set condition has a left adjoint (the Freyd adjoint functor theorem).

## Weaker forms

There are several weaker statements unprovable in ZF that are logically implied by the axiom of choice (AC) within ZF but are not equivalent to AC. One example is the axiom of dependent choice (DC). A still weaker example is the axiom of countable choice (ACω or CC), which states that a choice function exists for any countable family of nonempty sets. These axioms are sufficient for many proofs in elementary mathematical analysis, and are consistent with some principles, such as the Lebesgue measurability of all subsets of real numbers, that are disprovable from the full axiom of choice.

Given an ordinal parameter α ≥ ω+2 – for every set *S* with rank less than α, *S* is well-orderable. Given an ordinal parameter α ≥ 1 – for every set *S* with Hartogs number less than ωα, *S* is well-orderable. As the ordinal parameter is increased, these approximate the full axiom of choice more and more closely.

Other choice axioms weaker than axiom of choice include the Boolean prime ideal theorem and the axiom of uniformization. The former is equivalent in ZF to Tarski's 1930 ultrafilter lemma: every filter is a subset of some ultrafilter.

### Results requiring AC (or weaker forms) but weaker than it

One of the most interesting aspects of the axiom of choice is the large number of places in mathematics where it shows up. Here are some statements that require the axiom of choice in the sense that they are not provable from ZF but are provable from ZFC (ZF plus AC). Equivalently, these statements are true in all models of ZFC but false in some models of ZF.

- Set theory
  - Axiom of countable choice: The Cartesian product of any sequence (i.e., countable indexed family) of nonempty sets is nonempty. (This is just the axiom of choice with the indexing set restricted to countable size.)
  - Axiom of dependent choice: If R is any relation on a set S with the property that for every $x\in S$ , there is a $y\in S$ with $xRy$ , then, for every $x\in S$ , there exists a sequence $\left(x_{n}\right)_{n\in \mathbb {N} }$ in S starting at x and satisfying $x_{n}Rx_{n+1}$ for all $n\in \mathbb {N}$ . (In ZF, this statement logically implies the axiom of countable choice, and is strictly stronger.)
  - Axiom of choice for finite sets: The Cartesian product of any indexed family of non-empty *finite* sets is nonempty. (Note that here, it is each *member* of the indexed family that is restricted in size, not the *indexing set*, in contrast with countable choice.)
  - Ultrafilter lemma: Every filter on a set S can be extended to an ultrafilter on S . (In ZF, this statement logically implies the Axiom of choice for finite sets (above).)
  - The union of any countable family of countable sets is countable. (In ZF, this statement is logically implied by the axiom of countable choice.)
  - Every infinite set has a countable-infinite subset, i.e., has cardinality greater than or equal to $\aleph _{0}$ . (In ZF, this statement is logically implied by the axiom of countable choice but is not equivalent; see Dedekind infinite.)
  - Eight definitions of a finite set are equivalent.
  - Every infinite game $G_{S}$ in which S is a Borel subset of Baire space is determined.
  - Every infinite cardinal $\kappa$ satisfies $2\kappa =\kappa$ .
- Measure theory
  - The Vitali theorem: There exist subsets of $\mathbb {R} ^{n}$ (for any $n>0$ ) that are not Lebesgue measurable; i.e., the set of all subsets of $\mathbb {R} ^{n}$ does not form a measure space of $\mathbb {R} ^{n}$ under the standard (Lebesgue) outer-measure.
  - There exist Lebesgue-measurable subsets of $\mathbb {R} ^{n}$ that are not Borel sets; i.e., the Borel $\sigma$ -algebra on $\mathbb {R} ^{n}$ is *strictly* contained in the Lebesgue-measure $\sigma$ -algebra on $\mathbb {R} ^{n}$ .
  - The Hausdorff paradox.
  - The Banach–Tarski paradox.
- Abstract algebra
  - Every field has an algebraic closure.
  - Every field extension has a transcendence basis.
  - Every infinite-dimensional vector space contains an infinite linearly independent subset. (In ZF, this statement is logically implied by the axiom of countable choice.)
  - Stone's representation theorem for Boolean algebras needs the Boolean prime ideal theorem.
  - The Nielsen–Schreier theorem, that every subgroup of a free group is free.
  - The additive groups of **R** and **C** are isomorphic.
- Metric spaces
  - In any metric space X , the topological and sequential definitions of an accumulation point of a subset S are equivalent. (In the topological definition, x is an accumulation point of S iff every neighborhood of x in X intersects $S-\{x\}$ , while in the sequential definition, x is an accumulation point of S iff there exists a sequence in $S-\{x\}$ that converges to x in X .) This equivalence as well as the two below equivalences require the axiom of countable choice, but not the full axiom of choice.
  - For functions between metric spaces, the topological and sequential definitions of continuity are equivalent. (In the topological definition, a function $f:X\to Y$ is continuous at x iff for every neighborhood V of $f(x)$ in Y , there is a neighborhood U of x in X such that $f(U)\subseteq V$ . In the sequential definition, a function $f:X\to Y$ is continuous at x iff for every sequence $\{x_{n}\}_{n\geq 1}$ in X converging to x , the sequence $\{f(x_{n})\}_{n\geq 1}$ converges to $f(x)$ in Y .)
  - For metric spaces, the topological and sequential definitions of compactness are equivalent. (In the topological definition, X is compact iff every collection of open subsets of X that covers X has a finite subcollection which also covers X . In the sequential definition, X is compact iff every sequence in X has a subsequence that converges in X .)
- Functional analysis
  - The Hahn–Banach theorem in functional analysis, allowing the extension of linear functionals.
  - The theorem that every Hilbert space has an orthonormal basis.
  - The Banach–Alaoglu theorem about compactness of sets of functionals.
  - The Baire category theorem about complete metric spaces, and its consequences, such as the open mapping theorem and the closed graph theorem.
  - On every infinite-dimensional topological vector space there is a discontinuous linear map.
- General topology
  - A uniform space is compact if and only if it is complete and totally bounded.
  - Every Tychonoff space has a Stone–Čech compactification.
  - Urysohn's Lemma: For any two disjoint closed subsets A and B of a normal space X , and any compact interval $[a,b]$ of $\mathbb {R}$ , there exists a continuous map $f:X\to [a,b]$ such that $f(A)=\{a\}$ and $f(B)=\{b\}$ . (In ZF, this statement is logically implied by the axiom of dependent choice, but not by the axiom of countable choice.)
  - Tietze extension theorem: For any closed subspace A of a normal space X , and any closed or open interval I of $\mathbb {R}$ , and any continuous map $f:A\to I$ , there exists a continuous map from X to I that extends f . (In ZF, this statement is logically equivalent to Urysohn's lemma.)
  - Existence of partitions of unity: For any paracompact Hausdorff space X (in particular, any manifold), and any indexed open cover $(U_{i})_{i\in I}$ of X , there exists a partition of unity of X subordinate to $(U_{i})_{i\in I}$ .
- Mathematical logic
  - Gödel's completeness theorem for first-order logic: every consistent set of first-order sentences has a completion. That is, every consistent set of first-order sentences can be extended to a maximal consistent set.
  - The compactness theorem: If $\Sigma$ is a set of first-order (or alternatively, zero-order) sentences such that every finite subset of $\Sigma$ has a model, then $\Sigma$ has a model.

### Possibly equivalent implications of AC

Unsolved problem in mathematics

Does the partition principle imply the axiom of choice?

More unsolved problems in mathematics

There are several historically important set-theoretic statements implied by AC whose equivalence to AC is open. Zermelo cited the partition principle, which was formulated before AC itself, as a justification for believing AC. In 1906, Russell declared PP to be equivalent, but whether the partition principle implies AC is an old open problem in set theory, and the equivalences of the other statements are similarly hard old open problems. In every *known* model of ZF where choice fails, these statements fail too, but it is unknown whether they can hold without choice.

- Set theory
  - Partition principle: Given two sets *A* and *B*, if a surjection exists from *A* to *B*, then an injection exists from *B* to *A*. Equivalently, every partition *P* of a set *S* is less than or equal to *S* in size.
  - Given any two sets *A* and *B* where *B* is nonempty, either an injection or a surjection (or both) exists from *A* to *B*.
  - Given any two nonempty sets, a surjection exists from (at least) one of the sets to the other.
  - Converse Schröder–Bernstein theorem: If two sets have surjections to each other, then they have the same cardinality.
  - Weak partition principle: Given two sets *A* and *B*, if both an injection and a surjection exists from *A* to *B*, then *A* and *B* have the same cardinality. Equivalently, a partition of a set *S* cannot be strictly larger than *S*. If WPP holds, this already implies the existence of a non-measurable set. Each of the previous three statements is implied by the preceding one, but it is unknown if any of these implications can be reversed.
  - There is no infinite decreasing sequence of cardinals. The equivalence was conjectured by Schoenflies in 1905.
- Abstract algebra
  - Hahn embedding theorem: Every ordered abelian group *G* order-embeds as a subgroup of the additive group $\mathbb {R} ^{\Omega }$ endowed with a lexicographical order, where Ω is the set of Archimedean equivalence classes of *G*. This equivalence was conjectured by Hahn in 1907.

## Stronger forms of the negation of AC

If we abbreviate by BP the claim that every set of real numbers has the property of Baire, then BP is stronger than ¬AC, which asserts the nonexistence of any choice function on perhaps only a single set of nonempty sets. Strengthened negations may be compatible with weakened forms of AC. For example, ZF + DC + BP is consistent, if ZF is.

It is also consistent with ZF + DC that every set of reals is Lebesgue measurable, but this consistency result, due to Robert M. Solovay, cannot be proved in ZFC itself, but requires a mild large cardinal assumption (the existence of an inaccessible cardinal). The much stronger axiom of determinacy, or AD, implies that every set of reals is Lebesgue measurable, has the property of Baire, and has the perfect set property (all three of these results are refuted by AC itself). ZF + DC + AD is consistent provided that a sufficiently strong large cardinal axiom is consistent (the existence of infinitely many Woodin cardinals).

Quine's system of axiomatic set theory, New Foundations (NF), takes its name from the title ("New Foundations for Mathematical Logic") of the 1937 article that introduced it. In the NF axiomatic system, the axiom of choice can be disproved.

## Statements implying the negation of AC

There are models of Zermelo-Fraenkel set theory in which the axiom of choice is false. We shall abbreviate "Zermelo-Fraenkel set theory plus the negation of the axiom of choice" by ZF¬C. For certain models of ZF¬C, it is possible to validate the negation of some standard ZFC theorems. As any model of ZF¬C is also a model of ZF, it is the case that for each of the following statements, there exists a model of ZF in which that statement is true.

- The negation of the weak partition principle: There is a set that can be partitioned into strictly more equivalence classes than the original set has elements, and a function whose domain is strictly smaller than its range. In fact, this is the case in all *known* models.
- There is a function *f* from the real numbers to the real numbers such that *f* is not continuous at *a*, but *f* is sequentially continuous at *a*, i.e., for any sequence {*xn*} converging to *a*, lim*n* f(*xn*)=f(a).
- There is an infinite set of real numbers without a countably infinite subset.
- The real numbers are a countable union of countable sets. This does not imply that the real numbers are countable: As pointed out above, to show that a countable union of countable sets is itself countable requires the Axiom of countable choice.
- There is a field with no algebraic closure.
- There is a field with two non-isomorphic algebraic closures.
- In all models of ZF¬C there is a vector space with no basis.
- There is a vector space with two bases of different cardinalities.
- There is a free complete Boolean algebra on countably many generators.
- There is a set that cannot be linearly ordered.
- There exists a model of ZF¬C in which every set in R*n* is measurable. Thus it is possible to exclude counterintuitive results like the Banach–Tarski paradox which are provable in ZFC. Furthermore, this is possible whilst assuming the Axiom of dependent choice, which is weaker than AC but sufficient to develop most of real analysis.
- In all models of ZF¬C, the generalized continuum hypothesis does not hold.

For proofs, see Jech (2008).

Additionally, by imposing definability conditions on sets (in the sense of descriptive set theory) one can often prove restricted versions of the axiom of choice from axioms incompatible with general choice. This appears, for example, in the Moschovakis coding lemma.

## Axiom of choice in type theory

In type theory, a different kind of statement is known as the axiom of choice. This form begins with two types, σ and τ, and a relation *R* between objects of type σ and objects of type τ. The axiom of choice states that if for each *x* of type σ there exists a *y* of type τ such that *R*(*x*,*y*), then there is a function *f* from objects of type σ to objects of type τ such that *R*(*x*,*f*(*x*)) holds for all *x* of type σ:

$(\forall x^{\sigma })(\exists y^{\tau })R(x,y)\to (\exists f^{\sigma \to \tau })(\forall x^{\sigma })R(x,f(x)).$

Unlike in set theory, the axiom of choice in type theory is typically stated as an axiom scheme, in which *R* varies over all formulas or over all formulas of a particular logical form.
