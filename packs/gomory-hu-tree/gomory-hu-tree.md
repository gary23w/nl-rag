---
title: "Gomory–Hu tree"
source: https://en.wikipedia.org/wiki/Gomory–Hu_tree
domain: gomory-hu-tree
license: CC-BY-SA-4.0
tags: gomory hu tree, all pairs min cut, cut tree, flow equivalent tree
fetched: 2026-07-02
---

# Gomory–Hu tree

In combinatorial optimization, the **Gomory–Hu tree** of an undirected graph with capacities is a weighted tree that represents the minimum *s*-*t* cuts for all *s*-*t* pairs in the graph. The Gomory–Hu tree can be constructed in |*V*| − 1 maximum flow computations. It is named for Ralph E. Gomory and T. C. Hu.

## Definition

Let $G=(V_{G},E_{G},c)$ be an undirected graph with $c(u,v)$ being the capacity of the edge $(u,v)$ respectively.

Denote the minimum capacity of an

s

-

t

cut by

$\lambda _{st}$

for each

$s,t\in V_{G}$

.

Let

$T=(V_{G},E_{T})$

be a tree, and denote the set of edges in an

s

-

t

path by

$P_{st}$

for each

$s,t\in V_{G}$

.

Then T is said to be a **Gomory–Hu tree** of G, if for each $s,t\in V_{G}$

$\lambda _{st}=\min _{e\in P_{st}}c(S_{e},T_{e}),$

where

1. $S_{e},T_{e}\subseteq V_{G}$ are the two connected components of $T\setminus \{e\}$ , and thus $(S_{e},T_{e})$ forms an s-t cut in G.
2. $c(S_{e},T_{e})$ is the capacity of the $(S_{e},T_{e})$ cut in G.

## Algorithm

**Gomory–Hu Algorithm**

Input

: A weighted undirected graph

$G=((V_{G},E_{G}),c)$

Output

: A Gomory–Hu Tree

$T=(V_{T},E_{T}).$

