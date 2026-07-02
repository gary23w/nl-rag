---
title: "Knuth–Bendix completion algorithm"
source: https://en.wikipedia.org/wiki/Knuth%E2%80%93Bendix_completion_algorithm
domain: knuth-bendix
license: CC-BY-SA-4.0
tags: Knuth-Bendix completion, completion algorithm, reduction ordering, equational theory
fetched: 2026-07-02
---

# Knuth–Bendix completion algorithm

The **Knuth–Bendix completion algorithm** (named after Donald Knuth and Peter Bendix) is a semi-decision algorithm for transforming a set of equations (over terms) into a confluent term rewriting system. When the algorithm succeeds, it effectively solves the word problem for the specified algebra.

Buchberger's algorithm for computing Gröbner bases is a very similar algorithm. Although developed independently, it may also be seen as the instantiation of Knuth–Bendix algorithm in the theory of polynomial rings.

## Introduction

For a set *E* of equations, its **deductive closure** (⁎⟷*E*) is the set of all equations that can be derived by applying equations from *E* in any order. Formally, *E* is considered a binary relation, (⟶*E*) is its rewrite closure, and (⁎⟷*E*) is the equivalence closure of (⟶*E*). For a set *R* of rewrite rules, its **deductive closure** (⁎⟶*R* ∘ ⁎⟵*R*) is the set of all equations that can be confirmed by applying rules from *R* left-to-right to both sides until they are literally equal. Formally, *R* is again viewed as a binary relation, (⟶*R*) is its rewrite closure, (⟵*R*) is its converse, and (⁎⟶*R* ∘ ⁎⟵*R*) is the relation composition of their reflexive transitive closures (⁎⟶*R* and ⁎⟵*R*).

For example, if *E* = {1⋅*x* = *x*, *x*−1⋅*x* = 1, (*x*⋅*y*)⋅*z* = *x*⋅(*y*⋅*z*)} are the group axioms, the derivation chain

a

−1

⋅(

a

⋅

b

)

⁎

⟷

E

(

a

−1

⋅

a

)⋅

b

⁎

⟷

E

1⋅

b

⁎

⟷

E

b

demonstrates that *a*−1⋅(*a*⋅*b*) ⁎⟷*E* *b* is a member of *E'*s deductive closure. If *R* = { 1⋅*x* → *x*, *x*−1⋅*x* → 1, (*x*⋅*y*)⋅*z* → *x*⋅(*y*⋅*z*) } is a "rewrite rule" version of *E*, the derivation chains

(

a

−1

⋅

a

)⋅

b

⁎

⟶

R

1⋅

b

⁎

⟶

R

b

and

b

⁎

⟵

R

b

demonstrate that (*a*−1⋅*a*)⋅*b* ⁎⟶*R*∘⁎⟵*R* *b* is a member of *R'*s deductive closure. However, there is no way to derive *a*−1⋅(*a*⋅*b*) ⁎⟶*R*∘⁎⟵*R* *b* similar to above, since a right-to-left application of the rule (*x*⋅*y*)⋅*z* → *x*⋅(*y*⋅*z*) is not allowed.

The Knuth–Bendix algorithm takes a set *E* of equations between terms, and a reduction ordering (>) on the set of all terms, and attempts to construct a confluent and terminating term rewriting system *R* that has the same deductive closure as *E*. While proving consequences from *E* often requires human intuition, proving consequences from *R* does not. For more details, see Confluence (abstract rewriting)#Motivating examples, which gives an example proof from group theory, performed both using *E* and using *R*.

## Rules

Given a set *E* of equations between terms, the following inference rules can be used to transform it into an equivalent convergent term rewrite system (if possible): They are based on a user-given reduction ordering (>) on the set of all terms; it is lifted to a well-founded ordering (▻) on the set of rewrite rules by defining (*s* → *t*) ▻ (*l* → *r*) if

- *s* >e *l* in the encompassment ordering, or
- s and l are literally similar and *t* > *r*.

