---
title: "Coinduction"
source: https://en.wikipedia.org/wiki/Coinduction
domain: coinduction
license: CC-BY-SA-4.0
tags: coinduction principle, corecursion scheme, coinductive definition, infinite data structure
fetched: 2026-07-02
---

# Coinduction

In computer science, **coinduction** is a technique for defining and proving properties of systems of concurrent interacting objects.

Coinduction is the mathematical dual to structural induction. Coinductively defined data types are known as **codata** and are typically infinite data structures, such as streams.

As a definition or specification, coinduction describes how an object may be "observed", "broken down" or "destructed" into simpler objects. As a proof technique, it may be used to show that an equation is satisfied by all possible implementations of such a specification.

To generate and manipulate codata, one typically uses corecursive functions, in conjunction with lazy evaluation. Informally, rather than defining a function by pattern-matching on each of the inductive constructors, one defines each of the "destructors" or "observers" over the function result.

In programming, co-logic programming (co-LP for brevity) "is a natural generalization of logic programming and coinductive logic programming, which in turn generalizes other extensions of logic programming, such as infinite trees, lazy predicates, and concurrent communicating predicates. Co-LP has applications to rational trees, verifying infinitary properties, lazy evaluation, concurrent logic programming, model checking, bisimilarity proofs, etc." Experimental implementations of co-LP are available from the University of Texas at Dallas and in the language Logtalk (for examples see ) and SWI-Prolog.

## Description

In his book *Types and Programming Languages*, Benjamin C. Pierce gives a concise statement of both the *principle of induction* and the *principle of coinduction*. While this article is not primarily concerned with *induction*, it is useful to consider their somewhat generalized forms at once. In order to state the principles, a few preliminaries are required.

### Preliminaries

Let U be a set and F be a monotone function $2^{U}\rightarrow 2^{U}$ , that is:

$X\subseteq Y\Rightarrow F(X)\subseteq F(Y)$

Unless otherwise stated, F will be assumed to be monotone.

- *X* is *F-closed* if $F(X)\subseteq X$
- *X* is *F-consistent* if $X\subseteq F(X)$
- *X* is a fixed point if $X=F(X)$

These terms can be intuitively understood in the following way. Suppose that X is a set of assertions, and $F(X)$ is the operation that yields the consequences of X . Then X is *F-closed* when one cannot conclude any more than has already been asserted, while X is *F-consistent* when all of the assertions are supported by other assertions (i.e. there are no "non-*F*-logical assumptions").

The Knaster–Tarski theorem tells us that the *least fixed-point* of F (denoted $\mu F$ ) is given by the intersection of all *F-closed* sets, while the *greatest fixed-point* (denoted $\nu F$ ) is given by the union of all *F-consistent* sets. We can now state the principles of induction and coinduction.

### Definition

- *Principle of induction*: If X is *F-closed*, then $\mu F\subseteq X$
- *Principle of coinduction*: If X is *F-consistent*, then $X\subseteq \nu F$

## Discussion

The principles, as stated, are somewhat opaque, but can be usefully thought of in the following way. Suppose you wish to prove a property of $\mu F$ . By the *principle of induction*, it suffices to exhibit an *F-closed* set X for which the property holds. Dually, suppose you wish to show that $x\in \nu F$ . Then it suffices to exhibit an *F-consistent* set that x is known to be a member of.

## Examples

### Defining a set of data types

Consider the following grammar of datatypes:

$T=\bot \;|\;\top \;|\;T\times T$

That is, the set of types includes the "bottom type" $\bot$ , the "top type" $\top$ , and product types. These types can be identified with strings over the alphabet $\Sigma =\{\bot ,\top ,\times \}$ . Let $\Sigma ^{\leq \omega }$ denote all (possibly infinite) strings over $\Sigma$ . Consider the function $F:2^{\Sigma ^{\leq \omega }}\rightarrow 2^{\Sigma ^{\leq \omega }}$ :

$F(X)=\{\bot ,\top \}\cup \{x\times y:x,y\in X\}$

In this context, $x\times y$ means "the concatenation of string x , the symbol $\times$ , and string y ." We should now define our set of datatypes as a fixpoint of F , but it matters whether we take the *least* or *greatest* fixpoint.

Suppose we take $\mu F$ as our set of datatypes. Using the *principle of induction*, we can prove the following claim:

All datatypes in

$\mu F$

are

finite

To arrive at this conclusion, consider the set of all finite strings over $\Sigma$ . Clearly F cannot produce an infinite string, so it turns out this set is *F-closed* and the conclusion follows.

Now suppose that we take $\nu F$ as our set of datatypes. We would like to use the *principle of coinduction* to prove the following claim:

The type

$\bot \times \bot \times \cdots \in \nu F$

Here $\bot \times \bot \times \cdots$ denotes the infinite string $(\bot ,\times ,\bot ,\times ,\ldots )$ . To use the *principle of coinduction*, consider the set:

