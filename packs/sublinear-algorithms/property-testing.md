---
title: "Property testing"
source: https://en.wikipedia.org/wiki/Property_testing
domain: sublinear-algorithms
license: CC-BY-SA-4.0
tags: sublinear time algorithm, query complexity, sublinear approximation, estimation query
fetched: 2026-07-02
---

# Property testing

**Property testing** is a field of theoretical computer science, concerned with the design of super-fast algorithms for approximate decision making, where the decision refers to properties or parameters of huge objects.

A *property testing algorithm* for a decision problem is an algorithm whose query complexity (the number of queries made to its input) is much smaller than the instance size of the problem. Typically, property testing algorithms are used to determine whether some combinatorial structure S (such as a graph or a boolean function) satisfies some property P, or is "far" from having this property (meaning that an ε-fraction of the representation of S must be modified to make S satisfy P), using only a small number of "local" queries to the object.

For example, the following promise problem admits an algorithm whose query complexity is independent of the instance size (for an arbitrary constant *ε* > 0):

"Given a graph on

n

vertices, decide whether it is

bipartite

, or cannot be made bipartite even after removing an arbitrary subset of at most

ε

n

2

edges."

Property testing algorithms are central to the definition of probabilistically checkable proofs, as a probabilistically checkable proof is essentially a proof that can be verified by a property testing algorithm.

## Definition and variants

Formally, a **property testing algorithm** with query complexity *q*(*n*) and *proximity parameter* ε for a decision problem L is a randomized algorithm that, on input x (an instance of L) makes at most *q*(|*x*|) queries to x and behaves as follows:

- If x is in L, then the algorithm accepts x with probability at least 2/3.
- If x is ε-far from L, then the algorithm rejects x with probability at least 2/3.

Here, "x is ε-far from L" means that the Hamming distance between x and any string in L is at least *ε* |*x*|.

A property testing algorithm is said to have *one-sided error* if it satisfies the stronger condition that the accepting probability for instances *x* ∈ *L* is 1 instead of 2/3.

A property testing algorithm is said be *non-adaptive* if it performs all its queries before it "observes" any answers to previous queries. Such an algorithm can be viewed as operating in the following manner. First the algorithm receives its input. Before looking at the input, using its internal randomness, the algorithm decides which symbols of the input are to be queried. Next, the algorithm observes these symbols. Finally, without making any additional queries (but possibly using its randomness), the algorithm decides whether to accept or reject the input.

## Features and limitations

The main efficiency parameter of a property testing algorithm is its query complexity, which is the maximum number of input symbols inspected over all inputs of a given length (and all random choices made by the algorithm). Computer scientists are interested in designing algorithms whose query complexity is as small as possible. In many cases, the running time of property testing algorithms is sublinear in the instance length. Typically, the goal is first to make the query complexity as small as possible as a function of the instance size n, and then study the dependency on the proximity parameter ε.

Unlike other complexity-theoretic settings, the asymptotic query complexity of property testing algorithms is affected dramatically by the representation of instances. For example, when *ε* = 0.01, the problem of testing bipartiteness of *dense graphs* (which are represented by their adjacency matrix) admits an algorithm of constant query complexity. In contrast, sparse graphs on n vertices (which are represented by their adjacency list) require property testing algorithms of query complexity Ω(*n*1/2).

