---
title: "Permanent (mathematics)"
source: https://en.wikipedia.org/wiki/Permanent_(mathematics)
domain: counting-complexity
license: CC-BY-SA-4.0
tags: counting complexity, permanent computation, toda theorem, counting problem
fetched: 2026-07-02
---

# Permanent (mathematics)

In linear algebra, the **permanent** of a square matrix is a function of the matrix similar to the determinant. The permanent, as well as the determinant, is a polynomial in the entries of the matrix. Both are special cases of a more general function of a matrix called the immanant.

## Definition

The permanent of an *n*×*n* matrix *A* = (*a**i*,*j*) is defined as

$\operatorname {perm} (A)=\sum _{\sigma \in S_{n}}\prod _{i=1}^{n}a_{i,\sigma (i)}.$

The sum here extends over all elements *σ* of the symmetric group *S**n*; i.e., over all permutations of the numbers 1, 2, ..., *n*.

For example,

$\operatorname {perm} {\begin{pmatrix}a&b\\c&d\end{pmatrix}}=ad+bc,$

and

$\operatorname {perm} {\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix}}=aei+bfg+cdh+ceg+bdi+afh.$

The definition of the permanent of *A* differs from that of the determinant of *A* in that the signatures of the permutations are not taken into account.

The permanent of a matrix A is denoted per *A*, perm *A*, or Per *A*, sometimes with parentheses around the argument. Minc uses Per(*A*) for the permanent of rectangular matrices, and per(*A*) when *A* is a square matrix. Muir and Metzler use the notation ${\overset {+}{|}}\quad {\overset {+}{|}}$ .

The word, *permanent*, originated with Cauchy in 1812 as "fonctions symétriques permanentes" for a related type of function, and was used by Muir and Metzler in the modern, more specific, sense.

## Properties

If one views the permanent as a map that takes *n* vectors as arguments, then it is a multilinear map and it is symmetric (meaning that any order of the vectors results in the same permanent). Furthermore, given a square matrix $A=\left(a_{ij}\right)$ of order *n*:

- perm(*A*) is invariant under arbitrary permutations of the rows and/or columns of *A*. This property may be written symbolically as perm(*A*) = perm(*PAQ*) for any appropriately sized permutation matrices *P* and *Q*,
- multiplying any single row or column of *A* by a scalar *λ* changes perm(*A*) to *λ*⋅perm(*A*),
- perm(*A*) is invariant under transposition, that is, perm(*A*) = perm(*A*T).
- If $A=\left(a_{ij}\right)$ and $B=\left(b_{ij}\right)$ are square matrices of order *n*, then $\operatorname {perm} \left(A+B\right)=\sum _{s,t}\operatorname {perm} \left(a_{ij}\right)_{i\in s,j\in t}\operatorname {perm} \left(b_{ij}\right)_{i\in {\bar {s}},j\in {\bar {t}}},$ where *s* and *t* are subsets of the same size of {1, 2, ..., *n*} and ${\bar {s}},{\bar {t}}$ are their respective complements in that set.
- If A is a triangular matrix, i.e., $a_{ij}=0$ whenever $i>j$ or, alternatively, whenever $i<j$ , then its permanent equals the product of the diagonal entries: $\operatorname {perm} \left(A\right)=a_{11}a_{22}\cdots a_{nn}=\prod _{i=1}^{n}a_{ii}.$

## Comparison to determinants

Laplace's expansion by minors for computing the determinant along a row, column or diagonal extends to the permanent by ignoring all signs.

For every ${\textstyle i}$ ,

$\mathbb {perm} (B)=\sum _{j=1}^{n}B_{i,j}M_{i,j},$

where $B_{i,j}$ is the entry of the *i*th row and the *j*th column of *B*, and ${\textstyle M_{i,j}}$ is the permanent of the submatrix obtained by removing the *i*th row and the *j*th column of *B*.

For example, expanding along the first column,

