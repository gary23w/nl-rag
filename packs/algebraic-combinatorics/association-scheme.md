---
title: "Association scheme"
source: https://en.wikipedia.org/wiki/Association_scheme
domain: algebraic-combinatorics
license: CC-BY-SA-4.0
tags: algebraic combinatorics, young tableau, symmetric function, association scheme
fetched: 2026-07-02
---

# Association scheme

The theory of **association schemes** arose in statistics, in the theory of experimental design for the analysis of variance. In mathematics, association schemes belong to both algebra and combinatorics. In algebraic combinatorics, association schemes provide a unified approach to many topics, for example combinatorial designs and the theory of error-correcting codes. In algebra, the theory of association schemes generalizes the character theory of linear representations of groups.

## Definition

An *n*-class association scheme consists of a set *X* together with a partition *S* of *X* × *X* into *n* + 1 binary relations, *R*0, *R*1, ..., *R**n* which satisfy:

- $R_{0}=\{(x,x):x\in X\}$ ; it is called the identity relation.
- Defining $R^{*}:=\{(x,y):(y,x)\in R\}$ , if *R* in *S*, then *R** in *S*.
- If $(x,y)\in R_{k}$ , the number of $z\in X$ such that $(x,z)\in R_{i}$ and $(z,y)\in R_{j}$ is a constant $p_{ij}^{k}$ depending on i , j , k but not on the particular choice of x and y .

An association scheme is *commutative* if $p_{ij}^{k}=p_{ji}^{k}$ for all i , j and k . Most authors assume this property. Note, however, that while the notion of an association scheme generalizes the notion of a group, the notion of a commutative association scheme only generalizes the notion of a commutative group.

A *symmetric* association scheme is one in which each $R_{i}$ is a symmetric relation. That is:

- if (*x*, *y*) ∈ *R**i*, then (*y*, *x*) ∈ *R**i*. (Or equivalently, *R** = *R*.)

Every symmetric association scheme is commutative.

Two points *x* and *y* are called *i*th associates if $(x,y)\in R_{i}$ . The definition states that if *x* and *y* are *i*th associates then so are *y* and *x*. Every pair of points are *i*th associates for exactly one i . Each point is its own zeroth associate while distinct points are never zeroth associates. If *x* and *y* are *k*th associates then the number of points z which are both *i*th associates of x and *j*th associates of y is a constant $p_{ij}^{k}$ .

### Graph interpretation and adjacency matrices

A symmetric association scheme can be visualized as a complete graph with labeled edges. The graph has v vertices, one for each point of X , and the edge joining vertices x and y is labeled i if x and y are i th associates. Each edge has a unique label, and the number of triangles with a fixed base labeled k having the other edges labeled i and j is a constant $p_{ij}^{k}$ , depending on $i,j,k$ but not on the choice of the base. In particular, each vertex is incident with exactly $p_{ii}^{0}=v_{i}$ edges labeled i ; $v_{i}$ is the valency of the relation $R_{i}$ . There are also loops labeled 0 at each vertex x , corresponding to $R_{0}$ .

The relations are described by their adjacency matrices. $A_{i}$ is the adjacency matrix of $R_{i}$ for $i=0,\ldots ,n$ and is a *v* × *v* matrix with rows and columns labeled by the points of X .

$\left(A_{i}\right)_{x,y}={\begin{cases}1,&{\mbox{if }}(x,y)\in R_{i},\\0,&{\mbox{otherwise.}}\end{cases}}\qquad (1)$

The definition of a symmetric association scheme is equivalent to saying that the $A_{i}$ are *v* × *v* (0,1)-matrices which satisfy

I.

$A_{i}$

is symmetric,

II.

$\sum _{i=0}^{n}A_{i}=J$

(the all-ones matrix),

III.

$A_{0}=I$

,

IV.

$A_{i}A_{j}=\sum _{k=0}^{n}p_{ij}^{k}A_{k}=A_{j}A_{i},i,j=0,\ldots ,n$

.

The (*x*, *y*)-th entry of the left side of (IV) is the number of paths of length two between *x* and *y* with labels *i* and *j* in the graph. Note that the rows and columns of $A_{i}$ contain $v_{i}$ 1 's:

$A_{i}J=JA_{i}=v_{i}J.\qquad (2)$

### Terminology

- The numbers $p_{ij}^{k}$ are called the *parameters* of the scheme. They are also referred to as the *structural constants*.

