---
title: "Cardinal number"
source: https://en.wikipedia.org/wiki/Cardinal_number
domain: ordinal-arithmetic
license: CC-BY-SA-4.0
tags: ordinal arithmetic, ordinal number, transfinite induction, cantor normal form
fetched: 2026-07-02
---

# Cardinal number

In mathematics, a **cardinal number**, or **cardinal** for short, is a kind of number that measures the cardinality of a set, i.e., how many elements there are in a set. The cardinal number associated with a set ⁠ A ⁠ is generally denoted by ⁠ $\vert A\vert$ ⁠, with a vertical bar on each side, though it may also be denoted by A , $\operatorname {card} (A),$ or $\#A.$

Cardinality is defined in terms of bijective functions. Two sets have the same cardinality if, and only if, there is a one-to-one correspondence (bijection) between the elements of the two sets. The cardinality of a finite set can be identified with a natural number, which can be found simply by counting its elements. For example, the sets ⁠ $\{1,2,3\}$ ⁠ and ⁠ $\{4,5,6\}$ ⁠ both have the same cardinality 3, as evidenced by the bijection ⁠ $\{1\mapsto 4,2\mapsto 5,3\mapsto 6\}$ ⁠.

The behavior of cardinalities of infinite sets is more complex. For example, there exists a bijection between the set of all natural numbers ⁠ $\mathbb {N}$ ⁠ and the set of all rational numbers ⁠ $\mathbb {Q}$ ⁠, and thus ⁠ $\vert \mathbb {N} \vert =\vert \mathbb {Q} \vert$ ⁠ even though ⁠ $\mathbb {N}$ ⁠ is a proper subset of ⁠ $\mathbb {Q}$ ⁠—something that cannot happen with proper subsets of finite sets. However, a fundamental theorem due to Georg Cantor shows that it is possible for two infinite sets to have different cardinalities, and in particular the cardinality of the set of real numbers ⁠ $\mathbb {R}$ ⁠ is greater than the cardinality of ⁠ $\mathbb {N}$ ⁠.

The cardinality of ⁠ $\mathbb {N}$ ⁠ is usually denoted by ⁠ $\aleph _{0}$ ⁠ (aleph-null), since it is the smallest aleph number. The properties of other aleph numbers and of infinite cardinal numbers in general depend on statements independent of Zermelo–Fraenkel set theory, such as the axiom of choice and the continuum hypothesis. For example, all infinite cardinal numbers are aleph numbers if and only if the axiom of choice is true.

Cardinality is studied for its own sake as part of set theory. It is also a tool used in branches of mathematics including model theory, combinatorics, abstract algebra and mathematical analysis. In category theory, the cardinal numbers form a skeleton of the category of sets.

## Motivation

A natural number can be used for two purposes: to describe the size of a set, or to describe the position of an element in a sequence. These two notions diverge when generalized to infinite sets and sequences, with the position aspect leading to ordinal numbers, and the size aspect leading to cardinal numbers.

When considering the size of a set, the identities of individual members should be *abstracted away*; changing these individual members should not affect the size of the set, as long as they remain distinct from each other. For example, the set ⁠ $\{1,2,3\}$ ⁠ has three elements, so when one replaces its members following the mapping ⁠ $\{1\mapsto 4,2\mapsto 5,3\mapsto 6\}$ ⁠, the resulting set ⁠ $\{4,5,6\}$ ⁠ still has three elements. It is reasonable to further postulate that two sets ⁠ X ⁠ and ⁠ Y ⁠ have the same size if *and only if* such a mapping—a bijection—exists from ⁠ X ⁠ to ⁠ Y ⁠. This is exactly how the formal concept of cardinality is defined.

Sameness of cardinality is an equivalence relation. It is sometimes referred to as *equipotence*, *equipollence*, or *equinumerosity*. It is thus said that two sets with the same cardinality are, respectively, *equipotent*, *equipollent*, or *equinumerous*. Every equivalence class of sets under equinumerosity corresponds to a cardinal number.