${\begin{aligned}\operatorname {perm} \left({\begin{matrix}1&1&1&1\\2&1&0&0\\3&0&1&0\\4&0&0&1\end{matrix}}\right)={}&1\cdot \operatorname {perm} \left({\begin{matrix}1&0&0\\0&1&0\\0&0&1\end{matrix}}\right)+2\cdot \operatorname {perm} \left({\begin{matrix}1&1&1\\0&1&0\\0&0&1\end{matrix}}\right)\\&{}+\ 3\cdot \operatorname {perm} \left({\begin{matrix}1&1&1\\1&0&0\\0&0&1\end{matrix}}\right)+4\cdot \operatorname {perm} \left({\begin{matrix}1&1&1\\1&0&0\\0&1&0\end{matrix}}\right)\\={}&1(1)+2(1)+3(1)+4(1)=10,\end{aligned}}$

while expanding along the last row gives,

${\begin{aligned}\operatorname {perm} \left({\begin{matrix}1&1&1&1\\2&1&0&0\\3&0&1&0\\4&0&0&1\end{matrix}}\right)={}&4\cdot \operatorname {perm} \left({\begin{matrix}1&1&1\\1&0&0\\0&1&0\end{matrix}}\right)+0\cdot \operatorname {perm} \left({\begin{matrix}1&1&1\\2&0&0\\3&1&0\end{matrix}}\right)\\&{}+\ 0\cdot \operatorname {perm} \left({\begin{matrix}1&1&1\\2&1&0\\3&0&0\end{matrix}}\right)+1\cdot \operatorname {perm} \left({\begin{matrix}1&1&1\\2&1&0\\3&0&1\end{matrix}}\right)\\={}&4(1)+0+0+1(6)=10.\end{aligned}}$

On the other hand, the basic multiplicative property of determinants is not valid for permanents. A simple example shows that this is so.

${\begin{aligned}4&=\operatorname {perm} \left({\begin{matrix}1&1\\1&1\end{matrix}}\right)\operatorname {perm} \left({\begin{matrix}1&1\\1&1\end{matrix}}\right)\\&\neq \operatorname {perm} \left(\left({\begin{matrix}1&1\\1&1\end{matrix}}\right)\left({\begin{matrix}1&1\\1&1\end{matrix}}\right)\right)=\operatorname {perm} \left({\begin{matrix}2&2\\2&2\end{matrix}}\right)=8.\end{aligned}}$

Unlike the determinant, the permanent has no easy geometrical interpretation; it is mainly used in combinatorics, in treating boson Green's functions in quantum field theory, and in determining state probabilities of boson sampling systems. However, it has two graph-theoretic interpretations: as the sum of weights of cycle covers of a directed graph, and as the sum of weights of perfect matchings in a bipartite graph.

## Applications

### Symmetric tensors

The permanent arises naturally in the study of the symmetric tensor power of Hilbert spaces. In particular, for a Hilbert space H , let $\vee ^{k}H$ denote the k th symmetric tensor power of H , which is the space of symmetric tensors. Note in particular that $\vee ^{k}H$ is spanned by the symmetric products of elements in H . For $x_{1},x_{2},\dots ,x_{k}\in H$ , we define the symmetric product of these elements by $x_{1}\vee x_{2}\vee \cdots \vee x_{k}=(k!)^{-1/2}\sum _{\sigma \in S_{k}}x_{\sigma (1)}\otimes x_{\sigma (2)}\otimes \cdots \otimes x_{\sigma (k)}$ If we consider $\vee ^{k}H$ (as a subspace of $\otimes ^{k}H$ , the *k*th tensor power of H ) and define the inner product on $\vee ^{k}H$ accordingly, we find that for $x_{j},y_{j}\in H$ $\langle x_{1}\vee x_{2}\vee \cdots \vee x_{k},y_{1}\vee y_{2}\vee \cdots \vee y_{k}\rangle =\operatorname {perm} \left[\langle x_{i},y_{j}\rangle \right]_{i,j=1}^{k}$ Applying the Cauchy–Schwarz inequality, we find that $\operatorname {perm} \left[\langle x_{i},x_{j}\rangle \right]_{i,j=1}^{k}\geq 0$ , and that $\left|\operatorname {perm} \left[\langle x_{i},y_{j}\rangle \right]_{i,j=1}^{k}\right|^{2}\leq \operatorname {perm} \left[\langle x_{i},x_{j}\rangle \right]_{i,j=1}^{k}\cdot \operatorname {perm} \left[\langle y_{i},y_{j}\rangle \right]_{i,j=1}^{k}$

