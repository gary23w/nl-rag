---
title: "Compactness theorem"
source: https://en.wikipedia.org/wiki/Compactness_theorem
domain: model-theory
license: CC-BY-SA-4.0
tags: model theory, compactness theorem, elementary equivalence, quantifier elimination
fetched: 2026-07-02
---

# Compactness theorem

In mathematical logic, the **compactness theorem** states that a set of first-order sentences has a model if and only if every finite subset of it has a model. This theorem is an important tool in model theory, as it provides a useful (but generally not effective) method for constructing models of any set of sentences that is finitely consistent.

The compactness theorem for the propositional calculus is a consequence of Tychonoff's theorem (which says that the product of compact spaces is compact) applied to compact Stone spaces, hence the theorem's name. Likewise, it is analogous to the finite intersection property characterization of compactness in topological spaces: a collection of closed sets in a compact space has a non-empty intersection if every finite subcollection has a non-empty intersection.

The compactness theorem is one of the two key properties, along with the downward Löwenheim–Skolem theorem, that is used in Lindström's theorem to characterize first-order logic. Although there are some generalizations of the compactness theorem to non-first-order logics, the compactness theorem itself does not hold in them, except for a very limited number of examples.

## History

Kurt Gödel proved the countable compactness theorem in 1930. Anatoly Maltsev proved the uncountable case in 1936.

## Applications

The compactness theorem has many applications in model theory; a few typical results are sketched here.

### Robinson's principle

The compactness theorem implies the following result, stated by Abraham Robinson in his 1949 dissertation.

Robinson's principle: If a first-order sentence holds in every field of characteristic zero, then there exists a constant p such that the sentence holds for every field of characteristic larger than $p.$ This can be seen as follows: suppose $\varphi$ is a sentence that holds in every field of characteristic zero. Then its negation $\lnot \varphi ,$ together with the field axioms and the infinite sequence of sentences $1+1\neq 0,\;\;1+1+1\neq 0,\;\ldots$ is not satisfiable (because there is no field of characteristic 0 in which $\lnot \varphi$ holds, and the infinite sequence of sentences ensures any model would be a field of characteristic 0). Therefore, there is a finite subset A of these sentences that is not satisfiable. A must contain $\lnot \varphi$ because otherwise it would be satisfiable. Because adding more sentences to A does not change unsatisfiability, we can assume that A contains the field axioms and, for some $k,$ the first k sentences of the form $1+1+\cdots +1\neq 0.$ Let B contain all the sentences of A except $\lnot \varphi .$ Then any field with a characteristic greater than k is a model of $B,$ and $\lnot \varphi$ together with B is not satisfiable. This means that $\varphi$ must hold in every model of $B,$ which means precisely that $\varphi$ holds in every field of characteristic greater than $k.$ This completes the proof.

The Lefschetz principle, one of the first examples of a transfer principle, extends this result. A first-order sentence $\varphi$ in the language of rings is true in *some* (or equivalently, in *every*) algebraically closed field of characteristic 0 (such as the complex numbers for instance) if and only if there exist infinitely many primes p for which $\varphi$ is true in *some* algebraically closed field of characteristic $p,$ in which case $\varphi$ is true in *all* algebraically closed fields of sufficiently large non-0 characteristic $p.$ One consequence is the following special case of the Ax–Grothendieck theorem: all injective complex polynomials $\mathbb {C} ^{n}\to \mathbb {C} ^{n}$ are surjective (indeed, it can even be shown that its inverse will also be a polynomial). In fact, the surjectivity conclusion remains true for any injective polynomial $F^{n}\to F^{n}$ where F is a finite field or the algebraic closure of such a field.

### Upward Löwenheim–Skolem theorem