$S=\{\bot ,\;\bot \times \bot \times \cdots \}$

This set is *F-consistent*. First, $\bot \in \{\bot ,\top \}\subseteq F(S)$ . Second, since $\bot \in S$ and $\bot \times \bot \times \cdots \in S$ , we have $\bot \times (\bot \times \bot \times \cdots )\in F(S)$ . Interpreting strings as sequences (functions from $\mathbb {N} \rightarrow \Sigma$ ), prepending the finite prefix $\bot \times$ to the infinite string $\bot \times \bot \times \cdots$ yields $\bot \times \bot \times \cdots$ itself, so $\bot \times \bot \times \cdots \in F(S)$ . Therefore $S\subseteq F(S)$ , and by the *principle of coinduction*, $\bot \times \bot \times \cdots \in \nu F$ .

**Note.** The representation of types as strings over $\Sigma$ is not faithful to the underlying tree structure. Finite strings such as $\bot \times \top \times \bot$ are ambiguous without bracketing, and for any infinite string s the concatenation $s\times t=s$ for all t , so distinct trees may be identified. This does not affect the argument above, which only illustrates the *principle of coinduction* via *F*-consistency, but it would matter in settings where constructor structure must be preserved. A standard structural treatment represents types via the isomorphism $T\cong 1+1+(T\times T)$ ; see F-coalgebra for details.

### Coinductive datatypes in programming languages

Consider the following definition of a stream in Haskell:

```mw
data Stream a = S a (Stream a)

-- Stream "destructors"
head :: Stream a -> a
head (S a astream) = a
tail :: Stream a -> Stream a
tail (S a astream) = astream
```

The first line says that a stream is made up of an element followed by a stream (S is a constructor of elements, and a denotes for an arbitrary type for the elements). As there is no base case, this would seem to be a definition that is not well-founded, but it is nonetheless useful in programming and can be reasoned about. In any case, a stream is an infinite list of elements from which you may observe the first element, or place an element in front of to get another stream.

### Relationship with *F*-coalgebras

Consider the endofunctor F in the category of sets:

${\begin{aligned}F(x)&=A\times x\\F(f)&=\langle \mathrm {id} _{A},f\rangle \end{aligned}}$

The *final F-coalgebra* $\nu F$ has the following morphism associated with it:

$\mathrm {out$

This induces another coalgebra $F(\nu F)$ with associated morphism $F(\mathrm {out} )$ . Because $\nu F$ is *final*, there is a unique morphism

${\overline {F(\mathrm {out} )}}:F(\nu F)\rightarrow \nu F$

such that

$\mathrm {out} \circ {\overline {F(\mathrm {out} )}}=F\left({\overline {F(\mathrm {out} )}}\right)\circ F(\mathrm {out} )=F\left({\overline {F(\mathrm {out} )}}\circ \mathrm {out} \right)$

The composition ${\overline {F(\mathrm {out} )}}\circ \mathrm {out}$ induces another *F*-coalgebra homomorphism $\nu F\rightarrow \nu F$ . Since $\nu F$ is final, this homomorphism is unique and therefore $\mathrm {id} _{\nu F}$ . Altogether we have:

${\begin{aligned}{\overline {F(\mathrm {out} )}}\circ \mathrm {out} &=\mathrm {id} _{\nu F}\\[0.5ex]\mathrm {out} \circ {\overline {F(\mathrm {out} )}}=F{\bigl (}{\overline {F(\mathrm {out} )}}\circ \mathrm {out} {\bigr )}&=\mathrm {id} _{F(\nu F)}\end{aligned}}$

This witnesses the isomorphism $\nu F\simeq F(\nu F)$ , which in categorical terms indicates that $\nu F$ is a fixed point of F and justifies the notation.

#### Stream as a final coalgebra

We will show that `Stream A` is the final coalgebra of the functor $F(x)=A\times x$ . Consider the following implementations:

```mw
out astream = (head astream, tail astream)
out' (a, astream) = S a astream
```

These are easily seen to be mutually inverse, witnessing the isomorphism. See the reference for more details.

### Relationship with mathematical induction

We will demonstrate how the *principle of induction* subsumes mathematical induction. Let P be some property of natural numbers. We will take the following definition of mathematical induction:

$0\in P\land (n\in P\Rightarrow n+1\in P)\Rightarrow \mathbb {N} \subseteq P$

Now consider the function $F:2^{\mathbb {N} }\rightarrow 2^{\mathbb {N} }$ :

$F(X)=\{0\}\cup \{x+1:x\in X\}$

It should not be difficult to see that $\mu F=\mathbb {N}$ . Therefore, by the *principle of induction*, if we wish to prove some property P of $\mathbb {N}$ , it suffices to show that P is *F-closed*. In detail, we require:

$F(P)\subseteq P$

That is,

$\{0\}\cup \{x+1:x\in P\}\subseteq P$

This is precisely *mathematical induction* as stated.
