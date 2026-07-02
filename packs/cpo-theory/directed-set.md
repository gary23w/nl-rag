---
title: "Directed set"
source: https://en.wikipedia.org/wiki/Directed_set
domain: cpo-theory
license: CC-BY-SA-4.0
tags: complete partial order, directed-complete partial order, chain-complete poset, least upper bound
fetched: 2026-07-02
---

# Directed set

In mathematics, a **directed set** (or a **directed preorder** or a **filtered set**) is a preordered set in which every finite subset has an upper bound. In other words, it is a non-empty preordered set A such that for any a and b in A there exists c in A with $a\leq c$ and $b\leq c$ . A directed set's preorder is called a **direction**.

The notion defined above is sometimes called an **upward directed set**. A **downward directed set** is defined symmetrically, meaning that every finite subset has a lower bound. Some authors (and this article) assume that a directed set is directed upward, unless otherwise stated. Other authors call a set directed if and only if it is directed both upward and downward.

Directed sets are a generalization of nonempty totally ordered sets. That is, all totally ordered sets are directed sets (contrast *partially* ordered sets, which need not be directed). Join-semilattices (which are partially ordered sets) are directed sets as well, but not conversely. Likewise, lattices are directed sets both upward and downward.

In topology, directed sets are used to define nets, which generalize sequences and unify the various notions of limit used in analysis. Directed sets also give rise to direct limits in abstract algebra and (more generally) category theory.

## Examples

The set of natural numbers $\mathbb {N}$ with the ordinary order $\,\leq \,$ is one of the most important examples of a directed set. Every totally ordered set is a directed set, including $(\mathbb {Z} ,\leq ),$ $(\mathbb {Q} ,\leq ),$ and $(\mathbb {R} ,\leq ).$

A (trivial) example of a partially ordered set that is ***not*** directed is the set $\{a,b\},$ in which the only order relations are $a\leq a$ and $b\leq b.$ A less trivial example is like the following example of the "reals directed towards $x_{0}$ " but in which the ordering rule only applies to pairs of elements on the same side of $x_{0}$ (that is, if one takes an element a to the left of $x_{0},$ and b to its right, then a and b are not comparable, and the subset $\{a,b\}$ has no upper bound).

If an abstract rewriting system $(X,\to )$ is confluent, then its transitive closure $(X,\to ^{*})$ is a directed set.

### Product of directed sets

Let $\mathbb {D} _{1}$ and $\mathbb {D} _{2}$ be directed sets. Then the Cartesian product set $\mathbb {D} _{1}\times \mathbb {D} _{2}$ can be made into a directed set by defining $\left(n_{1},n_{2}\right)\leq \left(m_{1},m_{2}\right)$ if and only if $n_{1}\leq m_{1}$ and $n_{2}\leq m_{2}.$ In analogy to the product order this is the product direction on the Cartesian product. For example, the set $\mathbb {N} \times \mathbb {N}$ of pairs of natural numbers can be made into a directed set by defining $\left(n_{0},n_{1}\right)\leq \left(m_{0},m_{1}\right)$ if and only if $n_{0}\leq m_{0}$ and $n_{1}\leq m_{1}.$

### Directed towards a point

If $x_{0}$ is a real number then the set $I:=\mathbb {R} \backslash \lbrace x_{0}\rbrace$ can be turned into a directed set by defining $a\leq _{I}b$ if $\left|a-x_{0}\right|\geq \left|b-x_{0}\right|$ (so "greater" elements are closer to $x_{0}$ ). We then say that the reals have been **directed towards $x_{0}.$** This is an example of a directed set that is *neither* partially ordered nor totally ordered. This is because antisymmetry breaks down for every pair a and b equidistant from $x_{0},$ where a and b are on opposite sides of $x_{0}.$ Explicitly, this happens when $\{a,b\}=\left\{x_{0}-r,x_{0}+r\right\}$ for some real $r\neq 0,$ in which case $a\leq _{I}b$ and $b\leq _{I}a$ even though $a\neq b.$ Had this preorder been defined on $\mathbb {R}$ instead of $\mathbb {R} \backslash \lbrace x_{0}\rbrace$ then it would still form a directed set but it would now have a (unique) greatest element, specifically $x_{0}$ ; however, it still wouldn't be partially ordered. This example can be generalized to a metric space $(X,d)$ by defining on X or $X\setminus \left\{x_{0}\right\}$ the preorder $a\leq b$ if and only if $d\left(a,x_{0}\right)\geq d\left(b,x_{0}\right).$

### Maximal and greatest elements

An element m of a preordered set $(I,\leq )$ is a *maximal element* if for every $j\in I,$ $m\leq j$ implies $j\leq m.$ It is a *greatest element* if for every $j\in I,$ $j\leq m.$

Any preordered set with a greatest element is a directed set with the same preorder. For instance, in a poset $P,$ every lower closure of an element; that is, every subset of the form $\{a\in P:a\leq x\}$ where x is a fixed element from $P,$ is directed.

A preordered set is directed if and only if the (possibly empty) set of maximal elements is equal to the set of greatest elements.

### Subset inclusion

The subset inclusion relation $\,\subseteq ,\,$ along with its dual $\,\supseteq ,\,$ define partial orders on any given family of sets. A non-empty family of sets is a directed set with respect to the partial order $\,\supseteq \,$ (respectively, $\,\subseteq \,$ ) if and only if the intersection (respectively, union) of any two of its members contains as a subset (respectively, is contained as a subset of) some third member. In symbols, a family I of sets is directed with respect to $\,\supseteq \,$ (respectively, $\,\subseteq \,$ ) if and only if

for all

$A,B\in I,$

there exists some

$C\in I$

such that

