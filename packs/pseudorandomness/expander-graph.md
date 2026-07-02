---
title: "Expander graph"
source: https://en.wikipedia.org/wiki/Expander_graph
domain: pseudorandomness
license: CC-BY-SA-4.0
tags: pseudorandomness theory, pseudorandom generator, randomness extractor, expander construction
fetched: 2026-07-02
---

# Expander graph

In graph theory, an **expander graph** is a sparse graph that has strong connectivity properties, quantified using vertex, edge or spectral expansion. Expander constructions have spawned research in pure and applied mathematics, with several applications to complexity theory, design of robust computer networks, and the theory of error-correcting codes.

## Definitions

Intuitively, an expander graph is a finite, undirected multigraph in which every subset of the vertices that is not "too large" has a "large" boundary. Different formalisations of these notions give rise to different notions of expanders: *edge expanders*, *vertex expanders*, and *spectral expanders*, as defined below.

A disconnected graph is not an expander, since the boundary of a connected component is empty. Every connected finite graph is an expander; however, different connected graphs have different expansion parameters. The complete graph has the best expansion property, but it has largest possible degree. Informally, a graph is a good expander if it has low degree and high expansion parameters.

### Edge expansion

The *edge expansion* (also *isoperimetric number* or Cheeger constant) *h*(*G*) of a graph G on n vertices is defined as

$h(G)=\min _{0<|S|\leq {\frac {n}{2}}}{\frac {|\partial S|}{|S|}},$

where

$\partial S:=\{\{u,v\}\in E(G)\ :\ u\in S,v\notin S\},$

which can also be written as ∂*S* = *E*(*S*, *S*) with *S* := *V*(*G*) \ *S* the complement of S and

$E(A,B)=\{\{u,v\}\in E(G)\ :\ u\in A,v\in B\}$

the edges between the subsets of vertices *A*,*B* ⊆ *V*(*G*).

In the equation, the minimum is over all nonempty sets S of at most *n*⁄2 vertices and ∂*S* is the *edge boundary* of S, i.e., the set of edges with exactly one endpoint in S.

Intuitively,

$\min {|\partial S|}=\min |E({S},{\overline {S}})|$

is the minimum number of edges that need to be cut in order to split the graph in two. The edge expansion normalizes this concept by dividing with smallest number of vertices among the two parts. To see how the normalization can drastically change the value, consider the following example. Take two complete graphs with the same number of vertices n and add n edges between the two graphs by connecting their vertices one-to-one. The minimum cut will be n but the edge expansion will be 1.

Notice that in min |∂*S*|, the optimization can be equivalently done either over 0 ≤ |*S*| ≤ *n*⁄2 or over any non-empty subset, since $E(S,{\overline {S}})=E({\overline {S}},S)$ . The same is not true for *h*(*G*) because of the normalization by |*S*|. If we want to write *h*(*G*) with an optimization over all non-empty subsets, we can rewrite it as

$h(G)=\min _{\emptyset \subsetneq S\subsetneq V(G)}{\frac {|E({S},{\overline {S}})|}{\min\{|S|,|{\overline {S}}|\}}}.$

### Vertex expansion

The *vertex isoperimetric number* *h*out(*G*) (also *vertex expansion* or *magnification*) of a graph G is defined as

$h_{\text{out}}(G)=\min _{0<|S|\leq {\frac {n}{2}}}{\frac {|\partial _{\text{out}}(S)|}{|S|}},$

where ∂out(*S*) is the *outer boundary* of S, i.e., the set of vertices in *V*(*G*) \ *S* with at least one neighbor in S. In a variant of this definition (called *unique neighbor expansion*) ∂out(*S*) is replaced by the set of vertices in V with *exactly* one neighbor in S.

The *vertex isoperimetric number* *h*in(*G*) of a graph G is defined as

$h_{\text{in}}(G)=\min _{0<|S|\leq {\frac {n}{2}}}{\frac {|\partial _{\text{in}}(S)|}{|S|}},$

where $\partial _{\text{in}}(S)$ is the *inner boundary* of S, i.e., the set of vertices in S with at least one neighbor in *V*(*G*) \ *S*.

### Spectral expansion

When G is d-regular, a linear algebraic definition of expansion is possible based on the eigenvalues of the adjacency matrix *A* = *A*(*G*) of G, where Aij is the number of edges between vertices i and j. Because A is symmetric, the spectral theorem implies that A has n real-valued eigenvalues *λ*1 ≥ *λ*2 ≥ … ≥ *λ**n*. It is known that all these eigenvalues are in [−*d*, *d*] and more specifically, it is known that *λ**n* = −*d* if and only if G is bipartite.