### Cycle covers

Any square matrix $A=(a_{ij})_{i,j=1}^{n}$ can be viewed as the adjacency matrix of a weighted directed graph on vertex set $V=\{1,2,\dots ,n\}$ , with $a_{ij}$ representing the weight of the arc from vertex *i* to vertex *j*. A cycle cover of a weighted directed graph is a collection of vertex-disjoint directed cycles in the digraph that covers all vertices in the graph. Thus, each vertex *i* in the digraph has a unique "successor" $\sigma (i)$ in the cycle cover, and so $\sigma$ represents a permutation on *V*. Conversely, any permutation $\sigma$ on *V* corresponds to a cycle cover with arcs from each vertex *i* to vertex $\sigma (i)$ .

If the weight of a cycle-cover is defined to be the product of the weights of the arcs in each cycle, then $\operatorname {weight} (\sigma )=\prod _{i=1}^{n}a_{i,\sigma (i)},$ implying that $\operatorname {perm} (A)=\sum _{\sigma }\operatorname {weight} (\sigma ).$ Thus the permanent of *A* is equal to the sum of the weights of all cycle-covers of the digraph.

### Perfect matchings

A square matrix $A=(a_{ij})$ can also be viewed as the adjacency matrix of a bipartite graph which has vertices $x_{1},x_{2},\dots ,x_{n}$ on one side and $y_{1},y_{2},\dots ,y_{n}$ on the other side, with $a_{ij}$ representing the weight of the edge from vertex $x_{i}$ to vertex $y_{j}$ . If the weight of a perfect matching $\sigma$ that matches $x_{i}$ to $y_{\sigma (i)}$ is defined to be the product of the weights of the edges in the matching, then $\operatorname {weight} (\sigma )=\prod _{i=1}^{n}a_{i,\sigma (i)}.$ Thus the permanent of *A* is equal to the sum of the weights of all perfect matchings of the graph.

## Permanents of (0, 1) matrices

### Enumeration

The answers to many counting questions can be computed as permanents of matrices that only have 0 and 1 as entries.

Let Ω(*n*, *k*) be the class of all (0, 1)-matrices of order *n* with each row and column sum equal to *k*. Every matrix *A* in this class has perm(*A*) > 0. The incidence matrices every finite projective plane is in the class Ω(*n*2 + *n* + 1, *n* + 1) for some integer *n* > 1. The permanents corresponding to the smallest projective planes have been calculated. For *n* = 2, 3, and 4 the values are 24, 3852 and 18,534,400, respectively. Let *Z* be the incidence matrix of the projective plane with *n* = 2, the Fano plane. Remarkably, perm(*Z*) = 24 = |det (*Z*)|, the absolute value of the determinant of *Z*. This is a consequence of *Z* being a circulant matrix, as well as the theorem:

If

A

is a circulant matrix in the class Ω(

n

,

k

) then if

k

>

3, perm(

A

)

>

|det (

A

)| and if

k

=

3, perm(

A

)

=

|det (

A

)|. Furthermore, when

k

=

3, by permuting rows and columns,

A

can be put into the form of a direct sum of

e

copies of the matrix

Z

and consequently,

n

=

7

e

and perm(

A

)

=

24

e

.