The query complexity of property testing algorithms grows as the proximity parameter ε becomes smaller for all non-trivial properties. This dependence on ε is necessary, as a change of fewer than ε symbols in the input cannot be detected with constant probability using fewer than *O*(1/*ε*) queries. Many interesting properties of dense graphs can be tested using query complexity that depends only on ε and not on the graph size n. However, the query complexity can grow enormously fast as a function of ε. For example, for a long time, the best known algorithm for testing whether a graph does not contain any triangle had a query complexity which is a tower function of poly(1/*ε*), and only in 2010 was this improved to a tower function of log(1/*ε*). One of the reasons for this enormous growth in bounds is that many of the positive results for property testing of graphs are established using the Szemerédi regularity lemma, which also has tower-type bounds in its conclusions. The connection of property testing to the Szemerédi regularity lemma and related graph removal lemmas is elaborated on below.

## Testing graph properties

For a graph G with n vertices, the notion of distance we will use is the *edit distance*. That is, we say that the distance between two graphs is the smallest ε such that one can add and/or delete *εn*2 edges and get from the first graph to the second. Under a reasonable representation of graphs, this is equivalent to the earlier *Hamming distance* definition (up to possibly a change of constants).

To make precise the general notions of property testing in the context of graphs, we say a tester for graph property P should distinguish with at least two-thirds probability between the cases of G satisfying P and the cases where G is ε-far in edit distance from satisfying P. The tester can access some oracle to query whether a pair of vertices has an edge between them in G or not. The *query complexity* is the number of such oracle queries. Say the tester has *one-sided error* if it has false positives and not false negatives, i.e. if G satisfies P, the tester always outputs the correct answer.

We can only differentiate between graphs that satisfy P versus those far from P, as opposed to satisfying versus not satisfying P. In the latter case, consider two graphs: G satisfying P and H not satisfying P by changing only a few edges. One example is testing triangle-freeness with *H* a graph with exactly one triangle and G having one of these edges removed. Then, the tester cannot tell them apart unless it queries every edge, which it cannot do.

### Short history

The field of graph property testing was first introduced by Goldreich, Goldwasser, and Ron. In their seminal paper published in 1998, an abstract graph partition problem is analyzed and some testers provided. These include as special cases several important graph properties like bipartiteness, *k*-colorability, having a large clique, and having a large cut. In particular, the *natural* algorithms that sample a subgraph and check whether it satisfy the property are all correct, albeit with perhaps-suboptimal query complexities.

Since then, several related discoveries have been made

- In 1992, Alon, Duke, Lefmann, Rödl, and Yuster showed that for every graph *H*, the property of not containing *H* as a subgraph is testable.
- In 1999, Alon, Fischer, Krivelevich, and Szegedy showed that for every graph *H*, the property of not containing *H* as an induced subgraph subgraph is testable.
- In 2005, Alon and Shapira showed that any *monotone graph property* (one that is preserved under vertex and edge deletion) is testable with one-sided error.
- In 2008, Alon and Shapira exhibited testers with one-sided error for all *hereditary* graph properties. They also characterized properties that are easy to test. Namely, these natural properties are *semi-hereditary*. These statements will be clarified below.

### Testing hereditary graph properties

A graph property is *hereditary* if it is preserved under deletion of vertices, or equivalently, if it is preserved under taking induced subgraphs. A few important hereditary properties are *H*-freeness (for some graph *H*), k-colorability, and planarity. All hereditary properties are testable.

Theorem (Alon & Shapira 2008).

Every hereditary graph property is testable with one-sided error.

The proof relies on a version of the **graph removal lemma** for infinite families of induced subgraphs. The query complexity using this regularity approach is large due to the tower function bound in the **Szemerédi regularity lemma**.

Theorem (Infinite graph removal lemma).

For each (possibly infinite) set of graphs

H

and

ε

> 0

, there exist

h

0

and

δ

> 0

so that, if

G

is an

n

-vertex graph with fewer than

δ

n

v

(

H

)

copies of

H

for every

H

∈

H

with at most

h

0

vertices, then

G

can be made induced

H

-free by adding/removing fewer than

ε

n

2

edges.

### Oblivious testers

Informally, an *oblivious tester* is oblivious to the size of the input. For a graph property P, it is an algorithm that takes as input a parameter ε and graph G, and then runs as a property testing algorithm on G for the property P with proximity parameter ε that makes exactly *q*(*ε*) queries to G.

Definition.

An

oblivious tester

is an algorithm that takes as input a parameter

ε

. It computes an integer

q

(

ε

)

and then asks an oracle for an induced subgraph

H

on exactly

q

(

ε

)

vertices from

G

chosen uniformly at random. It then accepts or rejects (possibly randomly) according to

ε

and

H

. We say it tests for the property

P

if it accepts with probability at least

2/3

for

G

that has property

P

, and rejects with probability at least

2/3

or

G

that is

ε

-far from having property

P

.

Crucially, the number of queries an oblivious tester makes is a constant dependent only on ε and not the size of the input graph G. In complete analogy with property testing algorithms, we can talk about oblivious testers with one-sided error.

### Testing semi-hereditary graph properties

We can contrive some graph properties for which a tester must access the number of vertices.

Example.

A graph

G

satisfies property

P

if it is bipartite with an even number of vertices or

perfect

with an odd number of vertices.

In this case, the tester cannot even differentiate which property (bipartiteness or perfectness) to test unless it knows the number of vertices. There are many examples of such unnatural properties. In fact, the characterization of graph properties testable by an oblivious tester with one-sided error leads to a class of natural properties.

Definition.

A graph property

H

is

semi-hereditary

if there exists a hereditary graph property

H

such that any graph satisfying

P

satisfies

H

, and for every

ε

> 0

, there is an

M

(

ε

)

such that every graph of size at least

M

(

ε

)

that is

ε

-far from satisfying

P

contains an induced subgraph that does not satisfy

H

.

Trivially, hereditary properties are also semi-hereditary. This characterization partially answers the converse to the other Alon & Shapira theorem above: the properties that are easy to test properties (having oblivious testers with one-sided error) are almost hereditary. In the same paper, they showed that

Theorem (Alon & Shapira 2008).

A graph property

P

has an oblivious one-sided error tester

if and only if

P

is semi-hereditary.

### Examples: testing some graph properties

In this section, we will give some *natural* oblivious testing algorithms with one-sided error for triangle-freeness, bipartiteness, and k-colorability. They are natural in the sense that we follow the natural idea of randomly sampling some subset X of vertices of *G* and checking whether the graph property holds on the subgraph spanned by *X* by brute-force search. We have one-sided error since these properties are actually hereditary: if *G* satisfy the property, so must the induced subgraph spanned by *X*, so our tester always accepts.

For triangle-freeness, the tester is an application of the **triangle removal lemma**. In particular, it tells us that if graph *G* is ε-far from being triangle-free, then there is a (computable) constant *δ* = *δ*(*ε*) so that G has at least *δn*3 triangles.

> **Example (Triangle-freeness Testing Algorithm).**
> 
> 1. Given graph G, choose a random set *X* of *q*(*ε*) = 1/*δ* triples of vertices independently at random, where δ is as above.
> 2. For every triple of vertices in *X*, query whether all three pairs of vertices are adjacent in G.
> 3. The algorithm *accepts* if no triple of vertices induces a triangle, and *rejects* otherwise.

For bipartiteness and k-colorability, let δ be the desired upper bound on error probability for the following testers. Note that query complexity should not be confused with running time. The latter is often exponential (as is the case of both) due to a lack of polynomial time decision algorithm to test the property on the induced subgraph. We instead check by brute-force search.

> **Example (Bipartite Testing Algorithm).**
> 
> 1. Given graph G, choose a random set *X* of *q*(*ε*) = *O*(log(1/(*εδ*))/*ε*2) vertices.
> 2. For every pair of vertices in *X*, query whether they are adjacent in G.
> 3. It *accepts* if the induced subgraph of G on *X* is bipartite and *rejects* otherwise.

> **Example (k-colorability Testing Algorithm).**
> 
> 1. Given graph G, choose a random set *X* of *q*(*ε*) = *O*(*k*4 log2(*k*/*δ*)/*ε*3) vertices.
> 2. For every pair of vertices in *X*, query if they are adjacent in G.
> 3. It *accepts* if the induced subgraph of G on *X* is k-colorable and *rejects* otherwise.
