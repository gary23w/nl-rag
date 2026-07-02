---
title: "Abstract rewriting system"
source: https://en.wikipedia.org/wiki/Reduction_(abstract_rewriting)
domain: small-step-semantics
license: CC-BY-SA-4.0
tags: small-step semantics, structural operational semantics, reduction relation, evaluation context
fetched: 2026-07-02
---

# Abstract rewriting system

(Redirected from

Reduction (abstract rewriting)

)

In mathematical logic and theoretical computer science, an **abstract rewriting system** (also (**abstract**) **reduction system** or **abstract rewrite system**; abbreviated **ARS**) is a formalism that captures the quintessential notion and properties of rewriting systems. In its simplest form, an ARS is simply a set (of "objects") together with a binary relation, traditionally denoted with $\rightarrow$ ; this definition can be further refined if we index (label) subsets of the binary relation. Despite its simplicity, an ARS is sufficient to describe important properties of rewriting systems like normal forms, termination, and various notions of confluence.

Historically, there have been several formalizations of rewriting in an abstract setting, each with its idiosyncrasies. This is due in part to the fact that some notions are equivalent, see below in this article. The formalization that is most commonly encountered in monographs and textbooks, and which is generally followed here, is due to Gérard Huet (1980).

## Definition

An *abstract reduction system* (*ARS*) is the most general (unidimensional) notion about specifying a set of objects and rules that can be applied to transform them. More recently, authors use the term *abstract rewriting system* as well. (The preference for the word "reduction" here instead of "rewriting" constitutes a departure from the uniform use of "rewriting" in the names of systems that are particularizations of ARS. Because the word "reduction" does not appear in the names of more specialized systems, in older texts *reduction system* is a synonym for ARS.)

An ARS is a set *A*, whose elements are usually called objects, together with a binary relation on *A*, traditionally denoted by →, and called the **reduction relation**, *rewrite relation* or just **reduction**. This (entrenched) terminology using "reduction" is a little misleading, because the relation is not necessarily reducing some measure of the objects.

In some contexts it may be beneficial to distinguish between some subsets of the rules, i.e. some subsets of the reduction relation →, e.g. the entire reduction relation may consist of associativity and commutativity rules. Consequently, some authors define the reduction relation → as the indexed union of some relations; for instance if ${\rightarrow _{1}\cup \rightarrow _{2}}={\rightarrow }$ , the notation used is (A, →1, →2).

As a mathematical object, an ARS is exactly the same as an unlabeled state transition system, and if the relation is considered as an indexed union, then an ARS is the same as a labeled state transition system with the indices being the labels. The focus of the study, and the terminology are different however. In a state transition system one is interested in interpreting the labels as actions, whereas in an ARS the focus is on how objects may be transformed (rewritten) into others.

## Example 1

Suppose the set of objects is *T* = {*a*, *b*, *c*} and the binary relation is given by the rules *a* → *b*, *b* → *a*, *a* → *c*, and *b* → *c*. Observe that these rules can be applied to both *a* and *b* to get *c*. Furthermore, nothing can be applied to *c* to transform it any further. Such a property is clearly an important one.

## Basic notions

First define some basic notions and notations.

- ${\stackrel {+}{\rightarrow }}$ is the transitive closure of $\rightarrow$ .
- ${\stackrel {*}{\rightarrow }}$ is the reflexive transitive closure of $\rightarrow$ , i.e. the transitive closure of $(\rightarrow )\cup (=)$ , where = is the identity relation. Equivalently, ${\stackrel {*}{\rightarrow }}$ is the smallest preorder containing $\rightarrow$ .
- Similarly, ${\stackrel {+}{\leftarrow }}$ , and ${\stackrel {*}{\leftarrow }}$ are closures of ${\leftarrow }$ , the converse relation of ${\rightarrow }$ .
- $\leftrightarrow$ is the symmetric closure of $\rightarrow$ , that is, the union of $\rightarrow$ with ${\leftarrow }$ .
- ${\stackrel {*}{\leftrightarrow }}$ is the reflexive transitive symmetric closure of $\rightarrow$ , i.e. the transitive closure of $(\leftrightarrow )\cup (=)$ . Equivalently, ${\stackrel {*}{\leftrightarrow }}$ is the smallest equivalence relation containing $\rightarrow$ .

## Normal forms

An object *x* in *A* is called *reducible* if there exist some other *y* in *A* and $x\rightarrow y$ ; otherwise it is called *irreducible* or a *normal form*. An object *y* is called a normal form of *x* if $x{\stackrel {*}{\rightarrow }}y$ and *y* is irreducible. If *x* has a *unique* normal form, then this is usually denoted with $x\downarrow$ . In example 1 above, *c* is a normal form, and $c=a\downarrow =b\downarrow$ . If every object has at least one normal form, the ARS is called *normalizing*.

## Joinability