For finite sets, cardinal numbers defined this way agree with the intuitive notion of numbers of elements (as a natural number), but infinite sets exhibit more complex behaviors. A classic example is Hilbert's paradox of the Grand Hotel, which uses the following mapping:

1 ↦ 2

2 ↦ 3

3 ↦ 4

...

n

↦

n

+ 1

...

This is a bijection between the sets ⁠ $\{1,2,3,...\}$ ⁠ and ⁠ $\{2,3,4,...\}$ ⁠, and thus they have the same cardinality ⁠ $\aleph _{0}$ ⁠, despite the second being a proper subset of the first. Therefore the intuition that the size of a proper subset of ⁠ X ⁠ is always strictly less than the size of ⁠ X ⁠ is usually only valid for finite sets. Conversely, this also shows that ⁠ $\aleph _{0}+1=\aleph _{0}$ ⁠ (the cardinality of ⁠ $\{2,3,4,...\}$ ⁠ plus the cardinality of ⁠ $\{1\}$ ⁠ is equal to the cardinality of ⁠ $\{1,2,3,...\}$ ⁠), and thus the "plus one" operation does not always construct a new cardinal number as it does for natural numbers.

However, Cantor's diagonal argument shows that the power set operation always results in a strictly greater cardinality, allowing one to construct a larger cardinal number from any infinite cardinal number. For example, it can be shown that the cardinality of the set of real numbers is equal to ⁠ $2^{\aleph _{0}}$ ⁠, and thus there are strictly more real numbers than natural numbers.

## Cardinality function

The cardinality function is a cardinal function that takes in a set A and returns its cardinal number: ⁠ $A\mapsto \vert A\vert$ ⁠. However, it is somewhat difficult to define "cardinal number" formally, especially for infinite sets. Therefore, cardinal numbers are not usually thought of in terms of their formal definition, but immaterially in terms of their arithmetic/algebraic properties. The only fundamental requirement on a cardinality function $A\mapsto |A|$ is: $A\sim B\iff |A|=|B|.$ The assumption that there is *some* function that satisfies this requirement is sometimes called the *axiom of cardinality* or *Hume's principle*. It will be shown later that such a function can be constructed without the need to define it axiomatically.

An alternative approach is to define an equality relation for cardinal numbers ⁠ $=_{c}$ ⁠ that may be different from the equality relation for sets, and use ⁠ $=_{c}$ ⁠ to develop the theory of cardinality. Specifically, Moschovakis defines a (weak) **cardinal assignment** as an operation ⁠ $A\mapsto \vert A\vert$ ⁠ that satisfies ⁠ $A\sim \vert A\vert$ ⁠ (with the motivation that the cardinality of ⁠ A ⁠ should be represented by an "abstract" object ⁠ $\vert A\vert$ ⁠ that is equinumerous to ⁠ A ⁠). The relation ⁠ $=_{c}$ ⁠ is then the same as the equinumerosity relation ⁠ $\sim$ ⁠ between sets. If a cardinal assignment *also* satisfies ⁠ $A\sim B\iff \vert A\vert =\vert B\vert$ ⁠, then it is a **strong cardinal assignment**.

## Constructive definition

### Von Neumann cardinal assignment

The most commonly used (strong) cardinal assignment, which relies on the axiom of choice, is the **von Neumann cardinal assignment**, which represents the cardinality of a set ⁠ X ⁠ with (the von Neumann representation of) the least ordinal number ⁠ $\alpha$ ⁠ such that there is a bijection between ⁠ X ⁠ and ⁠ $\alpha$ ⁠. This ordinal number ⁠ $\alpha$ ⁠ is also known as the **initial ordinal** of the cardinal number ⁠ $\vert X\vert$ ⁠.

When ⁠ X ⁠ is a finite set, all possible well-orderings of ⁠ X ⁠ has the same order type; conversely, all finite ordinals have different cardinalities, and thus all finite ordinals are initial ordinals. Under their respective von Neumann representations, both finite ordinals and finite cardinals are identified with von Neumann natural numbers, and cardinal and ordinal arithmetic (addition, multiplication, power, proper subtraction) give the same answers for finite numbers.