Permanents can also be used to calculate the number of permutations with restricted (prohibited) positions. For the standard *n*-set {1, 2, ..., *n*}, let $A=(a_{ij})$ be the (0, 1)-matrix where *a**ij* = 1 if *i* → *j* is allowed in a permutation and *a**ij* = 0 otherwise. Then perm(*A*) is equal to the number of permutations of the *n*-set that satisfy all the restrictions. Two well known special cases of this are the solution of the derangement problem and the ménage problem: the number of permutations of an *n*-set with no fixed points (derangements) is given by $\operatorname {perm} (J-I)=\operatorname {perm} \left({\begin{matrix}0&1&1&\dots &1\\1&0&1&\dots &1\\1&1&0&\dots &1\\\vdots &\vdots &\vdots &\ddots &\vdots \\1&1&1&\dots &0\end{matrix}}\right)=n!\sum _{i=0}^{n}{\frac {(-1)^{i}}{i!}},$ where *J* is the *n*×*n* all 1's matrix and *I* is the identity matrix, and the ménage numbers are given by ${\begin{aligned}\operatorname {perm} (J-I-I')&=\operatorname {perm} \left({\begin{matrix}0&0&1&\dots &1\\1&0&0&\dots &1\\1&1&0&\dots &1\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&1&1&\dots &0\end{matrix}}\right)\\&=\sum _{k=0}^{n}(-1)^{k}{\frac {2n}{2n-k}}{2n-k \choose k}(n-k)!,\end{aligned}}$ where *I'* is the (0, 1)-matrix with nonzero entries in positions (*i*, *i* + 1) and (*n*, 1).

For an *n*×*n* (0, 1)-matrix, the permanent may be equivalently described as the number of ways of placing *n* mutually non-attacking rooks on the *n*×*n* chessboard so that no rook is at a position where the matrix has a 0 entry. (These numbers arise in combinatorics as leading coefficients of rook polynomials.)

### Bounds

The Bregman–Minc inequality, conjectured by H. Minc in 1963 and proved by L. M. Brégman in 1973, gives an upper bound for the permanent of an *n* × *n* (0, 1)-matrix. If *A* has *r**i* ones in row *i* for each 1 ≤ *i* ≤ *n*, the inequality states that $\operatorname {perm} A\leq \prod _{i=1}^{n}(r_{i})!^{1/r_{i}}.$

## Van der Waerden's conjecture

