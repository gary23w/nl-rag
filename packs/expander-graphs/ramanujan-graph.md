---
title: "Ramanujan graph"
source: https://en.wikipedia.org/wiki/Ramanujan_graph
domain: expander-graphs
license: CC-BY-SA-4.0
tags: expander graph, spectral gap, cheeger inequality, ramanujan graph
fetched: 2026-07-02
---

# Ramanujan graph

In the mathematical field of spectral graph theory, a **Ramanujan graph** is a regular graph whose spectral gap is almost as large as possible (see extremal graph theory). Such graphs are excellent spectral expanders. As Murty's survey paper notes, Ramanujan graphs "fuse diverse branches of pure mathematics, namely, number theory, representation theory, and algebraic geometry". These graphs are indirectly named after Srinivasa Ramanujan; their name comes from the Ramanujan–Petersson conjecture, which was used in a construction of some of these graphs.

## Definition

Let G be a connected d -regular graph with n vertices, and let $\lambda _{1}\geq \lambda _{2}\geq \cdots \geq \lambda _{n}$ be the eigenvalues of the adjacency matrix of G (or the spectrum of G ). Because G is connected and d -regular, its eigenvalues satisfy $d=\lambda _{1}>\lambda _{2}$ $\geq \cdots \geq \lambda _{n}\geq -d$ .

Define $\lambda (G)=\max _{i\neq 1}|\lambda _{i}|=\max(|\lambda _{2}|,\ldots ,|\lambda _{n}|)$ . A connected d -regular graph G is a *Ramanujan graph* if $\lambda (G)\leq 2{\sqrt {d-1}}$ .

Many sources uses an alternative definition $\lambda '(G)=\max _{|\lambda _{i}|<d}|\lambda _{i}|$ (whenever there exists $\lambda _{i}$ with $|\lambda _{i}|<d$ ) to define Ramanujan graphs. In other words, we allow $-d$ in addition to the "small" eigenvalues. Since $\lambda _{n}=-d$ if and only if the graph is bipartite, we will refer to the graphs that satisfy this alternative definition but not the first definition as *bipartite Ramanujan graphs*. If G is a Ramanujan graph, then $G\times K_{2}$ is a bipartite Ramanujan graph, so the existence of Ramanujan graphs is stronger.

As observed by Toshikazu Sunada, a regular graph is Ramanujan if and only if its Ihara zeta function satisfies an analog of the Riemann hypothesis.

## Examples and constructions

### Explicit examples

- The complete graph $K_{d+1}$ has spectrum $d,-1,-1,\dots ,-1$ , and thus $\lambda (K_{d+1})=1$ and the graph is a Ramanujan graph for every $d>1$ . The complete bipartite graph $K_{d,d}$ has spectrum $d,0,0,\dots ,0,-d$ and hence is a bipartite Ramanujan graph for every d .
- The Petersen graph has spectrum $3,1,1,1,1,1,-2,-2,-2,-2$ , so it is a 3-regular Ramanujan graph. The icosahedral graph is a 5-regular Ramanujan graph.
- A Paley graph of order q is ${\frac {q-1}{2}}$ -regular with all other eigenvalues being ${\frac {-1\pm {\sqrt {q}}}{2}}$ , making Paley graphs an infinite family of Ramanujan graphs.
- More generally, let $f(x)$ be a degree 2 or 3 polynomial over $\mathbb {F} _{q}$ . Let $S=\{f(x)\,:\,x\in \mathbb {F} _{q}\}$ be the image of $f(x)$ as a multiset, and suppose $S=-S$ . Then the Cayley graph for $\mathbb {F} _{q}$ with generators from S is a Ramanujan graph.

Mathematicians are often interested in constructing infinite families of d -regular Ramanujan graphs for every fixed d . Such families are useful in applications.

### Algebraic constructions

Several explicit constructions of Ramanujan graphs arise as Cayley graphs and are algebraic in nature. See Winnie Li's survey on Ramanujan's conjecture and other aspects of number theory relevant to these results.

Lubotzky, Phillips and Sarnak and independently Margulis showed how to construct an infinite family of $(p+1)$ -regular Ramanujan graphs, whenever p is a prime number and $p\equiv 1{\pmod {4}}$ . Both proofs use the Ramanujan conjecture, which led to the name of Ramanujan graphs. Besides being Ramanujan graphs, these constructions satisfies some other properties, for example, their girth is $\Omega (\log _{p}(n))$ where n is the number of nodes.

Let us sketch the Lubotzky-Phillips-Sarnak construction. Let $q\equiv 1{\bmod {4}}$ be a prime not equal to p . By Jacobi's four-square theorem, there are $p+1$ solutions to the equation $p=a_{0}^{2}+a_{1}^{2}+a_{2}^{2}+a_{3}^{2}$ where $a_{0}>0$ is odd and $a_{1},a_{2},a_{3}$ are even. To each such solution associate the $\operatorname {PGL} (2,\mathbb {Z} /q\mathbb {Z} )$ matrix ${\tilde {\alpha }}={\begin{pmatrix}a_{0}+ia_{1}&a_{2}+ia_{3}\\-a_{2}+ia_{3}&a_{0}-ia_{1}\end{pmatrix}},\qquad i{\text{ a fixed solution to }}i^{2}=-1{\bmod {q}}.$ If p is not a quadratic residue modulo q let $X^{p,q}$ be the Cayley graph of $\operatorname {PGL} (2,\mathbb {Z} /q\mathbb {Z} )$ with these $p+1$ generators, and otherwise, let $X^{p,q}$ be the Cayley graph of $\operatorname {PSL} (2,\mathbb {Z} /q\mathbb {Z} )$ with the same generators. Then $X^{p,q}$ is a $(p+1)$ -regular graph on $n=q(q^{2}-1)$ or $q(q^{2}-1)/2$ vertices depending on whether or not p is a quadratic residue modulo q . It is proved that $X^{p,q}$ is a Ramanujan graph.