On the other hand, many different infinite ordinal numbers can have the same cardinality. For example, the first infinite ordinal ⁠ $\omega$ ⁠ has the same cardinality as ⁠ $\omega +1$ ⁠, ⁠ $\omega ^{2}$ ⁠, ⁠ $\omega ^{\omega }$ ⁠, $\epsilon _{0}$ ..., all of which are countable ordinals. Among these, only ⁠ $\omega$ ⁠ itself is an initial ordinal.

The $\alpha$ -th infinite initial ordinal is written $\omega _{\alpha }$ . Its cardinality is written $\aleph _{\alpha }$ (the $\alpha$ -th aleph number). For example, ⁠ $\omega$ ⁠ is also written as ⁠ $\omega _{0}$ ⁠, and its cardinality (the cardinality of any countable set) as ⁠ $\aleph _{0}$ ⁠. The von Neumann cardinal assignment identifies $\omega _{\alpha }$ with $\aleph _{\alpha }$ , but the notation $\aleph _{\alpha }$ is used for writing cardinals, and $\omega _{\alpha }$ for writing ordinals. This is important because arithmetic on cardinals is different from arithmetic on ordinals. For example, $2^{\omega }=\omega <\omega ^{2}$ in ordinal arithmetic while $2^{\aleph _{0}}>\aleph _{0}=\aleph _{0}^{2}$ in cardinal arithmetic, even though under the von Neumann cardinal assignment ⁠ $\aleph _{0}$ ⁠ and ⁠ $\omega$ ⁠ are represented by the same set.

Also, $\omega _{1}$ is the smallest uncountable ordinal (to see that it exists, consider the set of equivalence classes of well-orderings of the natural numbers; each such well-ordering defines a countable ordinal, and $\omega _{1}$ is the order type of that set), $\omega _{2}$ is the smallest ordinal whose cardinality is greater than $\aleph _{1}$ , and so on, and $\omega _{\omega }$ is the limit of $\omega _{n}$ for natural numbers n (any limit of cardinals is a cardinal, so this limit is indeed the first cardinal after all the $\omega _{n}$ ).

Infinite initial ordinals are limit ordinals. Using ordinal arithmetic, $\alpha <\omega _{\beta }$ implies $\alpha +\omega _{\beta }=\omega _{\beta }$ , and 1 ≤ *α* < ω*β* implies *α*·ω*β* = ω*β*, and 2 ≤ *α* < ω*β* implies *α*ω*β* = ω*β*. Using the Veblen hierarchy, *β* ≠ 0 and *α* < ω*β* imply $\varphi _{\alpha }(\omega _{\beta })=\omega _{\beta }\,$ and Γω*β* = ω*β*. Indeed, one can go far beyond this. So as an ordinal, an infinite initial ordinal is an extremely strong kind of limit.

### Scott cardinals

If the axiom of choice is not assumed, then a different approach is needed. The oldest definition of the cardinality of a set *X* (implicit in Cantor and explicit in Frege and *Principia Mathematica*) is as the class [*X*] of all sets that are equinumerous with *X*. This does not work in ZFC or other related systems of axiomatic set theory because if *X* is non-empty, this collection is too large to be a set. In fact, for *X* ≠ ∅ there is an injection from the universe into [*X*] by mapping a set *m* to {*m*} × *X*, and so by the axiom of limitation of size, [*X*] is a proper class. The definition does work however in type theory and in New Foundations and related systems. However, if we restrict from this class to those equinumerous with *X* that have the least rank, then it will work (this is a trick due to Dana Scott: it works because the collection of objects with any given rank is a set).

Some sources use a mixed definition between von Neumann cardinals and Scott cardinals. For example, Lévy defines ⁠ $\vert X\vert$ ⁠ as the von Neumann cardinal when ⁠ X ⁠ is well-orderable, and as the Scott cardinal otherwise. This convention retains the convenience provided by the von Neumann representation for studying *well ordered cardinals*, which is still a significant part of cardinal study even when the axiom of choice is not assumed.