More formally, we refer to an n-vertex, d-regular graph with

$\max _{i\neq 1}|\lambda _{i}|\leq \lambda$

as an (*n*, *d*, *λ*)-*graph*. The bound given by an (*n*, *d*, *λ*)-graph on *λ**i* for *i* ≠ 1 is useful in many contexts, including the expander mixing lemma.

Spectral expansion can be *two-sided*, as above, with $\max _{i\neq 1}|\lambda _{i}|\leq \lambda$ , or it can be *one-sided*, with $\max _{i\neq 1}\lambda _{i}\leq \lambda$ . The latter is a weaker notion that holds also for bipartite graphs and is still useful for many applications, such as the Alon–Chung lemma.

Because G is regular, the uniform distribution $u\in \mathbb {R} ^{n}$ with *ui* = 1⁄*n* for all *i* = 1, …, *n* is the stationary distribution of G. That is, we have *Au* = *du*, and u is an eigenvector of A with eigenvalue *λ*1 = *d*, where d is the degree of the vertices of G. The *spectral gap* of G is defined to be *d* − *λ*2, and it measures the spectral expansion of the graph G.

If we set

$\lambda =\max\{|\lambda _{2}|,|\lambda _{n}|\}$

as this is the largest eigenvalue corresponding to an eigenvector orthogonal to u, it can be equivalently defined using the Rayleigh quotient:

$\lambda =\max _{v\perp u,v\neq 0}{\frac {\|Av\|_{2}}{\|v\|_{2}}},$

where

$\|v\|_{2}=\left(\sum _{i=1}^{n}v_{i}^{2}\right)^{1/2}$

is the 2-norm of the vector $v\in \mathbb {R} ^{n}$ .

