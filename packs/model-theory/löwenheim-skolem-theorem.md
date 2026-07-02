---
title: "Löwenheim–Skolem theorem"
source: https://en.wikipedia.org/wiki/L%C3%B6wenheim%E2%80%93Skolem_theorem
domain: model-theory
license: CC-BY-SA-4.0
tags: model theory, compactness theorem, elementary equivalence, quantifier elimination
fetched: 2026-07-02
---

# Löwenheim–Skolem theorem

In mathematical logic, the **Löwenheim–Skolem theorem** is a theorem on the existence and cardinality of models, named after Leopold Löwenheim and Thoralf Skolem.

The precise formulation is given below. It implies that if a countable first-order theory has an infinite model, then for every infinite cardinal number *κ* it has a model of size *κ*, and that no first-order theory with an infinite model can have a unique model up to isomorphism. As a consequence, first-order theories are unable to control the cardinality of their infinite models.

The (downward) Löwenheim–Skolem theorem is one of the two key properties, along with the compactness theorem, that are used in Lindström's theorem to characterize first-order logic. In general, the Löwenheim–Skolem theorem does not hold in stronger logics such as second-order logic.

## Theorem

In its general form, the **Löwenheim–Skolem Theorem** states that for every signature *σ*, every infinite *σ*-structure *M* and every infinite cardinal number *κ* ≥ |*σ*|, there is a *σ*-structure *N* such that |*N*| = *κ* and such that

- if *κ* < |*M*| then *N* is an elementary substructure of *M*;
- if *κ* ≥ |*M*| then *N* is an elementary extension of *M*.

The theorem is often divided into two parts corresponding to the two cases above. The part of the theorem asserting that a structure has elementary substructures of all smaller infinite cardinalities is known as the **downward Löwenheim–Skolem Theorem**. The part of the theorem asserting that a structure has elementary extensions of all larger cardinalities is known as the **upward Löwenheim–Skolem Theorem**.

## Discussion

Below we elaborate on the general concept of signatures and structures.

### Concepts

#### Signatures

A signature consists of a set of function symbols *S*func, a set of relation symbols *S*rel, and a function $\operatorname {ar} :S_{\operatorname {func} }\cup S_{\operatorname {rel} }\rightarrow \mathbb {N} _{0}$ representing the arity of function and relation symbols. (A nullary function symbol is called a constant symbol.) In the context of first-order logic, a signature is sometimes called a language. It is called countable if the set of function and relation symbols in it is countable, and in general the cardinality of a signature is the cardinality of the set of all the symbols it contains.

A first-order theory consists of a fixed signature and a fixed set of sentences (formulas with no free variables) in that signature. Theories are often specified by giving a list of axioms that generate the theory, or by giving a structure and taking the theory to consist of the sentences satisfied by the structure.

#### Structures / Models

Given a signature *σ*, a *σ*-structure *M* is a concrete interpretation of the symbols in *σ*. It consists of an underlying set (often also denoted by "*M*") together with an interpretation of the function and relation symbols of *σ*. An interpretation of a constant symbol of *σ* in *M* is simply an element of *M*. More generally, an interpretation of an *n*-ary function symbol *f* is a function from *M**n* to *M*. Similarly, an interpretation of a relation symbol *R* is an *n*-ary relation on *M*, i.e. a subset of *M**n*.

A substructure of a *σ*-structure *M* is obtained by taking a subset *N* of *M* which is closed under the interpretations of all the function symbols in *σ* (hence includes the interpretations of all constant symbols in *σ*), and then restricting the interpretations of the relation symbols to *N*. An elementary substructure is a very special case of this; in particular an elementary substructure satisfies exactly the same first-order sentences as the original structure (its elementary extension).

### Consequences

The statement given in the introduction follows immediately by taking *M* to be an infinite model of the theory. The proof of the upward part of the theorem also shows that a theory with arbitrarily large finite models must have an infinite model; sometimes this is considered to be part of the theorem.

A theory is called **categorical** if it has only one model, up to isomorphism. This term was introduced by Veblen (1904), and for some time thereafter mathematicians hoped they could put mathematics on a solid foundation by describing a categorical first-order theory of some version of set theory. The Löwenheim–Skolem theorem dealt a first blow to this hope, as it implies that a first-order theory which has an infinite model cannot be categorical. Later, in 1931, the hope was shattered completely by Gödel's incompleteness theorem.

Many consequences of the Löwenheim–Skolem theorem seemed counterintuitive to logicians in the early 20th century, as the distinction between first-order and non-first-order properties was not yet understood. One such consequence is the existence of uncountable models of true arithmetic, which satisfy every first-order induction axiom but have non-inductive subsets.

Let **N** denote the natural numbers and **R** the reals. It follows from the theorem that the theory of (**N**, +, ×, 0, 1) (the theory of true first-order arithmetic) has uncountable models, and that the theory of (**R**, +, ×, 0, 1) (the theory of real closed fields) has a countable model. There are, of course, axiomatizations characterizing (**N**, +, ×, 0, 1) and (**R**, +, ×, 0, 1) up to isomorphism. The Löwenheim–Skolem theorem shows that these axiomatizations cannot be first-order. For example, in the theory of the real numbers, the completeness of a linear order used to characterize **R** as a complete ordered field, is a non-first-order property.

Another consequence that was considered particularly troubling is the existence of a countable model of set theory, which nevertheless must satisfy the sentence saying the real numbers are uncountable. Cantor's theorem states that some sets are uncountable. This counterintuitive situation came to be known as Skolem's paradox; it shows that the notion of countability is not absolute.

## Proof sketch

### Downward part