A related, but weaker notion than the existence of normal forms is that of two objects being *joinable*: *x* and *y* are said to be joinable if there exists some *z* with the property that $x{\stackrel {*}{\rightarrow }}z{\stackrel {*}{\leftarrow }}y$ . From this definition, it's apparent one may define the joinability relation as ${\stackrel {*}{\rightarrow }}\circ {\stackrel {*}{\leftarrow }}$ , where $\circ$ is the composition of relations. Joinability is usually denoted, somewhat confusingly, also with $\downarrow$ , but in this notation the down arrow is a binary relation, i.e. we write $x\mathrel {\downarrow } y$ if *x* and *y* are joinable.

## The Church–Rosser property and notions of confluence

An ARS is said to possess the *Church–Rosser property* if and only if $x{\stackrel {*}{\leftrightarrow }}y$ implies $x\mathrel {\downarrow } y$ for all objects *x*, *y*. Equivalently, the Church–Rosser property means that the reflexive transitive symmetric closure is contained in the joinability relation. Alonzo Church and J. Barkley Rosser proved in 1936 that lambda calculus has this property; hence the name of the property. In an ARS with the Church–Rosser property the word problem may be reduced to the search for a common successor. In a Church–Rosser system, an object has *at most one* normal form; that is, the normal form of an object is unique if it exists, but it may well not exist.

Various properties, simpler than Church–Rosser, are equivalent to it. The existence of these equivalent properties allows one to prove that a system is Church–Rosser with less work. Furthermore, the notions of confluence can be defined as properties of a particular object, something that's not possible for Church–Rosser. An ARS $(A,\rightarrow )$ is said to be,

- *confluent* if and only if for all *w*, *x*, and *y* in *A*, $x{\stackrel {*}{\leftarrow }}w{\stackrel {*}{\rightarrow }}y$ implies $x\mathrel {\downarrow } y$ . Roughly speaking, confluence says that no matter how two paths diverge from a common ancestor (*w*), the paths are joining at *some* common successor. This notion may be refined as property of a particular object *w*, and the system called confluent if all its elements are confluent.
- *semi-confluent* if and only if for all *w*, *x*, and *y* in *A*, $x\leftarrow w{\stackrel {*}{\rightarrow }}y$ implies $x\mathrel {\downarrow } y$ . This differs from confluence by the single step reduction from *w* to *x*.
- *locally confluent* if and only if for all *w*, *x*, and *y* in *A*, $x\leftarrow w\rightarrow y$ implies $x\mathrel {\downarrow } y$ . This property is sometimes called *weak confluence*.

**Theorem.** For an ARS the following three conditions are equivalent: (i) it has the Church–Rosser property, (ii) it is confluent, (iii) it is semi-confluent.

**Corollary**. In a confluent ARS if $x{\stackrel {*}{\leftrightarrow }}y$ then

- If both *x* and *y* are normal forms, then *x* = *y*.
- If *y* is a normal form, then $x{\stackrel {*}{\rightarrow }}y$ .

Because of these equivalences, a fair bit of variation in definitions is encountered in the literature. For instance, in Terese the Church–Rosser property and confluence are defined to be synonymous and identical to the definition of confluence presented here; Church–Rosser as defined here remains unnamed, but is given as an equivalent property; this departure from other texts is deliberate. Because of the above corollary, one may define a normal form *y* of *x* as an irreducible *y* with the property that $x{\stackrel {*}{\leftrightarrow }}y$ . This definition, found in Book and Otto, is equivalent to the common one given here in a confluent system, but it is more inclusive in a non-confluent ARS.

Local confluence on the other hand is not equivalent with the other notions of confluence given in this section, but it is strictly weaker than confluence. The typical counterexample is $\{b\rightarrow c,c\rightarrow b,b\rightarrow a,c\rightarrow d\}$ , which is locally confluent but not confluent (cf. picture).

## Termination and convergence

An abstract rewriting system is said to be **terminating** or *noetherian* if there is no infinite chain $x_{0}\rightarrow x_{1}\rightarrow x_{2}\rightarrow \cdots$ . (This is just saying that the rewriting relation is a Noetherian relation.) In a terminating ARS, every object has at least one normal form, thus it is normalizing. The converse is not true. In example 1 for instance, there is an infinite rewriting chain, namely $a\rightarrow b\rightarrow a\rightarrow b\rightarrow \cdots$ , even though the system is normalizing. A confluent and terminating ARS is called **canonical**, or **convergent**. In a convergent ARS, every object has a unique normal form. But it is sufficient for the system to be confluent and normalizing for a unique normal to exist for every element, as seen in example 1.

**Theorem** (Newman's lemma): A terminating ARS is confluent if and only if it is locally confluent.

The original 1942 proof of this result by Newman was rather complicated. It wasn't until 1980 that Huet published a much simpler proof exploiting the fact that when $\rightarrow$ is terminating we can apply well-founded induction.