## History

The term *association scheme* is due to (Bose & Shimamoto 1952) but the concept is already inherent in (Bose & Nair 1939). These authors were studying what statisticians have called *partially balanced incomplete block designs* (PBIBDs). The subject became an object of algebraic interest with the publication of (Bose & Mesner 1959) and the introduction of the Bose–Mesner algebra. The most important contribution to the theory was the thesis of Ph. Delsarte (Delsarte 1973) who recognized and fully used the connections with coding theory and design theory.

A generalization called coherent configurations has been studied by D. G. Higman.

## Basic facts

- $p_{00}^{0}=1$ , i.e., if $(x,y)\in R_{0}$ then $x=y$ and the only z such that $(x,z)\in R_{0}$ is $z=x$ .
- $\sum _{i=0}^{k}p_{ii}^{0}=|X|$ ; this is because the $R_{i}$ partition X .

## The Bose–Mesner algebra

The adjacency matrices $A_{i}$ of the graphs $\left(X,R_{i}\right)$ generate a commutative and associative algebra ${\mathcal {A}}$ (over the real or complex numbers) both for the matrix product and the Hadamard (entrywise) product. The algebra formed with the matrix product is called the Bose–Mesner algebra of the association scheme.

Since the matrices in ${\mathcal {A}}$ are symmetric and commute with each other, they can be diagonalized simultaneously. Therefore, ${\mathcal {A}}$ is semi-simple and has a unique basis of primitive idempotents $J_{0},\ldots ,J_{n}$ .

There is another algebra of $(n+1)\times (n+1)$ matrices which is isomorphic to ${\mathcal {A}}$ , and is often easier to work with.

## Examples

- The Johnson scheme, denoted by *J*(*v*, *k*), is defined as follows. Let *S* be a set with *v* elements. The points of the scheme *J*(*v*, *k*) are the ${v \choose k}$ subsets of S with *k* elements. Two *k*-element subsets *A*, *B* of *S* are *i*th associates when their intersection has size *k* − *i*.
- The Hamming scheme, denoted by *H*(*n*, *q*), is defined as follows. The points of *H*(*n*, *q*) are the *qn* ordered *n*-tuples over a set of size *q*. Two *n*-tuples *x*, *y* are said to be *i*th associates if they disagree in exactly *i* coordinates. E.g., if *x* = (1,0,1,1), *y* = (1,1,1,1), *z* = (0,0,1,1), then *x* and *y* are 1st associates, *x* and *z* are 1st associates and *y* and *z* are 2nd associates in *H*(4,2).
- A distance-regular graph, *G*, forms an association scheme by defining two vertices to be *i*th associates if their distance is *i*.
- A finite group *G* yields an association scheme on $X=G$ , with a class *R**g* for each group element, as follows: for each $g\in G$ let $R_{g}=\{(x,y)\mid x=g*y\}$ where * is the group operation. The class of the group identity is *R*0. This association scheme is commutative if and only if *G* is abelian.
- A specific 3-class association scheme:

Let

A

(3) be the following association scheme with three associate classes on the set

X

= {1,2,3,4,5,6}. The (

i

,

j

) entry is

s

if elements

i

and

j

are in relation

R

s

.

|   | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| **1** | 0 | 1 | 1 | 2 | 3 | 3 |
| **2** | 1 | 0 | 1 | 3 | 2 | 3 |
| **3** | 1 | 1 | 0 | 3 | 3 | 2 |
| **4** | 2 | 3 | 3 | 0 | 1 | 1 |
| **5** | 3 | 2 | 3 | 1 | 0 | 1 |
| **6** | 3 | 3 | 2 | 1 | 1 | 0 |

## Coding theory

The Hamming scheme and the Johnson scheme are of major significance in classical coding theory.

In coding theory, association scheme theory is mainly concerned with the distance of a code. The linear programming method produces upper bounds for the size of a code with given minimum distance, and lower bounds for the size of a design with a given strength. The most specific results are obtained in the case where the underlying association scheme satisfies certain polynomial properties; this leads one into the realm of orthogonal polynomials. In particular, some universal bounds are derived for codes and designs in polynomial-type association schemes.

In classical coding theory, dealing with codes in a Hamming scheme, the MacWilliams transform involves a family of orthogonal polynomials known as the Krawtchouk polynomials. These polynomials give the eigenvalues of the distance relation matrices of the Hamming scheme.