In 1926, Van der Waerden conjectured that the minimum permanent among all *n* × *n* doubly stochastic matrices is *n*!/*n**n*, achieved by the matrix for which all entries are equal to 1/*n*. Proofs of this conjecture were published in 1980 by B. Gyires and in 1981 by G. P. Egorychev and D. I. Falikman. Egorychev's proof is an application of the Alexandrov–Fenchel inequality. For this work, Egorychev and Falikman won the Fulkerson Prize in 1982.

## Computation

The naïve approach, using the definition, of computing permanents is computationally infeasible even for relatively small matrices. One of the fastest known algorithms is due to H. J. Ryser. Ryser's method is based on an inclusion–exclusion formula that can be given as follows: Let $A_{k}$ be obtained from *A* by deleting *k* columns, let $P(A_{k})$ be the product of the row-sums of $A_{k}$ , and let $\Sigma _{k}$ be the sum of the values of $P(A_{k})$ over all possible $A_{k}$ . Then $\operatorname {perm} (A)=\sum _{k=0}^{n-1}(-1)^{k}\Sigma _{k}.$

It may be rewritten in terms of the matrix entries as follows: $\operatorname {perm} (A)=(-1)^{n}\sum _{S\subseteq \{1,\dots ,n\}}(-1)^{|S|}\prod _{i=1}^{n}\sum _{j\in S}a_{ij}.$

The permanent is believed to be more difficult to compute than the determinant. While the determinant can be computed in polynomial time by Gaussian elimination, Gaussian elimination cannot be used to compute the permanent. Moreover, computing the permanent of a (0,1)-matrix is #P-complete. Thus, if the permanent can be computed in polynomial time by any method, then **FP = #P**, which is an even stronger statement than P = NP. When the entries of *A* are nonnegative, however, the permanent can be computed approximately in probabilistic polynomial time, up to an error of $\varepsilon M$ , where M is the value of the permanent and $\varepsilon >0$ is arbitrary. The permanent of a certain set of positive semidefinite matrices is NP-hard to approximate within any subexponential factor. If further conditions on the spectrum are imposed, the permanent can be approximated in probabilistic polynomial time: the best achievable error of this approximation is $\varepsilon {\sqrt {M}}$ ( M is again the value of the permanent). The hardness in these instances is closely linked with difficulty of simulating boson sampling experiments.

## MacMahon's master theorem

Another way to view permanents is via multivariate generating functions. Let $A=(a_{ij})$ be a square matrix of order *n*. Consider the multivariate generating function: ${\begin{aligned}F(x_{1},x_{2},\dots ,x_{n})&=\prod _{i=1}^{n}\left(\sum _{j=1}^{n}a_{ij}x_{j}\right)\\&=\left(\sum _{j=1}^{n}a_{1j}x_{j}\right)\left(\sum _{j=1}^{n}a_{2j}x_{j}\right)\cdots \left(\sum _{j=1}^{n}a_{nj}x_{j}\right).\end{aligned}}$ The coefficient of $x_{1}x_{2}\dots x_{n}$ in $F(x_{1},x_{2},\dots ,x_{n})$ is perm(*A*).

As a generalization, for any sequence of *n* non-negative integers, $s_{1},s_{2},\dots ,s_{n}$ define: $\operatorname {perm} ^{(s_{1},s_{2},\dots ,s_{n})}(A)$ as the coefficient of $x_{1}^{s_{1}}x_{2}^{s_{2}}\cdots x_{n}^{s_{n}}$ in $\left(\sum _{j=1}^{n}a_{1j}x_{j}\right)^{s_{1}}\left(\sum _{j=1}^{n}a_{2j}x_{j}\right)^{s_{2}}\cdots \left(\sum _{j=1}^{n}a_{nj}x_{j}\right)^{s_{n}}.$

**MacMahon's master theorem** relating permanents and determinants is: $\operatorname {perm} ^{(s_{1},s_{2},\dots ,s_{n})}(A)={\text{ coefficient of }}x_{1}^{s_{1}}x_{2}^{s_{2}}\cdots x_{n}^{s_{n}}{\text{ in }}{\frac {1}{\det(I-XA)}},$ where *I* is the order *n* identity matrix and *X* is the diagonal matrix with diagonal $[x_{1},x_{2},\dots ,x_{n}].$

## Rectangular matrices

The permanent function can be generalized to apply to non-square matrices. Indeed, several authors make this the definition of a permanent and consider the restriction to square matrices a special case. Specifically, for an *m* × *n* matrix $A=(a_{ij})$ with *m* ≤ *n*, define $\operatorname {perm} (A)=\sum _{\sigma \in \operatorname {P} (n,m)}a_{1\sigma (1)}a_{2\sigma (2)}\ldots a_{m\sigma (m)},$ where P(*n*,*m*) is the set of all *m*-permutations of the *n*-set {1,2,...,n}.

Ryser's computational result for permanents also generalizes. If *A* is an *m* × *n* matrix with *m* ≤ *n*, let $A_{k}$ be obtained from *A* by deleting *k* columns, let $P(A_{k})$ be the product of the row-sums of $A_{k}$ , and let $\sigma _{k}$ be the sum of the values of $P(A_{k})$ over all possible $A_{k}$ . Then $\operatorname {perm} (A)=\sum _{k=0}^{m-1}(-1)^{k}{\binom {n-m+k}{k}}\sigma _{n-m+k}.$

### Systems of distinct representatives

The generalization of the definition of a permanent to non-square matrices allows the concept to be used in a more natural way in some applications. For instance:

Let *S*1, *S*2, ..., *S**m* be subsets (not necessarily distinct) of an *n*-set with *m* ≤ *n*. The incidence matrix of this collection of subsets is an *m* × *n* (0,1)-matrix *A*. The number of systems of distinct representatives (SDR's) of this collection is perm(*A*).