The normalized versions of these definitions are also widely used and more convenient in stating some results. Here one considers the matrix ⁠1/*d*⁠*A*, which is the Markov transition matrix of the graph G. Its eigenvalues are between −1 and 1. For not necessarily regular graphs, the spectrum of a graph can be defined similarly using the eigenvalues of the Laplacian matrix. For directed graphs, one considers the singular values of the adjacency matrix A, which are equal to the roots of the eigenvalues of the symmetric matrix *A*T*A*.

### Expander families

A family $(G_{i})_{i\in \mathbb {N} }$ of d -regular graphs of increasing size is an **expander family** if $h(G_{i})$ is bounded away from zero.

## Relationships between different expansion properties

The expansion parameters defined above are related to each other. In particular, for any d-regular graph G,

$h_{\text{out}}(G)\leq h(G)\leq d\cdot h_{\text{out}}(G).$

Consequently, for constant degree graphs, vertex and edge expansion are qualitatively the same.

### Cheeger inequalities

When G is d-regular, meaning each vertex is of degree d, there is a relationship between the isoperimetric constant *h*(*G*) and the gap *d* − *λ*2 in the spectrum of the adjacency operator of G. By standard spectral graph theory, the trivial eigenvalue of the adjacency operator of a d-regular graph is *λ*1 = *d* and the first non-trivial eigenvalue is *λ*2. If G is connected, then *λ*2 < *d*. An inequality due to Dodziuk and independently Alon and Milman states that

${\tfrac {1}{2}}(d-\lambda _{2})\leq h(G)\leq {\sqrt {2d(d-\lambda _{2})}}.$

In fact, the lower bound is tight. The lower bound is achieved in limit for the hypercube Qn, where *h*(*G*) = 1 and *d* – *λ*2 = 2. The upper bound is (asymptotically) achieved for a cycle, where *h*(*Cn*) = 4/*n* = Θ(1/*n*) and *d* – *λ*2 = 2 – 2cos(2 $\pi$ /*n*) ≈ (2 $\pi$ /*n*)2 = Θ(1/*n*2). A better bound is given in as

$h(G)\leq {\sqrt {d^{2}-\lambda _{2}^{2}}}.$

These inequalities are closely related to the Cheeger bound for Markov chains and can be seen as a discrete version of Cheeger's inequality in Riemannian geometry.

Similar connections between vertex isoperimetric numbers and the spectral gap have also been studied:

$h_{\text{out}}(G)\leq \left({\sqrt {4(d-\lambda _{2})}}+1\right)^{2}-1$

$h_{\text{in}}(G)\leq {\sqrt {8(d-\lambda _{2})}}.$

Asymptotically speaking, the quantities *h*2⁄*d*, *h*out, and *h*in2 are all bounded above by the spectral gap *O*(*d* – *λ*2).

## Constructions

There are four general strategies for explicitly constructing families of expander graphs. The first strategy is algebraic and group-theoretic, the second strategy is analytic and uses additive combinatorics, the third strategy is combinatorial and uses the zig-zag and related graph products, and the fourth strategy is based on lifts. Noga Alon showed that certain graphs constructed from finite geometries are the sparsest examples of highly expanding graphs.

### Margulis–Gabber–Galil

Algebraic constructions based on Cayley graphs are known for various variants of expander graphs. The following construction is due to Margulis and has been analysed by Gabber and Galil. For every natural number n, one considers the graph Gn with the vertex set $\mathbb {Z} _{n}\times \mathbb {Z} _{n}$ , where $\mathbb {Z} _{n}=\mathbb {Z} /n\mathbb {Z}$ : For every vertex $(x,y)\in \mathbb {Z} _{n}\times \mathbb {Z} _{n}$ , its eight adjacent vertices are

$(x\pm 2y,y),(x\pm (2y+1),y),(x,y\pm 2x),(x,y\pm (2x+1)).$

Then the following holds:

> **Theorem.** For all n, the graph Gn has second-largest eigenvalue $\lambda (G)\leq 5{\sqrt {2}}$ .

### Ramanujan graphs

By a theorem of Alon and Boppana, all sufficiently large d-regular graphs satisfy $\lambda _{2}\geq 2{\sqrt {d-1}}-o(1)$ , where *λ*2 is the second largest eigenvalue in absolute value. As a direct consequence, we know that for every fixed d and $\lambda <2{\sqrt {d-1}}$ , there are only finitely many (*n*, *d*, *λ*)-graphs. Ramanujan graphs are d-regular graphs for which this bound is tight, satisfying

$\lambda =\max _{|\lambda _{i}|<d}|\lambda _{i}|\leq 2{\sqrt {d-1}}.$

Hence Ramanujan graphs have an asymptotically smallest possible value of *λ*2. This makes them excellent spectral expanders.

Lubotzky, Phillips, and Sarnak (1988), Margulis (1988), and Morgenstern (1994) show how Ramanujan graphs can be constructed explicitly.

In 1985, Alon, conjectured that most d-regular graphs on n vertices, for sufficiently large n, are almost Ramanujan. That is, for *ε* > 0, they satisfy

$\lambda \leq 2{\sqrt {d-1}}+\varepsilon$

.

In 2003, Joel Friedman both proved the conjecture and specified what is meant by "most d-regular graphs" by showing that random d-regular graphs have $\lambda \leq 2{\sqrt {d-1}}+\varepsilon$ for every *ε* > 0 with probability 1 – *O*(*n*-τ), where

$\tau =\left\lceil {\frac {{\sqrt {d-1}}+1}{2}}\right\rceil .$

A simpler proof of a slightly weaker result was given by Puder.

Marcus, Spielman and Srivastava, gave a construction of bipartite Ramanujan graphs based on lifts.

In 2024 a preprint by Jiaoyang Huang, Theo McKenzieand and Horng-Tzer Yau proved that

$\lambda \leq 2{\sqrt {d-1}}$

.

with the fraction of eigenvalues that hit the Alon-Boppana bound approximately 69% from proving that edge universality holds, that is they follow a Tracy-Widom distribution associated with the Gaussian Orthogonal Ensemble

### Zig-zag product

Reingold, Vadhan, and Wigderson introduced the zig-zag product in 2000. Roughly speaking, the zig-zag product of two expander graphs produces a graph with only slightly worse expansion. Therefore, a zig-zag product can also be used to construct families of expander graphs. If G is a (*n*, *d*, *λ*1)-graph and H is an (*m*, *d*, *λ*2)-graph, then the zig-zag product *G* ◦ *H* is a (*nm*, *d*2, *φ*(*λ*1, *λ*2))-graph where φ has the following properties.

1. If *λ*1 < 1 and *λ*2 < 1, then *φ*(*λ*1, *λ*2) < 1;
2. *φ*(*λ*1, *λ*2) ≤ *λ*1 + *λ*2.

Specifically,

$\phi (\lambda _{1},\lambda _{2})={\frac {1}{2}}(1-\lambda _{2}^{2})\lambda _{2}+{\frac {1}{2}}{\sqrt {(1-\lambda _{2}^{2})^{2}\lambda _{1}^{2}+4\lambda _{2}^{2}}}.$

Note that property (1) implies that the zig-zag product of two expander graphs is also an expander graph, thus zig-zag products can be used inductively to create a family of expander graphs.

Intuitively, the construction of the zig-zag product can be thought of in the following way. Each vertex of G is blown up to a "cloud" of m vertices, each associated to a different edge connected to the vertex. Each vertex is now labeled as (*v*, *k*) where v refers to an original vertex of G and k refers to the kth edge of v. Two vertices, (*v*, *k*) and (*w*,*ℓ*) are connected if it is possible to get from (*v*, *k*) to (*w*, *ℓ*) through the following sequence of moves.

1. *Zig* – Move from (*v*, *k*) to (*v*, *k'*), using an edge of H.
2. Jump across clouds using edge k' in G to get to (*w*, *ℓ′*).
3. *Zag* – Move from (*w*, *ℓ′*) to (*w*, *ℓ*) using an edge of H.

### Lifts

An r-lift of a graph is formed by replacing each vertex by r vertices, and each edge by a matching between the corresponding sets of r vertices. The lifted graph inherits the eigenvalues of the original graph, and has some additional eigenvalues. Bilu and Linial showed that every d-regular graph has a 2-lift in which the additional eigenvalues are at most $O({\sqrt {d\log ^{3}d}})$ in magnitude. They also showed that if the starting graph is a good enough expander, then a good 2-lift can be found in polynomial time, thus giving an efficient construction of d-regular expanders for every d.

Bilu and Linial conjectured that the bound $O({\sqrt {d\log ^{3}d}})$ can be improved to $2{\sqrt {d-1}}$ , which would be optimal due to the Alon–Boppana bound. This conjecture was proved in the bipartite setting by Marcus, Spielman and Srivastava, who used the method of interlacing polynomials. As a result, they obtained an alternative construction of bipartite Ramanujan graphs. The original non-constructive proof was turned into an algorithm by Michael B. Cohen. Later the method was generalized to r-lifts by Hall, Puder and Sawin.

### Randomized constructions

There are many results that show the existence of graphs with good expansion properties through probabilistic arguments. In fact, the existence of expanders was first proved by Pinsker who showed that for a randomly chosen n vertex left d regular bipartite graph, |*N*(*S*)| ≥ (*d* – 2)|*S*| for all subsets of vertices |*S*| ≤ *cdn* with high probability, where cd is a constant depending on d that is *O*(*d*-4). Alon and Roichman showed that for every 1 > *ε* > 0, there is some *c*(*ε*) > 0 such that the following holds: For a group G of order n, consider the Cayley graph on G with *c*(*ε*) log2 *n* randomly chosen elements from G. Then, in the limit of n getting to infinity, the resulting graph is almost surely an *ε*-expander.

In 2021, Alexander modified an MCMC algorithm to look for randomized constructions to produce Ramanujan graphs with a fixed vertex size and degree of regularity. The results show the Ramanujan graphs exist for every vertex size and degree pair up to 2000 vertices.

In 2024 Alon produced an explicit construction for near Ramanujan graphs of every vertex size and degree pair.

## Applications and useful properties

The original motivation for expanders is to build economical robust networks (phone or computer): an expander with bounded degree is precisely an asymptotic robust graph with the number of edges growing linearly with size (number of vertices), for all subsets.

Expander graphs have found extensive applications in computer science, in designing algorithms, error correcting codes, extractors, pseudorandom generators, sorting networks (Ajtai, Komlós & Szemerédi (1983)) and robust computer networks. They have also been used in proofs of many important results in computational complexity theory, such as SL = L (Reingold (2008)) and the PCP theorem (Dinur (2007)). In cryptography, expander graphs are used to construct hash functions.

In a 2006 survey of expander graphs, Hoory, Linial, and Wigderson split the study of expander graphs into four categories: extremal problems, typical behavior, explicit constructions, and algorithms. Extremal problems focus on the bounding of expansion parameters, while typical behavior problems characterize how the expansion parameters are distributed over random graphs. Explicit constructions focus on constructing graphs that optimize certain parameters, and algorithmic questions study the evaluation and estimation of parameters.

### Expander mixing lemma

The expander mixing lemma states that for an (*n*, *d*, *λ*)-graph, for any two subsets of the vertices *S*, *T* ⊆ *V*, the number of edges between S and T is approximately what you would expect in a random d-regular graph. The approximation is better the smaller *λ* is. In a random d-regular graph, as well as in an Erdős–Rényi random graph with edge probability *d*⁄*n*, we expect *d*⁄*n* • |*S*| • |*T*| edges between S and T.

More formally, let *E*(*S*, *T*) denote the number of edges between S and T. If the two sets are not disjoint, edges in their intersection are counted twice, that is,

$E(S,T)=2|E(G[S\cap T])|+E(S\setminus T,T)+E(S,T\setminus S).$

Then the expander mixing lemma says that the following inequality holds:

$\left|E(S,T)-{\frac {d\cdot |S|\cdot |T|}{n}}\right|\leq \lambda {\sqrt {|S|\cdot |T|}}.$

Many properties of (*n*, *d*, *λ*)-graphs are corollaries of the expander mixing lemmas, including the following.

- An independent set of a graph is a subset of vertices with no two vertices adjacent. In an (*n*, *d*, *λ*)-graph, an independent set has size at most *λn*⁄*d*.
- The chromatic number of a graph G, *χ*(*G*), is the minimum number of colors needed such that adjacent vertices have different colors. Hoffman showed that *d*⁄*λ* ≤ *χ*(*G*), while Alon, Krivelevich, and Sudakov showed that if *d* < 2*n*⁄3, then

$\chi (G)\leq O\left({\frac {d}{\log(1+d/\lambda )}}\right).$

- The diameter of a graph is the maximum distance between two vertices, where the distance between two vertices is defined to be the shortest path between them. Chung showed that the diameter of an (*n*, *d*, *λ*)-graph is at most

$\left\lceil \log {\frac {n}{\log(d/\lambda )}}\right\rceil .$

### Expander walk sampling

The Chernoff bound states that, when sampling many independent samples from a random variable in the range [−1, 1], with high probability the average of our samples is close to the expectation of the random variable. The expander walk sampling lemma, due to Ajtai, Komlós & Szemerédi (1987) and Gillman (1998), states that this also holds true when sampling from a walk on an expander graph. This is particularly useful in the theory of derandomization, since sampling according to an expander walk uses many fewer random bits than sampling independently.

### AKS sorting network and approximate halvers

Sorting networks take a set of inputs and perform a series of parallel steps to sort the inputs. A parallel step consists of performing any number of disjoint comparisons and potentially swapping pairs of compared inputs. The depth of a network is given by the number of parallel steps it takes. Expander graphs play an important role in the AKS sorting network, which achieves depth *O*(log *n*). While this is asymptotically the best known depth for a sorting network, the reliance on expanders makes the constant bound too large for practical use.

Within the AKS sorting network, expander graphs are used to construct bounded depth ε-halvers. An ε-halver takes as input a length n permutation of (1, …, *n*) and halves the inputs into two disjoint sets A and B such that for each integer *k* ≤ *n*⁄2 at most εk of the k smallest inputs are in B and at most εk of the k largest inputs are in A. The sets A and B are an ε-halving.

Following Ajtai, Komlós & Szemerédi (1983), a depth d ε-halver can be constructed as follows. Take an n vertex, degree d bipartite expander with parts X and Y of equal size such that every subset of vertices of size at most εn has at least ⁠1 – *ε*/*ε*⁠ neighbors.