| **Delete** | ‹ *E*∪{*s* = *s*} | , *R* › | ⊢ | ‹ *E* | , *R* › |   |
|---|---|---|---|---|---|---|
| **Compose** | ‹ *E* | , *R*∪{*s* → *t*} › | ⊢ | ‹ *E* | , *R*∪{*s* → *u*} › | if *t* ⟶*R* *u* |
| **Simplify** | ‹ *E*∪{*s* = *t*} | , *R* › | ⊢ | ‹ *E*∪{*s* = *u*} | , *R* › | if *t* ⟶*R* *u* |
| **Orient** | ‹ *E*∪{*s* = *t*} | , *R* › | ⊢ | ‹ *E* | , *R*∪{*s* → *t*}  › | if *s* > *t* |
| **Collapse** | ‹ *E* | , *R*∪{*s* → *t*} › | ⊢ | ‹ *E*∪{*u* = *t*} | , *R* › | if *s* ⟶*R* *u* by *l* → *r* with (*s* → *t*) ▻ (*l* → *r*) |
| **Deduce** | ‹ *E* | , *R* › | ⊢ | ‹ *E*∪{*s* = *t*} | , *R* › | if (*s*,*t*) is a critical pair of *R* |

## Example

The following example run, obtained from the E theorem prover, computes a completion of the (additive) group axioms as in Knuth, Bendix (1970). It starts with the three initial equations for the group (neutral element 0, inverse elements, associativity), using `f(X,Y)` for *X*+*Y*, and `i(X)` for −*X*. The 10 starred equations turn out to constitute the resulting convergent rewrite system. "pm" is short for "paramodulation", implementing *deduce*. Critical pair computation is an instance of paramodulation for equational unit clauses. "rw" is rewriting, implementing *compose*, *collapse*, and *simplify*. Orienting of equations is done implicitly and not recorded.

| **Nr** |   | **Lhs** |   | **Rhs** | **Source** |
|---|---|---|---|---|---|
| 1: | * | f(X,0) | = | X | initial("GROUP.lop", at_line_9_column_1) |
| 2: | * | f(X,i(X)) | = | 0 | initial("GROUP.lop", at_line_12_column_1) |
| 3: | * | f(f(X,Y),Z) | = | f(X,f(Y,Z)) | initial("GROUP.lop", at_line_15_column_1) |
| 5: |   | f(X,Y) | = | f(X,f(0,Y)) | pm(3,1) |
| 6: |   | f(X,f(Y,i(f(X,Y)))) | = | 0 | pm(2,3) |
| 7: |   | f(0,Y) | = | f(X,f(i(X),Y)) | pm(3,2) |
| 27: |   | f(X,0) | = | f(0,i(i(X))) | pm(7,2) |
| 36: |   | X | = | f(0,i(i(X))) | rw(27,1) |
| 46: |   | f(X,Y) | = | f(X,i(i(Y))) | pm(5,36) |
| 52: | * | f(0,X) | = | X | rw(36,46) |
| 60: | * | i(0) | = | 0 | pm(2,52) |
| 63: |   | i(i(X)) | = | f(0,X) | pm(46,52) |
| 64: | * | f(X,f(i(X),Y)) | = | Y | rw(7,52) |
| 67: | * | i(i(X)) | = | X | rw(63,52) |
| 74: | * | f(i(X),X) | = | 0 | pm(2,67) |
| 79: |   | f(0,Y) | = | f(i(X),f(X,Y)) | pm(3,74) |
| 83: | * | Y | = | f(i(X),f(X,Y)) | rw(79,52) |
| 134: |   | f(i(X),0) | = | f(Y,i(f(X,Y))) | pm(83,6) |
| 151: |   | i(X) | = | f(Y,i(f(X,Y))) | rw(134,1) |
| 165: | * | f(i(X),i(Y)) | = | i(f(Y,X)) | pm(83,151) |

