---
title: "Bourbaki–Witt theorem"
source: https://en.wikipedia.org/wiki/Bourbaki%E2%80%93Witt_theorem
domain: denotational-domains
license: CC-BY-SA-4.0
tags: domain theory, directed-complete partial order, continuous function, algebraic lattice
fetched: 2026-07-02
---

# Bourbaki–Witt theorem

In mathematics, the **Bourbaki–Witt theorem** in order theory, named after Nicolas Bourbaki and Ernst Witt, is a basic fixed-point theorem for partially ordered sets. It states that

if

X

is a non-empty

poset

that is

chain complete

,

meaning each chain has a

least upper bound

, and

$f:X\to X$

is a function such that

$f(x)\geq x$

for all

$x,$

then

f

has a

fixed point

.

Such a function *f* is called *inflationary* or *progressive*.

## Special case of a finite poset

If the poset *X* is finite then the statement of the theorem has a clear interpretation that leads to the proof. The sequence of successive iterates,

$x_{n+1}=f(x_{n}),n=0,1,2,\ldots ,$

where *x*0 is any element of *X*, is monotone increasing. By the finiteness of *X*, it stabilizes:

$x_{n}=x_{\infty },$

for

n

sufficiently large.

It follows that *x*∞ is a fixed point of *f*.

## Maximal elements

A maximal element, *if any*, is trivially a fixed point of the inflationary map f . In particular, if Zorn's lemma is available (which is equivalent to assuming the axiom of choice), then the theorem holds trivially. However, the theorem is typically used in a proof that the axiom of choice implies Zorn's lemma as follows.

We first prove it for the case where *X* is chain complete and has no maximal element. Let *g* be a choice function on $P(X)-\{\varnothing \}.$ Define a function $f:X\to X$ by