A second application of the compactness theorem shows that any theory that has arbitrarily large finite models, or a single infinite model, has models of arbitrary large cardinality (this is the Upward Löwenheim–Skolem theorem). So for instance, there are nonstandard models of Peano arithmetic with uncountably many 'natural numbers'. To achieve this, let T be the initial theory and let $\kappa$ be any cardinal number. Add to the language of T one constant symbol for every element of $\kappa .$ Then add to T a collection of sentences that say that the objects denoted by any two distinct constant symbols from the new collection are distinct (this is a collection of $\kappa ^{2}$ sentences). Since every *finite* subset of this new theory is satisfiable by a sufficiently large finite model of $T,$ or by any infinite model, the entire extended theory is satisfiable. But any model of the extended theory has cardinality at least $\kappa$ .

### Non-standard analysis

A third application of the compactness theorem is the construction of nonstandard models of the real numbers, that is, consistent extensions of the theory of the real numbers that contain "infinitesimal" numbers. To see this, let $\Sigma$ be a first-order axiomatization of the theory of the real numbers. Consider the theory obtained by adding a new constant symbol $\varepsilon$ to the language and adjoining to $\Sigma$ the axiom $\varepsilon >0$ and the axioms $\varepsilon <{\tfrac {1}{n}}$ for all positive integers $n.$ Clearly, the standard real numbers $\mathbb {R}$ are a model for every finite subset of these axioms, because the real numbers satisfy everything in $\Sigma$ and, by suitable choice of $\varepsilon ,$ can be made to satisfy any finite subset of the axioms about $\varepsilon .$ By the compactness theorem, there is a model ${}^{*}\mathbb {R}$ that satisfies $\Sigma$ and also contains an infinitesimal element $\varepsilon .$

A similar argument, this time adjoining the axioms $\omega >0,\;\omega >1,\ldots ,$ etc., shows that the existence of numbers with infinitely large magnitudes cannot be ruled out by any axiomatization $\Sigma$ of the reals.

It can be shown that the hyperreal numbers ${}^{*}\mathbb {R}$ satisfy the transfer principle: a first-order sentence is true of $\mathbb {R}$ if and only if it is true of ${}^{*}\mathbb {R} .$

## Proofs

One can prove the compactness theorem using Gödel's completeness theorem, which establishes that a set of sentences is satisfiable if and only if no contradiction can be proven from it. Since proofs are always finite and therefore involve only finitely many of the given sentences, the compactness theorem follows. In fact, the compactness theorem is equivalent to Gödel's completeness theorem, and both are equivalent to the Boolean prime ideal theorem, a weak form of the axiom of choice.

Gödel originally proved the compactness theorem in just this way, but later some "purely semantic" proofs of the compactness theorem were found; that is, proofs that refer to *truth* instead of *provability*. One of those proofs relies on ultraproducts hinging on the axiom of choice as follows:

**Proof**: Fix a first-order language $L,$ and let $\Sigma$ be a collection of L -sentences such that every finite subcollection of L -sentences, $i\subseteq \Sigma$ of it has a model ${\mathcal {M}}_{i}.$ Also let ${\textstyle \prod _{i\subseteq \Sigma }{\mathcal {M}}_{i}}$ be the direct product of the structures and I be the collection of finite subsets of $\Sigma .$ For each $i\in I,$ let $A_{i}=\{j\in I:j\supseteq i\}.$ The family of all of these sets $A_{i}$ generates a proper filter, so there is an ultrafilter U containing all sets of the form $A_{i}.$

Now for any sentence $\varphi$ in ${\displaystyle \Sigma$

- the set $A_{\{\varphi \}}$ is in U
- whenever $j\in A_{\{\varphi \}},$ then $\varphi \in j,$ hence $\varphi$ holds in ${\mathcal {M}}_{j}$
- the set of all j with the property that $\varphi$ holds in ${\mathcal {M}}_{j}$ is a superset of $A_{\{\varphi \}},$ hence also in U

Łoś's theorem now implies that $\varphi$ holds in the ultraproduct ${\textstyle \prod _{i\subseteq \Sigma }{\mathcal {M}}_{i}/U.}$ So this ultraproduct satisfies all formulas in $\Sigma .$