For each first-order $\sigma$ -formula $\varphi (y,x_{1},\ldots ,x_{n})$ , the axiom of choice implies the existence of a function $f_{\varphi }:M^{n}\to M$

such that, for all $a_{1},\ldots ,a_{n}\in M$ , either $M\models \varphi (f_{\varphi }(a_{1},\dots ,a_{n}),a_{1},\dots ,a_{n})$

or $M\models \neg \exists y\,\varphi (y,a_{1},\dots ,a_{n})$ .

Applying the axiom of choice again we get a function from the first-order formulas $\varphi$ to such functions $f_{\varphi }$ .

The family of functions $f_{\varphi }$ gives rise to a preclosure operator F on the power set of M $F(A)=\{f_{\varphi }(a_{1},\dots ,a_{n})\in M\mid \varphi \in \sigma ;\,a_{1},\dots ,a_{n}\in A\}$

for $A\subseteq M$ .

Iterating F countably many times results in a closure operator $F^{\omega }$ . Taking an arbitrary subset $A\subseteq M$ such that $\left\vert A\right\vert =\kappa$ , and having defined $N=F^{\omega }(A)$ , one can see that also $\left\vert N\right\vert =\kappa$ . Then N is an elementary substructure of M by the Tarski–Vaught test.

The trick used in this proof is essentially due to Skolem, who introduced function symbols for the Skolem functions $f_{\varphi }$ into the language. One could also define the $f_{\varphi }$ as partial functions such that $f_{\varphi }$ is defined if and only if $M\models \exists y\,\varphi (y,a_{1},\ldots ,a_{n})$ . The only important point is that F is a preclosure operator such that $F(A)$ contains a solution for every formula with parameters in A which has a solution in M and that $\left\vert F(A)\right\vert \leq \left\vert A\right\vert +\left\vert \sigma \right\vert +\aleph _{0}.$

### Upward part

First, one extends the signature by adding a new constant symbol for every element of M . The complete theory of M for the extended signature $\sigma '$ is called the *elementary diagram* of M . In the next step one adds $\kappa$ many new constant symbols to the signature and adds to the elementary diagram of M the sentences $c\neq c'$ for any two distinct new constant symbols c and $c'$ . Using the compactness theorem, the resulting theory is easily seen to be consistent. Since its models must have cardinality at least $\kappa$ , the downward part of this theorem guarantees the existence of a model N which has cardinality exactly $\kappa$ . It contains an isomorphic copy of M as an elementary substructure.

## In other logics

Although the (classical) Löwenheim–Skolem theorem is tied very closely to first-order logic, variants hold for other logics. For example, every consistent theory in second-order logic has a model smaller than the first supercompact cardinal (assuming one exists). The minimum size at which a (downward) Löwenheim–Skolem–type theorem applies in a logic is known as the Löwenheim number, and can be used to characterize that logic's strength. Moreover, if we go beyond first-order logic, we must give up one of three things: countable compactness, the downward Löwenheim–Skolem Theorem, or the properties of an abstract logic.

## Historical notes

This account is based mainly on Dawson (1993). To understand the early history of model theory one must distinguish between *syntactical consistency* (no contradiction can be derived using the deduction rules for first-order logic) and *satisfiability* (there is a model). Somewhat surprisingly, even before the completeness theorem made the distinction unnecessary, the term *consistent* was used sometimes in one sense and sometimes in the other.

The first significant result in what later became model theory was *Löwenheim's theorem* in Leopold Löwenheim's publication "Über Möglichkeiten im Relativkalkül" [On possibilities in the calculus of relatives] (1915):

For every countable signature

σ

, every

σ

-sentence that is satisfiable is satisfiable in a countable model.

Löwenheim's paper was actually concerned with the more general Peirce–Schröder *calculus of relatives* (relation algebra with quantifiers). He also used the now antiquated notations of Ernst Schröder. For a summary of the paper in English and using modern notation see Brady (2000, chapter 8).

According to the received historical view, Löwenheim's proof was faulty because it implicitly used Kőnig's lemma without proving it, although the lemma was not yet a published result at the time. In a revisionist account, Badesa (2004) considers that Löwenheim's proof was complete.

Skolem (1920) gave a (correct) proof using formulas in what would later be called *Skolem normal form* and relying on the axiom of choice:

Every countable theory which is satisfiable in a model

M

is satisfiable in a countable substructure of

M

.

Skolem (1922) also proved the following weaker version without the axiom of choice:

Every countable theory which is satisfiable in a model is also satisfiable in a countable model.

Skolem (1929) simplified Skolem (1920). Finally, Anatoly Maltsev proved the Löwenheim–Skolem theorem in its full generality (Maltsev 1936). He cited a note by Skolem, according to which the theorem had been proved by Alfred Tarski in a seminar in 1928. Therefore, the general theorem is sometimes known as the *Löwenheim–Skolem–Tarski theorem*. But Tarski did not remember his proof, and it remains a mystery how he could do it without the compactness theorem.

It is somewhat ironic that Skolem's name is connected with the upward direction of the theorem as well as with the downward direction:

> I follow custom in calling Corollary 6.1.4 the upward Löwenheim–Skolem theorem. But in fact Skolem didn't even believe it, because he didn't believe in the existence of uncountable sets.

— Hodges (1993).

> Skolem [...] rejected the result as meaningless; Tarski [...] very reasonably responded that Skolem's formalist viewpoint ought to reckon the downward Löwenheim–Skolem theorem meaningless just like the upward.

— Hodges (1993).

> Legend has it that Thoralf Skolem, up until the end of his life, was scandalized by the association of his name to a result of this type, which he considered an absurdity, nondenumerable sets being, for him, fictions without real existence.

— Poizat (2000).
