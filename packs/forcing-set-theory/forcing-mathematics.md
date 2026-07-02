---
title: "Forcing (mathematics)"
source: https://en.wikipedia.org/wiki/Forcing_(mathematics)
domain: forcing-set-theory
license: CC-BY-SA-4.0
tags: forcing method, continuum hypothesis, constructible universe, large cardinal
fetched: 2026-07-02
---

# Forcing (mathematics)

In set theory, **forcing** is a technique for proving consistency and independence results. Intuitively, forcing can be thought of as a technique to expand the set theoretical universe V to a larger universe $V[G]$ by introducing a new "generic" object G .

Forcing was first used by Paul Cohen in 1963, to prove the independence of the axiom of choice and the continuum hypothesis from Zermelo–Fraenkel set theory. It has been considerably reworked and simplified in the following years, and has since served as a powerful technique, both in set theory and in areas of mathematical logic such as computability theory. Descriptive set theory uses the notions of forcing from both computability theory and set theory. Forcing has also been used in model theory, but it is common in model theory to define genericity directly without mention of forcing.

## Intuition

Forcing is usually used to construct an expanded universe that satisfies some desired property. For example, the expanded universe might contain many new real numbers (at least $\aleph _{2}$ of them), identified with subsets of the set $\mathbb {N}$ of natural numbers, that were not there in the old universe, and thereby violate the continuum hypothesis.

In order to intuitively justify such an expansion, it is best to think of the "old universe" as a model M of the set theory, which is itself a set in the "real universe" V . By the Löwenheim–Skolem theorem, M can be chosen to be a "bare bones" model that is externally countable, which guarantees that there will be many subsets (in V ) of $\mathbb {N}$ that are not in M . Specifically, there is an ordinal $\aleph _{2}^{M}$ that "plays the role of the cardinal $\aleph _{2}$ " in M , but is actually countable in V . Working in V , it should be easy to find one distinct subset of $\mathbb {N}$ per each element of $\aleph _{2}^{M}$ . (For simplicity, this family of subsets can be characterized with a single subset $X\subseteq \aleph _{2}^{M}\times \mathbb {N}$ .)

However, in some sense, it may be desirable to "construct the expanded model $M[X]$ within M ". This would help ensure that $M[X]$ "resembles" M in certain aspects, such as $\aleph _{2}^{M[X]}$ being the same as $\aleph _{2}^{M}$ (more generally, that *cardinal collapse* does not occur), and allow fine control over the properties of $M[X]$ . More precisely, every member of $M[X]$ should be given a (non-unique) *name* in M . The name can be thought as an expression in terms of X , just like in a simple field extension $L=K(\theta )$ every element of L can be expressed in terms of $\theta$ . A major component of forcing is manipulating those names within M , so sometimes it may help to directly think of M as "the universe", knowing that the theory of forcing guarantees that $M[X]$ will correspond to an actual model.

A subtle point of forcing is that, if X is taken to be an *arbitrary* "missing subset" of some set in M , then the $M[X]$ constructed "within M " may not even be a model. This is because X may encode "special" information about M that is invisible within M (e.g. the countability of M ), and thus prove the existence of sets that are "too complex for M to describe".

Forcing avoids such problems by requiring the newly introduced set X to be a **generic set** relative to M . Some statements are "forced" to hold for any generic X : For example, a generic X is "forced" to be infinite. Furthermore, any property (describable in M ) of a generic set is "forced" to hold under some **forcing condition**. The concept of "forcing" can be defined within M , and it gives M enough reasoning power to prove that $M[X]$ is indeed a model that satisfies the desired properties.

Cohen's original technique, now called ramified forcing, is slightly different from the **unramified forcing** expounded here. Forcing is also equivalent to the method of Boolean-valued models, which some feel is conceptually more natural and intuitive, but usually much more difficult to apply.

### The role of the model

In order for the above approach to work smoothly, M must in fact be a standard transitive model in V , so that membership and other elementary notions can be handled intuitively in both M and V . A standard transitive model can be obtained from any standard model through the Mostowski collapse lemma, but the existence of any standard model of ${\mathsf {ZFC}}$ (or any variant thereof) is in itself a stronger assumption than the consistency of ${\mathsf {ZFC}}$ .

To get around this issue, a standard technique is to let M be a standard transitive model of an arbitrary finite subset of ${\mathsf {ZFC}}$ (any axiomatization of ${\mathsf {ZFC}}$ has at least one axiom schema, and thus an infinite number of axioms), the existence of which is guaranteed by the reflection principle. As the goal of a forcing argument is to prove consistency results, this is enough since any inconsistency in a theory must manifest with a derivation of a finite length, and thus involve only a finite number of axioms.

## Forcing conditions and forcing posets

Each forcing condition can be regarded as a *finite* piece of information regarding the object X adjoined to the model. There are many different ways of providing information about an object, which give rise to different **forcing notions**. A general approach to formalizing forcing notions is to regard forcing conditions as abstract objects with a poset structure.