See also Word problem (mathematics) for another presentation of this example.

## String rewriting systems in group theory

An important case in computational group theory is string rewriting systems which can be used to give canonical labels to elements or cosets of a finitely presented group as products of the generators. This special case is the focus of this section.

### Motivation in group theory

The critical pair lemma states that a term rewriting system is locally confluent (or weakly confluent) if and only if all its critical pairs are convergent. Furthermore, we have Newman's lemma which states that if an (abstract) rewriting system is strongly normalizing and weakly confluent, then the rewriting system is confluent. So, if we can add rules to the term rewriting system in order to force all critical pairs to be convergent while maintaining the strong normalizing property, then this will force the resultant rewriting system to be confluent.

Consider a finitely presented monoid $M=\langle X\mid R\rangle$ where X is a finite set of generators and R is a set of defining relations on X. Let X* be the set of all words in X (i.e. the free monoid generated by X). Since the relations R generate an equivalence relation on X*, one can consider elements of M to be the equivalence classes of X* under R. For each class *{w1, w2, ... }* it is desirable to choose a standard representative *wk*. This representative is called the **canonical** or **normal form** for each word *wk* in the class. If there is a computable method to determine for each *wk* its normal form *wi* then the word problem is easily solved. A confluent rewriting system allows one to do precisely this.

Although the choice of a canonical form can theoretically be made in an arbitrary fashion this approach is generally not computable. (Consider that an equivalence relation on a language can produce an infinite number of infinite classes.) If the language is well-ordered then the order < gives a consistent method for defining minimal representatives, however computing these representatives may still not be possible. In particular, if a rewriting system is used to calculate minimal representatives then the order < should also have the property:

A < B → XAY < XBY for all words A,B,X,Y

This property is called **translation invariance**. An order that is both translation-invariant and a well-order is called a **reduction order**.

From the presentation of the monoid it is possible to define a rewriting system given by the relations R. If A x B is in R then either A < B in which case B → A is a rule in the rewriting system, otherwise A > B and A → B. Since < is a reduction order a given word W can be reduced W > W_1 > ... > W_n where W_n is irreducible under the rewriting system. However, depending on the rules that are applied at each Wi → Wi+1 it is possible to end up with two different irreducible reductions Wn ≠ W'm of W. However, if the rewriting system given by the relations is converted to a confluent rewriting system via the Knuth–Bendix algorithm, then all reductions are guaranteed to produce the same irreducible word, namely the normal form for that word.

### Description of the algorithm for finitely presented monoids

Suppose we are given a presentation $\langle X\mid R\rangle$ , where X is a set of generators and R is a set of relations giving the rewriting system. Suppose further that we have a reduction ordering < among the words generated by X (e.g., shortlex order). For each relation $P_{i}=Q_{i}$ in R , suppose $Q_{i}<P_{i}$ . Thus we begin with the set of reductions $P_{i}\rightarrow Q_{i}$ .

First, if any relation $P_{i}=Q_{i}$ can be reduced, replace $P_{i}$ and $Q_{i}$ with the reductions.

Next, we add more reductions (that is, rewriting rules) to eliminate possible exceptions of confluence. Suppose that $P_{i}$ and $P_{j}$ overlap.

1. Case 1: either the prefix of $P_{i}$ equals the suffix of $P_{j}$ , or vice versa. In the former case, we can write $P_{i}=BC$ and $P_{j}=AB$ ; in the latter case, $P_{i}=AB$ and $P_{j}=BC$ .
2. Case 2: either $P_{i}$ is completely contained in (surrounded by) $P_{j}$ , or vice versa. In the former case, we can write $P_{i}=B$ and $P_{j}=ABC$ ; in the latter case, $P_{i}=ABC$ and $P_{j}=B$ .

Reduce the word $ABC$ using $P_{i}$ first, then using $P_{j}$ first. Call the results $r_{1},r_{2}$ , respectively. If $r_{1}\neq r_{2}$ , then we have an instance where confluence could fail. Hence, add the reduction $\max r_{1},r_{2}\rightarrow \min r_{1},r_{2}$ to R .