## Cardinal comparison

Formally, the order among cardinal numbers is defined as follows: |*X*| ≤ |*Y*| means that there exists an injective function from *X* to *Y*. The Cantor–Bernstein–Schroeder theorem states that if |*X*| ≤ |*Y*| and |*Y*| ≤ |*X*| then |*X*| = |*Y*|. The axiom of choice is equivalent to the statement that given two sets *X* and *Y*, either |*X*| ≤ |*Y*| or |*Y*| ≤ |*X*|.

A set *X* is called *Dedekind-infinite* if there exists a proper subset *Y* of *X* with |*X*| = |*Y*|, and Dedekind-finite if such a subset does not exist. The finite cardinals are just the natural numbers, in the sense that, by definition, a set *X* is finite if and only if |*X*| = |*n*| = *n* for some natural number *n*. Any other set is infinite. It can be proven (without the axiom of choice) that any Dedekind-infinite set is infinite. Assuming the axiom of choice, it can be proved that the Dedekind notions correspond to the standard ones.

## Aleph numbers

The aleph numbers are the cardinalities of well-orderable infinite sets. They are denoted with the Hebrew letter $\aleph$ (aleph) marked with a subscript indicating their rank among aleph numbers. Since aleph numbers can be identified with their initial ordinals, they form a transfinite sequence: $\aleph _{0}=|\mathbb {N} |,\;\aleph _{1},\;\aleph _{2},\;\ldots ,\;\aleph _{\alpha },\;\ldots .$ For every ordinal ⁠ $\alpha$ ⁠, there exists an aleph number ⁠ $\aleph _{\alpha }$ ⁠. If the axiom of choice is true, then *all* sets are well-orderable (by the well-ordering theorem), and thus all infinite cardinal numbers are aleph numbers, i.e., this transfinite sequence is in fact the list of all infinite cardinal numbers.

If the axiom of choice is not true (see Axiom of choice § Independence), then there exist sets that are not well-orderable, and thus infinite cardinals that are not aleph numbers. Such a cardinal must be incomparable to some aleph number by Hartogs's theorem, so in this case it is impossible to write all cardinal numbers in a totally ordered sequence.

## Cardinal arithmetic

We can define arithmetic operations on cardinal numbers that generalize the ordinary operations for natural numbers. It can be shown that for finite cardinals, these operations coincide with the usual operations for natural numbers. Furthermore, these operations share many properties with ordinary arithmetic.

### Successor cardinal