Morgenstern later extended the construction of Lubotzky, Phillips and Sarnak. His extended construction holds whenever p is a prime power.

Arnold Pizer proved that the supersingular isogeny graphs are Ramanujan, although they tend to have lower girth than the graphs of Lubotzky, Phillips, and Sarnak. Like the graphs of Lubotzky, Phillips, and Sarnak, the degrees of these graphs are always a prime number plus one.

### Probabilistic examples

Adam Marcus, Daniel Spielman and Nikhil Srivastava proved the existence of infinitely many d -regular *bipartite* Ramanujan graphs for any $d\geq 3$ . Later they proved that there exist bipartite Ramanujan graphs of every degree and every number of vertices. Michael B. Cohen showed how to construct these graphs in polynomial time.

The initial work followed an approach of Bilu and Linial. They considered an operation called a 2-lift that takes a d -regular graph G with n vertices and a sign on each edge, and produces a new d -regular graph $G'$ on $2n$ vertices. Bilu & Linial conjectured that there always exists a signing so that every new eigenvalue of $G'$ has magnitude at most $2{\sqrt {d-1}}$ . This conjecture guarantees the existence of Ramanujan graphs with degree d and $2^{k}(d+1)$ vertices for any k —simply start with the complete graph $K_{d+1}$ , and iteratively take 2-lifts that retain the Ramanujan property.

Using the method of interlacing polynomials, Marcus, Spielman, and Srivastava proved Bilu & Linial's conjecture holds when G is already a bipartite Ramanujan graph, which is enough to conclude the existence result. The sequel proved the stronger statement that a sum of d random bipartite matchings is Ramanujan with non-vanishing probability. Hall, Puder and Sawin extended the original work of Marcus, Spielman and Srivastava to r-lifts.

It is still an open problem whether there are infinitely many d -regular (non-bipartite) Ramanujan graphs for any $d\geq 3$ . In particular, the problem is open for $d=7$ , the smallest case for which $d-1$ is not a prime power and hence not covered by Morgenstern's construction.

## Ramanujan graphs as expander graphs

The constant $2{\sqrt {d-1}}$ in the definition of Ramanujan graphs is asymptotically sharp. More precisely, the Alon-Boppana bound states that for every d and $\epsilon >0$ , there exists n such that all d -regular graphs G with at least n vertices satisfy $\lambda (G)>2{\sqrt {d-1}}-\epsilon$ . This means that Ramanujan graphs are essentially the best possible expander graphs.

Due to achieving the tight bound on $\lambda (G)$ , the expander mixing lemma gives excellent bounds on the uniformity of the distribution of the edges in Ramanujan graphs, and any random walks on the graphs has a logarithmic mixing time (in terms of the number of vertices): in other words, the random walk converges to the (uniform) stationary distribution very quickly. Therefore, the diameter of Ramanujan graphs are also bounded logarithmically in terms of the number of vertices.

### Random graphs

Confirming a conjecture of Alon, Friedman showed that many families of random graphs are *weakly-Ramanujan*. This means that for every d and $\epsilon >0$ and for sufficiently large n , a random d -regular n -vertex graph G satisfies $\lambda (G)<2{\sqrt {d-1}}+\epsilon$ with high probability. While this result shows that random graphs are close to being Ramanujan, it cannot be used to prove the existence of Ramanujan graphs. It is conjectured, though, that random graphs are Ramanujan with substantial probability (roughly 52%). In addition to direct numerical evidence, there is some theoretical support for this conjecture: the spectral gap of a d -regular graph seems to behave according to a Tracy-Widom distribution from random matrix theory, which would predict the same asymptotic.

In 2024 a preprint by Jiaoyang Huang, Theo McKenzie and Horng-Tzer Yau proved that $\lambda (G)\leq 2{\sqrt {d-1}}$ with the fraction of eigenvalues that hit the Alon-Boppana bound approximately 69% from proving that edge universality holds, that is they follow a Tracy-Widom distribution associated with the Gaussian Orthogonal Ensemble

## Applications of Ramanujan graphs

Expander graphs have many applications to computer science, number theory, and group theory, see e.g Lubotzky's survey on applications to pure and applied math and Hoory, Linial, and Wigderson's survey which focuses on computer science. Ramanujan graphs are in some sense the best expanders, and so they are especially useful in applications where expanders are needed. Importantly, the Lubotzky, Phillips, and Sarnak graphs can be traversed extremely quickly in practice, so they are practical for applications.

Some example applications include

- In an application to fast solvers for Laplacian linear systems, Lee, Peng, and Spielman relied on the existence of bipartite Ramanujan graphs of every degree in order to quickly approximate the complete graph.
- Lubetzky and Peres proved that the simple random walk exhibits cutoff phenomenon on all Ramanujan graphs. This means that the random walk undergoes a phase transition from being completely unmixed to completely mixed in the total variation norm. This result strongly relies on the graph being Ramanujan, not just an expander—some good expanders are known to not exhibit cutoff.
- Ramanujan graphs of Pizer have been proposed as the basis for post-quantum elliptic-curve cryptography.
- Ramanujan graphs can be used to construct expander codes, which are good error correcting codes.