After adding a rule to R , remove any rules in R that might have reducible left sides (after checking if such rules have critical pairs with other rules).

Repeat the procedure until all overlapping left sides have been checked.

### Examples

#### A terminating example

Consider the monoid:

$\langle x,y\mid x^{3}=y^{3}=(xy)^{3}=1\rangle$

.

We use the shortlex order. This is an infinite monoid but nevertheless, the Knuth–Bendix algorithm is able to solve the word problem.

Our beginning three reductions are therefore

| $x^{3}\rightarrow 1$ |   | 1 |
|---|---|---|

| $y^{3}\rightarrow 1$ |   | 2 |
|---|---|---|

| $(xy)^{3}\rightarrow 1$ . |   | 3 |
|---|---|---|

A suffix of $x^{3}$ (namely x ) is a prefix of $(xy)^{3}=xyxyxy$ , so consider the word $x^{3}yxyxy$ . Reducing using (**1**), we get $yxyxy$ . Reducing using (**3**), we get $x^{2}$ . Hence, we get $yxyxy=x^{2}$ , giving the reduction rule

| $yxyxy\rightarrow x^{2}$ . |   | 4 |
|---|---|---|

Similarly, using $xyxyxy^{3}$ and reducing using (**2**) and (**3**), we get $xyxyx=y^{2}$ . Hence the reduction

| $xyxyx\rightarrow y^{2}$ . |   | 5 |
|---|---|---|

Both of these rules obsolete (**3**), so we remove it.

Next, consider $x^{3}yxyx$ by overlapping (**1**) and (**5**). Reducing we get $yxyx=x^{2}y^{2}$ , so we add the rule

| $yxyx\rightarrow x^{2}y^{2}$ . |   | 6 |
|---|---|---|

Considering $xyxyx^{3}$ by overlapping (**1**) and (**5**), we get $xyxy=y^{2}x^{2}$ , so we add the rule

| $y^{2}x^{2}\rightarrow xyxy$ . |   | 7 |
|---|---|---|

These obsolete rules (**4**) and (**5**), so we remove them.

Now, we are left with the rewriting system

| $x^{3}\rightarrow 1$ |   | (**1**) |
|---|---|---|

| $y^{3}\rightarrow 1$ |   | (**2**) |
|---|---|---|

| $yxyx\rightarrow x^{2}y^{2}$ |   | (**6**) |
|---|---|---|

| $y^{2}x^{2}\rightarrow xyxy$ . |   | (**7**) |
|---|---|---|

Checking the overlaps of these rules, we find no potential failures of confluence. Therefore, we have a confluent rewriting system, and the algorithm terminates successfully.

#### A non-terminating example

The order of the generators may crucially affect whether the Knuth–Bendix completion terminates. As an example, consider the free Abelian group by the monoid presentation:

$\langle x,y,x^{-1},y^{-1}\,|\,xy=yx,xx^{-1}=x^{-1}x=yy^{-1}=y^{-1}y=1\rangle .$

The Knuth–Bendix completion with respect to lexicographic order $x<x^{-1}<y<y^{-1}$ finishes with a convergent system, however considering the length-lexicographic order $x<y<x^{-1}<y^{-1}$ it does not finish for there are no finite convergent systems compatible with this latter order.

## Generalizations

If Knuth–Bendix does not succeed, it will either run forever and produce successive approximations to an infinite complete system, or fail when it encounters an unorientable equation (i.e. an equation that it cannot turn into a rewrite rule). An enhanced version will not fail on unorientable equations and produces a ground confluent system, providing a semi-algorithm for the word problem.

The notion of logged rewriting discussed in the paper by Heyworth and Wensley listed below allows some recording or logging of the rewriting process as it proceeds. This is useful for computing identities among relations for presentations of groups.