$A\supseteq C$

and

$B\supseteq C$

(respectively,

$A\subseteq C$

and

$B\subseteq C$

)

or equivalently,

for all

$A,B\in I,$

there exists some

$C\in I$

such that

$A\cap B\supseteq C$

(respectively,

$A\cup B\subseteq C$

).

Many important examples of directed sets can be defined using these partial orders. For example, by definition, a *prefilter* or *filter base* is a non-empty family of sets that is a directed set with respect to the partial order $\,\supseteq \,$ and that also does not contain the empty set (this condition prevents triviality because otherwise, the empty set would then be a greatest element with respect to $\,\supseteq \,$ ). Every π-system, which is a non-empty family of sets that is closed under the intersection of any two of its members, is a directed set with respect to $\,\supseteq \,.$ Every λ-system is a directed set with respect to $\,\subseteq \,.$ Every filter, topology, and σ-algebra is a directed set with respect to both $\,\supseteq \,$ and $\,\subseteq \,.$

#### Tails of nets

By definition, a *net* is a function from a directed set and a sequence is a function from the natural numbers $\mathbb {N} .$ Every sequence canonically becomes a net by endowing $\mathbb {N}$ with $\,\leq .\,$

If $x_{\bullet }=\left(x_{i}\right)_{i\in I}$ is any net from a directed set $(I,\leq )$ then for any index $i\in I,$ the set $x_{\geq i}:=\left\{x_{j}:j\geq i{\text{ with }}j\in I\right\}$ is called the tail of $(I,\leq )$ starting at $i.$ The family $\operatorname {Tails} \left(x_{\bullet }\right):=\left\{x_{\geq i}:i\in I\right\}$ of all tails is a directed set with respect to ${\displaystyle \,\supseteq$ in fact, it is even a prefilter.

#### Neighborhoods

If T is a topological space and $x_{0}$ is a point in $T,$ the set of all neighbourhoods of $x_{0}$ can be turned into a directed set by writing $U\leq V$ if and only if U contains $V.$ For every $U,$ $V,$ and W  :

- $U\leq U$ since U contains itself.
- if $U\leq V$ and $V\leq W,$ then $U\supseteq V$ and $V\supseteq W,$ which implies $U\supseteq W.$ Thus $U\leq W.$
- because $x_{0}\in U\cap V,$ and since both $U\supseteq U\cap V$ and $V\supseteq U\cap V,$ we have $U\leq U\cap V$ and $V\leq U\cap V.$

#### Finite subsets

The set $\operatorname {Finite} (I)$ of all finite subsets of a set I is directed with respect to $\,\subseteq \,$ since given any two $A,B\in \operatorname {Finite} (I),$ their union $A\cup B\in \operatorname {Finite} (I)$ is an upper bound of A and B in $\operatorname {Finite} (I).$ This particular directed set is used to define the sum ${\textstyle \sum \limits _{i\in I}}r_{i}$ of a generalized series of an I -indexed collection of numbers $\left(r_{i}\right)_{i\in I}$ (or more generally, the sum of elements in an abelian topological group, such as vectors in a topological vector space) as the limit of the net of partial sums $F\in \operatorname {Finite} (I)\mapsto {\textstyle \sum \limits _{i\in F}}r_{i};$ that is: $\sum _{i\in I}r_{i}~:=~\lim _{F\in \operatorname {Finite} (I)}\ \sum _{i\in F}r_{i}~=~\lim \left\{\sum _{i\in F}r_{i}\,:F\subseteq I,F{\text{ finite }}\right\}.$

### Logic

Let S be a formal theory, which is a set of sentences with certain properties (details of which can be found in the article on the subject). For instance, S could be a first-order theory (like Zermelo–Fraenkel set theory) or a simpler zeroth-order theory. The preordered set $(S,\Leftarrow )$ is a directed set because if $A,B\in S$ and if $C:=A\wedge B$ denotes the sentence formed by logical conjunction $\,\wedge ,\,$ then $A\Leftarrow C$ and $B\Leftarrow C$ where $C\in S.$ If $S/\sim$ is the Lindenbaum–Tarski algebra associated with S then $\left(S/\sim ,\Leftarrow \right)$ is a partially ordered set that is also a directed set.

## Contrast with semilattices

Directed set is a more general concept than (join) semilattice: every join semilattice is a directed set, as the join or least upper bound of two elements is the desired $c.$ The converse does not hold however, witness the directed set {1000,0001,1101,1011,1111} ordered bitwise (e.g. $1000\leq 1011$ holds, but $0001\leq 1000$ does not, since in the last bit 1 > 0), where {1000,0001} has three upper bounds but no *least* upper bound, cf. picture. (Also note that without 1111, the set is not directed.)

## Directed subsets

The order relation in a directed set is not required to be antisymmetric, and therefore directed sets are not always partial orders. However, the term *directed set* is also used frequently in the context of posets. In this setting, a subset A of a partially ordered set $(P,\leq )$ is called a **directed subset** if it is a directed set according to the same partial order: in other words, it is not the empty set, and every pair of elements has an upper bound. Here the order relation on the elements of A is inherited from P ; for this reason, reflexivity and transitivity need not be required explicitly.

A directed subset of a poset is not required to be downward closed; a subset of a poset is directed if and only if its downward closure is an ideal. While the definition of a directed set is for an "upward-directed" set (every pair of elements has an upper bound), it is also possible to define a downward-directed set in which every pair of elements has a common lower bound. A subset of a poset is downward-directed if and only if its upper closure is a filter.

Directed subsets are used in domain theory, which studies directed-complete partial orders. These are posets in which every upward-directed set is required to have a least upper bound. In this context, directed subsets again provide a generalization of convergent sequences.