${\displaystyle f(x)=g(\{y\$

This is allowed as, by assumption, the set is non-empty. Then *f*(*x*) > *x*, so *f* is an inflationary function with no fixed point, contradicting the theorem.

This special case of Zorn's lemma is then applied to the set $P'$ of all chains in a given poset P , ordered by set inclusion. We get a maximal element in $P'$ ; i.e., a maximal chain in P . This proves the Hausdorff maximality principle, that every poset has a maximal chain, which is easily seen to be equivalent to Zorn's lemma (see also Zorn's lemma § Proof from the Hausdorff maximal principle).

## Proofs

### Proof 1

In the following, to say that an ordinal α is *embeddable in* a set *X* is to say that there exists an injection $f:U(\alpha )\hookrightarrow X$ from the underlying set of α to *X*. Such an injection amounts to a well-ordering of the image of *f* as a subset of *X*, thereby witnessing that that subset can be well-ordered.

Let β be the Hartogs number for the set *U(X)* of the given poset *X*. By definition this is the set of all ordinals embeddable in *U(X)*, itself an ordinal not embeddable in *U(X)* or we would have β ϵ β. (Equivalently, β is the least ordinal not embeddable in *U(X)*, necessarily a cardinal.) Let $x_{0}$ witness the non-emptiness of *X*, to serve as the basis for the following recursive construction of a chain in *X*.

For each ordinal $\alpha \in \beta$ such that $x_{\alpha }$ is defined, define $x_{\alpha +1}=f(x_{\alpha }).$ Since *f* is inflationary, $x_{\alpha }\leq x_{\alpha +1}$ in the poset *X*.

For each limit ordinal $\lambda \in \beta$ such that $x_{\alpha }$ is defined for all $\alpha <\lambda$ , define $x_{\lambda }=\sup\{x_{\alpha }|\alpha <\lambda \}.$ Then $x_{\alpha }\leq x_{\lambda }$ for all $\alpha <\lambda$ . The $\sup$ exists by chain-completeness of the poset *X*.

Now if *f* is strictly increasing on all of β, this would constitute an embedding of β, the order type of that chain, in *X*. But that's impossible by Hartogs' Lemma.

Hence there must exist $\alpha <\beta$ such that $x_{\alpha +1}=x_{\alpha }$ , bringing the construction of the chain to a halt at $x_{\alpha }$ , the promised fixed point. Q.E.D.

#### Independence of Choice

The foregoing argument avoids anything that depends on the Axiom of Choice.

Now it is tempting to argue that the Hartogs number for the set *X* must be the least cardinal greater than the cardinality of *X*. After all, surely the above recursive construction must eventually exhaust all the elements of *X* long before exhausting all the ordinals.

However a set that can only embed finite ordinals is called Dedekind-finite and ZF can have models in which infinite Dedekind-finite sets exist. The Hartogs number for such sets is therefore ω, and posets on them cannot contain any infinite chains.

To be sure we have not somehow smuggled in anything not provable in ZF without choice, we should stick to what is provable in ZF alone. Otherwise applications of the Bourbaki–Witt theorem to proofs relating equivalences between variants of the Axiom of Choice, such as done below, may introduce circularities into the reasoning.

### Proof 2

The theorem can also be proved by *adapting* a typical proof showing that the axiom of choice implies Zorn’s lemma. Indeed, let $\operatorname {Well} (X)$ denote the set of all well-ordered subsets of X . Then consider

$g:\operatorname {Well} (X)\to X$

given by $g(S)=f(\sup S).$ If f has no fixed point, then $g(S)$ is a strict upper bound of S . From this, one concludes a contradiction as in a standard proof of Zorn’s lemma. For the sake of completeness, here is a sketch of the proof following T. Tao.

Let $\operatorname {Well}$ be the class of all well-ordered sets. Then for each A in $\operatorname {Well}$ , using an iteration of g , we construct a sequence $x_{a}$ of distinct elements in X indexed by A . For example, if $A=\mathbb {N} _{1}$ , then recursively we let $x_{1}=g(\emptyset )$ and $x_{n}=g(x_{n-1})$ . For arbitrary A , we use transfinite recursion or transfinite induction to construct the sequences in a similar way. Now, this construction determines the map (class function to be precise)

${\displaystyle \rho$

by

$\rho (A)=\{x_{a}\mid a\in A\}$

.

It is not hard to see non-isomorphic A 's produce different sequences; i.e., $\rho$ is injective modulo isomorphisms. But $\operatorname {Well}$ contains all the ordinals in particular and it is known (the Burali-Forti paradox) that the class of all the ordinals is a proper class; i.e., not a set, contradicting that $\operatorname {Well} (X)$ is a set. $\square$

Note the above argument does not rely on the axiom of choice. (In the case of a proof of Zorn's lemma, Choice is used to define an inflationary map.) Also, we needed $\sup S$ only for well-ordered subsets S of P . The argument therefore establishes the following.

**Theorem**—Let X be a nonempty poset in which each well-ordered subset has a least upper bound. Then each inflationary map $f:X\to X$ admits a fixed point.

### Proof 3

Just as Zorn's lemma can be proved without transfinite induction or the theory of well-ordering and ordinals, it is possible to give a proof of the theorem that only uses a basic set theory. The idea here is first to prove a general lemma below, used implicitly in a traditional proof of Hausdorff's maximal principle and also noted independently by Kneser as well as Guillermo L. Incatasciato and Pedro Sánchez Terraf.

**Lemma** (Chain bounding)—Let P be a poset and F the set of all chains in P . Then there *does not* exist a function $g:F\to P$ such that, for each $C\in F$ , $g(C)$ is a strict upper bound of C .

The Bourbaki–Witt theorem follows since the function $g(C)=f(\sup C)$ has the property stated in the lemma if f has no fixed point.

*Proof of Lemma*: For a textbook proof, see Hausdorff's maximal principle#Proof 1. Here, we follow Incatasciato and Terraf (in the well-ordered case, their proof is the same as Kneser's proof; see the remark below). Assuming such g exists, let $C^{+}=C\cup \{g(C)\}$ for each C in F . We write $S\trianglelefteq C$ if S is an initial segment of C , meaning S is a subset and $y\leq x\in S,\,y\in C\Rightarrow y\in S$ . Also, write $S\triangleleft C$ if $S\trianglelefteq C,\,S\neq C$ .

Following the authors, we say a chain $C\subset P$ is *good* if for each $S\trianglelefteq C$ , we have either $S=C$ or $S^{+}\trianglelefteq C$ . Let $\Gamma$ be the set of all good chains in P . We claim

1. $\Gamma$ is totally ordered with respect to $\trianglelefteq$ ; i.e., good chains are comparable.
2. On $\Gamma$ , $\trianglelefteq$ is the same as set inclusion.
3. If C is a good chain in P , then $C^{+}$ is a good chain in P .

For (1), given two good chains $C,D$ , let S be the union of all chains that are both the initial segments of C and $D.$ Clearly, S itself is an initial segment of the two; i.e., it is the largest common initial segment. If $S^{+}\trianglelefteq C,D$ , then that would contradict the largest-ness of S . Thus, either $S=C$ or D . For (2), suppose $C\subsetneq D$ . By (1), either $C\triangleleft D$ or $D\triangleleft C$ , but the latter is not possible. Finally, (3) is straightforward.

We can now finish. Let U be the union of $\Gamma$ . By (1), U is a chain. To show it is good, suppose $S\triangleleft U$ . Let x be in $U-S$ . Pick a good chain C containing x . Then we have

$S\triangleleft C$

.

Indeed, if y is in S , then y is in a good chain D . If $D\trianglelefteq C$ , then y is in C . Otherwise, by (1), $C\trianglelefteq D$ . We have $y\leq x$ by $S\triangleleft U$ and so again y is in C . Hence, $S\subset C$ and that implies $S\triangleleft C$ as S is already an initial segment of U . Finally, $S^{+}\trianglelefteq C$ and, by (2), $S^{+}\trianglelefteq U$ . This finishes the proof of the fact that U is good. Since $U^{+}=U$ then, this is a contradiction. $\square$

**Remark**: In the above, we could have used well-ordered subsets instead of chains. That is, let U be the union of all good well-ordered subsets of P . All the assertions hold with well-ordered subsets in place of chains. Note U is well-ordered not just totally ordered by (2). Thus, the above argument also shows the well-ordered version of the theorem stated at § Proof 2. Moreover, for a well-ordered set C , since an initial segment is of the form $S_{x}=\{y\mid y<x\}$ , explicitly, C is good if and only if, for each x in C , we have:

$x=g(S_{x})$

.

Hence, a good well-ordered set is exactly the same as what Kneser calls *Kette* (and so the above proof reduces to Kneser's proof).

## Applications

Besides a proof of Zorn's lemma, Bourbaki–Witt has some other applications. In particular in computer science, it is used in the theory of computable functions. It is also used to define recursive data types, e.g. linked lists, in domain theory.