If the axiom of choice holds, then every cardinal *κ* has a successor, denoted *κ*+, where *κ*+ > *κ* and there are no cardinals between *κ* and its successor. (Without the axiom of choice, using Hartogs' theorem, it can be shown that for any cardinal number *κ*, there is a minimal cardinal *κ*+ such that $\kappa ^{+}\nleq \kappa .$ ) For finite cardinals, the successor is simply *κ* + 1. For infinite cardinals, the successor cardinal differs from the successor ordinal.

### Cardinal addition

If *X* and *Y* are disjoint, addition is given by the union of *X* and *Y*. If the two sets are not already disjoint, then they can be replaced by disjoint sets of the same cardinality (e.g., replace *X* by *X*×{0} and *Y* by *Y*×{1}).

$|X|+|Y|=|X\cup Y|.$

Zero is an additive identity *κ* + 0 = 0 + *κ* = *κ*.

Addition is associative (*κ* + *μ*) + *ν* = *κ* + (*μ* + *ν*).

Addition is commutative *κ* + *μ* = *μ* + *κ*.

Addition is non-decreasing in both arguments:

$(\kappa \leq \mu )\rightarrow ((\kappa +\nu \leq \mu +\nu ){\mbox{ and }}(\nu +\kappa \leq \nu +\mu )).$

Assuming the axiom of choice, addition of infinite cardinal numbers is easy. If either *κ* or *μ* is infinite, then

$\kappa +\mu =\max\{\kappa ,\mu \}\,.$

#### Subtraction

Assuming the axiom of choice and, given an infinite cardinal *σ* and a cardinal *μ*, there exists a cardinal *κ* such that *μ* + *κ* = *σ* if and only if *μ* ≤ *σ*. It will be unique (and equal to *σ*) if and only if *μ* < *σ*.

### Cardinal multiplication

The product of cardinals comes from the Cartesian product.

$|X|\cdot |Y|=|X\times Y|$

Zero is a multiplicative absorbing element: *κ*·0 = 0·*κ* = 0.

There are no nontrivial zero divisors: *κ*·*μ* = 0 → (*κ* = 0 or *μ* = 0).

One is a multiplicative identity: *κ*·1 = 1·*κ* = *κ*.

Multiplication is associative: (*κ*·*μ*)·*ν* = *κ*·(*μ*·*ν*).

Multiplication is commutative: *κ*·*μ* = *μ*·*κ*.

Multiplication is non-decreasing in both arguments: *κ* ≤ *μ* → (*κ*·*ν* ≤ *μ*·*ν* and *ν*·*κ* ≤ *ν*·*μ*).

Multiplication distributes over addition: *κ*·(*μ* + *ν*) = *κ*·*μ* + *κ*·*ν* and (*μ* + *ν*)·*κ* = *μ*·*κ* + *ν*·*κ*.

Assuming the axiom of choice, multiplication of infinite cardinal numbers is also easy. If either *κ* or *μ* is infinite and both are non-zero, then

$\kappa \cdot \mu =\max\{\kappa ,\mu \}.$

Thus the product of two infinite cardinal numbers is equal to their sum.

#### Division

Assuming the axiom of choice and given an infinite cardinal *π* and a non-zero cardinal *μ*, there exists a cardinal *κ* such that *μ* · *κ* = *π* if and only if *μ* ≤ *π*. It will be unique (and equal to *π*) if and only if *μ* < *π*.

### Cardinal exponentiation

Exponentiation is given by

$|X|^{|Y|}=\left|X^{Y}\right|,$

where *XY* is the set of all functions from *Y* to *X*. It is easy to check that the right-hand side depends only on ${|X|}$ and ${|Y|}$ .

κ

0

= 1 (in particular 0

0

= 1), see

empty function

.

If

μ

≥ 1, then 0

μ

= 0.

1

μ

= 1.

κ

1

=

κ

.

κ

μ

+

ν

=

κ

μ

·

κ

ν

.

κ

μ

·

ν

= (

κ

μ

)

ν

.

(

κ

·

μ

)

ν

=

κ

ν

·

μ

ν

.

Exponentiation is non-decreasing in both arguments:

(1 ≤

ν

and

κ

≤

μ

) → (

ν

κ

≤

ν

μ

) and

(

κ

≤

μ

) → (

κ

ν

≤

μ

ν

).

2|*X*| is the cardinality of the power set of the set *X* and Cantor's diagonal argument shows that 2|*X*| > |*X*| for any set *X*. This proves that no largest cardinal exists (because for any cardinal *κ*, we can always find a larger cardinal 2*κ*). In fact, the class of cardinals is a proper class. (This proof fails in some set theories, notably New Foundations.)

All the remaining propositions in this section assume the axiom of choice:

If

κ

and

μ

are both finite and greater than 1, and

ν

is infinite, then

κ

ν

=

μ

ν

.

If

κ

is infinite and

μ

is finite and non-zero, then

κ

μ

=

κ

.

If 2 ≤ *κ* and 1 ≤ *μ* and at least one of them is infinite, then:

max (

κ

, 2

μ

) ≤

κ

μ

≤ max (2

κ

, 2

μ

).

Using Kőnig's theorem, one can prove *κ* < *κ*cf(*κ*) and *κ* < cf(2*κ*) for any infinite cardinal *κ*, where cf(*κ*) is the cofinality of *κ*.

#### Roots

Assuming the axiom of choice and, given an infinite cardinal *κ* and a finite cardinal *μ* greater than 0, the cardinal *ν* satisfying $\nu ^{\mu }=\kappa$ will be $\kappa$ .

#### Logarithms

Assuming the axiom of choice and, given an infinite cardinal *κ* and a finite cardinal *μ* greater than 1, there may or may not be a cardinal *λ* satisfying $\mu ^{\lambda }=\kappa$ . However, if such a cardinal exists, it is infinite and less than *κ*, and any finite cardinality *ν* greater than 1 will also satisfy $\nu ^{\lambda }=\kappa$ .

The logarithm of an infinite cardinal number *κ* is defined as the least cardinal number *μ* such that *κ* ≤ 2*μ*. Logarithms of infinite cardinals are useful in some fields of mathematics, for example in the study of cardinal invariants of topological spaces, though they lack some of the properties that logarithms of positive real numbers possess.

## The continuum hypothesis

The continuum hypothesis (CH) states that there are no cardinals strictly between $\aleph _{0}$ and $2^{\aleph _{0}}.$ The latter cardinal number is also often denoted by ${\mathfrak {c}}$ ; it is the cardinality of the continuum (the set of real numbers). In this case $2^{\aleph _{0}}=\aleph _{1}.$

Similarly, the generalized continuum hypothesis (GCH) states that for every infinite cardinal $\kappa$ , there are no cardinals strictly between $\kappa$ and $2^{\kappa }$ . Both the continuum hypothesis and the generalized continuum hypothesis have been proved to be independent of the usual axioms of set theory, the Zermelo–Fraenkel axioms together with the axiom of choice (ZFC).

Indeed, Easton's theorem shows that, for regular cardinals $\kappa$ , the only restrictions ZFC places on the cardinality of $2^{\kappa }$ are that $\kappa <\operatorname {cf} (2^{\kappa })$ , and that the exponential function is non-decreasing.

## History

The notion of cardinality, as now understood, was formulated by Georg Cantor, the originator of set theory, in 1874–1884. Cantor noted that there is a bijection between two finite sets if and only if they have the same number of elements, and applied this concept of bijection to infinite sets (for example the set of natural numbers **N** = {0, 1, 2, 3, ...}). Thus, he called all sets having a bijection with **N** *denumerable (countably infinite) sets*, which all share the same cardinal number. He called the cardinal numbers of infinite sets transfinite cardinal numbers.

Cantor proved that any unbounded subset of **N** has the same cardinality as **N**, even though this might appear to run contrary to intuition. He also proved that the set of all ordered pairs of natural numbers is denumerable; this implies that the set of all rational numbers is also denumerable, since every rational can be represented by a pair of integers. He later proved that the set of all real algebraic numbers is also denumerable. Each real algebraic number *z* may be encoded as a finite sequence of integers, which are the coefficients in the polynomial equation of which it is a solution, i.e. the ordered *n*-tuple (*a*0, *a*1, ..., *an*), *ai* ∈ **Z** together with a pair of rationals (*b*0, *b*1) such that *z* is the unique root (if it exists) of the polynomial with coefficients (*a*0, *a*1, ..., *an*) that lies in the interval (*b*0, *b*1).

In his 1874 paper "On a Property of the Collection of All Real Algebraic Numbers", Cantor proved that there exist higher-order cardinal numbers, by showing that the set of real numbers has cardinality greater than that of **N**. His proof used an argument with nested intervals, but in an 1891 paper, he proved the same result using his ingenious and much simpler diagonal argument. The new cardinal number of the set of real numbers is called the cardinality of the continuum and Cantor used the symbol ${\mathfrak {c}}$ for it.

Cantor also developed a large portion of the general theory of cardinal numbers; he proved that (assuming the axiom of choice) there is a smallest transfinite cardinal number ( $\aleph _{0}$ , aleph-null), and that for every cardinal number there is a next-larger cardinal

$(\aleph _{1},\aleph _{2},\aleph _{3},\ldots ).$

Cantor formulated the continuum hypothesis in 1878. In 1940, Kurt Gödel showed that the continuum hypothesis cannot be disproved from ZFC, and in 1963, Paul Cohen showed that it cannot be proved from ZFC either, establishing its independence.