The vertices of the graph can be thought of as registers that contain inputs and the edges can be thought of as wires that compare the inputs of two registers. At the start, arbitrarily place half of the inputs in X and half of the inputs in Y and decompose the edges into d perfect matchings. The goal is to end with X roughly containing the smaller half of the inputs and Y containing roughly the larger half of the inputs. To achieve this, sequentially process each matching by comparing the registers paired up by the edges of this matching and correct any inputs that are out of order. Specifically, for each edge of the matching, if the larger input is in the register in X and the smaller input is in the register in Y, then swap the two inputs so that the smaller one is in X and the larger one is in Y. It is clear that this process consists of d parallel steps.

After all d rounds, take A to be the set of inputs in registers in X and B to be the set of inputs in registers in Y to obtain an ε-halving. To see this, notice that if a register u in X and v in Y are connected by an edge uv then after the matching with this edge is processed, the input in u is less than that of v. Furthermore, this property remains true throughout the rest of the process. Now, suppose for some *k* ≤ *n*⁄2 that more than εk of the inputs (1, …, *k*) are in B. Then by expansion properties of the graph, the registers of these inputs in Y are connected with at least ⁠1 – *ε*/*ε*⁠*k* registers in X. Altogether, this constitutes more than k registers so there must be some register A in X connected to some register B in Y such that the final input of A is not in (1, …, *k*), while the final input of B is. This violates the previous property however, and thus the output sets A and B must be an ε-halving.