A **forcing poset** is an ordered triple, $(\mathbb {P} ,\leq ,\mathbf {1} )$ , where $\leq$ is a preorder on $\mathbb {P}$ , and $\mathbf {1}$ is the largest element. Members of $\mathbb {P}$ are the **forcing conditions** (or just **conditions**). The order relation $p\leq q$ means " p is **stronger** than q ". (Intuitively, the "smaller" condition provides "more" information, just as the smaller interval $[3.1415926,3.1415927]$ provides more information about the number π than the interval $[3.1,3.2]$ does.) Furthermore, the preorder $\leq$ must satisfy the **splitting condition**:

- For each $p\in \mathbb {P}$ , there are $q,r\in \mathbb {P}$ such that $q,r\leq p$ , with no $s\in \mathbb {P}$ such that $s\leq q,r$ .

In other words, it must be possible to strengthen any forcing condition p in at least two incompatible directions. Intuitively, this is because p is only a finite piece of information, whereas an infinite piece of information is needed to determine X .

There are various conventions in use. Some authors require $\leq$ to also be antisymmetric, so that the relation is a partial order. Some use the term partial order anyway, conflicting with standard terminology, while some use the term preorder. The largest element can be dispensed with. The reverse ordering is also used, most notably by Saharon Shelah and his co-authors.

### Examples

Let S be any infinite set (such as $\mathbb {N}$ ), and let the generic object in question be a new subset $X\subseteq S$ . In Cohen's original formulation of forcing, each forcing condition is a *finite* set of sentences, either of the form $a\in X$ or $a\notin X$ , that are self-consistent (i.e. $a\in X$ *and* $a\notin X$ for the same value of a do not appear in the same condition). This forcing notion is usually called **Cohen forcing**.

The forcing poset for Cohen forcing can be formally written as $(\operatorname {Fin} (S,2),\supseteq ,\emptyset )$ , the finite partial functions from S to $2~{\stackrel {\text{df}}{=}}~\{0,1\}$ under *reverse* inclusion. Cohen forcing satisfies the splitting condition because given any condition p , one can always find an element $a\in S$ not mentioned in p , and add either the sentence $a\in X$ or $a\notin X$ to p to get two new forcing conditions, incompatible with each other.

Another instructive example of a forcing poset is $(\operatorname {Bor} (I),\subseteq ,I)$ , where $I=[0,1]$ and $\operatorname {Bor} (I)$ is the collection of Borel subsets of I having non-zero Lebesgue measure. The generic object associated with this forcing poset is a **random real number** $r\in [0,1]$ . It can be shown that r falls in every Borel subset of $[0,1]$ with measure 1, provided that the Borel subset is "described" in the original unexpanded universe (this can be formalized with the concept of *Borel codes*). Each forcing condition can be regarded as a random event with probability equal to its measure. Due to the ready intuition this example can provide, probabilistic language is sometimes used with other divergent forcing posets.

## Generic filters

Even though each individual forcing condition p cannot fully determine the generic object X , the set $G\subseteq \mathbb {P}$ of all true forcing conditions does determine X . In fact, without loss of generality, G is commonly considered to *be* the generic object adjoined to M , so the expanded model is called $M[G]$ . It is usually easy enough to show that the originally desired object X is indeed in the model $M[G]$ .

Under this convention, the concept of "generic object" can be described in a general way. Specifically, the set G should be a **generic filter** on $\mathbb {P}$ relative to M . The "filter" condition means that it makes sense that G is a set of all true forcing conditions:

- $G\subseteq \mathbb {P$
- $\mathbf {1} \in G;$
- if $p\geq q\in G$ , then $p\in G;$
- if $p,q\in G$ , then there exists an $r\in G$ such that $r\leq p,q.$

For G to be "generic relative to M " means:

- If $D\in M$ is a "dense" subset of $\mathbb {P}$ (that is, for each $p\in \mathbb {P}$ , there exists a $q\in D$ such that $q\leq p$ ), then $G\cap D\neq \varnothing$ .

Given that M is a countable model, the existence of a generic filter G follows from the Rasiowa–Sikorski lemma. In fact, slightly more is true: Given a condition $p\in \mathbb {P}$ , one can find a generic filter G such that $p\in G$ . Due to the splitting condition on $\mathbb {P}$ , if G is a filter, then $\mathbb {P} \setminus G$ is dense. If $G\in M$ , then $\mathbb {P} \setminus G\in M$ because M is a model of ${\mathsf {ZFC}}$ . For this reason, a generic filter is never in M .

## P-names and interpretations

Associated with a forcing poset $\mathbb {P}$ is the class $V^{(\mathbb {P} )}$ of $\mathbb {P}$ -**names**. A $\mathbb {P}$ -name is a set A of the form

$A\subseteq \{(u,p)\mid u~{\text{is a}}~\mathbb {P} {\text{-name and}}~p\in \mathbb {P} \}.$

Given any filter G on $\mathbb {P}$ , the **interpretation** or **valuation** map from $\mathbb {P}$ -names is given by

$\operatorname {val} (u,G)=\{\operatorname {val} (v,G)\mid \exists p\in G:~(v,p)\in u\}.$

The $\mathbb {P}$ -names are, in fact, an expansion of the universe. Given $x\in V$ , one defines ${\check {x}}$ to be the $\mathbb {P}$ -name

${\check {x}}=\{({\check {y}},\mathbf {1} )\mid y\in x\}.$

Since $\mathbf {1} \in G$ , it follows that $\operatorname {val} ({\check {x}},G)=x$ . In a sense, ${\check {x}}$ is a "name for x " that does not depend on the specific choice of G .

This also allows defining a "name for G " without explicitly referring to G :

${\underline {G}}=\{({\check {p}},p)\mid p\in \mathbb {P} \}$

so that $\operatorname {val} ({\underline {G}},G)=\{\operatorname {val} ({\check {p}},G)\mid p\in G\}=G$ .

### Rigorous definitions

The concepts of $\mathbb {P}$ -names, interpretations, and ${\check {x}}$ may be defined by transfinite recursion. With $\varnothing$ the empty set, $\alpha +1$ the successor ordinal to ordinal $\alpha$ , ${\mathcal {P}}$ the power-set operator, and $\lambda$ a limit ordinal, define the following hierarchy:

${\begin{aligned}\operatorname {Name} (\varnothing )&=\varnothing ,\\\operatorname {Name} (\alpha +1)&={\mathcal {P}}(\operatorname {Name} (\alpha )\times \mathbb {P} ),\\\operatorname {Name} (\lambda )&=\bigcup \{\operatorname {Name} (\alpha )\mid \alpha <\lambda \}.\end{aligned}}$

Then the class of $\mathbb {P}$ -names is defined as

$V^{(\mathbb {P} )}=\bigcup \{\operatorname {Name} (\alpha )~|~\alpha ~{\text{is an ordinal}}\}.$

The interpretation map and the map $x\mapsto {\check {x}}$ can similarly be defined with a hierarchical construction.

## Forcing

Given a generic filter $G\subseteq \mathbb {P}$ , one proceeds as follows. The subclass of $\mathbb {P}$ -names in M is denoted $M^{(\mathbb {P} )}$ . Let

$M[G]=\left\{\operatorname {val} (u,G)~{\Big |}~u\in M^{(\mathbb {P} )}\right\}.$

To reduce the study of the set theory of $M[G]$ to that of M , one works with the "forcing language", which is built up like ordinary first-order logic, with membership as the binary relation and all the $\mathbb {P}$ -names as constants.

Define $p\Vdash _{M,\mathbb {P} }\varphi (u_{1},\ldots ,u_{n})$ (to be read as " p forces $\varphi$ in the model M with poset $\mathbb {P}$ "), where p is a condition, $\varphi$ is a formula in the forcing language, and the $u_{i}$ 's are $\mathbb {P}$ -names, to mean that if G is a generic filter containing p , then $M[G]\models \varphi (\operatorname {val} (u_{1},G),\ldots ,\operatorname {val} (u_{n},G))$ . The special case $\mathbf {1} \Vdash _{M,\mathbb {P} }\varphi$ is often written as " $\mathbb {P} \Vdash _{M,\mathbb {P} }\varphi$ " or simply " $\Vdash _{M,\mathbb {P} }\varphi$ ". Such statements are true in $M[G]$ , no matter what G is.

What is important is that this **external** definition of the forcing relation $p\Vdash _{M,\mathbb {P} }\varphi$ is equivalent to an **internal** definition within M , defined by transfinite induction (specifically $\in$ -induction) over the $\mathbb {P}$ -names on instances of $u\in v$ and $u=v$ , and then by ordinary induction over the complexity of formulae. This has the effect that all the properties of $M[G]$ are really properties of M , and the verification of ${\mathsf {ZFC}}$ in $M[G]$ becomes straightforward. This is usually summarized as the following three key properties:

- **Truth**: $M[G]\models \varphi (\operatorname {val} (u_{1},G),\ldots ,\operatorname {val} (u_{n},G))$ if and only if it is forced by G , that is, for some condition $p\in G$ , we have $p\Vdash _{M,\mathbb {P} }\varphi (u_{1},\ldots ,u_{n})$ .
- **Definability**: The statement " $p\Vdash _{M,\mathbb {P} }\varphi (u_{1},\ldots ,u_{n})$ " is definable in M .
- **Coherence**: $p\Vdash _{M,\mathbb {P} }\varphi (u_{1},\ldots ,u_{n})\land q\leq p\implies q\Vdash _{M,\mathbb {P} }\varphi (u_{1},\ldots ,u_{n})$ .

### Internal definition

There are many different but equivalent ways to define the forcing relation $\Vdash _{M,\mathbb {P} }$ in M . One way to simplify the definition is to first define a modified forcing relation $\Vdash _{M,\mathbb {P} }^{*}$ that is strictly stronger than $\Vdash _{M,\mathbb {P} }$ . The modified relation $\Vdash _{M,\mathbb {P} }^{*}$ still satisfies the three key properties of forcing, but $p\Vdash _{M,\mathbb {P} }^{*}\varphi$ and $p\Vdash _{M,\mathbb {P} }^{*}\varphi '$ are not necessarily equivalent even if the first-order formulae $\varphi$ and $\varphi '$ are equivalent. The unmodified forcing relation can then be defined as $p\Vdash _{M,\mathbb {P} }\varphi \iff p\Vdash _{M,\mathbb {P} }^{*}\neg \neg \varphi .$ In fact, Cohen's original concept of forcing is essentially $\Vdash _{M,\mathbb {P} }^{*}$ rather than $\Vdash _{M,\mathbb {P} }$ .

The modified forcing relation $\Vdash _{M,\mathbb {P} }^{*}$ can be defined recursively as follows:

1. $p\Vdash _{M,\mathbb {P} }^{*}u\in v$ means $(\exists (w,q)\in v)(q\geq p\wedge p\Vdash _{M,\mathbb {P} }^{*}w=u).$
2. $p\Vdash _{M,\mathbb {P} }^{*}u\neq v$ means $(\exists (w,q)\in v)(q\geq p\wedge p\Vdash _{M,\mathbb {P} }^{*}w\notin u)\vee (\exists (w,q)\in u)(q\geq p\wedge p\Vdash _{M,\mathbb {P} }^{*}w\notin v).$
3. $p\Vdash _{M,\mathbb {P} }^{*}\neg \varphi$ means $\neg (\exists q\leq p)(q\Vdash _{M,\mathbb {P} }^{*}\varphi ).$
4. $p\Vdash _{M,\mathbb {P} }^{*}(\varphi \vee \psi )$ means $(p\Vdash _{M,\mathbb {P} }^{*}\varphi )\vee (p\Vdash _{M,\mathbb {P} }^{*}\psi ).$
5. $p\Vdash _{M,\mathbb {P} }^{*}\exists x\,\varphi (x)$ means $(\exists u\in M^{(\mathbb {P} )})(p\Vdash _{M,\mathbb {P} }^{*}\varphi (u)).$

Other symbols of the forcing language can be defined in terms of these symbols: For example, $u=v$ means $\neg (u\neq v)$ , $\forall x\,\varphi (x)$ means $\neg \exists x\,\neg \varphi (x)$ , etc. Cases 1 and 2 depend on each other and on case 3, but the recursion always refers to $\mathbb {P}$ -names with lesser ranks, so transfinite induction allows the definition to go through.

By construction, $\Vdash _{M,\mathbb {P} }^{*}$ (and thus $\Vdash _{M,\mathbb {P} }$ ) automatically satisfies **Definability**. The proof that $\Vdash _{M,\mathbb {P} }^{*}$ also satisfies **Truth** and **Coherence** is by inductively inspecting each of the five cases above. Cases 4 and 5 are trivial (thanks to the choice of $\vee$ and $\exists$ as the elementary symbols), cases 1 and 2 rely only on the assumption that G is a filter, and only case 3 requires G to be a *generic* filter.

Formally, an internal definition of the forcing relation (such as the one presented above) is actually a transformation of an arbitrary formula $\varphi (x_{1},\dots ,x_{n})$ to another formula $p\Vdash _{\mathbb {P} }\varphi (u_{1},\dots ,u_{n})$ where p and $\mathbb {P}$ are additional variables. The model M does not explicitly appear in the transformation (note that within M , $u\in M^{(\mathbb {P} )}$ just means " u is a $\mathbb {P}$ -name"), and indeed one may take this transformation as a "syntactic" definition of the forcing relation in the universe V of all sets regardless of any countable transitive model. However, if one wants to force over some countable transitive model M , then the latter formula should be interpreted under M (i.e. with all quantifiers ranging only over M ), in which case it is equivalent to the external "semantic" definition of $\Vdash _{M,\mathbb {P} }$ described at the top of this section:

For any formula

$\varphi (x_{1},\dots ,x_{n})$

there is a theorem

T

of the theory

${\mathsf {ZFC}}$

(for example, a conjunction of a finite number of axioms) such that for any countable transitive model

M

such that

$M\models T$

and any partial order satisfying the splitting condition

$\mathbb {P} \in M$

and any

$\mathbb {P}$

-generic filter

G

over

M

$(\forall a_{1},\ldots ,a_{n}\in M^{(\mathbb {P} )})(\forall p\in \mathbb {P} )(p\Vdash _{M,\mathbb {P} }\varphi (a_{1},\dots ,a_{n})\,\Leftrightarrow \,M\models p\Vdash _{\mathbb {P} }\varphi (a_{1},\dots ,a_{n})).$

This is the sense in which the forcing relation is indeed "definable in M ".

## Consistency

The discussion above can be summarized by the fundamental consistency result that, given a forcing poset $\mathbb {P}$ , we may assume the existence of a generic filter G , not belonging to the universe V , such that $V[G]$ is again a set-theoretic universe that models ${\mathsf {ZFC}}$ . Furthermore, all truths in $V[G]$ may be reduced to truths in V involving the forcing relation.

Both styles, adjoining G to either a countable transitive model M or the whole universe V , are commonly used. Less commonly seen is the approach using the "internal" definition of forcing, in which no mention of set or class models is made. This was Cohen's original method, and in one elaboration, it becomes the method of Boolean-valued analysis.

## Cohen forcing

The simplest nontrivial forcing poset is $(\operatorname {Fin} (\omega ,2),\supseteq ,\emptyset )$ , the finite partial functions from $\omega$ to $2~{\stackrel {\text{df}}{=}}~\{0,1\}$ under *reverse* inclusion. That is, a condition p is essentially two disjoint finite subsets ${p^{-1}}[1]$ and ${p^{-1}}[0]$ of $\omega$ , to be thought of as the "yes" and "no" parts of p , with no information provided on values outside the domain of p . " q is stronger than p " means that $q\supseteq p$ , in other words, the "yes" and "no" parts of q are supersets of the "yes" and "no" parts of p , and in that sense, provide more information.

Let G be a generic filter for this poset. If p and q are both in G , then $p\cup q$ is a condition because G is a filter. This means that $g=\bigcup G$ is a well-defined partial function from $\omega$ to 2 because any two conditions in G agree on their common domain.

In fact, g is a total function. Given $n\in \omega$ , let $D_{n}=\{p\mid p(n)~{\text{is defined}}\}$ . Then $D_{n}$ is dense. (Given any p , if n is not in p 's domain, adjoin a value for n —the result is in $D_{n}$ .) A condition $p\in G\cap D_{n}$ has n in its domain, and since $p\subseteq g$ , we find that $g(n)$ is defined.

Let $X={g^{-1}}[1]$ , the set of all "yes" members of the generic conditions. It is possible to give a name for X directly. Let

${\underline {X}}=\left\{\left({\check {n}},p\right)\mid p(n)=1\right\}.$

Then $\operatorname {val} ({\underline {X}},G)=X.$ Now suppose that $A\subseteq \omega$ in V . We claim that $X\neq A$ . Let

$D_{A}=\{p\mid \exists n(n\in \operatorname {Dom} (p)\land (p(n)=1\iff n\notin A))\}.$

Then $D_{A}$ is dense. (Given any p , find n that is not in its domain, and adjoin a value for n contrary to the status of " $n\in A$ ".) Then any $p\in G\cap D_{A}$ witnesses $X\neq A$ . To summarize, X is a "new" subset of $\omega$ , necessarily infinite.

Replacing $\omega$ with $\omega \times \omega _{2}$ , that is, considering instead finite partial functions whose inputs are of the form $(n,\alpha )$ , with $n<\omega$ and $\alpha <\omega _{2}$ , and whose outputs are 0 or 1 , one gets $\omega _{2}$ new subsets of $\omega$ . They are all distinct, by a density argument: Given $\alpha <\beta <\omega _{2}$ , let

$D_{\alpha ,\beta }=\{p\mid \exists n(p(n,\alpha )\neq p(n,\beta ))\},$

then each $D_{\alpha ,\beta }$ is dense, and a generic condition in it proves that the *α*th new set disagrees somewhere with the $\beta$ th new set.

This is not yet the falsification of the continuum hypothesis. One must prove that no new maps have been introduced that map $\omega$ onto $\omega _{1}$ , or $\omega _{1}$ onto $\omega _{2}$ . For example, if one considers instead $\operatorname {Fin} (\omega ,\omega _{1})$ , finite partial functions from $\omega$ to $\omega _{1}$ , the first uncountable ordinal, one gets in $V[G]$ a bijection from $\omega$ to $\omega _{1}$ . In other words, $\omega _{1}$ has *collapsed*, and in the forcing extension, is a countable ordinal.

The last step in showing the independence of the continuum hypothesis, then, is to show that Cohen forcing does not collapse cardinals. For this, a sufficient combinatorial property is that all of the antichains of the forcing poset are countable.

## The countable chain condition

A (strong) antichain A of $\mathbb {P}$ is a subset such that if $p,q\in A$ and $p\neq q$ , then p and q are **incompatible** (written $p\perp q$ ), meaning there is no r in $\mathbb {P}$ such that $r\leq p$ and $r\leq q$ . In the example on Borel sets, incompatibility means that $p\cap q$ has zero measure. In the example on finite partial functions, incompatibility means that $p\cup q$ is not a function, in other words, p and q assign different values to some domain input.

$\mathbb {P}$ is said to satisfy the *countable chain condition* (c.c.c.) if every antichain in $\mathbb {P}$ is countable. (The name, which is obviously inappropriate, is a holdover from older terminology. Some mathematicians write "c.a.c." for "countable antichain condition".)

It is easy to see that $\operatorname {Bor} (I)$ satisfies the c.c.c. because the measures add up to at most 1 . Also, $\operatorname {Fin} (E,2)$ satisfies the c.c.c., but the proof is more difficult.

Given an uncountable subfamily $W\subseteq \operatorname {Fin} (E,2)$ , shrink W to an uncountable subfamily $W_{0}$ of sets of size at most n , for some $n<\omega$ (for some n this is uncountable, since otherwise $W=\bigcup _{n<\omega }\{w\in W:|w|<n\}$ would be a countable union of countable sets, thus countable). If $p(e_{1})=b_{1}$ for uncountably many $p\in W_{0}$ , shrink this to an uncountable subfamily $W_{1}$ and repeat, getting a finite set $\{(e_{1},b_{1}),\ldots ,(e_{k},b_{k})\}\in W_{0}$ and an uncountable family $W_{k}$ of incompatible conditions of size $n-k$ such that every e is in $\operatorname {Dom} (p)$ for at most countable many $p\in W_{k}$ . Now, pick an arbitrary $p\in W_{k}$ , and pick from $W_{k}$ any q that is not one of the countably many members that have a domain member in common with p . Then $p\cup \{(e_{1},b_{1}),\ldots ,(e_{k},b_{k})\}$ and $q\cup \{(e_{1},b_{1}),\ldots ,(e_{k},b_{k})\}$ are compatible, so W is not an antichain. In other words, $\operatorname {Fin} (E,2)$ -antichains are countable.

The importance of antichains in forcing is that for most purposes, dense sets and maximal antichains are equivalent. A *maximal* antichain A is one that cannot be extended to a larger antichain. This means that every element $p\in \mathbb {P}$ is compatible with some member of A . The existence of a maximal antichain follows from Zorn's Lemma. Given a maximal antichain A , let

$D=\left\{p\in \mathbb {P} \mid (\exists q\in A)(p\leq q)\right\}.$

Then D is dense, and $G\cap D\neq \varnothing$ if and only if $G\cap A\neq \varnothing$ . Conversely, given a dense set D , Zorn's Lemma shows that there exists a maximal antichain $A\subseteq D$ , and then $G\cap D\neq \varnothing$ if and only if $G\cap A\neq \varnothing$ .

Assume that $\mathbb {P}$ satisfies the c.c.c. Given $x,y\in V$ , with $f:x\to y$ a function in $V[G]$ , one can approximate f inside V as follows. Let u be a name for f (by the definition of $V[G]$ ) and let p be a condition that forces u to be a function from x to y . Define a function $F:x\to {\mathcal {P}}(y)$ , by

$F(a){\stackrel {\text{df}}{=}}\left\{b\left|(\exists q\in \mathbb {P} )\left[(q\leq p)\land \left(q\Vdash ~u\left({\check {a}}\right)={\check {b}}\right)\right]\right\}.\right.$

By the definability of forcing, this definition makes sense within V . By the coherence of forcing, a different b must come from an incompatible p . By c.c.c., $F(a)$ is countable.

In summary, f is unknown in V as it depends on G , but it is not wildly unknown for a c.c.c.-forcing. One can identify a countable set of guesses for what the value of f is at any input, independent of G .

This has the following very important consequence. If in $V[G]$ , $f:\alpha \to \beta$ is a surjection from one infinite ordinal onto another, then there is a surjection $g:\omega \times \alpha \to \beta$ in V , and consequently, a surjection $h:\alpha \to \beta$ in V . In particular, cardinals cannot collapse. The conclusion is that $2^{\aleph _{0}}\geq \aleph _{2}$ in $V[G]$ .

## Easton forcing

The exact value of the continuum in the above Cohen model, and variants like $\operatorname {Fin} (\omega \times \kappa ,2)$ for cardinals $\kappa$ in general, was worked out by Robert M. Solovay, who also worked out how to violate ${\mathsf {GCH}}$ (the generalized continuum hypothesis), for regular cardinals only, a finite number of times. For example, in the above Cohen model, if ${\mathsf {CH}}$ holds in V , then $2^{\aleph _{0}}=\aleph _{2}$ holds in $V[G]$ .

William B. Easton worked out the proper class version of violating the ${\mathsf {GCH}}$ for regular cardinals, basically showing that the known restrictions, (monotonicity, Cantor's theorem and König's theorem), were the only ${\mathsf {ZFC}}$ -provable restrictions (see Easton's theorem).

Easton's work was notable in that it involved forcing with a proper class of conditions. In general, the method of forcing with a proper class of conditions fails to give a model of ${\mathsf {ZFC}}$ . For example, forcing with $\operatorname {Fin} (\omega \times \mathbf {On} ,2)$ , where $\mathbf {On}$ is the proper class of all ordinals, makes the continuum a proper class. On the other hand, forcing with $\operatorname {Fin} (\omega ,\mathbf {On} )$ introduces a countable enumeration of the ordinals. In both cases, the resulting $V[G]$ is visibly not a model of ${\mathsf {ZFC}}$ .

At one time, it was thought that more sophisticated forcing would also allow an arbitrary variation in the powers of singular cardinals. However, this has turned out to be a difficult, subtle and even surprising problem, with several more restrictions provable in ${\mathsf {ZFC}}$ and with the forcing models depending on the consistency of various large-cardinal properties. Many open problems remain.

## Random reals

Random forcing can be defined as forcing over the set P of all compact subsets of $[0,1]$ of positive measure, ordered by the relation $\subseteq$ (a smaller set in the context of inclusion is a smaller set in the ordering, and represents a condition with more information). There are two types of important dense sets:

1. For any positive integer n , the set $D_{n}=\left\{p\in P:\operatorname {diam} (p)<{\frac {1}{n}}\right\}$ is dense, where $\operatorname {diam} (p)$ is the diameter of the set p .
2. For any Borel subset $B\subseteq [0,1]$ of measure 1, the set $D_{B}=\{p\in P:p\subseteq B\}$ is dense.

For any filter G and any pair of elements $p_{1},p_{2}\in G$ there is $q\in G$ such that $q\leq p_{1},p_{2}$ . In this ordering, this means that any filter is closed under finite intersection. Therefore, by Cantor's intersection theorem, the intersection of *all* the elements in any filter is nonempty. If G is a filter intersecting the dense set $D_{n}$ for any positive integer n , then the filter G contains conditions of arbitrarily small positive diameter. Therefore, the intersection of all conditions from G has diameter 0. But the only nonempty sets of diameter 0 are singletons. So there is exactly one real number $r_{G}$ such that $r_{G}\in \bigcap G$ .

Let $B\subseteq [0,1]$ be any Borel set of measure 1. If G intersects $D_{B}$ , then $r_{G}\in B$ .

However, a generic filter over a countable transitive model M is not in M . The real $r_{G}$ defined by G is provably not an element of M . One issue with this construction is that if $p\in P$ , then $M\models$ " p is compact", but from the viewpoint of some larger universe $V\supseteq M$ , p can be non-compact and the intersection of all conditions from the generic filter G can then be empty. To fix this, we consider the set $C=\{{\bar {p}}:p\in G\}$ of topological closures of conditions from G . Because ${\bar {p}}\supseteq p$ , and because G is closed under finite intersection, Cantor's intersection theorem applies and the intersection of the set C is nonempty. Since $\operatorname {diam} ({\bar {p}})=\operatorname {diam} (p)$ and the ground model M inherits a metric from the universe V , the set C has elements of arbitrarily small diameter. Finally, there is exactly one real that belongs to all members of the set C . The generic filter G can be reconstructed from $r_{G}$ as $G=\{p\in P:r_{G}\in {\bar {p}}\}$ .

If $a\in M^{(\mathbb {P} )}$ is a name for $r_{G}$ (i.e., $M[G]\models val(a,G)=r_{G}$ ), and for $B\in M$ holds $M\models$ " B is a Borel set of measure 1", then by the truth property of forcing

$p\Vdash _{M,\mathbb {P} }a\in {\check {B}}$

for some $p\in G$ . There is a name a that satisfies

$\operatorname {val} (a,G)\in \bigcup _{p\in G}{\bar {p}}$

for any generic filter G . For that a ,

$p\Vdash _{M,\mathbb {P} }a\in {\check {B}}$

holds for any condition p .

Every Borel set can be (non-uniquely) built up, starting from intervals with rational endpoints and applying the operations of complement and countable union, a countable number of times. The record of such a construction is called a *Borel code*. Given a Borel set B in V , one recovers a Borel code, and then applies the same construction sequence in $M[G]$ , getting a Borel set $B^{*}$ . It can be proven that one gets the same set independent of the code chosen for B , and that basic properties are preserved. For example, if $B\subseteq C$ , then $B^{*}\subseteq C^{*}$ . If B has measure zero, then $B^{*}$ has measure zero. This mapping $B\mapsto B^{*}$ is injective.

For any set $B\subseteq [0,1]$ such that $B\in M$ and $M\models$ " B is a Borel set of measure 1" one has $r_{G}\in B^{*}$ .

This means that $r_{G}$ is an "infinite random sequence of 0s and 1s" from the viewpoint of M , which means that it satisfies all statistical tests from the ground model M .

So given $r_{G}$ , a random real, one can show that

$G=\left\{B~({\text{in }}M)\mid r\in B^{*}~({\text{in }}M[G])\right\}.$

Because of this mutual inter-definability between r and G , one generally writes $M[r]$ for $M[G]$ .

A different interpretation of reals in $M[G]$ was provided by Dana Scott. Rational numbers in $M[G]$ have names that correspond to countably-many distinct rational values assigned to a maximal antichain of Borel sets – in other words, a certain rational-valued function on $I=[0,1]$ . Real numbers in $M[G]$ then correspond to Dedekind cuts of such functions, that is, measurable functions.

## Boolean-valued models

Perhaps more clearly, the method can be explained in terms of Boolean-valued models. In these, any statement is assigned a truth value from some complete atomless Boolean algebra, rather than just a true/false value. Then an ultrafilter is picked in this Boolean algebra, which assigns values true/false to statements of our theory. The point is that the resulting theory has a model that contains this ultrafilter, which can be understood as a new model obtained by extending the old one with this ultrafilter. By picking a Boolean-valued model in an appropriate way, we can get a model that has the desired property. In it, only statements that must be true (are "forced" to be true) will be true, in a sense (since it has this extension/minimality property).

## Meta-mathematical explanation

In forcing, we usually seek to show that some sentence is consistent with ${\mathsf {ZFC}}$ (or optionally some extension of ${\mathsf {ZFC}}$ ). One way to interpret the argument is to assume that ${\mathsf {ZFC}}$ is consistent and then prove that ${\mathsf {ZFC}}$ combined with the new sentence is also consistent.

Each "condition" is a finite piece of information—the idea is that only finite pieces are relevant for consistency, since, by the compactness theorem, a theory is satisfiable if and only if every finite subset of its axioms is satisfiable. Then we can pick an infinite set of consistent conditions to extend our model. Therefore, assuming the consistency of ${\mathsf {ZFC}}$ , we prove the consistency of ${\mathsf {ZFC}}$ extended by this infinite set.

## Logical explanation

By Gödel's second incompleteness theorem, one cannot prove the consistency of any sufficiently strong formal theory, such as ${\mathsf {ZFC}}$ , using only the axioms of the theory itself, unless the theory is inconsistent. Consequently, mathematicians do not attempt to prove the consistency of ${\mathsf {ZFC}}$ using only the axioms of ${\mathsf {ZFC}}$ , or to prove that ${\mathsf {ZFC}}+H$ is consistent for any hypothesis H using only ${\mathsf {ZFC}}+H$ . For this reason, the aim of a consistency proof is to prove the consistency of ${\mathsf {ZFC}}+H$ relative to the consistency of ${\mathsf {ZFC}}$ . Such problems are known as problems of **relative consistency**, one of which proves

| ${\mathsf {ZFC}}\vdash \operatorname {Con} ({\mathsf {ZFC}})\rightarrow \operatorname {Con} ({\mathsf {ZFC}}+H).$ |   | ⁎ |
|---|---|---|

The general schema of relative consistency proofs follows. As any proof is finite, it uses only a finite number of axioms:

${\mathsf {ZFC}}+\lnot \operatorname {Con} ({\mathsf {ZFC}}+H)\vdash \exists T(\operatorname {Fin} (T)\land T\subseteq {\mathsf {ZFC}}\land (T\vdash \lnot H)).$

For any given proof, ${\mathsf {ZFC}}$ can verify the validity of this proof. This is provable by induction on the length of the proof.

${\mathsf {ZFC}}\vdash \forall T((T\vdash \lnot H)\rightarrow ({\mathsf {ZFC}}\vdash (T\vdash \lnot H))).$

Then resolve

${\mathsf {ZFC}}+\lnot \operatorname {Con} ({\mathsf {ZFC}}+H)\vdash \exists T(\operatorname {Fin} (T)\land T\subseteq {\mathsf {ZFC}}\land ({\mathsf {ZFC}}\vdash (T\vdash \lnot H))).$

By proving the following

| ${\mathsf {ZFC}}\vdash \forall T(\operatorname {Fin} (T)\land T\subseteq {\mathsf {ZFC}}\rightarrow ({\mathsf {ZFC}}\vdash \operatorname {Con} (T+H))),$ |   | ⁎⁎ |
|---|---|---|

it can be concluded that

${\mathsf {ZFC}}+\lnot \operatorname {Con} ({\mathsf {ZFC}}+H)\vdash \exists T(\operatorname {Fin} (T)\land T\subseteq {\mathsf {ZFC}}\land ({\mathsf {ZFC}}\vdash (T\vdash \lnot H))\land ({\mathsf {ZFC}}\vdash \operatorname {Con} (T+H))),$

which is equivalent to

${\mathsf {ZFC}}+\lnot \operatorname {Con} ({\mathsf {ZFC}}+H)\vdash \lnot \operatorname {Con} ({\mathsf {ZFC}}),$

which gives (*). The core of the relative consistency proof is proving (**). A ${\mathsf {ZFC}}$ proof of $\operatorname {Con} (T+H)$ can be constructed for any given finite subset T of the ${\mathsf {ZFC}}$ axioms (by ${\mathsf {ZFC}}$ instruments of course). (No universal proof of $\operatorname {Con} (T+H)$ of course.)

In ${\mathsf {ZFC}}$ , it is provable that for any condition p , the set of formulas (evaluated by names) forced by p is deductively closed. Furthermore, for any ${\mathsf {ZFC}}$ axiom, ${\mathsf {ZFC}}$ proves that this axiom is forced by $\mathbf {1}$ . Then it suffices to prove that there is at least one condition that forces H .

In the case of Boolean-valued forcing, the procedure is similar: proving that the Boolean value of H is not $\mathbf {0}$ .

Another approach uses the reflection principle. For any given finite set of ${\mathsf {ZFC}}$ axioms, there is a ${\mathsf {ZFC}}$ proof that this set of axioms has a countable transitive model. For any given finite set T of ${\mathsf {ZFC}}$ axioms, there is a finite set $T'$ of ${\mathsf {ZFC}}$ axioms such that ${\mathsf {ZFC}}$ proves that if a countable transitive model M satisfies $T'$ , then $M[G]$ satisfies T . Suppose it can also be shown that there is finite set $T''$ of ${\mathsf {ZFC}}$ axioms such that if a countable transitive model M satisfies $T''$ , then $M[G]$ satisfies the hypothesis H . Then for any given finite set T of ${\mathsf {ZFC}}$ axioms, ${\mathsf {ZFC}}$ proves $\operatorname {Con} (T+H)$ .

Sometimes in (**), a stronger theory S than ${\mathsf {ZFC}}$ is used for proving $\operatorname {Con} (T+H)$ . Then we have proof of the consistency of ${\mathsf {ZFC}}+H$ relative to the consistency of S . Note that ${\mathsf {ZFC}}\vdash \operatorname {Con} ({\mathsf {ZFC}})\leftrightarrow \operatorname {Con} ({\mathsf {ZFL}})$ , where ${\mathsf {ZFL}}$ is ${\mathsf {ZF}}+(V=L)$ (the axiom of constructibility).