1. Set $V_{T}=\{V_{G}\},\ E_{T}=\emptyset .$
2. Choose some $X\in V_{T}$ with |*X*| ≥ 2 if such X exists. Otherwise, go to step 6.
3. For each connected component $C=(V_{C},E_{C})\in T\setminus X,$ let ${\textstyle S_{C}=\bigcup _{v_{T}\in V_{C}}v_{T}.}$ Let $S=\{S_{C}\mid C{\text{ is a connected component in }}T\setminus X\}.$ Contract the components to form $G'=((V_{G'},E_{G'}),c'),$ where: ${\begin{aligned}V_{G'}&=X\cup S\\[2pt]E_{G'}&=E_{G}|_{X\times X}\cup \{(u,S_{C})\in X\times S\mid (u,v)\in E_{G}{\text{ for some }}v\in S_{C}\}\\[2pt]&\qquad \qquad \quad \!\cup \{(S_{C1},S_{C2})\in S\times S\mid (u,v)\in E_{G}{\text{ for some }}u\in S_{C1}{\text{ and }}v\in S_{C2}\}\end{aligned}}$ $c':V_{G'}\times V_{G'}\to R^{+}$ is the capacity function, defined as: ${\begin{aligned}&{\text{if }}\ (u,S_{C})\in E_{G}|_{X\times S}:&&c'(u,S_{C})=\!\!\!\sum _{\begin{smallmatrix}v\in S_{C}:\\(u,v)\in E_{G}\end{smallmatrix}}\!\!\!c(u,v)\\[4pt]&{\text{if }}\ (S_{C1},S_{C2})\in E_{G}|_{S\times S}:&&c'(S_{C1},S_{C2})=\!\!\!\!\!\!\!\sum _{\begin{smallmatrix}(u,v)\in E_{G}:\\u\in S_{C1}\,\land \,v\in S_{C2}\end{smallmatrix}}\!\!\!\!\!c(u,v)\\[4pt]&{\text{otherwise}}:&&c'(u,v)=c(u,v)\end{aligned}}$
4. Choose two vertices *s*, *t* ∈ *X* and find a minimum *s*-*t* cut (*A′*, *B′*) in G'. Set $A={\Biggl (}\bigcup _{S_{C}\in A'\cap S}\!\!\!S_{C}\!{\Biggr )}\cup (A'\cap X),\$ $B={\Biggl (}\bigcup _{S_{C}\in B'\cap S}\!\!\!S_{C}\!{\Biggr )}\cup (B'\cap X).$
5. Set $V_{T}=(V_{T}\setminus X)\cup \{A\cap X,B\cap X\}.$ For each $e=(X,Y)\in E_{T}$ do: Set $e'=(A\cap X,Y)$ if $Y\subset A,$ otherwise set $e'=(B\cap X,Y).$ Set $E_{T}=(E_{T}\setminus \{e\})\cup \{e'\}.$ Set $w(e')=w(e).$ Set $E_{T}=E_{T}\cup \{(A\cap X,\ B\cap X)\}.$ Set $w((A\cap X,B\cap X))=c'(A',B').$ Go to step 2.
6. Replace each $\{v\}\in V_{T}$ by v and each $(\{u\},\{v\})\in E_{T}$ by (*u*, *v*). Output T.

## Analysis

Using the submodular property of the capacity function c, one has $c(X)+c(Y)\geq c(X\cap Y)+c(X\cup Y).$ Then it can be shown that the minimum *s*-*t* cut in G' is also a minimum *s*-*t* cut in G for any *s*, *t* ∈ *X*.

To show that for all $(P,Q)\in E_{T},$ $w(P,Q)=\lambda _{pq}$ for some *p* ∈ *P*, *q* ∈ *Q* throughout the algorithm, one makes use of the following lemma,

For any

i, j, k

in

V

G

,

$\lambda _{ik}\geq \min(\lambda _{ij},\lambda _{jk}).$

The lemma can be used again repeatedly to show that the output T satisfies the properties of a Gomory–Hu Tree.

## Example

The following is a simulation of the Gomory–Hu algorithm, where

1. *green* circles are vertices of *T*.
2. *red* and *blue* circles are the vertices in *G*'.
3. *grey* vertices are the chosen *s* and *t*.
4. *red* and *blue* coloring represents the *s*-*t* cut.
5. *dashed* edges are the *s*-*t* cut-set.
6. *A* is the set of vertices circled in *red* and *B* is the set of vertices circled in *blue*.

|   | *G*' | *T* |
|---|---|---|
|   |   |   |
|   | 1. Set *V*T = {*V*G} = { {0, 1, 2, 3, 4, 5} } and *E*T = ∅. 2. Since *V*T has only one vertex, choose *X* = *V*G = {0, 1, 2, 3, 4, 5}. Note that \| *X* \| = 6 ≥ 2. |   |
| 1. |   |   |
|   | 3. Since *T*\*X* = ∅, there is no contraction and therefore *G*' = *G*. 4. Choose *s* = 1 and *t* = 5. The minimum *s*-*t* cut (*A*', *B*') is ({0, 1, 2, 4}, {3, 5}) with *c*'(*A*', *B*') = 6.     Set *A* = {0, 1, 2, 4} and *B* = {3, 5}. 5. Set *V*T = (*V*T\*X*) ∪ {*A* ∩ *X*, *B* ∩ *X*} = { {0, 1, 2, 4}, {3, 5} }.     Set *E*T = { ({0, 1, 2, 4}, {3, 5}) }.     Set *w*( ({0, 1, 2, 4}, {3, 5}) ) = *c*'(*A*', *B*') = 6.     Go to step 2. 2. Choose *X* = {3, 5}. Note that \| *X* \| = 2 ≥ 2. |   |
| 2. |   |   |
|   | 3. {0, 1, 2, 4} is the connected component in *T*\*X* and thus *S* = { {0, 1, 2, 4} }.     Contract {0, 1, 2, 4} to form *G*', where *c*'( (3, {0, 1, 2 ,4}) ) = *c*( (3, 1) ) + *c*( (3, 4) ) = 4. *c*'( (5, {0, 1, 2, 4}) ) = *c*( (5, 4) ) = 2. *c*'( (3, 5)) = *c*( (3, 5) ) = 6. 4. Choose *s* = 3, *t* = 5. The minimum *s*-*t* cut (*A*', *B*') in *G*' is ( {{0, 1, 2, 4}, 3}, {5} ) with *c*'(*A*', *B*') = 8.     Set *A* = {0, 1, 2, 3, 4} and *B* = {5}. 5. Set *V*T = (*V*T\*X*) ∪ {*A* ∩ *X*, *B* ∩ *X*} = { {0, 1, 2, 4}, {3}, {5} }.     Since (*X*, {0, 1, 2, 4}) ∈ *E*T and {0, 1, 2, 4} ⊂ *A*, replace it with (*A* ∩ *X*, *Y*) = ({3}, {0, 1, 2 ,4}).     Set *E*T = { ({3}, {0, 1, 2 ,4}), ({3}, {5}) } with *w*(({3}, {0, 1, 2 ,4})) = *w*((*X*, {0, 1, 2, 4})) = 6. *w*(({3}, {5})) = *c*'(*A*', *B*') = 8.     Go to step 2. 2. Choose *X* = {0, 1, 2, 4}. Note that \| *X* \| = 4 ≥ 2. |   |
| 3. |   |   |
|   | 3. { {3}, {5} } is the connected component in *T*\*X* and thus *S* = { {3, 5} }.     Contract {3, 5} to form *G*', where *c*'( (1, {3, 5}) ) = *c*( (1, 3) ) = 3. *c*'( (4, {3, 5}) ) = *c*( (4, 3) ) + *c*( (4, 5) ) = 3. *c*'(*u*,*v*) = *c*(*u*,*v*) for all *u*,*v* ∈ *X*. 4. Choose *s* = 1, *t* = 2. The minimum *s*-*t* cut (*A*', *B*') in *G*' is ( {1, {3, 5}, 4}, {0, 2} ) with *c*'(*A*', *B*') = 6.     Set *A* = {1, 3, 4, 5} and *B* = {0, 2}. 5. Set *V*T = (*V*T\*X*) ∪ {*A* ∩ *X*, *B* ∩ *X*} = { {3}, {5}, {1, 4}, {0, 2} }.     Since (*X*, {3}) ∈ *E*T and {3} ⊂ *A*, replace it with (*A* ∩ *X*, *Y*) = ({1, 4}, {3}).     Set *E*T = { ({1, 4}, {3}), ({3}, {5}), ({0, 2}, {1, 4}) } with *w*(({1, 4}, {3})) = *w*((*X*, {3})) = 6. *w*(({0, 2}, {1, 4})) = *c*'(*A*', *B*') = 6.     Go to step 2. 2. Choose *X* = {1, 4}. Note that \| *X* \| = 2 ≥ 2. |   |
| 4. |   |   |
|   | 3. { {3}, {5} }, { {0, 2} } are the connected components in *T*\*X* and thus *S* = { {0, 2}, {3, 5} }     Contract {0, 2} and {3, 5} to form *G*', where *c*'( (1, {3, 5}) ) = *c*( (1, 3) ) = 3. *c*'( (4, {3, 5}) ) = *c*( (4, 3) ) + *c*( (4, 5) ) = 3. *c*'( (1, {0, 2}) ) = *c*( (1, 0) ) + *c*( (1, 2) ) = 2. *c*'( (4, {0, 2}) ) = *c*( (4, 2) ) = 4. *c*'(*u*,*v*) = *c*(*u*,*v*) for all *u*,*v* ∈ *X*. 4. Choose *s* = 1, *t* = 4. The minimum *s*-*t* cut (*A*', *B*') in *G*' is ( {1, {3, 5}}, {{0, 2}, 4} ) with *c*'(*A*', *B*') = 7.     Set *A* = {1, 3, 5} and *B* = {0, 2, 4}. 5. Set *V*T = (*V*T\*X*) ∪ {*A* ∩ *X*, *B* ∩ *X*} = { {3}, {5}, {0, 2}, {1}, {4} }.     Since (*X*, {3}) ∈ *E*T and {3} ⊂ *A*, replace it with (*A* ∩ *X*, *Y*) = ({1}, {3}).     Since (*X*, {0, 2}) ∈ *E*T and {0, 2} ⊂ *B*, replace it with (*B* ∩ *X*, *Y*) = ({4}, {0, 2}).     Set *E*T = { ({1}, {3}), ({3}, {5}), ({4}, {0, 2}), ({1}, {4}) } with *w*(({1}, {3})) = *w*((*X*, {3})) = 6. *w*(({4}, {0, 2})) = *w*((*X*, {0, 2})) = 6. *w*(({1}, {4})) = *c*'(*A*', *B*') = 7.     Go to step 2. 2. Choose *X* = {0, 2}. Note that \| *X* \| = 2 ≥ 2. |   |
| 5. |   |   |
|   | 3. { {1}, {3}, {4}, {5} } is the connected component in *T*\*X* and thus *S* = { {1, 3, 4, 5} }.     Contract {1, 3, 4, 5} to form *G*', where *c*'( (0, {1, 3, 4, 5}) ) = *c*( (0, 1) ) = 1. *c*'( (2, {1, 3, 4, 5}) ) = *c*( (2, 1) ) + *c*( (2, 4) ) = 5. *c*'( (0, 2) ) = *c*( (0, 2) ) = 7. 4. Choose *s* = 0, *t* = 2. The minimum *s*-*t* cut (*A*', *B*') in *G*' is ( {0}, {2, {1, 3, 4, 5}} ) with *c*'(*A*', *B*') = 8.     Set *A* = {0} and *B* = {1, 2, 3 ,4 ,5}. 5. Set *V*T = (*V*T\*X*) ∪ {*A* ∩ *X*, *B* ∩ *X*} = { {3}, {5}, {1}, {4}, {0}, {2} }.     Since (*X*, {4}) ∈ *E*T and {4} ⊂ *B*, replace it with (*B* ∩ *X*, *Y*) = ({2}, {4}).     Set *E*T = { ({1}, {3}), ({3}, {5}), ({2}, {4}), ({1}, {4}), ({0}, {2}) } with *w*(({2}, {4})) = *w*((*X*, {4})) = 6. *w*(({0}, {2})) = *c*'(*A*', *B*') = 8.     Go to step 2. 2. There does not exist *X*∈*V*T with \| *X* \| ≥ 2. Hence, go to step 6. |   |
| 6. |   |   |
|   | 6. Replace *V*T = { {3}, {5}, {1}, {4}, {0}, {2} } by {3, 5, 1, 4, 0, 2}.     Replace *E*T = { ({1}, {3}), ({3}, {5}), ({2}, {4}), ({1}, {4}), ({0}, {2}) } by { (1, 3), (3, 5), (2, 4), (1, 4), (0, 2) }.     Output *T*. Note that exactly \| *V* \| − 1 = 6 − 1 = 5 times min-cut computation is performed. |   |

## Implementations: Sequential and Parallel

Gusfield's algorithm can be used to find a Gomory–Hu tree without any vertex contraction in the same running time-complexity, which simplifies the implementation of constructing a Gomory–Hu Tree.

Andrew V. Goldberg and K. Tsioutsiouliklis implemented the Gomory-Hu algorithm and Gusfield algorithm, and performed an experimental evaluation and comparison.

Cohen et al. report results on two parallel implementations of Gusfield's algorithm using OpenMP and MPI, respectively.

In planar graphs, the Gomory–Hu tree is dual to the minimum weight cycle basis, in the sense that the cuts of the Gomory–Hu tree are dual to a collection of cycles in the dual graph that form a minimum-weight cycle basis.
